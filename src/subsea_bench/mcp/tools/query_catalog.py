"""MCP tool: query_catalog.

Contract: Query the mooring equipment catalog for chain, shackles, or connectors.
Returns a list of matching catalog items with grades, MBLs, and unit costs.

Cost: free (no charge).
Sim-time advancement: none.
"""

from subsea_bench.models import CatalogItem


async def query_catalog(
    item_type: str,
    grade: str | None = None,
    diameter_mm: float | None = None,
    min_mbl_kn: float | None = None,
) -> list[CatalogItem]:
    """MCP tool handler: query the equipment catalog and return matching items."""
    raise NotImplementedError
