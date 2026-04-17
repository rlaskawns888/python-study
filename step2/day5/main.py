from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-test")
async def async_test():
    await asyncio.sleep(10)
    return {"message":"done"}