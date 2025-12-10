# =============================================================================
# DOCKER IMAGES — Noder 5-8 (Advanced Image Topics)
# Premium Bootcamp-Quality Content
# =============================================================================

NODE_05_MULTI_STAGE = {
    "id": "docker-multi-stage",
    "node_id": 5,
    "title": "Multi-stage Builds",
    "slug": "docker-multi-stage",
    "description": "Optimera images med multi-stage builds för minimala produktions-images",
    "type": "practice",
    "difficulty": "medium",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [4],
    "content": '''# 🏗️ Multi-stage Builds

## Lärande mål
Efter denna lektion kommer du att:
- Förstå varför multi-stage builds behövs
- Kunna skapa optimerade produktions-images
- Reducera image-storlek med 90%+
- Separera build- och runtime-dependencies

---

## 📖 Problemet med stora images

### Single-stage Dockerfile

```dockerfile
# ❌ DÅLIGT: Allt i en image
FROM node:20

WORKDIR /app

# Build tools behövs för native dependencies
RUN apt-get update && apt-get install -y \\
    python3 \\
    make \\
    g++ \\
    git

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

CMD ["npm", "start"]

# Resultat: ~1.2 GB image
# Innehåller: build tools, devDependencies, source code
```

### Varför är det ett problem?

```
+-----------------------------------------------------------------+
|              SINGLE-STAGE IMAGE: 1.2 GB                          |
+-----------------------------------------------------------------+
|                                                                  |
|  +------------------------------------------------------------+ |
|  | Build tools (python, make, g++)           |  ~300 MB       | |
|  | devDependencies (webpack, eslint, etc)    |  ~400 MB       | |
|  | Source code (.ts, tests)                  |  ~50 MB        | |
|  | node_modules (alla)                       |  ~300 MB       | |
|  | Built output (dist/)                      |  ~10 MB        | |
|  | Node.js runtime                           |  ~150 MB       | |
|  +------------------------------------------------------------+ |
|                                                                  |
|  I PRODUKTION behöver vi bara:                                  |
|  • Built output (dist/)        ~10 MB                           |
|  • Production dependencies     ~50 MB                           |
|  • Node.js runtime             ~50 MB (alpine)                  |
|  = ~110 MB istället för 1.2 GB!                                 |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 🚀 Multi-stage lösningen

### Grundläggande koncept

```dockerfile
# Stage 1: BUILD
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: RUNTIME
FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

```
+-----------------------------------------------------------------+
|                    MULTI-STAGE BUILD                             |
+-----------------------------------------------------------------+
|                                                                  |
|   STAGE 1: builder                    STAGE 2: runtime          |
|   +-----------------+                 +-----------------+       |
|   | FROM node:20    |                 | FROM node:alpine|       |
|   |                 |                 |                 |       |
|   | npm install     |   COPY --from   | dist/           |       |
|   | npm run build   |  ------------->  | node_modules/   |       |
|   |                 |                 | (prod only)     |       |
|   | ~1.2 GB         |                 | ~110 MB         |       |
|   +-----------------+                 +-----------------+       |
|         |                                     |                  |
|         ↓                                     ↓                  |
|      KASTAS                              FINAL IMAGE             |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 💻 Praktiska exempel

### TypeScript Node.js API

```dockerfile
# ===========================================
# Stage 1: Dependencies
# ===========================================
FROM node:20-alpine AS deps
WORKDIR /app

# Kopiera bara package files för cache
COPY package.json package-lock.json ./

# Installera ALLA dependencies (för build)
RUN npm ci

# ===========================================
# Stage 2: Builder
# ===========================================
FROM node:20-alpine AS builder
WORKDIR /app

# Kopiera dependencies från deps stage
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Bygg TypeScript
RUN npm run build

# Ta bort devDependencies
RUN npm prune --production

# ===========================================
# Stage 3: Runner
# ===========================================
FROM node:20-alpine AS runner
WORKDIR /app

# Säkerhets-best practice
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 app
USER app

# Kopiera endast det som behövs
COPY --from=builder --chown=app:nodejs /app/dist ./dist
COPY --from=builder --chown=app:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=app:nodejs /app/package.json ./

ENV NODE_ENV=production
EXPOSE 3000

CMD ["node", "dist/index.js"]
```

### Go-applikation (Extremt liten image)

```dockerfile
# ===========================================
# Stage 1: Build
# ===========================================
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server .

# ===========================================
# Stage 2: Runtime
# ===========================================
FROM scratch

# Kopiera CA-certifikat för HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Kopiera binären
COPY --from=builder /app/server /server

EXPOSE 8080
ENTRYPOINT ["/server"]

# Resultat: ~5-10 MB image!
```

### Python Django/FastAPI

```dockerfile
# ===========================================
# Stage 1: Builder
# ===========================================
FROM python:3.11-slim AS builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Exportera dependencies utan dev
RUN poetry export -f requirements.txt --without-hashes > requirements.txt

# Installera i virtuell miljö
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# ===========================================
# Stage 2: Runtime
# ===========================================
FROM python:3.11-slim AS runtime

# Kopiera virtuell miljö
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Kopiera appkod
COPY src/ ./src/

# Non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🎯 Avancerade tekniker

### Targeted builds

```dockerfile
FROM node:20-alpine AS base
WORKDIR /app

FROM base AS deps
COPY package*.json ./
RUN npm ci

FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Development target
FROM base AS development
COPY --from=deps /app/node_modules ./node_modules
COPY . .
CMD ["npm", "run", "dev"]

# Production target
FROM base AS production
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

```bash
# Bygg för development
docker build --target development -t myapp:dev .

# Bygg för production
docker build --target production -t myapp:prod .
```

### Caching med BuildKit

```dockerfile
# syntax=docker/dockerfile:1.4

FROM node:20-alpine AS builder
WORKDIR /app

# Cache npm downloads
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \\
    npm ci

COPY . .
RUN npm run build
```

---

## 📊 Storleksjämförelse

| Approach | Image Size | Build Time |
|----------|------------|------------|
| Single-stage (node:20) | ~1.2 GB | ~2 min |
| Multi-stage (node:20-slim) | ~300 MB | ~3 min |
| Multi-stage (node:20-alpine) | ~110 MB | ~3 min |
| Go med scratch | ~10 MB | ~1 min |

---

## ✅ Kunskapskontroll

1. **Vad är syftet med multi-stage builds?**
   - Separera build-time från runtime dependencies
   - Reducera final image storlek
   - Öka säkerhet (mindre attack surface)

2. **Vad gör `COPY --from=builder`?**
   - Kopierar filer från en tidigare build-stage
   - Endast det kopierade inkluderas i final image

---

## 🏋️ Övningar

### Övning: Optimera en Node.js app
```bash
# Skapa projekt
mkdir multi-stage-demo && cd multi-stage-demo

# Skapa package.json
cat > package.json << 'EOF'
{
  "name": "demo",
  "scripts": { "build": "echo 'built'" },
  "dependencies": { "express": "^4.18.2" }
}
EOF

# Skapa enkel app
echo "console.log('Hello');" > index.js

# Testa single-stage vs multi-stage
# Jämför storlek med docker images
```

---

**Nästa steg:** Node 6 - Docker Registry & Image Distribution
''',
}


