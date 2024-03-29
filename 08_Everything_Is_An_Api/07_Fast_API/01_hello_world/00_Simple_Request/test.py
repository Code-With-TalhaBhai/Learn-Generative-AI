import requests


res = requests.get('http://127.0.0.1:8000/')


print('status code: ',res.status_code)
print('In json: ',res.json())
print('Response: ',res.text)