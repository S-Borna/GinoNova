FROM python:3.11-slim

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

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port (Railway sets $PORT dynamically)
EXPOSE 8000

# Start command - shell form for $PORT variable expansion
CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000}
