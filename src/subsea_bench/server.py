"""FastMCP v3 server entrypoint for subsea-bench."""

from pathlib import Path

import click
from fastmcp import FastMCP

mcp = FastMCP("subsea-bench")


@click.command()
@click.option(
    "--scenario",
    type=click.Path(exists=False, path_type=Path),
    default=None,
    help="Path to scenario configuration file",
)
def main(scenario: Path | None) -> None:
    """CLI entrypoint for the subsea-bench MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
