results = [
    {"title": "문서1", "score": 0.95},
    {"title": "문서2", "score": 0.82},
    {"title": "문서3", "score": 0.65}
]

for rs in results:    
    if rs["score"] >= 0.8:
        print(rs["title"])

    
q = "RAG ? "
prompt = f"NEXT QUESTION: {q}"
print(prompt)