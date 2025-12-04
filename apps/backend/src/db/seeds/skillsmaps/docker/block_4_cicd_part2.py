# =============================================================================
# DOCKER MASTERY V3 - BLOCK 4 PART 2: OPTIMIZATION & HEALTHCHECKS
# Noder 15-16 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 4 PART 2 - OPTIMIZATION
====================================
Node 15: Build Optimization - Fast & Efficient
Node 16: Healthchecks - Reliability
"""

NODE_15 = {
    "id": "docker_node_15",
    "title": "Build Optimization - Fast & Efficient",
    "slug": "build-optimization-fast-efficient",
    "content": r'''# ⚡ Build Optimization

## 1. Introduktion & Kontext

Optimerade Docker builds reducerar CI/CD tid dramatiskt. Denna guide täcker avancerade tekniker för snabbare och effektivare builds.

### Optimization Impact

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BUILD OPTIMIZATION IMPACT                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  BEFORE OPTIMIZATION:                                                    │
│  ─────────────────────────────────────────────────────────────────────  │
│  Build time: 15 minutes                                                  │
│  Image size: 1.2 GB                                                      │
│  Cache hits: 20%                                                         │
│                                                                          │
│  AFTER OPTIMIZATION:                                                     │
│  ─────────────────────────────────────────────────────────────────────  │
│  Build time: 2 minutes (87% reduction)                                   │
│  Image size: 150 MB (88% reduction)                                      │
│  Cache hits: 85%                                                         │
│                                                                          │
│  OPTIMIZATION TECHNIQUES:                                                │
│  ─────────────────────────────────────────────────────────────────────  │
│  ┌────────────────────┬──────────────┬────────────────────────────┐    │
│  │ Technique          │ Impact       │ Implementation             │    │
│  ├────────────────────┼──────────────┼────────────────────────────┤    │
│  │ Layer ordering     │ 50% faster   │ Dependencies first         │    │
│  │ Multi-stage        │ 80% smaller  │ Build vs runtime           │    │
│  │ BuildKit cache     │ 70% faster   │ --mount=type=cache         │    │
│  │ .dockerignore      │ 30% faster   │ Exclude unnecessary        │    │
│  │ Parallel builds    │ 40% faster   │ Buildx bake                │    │
│  └────────────────────┴──────────────┴────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. BuildKit Features

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# ENABLE BUILDKIT
# ═══════════════════════════════════════════════════════════════════════

# Environment variable
export DOCKER_BUILDKIT=1

# Or in /etc/docker/daemon.json
{
  "features": {
    "buildkit": true
  }
}

# ═══════════════════════════════════════════════════════════════════════
# CACHE MOUNTS - Package managers
# ═══════════════════════════════════════════════════════════════════════

# syntax=docker/dockerfile:1.4
FROM python:3.11-slim

# Cache pip downloads
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Cache apt downloads
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update && apt-get install -y curl

# ═══════════════════════════════════════════════════════════════════════
# NODE.JS CACHE MOUNT
# ═══════════════════════════════════════════════════════════════════════

# syntax=docker/dockerfile:1.4
FROM node:20-slim

WORKDIR /app
COPY package*.json ./

# Cache npm
RUN --mount=type=cache,target=/root/.npm \
    npm ci

COPY . .
RUN npm run build
```

## 3. Layer Optimization

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# OPTIMAL LAYER ORDER
# ═══════════════════════════════════════════════════════════════════════

# syntax=docker/dockerfile:1.4
FROM python:3.11-slim AS base

# 1. System dependencies (changes rarely)
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Python dependencies (changes sometimes)
WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# 3. Application code (changes often)
COPY . .

# ═══════════════════════════════════════════════════════════════════════
# MINIMIZE LAYERS
# ═══════════════════════════════════════════════════════════════════════

# BAD: Multiple layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean

# GOOD: Single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

## 4. Parallel Builds

```yaml
# ═══════════════════════════════════════════════════════════════════════
# DOCKER BAKE - Parallel builds
# ═══════════════════════════════════════════════════════════════════════

# docker-bake.hcl
group "default" {
  targets = ["api", "frontend", "worker"]
}

target "api" {
  dockerfile = "api/Dockerfile"
  tags = ["myapp/api:latest"]
  cache-from = ["type=registry,ref=myapp/api:cache"]
  cache-to = ["type=registry,ref=myapp/api:cache,mode=max"]
}

target "frontend" {
  dockerfile = "frontend/Dockerfile"
  tags = ["myapp/frontend:latest"]
  cache-from = ["type=registry,ref=myapp/frontend:cache"]
  cache-to = ["type=registry,ref=myapp/frontend:cache,mode=max"]
}

target "worker" {
  dockerfile = "worker/Dockerfile"
  tags = ["myapp/worker:latest"]
  cache-from = ["type=registry,ref=myapp/worker:cache"]
  cache-to = ["type=registry,ref=myapp/worker:cache,mode=max"]
}
```

```bash
# Build all in parallel
docker buildx bake

# Build specific targets
docker buildx bake api frontend

# With push
docker buildx bake --push
```

## 5. Remote Cache

```bash
# ═══════════════════════════════════════════════════════════════════════
# REGISTRY CACHE
# ═══════════════════════════════════════════════════════════════════════

# Build with registry cache
docker buildx build \
  --cache-from type=registry,ref=myregistry/myapp:cache \
  --cache-to type=registry,ref=myregistry/myapp:cache,mode=max \
  --push \
  -t myregistry/myapp:latest .

# ═══════════════════════════════════════════════════════════════════════
# GITHUB ACTIONS CACHE
# ═══════════════════════════════════════════════════════════════════════

# GHA cache (free, fast)
- uses: docker/build-push-action@v5
  with:
    cache-from: type=gha
    cache-to: type=gha,mode=max

# ═══════════════════════════════════════════════════════════════════════
# S3 CACHE
# ═══════════════════════════════════════════════════════════════════════

docker buildx build \
  --cache-from type=s3,region=eu-west-1,bucket=my-cache \
  --cache-to type=s3,region=eu-west-1,bucket=my-cache,mode=max \
  -t myapp:latest .
```

## 6. Optimized Python Build

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# OPTIMIZED PYTHON DOCKERFILE
# ═══════════════════════════════════════════════════════════════════════

# syntax=docker/dockerfile:1.4

# Build stage
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install build dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev

# Create venv and install dependencies
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Production stage
FROM python:3.11-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r app && useradd -r -g app app

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY --chown=app:app . .

USER app
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

## 7-14. Sammanfattning

### Optimization Techniques

| Technique | Command | Impact |
|-----------|---------|--------|
| BuildKit | DOCKER_BUILDKIT=1 | 50%+ faster |
| Cache mount | --mount=type=cache | Persistent cache |
| Registry cache | --cache-from | Shared cache |
| Parallel | buildx bake | Multi-image |

---

**Nasta Node:** Healthchecks →
''',
    "xp_reward": 170,
    "estimated_minutes": 70,
    "prerequisites": ["docker_node_14"],
    "learning_outcomes": [
        "Anvanda BuildKit features",
        "Optimera layer caching",
        "Konfigurera remote cache",
        "Parallella builds"
    ]
}

NODE_16 = {
    "id": "docker_node_16",
    "title": "Healthchecks - Reliability",
    "slug": "healthchecks-reliability",
    "content": r'''# 💓 Docker Healthchecks

## 1. Introduktion & Kontext

Healthchecks gor det mojligt for Docker att overvaka container-halsa och automatiskt hantera ohalsosamma containers i orchestration.

### Healthcheck States

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CONTAINER HEALTH STATES                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                       Container Start                                    │
│                            │                                             │
│                            ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                       STARTING                                   │   │
│  │               (Within start_period)                              │   │
│  │                                                                  │   │
│  │  Healthcheck runs but failures dont count                       │   │
│  └────────────────────────┬────────────────────────────────────────┘   │
│                           │                                             │
│              First successful check                                     │
│                           │                                             │
│                           ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                       HEALTHY                                    │   │
│  │                                                                  │   │
│  │  Healthcheck passes - container operational                     │   │
│  └─────┬──────────────────────────────────────────────────┬────────┘   │
│        │                                                  │             │
│   Check passes                                   retries failures      │
│        │                                                  │             │
│        ▼                                                  ▼             │
│  ┌──────────┐                                    ┌──────────────────┐  │
│  │ HEALTHY  │◄───────────────────────────────────│   UNHEALTHY      │  │
│  │          │        Check passes again          │                  │  │
│  └──────────┘                                    │  Orchestrator    │  │
│                                                  │  may restart     │  │
│                                                  └──────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Dockerfile HEALTHCHECK

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# BASIC HEALTHCHECK
# ═══════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# ... app setup ...

HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

# ═══════════════════════════════════════════════════════════════════════
# FULL OPTIONS
# ═══════════════════════════════════════════════════════════════════════

HEALTHCHECK \
    --interval=30s \
    --timeout=10s \
    --start-period=60s \
    --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Options explained:
# --interval    Time between checks (default: 30s)
# --timeout     Max time for check to complete (default: 30s)
# --start-period  Grace period at startup (default: 0s)
# --retries     Consecutive failures before unhealthy (default: 3)

# ═══════════════════════════════════════════════════════════════════════
# DISABLE HEALTHCHECK
# ═══════════════════════════════════════════════════════════════════════

HEALTHCHECK NONE
```

## 3. Healthcheck Commands

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# HTTP HEALTHCHECKS
# ═══════════════════════════════════════════════════════════════════════

# Using curl
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

# Using wget (alpine)
HEALTHCHECK CMD wget --no-verbose --tries=1 --spider http://localhost:8000/health || exit 1

# ═══════════════════════════════════════════════════════════════════════
# DATABASE HEALTHCHECKS
# ═══════════════════════════════════════════════════════════════════════

# PostgreSQL
HEALTHCHECK CMD pg_isready -U postgres || exit 1

# MySQL
HEALTHCHECK CMD mysqladmin ping -h localhost || exit 1

# Redis
HEALTHCHECK CMD redis-cli ping || exit 1

# MongoDB
HEALTHCHECK CMD mongosh --eval "db.adminCommand('ping')" || exit 1

# ═══════════════════════════════════════════════════════════════════════
# CUSTOM HEALTHCHECKS
# ═══════════════════════════════════════════════════════════════════════

# Python script
HEALTHCHECK CMD python /app/healthcheck.py || exit 1

# Node.js
HEALTHCHECK CMD node /app/healthcheck.js || exit 1

# Check file exists
HEALTHCHECK CMD test -f /app/ready || exit 1
```

## 4. Compose Healthchecks

```yaml
# ═══════════════════════════════════════════════════════════════════════
# DOCKER COMPOSE HEALTHCHECK
# ═══════════════════════════════════════════════════════════════════════

services:
  api:
    image: myapi:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

# ═══════════════════════════════════════════════════════════════════════
# DEPENDS_ON WITH HEALTHCHECK
# ═══════════════════════════════════════════════════════════════════════

services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
```

## 5. Healthcheck Endpoint Examples

```python
# ═══════════════════════════════════════════════════════════════════════
# PYTHON/FASTAPI HEALTH ENDPOINT
# ═══════════════════════════════════════════════════════════════════════

from fastapi import FastAPI, Response
import asyncpg
import aioredis

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/health/ready")
async def readiness():
    # Check dependencies
    try:
        # Database
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.execute("SELECT 1")
        await conn.close()

        # Redis
        redis = await aioredis.from_url(REDIS_URL)
        await redis.ping()
        await redis.close()

        return {"status": "ready"}
    except Exception as e:
        return Response(
            content=f"Not ready: {str(e)}",
            status_code=503
        )

@app.get("/health/live")
async def liveness():
    # Simple check - app is running
    return {"status": "alive"}
```

```javascript
// ═══════════════════════════════════════════════════════════════════════
// NODE.JS/EXPRESS HEALTH ENDPOINT
// ═══════════════════════════════════════════════════════════════════════

const express = require('express');
const app = express();

// Liveness - app is running
app.get('/health/live', (req, res) => {
  res.json({ status: 'alive' });
});

// Readiness - dependencies OK
app.get('/health/ready', async (req, res) => {
  try {
    // Check database
    await db.query('SELECT 1');

    // Check Redis
    await redis.ping();

    res.json({ status: 'ready' });
  } catch (error) {
    res.status(503).json({
      status: 'not ready',
      error: error.message
    });
  }
});

// Combined
app.get('/health', async (req, res) => {
  try {
    await db.query('SELECT 1');
    res.json({ status: 'healthy' });
  } catch (error) {
    res.status(503).json({ status: 'unhealthy' });
  }
});
```

## 6. Monitoring Health

```bash
# ═══════════════════════════════════════════════════════════════════════
# CHECK HEALTH STATUS
# ═══════════════════════════════════════════════════════════════════════

# Se health status
docker ps
# CONTAINER ID  IMAGE   STATUS
# abc123        myapp   Up 5 min (healthy)
# def456        myapp   Up 3 min (unhealthy)

# Detaljerad health info
docker inspect --format='{{json .State.Health}}' myapp | jq

# Output:
# {
#   "Status": "healthy",
#   "FailingStreak": 0,
#   "Log": [
#     {
#       "Start": "2024-01-15T10:00:00Z",
#       "End": "2024-01-15T10:00:01Z",
#       "ExitCode": 0,
#       "Output": "OK"
#     }
#   ]
# }

# Filter by health
docker ps --filter "health=healthy"
docker ps --filter "health=unhealthy"

# Watch health changes
docker events --filter event=health_status
```

## 7-14. Sammanfattning

### Healthcheck Best Practices

| Practice | Implementation |
|----------|----------------|
| Set start_period | Allow startup time |
| Use dependencies | depends_on: condition |
| Separate endpoints | /live, /ready, /health |
| Check dependencies | DB, cache, services |

---

**Nasta Node:** Docker Swarm →
''',
    "xp_reward": 165,
    "estimated_minutes": 65,
    "prerequisites": ["docker_node_15"],
    "learning_outcomes": [
        "Konfigurera healthchecks",
        "Implementera health endpoints",
        "Anvanda depends_on conditions",
        "Overvaka container halsa"
    ]
}

# Block 4 Part 2 exports
BLOCK_4_PART_2_NODES = [NODE_15, NODE_16]

__all__ = ["NODE_15", "NODE_16", "BLOCK_4_PART_2_NODES"]
