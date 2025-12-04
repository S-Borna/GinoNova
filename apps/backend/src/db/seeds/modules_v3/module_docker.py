"""
Docker Mastery - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: containers-orchestration
Tasks: 40
Estimated Hours: 25
"""

MODULE_DOCKER_MASTERY = {
    "track_slug": "containers-orchestration",
    "order_index": 100,
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": """Behärska containerisering från grunden till produktion""",
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ['linux-fundamentals'],
    "tasks": [
            {
                "title": "Docker Introduktion",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 100,
                "content": r"""
# Docker Introduktion

Containers revolutionerade hur vi bygger och deployar applikationer.

## Varför Docker?

| Problem | Docker-lösning |
|---------|----------------|
| "Works on my machine" | Identisk miljö överallt |
| Tunga VMs | Lättvikts-containers |
| Dependency hell | Isolerade beroenden |
| Långsam deploy | Sekunder att starta |

## Installation

```bash
# macOS
brew install --cask docker

# Ubuntu
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Verifiera
docker --version
docker run hello-world
```

## Grundläggande Kommandon

```bash
# Kör container
docker run nginx

# Lista containers
docker ps        # Körande
docker ps -a     # Alla

# Stoppa/ta bort
docker stop <id>
docker rm <id>
```

## Container vs VM

```
┌─────────────────────────────────────┐
│           Containers                │
├─────────┬─────────┬─────────────────┤
│  App A  │  App B  │     App C       │
├─────────┴─────────┴─────────────────┤
│           Docker Engine             │
├─────────────────────────────────────┤
│           Host OS (Linux)           │
└─────────────────────────────────────┘
```

**Nästa steg:** Node 2 - Docker Images

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Images",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 120,
                "content": r"""
# Docker Images

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Images är blueprints för containers.

## Image Kommandon

```bash
# Sök images
docker search python

# Ladda ner image
docker pull python:3.11-slim

# Lista images
docker images

# Ta bort image
docker rmi python:3.11

# Image info
docker inspect python:3.11
```

## Image Naming

```
registry/repository:tag

docker.io/library/python:3.11-slim
└──────┘ └──────┘ └────┘ └────────┘
registry  org     image    tag
```

## Layers

```bash
# Se layers
docker history python:3.11-slim

# Varje instruktion = ny layer
FROM python:3.11-slim     # Layer 1
COPY . /app               # Layer 2
RUN pip install           # Layer 3
```

## Taggar

```bash
# Tagga image
docker tag myapp:latest myapp:v1.0.0
docker tag myapp:latest registry.com/myapp:v1.0.0

# Push till registry
docker push registry.com/myapp:v1.0.0
```

| Tag | Användning |
|-----|-----------|
| latest | Default (undvik i prod) |
| v1.0.0 | Semantisk version |
| sha-abc123 | Git commit |
| slim/alpine | Mindre variant |

**Nästa steg:** Node 3 - Dockerfile Basics

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Dockerfile Basics",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 140,
                "content": r"""
# Dockerfile Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Dockerfile definierar hur en image byggs.

## Grundläggande Dockerfile

```dockerfile
# Base image
FROM python:3.11-slim

# Metadata
LABEL maintainer="dev@example.com"

# Arbetskatalog
WORKDIR /app

# Kopiera filer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponera port
EXPOSE 8000

# Startkommando
CMD ["python", "app.py"]
```

## Bygga Image

```bash
# Bygg image
docker build -t myapp:v1 .

# Med annan Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# No cache
docker build --no-cache -t myapp:v1 .
```

## Viktiga Instruktioner

| Instruktion | Syfte |
|-------------|-------|
| FROM | Base image |
| WORKDIR | Sätt arbetskatalog |
| COPY | Kopiera filer |
| RUN | Kör kommando (build-time) |
| CMD | Default kommando (runtime) |
| ENTRYPOINT | Fast startpunkt |
| EXPOSE | Dokumentera port |
| ENV | Miljövariabler |

## RUN vs CMD vs ENTRYPOINT

```dockerfile
# RUN - körs vid build
RUN apt-get update && apt-get install -y curl

# CMD - default kommando (kan överskrivas)
CMD ["python", "app.py"]

# ENTRYPOINT - fast kommando
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argument till ENTRYPOINT
```

**Nästa steg:** Node 4 - Container Lifecycle

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Container Lifecycle",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Container Lifecycle

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Förstå containers livscykel.

## Lifecycle States

```
Created → Running → Paused → Stopped → Removed
```

## Hantera Containers

```bash
# Skapa utan starta
docker create --name myapp nginx

# Starta
docker start myapp

# Pausa/återuppta
docker pause myapp
docker unpause myapp

# Stoppa (graceful)
docker stop myapp

# Döda (force)
docker kill myapp

# Ta bort
docker rm myapp

# Starta och ta bort automatiskt
docker run --rm nginx
```

## Interaktiva Containers

```bash
# Interaktiv terminal
docker run -it ubuntu bash

# Attach till körande container
docker attach myapp

# Exec kommando i container
docker exec -it myapp bash
docker exec myapp ls -la /app
```

## Logs & Stats

```bash
# Se logs
docker logs myapp
docker logs -f myapp        # Follow
docker logs --tail 100 myapp

# Resource usage
docker stats
docker stats myapp

# Inspect container
docker inspect myapp
```

## Cleanup

```bash
# Ta bort stoppade containers
docker container prune

# Ta bort oanvända images
docker image prune

# Ta bort allt oanvänt
docker system prune -a
```

**Nästa steg:** Node 5 - Docker Volumes

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Volumes",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 135,
                "content": r"""
# Docker Volumes

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Persistent data i Docker.

## Volume-typer

```bash
# Named volume (rekommenderat)
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host path)
docker run -v /host/path:/container/path nginx
docker run -v $(pwd):/app nginx

# tmpfs (in-memory)
docker run --tmpfs /tmp nginx
```

## Volume Kommandon

```bash
# Lista volumes
docker volume ls

# Inspektera
docker volume inspect mydata

# Ta bort
docker volume rm mydata

# Ta bort oanvända
docker volume prune
```

## Praktiskt Exempel

```bash
# PostgreSQL med persistent data
docker run -d \
  --name postgres \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:15

# Backup volume
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata.tar.gz /data
```

## Read-only Mounts

```bash
# Read-only
docker run -v myconfig:/etc/config:ro nginx

# Read-write (default)
docker run -v mydata:/data:rw nginx
```

**Nästa steg:** Node 6 - Docker Networking

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Networking",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# Docker Networking

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Container-kommunikation.

## Network Drivers

| Driver | Användning |
|--------|-----------|
| bridge | Default, isolerat nätverk |
| host | Delad med host |
| none | Ingen nätverksåtkomst |
| overlay | Multi-host (Swarm) |

## Network Kommandon

```bash
# Lista nätverk
docker network ls

# Skapa nätverk
docker network create mynet

# Inspektera
docker network inspect mynet

# Koppla container
docker network connect mynet myapp
docker network disconnect mynet myapp
```

## Container DNS

```bash
# Containers på samma nätverk kan nå varandra via namn
docker network create app-net

docker run -d --name db --network app-net postgres
docker run -d --name api --network app-net myapi

# Inuti api-container:
# postgres://db:5432/mydb  # "db" resolvas automatiskt
```

## Port Mapping

```bash
# Publicera port
docker run -p 8080:80 nginx      # host:container
docker run -p 80 nginx           # Random host port
docker run -P nginx              # Alla EXPOSE:ade portar

# Bind till specifik IP
docker run -p 127.0.0.1:8080:80 nginx
```

## Praktiskt Exempel

```bash
# Frontend + Backend + DB
docker network create myapp

docker run -d --name db \
  --network myapp \
  -e POSTGRES_PASSWORD=secret \
  postgres

docker run -d --name api \
  --network myapp \
  -e DATABASE_URL=postgres://db:5432 \
  myapi

docker run -d --name web \
  --network myapp \
  -p 80:80 \
  -e API_URL=http://api:3000 \
  myfrontend
```

**Nästa steg:** Node 7 - Docker Compose Basics

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Docker Compose Basics",
                "difficulty": "easy",
                "estimated_minutes": 60,
                "xp_reward": 155,
                "content": r"""
# Docker Compose Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Multi-container applikationer.

## docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret

volumes:
  pgdata:
```

## Compose Kommandon

```bash
# Starta alla services
docker compose up
docker compose up -d          # Detached

# Stoppa
docker compose down
docker compose down -v        # + ta bort volumes

# Bygg om images
docker compose build
docker compose up --build

# Logs
docker compose logs
docker compose logs -f api

# Skala services
docker compose up -d --scale api=3
```

## Service Kommandon

```bash
# Kör kommando i service
docker compose exec api bash
docker compose exec db psql -U postgres

# Starta enskild service
docker compose up -d db

# Restart
docker compose restart api
```

**Nästa steg:** Node 8 - Docker Compose Advanced

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Docker Compose Advanced",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Compose Advanced

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Avancerade Compose-features.

## Miljövariabler

```yaml
# .env fil
services:
  api:
    environment:
      - DB_HOST=${DB_HOST:-localhost}
    env_file:
      - .env
      - .env.local
```

## Health Checks

```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
```

## Depends On med Condition

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
```

## Profiles

```yaml
services:
  web:
    profiles: ["frontend"]

  api:
    profiles: ["backend", "full"]

  debug:
    profiles: ["debug"]
    image: busybox

# docker compose --profile backend up
```

## Override Files

```yaml
# docker-compose.yml (base)
services:
  api:
    image: myapi:latest

# docker-compose.override.yml (dev - auto-loaded)
services:
  api:
    build: .
    volumes:
      - ./src:/app/src

# docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## Networks & Aliases

```yaml
services:
  api:
    networks:
      frontend:
        aliases:
          - backend-api
      backend:

networks:
  frontend:
  backend:
    internal: true  # Ingen extern åtkomst
```

**Nästa steg:** Node 9 - Dockerfile Best Practices

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Dockerfile Best Practices",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Dockerfile Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Optimera dina Docker images.

## Layer Caching

```dockerfile
# ❌ Dåligt - cache invalideras varje gång
COPY . .
RUN pip install -r requirements.txt

# ✅ Bra - dependencies cachas separat
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

## Minimera Layers

```dockerfile
# ❌ Flera layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git

# ✅ En layer + cleanup
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*
```

## Använd .dockerignore

```dockerignore
# .dockerignore
.git
node_modules
__pycache__
*.pyc
.env
.venv
Dockerfile
docker-compose.yml
README.md
tests/
```

## Specifika Base Images

```dockerfile
# ❌ Undvik latest
FROM python:latest

# ✅ Specifik version
FROM python:3.11.4-slim-bookworm
```

## Non-root User

```dockerfile
# Skapa user
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/app
```

| Tip | Varför |
|-----|--------|
| Små base images | Mindre attack surface |
| Specifika tags | Reproducerbarhet |
| Layer order | Bättre caching |
| .dockerignore | Snabbare builds |

**Nästa steg:** Node 10 - Multi-stage Builds

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Multi-stage Builds",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# Multi-stage Builds

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Mindre production images.

## Grundläggande Multi-stage

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## Python Exempel

```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt
RUN pip wheel --no-cache-dir -w /wheels -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY src/ ./src/
CMD ["python", "-m", "src.main"]
```

## Go Scratch Image

```dockerfile
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o /app/server

FROM scratch
COPY --from=builder /app/server /server
ENTRYPOINT ["/server"]
# Resultat: ~10MB image!
```

## Bygg Specifik Stage

```bash
# Bygg endast builder stage
docker build --target builder -t myapp:builder .

# Bygg production
docker build --target production -t myapp:prod .
```

**Nästa steg:** Node 11 - Docker Security

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Security",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Docker Security

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Säkra dina containers.

## Non-root Containers

```dockerfile
FROM python:3.11-slim

# Skapa non-root user
RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser

WORKDIR /app
COPY --chown=appuser:appgroup . .

USER appuser
CMD ["python", "app.py"]
```

## Read-only Filesystem

```bash
docker run --read-only \
  --tmpfs /tmp \
  --tmpfs /var/run \
  myapp
```

## Resource Limits

```bash
docker run \
  --memory=512m \
  --memory-swap=512m \
  --cpus=1.5 \
  --pids-limit=100 \
  myapp
```

## Security Scanning

```bash
# Trivy scan
docker run aquasec/trivy image myapp:latest

# Docker Scout
docker scout cves myapp:latest

# Snyk
snyk container test myapp:latest
```

## Secrets Management

```yaml
# docker-compose.yml
services:
  api:
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Security Checklist

| Check | Kommando/Åtgärd |
|-------|-----------------|
| Non-root | USER i Dockerfile |
| No secrets | Använd secrets/env |
| Scan images | trivy/scout |
| Limit resources | --memory/--cpus |
| Minimal base | alpine/distroless |

**Nästa steg:** Node 12 - Docker Registry

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Registry",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Docker Registry

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Lagra och distribuera images.

## Docker Hub

```bash
# Logga in
docker login

# Tagga för push
docker tag myapp:v1 username/myapp:v1

# Push
docker push username/myapp:v1

# Pull
docker pull username/myapp:v1
```

## Private Registry

```bash
# Kör lokal registry
docker run -d -p 5000:5000 --name registry registry:2

# Push till lokal
docker tag myapp localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
```

## Cloud Registries

```bash
# AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin 123456.dkr.ecr.eu-west-1.amazonaws.com
docker push 123456.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1

# Google GCR
gcloud auth configure-docker
docker push gcr.io/project-id/myapp:v1

# Azure ACR
az acr login --name myregistry
docker push myregistry.azurecr.io/myapp:v1
```

## GitHub Container Registry

```bash
# Login
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Push
docker tag myapp ghcr.io/username/myapp:v1
docker push ghcr.io/username/myapp:v1
```

| Registry | URL |
|----------|-----|
| Docker Hub | docker.io |
| GitHub | ghcr.io |
| AWS ECR | *.dkr.ecr.*.amazonaws.com |
| Google | gcr.io |
| Azure | *.azurecr.io |

**Nästa steg:** Node 13 - Docker in CI/CD

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker in CI/CD",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker in CI/CD

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisera Docker builds.

## GitHub Actions

```yaml
name: Build and Push

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## GitLab CI

```yaml
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

## Layer Caching i CI

```yaml
# GitHub Actions med cache
- uses: docker/build-push-action@v5
  with:
    cache-from: type=registry,ref=ghcr.io/org/app:cache
    cache-to: type=registry,ref=ghcr.io/org/app:cache,mode=max
```

**Nästa steg:** Node 14 - Docker Debugging

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Docker Debugging",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Docker Debugging

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Felsök containers effektivt.

## Container Inspection

```bash
# Full inspect
docker inspect myapp

# Specifika fält
docker inspect -f '{{.State.Status}}' myapp
docker inspect -f '{{.NetworkSettings.IPAddress}}' myapp
docker inspect -f '{{json .Config.Env}}' myapp | jq
```

## Logs

```bash
# Se logs
docker logs myapp
docker logs -f myapp              # Follow
docker logs --tail 100 myapp      # Senaste 100
docker logs --since 1h myapp      # Senaste timmen
docker logs -t myapp              # Med timestamps
```

## Exec in Container

```bash
# Shell access
docker exec -it myapp bash
docker exec -it myapp sh          # Om ingen bash

# Kör kommando
docker exec myapp cat /etc/hosts
docker exec myapp env
docker exec myapp ps aux
```

## Debug Stopped Container

```bash
# Skapa image från stoppad container
docker commit dead_container debug_image

# Starta med override
docker run -it --entrypoint bash debug_image
```

## Container Events

```bash
# Realtid events
docker events

# Filtrera
docker events --filter container=myapp
docker events --filter event=die
```

## Resource Monitoring

```bash
# Live stats
docker stats
docker stats myapp

# Top processes
docker top myapp
```

| Verktyg | Användning |
|---------|-----------|
| inspect | Metadata/config |
| logs | Application output |
| exec | Kör kommandon |
| events | Lifecycle events |
| stats | Resource usage |

**Nästa steg:** Node 15 - Docker Build Optimization

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Build Optimization",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Build Optimization

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Snabbare och mindre builds.

## BuildKit

```bash
# Aktivera BuildKit
export DOCKER_BUILDKIT=1

# Eller i docker build
docker buildx build -t myapp .
```

## Parallel Builds

```dockerfile
# Parallella stages med BuildKit
FROM node:18 AS frontend
WORKDIR /frontend
COPY frontend/ .
RUN npm ci && npm run build

FROM python:3.11 AS backend
WORKDIR /backend
COPY backend/ .
RUN pip install -r requirements.txt

FROM nginx:alpine
COPY --from=frontend /frontend/dist /usr/share/nginx/html
COPY --from=backend /backend /app
```

## Cache Mounts

```dockerfile
# Cache pip downloads
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Cache npm
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

## Secret Mounts

```dockerfile
# Säker secret hantering
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci

# Build med secret
docker build --secret id=npmrc,src=.npmrc .
```

## Image Size Tips

```bash
# Jämför image storlekar
docker images --format "table {{.Repository}}:{{.Tag}}	{{.Size}}"

# Analysera layers
docker history myapp:latest
dive myapp:latest  # Interaktivt verktyg
```

| Optimering | Effekt |
|------------|--------|
| Multi-stage | Mindre prod image |
| Cache mounts | Snabbare rebuilds |
| Alpine/slim | Mindre base |
| .dockerignore | Snabbare context |

**Nästa steg:** Node 16 - Docker Healthchecks

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Docker Healthchecks",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Docker Healthchecks

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisk hälsokontroll.

## Dockerfile HEALTHCHECK

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm ci

HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=5s \
  CMD curl -f http://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

## Health Status

```bash
# Se health status
docker ps
# CONTAINER   STATUS
# abc123      Up 2m (healthy)

# Detaljerad health info
docker inspect --format='{{json .State.Health}}' myapp | jq
```

## Compose Healthcheck

```yaml
services:
  api:
    build: .
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
```

## Wait for Dependencies

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
```

## Healthcheck Patterns

| Service | Test Command |
|---------|--------------|
| HTTP API | curl -f http://localhost/health |
| PostgreSQL | pg_isready -U user |
| Redis | redis-cli ping |
| MySQL | mysqladmin ping |

**Nästa steg:** Node 17 - Docker Swarm Basics

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Swarm Basics",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Swarm Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Native Docker orchestration.

## Initiera Swarm

```bash
# Skapa swarm
docker swarm init

# Join token för workers
docker swarm join-token worker

# Join token för managers
docker swarm join-token manager

# Lista nodes
docker node ls
```

## Services

```bash
# Skapa service
docker service create \
  --name web \
  --replicas 3 \
  -p 80:80 \
  nginx

# Lista services
docker service ls

# Skala
docker service scale web=5

# Uppdatera
docker service update --image nginx:latest web
```

## Stack Deploy

```yaml
# docker-stack.yml
version: '3.8'
services:
  web:
    image: nginx
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
```

```bash
# Deploy stack
docker stack deploy -c docker-stack.yml myapp

# Lista stacks
docker stack ls

# Stack services
docker stack services myapp
```

**Nästa steg:** Node 18 - Production Patterns

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Production Patterns",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# Docker Production Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Best practices för produktion.

## Logging

```bash
# JSON logging driver
docker run --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  myapp

# Compose logging
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Restart Policies

```bash
docker run --restart=always myapp

# Policies:
# no           - Aldrig
# on-failure   - Vid exit code != 0
# always       - Alltid
# unless-stopped - Alltid utom manuellt stoppad
```

## Resource Constraints

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 256M
```

## Rolling Updates

```yaml
services:
  app:
    deploy:
      update_config:
        parallelism: 2
        delay: 10s
        failure_action: rollback
        order: start-first
      rollback_config:
        parallelism: 1
        delay: 10s
```

## Graceful Shutdown

```dockerfile
# Dockerfile
STOPSIGNAL SIGTERM

# docker-compose.yml
services:
  app:
    stop_grace_period: 30s
```

**Nästa steg:** Node 19 - Docker Monitoring

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Monitoring",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Docker Monitoring

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Övervaka containers i produktion.

## cAdvisor

```bash
docker run -d \
  --name cadvisor \
  -p 8080:8080 \
  -v /:/rootfs:ro \
  -v /var/run:/var/run:ro \
  -v /sys:/sys:ro \
  -v /var/lib/docker/:/var/lib/docker:ro \
  gcr.io/cadvisor/cadvisor
```

## Prometheus + Docker

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'docker'
    static_configs:
      - targets: ['host.docker.internal:9323']

# docker-compose.yml
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
```

## Docker Daemon Metrics

```json
// /etc/docker/daemon.json
{
  "metrics-addr": "0.0.0.0:9323",
  "experimental": true
}
```

## Grafana Dashboard

```yaml
services:
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

| Metric | Beskrivning |
|--------|-------------|
| container_cpu_usage | CPU användning |
| container_memory_usage | Minne |
| container_network_receive | Nätverkstrafik |
| container_fs_usage | Diskutrymme |

**Nästa steg:** Node 20 - Docker at Scale

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker at Scale",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 170,
                "content": r"""
# Docker at Scale

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Enterprise Docker patterns.

## Overlay Networks

```bash
# Multi-host networking
docker network create \
  --driver overlay \
  --attachable \
  myoverlay
```

## Service Discovery

```yaml
services:
  api:
    deploy:
      replicas: 3
    networks:
      - backend

  nginx:
    image: nginx
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

configs:
  nginx_conf:
    file: ./nginx.conf
```

## Secrets at Scale

```bash
# Skapa secret
echo "supersecret" | docker secret create db_password -

# Använd i service
docker service create \
  --name db \
  --secret db_password \
  postgres
```

## Build Farm

```bash
# Skapa buildx builder
docker buildx create --name mybuilder --use

# Multi-platform build
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --push \
  -t myapp:latest .
```

## Enterprise Checklist

| Område | Implementation |
|--------|----------------|
| HA Registry | Harbor/ECR |
| Logging | ELK/Loki |
| Monitoring | Prometheus+Grafana |
| Security | Trivy scanning |
| Orchestration | Kubernetes/Swarm |
| Backup | Volume snapshots |

**🎉 Grattis! Du har slutfört Docker Mastery SkillsMap!**

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Introduktion",
                "difficulty": "hard",
                "estimated_minutes": 45,
                "xp_reward": 100,
                "content": r"""
# Docker Introduktion

Containers revolutionerade hur vi bygger och deployar applikationer.

## Varför Docker?

| Problem | Docker-lösning |
|---------|----------------|
| "Works on my machine" | Identisk miljö överallt |
| Tunga VMs | Lättvikts-containers |
| Dependency hell | Isolerade beroenden |
| Långsam deploy | Sekunder att starta |

## Installation

```bash
# macOS
brew install --cask docker

# Ubuntu
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER

# Verifiera
docker --version
docker run hello-world
```

## Grundläggande Kommandon

```bash
# Kör container
docker run nginx

# Lista containers
docker ps        # Körande
docker ps -a     # Alla

# Stoppa/ta bort
docker stop <id>
docker rm <id>
```

## Container vs VM

```
┌─────────────────────────────────────┐
│           Containers                │
├─────────┬─────────┬─────────────────┤
│  App A  │  App B  │     App C       │
├─────────┴─────────┴─────────────────┤
│           Docker Engine             │
├─────────────────────────────────────┤
│           Host OS (Linux)           │
└─────────────────────────────────────┘
```

**Nästa steg:** Node 2 - Docker Images

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Docker Images",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 120,
                "content": r"""
# Docker Images

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Images är blueprints för containers.

## Image Kommandon

```bash
# Sök images
docker search python

# Ladda ner image
docker pull python:3.11-slim

# Lista images
docker images

# Ta bort image
docker rmi python:3.11

# Image info
docker inspect python:3.11
```

## Image Naming

```
registry/repository:tag

docker.io/library/python:3.11-slim
└──────┘ └──────┘ └────┘ └────────┘
registry  org     image    tag
```

## Layers

```bash
# Se layers
docker history python:3.11-slim

# Varje instruktion = ny layer
FROM python:3.11-slim     # Layer 1
COPY . /app               # Layer 2
RUN pip install           # Layer 3
```

## Taggar

```bash
# Tagga image
docker tag myapp:latest myapp:v1.0.0
docker tag myapp:latest registry.com/myapp:v1.0.0

# Push till registry
docker push registry.com/myapp:v1.0.0
```

| Tag | Användning |
|-----|-----------|
| latest | Default (undvik i prod) |
| v1.0.0 | Semantisk version |
| sha-abc123 | Git commit |
| slim/alpine | Mindre variant |

**Nästa steg:** Node 3 - Dockerfile Basics

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Dockerfile Basics",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 140,
                "content": r"""
# Dockerfile Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Dockerfile definierar hur en image byggs.

## Grundläggande Dockerfile

```dockerfile
# Base image
FROM python:3.11-slim

# Metadata
LABEL maintainer="dev@example.com"

# Arbetskatalog
WORKDIR /app

# Kopiera filer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponera port
EXPOSE 8000

# Startkommando
CMD ["python", "app.py"]
```

## Bygga Image

```bash
# Bygg image
docker build -t myapp:v1 .

# Med annan Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# No cache
docker build --no-cache -t myapp:v1 .
```

## Viktiga Instruktioner

| Instruktion | Syfte |
|-------------|-------|
| FROM | Base image |
| WORKDIR | Sätt arbetskatalog |
| COPY | Kopiera filer |
| RUN | Kör kommando (build-time) |
| CMD | Default kommando (runtime) |
| ENTRYPOINT | Fast startpunkt |
| EXPOSE | Dokumentera port |
| ENV | Miljövariabler |

## RUN vs CMD vs ENTRYPOINT

```dockerfile
# RUN - körs vid build
RUN apt-get update && apt-get install -y curl

# CMD - default kommando (kan överskrivas)
CMD ["python", "app.py"]

# ENTRYPOINT - fast kommando
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argument till ENTRYPOINT
```

**Nästa steg:** Node 4 - Container Lifecycle

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Container Lifecycle",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 130,
                "content": r"""
# Container Lifecycle

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Förstå containers livscykel.

## Lifecycle States

```
Created → Running → Paused → Stopped → Removed
```

## Hantera Containers

```bash
# Skapa utan starta
docker create --name myapp nginx

# Starta
docker start myapp

# Pausa/återuppta
docker pause myapp
docker unpause myapp

# Stoppa (graceful)
docker stop myapp

# Döda (force)
docker kill myapp

# Ta bort
docker rm myapp

# Starta och ta bort automatiskt
docker run --rm nginx
```

## Interaktiva Containers

```bash
# Interaktiv terminal
docker run -it ubuntu bash

# Attach till körande container
docker attach myapp

# Exec kommando i container
docker exec -it myapp bash
docker exec myapp ls -la /app
```

## Logs & Stats

```bash
# Se logs
docker logs myapp
docker logs -f myapp        # Follow
docker logs --tail 100 myapp

# Resource usage
docker stats
docker stats myapp

# Inspect container
docker inspect myapp
```

## Cleanup

```bash
# Ta bort stoppade containers
docker container prune

# Ta bort oanvända images
docker image prune

# Ta bort allt oanvänt
docker system prune -a
```

**Nästa steg:** Node 5 - Docker Volumes

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Volumes",
                "difficulty": "hard",
                "estimated_minutes": 50,
                "xp_reward": 135,
                "content": r"""
# Docker Volumes

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Persistent data i Docker.

## Volume-typer

```bash
# Named volume (rekommenderat)
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host path)
docker run -v /host/path:/container/path nginx
docker run -v $(pwd):/app nginx

