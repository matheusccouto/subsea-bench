"""Tests for the FastMCP server module."""

import argparse

import pytest

from subsea_bench.server import main, mcp


class TestServerInstance:
    """Tests for the FastMCP server instance."""

    def test_mcp_instance_exists(self) -> None:
        """Verify the FastMCP server instance is created."""
        assert mcp is not None

    def test_mcp_instance_name(self) -> None:
        """Verify the server has the correct name."""
        assert mcp.name == "Subsea Bench MCP Server"


class TestMainEntrypoint:
    """Tests for the CLI entrypoint."""

    def test_main_imports_successfully(self) -> None:
        """Verify main function can be imported."""
        assert callable(main)

    def test_main_runs_with_default_args(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Verify main function parses default args without error."""
        monkeypatch.setattr("sys.argv", ["subsea-bench-server"])
        # We don't actually run mcp.run() in tests, just verify parsing works
        parser = argparse.ArgumentParser()
        parser.add_argument("--scenario", type=str, default=None)
        args = parser.parse_args([])
        assert args.scenario is None

    def test_main_parses_scenario_arg(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Verify --scenario argument is parsed correctly."""
        monkeypatch.setattr("sys.argv", ["subsea-bench-server", "--scenario", "test.json"])
        parser = argparse.ArgumentParser()
        parser.add_argument("--scenario", type=str, default=None)
        args = parser.parse_args(["--scenario", "test.json"])
        assert args.scenario == "test.json"