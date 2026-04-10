from fastapi import FastAPI
from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict, StrictInt

app = FastAPI()

@dataclass
class SummaryRequest(BaseModel):
    # model_config = ConfigDict(strict=True)

    text: str
    max_length: StrictInt

@dataclass
class ChatRequest:
    message: str
    user_id: str 

@app.post("/summarize")
def summarize(req: SummaryRequest) -> dict:
    return {
        "result": req.text[:req.max_length]
    }

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "response": f"{req.message}: {req.user_id}"
    }