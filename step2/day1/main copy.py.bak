from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="사용자 질문")
    user_name: str = Field(..., min_length=1, max_length=50, description="사용자 이름")
    model: str = Field(default="gpt-4.1-mini", min_length=1, description="사용할 모델명")
    max_tokens: int = Field(default=256, ge=1, le=2048, description="최대 토큰 수")

class ChatResponse(BaseModel):
    answer: str
    model: str
    status: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # return {"message": "POST API CREATED"}

    # return {
    #     "received_message": request.message
    #     , "received_user": request.user_name
    # }

    answer = f"[mock answer] {request.user_name}님의 질문 '{request.message}'에 대한 응답입니다."
    
    return ChatResponse(
        answer=answer,
        model=request.model,
        status="success"
    )




