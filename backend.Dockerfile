FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry==1.8.3

# Copy shared python package (build context is repo root)
COPY packages/shared/python ./packages/shared/python

# Copy dependency files from backend directory
COPY apps/backend/pyproject.toml apps/backend/poetry.lock ./

# Fix shared package path for Docker context (../../packages -> ./packages)
RUN sed -i 's|path = "../../packages/shared/python"|path = "./packages/shared/python"|' pyproject.toml

# Install dependencies (no virtualenv, install to system)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

# Copy application code
COPY apps/backend/src ./src

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Start command (Railway overrides this via Custom Start Command)
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
