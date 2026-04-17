from fastapi import FastAPI

from step2.day6.core.exceptions import register_exception_handlers
from step2.day6.routers.summarize import router as summarize_router

app = FastAPI(title="SIMPLE SUMMARIZE API")

register_exception_handlers(app)

app.include_router(summarize_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}