import httpx

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = httpx.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    print(data["name"])
    print(data["email"])

except httpx.TimeoutException:
    print("TIMTOUT")

except httpx.HTTPStatusError as e:
    print(e.response.status_code)
    print(e.response.text)

except httpx.RequestError as e:
    print("요청 실패:", str(e))