"""
Docker Mastery - Bootcamp v3 Format
Linux Mastery Standard - Premium Content

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
                "title": "Docker Introduktion & Arkitektur",
                "difficulty": "easy",
                "estimated_minutes": 60,
                "xp_reward": 100,
                "content": r"""# 🐳 Docker Introduktion & Arkitektur

## Varför detta är kritiskt

> "Containers changed everything. Before Docker, 'it works on my machine' was the most dreaded phrase in software. Today, if you can't containerize your application, you can't deploy it reliably. Period."

Tänk dig: Du har byggt en perfekt applikation på din laptop. Den fungerar felfritt. Så pushar du till produktion och... ingenting fungerar. Olika Python-version. Saknade bibliotek. Fel konfiguration. Du tillbringar natten med att felsöka.

**Med Docker hade deployen tagit 30 sekunder.**

---

## Vad är Docker egentligen?

Docker är en **containeriseringsplattform** som paketerar din applikation med ALLA dess beroenden i en isolerad enhet som kallas **container**.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DOCKER ARKITEKTUR                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐          │
│   │  Container  │     │  Container  │     │  Container  │          │
│   │   (nginx)   │     │  (python)   │     │  (postgres) │          │
│   │  Port 80    │     │  Port 8000  │     │  Port 5432  │          │
│   └──────┬──────┘     └──────┬──────┘     └──────┬──────┘          │
│          │                   │                   │                  │
│   ┌──────┴───────────────────┴───────────────────┴──────┐          │
│   │                   DOCKER ENGINE                      │          │
│   │   ┌─────────┐  ┌─────────┐  ┌─────────┐             │          │
│   │   │ Images  │  │Networks │  │ Volumes │             │          │
│   │   └─────────┘  └─────────┘  └─────────┘             │          │
│   └─────────────────────────────────────────────────────┘          │
│                              │                                      │
│   ┌──────────────────────────┴──────────────────────────┐          │
│   │                    HOST KERNEL                       │          │
│   │        (Linux / Windows with WSL2 / macOS VM)        │          │
│   └─────────────────────────────────────────────────────┘          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Container vs Virtual Machine

```
┌─────────────── VIRTUAL MACHINES ───────────────┐  ┌──────────── CONTAINERS ────────────┐
│                                                │  │                                    │
│  ┌──────┐  ┌──────┐  ┌──────┐                 │  │  ┌──────┐  ┌──────┐  ┌──────┐      │
│  │ App  │  │ App  │  │ App  │                 │  │  │ App  │  │ App  │  │ App  │      │
│  ├──────┤  ├──────┤  ├──────┤                 │  │  ├──────┤  ├──────┤  ├──────┤      │
│  │ Bins │  │ Bins │  │ Bins │                 │  │  │ Bins │  │ Bins │  │ Bins │      │
│  │ Libs │  │ Libs │  │ Libs │                 │  │  │ Libs │  │ Libs │  │ Libs │      │
│  ├──────┤  ├──────┤  ├──────┤                 │  │  └──┬───┘  └──┬───┘  └──┬───┘      │
│  │Guest │  │Guest │  │Guest │  (Heavyweight)  │  │     └─────────┼─────────┘          │
│  │  OS  │  │  OS  │  │  OS  │                 │  │         ┌─────┴─────┐              │
│  └──┬───┘  └──┬───┘  └──┬───┘                 │  │         │  Docker   │ (Lightweight)│
│     └─────────┼─────────┘                     │  │         │  Engine   │              │
│         ┌─────┴─────┐                         │  │         └─────┬─────┘              │
│         │Hypervisor │                         │  │               │                    │
│         └─────┬─────┘                         │  │         ┌─────┴─────┐              │
│         ┌─────┴─────┐                         │  │         │  Host OS  │              │
│         │  Host OS  │                         │  │         └───────────┘              │
│         └───────────┘                         │  │                                    │
│                                                │  │                                    │
│  Startup: Minutes | Size: GBs | Isolation: Full│  │  Startup: Seconds | Size: MBs     │
└────────────────────────────────────────────────┘  └────────────────────────────────────┘
```

| Aspekt | Virtual Machine | Container |
|--------|-----------------|-----------|
| **Starttid** | Minuter | Sekunder |
| **Storlek** | Gigabytes | Megabytes |
| **RAM-overhead** | Hög (eget OS) | Minimal |
| **Isolering** | Full (hypervisor) | Process-nivå |
| **Portabilitet** | Begränsad | Mycket hög |
| **Densitet** | ~10-20 per host | ~100-1000 per host |

---

## Docker-komponenter

### 1. Docker Daemon (dockerd)

Bakgrundsprocessen som hanterar containers, images, networks och volumes.

```bash
# Kontrollera daemon status
sudo systemctl status docker

# Docker daemon logs
sudo journalctl -u docker.service -f
```

### 2. Docker CLI

Kommandoradsverktyget du interagerar med.

```bash
# CLI pratar med daemon via socket
ls -la /var/run/docker.sock
```

### 3. Docker Registry

Där images lagras (Docker Hub, ECR, GCR, etc.)

```
┌─────────────────────────────────────────────────────────────────┐
│                        REGISTRY FLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Developer          Docker Hub           Production            │
│       │                  │                    │                 │
│       │  docker push     │                    │                 │
│       │ ───────────────▶ │                    │                 │
│       │                  │   docker pull      │                 │
│       │                  │ ◀───────────────── │                 │
│       │                  │                    │                 │
│   myapp:v1.0          myapp:v1.0          myapp:v1.0           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Installation

### macOS

```bash
# Via Homebrew
brew install --cask docker

# Starta Docker Desktop
open -a Docker

# Verifiera
docker --version
docker run hello-world
```

### Ubuntu/Debian

```bash
# Avinstallera gamla versioner
sudo apt-get remove docker docker-engine docker.io containerd runc

# Installera beroenden
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Lägg till Dockers GPG-nyckel
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Lägg till repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Kör utan sudo (logout/login krävs)
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker run hello-world
```

### Windows (WSL2)

```powershell
# 1. Aktivera WSL2
wsl --install

# 2. Ladda ner Docker Desktop
# https://www.docker.com/products/docker-desktop

