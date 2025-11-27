"""
In-memory database storage for Phase 1
Will be replaced by PostgreSQL in Phase 2
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..schemas.user import UserInDB

# In-memory user storage: key=email, value=UserInDB
USERS: dict[str, "UserInDB"] = {}


def clear_all():
    """Clear all in-memory data (useful for testing)"""
    USERS.clear()
