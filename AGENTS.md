# AGENTS.md

`subsea-bench` benchmarks AI coding agents on long-horizon subsea engineering tasks.
Agents are placed inside Devana Subsea (a fictional Aberdeen consultancy) and design a mooring system for a floating offshore wind turbine using five MCP tools.

## Project map

```
src/subsea_bench/
  config.py         Economic constants. Import from here; never hard-code fees or day counts.
  models.py         Pydantic v2 data models shared across the codebase.
  economics.py      Ledger: time tracking, charges, margin computation.
  workspace.py      Agent workspace provisioning and file access.
  catalog.py        Equipment catalog query and BOM pricing.
  analysis.py       Quasi-static analysis script execution.
  supervisor.py     Supervisor interface (LangChainSupervisor + FakeSupervisor).
  scoring.py        Final score computation (EM + CE -> composite).
  dnv.py            DNV-OS-E301 safety factor and MBL utilities.
  mcp/
    __init__.py     MCP server entry (binary: subsea-bench-mcp).
    tools/          One async function per file.
tests/unit/           CI-run tests (integration/ and validation/ are manual).
docs/
  architecture.md   System description. Read before any task.
  glossary.md       Domain term definitions.
  decisions/        Architecture decision records (ADRs).
  research/         Optional research docs (YYYY-MM-DD_<topic>.md).
```

## Commands

```
uv sync                        # install/update dependencies
uv run pytest tests/unit       # run unit tests
uv run ruff check src tests    # lint
uv run ruff format src tests   # format
uv run ty check src            # type check
```

## Workflow

Non-trivial work follows a fluid research -> plan -> implement loop.
Both Claude Code (`/plan`) and OpenCode (Plan primary agent, `Tab`) have plan mode built in; use it before editing any file you have not read.
The GitHub issue body is the spec.

<important if="you are starting any task">
Read first:
1. `docs/architecture.md` — system description, actors, tool surface, economics, scoring.
2. The issue body — files owned and acceptance criteria.
3. `src/subsea_bench/models.py` — shared data models; check here before inventing new types.
</important>

<important if="you are adding or modifying an MCP tool in src/subsea_bench/mcp/tools/">
One async function per file.
Module docstring must state: contract, cost (reference `config.py`), and sim-time advancement.
Never hard-code fee values; import from `config.py`.
</important>

<important if="you are adding an economic charge or sim-time advancement">
Import from `src/subsea_bench/config.py`.
Never hard-code a fee or a day count.
</important>

<important if="you are writing or modifying tests">
Unit tests in `tests/unit/`. CI runs only this directory.
Use `FakeSupervisor` for any test that exercises supervisor-dependent logic.
</important>

<important if="you are introducing a new dependency or a new top-level directory">
Record it as an ADR in `docs/decisions/`.
ADRs are for architecture and technical decisions only; workflow conventions live in this file.
Update `pyproject.toml` for any new dependency.
</important>

<important if="you are writing scenario content, briefing text, or documentation that names a firm">
The only firm used is Devana Subsea (fictional, based in Aberdeen).
Do not reference any real company or individual.
</important>

<important if="you are creating or modifying a diagram">
Use Mermaid syntax.
Run the `mermaid-diagram` skill (`.claude/skills/mermaid-diagram`) to render and verify before committing.
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

No `llms.txt` — use docs root: [pytest](https://docs.pytest.org/en/stable/) · [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/latest/) · [hatchling](https://hatch.pypa.io/latest/) · [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

Domain references: [MCP spec](https://modelcontextprotocol.io/specification) · [MoorPy](https://github.com/NREL/MoorPy) · [IEA-15MW turbine](https://github.com/IEAWindTask37/IEA-15-240-RWT) · [DNV-OS-E301](https://www.dnv.com/oilgas/standards/offshore-standards/)
