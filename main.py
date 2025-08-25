import faiss
import numpy as np
import httpx
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db import engine, Base, get_db
from models import User, Message
from schemas import UserCreate, UserLogin, Token, ChatRequest, ChatResponse
from auth import (
    get_password_hash, verify_password, create_access_token,
    get_current_user
)

app = FastAPI(debug=True)

# ------------------ FAISS Setup ------------------
dim = 1536
faiss_index = faiss.IndexFlatL2(dim)
corpus = ["Python is a programming language.", "FastAPI is used to build APIs.", "SQLAlchemy is an ORM."]
np.random.seed(42)
embeddings = np.random.random((len(corpus), dim)).astype("float32")
faiss_index.add(embeddings)

PERPLEXITY_API_KEY = "pplx-w4C1jRQXE859AoIC09t5XrZjgwDrojFKwbFfQnS22QS39D"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

async def call_perplexity_api(query: str, context: str) -> str:
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
    }
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": f"Use this context to answer: {context}"},
            {"role": "user", "content": query}
        ]
    }
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:  # <-- increase timeout
            response = await client.post(PERPLEXITY_URL, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
    except httpx.RequestError as e:
        # network issue
        return f"Error contacting Perplexity API: {str(e)}"
    except httpx.HTTPStatusError as e:
        # non-200 response
        return f"Perplexity API returned error {e.response.status_code}"
    except KeyError:
        return "Unexpected response format from Perplexity API"

# ------------------ Routes ------------------
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    db_user = User(
        username=user.username,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return {"detail": f"User {user.username} created successfully"}

@app.post("/login", response_model=Token)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalars().first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(db_user.id)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    query_embedding = np.random.random((1, dim)).astype("float32")
    _, indices = faiss_index.search(query_embedding, k=1)
    context = corpus[indices[0][0]]

    answer = await call_perplexity_api(req.query, context)

    new_message = Message(user_id=current_user.id, content=req.query, response=answer)
    db.add(new_message)
    await db.commit()

    return ChatResponse(answer=answer)
