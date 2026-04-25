# 0001: Supervisor framework: LangChain

**Status:** Accepted

**Date:** 2026-04-24

## Context

The Supervisor component (`supervisor.py`) has two responsibilities:
1. Ground answers in project facts (RAG retrieval).
2. Produce natural human-sounding replies on behalf of Devana Subsea (LLM generation).

A framework is needed to wire these two concerns together.
Candidates include raw Anthropic SDK with a custom retrieval layer, Pydantic AI, LlamaIndex, Haystack, and LangChain.

## Decision

**LangChain** (`langchain>=0.3` + `langchain-anthropic>=0.3`), provisionally.

Rationale: the project owner has direct familiarity with LangChain, which reduces ramp-up time and makes the first working supervisor faster to build.
LangChain's ecosystem covers retrievers, vector stores, and prompt-templated chat models in one package.

The decision is provisional.
The `Supervisor` abstract class in `supervisor.py` provides a framework-agnostic interface (`answer_question`, `review_submission`), so the LangChain implementation can be swapped out without changing callers.

Revisit conditions:
- Latency requirements make the LangChain overhead unacceptable for deterministic replay.
- The project needs offline-first evaluation (no network calls during scoring).
- A significantly simpler or cheaper alternative emerges after the first scenario ships.

Vector-store choice (Chroma, FAISS, pgvector, or cloud-managed) is deferred until the first scenario needs document indexing.

## Consequences

- `pyproject.toml` adds `langchain>=0.3` and `langchain-anthropic>=0.3` as runtime dependencies.
- `supervisor.py` declares `LangChainSupervisor(Supervisor)` as a scaffolding class; the body is stubbed until the supervisor implementation issue is opened.
- No LangChain-specific code is written until that issue ships, so the current scaffold has no concrete LangChain API calls.