NODE_06_REGISTRY = {
    "id": "docker-registry",
    "node_id": 6,
    "title": "Docker Registry & Distribution",
    "slug": "docker-registry",
    "description": "Hantera och distribuera images via registries",
    "type": "concept",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "prerequisites": [5],
    "content": '''# 📦 Docker Registry & Distribution

## Lärande mål
- Förstå hur Docker registries fungerar
- Pusha och pulla images till/från Docker Hub
- Sätta upp privat registry
- Använda tagging-strategier professionellt

---

## 📖 Vad är en Registry?

```
+-----------------------------------------------------------------+
|                    DOCKER REGISTRY                               |
+-----------------------------------------------------------------+
|                                                                  |
|   Developer                    Registry                         |
|   +-------------+              +-------------+                 |
|   | docker push |  -----------> | Docker Hub  |                 |
|   | docker pull |  <----------- |   / ECR     |                 |
|   +-------------+              |   / GCR     |                 |
|                                |   / Private |                 |
|                                +-------------+                 |
|                                       |                         |
|                                       ↓                         |
|                    +---------------------------------+         |
|                    |        REPOSITORY               |         |
|                    |  mycompany/webapp               |         |
|                    |   +-- :latest                   |         |
|                    |   +-- :1.0.0                    |         |
|                    |   +-- :1.0.1                    |         |
|                    |   +-- :develop                  |         |
|                    +---------------------------------+         |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 🌐 Docker Hub

### Login och push

```bash
# Logga in
docker login
# Username: myuser
# Password: ********

# Tagga image för Docker Hub
docker tag myapp:1.0 myuser/myapp:1.0

# Pusha till Docker Hub
docker push myuser/myapp:1.0

# Pulla från Docker Hub
docker pull myuser/myapp:1.0
```

### Image naming

```
registry.com/namespace/repository:tag

docker.io/library/nginx:latest
     |        |      |     |
     |        |      |     +-- Tag
     |        |      +-- Repository
     |        +-- Namespace (user/org)
     +-- Registry
```

---

## 🔒 Private Registry

### Enkel lokal registry

```bash
# Starta lokal registry
docker run -d -p 5000:5000 --name registry registry:2

# Tagga för lokal registry
docker tag myapp:1.0 localhost:5000/myapp:1.0

# Pusha
docker push localhost:5000/myapp:1.0

# Pulla
docker pull localhost:5000/myapp:1.0
```

### Cloud Registries

```bash
# AWS ECR
aws ecr get-login-password --region eu-north-1 | \\
    docker login --username AWS --password-stdin \\
    123456789.dkr.ecr.eu-north-1.amazonaws.com

docker tag myapp:1.0 123456789.dkr.ecr.eu-north-1.amazonaws.com/myapp:1.0
docker push 123456789.dkr.ecr.eu-north-1.amazonaws.com/myapp:1.0

# Google GCR
gcloud auth configure-docker
docker tag myapp:1.0 gcr.io/my-project/myapp:1.0
docker push gcr.io/my-project/myapp:1.0

# GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag myapp:1.0 ghcr.io/username/myapp:1.0
docker push ghcr.io/username/myapp:1.0
```

---

## 🏷️ Tagging Best Practices

```bash
# Semantic versioning
docker build -t myapp:1.2.3 -t myapp:1.2 -t myapp:1 -t myapp:latest .

# Git-baserad
docker build -t myapp:$(git rev-parse --short HEAD) .
docker build -t myapp:$(git describe --tags --always) .

# Miljö-baserad
docker build -t myapp:prod-1.2.3 .
docker build -t myapp:staging-$(date +%Y%m%d) .
```

---

**Nästa steg:** Node 7 - Dockerfile Best Practices
''',
}


