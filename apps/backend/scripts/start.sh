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

    echo "✅ Database setup complete!"
else
    echo "📝 No DATABASE_URL - using in-memory storage"
fi

# Start Uvicorn
echo "🌐 Starting Uvicorn server on port ${PORT:-8000}..."
exec python -m uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level debug
