from fastapi import APIRouter

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("")
def summerize():
    return {"message":"요약 API"}