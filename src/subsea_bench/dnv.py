"""DNV-OS-E301 (July 2018) mooring code utility functions.

Provides characteristic capacity, utilization, and MBL lookup helpers that
the analysis layer uses to verify mooring designs against the DNV standard.

Reference: DNV-OS-E301 Position Mooring, Edition July 2018.
"""


def characteristic_capacity(mbl_kn: float, safety_factor: float) -> float:
    """Return the characteristic mooring line capacity per DNV-OS-E301 Section 4.

    mbl_kn: minimum breaking load of the line in kN.
    safety_factor: consequence-class-dependent partial factor (e.g. 3.0 for CC2 ULS-a).
    """
    raise NotImplementedError


def ulsd_utilization(tension_kn: float, mbl_kn: float, safety_factor: float) -> float:
    """Compute ULS-d utilization ratio per DNV-OS-E301 Table 4-1.

    Returns tension / (mbl / safety_factor). Must be <= 1.0 to pass.
    """
    raise NotImplementedError


def mbl_studless(grade: str, diameter_mm: float) -> float:
    """Return the catalogue MBL (kN) for studless chain of the given grade and diameter.

    grade: one of R3, R3S, R4, R4S, R5.
    diameter_mm: nominal chain diameter in millimetres.

    Per DNV-OS-E301 Appendix A, Table A-1.
    """
    raise NotImplementedError