# 3. I Docker Desktop Settings:
# - Enable WSL2 integration
# - Select your WSL distro
```

---

## Dina första Docker-kommandon

### Kör din första container

```bash
# Kör hello-world (verifierar installation)
docker run hello-world

# Vad hände?
# 1. Docker letade efter image lokalt (hittade inte)
# 2. Laddade ner från Docker Hub
# 3. Skapade container från image
# 4. Körde container
# 5. Container avslutades (programmet körde klart)
```

### Kör en interaktiv container

```bash
# Starta Ubuntu interaktivt
docker run -it ubuntu bash

# Inuti containern:
cat /etc/os-release
apt update
apt install -y curl
curl --version
exit

# Containern stoppas när du exiterar
```

### Kör en bakgrundscontainer

```bash
# Nginx webserver i bakgrunden
docker run -d -p 8080:80 --name my-nginx nginx

# Förklaring:
# -d         = detached (bakgrund)
# -p 8080:80 = port mapping (host:container)
# --name     = ge containern ett namn
# nginx      = image att köra

# Besök http://localhost:8080

# Se körande containers
docker ps

# Se loggar
docker logs my-nginx

# Stoppa
docker stop my-nginx

# Ta bort
docker rm my-nginx
```

---

## Docker CLI Cheat Sheet

### Container-kommandon

```bash
# Hantera containers
docker run [options] IMAGE      # Skapa och starta
docker start CONTAINER          # Starta stoppad
docker stop CONTAINER           # Snäll stopp (SIGTERM)
docker kill CONTAINER           # Tvinga stopp (SIGKILL)
docker restart CONTAINER        # Omstart
docker rm CONTAINER             # Ta bort
docker rm -f CONTAINER          # Force remove (även körande)

# Inspektera containers
docker ps                       # Lista körande
docker ps -a                    # Lista alla
docker logs CONTAINER           # Visa loggar
docker logs -f CONTAINER        # Följ loggar
docker inspect CONTAINER        # Detaljerad info
docker stats                    # Live resursanvändning
docker top CONTAINER            # Processer i container

# Interagera med containers
docker exec -it CONTAINER bash  # Öppna shell
docker attach CONTAINER         # Attach till process
docker cp FILE CONTAINER:PATH   # Kopiera filer
```

### Image-kommandon

```bash
docker images                   # Lista images
docker pull IMAGE               # Ladda ner
docker push IMAGE               # Ladda upp
docker build -t NAME .          # Bygg image
docker rmi IMAGE                # Ta bort image
docker tag SOURCE TARGET        # Tagga image
docker history IMAGE            # Visa layers
```

---

## Praktisk Övning

### Övning 1: Utforska containers

```bash
# 1. Kör nginx och mappa port
docker run -d -p 8080:80 --name web nginx

# 2. Verifiera att den körs
docker ps

# 3. Öppna webbläsare: http://localhost:8080

# 4. Se loggar när du refreshar sidan
docker logs -f web

# 5. Gå in i containern
docker exec -it web bash
ls /usr/share/nginx/html/
cat /etc/nginx/nginx.conf
exit

# 6. Städa upp
docker stop web && docker rm web
```

### Övning 2: Resursövervakning

```bash
# 1. Starta några containers
docker run -d --name c1 nginx
docker run -d --name c2 redis
docker run -d --name c3 postgres -e POSTGRES_PASSWORD=secret

# 2. Övervaka resurser
docker stats

# 3. Inspektera en container
docker inspect c1 | grep -A 10 "NetworkSettings"

# 4. Städa upp
docker stop c1 c2 c3
docker rm c1 c2 c3
```

---

## Vanliga misstag att undvika

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `docker run` utan `-d` | Terminal blockeras | Använd `-d` för bakgrund |
| Glömmer `--rm` | Containers ackumuleras | `docker run --rm` för temp |
| Kör som root i container | Säkerhetsrisk | Skapa non-root user |
| Ignorerar logs | Svårt att felsöka | `docker logs -f` regelbundet |
| Hårdkodar portar | Port-konflikter | Använd `-p` dynamiskt |

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Container** | Isolerad process med egna filer |
| **Image** | Blueprint för container |
| **Docker Engine** | Runtime som kör containers |
| **Registry** | Lagring för images |
| **Dockerfile** | Recept för att bygga image |

---

## Nästa Steg

Du har nu grunderna i Docker! Nästa task: **Docker Images Deep Dive** — lär dig hur images byggs, lagras och optimeras.

> 💡 **Pro Tip:** Kör `docker system prune` regelbundet för att rensa oanvända resurser. Ditt diskutrymme kommer tacka dig!
"""
            },
            {
                "title": "Docker Images Deep Dive",
                "difficulty": "easy",
                "estimated_minutes": 55,
                "xp_reward": 120,
                "content": r"""# 📦 Docker Images Deep Dive

## Varför detta är kritiskt

> "An image is not just a file — it's a precisely layered, content-addressable filesystem that represents your entire application stack. Understanding images is understanding how Docker actually works under the hood."

Tänk dig: Din CI/CD-pipeline bygger samma image varje gång. Varje build tar 10 minuter. Men om du förstår hur layers fungerar kan samma build ta 30 sekunder. Det är skillnaden mellan frustration och flow.

---

## Vad är en Docker Image?

En image är en **read-only mall** som innehåller:
- Operativsystem (eller delar av det)
- Application runtime (Python, Node, Java, etc.)
- Din applikationskod
- Alla beroenden
- Konfiguration

```
┌─────────────────────────────────────────────────────────────────────┐
│                        IMAGE ANATOMY                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │  Layer 5: CMD ["python", "app.py"]          (metadata)      │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 4: COPY . /app                       (your code)     │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 3: RUN pip install -r requirements   (dependencies)  │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 2: COPY requirements.txt             (dep file)      │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 1: FROM python:3.11-slim             (base image)    │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              ▼                                      │
│                    Content-Addressable                              │
│                    (SHA256 hash per layer)                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Image Naming Convention

