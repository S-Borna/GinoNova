"""
Seeds Package — Content Source
===============================

All content kommer från: content/
- get_all_modules() → Lista med alla moduler
- get_tracks() → Lista med alla tracks
- get_bootcamp_summary() → Sammanfattning

Gammalt content finns arkiverat i: _archive/
"""
from .content import (
    get_all_modules,
    get_tracks,
    get_bootcamp_summary,
    get_module_by_slug,
    get_total_modules,
    get_total_tasks,
)

# Alias för bakåtkompatibilitet
get_modules = get_all_modules

__all__ = [
    "get_all_modules",
    "get_modules",
    "get_tracks",
    "get_bootcamp_summary",
    "get_module_by_slug",
    "get_total_modules",
    "get_total_tasks",
]
