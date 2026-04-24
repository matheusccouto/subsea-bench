"""FastMCP v3 server for subsea-bench."""

import argparse

from fastmcp import FastMCP

mcp = FastMCP("Subsea Bench MCP Server")


def main() -> None:
    """CLI entrypoint for the subsea-bench server."""
    parser = argparse.ArgumentParser(description="Subsea Bench MCP Server")
    parser.add_argument(
        "--scenario",
        type=str,
        default=None,
        help="Path to scenario configuration file (not yet implemented)",
    )
    _args = parser.parse_args()

    # Scenario path is parsed but not yet implemented
    # TODO: Load scenario from _args.scenario when implemented

    mcp.run()


if __name__ == "__main__":
    main()