def getRes(txt):
    return f"AI RESP: {txt}"

def validate_ipt(txt):
    if txt == "":
        raise ValueError("ENPTY......")
    return txt

def service(txt):
    try:
        valid_txt = validate_ipt(txt)
        res = getRes(valid_txt)
        return res
    except ValueError as e:
        return f"NO INPUT: {e}"
    

print(service("파이썬 공부"))
print(service(""))