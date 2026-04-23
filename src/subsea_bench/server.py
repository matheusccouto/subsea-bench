"""FastMCP v3 server entrypoint for subsea-bench."""

import argparse
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("subsea-bench")


def main() -> None:
    """CLI entrypoint for the subsea-bench MCP server."""
    parser = argparse.ArgumentParser(description="Subsea Bench MCP Server")
    parser.add_argument(
        "--scenario",
        type=Path,
        required=False,
        help="Path to scenario configuration (not yet implemented)",
    )
    args = parser.parse_args()

    # Scenario path is parsed but not yet fully implemented
    if args.scenario:
        print(f"Scenario path received: {args.scenario} (not yet implemented)")

    mcp.run()


if __name__ == "__main__":
    main()
