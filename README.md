# IntuCate Assessment - AI Chatbot (Full Stack)

An AI-powered educational assessment platform built with FastAPI (Backend) and React/Vite (Frontend). This service handles chat interactions, manages conversation history, and integrates with the Groq API for fast, intelligent responses.

## Live Demo

- **Frontend**: [intucate-case-study.vercel.app](https://intucate-case-study.vercel.app)
- **Backend**: [https://intucate-casestudy.onrender.com](https://intucate-casestudy.onrender.com)

## Features

- **FastAPI Backend**: High-performance, production-ready REST API.
- **React Frontend**: Modern, responsive UI built with Vite.
- **Groq API Integration**: Utilizes Groq's Llama 3.3 model for intelligent educational responses.
- **MongoDB Integration**: Efficient storage for conversation history and dynamic prompts.
- **Chat Capabilities**:
  - Single chat with prompt engineering.
  - Bulk chat processing (parallel execution).
- **History Tracking**: Automatic logging of all interactions.

## Project Structure

```
IntuCate assessment/
├── Backend/
│   ├── app/
│   │   ├── routes/       # API endpoints
│   │   ├── services/     # Business logic (AI, Prompts)
│   │   ├── models/       # Pydantic schemas
│   │   └── db/           # MongoDB configuration
│   ├── requirements.txt
│   └── .env              # Backend configuration
├── Frontend/
│   └── frontend/
│       ├── src/          # React components and logic
│       ├── index.html
│       ├── package.json
│       └── .env          # Frontend configuration
└── README.md
```

## Setup and Installation

### 1. Backend Setup

1.  **Navigate to Backend directory**:
    ```bash
    cd Backend
    ```

2.  **Create and activate virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    Create a `.env` file in the `Backend` directory:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    MONGO_URI=mongodb://localhost:27017
    DATABASE_NAME=intucate_db
    ```

5.  **Run Backend**:
    ```bash
    uvicorn app.main:app --reload
    ```

### 2. Frontend Setup

1.  **Navigate to Frontend directory**:
    ```bash
    cd Frontend/frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Environment Variables**:
    Create a `.env` file in `Frontend/frontend`:
    ```env
    VITE_API_URL=http://localhost:8000
    ```

4.  **Run Frontend**:
    ```bash
    npm run dev
    ```

## API Usage

### Single Chat
**POST** `/chat`
Input: `"What is a Chartered Accountant?"`

### Bulk Chat
**POST** `/bulk-chat`
Input: `["How should I prepare for CA final?", "Best study strategy?"]`

## Database Configuration

The application uses MongoDB for storing prompts and conversation history. On startup, it automatically ensures the required collections exist.

### Prompt Template
Default template stored in `prompts` collection:
```json
{
    "_id": "Education_Prompt",
    "template": "You are an expert educator. Answer the following question clearly and concisely:\n\n{userInput}"
}
```