NODE_07_DOCKERFILE_BEST_PRACTICES = {
    "id": "dockerfile-best-practices",
    "node_id": 7,
    "title": "Dockerfile Best Practices",
    "slug": "dockerfile-best-practices",
    "description": "Skriv säkra, effektiva och underhållbara Dockerfiles",
    "type": "deep_dive",
    "difficulty": "hard",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "prerequisites": [6],
    "content": '''# 🏆 Dockerfile Best Practices

## Lärande mål
- Skriva säkra Dockerfiles
- Optimera för storlek och build-tid
- Följa branschstandarder
- Undvika vanliga misstag

---

## 🔒 Säkerhet

### 1. Non-root user

```dockerfile
# ❌ DÅLIGT: Kör som root
FROM python:3.11-slim
COPY . /app
CMD ["python", "app.py"]

# ✅ BRA: Dedikerad användare
FROM python:3.11-slim
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app
COPY --chown=appuser:appuser . .
USER appuser
CMD ["python", "app.py"]
```

### 2. Specifika base image tags

```dockerfile
# ❌ DÅLIGT: "latest" kan ändras
FROM python:latest

# ✅ BRA: Specifik version och variant
FROM python:3.11.7-slim-bookworm
```

### 3. Scan för vulnerabilities

```bash
# Docker Scout (inbyggt)
docker scout cves myimage:1.0

# Trivy
trivy image myimage:1.0
```

---

## ⚡ Performance

### 1. Layer caching

```dockerfile
# ❌ DÅLIGT: Cache invalideras vid kodändring
COPY . .
RUN npm install

# ✅ BRA: Dependencies cachas separat
COPY package*.json ./
RUN npm ci
COPY . .
```

### 2. Minimera lager

```dockerfile
# ❌ DÅLIGT: Många RUN-instruktioner
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# ✅ BRA: Ett lager
RUN apt-get update && \\
    apt-get install -y --no-install-recommends curl && \\
    rm -rf /var/lib/apt/lists/*
```

### 3. .dockerignore

```
.git
.gitignore
node_modules
__pycache__
*.pyc
.env
.env.*
tests/
docs/
*.md
Dockerfile*
docker-compose*
```

---

## 📝 Underhållbarhet

### 1. Labels

```dockerfile
LABEL org.opencontainers.image.source="https://github.com/user/repo"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.description="My awesome app"
LABEL maintainer="dev@example.com"
```

### 2. Healthcheck

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \\
    CMD curl -f http://localhost:8080/health || exit 1
```

### 3. ARG för flexibilitet

```dockerfile
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}-alpine

ARG APP_VERSION=unknown
ENV APP_VERSION=${APP_VERSION}
```

---

## 🎯 Komplett produktions-Dockerfile

```dockerfile
# syntax=docker/dockerfile:1.4

# ===========================================
# Build Arguments
# ===========================================
ARG NODE_VERSION=20
ARG APP_VERSION=dev

# ===========================================
# Base Stage
# ===========================================
FROM node:${NODE_VERSION}-alpine AS base
WORKDIR /app
RUN apk add --no-cache tini

# ===========================================
# Dependencies
# ===========================================
FROM base AS deps
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \\
    npm ci --only=production

# ===========================================
# Builder
# ===========================================
FROM base AS builder
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ===========================================
# Production
# ===========================================
FROM base AS production

# Labels
LABEL org.opencontainers.image.version="${APP_VERSION}"

# Security
RUN addgroup -g 1001 -S nodejs && \\
    adduser -S nodejs -u 1001
USER nodejs

# Application
COPY --from=deps --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --chown=nodejs:nodejs package.json ./

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \\
    CMD wget -qO- http://localhost:3000/health || exit 1

# Runtime
ENV NODE_ENV=production
EXPOSE 3000
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "dist/index.js"]
```

---

**Nästa steg:** Node 8 - Image Optimization & Security Scanning
''',
}


