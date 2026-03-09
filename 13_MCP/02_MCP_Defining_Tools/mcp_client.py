import requests


url = "http://127.0.0.1:8000/mcp"


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json,text/event-stream"
}


# List all tools
response1 = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "params":{"name": "get_docs", "arguments": {"doc_id": "financials.docx"}},
    "method": "tools/call"
})


response2 = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 1,
    "params":{"name": "all_doc_ids"},
    "method": "tools/call"
})


print(response1.text)
print(response2.text)