"""Agent filesystem workspace provisioning and access utilities.

Each benchmark run gets an isolated workspace directory pre-populated with
the scenario brief, reference documents, and task instructions.
"""

from pathlib import Path


def provision_workspace(run_id: str, base_dir: Path) -> Path:
    """Create and populate an isolated workspace directory for *run_id*.

    Returns the path to the provisioned workspace root.
    """
    raise NotImplementedError


def read_workspace_file(workspace: Path, relative_path: str) -> str:
    """Read and return the text contents of a file inside *workspace*."""
    raise NotImplementedError


def list_workspace(workspace: Path) -> list[str]:
    """Return a sorted list of all relative file paths inside *workspace*."""
    raise NotImplementedError
