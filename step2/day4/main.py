from fastapi import FastAPI
from step2.day4.api.chat import router as chat_router
from step2.day4.api.summarize_router import router as summarize_router
from step2.day4.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug
)

app.include_router(chat_router)
app.include_router(summarize_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}