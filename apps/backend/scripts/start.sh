#!/bin/bash
# Backend Startup Script - Runs migrations before starting Uvicorn
# This ensures database schema is up-to-date on every deploy

set -e

echo "🚀 DevOps Hub Backend Startup"
echo "=============================="

# Ensure we're in the right directory
cd /app/apps/backend

# Check if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
    echo "🗄️  PostgreSQL detected - running Alembic migrations..."

    # Run Alembic migrations using python -m to ensure it's found
    python -m alembic upgrade head || {
        echo "⚠️  Alembic migration failed, trying init_db fallback..."
        python -c "from src.db.database import init_db; init_db()"
    }

    echo "✅ Database migrations complete!"

    # =========================================================================
    # AUTOMATIC V3 SKILLSMAPS SEEDING
    # Ensures modules and tasks are always populated after deploy
    # =========================================================================
    echo "🌱 Running V3 SkillsMaps seed (idempotent - safe to run multiple times)..."
    python -c "
from src.db.database import get_db
from src.api.admin import seed_skillsmaps_v3_internal
from src.db.seeds.modules_v3 import get_total_tasks

# Check if seeding is needed by counting tasks in V3 data
total_v3_tasks = get_total_tasks()
print(f'📊 V3 SkillsMaps contains {total_v3_tasks} tasks')

# Run idempotent seed
db = next(get_db())
try:
    result = seed_skillsmaps_v3_internal(db)
    print(f'✅ Seed result: {result}')
except Exception as e:
    print(f'⚠️  Seed warning: {e}')
finally:
    db.close()
" || echo "⚠️  V3 Seeding skipped (non-critical)"

    echo "✅ Database setup complete!"
else
    echo "📝 No DATABASE_URL - using in-memory storage"
fi

# Start Uvicorn
echo "🌐 Starting Uvicorn server on port ${PORT:-8000}..."
exec python -m uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level debug
