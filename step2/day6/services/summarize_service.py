import re
from step2.day6.core.exceptions import SummarizeException

def summarize_text(text: str) -> str:
    cleaned_text = text.strip()

    if not cleaned_text:
        raise SummarizeException("text에는 공백이 아닌 실제 내용이 들어와야 합니다.")
    
    # 문장 단위로 단순 분리
    sentences = re.split(r'(?<=[.!?])\s+', cleaned_text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if not sentences:
        raise SummarizeException("요약할 수 있는 문장을 찾지 못했습니다.")

    # 간단 요약 로직:
    # 1) 문장이 2개 이상이면 앞의 2문장 사용
    # 2) 문장이 1개면 그 문장 사용
    summary_sentences = sentences[:2]
    summary = " ".join(summary_sentences)

    # 혹시 너무 길면 잘라주기
    max_summary_length = 300
    if len(summary) > max_summary_length:
        summary = summary[:max_summary_length].rstrip() + "..."

    return summary