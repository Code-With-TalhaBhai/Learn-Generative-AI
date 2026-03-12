from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="Our FastAPI Mcp",stateless_http=True)


@mcp.tool(name="hello")
def hello(name: str)->str:
    return f"Hello greetings from {name}"


mcp_app = mcp.streamable_http_app()

