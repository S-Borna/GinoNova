"""
Docker Advanced - Tasks 11-20 (DevOps & Orchestration)
Premium Bootcamp-Quality Content
"""

TASKS_ADVANCED = [
    {
        "title": "Docker Registry & Image Distribution",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 150,
        "content": r"""
# 📦 Docker Registry & Image Distribution

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Docker registries
- Sätta upp privat registry
- Image tagging strategies
- Distribution best practices

---

## 📖 Registry Types

```
+-------------------------------------------------------------+
|                    REGISTRY LANDSCAPE                        |
+-------------------------------------------------------------+
|                                                              |
|  PUBLIC                    CLOUD                    PRIVATE |
|  +---------+              +---------+              +-----+ |
|  | Docker  |              |   ECR   |              |Self-| |
|  |   Hub   |              | (AWS)   |              |hosted| |
|  +---------+              +---------+              +-----+ |
|  +---------+              +---------+              +-----+ |
|  |  GHCR   |              |   GCR   |              |Harbor| |
|  |(GitHub) |              | (GCP)   |              |      | |
|  +---------+              +---------+              +-----+ |
|  +---------+              +---------+                      |
|  | Quay.io |              |   ACR   |                      |
|  |(RedHat) |              | (Azure) |                      |
|  +---------+              +---------+                      |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🏗️ Self-Hosted Registry

```yaml
# docker-compose.yml
version: '3.8'

services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - registry_data:/var/lib/registry
      - ./config.yml:/etc/docker/registry/config.yml
    environment:
      - REGISTRY_STORAGE_DELETE_ENABLED=true

  registry-ui:
    image: joxit/docker-registry-ui:latest
    ports:
      - "8080:80"
    environment:
      - REGISTRY_URL=http://registry:5000
      - DELETE_IMAGES=true

volumes:
  registry_data:
```

```yaml
# config.yml
version: 0.1
storage:
  filesystem:
    rootdirectory: /var/lib/registry
  delete:
    enabled: true
http:
  addr: :5000
  headers:
    X-Content-Type-Options: [nosniff]
```

---

## 🏷️ Tagging Strategies

```bash
# Semantic versioning
myapp:1.0.0
myapp:1.0
myapp:1

# Git-based
myapp:${GIT_SHA:0:7}       # Short SHA
myapp:${BRANCH_NAME}       # Branch name
myapp:${TAG}               # Git tag

# Environment-based
myapp:staging
myapp:production

# Kombinerat (rekommenderat)
myapp:v1.2.3-abc1234        # version + commit
myapp:v1.2.3-abc1234-linux  # + platform

# CI/CD pattern
myapp:${VERSION:-latest}
myapp:build-${BUILD_NUMBER}
```

---

## 📤 Push/Pull Workflow

```bash
# Login till olika registries
docker login                              # Docker Hub
docker login ghcr.io                      # GitHub
docker login 123456.dkr.ecr.eu-west-1.amazonaws.com  # AWS ECR

# Tagga för registry
docker tag myapp:latest ghcr.io/myorg/myapp:v1.0.0

# Push
docker push ghcr.io/myorg/myapp:v1.0.0

# Pull
docker pull ghcr.io/myorg/myapp:v1.0.0
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Local Registry
```bash
# Starta lokal registry
docker run -d -p 5000:5000 --name registry registry:2

# Tagga och pusha
docker tag myapp:latest localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1

# Verifiera
curl http://localhost:5000/v2/_catalog
```

---

## 📚 Sammanfattning

| Strategy | Use Case |
|----------|----------|
| Semver | Production releases |
| Git SHA | Traceability |
| Branch | Environment mapping |
| Build number | CI/CD |

**Nästa steg:** Multi-Architecture Builds

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Multi-Architecture Docker Builds",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 155,
        "content": r"""
# 🏗️ Multi-Architecture Docker Builds

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Bygga för flera arkitekturer (amd64, arm64)
- Använda Docker Buildx
- Manifest lists
- CI/CD för multi-arch

---

## 📖 Architecture Overview

```
+-------------------------------------------------------------+
|              MULTI-ARCHITECTURE SUPPORT                      |
+-------------------------------------------------------------+
|                                                              |
|  Image: myapp:v1.0.0                                        |
|  +-----------------------------------------------------+   |
|  |                  Manifest List                       |   |
|  +-----------------------------------------------------+   |
|  |                                                      |   |
|  |  +--------------+  +--------------+  +-----------+ |   |
|  |  | linux/amd64  |  | linux/arm64  |  |linux/arm/v7| |   |
|  |  |   (x86_64)   |  |   (M1/M2)    |  |  (RPi)    | |   |
|  |  +--------------+  +--------------+  +-----------+ |   |
|  |                                                      |   |
|  +-----------------------------------------------------+   |
|                                                              |
|  docker pull myapp:v1.0.0                                   |
|  -> Automatiskt rätt arkitektur!                            |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Docker Buildx Setup

```bash
# Kontrollera buildx
docker buildx version

# Skapa multi-platform builder
docker buildx create --name multiarch --driver docker-container --bootstrap
docker buildx use multiarch

# Inspektera builder
docker buildx inspect --bootstrap

# Lista builders
docker buildx ls
```

---

## 🚀 Multi-Platform Build

```bash
# Build och push för flera plattformar
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag myregistry.com/myapp:v1.0.0 \
  --push \
  .

# Build utan push (lokal)
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag myapp:v1.0.0 \
  --load \  # Endast för single platform
  .

# Med cache
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --cache-from type=registry,ref=myregistry.com/myapp:cache \
  --cache-to type=registry,ref=myregistry.com/myapp:cache,mode=max \
  --tag myregistry.com/myapp:v1.0.0 \
  --push \
  .
```

---

## 📝 Multi-Arch Dockerfile

```dockerfile
# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM golang:1.22-alpine AS builder

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ARG TARGETOS
ARG TARGETARCH

WORKDIR /app
COPY . .

# Cross-compile för target platform
RUN CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} \
    go build -ldflags="-s -w" -o /app/server

FROM alpine:3.19

COPY --from=builder /app/server /server

EXPOSE 8080
ENTRYPOINT ["/server"]
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Multi-Arch Build
```bash
# Skapa builder
docker buildx create --name mybuilder --use

# Build för arm64 och amd64
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:multiarch \
  --push \
  .

# Inspektera manifest
docker manifest inspect myapp:multiarch
```

---

## 📚 Sammanfattning

| Arkitektur | Plattform |
|------------|-----------|
| linux/amd64 | Intel/AMD servers |
| linux/arm64 | M1/M2 Mac, AWS Graviton |
| linux/arm/v7 | Raspberry Pi |

**Nästa steg:** Docker BuildKit Features

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Docker BuildKit Advanced Features",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# ⚡ Docker BuildKit Advanced Features

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- BuildKit caching strategies
- Secret mounts
- SSH forwarding
- Build-time mounts

---

## 📖 BuildKit Overview

```
+-------------------------------------------------------------+
|                     BUILDKIT FEATURES                        |
+-------------------------------------------------------------+
|                                                              |
|  +---------------+  +---------------+  +---------------+   |
|  | Parallel      |  | Advanced      |  | Secret        |   |
|  | Builds        |  | Caching       |  | Mounts        |   |
|  +---------------+  +---------------+  +---------------+   |
|                                                              |
|  +---------------+  +---------------+  +---------------+   |
|  | SSH           |  | Cache         |  | Build         |   |
|  | Forwarding    |  | Mounts        |  | Contexts      |   |
|  +---------------+  +---------------+  +---------------+   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔒 Secret Mounts

```dockerfile
# syntax=docker/dockerfile:1

FROM node:18-alpine

WORKDIR /app

# Mount secret vid build - exponeras ALDRIG i image layers!
RUN --mount=type=secret,id=npm_token \
    NPM_TOKEN=$(cat /run/secrets/npm_token) \
    npm config set //registry.npmjs.org/:_authToken=${NPM_TOKEN} && \
    npm ci && \
    npm config delete //registry.npmjs.org/:_authToken

COPY . .
CMD ["npm", "start"]
```

```bash
# Build med secret
docker build --secret id=npm_token,src=.npmrc -t myapp .

# Eller från env
echo $NPM_TOKEN | docker build --secret id=npm_token -t myapp .
```

---

## 🔑 SSH Forwarding

```dockerfile
# syntax=docker/dockerfile:1

FROM alpine:3.19

# Installera git och openssh
RUN apk add --no-cache git openssh-client

# Klona privat repo med SSH forwarding
RUN --mount=type=ssh \
    mkdir -p ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts && \
    git clone git@github.com:myorg/private-repo.git /app
```

```bash
# Build med SSH agent forwarding
docker build --ssh default -t myapp .

# Med specifik nyckel
docker build --ssh default=$HOME/.ssh/id_rsa -t myapp .
```

---

## 📂 Cache Mounts

```dockerfile
# syntax=docker/dockerfile:1

FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# Cache npm modules mellan builds
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# Golang cache example
FROM golang:1.22-alpine
WORKDIR /app
COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go build -o /app/server
```

---

## 🚀 Parallel Stage Execution

```dockerfile
# syntax=docker/dockerfile:1

# Dessa stages byggs parallellt!
FROM node:18-alpine AS frontend
WORKDIR /frontend
COPY frontend/ .
RUN npm ci && npm run build

FROM golang:1.22-alpine AS backend
WORKDIR /backend
COPY backend/ .
RUN go build -o /app/server

FROM python:3.11-slim AS ml-service
WORKDIR /ml
COPY ml/ .
RUN pip install -r requirements.txt

# Final stage samlar allt
FROM alpine:3.19
COPY --from=frontend /frontend/dist /app/static
COPY --from=backend /app/server /app/server
COPY --from=ml-service /ml /app/ml
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Optimized Build
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim AS builder

WORKDIR /app

# Cache pip downloads
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

COPY . .

FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app
WORKDIR /app
CMD ["python", "main.py"]
```

---

## 📚 Sammanfattning

| Mount Type | Use Case |
|------------|----------|
| secret | API tokens, credentials |
| ssh | Private repo access |
| cache | Package managers |
| bind | Read files utan COPY |

**Nästa steg:** Container Orchestration Intro

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Container Orchestration Introduction",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 🎭 Container Orchestration Introduction

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå behovet av orchestration
- Jämföra orchestration platforms
- Docker Swarm basics
- Förberedelse för Kubernetes

---

## 📖 Varför Orchestration?

```
+-------------------------------------------------------------+
|           SINGLE HOST vs ORCHESTRATION                       |
+-------------------------------------------------------------+
|                                                              |
|  Single Host:              With Orchestration:               |
|  --------------           -------------------               |
|  +----------+             +------------------------------+ |
|  |  Host    |             |         Orchestrator         | |
|  |+---++---+|             | +--------+ +--------+ +----+| |
|  ||C1 ||C2 ||             | | Node 1 | | Node 2 | | N3 || |
|  |+---++---+|             | |+-++-+  | | +-++-+ | |+-+ || |
|  |          |             | ||C||C|  | | |C||C| | ||C| || |
|  |  Manual  |             | |+-++-+  | | +-++-+ | |+-+ || |
|  |  scaling |             | +--------+ +--------+ +----+| |
|  +----------+             +------------------------------+ |
|                                                              |
|  Problems:                 Solutions:                        |
|  - No HA                   - Automatic HA                   |
|  - Manual scaling          - Auto-scaling                   |
|  - No load balancing       - Built-in LB                    |
|  - No self-healing         - Self-healing                   |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔄 Orchestration Features

```
+-------------------------------------------------------------+
|               ORCHESTRATION CAPABILITIES                     |
+-------------------------------------------------------------+
|                                                              |
|  Scheduling              Load Balancing                      |
|  +-----------------+    +-----------------+                |
|  | • Place containers   | • Distribute traffic |            |
|  | • Resource aware     | • Health-aware       |            |
|  | • Affinity rules     | • Service discovery  |            |
|  +-----------------+    +-----------------+                |
|                                                              |
|  Self-Healing            Scaling                             |
|  +-----------------+    +-----------------+                |
|  | • Auto-restart       | • Horizontal scale   |            |
|  | • Reschedule         | • Auto-scaling       |            |
|  | • Health checks      | • Rolling updates    |            |
|  +-----------------+    +-----------------+                |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🐝 Docker Swarm Basics

```bash
# Initiera Swarm
docker swarm init

# Lägg till worker node
docker swarm join-token worker
# Kör kommandot på worker noden

# Skapa service
docker service create \
  --name web \
  --replicas 3 \
  --publish 8080:80 \
  nginx

# Lista services
docker service ls

# Skala service
docker service scale web=5

# Inspektera
docker service ps web

# Uppdatera
docker service update --image nginx:1.25 web

# Ta bort
docker service rm web
```

---

## 📊 Swarm Stack Deploy

```yaml
# stack.yml
version: '3.8'

services:
  web:
    image: nginx:alpine
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    ports:
      - "8080:80"
    networks:
      - webnet

  visualizer:
    image: dockersamples/visualizer:latest
    ports:
      - "8081:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    deploy:
      placement:
        constraints: [node.role == manager]

networks:
  webnet:
```

```bash
# Deploy stack
docker stack deploy -c stack.yml myapp

# Lista stacks
docker stack ls

# Se services i stack
docker stack services myapp

# Ta bort stack
docker stack rm myapp
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Simple Swarm
```bash
# Init swarm
docker swarm init

# Deploy service
docker service create --name api --replicas 2 -p 8080:8080 myapi

# Verify
docker service ls
docker service ps api

# Scale
docker service scale api=5

# Cleanup
docker service rm api
docker swarm leave --force
```

---

## 📚 Sammanfattning

| Feature | Swarm | Kubernetes |
|---------|-------|------------|
| Komplexitet | Enkel | Komplex |
| Setup | Snabb | Kräver mer |
| Skalbarhet | Bra | Utmärkt |
| Ecosystem | Begränsat | Enormt |
| Use case | Små team | Enterprise |

**Nästa steg:** Debugging Docker

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Debugging Docker Applications",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🔍 Debugging Docker Applications

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Felsöka container-problem
- Debugging strategies
- Performance troubleshooting
- Common pitfalls

---

## 📖 Debugging Toolkit

```
+-------------------------------------------------------------+
|                  DOCKER DEBUGGING TOOLKIT                    |
+-------------------------------------------------------------+
|                                                              |
|  Container Info       Logs              Network              |
|  +-------------+     +-------------+   +-------------+     |
|  |docker inspect|     |docker logs  |   |docker network|    |
|  |docker top    |     |docker events|   |netstat/ss   |     |
|  |docker stats  |     |journalctl   |   |tcpdump      |     |
|  +-------------+     +-------------+   +-------------+     |
|                                                              |
|  Filesystem          Process           Debug Container       |
|  +-------------+     +-------------+   +-------------+     |
|  |docker diff  |     |docker exec  |   |--entrypoint |     |
|  |docker cp    |     |nsenter      |   |nicolaka/    |     |
|  |docker export|     |strace       |   |netshoot     |     |
|  +-------------+     +-------------+   +-------------+     |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Basic Debugging Commands

```bash
# Container won't start?
docker logs mycontainer
docker logs --tail 100 mycontainer
docker logs --since 5m mycontainer

# Inspect configuration
docker inspect mycontainer
docker inspect --format '{{.State.Status}}' mycontainer
docker inspect --format '{{.NetworkSettings.IPAddress}}' mycontainer

# Se vad som ändrats i container
docker diff mycontainer

# Resursanvändning
docker stats mycontainer
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Processer i container
docker top mycontainer
```

---

## 🐚 Interactive Debugging

```bash
# Exec in till körande container
docker exec -it mycontainer bash
docker exec -it mycontainer sh  # Om bash saknas

# Kör som root
docker exec -u root -it mycontainer bash

# Starta stoppad container för debugging
docker run -it --entrypoint sh myimage

# Debug container image
docker run -it --rm \
  --entrypoint sh \
  --user root \
  myimage

# Nätverksdebugging
docker run -it --rm --network container:mycontainer nicolaka/netshoot
```

---

## 🌐 Network Debugging

```bash
# Se container nätverk
docker network inspect bridge
docker inspect --format '{{json .NetworkSettings.Networks}}' mycontainer | jq

# Test connectivity från container
docker exec mycontainer ping other-container
docker exec mycontainer curl http://api:8080/health

# Debugging med netshoot
docker run -it --rm --network mynetwork nicolaka/netshoot
# Inside:
nslookup api
curl -v http://api:8080
tcpdump -i any port 8080
```

---

## 🔥 Common Issues & Fixes

```bash
# Issue: Container exits immediately
# Check logs
docker logs mycontainer

# Check if CMD/ENTRYPOINT runs in foreground
# BAD:  CMD service nginx start
# GOOD: CMD ["nginx", "-g", "daemon off;"]

# Issue: Port not accessible
# Check port mapping
docker port mycontainer

# Check if app binds to 0.0.0.0
docker exec mycontainer netstat -tlnp

# Issue: Permission denied
# Check user in container
docker exec mycontainer whoami
docker exec mycontainer id

# Fix: Change file ownership
docker exec -u root mycontainer chown -R appuser:appuser /app
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Debug Workflow
```bash
# Starta problem-container
docker run -d --name debug-test nginx:alpine

# Inspektera
docker logs debug-test
docker inspect debug-test | jq '.State'

# Exec in och debug
docker exec -it debug-test sh
# Inside: cat /etc/nginx/nginx.conf
# Inside: nginx -t

# Network test
docker exec debug-test wget -O- localhost
```

---

## 📚 Sammanfattning

| Problem | Verktyg |
|---------|---------|
| Crash loops | docker logs |
| Performance | docker stats |
| Network | netshoot, tcpdump |
| Filesystem | docker diff |
| Process | docker exec, top |

**Nästa steg:** Docker Image Optimization

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Docker Image Optimization",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 📦 Docker Image Optimization

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Minimera image storlek
- Optimera build-tid
- Layer efficiency
- Distroless och scratch images

---

## 📖 Size Comparison

```
+-------------------------------------------------------------+
|                    IMAGE SIZE COMPARISON                     |
+-------------------------------------------------------------+
|                                                              |
|  Base Image Sizes:                                          |
|  -----------------                                          |
|                                                              |
|  ubuntu:22.04          ############################ 77MB    |
|  debian:bookworm-slim  #################### 50MB            |
|  node:18               ############################## 900MB |
|  node:18-slim          ############### 180MB                |
|  node:18-alpine        ###### 50MB                          |
|  python:3.11           ############################## 1GB   |
|  python:3.11-slim      ############ 125MB                   |
|  python:3.11-alpine    ##### 45MB                           |
|  golang:1.22           ############################## 800MB |
|  golang:1.22-alpine    ########## 260MB                     |
|  alpine:3.19           # 7MB                                |
|  scratch               | 0MB                                |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🏗️ Multi-Stage Optimization

```dockerfile
# ============================================
# BEFORE: 1.2GB
# ============================================
FROM node:18
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build
CMD ["npm", "start"]

# ============================================
# AFTER: 180MB (85% reduction!)
# ============================================
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
RUN npm prune --production
CMD ["node", "dist/index.js"]
```

---

## ⚡ Distroless Images

```dockerfile
# Go with Distroless (20MB total!)
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /app/server

FROM gcr.io/distroless/static:nonroot
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]

