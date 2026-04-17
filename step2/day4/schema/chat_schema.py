from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="message..")
    user_name: str = Field(..., min_length=1, max_length=50, description="name..")
    max_toekns: int = Field(100, ge=1, le=2000, description="maxtoken..")

class ChatResponse(BaseModel):
    answer: str
    status: str
    user_name: str