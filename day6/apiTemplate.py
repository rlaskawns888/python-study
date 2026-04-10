import httpx 

def get_user(user_id):     
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = httpx.get(url, timeout=5)
        response.raise_for_status()

        print("RESPONSE CODE: ", response.status_code)

        data = response.json()
        print("RESPONSE: ", data)

        return data
    
    except httpx.TimeoutException:
        raise RuntimeError("timeout")

    except httpx.RequestError as e:
        raise RuntimeError(str(e))
        

def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        payload = {
            "title": title
            , "body": body
            , "userId": user_id
        }
        
        response = httpx.post(url, json=payload, timeout=5)
        response.raise_for_status()

        print("RESPONSE CODE: ", response.status_code)

        data = response.json()
        print("RESPONSE: ", data)

        return data
    
    except httpx.TimeoutException:
        raise RuntimeError("timeout")

    except httpx.RequestError as e:
        raise RuntimeError(str(e))