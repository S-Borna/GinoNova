"""
NOD 3.1: Docker Installation & Grunder
======================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 3: DEVOPS
FÖRSTA NODEN I MODUL 3!
"""

DOCKER_GRUNDER_NODE = {
    "title": "Docker - Installation & Grunder",
    "slug": "docker-installation-grunder",
    "description": "Containerplattformen Docker - vad det är, installation och grundläggande kommandon.",
    "difficulty": "medium",
    "estimated_minutes": 55,
    "xp_reward": 140,
    "order_index": 1,
    "content": r"""# Docker - Installation & Grunder

> **TL;DR:** Containers delar kernel med host = lätta och snabba. `docker run -d nginx` startar i bakgrunden, `docker ps` visar körande containers.

---

## 📖 TEORI: Vad är Docker?

**Docker** = Containerplattform
- Kör applikationer **isolerat**
- **Delar kernel** med host-systemet
- Mycket lättare än virtuella maskiner

### Nyckelprincipen

```
┌────────────────────────────────────────────────────┐
│              Containers delar kernel               │
│    = Lätta (MB) istället för tunga (GB)           │
│    = Snabba (sekunder) istället för långsamma     │
└────────────────────────────────────────────────────┘
```

### Container vs Virtual Machine

| Aspekt | Virtual Machine | Container |
|--------|-----------------|-----------|
| Storlek | GB (eget OS) | MB (bara app) |
| Starttid | Minuter | Sekunder |
| Resursanvändning | Tung | Lätt |
| Isolering | Full (eget OS) | Process-nivå |
| Underliggande | Hypervisor | Docker Engine |
| Kernel | Egen | Delar med host |

### Varför är det viktigt?

> "Hello World-imagen är **25 KB**. Python Alpine är **23 MB**. Ett helt VM är **flera GB** bara för OS:et!"

### Docker-arkitektur

```
┌─────────────────┐
│  Docker Client  │  ← CLI (docker run, docker ps...)
│    (CLI)        │
└────────┬────────┘
         │ Unix Socket
         ▼
┌─────────────────┐
│  Docker Daemon  │  ← Hanterar containers & images
│   (dockerd)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Docker Registry │  ← Docker Hub (lagrar images)
│   (Hub)         │
└─────────────────┘
```

**Komponenter:**
- **Docker Client** - CLI-verktyget du använder
- **Docker Daemon** - Bakgrundsprocessen som gör jobbet
- **Docker Registry** - Docker Hub, där images lagras

---

## 📖 Installation på Ubuntu

### Steg 1: Ta bort gamla versioner

```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

### Steg 2: Installera dependencies

```bash
sudo apt update
sudo apt install ca-certificates curl
```

### Steg 3: Lägg till Dockers GPG-nyckel

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Steg 4: Lägg till repository

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Steg 5: Installera Docker

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin
```

### Steg 6: Verifiera

```bash
sudo docker run hello-world
```

---

## 📖 Köra Docker utan sudo

### Varför krävs sudo?

> "Docker lyssnar på en **Unix socket**. Alla i docker-gruppen har access till den socketen."

### Lösningen

```bash
# Lägg till din användare i docker-gruppen
sudo usermod -aG docker $USER

# Logga ut och in igen, ELLER:
newgrp docker

# Verifiera att det fungerar
docker run hello-world
```

⚠️ **OBS:** Medlemskap i docker-gruppen ger root-liknande rättigheter!

---

## 📖 Grundläggande kommandon

### docker run - Kör container

```bash
# Kör och avsluta
docker run hello-world

# Interaktiv terminal (-it)
docker run -it ubuntu bash

# Detached/bakgrund (-d)
docker run -d nginx

# Ta bort efter körning (--rm)
docker run --rm alpine echo "hej"

# Ge containern ett namn
docker run --name minapp nginx

# Kombinera flaggor
docker run -d --name web --rm nginx
```

### Viktiga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| -d | Detached (bakgrund) | docker run -d nginx |
| -it | Interactive + TTY | docker run -it ubuntu bash |
| --rm | Ta bort efter avslut | docker run --rm alpine |
| --name | Ge namn | docker run --name web nginx |
| -p | Port-mapping | docker run -p 8080:80 nginx |
| -v | Volume-mount | docker run -v ./data:/data nginx |
| -e | Environment variable | docker run -e DEBUG=1 myapp |

### docker ps - Visa containers

```bash
# Visa körande containers
docker ps

# Visa ALLA (även stoppade)
docker ps -a

# Visa bara container-IDs
docker ps -q

# Visa senaste containern
docker ps -l
```

### Hantera containers

```bash
# Stoppa container
docker stop container_id
docker stop minapp          # Med namn

# Starta stoppad container
docker start container_id

# Starta om
docker restart container_id

# Ta bort stoppad container
docker rm container_id

# Tvinga bort (även körande)
docker rm -f container_id

# Ta bort alla stoppade
docker container prune
```

### Städa upp

```bash
# Ta bort alla stoppade containers
docker container prune

# Ta bort allt oanvänt (containers, networks, images)
docker system prune

# Ta bort ALLT oanvänt inkl alla images
docker system prune -a

# Visa diskutrymme
docker system df
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Interaktiv Python

```bash
# Kör Python interaktivt
docker run -it --rm python:3.12-alpine

# Nu är du i Python-shell!
>>> print("Hello from container!")
>>> import sys
>>> sys.version
>>> exit()

# Container försvinner automatiskt (--rm)
```

### Exempel 2: Flera Python-versioner parallellt

```bash
# Kör olika versioner samtidigt - inga konflikter!
docker run -d --name py310 python:3.10-alpine sleep infinity
docker run -d --name py312 python:3.12-alpine sleep infinity
docker run -d --name py313 python:3.13-alpine sleep infinity

# Alla kör parallellt!
docker ps

# Kör kommando i specifik version
docker exec py310 python --version  # Python 3.10.x
docker exec py312 python --version  # Python 3.12.x
docker exec py313 python --version  # Python 3.13.x

# Städa upp
docker rm -f py310 py312 py313
```

### Exempel 3: Webserver med port-mapping

```bash
# Starta nginx på port 8080
docker run -d --name web -p 8080:80 nginx

# Testa
curl localhost:8080

# Visa loggar
docker logs web

# Stoppa och ta bort
docker rm -f web
```

### Exempel 4: Komplett arbetsflöde

```bash
#!/usr/bin/env bash

# 1. Kör container i bakgrunden
docker run -d --name myapp nginx

# 2. Kolla att den kör
docker ps | grep myapp

# 3. Visa loggar
docker logs myapp

# 4. Kör kommando i containern
docker exec myapp cat /etc/nginx/nginx.conf

# 5. Stoppa
docker stop myapp

# 6. Starta igen
docker start myapp

# 7. Ta bort permanent
docker rm -f myapp
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Vad delar containers med host? | Kernel |
| 2 | docker run -d gör? | Kör i bakgrunden (detached) |
| 3 | docker run -it gör? | Interaktiv terminal |
| 4 | docker run --rm gör? | Tar bort containern efter avslut |
| 5 | docker ps visar? | Körande containers |
| 6 | docker ps -a visar? | ALLA containers (även stoppade) |
| 7 | docker rm -f gör? | Tvingar bort även körande container |
| 8 | Hur kör man Docker utan sudo? | usermod -aG docker $USER |
| 9 | docker container prune gör? | Tar bort alla stoppade containers |
| 10 | Container vs VM storlek? | MB vs GB |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad delar containers med host-systemet?**
- A) Hela operativsystemet
- B) Kernel ✅
- C) Ingenting
- D) Bara filsystemet

**2. Vilken flagga kör container i bakgrunden?**
- A) -b
- B) -d ✅
- C) --background
- D) -r

**3. Vad gör docker run --rm?**
- A) Tar bort image efter körning
- B) Startar om automatiskt
- C) Tar bort container efter avslut ✅
- D) Kör som root

**4. Hur visar du ALLA containers (även stoppade)?**
- A) docker ps --all
- B) docker ps -a ✅
- C) docker list
- D) docker containers

**5. Vad gör docker exec?**
- A) Kör ny container
- B) Kör kommando i körande container ✅
- C) Stoppar container
- D) Bygger image

**6. Hur lägger du användare i docker-gruppen?**
- A) docker adduser
- B) groupadd docker $USER
- C) usermod -aG docker $USER ✅
- D) chmod docker $USER

**7. Vilken flagga ger interaktiv terminal?**
- A) -t
- B) -i
- C) -it ✅
- D) --terminal

**8. Container vs VM - vilken startar snabbast?**
- A) VM (har eget OS)
- B) Container (delar kernel) ✅
- C) Samma hastighet
- D) Beror på image

**9. Vad gör docker system prune -a?**
- A) Bara stoppade containers
- B) Allt oanvänt inkl images ✅
- C) Bara images
- D) Bara volymer

**10. Varför krävs docker-gruppen för att köra utan sudo?**
- A) Docker kräver root
- B) Gruppen har access till Docker socket ✅
- C) Det är en bugg
- D) Det krävs inte

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Första containern
```bash
# 1. Kör hello-world
docker run hello-world

# 2. Vad hände? (imagen laddades ner och kördes)
docker ps -a | head -2

# 3. Ta bort
docker container prune -f
```

### Övning 2: Interaktivt arbete
```bash
# 1. Starta Ubuntu interaktivt
docker run -it --rm ubuntu bash

# 2. Inuti containern:
cat /etc/os-release
whoami
pwd
exit

# 3. Container försvann (--rm)
docker ps -a | grep ubuntu
```

### Övning 3: Bakgrundsprocesser
```bash
# 1. Starta nginx i bakgrunden
docker run -d --name web -p 8080:80 nginx

# 2. Verifiera
docker ps
curl localhost:8080

# 3. Visa loggar
docker logs web

# 4. Gå in i containern
docker exec -it web bash
ls /usr/share/nginx/html/
exit

# 5. Städa upp
docker rm -f web
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| Glömma -d | Terminal blockeras | Lägg till -d för bakgrund |
| Glömma --rm | Stoppade containers samlas | Använd --rm eller prune |
| Glömma newgrp docker | Måste logga ut/in | newgrp docker |
| Port redan upptagen | Container startar inte | Använd annan port (-p 8081:80) |

---

## 📝 SAMMANFATTNING

```bash
# KÄRNAN: Containers delar kernel = lätta och snabba!

# KÖR CONTAINER
docker run hello-world           # Kör och avsluta
docker run -d nginx              # Bakgrund
docker run -it ubuntu bash       # Interaktiv
docker run --rm alpine echo hi   # Ta bort efter
docker run --name web nginx      # Med namn
docker run -p 8080:80 nginx      # Port-mapping

# HANTERA
docker ps                        # Visa körande
docker ps -a                     # Visa alla
docker stop container            # Stoppa
docker start container           # Starta
docker rm container              # Ta bort
docker rm -f container           # Tvinga bort

# INTERAGERA
docker exec -it container bash   # Gå in
docker logs container            # Visa loggar
docker logs -f container         # Följ loggar

# STÄDA
docker container prune           # Stoppade containers
docker system prune              # Allt oanvänt
docker system prune -a           # Allt inkl images

# UTAN SUDO
sudo usermod -aG docker $USER
newgrp docker

# FLAGGOR
# -d = detached (bakgrund)
# -it = interactive terminal
# --rm = ta bort efter avslut
# --name = ge namn
# -p = port (host:container)
# -e = environment variable
```

"""
}

