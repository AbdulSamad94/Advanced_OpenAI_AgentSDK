from mcp.server import StdioTransport, ToolServer
from pydantic import BaseModel
import asyncio


server = ToolServer()


@server.tool()
def add(a: float, b: float) -> float:
    return a + b


@server.tool()
def sub(a: float, b: float) -> float:

    return a - b


@server.tool()
def mul(a: float, b: float) -> float:
    return a * b


@server.tool()
def div(a: float, b: float) -> float:
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    asyncio.run(StdioTransport(server).run())
