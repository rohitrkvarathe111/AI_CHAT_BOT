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

### POST /login: Login and get JWT token

### POST /chat: Send a query and get AI response (requires authentication)


