# MCP Tool Server and Client Example

A demonstration of a client-server architecture using MCP (Modular Computing Platform) with Server-Sent Events (SSE) transport. The server exposes several utility tools, and the client connects to interact with them.

## Project Overview

- **Server**: A FastMCP-based server providing mathematical, string manipulation, and utility tools.
- **Client**: Connects to the server, lists available tools, and demonstrates calling a tool (addition).

## Prerequisites

- Python 3.7+
- `pip` package manager
- `uv` (for running the server): Install with `pip install uv`

## Installation

1. Clone the repository (if applicable) and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root (though no specific environment variables are required for this example):
```bash
touch .env
```

## Running the Server

Start the server on port 8051 using SSE transport:
```bash
uv run server.py
```
**Note**: Ensure the server is running before starting the client.

## Available Tools

The server provides the following tools:

| Tool Name               | Description                                                                 | Parameters                                  |
|-------------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| `add`                   | Adds two integers.                                                          | `a` (int), `b` (int)                       |
| `subtract`              | Subtracts `b` (subtrahend) from `a` (minuend).                              | `a` (int), `b` (int)                       |
| `multiply`              | Multiplies two integers.                                                    | `a` (int), `b` (int)                       |
| `concatenate`           | Concatenates two strings.                                                   | `s1` (str), `s2` (str)                     |
| `is_even`               | Checks if an integer is even.                                               | `n` (int)                                  |
| `celsius_to_fahrenheit` | Converts Celsius to Fahrenheit.                                             | `c` (float)                                |
| `string_length`         | Returns the length of a string.                                             | `s` (str)                                  |
| `reverse_string`        | Reverses a string.                                                          | `s` (str)                                  |

## Running the Client

Execute the client script to interact with the server:
```bash
python client.py
```
**Expected Output**:
- List of available tools.
- Result of `2 + 3` calculation.

## Example Usage

Modify `client.py` to call other tools. For example, to subtract 3 from 5:
```python
result = await session.call_tool("subtract", arguments={"a": 5, "b": 3})
print(f"5 - 3 = {result.content[0].text}")
```

## Troubleshooting

- **Server Not Reachable**: Ensure the server is running on port 8051 and the client connects to `http://localhost:8051/sse`.
- **Missing Dependencies**: Verify all packages in `requirements.txt` are installed.
- **Async Issues**: If running in an interactive environment (e.g., Jupyter), keep `nest_asyncio.apply()` in the client code.
