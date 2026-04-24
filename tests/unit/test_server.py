"""Unit tests for the FastMCP server entrypoint."""

import subprocess
import sys
from pathlib import Path

import pytest

from subsea_bench.server import main, mcp, placeholder


class TestFastMCPInstance:
    """Tests for the FastMCP server instance."""

    def test_mcp_instance_exists(self) -> None:
        """Verify that the MCP server instance is created."""
        assert mcp is not None

    def test_mcp_server_name(self) -> None:
        """Verify the MCP server has the correct name."""
        # FastMCP stores the name internally
        assert mcp.name == "subsea-bench"


class TestPlaceholderTool:
    """Tests for the placeholder tool."""

    def test_placeholder_returns_string(self) -> None:
        """Verify placeholder tool returns a string."""
        result = placeholder()
        assert isinstance(result, str)

    def test_placeholder_content(self) -> None:
        """Verify placeholder tool returns expected content."""
        result = placeholder()
        assert "running" in result.lower()


class TestCLIEntrypoint:
    """Tests for the CLI entrypoint."""

    def test_cli_registered(self) -> None:
        """Verify the CLI entrypoint is registered."""
        result = subprocess.run(
            [sys.executable, "-m", "subsea_bench.server", "--help"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent.parent,
        )
        # Should show help, not error
        has_usage = "usage" in result.stdout.lower() or "usage" in result.stderr.lower()
        assert result.returncode == 0 or has_usage

    def test_cli_scenario_argument_missing_file(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Verify CLI exits with error for non-existent scenario file."""
        monkeypatch.setattr(
            sys, "argv", ["subsea-bench-server", "--scenario", "/nonexistent/path.json"]
        )
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1

    def test_cli_scenario_argument_with_file(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Verify CLI accepts scenario argument with existing file."""
        scenario_file = tmp_path / "scenario.json"
        scenario_file.write_text("{}")
        monkeypatch.setattr(sys, "argv", ["subsea-bench-server", "--scenario", str(scenario_file)])
        # main() will try to run the MCP server, which we can't test directly
        # but we can test that it doesn't exit with error for valid scenario path
        # by checking the argument parsing doesn't fail
        # We'll mock mcp.run to prevent actual server startup
        from unittest.mock import patch

        with patch.object(mcp, "run"):
            main()  # Should not raise
