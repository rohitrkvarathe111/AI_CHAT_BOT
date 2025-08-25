from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

class MessageOut(BaseModel):
    id: int
    content: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True
