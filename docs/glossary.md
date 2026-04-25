# Glossary

Domain terms used in the subsea-bench codebase and documentation.

**ALS** (Accidental Limit State): Design condition accounting for accidental events such as line breakage.
DNV-OS-E301 requires ALS checks with one line missing.

**AGENTS.md**: Root-level file read by AI coding agents at the start of every session.
Contains project context, workflow instructions, and pointers to detailed documentation.

**BOM** (Bill of Materials): The agent's proposed list of mooring hardware items with quantities and costs.
Used for CAPEX Efficiency scoring.

**Catenary mooring**: A mooring configuration where lines hang under their own weight between the fairlead and the anchor, providing restoring force through geometry and weight rather than elasticity alone.

**CC1 / CC2** (Consequence Class 1 / 2): DNV safety classification based on the consequence of a mooring failure.
CC2 applies to manned structures and carries higher partial safety factors than CC1.

**CAPEX Efficiency**: One of the two benchmark scoring metrics.
Ratio of reference CAPEX to the agent's proposed CAPEX, capped at 1.0.
See `docs/architecture.md`.

**Devana Subsea**: The fictional boutique subsea engineering consultancy based in Aberdeen, used in all benchmark scenarios.
Not a real company.
The agent is deployed as an AI assistant there.

**DLC** (Design Load Case): A specific combination of environmental conditions and operational state used in a structural or mooring analysis.

**DNV-OS-E301**: DNV standard "Position Mooring", July 2018 edition.
The normative reference for mooring safety factors and chain capacity in this benchmark.

**Engineering Margin (EM)**: One of the two benchmark scoring metrics.
Realized project margin divided by contract value.
See `docs/architecture.md`.

**Fairlead**: The attachment point on the floating structure where a mooring line connects.
Defines the upper end of the catenary.

**FLS** (Fatigue Limit State): Design condition assessing cumulative fatigue damage over the structure's service life.

**FOWT** (Floating Offshore Wind Turbine): A wind turbine mounted on a floating substructure (spar, semi-submersible, or TLP) and moored to the seabed.

**Grade** (R3, R3S, R4, R4S, R5): Steel grades for studless chain, in increasing order of minimum breaking load.
Defined in DNV-OS-E301 Appendix A.

**IEA-15MW**: The IEA Wind 15 MW offshore reference turbine.
Used as the benchmark turbine for all v0.1 scenarios.
Public reference: https://github.com/IEAWindTask37/IEA-15-240-RWT

**MBL** (Minimum Breaking Load): The guaranteed minimum tensile strength of a mooring line component, in kilonewtons (kN).

**MoorPy**: Open-source Python library for quasi-static mooring analysis.
Repository: https://github.com/NREL/MoorPy

**Mooring line**: A line (chain, wire, or rope) connecting a floating structure to its anchor on the seabed.
Provides station-keeping restoring force.

**Pretension**: The static tension in a mooring line at mean environmental conditions with no applied offset.

**Quasi-static analysis**: Mooring analysis method that computes restoring forces and tensions at a series of static offsets, ignoring inertia and damping effects.
Fast but conservative relative to dynamic methods.

**Review round**: One invocation of `submit_for_review`.
Each round costs REVIEW_FEE and advances sim time.
The supervisor returns a verdict (approved / rejected / conditional).

**Safety factor**: A divisor applied to MBL to obtain the allowable tension.
Depends on limit state (ULS/ALS/FLS) and consequence class.
See DNV-OS-E301 Table 4-1.

**Scenario**: A complete task definition for the benchmark, including site conditions, turbine specification, task brief, and reference answers.
Scenario structure is not yet defined (deferred past scaffolding).

**Scope change**: Any deviation from the task brief initiated by the agent without supervisor approval.
Penalised in the review process.

**Studless chain**: Chain without stud links.
Standard for modern permanent mooring systems.
Characterised by its grade and nominal diameter.

**Supervisor**: The LLM-backed client representative at Devana Subsea.
Answers the agent's technical questions and reviews design submissions.
Implemented in `supervisor.py`.

**ULS** (Ultimate Limit State): Design condition for extreme loading.
DNV-OS-E301 ULS-a and ULS-d conditions are the primary checks for mooring lines.

**VolturnUS-S**: A semi-submersible FOWT platform from the University of Maine.
One candidate platform type for v0.1 scenarios.

**Workspace**: The isolated filesystem directory given to the agent for a benchmark run.
Contains the task brief, site data, and reference documents.
Not tracked in the repo.
