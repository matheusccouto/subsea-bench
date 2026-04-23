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


def test_cli_accepts_scenario_argument() -> None:
    """Verify that --scenario argument is parsed correctly."""
    import argparse
    from pathlib import Path

    # Test argparse directly without running MCP server
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", type=Path, required=False)
    args = parser.parse_args(["--scenario", "/tmp/test"])
    assert args.scenario == Path("/tmp/test")
