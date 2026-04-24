"""FastMCP v3 server entrypoint for subsea-bench."""

import argparse
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP("subsea-bench")


@mcp.tool()
def placeholder() -> str:
    """Placeholder tool for initial server setup.

    Returns:
        A simple greeting message.
    """
    return "Subsea-bench MCP server is running."


def main() -> None:
    """CLI entrypoint for the subsea-bench MCP server.

    Parses command-line arguments and starts the FastMCP server.
    """
    parser = argparse.ArgumentParser(
        description="Subsea-bench MCP Server",
        prog="subsea-bench-server",
    )
    parser.add_argument(
        "--scenario",
        type=Path,
        help="Path to scenario configuration file (not yet fully implemented)",
    )
    args = parser.parse_args()

    # Scenario path is parsed but not yet fully implemented
    if args.scenario:
        if not args.scenario.exists():
            print(f"Error: Scenario file not found: {args.scenario}", file=sys.stderr)
            sys.exit(1)
        # Future: Load and use scenario configuration
        print(f"Scenario path: {args.scenario}", file=sys.stderr)

    # Run the FastMCP server
    mcp.run()


if __name__ == "__main__":
    main()