```
┌─────────────────────────────────────────────────────────────────────┐
│                     IMAGE REFERENCE FORMAT                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   docker.io / library / python : 3.11-slim                          │
│   ────────   ───────   ──────   ─────────                           │
│   registry   namespace  repo     tag                                │
│                                                                     │
│   Exempel:                                                          │
│   ─────────────────────────────────────────────────────────────     │
│   nginx                    → docker.io/library/nginx:latest         │
│   python:3.11              → docker.io/library/python:3.11          │
│   myuser/myapp:v1          → docker.io/myuser/myapp:v1              │
│   gcr.io/project/app:prod  → gcr.io/project/app:prod                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Tagging Best Practices

| Tag Style | Exempel | Användning |
|-----------|---------|------------|
| **latest** | `myapp:latest` | ⚠️ Undvik i produktion! |
| **Semantic** | `myapp:1.2.3` | ✅ Rekommenderat |
| **Git SHA** | `myapp:abc123f` | ✅ Spårbart till commit |
| **Date** | `myapp:2024-01-15` | ✅ Tidsstämplat |
| **Environment** | `myapp:prod` | ⚠️ Överskrivs ofta |

**Varför undvika `latest`?**
```bash
# Dag 1: Deploy
kubectl set image deployment/app app=myapp:latest
# Fungerar! Image är v1.0.0

# Dag 2: Någon pushar v1.1.0 som "latest"

# Dag 3: Pod restarts, pulls "latest"
# Nu kör du v1.1.0 utan att veta det!
```

---

## Layer-systemet

### Hur layers fungerar

```
┌─────────────────────────────────────────────────────────────────────┐
│                       LAYER SHARING                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Image A              Image B              Image C                 │
│   ┌───────────┐       ┌───────────┐        ┌───────────┐           │
│   │ Your App  │       │  API App  │        │ Worker    │           │
│   ├───────────┤       ├───────────┤        ├───────────┤           │
│   │ Flask     │       │ FastAPI   │        │ Celery    │           │
│   ├───────────┴───────┴───────────┴────────┴───────────┤           │
│   │              Python 3.11                           │ ◀─ DELAD! │
│   ├────────────────────────────────────────────────────┤           │
│   │              Debian Slim                           │ ◀─ DELAD! │
│   └────────────────────────────────────────────────────┘           │
│                                                                     │
│   Disk: Delade layers lagras ENDAST EN GÅNG!                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Inspektera layers

```bash
# Se image layers
docker history python:3.11-slim

# Output:
# IMAGE          CREATED       SIZE      COMMAND
# abc123         2 days ago    5.5MB     CMD ["python3"]
# def456         2 days ago    0B        EXPOSE 8000
# ghi789         2 days ago    45.3MB    RUN pip install...
# jkl012         2 days ago    125MB     FROM debian:slim

# Detaljerad layer-info
docker inspect python:3.11-slim | jq '.[0].RootFS.Layers'
```

### Layer Caching

```dockerfile
# ❌ DÅLIGT - Bryter cache vid varje kodändring
FROM python:3.11-slim
COPY . /app                      # Ändras ofta → alla efterföljande layers rebuilds
RUN pip install -r requirements.txt

# ✅ BRA - Maximerar cache
FROM python:3.11-slim
COPY requirements.txt /app/      # Ändras sällan
RUN pip install -r requirements.txt  # Cachas!
COPY . /app                      # Bara denna layer rebuilds
```

---

## Image-kommandon

### Hämta images

```bash
# Pull från Docker Hub
docker pull nginx
docker pull nginx:1.25
docker pull nginx:1.25-alpine

# Pull från andra registries
docker pull gcr.io/google-containers/nginx
docker pull ghcr.io/username/app:v1

# Pull alla taggar (sällan nödvändigt)
docker pull -a nginx
```

### Lista images

```bash
# Lista alla images
docker images

# Med mer detaljer
docker images --no-trunc

# Filtrera
docker images --filter "dangling=true"
docker images --filter "reference=nginx*"

# Formattera output
docker images --format "{{.Repository}}:{{.Tag}} - {{.Size}}"

# Bara IDs (bra för scripting)
docker images -q
```

### Ta bort images

```bash
# Ta bort specifik image
docker rmi nginx:1.25

# Force remove (även om container finns)
docker rmi -f nginx:1.25

# Ta bort alla oanvända images
docker image prune

# Ta bort ALLT (images, containers, volumes, networks)
docker system prune -a

# Ta bort images äldre än 24h
docker image prune -a --filter "until=24h"
```

### Tagga images

```bash
# Tagga lokal image
docker tag myapp:latest myapp:v1.0.0

# Tagga för push till registry
docker tag myapp:v1 registry.example.com/team/myapp:v1
docker tag myapp:v1 ghcr.io/myorg/myapp:v1
docker tag myapp:v1 123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1

# En image kan ha MÅNGA taggar (samma layer-data)
docker tag myapp:v1 myapp:latest
docker tag myapp:v1 myapp:stable
```

---

## Push och Pull

### Docker Hub

```bash
# Logga in
docker login

# Push
docker push myuser/myapp:v1

# Private repo (kräver plan)
docker push myuser/private-app:v1
```

### AWS ECR

```bash
# Få login-token
aws ecr get-login-password --region eu-west-1 | \
    docker login --username AWS --password-stdin \
    123456789.dkr.ecr.eu-west-1.amazonaws.com

# Push
docker push 123456789.dkr.ecr.eu-west-1.amazonaws.com/myapp:v1
```

### GitHub Container Registry

```bash
# Logga in med PAT
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# Push
docker push ghcr.io/myorg/myapp:v1
```

---

## Image Inspection

```bash
# Grundläggande info
docker inspect nginx:latest

# Specifik information med jq
docker inspect nginx | jq '.[0].Config.Env'
docker inspect nginx | jq '.[0].Config.ExposedPorts'
docker inspect nginx | jq '.[0].Config.Cmd'

# Image digest (för immutable deploys)
docker inspect --format='{{.RepoDigests}}' nginx

# Storlek
docker images nginx --format "{{.Size}}"
```

---

## Praktiska Övningar

### Övning 1: Layer-analys

```bash
# 1. Pull en image
docker pull python:3.11-slim

# 2. Analysera layers
docker history python:3.11-slim

# 3. Jämför med alpine
docker pull python:3.11-alpine
docker history python:3.11-alpine

# 4. Jämför storlekar
docker images python --format "{{.Tag}}: {{.Size}}"
```

