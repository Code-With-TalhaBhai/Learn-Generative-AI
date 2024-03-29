import requests

name = {'person':'Talha'}

res = requests.post('http://127.0.0.1:8000/bye',json=name)
# res = requests.post('http://127.0.0.1:8000/bye',json={'person':'Talha Bhai'})


print(res.json())