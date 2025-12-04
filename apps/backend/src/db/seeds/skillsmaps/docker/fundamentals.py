# =============================================================================
# DOCKER FUNDAMENTALS — Noder 1-4
# Premium Bootcamp-Quality Content
# =============================================================================

NODE_01_DOCKER_INTRO = {
    "id": "docker-intro",
    "node_id": 1,
    "title": "Docker Introduktion",
    "slug": "docker-intro",
    "description": "Förstå varför Docker revolutionerade mjukvaruutveckling och hur det löser verkliga problem",
    "type": "concept",
    "difficulty": "easy",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "prerequisites": [],
    "content": '''# 🐳 Docker Introduktion — Containerrevolutionen

## Lärande mål
Efter denna lektion kommer du att:
- Förstå varför Docker skapades och vilka problem det löser
- Kunna förklara skillnaden mellan containers och virtuella maskiner
- Ha Docker installerat och kört din första container
- Förstå Docker-ekosystemet och dess komponenter

---

## 📖 Problemet Docker löser

### "It works on my machine" — Den eviga mardrömen

Varje utvecklare har hört det. Koden fungerar perfekt lokalt men kraschar i produktion.

```
┌─────────────────────────────────────────────────────────────────┐
│                    UTAN DOCKER                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Developer laptop          Staging Server        Production     │
│  ┌─────────────┐          ┌─────────────┐      ┌─────────────┐ │
│  │ Python 3.11 │          │ Python 3.9  │      │ Python 3.8  │ │
│  │ Ubuntu 22   │          │ CentOS 7    │      │ RHEL 8      │ │
│  │ Node 18     │          │ Node 16     │      │ Node 14     │ │
│  └─────────────┘          └─────────────┘      └─────────────┘ │
│        ✅                        ⚠️                   ❌        │
│    "Funkar!"              "Konstigt..."         "KRASCH!"       │
└─────────────────────────────────────────────────────────────────┘
```

**Verkliga scenarion:**
- Utvecklaren använder macOS, servern kör Linux
- Lokalt: Python 3.11, produktion: Python 3.8
- Bibliotek installerade globalt i dev, saknas i prod
- Olika versioner av systembibliotek

### Dockers lösning: Paketera ALLT

```
┌─────────────────────────────────────────────────────────────────┐
│                    MED DOCKER                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │              DOCKER IMAGE: my-app:v1.0                      │ │
│  │  ┌────────────────────────────────────────────────────────┐│ │
│  │  │ Applikationskod                                        ││ │
│  │  │ Python 3.11 + alla dependencies                        ││ │
│  │  │ Node 18 + npm packages                                 ││ │
│  │  │ Systembibliotek                                        ││ │
│  │  │ Konfigurationsfiler                                    ││ │
│  │  └────────────────────────────────────────────────────────┘│ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  Developer laptop          Staging Server        Production     │
│        ✅                        ✅                   ✅        │
│   IDENTISKT ÖVERALLT!                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Container vs Virtuell Maskin

### Virtuella maskiner (VMs)

```
┌─────────────────────────────────────────────────────────────┐
│                    VIRTUELLA MASKINER                        │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │   App A   │  │   App B   │  │   App C   │               │
│  ├───────────┤  ├───────────┤  ├───────────┤               │
│  │  Bins/Lib │  │  Bins/Lib │  │  Bins/Lib │               │
│  ├───────────┤  ├───────────┤  ├───────────┤               │
│  │ Guest OS  │  │ Guest OS  │  │ Guest OS  │  <- Fullständigt OS!
│  │  (2GB+)   │  │  (2GB+)   │  │  (2GB+)   │               │
│  └───────────┘  └───────────┘  └───────────┘               │
│  ┌─────────────────────────────────────────────────────────┤
│  │              HYPERVISOR (VMware/VirtualBox)              │
│  ├─────────────────────────────────────────────────────────┤
│  │                     HOST OS                              │
│  ├─────────────────────────────────────────────────────────┤
│  │                   HÅRDVARA                               │
│  └─────────────────────────────────────────────────────────┘
└─────────────────────────────────────────────────────────────┘

Totalt minne: ~6GB+ bara för OS
Starttid: Minuter
```

### Docker Containers

```
┌─────────────────────────────────────────────────────────────┐
│                      CONTAINERS                              │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │   App A   │  │   App B   │  │   App C   │               │
│  ├───────────┤  ├───────────┤  ├───────────┤               │
│  │  Bins/Lib │  │  Bins/Lib │  │  Bins/Lib │  <- Endast det│
│  │  (50MB)   │  │  (50MB)   │  │  (50MB)   │     som behövs│
│  └───────────┘  └───────────┘  └───────────┘               │
│  ┌─────────────────────────────────────────────────────────┤
│  │              DOCKER ENGINE                               │
│  ├─────────────────────────────────────────────────────────┤
│  │                 HOST OS (Linux kernel)                   │
│  ├─────────────────────────────────────────────────────────┤
│  │                   HÅRDVARA                               │
│  └─────────────────────────────────────────────────────────┘
└─────────────────────────────────────────────────────────────┘

Totalt minne: ~150MB för alla tre
Starttid: Sekunder
```

### Jämförelse

| Aspekt | VM | Container |
|--------|-----|-----------|
| **Starttid** | Minuter | Sekunder |
| **Storlek** | GB | MB |
| **Minne** | Stort overhead | Minimal overhead |
| **Prestanda** | ~70-80% av native | ~95-99% av native |
| **Isolering** | Fullständig (separat OS) | Process-nivå |
| **Portabilitet** | Bunden till hypervisor | Kör överallt med Docker |

---

## 🛠️ Installation

### macOS

```bash
# Alternativ 1: Homebrew (rekommenderat)
brew install --cask docker

# Starta Docker Desktop från Applications
# Vänta på "Docker is running" i menyraden

# Verifiera
docker --version
docker run hello-world
```

### Ubuntu/Debian

```bash
# Uppdatera paketindex
sudo apt-get update

# Installera dependencies
sudo apt-get install -y \\
    ca-certificates \\
    curl \\
    gnupg \\
    lsb-release

# Lägg till Dockers officiella GPG-nyckel
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \\
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Lägg till repository
echo \\
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \\
  https://download.docker.com/linux/ubuntu \\
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Kör Docker utan sudo (valfritt men rekommenderat)
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker --version
docker run hello-world
```

### Windows (WSL2)

```powershell
# 1. Aktivera WSL2
wsl --install

# 2. Ladda ner Docker Desktop från docker.com
# 3. Under installation: välj "Use WSL 2 instead of Hyper-V"
# 4. Starta Docker Desktop
# 5. I Settings > Resources > WSL Integration: aktivera din distro

# Verifiera i WSL terminal
docker --version
docker run hello-world
```

---

## 🎯 Din första container

### Kör hello-world

```bash
$ docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:2498fce14358aa50ead0cc6c19990fc6ff866ce72aeb5546e1d59caac3d0d60f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image.
 4. The Docker daemon streamed that output to the Docker client.
```

### Vad hände egentligen?

```
┌─────────────────────────────────────────────────────────────────┐
│                     docker run hello-world                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Docker CLI → Docker Daemon                                  │
│     "Jag vill köra hello-world"                                 │
│                                                                  │
│  2. Docker Daemon kollar lokalt                                 │
│     "Finns inte lokalt..."                                      │
│                                                                  │
│  3. Docker Daemon → Docker Hub                                  │
│     "Laddar ner hello-world:latest"                             │
│                                                                  │
│  4. Image sparas lokalt                                         │
│     ~/.docker/images/hello-world                                │
│                                                                  │
│  5. Container skapas från image                                 │
│     Isolerad process startar                                    │
│                                                                  │
│  6. Output skrivs till terminalen                               │
│     Container avslutas                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Kör en interaktiv container

```bash
# Starta Ubuntu och få ett shell
$ docker run -it ubuntu bash

root@a1b2c3d4e5f6:/# cat /etc/os-release
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"

root@a1b2c3d4e5f6:/# apt update && apt install -y curl
# ... installerar curl ...

root@a1b2c3d4e5f6:/# curl --version
curl 7.81.0

root@a1b2c3d4e5f6:/# exit
```

**Flaggor förklarade:**
- `-i` = interactive (håll STDIN öppen)
- `-t` = tty (ge en terminal)
- `ubuntu` = image att köra
- `bash` = kommando att köra i containern

---

## 📋 Grundläggande Docker-kommandon

### Container-livscykeln

```bash
# STARTA
docker run nginx                    # Kör i förgrunden
docker run -d nginx                 # Kör i bakgrunden (detached)
docker run -d --name web nginx      # Med eget namn

# LISTA
docker ps                           # Körande containers
docker ps -a                        # Alla containers (inkl. stoppade)

# INSPEKTERA
docker logs web                     # Visa loggar
docker logs -f web                  # Följ loggar i realtid
docker inspect web                  # Detaljerad JSON-info

# INTERAGERA
docker exec -it web bash            # Kör kommando i körande container
docker attach web                   # Anslut till container (Ctrl+P, Ctrl+Q för att lämna)

# STOPPA
docker stop web                     # Graceful stop (SIGTERM, sen SIGKILL)
docker kill web                     # Forcerad stop (SIGKILL direkt)

# TA BORT
docker rm web                       # Ta bort stoppad container
docker rm -f web                    # Tvinga bort även körande
```

### Praktiskt exempel

```bash
# Starta en nginx-webbserver
docker run -d --name myserver -p 8080:80 nginx

# Kontrollera att den körs
docker ps
# CONTAINER ID   IMAGE   ...   PORTS                  NAMES
# a1b2c3d4e5f6   nginx   ...   0.0.0.0:8080->80/tcp   myserver

# Besök http://localhost:8080 i webbläsaren!

# Kolla loggarna
docker logs myserver

# Kör bash inuti containern
docker exec -it myserver bash
ls /usr/share/nginx/html/
cat /usr/share/nginx/html/index.html
exit

# Stoppa och ta bort
docker stop myserver
docker rm myserver
```

---

## 🧩 Docker-ekosystemet

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER ECOSYSTEM                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │ Docker CLI  │ →  │ Docker      │ →  │  Container  │         │
│  │   (docker)  │    │   Daemon    │    │   Runtime   │         │
│  └─────────────┘    └─────────────┘    └─────────────┘         │
│         │                  │                                    │
│         │                  ↓                                    │
│         │           ┌─────────────┐                             │
│         │           │ Docker Hub  │  ← Images repository        │
│         │           └─────────────┘                             │
│         │                                                       │
│         ↓                                                       │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │ Docker      │    │ Docker      │    │ Docker      │         │
│  │ Compose     │    │ Swarm       │    │ Desktop     │         │
│  │ (multi-     │    │ (clustering)│    │ (GUI)       │         │
│  │ container)  │    │             │    │             │         │
│  └─────────────┘    └─────────────┘    └─────────────┘         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Komponenterna:**

| Komponent | Syfte |
|-----------|-------|
| **Docker CLI** | Kommandoradsverktyg för att interagera med Docker |
| **Docker Daemon** | Bakgrundsprocess som hanterar containers |
| **Docker Hub** | Publik registry för images |
| **Docker Compose** | Verktyg för multi-container applikationer |
| **Docker Desktop** | GUI för macOS/Windows |
| **Docker Swarm** | Inbyggd orchestration (Kubernetes är vanligare) |

---

## ✅ Kunskapskontroll

Innan du går vidare, se till att du kan svara på:

1. **Varför skapades Docker?**
   - Löser "works on my machine"-problemet
   - Lättvikts alternativ till VMs
   - Portabilitet mellan miljöer

2. **Vad är skillnaden mellan container och VM?**
   - Containers delar host OS kernel
   - VMs har eget OS per instans
   - Containers är snabbare och lättare

3. **Vilka kommandon behöver du för att:**
   - Starta en container? `docker run`
   - Se körande containers? `docker ps`
   - Stoppa en container? `docker stop`
   - Ta bort en container? `docker rm`

---

## 🏋️ Övningar

### Övning 1: Utforska containers
```bash
# 1. Kör en Alpine Linux container interaktivt
docker run -it alpine sh

# 2. Inuti containern:
cat /etc/os-release
uname -a
ls -la
exit

# 3. Lista alla containers (inkl. stoppade)
docker ps -a

# 4. Ta bort containern
docker rm <container_id>
```

### Övning 2: Webbserver-experiment
```bash
# 1. Starta nginx på port 8080
docker run -d --name webb -p 8080:80 nginx

# 2. Verifiera med curl
curl localhost:8080

# 3. Ändra välkomstsidan
docker exec -it webb bash
echo "<h1>Hej från Docker!</h1>" > /usr/share/nginx/html/index.html
exit

# 4. Besök localhost:8080 igen
curl localhost:8080

# 5. Städa upp
docker stop webb && docker rm webb
```

---

**Nästa steg:** Node 2 - Docker Images och Dockerfile
''',
}


