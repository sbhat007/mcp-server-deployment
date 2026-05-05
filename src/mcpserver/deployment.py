from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Deployment demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b