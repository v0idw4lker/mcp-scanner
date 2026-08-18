"""
Minimal test MCP server, exposed over Streamable HTTP, WITHOUT
authentication.
Purpose: fixture to confirm core/dynamic_client.py actually detects a
missing auth enforcement (the server responds 200 with no Authorization
header at all). A local toy server, not a benchmark target.
"""
from mcp.server.mcpserver import MCPServer

server = MCPServer(name="fixture-http-server", version="0.1.0")


@server.tool()
def echo(text: str) -> str:
    """Echoes the given text back."""
    return text


if __name__ == "__main__":
    server.run(transport="streamable-http", host="127.0.0.1", port=8931)
