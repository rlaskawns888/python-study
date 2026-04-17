from fastapi import APIRouter, HTTPException
from step2.day4.schema.chat_schema import ChatRequest, ChatResponse
from step2.day4.service.chat_service import generate_chat_answer

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        return generate_chat_answer(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/test", response_model=ChatResponse)
def chatTest(request: ChatRequest):
    try:
        return generate_chat_answer(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))