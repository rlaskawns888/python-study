import json
import csv
from pathlib import Path

# with open("data.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# print(text)

# data = {
#     "name": "NJ"
#     , "age": 30
# }

# with open("result.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# with open("data.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

# path = Path("data.txt")
# print(path.exists())
# print(path.name)

with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()

    words = data.split()
    unique_words = list(set(words))
    print(words)
    print(unique_words)

    result = {
        "total_words": len(words)
        , "unique_words": len(unique_words)
        , "words": words
    }

    print(result)

    # total_word = len(data)
    # unique_words = (total_word)

    # for i in range(len(unique_words)):
    #     print(i)