# tmpfs (in-memory)
docker run --tmpfs /tmp nginx
```

## Volume Kommandon

```bash
# Lista volumes
docker volume ls

# Inspektera
docker volume inspect mydata

# Ta bort
docker volume rm mydata

# Ta bort oanvända
docker volume prune
```

## Praktiskt Exempel

```bash
# PostgreSQL med persistent data
docker run -d \
  --name postgres \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:15

# Backup volume
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata.tar.gz /data
```

## Read-only Mounts

```bash
# Read-only
docker run -v myconfig:/etc/config:ro nginx

# Read-write (default)
docker run -v mydata:/data:rw nginx
```

**Nästa steg:** Node 6 - Docker Networking

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Networking",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 145,
                "content": r"""
# Docker Networking

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Container-kommunikation.

## Network Drivers

| Driver | Användning |
|--------|-----------|
| bridge | Default, isolerat nätverk |
| host | Delad med host |
| none | Ingen nätverksåtkomst |
| overlay | Multi-host (Swarm) |

## Network Kommandon

```bash
# Lista nätverk
docker network ls

# Skapa nätverk
docker network create mynet

# Inspektera
docker network inspect mynet

# Koppla container
docker network connect mynet myapp
docker network disconnect mynet myapp
```

## Container DNS

```bash
# Containers på samma nätverk kan nå varandra via namn
docker network create app-net

