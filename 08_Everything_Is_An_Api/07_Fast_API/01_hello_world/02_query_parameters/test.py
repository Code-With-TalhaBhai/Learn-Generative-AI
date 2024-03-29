import requests


data = {
    'filter': 64
}

res = requests.get('http://127.0.0.1:8000/profile',params=data)

print(res.json())