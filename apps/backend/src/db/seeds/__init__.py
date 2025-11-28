"""
Seeds Package - Database seed data for development and testing
Bootcamp v3.0: 15 modules, 4 tracks, labs, projects
"""
from .bootcamp_v3_data import (
    get_tracks,
    get_modules,
    get_bootcamp_summary,
)

__all__ = ["get_tracks", "get_modules", "get_bootcamp_summary"]