# Node with Distroless
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM gcr.io/distroless/nodejs18-debian12
COPY --from=builder /app/dist /app
WORKDIR /app
CMD ["index.js"]
```

---

## 🎯 .dockerignore Best Practices

```
# .dockerignore
# Git
.git
.gitignore

# Dependencies (install fresh)
node_modules
vendor
venv

# Build artifacts
dist
build
*.pyc
__pycache__

# Development files
*.md
*.txt
docs/
tests/
coverage/
.env*

# IDE
.vscode
.idea

# Docker
Dockerfile*
docker-compose*
.docker

# OS files
.DS_Store
Thumbs.db
```

---

## 📊 Analyze Image

```bash
# Se image layers
docker history myimage:latest

# Detaljerad layer-info
docker history --no-trunc myimage:latest

# Med dive (interaktiv)
dive myimage:latest

# Jämför images
docker images --format "{{.Repository}}:{{.Tag}}\t{{.Size}}"

# Exportera och analysera
docker save myimage:latest | tar -tv
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Optimize Python App
```dockerfile
# Optimized Python Dockerfile
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

# Copy only runtime deps
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["python", "main.py"]
```

---

## 📚 Sammanfattning

| Teknik | Effekt |
|--------|--------|
| Alpine base | -70% storlek |
| Multi-stage | -80% storlek |
| .dockerignore | Snabbare build |
| Layer caching | Snabbare rebuild |
| Distroless | Minimal + secure |

