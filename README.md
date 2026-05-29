# IntuCate Assessment Backend

A FastAPI-based backend for an AI-powered educational assessment platform. This service handles chat interactions, manages conversation history, and integrates with the Groq API for AI responses.

## Features

- **FastAPI Framework**: High-performance, easy-to-learn, fast-to-code, production-ready.
- **MongoDB Integration**: Asynchronous MongoDB driver for efficient data storage and retrieval.
- **Groq API Integration**: Utilizes Groq's Llama 3.3 model for fast and intelligent AI responses.
- **Chat Endpoints**:
  - Single chat input with prompt engineering.
  - Bulk chat processing with parallel execution.
- **Prompt Management**: Dynamic prompt templates stored in MongoDB.
- **Conversation History**: Automatic logging of all chat interactions.

## Prerequisites

- Python 3.8+
- MongoDB instance
- Groq API Key

## Installation

1.  **Clone the repository** (if not already done).

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration**:
    Create a `.env` file in the `Backend` directory with the following variables:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    MONGO_URI=mongodb://localhost:27017
    DATABASE_NAME=intucate_db
    ```

## Project Structure

```
Backend/
├── app/
│   ├── config/       # Configuration settings
│   │   └── settings.py
│   ├── db/           # Database connections and models
│   │   └── database.py
│   ├── routes/       # API endpoints
│   │   └── chat.py
│   ├── services/     # Business logic
│   │   ├── ai_service.py
│   │   └── prompt_service.py
│   ├── models/       # Pydantic schemas
│   │   └── schemas.py
│   └── main.py       # FastAPI application entry point
├── .env              # Environment variables (not in git)
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## Usage

### Running the Server

Start the development server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`.

### API Endpoints

#### 1. Health Check

**GET** `/`

Checks if the database connection is working.

**Response:**
```json
{
    "message": "Database connected"
}
```

#### 2. Single Chat

**POST** `/chat`

Sends a single user input to the AI model.

**Request Body:**
```json
{
    "userInput": "What is a Chartered Accountant?"
}
```

**Response:**
```json
{
    "response": "A Chartered Accountant (CA) is a professional who is qualified to handle accounting, auditing, and taxation for individuals and businesses."
}
```

#### 3. Bulk Chat

**POST** `/bulk-chat`

Processes multiple chat inputs in parallel.

**Request Body:**
```json
{
    "inputs": [
        "How should I prepare for CA final?",
        "Best study strategy?",
        "How many mock tests should I solve?"
    ]
}
```

**Response:**
```json
{
    "responses": [
        {
            "response": "Preparing for CA Final requires a disciplined schedule, focused study on all subjects, and multiple revisions of the ICAI study material."
        },
        {
            "response": "The best strategy involves completing the syllabus early, making concise notes for last-day revisions, and practicing past papers."
        },
        {
            "response": "It is generally recommended to solve at least 2-3 full-length mock tests per subject to improve time management and identify weak areas."
        }
    ]
}
```

## Database Setup

Before running the application, ensure you have a MongoDB database running. The application will automatically create the `intucate_assessment` database and the `prompts` and `history` collections if they don't exist.

### Initial Prompt Configuration

The `prompts` collection should contain at least one document for the prompt template. Here's an example of the initial data to insert:

```json
{
    "_id": "Education_Prompt",
    "template": "You are an expert educator. Answer the following question clearly and concisely:\n\n{userInput}"
}
```
