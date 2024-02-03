import requests
import json

url = "http://localhost:8191/v1"


headers = {"Content-Type": "application/json",}

data = {
    "cmd": "request.get",
    "url": "https://www.subber.xyz/notsgtpepe/giveaways/not-sgt-pepe",
    "maxTimeout": 60000,
    "cookies": [{"name": "token", "value": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJkZGIzODNhOC02MTk1LTRkYjMtOTdkMi0xNGU3MzE1NzdmOWEiLCJleHAiOjE3MTQ3NDkyMDd9.ZXYwdGUygTNAa76Rk6rt_fu8XOsdqDifwyBF-SG5IeA"}],
        "proxy": {
            "url": "http://193.150.188.60:5595",
        "username": "user152203",
        "password": "iu1e8o"
    },
}
response = requests.post(url, headers=headers, json=data)

print(json.loads(response.text))