### Övning 2: Tagging Workflow

```bash
# 1. Pull base image
docker pull nginx:1.25

# 2. Skapa taggar för olika miljöer
docker tag nginx:1.25 myregistry/nginx:1.25
docker tag nginx:1.25 myregistry/nginx:prod
docker tag nginx:1.25 myregistry/nginx:latest

# 3. Lista och se att alla pekar på samma image ID
docker images myregistry/nginx

# 4. Städa upp
docker rmi myregistry/nginx:1.25 myregistry/nginx:prod myregistry/nginx:latest
```

---

## Vanliga misstag

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Använda `latest` | Oförutsägbara deploys | Specifika versioner |
| Stora base images | Långsam pull/push | Använd `-slim` eller `-alpine` |
| Ignorera layer-order | Långsamma builds | Sällan-ändrade först |
| Inte rensa gamla images | Disk full | `docker image prune` |

---

## Sammanfattning

| Kommando | Beskrivning |
|----------|-------------|
| `docker pull` | Hämta image |
| `docker images` | Lista images |
| `docker rmi` | Ta bort image |
| `docker tag` | Skapa ny tag |
| `docker push` | Ladda upp till registry |
| `docker inspect` | Visa metadata |
| `docker history` | Visa layers |

---

## Nästa Steg

Du förstår nu hur images fungerar! Nästa task: **Dockerfile Mastery** — bygg dina egna professionella images.

> 💡 **Pro Tip:** Kör `docker images | grep "<none>"` regelbundet. "Dangling images" tar plats utan att användas!
"""
            },
            {
                "title": "Dockerfile Mastery",
                "difficulty": "medium",
                "estimated_minutes": 65,
                "xp_reward": 150,
                "content": r"""# 🏗️ Dockerfile Mastery

## Varför detta är kritiskt

> "A Dockerfile is not just build instructions — it's a contract between your code and your infrastructure. A well-crafted Dockerfile means fast builds, small images, and secure deployments. A poorly written one means wasted hours and security vulnerabilities."

En dålig Dockerfile kan göra din 50MB-app till en 2GB-image. Den kan exponera secrets i layer-historiken. Den kan ta 20 minuter att bygga istället för 20 sekunder.

**Att skriva en bra Dockerfile är en konst. Låt oss behärska den.**

---

## Dockerfile-instruktioner

### FROM — Basimage

```dockerfile
# Alltid första instruktionen
FROM python:3.11-slim

# Med specifik digest (immutable)
FROM python@sha256:abc123...

# Multi-stage (mer om detta senare)
FROM node:18 AS builder
FROM nginx:alpine AS production
```

**Val av base image:**

| Image Type | Storlek | Användning |
|------------|---------|------------|
| `ubuntu:22.04` | ~77MB | Full distro, debugging |
| `python:3.11` | ~900MB | Allt inkluderat |
| `python:3.11-slim` | ~150MB | ✅ Rekommenderat |
| `python:3.11-alpine` | ~50MB | Minst, men kompatibilitetsproblem |
| `distroless` | ~20MB | Endast runtime, mest säkert |

### WORKDIR — Arbetskatalog

```dockerfile
# Skapa och sätt arbetskatalog
WORKDIR /app

# Alla efterföljande kommandon utgår från /app
COPY . .         # Kopierar till /app
RUN pwd          # Output: /app
```

### COPY vs ADD

```dockerfile
# COPY — enkel kopiering (REKOMMENDERAS)
COPY package.json .
COPY src/ ./src/

# ADD — kan mer, men använd sällan
ADD https://example.com/file.tar.gz /tmp/     # Laddar ner URL
ADD archive.tar.gz /app/                       # Extraherar automatiskt

# ✅ Best practice: Använd COPY, explicit ADD för tar/URL
```

### RUN — Bygg-kommandon

```dockerfile
# ❌ DÅLIGT - Många layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean

# ✅ BRA - En layer, rensar cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*
```

### ENV — Miljövariabler

```dockerfile
# Sätt miljövariabler
ENV NODE_ENV=production
ENV APP_PORT=8000

# Flera på en rad
ENV NODE_ENV=production APP_PORT=8000

# Använd i efterföljande kommandon
RUN echo "Port is $APP_PORT"
```

### ARG — Build-time variabler

```dockerfile
# Definiera build argument
ARG VERSION=latest
ARG BUILD_DATE

# Använd med docker build --build-arg
# docker build --build-arg VERSION=1.2.3 .

# Kombinera med ENV för runtime
ARG VERSION
ENV APP_VERSION=$VERSION
```

### EXPOSE — Dokumentera portar

```dockerfile
# Dokumentera vilka portar containern lyssnar på
EXPOSE 8000
EXPOSE 443/tcp
EXPOSE 8125/udp

# OBS: Detta ÖPPNAR inte porten!
# Du måste fortfarande använda -p vid docker run
```

### CMD vs ENTRYPOINT

```dockerfile
# CMD — Default kommando (kan överskrivas)
CMD ["python", "app.py"]
# docker run myapp               → python app.py
# docker run myapp python test.py → python test.py (CMD överskrivet)

# ENTRYPOINT — Fast kommando
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myapp               → python app.py
# docker run myapp test.py       → python test.py (argument till ENTRYPOINT)

# Shell form vs Exec form
CMD python app.py               # Shell form (kör via /bin/sh -c)
CMD ["python", "app.py"]        # Exec form (kör direkt) ✅
```

---

## Komplett Dockerfile-exempel

### Python Web Application

```dockerfile
# ============================================
# PRODUKTIONS-DOCKERFILE FÖR PYTHON APP
# ============================================

# Stage 1: Base
FROM python:3.11-slim AS base

# Förhindra Python att skriva .pyc och buffra output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Stage 2: Builder
FROM base AS builder

# Installera build-beroenden
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installera Python-beroenden
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 3: Production
FROM base AS production

# Skapa non-root user
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --shell /bin/bash appuser

# Kopiera installerade packages från builder
COPY --from=builder /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

# Kopiera applikationskod
COPY --chown=appuser:appgroup . .

# Byt till non-root user
USER appuser

# Exponera port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Startkommando
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
```

### Node.js Application

