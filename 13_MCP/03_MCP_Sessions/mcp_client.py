import asyncio
from mcp import ClientSession
from contextlib import AsyncExitStack
from mcp.client.streamable_http import streamable_http_client
from typing import Optional
from mcp_server import docs


class McpClient:
    def __init__(self,server_url:str):
        self._server_url = server_url
        self._exit_stack = AsyncExitStack()
        self._session : Optional[ClientSession] = None


    async def connect(self):
        streamable_transport = await self._exit_stack.enter_async_context(streamable_http_client(self._server_url))
        _read,_write,_get_session_id = streamable_transport
        self._session = await self._exit_stack.enter_async_context(ClientSession(_read,_write))
        await self._session.initialize()

    def session(self)->ClientSession:
        if self._session is None:
            raise ConnectionError("Client Session not initialized")
        return self._session
    
    async def tools_list(self):
        return (await self._session.list_tools()).tools
    
    async def call_tool(self,tool_name, *args, **kwargs):
        return await self._session.call_tool(tool_name, *args, **kwargs)

    async def __aenter__(self):
        await self.connect()
        return self
    
    async def cleanup(self):
        await self._exit_stack.aclose()
        self._session = None

    async def __aexit__(self,exc_type,exc_val,traceback):
        return await self.cleanup()


async def main():
    async with McpClient(server_url="http://localhost:8000/mcp/") as client:
        # Calling Tools List
        # tools = await client.tools_list()
        # print('tools are: ',tools)

        # Calling Specific Tool
        doc_tool1 = await client.call_tool('get_docs',{"doc_id":"plan.md"})
        print(doc_tool1)
        print()
        print(doc_tool1.content[0].text)
        print()


        # Calling Specific Tool To Edit
        doc_tool2 = await client.call_tool('edit_docs',{"doc_id": "plan.md", "new_str": "New Cusom Text"})
        print(doc_tool2)



if __name__ == "__main__":
    asyncio.run(main())