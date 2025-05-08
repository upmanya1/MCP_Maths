from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8051,  # only used for SSE transport (set this to any port)
)


# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Takes Two integers and add them together"""
    return a + b
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Takes two integers a (minuend) and b (subtrahend) as input. Subtract b from a"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Takes two integers a (factor) and b (factor) as input. Multiply two numbers"""
    return a * b

@mcp.tool()
def concatenate(s1: str, s2: str) -> str:
    """Takes two strings s1 (first part) and s2 (second part) as input. Concatenate two strings"""
    return s1 + s2

@mcp.tool()
def is_even(n: int) -> bool:
    """Takes an integer n (number to check) as input. Check if a number is even"""
    return n % 2 == 0

@mcp.tool()
def celsius_to_fahrenheit(c: float) -> float:
    """Takes a float c (temperature in Celsius) as input. Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

@mcp.tool()
def string_length(s: str) -> int:
    """Takes a string s (text to measure) as input. Get length of a string"""
    return len(s)

@mcp.tool()
def reverse_string(s: str) -> str:
    """Takes a string s (text to reverse) as input. Reverse a string"""
    return s[::-1]
# Run the server
if __name__ == "__main__":
    transport = "sse"
    print("Running server with SSE transport")
    mcp.run(transport="sse")