```dockerfile
# ============================================
# MULTI-STAGE DOCKERFILE FÖR NODE.JS
# ============================================

# Stage 1: Dependencies
FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Stage 2: Builder
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 3: Production
FROM node:18-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production

# Skapa non-root user
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

# Kopiera nödvändiga filer
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules

USER nextjs

EXPOSE 3000

CMD ["node", "dist/index.js"]
```

---

## .dockerignore

```bash
# .dockerignore - Exkludera från build context

# Dependencies
node_modules/
__pycache__/
*.pyc
.venv/
venv/

# Build artifacts
dist/
build/
*.egg-info/

# Development
.git/
.gitignore
*.md
docs/

# IDE
.vscode/
.idea/
*.swp

# Environment
.env
.env.local
*.env

# Docker
Dockerfile*
docker-compose*
.dockerignore

# Tests
tests/
__tests__/
coverage/
.pytest_cache/
```

---

## Build-optimering

### Layer Caching Strategy

```dockerfile
# ❌ DÅLIGT - Cache invalideras vid varje kodändring
FROM node:18
COPY . .                    # Kodändring → allt nedan rebuilds
RUN npm install
RUN npm run build

# ✅ BRA - Maximerar cache
FROM node:18
COPY package*.json ./       # Ändras sällan
RUN npm install             # Cachas om package.json inte ändrats
COPY . .                    # Bara detta rebuilds vid kodändring
RUN npm run build
```

### Multi-stage Builds

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MULTI-STAGE BUILD FLOW                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌──────────────────┐                                              │
│   │   Stage: deps    │   npm ci --only=production                   │
│   │   1.2 GB         │   (production dependencies)                  │
│   └────────┬─────────┘                                              │
│            │                                                        │
│   ┌────────▼─────────┐                                              │
│   │  Stage: builder  │   npm ci && npm run build                    │
│   │   2.5 GB         │   (all deps + build)                         │
│   └────────┬─────────┘                                              │
│            │                                                        │
│            │  COPY --from=builder /app/dist                         │
│            │  COPY --from=deps /app/node_modules                    │
│            ▼                                                        │
│   ┌──────────────────┐                                              │
│   │ Stage: production│   Final image                                │
│   │   150 MB         │   (only runtime files)                       │
│   └──────────────────┘                                              │
│                                                                     │
│   Resultat: 2.5 GB build → 150 MB production image                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Bygga images

```bash
# Grundläggande build
docker build -t myapp:v1 .

# Med annan Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build för specifik platform
docker build --platform linux/amd64 -t myapp:v1 .

# Build-args
docker build \
    --build-arg VERSION=1.2.3 \
    --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
    -t myapp:v1 .

# No cache (fullständig rebuild)
docker build --no-cache -t myapp:v1 .

# Visa alla layers under build
docker build --progress=plain -t myapp:v1 .
```

---

## Praktisk Övning

### Övning: Bygg en optimerad image

```bash
# 1. Skapa projekt
mkdir dockerfile-lab && cd dockerfile-lab

# 2. Skapa en enkel Python-app
cat > app.py << 'EOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
EOF

cat > requirements.txt << 'EOF'
flask==3.0.0
gunicorn==21.2.0
EOF

# 3. Skapa Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --gid 1000 app && \
    useradd --uid 1000 --gid app app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
EOF

# 4. Bygg och kör
docker build -t myapp:v1 .
docker run -d -p 8000:8000 --name myapp myapp:v1

# 5. Testa
curl http://localhost:8000
curl http://localhost:8000/health

# 6. Se image-storlek
docker images myapp

# 7. Städa
docker stop myapp && docker rm myapp
```

---

## Sammanfattning

| Instruktion | Syfte |
|-------------|-------|
| `FROM` | Base image |
| `WORKDIR` | Sätt arbetskatalog |
| `COPY` | Kopiera filer |
| `RUN` | Kör kommando vid build |
| `ENV` | Sätt miljövariabler |
| `ARG` | Build-time variabler |
| `EXPOSE` | Dokumentera portar |
| `CMD` | Default runtime-kommando |
| `ENTRYPOINT` | Fast runtime-kommando |
| `USER` | Byt användare |
| `HEALTHCHECK` | Hälsokontroll |

---

## Nästa Steg

Du kan nu skriva professionella Dockerfiles! Nästa task: **Container Lifecycle & Management** — hantera containers som ett proffs.

> 💡 **Pro Tip:** Kör alltid `docker scan myapp:v1` efter build för att hitta säkerhetsproblem i din image!
"""
            },
            {
                "title": "Container Lifecycle & Management",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 140,
                "content": r"""# 🔄 Container Lifecycle & Management

## Varför detta är kritiskt

> "Containers are ephemeral by design — they're meant to be created, destroyed, and recreated. Understanding the lifecycle is understanding how to build resilient systems. A container that can't handle graceful shutdown will corrupt data. A container that doesn't clean up will exhaust resources."

I produktion kan en container starta om tusentals gånger. Varje gång måste den:
1. Starta snabbt
2. Vara redo att ta emot trafik
3. Avsluta gracefully utan dataförlust

**Låt oss förstå varje fas.**

---

## Container States

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONTAINER LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   docker create                                                     │
│        │                                                            │
│        ▼                                                            │
│   ┌─────────┐    docker start    ┌─────────┐                       │
│   │ CREATED │ ─────────────────▶ │ RUNNING │                       │
│   └─────────┘                    └────┬────┘                       │
│                                       │                             │
│                          docker pause │ docker unpause              │
│                                       ▼                             │
│                                  ┌─────────┐                        │
│                                  │ PAUSED  │                        │
│                                  └────┬────┘                        │
│                                       │                             │
│                           docker stop │ docker kill                 │
│                                       ▼                             │
│   ┌─────────┐                   ┌─────────┐                        │
│   │ REMOVED │ ◀──── docker rm ──│ STOPPED │                        │
│   └─────────┘                   └─────────┘                        │
│                                       │                             │
│                                       │ docker start                │
│                                       └────────────▶ RUNNING        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

| State | Beskrivning | Resursanvändning |
|-------|-------------|------------------|
| **Created** | Container skapad men ej startad | Minimal (endast metadata) |
| **Running** | Process körs aktivt | CPU + RAM + Network |
| **Paused** | Frozen, process pausad | RAM (fryst i minnet) |
| **Stopped** | Process avslutad, data kvar | Disk (filesystem kvar) |
| **Removed** | Borttagen, allt rensat | Ingen |

