# -----------------------------
# Stage 1: Build environment
# -----------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry==1.8.3

# Copy project files
COPY pyproject.toml .
COPY poetry.lock .
COPY src ./src

# Install dependencies (no dev)
RUN poetry install --no-root --only main --no-interaction --no-ansi

# -----------------------------
# Stage 2: Production image
# -----------------------------
FROM python:3.11-slim AS runtime

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

# Copy built environment from builder
COPY --from=builder /app /app

# Expose port
EXPOSE 8000

# HEALTHCHECK for Railway, Netlify Edge, ECS, etc
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8000/health || exit 1

# Run as non-root
USER appuser

# Start FastAPI using Uvicorn in production mode
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
