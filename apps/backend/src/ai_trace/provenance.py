"""
PHASE 7.15 — AI Provenance

Builds provenance frames for AI engine operations.
Includes input/output fingerprints and dependency tracking.
"""
import hashlib
import json
from datetime import datetime
from typing import Any, Optional

from .trace_matrix import get_dependencies


def _compute_fingerprint(data: Any) -> str:
    """
    Compute SHA256 fingerprint of data.

    Args:
        data: Any JSON-serializable data

    Returns:
        SHA256 hex digest string
    """
    try:
        # Sort keys for deterministic output
        json_str = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(json_str.encode("utf-8")).hexdigest()
    except Exception:
        return "fingerprint_error"


def build_provenance_frame(
    engine_name: str,
    context: dict[str, Any],
    output: Optional[dict[str, Any]],
) -> dict[str, Any]:
    """
    Build a provenance frame for an AI engine execution.

    Creates a complete provenance record including:
    - Engine identification
    - Timestamp
    - Input/output fingerprints for verification
    - Dependency chain from trace matrix

    Args:
        engine_name: Name of the engine
        context: Input context dict
        output: Output dict (or None if failed)

    Returns:
        Provenance frame dict
    """
    input_fingerprint = _compute_fingerprint(context) if context else "empty_context"
    output_fingerprint = _compute_fingerprint(output) if output else "no_output"

    return {
        "engine": engine_name,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "input_fingerprint": input_fingerprint,
        "output_fingerprint": output_fingerprint,
        "dependencies": get_dependencies(engine_name),
        "context_keys": sorted(context.keys()) if context else [],
        "output_keys": sorted(output.keys()) if output else [],
    }
