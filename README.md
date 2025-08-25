# FastAPI FAISS Chat App

FastAPI chat application with FAISS-based context retrieval, async SQLAlchemy ORM, and Perplexity API integration.

## Features

- **Chat Endpoint**: `/chat` endpoint accepts user queries and returns AI-generated responses.
- **FAISS Vector Search**: Retrieves the most relevant context from a predefined corpus.
- **Perplexity API Integration**: Generates answers using AI with retrieved context.
- **User Authentication**: Register and login with JWT-based authentication.
- **Async SQLAlchemy ORM**: Stores users and chat messages in a database asynchronously.

## Tech Stack

- FastAPI
- SQLAlchemy (async)
- FAISS (vector search)
- Perplexity AI API
- SQLite (any SQL database)

## Installation

1. Clone the repository:
```bash
https://github.com/rohitrkvarathe111/AI_CHAT_BOT
cd AI_CHAT_BOT
```

## Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

```




## Install dependencies:
```bash
pip install -r requirements.txt
```


## Set your Perplexity API key in main.py or replace in code:
## Run the application:
```bash
uvicorn main:app --reload
```




## API Endpoints

### POST /register: Create a new user
```bash
curl --location 'http://localhost:8000/login' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=H8tnAyl2RxRe1aTnhpYjmS8RuGa0h2F2hTpU9XPaSh1gp1lPAE0b1F1OoTv2pcMe' \
--data '{
  "username": "rohit",
  "password": "rohit"
}'

```

### POST /login: Login and get JWT token
```bash
curl --location 'http://localhost:8000/login' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=H8tnAyl2RxRe1aTnhpYjmS8RuGa0h2F2hTpU9XPaSh1gp1lPAE0b1F1OoTv2pcMe' \
--data '{
  "username": "rohit",
  "password": "rohit"
}'
```

### POST /chat: Send a query and get AI response (requires authentication)
```bash
curl --location 'http://127.0.0.1:8000/chat' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzU2MTQ4MDcxfQ.nfudIGvZQmUMyRhEhf48EwT2BA2QZ6WdJubHY_hUtRs' \
--data '{"query":"What is Python?","variables":{}}'
```


