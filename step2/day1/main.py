from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    user_name: str = Field(..., min_length=1, max_length=50)
    max_tokens: int = Field(10, ge=1, le=2000)

class ChatResponse(BaseModel):
    answer: str
    status: str
    max_tokens: int


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer_msg = f"{request.user_name}님, 질문을 잘 받았습니다."

    return ChatResponse(
        answer=answer_msg
        , status="success"
        , max_tokens=request.max_tokens
    )