NODE_02_DOCKER_IMAGES = {
    "id": "docker-images",
    "node_id": 2,
    "title": "Docker Images & Dockerfile",
    "slug": "docker-images",
    "description": "Lär dig bygga egna images med Dockerfile",
    "type": "concept",
    "difficulty": "easy",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "prerequisites": [1],
    "content": '''# 🖼️ Docker Images & Dockerfile

## Lärande mål
Efter denna lektion kommer du att:
- Förstå vad en Docker Image är och hur den är uppbyggd
- Kunna skriva en Dockerfile från scratch
- Förstå och använda alla viktiga Dockerfile-instruktioner
- Bygga och tagga egna images
- Förstå layer-caching och optimering

---

## 📖 Vad är en Docker Image?

### Definition
En Docker Image är en **skrivskyddad mall** som innehåller allt som behövs för att köra en applikation:
- Operativsystem-bas (Alpine, Ubuntu, Debian)
- Runtime (Python, Node.js, Java)
- Applikationskod
- Dependencies och bibliotek
- Miljövariabler och konfiguration

### Images är lager (Layers)

```
┌─────────────────────────────────────────────────────────────────┐
│                    IMAGE: my-python-app:1.0                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 6: CMD ["python", "app.py"]              (0 KB)          │
│  ─────────────────────────────────────────────────────          │
│  Layer 5: COPY app.py /app/                     (5 KB)          │
│  ─────────────────────────────────────────────────────          │
│  Layer 4: RUN pip install flask requests        (15 MB)         │
│  ─────────────────────────────────────────────────────          │
│  Layer 3: WORKDIR /app                          (0 KB)          │
│  ─────────────────────────────────────────────────────          │
│  Layer 2: python:3.11-slim                      (120 MB)        │
│  ─────────────────────────────────────────────────────          │
│  Layer 1: Base OS (Debian slim)                 (80 MB)         │
│                                                                  │
│  Total: ~215 MB                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Varför lager?**
- **Delning:** Flera images kan dela samma bas-lager
- **Caching:** Oförändrade lager cachas → snabbare builds
- **Effektivitet:** Bara ändrade lager laddas om

---

## 📝 Dockerfile — Grunden

### Enkel Dockerfile

```dockerfile
# Bas-image
FROM python:3.11-slim

# Sätt arbetskatalog
WORKDIR /app

# Kopiera requirements först (för caching)
COPY requirements.txt .

# Installera dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera applikationskod
COPY . .

# Exponera port
EXPOSE 8000

# Startkommando
CMD ["python", "app.py"]
```

### Alla viktiga instruktioner

| Instruktion | Syfte | Exempel |
|-------------|-------|---------|
| `FROM` | Bas-image | `FROM python:3.11-slim` |
| `WORKDIR` | Sätt arbetskatalog | `WORKDIR /app` |
| `COPY` | Kopiera filer från host | `COPY . .` |
| `ADD` | Som COPY + URL + tar-extraktion | `ADD https://... /app/` |
| `RUN` | Kör kommando under build | `RUN apt-get update` |
| `ENV` | Sätt miljövariabel | `ENV NODE_ENV=production` |
| `EXPOSE` | Dokumentera port | `EXPOSE 3000` |
| `CMD` | Default startkommando | `CMD ["npm", "start"]` |
| `ENTRYPOINT` | Icke-överskrivbart kommando | `ENTRYPOINT ["python"]` |
| `ARG` | Build-time variabler | `ARG VERSION=1.0` |
| `USER` | Byt användare | `USER appuser` |
| `VOLUME` | Deklarera mount point | `VOLUME /data` |

---

## 🏗️ Praktiska exempel

### Python Flask-app

**app.py:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Docker!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt:**
```
flask==3.0.0
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

# Skapa non-root user
RUN useradd --create-home appuser

WORKDIR /app

# Kopiera och installera dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera appkod
COPY app.py .

# Byt till non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
```

**Bygg och kör:**
```bash
# Bygg image
docker build -t my-flask-app:1.0 .

# Kör container
docker run -d -p 5000:5000 my-flask-app:1.0

# Testa
curl localhost:5000
```

### Node.js Express-app

**package.json:**
```json
{
  "name": "docker-node",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

**server.js:**
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: 'Hello from Docker!', timestamp: new Date() });
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

**Dockerfile:**
```dockerfile
FROM node:20-alpine

# Skapa app-katalog
WORKDIR /app

# Kopiera package files
COPY package*.json ./

# Installera dependencies
RUN npm ci --only=production

# Kopiera källkod
COPY . .

# Skapa non-root user
RUN addgroup -g 1001 -S nodejs && \\
    adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000

CMD ["npm", "start"]
```

---

## 🚀 Build-kommandon

### Grundläggande build

```bash
# Bygg med default tag (latest)
docker build -t my-app .

# Bygg med specifik tag
docker build -t my-app:1.0.0 .

# Bygg med flera tags
docker build -t my-app:1.0.0 -t my-app:latest .

# Bygg från annan Dockerfile
docker build -f Dockerfile.prod -t my-app:prod .

# Bygg utan cache
docker build --no-cache -t my-app .

# Bygg med build arguments
docker build --build-arg VERSION=2.0 -t my-app .
```

### Inspektera images

```bash
# Lista alla lokala images
docker images

# Visa image-historik (layers)
docker history my-app:1.0.0

# Detaljerad info
docker inspect my-app:1.0.0

# Visa storlek per layer
docker history --no-trunc my-app:1.0.0
```

---

## ⚡ Layer Caching — Kritiskt för snabba builds

### Hur caching fungerar

```dockerfile
# ❌ DÅLIGT - Allt ombyggs vid kodändring
FROM node:20-alpine
WORKDIR /app
COPY . .                    # <- Ändras ofta → alla efterföljande lager ombyggs
RUN npm install
CMD ["npm", "start"]
```

```dockerfile
# ✅ BRA - Dependencies cachas separat
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./       # <- Ändras sällan
RUN npm install             # <- Cachas så länge package.json är samma!
COPY . .                    # <- Endast detta lager ombyggs vid kodändring
CMD ["npm", "start"]
```

### Cache-invalidering

```
┌─────────────────────────────────────────────────────────────────┐
│              LAYER CACHE INVALIDERING                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FROM node:20-alpine          ✅ Cached                         │
│  WORKDIR /app                 ✅ Cached                         │
│  COPY package.json .          ✅ Cached (om oförändrad)         │
│  RUN npm install              ✅ Cached (om package.json samma) │
│  COPY . .                     🔄 Ombyggs (kod ändrad)           │
│  CMD ["npm", "start"]         🔄 Ombyggs (layer före ändrades)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Best Practices

### 1. Använd specifika bas-image tags

```dockerfile
# ❌ DÅLIGT - "latest" kan ändras
FROM python:latest

# ✅ BRA - Specifik version
FROM python:3.11.7-slim-bookworm
```

### 2. Minimera antal lager

```dockerfile
# ❌ DÅLIGT - Många RUN-instruktioner
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# ✅ BRA - Kombinera till ett lager
RUN apt-get update && \\
    apt-get install -y curl git && \\
    rm -rf /var/lib/apt/lists/*
```

### 3. Använd .dockerignore

**.dockerignore:**
```
# Version control
.git
.gitignore

# Dependencies (installeras i container)
node_modules
__pycache__
*.pyc
.venv

# IDE
.vscode
.idea

# Testing/docs
tests/
docs/
*.md

# Env files
.env
.env.local
```

### 4. Non-root user

```dockerfile
# Skapa användare
RUN useradd --create-home --shell /bin/bash appuser

# Byt till användaren
USER appuser

# Nu körs CMD som appuser, inte root
CMD ["python", "app.py"]
```

---

## 🏷️ Tagging-strategi

### Semantic Versioning

```bash
# Major.Minor.Patch
docker build -t my-app:1.0.0 .
docker build -t my-app:1.0.1 .  # Bugfix
docker build -t my-app:1.1.0 .  # Ny feature
docker build -t my-app:2.0.0 .  # Breaking change
```

### Git-baserad tagging

```bash
# Med git commit hash
docker build -t my-app:$(git rev-parse --short HEAD) .

# Med git tag
docker build -t my-app:$(git describe --tags) .
```

### Multi-tag strategi

```bash
# Bygg med flera tags
docker build \\
  -t my-app:1.2.3 \\
  -t my-app:1.2 \\
  -t my-app:1 \\
  -t my-app:latest \\
  .
```

---

## ✅ Kunskapskontroll

1. **Vad är skillnaden mellan COPY och ADD?**
   - COPY: Enkel fil-kopiering
   - ADD: + URL-support + automatisk tar-extraktion

2. **Varför är layer-ordning viktig?**
   - Oftast-ändrade lager sist → bättre caching
   - Dependencies före kod

3. **Vad gör .dockerignore?**
   - Exkluderar filer från build context
   - Snabbare builds, mindre images

---

## 🏋️ Övningar

### Övning 1: Bygg en Python-app
```bash
# Skapa projektmapp
mkdir python-docker && cd python-docker

# Skapa app.py
cat > app.py << 'EOF'
import os
print(f"Hello! Running in: {os.environ.get('ENVIRONMENT', 'unknown')}")
EOF

# Skapa Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.11-alpine
WORKDIR /app
ENV ENVIRONMENT=docker
COPY app.py .
CMD ["python", "app.py"]
EOF

# Bygg och kör
docker build -t my-python:1.0 .
docker run my-python:1.0
```

### Övning 2: Multi-stage experiment
```bash
# Jämför storlek
docker images | grep python
# python:3.11         ~900MB
# python:3.11-slim    ~120MB
# python:3.11-alpine  ~50MB
```

---

**Nästa steg:** Node 3 - Docker Volumes och Data
''',
}


