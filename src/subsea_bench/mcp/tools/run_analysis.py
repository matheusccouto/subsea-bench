"""MCP tool: run_analysis.

Contract: Execute a Python analysis script (quasi-static mooring analysis).
The script runs in a sandboxed subprocess with MoorPy available.
Output must be JSON-serialisable and conform to AnalysisResult.

Cost: ANALYSIS_FEE per call (see config.py).
Sim-time advancement: 0.25 simulated days per call.
"""

from subsea_bench.models import AnalysisResult


async def run_analysis(script: str) -> AnalysisResult:
    """MCP tool handler: run an analysis script and return structured results."""
    raise NotImplementedError