docker run -d --name db --network app-net postgres
docker run -d --name api --network app-net myapi

# Inuti api-container:
# postgres://db:5432/mydb  # "db" resolvas automatiskt
```

## Port Mapping

```bash
# Publicera port
docker run -p 8080:80 nginx      # host:container
docker run -p 80 nginx           # Random host port
docker run -P nginx              # Alla EXPOSE:ade portar

# Bind till specifik IP
docker run -p 127.0.0.1:8080:80 nginx
```

## Praktiskt Exempel

```bash
# Frontend + Backend + DB
docker network create myapp

docker run -d --name db \
  --network myapp \
  -e POSTGRES_PASSWORD=secret \
  postgres

docker run -d --name api \
  --network myapp \
  -e DATABASE_URL=postgres://db:5432 \
  myapi

docker run -d --name web \
  --network myapp \
  -p 80:80 \
  -e API_URL=http://api:3000 \
  myfrontend
```

**Nästa steg:** Node 7 - Docker Compose Basics

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Compose Basics",
                "difficulty": "hard",
                "estimated_minutes": 60,
                "xp_reward": 155,
                "content": r"""
# Docker Compose Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Multi-container applikationer.

## docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret

volumes:
  pgdata:
```

## Compose Kommandon

```bash
# Starta alla services
docker compose up
docker compose up -d          # Detached

# Stoppa
docker compose down
docker compose down -v        # + ta bort volumes

# Bygg om images
docker compose build
docker compose up --build

# Logs
docker compose logs
docker compose logs -f api

# Skala services
docker compose up -d --scale api=3
```

