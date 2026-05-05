To run this mcp server locally add below json to your mcp client - 

'''json
    "Deployment demo - Add two numbers": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/sbhat007/mcp-server-deployment.git",
        "mcp-server"
      ]
    }

This should give access to this tool to your mcp client 
