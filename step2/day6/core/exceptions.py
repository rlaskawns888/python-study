from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class SummarizeException(Exception):
    def __init__(self, message:str):
        self.message = message

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(SummarizeException)
    async def summarize_exception_handler(
        request: Request
        , exc: SummarizeException
    ):
        return JSONResponse(
            status_code=400
            , content={
                "detail": exc.message
                , "error_type": "SUMMARIZE_ERROR"
            }
        )
