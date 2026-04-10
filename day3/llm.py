def call_llm(txt):
    if txt == "timeout":
        raise TimeoutError("TIMEOUT ERROR")
    elif txt == "empty":
        return ""
    elif txt == "server":
        raise Exception("SERVER ERROR")
    
    return f"AI RESP: {txt}"