"""
Minimal test MCP server, exposed over stdio.
Purpose: fixture for validating core/dynamic_client.py — a toy server with
a couple of tools, a resource, and a prompt, to confirm the scanner
actually connects, enumerates, and reports correctly.
"""
from mcp.server.mcpserver import MCPServer

server = MCPServer(name="fixture-stdio-server", version="0.1.0")


@server.tool()
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


@server.tool()
def read_note(note_id: str) -> str:
    """Reads a saved note by id."""
    notes = {"1": "Buy milk", "2": "Call the dentist"}
    return notes.get(note_id, "Note not found.")


@server.resource("notes://all")
def all_notes() -> str:
    """All saved notes, concatenated."""
    return "Buy milk\nCall the dentist"


@server.prompt()
def summarize_notes() -> str:
    """Prompt requesting a summary of the notes."""
    return "Summarize the notes below in a single sentence."


if __name__ == "__main__":
    server.run(transport="stdio")
