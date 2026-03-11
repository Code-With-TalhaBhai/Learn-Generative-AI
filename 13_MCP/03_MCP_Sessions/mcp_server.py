from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from mcp.types import PromptMessage, TextContent


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


# TODO: Write a resource to return all doc id's
@mcp.resource(uri='docs://documents',mime_type="application/json")
def list_docs_resources():
    return list(docs.keys())


# Resource template
# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(uri="docs://documents/{doc_id}", mime_type="application/json")
def doc_content(doc_id: str):
    if doc_id in docs:
        return docs[doc_id]
    else:
        # raise mcp.ResourceNotFound('Document Not Found')
        raise Exception('Document Not Found')



# TODO: Write a prompt to rewrite a doc in markdown format
# @mcp.prompt()
@mcp.prompt(name="format", description="Rewrites the contents of the document in Markdown format")
def format_document(doc_id: str)->list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.

    The contents of the document you need to reformat is:
    <document_content>
    {docs[doc_id]}
    </document_content>

    Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra text, but don't change the meaning of the report.
    After the document has been edited, respond with the final version of the doc. Don't explain your changes.
    """

    return [base.UserMessage(prompt)]



@mcp.prompt(name="summarize", description="Summarizes the contents of the document")
def summarize_document(doc_id: str ) -> list[PromptMessage]:

    prompt_text = f"""
    Your goal is to summarize the contents of the document.
    Document Contents: {docs[doc_id]}
    Include a concise summary of the document's main points.
    """
    return [PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))]



# TODO: Write a tool to read a doc
# TODO: Write a tool to edit a doc
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc
mcp_app = mcp.streamable_http_app()