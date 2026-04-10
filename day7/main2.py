import json
from pathlib import Path

# input_path = "input/sample.txt"
input_path = "input"
output_path = "output/result.json"

# 여러 txt 파일 처리 (for loop)
# 단어 TOP 5 추출
# 실행 시간 측정 추가

def read_file(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"NOT FOUD FILE: {file_path}")

    if not path.is_file:
        raise ValueError(f"파일 경로가 아닙니다: {file_path}")

    read_data = []
    files = list(path.glob("*.txt"))
    for fp in files:
        try:
            read_path = Path(fp)
            read_text = read_path.read_text(encoding="utf-8")

            processed_text = preprocess_text(read_text)

            read_data.append(processed_text)

        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(
                e.encoding, e.object, e.start, e.encoding
                , f"파일 인코딩을 읽을 수 없습니다: {file_path}"
            )

    return read_data





def preprocess_text(text: str) -> str:
    lines = text.splitlines()
    print(lines)

    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            normalized = " ".join(stripped.split())
            cleaned_lines.append(normalized)

    return "\n".join(cleaned_lines)

def build_analysis_result(file_name: str, original_text: str, processed_text: str) -> dict:
    return {
        "file_name": file_name,
        "original_char_count": count_characters(original_text),
        "processed_char_count": count_characters(processed_text),
        "line_count": count_lines(processed_text),
        "word_count": count_words(processed_text),
        "processed_text": processed_text
    }

def count_characters(text: str) -> int:
    return len(text)

def count_lines(text: str) -> int:
    if not text: 
        return 0
    return len(text.splitlines())

def count_words(text: str) -> int:
    if not text.strip():
        return 0
    return len(text.split())

def save_to_json(data: dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


original_text  = read_file(input_path)
print(original_text)
# processed_text = preprocess_text(original_text)

# result = build_analysis_result(
#     file_name=Path(input_path).name
#     , original_text=original_text
#     , processed_text=processed_text
# )

# save_to_json(result, output_path)


# 글자 수
# 줄 수
# 단어 수