## Service Kommandon

```bash
# Kör kommando i service
docker compose exec api bash
docker compose exec db psql -U postgres

# Starta enskild service
docker compose up -d db

# Restart
docker compose restart api
```

**Nästa steg:** Node 8 - Docker Compose Advanced

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Compose Advanced",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Compose Advanced

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Avancerade Compose-features.

## Miljövariabler

```yaml
# .env fil
services:
  api:
    environment:
      - DB_HOST=${DB_HOST:-localhost}
    env_file:
      - .env
      - .env.local
```

## Health Checks

```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
```

## Depends On med Condition

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
```

## Profiles

```yaml
services:
  web:
    profiles: ["frontend"]

  api:
    profiles: ["backend", "full"]

  debug:
    profiles: ["debug"]
    image: busybox

# docker compose --profile backend up
```

## Override Files

```yaml
# docker-compose.yml (base)
services:
  api:
    image: myapi:latest

# docker-compose.override.yml (dev - auto-loaded)
services:
  api:
    build: .
    volumes:
      - ./src:/app/src

# docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

## Networks & Aliases

```yaml
services:
  api:
    networks:
      frontend:
        aliases:
          - backend-api
      backend:

networks:
  frontend:
  backend:
    internal: true  # Ingen extern åtkomst
```

