Offshore-engineering benchmark for LLM agents. LangChain supervisors, MCP tools, ADR-driven design, Pydantic-typed I/O.

## Stack
Python 3.14+, uv, Pydantic v2, LangChain (supervisor pattern), MCP servers.
Tests: `uv run pytest -x tests/unit`. Lint: `uv run ruff check src tests`. Format: `uv run ruff format --check src tests`. Type: `uv run ty check src`.

## Hard rules
1. Never delete a failing test to pass CI.
2. Every new tool gets a Pydantic schema in `src/subsea_bench/models.py` first.
3. Cross-cutting design decisions get an ADR in `docs/decisions/`.

<important if="you are starting any task">
Read the docs relevant to your task. Start with `docs/architecture.md` for system overview, then drill into the specific area. Check `docs/decisions/` for prior decisions on related topics.
</important>

<important if="you are adding or modifying an MCP tool">
One async function per file in `src/subsea_bench/mcp/tools/`. Module docstring must state contract, cost (reference `config.py`), sim-time. Never hard-code fees.
</important>

<important if="you are writing or modifying tests">
Unit tests in `tests/unit/`. Use `FakeSupervisor` for supervisor-dependent logic. CI runs only this directory.
</important>

<important if="you are introducing a new dependency or top-level directory">
Record as ADR in `docs/decisions/`. Update `pyproject.toml`.
</important>

<important if="you are creating or modifying a diagram">
Use Mermaid syntax. Render and verify before committing.
</important>

## References
Fetch the `llms.txt` before making assumptions about tool APIs or CLI flags:

| Tool | llms.txt |
|---|---|
| uv | https://docs.astral.sh/uv/llms.txt |
| ruff | https://docs.astral.sh/ruff/llms.txt |
| ty | https://docs.astral.sh/ty/llms.txt |
| FastMCP | https://gofastmcp.com/llms.txt |
| MCP spec | https://modelcontextprotocol.io/llms.txt |
| LangChain | https://docs.langchain.com/llms.txt |
| Pydantic | https://docs.pydantic.dev/latest/llms.txt |
| Claude API | https://platform.claude.com/llms.txt |

No `llms.txt` -- use docs root: [pytest](https://docs.pytest.org/en/stable/) | [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/latest/) | [hatchling](https://hatch.pypa.io/latest/) | [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

Domain: [MCP spec](https://modelcontextprotocol.io/specification) | [MoorPy](https://github.com/NREL/MoorPy) | [IEA-15MW](https://github.com/IEAWindTask37/IEA-15-240-RWT) | [DNV-OS-E301](https://www.dnv.com/oilgas/standards/offshore-standards/)