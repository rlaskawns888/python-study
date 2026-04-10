import requests

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Content-Type": "application/json"
    , "Accept": "application/json"
}

payload = {
    "title": "AI Service",
    "body": "Learning Python HTTP API",
    "userId": 99
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=5
)

print("status_code:", response.status_code)

if response.status_code in (200, 201):
    data = response.json()
    print("생성된 id:", data["id"])
    print("title:", data["title"])
else:
    print("요청 실패:", response.text)