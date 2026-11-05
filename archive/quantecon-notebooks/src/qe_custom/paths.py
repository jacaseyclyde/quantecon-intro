from pathlib import Path

DATA_KINDS = {"raw", "processed", "external"}


def project_root() -> Path:
    """Return the repository root path."""
    return Path(__file__).resolve().parents[2]


def data_dir(kind: str) -> Path:
    """Return a data directory by kind."""
    if kind not in DATA_KINDS:
        allowed = ", ".join(sorted(DATA_KINDS))
        msg = f"Unsupported data kind '{kind}'. Expected one of: {allowed}."
        raise ValueError(msg)
    return project_root() / "data" / kind
