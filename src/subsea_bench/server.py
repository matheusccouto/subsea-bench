"""FastMCP v3 server entrypoint for subsea-bench."""

from fastmcp import FastMCP

mcp = FastMCP("subsea-bench")


def main() -> None:
    """CLI entrypoint for the subsea-bench MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
