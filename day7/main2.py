import json
import time
from pathlib import Path
from collections import Counter

# 여러 txt 파일 처리 (for loop)
# 단어 TOP 5 추출
# 실행 시간 측정 추가

input_path = "input"
output_path = "output/result.json"

def read_files(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"NOT FOUD FILE: {file_path}")

    if not path.is_dir:
        raise ValueError(f"파일 경로가 아닙니다: {file_path}")

    read_data = []
    files = list(path.glob("*.txt"))

    if not files:
        raise FileNotFoundError(f"txt 파일이 없습니다: {file_path}")

    for fp in files:
        try:
            original_text = fp.read_text(encoding="utf-8")
            processed_text = preprocess_text(original_text)
            top_words = get_top_words(processed_text)

            read_data.append(
                build_analysis_result(
                    file_name=fp.name
                    , original_text=original_text
                    , processed_text=processed_text
                    , top_words=top_words
                )
            )

        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(
                e.encoding, e.object, e.start, e.encoding
                , f"파일 인코딩을 읽을 수 없습니다: {file_path}"
            )

    return read_data

def preprocess_text(text: str) -> str:
    lines = text.splitlines()

    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            normalized = " ".join(stripped.split())
            cleaned_lines.append(normalized)

    return "\n".join(cleaned_lines)

def get_top_words(text: str, top_n: int = 5):
    words = text.lower().split()
    counter = Counter(words)
    return counter.most_common(top_n)

def build_analysis_result(file_name: str, original_text: str, processed_text: str, top_words: list) -> dict:
    return {
        "file_name": file_name,
        "original_char_count": count_characters(original_text),
        "processed_char_count": count_characters(processed_text),
        "line_count": count_lines(processed_text),
        "word_count": count_words(processed_text),
        "top_5_words": top_words,
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


start = time.time()

results = read_files(input_path)
print(results)

save_to_json(results, output_path)

end = time.time()

print("총실행시간:", end - start)


