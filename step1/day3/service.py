from step1.day3.utils import validate_input, preprocess
from step1.day3.llm import call_llm

def postprocess(result):
    return result + "[END]"


def service(text):
    try:
        validated_text = validate_input(text)
        preprocessed_text = preprocess(validated_text)
        result = call_llm(preprocessed_text)

        if result == "":
            raise ValueError("AI 응답이 비어 있습니다")
        
        final_result = postprocess(result)

        return {
            "status": "success",
            "message": "정상 처리되었습니다",
            "data": final_result
        }

    except ValueError as e:
        return {
            "status": "error",
            "message": f"값 오류: {e}"
        }

    except TimeoutError as e:
        return {
            "status": "error",
            "message": f"시간 초과 오류: {e}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"서버 오류: {e}"
        }