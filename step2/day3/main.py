from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class ChatRequest(BaseModel): 
    message: str = Field(..., min_length=1, max_length=10)

class ChatResponse(BaseModel):
    answer: str
    status: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException (status_code=400, detail="message 비어 있음")
    
    if len(request.message) > 500:
        raise HTTPException (status_code=400, detail="message 길이가 너무 김")
    
    try:
        if request.message == "fail":
            raise RuntimeError("외부 API 실패")

        answer = f"응답: {request.message}"

        return ChatResponse (
            answer=answer
            , status="success"
        )

    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))
    
    except Exception as e:
        # 알 수 없는 에러
        raise HTTPException(status_code=500, detail="서버 내부 오류")






