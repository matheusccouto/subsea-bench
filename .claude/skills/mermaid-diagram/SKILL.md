---
name: mermaid-diagram
description: Render and verify a Mermaid diagram locally before committing it
triggers:
  - creating a Mermaid diagram
  - modifying a Mermaid diagram
---

# mermaid-diagram

Use this skill whenever you are creating or modifying a Mermaid diagram in any documentation file.

## What to do

1. Write the Mermaid diagram source in the target file (or a temporary `.mmd` file if you prefer to iterate before committing).
2. Render it locally to verify syntax:

```bash
npx -y @mermaid-js/mermaid-cli -i <path-to-file>.mmd -o /tmp/diagram-check.svg
```

3. Check the exit code and stderr output.
   If rendering fails, read the error message, fix the diagram source, and repeat from step 2.
4. Only commit the diagram once the render succeeds cleanly.

## Notes

- `npx -y` downloads `@mermaid-js/mermaid-cli` on first use; no global install needed.
- The output file (`/tmp/diagram-check.svg`) is just for validation and can be discarded.
- Common errors: unclosed quotes in node labels, unsupported syntax in the installed mermaid version, invalid edge syntax. Read the stderr carefully.
- If `npx` is not available, ask the user to install Node.js or run the render step manually.
