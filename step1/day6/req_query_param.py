import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {
    "postId": 1
}

response = requests.get(url, params=params, timeout=5)
print("URL: ", response.url)
print("CODE: ", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("LEN: ", len(data))
    print("FIRST EMAI: ", data[0]["email"])