NODE_03_DOCKER_CONTAINERS = {
    "id": "docker-containers",
    "node_id": 3,
    "title": "Container Lifecycle & Management",
    "slug": "docker-containers",
    "description": "Behärska container-livscykeln och hantering",
    "type": "practice",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 110,
    "prerequisites": [2],
    "content": '''# 🔄 Container Lifecycle & Management

## Lärande mål
Efter denna lektion kommer du att:
- Förstå containerns kompletta livscykel
- Kunna hantera container-tillstånd professionellt
- Använda resursbegränsningar effektivt
- Debugga containers med loggar och exec

---

## 📖 Container-livscykeln

### Tillstånd

```
┌─────────────────────────────────────────────────────────────────┐
│                  CONTAINER LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    docker create                                │
│                         ↓                                       │
│  ┌─────────────┐   docker start   ┌─────────────┐              │
│  │   CREATED   │ ─────────────→   │   RUNNING   │              │
│  └─────────────┘                  └─────────────┘              │
│                                          │                      │
│                                    docker stop                  │
│                                          ↓                      │
│                                   ┌─────────────┐              │
│                                   │   STOPPED   │              │
│                                   └─────────────┘              │
│                                          │                      │
│                              docker start │ docker rm           │
│                                    ↓      │      ↓              │
│                              ┌─────────┐  │  ┌─────────┐       │
│                              │ RUNNING │  │  │ REMOVED │       │
│                              └─────────┘  │  └─────────┘       │
│                                          │                      │
│  docker run = docker create + docker start                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Tillståndskommandon

```bash
# Skapa utan att starta
docker create --name myapp nginx
docker ps -a  # STATUS: Created

# Starta
docker start myapp
docker ps     # STATUS: Up X seconds

# Pausa (fryser processer)
docker pause myapp
docker ps     # STATUS: Up X seconds (Paused)

# Avpausa
docker unpause myapp

# Stoppa (SIGTERM → 10s → SIGKILL)
docker stop myapp
docker ps -a  # STATUS: Exited (0)

# Starta om stoppad
docker start myapp

# Restart (stop + start)
docker restart myapp

# Tvinga stopp (SIGKILL direkt)
docker kill myapp

# Ta bort
docker rm myapp

# Ta bort körande (force)
docker rm -f myapp
```

---

## 🚀 Run-flaggor i detalj

### Detached mode (-d)

```bash
# Förgrund (blockerar terminal)
docker run nginx
# Ctrl+C för att stoppa

# Bakgrund (returnerar direkt)
docker run -d nginx
# Returnerar container ID
```

### Interaktiv mode (-it)

```bash
# -i = interactive (håll STDIN öppen)
# -t = tty (allokera pseudo-terminal)
docker run -it ubuntu bash

# Endast -i (för pipelines)
echo "hello" | docker run -i alpine cat
```

### Namngivning (--name)

```bash
# Automatiskt namn
docker run -d nginx
# NAMES: amazing_einstein

# Eget namn
docker run -d --name webserver nginx
# NAMES: webserver

# Användbart för:
docker logs webserver
docker stop webserver
docker exec -it webserver bash
```

### Automatisk borttagning (--rm)

```bash
# Container tas bort när den stoppar
docker run --rm nginx
# Perfekt för engångskörningar

docker run --rm alpine echo "Hello"
# Container försvinner efter output
```

### Port-mappning (-p)

```bash
# HOST_PORT:CONTAINER_PORT
docker run -d -p 8080:80 nginx
# localhost:8080 → container:80

# Slumpmässig host-port
docker run -d -p 80 nginx
# docker ps visar vilken port

# Specifik IP
docker run -d -p 127.0.0.1:8080:80 nginx

# Flera portar
docker run -d -p 80:80 -p 443:443 nginx
```

### Miljövariabler (-e)

```bash
# Enkel variabel
docker run -e NODE_ENV=production node-app

# Flera variabler
docker run -e NODE_ENV=production -e DEBUG=true node-app

# Från fil
docker run --env-file .env node-app
```

---

## 💾 Resursbegränsningar

### Minne

```bash
# Begränsa till 512MB
docker run -d --memory=512m nginx

# Med swap
docker run -d --memory=512m --memory-swap=1g nginx

# Reservation (soft limit)
docker run -d --memory=512m --memory-reservation=256m nginx
```

### CPU

```bash
# Begränsa till 1.5 CPU-cores
docker run -d --cpus=1.5 nginx

# CPU-shares (relativt andra containers)
docker run -d --cpu-shares=512 nginx  # Default är 1024

# Specifika cores
docker run -d --cpuset-cpus="0,1" nginx  # Endast core 0 och 1
```

### Disk I/O

```bash
# Begränsa läs-hastighet
docker run -d --device-read-bps=/dev/sda:1mb nginx

# Begränsa skriv-hastighet
docker run -d --device-write-bps=/dev/sda:1mb nginx
```

### Se resurser i realtid

```bash
# Alla containers
docker stats

# Specifik container
docker stats webserver

# Formaterad output
docker stats --format "table {{.Name}}\\t{{.CPUPerc}}\\t{{.MemUsage}}"
```

---

## 🔍 Debugging & Inspektion

### Loggar

```bash
# Visa alla loggar
docker logs webserver

# Följ i realtid
docker logs -f webserver

# Senaste N rader
docker logs --tail 100 webserver

# Med timestamps
docker logs -t webserver

# Sedan viss tid
docker logs --since 10m webserver
docker logs --since 2024-01-01T00:00:00 webserver
```

### Exec — Kör kommandon

```bash
# Interaktiv shell
docker exec -it webserver bash

# Enkel kommando
docker exec webserver cat /etc/nginx/nginx.conf

# Som annan användare
docker exec -u root webserver whoami

# Med miljövariabler
docker exec -e DEBUG=true webserver printenv
```

### Inspect — Detaljerad info

```bash
# All info (lång JSON)
docker inspect webserver

# Specifik info med format
docker inspect --format='{{.State.Status}}' webserver
docker inspect --format='{{.NetworkSettings.IPAddress}}' webserver
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' webserver
```

### Top — Processer

```bash
# Visa processer i container
docker top webserver

# Output:
# UID   PID    PPID   CMD
# root  1234   1233   nginx: master process
# www   1235   1234   nginx: worker process
```

### Diff — Filsystemändringar

```bash
# Visa ändringar sedan start
docker diff webserver

# Output:
# C /var           # Changed
# A /var/log/app   # Added
# D /tmp/cache     # Deleted
```

---

## 🧹 Städning

### Ta bort containers

```bash
# Ta bort stoppad container
docker rm webserver

# Ta bort alla stoppade
docker container prune

# Force ta bort körande
docker rm -f webserver

# Ta bort alla (farligt!)
docker rm -f $(docker ps -aq)
```

### Ta bort images

```bash
# Ta bort specifik
docker rmi nginx:latest

# Ta bort oanvända
docker image prune

# Ta bort ALLA oanvända (inkl. tagged)
docker image prune -a
```

### Total städning

```bash
# Ta bort ALLT oanvänt
docker system prune

# Inkludera volumes (data försvinner!)
docker system prune --volumes

# Visa vad som tar plats
docker system df
```

---

## 🏋️ Övningar

### Övning 1: Livscykelhantering
```bash
# 1. Skapa utan att starta
docker create --name lifecycle-test alpine echo "Hello"
docker ps -a | grep lifecycle-test

# 2. Starta och se output
docker start -a lifecycle-test

# 3. Starta igen
docker start -a lifecycle-test

# 4. Ta bort
docker rm lifecycle-test
```

### Övning 2: Resursbegränsning
```bash
# Starta med begränsningar
docker run -d --name limited \\
  --memory=128m \\
  --cpus=0.5 \\
  nginx

# Övervaka
docker stats limited

# Städa
docker rm -f limited
```

---

**Nästa steg:** Node 4 - Docker Volumes och persistent data
''',
}


