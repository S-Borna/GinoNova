#!/usr/bin/env python3
"""
Seed Tasks to Production Database
==================================
This script adds tasks to existing modules that have 0 tasks.
It does NOT create new modules or modify existing tasks.

Safe to run multiple times - it skips modules that already have tasks.

Usage:
    DATABASE_URL=postgresql://... python scripts/seed_tasks_to_prod.py
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Import v3 modules data
from src.db.seeds.modules_v3 import ALL_V3_MODULES


def get_database_url():
    """Get database URL from environment."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        print("❌ DATABASE_URL not set")
        sys.exit(1)
    return url


def seed_tasks():
    """Seed tasks to existing modules."""
    db_url = get_database_url()

    # Handle Railway's postgres:// vs postgresql://
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    print(f"🔗 Connecting to database...")
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get existing modules from database
        result = session.execute(text("SELECT id, slug, name FROM modules"))
        db_modules = {row[1]: {"id": row[0], "name": row[2]} for row in result}

        print(f"📦 Found {len(db_modules)} modules in database")

        # Build lookup from v3 data
        v3_data = {m["slug"]: m for m in ALL_V3_MODULES}

        modules_updated = 0
        tasks_created = 0

        for slug, db_module in db_modules.items():
            module_id = db_module["id"]
            module_name = db_module["name"]

            # Check if module already has tasks
            task_count = session.execute(
                text("SELECT COUNT(*) FROM tasks WHERE module_id = :mid"),
                {"mid": module_id}
            ).scalar()

            if task_count > 0:
                print(f"⏭️  {module_name}: Already has {task_count} tasks, skipping")
                continue

            # Find matching v3 data
            v3_module = v3_data.get(slug)
            if not v3_module:
                # Try to find by name match
                for v3_slug, v3_mod in v3_data.items():
                    if v3_mod["name"].lower() == module_name.lower():
                        v3_module = v3_mod
                        break

            if not v3_module or not v3_module.get("tasks"):
                print(f"⚠️  {module_name}: No v3 data found")
                continue

            # Insert tasks
            for idx, task in enumerate(v3_module["tasks"]):
                session.execute(
                    text("""
                        INSERT INTO tasks (module_id, title, description, content, order_index,
                                          difficulty, estimated_minutes, xp_reward)
                        VALUES (:module_id, :title, :description, :content, :order_index,
                                :difficulty, :estimated_minutes, :xp_reward)
                    """),
                    {
                        "module_id": module_id,
                        "title": task.get("title", f"Task {idx + 1}"),
                        "description": task.get("description", ""),
                        "content": task.get("content", ""),
                        "order_index": idx + 1,
                        "difficulty": task.get("difficulty", "medium"),
                        "estimated_minutes": task.get("estimated_minutes", 30),
                        "xp_reward": task.get("xp_reward", 50),
                    }
                )
                tasks_created += 1

            modules_updated += 1
            print(f"✅ {module_name}: Added {len(v3_module['tasks'])} tasks")

        session.commit()
        print(f"\n🎉 Done! Updated {modules_updated} modules, created {tasks_created} tasks")

    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed_tasks()
