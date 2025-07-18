 What is VeritasAI?
VeritasAI integrates directly with LLM systems through the Model Context Protocol (MCP) to provide:

Real-time command analysis - Evaluates user inputs before they reach the LLM
Risk assessment - Categorizes threats and assigns risk levels
Pattern-based detection - Uses sophisticated patterns to identify potential security threats
Native LLM integration - Works seamlessly within the LLM workflow, not as an external filter


Key Features:

Proactive Security: Analyzes commands before execution
Real-time Processing: Zero-latency threat detection
LLM-Specific: Purpose-built for AI security, not retrofitted
Native Integration: Works directly with Claude via MCP
Risk Classification: Intelligent threat categorization
Pattern Recognition: Advanced threat pattern detection

Installation
Prerequisites:

Python 3.8+
uv package manager - Required for dependency management


Configurations:

{
  "mcpServers": {
    "VeritasAi": {
      "command": "uv",
      "args": [
        "run",
        "--with", "pandas",
        "--with", "requests",
        "--with", "pydantic",
        "--with", "fastmcp",
        "python",
        "/Users/full-path/VeritasAI/server.py"
      ]
    }
  }
}

Debuging: 
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log



