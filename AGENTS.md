# AGENTS.md -- subsea-bench

Offshore-engineering benchmark for LLM agents. LangChain supervisors, MCP tools, ADR-driven design, Pydantic-typed I/O.

## Stack
Python 3.14+, uv, Pydantic v2, LangChain (supervisor pattern), MCP servers.
Tests: `uv run pytest -x tests/unit`. Lint: `uv run ruff check src tests`. Format: `uv run ruff format --check src tests`. Type: `uv run ty check src`.

## Hard rules
1. Never push to `main`. Branch + draft PR.
2. Never delete a failing test to pass CI.
3. Every new tool gets a Pydantic schema in `src/subsea_bench/models.py` first.
4. Cross-cutting design decisions get an ADR in `docs/decisions/`.
5. No code style rules here -- ruff enforces them.

<important if="you are starting any task">
Read `docs/architecture.md`, the issue body, and `src/subsea_bench/models.py` before starting.
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
