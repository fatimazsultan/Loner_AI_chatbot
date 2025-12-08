# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from lonerai import generate_response  # your chatbot function

app = FastAPI(title="LonerAI Chatbot API")

# Input JSON model
class ChatRequest(BaseModel):
    message: str

# API endpoint
@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    user_message = request.message
    response = generate_response(user_message)
    return {"response": response}

# Run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