NODE_08_IMAGE_SECURITY = {
    "id": "image-security",
    "node_id": 8,
    "title": "Image Security & Scanning",
    "slug": "image-security",
    "description": "Säkra dina images med scanning och best practices",
    "type": "practice",
    "difficulty": "hard",
    "estimated_minutes": 50,
    "xp_reward": 140,
    "prerequisites": [7],
    "content": '''# 🔐 Image Security & Scanning

## Lärande mål
- Förstå container-säkerhetshot
- Scanna images för sårbarheter
- Implementera säkra CI/CD pipelines
- Följa säkerhets-best practices

---

## 🛡️ Säkerhetshot

### Attack Vectors

```
+-----------------------------------------------------------------+
|                 CONTAINER SECURITY THREATS                       |
+-----------------------------------------------------------------+
|                                                                  |
|  1. Vulnerable base images (CVEs)                               |
|  2. Malicious packages i dependencies                           |
|  3. Secrets i image layers                                      |
|  4. Running as root                                             |
|  5. Excessive permissions                                       |
|  6. Outdated packages                                           |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 🔍 Scanning Tools

### Docker Scout

```bash
# Scanna lokal image
docker scout cves myimage:1.0

# Detaljerad rapport
docker scout cves --format markdown myimage:1.0

# Rekommendationer
docker scout recommendations myimage:1.0
```

### Trivy

```bash
# Installera
brew install trivy  # macOS

# Scanna image
trivy image myimage:1.0

# Endast HIGH och CRITICAL
trivy image --severity HIGH,CRITICAL myimage:1.0

# JSON output för CI
trivy image --format json -o results.json myimage:1.0
```

---

## 🔧 Security Hardening

### Minimal base images

```dockerfile
# Vanlig: ~900MB
FROM python:3.11

# Slim: ~150MB
FROM python:3.11-slim

# Alpine: ~50MB
FROM python:3.11-alpine

# Distroless: ~20MB (Google)
FROM gcr.io/distroless/python3-debian12
```

### Read-only filesystem

```bash
docker run --read-only --tmpfs /tmp myimage:1.0
```

### Secrets management

```dockerfile
# ❌ DÅLIGT: Secret i image
ENV DATABASE_PASSWORD=secret123

# ✅ BRA: Använd Docker secrets eller env vid runtime
docker run -e DATABASE_PASSWORD=$DB_PASS myimage:1.0
```

---

## 📋 Security Checklist

- [ ] Non-root user
- [ ] Specifik base image version
- [ ] Ingen känslig data i image
- [ ] Scanna regelbundet för CVEs
- [ ] Minimal base image
- [ ] HEALTHCHECK definierad
- [ ] .dockerignore konfigurerad

---

**Nästa steg:** Node 9 - Docker Networking Fundamentals
''',
}


NODES = [
    NODE_05_MULTI_STAGE,
    NODE_06_REGISTRY,
    NODE_07_DOCKERFILE_BEST_PRACTICES,
    NODE_08_IMAGE_SECURITY,
]
