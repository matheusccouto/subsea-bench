"""Unit tests for the FastMCP server."""

import subprocess
import sys

import pytest


def test_server_module_imports() -> None:
    """Test that the server module can be imported."""
    from subsea_bench import server

    assert hasattr(server, "mcp")
    assert hasattr(server, "main")


@pytest.mark.asyncio
async def test_server_has_placeholder_tool() -> None:
    """Test that the server has a placeholder tool."""
    from subsea_bench.server import mcp

    tools = await mcp.list_tools()
    tool_names = [t.name for t in tools]
    assert "placeholder" in tool_names


def test_cli_help() -> None:
    """Test that CLI help works."""
    result = subprocess.run(
        [sys.executable, "-m", "subsea_bench.server", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "--scenario" in result.stdout


def test_cli_scenario_arg() -> None:
    """Test that --scenario argument is parsed."""
    result = subprocess.run(
        [sys.executable, "-m", "subsea_bench.server", "--scenario", "test.yaml"],
        capture_output=True,
        text=True,
        timeout=5,
    )
    # Server will start but we just check the arg was parsed
    assert "test.yaml" in result.stderr or result.returncode == 0
