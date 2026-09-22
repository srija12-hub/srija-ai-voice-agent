# api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import ask_agent


# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="Srija AI - Developer Voice Agent",
    description="AI interview assistant based on Srija's professional profile",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://srija-ai-voice-agent.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODEL
# ============================================================

class QuestionRequest(BaseModel):
    question: str


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Srija AI Backend is running",
        "status": "online"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "agent": "Srija AI"
    }


# ============================================================
# ASK AI
# ============================================================

@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    # --------------------------------------------------------
    # Empty question
    # --------------------------------------------------------

    if not question:

        return {
            "success": False,
            "answer": "Please ask me a question about Srija."
        }

    # --------------------------------------------------------
    # Ask Agent
    # --------------------------------------------------------

    try:

        answer = ask_agent(question)

        return {
            "success": True,
            "question": question,
            "answer": answer
        }

    except Exception as error:

        print(f"API Error: {error}")

        return {
            "success": False,
            "question": question,
            "answer": (
                "Sorry, I couldn't process that question."
            )
        }


# ============================================================
# SERVER TEST
# ============================================================

@app.get("/test")
def test():

    return {
        "message": "Srija AI API is working correctly."
    }