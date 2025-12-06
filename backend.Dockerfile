FROM python:3.11-slim

# Build version to invalidate cache: 2025-12-06-v2
WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip && pip install poetry==1.8.3

# Copy shared python package (preserving relative structure for pyproject.toml path)
COPY packages/shared/python /app/packages/shared/python

# Copy backend directory (preserving structure so ../../packages/shared/python resolves)
COPY apps/backend /app/apps/backend

# Set working directory to backend for Poetry
WORKDIR /app/apps/backend

# Install dependencies with Poetry (no virtualenv, install to system)
# The path "../../packages/shared/python" now correctly resolves to /app/packages/shared/python
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

# Set PYTHONPATH for module imports
ENV PYTHONPATH="/app/apps/backend:${PYTHONPATH}"

# Make startup script executable
RUN chmod +x /app/apps/backend/scripts/start.sh

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port (Railway sets $PORT dynamically)
EXPOSE 8000

# Start command - uses startup script that runs migrations first
CMD ["bash", "/app/apps/backend/scripts/start.sh"]
