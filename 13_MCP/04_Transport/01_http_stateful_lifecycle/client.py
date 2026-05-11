import asyncio
import httpx



async def initialize_mcp(client,url):
    init_payload = {
        "jsonrpc": "2.0",
        "method": "initialize",
        "id": 1,
        "params": {
            "protocolVersion": "2025-06-18",
            "capabilities": {
                "roots": {
                    "listChanged": True
                },
                "sampling": {},
                "elicitation": {}
            },
            "clientInfo": {
                "name": "ExampleClient",
                "title": "Example Client Display Name",
                "version": "1.0.0"
            }
        }
    }
        
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }

    print("sending initialized request")
    response = await client.post(url, json=init_payload, headers=headers)
    response.raise_for_status()
    print('response header is: ',response.headers)

    session_id = response.headers.get('mcp-session-id')

    if session_id:
        print(f"Session Id is: {session_id}")
    print(f"Response: {response.text}")


    return session_id


async def send_initialized(client, url, session_id):

    initialized_payload = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "MCP-Protocol-Version": "2025-06-18",
        "mcp-session-id": session_id
    }

    print("Send initialized notification")
    response = await client.post(url, json=initialized_payload, headers=headers)
    print(f"Initialized Notification Response {response}")
    return response


async def list_tools(client, url, session_id):
    
    list_tools_payload = {
        "jsonrpc": "2.0",
        "method": "tools/list",
        "id": 2,
        "params": {}
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "MCP-Protocol-Version": "2025-06-18",
        "mcp-session-id": session_id
    }


    tools_response = await client.post(url, json=list_tools_payload, headers=headers)
    print(f"Tools List Response: {tools_response.text}")


async def call_tool(client, url, session_id):

    call_tool_payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": "3",
        "params": {"name": "get_forecast", "arguments": {"city": "Lahore"}}
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "MCP-Protocol-Version": "2025-06-18",
        "mcp-session-id": session_id
    }

    tools_call_response = await client.post(url, json=call_tool_payload, headers=headers)
    print(f'Tools call response', {tools_call_response.text})



def prepare_for_shutdown(session_id: str):
    print("Prepare MCP Server for shutdown")
    print("   -> For HTTP transport: 'shutdown is indicated by closing HTTP connection'")
    print(f"   -> Session {session_id} will terminate when connection closes")



async def main():
    url = "http://localhost:8000/mcp"
    session_id = None

    async with httpx.AsyncClient() as client:
        print('Opening http connnection for MCP Session')

        try:
            session_id  = await initialize_mcp(client, url)
            if not session_id:
                print("Failed to get Session ID")
                return
            
            await send_initialized(client,url, session_id)
            print()
            await list_tools(client,url,session_id)
            print()
            await call_tool(client,url,session_id)
            print()
            prepare_for_shutdown(session_id)


        except Exception as e:
            print(f"MCP lifecycle error: {e}")


if __name__ == "__main__":
    asyncio.run(main())