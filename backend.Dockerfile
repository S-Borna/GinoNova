FROM python:3.11-slim

WORKDIR /app

# Install build tools (pip-based installation, no Poetry dependency resolution)
RUN pip install --upgrade pip

# Copy shared python package first (build context is repo root)
COPY packages/shared/python /app/packages/shared/python

# Install shared package
RUN pip install /app/packages/shared/python

# Copy backend application
COPY apps/backend /app/backend

# Install backend dependencies directly via pip (bypass Poetry lockfile)
RUN pip install \
    "fastapi>=0.111.0" \
    "uvicorn[standard]>=0.30.0" \
    "pydantic[email]>=2.0.0" \
    "pydantic-settings>=2.2.1" \
    "python-jose[cryptography]>=3.3.0" \
    "bcrypt>=4.0.0"

# Set PYTHONPATH so backend can import src modules
ENV PYTHONPATH="/app/backend:${PYTHONPATH}"

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Set working directory to backend for uvicorn
WORKDIR /app/backend

# Expose port (Railway sets $PORT dynamically)
EXPOSE 8000

# Start command - shell form for $PORT variable expansion
CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8000}