---

## Skapa och starta containers

### docker run (skapa + starta)

```bash
# Enklaste form
docker run nginx

# Med alla vanliga flaggor
docker run \
    -d \                          # Detached (bakgrund)
    --name webserver \            # Namnge containern
    -p 8080:80 \                  # Port mapping
    -e NGINX_HOST=example.com \   # Miljövariabel
    -v /data:/usr/share/nginx/html \ # Volume mount
    --restart unless-stopped \    # Restart policy
    --memory 512m \               # Minnesgräns
    --cpus 0.5 \                  # CPU-gräns
    nginx:1.25
```

### docker create + start (separat)

```bash
# Skapa utan att starta
docker create --name myapp nginx

# Starta senare
docker start myapp

# Användbart för:
# - Förbereda containers före lansering
# - Scripting och automation
# - Debugga startup-problem
```

### Auto-remove containers

```bash
# Ta bort när den avslutas (bra för engångsjobb)
docker run --rm alpine echo "Hello and goodbye!"

# Containern finns inte längre
docker ps -a | grep alpine  # Tom!
```

---

## Hantera körande containers

### Exec — Kör kommandon inuti container

```bash
# Öppna shell i körande container
docker exec -it myapp bash

# Kör enstaka kommando
docker exec myapp ls -la /app
docker exec myapp cat /etc/nginx/nginx.conf

# Som annan användare
docker exec -u root myapp apt-get update

# Med miljövariabler
docker exec -e DEBUG=true myapp python script.py
```

### Attach vs Exec

```bash
# Attach - Koppla till HUVUDPROCESSEN (PID 1)
docker attach myapp
# Ctrl+C skickar signal till containern!
# Ctrl+P Ctrl+Q för att detacha utan att stoppa

# Exec - Startar NY process
docker exec -it myapp bash
# Ctrl+C avslutar bara bash, inte containern
```

### Kopiera filer

```bash
# Kopiera TILL container
docker cp local_file.txt myapp:/app/

# Kopiera FRÅN container
docker cp myapp:/app/config.yaml ./

# Kopiera hela katalog
docker cp myapp:/var/log/nginx ./nginx-logs/
```

---

## Stoppa containers

### Graceful shutdown (SIGTERM)

```bash
# Skickar SIGTERM, väntar 10s, sen SIGKILL
docker stop myapp

# Ändra timeout (vänta längre)
docker stop -t 30 myapp

# Vad händer?
# 1. Docker skickar SIGTERM till PID 1
# 2. Applikationen har 10s att städa upp
# 3. Om den inte avslutat: SIGKILL (tvingad)
```

### Force kill (SIGKILL)

```bash
# Omedelbar död (ingen cleanup)
docker kill myapp

# Skicka annan signal
docker kill -s SIGHUP myapp   # Reload config
docker kill -s SIGUSR1 myapp  # Custom signal
```

### Hantera SIGTERM i din app

```python
# Python exempel - graceful shutdown
import signal
import sys

def shutdown_handler(signum, frame):
    print("Received shutdown signal, cleaning up...")
    # Stäng databaskopplingar
    # Slutför pågående requests
    # Spara state
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
```

```javascript
// Node.js exempel
process.on('SIGTERM', () => {
    console.log('SIGTERM received, shutting down gracefully');
    server.close(() => {
        console.log('Server closed');
        process.exit(0);
    });
});
```

---

## Restart Policies

```bash
# Starta aldrig om automatiskt (default)
docker run --restart no nginx

# Starta om vid krasch (ej manuell stop)
docker run --restart on-failure nginx

# Max antal omstarter vid krasch
docker run --restart on-failure:5 nginx

# Alltid starta om (även efter reboot)
docker run --restart always nginx

# Alltid, utom vid manuell stop
docker run --restart unless-stopped nginx
```

| Policy | Krasch | Manuell stop | Docker restart | Användning |
|--------|--------|--------------|----------------|------------|
| `no` | ❌ | - | ❌ | Engångsjobb |
| `on-failure` | ✅ | ❌ | ❌ | Dev/test |
| `always` | ✅ | ✅ | ✅ | Produktion |
| `unless-stopped` | ✅ | ❌ | ✅ | ✅ Rekommenderat |

---

## Monitoring & Logging

### Logs

```bash
# Visa alla logs
docker logs myapp

# Följ logs i realtid
docker logs -f myapp

# Senaste N rader
docker logs --tail 100 myapp

# Med timestamps
docker logs -t myapp

# Sedan tidpunkt
docker logs --since 2024-01-15 myapp
docker logs --since 10m myapp

# Kombinera
docker logs -f --tail 50 --since 5m myapp
```

### Stats (resursanvändning)

```bash
# Live stats för alla containers
docker stats

# Specifik container
docker stats myapp

# Utan stream (en gång)
docker stats --no-stream

# Formattera output
docker stats --format "{{.Name}}: {{.CPUPerc}} CPU, {{.MemUsage}}"
```

### Inspect (detaljerad info)

```bash
# All metadata
docker inspect myapp

# Specifik info med Go template
docker inspect --format '{{.State.Status}}' myapp
docker inspect --format '{{.NetworkSettings.IPAddress}}' myapp
docker inspect --format '{{json .Config.Env}}' myapp | jq

# Healthcheck status
docker inspect --format '{{.State.Health.Status}}' myapp
```

---

## Healthchecks

```dockerfile
# I Dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
```

```bash
# Vid docker run
docker run -d \
    --health-cmd="curl -f http://localhost:8000/health || exit 1" \
    --health-interval=30s \
    --health-timeout=10s \
    --health-retries=3 \
    myapp

# Kontrollera status
docker inspect --format '{{.State.Health.Status}}' myapp
# Möjliga värden: starting, healthy, unhealthy
```

---

## Cleanup & Maintenance

```bash
# Ta bort stoppade containers
docker container prune

# Ta bort specifik container
docker rm myapp

# Force remove (även körande)
docker rm -f myapp

# Ta bort alla stoppade
docker rm $(docker ps -aq --filter status=exited)

# System-wide cleanup
docker system prune          # Containers, networks, dangling images
docker system prune -a       # + alla oanvända images
docker system prune -a --volumes  # + volumes (VARNING: data försvinner!)

# Se diskutrymme
docker system df
```

