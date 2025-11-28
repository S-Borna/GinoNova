"""
Seeds Package - Database seed data for development and testing
"""
from .bootcamp_data import BOOTCAMP_MODULES, get_bootcamp_seed_data

__all__ = ["BOOTCAMP_MODULES", "get_bootcamp_seed_data"]