**Nästa steg:** Node 9 - Dockerfile Best Practices

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Dockerfile Best Practices",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Dockerfile Best Practices

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Optimera dina Docker images.

## Layer Caching

```dockerfile
# ❌ Dåligt - cache invalideras varje gång
COPY . .
RUN pip install -r requirements.txt

# ✅ Bra - dependencies cachas separat
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

## Minimera Layers

```dockerfile
# ❌ Flera layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git

# ✅ En layer + cleanup
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*
```

## Använd .dockerignore

```dockerignore
# .dockerignore
.git
node_modules
__pycache__
*.pyc
.env
.venv
Dockerfile
docker-compose.yml
README.md
tests/
```

## Specifika Base Images

```dockerfile
# ❌ Undvik latest
FROM python:latest

# ✅ Specifik version
FROM python:3.11.4-slim-bookworm
```

## Non-root User

```dockerfile
# Skapa user
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/app
```

| Tip | Varför |
|-----|--------|
| Små base images | Mindre attack surface |
| Specifika tags | Reproducerbarhet |
| Layer order | Bättre caching |
| .dockerignore | Snabbare builds |

**Nästa steg:** Node 10 - Multi-stage Builds

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Multi-stage Builds",
                "difficulty": "expert",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# Multi-stage Builds

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Mindre production images.

## Grundläggande Multi-stage

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## Python Exempel

```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt
RUN pip wheel --no-cache-dir -w /wheels -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY src/ ./src/
CMD ["python", "-m", "src.main"]
```

## Go Scratch Image

```dockerfile
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o /app/server