**Nästa steg:** Docker Healthchecks & Recovery

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Docker Healthchecks & Self-Healing",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 150,
        "content": r"""
# 🏥 Docker Healthchecks & Self-Healing

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Implementera robusta healthchecks
- Konfigurera restart policies
- Self-healing patterns
- Integration med orchestrators

---

## 📖 Healthcheck Anatomy

```dockerfile
HEALTHCHECK [OPTIONS] CMD command

# Options:
# --interval=30s   Tid mellan checks (default 30s)
# --timeout=30s    Timeout för check (default 30s)
# --start-period=0s  Grace period vid start
# --retries=3      Antal failures före unhealthy

# Exit codes:
# 0 = healthy
# 1 = unhealthy
# 2 = reserved
```

---

## 🔧 Healthcheck Examples

```dockerfile
# HTTP endpoint
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Utan curl (använd wget)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

# TCP port check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD nc -z localhost 8080 || exit 1

# Database connection
HEALTHCHECK --interval=30s --timeout=5s \
  CMD pg_isready -h localhost -p 5432 || exit 1

# Redis ping
HEALTHCHECK --interval=30s --timeout=3s \
  CMD redis-cli ping | grep -q PONG || exit 1

# Custom script
HEALTHCHECK --interval=30s --timeout=5s \
  CMD /app/healthcheck.sh || exit 1
```

---

## 🔄 Restart Policies

```bash
# no - Starta aldrig om (default)
docker run --restart=no myapp

# on-failure - Restart vid non-zero exit
docker run --restart=on-failure myapp
docker run --restart=on-failure:5 myapp  # Max 5 retries

# always - Starta alltid om
docker run --restart=always myapp

# unless-stopped - Som always, men inte efter manuell stop
docker run --restart=unless-stopped myapp
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi:latest
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

---

## 📊 Health Status

```bash
# Se health status
docker ps
# CONTAINER ID   IMAGE   STATUS
# abc123         myapi   Up 2 min (healthy)

# Detaljerad health info
docker inspect --format='{{json .State.Health}}' mycontainer | jq

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
```

---

## 🎯 Application Health Endpoint

```python
# FastAPI health endpoint
from fastapi import FastAPI, Response
import asyncpg

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/ready")
async def readiness_check():
    # Check all dependencies
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "external_api": await check_external_api()
    }

    all_healthy = all(checks.values())
    status_code = 200 if all_healthy else 503

    return Response(
        content=json.dumps(checks),
        status_code=status_code
    )
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Complete Health Setup
```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 30s
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
```

---

## 📚 Sammanfattning

| Policy | Use Case |
|--------|----------|
| no | Development, oneshot tasks |
| on-failure | Batch jobs |
| always | Production services |
| unless-stopped | Services med manuell kontroll |

**Nästa steg:** Docker Logging Strategies

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Docker Logging Strategies",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 150,
        "content": r"""
