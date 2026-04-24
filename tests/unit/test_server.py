"""Unit tests for the FastMCP server."""

import pytest
from fastmcp.client import Client

from subsea_bench.server import mcp


@pytest.fixture
async def server_client():
    """Fixture that provides a FastMCP client connected to the server."""
    async with Client(mcp) as client:
        yield client


async def test_mcp_instance_created() -> None:
    """Verify that the FastMCP instance is created."""
    assert mcp is not None
    assert mcp.name == "subsea-bench"


async def test_mcp_has_instructions(server_client: Client) -> None:
    """Verify that the server has instructions for clients."""
    # The server should have instructions set
    assert mcp.instructions is not None
    assert "subsea engineering" in mcp.instructions.lower()


async def test_server_connects(server_client: Client) -> None:
    """Verify that the server can be connected to via client."""
    # Connection successful if fixture works
    assert server_client is not None
