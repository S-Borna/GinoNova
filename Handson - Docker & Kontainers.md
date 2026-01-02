# Docker & Containers - Hands-On Guide

## Från installation till första container på 30 minuter

---

## 📋 Innehållsförteckning

1. [Varför Docker?](#varför-docker)
2. [Installation - Ubuntu](#installation---ubuntu)
3. [Installation - Fedora](#installation---fedora)
4. [Fix: Docker utan sudo](#fix-docker-utan-sudo)
5. [Grundläggande Kommandon](#grundläggande-kommandon)
6. [Praktiska Exempel](#praktiska-exempel)
7. [Felsökning](#felsökning)
8. [Cheat Sheet](#cheat-sheet)

---

## 🎯 Varför Docker?

### Container vs VM

**Virtual Machine (VM):**

```
┌─────────────────────┐
│  Applikation        │
│  Python 3.12        │
│  Bibliotek          │
├─────────────────────┤
│  Guest OS (Ubuntu)  │  ← Flera GB
│  Kernel             │
├─────────────────────┤
│  Hypervisor         │
├─────────────────────┤
│  Host OS            │
└─────────────────────┘
```

**Container:**

```
┌─────────────────────┐
│  Applikation        │
│  Python 3.12        │
│  Bibliotek          │  ← 25 KB - 80 MB
├─────────────────────┤
│  Host OS Kernel     │  ← Delad!
└─────────────────────┘
```

### Konkret Exempel från Lektionen

**Python Hello World:**

- VM: Flera GB (helt OS)
- Container: 25 KB

**Python 3.14 Alpine:**

- VM: Flera GB
- Container: 73 MB

### Varför Containers Vinner

✅ **Versionshantering:**

- Kör 5 olika Python-versioner samtidigt
- Ingen konflikt med OS:ets version
- Inga panikuppdateringar när OS uppdaterar

✅ **Effektivitet:**

- Delar kernel med host
- Bara det du behöver, inget mer
- Snabb start (sekunder vs minuter)

✅ **Isolation:**

- Varje app i sin egen miljö
- Dependencies krockar inte
- Enklare säkerhet

---

## 🔧 Installation - Ubuntu

### Steg 1: Rensa Gamla Versioner

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

**Om du får:** "No packages found" → Perfekt! Fortsätt.

### Steg 2: Sätt upp Docker's Repository

**Varför?** Docker's egna repos är mer up-to-date än Ubuntu's.

```bash
# Update och installera dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl

# Skapa directory för GPG-nycklar
sudo install -m 0755 -d /etc/apt/keyrings

# Ladda ner Docker's GPG-nyckel (verifierar paket är äkta)
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Lägg till Docker's repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Uppdatera mot nya repository
sudo apt-get update
```

### Steg 3: Installera Docker

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

**Vad installeras?**

- `docker-ce` - Docker Engine
- `docker-ce-cli` - Kommandoradsverktyg
- `containerd.io` - Container runtime
- `docker-buildx-plugin` - Bygga images
- `docker-compose-plugin` - Multi-container appar

### Steg 4: Verifiera Installation

```bash
# Kolla att docker finns
which docker
# Output: /usr/bin/docker

# Kolla Docker-servicen
systemctl status docker.service
```

**Du ska se:**

- ● docker.service - Docker Application Container Engine
- Active: **active (running)**
- Enabled: **enabled**

**Om servicen inte är igång:**

```bash
sudo systemctl start docker.service
sudo systemctl enable docker.service
```

### Steg 5: Testa

```bash
sudo docker run hello-world
```

**Du ska se:**

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## 🔧 Installation - Fedora

### Samma Koncept, Andra Kommandon

**Dokumentation:** <https://docs.docker.com/engine/install/fedora/>

```bash
# 1. Ta bort gamla versioner
sudo dnf remove docker docker-client docker-client-latest \
  docker-common docker-latest docker-latest-logrotate \
  docker-logrotate docker-selinux docker-engine-selinux docker-engine

# 2. Sätt upp repository
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo \
  https://download.docker.com/linux/fedora/docker-ce.repo

# 3. Installera Docker
sudo dnf install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin

# 4. Starta Docker
sudo systemctl start docker
sudo systemctl enable docker

# 5. Testa
sudo docker run hello-world
```

---

## ⚡ Fix: Docker utan sudo

### Problemet

```bash
docker run hello-world
# permission denied while trying to connect to the Docker daemon socket
```

### Varför?

Docker lyssnar på en **Unix socket** (`/var/run/docker.sock`).
Bara `root` och medlemmar i gruppen `docker` får koppla till den.

### Lösningen

```bash
# Se alla grupper du är med i
id

# Lägg till dig själv i docker-gruppen
sudo usermod -aG docker $USER

# ALTERNATIVT (samma sak):
sudo gpasswd -a $USER docker

# Logga ut och in igen
exit
# (SSH in igen)

# Verifiera att docker-gruppen finns
id
# Du ska se "docker" i listan

# Testa utan sudo
docker run hello-world
# Success! 🎉
```

**VIKTIGT:** Du MÅSTE logga ut och in igen för att ändringen ska gälla!

---

## 🚀 Grundläggande Kommandon

### docker run - Starta Container

**Syntax:**

```bash
docker run [OPTIONS] IMAGE[:TAG] [COMMAND]
```

**Grundläggande:**

```bash
# Kör hello-world
docker run hello-world

# Kör med specifik tag/version
docker run python:3.14-alpine

# Kör med namn
docker run --name my-container python:3.14-alpine
```

**Vanliga Flaggor:**

| Flagga | Betydelse | Användning |
|--------|-----------|------------|
| `-i` | Interactive | Håll stdin öppen |
| `-t` | TTY | Allokera pseudo-terminal |
| `-it` | Kombinerat | Interaktiv session (båda ovan) |
| `--rm` | Remove | Ta bort container vid exit |
| `--name` | Namnge | Ge containern ett namn |
| `-d` | Detached | Kör i bakgrunden |

**Exempel:**

```bash
# Interaktiv Python-shell (stanna i containern)
docker run -it python:3.14-alpine

# Interaktiv, ta bort när klar
docker run -it --rm python:3.14-alpine

# Bakgrund med namn
docker run -d --name my-app nginx
```

### docker ps - Lista Containers

```bash
# Visa körande containers
docker ps

# Visa ALLA (även stoppade)
docker ps -a
```

**Output:**

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    NAMES
abc123def456   python    "python"  2 min ago Up 2 min  eager_tesla
```

### docker images - Lista Images

```bash
# Visa nedladdade images
docker images
# ELLER
docker image ls
```

**Output:**

```
REPOSITORY   TAG      IMAGE ID      CREATED      SIZE
python       3.14     abc123def     2 days ago   73MB
hello-world  latest   def456abc     3 weeks ago  25KB
```

### docker rm - Ta Bort Container

```bash
# Ta bort en stoppad container (med namn)
docker rm blissful_bell

# Ta bort med container ID
docker rm abc123def456

# Ta bort alla stoppade containers
docker container prune
```

### docker rmi - Ta Bort Image

```bash
# Ta bort en image
docker rmi python:3.12-alpine

# Ta bort alla oanvända images
docker image prune
```

### docker stop/start/restart

```bash
# Stoppa en körande container
docker stop my-container

# Starta en stoppad container
docker start my-container

# Starta om
docker restart my-container
```

---

## 💡 Praktiska Exempel

### Exempel 1: Testa Olika Python-Versioner

**Problem:** Du har Python 3.12 på din maskin, men behöver testa kod i 3.9, 3.10, 3.13, 3.14.

**Lösning med Docker:**

```bash
# Python 3.9
docker run -it --rm python:3.9-alpine
# Python 3.9.25

# Python 3.10
docker run -it --rm python:3.10-alpine
# Python 3.10.x

# Python 3.13
docker run -it --rm python:3.13-alpine
# Python 3.13.x

# Python 3.14 (senaste)
docker run -it --rm python:3.14-alpine
# Python 3.14.1
```

**Utan Docker:**

- Installera flera Python-versioner manuellt
- Hantera PATH
- Potentiella konflikter
- Röra med OS:ets Python = Farligt!

**Med Docker:**

- En rad kod
- Noll konflikter
- Noll påverkan på host

### Exempel 2: Image Tags

**Koncept:** Ett image kan ha flera **tags** (versioner).

**Format:** `image:tag`

```bash
# Utan tag = latest (default)
docker run python
# = docker run python:latest

# Med specifik tag
docker run python:3.14-alpine
docker run python:3.13
docker run python:3.12-slim
```

**Vanliga Tag-typer:**

| Tag | Betydelse |
|-----|-----------|
| `latest` | Senaste versionen (default) |
| `3.14` | Specifik version |
| `3.14-alpine` | Version + Alpine Linux (mindre) |
| `3.14-slim` | Version + minimal Debian |
| `3.14.1` | Exakt patch-version |

**Best Practice:** Använd **specifika tags** i produktion!

```bash
# ❌ Dåligt (kan ändras)
docker run python:latest

# ✅ Bra (förutsägbart)
docker run python:3.14.1-alpine
```

### Exempel 3: Container Lifecycle

```bash
# 1. Starta en container MED namn
docker run -it --name test-python python:3.14-alpine

# (Inne i containern, kör Python-kod)
>>> print("Hello Docker!")
>>> exit()

# 2. Container stoppades när du exitade
docker ps
# Tom lista

docker ps -a
# test-python   Exited (0) 2 seconds ago

# 3. Starta om samma container
docker start -i test-python
# (Inne igen!)

# 4. Stoppa från host (annat terminal)
docker stop test-python

# 5. Ta bort
docker rm test-python
```

### Exempel 4: Auto-Remove

**Problem:** Du vill bara testa något snabbt, vill inte städa efter dig.

**Lösning:**

```bash
# MED --rm flaggan
docker run -it --rm --name temp-test python:3.14-alpine

# (Inne i containern)
>>> print("Temporär container!")
>>> exit()

# Container är AUTOMATISKT BORTA
docker ps -a
# Ingen "temp-test"!
```

---

## 🔍 Felsökning

### Problem 1: Kan inte nå Internet från Container

**Symptom:**

```bash
docker run -it ubuntu
apt-get update
# Err: Could not resolve archive.ubuntu.com
```

**Diagnos:**

```bash
# 1. Kolla network interfaces
ip addr

# 2. Kolla routes
ip route

# 3. Testa internet från host
ping google.com
```

**Lösning (från lektionen):**

NAT-interface har ingen IP-adress → DHCP inte startad.

```bash
# Starta DHCP på NAT-interface
sudo dhclient enp0s8
# (byt enp0s8 mot ditt NAT-interface namn)

# Verifiera
ip addr
# Ser du IP på NAT-interface?

ip route
# Ser du default via NAT?

# Testa
ping 8.8.8.8
ping google.com
```

### Problem 2: DNS fungerar inte

**Symptom:**

```bash
docker run hello-world
# Error: Could not resolve docker registry
```

**Lösning:**

```bash
# Ändra DNS i resolv.conf
sudo nano /etc/resolv.conf

# Lägg till:
nameserver 8.8.8.8
nameserver 1.1.1.1
```

### Problem 3: "Unit docker.service could not be found"

**På Fedora:**

**Fel:**

```bash
systemctl status docker.services
# Unit docker.services could not be found
```

**Rätt:**

```bash
systemctl status docker.service
# (Notera: .service INTE .services)
```

### Problem 4: Permission Denied (igen och igen)

**Lösning:**

```bash
# Dubbelkolla att du är i docker-gruppen
id | grep docker

# Om inte:
sudo usermod -aG docker $USER

# Logga ut och in HELT
exit
# SSH in igen

# Testa
docker run hello-world
```

---

## 📋 Cheat Sheet

### Installation

```bash
# Ubuntu - One-liner (efter dependencies)
sudo apt-get install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin

# Fedora - One-liner
sudo dnf install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

### Användarrättigheter

```bash
# Lägg till dig själv i docker-gruppen
sudo usermod -aG docker $USER
# Logga ut och in igen!
```

### Grundläggande Kommandon

```bash
# Kör container
docker run [OPTIONS] IMAGE[:TAG]

# Interaktiv
docker run -it IMAGE

# Interaktiv + auto-remove
docker run -it --rm IMAGE

# Med namn
docker run --name NAMN IMAGE

# Lista körande
docker ps

# Lista alla
docker ps -a

# Lista images
docker images

# Stoppa container
docker stop NAMN/ID

# Starta container
docker start NAMN/ID

# Ta bort container
docker rm NAMN/ID

# Ta bort alla stoppade
docker container prune

# Ta bort image
docker rmi IMAGE:TAG
```

### Vanliga Images

```bash
# Hello World (test)
docker run hello-world

# Python (olika versioner)
docker run -it --rm python:3.14-alpine
docker run -it --rm python:3.13
docker run -it --rm python:3.9

# Ubuntu (för testing)
docker run -it --rm ubuntu

# Nginx (web server)
docker run -d -p 80:80 nginx
```

### Flaggor - Snabbguide

```bash
-i          # Interactive (håll stdin öppen)
-t          # TTY (terminal)
-it         # Kombinerat (interaktiv session)
--rm        # Ta bort vid exit
--name      # Ge namn
-d          # Detached (bakgrund)
-p 80:80    # Port mapping (host:container)
-v /path    # Volume (persistent data)
```

---

## 🎯 Viktiga Koncept

### Images vs Containers

**Image:**

- Mall/blueprint
- Läses från disk
- Kan användas om och om igen
- Tar diskutrymme

**Container:**

- Körande instans av image
- Kan ha många containers från samma image
- Tar MINIMAL extra diskutrymme (bara ändringar)
- Tar RAM när den kör

**Analogi:**

- Image = Klass
- Container = Objekt/instans

### Layers & Storage

**Varför 8 images tar bara ~300 MB?**

Images delar **layers**:

```
python:3.14-alpine    73 MB
  ├─ Alpine base      5 MB   ← Delad
  ├─ Python deps      50 MB  ← Delad
  └─ Python 3.14      18 MB

python:3.13-alpine    70 MB
  ├─ Alpine base      5 MB   ← SAMMA! Ingen extra diskplats
  ├─ Python deps      50 MB  ← SAMMA!
  └─ Python 3.13      15 MB  ← Bara DENNA är ny
```

**Resultat:**

- Första imagen: 73 MB
- Andra imagen: +15 MB (inte +70 MB!)

### Container Disk Usage

När du kör `docker container prune`:

```
Total reclaimed space: 8 MB
```

**Varför så lite?**

- Containers **delar** image-data
- Bara **ändringar** sparas per container
- En stoppad container = några MB av diff

---

## 🚀 Nästa Steg

### Måndagens Lektion (Fördjupning)

Vi kommer lära oss:

- Port mapping (exponera services)
- Volumes (persistent data)
- Networks (containers som pratar)
- Docker Compose (multi-container apps)
- Bygga egna images

### Förberedelser

**Gör klart till måndag:**

1. ✅ Docker installerat på **minst 1 VM** (helst båda)
2. ✅ Kan köra `docker run` utan sudo
3. ✅ Testat basic commands
4. ✅ (Frivilligt) Installera Docker Desktop på Mac/PC

### Övningar

**Testa själv:**

```bash
# 1. Kör olika Python-versioner
docker run -it --rm python:3.9-alpine
docker run -it --rm python:3.14-alpine

# 2. Kör Ubuntu och installera något
docker run -it --rm ubuntu
# apt-get update && apt-get install curl

# 3. Kolla disk usage
docker images
docker ps -a

# 4. Städa
docker container prune
docker image prune
```

---

### Nyckelpunkter

**Containers är:**

- Lightweight (KB till MB, inte GB)
- Isolerade (egen miljö per app)
- Portabla (samma överallt)
- Versionshanterbara (specifika tags)

**Docker är:**

- Framtiden för deployment
- Standard i DevOps
- Grunden för Kubernetes
- Viktigt för er LIA

### Långsiktig Plan

1. **Linux-kursen (nu):** Docker basics
2. **DevOps-kursen:** Kubernetes + CI/CD
3. **Fördjupning:** Drifta Kubernetes
4. **LIA:** Använd från dag 1!

---

*"Containers are like Lego blocks - små, modulära, och går att kombinera hur som helst!"*
