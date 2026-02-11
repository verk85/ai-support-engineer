from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings

app = FastAPI(title="settings.PROJECT_NAME")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Support Engineer API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "answer": "Hello World!",
        "echo": req.message
    }
