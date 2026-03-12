import asyncio
from mcp import ClientSession, types
from contextlib import AsyncExitStack
from mcp.client.streamable_http import streamable_http_client
from typing import Optional
from mcp_server import docs
from pydantic import AnyUrl
import json

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
        return (await self.session().list_tools()).tools
    
    async def call_tool(self,tool_name, *args, **kwargs):
        return await self.session().call_tool(tool_name, *args, **kwargs)
    
    async def resources_list(self):
        return (await self.session().list_resources()).resources
    
    async def resource_templates_list(self):
        return (await self.session().list_resource_templates()).resourceTemplates
    
    async def read_resources(self,uri):
        result = await self.session().read_resource(AnyUrl(uri))
        resource = result.contents[0]

        if isinstance(resource, types.TextResourceContents):
            if resource.mimeType == "application/json":
                final_result = resource.text
                try:
                    final = json.loads(final_result)
                    return final
                except:
                    return final_result   
        return resource
    

    async def list_prompts(self):
        return (await self.session().list_prompts()).prompts


    async def get_prompt(self,doc_id):
        return (await self.session().get_prompt(name="format", arguments= {'doc_id': doc_id})).messages


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
        # Tool --- ------Tools List
        tools = await client.tools_list()
        print('List Tools')
        print(tools)
        print()

        # Calling Specific Tool
        doc_tool_1 = await client.call_tool('get_docs',{"doc_id":"plan.md"})
        print('Tool Call 1')
        print(doc_tool_1)
        print()

        # Calling Specific Tool To Edit
        doc_tool2 = await client.call_tool('edit_docs',{"doc_id": "plan.md", "new_str": "New Cusom Planning"})
        print('Tool Call 2')
        print(doc_tool2)
        print()

        # Again making tool call to see if there actual changes happened in 'report.pdf'
        doc_tool_3 = await client.call_tool('get_docs',{"doc_id":"plan.md"})
        print('Tool Call 3')
        print(doc_tool_3)
        print()

        

        # Resources
        # Resoures List
        resources_list = await client.resources_list()
        print('List Resources')
        print(resources_list)
        print()

        # Resource Template List
        resource_template_list = await client.resource_templates_list()
        print('List Resource Templates')
        print(resource_template_list)
        print()

        # Read Resources
        read_resources1 = await client.read_resources('docs://documents')
        print('Read Resources 1')
        print(read_resources1)
        print()


        read_resources2 = await client.read_resources('docs://documents/outlook.pdf')
        print('Read Resources 2')
        print(read_resources2)
        print()


        
        # Prompts
        # List Prompts
        list_prompts = await client.list_prompts()
        print('List Prompts')
        print(list_prompts)
        print()


        # Get Prompt 1
        prompt1 = await client.get_prompt('plan.md')
        print('Get Prompt 1')
        print(prompt1)
        print()

        # Get Prompt 2
        prompt2 = await client.get_prompt('financials.docx')
        print('Get Prompt 2')
        print(prompt2)
        print()





if __name__ == "__main__":
    asyncio.run(main())