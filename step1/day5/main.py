from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import json

app = FastAPI()

@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):

    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="only .txt")


    base_dir = Path(__file__).parent
    output_dir  = base_dir / "data" / "result"
    output_dir.mkdir(exist_ok=True)


    content = await file.read()

    try:
        text = content.decode("utf-8")
        if not text.strip():
            raise HTTPException(status_code=400, detail="빈 파일입니다.")

    except UnicodeDecodeError:
        try:
            text = content.decode("cp949")
            if not text.strip():
                raise HTTPException(status_code=400, detail="빈 파일입니다.")
        except UnicodeDecodeError:
            raise HTTPException(status_code=400, detail="지원하지 않는 인코딩입니다.")
        


    lines = text.splitlines()
    sentences = [line.strip() for line in lines if line.strip()]

    longest_sentence = max(sentences, key=len) if sentences else ""
    print(f"가장 긴 문장: {longest_sentence}")

    sentence_data = []
    for i, sentence in enumerate(sentences, start=1):
        sentence_data.append({
            "index": i,
            "text": sentence,
            "length": len(sentence),
            "word_count": len(sentence.split()),
            "long_word": longest_sentence            
        })

    result = {
        "file_name": file.filename,
        "summary": {
            "line_count": len(lines),
            "sentence_count": len(sentences),
            "word_count": len(text.split()),
            "char_count": len(text)
        },
        "sentences": sentence_data
    }

    # output_file = output_dir / f"{file.stem}.json"
    output_path = output_dir / f"{Path(file.filename).stem}.json"


    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


    return result

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

