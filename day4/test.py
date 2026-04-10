from dataclasses import dataclass

# class ChatReq:
#     def __init__(self, msg):
#         self.message = msg

# req = ChatReq("Hello World")
# print(req.message)

@dataclass
class ChatReq:
    message: str
    count: int
    trueAndFalse: bool = True


req = ChatReq("Hello World", 10)
print(req.message)
print(req)

@dataclass
class SummaryRequest:
    text: str
    maxLen: int = 100

def summarize(req: SummaryRequest) -> str:
    return f"{req.text[:req.maxLen]}"

def service(req: SummaryRequest):
    return {
        "result": req.text[:req.maxLen]
    }

req2 = SummaryRequest("THIS IS LONG TEXT", 5)
print(summarize(req2))
print(service(req2))

