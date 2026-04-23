"""Unit tests for the FastMCP server."""

import subprocess
import sys

from subsea_bench.server import mcp


def test_mcp_instance_created() -> None:
    """Verify that the FastMCP instance is created."""
    assert mcp is not None
    assert mcp.name == "subsea-bench"


def test_cli_entrypoint_exists() -> None:
    """Verify that the CLI entrypoint is registered."""
    result = subprocess.run(
        [sys.executable, "-m", "subsea_bench.server", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--scenario" in result.stdout