NODE_04_DOCKER_VOLUMES = {
    "id": "docker-volumes",
    "node_id": 4,
    "title": "Docker Volumes & Persistent Data",
    "slug": "docker-volumes",
    "description": "Hantera persistent data med volumes och bind mounts",
    "type": "concept",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 130,
    "prerequisites": [3],
    "content": '''# 💾 Docker Volumes & Persistent Data

## Lärande mål
Efter denna lektion kommer du att:
- Förstå varför containers behöver volumes
- Kunna använda named volumes, bind mounts och tmpfs
- Hantera data-livscykeln professionellt
- Implementera backup och restore av data

---

## 📖 Problemet med container-data

### Containers är flyktiga

```
┌─────────────────────────────────────────────────────────────────┐
│                    UTAN VOLUMES                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Container 1 (v1.0)          Container 2 (v1.1)               │
│   ┌─────────────────┐         ┌─────────────────┐              │
│   │ /data           │         │ /data           │              │
│   │  - users.db     │   →→→   │  (TOM!)         │              │
│   │  - cache/       │  Uppg.  │                 │              │
│   │  - uploads/     │         │                 │              │
│   └─────────────────┘         └─────────────────┘              │
│                                                                  │
│   Data FÖRSVINNER vid:                                          │
│   • docker rm                                                   │
│   • Container crash                                             │
│   • Image update                                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Med volumes

```
┌─────────────────────────────────────────────────────────────────┐
│                    MED VOLUMES                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Container 1 (v1.0)          Container 2 (v1.1)               │
│   ┌─────────────────┐         ┌─────────────────┐              │
│   │ /data ─────────────────────────→ /data      │              │
│   └─────────────────┘         └─────────────────┘              │
│              │                         │                        │
│              └───────────┬─────────────┘                        │
│                          │                                      │
│                   ┌──────▼──────┐                               │
│                   │   VOLUME    │                               │
│                   │ - users.db  │ ← Data BEVARAS!              │
│                   │ - cache/    │                               │
│                   │ - uploads/  │                               │
│                   └─────────────┘                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Tre typer av data-storage

### 1. Named Volumes (Rekommenderat)

```bash
# Docker hanterar allt
docker volume create mydata
docker run -v mydata:/app/data nginx

# Data sparas i /var/lib/docker/volumes/mydata/_data
```

### 2. Bind Mounts (Host-katalog)

```bash
# Mappar host-katalog till container
docker run -v /home/user/data:/app/data nginx

# Eller med $(pwd)
docker run -v $(pwd)/data:/app/data nginx
```

### 3. tmpfs Mounts (I minnet)

```bash
# Data i RAM (snabbt, flyktigt)
docker run --tmpfs /app/cache nginx
```

### Jämförelse

| Typ | Var sparas data? | Persistens | Use case |
|-----|------------------|------------|----------|
| **Named Volume** | Docker-hanterad | ✅ Persistent | Databaser, uploads |
| **Bind Mount** | Host-filesystem | ✅ Persistent | Development, configs |
| **tmpfs** | RAM | ❌ Flyktigt | Cache, secrets |

---

## 📁 Named Volumes — Detaljerat

### Skapa och hantera

```bash
# Skapa volume
docker volume create mydata

# Lista volumes
docker volume ls

# Inspektera
docker volume inspect mydata
# {
#     "Name": "mydata",
#     "Driver": "local",
#     "Mountpoint": "/var/lib/docker/volumes/mydata/_data",
#     "Labels": {},
#     "Scope": "local"
# }

# Ta bort
docker volume rm mydata

# Ta bort alla oanvända
docker volume prune
```

### Använda med containers

```bash
# Skapa volume automatiskt om den inte finns
docker run -d --name db \\
    -v postgres_data:/var/lib/postgresql/data \\
    postgres:15

# Samma volume till ny container
docker run -d --name db2 \\
    -v postgres_data:/var/lib/postgresql/data \\
    postgres:15
```

### Read-only volumes

```bash
# Container kan bara läsa
docker run -v mydata:/app/data:ro nginx
```

---

## 📂 Bind Mounts — Detaljerat

### Development workflow

```bash
# Mappa lokal kod till container
docker run -d --name dev \\
    -v $(pwd)/src:/app/src \\
    -v $(pwd)/package.json:/app/package.json \\
    -p 3000:3000 \\
    node:20 npm run dev
```

```
┌─────────────────────────────────────────────────────────────────┐
│                    BIND MOUNT FÖR DEV                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   HOST                              CONTAINER                   │
│   ~/project/                        /app/                       │
│   ├── src/        ←────────────→    ├── src/                   │
│   │   ├── app.js  (synkad!)         │   ├── app.js             │
│   │   └── ...                       │   └── ...                │
│   └── package.json ←────────────→   └── package.json           │
│                                                                  │
│   Ändringar på host → omedelbart i container                   │
│   Hot-reload fungerar!                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Ny --mount syntax (rekommenderas)

```bash
# Bind mount med --mount
docker run -d \\
    --mount type=bind,source=$(pwd)/data,target=/app/data \\
    nginx

# Named volume med --mount
docker run -d \\
    --mount type=volume,source=mydata,target=/app/data \\
    nginx

# Read-only
docker run -d \\
    --mount type=bind,source=$(pwd)/config,target=/app/config,readonly \\
    nginx
```

---

## 🔐 Praktiska patterns

### Database med volume

```bash
# PostgreSQL
docker run -d --name postgres \\
    -e POSTGRES_PASSWORD=secret \\
    -v pg_data:/var/lib/postgresql/data \\
    -p 5432:5432 \\
    postgres:15

# MySQL
docker run -d --name mysql \\
    -e MYSQL_ROOT_PASSWORD=secret \\
    -v mysql_data:/var/lib/mysql \\
    -p 3306:3306 \\
    mysql:8

# MongoDB
docker run -d --name mongo \\
    -v mongo_data:/data/db \\
    -p 27017:27017 \\
    mongo:7
```

### Delad data mellan containers

```bash
# Skapa delad volume
docker volume create shared_data

# Container 1 skriver
docker run -d --name writer \\
    -v shared_data:/data \\
    alpine sh -c "while true; do date >> /data/log.txt; sleep 5; done"

# Container 2 läser
docker run --rm \\
    -v shared_data:/data:ro \\
    alpine tail -f /data/log.txt
```

---

## 💾 Backup & Restore

### Backup en volume

```bash
# Backup till tar-fil
docker run --rm \\
    -v pg_data:/data:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/pg_data_backup.tar.gz -C /data .

# Verifiera backup
tar tzf pg_data_backup.tar.gz | head
```

### Restore från backup

```bash
# Skapa ny volume
docker volume create pg_data_restored

# Restore från tar
docker run --rm \\
    -v pg_data_restored:/data \\
    -v $(pwd):/backup:ro \\
    alpine tar xzf /backup/pg_data_backup.tar.gz -C /data
```

### Kopiera mellan volumes

```bash
# Direkt kopiering
docker run --rm \\
    -v source_volume:/source:ro \\
    -v dest_volume:/dest \\
    alpine cp -a /source/. /dest/
```

---

## ⚠️ Vanliga problem

### Permission issues

```bash
# Problem: Container kan inte skriva
# Lösning 1: Matcha UID/GID
docker run -u $(id -u):$(id -g) -v $(pwd)/data:/app/data myapp

# Lösning 2: Ändra permissions på host
chmod -R 777 ./data  # (inte säkert i prod!)

# Lösning 3: Skapa user i Dockerfile med rätt UID
```

### macOS/Windows: Långsamma bind mounts

```bash
# Problem: Sync är långsam för node_modules
# Lösning: Använd named volume för dependencies

docker run -d \\
    -v $(pwd):/app \\
    -v node_modules:/app/node_modules \\  # Named volume!
    node:20 npm run dev
```

---

## ✅ Kunskapskontroll

1. **När ska du använda named volumes vs bind mounts?**
   - Named: Databaser, persistent app-data
   - Bind: Development, konfigurationsfiler

2. **Hur gör du backup av en volume?**
   - Kör container med volumen monterad + backup-katalog
   - Använd tar för att packa datan

3. **Vad händer med data när du tar bort en container?**
   - Utan volume: Data försvinner
   - Med volume: Data bevaras i volumen

---

## 🏋️ Övningar

### Övning 1: Database persistence
```bash
# 1. Starta PostgreSQL med volume
docker run -d --name pg \\
    -e POSTGRES_PASSWORD=test \\
    -v pg_test:/var/lib/postgresql/data \\
    postgres:15

# 2. Skapa databas
docker exec -it pg psql -U postgres -c "CREATE DATABASE testdb;"

# 3. Stoppa och ta bort container
docker stop pg && docker rm pg

# 4. Starta ny container med samma volume
docker run -d --name pg2 \\
    -e POSTGRES_PASSWORD=test \\
    -v pg_test:/var/lib/postgresql/data \\
    postgres:15

# 5. Verifiera att databasen finns kvar
docker exec -it pg2 psql -U postgres -c "\\l"

# 6. Städa
docker stop pg2 && docker rm pg2
docker volume rm pg_test
```

---

**Nästa steg:** Node 5 - Docker Networking
''',
}


NODES = [
    NODE_01_DOCKER_INTRO,
    NODE_02_DOCKER_IMAGES,
    NODE_03_DOCKER_CONTAINERS,
    NODE_04_DOCKER_VOLUMES,
]