FROM scratch
COPY --from=builder /app/server /server
ENTRYPOINT ["/server"]
# Resultat: ~10MB image!
```

## Bygg Specifik Stage

```bash
# Bygg endast builder stage
docker build --target builder -t myapp:builder .

# Bygg production
docker build --target production -t myapp:prod .
```

**Nästa steg:** Node 11 - Docker Security

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Security",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 155,
                "content": r"""
# Docker Security

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Säkra dina containers.

## Non-root Containers

```dockerfile
FROM python:3.11-slim

# Skapa non-root user
RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser

WORKDIR /app
COPY --chown=appuser:appgroup . .

USER appuser
CMD ["python", "app.py"]
```

## Read-only Filesystem

```bash
docker run --read-only \
  --tmpfs /tmp \
  --tmpfs /var/run \
  myapp
```

## Resource Limits

```bash
docker run \
  --memory=512m \
  --memory-swap=512m \
  --cpus=1.5 \
  --pids-limit=100 \
  myapp
```

## Security Scanning

```bash
# Trivy scan
docker run aquasec/trivy image myapp:latest

# Docker Scout
docker scout cves myapp:latest

# Snyk
snyk container test myapp:latest
```

## Secrets Management

```yaml
# docker-compose.yml
services:
  api:
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Security Checklist

