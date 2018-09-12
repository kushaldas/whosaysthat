import requests

def say():
    print("Freedom is everything.")
    
def ip_details():
    r = requests.get("https://httpbin.org/get")
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Not 200")