# 📋 Docker Logging Strategies

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Docker logging drivers
- Strukturerad logging
- Centraliserad log aggregation
- Log management best practices

---

## 📖 Logging Architecture

```
+-------------------------------------------------------------+
|                  LOGGING PIPELINE                            |
+-------------------------------------------------------------+
|                                                              |
|  Container          Log Driver          Destination          |
|  +---------+       +---------+        +-----------------+  |
|  |  App    |------▶|json-file|-------▶|  Local file     |  |
|  |(stdout) |       |         |        |  /var/lib/docker|  |
|  +---------+       +---------+        +-----------------+  |
|                                                              |
|  +---------+       +---------+        +-----------------+  |
|  |  App    |------▶| fluentd |-------▶| Elasticsearch   |  |
|  |(stdout) |       |         |        | Loki, etc       |  |
|  +---------+       +---------+        +-----------------+  |
|                                                              |
|  +---------+       +---------+        +-----------------+  |
|  |  App    |------▶| awslogs |-------▶| CloudWatch      |  |
|  |(stdout) |       |         |        |                 |  |
|  +---------+       +---------+        +-----------------+  |
|                                                              |
+-------------------------------------------------------------+
```

---

## 🔧 Logging Drivers

```bash
# Se default logging driver
docker info | grep "Logging Driver"

# Kör med specifik driver
docker run --log-driver json-file --log-opt max-size=10m nginx

# Available drivers:
# - json-file (default)
# - local
# - syslog
# - journald
# - fluentd
# - awslogs
# - gcplogs
# - none
```

