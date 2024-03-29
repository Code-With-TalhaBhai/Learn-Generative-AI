import requests


res = requests.get('http://127.0.0.1:8000/talha/pk/bhai')


print(res.json())