---

## Praktiska Övningar

### Övning 1: Lifecycle exploration

```bash
# 1. Skapa container utan att starta
docker create --name lifecycle-test nginx

# 2. Se status
docker ps -a | grep lifecycle-test

# 3. Starta
docker start lifecycle-test

# 4. Pausa och kontrollera
docker pause lifecycle-test
docker ps | grep lifecycle-test  # Status: paused

# 5. Unpause
docker unpause lifecycle-test

# 6. Graceful stop
docker stop lifecycle-test

# 7. Starta igen
docker start lifecycle-test

# 8. Force kill
docker kill lifecycle-test

# 9. Ta bort
docker rm lifecycle-test
```

### Övning 2: Graceful shutdown test

```bash
# Skapa en container som loggar SIGTERM
docker run -d --name signal-test alpine sh -c '
trap "echo SIGTERM received; exit 0" TERM
while true; do echo "Running..."; sleep 1; done
'

# Följ logs
docker logs -f signal-test &

# Stoppa gracefully
docker stop signal-test

# Se att SIGTERM loggades
```

---

## Sammanfattning

| Kommando | Beskrivning |
|----------|-------------|
| `docker run` | Skapa + starta |
| `docker create` | Endast skapa |
| `docker start/stop` | Starta/stoppa |
| `docker pause/unpause` | Pausa/återuppta |
| `docker kill` | Tvångs-stopp |
| `docker rm` | Ta bort |
| `docker exec` | Kör kommando i container |
| `docker logs` | Visa loggar |
| `docker stats` | Resursanvändning |
| `docker inspect` | Detaljerad info |

---

## Nästa Steg

Du förstår nu container-livscykeln! Nästa task: **Docker Volumes** — persistent data som överlever containers.

> 💡 **Pro Tip:** Sätt alltid `--restart unless-stopped` på produktions-containers. Det sparar dig från 3 AM-samtal!
"""
            },
            {
                "title": "Docker Volumes & Persistent Data",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 145,
                "content": r"""# 💾 Docker Volumes & Persistent Data

## Varför detta är kritiskt

> "Containers are ephemeral — when they die, so does everything inside them. Your database data, uploaded files, application state — gone. Volumes are the bridge between container ephemerality and data persistence. Get this wrong, and you'll lose production data."

Tänk dig: Du kör PostgreSQL i Docker. Allt fungerar. Så restarts Docker daemon. Databasen startar om. All data är borta. Två år av kunddata. Raderat.

**Volumes hade förhindrat detta. Låt oss aldrig göra det misstaget.**

---

## Förstå Container Storage

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONTAINER STORAGE LAYERS                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │           CONTAINER LAYER (Read-Write)                      │  │
│   │   • Alla ändringar skrivs här                               │  │
│   │   • FÖRSVINNER när containern tas bort                      │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │           IMAGE LAYERS (Read-Only)                          │  │
│   │   Layer 3: Application code                                 │  │
│   │   Layer 2: Dependencies                                     │  │
│   │   Layer 1: Base OS                                          │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   PROBLEM: Container layer är INTE persistent!                      │
│                                                                     │
│   LÖSNING: VOLUMES                                                  │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │  Container          ◀─────────────▶  Volume (på host)       │  │
│   │  /var/lib/data              /var/lib/docker/volumes/mydata  │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   Volume-data ÖVERLEVER container-borttagning!                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Tre sätt att hantera data

### 1. Named Volumes (Rekommenderat)

```bash
# Skapa en named volume
docker volume create mydata

# Använd i container
docker run -d \
    --name db \
    -v mydata:/var/lib/postgresql/data \
    postgres:15

# Docker hanterar storage location
# Typically: /var/lib/docker/volumes/mydata/_data
```

**Fördelar:**
- Docker hanterar platsen
- Enkelt att backup/restore
- Fungerar på alla plattformar
- Kan delas mellan containers

### 2. Bind Mounts (Host paths)

```bash
# Mount specifik host-katalog
docker run -d \
    -v /home/user/data:/app/data \
    myapp

# Mount current directory (development)
docker run -d \
    -v $(pwd):/app \
    -v $(pwd)/node_modules:/app/node_modules \  # Exclude node_modules
    node:18

# Read-only mount
docker run -d \
    -v /host/config:/app/config:ro \
    myapp
```

**Fördelar:**
- Full kontroll över platsen
- Enkelt för development
- Direkt access till filer

**Nackdelar:**
- Plattformsspecifikt
- Permission-problem vanliga
- Sämre portabilitet

### 3. tmpfs Mounts (In-memory)

```bash
# Temporär data i RAM (försvinner vid restart)
docker run -d \
    --tmpfs /tmp:rw,size=100m \
    myapp

# Användningsfall:
# - Temporära filer
# - Session data
# - Caches som ska vara snabba
# - Känslig data som inte ska skrivas till disk
```

---

## Volume-kommandon

### Skapa och hantera

```bash
# Skapa volume
docker volume create mydata

# Lista volumes
docker volume ls

# Detaljerad info
docker volume inspect mydata

# Output:
# [
#     {
#         "CreatedAt": "2024-01-15T10:30:00Z",
#         "Driver": "local",
#         "Labels": {},
#         "Mountpoint": "/var/lib/docker/volumes/mydata/_data",
#         "Name": "mydata",
#         "Options": {},
#         "Scope": "local"
#     }
# ]

# Ta bort volume (måste vara oanvänd)
docker volume rm mydata

# Ta bort alla oanvända volumes
docker volume prune

# Force remove (även om den används)
docker volume rm -f mydata  # VARNING: Dataförlust!
```

### Mount syntax (nyare --mount vs äldre -v)

```bash
# Gammal syntax (-v)
docker run -v mydata:/app/data nginx
docker run -v /host/path:/container/path nginx

# Ny syntax (--mount) - mer explicit
docker run \
    --mount type=volume,source=mydata,target=/app/data \
    nginx

docker run \
    --mount type=bind,source=/host/path,target=/container/path,readonly \
    nginx

# --mount fördelar:
# - Mer explicit och läsbar
# - Bättre felmeddelanden
# - Stödjer alla options
```

