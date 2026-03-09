from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="MCP Tool Server", log_level="ERROR", stateless_http=True)


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


# TODO: Write a resource to return the contents of a particular doc
@mcp.tool(name="get_docs")
def get_docs(doc_id:str):
    return docs[doc_id]


# TODO: Write a resource to return all doc id's
@mcp.tool(name="all_doc_ids")
def doc_ids():
    return list(docs.keys())   


mcp_app = mcp.streamable_http_app()