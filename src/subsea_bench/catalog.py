"""Equipment catalog query and BOM pricing utilities.

The catalog exposes mooring hardware (studless chain, shackles, connectors)
with grades, MBLs, and unit costs.
The agent queries it via the query_catalog MCP tool.
"""

from subsea_bench.models import BOM, CatalogItem


def query_chain(
    grade: str,
    diameter_mm: float | None = None,
    min_mbl_kn: float | None = None,
) -> list[CatalogItem]:
    """Return catalog items matching the given chain grade and optional filters."""
    raise NotImplementedError


def price_bom(lines: list[tuple[str, float, str]]) -> BOM:
    """Price a bill of materials from a list of (catalog_id, quantity, unit) tuples."""
    raise NotImplementedError
