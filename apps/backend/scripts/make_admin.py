#!/usr/bin/env python3
"""
Make a user admin by email
Usage: python make_admin.py email@example.com
"""
import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from src.core.settings import settings

def make_admin(email: str):
    """Set is_admin=True for the given email"""
    database_url = settings.database_url
    if not database_url:
        print("ERROR: DATABASE_URL not configured")
        return False

    engine = create_engine(database_url)

    with engine.connect() as conn:
        # Check if user exists
        result = conn.execute(
            text("SELECT id, email, is_admin FROM users WHERE email = :email"),
            {"email": email}
        )
        row = result.fetchone()

        if not row:
            print(f"ERROR: User with email '{email}' not found")
            return False

        user_id, user_email, is_admin = row

        if is_admin:
            print(f"User '{user_email}' is already an admin")
            return True

        # Make admin
        conn.execute(
            text("UPDATE users SET is_admin = true WHERE email = :email"),
            {"email": email}
        )
        conn.commit()

        print(f"SUCCESS: User '{user_email}' is now an admin!")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_admin.py email@example.com")
        sys.exit(1)

    email = sys.argv[1]
    success = make_admin(email)
    sys.exit(0 if success else 1)
