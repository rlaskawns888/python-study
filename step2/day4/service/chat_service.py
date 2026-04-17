from step2.day4.schema.chat_schema import ChatRequest, ChatResponse

def generate_chat_answer(request: ChatRequest) -> ChatResponse:
    if not request.message.strip():
        raise ValueError("message 공백 X ")
    
    answer_text = f"{request.user_name}님, 질문을 잘 받았습니다. 입력하신 내용은 '{request.message}' 입니다."

    return ChatResponse(
        answer=answer_text
        , status="success"
        , user_name=request.user_name
    )

