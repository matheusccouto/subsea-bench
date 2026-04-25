# Architecture Decision Records

ADRs document significant **architecture and technical decisions** made during the development of subsea-bench.
Workflow conventions and coding patterns live in `AGENTS.md`, not here.

## Format

Each ADR is a markdown file named `NNNN-<short-title>.md` where `NNNN` is a zero-padded four-digit sequence number.
Use the following template:

```markdown
# NNNN: Title

**Status:** Accepted | Proposed | Deprecated | Superseded by #NNNN

## Context

What situation, constraint, or question prompted this decision?

## Decision

What was decided?

## Consequences

What are the trade-offs, follow-on tasks, or known limitations?
```

## Index

| # | Title | Status |
|---|-------|--------|
| [0001](0001-supervisor-framework.md) | Supervisor framework: LangChain | Accepted |

## Guidance

- Record a new ADR for every non-obvious architectural or technical decision: framework choices, language, data model, licence, storage backend.
- Do not write ADRs for workflow or process decisions; those live in `AGENTS.md`.
- Do not retroactively delete superseded ADRs; mark them "Superseded by #NNNN".
- Keep ADRs short (under 60 lines). If the reasoning is long, link to a research doc in `docs/research/`.
- Any issue that introduces a new external dependency, top-level directory, or language must include a new ADR.
