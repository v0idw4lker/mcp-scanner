"""
VULNERABLE test MCP server, used to validate the end-to-end scanner
pipeline.

Capability: network-out (tool name + description contain "send http
webhook"). Serves as a second live target for the dynamic-scanning demo,
alongside fixtures/vulnerable_server_a.py.
"""
from mcp.server.mcpserver import MCPServer

server = MCPServer(name="vulnerable-webhook-server", version="0.1.0")


@server.tool()
def send_webhook(url: str, payload: str) -> str:
    """Sends a payload via an HTTP POST request to an external webhook."""
    return f"(simulated) POST to {url} with a payload of {len(payload)} characters."


if __name__ == "__main__":
    server.run(transport="stdio")
