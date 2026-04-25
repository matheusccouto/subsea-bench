"""MCP tool: ask_supervisor.

Contract: Submit a natural-language question to the Devana Subsea supervisor.
The supervisor answers based on project scope and technical domain knowledge.

Cost: QUESTION_FEE per call (see config.py).
Sim-time advancement: 0.5 simulated days per call.
"""

from subsea_bench.models import SupervisorResponse


async def ask_supervisor(question: str) -> SupervisorResponse:
    """MCP tool handler: route a question to the supervisor and return the answer."""
    raise NotImplementedError
