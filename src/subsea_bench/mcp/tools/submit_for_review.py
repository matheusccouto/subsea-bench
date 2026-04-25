"""MCP tool: submit_for_review.

Contract: Submit the agent's current design for a supervisor review round.
The supervisor evaluates the submission against scope and code requirements
and returns a verdict (approved / rejected / conditional).

Cost: REVIEW_FEE per call (see config.py).
Sim-time advancement: 2.0 simulated days per call.
"""

from subsea_bench.models import ReviewVerdict


async def submit_for_review(submission: str) -> ReviewVerdict:
    """MCP tool handler: submit design text for supervisor review."""
    raise NotImplementedError
