"""Scoring engine: computes Engineering Margin and CAPEX Efficiency metrics.

Takes the completed ledger and a reference CAPEX value, and produces a single
composite FinalScore.
The two sub-scores are combined into a weighted composite.
"""

from decimal import Decimal

from subsea_bench.models import BOM, FinalScore, Ledger


def score_run(
    ledger: Ledger,
    proposed_bom: BOM,
    reference_capex_usd: Decimal,
    run_id: str,
) -> FinalScore:
    """Compute the composite benchmark score for a completed run.

    Engineering Margin = realized margin / contract value (higher is better).
    CAPEX Efficiency = reference_capex / proposed_capex (higher is better, capped at 1.0).
    Composite = 0.5 * engineering_margin + 0.5 * capex_efficiency.
    """
    raise NotImplementedError