---

## 📝 JSON-File Driver (Default)

```bash
# Konfigurera json-file
docker run -d \
  --name myapp \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  --log-opt labels=environment,app \
  --label environment=production \
  --label app=api \
  myapp:latest

# Hitta log filer
docker inspect --format='{{.LogPath}}' myapp

# Läs loggar
docker logs myapp
docker logs --tail 100 -f myapp
docker logs --since 2024-01-01T00:00:00 myapp
```

```json
// /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

---

## 🌐 Centralized Logging

```yaml
# docker-compose.yml med Loki
version: '3.8'

services:
  app:
    image: myapp:latest
    logging:
      driver: loki
      options:
        loki-url: "http://loki:3100/loki/api/v1/push"
        loki-batch-size: "400"

  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    volumes:
      - loki_data:/loki

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_AUTH_ANONYMOUS_ENABLED=true

volumes:
  loki_data:
```

---

## 📊 Structured Logging

```python
# Python structured logging
import json
import logging
import sys

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id
        return json.dumps(log_record)

# Setup
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("Request processed", extra={"request_id": "abc123"})
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Log Management Stack
```yaml
version: '3.8'

services:
  app:
    image: nginx
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
        labels: "app,environment"
    labels:
      app: "nginx"
      environment: "dev"
```

---

