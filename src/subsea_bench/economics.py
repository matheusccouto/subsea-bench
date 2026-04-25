"""Project economics engine: time advancement and cost accounting.

ProjectLedger tracks simulated time, applies charges from tool use, and
computes engineering margin as the basis for the first scoring metric.
Wraps the ``models.Ledger`` data model with business logic.
"""

from decimal import Decimal

from subsea_bench.models import CostCategory, FinalScore, Ledger, LedgerState, ProjectStatus


class ProjectLedger:
    """Tracks project time, charges, and lifecycle state for one benchmark run."""

    def __init__(self, ledger: Ledger) -> None:
        """Wrap *ledger* with business logic for a single benchmark run."""
        self._ledger = ledger

    def advance_time(self, days: float) -> None:
        """Advance simulated time by *days*, applying PM overhead charges."""
        raise NotImplementedError

    def charge(self, category: CostCategory, amount: Decimal, description: str) -> None:
        """Record a cost charge against the project margin."""
        raise NotImplementedError

    def status(self) -> ProjectStatus:
        """Return a point-in-time snapshot of the project status."""
        raise NotImplementedError

    def current_margin(self) -> Decimal:
        """Return current engineering margin (contract value minus all charges)."""
        raise NotImplementedError

    def complete(self) -> FinalScore:
        """Mark the project completed and produce a partial FinalScore (margin metrics only)."""
        raise NotImplementedError

    def cancel(self, reason: str) -> None:
        """Mark the project cancelled (hard deadline exceeded or fatal error)."""
        raise NotImplementedError

    @property
    def state(self) -> LedgerState:
        """Return the current ledger lifecycle state."""
        raise NotImplementedError