---

## Praktiska scenarier

### Databas med persistent data

```bash
# PostgreSQL
docker run -d \
    --name postgres \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=secret \
    -e POSTGRES_DB=myapp \
    -p 5432:5432 \
    postgres:15

# MySQL
docker run -d \
    --name mysql \
    -v mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -p 3306:3306 \
    mysql:8

# MongoDB
docker run -d \
    --name mongo \
    -v mongo-data:/data/db \
    -p 27017:27017 \
    mongo:6
```

### Development med live reload

```bash
# Node.js development
docker run -d \
    --name node-dev \
    -v $(pwd):/app \
    -v /app/node_modules \        # Anonymous volume för node_modules
    -p 3000:3000 \
    -w /app \
    node:18 npm run dev

# Python development
docker run -d \
    --name python-dev \
    -v $(pwd):/app \
    -p 8000:8000 \
    -w /app \
    python:3.11 python -m flask run --reload
```

### Dela data mellan containers

```bash
# Skapa shared volume
docker volume create shared-data

# Container 1: Writer
docker run -d \
    --name writer \
    -v shared-data:/data \
    alpine sh -c 'while true; do date >> /data/log.txt; sleep 5; done'

# Container 2: Reader
docker run -d \
    --name reader \
    -v shared-data:/data:ro \
    alpine tail -f /data/log.txt
```

---

## Backup och Restore

### Backup volume

```bash
# Backup till tar-fil
docker run --rm \
    -v mydata:/source:ro \
    -v $(pwd):/backup \
    alpine tar czf /backup/mydata-backup.tar.gz -C /source .

# Med tidsstämpel
docker run --rm \
    -v pgdata:/source:ro \
    -v $(pwd):/backup \
    alpine tar czf /backup/pgdata-$(date +%Y%m%d-%H%M%S).tar.gz -C /source .
```

### Restore volume

```bash
# Skapa ny volume
docker volume create restored-data

# Restore från backup
docker run --rm \
    -v restored-data:/target \
    -v $(pwd):/backup:ro \
    alpine tar xzf /backup/mydata-backup.tar.gz -C /target
```

### PostgreSQL-specifik backup

```bash
# Dump databas
docker exec postgres pg_dump -U postgres mydb > backup.sql

# Restore databas
docker exec -i postgres psql -U postgres mydb < backup.sql
```

---

## Permission-problem (vanligt!)

```bash
# Problem: Container körs som annan användare
docker run -v $(pwd):/app alpine ls -la /app
# drwxr-xr-x  user  user  (host user)

# Container körs som root → kan skriva
# Men filer skapas som root på host!

# Lösning 1: Matcha UID
docker run \
    --user $(id -u):$(id -g) \
    -v $(pwd):/app \
    myapp

# Lösning 2: I Dockerfile
RUN useradd -u 1000 appuser
USER appuser

# Lösning 3: Ändra permissions
docker run -v $(pwd):/app alpine chmod -R 777 /app  # Osäkert men fungerar
```

---

## Volume Drivers (avancerat)

```bash
# Default: local driver
docker volume create --driver local mydata

# NFS mount
docker volume create \
    --driver local \
    --opt type=nfs \
    --opt o=addr=192.168.1.1,rw \
    --opt device=:/path/to/dir \
    nfs-data

# Cloud storage (kräver plugin)
docker plugin install rexray/ebs
docker volume create --driver rexray/ebs --opt size=100 ebs-data
```

---

## Praktiska Övningar

### Övning 1: Persistent database

```bash
# 1. Starta postgres utan volume
docker run -d --name pg-temp \
    -e POSTGRES_PASSWORD=secret \
    postgres:15

# 2. Skapa data
docker exec -it pg-temp psql -U postgres -c "CREATE DATABASE testdb;"
docker exec -it pg-temp psql -U postgres testdb -c "CREATE TABLE users (id serial, name text);"
docker exec -it pg-temp psql -U postgres testdb -c "INSERT INTO users (name) VALUES ('Alice');"

# 3. Ta bort containern
docker rm -f pg-temp

# 4. Starta igen - data är BORTA!
docker run -d --name pg-temp -e POSTGRES_PASSWORD=secret postgres:15
docker exec -it pg-temp psql -U postgres -c "\l"  # Ingen testdb!

# 5. Gör rätt med volume
docker rm -f pg-temp
docker volume create pgdata
docker run -d --name pg-persistent \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=secret \
    postgres:15

# 6. Skapa data igen
docker exec -it pg-persistent psql -U postgres -c "CREATE DATABASE testdb;"
docker exec -it pg-persistent psql -U postgres testdb -c "CREATE TABLE users (id serial, name text);"
docker exec -it pg-persistent psql -U postgres testdb -c "INSERT INTO users (name) VALUES ('Bob');"

# 7. Ta bort och återskapa
docker rm -f pg-persistent
docker run -d --name pg-persistent \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=secret \
    postgres:15

# 8. Data finns kvar!
docker exec -it pg-persistent psql -U postgres testdb -c "SELECT * FROM users;"

# 9. Städa upp
docker rm -f pg-persistent
docker volume rm pgdata
```

---

## Sammanfattning

| Typ | Användning | Persistens |
|-----|------------|------------|
| **Named Volume** | Databaser, app-data | ✅ Persistent |
| **Bind Mount** | Development, config | ✅ På host |
| **tmpfs** | Temp files, secrets | ❌ I minnet |

| Kommando | Beskrivning |
|----------|-------------|
| `docker volume create` | Skapa volume |
| `docker volume ls` | Lista volumes |
| `docker volume inspect` | Visa detaljer |
| `docker volume rm` | Ta bort volume |
| `docker volume prune` | Rensa oanvända |
| `-v name:/path` | Mount volume |
| `--mount type=...` | Explicit mount |

---

## Nästa Steg

Du behärskar nu Docker volumes! Nästa task: **Docker Networking** — låt containers prata med varandra.

> 💡 **Pro Tip:** Kör ALDRIG `docker volume prune` i produktion utan att dubbelkolla. En felaktig prune kan radera kritisk data!
"""
            },# Backup volume
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
