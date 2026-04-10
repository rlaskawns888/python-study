import requests

url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # 4xx, 5xx 면 예외 발생

    data = response.json()
    print("name:", data["name"])
    print("email:", data["email"])

except requests.exceptions.Timeout:
    print("TIME oUT")

except requests.exceptions.HTTPError as e:
    print("HTTP ERROR")
    print(e.response.status_code)
    print(e.response.text)

except requests.exceptions.RequestException as e:
    print("error: ", str(e))