| Check | Kommando/Åtgärd |
|-------|-----------------|
| Non-root | USER i Dockerfile |
| No secrets | Använd secrets/env |
| Scan images | trivy/scout |
| Limit resources | --memory/--cpus |
| Minimal base | alpine/distroless |

**Nästa steg:** Node 12 - Docker Registry

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Docker Registry",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Docker Registry

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Lagra och distribuera images.

## Docker Hub

```bash
# Logga in
docker login

# Tagga för push
docker tag myapp:v1 username/myapp:v1

# Push
docker push username/myapp:v1

# Pull
docker pull username/myapp:v1
```

## Private Registry

```bash
# Kör lokal registry
docker run -d -p 5000:5000 --name registry registry:2

# Push till lokal
docker tag myapp localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
```

## Cloud Registries

```bash
# AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin 123456.dkr.ecr.eu-west-1.amazonaws.com
docker push 123456.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1

# Google GCR
gcloud auth configure-docker
docker push gcr.io/project-id/myapp:v1

# Azure ACR
az acr login --name myregistry
docker push myregistry.azurecr.io/myapp:v1
```

## GitHub Container Registry

```bash
# Login
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Push
docker tag myapp ghcr.io/username/myapp:v1
docker push ghcr.io/username/myapp:v1
```

| Registry | URL |
|----------|-----|
| Docker Hub | docker.io |
| GitHub | ghcr.io |
| AWS ECR | *.dkr.ecr.*.amazonaws.com |
| Google | gcr.io |
| Azure | *.azurecr.io |

