
from logic import SecurityLogic
from patterns import DETECTION_PATTERNS
from fastmcp import FastMCP

mcp = FastMCP("Veritas")


security_logic = SecurityLogic(security_service=None)

@mcp.tool(
    name="let_safe_commands",
    description="if command is safe then run it, else block it"
)
def let_safe_commands(content: str) -> bool:
    """Check if the given content is safe to execute"""
    try:
        return {
            "command is safe to run: "security_logic.is_content_safe(content)
            }
    except Exception as e:
        print(f"Error: {e}")
        return False




if __name__ == '__main__':  
    mcp.run()