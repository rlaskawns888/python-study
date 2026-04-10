import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()

    print("1`: ", data["name"])
    print("2: ", data["email"])
    print("3: ", data["address"]["city"])
else:
    prnt("fail: ", response.text)