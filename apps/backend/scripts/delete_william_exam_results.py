#!/usr/bin/env python3
"""
One-time script to delete William Boström's exam results
Run with: python -m scripts.delete_william_exam_results
"""
import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Get database URL from environment or use default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./devopshub.db")

# Handle Railway PostgreSQL URL format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

def main():
    print(f"Connecting to database...")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Find William Boström's user (use LIKE for SQLite compatibility, ILIKE for PostgreSQL)
        # Check if PostgreSQL or SQLite
        is_postgres = "postgresql" in DATABASE_URL
        
        if is_postgres:
            query = "SELECT id, email, full_name FROM users WHERE full_name ILIKE '%william%' OR email ILIKE '%william%'"
        else:
            query = "SELECT id, email, full_name FROM users WHERE LOWER(full_name) LIKE '%william%' OR LOWER(email) LIKE '%william%'"
        
        result = session.execute(text(query))
        users = result.fetchall()
        
        if not users:
            print("❌ No user found with name containing 'William Boström'")
            # Try to list all users to help debug
            all_users = session.execute(text("SELECT id, email, full_name FROM users LIMIT 20")).fetchall()
            print("\nAvailable users:")
            for u in all_users:
                print(f"  - {u.full_name} ({u.email})")
            return
        
        for user in users:
            user_id = user.id
            print(f"✓ Found user: {user.full_name} ({user.email})")
            print(f"  User ID: {user_id}")
            
            # Count exam results before deletion
            count_result = session.execute(
                text("SELECT COUNT(*) FROM exam_results WHERE user_id = :user_id"),
                {"user_id": user_id}
            )
            count = count_result.scalar()
            print(f"  Exam results to delete: {count}")
            
            if count > 0:
                # Delete exam results
                session.execute(
                    text("DELETE FROM exam_results WHERE user_id = :user_id"),
                    {"user_id": user_id}
                )
                session.commit()
                print(f"✅ Successfully deleted {count} exam result(s) for {user.full_name}")
            else:
                print(f"ℹ️ No exam results found for {user.full_name}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    main()
