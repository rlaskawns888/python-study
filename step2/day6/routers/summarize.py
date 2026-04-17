from fastapi import APIRouter

from step2.day6.schemas.summarize_schema import SummarizedRequest, SummarizedResponse
from step2.day6.services.summarize_service import summarize_text

router = APIRouter(prefix="/summarize", tags=["Summarize"])

@router.post("", response_model=SummarizedResponse)
def summarize(request: SummarizedRequest):
    summary_reult = summarize_text(request.text)
    
    return SummarizedResponse(summary=summary_reult)