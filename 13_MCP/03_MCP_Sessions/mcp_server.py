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


# TODO: Write a tool to edit a doc
@mcp.tool(name="edit_docs")
def edit_docs(doc_id:str, new_str:str):
    docs[doc_id] = new_str
    return new_str



@mcp.resource(uri='docs://documents',mime_type="application/json")
def list_docs():
    return list(docs.keys())



@mcp.resource(uri="docs://documents/{doc_id}", mime_type="application/json")
def doc_content(doc_id: str):
    if doc_id in docs:
        return docs[doc_id]
    else:
        raise mcp.ResourceNotFound('Document Not Found')







# TODO: Write a tool to read a doc
# TODO: Write a tool to edit a doc
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc
mcp_app = mcp.streamable_http_app()