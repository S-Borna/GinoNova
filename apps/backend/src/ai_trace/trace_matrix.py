"""
PHASE 7.15 — AI Trace Matrix

Provides static, deterministic mapping of AI engine dependencies.
This matrix defines which sub-engines each service relies on.
"""
from typing import Any


# Static trace matrix - deterministic mapping of engine dependencies
_TRACE_MATRIX: dict[str, list[str]] = {
    "recommendation_service": ["pattern_engine", "modules_engine", "tasks_engine"],
    "summary_service": ["studyflow_engine", "progress_engine"],
    "next_step_service": ["recommendation_service", "difficulty_engine"],
    "difficulty_service": ["tasks_engine"],
}


def get_trace_matrix() -> dict[str, Any]:
    """
    Get the static AI engine dependency trace matrix.

    Returns a deterministic mapping showing which sub-engines
    each AI service depends on for its computations.

    Returns:
        Dict with:
        - matrix: The dependency mapping
        - version: Matrix version for tracking changes
        - engines: List of all tracked engines
    """
    return {
        "matrix": _TRACE_MATRIX,
        "version": "7.15.0",
        "engines": sorted(_TRACE_MATRIX.keys()),
        "total_dependencies": sum(len(deps) for deps in _TRACE_MATRIX.values()),
    }


def get_dependencies(engine_name: str) -> list[str]:
    """
    Get dependencies for a specific engine.

    Args:
        engine_name: Name of the engine to look up

    Returns:
        List of dependency engine names, empty if not found
    """
    return _TRACE_MATRIX.get(engine_name, [])
