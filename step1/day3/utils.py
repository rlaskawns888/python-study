def validate_input(text):
    if text == "":
        raise ValueError("입력값이 비어 있습니다")
    return text


def preprocess(txt):
    return txt.strip().lower()