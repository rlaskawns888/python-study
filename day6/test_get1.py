import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)

# print(response.status_code)

# if response.status_code == 200:
#     data = response.json()

#     print(data["name"])
#     print(data["email"])
#     print(data["address"]["city"])


# payload = {
#     "postId": 1
# }

# response = httpx.get("https://jsonplaceholder.typicode.com/comments", params=payload, timeout=5)
# response.raise_for_status()


# if response.status_code == 200:
#     data = response.json()

#     print(len(data))
#     print(data[0]["email"])


payload = {
    "title": "title test"
    , "body": "bodytest"
    , "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=5)
response.raise_for_status()

print(response.status_code)


try:
    if response.status_code in(200, 201):
        data = response.json()

        print(response.status_code)
        print(data["id"])

except httpx.TimeoutException:
    print("TIME OUT")

except httpx.HTTPStatusError as e:
    print(e.response.status_code)
    print(e.response.text)

except httpx.RequestError as e:
    print(str(e))
    



    
