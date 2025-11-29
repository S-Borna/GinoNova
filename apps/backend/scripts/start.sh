#!/bin/bash
# Backend Startup Script - Runs migrations before starting Uvicorn
# This ensures database schema is up-to-date on every deploy

set -e

echo "🚀 DevOps Hub Backend Startup"
echo "=============================="

# Check if DATABASE_URL is set
if [ -n "$DATABASE_URL" ]; then
    echo "🗄️  PostgreSQL detected - running Alembic migrations..."

    # Run Alembic migrations
    cd /app/apps/backend
    alembic upgrade head

    echo "✅ Database migrations complete!"
else
    echo "📝 No DATABASE_URL - using in-memory storage"
fi

# Start Uvicorn
echo "🌐 Starting Uvicorn server on port ${PORT:-8000}..."
exec uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level debug
