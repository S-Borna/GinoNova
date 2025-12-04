# =============================================================================
# DOCKER MASTERY V3 - BLOCK 3 PART 1: BEST PRACTICES & MULTI-STAGE
# Noder 9-10 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 3 PART 1 - OPTIMIZATION
====================================
Node 9: Dockerfile Best Practices - Optimization
Node 10: Multi-stage Builds - Efficient Images
"""

NODE_9 = {
    "id": "docker_node_9",
    "title": "Dockerfile Best Practices - Optimization",
    "slug": "dockerfile-best-practices-optimization",
    "content": r'''# ⚡ Dockerfile Best Practices

## 1. Introduktion & Kontext

Optimerade Dockerfiles resulterar i mindre images, snabbare builds och säkrare containers. Dessa best practices är kritiska för produktion.

### Optimization Pyramid

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   DOCKERFILE OPTIMIZATION PYRAMID                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│                           ┌───────────┐                                  │
│                           │  SECURITY │                                  │
│                           │  Non-root │                                  │
│                           │  Scanning │                                  │
│                         ┌─┴───────────┴─┐                               │
│                         │   EFFICIENCY   │                               │
│                         │  Multi-stage   │                               │
│                         │  .dockerignore │                               │
│                       ┌─┴───────────────┴─┐                             │
│                       │   LAYER CACHING   │                              │
│                       │ Instruction order │                              │
│                       │  Combine RUN cmds │                              │
│                     ┌─┴───────────────────┴─┐                           │
│                     │     BASE IMAGE         │                           │
│                     │  Minimal (alpine/slim) │                           │
│                     │  Specific tags         │                           │
│                     └───────────────────────┘                           │
│                                                                          │
│  IMPACT:                                                                 │
│  ─────────────────────────────────────────────────────────────────────  │
│  Base Image      │ 50-90% size reduction                                │
│  Layer Caching   │ 10x faster builds                                    │
│  Multi-stage     │ 70-80% smaller final image                          │
│  Security        │ Reduced attack surface                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Base Image Selection

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# BASE IMAGE COMPARISON
# ═══════════════════════════════════════════════════════════════════════

# ❌ AVOID: Full images
FROM python:3.11           # ~1.0 GB
FROM node:20               # ~1.1 GB
FROM ubuntu:22.04          # ~77 MB

# ✅ PREFER: Slim variants
FROM python:3.11-slim      # ~130 MB
FROM node:20-slim          # ~240 MB
FROM debian:bookworm-slim  # ~74 MB

# ✅ BEST: Alpine (when compatible)
FROM python:3.11-alpine    # ~50 MB
FROM node:20-alpine        # ~140 MB
FROM alpine:3.18           # ~7 MB

# ═══════════════════════════════════════════════════════════════════════
# TAG SPECIFICITY
# ═══════════════════════════════════════════════════════════════════════

# ❌ AVOID: Mutable tags
FROM python:latest         # Oförutsägbar
FROM node:lts              # Förändras

# ✅ PREFER: Specific versions
FROM python:3.11.7-slim-bookworm
FROM node:20.10.0-alpine3.18

# ✅ BEST: Digest för reproducerbarhet
FROM python:3.11-slim@sha256:abc123...
```

### Size Comparison

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    IMAGE SIZE COMPARISON                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  IMAGE                        │ SIZE     │ PACKAGES  │ USE CASE         │
│  ─────────────────────────────────────────────────────────────────────  │
│  python:3.11                  │ 1.0 GB   │ Full      │ Development      │
│  python:3.11-slim             │ 130 MB   │ Minimal   │ Production       │
│  python:3.11-alpine           │ 50 MB    │ musl      │ Size-critical    │
│  ─────────────────────────────────────────────────────────────────────  │
│  node:20                      │ 1.1 GB   │ Full      │ Development      │
│  node:20-slim                 │ 240 MB   │ Minimal   │ Production       │
│  node:20-alpine               │ 140 MB   │ musl      │ Size-critical    │
│  ─────────────────────────────────────────────────────────────────────  │
│  golang:1.21                  │ 800 MB   │ Full      │ Build only       │
│  gcr.io/distroless/static    │ 2 MB     │ None      │ Go binaries      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Layer Optimization

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# LAYER CACHING - Order matters!
# ═══════════════════════════════════════════════════════════════════════

# ❌ BAD: Code before dependencies
FROM python:3.11-slim
WORKDIR /app
COPY . .                        # Invaliderar cache vid varje ändring
RUN pip install -r requirements.txt  # Måste köras om varje gång

# ✅ GOOD: Dependencies before code
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .         # Ändras sällan
RUN pip install -r requirements.txt  # Cachas
COPY . .                        # Endast detta invalideras

# ═══════════════════════════════════════════════════════════════════════
# COMBINE RUN COMMANDS
# ═══════════════════════════════════════════════════════════════════════

# ❌ BAD: Multiple layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get clean

# ✅ GOOD: Single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ═══════════════════════════════════════════════════════════════════════
# CLEANUP IN SAME LAYER
# ═══════════════════════════════════════════════════════════════════════

# ❌ BAD: Cleanup i separat layer (sparar inte plats)
RUN wget https://example.com/big-file.tar.gz
RUN tar xzf big-file.tar.gz
RUN rm big-file.tar.gz          # Filen finns fortfarande i tidigare layer!

# ✅ GOOD: Allt i samma layer
RUN wget https://example.com/big-file.tar.gz && \
    tar xzf big-file.tar.gz && \
    rm big-file.tar.gz
```

## 4. .dockerignore

```bash
# ═══════════════════════════════════════════════════════════════════════
# .dockerignore - Exclude from build context
# ═══════════════════════════════════════════════════════════════════════

# Git
.git
.gitignore

# IDE
.vscode
.idea
*.swp

# Dependencies (reinstalleras i container)
node_modules
__pycache__
*.pyc
.venv
venv

# Build artifacts
dist
build
*.egg-info

# Tests
tests
test
*.test.js
*.test.py
coverage
.pytest_cache
.coverage

# Documentation
docs
*.md
!README.md

# Docker files
Dockerfile*
docker-compose*.yml
.docker

# Environment
.env
.env.*

# Logs
logs
*.log

# OS
.DS_Store
Thumbs.db
```

### Impact Demonstration

```bash
# Utan .dockerignore
$ du -sh .
1.2G    .

$ docker build -t myapp .
Sending build context to Docker daemon  1.2GB  # Långsamt!

# Med .dockerignore
$ docker build -t myapp .
Sending build context to Docker daemon  50MB   # Snabbt!
```

## 5. Optimized Examples

### Python Application

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# OPTIMIZED PYTHON DOCKERFILE
# ═══════════════════════════════════════════════════════════════════════

FROM python:3.11-slim-bookworm AS base

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# Install system dependencies in single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

### Node.js Application

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# OPTIMIZED NODE.JS DOCKERFILE
# ═══════════════════════════════════════════════════════════════════════

FROM node:20-slim AS base

ENV NODE_ENV=production

WORKDIR /app

# Copy only package files first (cached layer)
COPY package*.json ./

# Install production dependencies only
RUN npm ci --only=production && \
    npm cache clean --force

# Copy application code
COPY --chown=node:node . .

USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=10s \
    CMD node -e "require('http').get('http://localhost:3000/health')"

CMD ["node", "server.js"]
```

## 6. Practical Exercises

### Övning 1: Optimera en Dockerfile

```dockerfile
# BEFORE: Ooptimerad (analysera problem)
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip curl vim nano
COPY . /app
WORKDIR /app
RUN pip3 install flask requests pandas numpy
RUN pip3 install gunicorn
EXPOSE 5000
CMD python3 app.py

# AFTER: Optimerad
FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Only curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r app && useradd -r -g app app
USER app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Övning 2: Mät förbättring

```bash
# Bygg båda
docker build -f Dockerfile.before -t app:before .
docker build -f Dockerfile.after -t app:after .

# Jämför storlek
docker images | grep app
# app    before   1.2GB
# app    after    180MB

# Jämför build tid (andra körning för cache)
time docker build -f Dockerfile.after -t app:after .
```

## 7-14. Sammanfattning

### Best Practices Checklist

| Category | Practice |
|----------|----------|
| Base Image | Use slim/alpine |
| Tags | Specific versions |
| Layers | Combine RUN commands |
| Caching | Dependencies first |
| Security | Non-root USER |
| Cleanup | Same layer as install |

---

**Nästa Node:** Multi-stage Builds →
''',
    "xp_reward": 175,
    "estimated_minutes": 75,
    "prerequisites": ["docker_node_8"],
    "learning_outcomes": [
        "Optimera Dockerfiles",
        "Välja rätt base images",
        "Maximera layer caching",
        "Skriva säkra Dockerfiles"
    ]
}

NODE_10 = {
    "id": "docker_node_10",
    "title": "Multi-stage Builds - Efficient Images",
    "slug": "multi-stage-builds-efficient-images",
    "content": r'''# 🏗️ Multi-stage Builds

## 1. Introduktion & Kontext

Multi-stage builds låter dig använda flera FROM-statements i samma Dockerfile. Du kan kopiera artefakter mellan stages för att skapa minimala production images.

### Multi-stage Concept

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MULTI-STAGE BUILD CONCEPT                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  TRADITIONAL BUILD:                                                      │
│  ═══════════════════════════════════════════════════════════════════   │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    SINGLE IMAGE                                  │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │   │
│  │  │ Build tools  │ │   Source     │ │  Final app   │            │   │
│  │  │  (100 MB)    │ │  (50 MB)     │ │  (10 MB)     │            │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘            │   │
│  │                                                                  │   │
│  │  Total: 160+ MB (inkluderar allt)                               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  MULTI-STAGE BUILD:                                                      │
│  ═══════════════════════════════════════════════════════════════════   │
│                                                                          │
│  Stage 1: BUILD                        Stage 2: PRODUCTION              │
│  ┌─────────────────────────┐          ┌─────────────────────────┐      │
│  │  FROM node:20           │          │  FROM node:20-alpine    │      │
│  │  ┌──────────────┐       │          │                         │      │
│  │  │ Build tools  │       │   COPY   │  ┌──────────────┐       │      │
│  │  │ Source code  │──────────────────│→ │  Built app   │       │      │
│  │  │ Dependencies │       │  only    │  │  only        │       │      │
│  │  └──────────────┘       │  dist/   │  └──────────────┘       │      │
│  │                         │          │                         │      │
│  │  (DISCARDED)            │          │  Final: 50 MB           │      │
│  └─────────────────────────┘          └─────────────────────────┘      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Basic Multi-stage

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# BASIC MULTI-STAGE BUILD
# ═══════════════════════════════════════════════════════════════════════

# Stage 1: Build
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

## 3. Named Stages

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# NAMED STAGES WITH TARGETS
# ═══════════════════════════════════════════════════════════════════════

# Stage: dependencies
FROM node:20 AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Stage: builder
FROM deps AS builder
COPY . .
RUN npm run build
RUN npm run test

# Stage: development
FROM deps AS development
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

# Stage: production
FROM node:20-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=deps --chown=nodejs:nodejs /app/node_modules ./node_modules
USER nodejs
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

```bash
# Build specific target
docker build --target development -t myapp:dev .
docker build --target production -t myapp:prod .
```

## 4. Go Application (Distroless)

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# GO MULTI-STAGE (DISTROLESS)
# ═══════════════════════════════════════════════════════════════════════

# Stage 1: Build
FROM golang:1.21 AS builder

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \
    go build -ldflags="-w -s" -o /app/server ./cmd/server

# Stage 2: Minimal production image
FROM gcr.io/distroless/static-debian12 AS production

COPY --from=builder /app/server /server

USER nonroot:nonroot

EXPOSE 8080

ENTRYPOINT ["/server"]
```

### Size Comparison

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GO BUILD SIZE COMPARISON                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Stage                    │ Image Size │ Contents                       │
│  ─────────────────────────────────────────────────────────────────────  │
│  golang:1.21              │ 800 MB     │ Full Go toolchain              │
│  golang:1.21-alpine       │ 250 MB     │ Go + Alpine                    │
│  alpine:3.18              │ 7 MB       │ Minimal Linux                  │
│  distroless/static        │ 2 MB       │ Static binary only             │
│  scratch                  │ 0 MB       │ Empty (binary only)            │
│                                                                          │
│  RESULT:                                                                │
│  ─────────────────────────────────────────────────────────────────────  │
│  Without multi-stage      │ 800 MB                                      │
│  With multi-stage         │ 12 MB (binary + distroless)                │
│  Reduction                │ 98%                                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 5. Python with Virtual Environment

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# PYTHON MULTI-STAGE WITH VENV
# ═══════════════════════════════════════════════════════════════════════

# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.11-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r app && useradd -r -g app app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application
COPY --chown=app:app . .

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

## 6. Frontend Build (React/Next.js)

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# NEXT.JS MULTI-STAGE
# ═══════════════════════════════════════════════════════════════════════

# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Stage 2: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build

# Stage 3: Production
FROM node:20-alpine AS production
WORKDIR /app

ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

# Copy only necessary files
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
```

## 7. Copy from External Image

```dockerfile
# ═══════════════════════════════════════════════════════════════════════
# COPY FROM EXTERNAL IMAGES
# ═══════════════════════════════════════════════════════════════════════

FROM alpine:3.18

# Copy binary from official image
COPY --from=docker:24.0.6 /usr/local/bin/docker /usr/local/bin/docker

# Copy from any image
COPY --from=redis:alpine /usr/local/bin/redis-cli /usr/local/bin/
COPY --from=nginx:alpine /etc/nginx/nginx.conf /etc/nginx/

# Useful for adding tools to custom images
```

## 8. Practical Exercises

### Övning 1: Basic Multi-stage

```bash
mkdir multi-stage-demo && cd multi-stage-demo

# Simple Go app
cat << 'EOF' > main.go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello from Multi-stage!")
    })
    http.ListenAndServe(":8080", nil)
}
EOF

cat << 'EOF' > go.mod
module app
go 1.21
EOF

# Multi-stage Dockerfile
cat << 'EOF' > Dockerfile
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o server .

FROM alpine:3.18
COPY --from=builder /app/server /server
EXPOSE 8080
CMD ["/server"]
EOF

# Build and compare
docker build -t app:multi .
docker images | grep app
# → Se storleken (ska vara ~15MB)

# Test
docker run -d -p 8080:8080 --name test app:multi
curl http://localhost:8080
docker stop test && docker rm test
```

### Övning 2: Target Selection

```dockerfile
# Dockerfile med multipla targets
FROM node:20 AS base
WORKDIR /app
COPY package*.json ./

FROM base AS development
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS test
RUN npm ci
COPY . .
CMD ["npm", "test"]

FROM base AS production
RUN npm ci --only=production
COPY . .
CMD ["npm", "start"]
```

```bash
# Bygg olika targets
docker build --target development -t app:dev .
docker build --target test -t app:test .
docker build --target production -t app:prod .

# Kör test
docker run --rm app:test
```

## 9-14. Sammanfattning

### Multi-stage Benefits

| Benefit | Description |
|---------|-------------|
| Size | 50-98% smaller images |
| Security | No build tools in prod |
| Speed | Faster deployments |
| Cache | Efficient layer caching |

---

**Nästa Node:** Docker Security →
''',
    "xp_reward": 180,
    "estimated_minutes": 80,
    "prerequisites": ["docker_node_9"],
    "learning_outcomes": [
        "Bygga multi-stage Dockerfiles",
        "Optimera image storlek",
        "Använda named stages",
        "Kopiera mellan stages"
    ]
}

# Block 3 Part 1 exports
BLOCK_3_PART_1_NODES = [NODE_9, NODE_10]
