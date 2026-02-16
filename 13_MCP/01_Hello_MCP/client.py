import requests


url = "http://127.0.0.1:8000/mcp"


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json,text/event-stream"
}


# List all tools
response = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "params":{},
    "method": "tools/list"
})

print(response.text)


# response = requests.post(url,headers=headers, json={
#     "jsonrpc": "2.0",
#     "id": 1,
#     "params": {"name": "hello","arguments": {"name": "Talha"}},
#     "method": "tools/call"
# })

# print(response.text)


# for line in response.iter_lines():
#     if line:
#         print(line)
