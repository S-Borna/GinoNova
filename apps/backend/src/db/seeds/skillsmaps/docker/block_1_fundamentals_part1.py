# =============================================================================
# DOCKER MASTERY V3 - BLOCK 1 PART 1: INTRODUCTION & IMAGES
# Noder 1-2 av 20 | Linux Mastery Standard (~10,000+ chars/node)
# =============================================================================

"""
DOCKER BLOCK 1 PART 1 - CONTAINER FUNDAMENTALS
==============================================
Node 1: Docker Introduction - Why Containers?
Node 2: Docker Images - Building Blocks
"""

NODE_1 = {
    "id": "docker_node_1",
    "title": "Docker Introduction - Why Containers?",
    "slug": "docker-introduction-why-containers",
    "content": r'''# 🐳 Docker Introduction - Why Containers?

## 1. Introduktion & Kontext

Docker revolutionerade hur vi bygger, distribuerar och kör applikationer. Containers löser "works on my machine"-problemet genom att paketera applikationer med alla deras beroenden.

### The Problem Docker Solves

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    BEFORE DOCKER (The Pain)                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Developer Machine          Staging Server         Production Server    │
│  ┌─────────────────┐       ┌─────────────────┐    ┌─────────────────┐  │
│  │ Python 3.11     │       │ Python 3.9      │    │ Python 3.8      │  │
│  │ Node 18         │       │ Node 16         │    │ Node 14         │  │
│  │ PostgreSQL 15   │       │ PostgreSQL 13   │    │ PostgreSQL 12   │  │
│  │ Ubuntu 22.04    │       │ CentOS 7        │    │ Amazon Linux 2  │  │
│  └─────────────────┘       └─────────────────┘    └─────────────────┘  │
│           │                         │                      │            │
│           │     "Works on my        │                      │            │
│           │      machine!"          │    "Broke in         │            │
│           │         😤              │     staging!"        │            │
│           │                         │        😱            │   "Down    │
│           └─────────────────────────┴──────────────────────┘   in prod!"│
│                                                                   💀    │
│                                                                          │
│  PROBLEMS:                                                               │
│  • Different OS versions                                                │
│  • Different library versions                                           │
│  • Different configurations                                             │
│  • Missing dependencies                                                 │
│  • Conflicting dependencies                                             │
│  • Environment drift over time                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                     WITH DOCKER (The Solution)                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Developer Machine          Staging Server         Production Server    │
│  ┌─────────────────┐       ┌─────────────────┐    ┌─────────────────┐  │
│  │ ┌─────────────┐ │       │ ┌─────────────┐ │    │ ┌─────────────┐ │  │
│  │ │   Docker    │ │       │ │   Docker    │ │    │ │   Docker    │ │  │
│  │ │  Container  │ │       │ │  Container  │ │    │ │  Container  │ │  │
│  │ │ (Identical) │ │  ───▶ │ │ (Identical) │ │───▶│ │ (Identical) │ │  │
│  │ └─────────────┘ │       │ └─────────────┘ │    │ └─────────────┘ │  │
│  │    Any Host OS  │       │    Any Host OS  │    │    Any Host OS  │  │
│  └─────────────────┘       └─────────────────┘    └─────────────────┘  │
│                                                                          │
│  BENEFITS:                                                               │
│  ✅ Same environment everywhere                                         │
│  ✅ All dependencies included                                           │
│  ✅ Version controlled                                                  │
│  ✅ Reproducible builds                                                 │
│  ✅ Fast startup (seconds vs minutes)                                   │
│  ✅ Resource efficient                                                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Containers vs Virtual Machines

```
┌─────────────────────────────────────────────────────────────────────────┐
│                CONTAINERS VS VIRTUAL MACHINES                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  VIRTUAL MACHINES                     CONTAINERS                         │
│  ─────────────────────                ──────────────────────            │
│                                                                          │
│  ┌────────────────────┐              ┌──────────────────────────┐       │
│  │   App A  │  App B  │              │  App A │ App B │  App C  │       │
│  ├──────────┼─────────┤              ├────────┼───────┼─────────┤       │
│  │ Bins/Libs│Bins/Libs│              │Bins/   │Bins/  │Bins/    │       │
│  ├──────────┼─────────┤              │Libs    │Libs   │Libs     │       │
│  │ Guest OS │ Guest OS│              ├────────┴───────┴─────────┤       │
│  ├──────────┴─────────┤              │     Container Runtime     │       │
│  │    Hypervisor      │              │        (Docker)           │       │
│  ├────────────────────┤              ├──────────────────────────┤       │
│  │      Host OS       │              │        Host OS            │       │
│  ├────────────────────┤              ├──────────────────────────┤       │
│  │    Infrastructure  │              │     Infrastructure        │       │
│  └────────────────────┘              └──────────────────────────┘       │
│                                                                          │
│  Size:      ~1-10 GB per VM           ~10-100 MB per container          │
│  Startup:   Minutes                    Seconds                          │
│  Isolation: Full OS isolation          Process-level isolation          │
│  Overhead:  High (full OS)             Low (shared kernel)              │
│  Density:   10-20 VMs/host             100-1000 containers/host         │
│                                                                          │
│  USE CASES:                                                              │
│  VMs: Different OS requirements, full isolation needed                  │
│  Containers: Microservices, CI/CD, development, scaling                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Docker Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      DOCKER ARCHITECTURE                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   CLIENT                     DOCKER HOST                   REGISTRY     │
│  ┌─────────────┐           ┌─────────────────────┐       ┌──────────┐  │
│  │             │           │                     │       │          │  │
│  │ docker CLI  │──────────▶│    Docker Daemon    │◀─────▶│ Docker   │  │
│  │             │  REST API │      (dockerd)      │       │   Hub    │  │
│  │ docker build│           │                     │       │          │  │
│  │ docker pull │           │  ┌───────────────┐  │       │ Images:  │  │
│  │ docker run  │           │  │   Containers  │  │       │ nginx    │  │
│  │ docker push │           │  │ ┌───┐ ┌───┐   │  │       │ python   │  │
│  │             │           │  │ │ C │ │ C │   │  │       │ postgres │  │
│  └─────────────┘           │  │ └───┘ └───┘   │  │       │ redis    │  │
│                            │  └───────────────┘  │       │ ...      │  │
│                            │                     │       │          │  │
│                            │  ┌───────────────┐  │       └──────────┘  │
│                            │  │    Images     │  │                     │
│                            │  │ ┌───┐ ┌───┐   │  │                     │
│                            │  │ │ I │ │ I │   │  │                     │
│                            │  │ └───┘ └───┘   │  │                     │
│                            │  └───────────────┘  │                     │
│                            │                     │                     │
│                            └─────────────────────┘                     │
│                                                                          │
│  COMPONENTS:                                                             │
│  • Docker Client: CLI tool för att interagera med Docker                │
│  • Docker Daemon: Bakgrundsprocess som hanterar containers              │
│  • Docker Registry: Lagrar och distribuerar Docker images               │
│  • Docker Objects: Images, containers, networks, volumes                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 4. Installation

### macOS

```bash
# Homebrew installation
brew install --cask docker

# Starta Docker Desktop
open /Applications/Docker.app

# Verifiera installation
docker --version
docker compose version
```

### Ubuntu/Debian

```bash
# Ta bort gamla versioner
sudo apt-get remove docker docker-engine docker.io containerd runc

# Installera dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# Lägg till Docker GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Lägg till repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Lägg till user i docker group (kör utan sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker run hello-world
```

### Post-Installation (Linux)

```bash
# Starta Docker vid boot
sudo systemctl enable docker.service
sudo systemctl enable containerd.service

# Konfigurera logging
sudo mkdir -p /etc/docker
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
EOF

sudo systemctl restart docker
```

## 5. Grundläggande Kommandon

```bash
# ═══════════════════════════════════════════════════════════════════════
# CONTAINER LIFECYCLE
# ═══════════════════════════════════════════════════════════════════════

# Kör container (pull + create + start)
docker run nginx                    # Kör i förgrund
docker run -d nginx                 # Detached (bakgrund)
docker run -it ubuntu bash          # Interactive terminal
docker run --rm nginx               # Ta bort efter stopp
docker run --name webserver nginx   # Namnge container

# Container management
docker ps                           # Lista körande containers
docker ps -a                        # Lista ALLA containers
docker stop <container>             # Graceful stop
docker kill <container>             # Force stop
docker start <container>            # Starta stoppad
docker restart <container>          # Restart
docker rm <container>               # Ta bort container

# ═══════════════════════════════════════════════════════════════════════
# IMAGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════

docker images                       # Lista lokala images
docker pull nginx:latest            # Ladda ner image
docker rmi nginx                    # Ta bort image
docker image prune                  # Ta bort oanvända images

# ═══════════════════════════════════════════════════════════════════════
# INSPECT & DEBUG
# ═══════════════════════════════════════════════════════════════════════

docker logs <container>             # Se container logs
docker logs -f <container>          # Follow logs
docker exec -it <container> bash    # Shell i container
docker inspect <container>          # Detaljerad info
docker stats                        # Resource usage

# ═══════════════════════════════════════════════════════════════════════
# CLEANUP
# ═══════════════════════════════════════════════════════════════════════

docker container prune              # Ta bort stoppade containers
docker image prune -a               # Ta bort oanvända images
docker system prune -a              # Rensa ALLT oanvänt
docker system df                    # Visa disk usage
```

## 6. Praktiska Övningar

### Övning 1: Hello World

```bash
# Kör hello-world container
docker run hello-world

# Vad händer:
# 1. Docker letar efter image lokalt
# 2. Om inte hittas → pull från Docker Hub
# 3. Skapar container från image
# 4. Kör container
# 5. Container avslutas (exit 0)

# Se att containern kördes
docker ps -a | grep hello-world
```

### Övning 2: Interaktiv Container

```bash
# Starta Ubuntu container interaktivt
docker run -it --rm ubuntu:22.04 bash

# Inuti containern:
cat /etc/os-release        # Se OS info
apt update && apt install -y curl
curl --version
hostname                   # Container hostname
exit                       # Lämna (container tas bort pga --rm)
```

### Övning 3: Web Server

```bash
# Starta Nginx web server
docker run -d \
  --name webserver \
  -p 8080:80 \
  nginx:alpine

# Testa
curl http://localhost:8080

# Se logs
docker logs webserver

# Stoppa och ta bort
docker stop webserver
docker rm webserver
```

### Övning 4: Environment Variables & Ports

```bash
# PostgreSQL med environment variables
docker run -d \
  --name mydb \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret123 \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  postgres:15-alpine

# Verifiera
docker exec -it mydb psql -U admin -d myapp -c "SELECT version();"

# Cleanup
docker stop mydb && docker rm mydb
```

## 7. Command Reference

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DOCKER RUN OPTIONS                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]                          │
│                                                                          │
│  OPTION              │ DESCRIPTION                                       │
│  ────────────────────────────────────────────────────────────────────── │
│  -d, --detach        │ Kör i bakgrunden                                 │
│  -it                 │ Interactive terminal                             │
│  --name NAME         │ Namnge container                                 │
│  --rm                │ Ta bort container vid exit                       │
│  -p HOST:CONTAINER   │ Port mapping                                     │
│  -P                  │ Publicera alla exponerade portar                 │
│  -e KEY=VALUE        │ Sätt environment variable                        │
│  -v HOST:CONTAINER   │ Mount volume                                     │
│  --network NAME      │ Anslut till nätverk                              │
│  --restart POLICY    │ Restart policy (no/always/on-failure)           │
│  --memory            │ Memory limit                                     │
│  --cpus              │ CPU limit                                        │
│  -w, --workdir       │ Working directory i container                    │
│  -u, --user          │ Username eller UID                               │
│                                                                          │
│  EXAMPLES:                                                               │
│  docker run -d -p 80:80 --name web nginx                                │
│  docker run -it --rm -v $(pwd):/app python:3.11 python script.py        │
│  docker run -d -e DB_HOST=localhost --memory=512m myapp                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DOCKER BEST PRACTICES                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Naming                                                               │
│     □ Namnge containers (--name) för enklare management                 │
│     □ Använd konsekventa namn (project-service format)                  │
│                                                                          │
│  ✅ Cleanup                                                              │
│     □ Använd --rm för temporära containers                              │
│     □ Regelbunden docker system prune                                   │
│     □ Övervaka disk usage med docker system df                          │
│                                                                          │
│  ✅ Security                                                             │
│     □ Undvik att köra som root där möjligt                              │
│     □ Använd secrets för känslig data (inte -e för lösenord)            │
│     □ Håll images uppdaterade                                           │
│                                                                          │
│  ✅ Resources                                                            │
│     □ Sätt memory/CPU limits i produktion                               │
│     □ Övervaka med docker stats                                         │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 9-14. Sammanfattning & Task

### Quick Reference

| Kommando | Syfte |
|----------|-------|
| `docker run` | Skapa och starta container |
| `docker ps` | Lista containers |
| `docker stop/rm` | Stoppa/ta bort |
| `docker logs` | Se output |
| `docker exec` | Kör kommando i container |

---

**Nästa Node:** Docker Images →
''',
    "xp_reward": 150,
    "estimated_minutes": 60,
    "prerequisites": [],
    "learning_outcomes": [
        "Förstå varför Docker behövs",
        "Installera Docker",
        "Köra grundläggande kommandon",
        "Hantera container lifecycle"
    ]
}

