import requests
from pprint import pprint

def say():
    print("Freedom is everything.")
    
def ip_details():
    r = requests.get("https://httpbin.org/get")
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Not 200")

def main():
    "This is our entry point"
    pprint(ip_details())

if __name__ == '__main__':
    main()
