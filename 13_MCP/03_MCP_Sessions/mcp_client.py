import asyncio
from mcp import ClientSession


class McpClient:
    def __init__(self,server_url:str):
        self._server_url = server_url


    async def connect(self):
        ...


    async def __aenter__(self):
        await self.connect()
        return self
    
    async def cleanup():
        ...

    async def __aexit__(self,exc_type,exc_val,traceback):
        return self.cleanup()


async def main():
    with await McpClient() as client:
        ...




if __name__ == "__main__":
    asyncio.run(main)