"""Pydantic v2 data models for subsea-bench.

These models define the data exchange surface between the MCP tools, the
supervisor, the workspace, and the scoring engine. No business logic here.
"""

from decimal import Decimal
from enum import StrEnum

from pydantic import BaseModel, Field


class ReviewVerdictKind(StrEnum):
    """Outcome of a supervisor review round."""

    APPROVED = "approved"
    REJECTED = "rejected"
    CONDITIONAL = "conditional"


class LedgerState(StrEnum):
    """Lifecycle state of the project ledger."""

    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class CostCategory(StrEnum):
    """Category of a ledger charge."""

    REVIEW = "review"
    QUESTION = "question"
    ANALYSIS = "analysis"
    PM_OVERHEAD = "pm_overhead"
    LATE_PENALTY = "late_penalty"


class CatalogItem(BaseModel):
    """A single item in the equipment catalog."""

    id: str
    description: str
    grade: str
    diameter_mm: float
    mbl_kn: float
    mass_per_metre_kg: float
    unit_cost_usd: Decimal


class BOMLine(BaseModel):
    """One line of a bill of materials."""

    catalog_id: str
    quantity: float
    unit: str
    unit_cost_usd: Decimal
    total_cost_usd: Decimal


class BOM(BaseModel):
    """Bill of materials for the proposed mooring system."""

    lines: list[BOMLine] = Field(default_factory=list)
    total_cost_usd: Decimal = Decimal(0)


class AnalysisResult(BaseModel):
    """Output of a quasi-static mooring analysis run."""

    utilization_max: float
    utilization_by_line: list[float]
    offset_m: float
    passed: bool
    notes: str = ""


class ReviewVerdict(BaseModel):
    """Supervisor verdict on a submitted design."""

    kind: ReviewVerdictKind
    comments: str
    round_number: int


class SupervisorResponse(BaseModel):
    """Supervisor answer to a technical question."""

    answer: str
    sim_time_advanced_days: float


class ProjectStatus(BaseModel):
    """Snapshot of the project's current state."""

    sim_day: float
    ledger_state: LedgerState
    margin_usd: Decimal
    review_rounds_used: int
    questions_asked: int
    analyses_run: int


class LedgerEntry(BaseModel):
    """A single debit recorded in the project ledger."""

    sim_day: float
    category: CostCategory
    amount_usd: Decimal
    description: str


class Ledger(BaseModel):
    """Complete project ledger: tracks time, charges, and lifecycle state."""

    state: LedgerState = LedgerState.ACTIVE
    sim_day: float = 0.0
    entries: list[LedgerEntry] = Field(default_factory=list)
    contract_value_usd: Decimal = Decimal(0)


class FinalScore(BaseModel):
    """Composite benchmark score for a completed run."""

    engineering_margin: float
    capex_efficiency: float
    composite_score: float
    sim_day_completed: float
    run_id: str
