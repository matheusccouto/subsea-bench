"""Numerical analysis execution sandbox for mooring system evaluations.

The agent submits a Python script (using MoorPy or similar) that is run in a
restricted subprocess.
Results are returned as structured data.
"""

from pathlib import Path

from subsea_bench.models import AnalysisResult


def execute_script(script: str, workspace: Path) -> AnalysisResult:
    """Execute *script* in a sandboxed subprocess within *workspace*.

    The script must write its result to stdout as JSON matching AnalysisResult.
    Returns parsed AnalysisResult on success; raises on timeout or error.
    """
    raise NotImplementedError
