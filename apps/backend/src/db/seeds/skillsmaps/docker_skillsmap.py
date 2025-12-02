# =============================================================================
# DOCKER SKILLSMAP - 20 NODER
# Akhilesh Pedagogical Style: Intro → Koncept → Kommandon → Tips → Task
# =============================================================================

DOCKER_SKILLSMAP_INFO = {
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": "Behärska containerisering från grunden till produktion",
    "total_nodes": 20,
    "estimated_hours": 25,
    "difficulty": "intermediate",
    "prerequisites": ["linux-fundamentals"],
    "skills": ["Docker", "Containers", "Images", "Compose", "Networking", "Security"],
}


# =============================================================================
# BLOCK 1: DOCKER FUNDAMENTALS (Noder 1-4)
# =============================================================================

NODE_01_DOCKER_INTRO = {
    "node_id": 1,
    "title": "Docker Introduktion",
    "slug": "docker-intro",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "prerequisites": [],
    "content": '''
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
''',
}

NODE_02_DOCKER_IMAGES = {
    "node_id": 2,
    "title": "Docker Images",
    "slug": "docker-images",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''
# Docker Images

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
''',
}

NODE_03_DOCKERFILE_BASICS = {
    "node_id": 3,
    "title": "Dockerfile Basics",
    "slug": "dockerfile-basics",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "prerequisites": [2],
    "content": '''
# Dockerfile Basics

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
''',
}

NODE_04_CONTAINER_LIFECYCLE = {
    "node_id": 4,
    "title": "Container Lifecycle",
    "slug": "container-lifecycle",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [3],
    "content": '''
# Container Lifecycle

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
''',
}

DOCKER_SKILLSMAP_BLOCK_1 = [
    NODE_01_DOCKER_INTRO,
    NODE_02_DOCKER_IMAGES,
    NODE_03_DOCKERFILE_BASICS,
    NODE_04_CONTAINER_LIFECYCLE,
]

# Block 2-5 kommer i nästa commits