**Nästa steg:** Node 13 - Docker in CI/CD

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
            },
            {
                "title": "Docker in CI/CD",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker in CI/CD

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisera Docker builds.

## GitHub Actions

```yaml
name: Build and Push

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and Push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## GitLab CI

```yaml
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

## Layer Caching i CI

```yaml
# GitHub Actions med cache
- uses: docker/build-push-action@v5
  with:
    cache-from: type=registry,ref=ghcr.io/org/app:cache
    cache-to: type=registry,ref=ghcr.io/org/app:cache,mode=max
```

**Nästa steg:** Node 14 - Docker Debugging

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Debugging",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 140,
                "content": r"""
# Docker Debugging

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Felsök containers effektivt.

## Container Inspection

```bash
# Full inspect
docker inspect myapp

# Specifika fält
docker inspect -f '{{.State.Status}}' myapp
docker inspect -f '{{.NetworkSettings.IPAddress}}' myapp
docker inspect -f '{{json .Config.Env}}' myapp | jq
```

## Logs

```bash
# Se logs
docker logs myapp
docker logs -f myapp              # Follow
docker logs --tail 100 myapp      # Senaste 100
docker logs --since 1h myapp      # Senaste timmen
docker logs -t myapp              # Med timestamps
```

## Exec in Container

```bash
# Shell access
docker exec -it myapp bash
docker exec -it myapp sh          # Om ingen bash

# Kör kommando
docker exec myapp cat /etc/hosts
docker exec myapp env
docker exec myapp ps aux
```

## Debug Stopped Container

```bash
# Skapa image från stoppad container
docker commit dead_container debug_image

# Starta med override
docker run -it --entrypoint bash debug_image
```

## Container Events

```bash
# Realtid events
docker events

# Filtrera
docker events --filter container=myapp
docker events --filter event=die
```

## Resource Monitoring

```bash
# Live stats
docker stats
docker stats myapp

# Top processes
docker top myapp
```

| Verktyg | Användning |
|---------|-----------|
| inspect | Metadata/config |
| logs | Application output |
| exec | Kör kommandon |
| events | Lifecycle events |
| stats | Resource usage |

**Nästa steg:** Node 15 - Docker Build Optimization

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Build Optimization",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Build Optimization

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Snabbare och mindre builds.

## BuildKit

```bash
# Aktivera BuildKit
export DOCKER_BUILDKIT=1

# Eller i docker build
docker buildx build -t myapp .
```

## Parallel Builds

```dockerfile
# Parallella stages med BuildKit
FROM node:18 AS frontend
WORKDIR /frontend
COPY frontend/ .
RUN npm ci && npm run build

FROM python:3.11 AS backend
WORKDIR /backend
COPY backend/ .
RUN pip install -r requirements.txt

FROM nginx:alpine
COPY --from=frontend /frontend/dist /usr/share/nginx/html
COPY --from=backend /backend /app
```

## Cache Mounts

```dockerfile
# Cache pip downloads
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Cache npm
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

## Secret Mounts

```dockerfile
# Säker secret hantering
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci

# Build med secret
docker build --secret id=npmrc,src=.npmrc .
```

## Image Size Tips

```bash
# Jämför image storlekar
docker images --format "table {{.Repository}}:{{.Tag}}	{{.Size}}"

# Analysera layers
docker history myapp:latest
dive myapp:latest  # Interaktivt verktyg
```

| Optimering | Effekt |
|------------|--------|
| Multi-stage | Mindre prod image |
| Cache mounts | Snabbare rebuilds |
| Alpine/slim | Mindre base |
| .dockerignore | Snabbare context |

**Nästa steg:** Node 16 - Docker Healthchecks

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
            {
                "title": "Docker Healthchecks",
                "difficulty": "expert",
                "estimated_minutes": 45,
                "xp_reward": 130,
                "content": r"""
# Docker Healthchecks

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Automatisk hälsokontroll.

## Dockerfile HEALTHCHECK

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm ci

HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=5s \
  CMD curl -f http://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

## Health Status

```bash
# Se health status
docker ps
# CONTAINER   STATUS
# abc123      Up 2m (healthy)

# Detaljerad health info
docker inspect --format='{{json .State.Health}}' myapp | jq
```

## Compose Healthcheck

```yaml
services:
  api:
    build: .
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
```

## Wait for Dependencies

```yaml
services:
  api:
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
```

## Healthcheck Patterns

| Service | Test Command |
|---------|--------------|
| HTTP API | curl -f http://localhost/health |
| PostgreSQL | pg_isready -U user |
| Redis | redis-cli ping |
| MySQL | mysqladmin ping |

**Nästa steg:** Node 17 - Docker Swarm Basics

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Swarm Basics",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 150,
                "content": r"""
# Docker Swarm Basics

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Native Docker orchestration.

## Initiera Swarm

```bash
# Skapa swarm
docker swarm init

# Join token för workers
docker swarm join-token worker

# Join token för managers
docker swarm join-token manager

# Lista nodes
docker node ls
```

## Services

```bash
# Skapa service
docker service create \
  --name web \
  --replicas 3 \
  -p 80:80 \
  nginx

# Lista services
docker service ls

# Skala
docker service scale web=5

# Uppdatera
docker service update --image nginx:latest web
```

## Stack Deploy

```yaml
# docker-stack.yml
version: '3.8'
services:
  web:
    image: nginx
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
```

```bash
# Deploy stack
docker stack deploy -c docker-stack.yml myapp

# Lista stacks
docker stack ls

# Stack services
docker stack services myapp
```

**Nästa steg:** Node 18 - Production Patterns

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
            },
            {
                "title": "Production Patterns",
                "difficulty": "expert",
                "estimated_minutes": 60,
                "xp_reward": 160,
                "content": r"""
# Docker Production Patterns

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Best practices för produktion.

## Logging

```bash
# JSON logging driver
docker run --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  myapp

# Compose logging
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Restart Policies

```bash
docker run --restart=always myapp

# Policies:
# no           - Aldrig
# on-failure   - Vid exit code != 0
# always       - Alltid
# unless-stopped - Alltid utom manuellt stoppad
```

## Resource Constraints

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 256M
```

## Rolling Updates

```yaml
services:
  app:
    deploy:
      update_config:
        parallelism: 2
        delay: 10s
        failure_action: rollback
        order: start-first
      rollback_config:
        parallelism: 1
        delay: 10s
```

## Graceful Shutdown

```dockerfile
# Dockerfile
STOPSIGNAL SIGTERM

# docker-compose.yml
services:
  app:
    stop_grace_period: 30s
```

**Nästa steg:** Node 19 - Docker Monitoring

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
            },
            {
                "title": "Docker Monitoring",
                "difficulty": "expert",
                "estimated_minutes": 50,
                "xp_reward": 145,
                "content": r"""
# Docker Monitoring

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Övervaka containers i produktion.

## cAdvisor

```bash
docker run -d \
  --name cadvisor \
  -p 8080:8080 \
  -v /:/rootfs:ro \
  -v /var/run:/var/run:ro \
  -v /sys:/sys:ro \
  -v /var/lib/docker/:/var/lib/docker:ro \
  gcr.io/cadvisor/cadvisor
```

## Prometheus + Docker

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'docker'
    static_configs:
      - targets: ['host.docker.internal:9323']

# docker-compose.yml
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
```

## Docker Daemon Metrics

```json
// /etc/docker/daemon.json
{
  "metrics-addr": "0.0.0.0:9323",
  "experimental": true
}
```

## Grafana Dashboard

```yaml
services:
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

| Metric | Beskrivning |
|--------|-------------|
| container_cpu_usage | CPU användning |
| container_memory_usage | Minne |
| container_network_receive | Nätverkstrafik |
| container_fs_usage | Diskutrymme |

**Nästa steg:** Node 20 - Docker at Scale

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
            },
            {
                "title": "Docker at Scale",
                "difficulty": "expert",
                "estimated_minutes": 55,
                "xp_reward": 170,
                "content": r"""
# Docker at Scale

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEVOPS CONTINUOUS FLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│   Code ──▶ Build ──▶ Test ──▶ Deploy ──▶ Monitor ──▶ Feedback      │
└─────────────────────────────────────────────────────────────────────┘
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


Enterprise Docker patterns.

## Overlay Networks

```bash
# Multi-host networking
docker network create \
  --driver overlay \
  --attachable \
  myoverlay
```

## Service Discovery

```yaml
services:
  api:
    deploy:
      replicas: 3
    networks:
      - backend

  nginx:
    image: nginx
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

configs:
  nginx_conf:
    file: ./nginx.conf
```

## Secrets at Scale

```bash
# Skapa secret
echo "supersecret" | docker secret create db_password -

# Använd i service
docker service create \
  --name db \
  --secret db_password \
  postgres
```

## Build Farm

```bash
# Skapa buildx builder
docker buildx create --name mybuilder --use

# Multi-platform build
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --push \
  -t myapp:latest .
```

## Enterprise Checklist

| Område | Implementation |
|--------|----------------|
| HA Registry | Harbor/ECR |
| Logging | ELK/Loki |
| Monitoring | Prometheus+Grafana |
| Security | Trivy scanning |
| Orchestration | Kubernetes/Swarm |
| Backup | Volume snapshots |

**🎉 Grattis! Du har slutfört Docker Mastery SkillsMap!**

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_DOCKER_MASTERY


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_DOCKER_MASTERY["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
