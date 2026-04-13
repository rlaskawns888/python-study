from pathlib import Path
import json 

base_dir = Path(__file__).parent
input_dir = base_dir / "data" / "input"
output_dir  = base_dir / "data" / "output"

output_dir.mkdir(exist_ok=True)

txt_files = list(input_dir.glob("*.txt"))

for file_path in txt_files:
    print(f"처리중: {file_path.name}")

    with open (file_path, "r", encoding="utf-8") as f:
        text = f.read()


    lines = text.splitlines()
    sentences = [line.strip() for line in lines if line.strip()]


    sentence_data = []
    for i, sentence in enumerate(sentences, start=1):
        item = {
            "index": i,
            "text": sentence,
            "length": len(sentence),
            "word_count": len(sentence.split())
        }
        sentence_data.append(item)


    result = {
        "summary": {
            "line_count": len(lines),
            "sentence_count": len(sentences),
            "word_count": len(text.split())
        },
        "sentences": sentence_data
    }

    output_file = output_dir / f"{file_path.stem}.json"

    # 7. JSON 저장
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

print("저장 완료")
                    