## 📚 Sammanfattning

| Driver | Use Case |
|--------|----------|
| json-file | Development, small scale |
| fluentd | Centralized logging |
| awslogs | AWS infrastructure |
| loki | Grafana ecosystem |

**Nästa steg:** Complete Docker Project

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Complete Docker DevOps Project",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 180,
        "content": r"""
# 🎯 Complete Docker DevOps Project

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Bygga production-ready Docker setup
- CI/CD pipeline med Docker
- Full-stack deployment
- Monitoring och observability

---

## 🏗️ Project Structure

```
myproject/
+-- apps/
|   +-- frontend/
|   |   +-- Dockerfile
|   |   +-- ...
|   +-- api/
|   |   +-- Dockerfile
|   |   +-- ...
|   +-- worker/
|       +-- Dockerfile
|       +-- ...
+-- docker/
|   +-- nginx/
|   |   +-- nginx.conf
|   +-- prometheus/
|       +-- prometheus.yml
+-- docker-compose.yml
+-- docker-compose.override.yml
+-- docker-compose.prod.yml
+-- .dockerignore
+-- .env.example
+-- Makefile
```

---

## 📝 Production Compose

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      api:
        condition: service_healthy
    restart: always

  frontend:
    image: ${REGISTRY}/frontend:${VERSION}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3

  api:
    image: ${REGISTRY}/api:${VERSION}
    environment:
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASS}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M

  worker:
    image: ${REGISTRY}/worker:${VERSION}
    environment:
      - DATABASE_URL=postgresql://${DB_USER}:${DB_PASS}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379
    depends_on:
      - api
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASS}
      - POSTGRES_DB=${DB_NAME}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

---

## 🔧 Makefile

```makefile
.PHONY: build push deploy

VERSION ?= $(shell git rev-parse --short HEAD)
REGISTRY ?= ghcr.io/myorg

build:
	docker compose build

build-prod:
	docker build -t $(REGISTRY)/api:$(VERSION) ./apps/api
	docker build -t $(REGISTRY)/frontend:$(VERSION) ./apps/frontend
	docker build -t $(REGISTRY)/worker:$(VERSION) ./apps/worker

push:
	docker push $(REGISTRY)/api:$(VERSION)
	docker push $(REGISTRY)/frontend:$(VERSION)
	docker push $(REGISTRY)/worker:$(VERSION)

deploy:
	VERSION=$(VERSION) docker compose -f docker-compose.prod.yml up -d

logs:
	docker compose logs -f

clean:
	docker compose down -v
	docker system prune -af
```

---

## 🚀 GitHub Actions CI/CD

```yaml
# .github/workflows/docker.yml
name: Build and Deploy

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push API
        uses: docker/build-push-action@v5
        with:
          context: ./apps/api
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ github.repository }}/api:${{ github.sha }}
            ${{ env.REGISTRY }}/${{ github.repository }}/api:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to server
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /app
            docker compose pull
            VERSION=${{ github.sha }} docker compose up -d
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Deploy Complete Stack
```bash
# Starta alla services
make build
docker compose up -d

# Verifiera health
docker compose ps

# Se loggar
docker compose logs -f api

# Deploy ny version
make build-prod VERSION=v1.0.0
make push VERSION=v1.0.0
make deploy VERSION=v1.0.0
```

---

## 📚 Sammanfattning

| Komponent | Teknologi |
|-----------|-----------|
| Build | Multi-stage, BuildKit |
| Registry | GHCR, ECR, Harbor |
| Orchestration | Compose, Swarm, K8s |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus, Grafana |

**🎉 Grattis! Du har slutfört Docker Mastery!**

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
]
