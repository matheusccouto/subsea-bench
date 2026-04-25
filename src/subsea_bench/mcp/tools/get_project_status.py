"""MCP tool: get_project_status.

Contract: Return the current project status snapshot, including simulated day,
margin, review rounds used, questions asked, and analyses run.

Cost: free (no charge).
Sim-time advancement: none.
"""

from subsea_bench.models import ProjectStatus


async def get_project_status() -> ProjectStatus:
    """MCP tool handler: return the current ProjectStatus."""
    raise NotImplementedError
