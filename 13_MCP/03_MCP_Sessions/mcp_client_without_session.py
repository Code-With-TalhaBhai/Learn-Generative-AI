import requests


headers = {
    "Accept": "application/json,text/event-stream"
}

url = "http://localhost:8000/mcp/"



# ---------------------------------------- Tools -------------------------------------



# List Tools
tools_list = requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
})
print('Tools List')
print(tools_list.text)



# Call Tools
tool_call_1 = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {"name": "get_docs", "arguments": {"doc_id": "report.pdf"}}
})
print('Tools Call: 1')
print(tool_call_1.text)


tool_call_2 = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {"name": "edit_docs", "arguments": {"doc_id": "report.pdf", "new_str": "This is the new report added to pdf"}}
})
print('Tools Call: 2')
print(tool_call_2.text)


# Again making tool call to see if there actual changes happened in 'report.pdf'
tool_call_3 = requests.post(url, headers=headers, json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {"name": "get_docs", "arguments": {"doc_id": "report.pdf"}}
})
print('Tools Call: 3')
print(tool_call_3.text)


# ---------------------------------------- RESOURCES -------------------------------------

# # List Resources
resouces_list = requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/list",
    "params": {}
})
print('List Resources')
print(resouces_list.text)


# Read Particular Resources
read_resouces1= requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://documents"}
})
print('Resources 1')
print(read_resouces1.text)

read_resouces2= requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://documents/financials.docx"}
})
print('Resources 2')
print(read_resouces2.text)

read_resouces3= requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "resources/read",
    "params": {"uri": "docs://documents/outlook.pdf"}
})
print('Resources 3')
print(read_resouces3.text)



# ------------------------------------- PROMPTS -----------------------------------------

# List Prompts
prompts_list = requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "prompts/list",
    "params": {}
})
print('List Prompts')
print(prompts_list.text)


# Read Prompts
prompt1 = requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "prompts/get",
    "params": {"name": "format","arguments": {"doc_id": "spec.txt"}}
})
print('Prompt 1')
print(prompt1.text)


prompt2 = requests.post(url=url,headers=headers,json={
    "jsonrpc": "2.0",
    "id": 2,
    "method": "prompts/get",
    "params": {"name": "summarize","arguments": {"doc_id": "spec.txt"}}
})
print('Prompt 2')
print(prompt2.text)