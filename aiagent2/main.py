from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


def fake_ai_response(user_msg: str):
    user_msg = user_msg.lower()

    if "hello" in user_msg or "hi" in user_msg:
        return "Hey! 👋 I'm your AI assistant. How can I help you?"

    elif "how are you" in user_msg:
        return "I'm just code, but I'm running perfectly 😄 What about you?"

    elif "name" in user_msg:
        return "I'm your custom AI chatbot built with FastAPI 🚀"

    elif "ai" in user_msg:
        return "AI stands for Artificial Intelligence. You're actually building one right now 🔥"

    elif "study" in user_msg:
        return "Focus on consistency. 2 hours daily beats 10 hours once a week."

    else:
        responses = [
            "That's interesting. Tell me more.",
            "I see 👀 Can you explain further?",
            "Hmm… I'm thinking about that 🤔",
            "Nice question! I'm still learning too.",
        ]
        return random.choice(responses)

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = fake_ai_response(req.message)
    return {"reply": reply}