FROM python:3.11-slim

WORKDIR /app

# Install build tools
RUN pip install --upgrade pip

# Copy shared python package first (build context is repo root)
COPY packages/shared/python /app/packages/shared/python

# Install shared package
RUN pip install /app/packages/shared/python

# Copy backend requirements and install dependencies
COPY apps/backend/requirements.txt /app/backend/requirements.txt
RUN pip install -r /app/backend/requirements.txt

# Copy backend application
COPY apps/backend /app/backend

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
