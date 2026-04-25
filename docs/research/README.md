# Research documents

This directory contains research documents produced during issue development.

## Naming convention

`YYYY-MM-DD_<topic>.md`

where `YYYY-MM-DD` is the date the document was produced and `<topic>` is a short kebab-case description of the research question.

Example: `2026-05-01_mooring-analysis-library-comparison.md`

## Structure

Every research document must have the following sections:

```
# Research: <topic>

## Research question
## Summary
## Relevant files
## Findings
## Open questions
## References
```

Keep research documents under 300 lines.
If findings are longer, summarize inline and link to external references.

## Plans

Implementation plans live in the `plans/` subdirectory.
They follow the same naming convention.

## Lifecycle

Research documents are produced during planning and are not deleted after implementation.
They serve as a historical record of why decisions were made and where information was found at the time of the issue.
