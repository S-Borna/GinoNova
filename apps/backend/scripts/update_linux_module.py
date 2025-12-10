#!/usr/bin/env python3
"""
Update Linux Module with V3 Content
====================================
Replaces all tasks in the existing linux-mastery module with the new
Swedish pedagogical style content.

Usage:
    DATABASE_URL=postgresql://... python scripts/update_linux_module.py
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Import the new V3 Linux module
from src.db.seeds.modules_v3.module_linux_v3 import MODULE_LINUX_MASTERY_V3


def get_database_url():
    """Get database URL from environment."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        print("❌ DATABASE_URL not set")
        print("   Set it with: export DATABASE_URL=postgresql://...")
        sys.exit(1)
    return url


def update_linux_module():
    """Replace all tasks in linux-mastery with V3 content, or create if not exists."""
    db_url = get_database_url()

    # Handle Railway's postgres:// vs postgresql://
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    print("🔗 Connecting to database...")
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Find the Linux module (try multiple possible slugs)
        linux_slugs = ["linux-mastery", "linux-mastery-v2", "linux"]
        module_id = None
        module_name = None
        found_slug = None

        for slug in linux_slugs:
            result = session.execute(
                text("SELECT id, name FROM modules WHERE slug = :slug"),
                {"slug": slug}
            ).fetchone()
            if result:
                module_id = result[0]
                module_name = result[1]
                found_slug = slug
                break

        if not module_id:
            print("📦 Linux module not found - creating new module...")

            # First ensure track exists
            track_result = session.execute(
                text("SELECT id FROM tracks WHERE slug = 'foundation'")
            ).fetchone()

            if not track_result:
                print("   Creating 'foundation' track...")
                import uuid
                track_uuid = str(uuid.uuid4())
                session.execute(
                    text("""
                        INSERT INTO tracks (id, name, slug, description, color, icon, order_index)
                        VALUES (:id, 'Foundation', 'foundation', 'Core DevOps fundamentals', '#3b82f6', '🏗️', 1)
                    """),
                    {"id": track_uuid}
                )
                session.commit()
                track_result = session.execute(
                    text("SELECT id FROM tracks WHERE slug = 'foundation'")
                ).fetchone()

            track_id = track_result[0]

            # Create the Linux module
            import uuid
            module_uuid = str(uuid.uuid4())
            session.execute(
                text("""
                    INSERT INTO modules (id, track_id, name, slug, description, order_index, difficulty, estimated_hours)
                    VALUES (:id, :track_id, :name, :slug, :desc, 1, 'intermediate', :hours)
                """),
                {
                    "id": module_uuid,
                    "track_id": track_id,
                    "name": MODULE_LINUX_MASTERY_V3["name"],
                    "slug": "linux-mastery",
                    "desc": MODULE_LINUX_MASTERY_V3.get("description", ""),
                    "hours": MODULE_LINUX_MASTERY_V3.get("estimated_hours", 30),
                }
            )
            session.commit()

            result = session.execute(
                text("SELECT id, name FROM modules WHERE slug = 'linux-mastery'")
            ).fetchone()
            module_id = result[0]
            module_name = result[1]
            found_slug = "linux-mastery"
            print(f"   ✅ Created module: {module_name}")

        print(f"✅ Found module: {module_name} (slug: {found_slug}, id: {module_id})")

        # Count existing tasks
        old_count = session.execute(
            text("SELECT COUNT(*) FROM tasks WHERE module_id = :mid"),
            {"mid": module_id}
        ).scalar()
        print(f"📊 Current tasks: {old_count}")

        # Delete all existing tasks for this module
        print("🗑️  Deleting old tasks...")
        session.execute(
            text("DELETE FROM tasks WHERE module_id = :mid"),
            {"mid": module_id}
        )

        # Insert new V3 tasks
        print(f"📝 Inserting {len(MODULE_LINUX_MASTERY_V3['tasks'])} new tasks...")
        import uuid

        new_tasks = MODULE_LINUX_MASTERY_V3["tasks"]
        for idx, task in enumerate(new_tasks, 1):
            task_uuid = str(uuid.uuid4())
            session.execute(
                text("""
                    INSERT INTO tasks (id, module_id, title, description, content, order_index,
                                       difficulty, estimated_minutes, xp_reward)
                    VALUES (:id, :module_id, :title, :description, :content, :order_index,
                            :difficulty, :estimated_minutes, :xp_reward)
                """),
                {
                    "id": task_uuid,
                    "module_id": module_id,
                    "title": task["title"],
                    "description": task.get("description", ""),
                    "content": task.get("content", ""),
                    "order_index": idx,
                    "difficulty": task.get("difficulty", "medium"),
                    "estimated_minutes": task.get("estimated_minutes", 45),
                    "xp_reward": task.get("xp_reward", 75),
                }
            )
            print(f"   ✓ {idx:2}. {task['title']}")

        # Update module metadata
        print("📦 Updating module metadata...")
        session.execute(
            text("""
                UPDATE modules
                SET description = :desc,
                    estimated_hours = :hours
                WHERE id = :mid
            """),
            {
                "mid": module_id,
                "desc": MODULE_LINUX_MASTERY_V3.get("description", ""),
                "hours": MODULE_LINUX_MASTERY_V3.get("estimated_hours", 30),
            }
        )

        # Commit all changes
        session.commit()
        print("\n" + "=" * 55)
        print("✅ SUCCESS! Linux module updated with V3 content!")
        print(f"   📚 Module: {module_name}")
        print(f"   📝 Tasks: {old_count} -> {len(new_tasks)}")
        print("=" * 55)

    except Exception as e:
        session.rollback()
        print(f"\n❌ ERROR: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    print("=" * 55)
    print("🐧 Linux Mastery V3 Update Script")
    print("=" * 55)
    print()
    update_linux_module()
