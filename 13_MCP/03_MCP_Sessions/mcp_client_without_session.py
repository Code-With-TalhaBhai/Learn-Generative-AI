import requests


headers = {
    "Accept": "application/json,text/event-stream"
}


# Resources

# List Resources
# resouces_list = requests.post(url='http://localhost:8000/mcp/',headers=headers,json={
#     "jsonrpc": "2.0",
#     "id": 2,
#     "method": "resources/list",
#     "params": {}
# })
# print(resouces_list.text)


# Read Resources
read_resouces1= requests.post(url='http://localhost:8000/mcp/',headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://documents"}
})
print(read_resouces1.text)


read_resouces2= requests.post(url='http://localhost:8000/mcp/',headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://{financials.docx}"}
})
print(read_resouces1.text)