# subsea-bench

A benchmark for evaluating AI coding agents on long-horizon subsea engineering tasks.

## Status

Pre-v0.1 scaffolding. Not ready for use.

## What it is

`subsea-bench` evaluates AI coding agents (Claude Code, Gemini CLI, and similar tools) on the task of designing a mooring system for a floating offshore wind turbine.
Agents use a set of MCP tools to interact with a simulated engineering project, then are scored on the economic efficiency of their process and the quality of their proposed design.

The benchmark is conceptually similar to Vending-Bench and tau-bench but targets the offshore engineering domain, where no benchmark currently exists.

## What it is not

This is not a production engineering tool and its outputs should not be used for any real design or safety-critical decision.
The simulated firm (Devana Subsea) is fictional.
All reference data is simplified for benchmark purposes and does not constitute engineering advice.

## License

GPL-3.0-or-later. See [LICENSE](LICENSE) for details.