NODE_2 = {
    "id": "docker_node_2",
    "title": "Docker Images - Building Blocks",
    "slug": "docker-images-building-blocks",
    "content": r'''# 📦 Docker Images - Building Blocks

## 1. Introduktion & Kontext

Docker Images är read-only templates som används för att skapa containers. De är byggstenar för containeriserade applikationer och lagras i layers för effektivitet.

### Image Anatomy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      DOCKER IMAGE ANATOMY                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  IMAGE = STACKED READ-ONLY LAYERS                                        │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  Layer 6: CMD ["python", "app.py"]              (metadata)      │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │  Layer 5: COPY . /app                           (+50 MB)        │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │  Layer 4: RUN pip install -r requirements.txt   (+100 MB)       │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │  Layer 3: COPY requirements.txt /app            (+2 KB)         │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │  Layer 2: WORKDIR /app                          (metadata)      │   │
│  ├─────────────────────────────────────────────────────────────────┤   │
│  │  Layer 1: FROM python:3.11-slim                 (+150 MB)       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                               │                                         │
│                               ▼                                         │
│                    Total Size: ~300 MB                                  │
│                                                                          │
│  LAYER BENEFITS:                                                         │
│  • Delade mellan images (samma base = delad)                            │
│  • Cached (snabbare builds)                                             │
│  • Inkrementella uppdateringar                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2. Image Naming & Tags

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     IMAGE NAMING CONVENTION                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FULL FORMAT:                                                            │
│  [registry/][namespace/]repository[:tag][@digest]                       │
│                                                                          │
│  EXAMPLES:                                                               │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  nginx                                                                   │
│  └─────┘                                                                │
│  repository (implicit: docker.io/library/nginx:latest)                  │
│                                                                          │
│  nginx:1.25-alpine                                                       │
│  └─────┘└──────────┘                                                    │
│  repo     tag                                                           │
│                                                                          │
│  mycompany/myapp:v1.2.3                                                  │
│  └─────────┘└────┘└─────┘                                               │
│  namespace  repo   tag                                                  │
│                                                                          │
│  ghcr.io/myorg/myapp:latest                                              │
│  └──────┘└────┘└────┘└─────┘                                            │
│  registry org   repo   tag                                              │
│                                                                          │
│  docker.io/library/python:3.11-slim-bookworm                            │
│  └────────┘└──────┘└────┘ └────────────────┘                            │
│  registry namespace repo        tag                                     │
│                                                                          │
│  COMMON TAG PATTERNS:                                                    │
│  ─────────────────────────────────────────────────────────────────────  │
│  latest           │ Default (undvik i produktion!)                      │
│  v1.2.3           │ Semantic version                                    │
│  1.25             │ Major.minor                                         │
│  1.25-alpine      │ Version + variant                                   │
│  sha-abc123       │ Git commit                                          │
│  2024-01-15       │ Date-based                                          │
│  slim/alpine      │ Smaller variant                                     │
│  bullseye/bookworm│ Debian version                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3. Image Commands

```bash
# ═══════════════════════════════════════════════════════════════════════
# SEARCH & PULL
# ═══════════════════════════════════════════════════════════════════════

# Sök på Docker Hub
docker search python
docker search --filter is-official=true python
docker search --filter stars=100 nginx

# Pull image
docker pull nginx                      # Latest (undvik!)
docker pull nginx:1.25-alpine          # Specifik version
docker pull python:3.11-slim-bookworm  # Full qualified

# Pull från andra registries
docker pull ghcr.io/username/myapp:v1
docker pull gcr.io/google-containers/nginx

# ═══════════════════════════════════════════════════════════════════════
# LIST & INSPECT
# ═══════════════════════════════════════════════════════════════════════

# Lista lokala images
docker images
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
docker images -q                       # Endast IDs

# Image detaljer
docker inspect nginx:alpine
docker inspect --format='{{.Config.Env}}' python:3.11

# Se layers
docker history nginx:alpine
docker history --no-trunc nginx:alpine

# Image disk usage
docker system df
docker system df -v                    # Verbose

# ═══════════════════════════════════════════════════════════════════════
# TAG & PUSH
# ═══════════════════════════════════════════════════════════════════════

# Tagga image
docker tag myapp:latest myapp:v1.0.0
docker tag myapp:latest myregistry.com/myapp:v1.0.0

# Push till registry
docker login                           # Docker Hub
docker login ghcr.io                   # GitHub
docker push myregistry.com/myapp:v1.0.0

# ═══════════════════════════════════════════════════════════════════════
# CLEANUP
# ═══════════════════════════════════════════════════════════════════════

# Ta bort image
docker rmi nginx:alpine
docker rmi -f nginx:alpine             # Force

# Ta bort oanvända
docker image prune                     # Dangling images
docker image prune -a                  # Alla oanvända

# Ta bort alla images (FÖRSIKTIGT!)
docker rmi $(docker images -q)
```

## 4. Image Variants

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      IMAGE VARIANTS                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PYTHON EXAMPLE:                                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  TAG                        │ SIZE    │ USE CASE                        │
│  ────────────────────────────────────────────────────────────────────── │
│  python:3.11                │ ~920 MB │ Full Debian, all tools          │
│  python:3.11-slim           │ ~150 MB │ Minimal Debian                  │
│  python:3.11-alpine         │ ~50 MB  │ Alpine Linux, musl libc         │
│  python:3.11-slim-bookworm  │ ~150 MB │ Debian Bookworm slim            │
│                                                                          │
│  NODEJS EXAMPLE:                                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  node:20                    │ ~1 GB   │ Full Debian                     │
│  node:20-slim               │ ~250 MB │ Minimal Debian                  │
│  node:20-alpine             │ ~130 MB │ Alpine Linux                    │
│  node:20-bookworm           │ ~1 GB   │ Debian Bookworm                 │
│                                                                          │
│  RECOMMENDATION:                                                         │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  Development:  Full image (debugging tools)                             │
│  Production:   slim variant (balance)                                   │
│  Size-critical: alpine (men testa noga - musl vs glibc!)               │
│                                                                          │
│  ⚠️ ALPINE GOTCHAS:                                                      │
│  • musl libc istället för glibc                                         │
│  • Vissa Python packages kompilerar inte                                │
│  • Saknar bash (ash default shell)                                      │
│  • Mindre package ecosystem                                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 5. Praktiska Övningar

### Övning 1: Utforska Images

```bash
# Lista alla varianter av python
docker search python --filter is-official=true

# Pull och jämför storlekar
docker pull python:3.11
docker pull python:3.11-slim
docker pull python:3.11-alpine

# Jämför storlekar
docker images python --format "{{.Repository}}:{{.Tag}}\t{{.Size}}"

# Output:
# python:3.11         920MB
# python:3.11-slim    150MB
# python:3.11-alpine  51.5MB
```

### Övning 2: Inspektera Layers

```bash
# Se layer history
docker history python:3.11-slim

# Detaljerad output
docker history --no-trunc --format "{{.CreatedBy}}: {{.Size}}" python:3.11-slim

# Inspektera config
docker inspect python:3.11-slim | jq '.[0].Config.Env'
docker inspect python:3.11-slim | jq '.[0].Config.Cmd'
```

### Övning 3: Tagga och Organisera

```bash
# Bygg enkel image
cat << 'EOF' > Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
EOF

echo 'print("Hello from Docker!")' > app.py

# Bygg
docker build -t myapp .

# Tagga med versions
docker tag myapp myapp:v1.0.0
docker tag myapp myapp:v1.0
docker tag myapp myapp:v1
docker tag myapp myapp:latest

# Lista alla tags
docker images myapp

# Förbered för registry
docker tag myapp:v1.0.0 ghcr.io/myuser/myapp:v1.0.0
```

### Övning 4: Cleanup Strategy

```bash
# Se disk usage
docker system df

# Identifiera stora images
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" | sort -k3 -h

# Ta bort dangling images (untagged)
docker image prune

# Ta bort alla oanvända images
docker image prune -a

# Ta bort specifika old versions
docker images | grep "myapp" | grep -v "latest\|v1.0.0" | awk '{print $3}' | xargs docker rmi
```

## 6. Layer Caching

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      LAYER CACHING                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  HOW CACHING WORKS:                                                      │
│                                                                          │
│  Build #1 (Fresh):                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Step 1: FROM python:3.11-slim        → PULL                     │   │
│  │ Step 2: WORKDIR /app                 → CREATE                   │   │
│  │ Step 3: COPY requirements.txt .      → CREATE                   │   │
│  │ Step 4: RUN pip install ...          → CREATE (SLOW!)           │   │
│  │ Step 5: COPY . .                     → CREATE                   │   │
│  │ Step 6: CMD [...]                    → CREATE                   │   │
│  │                                                                  │   │
│  │ Total time: ~2 minutes                                          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  Build #2 (Only code changed):                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Step 1: FROM python:3.11-slim        → CACHED ✓                 │   │
│  │ Step 2: WORKDIR /app                 → CACHED ✓                 │   │
│  │ Step 3: COPY requirements.txt .      → CACHED ✓                 │   │
│  │ Step 4: RUN pip install ...          → CACHED ✓                 │   │
│  │ Step 5: COPY . .                     → REBUILD (new code)       │   │
│  │ Step 6: CMD [...]                    → REBUILD                  │   │
│  │                                                                  │   │
│  │ Total time: ~5 seconds                                          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  CACHE INVALIDATION:                                                     │
│  • När en layer ändras, invalideras alla efterföljande layers           │
│  • Ordningen av instruktioner är KRITISK                                │
│  • Lägg sällan-ändrade saker först (dependencies)                       │
│  • Lägg ofta-ändrade saker sist (kod)                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 7. Best Practices

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    IMAGE BEST PRACTICES                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ✅ Versioning                                                          │
│     □ ALDRIG använd :latest i produktion                               │
│     □ Använd semantic versioning (v1.2.3)                              │
│     □ Inkludera git SHA för spårbarhet                                 │
│     □ Tagga med datum för CI/CD builds                                 │
│                                                                          │
│  ✅ Size                                                                 │
│     □ Välj slim/alpine där möjligt                                     │
│     □ Använd multi-stage builds                                        │
│     □ Ta bort build dependencies i samma RUN                           │
│     □ Använd .dockerignore                                             │
│                                                                          │
│  ✅ Security                                                            │
│     □ Använd specifika versioner (ej latest)                           │
│     □ Scanna images för vulnerabilities                                │
│     □ Använd trusted base images                                       │
│     □ Uppdatera regelbundet                                            │
│                                                                          │
│  ✅ Organization                                                        │
│     □ Konsekventa naming conventions                                   │
│     □ Dokumentera images                                               │
│     □ Rensa gamla images regelbundet                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## 8-14. Sammanfattning & Task

### Image Selection Guide

| Scenario | Recommended Image |
|----------|------------------|
| Development | Full (python:3.11) |
| Production API | Slim (python:3.11-slim) |
| Minimal binary | Alpine or distroless |
| Enterprise | Verified publisher images |

### Praktisk Task

```bash
# 1. Pull tre Python-varianter
# 2. Jämför storlekar
# 3. Kör samma script i alla tre
# 4. Mät startup time
# 5. Välj lämplig för ditt use case
```

---

**Nästa Node:** Dockerfile Basics →
''',
    "xp_reward": 140,
    "estimated_minutes": 55,
    "prerequisites": ["docker_node_1"],
    "learning_outcomes": [
        "Förstå image layers",
        "Använda image naming conventions",
        "Välja rätt image variant",
        "Hantera images effektivt"
    ]
}

# Block 1 Part 1 exports
BLOCK_1_PART_1_NODES = [NODE_1, NODE_2]
