"""
Docker Fundamentals - Tasks 1-10
Premium Bootcamp-Quality Content
"""

TASKS_FUNDAMENTALS = [
    {
        "title": "Docker Fundamentals & Architecture",
        "difficulty": "beginner",
        "estimated_minutes": 45,
        "xp_reward": 120,
        "content": r"""
# 🐳 Docker Fundamentals & Architecture

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


## Lärande mål
- Förstå vad Docker är och varför det revolutionerade deployment
- Lära dig Docker-arkitekturen (daemon, client, registry)
- Förstå skillnaden mellan containers och VMs
- Installera och konfigurera Docker

---

## 📖 Vad är Docker?

Docker är en **containeriseringsplattform** som låter dig paketera applikationer med alla deras dependencies i en standardiserad enhet kallad **container**.

```
┌─────────────────────────────────────────────────────────────┐
│                      DOCKER ECOSYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │   Docker    │────▶│   Docker    │────▶│   Docker    │   │
│  │   Client    │     │   Daemon    │     │   Registry  │   │
│  │  (docker)   │     │  (dockerd)  │     │ (Hub/ECR)   │   │
│  └─────────────┘     └──────┬──────┘     └─────────────┘   │
│                             │                               │
│                   ┌─────────┴─────────┐                    │
│                   │                    │                    │
│              ┌────▼────┐         ┌────▼────┐               │
│              │Container│         │Container│               │
│              │   API   │         │  nginx  │               │
│              └─────────┘         └─────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🆚 Containers vs Virtual Machines

```
      VIRTUAL MACHINES                    CONTAINERS
┌──────────────────────────┐     ┌──────────────────────────┐
│        App A │ App B     │     │    App A │ App B │ App C │
├──────────────┼───────────┤     ├──────────┴───────┴───────┤
│    Bins/Libs │ Bins/Libs │     │       Bins/Libraries     │
├──────────────┼───────────┤     ├──────────────────────────┤
│  Guest OS    │ Guest OS  │     │     Docker Engine        │
├──────────────┴───────────┤     ├──────────────────────────┤
│       Hypervisor         │     │       Host OS            │
├──────────────────────────┤     ├──────────────────────────┤
│     Infrastructure       │     │     Infrastructure       │
└──────────────────────────┘     └──────────────────────────┘
   Heavy (GBs), Minutes            Light (MBs), Seconds
```

| Aspekt | VM | Container |
|--------|-------|-----------|
| Storlek | GB | MB |
| Startid | Minuter | Sekunder |
| Isolation | Full OS | Process-nivå |
| Overhead | Hög | Minimal |

---

## 🏗️ Docker Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        DOCKER HOST                              │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌─────────────────────────────────────────────────────┐    │
│    │                  DOCKER DAEMON                       │    │
│    ├─────────────────────────────────────────────────────┤    │
│    │                                                      │    │
│    │  ┌───────────┐  ┌───────────┐  ┌───────────┐       │    │
│    │  │ Container │  │  Images   │  │  Volumes  │       │    │
│    │  │  Runtime  │  │  Store    │  │  Manager  │       │    │
│    │  │(containerd│  │           │  │           │       │    │
│    │  └───────────┘  └───────────┘  └───────────┘       │    │
│    │                                                      │    │
│    │  ┌───────────┐  ┌───────────┐  ┌───────────┐       │    │
│    │  │  Network  │  │   Build   │  │  Plugin   │       │    │
│    │  │  Driver   │  │  System   │  │  System   │       │    │
│    │  └───────────┘  └───────────┘  └───────────┘       │    │
│    │                                                      │    │
│    └─────────────────────────────────────────────────────┘    │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Installation

### macOS
```bash
# Med Homebrew
brew install --cask docker

# Starta Docker Desktop
open -a Docker
```

### Ubuntu/Debian
```bash
# Lägg till Docker repository
curl -fsSL https://get.docker.com | sh

# Lägg till användare i docker gruppen
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker --version
docker run hello-world
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Verifiera Installation
```bash
# Kontrollera Docker version
docker version

# Kontrollera system info
docker info

# Kör hello-world
docker run hello-world
```

### Övning 2: Utforska Docker CLI
```bash
# Se alla kommandon
docker --help

# Se hjälp för specifikt kommando
docker run --help
docker ps --help
```

---

## 📚 Sammanfattning

| Komponent | Ansvar |
|-----------|--------|
| Docker Client | Skickar kommandon till daemon |
| Docker Daemon | Bygger, kör och distribuerar containers |
| Docker Registry | Lagrar Docker images |
| containerd | Container runtime |

**Nästa steg:** Docker Images & Containers

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Docker Images Deep Dive",
        "difficulty": "beginner",
        "estimated_minutes": 50,
        "xp_reward": 130,
        "content": r"""
# 📦 Docker Images Deep Dive

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


## Lärande mål
- Förstå vad Docker images är
- Lära dig image layers och caching
- Hantera images (pull, push, tag)
- Använda Docker Hub och privata registries

---

## 📖 Vad är en Docker Image?

En Docker image är en **read-only template** med instruktioner för att skapa en container. Den innehåller:

- Base OS (Alpine, Ubuntu, etc.)
- Runtime (Node, Python, Go)
- Application code
- Dependencies
- Configuration

```
┌─────────────────────────────────────────────────────────┐
│                    IMAGE LAYERS                          │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐   │
│  │  Layer 5: ENTRYPOINT ["node", "app.js"]         │   │
│  ├─────────────────────────────────────────────────┤   │
│  │  Layer 4: COPY . /app                           │   │
│  ├─────────────────────────────────────────────────┤   │
│  │  Layer 3: RUN npm install                       │   │
│  ├─────────────────────────────────────────────────┤   │
│  │  Layer 2: WORKDIR /app                          │   │
│  ├─────────────────────────────────────────────────┤   │
│  │  Layer 1: node:18-alpine (Base Image)           │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  Varje layer är READ-ONLY och cachas separatm          │
└─────────────────────────────────────────────────────────┘
```

---

## 🏷️ Image Naming Convention

```
registry.example.com/namespace/repository:tag
└────────┬────────┘ └───┬───┘ └───┬────┘ └─┬┘
      Registry      Owner    Image    Version

Exempel:
- docker.io/library/nginx:1.25
- nginx:latest (default registry + namespace)
- gcr.io/google-containers/nginx:1.25
- 123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1.2.3
```

---

## 🔧 Grundläggande Image Commands

```bash
# Sök efter images
docker search nginx

# Ladda ner image
docker pull nginx
docker pull nginx:1.25-alpine

# Lista lokala images
docker images
docker image ls

# Visa detaljerad info
docker image inspect nginx

# Se image history (layers)
docker history nginx

# Ta bort image
docker rmi nginx
docker image rm nginx:1.25

# Ta bort alla oanvända images
docker image prune -a
```

---

## 📊 Layer Caching

```
┌─────────────────────────────────────────────────────────┐
│               LAYER CACHING EXAMPLE                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  First Build:                Second Build:               │
│  ───────────                 ───────────                │
│  FROM node:18   ──┐          FROM node:18   ◀── CACHED  │
│  WORKDIR /app   ──┼──▶       WORKDIR /app   ◀── CACHED  │
│  COPY package*  ──┤          COPY package*  ◀── CACHED  │
│  RUN npm install──┤          RUN npm install◀── CACHED  │
│  COPY . .       ──┤          COPY . .       ◀── REBUILD │
│  CMD ["npm"]    ──┘          CMD ["npm"]    ◀── REBUILD │
│                                                          │
│  Time: 45s                   Time: 3s                   │
│                                                          │
│  💡 Ordna layers från minst till mest ändringsbenägna!  │
└─────────────────────────────────────────────────────────┘
```

---

## 🏭 Tagga och Pusha Images

```bash
# Tagga en image
docker tag myapp:latest myregistry.com/myapp:v1.0.0
docker tag myapp:latest myregistry.com/myapp:latest

# Logga in på registry
docker login
docker login myregistry.com

# Pusha till registry
docker push myregistry.com/myapp:v1.0.0
docker push myregistry.com/myapp:latest

# Multi-tag push
docker tag myapp:latest myregistry.com/myapp:v1.0.0
docker tag myapp:latest myregistry.com/myapp:v1
docker tag myapp:latest myregistry.com/myapp:latest
docker push myregistry.com/myapp --all-tags
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Utforska Image Layers
```bash
# Ladda ner och inspektera
docker pull python:3.11-slim
docker history python:3.11-slim

# Jämför storlekar
docker images | grep python
```

### Övning 2: Arbeta med Tags
```bash
# Pull flera versioner
docker pull nginx:1.24
docker pull nginx:1.25
docker pull nginx:alpine

# Jämför storlekar
docker images nginx
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| docker pull | Ladda ner image |
| docker images | Lista images |
| docker tag | Tagga image |
| docker push | Ladda upp image |
| docker rmi | Ta bort image |
| docker history | Visa layers |

**Nästa steg:** Container Lifecycle
"""
    },
    {
        "title": "Container Lifecycle Management",
        "difficulty": "beginner",
        "estimated_minutes": 55,
        "xp_reward": 140,
        "content": r"""
# 🔄 Container Lifecycle Management

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


## Lärande mål
- Hantera hela container-livscykeln
- Förstå container states
- Köra containers i olika modes
- Felsöka containers

---

## 📖 Container Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                  CONTAINER LIFECYCLE                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│    ┌─────────┐                                              │
│    │ Created │ ◀──────── docker create                      │
│    └────┬────┘                                              │
│         │ docker start                                       │
│         ▼                                                    │
│    ┌─────────┐   docker pause   ┌─────────┐                 │
│    │ Running │ ◀──────────────▶ │ Paused  │                 │
│    └────┬────┘  docker unpause  └─────────┘                 │
│         │                                                    │
│         │ docker stop / exit                                │
│         ▼                                                    │
│    ┌─────────┐                                              │
│    │ Stopped │                                              │
│    └────┬────┘                                              │
│         │ docker rm                                         │
│         ▼                                                    │
│    ┌─────────┐                                              │
│    │ Removed │                                              │
│    └─────────┘                                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Starta Containers

```bash
# Grundläggande run
docker run nginx

# Med namn
docker run --name my-nginx nginx

# I bakgrunden (detached)
docker run -d --name my-nginx nginx

# Interaktivt mode
docker run -it ubuntu bash

# Ta bort efter avslut
docker run --rm nginx

# Med environment variables
docker run -d --name myapp \
  -e NODE_ENV=production \
  -e API_KEY=secret123 \
  myapp:latest

# Med port mapping
docker run -d -p 8080:80 nginx
docker run -d -p 127.0.0.1:8080:80 nginx

# Med volume
docker run -d -v /host/path:/container/path nginx
docker run -d -v mydata:/data nginx
```

---

## 📊 Hantera Körande Containers

```bash
# Lista körande containers
docker ps

# Lista alla containers (inklusive stoppade)
docker ps -a

# Stopp container (graceful)
docker stop my-nginx

# Tvinga stopp (kill)
docker kill my-nginx

# Starta stoppad container
docker start my-nginx

# Restart
docker restart my-nginx

# Pause/Unpause
docker pause my-nginx
docker unpause my-nginx

# Ta bort container
docker rm my-nginx

# Force remove körande container
docker rm -f my-nginx

# Ta bort alla stoppade containers
docker container prune
```

---

## 🔍 Inspektera Containers

```bash
# Se loggar
docker logs my-nginx
docker logs -f my-nginx  # Follow (tail -f)
docker logs --tail 100 my-nginx
docker logs --since 1h my-nginx

# Inspektera container
docker inspect my-nginx

# Se resursanvändning
docker stats
docker stats my-nginx

# Se processer i container
docker top my-nginx

# Kör kommando i körande container
docker exec -it my-nginx bash
docker exec my-nginx cat /etc/nginx/nginx.conf

# Kopiera filer
docker cp my-nginx:/etc/nginx/nginx.conf ./
docker cp ./app.conf my-nginx:/etc/nginx/conf.d/
```

---

## 🏗️ Container Resource Limits

```bash
# Begränsa minne
docker run -d --memory=512m nginx

# Begränsa CPU
docker run -d --cpus=0.5 nginx

# Kombinerat
docker run -d \
  --name limited-nginx \
  --memory=256m \
  --cpus=0.25 \
  --memory-swap=512m \
  nginx

# Restart policy
docker run -d --restart=always nginx
docker run -d --restart=unless-stopped nginx
docker run -d --restart=on-failure:3 nginx
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Full Lifecycle
```bash
# Skapa utan att starta
docker create --name lifecycle-test nginx
docker ps -a | grep lifecycle

# Starta
docker start lifecycle-test
docker ps

# Stoppa
docker stop lifecycle-test

# Starta igen
docker start lifecycle-test

# Ta bort
docker rm -f lifecycle-test
```

### Övning 2: Debugging
```bash
# Starta container
docker run -d --name debug-test nginx

# Inspektera
docker logs debug-test
docker exec -it debug-test bash

# Se processer
docker top debug-test

# Cleanup
docker rm -f debug-test
```

---

## 📚 Sammanfattning

| State | Beskrivning |
|-------|-------------|
| Created | Skapad men ej startad |
| Running | Aktiv och kör |
| Paused | Temporärt pausad |
| Stopped | Stoppad men finns kvar |
| Removed | Borttagen permanent |

**Nästa steg:** Dockerfile Mastery

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Dockerfile Mastery",
        "difficulty": "medium",
        "estimated_minutes": 60,
        "xp_reward": 160,
        "content": r"""
# 📝 Dockerfile Mastery

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


## Lärande mål
- Skriva effektiva Dockerfiles
- Förstå alla Dockerfile-instruktioner
- Optimera build-tiden med caching
- Best practices för production

---

## 📖 Dockerfile Anatomy

```dockerfile
# ============================================
# DOCKERFILE ANATOMY
# ============================================

# Base image (required)
FROM node:18-alpine

# Metadata
LABEL maintainer="dev@company.com"
LABEL version="1.0"

# Set working directory
WORKDIR /app

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Add arguments (build-time)
ARG BUILD_DATE
ARG VERSION

# Copy files
COPY package*.json ./
RUN npm ci --only=production

COPY . .

# Expose port (documentation)
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/health || exit 1

# Run as non-root user
USER node

# Default command
CMD ["node", "server.js"]
```

---

## 🔧 Dockerfile Instructions

```
┌─────────────────────────────────────────────────────────────┐
│                 DOCKERFILE INSTRUCTIONS                      │
├──────────┬──────────────────────────────────────────────────┤
│ FROM     │ Sätter base image                                │
├──────────┼──────────────────────────────────────────────────┤
│ WORKDIR  │ Sätter working directory                         │
├──────────┼──────────────────────────────────────────────────┤
│ COPY     │ Kopierar filer från host till image              │
├──────────┼──────────────────────────────────────────────────┤
│ ADD      │ Som COPY + kan extrahera tar och hämta URL       │
├──────────┼──────────────────────────────────────────────────┤
│ RUN      │ Kör kommandon vid build-time                     │
├──────────┼──────────────────────────────────────────────────┤
│ CMD      │ Default kommando vid container start             │
├──────────┼──────────────────────────────────────────────────┤
│ ENTRYPOINT│ Huvudkommando (CMD blir argument)               │
├──────────┼──────────────────────────────────────────────────┤
│ ENV      │ Sätter miljövariabler                            │
├──────────┼──────────────────────────────────────────────────┤
│ ARG      │ Build-time variabler                             │
├──────────┼──────────────────────────────────────────────────┤
│ EXPOSE   │ Dokumenterar portar (exponerar ej)               │
├──────────┼──────────────────────────────────────────────────┤
│ VOLUME   │ Skapar mount point                               │
├──────────┼──────────────────────────────────────────────────┤
│ USER     │ Sätter användare för efterföljande kommandon     │
└──────────┴──────────────────────────────────────────────────┘
```

---

## 🚀 Multi-Stage Builds

```dockerfile
# ============================================
# MULTI-STAGE BUILD - Go Application
# ============================================

# Stage 1: Build
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build application
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /app/server

# Stage 2: Production
FROM scratch

# Copy binary from builder
COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

EXPOSE 8080
USER 1000

ENTRYPOINT ["/server"]
```

---

## 📊 Build Optimization

```dockerfile
# ❌ DÅLIGT - Invaliderar cache vid varje ändring
FROM node:18
COPY . /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]

# ✅ BRA - Maximerar cache-användning
FROM node:18-alpine
WORKDIR /app

# Dependencies ändras sällan - cachelagras
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Kod ändras ofta - körs sist
COPY . .

CMD ["npm", "start"]
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Python App Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

### Övning 2: Node.js Multi-Stage
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

---

## 📚 Sammanfattning

| Best Practice | Beskrivning |
|--------------|-------------|
| Slim base images | Använd -alpine eller -slim |
| Multi-stage builds | Mindre production images |
| Layer caching | Ordna från stabil → instabil |
| .dockerignore | Exkludera onödiga filer |
| Non-root user | Säkerhet |
| HEALTHCHECK | Monitoring |

**Nästa steg:** Docker Networking

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Docker Networking",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 150,
        "content": r"""
# 🌐 Docker Networking

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


## Lärande mål
- Förstå Docker network drivers
- Skapa och hantera nätverk
- Container-to-container kommunikation
- DNS resolution i Docker

---

## 📖 Network Drivers

```
┌─────────────────────────────────────────────────────────────┐
│                  DOCKER NETWORK DRIVERS                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │ bridge  │  │  host   │  │  none   │  │ overlay │       │
│  │(default)│  │         │  │         │  │         │       │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘       │
│       │            │            │            │              │
│  Container     Container    Container   Multi-host         │
│  isolation     shares       no network  networking         │
│  with NAT      host net                 (Swarm)            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Network Commands

```bash
# Lista nätverk
docker network ls

# Skapa nätverk
docker network create mynetwork
docker network create --driver bridge --subnet 172.20.0.0/16 mynetwork

# Inspektera nätverk
docker network inspect bridge
docker network inspect mynetwork

# Anslut container till nätverk
docker network connect mynetwork container1

# Koppla bort
docker network disconnect mynetwork container1

# Ta bort nätverk
docker network rm mynetwork

# Ta bort oanvända nätverk
docker network prune
```

---

## 🌉 Bridge Network (Default)

```
┌─────────────────────────────────────────────────────────────┐
│                    HOST MACHINE                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              docker0 bridge (172.17.0.1)             │   │
│  └────────────────────────┬────────────────────────────┘   │
│                           │                                 │
│          ┌────────────────┼────────────────┐               │
│          │                │                │                │
│    ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐        │
│    │ Container │    │ Container │    │ Container │        │
│    │ 172.17.0.2│    │ 172.17.0.3│    │ 172.17.0.4│        │
│    └───────────┘    └───────────┘    └───────────┘        │
│                                                             │
│  Containers kan nå varandra via IP                         │
│  Port mapping krävs för extern access                      │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Default bridge
docker run -d --name web nginx
docker run -d --name api node-api

# Containers kan INTE nå varandra med namn på default bridge!
# Endast IP fungerar
docker inspect web | grep IPAddress
```

---

## 🎯 Custom Bridge Network (Rekommenderat)

```bash
# Skapa custom network
docker network create app-network

# Starta containers på samma network
docker run -d --name web --network app-network nginx
docker run -d --name api --network app-network node-api
docker run -d --name db --network app-network postgres

# Nu fungerar DNS!
docker exec web ping api  # Fungerar!
docker exec api ping db   # Fungerar!
```

```
┌─────────────────────────────────────────────────────────────┐
│                    CUSTOM BRIDGE                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         app-network (with DNS resolution)            │   │
│  └────────────────────────┬────────────────────────────┘   │
│                           │                                 │
│    ┌──────────────────────┼──────────────────────┐         │
│    │                      │                       │         │
│    ▼                      ▼                       ▼         │
│  ┌─────┐              ┌─────┐               ┌─────┐        │
│  │ web │◀────────────▶│ api │◀─────────────▶│ db  │        │
│  │nginx│              │node │               │pg   │        │
│  └─────┘              └─────┘               └─────┘        │
│                                                             │
│  DNS: web → 172.18.0.2, api → 172.18.0.3, db → 172.18.0.4 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Multi-Container App
```bash
# Skapa nätverk
docker network create fullstack

# Starta databas
docker run -d --name postgres \
  --network fullstack \
  -e POSTGRES_PASSWORD=secret \
  postgres:15

# Starta backend
docker run -d --name backend \
  --network fullstack \
  -e DATABASE_URL=postgresql://postgres:secret@postgres:5432/db \
  backend-api

# Starta frontend
docker run -d --name frontend \
  --network fullstack \
  -p 3000:3000 \
  -e API_URL=http://backend:8080 \
  frontend-app
```

### Övning 2: Network Isolation
```bash
# Skapa två isolerade nätverk
docker network create frontend-net
docker network create backend-net

# Backend pratar med båda
docker run -d --name api --network backend-net api-image
docker network connect frontend-net api

# Frontend endast frontend-net
docker run -d --name web --network frontend-net web-image

# DB endast backend-net
docker run -d --name db --network backend-net postgres
```

---

## 📚 Sammanfattning

| Driver | Use Case |
|--------|----------|
| bridge | Default, single-host |
| host | Performance, no isolation |
| none | Completely isolated |
| overlay | Multi-host (Swarm/K8s) |

**Nästa steg:** Docker Volumes & Persistence

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Docker Volumes & Persistence",
        "difficulty": "medium",
        "estimated_minutes": 50,
        "xp_reward": 145,
        "content": r"""
# 💾 Docker Volumes & Persistence

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


## Lärande mål
- Förstå Docker storage options
- Hantera volumes
- Bind mounts vs named volumes
- Backup och restore

---

## 📖 Storage Types

```
┌─────────────────────────────────────────────────────────────┐
│                  DOCKER STORAGE OPTIONS                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   Volumes       │  │  Bind Mounts    │  │   tmpfs     │ │
│  │   (Named)       │  │                 │  │             │ │
│  └────────┬────────┘  └────────┬────────┘  └──────┬──────┘ │
│           │                    │                   │        │
│           ▼                    ▼                   ▼        │
│  /var/lib/docker/     /path/on/host        RAM (memory)    │
│  volumes/mydata                                             │
│                                                              │
│  Best for:           Best for:            Best for:        │
│  - Data persistence  - Development        - Sensitive data │
│  - Sharing data      - Config files       - Performance    │
│  - Backup            - Source code                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Volume Commands

```bash
# Skapa volume
docker volume create mydata

# Lista volumes
docker volume ls

# Inspektera volume
docker volume inspect mydata

# Ta bort volume
docker volume rm mydata

# Ta bort oanvända volumes
docker volume prune

# Se var data lagras
docker volume inspect mydata --format '{{ .Mountpoint }}'
```

---

## 📦 Named Volumes (Rekommenderat för data)

```bash
# Skapa och använd volume
docker run -d --name postgres \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15

# Data persists efter container removal!
docker rm -f postgres
docker run -d --name postgres-new \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
# Data finns kvar!
```

---

## 📂 Bind Mounts (Bra för development)

```bash
# Mount aktuell katalog (development)
docker run -d --name dev-api \
  -v $(pwd):/app \
  -v /app/node_modules \
  node:18 npm run dev

# Read-only mount
docker run -d \
  -v /host/config:/etc/app/config:ro \
  myapp

# Specifik fil
docker run -d \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx
```

---

## 🔄 Backup & Restore

```bash
# Backup volume till tar
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar cvf /backup/pgdata-backup.tar /data

# Restore från tar
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar xvf /backup/pgdata-backup.tar -C /

# Kopiera från container till host
docker cp postgres:/var/lib/postgresql/data ./backup/

# Kopiera från host till container
docker cp ./backup/ postgres:/var/lib/postgresql/data
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Persistent Database
```bash
# Starta MongoDB med persistent data
docker volume create mongodata

docker run -d --name mongodb \
  -v mongodata:/data/db \
  -p 27017:27017 \
  mongo:7

# Lägg till data
docker exec -it mongodb mongosh
# > db.users.insertOne({name: "Alice"})
# > exit

# Ta bort container
docker rm -f mongodb

# Starta ny - data finns kvar!
docker run -d --name mongodb-new \
  -v mongodata:/data/db \
  -p 27017:27017 \
  mongo:7

docker exec -it mongodb-new mongosh
# > db.users.find()
```

### Övning 2: Development Setup
```bash
# Skapa projekt
mkdir myapp && cd myapp
echo 'console.log("Hello")' > app.js

# Kör med bind mount
docker run --rm -it \
  -v $(pwd):/app \
  -w /app \
  node:18 node app.js

# Ändra app.js lokalt - ändringen syns i containern!
```

---

## 📚 Sammanfattning

| Typ | Use Case | Persistence |
|-----|----------|-------------|
| Named Volume | Database, app data | Ja |
| Bind Mount | Development, config | Host-baserad |
| tmpfs | Secrets, temp data | Nej (RAM) |

**Nästa steg:** Docker Compose

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Docker Compose Fundamentals",
        "difficulty": "medium",
        "estimated_minutes": 60,
        "xp_reward": 165,
        "content": r"""
# 🎼 Docker Compose Fundamentals

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


## Lärande mål
- Skriva docker-compose.yml
- Hantera multi-container applikationer
- Förstå service dependencies
- Development vs Production configs

---

## 📖 Docker Compose Overview

```yaml
# docker-compose.yml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - api
    environment:
      - API_URL=http://api:8080

  api:
    build: ./backend
    ports:
      - "8080:8080"
    depends_on:
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/app
      - REDIS_URL=redis://redis:6379

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=app

  redis:
    image: redis:7-alpine

volumes:
  pgdata:
```

```
┌─────────────────────────────────────────────────────────────┐
│                  DOCKER COMPOSE STACK                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    app_default network                 │  │
│  │                                                        │  │
│  │  ┌─────────┐     ┌─────────┐     ┌─────────────────┐ │  │
│  │  │frontend │────▶│   api   │────▶│    db (pg)      │ │  │
│  │  │  :3000  │     │  :8080  │     │    :5432        │ │  │
│  │  └─────────┘     └────┬────┘     └─────────────────┘ │  │
│  │                       │                               │  │
│  │                       │          ┌─────────────────┐ │  │
│  │                       └─────────▶│  redis          │ │  │
│  │                                  │    :6379        │ │  │
│  │                                  └─────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Volume: pgdata ──────▶ /var/lib/postgresql/data            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Compose Commands

```bash
# Starta alla services
docker compose up
docker compose up -d  # Detached

# Bygg och starta
docker compose up --build

# Stoppa
docker compose down
docker compose down -v  # Ta bort volumes också

# Se loggar
docker compose logs
docker compose logs -f api  # Follow specific service

# Se status
docker compose ps

# Kör kommando i service
docker compose exec api bash

# Skala service
docker compose up -d --scale api=3
```

---

## 📝 Service Configuration

```yaml
services:
  api:
    # Build from Dockerfile
    build:
      context: ./backend
      dockerfile: Dockerfile
      args:
        - BUILD_ENV=production

    # Or use image
    # image: myregistry.com/api:v1.0.0

    # Container name
    container_name: my-api

    # Ports
    ports:
      - "8080:8080"

    # Environment
    environment:
      - NODE_ENV=production

    # Or from file
    env_file:
      - .env

    # Volumes
    volumes:
      - ./src:/app/src
      - node_modules:/app/node_modules

    # Networks
    networks:
      - frontend
      - backend

    # Dependencies
    depends_on:
      db:
        condition: service_healthy

    # Health check
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

    # Restart policy
    restart: unless-stopped

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

---

## 🎯 Environment Files

```bash
# .env
POSTGRES_USER=devops
POSTGRES_PASSWORD=secret123
POSTGRES_DB=myapp

# docker-compose.yml
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Full-Stack App
```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend/src:/app/src
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/app
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=app

volumes:
  pgdata:
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| docker compose up | Starta stack |
| docker compose down | Stoppa stack |
| docker compose logs | Se loggar |
| docker compose exec | Kör kommando |
| docker compose ps | Se status |

**Nästa steg:** Docker Compose Advanced

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Docker Compose Advanced Patterns",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🚀 Docker Compose Advanced Patterns

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


## Lärande mål
- Multiple compose files
- Profiles för olika miljöer
- Extends och anchors
- Health checks och dependencies

---

## 📖 Multiple Compose Files

```yaml
# docker-compose.yml (base)
version: '3.8'

services:
  api:
    build: ./backend
    environment:
      - NODE_ENV=production

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```yaml
# docker-compose.override.yml (development)
version: '3.8'

services:
  api:
    build:
      context: ./backend
      target: development
    volumes:
      - ./backend:/app
    environment:
      - NODE_ENV=development
      - DEBUG=true
    ports:
      - "8080:8080"
      - "9229:9229"  # Debug port
```

```yaml
# docker-compose.prod.yml (production)
version: '3.8'

services:
  api:
    image: myregistry.com/api:${VERSION:-latest}
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    restart: always
```

```bash
# Development (auto-mergar med override)
docker compose up

# Production
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

---

## 🎭 Profiles

```yaml
version: '3.8'

services:
  api:
    build: ./backend
    profiles: ["", "production"]  # Default + production

  frontend:
    build: ./frontend
    profiles: ["", "production"]

  # Dev-only services
  mailhog:
    image: mailhog/mailhog
    profiles: ["debug"]
    ports:
      - "8025:8025"

  debug-db:
    image: dpage/pgadmin4
    profiles: ["debug"]
    ports:
      - "5050:80"
```

```bash
# Starta default services
docker compose up

# Starta med debug profile
docker compose --profile debug up

# Starta flera profiles
docker compose --profile debug --profile monitoring up
```

---

## 🔗 YAML Anchors & Extensions

```yaml
version: '3.8'

# Definiera anchor
x-common-env: &common-env
  NODE_ENV: production
  LOG_LEVEL: info

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 10s

services:
  api:
    build: ./api
    environment:
      <<: *common-env  # Merge anchor
      API_KEY: ${API_KEY}
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]

  worker:
    build: ./worker
    environment:
      <<: *common-env
      WORKER_ID: ${WORKER_ID}
    healthcheck:
      <<: *default-healthcheck
      test: ["CMD", "pgrep", "-f", "worker"]
```

---

## 🏥 Health Checks & Dependencies

```yaml
services:
  api:
    build: ./backend
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
      migrations:
        condition: service_completed_successfully
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  migrations:
    build: ./migrations
    command: ["npm", "run", "migrate"]
    depends_on:
      db:
        condition: service_healthy
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Multi-Environment Setup
```yaml
# docker-compose.yml
version: '3.8'

x-logging: &default-logging
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"

services:
  api:
    build: ./backend
    logging: *default-logging

  frontend:
    build: ./frontend
    logging: *default-logging
```

---

## 📚 Sammanfattning

| Pattern | Use Case |
|---------|----------|
| Override files | Dev vs Prod |
| Profiles | Optional services |
| Anchors | DRY config |
| Health checks | Dependencies |

**Nästa steg:** Docker Security

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Docker Security Best Practices",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 155,
        "content": r"""
# 🔒 Docker Security Best Practices

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


## Lärande mål
- Secure Dockerfile patterns
- Hantera secrets
- Network security
- Image scanning

---

## 📖 Secure Dockerfiles

```dockerfile
# ============================================
# SECURE DOCKERFILE EXAMPLE
# ============================================

# Använd specifik version (inte latest)
FROM node:18.19.0-alpine3.19

# Uppdatera base image
RUN apk update && apk upgrade --no-cache

# Skapa non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

WORKDIR /app

# Kopiera endast nödvändiga filer
COPY --chown=appuser:appgroup package*.json ./
RUN npm ci --only=production && npm cache clean --force

COPY --chown=appuser:appgroup . .

# Ta bort onödiga filer
RUN rm -rf tests docs .git

# Byt till non-root user
USER appuser

# Read-only filesystem
# (sätts vid runtime med --read-only)

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "server.js"]
```

---

## 🔐 Secrets Management

```yaml
# docker-compose.yml med secrets
version: '3.8'

services:
  api:
    image: myapi:latest
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    external: true  # Från Docker Swarm secrets
```

```go
// Läs secret i applikationen
func readSecret(name string) (string, error) {
    data, err := os.ReadFile("/run/secrets/" + name)
    if err != nil {
        return "", err
    }
    return strings.TrimSpace(string(data)), nil
}
```

---

## 🛡️ Runtime Security

```bash
# Kör som non-root
docker run --user 1000:1000 myimage

# Read-only filesystem
docker run --read-only myimage

# No new privileges
docker run --security-opt=no-new-privileges myimage

# Drop capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myimage

# Resource limits
docker run --memory=512m --cpus=0.5 myimage

# Kombinerat
docker run \
  --user 1000:1000 \
  --read-only \
  --security-opt=no-new-privileges \
  --cap-drop=ALL \
  --memory=512m \
  --cpus=0.5 \
  --tmpfs /tmp \
  myimage
```

---

## 🔍 Image Scanning

```bash
# Docker Scout (built-in)
docker scout cves myimage:latest
docker scout quickview myimage:latest

# Trivy (open source)
trivy image myimage:latest

# CI/CD integration
trivy image --exit-code 1 --severity HIGH,CRITICAL myimage:latest
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Hardened Container
```bash
# Skapa hardened run command
docker run -d \
  --name secure-api \
  --user 1000:1000 \
  --read-only \
  --security-opt=no-new-privileges \
  --cap-drop=ALL \
  --cap-add=NET_BIND_SERVICE \
  --memory=256m \
  --cpus=0.25 \
  --tmpfs /tmp:rw,noexec,nosuid \
  -p 8080:8080 \
  myapi:latest
```

---

## 📚 Sammanfattning

| Practice | Beskrivning |
|----------|-------------|
| Non-root user | Kör som non-root |
| Minimal base | Alpine/distroless |
| Scan images | Trivy/Scout |
| Drop capabilities | Minsta privilege |
| Secrets | Aldrig i image |

**Nästa steg:** Docker in Production

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Docker in Production",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 165,
        "content": r"""
# 🏭 Docker in Production

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


## Lärande mål
- Production deployment strategies
- Logging och monitoring
- Performance tuning
- CI/CD integration

---

## 📖 Production Checklist

```
┌─────────────────────────────────────────────────────────────┐
│              DOCKER PRODUCTION CHECKLIST                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ☐ Images                                                   │
│    ├─ ☐ Använd specifika tags (inte :latest)               │
│    ├─ ☐ Multi-stage builds                                 │
│    ├─ ☐ Slim base images                                   │
│    └─ ☐ Security scanning                                  │
│                                                              │
│  ☐ Runtime                                                  │
│    ├─ ☐ Non-root user                                      │
│    ├─ ☐ Resource limits                                    │
│    ├─ ☐ Health checks                                      │
│    └─ ☐ Restart policies                                   │
│                                                              │
│  ☐ Observability                                            │
│    ├─ ☐ Centralized logging                                │
│    ├─ ☐ Metrics collection                                 │
│    └─ ☐ Alerting                                           │
│                                                              │
│  ☐ Data                                                     │
│    ├─ ☐ Persistent volumes                                 │
│    └─ ☐ Backup strategy                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Logging Configuration

```yaml
# docker-compose.yml
services:
  api:
    image: myapi:v1.0.0
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "5"
        labels: "app,environment"
        env: "NODE_ENV"

  # Eller till extern service
  api-fluentd:
    image: myapi:v1.0.0
    logging:
      driver: fluentd
      options:
        fluentd-address: localhost:24224
        tag: "docker.{{.Name}}"
```

```bash
# Application logging best practices
# Logga till stdout/stderr
console.log(JSON.stringify({
  timestamp: new Date().toISOString(),
  level: 'info',
  message: 'Request processed',
  requestId: req.id,
  duration: 45
}));
```

---

## 📈 Monitoring

```yaml
# docker-compose.monitoring.yml
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    ports:
      - "3000:3000"

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"

volumes:
  prometheus_data:
  grafana_data:
```

---

## 🚀 CI/CD Pipeline

```yaml
# .github/workflows/docker.yml
name: Docker Build & Deploy

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Registry
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
          tags: |
            ghcr.io/${{ github.repository }}:${{ github.sha }}
            ghcr.io/${{ github.repository }}:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Security Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
          exit-code: 1
          severity: 'CRITICAL,HIGH'
```

---

## 🏋️ Praktiska Övningar

### Övning 1: Production Stack
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  api:
    image: myapi:${VERSION}
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
```

---

## 📚 Sammanfattning

| Area | Best Practice |
|------|---------------|
| Images | Specifika tags, scanning |
| Runtime | Resource limits, health checks |
| Logging | JSON, centralized |
| Monitoring | Prometheus/Grafana |
| CI/CD | Automated builds |

**🎉 Grattis! Du har slutfört Docker Fundamentals!**

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
]
