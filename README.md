# FastAPI FAISS Chat App

FastAPI chat application with FAISS-based context retrieval, async SQLAlchemy ORM, and Perplexity API integration.

## Features

- **Chat Endpoint**: `/chat` endpoint accepts user queries and returns AI-generated responses.
- **FAISS Vector Search**: Retrieves the most relevant context from a predefined corpus.
- **Perplexity API Integration**: Generates answers using AI with retrieved context.
- **User Authentication**: Register and login with JWT-based authentication.
- **Async SQLAlchemy ORM**: Stores users and chat messages in a database asynchronously.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/fastapi-faiss-chat.git
cd fastapi-faiss-chat
