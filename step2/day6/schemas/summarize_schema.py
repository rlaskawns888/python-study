from pydantic import BaseModel, Field

class SummarizedRequest(BaseModel):
    text: str = Field(
        ...
        , min_length=1
        , max_length=5000
        , description="요약 원문 텍스트"
    )

class SummarizedResponse(BaseModel):
    summary: str = Field(..., description="요약 결과")