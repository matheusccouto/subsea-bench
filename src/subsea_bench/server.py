"""FastMCP v3 server entrypoint for subsea-bench."""

import argparse
import sys

from fastmcp import FastMCP

mcp = FastMCP("subsea-bench")


@mcp.tool()
def placeholder() -> str:
    """Placeholder tool for testing server connectivity."""
    return "subsea-bench server is running"


def main() -> None:
    """CLI entrypoint for the subsea-bench MCP server."""
    parser = argparse.ArgumentParser(description="Subsea-bench MCP server")
    parser.add_argument(
        "--scenario",
        type=str,
        default=None,
        help="Path to scenario configuration file (not yet implemented)",
    )
    args = parser.parse_args()

    if args.scenario:
        print(f"Scenario path: {args.scenario} (not yet implemented)", file=sys.stderr)

    mcp.run()


if __name__ == "__main__":
    main()
