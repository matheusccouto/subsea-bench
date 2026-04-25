"""Economic and simulation configuration constants for subsea-bench.

All monetary values use Decimal for exact arithmetic.
"""

from decimal import Decimal

CONTRACT_VALUE: Decimal = Decimal(500000)

REVIEW_FEE: Decimal = Decimal(5000)

QUESTION_FEE: Decimal = Decimal(1000)

ANALYSIS_FEE: Decimal = Decimal(500)

PM_OVERHEAD_PER_DAY: Decimal = Decimal(2000)

# Soft deadline: charges LATE_PENALTY_PER_DAY for each day past this.
DEADLINE_DAYS: int = 30

# Hard deadline: project is cancelled if this day is exceeded regardless of state.
DROP_DEAD_DAY: int = 45

LATE_PENALTY_PER_DAY: Decimal = Decimal(3000)
