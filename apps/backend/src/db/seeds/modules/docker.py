"""
Docker Mastery Module
=====================

20 noder med svensk pedagogisk stil.
Komplett Docker-kunskap - från grunderna till produktion.

Track: containers
Difficulty: intermediate
Estimated Hours: 25
"""

MODULE = {
    "name": "Docker Mastery",
    "slug": "docker-mastery",
    "description": "Komplett Docker-kunskap - från containers till produktion med naturlig svensk pedagogik",
    "track_slug": "containers",
    "order_index": 18,
    "difficulty": "intermediate",
    "estimated_hours": 25,
    "prerequisites": ["linux-mastery"],
    "icon": "🐳",
    "color": "#2496ED",
    "tasks": [
        {
            "title": "Docker Fundamentals & Architecture",
            "slug": "docker-fundamentals-architecture",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Fundamentals & Architecture

------------------------------------------------------------

## Introduktion

Föreställ dig att du precis har byggt en fantastisk webbapplikation på din dator. Den fungerar perfekt - alla tester passar, databasen kopplar ihop fint, och allt ser bra ut. Så skickar du koden till din kollega, och plötsligt: "Det fungerar inte på min maskin." Kanske har de en annan version av Node.js, kanske saknas det några bibliotek, eller så är deras operativsystem konfigurerat annorlunda.

Det här är problemet som Docker löser. Tänk på Docker som en **standardiserad fraktcontainer för mjukvara**. Precis som fraktcontainrar revolutionerade global handel genom att standardisera hur gods transporteras - oavsett om det är på båt, tåg eller lastbil - revolutionerar Docker hur mjukvara paketeras och levereras.

Som DevOps-ingenjör kommer du använda Docker dagligen. Du kommer bygga images i CI/CD-pipelines, felsöka containers i produktion, och optimera deployments för skalning. Utan en solid förståelse för hur Docker faktiskt fungerar under huven, kommer du stå handfallen när något går fel.

I den här noden bygger du en djup förståelse för Dockers arkitektur - från de Linux-primitiver som möjliggör isolering till hur Docker Engine koordinerar allt. Efter det här kommer du inte bara *använda* Docker, du kommer *förstå* det.

------------------------------------------------------------

## Teori

### Vad är containerisering?

Containerisering är en metod för att paketera en applikation tillsammans med alla dess beroenden i en isolerad enhet som kan köras var som helst. Tänk på det som en "virtuell miljö" för din applikation, men mycket lättare än en virtuell maskin.

```
+---------------------------------------------------------------+
|                 CONTAINERISERING KONCEPTET                    |
+---------------------------------------------------------------+
|                                                               |
|   Traditionell deployment:          Container deployment:     |
|   ----------------------           ----------------------     |
|   - App på Server 1                 - App + deps i container  |
|   - Manuell installation           - Standardformat          |
|   - "Works on my machine"          - Körs identiskt överallt |
|   - Svårt att replikera            - Enkelt att skala        |
|                                                               |
+---------------------------------------------------------------+
```

### Docker vs Virtuella Maskiner

Många blandar ihop containers med virtuella maskiner, men det är fundamentalt olika tekniker:

```
+---------------------------------------------------------------+
|              VIRTUELLA MASKINER (VMs)                         |
+---------------------------------------------------------------+
|  +-----------+ +-----------+ +-----------+                   |
|  |   App A   | |   App B   | |   App C   |                   |
|  +-----------+ +-----------+ +-----------+                   |
|  | Guest OS  | | Guest OS  | | Guest OS  |  <- Varje VM har  |
|  | (5-10 GB) | | (5-10 GB) | | (5-10 GB) |     eget OS!      |
|  +-----------+ +-----------+ +-----------+                   |
|  +-------------------------------------------------------+   |
|  |              Hypervisor (VMware, KVM)                 |   |
|  +-------------------------------------------------------+   |
|  +-------------------------------------------------------+   |
|  |                     Host OS                           |   |
|  +-------------------------------------------------------+   |
+---------------------------------------------------------------+

+---------------------------------------------------------------+
|                      CONTAINERS                               |
+---------------------------------------------------------------+
|  +-----------+ +-----------+ +-----------+                   |
|  |   App A   | |   App B   | |   App C   |                   |
|  |  (50 MB)  | | (100 MB)  | |  (30 MB)  |  <- Bara appen!   |
|  +-----------+ +-----------+ +-----------+                   |
|  +-------------------------------------------------------+   |
|  |           Docker Engine (Container Runtime)           |   |
|  +-------------------------------------------------------+   |
|  +-------------------------------------------------------+   |
|  |              Host OS (delad kernel)                   |   |
|  +-------------------------------------------------------+   |
+---------------------------------------------------------------+
```

| Egenskap | Virtual Machine | Container |
|----------|-----------------|-----------|
| **Storlek** | 5-10 GB+ | 50-500 MB |
| **Starttid** | Minuter | Sekunder |
| **Isolation** | Fullständig (egen kernel) | Process-nivå (delad kernel) |
| **Resursanvändning** | Hög (kör helt OS) | Låg (bara appen) |
| **Portabilitet** | Begränsad | Hög |

### Docker Engine Arkitektur

Docker Engine består av tre huvudkomponenter som samverkar:

```
+---------------------------------------------------------------+
|                      DIN TERMINAL                             |
|                    $ docker run nginx                         |
+-----------------------------+---------------------------------+
                              |
                              v
+---------------------------------------------------------------+
|                     DOCKER CLIENT                             |
|                     (docker CLI)                              |
|         Tar dina kommandon och skickar till daemon            |
+-----------------------------+---------------------------------+
                              | REST API (unix socket)
                              v
+---------------------------------------------------------------+
|                     DOCKER DAEMON                             |
|                      (dockerd)                                |
+-----------+-----------+-----------+---------------------------+
|  Images   | Containers| Networks  | Volumes                   |
+-----------+-----------+-----------+---------------------------+
                              |
                              v
+---------------------------------------------------------------+
|                   CONTAINER RUNTIME                           |
|              (containerd -> runc -> container)                |
+---------------------------------------------------------------+
```

**Docker Client (CLI):** Det du interagerar med när du skriver `docker`-kommandon. Den skickar API-anrop till daemon.

**Docker Daemon (dockerd):** Bakgrundsprocessen som gör det tunga jobbet - bygger images, startar containers, hanterar nätverk.

**Container Runtime (containerd + runc):** De lågre komponenter som faktiskt skapar och kör containers på kernel-nivå.

### Linux-primitiver: Namespaces och Cgroups

Docker är inte magi - det bygger på Linux kernel-funktioner som funnits i över 10 år:

**Namespaces** ger isolation genom att skapa separata vyer av systemresurser:

| Namespace | Isolerar | Exempel |
|-----------|----------|---------|
| **PID** | Process-IDs | Container ser bara sina egna processer |
| **NET** | Nätverk | Container har eget nätverksgränssnitt |
| **MNT** | Filsystem | Container har egen filsystemvy |
| **UTS** | Hostname | Container har eget hostname |
| **IPC** | Inter-process comm | Isolerad IPC |
| **USER** | Användare | UID mapping |

**Cgroups (Control Groups)** begränsar resursanvändning:

```bash
# Exempel: Begränsar en container till 512MB minne och 50% CPU
docker run --memory=512m --cpus=0.5 nginx
```

### Union Filesystem och Layers

Docker images är uppbyggda av **lager (layers)** som staplas på varandra:

```
+---------------------------------------------------------------+
|                   DOCKER IMAGE LAYERS                         |
+---------------------------------------------------------------+
|                                                               |
|   +-----------------------------------------------------+    |
|   | Layer 5: COPY app.py /app  (din kod, 50 KB)        |    |
|   +-----------------------------------------------------+    |
|   | Layer 4: RUN pip install flask  (2 MB)              |    |
|   +-----------------------------------------------------+    |
|   | Layer 3: RUN apt-get install python3  (50 MB)       |    |
|   +-----------------------------------------------------+    |
|   | Layer 2: RUN apt-get update  (20 MB)                |    |
|   +-----------------------------------------------------+    |
|   | Layer 1: FROM ubuntu:22.04 (base image, 77 MB)      |    |
|   +-----------------------------------------------------+    |
|                                                               |
|   Varje layer är READ-ONLY och cachas separat!               |
|   Ändrar du Layer 5 behöver bara det lagret byggas om.       |
|                                                               |
+---------------------------------------------------------------+
```

### OCI-standarden

Open Container Initiative (OCI) är en öppen standard som definierar:
- **Runtime Specification:** Hur containers ska köras
- **Image Specification:** Hur images ska paketeras

Detta gör att Docker-images kan köras av andra runtimes som Podman, containerd direkt, eller CRI-O.

### Docker Hub och Registries

Docker Hub är som "GitHub för containers" - ett centralt ställe för att lagra och dela images:

```
+---------------------------------------------------------------+
|                    IMAGE NAMING CONVENTION                    |
+---------------------------------------------------------------+
|                                                               |
|   [registry/][namespace/]repository:tag                       |
|                                                               |
|   Exempel:                                                    |
|   -------                                                     |
|   nginx                      -> docker.io/library/nginx:latest|
|   myuser/myapp:v1.0          -> docker.io/myuser/myapp:v1.0   |
|   gcr.io/project/image:tag   -> Google Container Registry     |
|   ghcr.io/user/image:tag     -> GitHub Container Registry     |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Installera Docker

**macOS:**
```bash
# Ladda ner Docker Desktop från docker.com
# Eller via Homebrew:
brew install --cask docker

# Starta Docker Desktop från Applications
# Vänta tills ikonen i menyraden visar "Docker Desktop is running"
```

**Ubuntu/Debian:**
```bash
# Ta bort gamla versioner om de finns
sudo apt-get remove docker docker-engine docker.io containerd runc

# Installera beroenden
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

# Lägg till Dockers officiella GPG-nyckel
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Lägg till Docker repository
echo \\
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \\
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \\
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Lägg till din användare i docker-gruppen (så du slipper sudo)
sudo usermod -aG docker $USER
# Logga ut och in igen för att gruppändringen ska ta effekt
```

### Steg 2: Verifiera installationen

```bash
# Kontrollera Docker-versionen
docker version
# Förväntad output:
# Client: Docker Engine - Community
#  Version:           24.0.x
#  ...
# Server: Docker Engine - Community
#  Version:           24.0.x
#  ...

# Visa detaljerad systeminformation
docker info
# Visar antal containers, images, storage driver, etc.

# Kör ett snabbt test
docker run hello-world
# Detta:
# 1. Laddar ner hello-world image från Docker Hub
# 2. Skapar en container från imagen
# 3. Kör containern som skriver ut ett meddelande
# 4. Containern avslutas
```

### Steg 3: Utforska grundläggande kommandon

```bash
# Lista alla körande containers
docker ps
# Output: Tom lista (inga containers körs)

# Lista ALLA containers (även stoppade)
docker ps -a
# Output: Visar hello-world containern som avslutats

# Lista alla images på systemet
docker images
# Output: Visar hello-world imagen

# Ladda ner en image utan att köra den
docker pull nginx
# Output: Visar nedladdning av lager

# Kör nginx i bakgrunden (-d = detached mode)
docker run -d --name min-nginx -p 8080:80 nginx
# -d: Kör i bakgrunden
# --name: Ge containern ett namn
# -p 8080:80: Mappa port 8080 på host till port 80 i container

# Öppna webbläsaren och gå till http://localhost:8080
# Du ska se nginx välkommen-sida!

# Stoppa containern
docker stop min-nginx

# Ta bort containern
docker rm min-nginx
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Sätta upp en utvecklingsmiljö

Du vill snabbt testa en Python-applikation utan att installera Python på din maskin:

```bash
# Starta en interaktiv Python-container
docker run -it --rm python:3.11 bash
# -it: Interaktivt läge med terminal
# --rm: Ta bort containern när den avslutas
# bash: Kör bash istället för Python REPL

# Nu är du inne i containern!
# Kontrollera Python-versionen
python --version
# Output: Python 3.11.x

# Testa lite Python
python -c "print('Hello from Docker!')"

# Skriv exit för att lämna containern
exit
# Containern tas bort automatiskt (--rm flaggan)
```

### Exempel 2: Köra en databas för lokal utveckling

```bash
# Starta PostgreSQL med persistent data
docker run -d \\
  --name dev-postgres \\
  -e POSTGRES_USER=devuser \\
  -e POSTGRES_PASSWORD=devpassword \\
  -e POSTGRES_DB=myapp \\
  -p 5432:5432 \\
  -v postgres-data:/var/lib/postgresql/data \\
  postgres:15

# Förklaring:
# -e: Sätter miljövariabler för konfiguration
# -v: Skapar en namngiven volym för att spara data mellan omstarter

# Anslut till databasen
docker exec -it dev-postgres psql -U devuser -d myapp
# Nu kan du köra SQL-kommandon!
# \\dt  - visa tabeller
# \\q   - avsluta
```

### Exempel 3: Inspektera vad som händer i en container

```bash
# Starta en nginx-container
docker run -d --name debug-nginx nginx

# Se vilka processer som körs i containern
docker top debug-nginx
# Output: Visar nginx master och worker processes

# Se resursanvändning i realtid
docker stats debug-nginx
# Output: CPU%, MEM USAGE, NET I/O, BLOCK I/O
# Tryck Ctrl+C för att avsluta

# Inspektera full konfiguration och metadata
docker inspect debug-nginx
# Output: JSON med allt - nätverk, volumes, miljövariabler, etc.

# Se loggarna
docker logs debug-nginx
# Lägg till -f för att följa loggar i realtid
docker logs -f debug-nginx
```

------------------------------------------------------------

## Bästa Praxis

1. **Använd alltid specifika taggar, aldrig `latest`**
   ```bash
   # Bra - explicit version
   docker pull nginx:1.25.3

   # Dåligt - oförutsägbart
   docker pull nginx:latest
   ```

2. **Ge containers meningsfulla namn**
   ```bash
   # Bra - beskrivande namn
   docker run -d --name api-server-prod myapp:v1.2

   # Dåligt - slumpmässigt genererat namn
   docker run -d myapp:v1.2
   ```

3. **Rensa regelbundet oanvända resurser**
   ```bash
   # Ta bort stoppade containers, oanvända nätverk och dangling images
   docker system prune

   # Mer aggressiv rensning (inklusive oanvända volumes)
   docker system prune -a --volumes
   ```

4. **Använd volumes för persistent data**
   ```bash
   # Bra - data överlever container-omstarter
   docker run -v mydata:/app/data myapp

   # Dåligt - data försvinner när containern tas bort
   docker run myapp
   ```

5. **Begränsa resurser i produktion**
   ```bash
   docker run --memory=512m --cpus=1.0 myapp
   ```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: "permission denied" när du kör docker

**Symptom:**
```
Got permission denied while trying to connect to the Docker daemon socket
```

**Orsak:** Din användare är inte med i docker-gruppen.

**Lösning:**
```bash
# Lägg till användaren i docker-gruppen
sudo usermod -aG docker $USER

# Logga ut och in igen, eller kör:
newgrp docker

# Verifiera att det fungerar
docker ps
```

### Problem 2: Container startar men avslutas direkt

**Symptom:** `docker ps` visar ingen container, men `docker ps -a` visar status "Exited".

**Orsak:** Huvudprocessen i containern avslutas omedelbart.

**Lösning:**
```bash
# Kontrollera vad som hände
docker logs <container-id>

# För debugging, kör interaktivt
docker run -it <image> bash
```

### Problem 3: Port already in use

**Symptom:**
```
Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:8080
```

**Lösning:**
```bash
# Hitta vad som använder porten
lsof -i :8080
# eller
sudo netstat -tlnp | grep 8080

# Använd en annan port
docker run -p 8081:80 nginx
```

### Problem 4: No space left on device

**Symptom:** Docker klagar på utrymmesbrist.

**Lösning:**
```bash
# Se vad som tar plats
docker system df

# Rensa oanvända resurser
docker system prune -a

# Om det fortfarande är fullt, kontrollera Docker Desktop-inställningar
# eller öka disk-allokeringen
```

------------------------------------------------------------

## Övningar

### Övning 1: Din första container (20 XP)

**Mål:** Installera Docker, verifiera installationen och kör dina första containers.

**Din uppgift:**
1. Installera Docker på ditt system (Docker Desktop eller Docker Engine)
2. Verifiera installationen med `docker version` och `docker info`
3. Kör `hello-world` containern
4. Kör en nginx-container på port 8080 och besök den i webbläsaren
5. Lista alla containers och images på systemet
6. Stoppa och ta bort nginx-containern

<details>
<summary>Ledtråd</summary>

- Docker Desktop är enklast på macOS/Windows
- På Linux, följ den officiella installationsguiden
- Använd `docker ps -a` för att se ALLA containers
- Glöm inte `-p` flaggan för port mapping

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Verifiera installation
docker version
docker info

# 2. Kör hello-world
docker run hello-world

# 3. Kör nginx på port 8080
docker run -d --name test-nginx -p 8080:80 nginx

# 4. Besök http://localhost:8080 i webbläsaren

# 5. Lista allt
docker ps        # Körande containers
docker ps -a     # Alla containers
docker images    # Alla images

# 6. Rensa
docker stop test-nginx
docker rm test-nginx
```

</details>

**Verifikation:** Du kan besöka http://localhost:8080 och se nginx välkommen-sida.

---

### Övning 2: Utforska container-arkitekturen (25 XP)

**Mål:** Förstå hur containers isoleras från värdsystemet.

**Scenario:** Du vill undersöka hur Docker använder Linux-primitiver för isolation.

**Din uppgift:**
1. Starta en Ubuntu-container i interaktivt läge
2. Inifrån containern, lista processer med `ps aux` - hur många ser du?
3. I ett annat terminalfönster (på host), kör `docker top <container>` - vad ser du?
4. Jämför hostname inuti containern vs på host
5. Använd `docker inspect` för att hitta containerns PID på host-systemet
6. Dokumentera skillnaderna du observerar

<details>
<summary>Ledtråd</summary>

- Starta containern med: `docker run -it --name test-ubuntu ubuntu bash`
- Inuti containern är PID-namespace isolerat - du ser bara containerns processer
- `docker inspect` returnerar JSON - leta efter "Pid" i "State"
- På Linux kan du använda `ls /proc/<pid>/ns/` för att se namespaces

</details>

<details>
<summary>Lösning</summary>

```bash
# Terminal 1: Starta containern
docker run -it --name test-ubuntu ubuntu bash

# Inuti containern:
ps aux
# Du ser bara 1-2 processer (bash och ps)

hostname
# Visar container-ID som hostname

# Terminal 2 (på host):
docker top test-ubuntu
# Visar containerns processer med HOST PIDs

docker inspect test-ubuntu --format='{{.State.Pid}}'
# Returnerar PID på host-systemet (t.ex. 12345)

# På Linux kan du inspektera namespaces:
sudo ls -la /proc/12345/ns/
# Visar alla namespaces (pid, net, mnt, etc.)

# När du är klar:
# I terminal 1: exit
docker rm test-ubuntu
```

</details>

**Verifikation:** Du kan förklara varför `ps aux` i containern visar färre processer än på host.

---

### Övning 3: Multi-container demonstration (30 XP)

**Mål:** Sätta upp en realistisk multi-container applikation och förstå isolering.

**Scenario:** Du ska demonstrera Docker för ditt team genom att köra en webbserver och databas som separata containers.

**Din uppgift:**
1. Skapa ett custom nätverk för dina containers
2. Starta en PostgreSQL-databas med miljövariabler och namngiven volym
3. Starta en nginx-container på samma nätverk
4. Verifiera att containers kan kommunicera via nätverket
5. Dokumentera resursanvändning för båda containers
6. Skapa ett enkelt diagram över arkitekturen

<details>
<summary>Ledtråd</summary>

- Skapa nätverk med: `docker network create`
- Använd `--network` flaggan när du startar containers
- Containers på samma nätverk kan nå varandra via namn
- Använd `docker stats` för resursanvändning
- `docker network inspect` visar vilka containers som är anslutna

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Skapa ett dedikerat nätverk
docker network create demo-network

# 2. Starta PostgreSQL
docker run -d \\
  --name demo-db \\
  --network demo-network \\
  -e POSTGRES_USER=admin \\
  -e POSTGRES_PASSWORD=secret \\
  -e POSTGRES_DB=demoapp \\
  -v demo-pgdata:/var/lib/postgresql/data \\
  postgres:15

# 3. Starta nginx
docker run -d \\
  --name demo-web \\
  --network demo-network \\
  -p 8080:80 \\
  nginx

# 4. Verifiera kommunikation
# Från nginx-containern, kan vi nå databasen via DNS-namn:
docker exec demo-web apt-get update && apt-get install -y postgresql-client
docker exec demo-web pg_isready -h demo-db -U admin
# Output: demo-db:5432 - accepting connections

# 5. Övervaka resurser
docker stats demo-db demo-web --no-stream

# 6. Se nätverkskonfiguration
docker network inspect demo-network

# Arkitekturdiagram (ASCII):
# +-----------------------------------------------------+
# |                   demo-network                      |
# |  +-------------+              +-------------+       |
# |  |  demo-db    |              |  demo-web   |       |
# |  | PostgreSQL  | <-- DNS -->  |   nginx     |       |
# |  |  :5432      |              |   :80       |       |
# |  +-------------+              +------+------+       |
# +----------------------------------------|------------+
#                                          |
#                                     port 8080
#                                          |
#                                       HOST

# Rensa efteråt
docker stop demo-db demo-web
docker rm demo-db demo-web
docker network rm demo-network
docker volume rm demo-pgdata
```

</details>

**Verifikation:** Du kan visa att nginx kan nå PostgreSQL via DNS-namn och du har ett dokumenterat diagram.

------------------------------------------------------------

## Kopplingar

Denna nod är grunden för allt som kommer. Här är hur den hänger ihop med resten av modulen:

| Nästa nod | Vad den bygger på |
|-----------|-------------------|
| **Docker Images Deep Dive** | Förståelse för layers och union filesystem |
| **Container Lifecycle** | Kunskap om container states och processer |
| **Dockerfile Mastery** | Insikt i hur images byggs lager för lager |
| **Docker Networking** | Grunder i Docker nätverksarkitektur |

**Förutsätter kunskap från:**
- Grundläggande Linux-kommandon
- Terminal/shell-användning

------------------------------------------------------------

## Sammanfattning

- **Docker löser "works on my machine"** genom att paketera applikationer med alla beroenden
- **Containers är INTE virtuella maskiner** - de delar kernel med host och är mycket lättare
- **Docker Engine** består av Client (CLI), Daemon (dockerd) och Container Runtime
- **Namespaces** ger isolation (process, nätverk, filsystem)
- **Cgroups** begränsar resurser (CPU, minne)
- **Images byggs i lager** som cachas för snabbare builds
- **OCI-standarden** gör att Docker-images kan köras av andra runtimes
- **Docker Hub** är standard-registryt för publika images

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `docker version` | Visa Docker-version | `docker version` |
| `docker info` | Visa systeminformation | `docker info` |
| `docker run` | Kör en container | `docker run -d -p 8080:80 nginx` |
| `docker ps` | Lista körande containers | `docker ps -a` (alla) |
| `docker images` | Lista images | `docker images` |
| `docker pull` | Ladda ner image | `docker pull nginx:1.25` |
| `docker stop` | Stoppa container | `docker stop mycontainer` |
| `docker rm` | Ta bort container | `docker rm mycontainer` |
| `docker logs` | Visa container-loggar | `docker logs -f mycontainer` |
| `docker exec` | Kör kommando i container | `docker exec -it mycontainer bash` |
| `docker inspect` | Visa detaljerad info | `docker inspect mycontainer` |
| `docker system prune` | Rensa oanvända resurser | `docker system prune -a` |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Docker Documentation](https://docs.docker.com/)
- [Docker Get Started Guide](https://docs.docker.com/get-started/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

**Fördjupning:**
- [Docker Deep Dive](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256) - Nigel Poulton
- [Container Security](https://www.oreilly.com/library/view/container-security/9781492056690/) - Liz Rice

**Hands-on:**
- [Play with Docker](https://labs.play-with-docker.com/) - Gratis Docker-miljö i webbläsaren
- [Docker 101 Tutorial](https://www.docker.com/101-tutorial/)

**OCI och standards:**
- [Open Container Initiative](https://opencontainers.org/)
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)
""",
        },
        {
            "title": "Docker Images Deep Dive",
            "slug": "docker-images-deep-dive",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Images Deep Dive

------------------------------------------------------------

## Introduktion

Du har startat din första container och sett magin hända - en hel applikationsmiljö som snurrar upp på sekunder. Men vad är det egentligen du laddar ner när du kör `docker pull nginx`? Var kommer alla filer ifrån, och varför är vissa images 50 MB medan andra är 1 GB?

Docker images är hjärtat i containerteknologin. Tänk på en image som en **färdigpackad resväska** innehållande allt din applikation behöver för att köra - operativsystemfiler, bibliotek, beroenden och din kod. Precis som du kan packa upp samma resväska på olika hotellrum runt världen, kan du starta samma image som identiska containers var som helst.

Som DevOps-ingenjör kommer du arbeta med images dagligen. Du kommer optimera build-tider i CI/CD-pipelines, reducera image-storlekar för snabbare deployments, och hantera versioner för säkra rollbacks. Ett misstag i din image-strategi kan kosta timmar i build-tid eller megabyte i onödig bandbredd - varje dag.

I den här noden dyker vi djupt i hur images faktiskt fungerar. Du kommer förstå layer-arkitekturen som gör caching möjligt, lära dig tagging-strategier som håller ordning i kaos, och bemästra de kommandon som ger dig full kontroll över ditt image-bibliotek.

------------------------------------------------------------

## Teori

### Vad är en Docker Image?

En Docker image är en **read-only mall** som innehåller allt som behövs för att skapa en container. Det inkluderar:

- Ett minimalt operativsystem (eller delar av det)
- Applikationskod och filer
- Runtime-miljö (Python, Node.js, Java, etc.)
- Bibliotek och beroenden
- Konfigurationsfiler
- Metadata (vilka kommandon som ska köras, portar, etc.)

```
+---------------------------------------------------------------+
|                      DOCKER IMAGE ANATOMI                     |
+---------------------------------------------------------------+
|                                                               |
|   +-------------------------------------------------------+   |
|   |                    METADATA                           |   |
|   |  - CMD: Standardkommando att köra                     |   |
|   |  - ENTRYPOINT: Container startpunkt                   |   |
|   |  - ENV: Miljövariabler                                |   |
|   |  - EXPOSE: Dokumenterade portar                       |   |
|   |  - WORKDIR: Arbetskatalog                             |   |
|   +-------------------------------------------------------+   |
|                                                               |
|   +-------------------------------------------------------+   |
|   |                    FILSYSTEM                          |   |
|   |  /bin      - Binärfiler                               |   |
|   |  /lib      - Bibliotek                                |   |
|   |  /usr      - Användarprogram                          |   |
|   |  /etc      - Konfiguration                            |   |
|   |  /app      - Din applikation                          |   |
|   +-------------------------------------------------------+   |
|                                                               |
+---------------------------------------------------------------+
```

### Image vs Container - Konceptuell Skillnad

Den vanligaste förvirringen för nybörjare är skillnaden mellan image och container:

| Koncept | Beskrivning | Analogi |
|---------|-------------|---------|
| **Image** | Read-only mall | Klass i programmering |
| **Container** | Körande instans | Objekt/instans av klassen |

```
+---------------------------------------------------------------+
|                     IMAGE -> CONTAINERS                       |
+---------------------------------------------------------------+
|                                                               |
|                    +---------------+                          |
|                    |    IMAGE      |                          |
|                    |   nginx:1.25  |                          |
|                    +-------+-------+                          |
|                            |                                  |
|            +---------------+---------------+                  |
|            |               |               |                  |
|            v               v               v                  |
|     +-----------+   +-----------+   +-----------+            |
|     | Container |   | Container |   | Container |            |
|     |   web-1   |   |   web-2   |   |   web-3   |            |
|     +-----------+   +-----------+   +-----------+            |
|                                                               |
|   Samma image -> Flera identiska containers                  |
|                                                               |
+---------------------------------------------------------------+
```

### Layer-arkitekturen

Docker images byggs upp av **lager (layers)** som staplas på varandra. Varje instruktion i en Dockerfile skapar ett nytt lager.

```
+---------------------------------------------------------------+
|                    LAYER ARCHITECTURE                         |
+---------------------------------------------------------------+
|                                                               |
|   Container (R/W Layer)                                       |
|   +-------------------------------------------------------+   |
|   |  Thin writable layer - ändringar sparas här           |   |
|   +-------------------------------------------------------+   |
|                            |                                  |
|   Image Layers (Read-Only) |                                  |
|   +-------------------------------------------------------+   |
|   |  Layer 5: COPY . /app                        [10 KB]  |   |
|   +-------------------------------------------------------+   |
|   |  Layer 4: RUN npm install                    [85 MB]  |   |
|   +-------------------------------------------------------+   |
|   |  Layer 3: COPY package*.json /app           [2 KB]    |   |
|   +-------------------------------------------------------+   |
|   |  Layer 2: WORKDIR /app                      [0 KB]    |   |
|   +-------------------------------------------------------+   |
|   |  Layer 1: FROM node:18-alpine               [170 MB]  |   |
|   +-------------------------------------------------------+   |
|                                                               |
+---------------------------------------------------------------+
```

**Varför layers är viktiga:**

1. **Caching**: Oförändrade layers återanvänds vid rebuild
2. **Delning**: Flera images kan dela samma base layers
3. **Effektivitet**: Endast ändrade layers behöver överföras
4. **Spårbarhet**: Du kan se exakt vad varje layer innehåller

### Image Naming Convention

Docker images följer ett specifikt namnformat:

```
[registry/][namespace/]repository[:tag][@digest]
```

| Del | Beskrivning | Exempel |
|-----|-------------|---------|
| **registry** | Var imagen lagras | docker.io, gcr.io, ghcr.io |
| **namespace** | Organisation/användare | library (official), mycompany |
| **repository** | Image-namn | nginx, python, myapp |
| **tag** | Version/variant | 1.25, 3.11-slim, latest |
| **digest** | Unik hash | sha256:abc123... |

```
+---------------------------------------------------------------+
|                    IMAGE NAMING EXAMPLES                      |
+---------------------------------------------------------------+
|                                                               |
|   nginx                                                       |
|   -> docker.io/library/nginx:latest                           |
|                                                               |
|   python:3.11-slim                                            |
|   -> docker.io/library/python:3.11-slim                       |
|                                                               |
|   mycompany/api:v2.3.1                                        |
|   -> docker.io/mycompany/api:v2.3.1                           |
|                                                               |
|   ghcr.io/owner/repo:sha-abc123                               |
|   -> GitHub Container Registry image                          |
|                                                               |
+---------------------------------------------------------------+
```

### Docker Hub och Registries

Docker Hub är det officiella och största publika registryt för Docker images:

| Registry | URL | Användning |
|----------|-----|------------|
| **Docker Hub** | hub.docker.com | Standard, publika images |
| **GitHub CR** | ghcr.io | GitHub-integrerade projekt |
| **Google CR** | gcr.io | Google Cloud projekt |
| **Amazon ECR** | *.ecr.*.amazonaws.com | AWS-projekt |
| **Azure CR** | *.azurecr.io | Azure-projekt |

**Officiella images** på Docker Hub är verifierade och underhållna av Docker eller upstrream-projektet. De känns igen på att de saknar namespace (t.ex. `nginx` istället för `someone/nginx`).

### Content-Addressable Storage

Docker använder **content-addressable storage** vilket innebär att varje layer identifieras av sin SHA256-hash. Detta garanterar:

- **Integritet**: Om innehållet ändras, ändras hashen
- **Deduplicering**: Identiskt innehåll lagras bara en gång
- **Verifiering**: Du kan verifiera att en image är exakt den du förväntar dig

```bash
# Image digest garanterar exakt samma image
docker pull nginx@sha256:abc123def456...

# Jämfört med tag som kan ändras
docker pull nginx:latest  # Kan peka på olika images över tid
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Utforska images på ditt system

```bash
# Lista alla images på systemet
docker images
# Eller med ny syntax
docker image ls

# Förväntad output:
# REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
# nginx        latest    a6bd71f48f68   2 days ago    187MB
# python       3.11      abc123def456   1 week ago    1.01GB

# Visa alla images inklusive intermediate layers
docker images -a

# Filtrera images
docker images --filter "dangling=true"  # Ej taggade images
docker images nginx  # Bara nginx images
```

### Steg 2: Ladda ner images från Docker Hub

```bash
# Sök efter images på Docker Hub
docker search python
# Output visar: NAME, DESCRIPTION, STARS, OFFICIAL

# Ladda ner en specifik image
docker pull python:3.11-slim
# Output visar nedladdning av varje layer:
# 3.11-slim: Pulling from library/python
# a2abf6c4d29d: Pull complete
# ...

# Ladda ner med specifik digest (garanterat samma image)
docker pull nginx@sha256:593dac25b7733ff...
```

### Steg 3: Inspektera images i detalj

```bash
# Visa detaljerad metadata för en image
docker image inspect nginx:latest

# Visa bara specifik information med Go templates
docker image inspect nginx --format '{{.Config.Cmd}}'
# Output: [nginx -g daemon off;]

docker image inspect nginx --format '{{.Config.ExposedPorts}}'
# Output: map[80/tcp:{}]

# Visa layer-historik
docker history nginx:latest
# Output visar varje layer och dess storlek
```

### Steg 4: Tagga och organisera images

```bash
# Skapa en ny tagg för en befintlig image
docker tag nginx:latest mycompany/nginx:v1.0

# Nu finns samma image under två namn
docker images | grep nginx
# nginx          latest   a6bd71f48f68   ...
# mycompany/nginx  v1.0     a6bd71f48f68   ...  <- Samma IMAGE ID!

# Tagga med flera tags
docker tag myapp:latest myapp:v2.3.1
docker tag myapp:latest myapp:stable
```

### Steg 5: Städa upp images

```bash
# Ta bort en specifik image
docker rmi nginx:latest
# Eller
docker image rm nginx:latest

# Ta bort flera images
docker rmi nginx:1.24 nginx:1.23

# Ta bort ALLA oanvända images (försiktig!)
docker image prune -a

# Ta bort bara dangling images (säkrare)
docker image prune

# Se hur mycket diskutrymme som används
docker system df
# Output visar utrymme för images, containers, volumes
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Jämföra base images

Olika base images har drastiskt olika storlekar:

```bash
# Ladda ner tre varianter av Python
docker pull python:3.11
docker pull python:3.11-slim
docker pull python:3.11-alpine

# Jämför storlekarna
docker images python
# REPOSITORY   TAG           SIZE
# python       3.11          1.01GB   <- Full Debian-baserad
# python       3.11-slim     154MB    <- Stripped Debian
# python       3.11-alpine   51.8MB   <- Alpine Linux

# Skillnad: ~950 MB mellan full och alpine!
```

### Exempel 2: Analysera layer-struktur

```bash
# Se exakt vad som finns i varje layer
docker history python:3.11-slim --no-trunc

# Formaterad output
docker history python:3.11-slim --format "{{.Size}}\\t{{.CreatedBy}}"

# Installera dive för visuell analys (valfritt)
# brew install dive  # macOS
# dive python:3.11-slim
```

### Exempel 3: Exportera och importera images

```bash
# Spara en image som tar-fil (för backup eller transport)
docker save nginx:latest -o nginx-backup.tar

# Kontrollera filen
ls -lh nginx-backup.tar
# -rw-------  1 user  staff   186M Dec 10 10:00 nginx-backup.tar

# Ladda in image från tar-fil
docker load -i nginx-backup.tar

# Alternativ: export container (bara filsystemet, inte metadata)
docker export mycontainer -o container-fs.tar
docker import container-fs.tar myimage:imported
```

### Exempel 4: Arbeta med registries

```bash
# Logga in på Docker Hub
docker login
# Username: myusername
# Password: ********

# Pusha en image till Docker Hub
docker tag myapp:v1.0 myusername/myapp:v1.0
docker push myusername/myapp:v1.0

# Logga in på GitHub Container Registry
docker login ghcr.io -u USERNAME
# Ange Personal Access Token som lösenord

# Pusha till GHCR
docker tag myapp:v1.0 ghcr.io/myusername/myapp:v1.0
docker push ghcr.io/myusername/myapp:v1.0
```

------------------------------------------------------------

## Bästa Praxis

1. **Använd specifika taggar, aldrig bara `latest`**
   ```bash
   # Bra - reproducerbart
   FROM python:3.11.6-slim-bookworm

   # Dåligt - kan ändras när som helst
   FROM python:latest
   ```

2. **Välj rätt base image för användningsfallet**
   ```bash
   # Produktion - minimal attack surface
   FROM python:3.11-alpine

   # Utveckling - alla verktyg tillgängliga
   FROM python:3.11

   # Balans - lagom storlek med glibc
   FROM python:3.11-slim
   ```

3. **Städa regelbundet med automatisering**
   ```bash
   # Lägg till i cron eller CI/CD
   docker image prune -f --filter "until=168h"  # Äldre än 7 dagar
   ```

4. **Verifiera images med digest i produktion**
   ```bash
   # I docker-compose.yml eller Kubernetes manifests
   image: nginx@sha256:593dac25b7733ff...
   ```

5. **Dokumentera image-val och versioner**
   ```dockerfile
   # Dokumentera varför denna base image valdes
   # python:3.11-slim väljs för:
   # - Balans mellan storlek och kompatibilitet
   # - glibc för native extensions
   # - Debian stable security updates
   FROM python:3.11-slim
   ```

------------------------------------------------------------

## Vanliga Fallgropar

### Problem 1: Disk full av images

**Symptom:**
```
No space left on device
```

**Orsak:** Images, containers och build cache samlas över tid.

**Lösning:**
```bash
# Se vad som tar plats
docker system df

# Aggressiv städning
docker system prune -a --volumes

# Regelbunden städning (säkrare)
docker image prune -a --filter "until=168h"
```

### Problem 2: Kan inte ta bort image "in use"

**Symptom:**
```
Error response from daemon: conflict: unable to delete (must be forced)
image is being used by stopped container abc123
```

**Lösning:**
```bash
# Hitta vilka containers som använder imagen
docker ps -a --filter ancestor=nginx:old

# Ta bort containrarna först
docker rm container1 container2

# Nu kan du ta bort imagen
docker rmi nginx:old

# Eller tvinga bort (tar bort containers också)
docker rmi -f nginx:old
```

### Problem 3: Latest är inte senaste

**Symptom:** Du kör `docker pull myimage:latest` men får inte senaste ändringarna.

**Orsak:** `latest` är bara en tag som kan peka på vilken version som helst.

**Lösning:**
```bash
# Alltid pull innan körning för att säkerställa senaste
docker pull myimage:latest

# Bättre: Använd specifika versioner
docker pull myimage:v2.3.1

# Se när imagen senast uppdaterades
docker image inspect myimage:latest --format '{{.Created}}'
```

### Problem 4: Alpine-kompatibilitetsproblem

**Symptom:** Python-paket eller binärer fungerar inte i alpine images.

**Orsak:** Alpine använder musl libc istället för glibc.

**Lösning:**
```bash
# Använd slim istället för alpine om du behöver glibc
FROM python:3.11-slim

# Eller installera build-verktyg i alpine
FROM python:3.11-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
```

------------------------------------------------------------

## Övningar

### Övning 1: Image-hantering Basics (20 XP)

**Mål:** Bemästra grundläggande image-kommandon.

**Din uppgift:**
1. Ladda ner tre olika Python images (full, slim, alpine)
2. Jämför deras storlekar och dokumentera skillnaden
3. Tagga python:3.11-slim som `mycompany/python:prod`
4. Visa layer-historik för alpine-varianten
5. Ta bort alla tre images och verifiera att de är borta

<details>
<summary>Ledtråd</summary>

- Använd `docker pull` för att ladda ner
- `docker images python` filtrerar på repository
- `docker tag` skapar en ny referens till samma IMAGE ID
- `docker history` visar layers
- `docker rmi` tar bort, verifiera med `docker images`

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Ladda ner images
docker pull python:3.11
docker pull python:3.11-slim
docker pull python:3.11-alpine

# 2. Jämför storlekar
docker images python --format "table {{.Tag}}\\t{{.Size}}"
# TAG           SIZE
# 3.11          1.01GB
# 3.11-slim     154MB
# 3.11-alpine   51.8MB
# Skillnad: Full är ~20x större än alpine!

# 3. Tagga slim
docker tag python:3.11-slim mycompany/python:prod
docker images | grep mycompany
# mycompany/python   prod   abc123   154MB

# 4. Visa history för alpine
docker history python:3.11-alpine
# Visar varje layer och storlek

# 5. Ta bort alla
docker rmi python:3.11 python:3.11-slim python:3.11-alpine mycompany/python:prod
docker images python
# Bör vara tom
```

</details>

**Verifikation:** Du kan förklara varför samma IMAGE ID kan ha flera taggar.

---

### Övning 2: Layer-analys (25 XP)

**Mål:** Förstå hur layers påverkar image-storlek och build-tid.

**Scenario:** Du ska analysera varför din images är så stora.

**Din uppgift:**
1. Ladda ner `node:18` och `node:18-alpine`
2. Använd `docker history` för att jämföra antal layers
3. Identifiera de tre största layers i varje image
4. Exportera `node:18-alpine` till en tar-fil och undersök innehållet
5. Dokumentera dina findings i en kort rapport

<details>
<summary>Ledtråd</summary>

- `docker history --no-trunc` visar full information
- `docker save` skapar tar-fil med alla layers
- `tar -tvf` listar innehåll utan att extrahera
- Layers lagras som separata tar-filer i exporten

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Ladda ner images
docker pull node:18
docker pull node:18-alpine

# 2. Jämför layers
docker history node:18 | wc -l
# Ca 15-20 layers

docker history node:18-alpine | wc -l
# Ca 10-12 layers

# 3. Största layers
docker history node:18 --format "{{.Size}}\\t{{.CreatedBy}}" | sort -h | tail -5

docker history node:18-alpine --format "{{.Size}}\\t{{.CreatedBy}}" | sort -h | tail -5

# 4. Exportera och undersök
docker save node:18-alpine -o node-alpine.tar
tar -tvf node-alpine.tar | head -20
# Visar manifest.json och layer-kataloger

# 5. Rapport
# node:18 (~1GB): Baserad på Debian, inkluderar många utvecklingsverktyg
# node:18-alpine (~175MB): Baserad på Alpine, minimal, saknar glibc
# Största layers är ofta: base OS, npm cache, node binaries
```

</details>

**Verifikation:** Du kan förklara varför vissa layers är större än andra.

---

### Övning 3: Registry-workflow (30 XP)

**Mål:** Hantera images professionellt med taggar och registries.

**Scenario:** Du ska sätta upp ett image-workflow för ditt team.

**Din uppgift:**
1. Skapa ett Docker Hub-konto (om du inte har)
2. Tagga `nginx:alpine` med tre versioner:
   - `yourusername/nginx:v1.0.0`
   - `yourusername/nginx:v1.0`
   - `yourusername/nginx:latest`
3. Pusha alla tre till Docker Hub
4. Ta bort de lokala kopiorna
5. Dra ner med digest och verifiera

<details>
<summary>Ledtråd</summary>

- Skapa konto på hub.docker.com
- `docker login` innan push
- Alla tre taggar pekar på samma image (samma digest)
- `docker inspect` visar digest under RepoDigests
- `docker pull image@sha256:...` drar med digest

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Logga in
docker login
# Ange användarnamn och lösenord

# 2. Skapa taggar (ersätt 'yourusername')
docker pull nginx:alpine
docker tag nginx:alpine yourusername/nginx:v1.0.0
docker tag nginx:alpine yourusername/nginx:v1.0
docker tag nginx:alpine yourusername/nginx:latest

# 3. Pusha alla
docker push yourusername/nginx:v1.0.0
docker push yourusername/nginx:v1.0
docker push yourusername/nginx:latest

# 4. Ta bort lokala
docker rmi yourusername/nginx:v1.0.0 yourusername/nginx:v1.0 yourusername/nginx:latest

# 5. Hämta digest och dra med den
# Gå till hub.docker.com och hitta digest, eller:
docker pull yourusername/nginx:latest
docker inspect yourusername/nginx:latest --format '{{index .RepoDigests 0}}'
# Output: yourusername/nginx@sha256:abc123...

# Dra med digest
docker rmi yourusername/nginx:latest
docker pull yourusername/nginx@sha256:abc123...
```

</details>

**Verifikation:** Du kan visa att din image finns på Docker Hub och förklara fördelen med digest.

------------------------------------------------------------

## Kopplingar

| Relaterad nod | Koppling |
|---------------|----------|
| **Docker Fundamentals** | Bygger på grundläggande container-koncept |
| **Dockerfile Mastery** | Nästa steg - skapa egna images |
| **Multi-stage Builds** | Avancerad image-optimering |
| **Docker Registry** | Djupdykning i registry-hantering |
| **Docker Security** | Image scanning och säkerhet |

**Förkunskaper:**
- Docker Fundamentals & Architecture (Nod 1)

------------------------------------------------------------

## Sammanfattning

- **Images är read-only mallar** som innehåller allt en container behöver
- **Layers stackas** och varje Dockerfile-instruktion skapar ett nytt layer
- **Caching** gör att oförändrade layers återanvänds - ordning spelar roll!
- **Taggar är pekare** till specifika image-versioner - använd specifika versioner
- **Digests** (SHA256) garanterar exakt samma image varje gång
- **Alpine images** är minst men kan ha kompatibilitetsproblem med glibc
- **Städa regelbundet** med `docker image prune` för att spara diskutrymme
- **Docker Hub** är default registry - verifiera officiella images

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `docker images` | Lista images | `docker images python` |
| `docker pull` | Ladda ner image | `docker pull nginx:1.25` |
| `docker push` | Ladda upp image | `docker push myuser/app:v1` |
| `docker tag` | Skapa ny tagg | `docker tag app:latest app:v2` |
| `docker rmi` | Ta bort image | `docker rmi nginx:old` |
| `docker image prune` | Ta bort oanvända | `docker image prune -a` |
| `docker history` | Visa layers | `docker history nginx` |
| `docker inspect` | Visa metadata | `docker inspect nginx` |
| `docker save` | Exportera till tar | `docker save nginx -o nginx.tar` |
| `docker load` | Importera från tar | `docker load -i nginx.tar` |
| `docker search` | Sök på Docker Hub | `docker search python` |
| `docker login` | Logga in registry | `docker login ghcr.io` |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Docker Image Documentation](https://docs.docker.com/engine/reference/commandline/image/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

**Fördjupning:**
- [Dive - Image Layer Explorer](https://github.com/wagoodman/dive)
- [Docker Image Specification](https://github.com/moby/moby/blob/master/image/spec/v1.md)

**Verktyg:**
- [Trivy - Image Vulnerability Scanner](https://github.com/aquasecurity/trivy)
- [Hadolint - Dockerfile Linter](https://github.com/hadolint/hadolint)
""",
        },
        {
            "title": "Container Lifecycle Management",
            "slug": "container-lifecycle-management",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Container Lifecycle Management

------------------------------------------------------------

## Introduktion

Containers är som levande organismer med en tydlig livscykel - de föds (skapas), lever (körs), pausas, återupptas och slutligen dör (stoppas/tas bort). Att förstå denna livscykel är fundamental för att effektivt hantera containeriserade applikationer i produktion.

I denna modul lär du dig att hantera hela container-livscykeln: från att starta containers med rätt konfiguration, till att övervaka deras hälsa, och slutligen stoppa dem på ett säkert sätt som bevarar data och möjliggör graceful shutdown.

**I denna modul lär du dig:**
- Förstå de olika tillstånden en container kan befinna sig i
- Starta containers med rätt flaggor för olika användningsfall
- Övervaka och felsöka körande containers
- Stoppa containers korrekt med graceful shutdown
- Hantera container-livscykeln i automatiserade miljöer

**Förkunskapskrav:**
- Grundläggande Docker-kunskap (Node 1)
- Förståelse för Docker Images (Node 2)
- Terminal/kommandoradsvana

------------------------------------------------------------

## Teori

### Varför viktigt för DevOps?

| Scenario | Varför Lifecycle Management är avgörande |
|----------|------------------------------------------|
| **Zero-downtime deploys** | Graceful shutdown krävs för rolling updates utan avbrott |
| **Resource management** | Stoppa och ta bort containers för att frigöra resurser |
| **Incident response** | Snabbt kunna starta om eller byta ut problemcontainers |
| **Auto-scaling** | Automatiskt starta/stoppa containers baserat på last |
| **CI/CD pipelines** | Kortlivade containers för test och build |

### Container States Förklarade

En Docker container kan befinna sig i något av följande tillstånd:

| State | Beskrivning | Minnesanvändning |
|-------|-------------|------------------|
| **Created** | Container skapad men ej startad | Minimal |
| **Running** | Processer körs aktivt | Full allokering |
| **Paused** | Processer frysta (SIGSTOP) | Full (minnet behålls) |
| **Restarting** | Container startar om | Varierar |
| **Exited** | Container stoppat | Ingen (men filsystem finns kvar) |
| **Dead** | Fel vid borttagning | Minimal (kräver manuell rensning) |

### Container Lifecycle Diagram

```
+---------------------------------------------------------------------+
|                     CONTAINER LIFECYCLE                              |
+---------------------------------------------------------------------+
|                                                                      |
|                         +-----------+                                |
|                         |   IMAGE   |                                |
|                         +-----+-----+                                |
|                               |                                      |
|                               | docker create                        |
|                               v                                      |
|   +---------------------------------------------------------------+  |
|   |                                                               |  |
|   |   +-----------+                         +-----------+         |  |
|   |   |  CREATED  |------- docker start --->|  RUNNING  |         |  |
|   |   +-----------+                         +-----+-----+         |  |
|   |        ^                                      |               |  |
|   |        |                                      |               |  |
|   |        |                          +-----------+-----------+   |  |
|   |        |                          |           |           |   |  |
|   |        |                    docker pause  docker stop  crash  |  |
|   |        |                          |       (SIGTERM)       |   |  |
|   |        |                          v           |           |   |  |
|   |        |                    +-----------+     |           |   |  |
|   |        |                    |  PAUSED   |     |           |   |  |
|   |        |                    +-----+-----+     |           |   |  |
|   |        |                          |           |           |   |  |
|   |        |                  docker unpause      |           |   |  |
|   |        |                          |           |           |   |  |
|   |        |                          v           v           v   |  |
|   |        |                    +-----------+ +-------+ +-------+ |  |
|   |        +--- docker start ---|  RUNNING  | | EXITED| | DEAD  | |  |
|   |                             +-----------+ +-------+ +-------+ |  |
|   |                                                               |  |
|   +---------------------------------------------------------------+  |
|                                                                      |
+---------------------------------------------------------------------+
```

### Signaler och Shutdown

| Signal | Kommando | Beteende |
|--------|----------|----------|
| **SIGTERM** | `docker stop` | Ber processen avsluta snyggt |
| **SIGKILL** | `docker kill` | Tvingar omedelbar avslutning |
| **SIGSTOP** | `docker pause` | Fryser alla processer |
| **SIGCONT** | `docker unpause` | Återupptar frysta processer |

**Graceful Shutdown-flöde:**
1. `docker stop` skickar SIGTERM
2. Applikationen får 10 sekunder (default) att städa
3. Om processen fortfarande körs, skickas SIGKILL
4. Container status blir "Exited"

### Exit Codes

| Exit Code | Betydelse | Vanlig orsak |
|-----------|-----------|--------------|
| **0** | Framgång | Applikationen avslutades normalt |
| **1** | Generellt fel | Applikationsfel |
| **125** | Docker daemon-fel | Problem med Docker själv |
| **126** | Kan ej köra kommando | Permission denied |
| **127** | Kommando ej hittat | Fel CMD/ENTRYPOINT i Dockerfile |
| **137** | SIGKILL (128+9) | OOM killed eller `docker kill` |
| **143** | SIGTERM (128+15) | Normal `docker stop` |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa och Starta Containers

```bash
# Metod 1: docker run (create + start i ett steg)
docker run -d --name webserver nginx:1.25

# Metod 2: Separata steg (mer kontroll)
docker create --name webserver nginx:1.25
docker start webserver
```

### Steg 2: Verifiera Container Status

```bash
# Lista körande containers
docker ps

# Visa output:
# CONTAINER ID   IMAGE        STATUS         PORTS     NAMES
# a1b2c3d4e5f6   nginx:1.25   Up 2 minutes   80/tcp    webserver

# Lista ALLA containers (inklusive stoppade)
docker ps -a

# Detaljerad information
docker inspect webserver
```

### Steg 3: Interagera med Körande Container

```bash
# Kör kommando i containern
docker exec webserver cat /etc/nginx/nginx.conf

# Öppna interaktiv shell
docker exec -it webserver /bin/bash

# Visa processer inne i containern
docker top webserver
```

### Steg 4: Övervaka Container

```bash
# Visa loggar
docker logs webserver

# Följ loggar i realtid
docker logs -f webserver

# Senaste 100 rader
docker logs --tail 100 webserver

# Live CPU/minnesanvändning
docker stats webserver
```

### Steg 5: Stoppa Container Korrekt

```bash
# Graceful stop (SIGTERM, väntar 10s, sedan SIGKILL)
docker stop webserver

# Med längre timeout för tunga applikationer
docker stop -t 30 webserver

# Forcerad stopp (endast vid problem)
docker kill webserver
```

### Steg 6: Ta Bort Container

```bash
# Ta bort stoppad container
docker rm webserver

# Forcera borttagning av körande container
docker rm -f webserver

# Ta bort alla stoppade containers
docker container prune
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Webserver med Auto-Restart

```bash
# Starta nginx med automatisk omstart vid krasch
docker run -d \\
    --name production-web \\
    --restart unless-stopped \\
    -p 80:80 \\
    nginx:1.25-alpine

# Restart policies:
# no            - Aldrig starta om (default)
# always        - Starta alltid om
# unless-stopped - Starta om om inte manuellt stoppad
# on-failure    - Starta om endast vid fel (exit != 0)
```

### Exempel 2: Engångs-Container för Jobb

```bash
# Kör databasbackup och ta bort containern efteråt
docker run --rm \\
    --name db-backup \\
    -v backup:/backup \\
    postgres:15 \\
    pg_dump -h db.example.com mydb > /backup/dump.sql

# --rm flaggan säkerställer att containern tas bort
```

### Exempel 3: Debug-Container

```bash
# Starta tillfällig debug-container i samma nätverk
docker run -it --rm \\
    --name debugger \\
    --network app_network \\
    alpine:3.19 sh

# Inne i containern:
# ping other-container
# wget -qO- http://api-server:8080/health
```

### Exempel 4: Health Check Monitoring

```bash
# Starta container med inbyggd health check
docker run -d \\
    --name healthy-app \\
    --health-cmd="curl -f http://localhost:8080/health || exit 1" \\
    --health-interval=30s \\
    --health-timeout=10s \\
    --health-retries=3 \\
    myapp:latest

# Övervaka hälsostatus
docker inspect --format='{{.State.Health.Status}}' healthy-app
```

### Exempel 5: Graceful Shutdown i Applikation

```python
# Python-app som hanterar SIGTERM korrekt
import signal
import sys
import time

def graceful_shutdown(signum, frame):
    print("Received SIGTERM, cleaning up...")
    # Stäng databasanslutningar
    # Spara state
    # Avsluta pågående requests
    time.sleep(2)  # Simulera cleanup
    print("Cleanup complete, exiting")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)

# Huvudloop
while True:
    print("Working...")
    time.sleep(1)
```

------------------------------------------------------------

## Bästa Praxis

### Namngivning och Organisation

| Princip | Exempel | Förklaring |
|---------|---------|------------|
| **Använd beskrivande namn** | `--name api-prod-v2` | Underlättar identifiering |
| **Inkludera miljö** | `web-staging`, `web-prod` | Separera miljöer tydligt |
| **Versionsprefix** | `api-v2.1.0` | Spåra vilken version som körs |

### Restart Policies

| Policy | Användning |
|--------|------------|
| `no` | Development, engångsjobb |
| `on-failure` | Services som bör stanna om de lyckas |
| `unless-stopped` | Production services (bästa val oftast) |
| `always` | Kritiska services som ALLTID måste köra |

### Resource Limits

```bash
# Sätt minnesgräns för att förhindra OOM på host
docker run -d \\
    --name api \\
    --memory=512m \\
    --memory-swap=512m \\
    --cpus=1.0 \\
    myapi:latest
```

### Logging Best Practices

```bash
# Konfigurera loggrotation för att spara disk
docker run -d \\
    --name app \\
    --log-driver json-file \\
    --log-opt max-size=10m \\
    --log-opt max-file=3 \\
    myapp:latest
```

------------------------------------------------------------

## Vanliga Fallgropar

| Fallgrop | Problem | Lösning |
|----------|---------|---------|
| **Glömma --rm** | Oanvända containers fyller disken | Använd `--rm` för temporära containers |
| **Använda docker kill som default** | Ingen graceful shutdown | Använd alltid `docker stop` först |
| **Inga minnesgränser** | Container tar all RAM, kraschar host | Sätt alltid `-m` i produktion |
| **latest tag** | Vet inte vilken version som körs | Använd specifika versioner |
| **Ignorera exit codes** | Missar varför containers dör | Analysera `docker inspect` |

### Felsökningskommandon

```bash
# Container startar inte?
docker logs container_name
docker inspect container_name --format='{{.State.Error}}'

# Container crashar direkt?
docker run -it image_name sh  # Kör interaktivt istället

# Out of memory?
docker inspect container_name --format='{{.State.OOMKilled}}'

# Se senaste events
docker events --since 1h
```

------------------------------------------------------------

## Övningar

### Övning 1: Livscykel-hantering (Grundläggande)

**Uppgift:** Demonstrera hela container-livscykeln genom att skapa, starta, pausa, återuppta och stoppa en container.

1. Skapa en nginx container utan att starta den
2. Starta containern
3. Verifiera att den körs
4. Pausa containern och verifiera status
5. Återuppta och verifiera
6. Stoppa med 5 sekunders timeout
7. Ta bort containern

<details>
<summary>Ledtråd</summary>

Använd följande kommandon i sekvens:
- `docker create --name`
- `docker start`
- `docker ps`
- `docker pause` / `docker unpause`
- `docker stop -t`
- `docker rm`

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Skapa container utan att starta
docker create --name lifecycle-demo nginx:alpine

# 2. Starta containern
docker start lifecycle-demo

# 3. Verifiera att den körs
docker ps --filter name=lifecycle-demo
# STATUS: Up X seconds

# 4. Pausa containern
docker pause lifecycle-demo
docker ps --filter name=lifecycle-demo
# STATUS: Up X seconds (Paused)

# 5. Återuppta
docker unpause lifecycle-demo
docker ps --filter name=lifecycle-demo
# STATUS: Up X seconds (ej längre Paused)

# 6. Stoppa med 5 sekunders timeout
docker stop -t 5 lifecycle-demo

# 7. Ta bort containern
docker rm lifecycle-demo

# Verifiera borttagning
docker ps -a --filter name=lifecycle-demo
# (ingen output = borttagen)
```

</details>

### Övning 2: Exit Code Analys (Medel)

**Uppgift:** Skapa tre containers som avslutas med olika exit codes och analysera resultaten.

1. Skapa en container som avslutas med exit code 0
2. Skapa en container som avslutas med exit code 1
3. Skapa en container som du force-killar
4. Analysera exit codes för alla tre

<details>
<summary>Ledtråd</summary>

- För exit 0: `docker run alpine exit 0`
- För exit 1: `docker run alpine exit 1`
- För exit 137: starta en långkörande process och använd `docker kill`
- Använd `docker inspect` med format-flagga för att läsa exit codes

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Container med exit 0 (success)
docker run --name exit-zero alpine:3.19 sh -c "exit 0"

# 2. Container med exit 1 (error)
docker run --name exit-one alpine:3.19 sh -c "exit 1"

# 3. Container som kill:as (exit 137)
docker run -d --name exit-kill alpine:3.19 sleep 3600
docker kill exit-kill

# 4. Analysera exit codes
echo "Exit codes:"
docker inspect exit-zero --format='exit-zero: {{.State.ExitCode}}'
# exit-zero: 0

docker inspect exit-one --format='exit-one: {{.State.ExitCode}}'
# exit-one: 1

docker inspect exit-kill --format='exit-kill: {{.State.ExitCode}}'
# exit-kill: 137

# Bonus: Kolla om OOM killed
docker inspect exit-kill --format='OOMKilled: {{.State.OOMKilled}}'
# OOMKilled: false

# Städa upp
docker rm exit-zero exit-one exit-kill
```

</details>

### Övning 3: Production-Ready Setup (Avancerad)

**Uppgift:** Sätt upp en produktionsklar container med restart policy, resource limits, health checks och loggrotation.

Krav:
- Använd nginx:alpine
- Sätt minnesgräns till 128MB
- CPU-gräns till 0.5 cores
- Health check som kontrollerar port 80 var 30:e sekund
- Loggrotation: max 5MB, max 3 filer
- Restart policy: unless-stopped

<details>
<summary>Ledtråd</summary>

Kombinera flera docker run-flaggor:
- `--memory` och `--cpus` för resursgränser
- `--health-cmd`, `--health-interval` för health checks
- `--log-opt max-size`, `--log-opt max-file` för loggar
- `--restart unless-stopped` för restart policy

</details>

<details>
<summary>Lösning</summary>

```bash
# Production-ready container setup
docker run -d \\
    --name prod-nginx \\
    --restart unless-stopped \\
    --memory=128m \\
    --cpus=0.5 \\
    --health-cmd="wget -q --spider http://localhost:80 || exit 1" \\
    --health-interval=30s \\
    --health-timeout=5s \\
    --health-retries=3 \\
    --health-start-period=10s \\
    --log-driver json-file \\
    --log-opt max-size=5m \\
    --log-opt max-file=3 \\
    -p 8080:80 \\
    nginx:alpine

# Verifiera konfiguration
echo "=== Resource Limits ==="
docker inspect prod-nginx --format='Memory: {{.HostConfig.Memory}}'
docker inspect prod-nginx --format='CPUs: {{.HostConfig.NanoCpus}}'

echo "=== Health Status ==="
docker inspect prod-nginx --format='Health: {{.State.Health.Status}}'

echo "=== Restart Policy ==="
docker inspect prod-nginx --format='Restart: {{.HostConfig.RestartPolicy.Name}}'

echo "=== Log Config ==="
docker inspect prod-nginx --format='LogConfig: {{.HostConfig.LogConfig}}'

# Testa health check (vänta 30 sekunder)
sleep 35
docker inspect prod-nginx --format='Health: {{.State.Health.Status}}'
# Expected: healthy

# Städa upp
docker rm -f prod-nginx
```

</details>

------------------------------------------------------------

## Kopplingar

| Ämne | Koppling |
|------|----------|
| **Docker Compose** | Definierar livscykel för multi-container apps |
| **Kubernetes** | Pods hanterar container-livscykler automatiskt |
| **CI/CD** | Kortlivade containers för build och test |
| **Monitoring** | Prometheus/Grafana övervakar container-metrics |
| **Orchestration** | Swarm/K8s hanterar restart och scaling automatiskt |

### Nästa steg i din DevOps-resa

```
+---------------------------------------------------------------------+
|                     LEARNING PATH                                    |
+---------------------------------------------------------------------+
|                                                                      |
|   [Du är här]                                                        |
|        |                                                             |
|        v                                                             |
|   Container Lifecycle --> Dockerfile Mastery --> Docker Networking   |
|        |                        |                      |             |
|        |                        v                      v             |
|        +-------------> Docker Compose <---------------+              |
|                             |                                        |
|                             v                                        |
|                    Production Deployment                             |
|                             |                                        |
|                             v                                        |
|                   Kubernetes / Docker Swarm                          |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

### Centrala Koncept

| Koncept | Huvudpoäng |
|---------|------------|
| **States** | Created, Running, Paused, Exited, Dead |
| **Signaler** | SIGTERM för graceful, SIGKILL för force |
| **Exit codes** | 0=OK, 1=fel, 137=killed, 143=stopped |
| **Restart policies** | unless-stopped för produktion |

### Viktiga Insikter

1. **Graceful shutdown är kritiskt** - Använd alltid `docker stop` före `docker kill`
2. **Exit codes berättar historien** - Analysera dem för att förstå varför containers dog
3. **Resource limits skyddar hosten** - Sätt alltid minnesgränser i produktion
4. **Health checks möjliggör automation** - Orchestrators använder dem för att hantera livscykeln

------------------------------------------------------------

## Nyckelkommandon

### Livscykelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker create --name X image` | Skapa utan att starta |
| `docker start X` | Starta container |
| `docker run -d --name X image` | Create + start i ett |
| `docker stop X` | Graceful stop (SIGTERM) |
| `docker stop -t 30 X` | Stop med 30s timeout |
| `docker kill X` | Force stop (SIGKILL) |
| `docker restart X` | Stop + start |
| `docker pause X` | Frys processer |
| `docker unpause X` | Återuppta |
| `docker rm X` | Ta bort container |
| `docker rm -f X` | Force ta bort |

### Övervakningskommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker ps` | Lista körande |
| `docker ps -a` | Lista alla |
| `docker logs X` | Visa loggar |
| `docker logs -f X` | Följ loggar live |
| `docker stats X` | CPU/minne live |
| `docker top X` | Processer i container |
| `docker inspect X` | All metadata |

### Diagnostikkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker inspect X --format='{{.State.ExitCode}}'` | Hämta exit code |
| `docker inspect X --format='{{.State.OOMKilled}}'` | Kolla OOM |
| `docker events --since 1h` | Senaste events |
| `docker exec -it X sh` | Debug shell |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Docker Run Reference](https://docs.docker.com/engine/reference/run/)
- [Container Lifecycle](https://docs.docker.com/engine/reference/commandline/container/)
- [Docker Events](https://docs.docker.com/engine/reference/commandline/events/)

**Fördjupning:**
- [Understanding Docker Container Exit Codes](https://betterprogramming.pub/understanding-docker-container-exit-codes-5ee79a1d58f6)
- [Graceful Shutdown in Containers](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace)

**Verktyg:**
- [ctop - Container Top](https://github.com/bcicen/ctop) - Visuell container-övervakning
- [lazydocker](https://github.com/jesseduffield/lazydocker) - Terminal UI för Docker
""",
        },
        {
            "title": "Dockerfile Mastery",
            "slug": "dockerfile-mastery",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Dockerfile Mastery

------------------------------------------------------------

## Introduktion

Dockerfile är ritningen för dina Docker images - ett recept som definierar exakt hur din applikation ska paketeras och köras. Att behärska Dockerfile-syntax och best practices är en kärnkompetens för varje DevOps-ingenjör eftersom det direkt påverkar build-tider, image-storlek, säkerhet och reproducerbarhet.

En välskriven Dockerfile kan reducera build-tider från minuter till sekunder, minska image-storlek med 90%, och eliminera hela kategorier av säkerhetsproblem. Omvänt kan en dålig Dockerfile skapa flaskhalsar i din CI/CD-pipeline och introducera sårbarheter.

**I denna modul lär du dig:**
- Förstå varje Dockerfile-instruktion och när den ska användas
- Optimera layer caching för snabbare builds
- Skriva säkra Dockerfiles med non-root users
- Implementera multi-stage builds för minimala production images
- Felsöka vanliga Dockerfile-problem

**Förkunskapskrav:**
- Docker Images Deep Dive (Node 2)
- Container Lifecycle Management (Node 3)
- Grundläggande terminalkunskap

------------------------------------------------------------

## Teori

### Varför viktigt för DevOps?

| Scenario | Varför Dockerfile-kunskap är kritisk |
|----------|-------------------------------------|
| **CI/CD Pipelines** | Automatiska builds kräver reproducerbara, snabba Dockerfiles |
| **Team-samarbete** | Dockerfile dokumenterar exakt hur appen byggs |
| **Säkerhet** | CVE-scanning, minimal attack-yta, non-root execution |
| **Kostnadsoptimering** | Mindre images = lägre registry-kostnader, snabbare deploys |
| **Incident Response** | Kunna snabbt bygga om och deploya fixar |

### Dockerfile Anatomy

```
+---------------------------------------------------------------------+
|                       DOCKERFILE STRUKTUR                            |
+---------------------------------------------------------------------+
|                                                                      |
|   # Syntax och parser directive (optional, måste vara först)         |
|   # syntax=docker/dockerfile:1                                       |
|                                                                      |
|   +--------------------------------------------------------------+   |
|   |                      BASE IMAGE STAGE                         |   |
|   |  FROM python:3.11-slim AS base                                |   |
|   |  ENV PYTHONUNBUFFERED=1                                       |   |
|   +--------------------------------------------------------------+   |
|                              |                                       |
|                              v                                       |
|   +--------------------------------------------------------------+   |
|   |                    DEPENDENCIES STAGE                         |   |
|   |  FROM base AS deps                                            |   |
|   |  COPY requirements.txt .                                      |   |
|   |  RUN pip install -r requirements.txt                          |   |
|   +--------------------------------------------------------------+   |
|                              |                                       |
|                              v                                       |
|   +--------------------------------------------------------------+   |
|   |                    PRODUCTION STAGE                           |   |
|   |  FROM base AS production                                      |   |
|   |  COPY --from=deps /usr/local/lib/python3.11 ...              |   |
|   |  COPY . .                                                     |   |
|   |  USER appuser                                                 |   |
|   |  CMD ["python", "app.py"]                                     |   |
|   +--------------------------------------------------------------+   |
|                                                                      |
+---------------------------------------------------------------------+
```

### Dockerfile Instruktioner - Komplett Referens

| Instruktion | Beskrivning | Skapar Layer? | Körs vid |
|-------------|-------------|---------------|----------|
| `FROM` | Sätt base image | Ja | Build |
| `ARG` | Build-time variabel | Nej | Build |
| `ENV` | Runtime miljövariabel | Ja | Build + Run |
| `WORKDIR` | Sätt arbetskatalog | Ja | Build + Run |
| `COPY` | Kopiera filer från context | Ja | Build |
| `ADD` | Kopiera + extrahera/URL | Ja | Build |
| `RUN` | Kör kommando | Ja | Build |
| `USER` | Byt användare | Ja | Build + Run |
| `EXPOSE` | Dokumentera port | Nej | - |
| `VOLUME` | Definiera mount point | Ja | Run |
| `CMD` | Default startkommando | Nej | Run |
| `ENTRYPOINT` | Fast startkommando | Nej | Run |
| `HEALTHCHECK` | Hälsokontroll | Nej | Run |
| `LABEL` | Metadata | Ja | - |
| `STOPSIGNAL` | Shutdown-signal | Nej | Run |
| `SHELL` | Byt default shell | Nej | Build |

### Layer Caching Mekanik

```
+---------------------------------------------------------------------+
|                      LAYER CACHING                                   |
+---------------------------------------------------------------------+
|                                                                      |
|   Dockerfile                    Cache Status                         |
|   ----------                    ------------                         |
|                                                                      |
|   FROM python:3.11-slim         [CACHED] - base image finns lokalt   |
|           |                                                          |
|           v                                                          |
|   WORKDIR /app                  [CACHED] - samma som förra build     |
|           |                                                          |
|           v                                                          |
|   COPY requirements.txt .       [CACHED] - filen oförändrad          |
|           |                                                          |
|           v                                                          |
|   RUN pip install ...           [CACHED] - föregående lager cachat   |
|           |                                                          |
|           v                                                          |
|   COPY . .                      [INVALIDATED!] - kod ändrad          |
|           |                                                          |
|           v                                                          |
|   CMD ["python", "app.py"]      [REBUILD] - alla efter invalidering  |
|                                                                      |
|   VIKTIGT: När ett layer invalideras, måste alla efterföljande       |
|            layers också byggas om!                                   |
|                                                                      |
+---------------------------------------------------------------------+
```

### CMD vs ENTRYPOINT Fördjupning

| Scenario | Dockerfile | `docker run img` | `docker run img xyz` |
|----------|------------|------------------|---------------------|
| Bara CMD | `CMD ["app"]` | `app` | `xyz` (CMD ersatt) |
| Bara ENTRYPOINT | `ENTRYPOINT ["app"]` | `app` | `app xyz` |
| Båda | `ENTRYPOINT ["app"]` + `CMD ["--help"]` | `app --help` | `app xyz` |

```
+---------------------------------------------------------------------+
|                    ENTRYPOINT + CMD PATTERN                          |
+---------------------------------------------------------------------+
|                                                                      |
|   ENTRYPOINT ["python", "manage.py"]                                 |
|   CMD ["runserver", "0.0.0.0:8000"]                                  |
|                                                                      |
|   docker run myapp                                                   |
|   -> python manage.py runserver 0.0.0.0:8000                         |
|                                                                      |
|   docker run myapp migrate                                           |
|   -> python manage.py migrate                                        |
|                                                                      |
|   docker run myapp shell                                             |
|   -> python manage.py shell                                          |
|                                                                      |
|   Perfekt för CLI-verktyg som Django manage.py!                      |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa Grundläggande Dockerfile

```dockerfile
# 1. Välj base image - börja alltid med FROM
FROM python:3.11-slim

# 2. Sätt arbetskatalog
WORKDIR /app

# 3. Kopiera dependencies först (för caching)
COPY requirements.txt .

# 4. Installera dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiera applikationskod
COPY . .

# 6. Dokumentera port
EXPOSE 8000

# 7. Definiera startkommando
CMD ["python", "app.py"]
```

### Steg 2: Lägg till Säkerhet

```dockerfile
FROM python:3.11-slim

# Skapa non-root användare tidigt
RUN groupadd --gid 1000 appgroup && \\
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

WORKDIR /app

# Installera dependencies som root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera kod och sätt ownership
COPY --chown=appuser:appgroup . .

# Byt till non-root INNAN runtime
USER appuser

EXPOSE 8000
CMD ["python", "app.py"]
```

### Steg 3: Optimera för Caching

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dependencies ändras sällan - kopiera och installera först
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kod ändras ofta - kopiera sist
COPY . .

CMD ["python", "app.py"]
```

### Steg 4: Lägg till Health Check

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

# Health check för orchestrators
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "app.py"]
```

### Steg 5: Skapa .dockerignore

```bash
# .dockerignore
.git
.gitignore
.env
.env.*
__pycache__
*.pyc
*.pyo
.pytest_cache
.coverage
htmlcov/
.mypy_cache
.vscode
.idea
*.md
!README.md
Dockerfile*
docker-compose*
.dockerignore
venv/
.venv/
node_modules/
*.log
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Python FastAPI Application

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

# Prevent Python from writing bytecode and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PIP_NO_CACHE_DIR=1 \\
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Create non-root user
RUN groupadd --gid 1000 appgroup && \\
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application
COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \\
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Exempel 2: Node.js Multi-stage Build

```dockerfile
# syntax=docker/dockerfile:1

# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy source and build
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:20-alpine AS production

WORKDIR /app

# Create non-root user
RUN addgroup -g 1000 appgroup && \\
    adduser -u 1000 -G appgroup -s /bin/sh -D appuser

# Copy only necessary files from builder
COPY --from=builder --chown=appuser:appgroup /app/dist ./dist
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules
COPY --from=builder --chown=appuser:appgroup /app/package.json ./

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \\
    CMD wget -q --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/index.js"]
```

### Exempel 3: Go Application (Ultra-minimal)

```dockerfile
# syntax=docker/dockerfile:1

# Stage 1: Build
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build static binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /app/server ./cmd/server

# Stage 2: Minimal production image
FROM scratch

# Copy CA certificates for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Copy binary
COPY --from=builder /app/server /server

EXPOSE 8080

ENTRYPOINT ["/server"]
```

### Exempel 4: React Frontend med Nginx

```dockerfile
# syntax=docker/dockerfile:1

# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/

# Copy built assets
COPY --from=builder /app/dist /usr/share/nginx/html

# Non-root nginx
RUN chown -R nginx:nginx /usr/share/nginx/html && \\
    chown -R nginx:nginx /var/cache/nginx && \\
    chown -R nginx:nginx /var/log/nginx && \\
    touch /var/run/nginx.pid && \\
    chown -R nginx:nginx /var/run/nginx.pid

USER nginx

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s \\
    CMD wget -q --spider http://localhost:80 || exit 1

CMD ["nginx", "-g", "daemon off;"]
```

------------------------------------------------------------

## Bästa Praxis

### Layer Optimization

| Princip | Exempel |
|---------|---------|
| **Kombinera RUN-kommandon** | `RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*` |
| **Sortera multi-line arguments** | Alfabetisk ordning för läsbarhet |
| **Använd --no-cache-dir** | `pip install --no-cache-dir` |
| **Städa i samma layer** | Ta bort temp-filer i samma RUN |

### Security Checklist

```dockerfile
# 1. Använd specifik tag, inte latest
FROM python:3.11.7-slim  # BRA
# FROM python:latest     # DÅLIGT

# 2. Skapa och använd non-root user
RUN useradd --create-home appuser
USER appuser

# 3. Kopiera med rätt ownership
COPY --chown=appuser:appuser . .

# 4. Sätt lämpliga permissions
RUN chmod 755 /app

# 5. Undvik secrets i image
# DÅLIGT: ENV API_KEY=secret123
# BRA: Använd runtime secrets/environment
```

### Build Optimization

| Teknik | Effekt |
|--------|--------|
| **Dependencies före kod** | Cache används vid kodändringar |
| **.dockerignore** | Mindre build context, snabbare COPY |
| **Multi-stage builds** | Dramatiskt mindre images |
| **BuildKit** | Parallella builds, bättre caching |

------------------------------------------------------------

## Vanliga Fallgropar

| Fallgrop | Problem | Lösning |
|----------|---------|---------|
| **Root user** | Säkerhetsrisk | Skapa och använd non-root user |
| **latest tag** | Ej reproducerbart | Använd specifika version tags |
| **COPY . . först** | Ingen caching | Dependencies före kod |
| **Ingen .dockerignore** | Stora images, långsam build | Skapa .dockerignore |
| **Secrets i Dockerfile** | Läcker hemligheter | Använd build secrets eller runtime env |
| **ADD istället för COPY** | Oförutsägbart beteende | COPY för filer, RUN curl för URLs |

### Felsökning

```bash
# Debug build process
docker build --progress=plain -t myapp .

# Se layer-storlekar
docker history myapp

# Kör interaktivt för att debugga
docker run -it --rm myapp sh

# Bygg utan cache för att se full output
docker build --no-cache -t myapp .

# Bygg specifikt stage
docker build --target builder -t myapp-builder .
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande Dockerfile (Grundläggande)

**Uppgift:** Skapa en Dockerfile för en enkel Python Flask-applikation.

Krav:
- Base image: python:3.11-slim
- Installera Flask via requirements.txt
- Exponera port 5000
- Startkommando: flask run --host=0.0.0.0

<details>
<summary>Ledtråd</summary>

Strukturen ska vara:
1. FROM för base image
2. WORKDIR för arbetskatalog
3. COPY requirements.txt och installera
4. COPY resten av koden
5. EXPOSE för port
6. CMD för start

</details>

<details>
<summary>Lösning</summary>

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Set environment and start
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
```

```txt
# requirements.txt
flask==3.0.0
```

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker!'

@app.route('/health')
def health():
    return 'OK'
```

```bash
# Build and test
docker build -t flask-app .
docker run -d -p 5000:5000 --name myflask flask-app
curl http://localhost:5000
# Hello from Docker!

docker rm -f myflask
```

</details>

### Övning 2: Säker Production Dockerfile (Medel)

**Uppgift:** Förbättra Dockerfile från övning 1 med produktionssäkerhet.

Krav:
- Non-root user
- Health check
- Proper ownership på filer
- Gunicorn istället för Flask dev server

<details>
<summary>Ledtråd</summary>

Lägg till:
1. `useradd` för att skapa användare
2. `--chown` på COPY-kommando
3. `USER` direktiv
4. `HEALTHCHECK` direktiv
5. Gunicorn i requirements.txt

</details>

<details>
<summary>Lösning</summary>

```dockerfile
# Dockerfile
FROM python:3.11-slim

# Create non-root user
RUN groupadd --gid 1000 appgroup && \\
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy with correct ownership
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
```

```txt
# requirements.txt
flask==3.0.0
gunicorn==21.2.0
```

```bash
# Verify security
docker build -t flask-secure .
docker run -d -p 5000:5000 --name secure flask-secure

# Check user
docker exec secure whoami
# appuser

# Check health
docker inspect secure --format='{{.State.Health.Status}}'
# healthy (efter ~35 sekunder)

docker rm -f secure
```

</details>

### Övning 3: Multi-stage Build (Avancerad)

**Uppgift:** Skapa en multi-stage Dockerfile för en TypeScript Node.js-applikation.

Krav:
- Stage 1 (builder): Kompilera TypeScript till JavaScript
- Stage 2 (production): Minimal image med bara compiled code
- Jämför storlek med single-stage build
- Non-root user i production stage

<details>
<summary>Ledtråd</summary>

Stage 1:
- FROM node:20 (för att bygga)
- npm ci, npm run build

Stage 2:
- FROM node:20-alpine (minimal)
- COPY --from=builder för dist och node_modules
- Skapa user och byt till den

</details>

<details>
<summary>Lösning</summary>

```json
// package.json
{
  "name": "ts-app",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.0",
    "typescript": "^5.3.2"
  }
}
```

```typescript
// src/index.ts
import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from TypeScript!');
});

app.get('/health', (req, res) => {
  res.send('OK');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*"]
}
```

```dockerfile
# Dockerfile.multistage
# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY tsconfig.json ./
COPY src ./src

RUN npm run build

# Stage 2: Production
FROM node:20-alpine AS production

WORKDIR /app

# Create non-root user
RUN addgroup -g 1000 appgroup && \\
    adduser -u 1000 -G appgroup -s /bin/sh -D appuser

# Copy only production dependencies
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Copy compiled code
COPY --from=builder /app/dist ./dist

# Set ownership
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \\
    CMD wget -q --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/index.js"]
```

```dockerfile
# Dockerfile.single (för jämförelse)
FROM node:20

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY tsconfig.json ./
COPY src ./src
RUN npm run build

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

```bash
# Build both versions
docker build -f Dockerfile.single -t ts-single .
docker build -f Dockerfile.multistage -t ts-multi .

# Compare sizes
docker images | grep ts-
# ts-single    latest    xxxMB (ca 1GB+)
# ts-multi     latest    xxxMB (ca 150MB)

# Size reduction: ~85%!

# Test multi-stage
docker run -d -p 3000:3000 --name ts ts-multi
curl http://localhost:3000
# Hello from TypeScript!

docker rm -f ts
```

</details>

------------------------------------------------------------

## Kopplingar

| Ämne | Koppling |
|------|----------|
| **Docker Images** | Dockerfile producerar images |
| **CI/CD** | Automatiska builds från Dockerfile |
| **Security** | CVE scanning av images, non-root execution |
| **Kubernetes** | Images deployade i pods |
| **Registry** | Push/pull av byggda images |

### DevOps Pipeline Integration

```
+---------------------------------------------------------------------+
|                       CI/CD PIPELINE                                 |
+---------------------------------------------------------------------+
|                                                                      |
|   [Git Push] --> [CI Server] --> [Docker Build] --> [Push Registry] |
|                       |               |                   |          |
|                       v               v                   v          |
|                   Lint          Multi-stage          Tag with        |
|                   Dockerfile    Build               commit SHA       |
|                                     |                   |            |
|                                     v                   v            |
|                               Scan for CVEs      Deploy to K8s       |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

### Centrala Koncept

| Koncept | Huvudpoäng |
|---------|------------|
| **Layer Caching** | Ordning spelar roll - dependencies före kod |
| **Multi-stage** | Separera build och runtime för mindre images |
| **Security** | Non-root users, specifika tags, inga secrets |
| **Instruktioner** | Förstå skillnaden mellan CMD/ENTRYPOINT, COPY/ADD |

### Viktiga Insikter

1. **Varje instruktion kan skapa ett layer** - minimera och kombinera klokt
2. **Cache invalideras kaskadvis** - ändras ett layer, byggs alla efter om
3. **Multi-stage builds är standard** för production images
4. **Säkerhet börjar i Dockerfile** - non-root är inte optional

------------------------------------------------------------

## Nyckelkommandon

### Dockerfile Instruktioner

| Instruktion | Syntax | Användning |
|-------------|--------|------------|
| `FROM` | `FROM image:tag AS name` | Base image |
| `WORKDIR` | `WORKDIR /app` | Sätt arbetskatalog |
| `COPY` | `COPY [--chown=user] src dst` | Kopiera filer |
| `RUN` | `RUN command` | Kör vid build |
| `ENV` | `ENV KEY=value` | Miljövariabel |
| `ARG` | `ARG NAME=default` | Build-argument |
| `EXPOSE` | `EXPOSE port` | Dokumentera port |
| `USER` | `USER username` | Byt användare |
| `HEALTHCHECK` | `HEALTHCHECK CMD ...` | Hälsokontroll |
| `CMD` | `CMD ["exec", "arg"]` | Default start |
| `ENTRYPOINT` | `ENTRYPOINT ["exec"]` | Fast start |

### Build-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker build -t name:tag .` | Bygg image |
| `docker build -f Dockerfile.prod .` | Specifik fil |
| `docker build --target stage .` | Bygg till stage |
| `docker build --no-cache .` | Utan cache |
| `docker build --progress=plain .` | Verbose output |
| `docker history image` | Visa layers |
| `DOCKER_BUILDKIT=1 docker build .` | Använd BuildKit |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Multi-stage Builds](https://docs.docker.com/build/building/multi-stage/)

**Fördjupning:**
- [BuildKit Documentation](https://docs.docker.com/build/buildkit/)
- [Docker Security Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

**Verktyg:**
- [Hadolint - Dockerfile Linter](https://github.com/hadolint/hadolint)
- [Dive - Image Layer Explorer](https://github.com/wagoodman/dive)
- [Trivy - Vulnerability Scanner](https://github.com/aquasecurity/trivy)
""",
        },
        {
            "title": "Docker Networking",
            "slug": "docker-networking",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 90,
            "content": """# Docker Networking

------------------------------------------------------------

## Introduktion

Nätverk är livsnerven i containeriserade applikationer. I en microservices-arkitektur måste dussintals tjänster kommunicera effektivt och säkert med varandra. Docker Networking ger dig verktygen att isolera, koppla samman och säkra kommunikationen mellan containers.

Att förstå Docker-nätverk är avgörande för att bygga robusta, säkra och skalbara applikationer. Rätt nätverkskonfiguration kan förhindra säkerhetsincidenter, förbättra prestanda och förenkla service discovery.

**I denna modul lär du dig:**
- Förstå de olika nätverksdrivrutinerna och deras användningsfall
- Skapa och hantera Docker-nätverk för container-kommunikation
- Implementera service discovery med inbyggd DNS
- Konfigurera port mapping för extern åtkomst
- Designa säkra nätverkstopologier för produktion

**Förkunskapskrav:**
- Container Lifecycle Management (Node 3)
- Grundläggande nätverkskunskap (TCP/IP, portar, DNS)
- Terminal/kommandoradsvana

------------------------------------------------------------

## Teori

### Varför viktigt för DevOps?

| Scenario | Varför Docker Networking är kritiskt |
|----------|-------------------------------------|
| **Microservices** | Tjänster måste hitta och kommunicera med varandra |
| **Säkerhet** | Isolera databaser och känsliga tjänster från internet |
| **Service Discovery** | Automatisk DNS-upplösning mellan containers |
| **Zero-downtime deploys** | Load balancing och rolling updates |
| **Multi-environment** | Separera dev/staging/prod-nätverk |

### Docker Networking Architecture

```
+---------------------------------------------------------------------+
|                    DOCKER NETWORKING OVERVIEW                        |
+---------------------------------------------------------------------+
|                                                                      |
|   +-----------------------+     +-----------------------+            |
|   |    BRIDGE NETWORK     |     |     HOST NETWORK      |            |
|   |   (Default/Custom)    |     |   (No isolation)      |            |
|   +-----------------------+     +-----------------------+            |
|   |                       |     |                       |            |
|   |  +-----+   +-----+    |     |  Container uses       |            |
|   |  | C1  |   | C2  |    |     |  host's network       |            |
|   |  +--+--+   +--+--+    |     |  stack directly       |            |
|   |     |         |       |     |                       |            |
|   |     +----+----+       |     +-----------------------+            |
|   |          |            |                                          |
|   |     [docker0]         |     +-----------------------+            |
|   |          |            |     |     NONE NETWORK      |            |
|   +-----------+-----------+     |   (Total isolation)   |            |
|               |                 +-----------------------+            |
|               v                                                      |
|        [Host Network]           +-----------------------+            |
|               |                 |   OVERLAY NETWORK     |            |
|               v                 |   (Multi-host)        |            |
|          Internet               +-----------------------+            |
|                                                                      |
+---------------------------------------------------------------------+
```

### Network Drivers Förklarade

| Driver | Beskrivning | Isolation | Användning |
|--------|-------------|-----------|------------|
| **bridge** | Virtuellt nätverk på en host | Hög | Default för standalone containers |
| **host** | Container delar hosts nätverksstack | Ingen | Performance-kritiska applikationer |
| **none** | Ingen nätverksåtkomst | Total | Säkerhetskritiska jobb |
| **overlay** | Spänner över flera Docker-hosts | Hög | Swarm/Kubernetes |
| **macvlan** | Tilldelar MAC-adress, visas som fysisk enhet | Medium | Legacy-integration |

### Bridge Network Anatomy

```
+---------------------------------------------------------------------+
|                      BRIDGE NETWORK INTERNALS                        |
+---------------------------------------------------------------------+
|                                                                      |
|   Host Machine                                                       |
|   +---------------------------------------------------------------+  |
|   |                                                               |  |
|   |   Bridge: myapp-net (172.18.0.0/16)                           |  |
|   |   +-------------------------------------------------------+   |  |
|   |   |                                                       |   |  |
|   |   |   +-------------+       +-------------+               |   |  |
|   |   |   |   webapp    |       |   database  |               |   |  |
|   |   |   | 172.18.0.2  |       | 172.18.0.3  |               |   |  |
|   |   |   |   :8000     |       |   :5432     |               |   |  |
|   |   |   +------+------+       +------+------+               |   |  |
|   |   |          |                     |                      |   |  |
|   |   |          |     DNS: "database" |                      |   |  |
|   |   |          +-------resolves------+                      |   |  |
|   |   |                    to                                 |   |  |
|   |   |               172.18.0.3                              |   |  |
|   |   |                                                       |   |  |
|   |   +-------------------------------------------------------+   |  |
|   |                            |                                  |  |
|   |   iptables NAT        [docker0]                               |  |
|   |   (port mapping)           |                                  |  |
|   |                            v                                  |  |
|   +---------------------------------------------------------------+  |
|                                |                                     |
|                          [eth0: Host IP]                             |
|                                |                                     |
|                            Internet                                  |
|                                                                      |
+---------------------------------------------------------------------+
```

### DNS Resolution i Docker

```
+---------------------------------------------------------------------+
|                       DOCKER DNS                                     |
+---------------------------------------------------------------------+
|                                                                      |
|   Container: webapp                                                  |
|   +---------------------------------------------------------------+  |
|   |                                                               |  |
|   |   Application code:                                           |  |
|   |   db = psycopg2.connect(host="database", port=5432)           |  |
|   |                                                               |  |
|   |   1. App asks for "database"                                  |  |
|   |      |                                                        |  |
|   |      v                                                        |  |
|   |   2. Docker's embedded DNS (127.0.0.11)                       |  |
|   |      |                                                        |  |
|   |      v                                                        |  |
|   |   3. Looks up containers in same network                      |  |
|   |      |                                                        |  |
|   |      v                                                        |  |
|   |   4. Returns 172.18.0.3 (database container IP)               |  |
|   |      |                                                        |  |
|   |      v                                                        |  |
|   |   5. Connection established!                                  |  |
|   |                                                               |  |
|   +---------------------------------------------------------------+  |
|                                                                      |
|   VIKTIGT: DNS fungerar BARA i user-defined networks,                |
|            INTE i default "bridge" network!                          |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa ett User-Defined Network

```bash
# Skapa bridge-nätverk
docker network create myapp-network

# Verifiera
docker network ls
# NETWORK ID     NAME             DRIVER    SCOPE
# abc123def456   myapp-network    bridge    local
```

### Steg 2: Starta Containers i Nätverket

```bash
# Starta databas i nätverket
docker run -d \\
    --name database \\
    --network myapp-network \\
    -e POSTGRES_PASSWORD=secret \\
    postgres:15-alpine

# Starta applikation som behöver databasen
docker run -d \\
    --name webapp \\
    --network myapp-network \\
    -e DATABASE_HOST=database \\
    -e DATABASE_PORT=5432 \\
    myapp:latest
```

### Steg 3: Verifiera Kommunikation

```bash
# Testa DNS-upplösning
docker exec webapp ping -c 3 database
# PING database (172.18.0.2): 56 data bytes
# 64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.089 ms

# Testa port connectivity
docker exec webapp nc -zv database 5432
# database (172.18.0.2:5432) open
```

### Steg 4: Exponera Webapp till Internet

```bash
# Stoppa och ta bort webapp
docker rm -f webapp

# Starta med port mapping
docker run -d \\
    --name webapp \\
    --network myapp-network \\
    -e DATABASE_HOST=database \\
    -p 8080:8000 \\
    myapp:latest

# Nu nåbar på http://localhost:8080
```

### Steg 5: Inspektera Nätverket

```bash
# Se alla containers i nätverket
docker network inspect myapp-network

# Output visar:
# - Subnet: 172.18.0.0/16
# - Gateway: 172.18.0.1
# - Containers: database (172.18.0.2), webapp (172.18.0.3)
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Microservices Architecture

```
+---------------------------------------------------------------------+
|                 MICROSERVICES NETWORK TOPOLOGY                       |
+---------------------------------------------------------------------+
|                                                                      |
|   Internet                                                           |
|       |                                                              |
|       | :80, :443                                                    |
|       v                                                              |
|   +-------+                                                          |
|   | nginx | (reverse proxy)                                          |
|   +---+---+                                                          |
|       |                                                              |
|       +------------+-----------+                                     |
|       |            |           |                                     |
|       v            v           v                                     |
|   +-------+    +-------+   +-------+                                 |
|   |  api  |    |  web  |   | admin |                                 |
|   +---+---+    +-------+   +-------+                                 |
|       |                                                              |
|       +------------+------------+                                    |
|       |            |            |                                    |
|       v            v            v                                    |
|   +-------+    +-------+    +-------+                                |
|   |  db   |    | redis |    | queue |                                |
|   +-------+    +-------+    +-------+                                |
|                                                                      |
+---------------------------------------------------------------------+
```

```bash
# Skapa separata nätverk för olika tiers
docker network create frontend-net
docker network create backend-net

# Frontend tier (exponerad)
docker run -d --name nginx --network frontend-net -p 80:80 -p 443:443 nginx
docker run -d --name web --network frontend-net mywebapp
docker run -d --name admin --network frontend-net myadmin

# Backend tier (isolerad)
docker run -d --name api --network backend-net myapi
docker run -d --name db --network backend-net postgres
docker run -d --name redis --network backend-net redis
docker run -d --name queue --network backend-net rabbitmq

# Koppla api till båda nätverken
docker network connect frontend-net api

# Nu kan:
# - nginx prata med web, admin, api
# - api prata med db, redis, queue
# - db INTE prata med nginx (säkert!)
```

### Exempel 2: Development vs Production Isolation

```bash
# Development network
docker network create dev-net
docker run -d --name dev-db --network dev-net -p 5432:5432 postgres
docker run -d --name dev-app --network dev-net -p 3000:3000 myapp

# Production network (isolerad)
docker network create prod-net
docker run -d --name prod-db --network prod-net postgres  # Ingen port!
docker run -d --name prod-app --network prod-net -p 80:3000 myapp

# Dev och prod kan ALDRIG prata med varandra
```

### Exempel 3: Debugging Network Issues

```bash
# Starta debug-container i samma nätverk
docker run -it --rm \\
    --name debugger \\
    --network myapp-network \\
    nicolaka/netshoot

# Inne i debug-containern:
# nslookup database
# ping database
# traceroute database
# nc -zv database 5432
# curl -v http://api:8000/health
# tcpdump -i eth0
```

### Exempel 4: Host Network för Performance

```bash
# Använd host network för nätverkskritiska applikationer
docker run -d \\
    --name fast-proxy \\
    --network host \\
    nginx

# Container lyssnar direkt på host:80
# Ingen NAT overhead
# Men: ingen port isolation!
```

------------------------------------------------------------

## Bästa Praxis

### Nätverksdesign

| Princip | Implementation |
|---------|---------------|
| **Principle of Least Privilege** | Skapa separata nätverk per tier |
| **Exponera minimalt** | Bara frontend-portar till internet |
| **Namnkonventioner** | `projekt-tier-net` (ex: `myapp-backend-net`) |
| **Dokumentera** | Kommentera nätverkstopologi |

### Säkerhet

```bash
# DÅLIGT: Allt i samma nätverk
docker run -d --name db -p 5432:5432 postgres  # DB exponerad!

# BRA: Separata nätverk, DB isolerad
docker network create backend-net
docker run -d --name db --network backend-net postgres
docker run -d --name api --network backend-net -p 8080:8000 myapi
```

### Port Mapping Best Practices

| Pattern | Exempel | Användning |
|---------|---------|------------|
| **Localhost only** | `-p 127.0.0.1:5432:5432` | Development, admin-verktyg |
| **Specific interface** | `-p 10.0.0.1:8080:80` | Multi-homed hosts |
| **Random port** | `-p 80` | Dynamiska miljöer |
| **Standard port** | `-p 80:80` | Production web |

------------------------------------------------------------

## Vanliga Fallgropar

| Fallgrop | Problem | Lösning |
|----------|---------|---------|
| **Default bridge** | Ingen DNS | Använd user-defined network |
| **Exponera databas** | Säkerhetsrisk | Aldrig `-p` på databas |
| **Hardcodade IPs** | Bräckligt | Använd container-namn (DNS) |
| **Glömma network** | Container isolerad | `--network` vid `docker run` |
| **Port konflikter** | Port redan i bruk | Välj annan host-port |

### Felsökning

```bash
# "Cannot resolve hostname"
# Orsak: Containers i olika nätverk
docker network connect same-network container1

# "Connection refused"
# Orsak: Tjänsten körs inte eller fel port
docker exec container netstat -tlnp
docker logs container

# "Port already in use"
# Orsak: Annan process på porten
lsof -i :8080
docker run -p 8081:80 nginx  # Byt host-port

# Generell debug
docker network inspect network-name
docker exec container ip addr
docker exec container cat /etc/resolv.conf
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande Nätverkskonfiguration (Grundläggande)

**Uppgift:** Skapa ett nätverk och starta två containers som kan prata med varandra.

1. Skapa ett bridge-nätverk kallat "test-net"
2. Starta en nginx-container i nätverket
3. Starta en alpine-container i samma nätverk
4. Från alpine, ping nginx via container-namn

<details>
<summary>Ledtråd</summary>

Använd:
- `docker network create` för att skapa nätverk
- `--network` flaggan vid `docker run`
- `docker exec` för att köra ping

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Skapa nätverk
docker network create test-net

# 2. Starta nginx
docker run -d --name webserver --network test-net nginx:alpine

# 3. Starta alpine
docker run -d --name tester --network test-net alpine:3.19 sleep 3600

# 4. Ping från alpine till nginx
docker exec tester ping -c 3 webserver
# PING webserver (172.18.0.2): 56 data bytes
# 64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.078 ms
# 64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.095 ms
# 64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.091 ms

# Bonus: Testa HTTP
docker exec tester wget -qO- http://webserver:80
# <!DOCTYPE html>...

# Städa upp
docker rm -f webserver tester
docker network rm test-net
```

</details>

### Övning 2: Multi-tier Arkitektur (Medel)

**Uppgift:** Implementera en säker multi-tier arkitektur med frontend och backend nätverk.

Krav:
- Frontend-nätverk med nginx (exponerad på port 8080)
- Backend-nätverk med Redis
- API-server som finns i båda nätverken
- Verifiera att nginx INTE kan nå Redis direkt

<details>
<summary>Ledtråd</summary>

1. Skapa två nätverk: frontend-net och backend-net
2. Nginx i frontend-net
3. Redis i backend-net
4. API-server i backend-net, sedan connect till frontend-net
5. Testa med `docker exec nginx ping redis` (ska misslyckas)

</details>

<details>
<summary>Lösning</summary>

```bash
# Skapa nätverk
docker network create frontend-net
docker network create backend-net

# Backend tier (isolerat)
docker run -d --name redis --network backend-net redis:alpine

# API i backend först
docker run -d --name api --network backend-net \\
    -e REDIS_HOST=redis \\
    alpine:3.19 sleep 3600

# Koppla API till frontend också
docker network connect frontend-net api

# Frontend tier (exponerad)
docker run -d --name nginx --network frontend-net \\
    -p 8080:80 nginx:alpine

# Verifiera: API kan nå redis
docker exec api ping -c 2 redis
# PING redis (172.19.0.2): 56 data bytes - SUCCESS

# Verifiera: Nginx kan nå API
docker exec nginx ping -c 2 api
# PING api (172.18.0.2): 56 data bytes - SUCCESS

# Verifiera: Nginx KAN INTE nå redis (säkert!)
docker exec nginx ping -c 2 redis 2>&1
# ping: bad address 'redis' - EXPECTED!

# Verifiera nätverkstopologi
echo "=== Frontend Network ==="
docker network inspect frontend-net --format='{{range .Containers}}{{.Name}} {{end}}'
# nginx api

echo "=== Backend Network ==="
docker network inspect backend-net --format='{{range .Containers}}{{.Name}} {{end}}'
# redis api

# Städa upp
docker rm -f nginx api redis
docker network rm frontend-net backend-net
```

</details>

### Övning 3: Network Troubleshooting (Avancerad)

**Uppgift:** Diagnostisera och fixa ett nätverksproblem.

Scenario: Du har följande setup men webapp kan inte ansluta till database:

```bash
docker network create broken-net
docker run -d --name database postgres:15-alpine
docker run -d --name webapp --network broken-net alpine sleep 3600
```

Uppgift:
1. Identifiera problemet
2. Fixa det utan att ta bort containers
3. Verifiera att det fungerar

<details>
<summary>Ledtråd</summary>

Problemet är att `database` inte startades med `--network broken-net`.
Lösning: `docker network connect` kan lägga till container till nätverk i efterhand.

</details>

<details>
<summary>Lösning</summary>

```bash
# Setup (kör detta först)
docker network create broken-net
docker run -d --name database -e POSTGRES_PASSWORD=secret postgres:15-alpine
docker run -d --name webapp --network broken-net alpine:3.19 sleep 3600

# 1. Identifiera problemet
echo "=== Checking webapp's network ==="
docker inspect webapp --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'
# broken-net

echo "=== Checking database's network ==="
docker inspect database --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'
# bridge  (PROBLEM! Inte samma nätverk!)

echo "=== Testing connectivity ==="
docker exec webapp ping -c 1 database 2>&1
# ping: bad address 'database'  (MISSLYCKAS!)

# 2. Fixa problemet - koppla database till rätt nätverk
docker network connect broken-net database

# 3. Verifiera
echo "=== After fix ==="
docker inspect database --format='{{range $k, $v := .NetworkSettings.Networks}}{{$k}} {{end}}'
# bridge broken-net  (Nu i båda!)

docker exec webapp ping -c 3 database
# PING database (172.20.0.3): 56 data bytes
# 64 bytes from 172.20.0.3: seq=0 ttl=64 time=0.098 ms

# Bonus: Verifiera postgres-anslutning
docker exec webapp sh -c "apk add --no-cache postgresql-client && pg_isready -h database -p 5432"
# database:5432 - accepting connections

# Städa upp
docker rm -f database webapp
docker network rm broken-net
```

</details>

------------------------------------------------------------

## Kopplingar

| Ämne | Koppling |
|------|----------|
| **Docker Compose** | Nätverk definieras deklarativt i docker-compose.yml |
| **Kubernetes** | Pod networking, Services, Ingress |
| **Service Mesh** | Istio, Linkerd för avancerad traffic management |
| **Load Balancing** | Traefik, nginx för routing till containers |
| **Security** | Network policies, firewalls |

### Nästa steg i din DevOps-resa

```
+---------------------------------------------------------------------+
|                     NETWORKING LEARNING PATH                         |
+---------------------------------------------------------------------+
|                                                                      |
|   [Du är här]                                                        |
|        |                                                             |
|        v                                                             |
|   Docker Networking --> Docker Compose --> Container Orchestration   |
|        |                     |                    |                  |
|        v                     v                    v                  |
|   Network Security     Multi-container      Kubernetes Networking    |
|        |                   Apps                   |                  |
|        v                     |                    v                  |
|   Service Mesh <-------------+--------------> Ingress Controllers    |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

### Centrala Koncept

| Koncept | Huvudpoäng |
|---------|------------|
| **Bridge Network** | Default för container-till-container kommunikation |
| **DNS** | Container-namn resolvas automatiskt i user-defined networks |
| **Port Mapping** | `-p host:container` för extern åtkomst |
| **Network Isolation** | Separata nätverk för säkerhet |

### Viktiga Insikter

1. **Använd alltid user-defined networks** - default bridge saknar DNS
2. **Exponera aldrig databaser** - håll dem i isolerade nätverk
3. **Container-namn är DNS-namn** - hardkoda inte IP-adresser
4. **Containers kan vara i flera nätverk** - för multi-tier arkitektur

------------------------------------------------------------

## Nyckelkommandon

### Network Management

| Kommando | Beskrivning |
|----------|-------------|
| `docker network create name` | Skapa nätverk |
| `docker network ls` | Lista alla nätverk |
| `docker network inspect name` | Visa detaljer |
| `docker network rm name` | Ta bort nätverk |
| `docker network prune` | Ta bort oanvända |

### Container Network Operations

| Kommando | Beskrivning |
|----------|-------------|
| `docker run --network name ...` | Starta i specifikt nätverk |
| `docker network connect net container` | Koppla till nätverk |
| `docker network disconnect net container` | Koppla från nätverk |

### Port Mapping

| Kommando | Beskrivning |
|----------|-------------|
| `-p 8080:80` | Map host:8080 till container:80 |
| `-p 127.0.0.1:8080:80` | Bara localhost |
| `-p 80` | Random host port |
| `docker port container` | Visa port mappings |

### Debugging

| Kommando | Beskrivning |
|----------|-------------|
| `docker exec c1 ping c2` | Testa connectivity |
| `docker exec c1 nslookup c2` | Testa DNS |
| `docker network inspect net` | Se containers i nätverk |
| `docker inspect --format` | Filtrera output |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Docker Networking Overview](https://docs.docker.com/network/)
- [Bridge Network Driver](https://docs.docker.com/network/bridge/)
- [Use Host Networking](https://docs.docker.com/network/host/)

**Fördjupning:**
- [Container Networking Deep Dive](https://docs.docker.com/config/containers/container-networking/)
- [Docker Network Security](https://docs.docker.com/engine/security/)

**Verktyg:**
- [netshoot - Network Troubleshooting](https://github.com/nicolaka/netshoot)
- [Weave Net - Multi-host Networking](https://github.com/weaveworks/weave)
""",
        },
        {
            "title": "Docker Volumes & Persistence",
            "slug": "docker-volumes-persistence",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Volumes & Persistence

------------------------------------------------------------

## Introduktion

Data är livsnerven i de flesta applikationer, men containers är designade att vara ephemeral - när en container tas bort, försvinner all data inuti den. Docker Volumes löser detta fundamentala problem genom att erbjuda persistent lagring som överlever container-livscykeln.

För DevOps-ingenjörer är förståelsen av Docker-lagring kritisk. Databaser, användaruppladdningar, cache-filer och konfiguration - allt måste hanteras korrekt för att undvika dataförlust och möjliggöra skalning.

**I denna modul lär du dig:**
- Förstå skillnaden mellan container-lagring och persistent lagring
- Använda volumes för produktionsmiljöer
- Implementera bind mounts för utveckling
- Genomföra backup och restore av Docker-data
- Designa datastrategier för containeriserade applikationer

**Förkunskapskrav:**
- Container Lifecycle Management (Node 3)
- Grundläggande filsystemskunskap
- Terminal/kommandoradsvana

------------------------------------------------------------

## Teori

### Varför viktigt för DevOps?

| Scenario | Varför Volumes är kritiskt |
|----------|---------------------------|
| **Databaser** | Data måste överleva container restarts och updates |
| **Stateful Applications** | User uploads, sessions, generated content |
| **Development Workflow** | Hot reload utan rebuild |
| **Disaster Recovery** | Backup och restore-strategier |
| **Microservices** | Delad state mellan services |

### Container Storage Architecture

```
+---------------------------------------------------------------------+
|                    CONTAINER STORAGE LAYERS                          |
+---------------------------------------------------------------------+
|                                                                      |
|   Container                                                          |
|   +---------------------------------------------------------------+  |
|   |                     Writable Layer (R/W)                      |  |
|   |   Ändringar här FÖRSVINNER när containern tas bort!           |  |
|   +---------------------------------------------------------------+  |
|   |                     Image Layer 3 (R/O)                       |  |
|   +---------------------------------------------------------------+  |
|   |                     Image Layer 2 (R/O)                       |  |
|   +---------------------------------------------------------------+  |
|   |                     Image Layer 1 (R/O)                       |  |
|   +---------------------------------------------------------------+  |
|                                                                      |
|   PROBLEM: Alla ändringar i Writable Layer försvinner!               |
|                                                                      |
|   LÖSNING: Docker Volumes                                            |
|                                                                      |
|   +---------------------------------------------------------------+  |
|   |                     Container                                 |  |
|   |   +-------------+                                             |  |
|   |   | /app/data   | <----- VOLUME (persistent!)                 |  |
|   |   +-------------+          |                                  |  |
|   +---------------------------------------------------------------+  |
|                                |                                     |
|                                v                                     |
|   +---------------------------------------------------------------+  |
|   |                Docker Volume (on host)                        |  |
|   |   /var/lib/docker/volumes/mydata/_data                        |  |
|   |   Data ÖVERLEVER container lifecycle!                         |  |
|   +---------------------------------------------------------------+  |
|                                                                      |
+---------------------------------------------------------------------+
```

### De Tre Lagringstyper

| Typ | Beskrivning | Syntax | Användning |
|-----|-------------|--------|------------|
| **Volumes** | Docker-managed storage | `-v mydata:/app/data` | Produktion, databaser |
| **Bind Mounts** | Host-katalog monteras | `-v /host/path:/container/path` | Utveckling, config |
| **tmpfs** | RAM-baserad temporär lagring | `--tmpfs /tmp` | Secrets, temp-filer |

```
+---------------------------------------------------------------------+
|                    STORAGE TYPE COMPARISON                           |
+---------------------------------------------------------------------+
|                                                                      |
|   VOLUMES                BIND MOUNTS              TMPFS              |
|   +--------+             +--------+               +--------+         |
|   | Volume |             | Host   |               |  RAM   |         |
|   | Driver |             | Path   |               | Memory |         |
|   +---+----+             +---+----+               +---+----+         |
|       |                      |                       |               |
|       v                      v                       v               |
|   Docker Area            Any Host Dir           Container Memory     |
|   /var/lib/docker/       /home/user/code        (Försvinner)         |
|   volumes/...                                                        |
|                                                                      |
|   BEST FOR:              BEST FOR:               BEST FOR:           |
|   - Databases            - Development           - Secrets           |
|   - Uploads              - Config files          - Session data      |
|   - Cache                - Source code           - Temp files        |
|   - Shared data          - Logs                                      |
|                                                                      |
+---------------------------------------------------------------------+
```

### Volume Lifecycle

```
+---------------------------------------------------------------------+
|                       VOLUME LIFECYCLE                               |
+---------------------------------------------------------------------+
|                                                                      |
|   docker volume create dbdata                                        |
|        |                                                             |
|        v                                                             |
|   +-----------+                                                      |
|   |  CREATED  | -----> Volume existerar på host                      |
|   +-----------+                                                      |
|        |                                                             |
|        | docker run -v dbdata:/data ...                              |
|        v                                                             |
|   +-----------+                                                      |
|   |  IN USE   | -----> Monterad i container                          |
|   +-----------+                                                      |
|        |                                                             |
|        | docker rm container                                         |
|        v                                                             |
|   +-----------+                                                      |
|   | AVAILABLE | -----> Container borta, volume finns kvar!           |
|   +-----------+                                                      |
|        |                                                             |
|        | docker volume rm dbdata                                     |
|        v                                                             |
|   +-----------+                                                      |
|   |  DELETED  | -----> Data permanent borta                          |
|   +-----------+                                                      |
|                                                                      |
|   VIKTIGT: docker rm tar INTE bort volumes automatiskt               |
|            (om inte --volumes flaggan används)                       |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa och Använda en Volume

```bash
# Skapa en named volume
docker volume create myapp-data

# Verifiera
docker volume ls
# DRIVER    VOLUME NAME
# local     myapp-data

# Inspektera volume
docker volume inspect myapp-data
```

### Steg 2: Montera Volume i Container

```bash
# Starta container med volume
docker run -d \\
    --name myapp \\
    -v myapp-data:/app/data \\
    alpine sh -c "while true; do date >> /app/data/log.txt; sleep 5; done"

# Verifiera data
docker exec myapp cat /app/data/log.txt
```

### Steg 3: Testa Persistence

```bash
# Ta bort container
docker rm -f myapp

# Starta ny container med samma volume
docker run -d \\
    --name myapp-new \\
    -v myapp-data:/app/data \\
    alpine cat /app/data/log.txt

# Data finns kvar!
docker logs myapp-new
```

### Steg 4: Använd Bind Mount för Utveckling

```bash
# Montera lokal katalog
docker run -d \\
    --name dev-server \\
    -v $(pwd)/src:/app/src \\
    -p 3000:3000 \\
    node:20-alpine npm run dev

# Ändringar i ./src syns direkt i containern
```

### Steg 5: Read-Only Mount för Säkerhet

```bash
# Config-filer som containern inte ska kunna ändra
docker run -d \\
    --name app \\
    -v $(pwd)/config:/app/config:ro \\
    myapp
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: PostgreSQL med Persistent Data

```bash
# Skapa volume för databasdata
docker volume create postgres-data

# Starta PostgreSQL
docker run -d \\
    --name postgres \\
    -v postgres-data:/var/lib/postgresql/data \\
    -e POSTGRES_USER=admin \\
    -e POSTGRES_PASSWORD=secret \\
    -e POSTGRES_DB=myapp \\
    postgres:15-alpine

# Skapa testdata
docker exec -it postgres psql -U admin -d myapp -c \\
    "CREATE TABLE users (id SERIAL, name VARCHAR(100)); INSERT INTO users (name) VALUES ('Alice');"

# Verifiera
docker exec postgres psql -U admin -d myapp -c "SELECT * FROM users;"
#  id | name
# ----+-------
#   1 | Alice

# Ta bort container och skapa ny
docker rm -f postgres
docker run -d \\
    --name postgres-new \\
    -v postgres-data:/var/lib/postgresql/data \\
    postgres:15-alpine

# Data överlevde!
docker exec postgres-new psql -U admin -d myapp -c "SELECT * FROM users;"
```

### Exempel 2: Development Environment med Hot Reload

```bash
# Python Flask med auto-reload
docker run -d \\
    --name flask-dev \\
    -v $(pwd):/app \\
    -w /app \\
    -p 5000:5000 \\
    -e FLASK_ENV=development \\
    python:3.11-slim \\
    sh -c "pip install flask && flask run --host=0.0.0.0"

# Node.js med nodemon
docker run -d \\
    --name node-dev \\
    -v $(pwd):/app \\
    -w /app \\
    -p 3000:3000 \\
    node:20-alpine \\
    sh -c "npm install && npm run dev"
```

### Exempel 3: Backup och Restore

```bash
# Backup volume till tar-fil
docker run --rm \\
    -v postgres-data:/source:ro \\
    -v $(pwd)/backups:/backup \\
    alpine tar czf /backup/postgres-$(date +%Y%m%d).tar.gz -C /source .

# Restore från backup
docker volume create postgres-restored

docker run --rm \\
    -v postgres-restored:/target \\
    -v $(pwd)/backups:/backup \\
    alpine tar xzf /backup/postgres-20240101.tar.gz -C /target
```

### Exempel 4: Shared Volume mellan Containers

```bash
# Skapa shared volume
docker volume create shared-logs

# App skriver loggar
docker run -d \\
    --name app \\
    -v shared-logs:/var/log/app \\
    alpine sh -c "while true; do echo $(date) >> /var/log/app/app.log; sleep 10; done"

# Log collector läser loggar
docker run -d \\
    --name log-collector \\
    -v shared-logs:/logs:ro \\
    alpine tail -f /logs/app.log
```

------------------------------------------------------------

## Bästa Praxis

### Volume Naming Conventions

| Pattern | Exempel | Användning |
|---------|---------|------------|
| `{project}-{service}-data` | `myapp-postgres-data` | Databasdata |
| `{project}-{service}-config` | `myapp-nginx-config` | Konfiguration |
| `{project}-shared` | `myapp-shared` | Delad data |

### Vanliga Mount Points per Image

| Image | Data Path | Beskrivning |
|-------|-----------|-------------|
| `postgres` | `/var/lib/postgresql/data` | Databasdata |
| `mysql` | `/var/lib/mysql` | Databasdata |
| `mongodb` | `/data/db` | Databasdata |
| `redis` | `/data` | RDB/AOF-filer |
| `elasticsearch` | `/usr/share/elasticsearch/data` | Index-data |
| `nginx` | `/etc/nginx/conf.d` | Config |

### Backup Strategy

| Frekvens | Typ | Retention |
|----------|-----|-----------|
| Dagligen | Full backup | 7 dagar |
| Veckovis | Full backup | 4 veckor |
| Månatligen | Full backup | 12 månader |

------------------------------------------------------------

## Vanliga Fallgropar

| Fallgrop | Problem | Lösning |
|----------|---------|---------|
| **Glömmer volume** | Data förloras | Alltid `-v` för stateful apps |
| **Permission denied** | UID mismatch host/container | `--user` eller fixar permissions |
| **Volume ej borttagen** | Disk full | `docker volume prune` regelbundet |
| **Bind mount path** | Relativ sökväg | Använd `$(pwd)` eller absolut path |
| **:ro glömd** | Container ändrar config | Lägg till `:ro` på config-mounts |

### Felsökning

```bash
# Permission denied?
# Kolla UID inne vs utanför
docker exec container id
id

# Fixa genom att köra som samma user
docker run --user $(id -u):$(id -g) -v ...

# Eller ändra permissions på host
sudo chown -R 1000:1000 /path/to/data

# Volume finns men data saknas?
# Kolla att mount point är korrekt
docker inspect container --format='{{json .Mounts}}'

# Se var volume faktiskt finns på host
docker volume inspect myvolume --format='{{.Mountpoint}}'
```

------------------------------------------------------------

## Övningar

### Övning 1: Grundläggande Volymhantering (Grundläggande)

**Uppgift:** Skapa en volume, skriv data till den, och verifiera att data överlever container-bortagning.

1. Skapa en volume kallad "test-data"
2. Starta en alpine-container som skriver "Hello Volumes!" till /data/message.txt
3. Ta bort containern
4. Starta en ny container och läs filen
5. Städa upp

<details>
<summary>Ledtråd</summary>

Använd:
- `docker volume create`
- `docker run -v test-data:/data alpine sh -c "echo ... > ..."`
- `docker rm`
- `docker run -v test-data:/data alpine cat ...`

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Skapa volume
docker volume create test-data

# 2. Skriv data
docker run --rm \\
    -v test-data:/data \\
    alpine sh -c "echo 'Hello Volumes!' > /data/message.txt"

# 3. Container är redan borta (--rm)

# 4. Läs data med ny container
docker run --rm \\
    -v test-data:/data \\
    alpine cat /data/message.txt
# Output: Hello Volumes!

# 5. Städa upp
docker volume rm test-data

# Verifiera att volume är borta
docker volume ls | grep test-data
# (ingen output)
```

</details>

### Övning 2: PostgreSQL Backup och Restore (Medel)

**Uppgift:** Sätt upp PostgreSQL, skapa testdata, gör backup, simulera dataförlust, och återställ.

1. Starta PostgreSQL med en volume
2. Skapa en tabell och lägg till data
3. Gör en backup av volumen till en tar-fil
4. Ta bort BÅDE container och volume
5. Återställ från backup
6. Verifiera att datan finns

<details>
<summary>Ledtråd</summary>

Backup-kommando:
```bash
docker run --rm \\
    -v volume-name:/source:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/backup.tar.gz -C /source .
```

Restore-kommando:
```bash
docker run --rm \\
    -v volume-name:/target \\
    -v $(pwd):/backup \\
    alpine tar xzf /backup/backup.tar.gz -C /target
```

</details>

<details>
<summary>Lösning</summary>

```bash
# 1. Starta PostgreSQL
docker volume create pg-exercise
docker run -d \\
    --name pg-exercise \\
    -v pg-exercise:/var/lib/postgresql/data \\
    -e POSTGRES_PASSWORD=secret \\
    postgres:15-alpine

# Vänta på uppstart
sleep 5

# 2. Skapa data
docker exec pg-exercise psql -U postgres -c \\
    "CREATE TABLE products (id SERIAL, name VARCHAR(50), price DECIMAL);"
docker exec pg-exercise psql -U postgres -c \\
    "INSERT INTO products (name, price) VALUES ('Laptop', 999.99), ('Mouse', 29.99);"

# Verifiera
docker exec pg-exercise psql -U postgres -c "SELECT * FROM products;"

# 3. Backup
docker stop pg-exercise  # Viktigt: stoppa innan backup för konsistens
docker run --rm \\
    -v pg-exercise:/source:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/pg-backup.tar.gz -C /source .

# 4. Ta bort ALLT (simulerar disaster)
docker rm pg-exercise
docker volume rm pg-exercise

# 5. Restore
docker volume create pg-exercise
docker run --rm \\
    -v pg-exercise:/target \\
    -v $(pwd):/backup \\
    alpine tar xzf /backup/pg-backup.tar.gz -C /target

# 6. Verifiera
docker run -d \\
    --name pg-restored \\
    -v pg-exercise:/var/lib/postgresql/data \\
    postgres:15-alpine

sleep 5
docker exec pg-restored psql -U postgres -c "SELECT * FROM products;"
# Output ska visa: Laptop och Mouse!

# Städa upp
docker rm -f pg-restored
docker volume rm pg-exercise
rm pg-backup.tar.gz
```

</details>

### Övning 3: Multi-Container Shared Storage (Avancerad)

**Uppgift:** Implementera ett scenario där en "producer" container skriver filer och en "consumer" container läser dem.

Krav:
- Producer skriver tidsstämplade filer var 5:e sekund
- Consumer visar innehållet i alla filer
- Använd en shared volume
- Consumer ska ha read-only access

<details>
<summary>Ledtråd</summary>

Producer: `while true; do echo $(date) > /data/$(date +%s).txt; sleep 5; done`
Consumer: `watch ls -la /data/` eller `tail -f` pattern

</details>

<details>
<summary>Lösning</summary>

```bash
# Skapa shared volume
docker volume create shared-files

# Producer - skriver filer
docker run -d \\
    --name producer \\
    -v shared-files:/data \\
    alpine sh -c 'while true; do
        filename="/data/file-$(date +%s).txt"
        echo "Created at: $(date)" > "$filename"
        echo "Written: $filename"
        sleep 5
    done'

# Consumer - läser filer (read-only!)
docker run -d \\
    --name consumer \\
    -v shared-files:/data:ro \\
    alpine sh -c 'while true; do
        echo "=== Files in /data ==="
        ls -la /data/
        echo ""
        echo "=== Latest file content ==="
        latest=$(ls -t /data/*.txt 2>/dev/null | head -1)
        if [ -n "$latest" ]; then cat "$latest"; fi
        echo ""
        sleep 3
    done'

# Verifiera producer
docker logs producer

# Verifiera consumer
docker logs consumer

# Verifiera read-only (detta ska misslyckas)
docker exec consumer touch /data/test.txt 2>&1
# Output: touch: /data/test.txt: Read-only file system

# Visa volume-innehåll direkt
docker run --rm -v shared-files:/data alpine ls -la /data/

# Städa upp
docker rm -f producer consumer
docker volume rm shared-files
```

</details>

------------------------------------------------------------

## Kopplingar

| Ämne | Koppling |
|------|----------|
| **Docker Compose** | Volumes definieras deklarativt i docker-compose.yml |
| **Kubernetes** | PersistentVolumes och PersistentVolumeClaims |
| **Backup** | Integreras med backup-system som Velero |
| **Databases** | Alla databaser kräver persistent storage |
| **CI/CD** | Cache-volumes för snabbare builds |

### Storage i Kubernetes-kontexten

```
+---------------------------------------------------------------------+
|                    KUBERNETES STORAGE MAPPING                        |
+---------------------------------------------------------------------+
|                                                                      |
|   Docker                          Kubernetes                         |
|   ------                          ----------                         |
|                                                                      |
|   docker volume create     -->    PersistentVolume (PV)              |
|   -v mydata:/data          -->    PersistentVolumeClaim (PVC)        |
|   Volume drivers           -->    StorageClasses                     |
|                                                                      |
|   Liknande koncept, mer flexibilitet i Kubernetes                    |
|                                                                      |
+---------------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

### Centrala Koncept

| Koncept | Huvudpoäng |
|---------|------------|
| **Volumes** | Docker-managed persistent storage för produktion |
| **Bind Mounts** | Host-katalog för utveckling och config |
| **tmpfs** | RAM-baserad temporär lagring |
| **Persistence** | Volumes överlever container-livscykeln |

### Viktiga Insikter

1. **Containers är ephemeral** - använd alltid volumes för data som ska bevaras
2. **Volumes för produktion** - Docker hanterar, plattformsoberoende
3. **Bind mounts för utveckling** - Hot reload, direkt access
4. **Backup är ditt ansvar** - Automatisera backups av volumes

------------------------------------------------------------

## Nyckelkommandon

### Volume Management

| Kommando | Beskrivning |
|----------|-------------|
| `docker volume create name` | Skapa volume |
| `docker volume ls` | Lista volumes |
| `docker volume inspect name` | Visa detaljer |
| `docker volume rm name` | Ta bort volume |
| `docker volume prune` | Ta bort oanvända |

### Mounting

| Syntax | Beskrivning |
|--------|-------------|
| `-v mydata:/app/data` | Named volume |
| `-v /host/path:/container/path` | Bind mount |
| `-v /host/path:/container/path:ro` | Read-only |
| `--tmpfs /tmp` | RAM-disk |
| `--mount type=volume,src=X,dst=Y` | Explicit syntax |

### Backup Commands

| Kommando | Beskrivning |
|----------|-------------|
| `docker cp container:/path ./local` | Kopiera från container |
| `docker cp ./local container:/path` | Kopiera till container |
| `tar czf backup.tar.gz -C /source .` | Backup via tar |

------------------------------------------------------------

## Referenser

**Officiell dokumentation:**
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
- [tmpfs Mounts](https://docs.docker.com/storage/tmpfs/)

**Fördjupning:**
- [Storage Drivers](https://docs.docker.com/storage/storagedriver/)
- [Best Practices for Data Management](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#volume)

**Verktyg:**
- [docker-volume-backup](https://github.com/jareware/docker-volume-backup)
- [Restic - Backup Program](https://restic.net/)
""",
        },
        {
            "title": "Docker Compose Fundamentals",
            "slug": "docker-compose-fundamentals",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Compose Fundamentals

------------------------------------------------------------

## Introduktion

Forstall dig att du bygger en modern webbapplikation. Du har en React-frontend, en Python-backend, en PostgreSQL-databas och kanske Redis for caching. Att starta varje komponent manuellt med separata docker run-kommandon blir snabbt ohanterligt - du maste komma ihag natverk, volymer, miljovariabler och startordning for varje container.

Docker Compose loser detta problem genom att lata dig definiera hela din applikationsstack i en enda YAML-fil. Istallet for att skriva tio olika docker run-kommandon skriver du docker compose up och hela din miljo startar med korrekt konfiguration.

Som DevOps-ingenjor kommer du anvanda Docker Compose dagligen. Det ar standarden for lokal utveckling, CI/CD-testmiljoer och till och med enklare produktionsmiljoer. Nar en ny teammedlem borjar kan de klona repot och kora ett enda kommando for att fa upp hela utvecklingsmiljon - ingen manuell installation av databaser eller konfiguration av natverksinställningar.

I den har noden lar du dig syntaxen for docker-compose.yml, de viktigaste kommandona, hur du hanterar multi-container-applikationer och hur du arbetar med miljovariabler och olika konfigurationer for olika miljoer.

------------------------------------------------------------

## Teori

Docker Compose ar ett verktyg for att definiera och kora multi-container Docker-applikationer. Istallet for imperativa kommandon (gor detta, sedan detta) anvander du en deklarativ YAML-fil som beskriver onskat tillstand.

### Compose i DevOps-kontexten

| Scenario | Utan Compose | Med Compose |
|----------|--------------|-------------|
| Starta utvecklingsmiljo | 5-10 manuella kommandon | docker compose up |
| Onboarding ny utvecklare | Dokumentation, manuell setup | Klona repo, kora ett kommando |
| CI/CD testmiljo | Komplexa shell-scripts | docker-compose.test.yml |
| Reproducerbarhet | Varierande resultat | Identisk miljo varje gang |
| Versionshantering | Svart att spara | Hela infran i git |

### Arkitektur och komponenter

```
+------------------------------------------------------------+
|                    DOCKER COMPOSE ARKITEKTUR                |
+------------------------------------------------------------+
|                                                            |
|   docker-compose.yml                                       |
|   +--------------------------+                             |
|   | services:                |                             |
|   |   web:                   |                             |
|   |   api:                   |----> Docker Compose CLI     |
|   |   db:                    |           |                 |
|   | networks:                |           |                 |
|   | volumes:                 |           v                 |
|   +--------------------------+     Docker Daemon           |
|                                          |                 |
|              +---------------------------+                 |
|              |           |               |                 |
|              v           v               v                 |
|         Container    Container      Container              |
|           (web)        (api)          (db)                 |
|              |           |               |                 |
|              +-----+-----+---------------+                 |
|                    |                                       |
|              Default Network (bridge)                      |
|                                                            |
+------------------------------------------------------------+
```

### YAML-filens huvudsektioner

En docker-compose.yml-fil har flera toppniva-sektioner:

```
+------------------------------------------------------------+
|              DOCKER-COMPOSE.YML STRUKTUR                   |
+------------------------------------------------------------+
|                                                            |
|   +------------------+   services: (obligatorisk)          |
|   |    SERVICES      |   - Definierar containers          |
|   |                  |   - Image eller build              |
|   | web, api, db,    |   - Portar, volymer, miljovar     |
|   | redis, worker    |                                    |
|   +------------------+                                     |
|           |                                                |
|           v                                                |
|   +------------------+   networks: (valfri)                |
|   |    NETWORKS      |   - Custom natverk                 |
|   |                  |   - Isolering mellan services      |
|   | frontend,        |   - DNS-upplosning                 |
|   | backend          |                                    |
|   +------------------+                                     |
|           |                                                |
|           v                                                |
|   +------------------+   volumes: (valfri)                 |
|   |    VOLUMES       |   - Named volumes                  |
|   |                  |   - Persistent data                |
|   | pgdata,          |   - Delad data mellan services     |
|   | uploads          |                                    |
|   +------------------+                                     |
|                                                            |
+------------------------------------------------------------+
```

### Service-konfigurationsnycklar

| Nyckel | Beskrivning | Exempel |
|--------|-------------|---------|
| image | Anvand befintlig image | postgres:15-alpine |
| build | Bygg fran Dockerfile | ./backend |
| ports | Exponera portar | "8080:80" |
| environment | Miljovariabler | DATABASE_URL=... |
| env_file | Variabler fran fil | .env |
| volumes | Montera volymer | ./app:/app |
| depends_on | Startberoenden | [db, redis] |
| networks | Anslutnande natverk | [backend] |
| restart | Omstartspolicy | unless-stopped |
| healthcheck | Halsokontroll | test: curl localhost |
| command | Overskriv CMD | ["python", "app.py"] |
| entrypoint | Overskriv ENTRYPOINT | ["/entrypoint.sh"] |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa grundlaggande docker-compose.yml

Borja med att skapa en docker-compose.yml i projektets rotmapp:

```yaml
# docker-compose.yml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

Starta med:
```bash
docker compose up
```

### Steg 2: Lagg till databas

Utoka med en PostgreSQL-databas:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: secretpass
      POSTGRES_DB: appdb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Steg 3: Lagg till backend med build

Lagg till en backend som byggs fran Dockerfile:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - api

  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://appuser:secretpass@db:5432/appdb
    depends_on:
      - db
    volumes:
      - ./backend:/app

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: secretpass
      POSTGRES_DB: appdb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Steg 4: Anvand .env-fil

Flytta kansliga variabler till .env:

```bash
# .env
POSTGRES_USER=appuser
POSTGRES_PASSWORD=secretpass
POSTGRES_DB=appdb
```

```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
```

### Steg 5: Lagg till healthchecks

Sakerstall att services ar redo innan beroende services startar:

```yaml
services:
  api:
    build: ./backend
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Enkel webbapplikation med databas

```yaml
# docker-compose.yml - Enkel Flask-app med PostgreSQL
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:pass@db:5432/flask_db
    volumes:
      - .:/app
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: flask_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d flask_db"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

### Exempel 2: Full-stack med frontend, backend och cache

```yaml
# docker-compose.yml - React + FastAPI + PostgreSQL + Redis
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/app
      - REDIS_URL=redis://cache:6379/0
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    volumes:
      - ./backend/src:/app/src

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  pgdata:
  redis_data:
```

### Exempel 3: Microservices med custom natverk

```yaml
# docker-compose.yml - Microservices med natverksisolering
services:
  gateway:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - frontend
    depends_on:
      - user-service
      - order-service

  user-service:
    build: ./services/user
    networks:
      - frontend
      - backend
    environment:
      - DB_HOST=user-db

  order-service:
    build: ./services/order
    networks:
      - frontend
      - backend
    environment:
      - DB_HOST=order-db

  user-db:
    image: postgres:15-alpine
    networks:
      - backend
    volumes:
      - user_data:/var/lib/postgresql/data

  order-db:
    image: postgres:15-alpine
    networks:
      - backend
    volumes:
      - order_data:/var/lib/postgresql/data

networks:
  frontend:
  backend:

volumes:
  user_data:
  order_data:
```

### Exempel 4: Utvecklingsmiljo med hot reload

```yaml
# docker-compose.yml - Development med hot reload
services:
  frontend:
    build:
      context: ./frontend
      target: development
    ports:
      - "3000:3000"
    volumes:
      - ./frontend/src:/app/src
      - ./frontend/public:/app/public
      - /app/node_modules
    environment:
      - CHOKIDAR_USEPOLLING=true

  backend:
    build:
      context: ./backend
      target: development
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - DEBUG=true
      - RELOAD=true
    command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
```

### Exempel 5: Override-filer for olika miljoer

```yaml
# docker-compose.yml - Baskonfiguration
services:
  api:
    build: ./backend
    environment:
      - LOG_LEVEL=info

  db:
    image: postgres:15-alpine
```

```yaml
# docker-compose.override.yml - Development (laddas automatiskt)
services:
  api:
    volumes:
      - ./backend:/app
    environment:
      - DEBUG=true
    ports:
      - "8000:8000"

  db:
    ports:
      - "5432:5432"
```

```yaml
# docker-compose.prod.yml - Production
services:
  api:
    image: registry.example.com/api:latest
    environment:
      - DEBUG=false
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

------------------------------------------------------------

## Bästa Praxis

### 1. Anvand alltid named volumes for persistent data

```yaml
# Bra - named volume
volumes:
  - pgdata:/var/lib/postgresql/data

# Undvik - anonym volume
volumes:
  - /var/lib/postgresql/data
```

### 2. Separera miljovariabler i .env-filer

```yaml
# Bra - anvand env_file
services:
  api:
    env_file:
      - .env
      - .env.local

# Undvik - hardkodade hemligheter
services:
  api:
    environment:
      - DB_PASSWORD=supersecret123
```

### 3. Anvand healthchecks for tillforlitliga beroenden

```yaml
# Bra - vanta pa faktisk readiness
depends_on:
  db:
    condition: service_healthy

# Otillrackligt - vantar bara pa start
depends_on:
  - db
```

### 4. Specifiera image-versioner explicit

```yaml
# Bra - explicit version
image: postgres:15.4-alpine

# Riskabelt - kan andra ovantat
image: postgres:latest
```

### 5. Anvand multi-stage builds for mindre images

```dockerfile
# Dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine
COPY --from=builder /app/dist ./dist
CMD ["node", "dist/main.js"]
```

### 6. Begranså resurser i produktion

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.25'
          memory: 256M
```

------------------------------------------------------------

## Vanliga Fallgropar

### 1. depends_on garanterar inte readiness

depends_on vantar bara pa att containern startar, inte att tjansten inuti ar redo.

```yaml
# Problem - api kan starta innan db ar redo
services:
  api:
    depends_on:
      - db

# Losning - anvand healthcheck condition
services:
  api:
    depends_on:
      db:
        condition: service_healthy
```

### 2. Glomma att named volumes persisterar data

```bash
# docker compose down tar INTE bort volumes
docker compose down

# For att ta bort volumes, anvand -v flaggan
docker compose down -v
```

### 3. Port-konflikter pa host

```yaml
# Om port 5432 ar upptagen pa host
services:
  db:
    ports:
      - "5432:5432"  # Kommer misslyckas

# Losning - anvand annan host-port
services:
  db:
    ports:
      - "5433:5432"
```

### 4. Bind mounts med fel permissions

```yaml
# Problem - container kor som root, skapar filer som root
volumes:
  - ./app:/app

# Losning - matcha user ID
services:
  api:
    user: "${UID}:${GID}"
    volumes:
      - ./app:/app
```

### 5. Glomma att bygga om efter Dockerfile-andringar

```bash
# docker compose up anvander cached image
docker compose up

# Tving rebuild
docker compose up --build

# Eller bygg separat
docker compose build --no-cache
docker compose up
```

### 6. Anvanda localhost istallet for service-namn

```yaml
# Fel - localhost pekar pa containern sjalv
environment:
  - DATABASE_URL=postgresql://user:pass@localhost:5432/db

# Ratt - anvand service-namn
environment:
  - DATABASE_URL=postgresql://user:pass@db:5432/db
```

------------------------------------------------------------

## Övningar

### Ovning 1: Grundlaggande WordPress-stack

Skapa en docker-compose.yml som kor WordPress med MySQL. WordPress ska vara tillganglig pa port 8080 och databasdata ska persistera mellan omstarter.

<details>
<summary>Ledtrad</summary>

Anvand officiella images wordpress och mysql. WordPress behover miljovariabler for databaskoppling (WORDPRESS_DB_HOST, WORDPRESS_DB_USER, etc). MySQL behover MYSQL_ROOT_PASSWORD. Skapa en named volume for MySQL-data.

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.yml
services:
  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress_pass
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - db
    volumes:
      - wp_content:/var/www/html/wp-content

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root_pass
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress_pass
    volumes:
      - db_data:/var/lib/mysql

volumes:
  wp_content:
  db_data:
```

Starta med: docker compose up -d
Oppna: http://localhost:8080

</details>

### Ovning 2: Multi-miljö med override-filer

Skapa en setup med docker-compose.yml (bas), docker-compose.override.yml (development) och docker-compose.prod.yml (production). I development ska koden monteras for hot reload och debug vara aktiverat. I production ska en forbyggd image anvandas.

<details>
<summary>Ledtrad</summary>

Baskonfigurationen innehaller services utan miljospecifika installningar. Override-filen (laddas automatiskt) lagger till volumes och debug-variabler. Prod-filen anvander image istallet for build. Kor prod med: docker compose -f docker-compose.yml -f docker-compose.prod.yml up

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.yml
services:
  api:
    build: ./api
    environment:
      - LOG_LEVEL=info
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD:-secret}
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```yaml
# docker-compose.override.yml
services:
  api:
    volumes:
      - ./api:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=true
      - LOG_LEVEL=debug

  db:
    ports:
      - "5432:5432"
```

```yaml
# docker-compose.prod.yml
services:
  api:
    image: registry.example.com/api:${VERSION:-latest}
    environment:
      - DEBUG=false
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
```

Kommandon:
- Development: docker compose up
- Production: docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

</details>

### Ovning 3: Healthchecks och startordning

Skapa en stack med en API (Python/Node) och PostgreSQL dar API:et vantar pa att databasen ar fullstandigt redo (inte bara startad) innan den startar. Lagg till en healthcheck for API:et ocksa.

<details>
<summary>Ledtrad</summary>

Anvand pg_isready for PostgreSQL healthcheck. For API:et, anvand curl mot en /health-endpoint. Anvand depends_on med condition: service_healthy. Kom ihag start_period for att ge containern tid att starta.

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.yml
services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/app
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d app"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  pgdata:
```

API:et maste ha en /health-endpoint:
```python
@app.get("/health")
def health():
    return {"status": "healthy"}
```

</details>

------------------------------------------------------------

## Kopplingar

| Amne | Koppling |
|------|----------|
| Docker Images | Compose anvander images du bygger eller hamtar |
| Docker Networking | Compose skapar automatiskt natverk for services |
| Docker Volumes | Named volumes i Compose for persistent data |
| CI/CD | Compose for testmiljoer i pipelines |
| Kubernetes | Compose ar steg 1 innan K8s-migration |
| Infrastructure as Code | docker-compose.yml ar IaC for containers |
| Microservices | Compose orkestrerar flera services lokalt |

```
+------------------------------------------------------------+
|                  COMPOSE I DEVOPS-FLODE                    |
+------------------------------------------------------------+
|                                                            |
|   Developer        CI/CD Pipeline       Production         |
|   +--------+       +-------------+      +-----------+      |
|   | docker |       | docker      |      | Kubernetes|      |
|   | compose|  -->  | compose     | -->  | Helm      |      |
|   | up     |       | -f test.yml |      | Charts    |      |
|   +--------+       +-------------+      +-----------+      |
|                                                            |
|   Lokal dev        Automatiserade       Skalbar            |
|   och test         integrationstester   produktion         |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

Docker Compose transformerar hur vi arbetar med multi-container-applikationer. Istallet for att jonglera manga docker run-kommandon med komplexa flaggor definierar vi hela stacken deklarativt i en YAML-fil.

De viktigaste koncepten:

1. **Deklarativ konfiguration** - Beskriv onskat tillstand, lat Compose hantera detaljerna
2. **Automatiskt natverk** - Services hittar varandra via namn, ingen manuell natverkskonfiguration
3. **Named volumes** - Persistent data som overelever container-omstarter
4. **Environment variables** - Flexibel konfiguration via .env-filer
5. **Healthchecks** - Sakerstall att services ar faktiskt redo, inte bara startade
6. **Override-filer** - Samma bas, olika konfiguration for dev/test/prod

Docker Compose ar bryggan mellan enkel containerkorning och fullskalig orkestrering. Beharskar du Compose ar steget till Kubernetes mycket kortare.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| docker compose up | Starta alla services (forgrund) |
| docker compose up -d | Starta i bakgrunden (detached) |
| docker compose down | Stoppa och ta bort containers |
| docker compose down -v | Stoppa och ta bort inkl. volumes |
| docker compose ps | Lista korande services |
| docker compose logs | Visa loggar fran alla services |
| docker compose logs -f [service] | Folj loggar (specifik service) |
| docker compose build | Bygg/ombygg images |
| docker compose up --build | Bygg och starta |
| docker compose exec [service] [cmd] | Kor kommando i service |
| docker compose run [service] [cmd] | Kor engångskommando |
| docker compose pull | Hamta senaste images |
| docker compose restart [service] | Starta om service |
| docker compose stop | Stoppa utan att ta bort |
| docker compose config | Validera och visa konfiguration |

------------------------------------------------------------

## Referenser

### Officiell dokumentation
- Docker Compose Overview: https://docs.docker.com/compose/
- Compose File Reference: https://docs.docker.com/compose/compose-file/
- Compose CLI Reference: https://docs.docker.com/compose/reference/

### Fordjupning
- Docker Compose Specification: https://github.com/compose-spec/compose-spec
- Awesome Compose (exempel): https://github.com/docker/awesome-compose
- Docker Compose Best Practices: https://docs.docker.com/develop/dev-best-practices/

### Relaterade verktyg
- Docker Desktop: https://www.docker.com/products/docker-desktop/
- Podman Compose: https://github.com/containers/podman-compose
- Kompose (Compose till K8s): https://kompose.io/
""",
        },
        {
            "title": "Docker Compose Advanced Patterns",
            "slug": "docker-compose-advanced-patterns",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker Compose Advanced Patterns

------------------------------------------------------------

## Introduktion

Docker Compose ar kraftfullt for multi-container hantering, men produktionsmiljoer kraver avancerade patterns. Denna modul gar bortom grunderna och utforskar tekniker som professionella DevOps-ingenjorer anvander dagligen for att hantera komplexa applikationer.

Vad du kommer lara dig:
- Multi-file compose for miljospecifik konfiguration
- Profiles for valfria tjanster
- Build context och args
- Extension fields (x-) och YAML anchors
- Secrets och configs
- Skalning med --scale
- Resource limits i Compose

```
+----------------------------------------------------------+
|         COMPOSE ADVANCED PATTERNS OVERVIEW               |
+----------------------------------------------------------+
|  docker-compose.yml ---> docker-compose.override.yml     |
|       (bas)                  (dev-specifik)              |
|              |                     |                     |
|              +----------+----------+                     |
|                         |                                |
|                         v                                |
|              MERGED CONFIGURATION                        |
|              - Services kombineras                       |
|              - Extension fields expanderas               |
|              - Profiles filtrerar vid runtime            |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Teori

### Multi-file Compose Arkitektur

Docker Compose stodjer flera konfigurationsfiler som mergas i ordning:

| Fil | Laddning | Anvandning |
|-----|----------|------------|
| docker-compose.yml | Alltid | Bas-konfiguration |
| docker-compose.override.yml | Automatiskt | Development |
| docker-compose.prod.yml | Med -f flagga | Production |

Merge-regler:
- Skalara varden overskrivs helt
- Maps (environment som objekt) mergas rekursivt
- Listor (ports) kan utoka eller overskrivas

### Profiles - Valfria Services

Profiles grupperar services som inte alltid ska startas:

```
+----------------------------------------------------------+
|                   PROFILES KONCEPT                       |
+----------------------------------------------------------+
| docker compose up      | docker compose --profile debug  |
| (ingen profile)        | (aktiverar debug)               |
+------------------------+----------------------------------+
| api      [startar]     | api         [startar]           |
| db       [startar]     | db          [startar]           |
| mailhog  [STARTAR EJ]  | mailhog     [startar]           |
+----------------------------------------------------------+
```

### Extension Fields och YAML Anchors

YAML anchors (&) och aliases (*) mojliggor ateranvandning. Docker Compose utvidgar med x- prefix for delade definitioner som ignoreras vid parsning:

```
x-common: &common        <-- Definiera anchor med &
  environment:
    LOG_LEVEL: info

services:
  api:
    <<: *common          <-- Anvand med << och *
```

### Secrets vs Environment Variables

| Aspekt | Environment Variables | Secrets |
|--------|----------------------|---------|
| Lagring | Processminne | /run/secrets/ |
| Synlighet | docker inspect visar | Dold |
| Bast for | Konfiguration | Losenord, nycklar |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Skapa Multi-file Struktur

```bash
mkdir -p myapp/{secrets,config}
cd myapp
touch docker-compose.yml docker-compose.override.yml docker-compose.prod.yml
```

### Steg 2: Bas-konfiguration

```yaml
# docker-compose.yml
services:
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

### Steg 3: Development Override

```yaml
# docker-compose.override.yml (laddas automatiskt)
services:
  api:
    build:
      args:
        DEBUG: "true"
    volumes:
      - ./api/src:/app/src:ro
    ports:
      - "8000:8000"
    environment:
      DEBUG: "true"

  db:
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: devpassword
```

### Steg 4: Produktions-konfiguration

```yaml
# docker-compose.prod.yml
services:
  api:
    image: myregistry.io/api:${VERSION:-latest}
    restart: always
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
    secrets:
      - db_password
    environment:
      DATABASE_PASSWORD_FILE: /run/secrets/db_password

  db:
    restart: always
    deploy:
      resources:
        limits:
          memory: 1G
    secrets:
      - db_password
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Steg 5: Starta Olika Miljoer

```bash
# Development (override laddas automatiskt)
docker compose up -d

# Produktion (explicit filer)
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Validera innan start
docker compose -f docker-compose.yml -f docker-compose.prod.yml config
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Microservices med Profiles och Anchors

```yaml
x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
    max-file: "3"

x-healthcheck: &healthcheck-defaults
  interval: 30s
  timeout: 10s
  retries: 3

services:
  api:
    build: ./api
    ports:
      - "8080:8080"
    logging: *default-logging
    healthcheck:
      <<: *healthcheck-defaults
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]

  worker:
    build: ./worker
    logging: *default-logging

  # Monitoring - endast med --profile monitoring
  prometheus:
    image: prom/prometheus
    profiles: [monitoring]
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    profiles: [monitoring]
    ports:
      - "3000:3000"
    depends_on: [prometheus]

  # Debug-verktyg
  jaeger:
    image: jaegertracing/all-in-one
    profiles: [debug]
    ports:
      - "16686:16686"
```

### Exempel 2: Build med Context och Args

```yaml
services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: ${BUILD_TARGET:-development}
      args:
        NODE_VERSION: "18"
        NPM_TOKEN: ${NPM_TOKEN}
      cache_from:
        - myregistry.io/frontend:cache

  api:
    build:
      context: .
      dockerfile: ./backend/Dockerfile
      args:
        PYTHON_VERSION: "3.11"
```

### Exempel 3: Configs for Konfigurationsfiler

```yaml
services:
  nginx:
    image: nginx:alpine
    configs:
      - source: nginx_config
        target: /etc/nginx/nginx.conf

configs:
  nginx_config:
    file: ./config/nginx.conf
```

------------------------------------------------------------

## Bästa Praxis

### Filorganisation

```
project/
+-- docker-compose.yml           # Bas-konfiguration
+-- docker-compose.override.yml  # Development (gitignore)
+-- docker-compose.prod.yml      # Produktion
+-- .env.example                 # Mall for variabler
+-- secrets/                     # Secrets (gitignore!)
+-- config/                      # Konfigurationsfiler
```

### Extension Fields for DRY

```yaml
x-common-env: &common-env
  TZ: Europe/Stockholm
  LOG_FORMAT: json

x-resource-limits: &resource-limits
  deploy:
    resources:
      limits:
        cpus: '0.5'
        memory: 256M

services:
  service-a:
    <<: *resource-limits
    environment:
      <<: *common-env
      SERVICE_NAME: service-a

  service-b:
    <<: *resource-limits
    environment:
      <<: *common-env
      SERVICE_NAME: service-b
```

### Secrets - Aldrig Hardkoda Losenord

```yaml
# RATT
services:
  api:
    secrets: [db_password]
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password

# FEL - Aldrig!
services:
  api:
    environment:
      DB_PASSWORD: supersecret123
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Override laddas inte
```bash
# Problem: .yaml vs .yml
docker-compose.yaml         # Override hittas INTE
docker-compose.override.yml

# Losning: Samma extension
docker-compose.yml
docker-compose.override.yml
```

### Fallgrop 2: List-merge missforstand
```yaml
# Bas: environment som lista
environment:
  - LOG_LEVEL=info
  - DEBUG=false

# Override: Lista ERSATTER, mergar inte!
environment:
  - DEBUG=true  # LOG_LEVEL forsvinner!

# Losning: Anvand map-syntax
environment:
  LOG_LEVEL: info
  DEBUG: false
```

### Fallgrop 3: Scale med port-konflikt
```yaml
# Problem
ports:
  - "8080:8080"  # Kan inte skalas!

# Losning
expose:
  - "8080"  # Intern port utan host-mapping
```

### Fallgrop 4: Resource limits ignoreras
```bash
# Problem: deploy.resources kraever --compatibility
docker compose up  # Limits ignoreras

# Losning
docker compose --compatibility up -d
```

------------------------------------------------------------

## Övningar

### Ovning 1: Multi-environment Setup

Skapa multi-file struktur for webapp med:
- Bas: api + postgres
- Dev: Hot reload, exponerade portar, debug=true
- Prod: Resource limits, secrets, restart policies

<details>
<summary>Ledtrad</summary>
Borja med bas-filen utan miljospecifika installningar. Override lagger till volumes och portar. Prod-filen lagger till restart, deploy.resources och secrets.
</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.yml
services:
  api:
    build: ./api
    depends_on:
      db: {condition: service_healthy}
  db:
    image: postgres:15-alpine
    volumes: [db_data:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
volumes:
  db_data:

# docker-compose.override.yml
services:
  api:
    volumes: [./api/src:/app/src]
    ports: ["8000:8000"]
    environment: {DEBUG: "true"}
  db:
    ports: ["5432:5432"]
    environment: {POSTGRES_PASSWORD: devpass}

# docker-compose.prod.yml
services:
  api:
    restart: always
    deploy: {resources: {limits: {cpus: '1.0', memory: 512M}}}
    secrets: [db_password]
  db:
    restart: always
    secrets: [db_password]
    environment: {POSTGRES_PASSWORD_FILE: /run/secrets/db_password}
secrets:
  db_password: {file: ./secrets/db_password.txt}
```
</details>

### Ovning 2: Extension Fields Refactoring

Refaktorera denna duplicerade konfiguration med extension fields:

```yaml
services:
  api:
    environment: {LOG_LEVEL: info, TZ: Europe/Stockholm}
    logging: {driver: json-file, options: {max-size: 10m}}
  worker:
    environment: {LOG_LEVEL: info, TZ: Europe/Stockholm}
    logging: {driver: json-file, options: {max-size: 10m}}
```

<details>
<summary>Ledtrad</summary>
Skapa x-common-env och x-logging med YAML anchors. Anvand << for att infoga.
</details>

<details>
<summary>Losning</summary>

```yaml
x-common-env: &common-env
  LOG_LEVEL: info
  TZ: Europe/Stockholm

x-logging: &default-logging
  driver: json-file
  options: {max-size: 10m}

services:
  api:
    environment: {<<: *common-env}
    logging: *default-logging
  worker:
    environment: {<<: *common-env}
    logging: *default-logging
```
</details>

### Ovning 3: Profiles och Skalning

Skapa compose-fil med:
- Core: nginx (LB) + api (skalbar till 3)
- Profile monitoring: prometheus + grafana
- API utan fast port-mapping

<details>
<summary>Ledtrad</summary>
Anvand expose istallet for ports pa api. Nginx har extern port. Definiera profiles pa monitoring-services.
</details>

<details>
<summary>Losning</summary>

```yaml
services:
  nginx:
    image: nginx:alpine
    ports: ["80:80"]
    depends_on: [api]

  api:
    build: ./api
    expose: ["8000"]
    deploy: {replicas: 1}

  prometheus:
    image: prom/prometheus
    profiles: [monitoring]
    ports: ["9090:9090"]

  grafana:
    image: grafana/grafana
    profiles: [monitoring]
    ports: ["3000:3000"]
```

```bash
docker compose --profile monitoring up -d --scale api=3
```
</details>

------------------------------------------------------------

## Kopplingar

| Amne | Koppling |
|------|----------|
| Docker Networking | Multi-file delar natverksdefinitioner |
| Docker Volumes | Secrets och configs ar specialvolumes |
| CI/CD Pipelines | Olika compose-filer for build vs deploy |
| Kubernetes | Profiles liknar kustomize overlays |
| Infrastructure as Code | Extension fields liknar Terraform modules |

```
+----------------------------------------------------------+
|           DOCKER COMPOSE I DEVOPS ECOSYSTEM              |
+----------------------------------------------------------+
|  Development     CI/CD          Production               |
|  [override]  --> [test.yml] --> [prod.yml]               |
|       |              |              |                    |
|       +------+-------+------+-------+                    |
|              |              |                            |
|              v              v                            |
|       docker-compose.yml (bas)                           |
|              |                                           |
|              v                                           |
|       Kubernetes/Swarm (konverteras med kompose)         |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

Docker Compose Advanced Patterns ger verktyg for professionell multi-container hantering:

- **Multi-file compose** separerar bas-config fran miljospecifika installningar med automatisk merge av override.yml
- **Profiles** grupperar valfria services som startas med --profile flaggan
- **Extension fields** eliminerar duplicering med x- prefix och YAML anchors
- **Secrets och configs** hanterar kanslig data sakrare an environment variables
- **Skalning** med --scale och expose for intern kommunikation utan port-konflikter
- **Resource limits** kontrollerar CPU/minne med deploy.resources

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| docker compose config | Visa merged konfiguration |
| docker compose -f A.yml -f B.yml up | Multi-file start |
| docker compose --profile NAME up | Starta med profile |
| docker compose up --scale SERVICE=N | Skala service |
| docker compose --compatibility up | Aktivera deploy.resources |

```bash
# Validera konfiguration
docker compose -f docker-compose.yml -f docker-compose.prod.yml config

# Produktion med monitoring
docker compose -f docker-compose.yml -f docker-compose.prod.yml --profile monitoring up -d

# Skala workers
docker compose up -d --scale worker=5
```

------------------------------------------------------------

## Referenser

### Officiell Dokumentation
- Compose Specification: https://docs.docker.com/compose/compose-file/
- Compose Profiles: https://docs.docker.com/compose/profiles/
- Compose Secrets: https://docs.docker.com/compose/use-secrets/

### Fordjupning
- Awesome Compose Examples: https://github.com/docker/awesome-compose
- Docker Compose Best Practices: https://docs.docker.com/develop/dev-best-practices/

### Relaterade Verktyg
- Kompose (Compose till K8s): https://kompose.io/
- Docker Swarm: https://docs.docker.com/engine/swarm/
""",
        },
        {
            "title": "Docker Security Best Practices",
            "slug": "docker-security-best-practices",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Security Best Practices

------------------------------------------------------------

## Introduktion

Containersäkerhet är en kritisk komponent i modern DevOps. Trots att Docker ger isolation mellan containers och hosten, är denna isolation inte perfekt. En felkonfigurerad container kan leda till att angripare får tillgång till hela hosten eller känslig data.

Denna modul täcker de viktigaste säkerhetsprinciperna för Docker:

- Köra containers som non-root användare
- Skanna images för sårbarheter med verktyg som Trivy och Snyk
- Hantera hemligheter säkert utan att exponera dem i images
- Nätverksisolering mellan containers
- Resursbegränsningar för att förhindra denial-of-service
- Skrivskyddade filsystem för ökad säkerhet
- Linux capabilities och seccomp-profiler
- Content trust och signering av images

Efter denna modul kommer du kunna implementera en robust säkerhetsstrategi för dina Docker-miljöer.

------------------------------------------------------------

## Teori

Containersäkerhet bygger på principen om defense in depth - flera lager av skydd som tillsammans minimerar risken för intrång.

**Linux Namespaces och Cgroups**

Docker använder Linux-kernelfunktioner för isolation:

```
+------------------------------------------------------------------+
|                         HOST SYSTEM                               |
+------------------------------------------------------------------+
|  +---------------------------+  +---------------------------+     |
|  |       CONTAINER A         |  |       CONTAINER B         |     |
|  +---------------------------+  +---------------------------+     |
|  | PID Namespace    (egna)   |  | PID Namespace    (egna)   |     |
|  | Network Namespace (egna)  |  | Network Namespace (egna)  |     |
|  | Mount Namespace  (egna)   |  | Mount Namespace  (egna)   |     |
|  | User Namespace   (egna)   |  | User Namespace   (egna)   |     |
|  +---------------------------+  +---------------------------+     |
|                                                                   |
|  +---------------------------+                                    |
|  |    SHARED KERNEL         |                                    |
|  +---------------------------+                                    |
+------------------------------------------------------------------+
```

| Koncept | Beskrivning | Säkerhetsimplikation |
|---------|-------------|---------------------|
| Namespaces | Isolerar processer, nätverk, filsystem | Process i container ser inte host |
| Cgroups | Begränsar resurser (CPU, RAM) | Förhindrar resource exhaustion |
| Capabilities | Finkorniga privilegier | Minimerar root-rättigheter |
| Seccomp | Filtrerar syscalls | Blockerar farliga operationer |
| AppArmor/SELinux | Mandatory Access Control | Extra lager av skydd |

**Principle of Least Privilege**

Varje container ska endast ha de rättigheter som krävs för att utföra sin uppgift:

```
+------------------------------------------------------------------+
|              PRIVILEGE HIERARCHY                                  |
+------------------------------------------------------------------+
|                                                                   |
|   HOGST RISK                                                      |
|   +--------------------------------------------------------+     |
|   | --privileged (full host access)                        |     |
|   +--------------------------------------------------------+     |
|                          |                                        |
|                          v                                        |
|   +--------------------------------------------------------+     |
|   | root user + alla capabilities                          |     |
|   +--------------------------------------------------------+     |
|                          |                                        |
|                          v                                        |
|   +--------------------------------------------------------+     |
|   | root user + begransade capabilities                    |     |
|   +--------------------------------------------------------+     |
|                          |                                        |
|                          v                                        |
|   +--------------------------------------------------------+     |
|   | non-root user + minimala capabilities                  |     |
|   +--------------------------------------------------------+     |
|   LAGST RISK                                                      |
|                                                                   |
+------------------------------------------------------------------+
```

**Attack Surface**

Varje komponent i en container bidrar till attack surface:

| Komponent | Risk | Mitigation |
|-----------|------|------------|
| Base image | Fler paket = fler sårbarheter | Använd minimala images |
| Application code | Buggar, injections | Code review, scanning |
| Dependencies | Kända CVEs | Dependency scanning |
| Configuration | Felkonfiguration | Security policies |
| Secrets | Exponering | Secret management |
| Network | Oönskad åtkomst | Network isolation |

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera Non-root User i Dockerfile

Att köra som root i containers är en av de vanligaste säkerhetsriskerna.

```dockerfile
# Steg 1: Börja med minimal base image
FROM python:3.11-slim

# Steg 2: Skapa en dedikerad användare och grupp
RUN groupadd --gid 1000 appgroup && \\
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

# Steg 3: Sätt arbetskatalog
WORKDIR /home/appuser/app

# Steg 4: Kopiera filer med rätt ägare
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup . .

# Steg 5: Byt till non-root användare
USER appuser

# Steg 6: Definiera startkommando
CMD ["python", "main.py"]
```

### Steg 2: Sätta upp Image Scanning med Trivy

```bash
# Installera Trivy
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Scanna en image
trivy image python:3.11-slim

# Scanna med specifik severity
trivy image --severity HIGH,CRITICAL myapp:latest

# Ignorera unfixed vulnerabilities
trivy image --ignore-unfixed myapp:latest

# Exportera resultat som JSON
trivy image --format json --output results.json myapp:latest
```

### Steg 3: Konfigurera Docker Secrets

```bash
# Skapa en secret från fil
echo "SuperSecretPassword123" > db_password.txt
docker secret create db_password db_password.txt
rm db_password.txt

# Lista secrets
docker secret ls

# Använd secret i service (Swarm mode)
docker service create \\
    --name myapp \\
    --secret db_password \\
    myapp:latest
```

I containern läses secret från `/run/secrets/db_password`:

```python
# Python-kod för att läsa secret
def get_secret(secret_name):
    secret_path = f"/run/secrets/{secret_name}"
    try:
        with open(secret_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

db_password = get_secret("db_password")
```

### Steg 4: Konfigurera Network Isolation

```bash
# Skapa isolerat nätverk utan internet-access
docker network create --internal backend-network

# Skapa frontend-nätverk med internet-access
docker network create frontend-network

# Kör database endast på backend-nätverket
docker run -d \\
    --name postgres \\
    --network backend-network \\
    postgres:15

# Kör API på båda nätverken
docker run -d \\
    --name api \\
    --network backend-network \\
    myapi:latest

docker network connect frontend-network api

# Kör nginx endast på frontend
docker run -d \\
    --name nginx \\
    --network frontend-network \\
    -p 80:80 \\
    nginx:alpine
```

### Steg 5: Aktivera Resource Limits

```bash
# Kör container med resursbegränsningar
docker run -d \\
    --name myapp \\
    --memory=512m \\
    --memory-swap=512m \\
    --cpus=0.5 \\
    --pids-limit=100 \\
    --ulimit nofile=1024:1024 \\
    myapp:latest
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Säker Multi-stage Dockerfile

```dockerfile
# Build stage - kan köras som root
FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Production stage - körs som non-root
FROM python:3.11-slim AS production

# Säkerhetshärdning
RUN apt-get update && \\
    apt-get install -y --no-install-recommends \\
        ca-certificates && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/* && \\
    groupadd --gid 1000 app && \\
    useradd --uid 1000 --gid app --shell /bin/bash --create-home app

WORKDIR /home/app

# Kopiera wheels från builder
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Kopiera applikation
COPY --chown=app:app . .

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Exempel 2: Docker Compose med Säkerhetskonfiguration

```yaml
version: "3.8"

services:
  api:
    build: .
    user: "1000:1000"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    tmpfs:
      - /tmp:noexec,nosuid,size=100m
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 512M
          pids: 100
        reservations:
          memory: 256M
    networks:
      - frontend
      - backend
    secrets:
      - db_password
      - api_key

  postgres:
    image: postgres:15-alpine
    user: "999:999"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    tmpfs:
      - /tmp:noexec,nosuid
      - /run/postgresql:noexec,nosuid
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend
    secrets:
      - db_password
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password

networks:
  frontend:
  backend:
    internal: true

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    file: ./secrets/api_key.txt

volumes:
  postgres_data:
```

### Exempel 3: CI/CD Pipeline med Säkerhetsscanning

```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
          severity: CRITICAL,HIGH

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: trivy-results.sarif

      - name: Fail on critical vulnerabilities
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          exit-code: 1
          severity: CRITICAL
```

### Exempel 4: Seccomp Profile

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": [
        "accept", "access", "bind", "brk", "close",
        "connect", "dup", "dup2", "execve", "exit",
        "exit_group", "fstat", "futex", "getdents64",
        "getpid", "getuid", "listen", "lseek", "mmap",
        "mprotect", "munmap", "nanosleep", "open",
        "openat", "poll", "read", "recvfrom", "rt_sigaction",
        "rt_sigprocmask", "sendto", "set_robust_list",
        "set_tid_address", "socket", "stat", "write"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

Använd profilen:

```bash
docker run --security-opt seccomp=./seccomp-profile.json myapp:latest
```

------------------------------------------------------------

## Bästa Praxis

| Praxis | Beskrivning | Prioritet |
|--------|-------------|-----------|
| Non-root user | Kör alltid containers som non-root | Kritisk |
| Minimal images | Använd slim, alpine eller distroless | Hög |
| Specifika tags | Undvik :latest, använd sha256 digest | Hög |
| Image scanning | Scanna i CI/CD och regelbundet | Kritisk |
| Secret management | Använd Docker secrets eller Vault | Kritisk |
| Network isolation | Separera frontend och backend | Hög |
| Resource limits | Sätt alltid memory och CPU limits | Hög |
| Read-only filesystem | Aktivera där möjligt | Medium |
| Drop capabilities | Ta bort alla, lägg till minimalt | Hög |
| Content trust | Signera och verifiera images | Medium |

**Dockerfile Best Practices:**

```dockerfile
# 1. Använd specifik tag med digest
FROM python:3.11.7-slim@sha256:abc123...

# 2. Skapa non-root user tidigt
RUN useradd --create-home --shell /bin/bash app

# 3. Minimera lager och rensa cache
RUN apt-get update && \\
    apt-get install -y --no-install-recommends package && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*

# 4. Kopiera endast nödvändiga filer
COPY --chown=app:app src/ ./src/
COPY --chown=app:app requirements.txt .

# 5. Byt till non-root innan CMD
USER app

# 6. Använd HEALTHCHECK
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
```

**Signering av Images (Content Trust):**

```bash
# Aktivera Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# Signera och pusha image
docker push myregistry/myapp:1.0.0

# Verifiera signatur vid pull
docker pull myregistry/myapp:1.0.0
```

------------------------------------------------------------

## Vanliga Fallgropar

| Fallgrop | Problem | Lösning |
|----------|---------|---------|
| Köra som root | Container escape ger host access | Använd USER directive |
| :latest tag | Oförutsägbara uppdateringar | Använd specifika versioner |
| Secrets i ENV | Synliga i docker inspect | Använd Docker secrets |
| Secrets i image | Finns i alla lager | Multi-stage builds |
| Inga resource limits | DoS, påverkar andra containers | Sätt memory/CPU limits |
| Exponera alla portar | Onödig attack surface | Exponera endast nödvändiga |
| Privileged mode | Full host access | Undvik --privileged |
| Stora base images | Fler sårbarheter | Använd minimala images |

**Felaktig secret-hantering:**

```dockerfile
# DÅLIGT - secret i environment variable
ENV DATABASE_PASSWORD=secret123

# DÅLIGT - secret kopieras till image
COPY secrets/password.txt /app/

# BRA - använd build secrets (BuildKit)
RUN --mount=type=secret,id=db_pass \\
    cat /run/secrets/db_pass > /dev/null
```

**Felaktig nätverkskonfiguration:**

```bash
# DÅLIGT - exponerar port på alla interfaces
docker run -p 5432:5432 postgres

# BRA - exponerar endast på localhost
docker run -p 127.0.0.1:5432:5432 postgres

# BRA - använd internal network för databaser
docker network create --internal db-network
docker run --network db-network postgres
```

------------------------------------------------------------

## Övningar

### Övning 1: Säkra en Osäker Dockerfile

Givet följande osäkra Dockerfile, identifiera och åtgärda alla säkerhetsproblem:

```dockerfile
FROM ubuntu:latest
ENV DB_PASSWORD=admin123
RUN apt-get update && apt-get install -y python3 python3-pip curl wget vim
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 22 80 443 8080
CMD ["python3", "app.py"]
```

<details>
<summary>Ledtråd</summary>

Identifiera följande problem:
1. Base image - är ubuntu:latest säker och minimal?
2. Secrets - hur hanteras DB_PASSWORD?
3. Paket - behövs alla installerade paket?
4. User - vem kör applikationen?
5. Portar - behövs alla exponerade portar?
6. Tags - vad är problemet med :latest?

</details>

<details>
<summary>Lösning</summary>

```dockerfile
# 1. Specifik, minimal base image
FROM python:3.11-slim@sha256:abc123...

# 2. Skapa non-root user
RUN groupadd --gid 1000 app && \\
    useradd --uid 1000 --gid app --shell /bin/bash --create-home app

WORKDIR /home/app

# 3. Installera endast nödvändiga paket och rensa cache
RUN apt-get update && \\
    apt-get install -y --no-install-recommends ca-certificates && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*

# 4. Kopiera requirements först (cache-optimering)
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiera applikation med rätt ägare
COPY --chown=app:app . .

# 6. Byt till non-root user
USER app

# 7. Exponera endast nödvändig port
EXPOSE 8080

# 8. Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \\
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')"

CMD ["python", "app.py"]

# OBS: DB_PASSWORD ska hanteras via Docker secrets eller environment vid runtime
# INTE i Dockerfile
```

Förbättringar:
- Specifik Python slim image istället för ubuntu:latest
- Non-root user skapad och använd
- Minimal paketinstallation
- Secrets borttagen från Dockerfile
- Endast nödvändig port exponerad
- Healthcheck tillagd

</details>

### Övning 2: Konfigurera Nätverksisolering

Skapa en Docker Compose-konfiguration för en applikation med följande krav:
- Frontend (nginx) - ska vara tillgänglig från internet
- API (python) - ska kunna nås av frontend men inte direkt från internet
- Database (postgres) - ska endast kunna nås av API

<details>
<summary>Ledtråd</summary>

Du behöver:
1. Två nätverk - ett publikt och ett internt
2. Frontend på publikt nätverk med port-mapping
3. API på båda nätverken (bridge mellan frontend och backend)
4. Database endast på internt nätverk
5. Internt nätverk ska skapas med --internal flaggan

</details>

<details>
<summary>Lösning</summary>

```yaml
version: "3.8"

services:
  nginx:
    image: nginx:1.25-alpine
    ports:
      - "80:80"
      - "443:443"
    networks:
      - public
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
      - CHOWN
      - SETGID
      - SETUID

  api:
    build: ./api
    user: "1000:1000"
    networks:
      - public
      - internal
    environment:
      - DATABASE_HOST=postgres
      - DATABASE_PORT=5432
    secrets:
      - db_password
    depends_on:
      - postgres
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "0.5"

  postgres:
    image: postgres:15-alpine
    networks:
      - internal
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL

networks:
  public:
    driver: bridge
  internal:
    driver: bridge
    internal: true  # Ingen internet-access

secrets:
  db_password:
    file: ./secrets/db_password.txt

volumes:
  postgres_data:
```

Nätverkstopologi:
```
+------------------------------------------------------------------+
|                        INTERNET                                   |
+------------------------------------------------------------------+
                              |
                              | port 80/443
                              v
+------------------------------------------------------------------+
|                     PUBLIC NETWORK                                |
|  +------------------+              +------------------+           |
|  |      nginx       |  ----------> |       api        |           |
|  +------------------+              +------------------+           |
+------------------------------------------------------------------+
                                              |
                                              |
+------------------------------------------------------------------+
|                    INTERNAL NETWORK                               |
|                     +------------------+                          |
|                     |     postgres     |                          |
|                     +------------------+                          |
+------------------------------------------------------------------+
```

</details>

### Övning 3: Implementera Image Scanning i CI/CD

Skapa ett GitHub Actions workflow som:
1. Bygger en Docker image
2. Skannar imagen med Trivy
3. Misslyckas om CRITICAL sårbarheter hittas
4. Laddar upp scanningsresultat till GitHub Security tab

<details>
<summary>Ledtråd</summary>

Du behöver:
1. actions/checkout för att hämta kod
2. docker build för att bygga imagen
3. aquasecurity/trivy-action för scanning
4. Två Trivy-körningar: en för rapport, en för att faila på CRITICAL
5. github/codeql-action/upload-sarif för att ladda upp resultat

</details>

<details>
<summary>Lösning</summary>

```yaml
name: Container Security Scan

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 6 * * 1"  # Varje måndag kl 06:00

env:
  IMAGE_NAME: myapp
  REGISTRY: ghcr.io

jobs:
  build-and-scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
      packages: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          load: true
          tags: ${{ env.IMAGE_NAME }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Run Trivy vulnerability scanner (SARIF)
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: sarif
          output: trivy-results.sarif
          severity: CRITICAL,HIGH,MEDIUM

      - name: Upload Trivy scan results to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: trivy-results.sarif

      - name: Run Trivy and fail on CRITICAL
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: table
          exit-code: 1
          severity: CRITICAL
          ignore-unfixed: true

      - name: Generate SBOM
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: cyclonedx
          output: sbom.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v3
        with:
          name: sbom
          path: sbom.json

      - name: Login to GitHub Container Registry
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Push image
        if: github.event_name != 'pull_request'
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ env.REGISTRY }}/${{ github.repository }}:${{ github.sha }}
            ${{ env.REGISTRY }}/${{ github.repository }}:latest
```

Workflowet:
1. Bygger imagen med BuildKit och caching
2. Skannar och genererar SARIF-rapport för GitHub Security
3. Failar om CRITICAL sårbarheter hittas
4. Genererar Software Bill of Materials (SBOM)
5. Pushar imagen endast om inga kritiska sårbarheter finns

</details>

------------------------------------------------------------

## Kopplingar

| Ämne | Koppling till Docker Security |
|------|------------------------------|
| **Kubernetes** | Pod Security Standards, Network Policies, RBAC |
| **CI/CD** | Automated scanning, secure build pipelines |
| **Infrastructure as Code** | Terraform för säkra nätverk och secrets |
| **Monitoring** | Falco för runtime security monitoring |
| **Secret Management** | HashiCorp Vault, AWS Secrets Manager integration |
| **Compliance** | CIS Docker Benchmark, SOC2, HIPAA |

**Kubernetes Security Extensions:**

```yaml
# Pod Security Standard - Restricted
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:1.0.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
      resources:
        limits:
          memory: 512Mi
          cpu: 500m
```

**Falco Runtime Security:**

```yaml
# Falco regel för att detektera container escape
- rule: Container Escape via nsenter
  desc: Detect nsenter usage which may indicate container escape attempt
  condition: >
    spawned_process and
    container and
    proc.name = nsenter
  output: >
    Possible container escape via nsenter
    (user=%user.name command=%proc.cmdline container=%container.name)
  priority: CRITICAL
```

------------------------------------------------------------

## Sammanfattning

Docker-säkerhet kräver ett flerskiktat tillvägagångssätt där varje komponent bidrar till den totala säkerheten:

| Område | Nyckelåtgärd |
|--------|--------------|
| **User** | Kör alltid som non-root med USER directive |
| **Images** | Minimala base images, specifika tags, regelbunden scanning |
| **Secrets** | Docker secrets eller externa lösningar, aldrig i images |
| **Network** | Isolera med interna nätverk, exponera minimalt |
| **Resources** | Sätt alltid memory, CPU och PID limits |
| **Filesystem** | Read-only där möjligt, tmpfs för temporära filer |
| **Capabilities** | Drop ALL, lägg till endast nödvändiga |
| **Profiles** | Använd seccomp och AppArmor för extra skydd |

Säkerhet är inte en engångsåtgärd utan en kontinuerlig process:

```
+------------------------------------------------------------------+
|              KONTINUERLIG SAKERHETSCYKEL                          |
+------------------------------------------------------------------+
|                                                                   |
|    +----------+     +----------+     +----------+                 |
|    |  BUILD   | --> |   SCAN   | --> |  DEPLOY  |                 |
|    +----------+     +----------+     +----------+                 |
|         ^                                  |                      |
|         |                                  v                      |
|    +----------+     +----------+     +----------+                 |
|    |  UPDATE  | <-- | MONITOR  | <-- | RUNTIME  |                 |
|    +----------+     +----------+     +----------+                 |
|                                                                   |
+------------------------------------------------------------------+
```

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker run --user 1000:1000` | Kör container som specifik user |
| `docker run --read-only` | Read-only root filesystem |
| `docker run --cap-drop=ALL` | Ta bort alla capabilities |
| `docker run --cap-add=NET_BIND_SERVICE` | Lägg till specifik capability |
| `docker run --memory=512m` | Sätt memory limit |
| `docker run --cpus=0.5` | Sätt CPU limit |
| `docker run --pids-limit=100` | Sätt process limit |
| `docker run --security-opt=no-new-privileges` | Förhindra privilege escalation |
| `docker run --network=none` | Ingen nätverksåtkomst |
| `docker network create --internal` | Skapa internt nätverk |
| `docker secret create` | Skapa Docker secret |
| `trivy image <image>` | Scanna image för sårbarheter |
| `docker scout cves <image>` | Docker's inbyggda scanning |
| `docker trust sign` | Signera image |
| `export DOCKER_CONTENT_TRUST=1` | Aktivera content trust |

------------------------------------------------------------

## Referenser

| Resurs | Länk |
|--------|------|
| Docker Security Best Practices | https://docs.docker.com/develop/security-best-practices/ |
| CIS Docker Benchmark | https://www.cisecurity.org/benchmark/docker |
| OWASP Docker Security | https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html |
| Trivy Documentation | https://aquasecurity.github.io/trivy/ |
| Snyk Container Security | https://snyk.io/product/container-vulnerability-management/ |
| Docker Content Trust | https://docs.docker.com/engine/security/trust/ |
| Linux Capabilities | https://man7.org/linux/man-pages/man7/capabilities.7.html |
| Seccomp Profiles | https://docs.docker.com/engine/security/seccomp/ |
| Falco Runtime Security | https://falco.org/docs/ |
| NIST Container Security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf |
""",
        },
        {
            "title": "Docker in Production",
            "slug": "docker-in-production",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker in Production

------------------------------------------------------------

## Introduktion

Att kora Docker i produktion skiljer sig drastiskt fran lokal utveckling. I produktion maste dina containers vara stabila, observerbara och hantera fel graciost. Denna nod ger dig verktygen for att kora Docker-applikationer med enterprise-kvalitet.

Produktion kraver att du tanker pa:

- Hur containers aterhamtar sig fran crashes
- Hur du samlar och analyserar loggar centralt
- Hur du overvakar prestanda och halsa i realtid
- Hur du uppdaterar utan avbrott for anvandarna

En container som fungerar perfekt lokalt kan kollapsa i produktion utan ratt konfiguration. Skillnaden ligger i restart policies, resource limits, health checks och robust logging - alla amnen vi tar upp har.

------------------------------------------------------------

## Teori

### Production-Ready Checklist

Innan en container gar till produktion, validera foljande:

```
+---------------------------------------------------------------+
|              PRODUCTION-READY CHECKLIST                       |
+---------------------------------------------------------------+
|                                                               |
|  [ ] Health check konfigurerad                                |
|  [ ] Resource limits (CPU/memory) satta                       |
|  [ ] Restart policy definierad                                |
|  [ ] Logging driver konfigurerad                              |
|  [ ] Secrets hanteras sakert (ej i image)                     |
|  [ ] Non-root user i container                                |
|  [ ] Read-only filesystem dar mojligt                         |
|  [ ] Network policies definierade                             |
|  [ ] Backup-strategi dokumenterad                             |
|  [ ] Rollback-plan testad                                     |
|                                                               |
+---------------------------------------------------------------+
```

### Restart Policies

Docker kan automatiskt starta om containers som kraschar:

| Policy | Beteende | Anvandning |
|--------|----------|------------|
| no | Starta aldrig om | Test och debug |
| always | Starta alltid om | Kritiska services |
| unless-stopped | Som always, men ej om manuellt stoppad | Production standard |
| on-failure:N | Endast vid crash, max N forsok | Batch jobs |

### Logging Strategies

Loggar ar din enda insyn i vad som hander i produktion:

```
+---------------------------------------------------------------+
|                   LOGGING ARKITEKTUR                          |
+---------------------------------------------------------------+
|                                                               |
|   Container 1 ----+                                           |
|                   |     +-------------+     +-----------+     |
|   Container 2 ----+---->| Log Driver  |---->| Centralt  |     |
|                   |     | (fluentd)   |     | (ELK/Loki)|     |
|   Container 3 ----+     +-------------+     +-----------+     |
|                                                               |
|   Log Drivers:                                                |
|   - json-file : Default, lokal fil                            |
|   - syslog    : System syslog daemon                          |
|   - fluentd   : Fluentd log collector                         |
|   - awslogs   : AWS CloudWatch                                |
|   - gcplogs   : Google Cloud Logging                          |
|                                                               |
+---------------------------------------------------------------+
```

### Monitoring med Prometheus och Grafana

Prometheus scrapar metrics fran dina containers och Grafana visualiserar dem:

```
+---------------------------------------------------------------+
|              MONITORING STACK                                 |
+---------------------------------------------------------------+
|                                                               |
|   +----------+     +------------+     +-----------+           |
|   | Container|---->| cAdvisor   |---->| Prometheus|           |
|   | metrics  |     | (exporter) |     | (scrape)  |           |
|   +----------+     +------------+     +-----------+           |
|                                             |                 |
|                                             v                 |
|                                       +-----------+           |
|                                       | Grafana   |           |
|                                       | (dashoard)|           |
|                                       +-----------+           |
|                                                               |
|   Metrics att overvaka:                                       |
|   - CPU-anvandning per container                              |
|   - Minnesanvandning och limits                               |
|   - Natverk I/O                                               |
|   - Container restart count                                   |
|   - Health check status                                       |
|                                                               |
+---------------------------------------------------------------+
```

### Health Checks och Readiness

Docker stodjer tva typer av halsokonroll:

- Liveness: Ar containern vid liv? Om inte, starta om den
- Readiness: Ar containern redo att ta emot trafik?

```
+---------------------------------------------------------------+
|              HEALTH CHECK FLODE                               |
+---------------------------------------------------------------+
|                                                               |
|   Container startar                                           |
|        |                                                      |
|        v                                                      |
|   [start-period: 30s] <-- Grace period for uppstart           |
|        |                                                      |
|        v                                                      |
|   +--------------------+                                      |
|   | Health Check       |<--+                                  |
|   | (var 30:e sekund)  |   |                                  |
|   +--------------------+   |                                  |
|        |                   |                                  |
|   OK?  +----> JA ----------+ (fortsatt kora)                  |
|        |                                                      |
|        +----> NEJ (3 retries) ----> UNHEALTHY                 |
|                                          |                    |
|                                          v                    |
|                                    Restart container          |
|                                                               |
+---------------------------------------------------------------+
```

### Resource Management

Utan limits kan en container konsumera all host-resurser:

| Resource | Flag | Exempel |
|----------|------|---------|
| CPU | --cpus | --cpus="1.5" (1.5 CPU cores) |
| Memory | --memory | --memory="512m" |
| Memory Swap | --memory-swap | --memory-swap="1g" |
| CPU Shares | --cpu-shares | --cpu-shares=512 (relativ vikt) |

### Rolling Updates och Zero-Downtime

```
+---------------------------------------------------------------+
|              ROLLING UPDATE STRATEGI                          |
+---------------------------------------------------------------+
|                                                               |
|   Tid    Container 1    Container 2    Container 3            |
|   ---    -----------    -----------    -----------            |
|   T0     [  v1.0   ]    [  v1.0   ]    [  v1.0   ]            |
|          (running)      (running)      (running)              |
|                                                               |
|   T1     [  v2.0   ]    [  v1.0   ]    [  v1.0   ]            |
|          (starting)     (running)      (running)              |
|                                                               |
|   T2     [  v2.0   ]    [  v2.0   ]    [  v1.0   ]            |
|          (running)      (starting)     (running)              |
|                                                               |
|   T3     [  v2.0   ]    [  v2.0   ]    [  v2.0   ]            |
|          (running)      (running)      (starting)             |
|                                                               |
|   T4     [  v2.0   ]    [  v2.0   ]    [  v2.0   ]            |
|          (running)      (running)      (running)              |
|                                                               |
|   Fordelar: Ingen downtime, gradvis rollout                   |
|   Krav: Health checks for att validera nya instanser          |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera Restart Policy

```bash
# For enskild container
docker run -d \\
    --name api \\
    --restart unless-stopped \\
    myapp:latest

# Verifiera policy
docker inspect --format='{{.HostConfig.RestartPolicy.Name}}' api
```

### Steg 2: Satt Resource Limits

```bash
# Starta med limits
docker run -d \\
    --name api \\
    --cpus="1.0" \\
    --memory="512m" \\
    --memory-swap="1g" \\
    myapp:latest

# Verifiera limits
docker stats api --no-stream
```

### Steg 3: Lagg till Health Check

```dockerfile
# I Dockerfile
FROM python:3.11-slim

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
```

### Steg 4: Konfigurera Logging

```bash
# Med json-file driver och rotation
docker run -d \\
    --name api \\
    --log-driver json-file \\
    --log-opt max-size=10m \\
    --log-opt max-file=5 \\
    myapp:latest

# Med fluentd for centraliserad logging
docker run -d \\
    --name api \\
    --log-driver fluentd \\
    --log-opt fluentd-address=localhost:24224 \\
    --log-opt tag="docker.{{.Name}}" \\
    myapp:latest
```

### Steg 5: Satt upp Reverse Proxy med Traefik

```yaml
# docker-compose.yml
services:
  traefik:
    image: traefik:v2.10
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro

  api:
    image: myapp:latest
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`api.example.com`)"
      - "traefik.http.services.api.loadbalancer.server.port=8000"
    deploy:
      replicas: 3
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett Production Compose

```yaml
# docker-compose.prod.yml
version: "3.8"

services:
  api:
    image: myregistry/api:${VERSION:-latest}
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
        reservations:
          cpus: "0.5"
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      start_period: 30s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"
    environment:
      - NODE_ENV=production
    secrets:
      - db_password
    networks:
      - backend

  nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      api:
        condition: service_healthy
    networks:
      - backend

secrets:
  db_password:
    file: ./secrets/db_password.txt

networks:
  backend:
    driver: bridge
```

### Exempel 2: Prometheus Monitoring Setup

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
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=secret
    restart: unless-stopped

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
```

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "cadvisor"
    static_configs:
      - targets: ["cadvisor:8080"]

  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
```

### Exempel 3: Nginx Reverse Proxy Config

```nginx
# nginx.conf
upstream api_servers {
    least_conn;
    server api:8000 weight=1 max_fails=3 fail_timeout=30s;
}

server {
    listen 80;
    server_name api.example.com;

    location /health {
        access_log off;
        return 200 "OK";
    }

    location / {
        proxy_pass http://api_servers;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

------------------------------------------------------------

## Bästa Praxis

### Restart Policies

- Anvand unless-stopped for production services
- Anvand on-failure:5 for batch jobs som inte ska loopa
- Undvik always om du behover kunna stoppa manuellt

### Logging

- Satt alltid max-size och max-file for json-file driver
- Anvand strukturerad JSON-logging i applikationen
- Centralisera loggar med fluentd eller liknande i storre miljoer

### Health Checks

- Implementera alltid health checks i produktion
- Anvand start-period for att ge applikationen tid att starta
- Halsokontroll ska vara snabb och billig

### Resource Limits

- Satt alltid memory limits for att undvika OOM pa hosten
- Anvand CPU reservations for garanterad prestanda
- Overvaka faktisk anvandning och justera limits

### Reverse Proxy

- Anvand alltid en reverse proxy framfor dina containers
- Traefik for dynamisk konfiguration via Docker labels
- Nginx for mer kontroll och caching

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Ingen restart policy

```bash
# Fel - container dor permanent vid crash
docker run -d myapp

# Ratt - aterstart automatiskt
docker run -d --restart unless-stopped myapp
```

### Fallgrop 2: Obegransade resurser

```bash
# Fel - kan ta ner hela hosten
docker run -d myapp

# Ratt - begransat till 512MB minne
docker run -d --memory="512m" myapp
```

### Fallgrop 3: Ingen log rotation

```yaml
# Fel - loggar vaxer okontrollerat
services:
  api:
    image: myapp

# Ratt - rotation konfigurerad
services:
  api:
    image: myapp
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"
```

### Fallgrop 4: Health check utan start-period

```dockerfile
# Fel - markeras unhealthy innan app hunnit starta
HEALTHCHECK --interval=5s --retries=1 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Ratt - ger 30 sekunder for uppstart
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1
```

### Fallgrop 5: Hardkodade secrets

```yaml
# Fel - secrets i compose-filen
services:
  api:
    environment:
      - DB_PASSWORD=secret123

# Ratt - anvand Docker secrets
services:
  api:
    secrets:
      - db_password
secrets:
  db_password:
    external: true
```

------------------------------------------------------------

## Övningar

### Ovning 1: Production-Ready Container

Skapa en docker-compose.yml for en web-applikation med:
- Restart policy unless-stopped
- Memory limit 256MB
- Health check som kollar /health var 30:e sekund
- Log rotation (max 5 filer, 10MB vardera)

<details>
<summary>Ledtrad</summary>

Anvand deploy.resources.limits for memory, healthcheck-blocket for halsokonroll, och logging.options for rotation.

</details>

<details>
<summary>Losning</summary>

```yaml
version: "3.8"

services:
  webapp:
    image: nginx:alpine
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      start_period: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"
    ports:
      - "80:80"
```

</details>

### Ovning 2: Monitoring Stack

Konfigurera cAdvisor och Prometheus for att overvaka dina containers. Skapa prometheus.yml som scrapar cAdvisor var 15:e sekund.

<details>
<summary>Ledtrad</summary>

cAdvisor exponerar metrics pa port 8080. Prometheus behover en scrape_configs sektion som pekar pa cadvisor:8080.

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.yml
services:
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    ports:
      - "8080:8080"

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
```

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "cadvisor"
    static_configs:
      - targets: ["cadvisor:8080"]
```

</details>

### Ovning 3: Zero-Downtime Deploy

Implementera en blue-green deployment med docker compose. Skapa tva compose-filer (blue och green) och skriv ett bash-script som byter mellan dem.

<details>
<summary>Ledtrad</summary>

Anvand -p flaggan for att ge projektnamn. Starta green, verifiera health, uppdatera reverse proxy, stoppa blue.

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.blue.yml
services:
  api:
    image: myapp:v1
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    ports:
      - "8001:8000"
```

```yaml
# docker-compose.green.yml
services:
  api:
    image: myapp:v2
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    ports:
      - "8002:8000"
```

```bash
#!/bin/bash
# deploy.sh

# Starta green
docker compose -f docker-compose.green.yml -p green up -d

# Vanta pa health
sleep 30

# Verifiera
if curl -f http://localhost:8002/health; then
    echo "Green ar uppe, byter trafik..."
    # Har uppdaterar du reverse proxy
    docker compose -f docker-compose.blue.yml -p blue down
    echo "Deploy klar!"
else
    echo "Green misslyckades, rullar tillbaka"
    docker compose -f docker-compose.green.yml -p green down
fi
```

</details>

------------------------------------------------------------

## Kopplingar

| Amne | Koppling |
|------|----------|
| Docker Compose | Grund for multi-container production setup |
| Docker Networks | Isolering och kommunikation i produktion |
| Docker Security | Sakerhetsaspekter av production deployment |
| Kubernetes | Nasta steg for container orchestration |
| CI/CD | Automatiserad deployment pipeline |

------------------------------------------------------------

## Sammanfattning

Att kora Docker i produktion kraver omtanke kring flera omraden:

- Restart policies sakerstaller att containers aterstartar vid crash
- Resource limits skyddar hosten fran resurshungriga containers
- Health checks ger Docker information om containerns tillstand
- Centraliserad logging ar nodvandigt for felsokningi
- Monitoring med Prometheus och Grafana ger realtidsinsikt
- Reverse proxies hanterar lastbalansering och SSL
- Rolling updates mojliggor zero-downtime deploys

Planera alltid for failure - containers kommer krascha. Det viktiga ar hur snabbt och automatiskt systemet aterhamtar sig.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| docker run --restart unless-stopped | Satt restart policy |
| docker run --memory="512m" | Begansa minne |
| docker run --cpus="1.0" | Begransa CPU |
| docker stats | Visa resursanvandning |
| docker logs -f container | Folja loggar |
| docker inspect --format | Hamta specifik metadata |
| docker compose up -d | Starta i bakgrunden |
| docker compose down | Stoppa och ta bort |

------------------------------------------------------------

## Referenser

| Resurs | Lank |
|--------|------|
| Docker Production Best Practices | https://docs.docker.com/develop/dev-best-practices/ |
| Docker Logging Drivers | https://docs.docker.com/config/containers/logging/configure/ |
| Prometheus Documentation | https://prometheus.io/docs/introduction/overview/ |
| Grafana Documentation | https://grafana.com/docs/ |
| Traefik Documentation | https://doc.traefik.io/traefik/ |
| cAdvisor | https://github.com/google/cadvisor |
""",
        },
        {
            "title": "Docker Registry & Image Distribution",
            "slug": "docker-registry-image-distribution",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Registry & Image Distribution

------------------------------------------------------------

## Introduktion

Docker registries ar centrala lagringsplatser for container images. De mojliggor distribution av images mellan utvecklare, CI/CD-pipelines och produktionsmiljoer. Utan ett registry skulle varje server behova bygga images lokalt, vilket ar ineffektivt och skapar inkonsistens.

Ett registry fungerar som ett versionskontrollsystem for container images. Du pushar nya versioner, pullar specifika taggar och kan spara historik for rollback. For foretag ar private registries kritiska for att skydda proprietar kod och uppfylla compliance-krav.

```
+---------------------------------------------------------------+
|                    REGISTRY EKOSYSTEM                         |
+---------------------------------------------------------------+
|                                                               |
|   Developer        CI/CD Pipeline        Production           |
|       |                  |                    |                |
|       v                  v                    v                |
|   +-------+          +-------+           +-------+            |
|   | Build |          | Build |           |  Pull |            |
|   +---+---+          +---+---+           +---+---+            |
|       |                  |                    ^                |
|       v                  v                    |                |
|   +---------------------------------------------------+       |
|   |              CONTAINER REGISTRY                   |       |
|   |  +----------+  +----------+  +----------+        |       |
|   |  | myapp:v1 |  | myapp:v2 |  | myapp:v3 |        |       |
|   |  +----------+  +----------+  +----------+        |       |
|   +---------------------------------------------------+       |
|                                                               |
+---------------------------------------------------------------+
```

I denna modul lar du dig:

- Arbeta med Docker Hub (public och private repositories)
- Satta upp och anvanda private registries
- Konfigurera cloud registries (ECR, GCR, ACR)
- Implementera effektiva tagging-strategier
- Hantera autentisering och sakerhet
- Skapa policies for image cleanup och retention

------------------------------------------------------------

## Teori

### Vad ar ett Container Registry?

Ett container registry ar en lagringstjanst for container images. Nar du bygger en image lokalt finns den bara pa din maskin. For att dela den med andra eller deploya till servers maste den lagras i ett registry.

```
+---------------------------------------------------------------+
|                 IMAGE NAMING CONVENTION                       |
+---------------------------------------------------------------+
|                                                               |
|   [registry]/[namespace]/[repository]:[tag]                   |
|                                                               |
|   Komponenter:                                                |
|   +------------------+----------------------------------------+
|   | registry         | Var imagen lagras (default: docker.io)|
|   | namespace        | Organisation eller anvandare          |
|   | repository       | Imagenamn                             |
|   | tag              | Version (default: latest)             |
|   +------------------+----------------------------------------+
|                                                               |
|   Exempel:                                                    |
|   docker.io/library/nginx:1.25-alpine                         |
|   gcr.io/my-project/api-server:v2.1.0                        |
|   123456789.dkr.ecr.eu-north-1.amazonaws.com/backend:abc123  |
|   ghcr.io/myorg/frontend:main-20241210                       |
|                                                               |
+---------------------------------------------------------------+
```

### Registry-typer och Anvandningsomraden

| Registry-typ | Beskrivning | Anvandning |
|--------------|-------------|------------|
| **Public** | Oppet for alla att pulla | Open source, base images |
| **Private** | Krav pa autentisering | Foretagsapplikationer |
| **Self-hosted** | Driftas i egen infrastruktur | On-premise, air-gapped |
| **Cloud-managed** | Driftas av molnleverantor | AWS, GCP, Azure |

### Registry-arkitektur

```
+---------------------------------------------------------------+
|                   REGISTRY ARKITEKTUR                         |
+---------------------------------------------------------------+
|                                                               |
|   +-------------------+                                       |
|   |   Docker Client   |                                       |
|   +--------+----------+                                       |
|            |                                                  |
|            | HTTPS (TLS)                                      |
|            v                                                  |
|   +-------------------+      +-------------------+            |
|   |   Registry API    |----->|   Authentication  |            |
|   |   (v2)            |      |   (OAuth/Basic)   |            |
|   +--------+----------+      +-------------------+            |
|            |                                                  |
|            v                                                  |
|   +-------------------+      +-------------------+            |
|   |   Blob Storage    |<---->|   Manifest Store  |            |
|   |   (layers)        |      |   (metadata)      |            |
|   +-------------------+      +-------------------+            |
|                                                               |
+---------------------------------------------------------------+
```

### Image Layers och Distribution

Nar du pullar en image hamtas endast de lager som inte redan finns lokalt. Detta gor distribution effektiv:

```
+---------------------------------------------------------------+
|               LAYER DISTRIBUTION                              |
+---------------------------------------------------------------+
|                                                               |
|   Forsta pull (alla lager hamtas):                           |
|   +-------+  +-------+  +-------+  +-------+                 |
|   |Layer 1|  |Layer 2|  |Layer 3|  |Layer 4|  = 500 MB       |
|   +-------+  +-------+  +-------+  +-------+                 |
|       |          |          |          |                      |
|       v          v          v          v                      |
|   [Registry] --------------------------------> [Local]        |
|                                                               |
|   Andra pull (delade lager cachas):                          |
|   +-------+  +-------+  +-------+  +-------+                 |
|   |Layer 1|  |Layer 2|  |Layer 3|  |Layer 5|  = 50 MB        |
|   +-------+  +-------+  +-------+  +-------+                 |
|   [cached]   [cached]   [cached]      |                      |
|                                       v                       |
|   [Registry] --------------------------------> [Local]        |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### 1. Docker Hub - Public och Private Repositories

Docker Hub ar standardregistryt for Docker. Du far ett gratis konto med obegransade public repos och ett private repo.

```bash
# Steg 1: Logga in pa Docker Hub
docker login
# Ange anvandarnman och losenord

# Steg 2: Tagga din image for Docker Hub
docker tag myapp:latest username/myapp:v1.0.0

# Steg 3: Pusha till Docker Hub
docker push username/myapp:v1.0.0

# Steg 4: Pulla fran Docker Hub (annan maskin)
docker pull username/myapp:v1.0.0

# Lista taggar i repository
docker search username/myapp
```

### 2. Satta upp ett Private Registry

For fullstandig kontroll kan du kora ett eget registry:

```bash
# Steg 1: Starta registry-container
docker run -d \
  --name registry \
  --restart=always \
  -p 5000:5000 \
  -v registry-data:/var/lib/registry \
  registry:2

# Steg 2: Tagga image for lokalt registry
docker tag myapp:latest localhost:5000/myapp:v1.0.0

# Steg 3: Pusha till lokalt registry
docker push localhost:5000/myapp:v1.0.0

# Steg 4: Verifiera att imagen finns
curl http://localhost:5000/v2/_catalog
# Output: {"repositories":["myapp"]}

# Lista taggar for en image
curl http://localhost:5000/v2/myapp/tags/list
# Output: {"name":"myapp","tags":["v1.0.0"]}
```

### 3. Registry med TLS och Autentisering

```bash
# Skapa kataloger for certifikat och auth
mkdir -p /opt/registry/{certs,auth,data}

# Generera sjalvsignerat certifikat
openssl req -newkey rsa:4096 -nodes -sha256 \
  -keyout /opt/registry/certs/domain.key \
  -x509 -days 365 \
  -out /opt/registry/certs/domain.crt \
  -subj "/CN=registry.example.com"

# Skapa htpasswd-fil for autentisering
docker run --rm --entrypoint htpasswd \
  httpd:2 -Bbn admin secretpassword > /opt/registry/auth/htpasswd

# Starta registry med TLS och auth
docker run -d \
  --name secure-registry \
  --restart=always \
  -p 443:5000 \
  -v /opt/registry/data:/var/lib/registry \
  -v /opt/registry/certs:/certs \
  -v /opt/registry/auth:/auth \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  registry:2

# Logga in pa secure registry
docker login registry.example.com
```

### 4. AWS ECR (Elastic Container Registry)

```bash
# Steg 1: Skapa ECR repository via AWS CLI
aws ecr create-repository \
  --repository-name myapp \
  --region eu-north-1

# Steg 2: Hamta inloggningstoken (giltig 12 timmar)
aws ecr get-login-password --region eu-north-1 | \
  docker login --username AWS --password-stdin \
  123456789012.dkr.ecr.eu-north-1.amazonaws.com

# Steg 3: Tagga och pusha
docker tag myapp:latest \
  123456789012.dkr.ecr.eu-north-1.amazonaws.com/myapp:v1.0.0

docker push \
  123456789012.dkr.ecr.eu-north-1.amazonaws.com/myapp:v1.0.0

# Lista images i repository
aws ecr list-images --repository-name myapp --region eu-north-1
```

### 5. Google Container Registry (GCR) / Artifact Registry

```bash
# Steg 1: Konfigurera Docker att anvanda gcloud
gcloud auth configure-docker

# For Artifact Registry (rekommenderat):
gcloud auth configure-docker europe-north1-docker.pkg.dev

# Steg 2: Tagga image
# GCR format:
docker tag myapp:latest gcr.io/my-project-id/myapp:v1.0.0

# Artifact Registry format:
docker tag myapp:latest \
  europe-north1-docker.pkg.dev/my-project-id/my-repo/myapp:v1.0.0

# Steg 3: Pusha
docker push gcr.io/my-project-id/myapp:v1.0.0
```

### 6. Azure Container Registry (ACR)

```bash
# Steg 1: Skapa ACR via Azure CLI
az acr create \
  --resource-group myResourceGroup \
  --name myregistry \
  --sku Basic

# Steg 2: Logga in
az acr login --name myregistry

# Steg 3: Tagga och pusha
docker tag myapp:latest myregistry.azurecr.io/myapp:v1.0.0
docker push myregistry.azurecr.io/myapp:v1.0.0

# Lista repositories
az acr repository list --name myregistry --output table
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: CI/CD Pipeline med Docker Hub

```yaml
# .github/workflows/docker-publish.yml
name: Build and Push Docker Image

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: docker.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix=

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

### Exempel 2: AWS ECR med Lifecycle Policy

```bash
# Skapa lifecycle policy for automatisk cleanup
cat > lifecycle-policy.json << 'EOF'
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Keep last 10 tagged images",
      "selection": {
        "tagStatus": "tagged",
        "tagPrefixList": ["v"],
        "countType": "imageCountMoreThan",
        "countNumber": 10
      },
      "action": {
        "type": "expire"
      }
    },
    {
      "rulePriority": 2,
      "description": "Delete untagged images older than 7 days",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 7
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
EOF

# Applicera policy
aws ecr put-lifecycle-policy \
  --repository-name myapp \
  --lifecycle-policy-text file://lifecycle-policy.json
```

### Exempel 3: Registry Mirroring for Hog Tillganglighet

```yaml
# docker-compose.yml for registry mirror setup
version: '3.8'

services:
  registry-primary:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - primary-data:/var/lib/registry
      - ./config-primary.yml:/etc/docker/registry/config.yml
    environment:
      REGISTRY_HTTP_SECRET: shared-secret-key

  registry-mirror:
    image: registry:2
    ports:
      - "5001:5000"
    volumes:
      - mirror-data:/var/lib/registry
      - ./config-mirror.yml:/etc/docker/registry/config.yml
    environment:
      REGISTRY_HTTP_SECRET: shared-secret-key
      REGISTRY_PROXY_REMOTEURL: http://registry-primary:5000

volumes:
  primary-data:
  mirror-data:
```

```yaml
# config-mirror.yml - Registry som mirror/cache
version: 0.1
log:
  level: info
storage:
  filesystem:
    rootdirectory: /var/lib/registry
  delete:
    enabled: true
http:
  addr: :5000
proxy:
  remoteurl: http://registry-primary:5000
```

### Exempel 4: Multi-Registry Distribution Script

```bash
#!/bin/bash
# distribute-image.sh - Pusha samma image till flera registries

set -e

IMAGE_NAME=$1
VERSION=$2

if [[ -z "$IMAGE_NAME" || -z "$VERSION" ]]; then
    echo "Usage: $0 <image-name> <version>"
    exit 1
fi

# Registries att pusha till
REGISTRIES=(
    "docker.io/myorg"
    "ghcr.io/myorg"
    "123456789012.dkr.ecr.eu-north-1.amazonaws.com"
)

# Bygga lokalt forst
echo "Building ${IMAGE_NAME}:${VERSION}..."
docker build -t "${IMAGE_NAME}:${VERSION}" .

# Pusha till varje registry
for REGISTRY in "${REGISTRIES[@]}"; do
    echo ""
    echo "Pushing to ${REGISTRY}..."

    FULL_TAG="${REGISTRY}/${IMAGE_NAME}:${VERSION}"

    docker tag "${IMAGE_NAME}:${VERSION}" "${FULL_TAG}"
    docker push "${FULL_TAG}"

    echo "Successfully pushed to ${REGISTRY}"
done

echo ""
echo "Image distributed to all registries!"
```

------------------------------------------------------------

## Bästa Praxis

### Tagging-strategier

| Strategi | Format | Anvandning |
|----------|--------|------------|
| **Semantic Versioning** | `v1.2.3` | Releases, stabil kod |
| **Git SHA** | `abc123f` | CI/CD, sparbarhet |
| **Branch + Date** | `main-20241210` | Development |
| **Combined** | `v1.2.3-abc123f` | Bast av bada varldar |

```bash
# Rekommenderad tagging i CI/CD
VERSION="1.2.3"
SHA=$(git rev-parse --short HEAD)
DATE=$(date +%Y%m%d)

# Tagga med flera taggar
docker tag myapp:latest myapp:${VERSION}
docker tag myapp:latest myapp:${VERSION}-${SHA}
docker tag myapp:latest myapp:${SHA}
```

### Sakerhetsrekommendationer

| Praxis | Beskrivning |
|--------|-------------|
| **Undvik latest** | Anvand alltid specifika taggar i produktion |
| **Image signing** | Signera images med Docker Content Trust |
| **Vulnerability scanning** | Skanna images for sakerhetsproblem |
| **Minimal base images** | Anvand alpine eller distroless |
| **Credential rotation** | Rotera registry-credentials regelbundet |

```bash
# Aktivera Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# Signera och pusha
docker push myregistry/myapp:v1.0.0
# Docker fragar efter signing key

# Verifiera signatur vid pull
docker pull myregistry/myapp:v1.0.0
```

### Image Cleanup och Retention

```bash
# Lokal cleanup - ta bort oanvanda images
docker image prune -a --filter "until=168h"  # Aldre an 7 dagar

# Lista images sorterade pa storlek
docker images --format "{{.Size}}\t{{.Repository}}:{{.Tag}}" | sort -h

# Ta bort specifika taggar fran registry (self-hosted)
# Kraver REGISTRY_STORAGE_DELETE_ENABLED=true
curl -X DELETE \
  https://registry.example.com/v2/myapp/manifests/sha256:abc123...
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Anvanda latest-taggen i produktion

```
+---------------------------------------------------------------+
|                    PROBLEM: latest TAG                        |
+---------------------------------------------------------------+
|                                                               |
|   Deployment 1        Deployment 2        Deployment 3        |
|   (Mandag)            (Tisdag)            (Onsdag)            |
|       |                   |                   |               |
|       v                   v                   v               |
|   myapp:latest        myapp:latest        myapp:latest        |
|   (version A)         (version B)         (version C)         |
|                                                               |
|   Problem: Vilken version kor i produktion?                   |
|   Rollback: Till vilken version?                              |
|                                                               |
+---------------------------------------------------------------+
|                                                               |
|   LOSNING: Anvand specifika taggar                            |
|                                                               |
|   myapp:v1.0.0  -->  myapp:v1.1.0  -->  myapp:v1.2.0         |
|                                                               |
+---------------------------------------------------------------+
```

### Fallgrop 2: Credentials i Dockerfile

```dockerfile
# FEL - credentials exponeras i image layers
FROM node:18
ARG NPM_TOKEN
RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" >> .npmrc
RUN npm install
# Token finns kvar i image history!

# RATT - anvand multi-stage builds
FROM node:18 AS builder
ARG NPM_TOKEN
RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" >> .npmrc
RUN npm install
RUN rm .npmrc

FROM node:18-slim
COPY --from=builder /app/node_modules ./node_modules
# Token finns INTE i final image
```

### Fallgrop 3: Ingen garbage collection

```bash
# Problem: Registry vaxer okontrollerat
# Losning: Konfigurera garbage collection

# For self-hosted registry:
docker exec registry bin/registry garbage-collect \
  /etc/docker/registry/config.yml

# Schemalag regelbunden cleanup (crontab)
0 3 * * 0 docker exec registry bin/registry garbage-collect /etc/docker/registry/config.yml
```

### Fallgrop 4: Saknad layer caching i CI/CD

```yaml
# FEL - ingen caching, bygger alltid fran scratch
- name: Build
  run: docker build -t myapp:${{ github.sha }} .

# RATT - anvand cache fran registry
- name: Build with cache
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myapp:${{ github.sha }}
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

------------------------------------------------------------

## Övningar

### Ovning 1: Konfigurera Private Registry med TLS

Satt upp ett lokalt Docker registry med TLS-certifikat och basic authentication.

**Krav:**
- Registry ska kora pa port 5000
- TLS med sjalvsignerat certifikat
- Basic auth med minst en anvandare
- Pusha och pulla en testimage

<details>
<summary>Ledtrad</summary>

Anvand openssl for att generera certifikat. Skapa htpasswd-fil med httpd-imagen. Konfigurera registry med miljovariablerna REGISTRY_HTTP_TLS_* och REGISTRY_AUTH_*.

</details>

<details>
<summary>Losning</summary>

```bash
# Skapa kataloger
mkdir -p ~/registry/{certs,auth,data}
cd ~/registry

# Generera certifikat
openssl req -newkey rsa:4096 -nodes -sha256 \
  -keyout certs/registry.key \
  -x509 -days 365 \
  -out certs/registry.crt \
  -subj "/CN=localhost"

# Skapa anvandare
docker run --rm --entrypoint htpasswd \
  httpd:2 -Bbn testuser testpass > auth/htpasswd

# Starta registry
docker run -d \
  --name secure-registry \
  -p 5000:5000 \
  -v $(pwd)/data:/var/lib/registry \
  -v $(pwd)/certs:/certs \
  -v $(pwd)/auth:/auth \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/registry.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/registry.key \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM="Registry" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  registry:2

# Lagg till certifikat som betrott (macOS)
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain certs/registry.crt

# Logga in och testa
docker login localhost:5000 -u testuser -p testpass
docker tag alpine:latest localhost:5000/test:v1
docker push localhost:5000/test:v1
docker pull localhost:5000/test:v1
```

</details>

### Ovning 2: Implementera Multi-Tag Strategy

Skapa ett shell-script som bygger en Docker image och taggar den med flera taggar enligt bast praxis.

**Krav:**
- Tagga med semantic version (t.ex. v1.2.3)
- Tagga med major.minor (t.ex. v1.2)
- Tagga med git commit SHA
- Tagga med kombinerad version+SHA

<details>
<summary>Ledtrad</summary>

Anvand git rev-parse for att hamta commit SHA. Splitta versionen med IFS eller cut for att fa major och minor. Loop genom alla taggar och kör docker tag.

</details>

<details>
<summary>Losning</summary>

```bash
#!/bin/bash
# multi-tag.sh

set -e

IMAGE_NAME=${1:-myapp}
VERSION=${2:-1.0.0}
REGISTRY=${3:-docker.io/myorg}

# Hamta git SHA
SHA=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

# Splitta version
MAJOR=$(echo $VERSION | cut -d. -f1)
MINOR=$(echo $VERSION | cut -d. -f2)

# Definiera alla taggar
TAGS=(
    "${VERSION}"           # 1.2.3
    "${MAJOR}.${MINOR}"    # 1.2
    "${MAJOR}"             # 1
    "${SHA}"               # abc123f
    "${VERSION}-${SHA}"    # 1.2.3-abc123f
)

echo "Building ${IMAGE_NAME}..."
docker build -t ${IMAGE_NAME}:local .

echo ""
echo "Tagging with:"
for TAG in "${TAGS[@]}"; do
    FULL_TAG="${REGISTRY}/${IMAGE_NAME}:${TAG}"
    echo "  - ${FULL_TAG}"
    docker tag ${IMAGE_NAME}:local ${FULL_TAG}
done

echo ""
echo "Pushing to ${REGISTRY}..."
for TAG in "${TAGS[@]}"; do
    docker push "${REGISTRY}/${IMAGE_NAME}:${TAG}"
done

echo ""
echo "Done! All tags pushed."
```

Anvandning:
```bash
chmod +x multi-tag.sh
./multi-tag.sh myapp 1.2.3 docker.io/myorg
```

</details>

### Ovning 3: Skapa ECR Lifecycle Policy

Skapa en AWS ECR lifecycle policy som:
- Behallar de senaste 20 taggade images (v*)
- Tar bort otaggade images aldre an 3 dagar
- Behallar images taggade med "release-*" i 90 dagar

<details>
<summary>Ledtrad</summary>

Lifecycle policies anvander JSON-format med rules-array. Varje regel har rulePriority, selection och action. Selection kan filtrera pa tagStatus, tagPrefixList, countType och countNumber.

</details>

<details>
<summary>Losning</summary>

```json
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Keep release images for 90 days",
      "selection": {
        "tagStatus": "tagged",
        "tagPrefixList": ["release-"],
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 90
      },
      "action": {
        "type": "expire"
      }
    },
    {
      "rulePriority": 2,
      "description": "Keep last 20 version-tagged images",
      "selection": {
        "tagStatus": "tagged",
        "tagPrefixList": ["v"],
        "countType": "imageCountMoreThan",
        "countNumber": 20
      },
      "action": {
        "type": "expire"
      }
    },
    {
      "rulePriority": 3,
      "description": "Delete untagged images after 3 days",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 3
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
```

Applicera med AWS CLI:
```bash
# Spara som lifecycle-policy.json och applicera
aws ecr put-lifecycle-policy \
  --repository-name myapp \
  --lifecycle-policy-text file://lifecycle-policy.json \
  --region eu-north-1

# Verifiera
aws ecr get-lifecycle-policy \
  --repository-name myapp \
  --region eu-north-1
```

</details>

------------------------------------------------------------

## Kopplingar

| Amne | Koppling |
|------|----------|
| **Docker Fundamentals** | Images maste finnas innan de kan pushas |
| **Dockerfile Best Practices** | Optimerade images ger effektivare distribution |
| **Multi-stage Builds** | Mindre images = snabbare pull fran registry |
| **CI/CD Pipelines** | Automatiserad build och push till registry |
| **Kubernetes** | Pullar images fran registry vid deployment |
| **Container Security** | Image scanning och signing i registry |

```
+---------------------------------------------------------------+
|               REGISTRY I CI/CD PIPELINE                       |
+---------------------------------------------------------------+
|                                                               |
|   [Code Push] --> [Build] --> [Test] --> [Push to Registry]  |
|                                               |                |
|                                               v                |
|   [Dev Env] <-- [Pull] <-- [Registry] --> [Pull] --> [Prod]  |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

I denna modul har du lart dig:

- **Docker Hub**: Public och private repositories, login och push/pull workflows
- **Private Registry**: Satta upp eget registry med TLS och autentisering
- **Cloud Registries**: Konfigurera och anvanda ECR, GCR och ACR
- **Tagging-strategier**: Semantic versioning, git SHA och kombinerade taggar
- **Authentication**: Olika autentiseringsmetoder for olika registries
- **Cleanup och Retention**: Lifecycle policies for automatisk image cleanup
- **Registry Mirroring**: Hog tillganglighet genom mirrors

**Viktiga principer:**

1. **Aldrig anvand latest i produktion** - specifika taggar ger sparbarhet
2. **Automatisera i CI/CD** - manuell push ar felbenaget
3. **Implementera retention policies** - registries vaxer snabbt
4. **Anvand private registries** - for foretagskod och kanslighet

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker login [registry]` | Logga in pa registry |
| `docker logout [registry]` | Logga ut fran registry |
| `docker tag SOURCE TARGET` | Tagga image med nytt namn |
| `docker push IMAGE:TAG` | Pusha image till registry |
| `docker pull IMAGE:TAG` | Pulla image fran registry |
| `docker search TERM` | Sok images pa Docker Hub |
| `docker manifest inspect IMAGE` | Inspektera image manifest |
| `aws ecr get-login-password` | Hamta ECR login token |
| `gcloud auth configure-docker` | Konfigurera Docker for GCR |
| `az acr login --name NAME` | Logga in pa Azure ACR |

------------------------------------------------------------

## Referenser

| Resurs | Lank |
|--------|------|
| Docker Registry Documentation | https://docs.docker.com/registry/ |
| Docker Hub Documentation | https://docs.docker.com/docker-hub/ |
| AWS ECR User Guide | https://docs.aws.amazon.com/AmazonECR/latest/userguide/ |
| Google Artifact Registry | https://cloud.google.com/artifact-registry/docs |
| Azure Container Registry | https://docs.microsoft.com/azure/container-registry/ |
| Harbor Registry | https://goharbor.io/docs/ |
| Docker Content Trust | https://docs.docker.com/engine/security/trust/ |
| Registry API Specification | https://docs.docker.com/registry/spec/api/ |
""",
        },
        {
            "title": "Docker Multi-stage Builds",
            "slug": "docker-multi-stage-builds",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Multi-stage Builds

------------------------------------------------------------

## Introduktion

Multi-stage builds ar en kraftfull teknik som lat dig anvanda flera FROM-instruktioner i samma Dockerfile. Varje FROM startar en ny stage, och du kan selektivt kopiera artefakter fran en stage till en annan. Detta ger dig dramatiskt mindre production images utan att offra build-flexibilitet.

Innan multi-stage builds var du tvungen att antingen ha stora images med alla build-verktyg, eller anvanda komplicerade skript for att bygga utanfor Docker och sedan kopiera in resultatet. Multi-stage builds loser detta elegant genom att separera build-miljö fran runtime-miljo i samma Dockerfile.

------------------------------------------------------------

## Teori

### Grundlaggande arkitektur

```
+---------------------------------------------------------------+
|                    MULTI-STAGE BUILD PROCESS                  |
+---------------------------------------------------------------+
|                                                               |
|  Dockerfile med flera stages:                                 |
|                                                               |
|  +------------------+    +------------------+                 |
|  |   STAGE 1        |    |   STAGE 2        |                 |
|  |   (AS builder)   |    |   (AS tester)    |                 |
|  +------------------+    +------------------+                 |
|  | FROM golang:1.21 |    | FROM builder     |                 |
|  | COPY . .         |    | RUN go test      |                 |
|  | RUN go build     |    +------------------+                 |
|  +--------+---------+              |                          |
|           |                        |                          |
|           v                        v                          |
|  +------------------+    +------------------+                 |
|  |   STAGE 3        |    |   FINAL IMAGE    |                 |
|  |   (AS prod-deps) |    |   (runtime)      |                 |
|  +------------------+    +------------------+                 |
|  | FROM alpine      |    | FROM scratch     |                 |
|  | apk add ca-certs |    | COPY --from=     |                 |
|  +------------------+    |   builder /app   |                 |
|                          +------------------+                 |
|                                   |                           |
|                                   v                           |
|                          [Minimal Production Image]           |
|                                                               |
+---------------------------------------------------------------+
```

### Nyckelkoncept

| Koncept | Beskrivning |
|---------|-------------|
| **Stage** | Varje FROM-instruktion startar en ny stage |
| **Named stage** | FROM image AS name - ger stage ett namn |
| **COPY --from** | Kopierar filer fran annan stage eller image |
| **--target** | Bygger upp till och med en specifik stage |
| **Final stage** | Sista FROM blir den slutgiltiga imagen |

### Varfor multi-stage?

```
+---------------------------------------------------------------+
|              SINGLE-STAGE vs MULTI-STAGE                      |
+---------------------------------------------------------------+
|                                                               |
|   SINGLE-STAGE:                                               |
|   +---------------------------------------------------+       |
|   | Base Image (debian:bullseye)              500 MB  |       |
|   | + Build tools (gcc, make, etc)            300 MB  |       |
|   | + Development dependencies                200 MB  |       |
|   | + Source code                              50 MB  |       |
|   | + Compiled application                     20 MB  |       |
|   +---------------------------------------------------+       |
|   | TOTAL:                                   1070 MB  |       |
|   +---------------------------------------------------+       |
|                                                               |
|   MULTI-STAGE:                                                |
|   +---------------------------------------------------+       |
|   | Base Image (alpine/scratch)                 5 MB  |       |
|   | + Runtime dependencies only                15 MB  |       |
|   | + Compiled application                     20 MB  |       |
|   +---------------------------------------------------+       |
|   | TOTAL:                                     40 MB  |       |
|   +---------------------------------------------------+       |
|                                                               |
|   BESPARING: 96% mindre image!                                |
|                                                               |
+---------------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Identifiera build vs runtime dependencies

Forst maste du forsta vad som behovs for att bygga vs kora din applikation:

| Fas | Exempel dependencies |
|-----|----------------------|
| **Build** | Kompilator, build-verktyg, devDependencies |
| **Runtime** | Enbart det kompilerade programmet och runtime-bibliotek |

### Steg 2: Skapa named stages

```dockerfile
# Syntax: FROM image AS stage-name
FROM node:18 AS builder
# ... build instruktioner

FROM node:18-slim AS production
# ... production instruktioner
```

### Steg 3: Bygg i forsta stage

```dockerfile
FROM golang:1.21 AS builder

WORKDIR /app

# Kopiera dependency-filer forst (cache-optimering)
COPY go.mod go.sum ./
RUN go mod download

# Kopiera resten av koden
COPY . .

# Bygg applikationen
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /app/server ./cmd/server
```

### Steg 4: Kopiera artefakter till production stage

```dockerfile
FROM scratch AS production

# Kopiera enbart den kompilerade binaren
COPY --from=builder /app/server /server

# Kopiera nodvandiga certifikat for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

USER 1000:1000
ENTRYPOINT ["/server"]
```

### Steg 5: Bygg och verifiera

```bash
# Bygg imagen
docker build -t myapp:latest .

# Verifiera storlek
docker images myapp:latest

# Testa att imagen fungerar
docker run --rm myapp:latest --version
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Go-applikation med minimal image

```dockerfile
# ============================================================
# Stage 1: Build
# ============================================================
FROM golang:1.21-alpine AS builder

# Installera git for go mod (om private repos anvands)
RUN apk add --no-cache git ca-certificates tzdata

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download && go mod verify

# Kopiera och bygg
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \\
    -ldflags="-w -s -X main.version=1.0.0" \\
    -o /app/server \\
    ./cmd/server

# ============================================================
# Stage 2: Production
# ============================================================
FROM scratch

# Kopiera CA-certifikat for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

# Kopiera binaren
COPY --from=builder /app/server /server

# Non-root user
USER 1000:1000

EXPOSE 8080
ENTRYPOINT ["/server"]
```

### Exempel 2: Node.js med separata dependency stages

```dockerfile
# ============================================================
# Stage 1: Base
# ============================================================
FROM node:18-alpine AS base
WORKDIR /app

# ============================================================
# Stage 2: Dependencies
# ============================================================
FROM base AS deps
COPY package.json package-lock.json ./
RUN npm ci --only=production && \\
    cp -R node_modules /prod_modules && \\
    npm ci

# ============================================================
# Stage 3: Build
# ============================================================
FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build && npm prune --production

# ============================================================
# Stage 4: Production
# ============================================================
FROM node:18-alpine AS production

WORKDIR /app

# Kopiera endast production dependencies och build output
COPY --from=deps /prod_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./

USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Exempel 3: Python med virtual environment

```dockerfile
# ============================================================
# Stage 1: Build
# ============================================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Installera build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    && rm -rf /var/lib/apt/lists/*

# Skapa virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installera dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================================
# Stage 2: Production
# ============================================================
FROM python:3.11-slim AS production

WORKDIR /app

# Kopiera virtual environment fran builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Kopiera applikationskod
COPY src/ ./src/
COPY config/ ./config/

# Skapa non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

EXPOSE 8000
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

------------------------------------------------------------

## Bästa Praxis

### 1. Namnge dina stages

```dockerfile
# BRA: Tydliga namn
FROM node:18 AS builder
FROM node:18 AS tester
FROM node:18-slim AS production

# UNDVIK: Anonyma stages
FROM node:18
FROM node:18
FROM node:18-slim
```

### 2. Optimera for cache

```
+---------------------------------------------------------------+
|                 LAYER CACHE STRATEGI                          |
+---------------------------------------------------------------+
|                                                               |
|   OPTIMAL ORDNING (langsamst andrande forst):                 |
|                                                               |
|   1. FROM base-image            [andras sällan]               |
|   2. System packages            [andras sällan]               |
|   3. COPY dependency files      [andras ibland]               |
|   4. RUN install dependencies   [cached om filer oforandrade] |
|   5. COPY source code           [andras ofta]                 |
|   6. RUN build                  [alltid efter kodandring]     |
|                                                               |
+---------------------------------------------------------------+
```

### 3. Minimera final image

| Base image | Storlek | Anvandning |
|------------|---------|------------|
| `scratch` | 0 MB | Statiska binarer (Go, Rust) |
| `alpine` | 5 MB | Nar shell behovs |
| `distroless` | 2-20 MB | Sakerhetsfokuserat |
| `*-slim` | 50-100 MB | Nar fler verktyg behovs |

### 4. Anvand --target for development

```bash
# Bygg endast test stage
docker build --target tester -t myapp:test .

# Bygg development stage med alla verktyg
docker build --target builder -t myapp:dev .

# Bygg production (standard - sista stage)
docker build -t myapp:prod .
```

### 5. Kopiera fran externa images

```dockerfile
# Kopiera verktyg fran officiella images
FROM alpine AS production

# Kopiera Docker CLI
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/

# Kopiera kubectl
COPY --from=bitnami/kubectl:latest /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/

# Kopiera Terraform
COPY --from=hashicorp/terraform:latest /bin/terraform /usr/local/bin/
```

------------------------------------------------------------

## Vanliga Fallgropar

### Fallgrop 1: Glommer runtime dependencies

```dockerfile
# FEL: Missar runtime dependencies
FROM golang:1.21 AS builder
RUN CGO_ENABLED=1 go build -o /app/server

FROM scratch
COPY --from=builder /app/server /server
# KRASCHAR! CGO kraver glibc som saknas i scratch

# RATT: Anvand CGO_ENABLED=0 eller inkludera dependencies
FROM golang:1.21 AS builder
RUN CGO_ENABLED=0 go build -o /app/server

FROM scratch
COPY --from=builder /app/server /server
```

### Fallgrop 2: Kopierar for mycket

```dockerfile
# FEL: Kopierar hela /app inklusive node_modules och source
COPY --from=builder /app /app

# RATT: Kopiera endast det nodvandiga
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
```

### Fallgrop 3: Felaktig stage-referens

```dockerfile
# FEL: Stage finns inte
COPY --from=buildstage /app /app  # Typo!

# RATT: Kontrollera stage-namn
FROM node:18 AS builder
# ...
COPY --from=builder /app /app
```

### Fallgrop 4: Glomt certificates for HTTPS

```dockerfile
# FEL: Scratch-image utan CA-certifikat
FROM scratch
COPY --from=builder /app/server /server
# HTTPS-anrop misslyckas!

# RATT: Inkludera CA-certifikat
FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/server /server
```

------------------------------------------------------------

## Övningar

### Ovning 1: Konvertera single-stage till multi-stage

Givet foljande single-stage Dockerfile, konvertera den till multi-stage:

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

<details>
<summary>Ledtrad</summary>

- Skapa en builder stage for npm install och build
- Skapa en production stage med node:18-slim
- Kopiera endast dist och node_modules (production) till final stage
- Glom inte att anvanda npm ci istallet for npm install

</details>

<details>
<summary>Losning</summary>

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-slim AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production
USER node
CMD ["node", "dist/index.js"]
```

</details>

### Ovning 2: Skapa test stage

Lagg till en test stage i foljande Dockerfile som kor tester innan production:

```dockerfile
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o /app/server

FROM scratch
COPY --from=builder /app/server /server
CMD ["/server"]
```

<details>
<summary>Ledtrad</summary>

- Lagg till en stage mellan builder och production
- Tester ska koras med go test ./...
- Test stage ska baseras pa builder stage
- Du kan kora docker build --target tester for att bara kora tester

</details>

<details>
<summary>Losning</summary>

```dockerfile
FROM golang:1.21 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /app/server ./cmd/server

# Test stage
FROM builder AS tester
RUN go test -v ./...

# Production stage
FROM scratch AS production
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/server /server
USER 1000:1000
ENTRYPOINT ["/server"]
```

Kor tester: `docker build --target tester .`
Bygg prod: `docker build --target production -t myapp:prod .`

</details>

### Ovning 3: Optimera build-cache

Foljande Dockerfile har dalig cache-anvandning. Optimera den:

```dockerfile
FROM python:3.11 AS builder
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python setup.py build

FROM python:3.11-slim
COPY --from=builder /app /app
CMD ["python", "/app/main.py"]
```

<details>
<summary>Ledtrad</summary>

- Kopiera requirements.txt separat fore resten av koden
- Anvand virtual environment for renare kopiering
- Kopiera endast det nodvandiga till final stage
- Tank pa ordningen: langsamast andrande forst

</details>

<details>
<summary>Losning</summary>

```dockerfile
FROM python:3.11 AS builder
WORKDIR /app

# 1. Skapa virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 2. Installera dependencies forst (cachas om requirements.txt oandrad)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Kopiera och bygg applikation
COPY . .
RUN python setup.py build

FROM python:3.11-slim AS production
WORKDIR /app

# Kopiera virtual environment
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Kopiera endast byggd applikation
COPY --from=builder /app/build ./build
COPY --from=builder /app/main.py ./

USER nobody
CMD ["python", "main.py"]
```

</details>

------------------------------------------------------------

## Kopplingar

| Amne | Koppling |
|------|----------|
| **Dockerfile Basta Praxis** | Multi-stage ar central del av optimering |
| **Image Security** | Mindre images = mindre attack surface |
| **CI/CD Pipelines** | --target for separata build/test steg |
| **Docker Cache** | Layer-ordning kritisk for cache-effektivitet |
| **Container Registries** | Mindre images = snabbare push/pull |
| **Kubernetes Deployments** | Mindre images = snabbare pod startup |

------------------------------------------------------------

## Sammanfattning

Multi-stage builds ar en fundamental teknik for att skapa produktionsklara Docker images. Genom att separera build och runtime miljoer kan du:

1. **Dramatiskt minska image-storlek** - Ofta 80-99% mindre
2. **Forbattra sakerhet** - Inga build-verktyg i produktion
3. **Snabbare deploys** - Mindre images = snabbare pull
4. **Battre organisation** - Tydlig separation av concerns

Kom ihag att alltid namnge dina stages, optimera for cache genom att kopiera dependencies forst, och anvanda minimala base images for production.

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `FROM image AS name` | Starta named stage |
| `COPY --from=stage` | Kopiera fran annan stage |
| `COPY --from=image` | Kopiera fran extern image |
| `docker build --target stage` | Bygg specifik stage |
| `docker build --target stage -t tag` | Bygg och tagga specifik stage |

```bash
# Bygg production image (sista stage)
docker build -t myapp:prod .

# Bygg specifik stage
docker build --target builder -t myapp:builder .
docker build --target tester -t myapp:test .

# Visa alla stages i Dockerfile
grep "^FROM" Dockerfile

# Jamfor image-storlekar
docker images | grep myapp
```

------------------------------------------------------------

## Referenser

| Resurs | Lank |
|--------|------|
| Docker Multi-stage Builds | https://docs.docker.com/build/building/multi-stage/ |
| Dockerfile Best Practices | https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ |
| Distroless Images | https://github.com/GoogleContainerTools/distroless |
| Alpine Linux | https://alpinelinux.org/ |
| BuildKit Documentation | https://docs.docker.com/build/buildkit/ |
""",
        },
        {
            "title": "Docker Performance Optimization",
            "slug": "docker-performance-optimization",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker Performance Optimization

------------------------------------------------------------

## Introduktion

Föreställ dig att ditt team väntar 15 minuter på varje Docker-build i CI/CD-pipelinen. Varje kodändring innebär en kvarts väntan innan feedback. Images på 2GB tar evigheter att pusha och pulla. Containers slukar minne och CPU utan begränsning.

Docker-prestanda påverkar hela utvecklingscykeln - från lokal utveckling till produktion. Optimering handlar om att minska build-tid, krympa images och maximera runtime-effektivitet. Som DevOps-ingenjör är detta en av de mest värdefulla kompetenserna du kan ha.

I denna modul lär du dig konkreta tekniker för att göra dina containers snabbare och smidigare. Du kommer att förstå varför vissa Dockerfiles bygger på sekunder medan andra tar minuter, och hur du kan reducera image-storlekar med 90% eller mer.

Efter denna modul kommer du kunna diagnostisera prestandaproblem, implementera effektiva caching-strategier och konfigurera resursbegränsningar för produktion.

------------------------------------------------------------

## Teori

### Performance Optimization Pyramid

Docker-prestanda kan visualiseras som en pyramid där varje lager bygger på det under:

```
+------------------------------------------------------------+
|           PERFORMANCE OPTIMIZATION PYRAMID                  |
+------------------------------------------------------------+
|                                                            |
|                    +------------+                          |
|                    | PROFILING  |  <-- Mät och analysera   |
|                    +------------+                          |
|                   /              \\                         |
|            +--------+        +--------+                    |
|            | RUNTIME|        | BUILD  |                    |
|            +--------+        +--------+                    |
|           /          \\      /          \\                   |
|     +-------+    +-------+-------+    +-------+            |
|     | CPU   |    | MEMORY| CACHE |    | SIZE  |            |
|     +-------+    +-------+-------+    +-------+            |
|    /         \\                      /         \\           |
|   +-----------+--------------------+-----------+           |
|   |        STORAGE DRIVERS & I/O              |           |
|   +-------------------------------------------+           |
|                                                            |
+------------------------------------------------------------+
```

### Layer Caching - Grundkonceptet

Docker bygger images i lager. Varje instruktion skapar ett nytt lager som cachas. Nyckeln är att ordna instruktioner så att saker som ändras sällan kommer först:

```
+------------------------------------------------------------+
|                  LAYER CACHING FLÖDE                       |
+------------------------------------------------------------+
|                                                            |
|   Dockerfile          Cache Status        Resultat         |
|   +-----------+       +------------+      +------------+   |
|   | FROM      | ----> | CACHAD     | ---> | Återanvänd |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | COPY deps | ----> | CACHAD     | ---> | Återanvänd |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | RUN inst  | ----> | CACHAD     | ---> | Återanvänd |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | COPY src  | ----> | INVALIDERAD| ---> | OMBYGGD    |   |
|   +-----------+       +------------+      +------------+   |
|                                                            |
+------------------------------------------------------------+
```

### BuildKit Features

BuildKit är Dockers moderna build-backend med avancerade optimeringsfunktioner:

| Feature | Beskrivning | Användning |
|---------|-------------|------------|
| Parallella stages | Bygger oberoende stages samtidigt | Multi-stage builds |
| Cache mounts | Persistent cache mellan builds | Pakethanterare |
| Secret mounts | Säker hantering av hemligheter | API-nycklar under build |
| SSH mounts | SSH-agent forwarding | Git clone från privata repos |
| Heredocs | Multi-line scripts | Komplexa RUN-kommandon |

### Image-storlek och Prestanda

Mindre images ger snabbare pull/push och mindre säkerhetshot:

| Base Image | Storlek | Användning |
|------------|---------|------------|
| python:3.11 | ~1.0 GB | Development |
| python:3.11-slim | ~350 MB | Produktion |
| python:3.11-alpine | ~50 MB | Minimal |
| distroless/python3 | ~70 MB | Säkerhet |

### Resource Limits med cgroups

Docker använder Linux cgroups för resursbegränsning:

| Flagga | Beskrivning | Rekommendation |
|--------|-------------|----------------|
| --memory | Hard limit | Sätt till max tillåtet |
| --memory-swap | Swap limit | Samma som memory |
| --cpus | CPU-begränsning | Baserat på workload |
| --memory-reservation | Soft limit | 75% av --memory |

------------------------------------------------------------

## Steg-för-steg Guide

### Layer Caching Strategier

Docker bygger images i lager. Varje instruktion skapar ett nytt lager som cachas. Nyckeln ar att ordna instruktioner sa att saker som andras sallan kommer forst.

```
+------------------------------------------------------------+
|                  LAYER CACHING FLODE                       |
+------------------------------------------------------------+
|                                                            |
|   Dockerfile          Cache Status        Resultat         |
|   +-----------+       +------------+      +------------+   |
|   | FROM      | ----> | CACHAD     | ---> | Ateranvand |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | COPY deps | ----> | CACHAD     | ---> | Ateranvand |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | RUN inst  | ----> | CACHAD     | ---> | Ateranvand |   |
|   +-----------+       +------------+      +------------+   |
|        |                                                   |
|        v                                                   |
|   +-----------+       +------------+      +------------+   |
|   | COPY src  | ----> | INVALIDERAD| ---> | OMBYGGD    |   |
|   +-----------+       +------------+      +------------+   |
|        |                   ^                               |
|        |                   |                               |
|        +------- Andring har! Cache invalideras ----------> |
|                                                            |
+------------------------------------------------------------+
```

```dockerfile
# DALIGT: Cache invalideras vid varje kodandring
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# BRA: Dependencies cachas separat fran kod
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Optimal Layer-ordning

| Prioritet | Innehall | Andringsfrekvens |
|-----------|----------|------------------|
| 1 | Base image | Mycket sallan |
| 2 | Systempaket | Sallan |
| 3 | Sprakkonfiguration | Sallan |
| 4 | Dependencies | Ibland |
| 5 | Applikationskod | Ofta |
| 6 | Konfigurationsfiler | Ofta |

------------------------------------------------------------

## Praktiska Exempel

BuildKit ar Dockers moderna build-backend med avancerade optimeringsfunktioner. Aktivera med DOCKER_BUILDKIT=1 eller konfigurera som standard.

### BuildKit Features

| Feature | Beskrivning | Anvandning |
|---------|-------------|------------|
| Parallella stages | Bygger oberoende stages samtidigt | Multi-stage builds |
| Cache mounts | Persistent cache mellan builds | Pakethanterare |
| Secret mounts | Saker hantering av hemligheter | API-nycklar under build |
| SSH mounts | SSH-agentforwarding | Git clone fran privata repos |
| Heredocs | Multi-line scripts | Komplexa RUN-kommandon |

```dockerfile
# syntax=docker/dockerfile:1.4

FROM python:3.11-slim AS builder

WORKDIR /app

# Cache mount for pip - sparar nedladdade paket mellan builds
RUN --mount=type=cache,target=/root/.cache/pip \\
    --mount=type=bind,source=requirements.txt,target=requirements.txt \\
    pip install -r requirements.txt

# Secret mount - exponerar inte secrets i image layers
RUN --mount=type=secret,id=api_key \\
    cat /run/secrets/api_key > /app/.env

# SSH mount for privata Git repos
RUN --mount=type=ssh \\
    git clone git@github.com:org/private-repo.git
```

### Cache Mount for olika pakethanterare

```dockerfile
# Python pip
RUN --mount=type=cache,target=/root/.cache/pip \\
    pip install -r requirements.txt

# Node npm
RUN --mount=type=cache,target=/root/.npm \\
    npm ci

# Go modules
RUN --mount=type=cache,target=/go/pkg/mod \\
    go build -o /app/main .

# Rust cargo
RUN --mount=type=cache,target=/usr/local/cargo/registry \\
    cargo build --release

# Apt packages
RUN --mount=type=cache,target=/var/cache/apt \\
    apt-get update && apt-get install -y curl
```

------------------------------------------------------------

## Bästa Praxis

Mindre images betyder snabbare pull/push, mindre sakerhetshot och lagre lagringskostnader.

### Storlek jamforelse

```
+------------------------------------------------------------+
|              IMAGE STORLEK JAMFORELSE                       |
+------------------------------------------------------------+
|                                                            |
| python:3.11          |============================| 1.0 GB |
| python:3.11-slim     |========|                    350 MB  |
| python:3.11-alpine   |===|                         50 MB   |
| distroless/python3   |====|                        70 MB   |
|                                                            |
| node:20              |==========================|  950 MB  |
| node:20-slim         |=======|                    250 MB   |
| node:20-alpine       |====|                       140 MB   |
|                                                            |
| golang:1.21          |========================|   850 MB  |
| golang:1.21-alpine   |=====|                     250 MB   |
| scratch + go binary  |=|                          15 MB   |
|                                                            |
+------------------------------------------------------------+
```

### Multi-stage for minimal storlek

```dockerfile
# Build stage - innehaller alla build-verktyg
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /app/server

# Runtime stage - minimal image
FROM scratch
COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
EXPOSE 8080
ENTRYPOINT ["/server"]
```

### Storleksoptimeringstekniker

| Teknik | Besparing | Exempel |
|--------|-----------|---------|
| Slim/Alpine base | 70-90% | python:3.11-slim |
| Multi-stage builds | 80-95% | Separat build/runtime |
| --no-cache-dir | 10-30% | pip install --no-cache-dir |
| Rensa apt cache | 5-15% | rm -rf /var/lib/apt/lists/* |
| Strip binaries | 20-40% | -ldflags="-s -w" |
| .dockerignore | Varierar | Exkludera node_modules, .git |

------------------------------------------------------------

## Vanliga Fallgropar

### CPU och Memory Tuning

```bash
# Begransningar for produktion
docker run -d \\
    --name myapp \\
    --cpus="2.0" \\
    --memory="2g" \\
    --memory-swap="2g" \\
    --memory-reservation="1g" \\
    --cpu-shares=1024 \\
    myimage:latest

# CPU pinning for prediktabel prestanda
docker run -d \\
    --cpuset-cpus="0,1" \\
    --cpuset-mems="0" \\
    myimage:latest
```

### Resource Limits Oversikt

```
+------------------------------------------------------------+
|              RESOURCE LIMITS ARKITEKTUR                     |
+------------------------------------------------------------+
|                                                            |
|   Host System Resources                                    |
|   +------------------------------------------------------+ |
|   |  CPU: 8 cores    Memory: 32GB    Disk: 500GB        | |
|   +------------------------------------------------------+ |
|            |                |                |             |
|            v                v                v             |
|   +----------------+ +----------------+ +----------------+ |
|   | Container A    | | Container B    | | Container C    | |
|   | --cpus=2       | | --cpus=1       | | --cpus=4       | |
|   | --memory=4g    | | --memory=2g    | | --memory=8g    | |
|   | --blkio=500    | | --blkio=100    | | --blkio=1000   | |
|   +----------------+ +----------------+ +----------------+ |
|                                                            |
|   cgroups v2 enligatvingar:                                |
|   - cpu.max         - memory.max      - io.max            |
|   - cpu.weight      - memory.high     - io.weight         |
|                                                            |
+------------------------------------------------------------+
```

### Memory-flaggor

| Flagga | Beskrivning | Rekommendation |
|--------|-------------|----------------|
| --memory | Hard limit | Satt till max tillatet |
| --memory-swap | Swap limit | Samma som memory (ingen swap) |
| --memory-reservation | Soft limit | 75% av --memory |
| --oom-kill-disable | Forhindra OOM kill | Anvand forsiktigt |

------------------------------------------------------------

## Kopplingar

Storage driver paverkar I/O-prestanda och ar kritisk for databascontainers och I/O-intensiva applikationer.

### Storage Driver Jamforelse

| Driver | Prestanda | Stabilitet | Anvandning |
|--------|-----------|------------|------------|
| overlay2 | Utmarkt | Stabil | Default, rekommenderad |
| btrfs | Bra | Stabil | Snapshots |
| zfs | Bra | Stabil | Enterprise features |
| devicemapper | Medel | Stabil | Aldre system |
| vfs | Dalig | Stabil | Testing endast |

```bash
# Kontrollera nuvarande storage driver
docker info | grep "Storage Driver"

# Konfigurera overlay2 (rekommenderad)
# /etc/docker/daemon.json
{
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
```

### Volume Performance

```bash
# Anonym volume - Docker hanterar
docker run -v /data myimage

# Named volume - battre prestanda
docker run -v mydata:/data myimage

# Bind mount - host filesystem
docker run -v /host/path:/container/path myimage

# tmpfs - i minnet, snabbast
docker run --tmpfs /tmp:rw,noexec,nosuid,size=100m myimage
```

------------------------------------------------------------

## Nyckelkommandon

### Docker Stats och Monitoring

```bash
# Realtids-statistik
docker stats --format "table {{.Name}}\\t{{.CPUPerc}}\\t{{.MemUsage}}"

# En container
docker stats mycontainer --no-stream

# Med custom format
docker stats --format \\
    "{{.Name}}: CPU {{.CPUPerc}}, MEM {{.MemPerc}}, NET {{.NetIO}}"
```

### Profiling-verktyg

| Verktyg | Syfte | Installation |
|---------|-------|--------------|
| docker stats | Grund-metrics | Inbyggd |
| ctop | Interaktiv monitoring | brew install ctop |
| dive | Layer-analys | brew install dive |
| hadolint | Dockerfile linting | brew install hadolint |
| docker scout | Sakerhet + prestanda | docker scout |

```bash
# Dive - analysera image layers
dive myimage:latest

# Hadolint - Dockerfile best practices
hadolint Dockerfile

# Docker Scout - sakerhet och rekommendationer
docker scout quickview myimage:latest
docker scout recommendations myimage:latest
```

### Build-tid Benchmarking

```bash
# Mat build-tid
time docker build -t myimage .

# Med BuildKit timing
DOCKER_BUILDKIT=1 docker build -t myimage . 2>&1 | tee build.log

# Jamfor builds
hyperfine "docker build -t test1 ." "docker build -t test2 -f Dockerfile.optimized ."
```

------------------------------------------------------------

## Övningar

### Ovning 1: Optimera Build Cache

Du har en Dockerfile som bygger om dependencies vid varje kodandring. Optimera den for battre caching.

Ursprunglig Dockerfile:
```dockerfile
FROM node:20
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["npm", "start"]
```

<details>
<summary>Ledtrad</summary>

Tanka pa ordningen av COPY-instruktioner. Vad andras sallan? Vad andras ofta? Dependencies (package.json) andras mer sallan an kallkod.
</details>

<details>
<summary>Losning</summary>

```dockerfile
FROM node:20-slim
WORKDIR /app

# Kopiera endast dependency-filer forst
COPY package.json package-lock.json ./

# Installera dependencies (cachas om package*.json inte andras)
RUN npm ci --only=production

# Kopiera resten av koden
COPY . .

# Bygg applikationen
RUN npm run build

CMD ["npm", "start"]
```

Forandringar:
1. Anvander node:20-slim for mindre storlek
2. Kopierar package*.json separat fore npm ci
3. npm ci istallet for npm install (snabbare, mer deterministisk)
4. Dependencies cachas tills package.json andras
</details>

### Ovning 2: Multi-stage for Minimal Image

Skapa en multi-stage Dockerfile for en Go-applikation som resulterar i minimal image-storlek.

Krav:
- Build-stage med alla verktyg
- Runtime-stage med endast binar
- Slutlig image under 20MB

<details>
<summary>Ledtrad</summary>

Go kan kompileras till en statisk binar med CGO_ENABLED=0. Scratch-imagen ar helt tom och perfekt for statiska binarer. Glom inte SSL-certifikat om applikationen gor HTTPS-anrop.
</details>

<details>
<summary>Losning</summary>

```dockerfile
# Build stage
FROM golang:1.21-alpine AS builder

# Installera certificates for HTTPS
RUN apk --no-cache add ca-certificates

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download

# Kopiera kod och bygg
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \\
    go build -ldflags="-s -w" -o /app/server ./cmd/server

# Runtime stage - from scratch (tom image)
FROM scratch

# Kopiera SSL certs for HTTPS
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Kopiera binar
COPY --from=builder /app/server /server

# Metadata
EXPOSE 8080
USER 1000:1000

ENTRYPOINT ["/server"]
```

Resultat: ~10-15MB image med full funktionalitet.
</details>

### Ovning 3: BuildKit Cache Mounts

Implementera BuildKit cache mounts for att snabba upp Python-builds med stora dependencies.

Scenario: En ML-applikation med tensorflow, pytorch och andra tunga paket.

<details>
<summary>Ledtrad</summary>

Pip cachar nedladdade paket i /root/.cache/pip. Med cache mount sparas dessa mellan builds. Tanka ocksa pa wheel-byggning som kan cachas separat.
</details>

<details>
<summary>Losning</summary>

```dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.11-slim AS builder

WORKDIR /app

# Installera build-dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    && rm -rf /var/lib/apt/lists/*

# Cache mount for pip - sparar nedladdningar mellan builds
# Cache mount for wheels - sparar kompilerade paket
RUN --mount=type=cache,target=/root/.cache/pip \\
    --mount=type=cache,target=/root/.cache/wheel \\
    --mount=type=bind,source=requirements.txt,target=requirements.txt \\
    pip wheel -w /wheels -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Kopiera fardiga wheels och installera (snabbt)
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*.whl && rm -rf /wheels

COPY . .

CMD ["python", "app.py"]
```

Forsta build: ~5 minuter (laddar ner allt)
Efterfoljande builds: ~30 sekunder (anvander cache)
</details>

------------------------------------------------------------

## Sammanfattning

| Omrade | Viktigaste Larosomt |
|--------|---------------------|
| Layer Caching | Ordna fran sallan-andrat till ofta-andrat |
| BuildKit | Aktivera och anvand cache mounts |
| Image-storlek | Multi-stage + slim/alpine bases |
| Runtime | Satt memory och CPU limits |
| Storage | overlay2 driver, tmpfs for temp-data |
| Profiling | Mat fore och efter, anvand dive |

------------------------------------------------------------

## Referenser

| Resurs | Lank |
|--------|------|
| BuildKit Documentation | https://docs.docker.com/build/buildkit/ |
| Dockerfile Best Practices | https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ |
| Docker Storage Drivers | https://docs.docker.com/storage/storagedriver/ |
| Dive Image Analyzer | https://github.com/wagoodman/dive |
| Hadolint Linter | https://github.com/hadolint/hadolint |
| Docker Scout | https://docs.docker.com/scout/ |
""",
        },
        {
            "title": "Docker Debugging & Troubleshooting",
            "slug": "docker-debugging-troubleshooting",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Debugging & Troubleshooting

------------------------------------------------------------

## Introduktion

Det ar fredag eftermiddag och din telefon ringer. Produktionssystemet ar nere, och den enda information du har ar "containern bara dog". Hjartslag okar, svetten bryter fram - men du behover inte panikera. Med ratt verktyg och en systematisk approach kan du snabbt hitta och losa problemet.

Docker-debugging ar en av de viktigaste fardigheter du behover som DevOps-ingenjor. Containers ar fantastiska nar de fungerar, men nar nagot gar fel kan de kanna som svarta lador dar information ar svart att komma at. Den goda nyheten ar att Docker erbjuder kraftfulla verktyg for att inspektera, analysera och felsoka containers.

I den har noden lar du dig ett systematiskt tillvagagangssatt for debugging. Du kommer beharska docker logs med olika log drivers, anvanda docker exec for att komma in i korande containers, analysera metadata med docker inspect, och spara container-events i realtid. Du far ocksa lara dig om specialiserade verktyg som netshoot, dive och ctop som gor debugging annu enklare.

Nar du ar klar med den har noden kommer du kunna hantera de flesta produktionsproblem lugnt och metodiskt - oavsett om det ar en fredag kvall eller inte.

------------------------------------------------------------

## Teori

Debugging i Docker handlar om att systematiskt samla information tills du hittar rotorsaken. Tänk pa det som en detektiv som samlar ledtradar - ju fler datapunkter du har, desto snabbare kan du losa mysteriet.

```
+------------------------------------------------------------+
|              DOCKER DEBUGGING EKOSYSTEM                    |
+------------------------------------------------------------+
|                                                            |
|   +------------------+    +------------------+             |
|   |   docker logs    |    |  docker inspect  |             |
|   |  (vad hande?)    |    | (hur ser det ut?)|             |
|   +--------+---------+    +--------+---------+             |
|            |                       |                       |
|            v                       v                       |
|   +--------------------------------------------+           |
|   |           CONTAINER PROBLEM                |           |
|   +--------------------------------------------+           |
|            ^                       ^                       |
|            |                       |                       |
|   +--------+---------+    +--------+---------+             |
|   |   docker exec    |    |  docker events   |             |
|   | (undersok live)  |    | (vad trigger?)   |             |
|   +------------------+    +------------------+             |
|                                                            |
+------------------------------------------------------------+
```

De fyra huvudverktygen kompletterar varandra:

- **docker logs** - Visar vad applikationen sager (stdout/stderr)
- **docker inspect** - Visar all metadata om containern
- **docker exec** - Later dig kora kommandon inne i containern
- **docker events** - Visar systemhandelser i realtid

------------------------------------------------------------

## Steg-för-steg Guide

Nar nagot gar fel ar loggar alltid forsta stoppet. Docker fangar automatiskt allt som skrivs till stdout och stderr fran huvudprocessen.

### Grundlaggande loggkommandon

```bash
# Visa alla loggar for en container
docker logs mycontainer

# Visa de senaste 100 raderna
docker logs --tail 100 mycontainer

# Folj loggar i realtid (som tail -f)
docker logs -f mycontainer

# Kombinera: senaste 50 rader + folj
docker logs --tail 50 -f mycontainer

# Visa loggar med tidsstamplar
docker logs -t mycontainer

# Loggar fran en specifik tidsperiod
docker logs --since "2024-01-15T10:00:00" mycontainer
docker logs --since "10m" mycontainer  # senaste 10 minuterna
docker logs --until "5m" mycontainer   # fram till 5 min sedan
```

### Log Drivers - Var hamnar loggarna?

Docker stodjer flera log drivers som bestammer var loggar lagras:

```
+------------------------------------------------------------+
|                    LOG DRIVERS                             |
+------------------------------------------------------------+
|                                                            |
|   Container stdout/stderr                                  |
|            |                                               |
|            v                                               |
|   +------------------+                                     |
|   |   Docker Daemon  |                                     |
|   +--------+---------+                                     |
|            |                                               |
|   +--------+--------+--------+--------+                    |
|   |        |        |        |        |                    |
|   v        v        v        v        v                    |
| json-file syslog  journald  gelf   fluentd                |
| (default)                                                  |
|                                                            |
+------------------------------------------------------------+
```

| Log Driver | Beskrivning | Anvandningsfall |
|------------|-------------|-----------------|
| json-file | JSON-filer pa disk (default) | Utveckling, sma system |
| syslog | Skickar till syslog daemon | Integration med befintlig logging |
| journald | Systemd journal | Linux-servrar med systemd |
| gelf | Graylog Extended Log Format | Graylog-integration |
| fluentd | Skickar till Fluentd | Kubernetes, centraliserad logging |
| awslogs | AWS CloudWatch | AWS-miljoer |
| splunk | Splunk HTTP Event Collector | Splunk-integration |

### Konfigurera log driver

```bash
# Per container
docker run --log-driver=syslog --log-opt syslog-address=udp://logserver:514 myimage

# Med json-file och rotation
docker run --log-driver=json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  myimage

# Viktigt: Vissa log drivers stodjer inte docker logs!
# json-file, journald och local stodjer det
# syslog, gelf, fluentd gor INTE det
```

### Hitta loggfiler manuellt

```bash
# Default loggplats for json-file driver
sudo cat /var/lib/docker/containers/<container-id>/<container-id>-json.log

# Hitta container ID
docker inspect --format='{{.Id}}' mycontainer
```

------------------------------------------------------------

## Praktiska Exempel

Nar loggar inte racker behover du komma in i containern och undersoka direkt. docker exec later dig kora kommandon i en korande container.

### Grundlaggande exec-kommandon

```bash
# Oppna interaktiv shell
docker exec -it mycontainer /bin/bash
docker exec -it mycontainer /bin/sh  # om bash saknas

# Kora enskilt kommando
docker exec mycontainer cat /etc/hosts
docker exec mycontainer env
docker exec mycontainer ps aux

# Kora som root (om containern kor som annan user)
docker exec -u 0 mycontainer bash
docker exec --user root mycontainer bash

# Kora med specifika environment-variabler
docker exec -e DEBUG=true mycontainer printenv

# Kora i specifik arbetskatalog
docker exec -w /app mycontainer ls -la
```

### Vanliga debugging-kommandon inne i container

```bash
# Nar du ar inne i containern:

# Kolla processer
ps aux
top

# Kolla natverksanslutningar
netstat -tulpn
ss -tulpn

# Kolla DNS-upplosning
cat /etc/resolv.conf
nslookup google.com
dig google.com

# Kolla diskutrymme
df -h
du -sh /*

# Kolla environment
env | sort
printenv

# Kolla oppna filer
lsof

# Kolla systemloggar (om tillgangliga)
cat /var/log/messages
dmesg
```

### Vad gor du nar verktyg saknas?

Manga produktionsimages ar minimala och saknar debugging-verktyg. Har ar losningar:

```bash
# Alternativ 1: Installera i korande container (temporart)
docker exec -u 0 mycontainer apt-get update && apt-get install -y curl net-tools

# Alternativ 2: Anvand netshoot (se Debug Tools sektionen)
docker run -it --net container:mycontainer nicolaka/netshoot

# Alternativ 3: Kopiera in verktyg
docker cp /usr/bin/strace mycontainer:/tmp/
docker exec mycontainer /tmp/strace -p 1
```

------------------------------------------------------------

## Bästa Praxis

docker inspect ger dig ALL information om en container - konfiguration, natverk, mounts, state och mer. Det ar som att lasa containerns fullstandiga journal.

### Grundlaggande inspect

```bash
# All metadata (JSON output)
docker inspect mycontainer

# Formaterad output med Go templates
docker inspect --format='{{.State.Status}}' mycontainer
docker inspect --format='{{.State.ExitCode}}' mycontainer
docker inspect --format='{{.NetworkSettings.IPAddress}}' mycontainer
```

### Vanliga inspect-queries

```bash
# Container state
docker inspect --format='{{.State.Status}}' mycontainer
docker inspect --format='{{.State.Running}}' mycontainer
docker inspect --format='{{.State.ExitCode}}' mycontainer
docker inspect --format='{{.State.OOMKilled}}' mycontainer
docker inspect --format='{{.State.Error}}' mycontainer

# Natverk
docker inspect --format='{{.NetworkSettings.IPAddress}}' mycontainer
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mycontainer
docker inspect --format='{{json .NetworkSettings.Ports}}' mycontainer | jq

# Mounts och volumes
docker inspect --format='{{json .Mounts}}' mycontainer | jq
docker inspect --format='{{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}' mycontainer

# Environment variabler
docker inspect --format='{{json .Config.Env}}' mycontainer | jq

# Resource limits
docker inspect --format='{{.HostConfig.Memory}}' mycontainer
docker inspect --format='{{.HostConfig.CpuShares}}' mycontainer

# Image information
docker inspect --format='{{.Config.Image}}' mycontainer
docker inspect --format='{{.Image}}' mycontainer  # full SHA
```

### Exit Codes - Vad betyder de?

```
+------------------------------------------------------------+
|                    EXIT CODES                              |
+------------------------------------------------------------+
|                                                            |
|   Code    Betydelse                                        |
|   ----    ---------                                        |
|   0       Normal avslutning (success)                      |
|   1       Generellt applikationsfel                        |
|   126     Permission denied (kan inte kora)                |
|   127     Command not found                                |
|   128+N   Fatal signal N (t.ex. 137 = 128+9 = SIGKILL)    |
|   137     SIGKILL (ofta OOM-killer)                        |
|   143     SIGTERM (graceful shutdown)                      |
|   255     Exit status out of range                         |
|                                                            |
+------------------------------------------------------------+
```

```bash
# Debugga baserat pa exit code
EXIT_CODE=$(docker inspect --format='{{.State.ExitCode}}' mycontainer)

case $EXIT_CODE in
  0)   echo "Normal exit" ;;
  1)   echo "App error - check logs" ;;
  137) echo "OOM killed or SIGKILL" ;;
  143) echo "SIGTERM - graceful shutdown" ;;
  *)   echo "Unknown exit code: $EXIT_CODE" ;;
esac
```

------------------------------------------------------------

## Kopplingar

docker events visar systemhandelser i realtid - perfekt for att forsta VAD som triggade ett problem.

### Grundlaggande events

```bash
# Alla events i realtid
docker events

# Events for specifik container
docker events --filter container=mycontainer

# Events for specifik typ
docker events --filter type=container
docker events --filter type=image
docker events --filter type=network
docker events --filter type=volume

# Events for specifik action
docker events --filter event=start
docker events --filter event=stop
docker events --filter event=die
docker events --filter event=oom
```

### Historiska events

```bash
# Events sedan specifik tid
docker events --since "2024-01-15T10:00:00"
docker events --since "1h"

# Events inom tidsintervall
docker events --since "1h" --until "30m"
```

### Event-typer att kanna till

| Event | Beskrivning | Nar det intraffar |
|-------|-------------|-------------------|
| create | Container skapad | docker create/run |
| start | Container startad | docker start/run |
| die | Container avslutad | Process exited |
| stop | Container stoppad | docker stop |
| kill | Container killad | docker kill eller OOM |
| oom | Out of memory | Minnet slut |
| pause | Container pausad | docker pause |
| unpause | Container opausad | docker unpause |
| restart | Container omstartad | docker restart |
| destroy | Container borttagen | docker rm |

### Praktiskt: Overvaka for OOM

```bash
# Kolla om container dog av OOM
docker events --filter event=oom --filter container=mycontainer

# Kombinera med inspect
docker inspect --format='{{.State.OOMKilled}}' mycontainer
```

------------------------------------------------------------

## Nyckelkommandon

Har ar ett systematiskt tillvagagangssatt for att debugga containerproblem:

```
+------------------------------------------------------------+
|           DEBUGGING WORKFLOW                               |
+------------------------------------------------------------+
|                                                            |
|   STEG 1: Identifiera problemet                           |
|   +----------------------------------------------------+   |
|   | - Vilken container? docker ps -a                   |   |
|   | - Nar hande det? docker events --since "1h"        |   |
|   | - Vad ar status? docker inspect --format State     |   |
|   +----------------------------------------------------+   |
|                         |                                  |
|                         v                                  |
|   STEG 2: Samla loggar                                    |
|   +----------------------------------------------------+   |
|   | - docker logs --tail 200 container                 |   |
|   | - Kolla exit code                                  |   |
|   | - Kolla OOMKilled                                  |   |
|   +----------------------------------------------------+   |
|                         |                                  |
|                         v                                  |
|   STEG 3: Djupare analys                                  |
|   +----------------------------------------------------+   |
|   | - docker exec for live debugging                   |   |
|   | - docker inspect for konfiguration                 |   |
|   | - Testa med debug-container                        |   |
|   +----------------------------------------------------+   |
|                         |                                  |
|                         v                                  |
|   STEG 4: Atgarda och verifiera                           |
|   +----------------------------------------------------+   |
|   | - Fixa konfiguration eller kod                     |   |
|   | - Starta om container                              |   |
|   | - Overvaka med docker events/stats                 |   |
|   +----------------------------------------------------+   |
|                                                            |
+------------------------------------------------------------+
```

### Snabb-checklista

```bash
# 1. Vad ar status?
docker ps -a | grep mycontainer

# 2. Vad sager loggarna?
docker logs --tail 100 mycontainer

# 3. Vad ar exit code?
docker inspect --format='{{.State.ExitCode}}' mycontainer

# 4. OOM?
docker inspect --format='{{.State.OOMKilled}}' mycontainer

# 5. Nar dog den?
docker inspect --format='{{.State.FinishedAt}}' mycontainer

# 6. Vad var senaste events?
docker events --filter container=mycontainer --since "1h"
```

------------------------------------------------------------

## Vanliga Fallgropar

Natverksproblem ar bland de vanligaste issues i Docker. Har ar hur du debuggar dem.

### Diagnostik-kommandon

```bash
# Kolla container IP
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mycontainer

# Kolla vilka natverk containern ar pa
docker inspect --format='{{json .NetworkSettings.Networks}}' mycontainer | jq

# Kolla port mappings
docker port mycontainer

# Lista alla natverk
docker network ls

# Inspektera natverk
docker network inspect mynetwork
```

### Testa konnektivitet

```bash
# Testa DNS fran container
docker exec mycontainer nslookup otherservice
docker exec mycontainer cat /etc/resolv.conf

# Testa TCP-anslutning
docker exec mycontainer nc -zv otherservice 8080

# Testa HTTP
docker exec mycontainer curl -v http://otherservice:8080/health

# Ping (om ICMP tillats)
docker exec mycontainer ping -c 3 otherservice
```

### Vanliga natverksproblem

```
+------------------------------------------------------------+
|              NATVERK TROUBLESHOOTING                       |
+------------------------------------------------------------+
|                                                            |
|   Problem: Container kan inte na annan container           |
|   +----------------------------------------------------+   |
|   | 1. Ar de pa samma natverk?                         |   |
|   |    docker network inspect mynetwork                |   |
|   | 2. Anvander du ratt hostname?                      |   |
|   |    (container name = DNS name pa custom networks)  |   |
|   | 3. Ar porten exponerad internt?                    |   |
|   |    EXPOSE i Dockerfile eller --expose              |   |
|   +----------------------------------------------------+   |
|                                                            |
|   Problem: Kan inte na container fran host                 |
|   +----------------------------------------------------+   |
|   | 1. Ar porten publicerad?                           |   |
|   |    docker port mycontainer                         |   |
|   | 2. Lystsnar appen pa ratt interface?               |   |
|   |    (0.0.0.0 inte 127.0.0.1)                        |   |
|   | 3. Brandvagg blockerar?                            |   |
|   |    sudo iptables -L -n                             |   |
|   +----------------------------------------------------+   |
|                                                            |
+------------------------------------------------------------+
```

### Anvand netshoot for avancerad debugging

```bash
# Anslut till containers network namespace
docker run -it --net container:mycontainer nicolaka/netshoot

# Nu har du tillgang till alla natverksverktyg:
# tcpdump, netstat, nmap, curl, dig, etc.
```

------------------------------------------------------------

## Referenser

Har ar de vanligaste felmeddelandena och hur du loser dem:

| Fel | Orsak | Losning |
|-----|-------|---------|
| OCI runtime exec failed | Container ej running | Starta containern forst |
| executable file not found | CMD/ENTRYPOINT fel | Kolla att binaren finns i image |
| permission denied | Fel ratighter | Kolla user, chmod, chown |
| port is already allocated | Port upptagen | Byt port eller stoppa annan process |
| no space left on device | Disk full | docker system prune -a |
| cannot connect to Docker daemon | Docker ej igång | sudo systemctl start docker |
| network not found | Natverket finns ej | docker network create |
| name already in use | Container med samma namn | docker rm eller annat namn |

### Djupdykning i vanliga fel

```bash
# "OCI runtime exec failed: exec failed: container_linux.go"
# Containern kor inte - starta den
docker start mycontainer

# "executable file not found in $PATH"
# Kommandot finns inte i imagen
docker run -it myimage ls /bin/  # Se vad som finns
docker run -it myimage which bash  # Prova hitta bash/sh

# "permission denied"
# Kolla ratigheter och user
docker exec mycontainer ls -la /app
docker exec mycontainer id  # Se vilken user containern kor som

# "port is already allocated"
# Hitta vad som anvander porten
sudo lsof -i :8080
sudo netstat -tulpn | grep 8080

# "no space left on device"
docker system df  # Se vad som tar plats
docker system prune -a --volumes  # Rensa allt onodit
```

------------------------------------------------------------



Specialiserade verktyg gor Docker-debugging mycket enklare.

### netshoot - Natverksdebugging

```bash
# netshoot har alla natverksverktyg du behover
docker run -it --net container:mycontainer nicolaka/netshoot

# Eller som sidecar i docker-compose
# services:
#   debug:
#     image: nicolaka/netshoot
#     network_mode: "service:myapp"

# Verktyg inkluderade:
# - tcpdump, wireshark
# - netstat, ss, ip
# - curl, wget
# - dig, nslookup
# - nmap, netcat
# - iperf, mtr
```

### dive - Image Layer Analys

```bash
# Installera dive
brew install dive  # macOS
# eller
docker pull wagoodman/dive

# Analysera image layers
dive myimage:latest

# Interaktivt granssnitt visar:
# - Varje layer och dess storlek
# - Vilka filer som lagts till/andrats
# - Slosakvot (wasted space)
# - Potentiella optimeringar
```

### ctop - Container Monitoring

```bash
# Installera ctop
brew install ctop  # macOS
# eller
docker run --rm -it \
  --name ctop \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  quay.io/vektorlab/ctop

# ctop visar:
# - CPU/Memory/Net/IO for alla containers
# - Interaktiv sortering och filtrering
# - Snabbkommandon for start/stop/logs
```

### lazydocker - TUI for Docker

```bash
# Installera lazydocker
brew install lazydocker

# Kor
lazydocker

# Ger dig:
# - Oversikt av containers, images, volumes
# - Logs i realtid
# - Stats och resursanvandning
# - Snabbkommandon for vanliga operationer
```

### docker debug (Docker Desktop)

```bash
# Nytt verktyg i Docker Desktop
docker debug mycontainer

# Startar shell med extra verktyg
# Fungerar aven pa minimala images
```

------------------------------------------------------------

## Övningar

### Ovning 1: Debugga en kraschad container

En webserver-container kraschar vid start. Anvand debugging-tekniker for att hitta och losa problemet.

```bash
# Skapa en buggig container
docker run -d --name buggy-web nginx:alpine sh -c "exit 1"

# Din uppgift:
# 1. Kolla containerns status
# 2. Ta reda pa exit code
# 3. Kolla loggarna
# 4. Bestam orsaken och losa problemet
```

<details>
<summary>Ledtrad</summary>

Borja med docker ps -a for att se containerns status. Anvand sedan docker inspect for att se exit code och docker logs for eventuella felmeddelanden. Exit code 1 indikerar ett applikationsfel.

</details>

<details>
<summary>Losning</summary>

```bash
# Steg 1: Kolla status
docker ps -a | grep buggy-web
# Visar: Exited (1)

# Steg 2: Kolla exit code
docker inspect --format='{{.State.ExitCode}}' buggy-web
# Output: 1

# Steg 3: Kolla loggar
docker logs buggy-web
# Inga loggar - kommandot dog direkt

# Steg 4: Analysera - vi skickade "exit 1" som kommando
# Det ersatte nginx startkommando

# Losning - kor nginx korrekt:
docker rm buggy-web
docker run -d --name buggy-web nginx:alpine
# Nu startar nginx korrekt
```

</details>

### Ovning 2: Network Troubleshooting

Tva containers ska kommunicera men det fungerar inte. Debugga natverksproblemet.

```bash
# Skapa scenario med natverksproblem
docker network create isolated
docker run -d --name web --network isolated nginx:alpine
docker run -d --name client alpine sleep 3600

# Din uppgift:
# 1. Forklara varfor client inte kan na web
# 2. Diagnosticera med ratt verktyg
# 3. Los problemet
```

<details>
<summary>Ledtrad</summary>

Kolla vilka natverk varje container tillhor med docker network inspect. Containers pa olika natverk kan inte kommunicera direkt om de inte delar ett gemensamt natverk eller om host networking anvands.

</details>

<details>
<summary>Losning</summary>

```bash
# Steg 1: Identifiera problemet
docker network inspect isolated
# web ar pa "isolated" network

docker inspect client --format='{{json .NetworkSettings.Networks}}' | jq
# client ar pa default "bridge" network

# Steg 2: Verifiera att de inte kan kommunicera
docker exec client ping web
# ping: bad address 'web' (DNS fungerar inte mellan natverk)

# Steg 3: Los genom att lagga client pa samma natverk
docker network connect isolated client

# Steg 4: Verifiera
docker exec client ping -c 3 web
# Nu fungerar det!

# Alternativ losning - skapa client pa ratt natverk fran borjan:
docker rm -f client
docker run -d --name client --network isolated alpine sleep 3600
```

</details>

### Ovning 3: Memory Debugging

En container blir OOM-killed. Identifiera problemet och los det.

```bash
# Skapa container med lag minnesgrans som kommer OOM-killed
docker run -d --name memory-hog --memory=10m alpine sh -c "
  while true; do
    dd if=/dev/zero of=/tmp/fill bs=1M count=100 2>/dev/null
    sleep 1
  done
"

# Vanta nagra sekunder, sen:
# Din uppgift:
# 1. Bekrafta att containern dog av OOM
# 2. Ta reda pa minnesbegransningen
# 3. Los problemet med en rimlig minnesgrans
```

<details>
<summary>Ledtrad</summary>

Anvand docker inspect for att kolla State.OOMKilled. For att se minnesbegransningen, kolla HostConfig.Memory. Kom ihag att docker stats visar realtidsanvandning om containern fortfarande kor.

</details>

<details>
<summary>Losning</summary>

```bash
# Steg 1: Kolla om OOM-killed
docker inspect --format='{{.State.OOMKilled}}' memory-hog
# Output: true

# Steg 2: Kolla minnesbegransningen
docker inspect --format='{{.HostConfig.Memory}}' memory-hog
# Output: 10485760 (10MB i bytes)

# Steg 3: Se exit code (128+9=137 for SIGKILL)
docker inspect --format='{{.State.ExitCode}}' memory-hog
# Output: 137

# Steg 4: Los med mer minne
docker rm memory-hog
docker run -d --name memory-hog --memory=256m alpine sh -c "
  while true; do
    dd if=/dev/zero of=/tmp/fill bs=1M count=100 2>/dev/null
    sleep 1
  done
"

# Verifiera att den kor
docker stats memory-hog --no-stream
```

</details>

------------------------------------------------------------

## Sammanfattning

I den har noden har du lart dig att systematiskt debugga Docker-containrar:

| Verktyg | Anvandning | Nar |
|---------|-----------|-----|
| docker logs | Se applikationsutdata | Forsta steget alltid |
| docker inspect | Metadata och konfiguration | Exit codes, OOM, natverk |
| docker exec | Interaktiv debugging | Nar loggar inte racker |
| docker events | Systemhandelser | Forsta VAD som hande |

Du har ocksa lart dig:

- Log drivers och hur de paverkar loggning
- Exit codes och vad de betyder
- Network troubleshooting tekniker
- Specialverktyg som netshoot, dive och ctop
- Vanliga felmeddelanden och deras losningar

Kom ihag debugging-mantrat: **Loggar forst, inspect sen, exec om nodat**. Med systematisk approach och ratt verktyg kan du losa de flesta containerproblem snabbt och effektivt.

------------------------------------------------------------

## Referenser

| Resurs | Lank |
|--------|------|
| Docker Logs Reference | https://docs.docker.com/engine/reference/commandline/logs/ |
| Docker Inspect Reference | https://docs.docker.com/engine/reference/commandline/inspect/ |
| Log Drivers | https://docs.docker.com/config/containers/logging/configure/ |
| netshoot | https://github.com/nicolaka/netshoot |
| dive | https://github.com/wagoodman/dive |
| ctop | https://github.com/bcicen/ctop |
| lazydocker | https://github.com/jesseduffield/lazydocker |
""",
        },
        {
            "title": "Docker with CI/CD",
            "slug": "docker-with-cicd",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker with CI/CD

------------------------------------------------------------

## Introduktion

Forestall dig att du sitter i ett team som deployar manuellt. Nagon bygger imagen lokalt, nagon annan pushar till registryt, en tredje loggar in pa servern och kor docker pull. Det tar timmar, det ar felbenaget, och nagon glomde att tagga imagen ratt sa nu vet ingen vilken version som kors i produktion.

Det har ar verkligheten for manga team innan de implementerar Docker i sin CI/CD-pipeline. Och det ar exakt det problem som den har noden loser.

Nar du integrerar Docker med CI/CD far du automatiserade, reproducerbara deployments. Varje commit triggar en build. Varje image taggas med commit-SHA for perfekt sparbarhet. Varje deployment ar identisk oavsett vem som triggar den eller nar. Det ar skillnaden mellan amatormassig och professionell mjukvaruleverans.

Som DevOps-ingenjor kommer du konfigurera dessa pipelines dagligen. Du kommer optimera build-tider med smart caching, sakerstalla att inga sarbara images nar produktion genom automatisk scanning, och bygga deployment-workflows som teamet kan lita pa. Utan den har kunskapen ar du bara en som kor kommandon - med den ar du en som bygger system.

------------------------------------------------------------

## Teori

### Varfor Docker i CI/CD?

Traditionell CI/CD hanterar kod - den bygger, testar och deployar applikationer. Men med Docker hanterar du hela miljon. Du paketerar inte bara din applikation, utan allt den behover for att kora: runtime, bibliotek, konfiguration, allt.

```
+------------------------------------------------------------+
|              TRADITIONELL CI/CD VS DOCKER CI/CD            |
+------------------------------------------------------------+
|                                                            |
|  Traditionell:                Docker-baserad:              |
|  ------------                 ---------------              |
|                                                            |
|  1. Bygg kod                  1. Bygg Docker image         |
|  2. Kor tester                2. Kor tester i container    |
|  3. Kopiera filer till        3. Push image till registry  |
|     server                    4. Pull och kor pa server    |
|  4. Installera beroenden                                   |
|  5. Starta om tjansterna      Samma miljo overallt!        |
|                                                            |
|  Problem: "Works on my        Losning: Identisk container  |
|  machine" i varje steg        fran dev till prod           |
|                                                            |
+------------------------------------------------------------+
```

### CI/CD Pipeline-stadier for Docker

En typisk Docker CI/CD-pipeline har foljande stadier:

```
+------------------------------------------------------------+
|                    DOCKER CI/CD PIPELINE                   |
+------------------------------------------------------------+
|                                                            |
|   +--------+    +--------+    +--------+    +--------+     |
|   |  BUILD |    |  TEST  |    |  SCAN  |    | DEPLOY |     |
|   +--------+    +--------+    +--------+    +--------+     |
|       |             |             |             |          |
|       v             v             v             v          |
|   Dockerfile    Container     Trivy/         Registry      |
|   Multi-stage   som test-    Snyk for       + Server       |
|   Build         miljo        CVE:er         Deployment     |
|                                                            |
+------------------------------------------------------------+
|                                                            |
|   Triggers:                                                |
|   - Push till main -> Full pipeline + deploy               |
|   - Pull Request -> Build + Test + Scan (ingen deploy)     |
|   - Tag (v1.2.3) -> Build + Release till prod              |
|                                                            |
+------------------------------------------------------------+
```

### Image Tagging-strategier

Hur du taggar dina images ar kritiskt for sparbarhet och rollbacks:

| Tagg-typ | Format | Anvandning | Exempel |
|----------|--------|------------|---------|
| **SHA** | Kort commit-hash | Unik identifiering | myapp:a1b2c3d |
| **Branch** | Branch-namn | Development/staging | myapp:main |
| **Semver** | Semantisk version | Releases | myapp:1.2.3 |
| **Latest** | Senaste build | Convenience (undvik i prod) | myapp:latest |
| **PR** | Pull request-nummer | Review-miljoer | myapp:pr-42 |

```
+------------------------------------------------------------+
|                    TAGGING BEST PRACTICES                  |
+------------------------------------------------------------+
|                                                            |
|   REKOMMENDERAD STRATEGI:                                  |
|                                                            |
|   Vid varje build, skapa FLERA taggar:                     |
|                                                            |
|   docker build -t myapp:a1b2c3d \\                          |
|                 -t myapp:main \\                            |
|                 -t myapp:latest .                          |
|                                                            |
|   Vid release, lagg till semver:                           |
|                                                            |
|   docker tag myapp:a1b2c3d myapp:1.2.3                     |
|   docker tag myapp:a1b2c3d myapp:1.2                       |
|   docker tag myapp:a1b2c3d myapp:1                         |
|                                                            |
+------------------------------------------------------------+
```

### Cache-strategier for snabbare builds

Docker-builds kan vara lAngsamma, men med ratt caching kan du reducera build-tider dramatiskt:

```
+------------------------------------------------------------+
|                    CACHE-STRATEGIER                        |
+------------------------------------------------------------+
|                                                            |
|   1. LAYER CACHING                                         |
|      - Docker cachar varje layer                           |
|      - Andring i en layer invaliderar alla efterfoljande   |
|      - Ordna Dockerfile: sallan andrande forst             |
|                                                            |
|   2. BUILDX CACHE                                          |
|      +------------------+                                  |
|      |   type=gha       |  GitHub Actions cache (10GB)     |
|      +------------------+                                  |
|      |   type=registry  |  Cache i registry (persistent)   |
|      +------------------+                                  |
|      |   type=local     |  Lokal katalog (snabbast)        |
|      +------------------+                                  |
|                                                            |
|   3. DEPENDENCY CACHING                                    |
|      - Kopiera package.json FORE kallkod                   |
|      - npm ci cachar om package.json inte andrats          |
|                                                            |
+------------------------------------------------------------+
```

### Sakerhetsscanning i Pipeline

Att deploya sarbara images ar en av de vanligaste sakerhetsriskerna. Automatisk scanning loser detta:

```
+------------------------------------------------------------+
|              SECURITY SCANNING WORKFLOW                    |
+------------------------------------------------------------+
|                                                            |
|   +----------+     +----------+     +----------+           |
|   |  BUILD   | --> |   SCAN   | --> |  DECIDE  |           |
|   |  image   |     |  Trivy/  |     |  Pass/   |           |
|   +----------+     |  Snyk    |     |  Fail    |           |
|                    +----------+     +----------+           |
|                         |                |                 |
|                         v                v                 |
|                    +---------+     +-----------+           |
|                    | SARIF   |     | CRITICAL  |           |
|                    | Report  |     | = FAIL    |           |
|                    +---------+     | HIGH = ?  |           |
|                                    | MED = OK  |           |
|                                    +-----------+           |
|                                                            |
|   Vanliga verktyg:                                         |
|   - Trivy (gratis, snabb)                                  |
|   - Snyk (enterprise features)                             |
|   - Docker Scout (inbyggt i Docker)                        |
|   - Anchore (policy-baserat)                               |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett GitHub Actions Pipeline

Den har pipelinen bygger, testar, scannar och deployar en Docker-image:

```yaml
# .github/workflows/docker-cicd.yml
name: Docker CI/CD Pipeline

on:
  push:
    branches: [main, develop]
    tags: ['v*']
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ============================================
  # STEG 1: Bygg och testa
  # ============================================
  build-and-test:
    runs-on: ubuntu-latest
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata for Docker
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix=

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Run tests in container
        run: |
          docker run --rm ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} \\
            npm test

  # ============================================
  # STEG 2: Sakerhetsskanning
  # ============================================
  security-scan:
    needs: build-and-test
    runs-on: ubuntu-latest
    if: github.event_name != 'pull_request'

    steps:
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy scan results to GitHub Security
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'

  # ============================================
  # STEG 3: Deploy till staging
  # ============================================
  deploy-staging:
    needs: [build-and-test, security-scan]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    environment: staging

    steps:
      - name: Deploy to staging
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          script: |
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
            docker stop app || true
            docker rm app || true
            docker run -d --name app -p 8080:8080 \\
              ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}

  # ============================================
  # STEG 4: Deploy till produktion
  # ============================================
  deploy-production:
    needs: [build-and-test, security-scan]
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/tags/v')
    environment: production

    steps:
      - name: Deploy to production
        uses: appleboy/ssh-action@v1.0.0
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: |
            cd /opt/app
            docker compose pull
            docker compose up -d --remove-orphans
```

### Exempel 2: GitLab CI med Docker-in-Docker

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - scan
  - deploy

variables:
  DOCKER_HOST: tcp://docker:2376
  DOCKER_TLS_CERTDIR: "/certs"
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  IMAGE_LATEST: $CI_REGISTRY_IMAGE:latest

# ============================================
# Byggstadiet
# ============================================
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    # Bygg med cache fran tidigare builds
    - docker pull $IMAGE_LATEST || true
    - docker build
        --cache-from $IMAGE_LATEST
        --tag $IMAGE_TAG
        --tag $IMAGE_LATEST
        --build-arg BUILDKIT_INLINE_CACHE=1
        .
    - docker push $IMAGE_TAG
    - docker push $IMAGE_LATEST

# ============================================
# Teststadiet - kor tester i den byggda imagen
# ============================================
test:unit:
  stage: test
  image: $IMAGE_TAG
  script:
    - npm test
  coverage: '/Coverage: \\d+\\.\\d+%/'

test:integration:
  stage: test
  image: docker:24
  services:
    - docker:24-dind
    - postgres:15
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: testuser
    POSTGRES_PASSWORD: testpass
  script:
    - docker run --rm
        --network host
        -e DATABASE_URL=postgresql://testuser:testpass@postgres:5432/testdb
        $IMAGE_TAG npm run test:integration

# ============================================
# Sakerhetsscanning
# ============================================
security:trivy:
  stage: scan
  image:
    name: aquasec/trivy:latest
    entrypoint: [""]
  script:
    - trivy image --exit-code 1 --severity CRITICAL $IMAGE_TAG
  allow_failure: true

# ============================================
# Deploy till staging
# ============================================
deploy:staging:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$STAGING_SSH_KEY" | ssh-add -
  script:
    - ssh -o StrictHostKeyChecking=no $STAGING_USER@$STAGING_HOST "
        docker pull $IMAGE_TAG &&
        docker stop app || true &&
        docker rm app || true &&
        docker run -d --name app -p 8080:8080 $IMAGE_TAG
      "
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - develop

# ============================================
# Deploy till produktion med manuell approval
# ============================================
deploy:production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$PROD_SSH_KEY" | ssh-add -
  script:
    - ssh -o StrictHostKeyChecking=no $PROD_USER@$PROD_HOST "
        cd /opt/app &&
        docker compose pull &&
        docker compose up -d --remove-orphans
      "
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
```

### Exempel 3: Jenkins Pipeline med Docker

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'mycompany/myapp'
        IMAGE_TAG = "${env.BUILD_NUMBER}-${env.GIT_COMMIT.take(7)}"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Bygg Docker image
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Kor tester i containern
                    docker.image("${IMAGE_NAME}:${IMAGE_TAG}").inside {
                        sh 'npm test'
                    }
                }
            }
        }

        stage('Security Scan') {
            steps {
                // Scanna med Trivy
                sh '''
                    docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \\
                        aquasec/trivy:latest image \\
                        --exit-code 1 \\
                        --severity CRITICAL,HIGH \\
                        ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Push') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry("https://${REGISTRY}", 'docker-credentials') {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push('latest')
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sshagent(['staging-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@staging.example.com \\
                            'docker pull ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} && \\
                             docker stop app || true && \\
                             docker rm app || true && \\
                             docker run -d --name app -p 8080:8080 \\
                             ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
                    '''
                }
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
            }
            steps {
                sshagent(['prod-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@prod.example.com \\
                            'cd /opt/app && \\
                             docker compose pull && \\
                             docker compose up -d --remove-orphans'
                    '''
                }
            }
        }
    }

    post {
        always {
            // Rensa upp lokala images
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
        failure {
            // Notifiera vid fel
            slackSend(color: 'danger', message: "Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
        }
    }
}
```

### Exempel 4: Multi-Platform Build for ARM och AMD64

```yaml
# .github/workflows/multi-platform.yml
name: Multi-Platform Build

on:
  push:
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_TOKEN }}

      - name: Build and push multi-platform
        uses: docker/build-push-action@v5
        with:
          context: .
          platforms: linux/amd64,linux/arm64,linux/arm/v7
          push: true
          tags: |
            mycompany/myapp:${{ github.ref_name }}
            mycompany/myapp:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Konfigurera CI/CD Pipeline för Docker

1. **Skapa workflow-fil**
   ```yaml
   # .github/workflows/docker.yml
   name: Docker Build Pipeline
   on:
     push:
       branches: [main, develop]
     pull_request:
       branches: [main]
   ```

2. **Lägg till build-jobb**
   ```yaml
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: docker/setup-buildx-action@v3
   ```

3. **Konfigurera registry-login**
   ```yaml
         - uses: docker/login-action@v3
           with:
             registry: ghcr.io
             username: ${{ github.actor }}
             password: ${{ secrets.GITHUB_TOKEN }}
   ```

4. **Bygg och pusha image**
   ```yaml
         - uses: docker/build-push-action@v5
           with:
             context: .
             push: ${{ github.event_name != 'pull_request' }}
             tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
             cache-from: type=gha
             cache-to: type=gha,mode=max
   ```

### Steg 2: Implementera Multi-stage Testing

1. **Lägg till test-steg i Dockerfile**
   ```dockerfile
   # Test stage
   FROM base as test
   RUN npm test

   # Production stage
   FROM base as production
   COPY --from=build /app/dist ./dist
   ```

2. **Kör tester i pipeline**
   ```yaml
         - name: Run tests in container
           run: docker build --target test .
   ```

### Steg 3: Säkerhetsskanning

1. **Lägg till Trivy-skanning**
   ```yaml
         - name: Run Trivy vulnerability scanner
           uses: aquasecurity/trivy-action@master
           with:
             image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
             severity: 'CRITICAL,HIGH'
   ```

------------------------------------------------------------

## Bästa Praxis

### Tagging-strategi
- Använd **SHA-taggar** för spårbarhet: `myapp:abc123f`
- Använd **semver** för releases: `myapp:v1.2.3`
- Använd **branch-taggar** för utveckling: `myapp:develop`
- Undvik `:latest` i produktion

### Cache-optimering
- Aktivera BuildKit med `DOCKER_BUILDKIT=1`
- Använd GitHub Actions cache: `cache-from: type=gha`
- Ordna Dockerfile-lager för maximal cache-återanvändning

### Säkerhet i Pipelines
- Använd secrets för credentials: `${{ secrets.DOCKER_TOKEN }}`
- Skanna images innan push till produktion
- Använd read-only containers där möjligt
- Signera images med Docker Content Trust

### Parallellisering
- Bygg flera arkitekturer parallellt med Buildx
- Kör tester parallellt med lint-kontroller
- Använd matrix builds för flera versioner

------------------------------------------------------------

## Referenser

- [Docker Build Push Action](https://github.com/docker/build-push-action)
- [GitHub Actions for Docker](https://docs.docker.com/build/ci/github-actions/)
- [Docker Buildx Documentation](https://docs.docker.com/buildx/working-with-buildx/)
- [Trivy Security Scanner](https://aquasecurity.github.io/trivy/)
- [Docker Official CI/CD Best Practices](https://docs.docker.com/develop/dev-best-practices/)

------------------------------------------------------------

## Arkitekturöversikt

```
+------------------------------------------------------------+
|              DOCKER CI/CD ARKITEKTUR                       |
+------------------------------------------------------------+
|                                                            |
|  DEVELOPER                                                 |
|  +--------+                                                |
|  | git    |                                                |
|  | push   |                                                |
|  +---+----+                                                |
|      |                                                     |
|      v                                                     |
|  +------------------------------------------------------------+
|  |                    CI/CD PLATFORM                       |
|  |  (GitHub Actions / GitLab CI / Jenkins)                 |
|  +------------------------------------------------------------+
|  |                                                         |
|  |  +----------+  +----------+  +----------+  +----------+ |
|  |  |  BUILD   |->|   TEST   |->|   SCAN   |->|   PUSH   | |
|  |  | Dockerfile  | Container |  | Trivy    |  | Registry | |
|  |  | Buildx   |  | npm test |  | Snyk     |  | GHCR     | |
|  |  +----------+  +----------+  +----------+  +----------+ |
|  |                                                         |
|  +------------------------------------------------------------+
|      |                                     |               |
|      v                                     v               |
|  +------------------+              +------------------+    |
|  |     STAGING      |              |   PRODUCTION     |    |
|  |  +------------+  |              |  +------------+  |    |
|  |  | Container  |  |              |  | Container  |  |    |
|  |  | myapp:sha  |  |              |  | myapp:v1.0 |  |    |
|  |  +------------+  |              |  +------------+  |    |
|  +------------------+              +------------------+    |
|                                                            |
+------------------------------------------------------------+
```

```
+------------------------------------------------------------+
|              CACHE-STRATEGI I PRAKTIKEN                    |
+------------------------------------------------------------+
|                                                            |
|   Build 1 (ingen cache):                                   |
|   +----------------+                                       |
|   | FROM node:18   | Layer 1 - base                        |
|   | COPY pkg.json  | Layer 2 - dependencies def            |
|   | RUN npm ci     | Layer 3 - install (LANG TID)          |
|   | COPY . .       | Layer 4 - source code                 |
|   | RUN npm build  | Layer 5 - build                       |
|   +----------------+                                       |
|   Total tid: 5 minuter                                     |
|                                                            |
|   Build 2 (med cache, endast src andrad):                  |
|   +----------------+                                       |
|   | FROM node:18   | CACHED                                |
|   | COPY pkg.json  | CACHED                                |
|   | RUN npm ci     | CACHED (sparar 3 min!)                |
|   | COPY . .       | Ny layer                              |
|   | RUN npm build  | Ny layer                              |
|   +----------------+                                       |
|   Total tid: 45 sekunder                                   |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Vanliga Fallgropar

| Problem | Orsak | Losning |
|---------|-------|---------|
| Langa build-tider | Ingen caching | Implementera BuildX cache |
| "Image not found" | Push misslyckades | Kontrollera registry-login |
| Sakerhetssarbarhet i prod | Ingen scanning | Lagg till Trivy/Snyk-steg |
| Fel image i miljö | Tagging-problem | Anvand SHA-taggar konsekvent |
| Docker-in-Docker krasch | Privileges saknas | Anvand services: docker:dind |
| Cache fungerar inte | Felaktig Dockerfile-ordning | Kopiera dependencies forst |
| Multi-platform misslyckas | QEMU ej uppsatt | Lagg till setup-qemu-action |
| Registry rate limit | For manga pulls | Anvand authenticated pulls |

------------------------------------------------------------

## Övningar

### Ovning 1: Skapa en komplett GitHub Actions pipeline

Skapa en GitHub Actions workflow som bygger, testar och pushar en Docker-image med ratt tagging-strategi.

**Krav:**
- Bygg vid push till main och pull requests
- Tagga med SHA och branch-namn
- Anvand BuildX cache
- Pusha endast vid merge till main (inte PR)

<details>
<summary>Ledtrad</summary>

Du behover tre viktiga actions:
1. docker/setup-buildx-action for att aktivera BuildX
2. docker/metadata-action for att generera taggar automatiskt
3. docker/build-push-action for att bygga och pusha

Anvand villkoret github.event_name != 'pull_request' for att kontrollera om du ska pusha.

</details>

<details>
<summary>Losning</summary>

```yaml
# .github/workflows/docker.yml
name: Docker Build and Push

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix=

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

</details>

### Ovning 2: Implementera sakerhetsscanning som blockar deploys

Lagg till Trivy-scanning i din pipeline som stoppar deployment om kritiska sarbarheter hittas.

**Krav:**
- Scanna den byggda imagen med Trivy
- Misslyckas om CRITICAL-sarbarheter hittas
- Generera SARIF-rapport for GitHub Security-tabben
- Scanning ska koras efter build men fore deploy

<details>
<summary>Ledtrad</summary>

Trivy-action har flera viktiga parametrar:
- exit-code: 1 gor att jobbet misslyckas om sarbarheter hittas
- severity: Bestammer vilka nivaer som ska rapporteras
- format: sarif genererar rapport for GitHub Security

Du kan anvanda needs: for att kontrollera jobbordningen.

</details>

<details>
<summary>Losning</summary>

```yaml
jobs:
  build:
    # ... (fran forra ovningen)

  security-scan:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          exit-code: '1'
          severity: 'CRITICAL'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

  deploy:
    needs: [build, security-scan]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to production
        run: echo "Deploying secure image..."
```

</details>

### Ovning 3: Optimera build-tider med cache-strategi

Du har en pipeline som tar 8 minuter att bygga. Optimera den till under 2 minuter med ratt cache-strategi.

**Scenario:**
- Node.js-applikation
- npm ci tar 4 minuter
- npm run build tar 2 minuter
- Dockerfilen ar inte optimerad for cache

<details>
<summary>Ledtrad</summary>

Tva saker behovs:
1. Optimera Dockerfile-ordningen - kopiera package.json och package-lock.json FORE resten av koden
2. Anvand BuildX cache i CI/CD (type=gha eller type=registry)

Kom ihag: Docker invaliderar cache for alla layers efter en andrad layer.

</details>

<details>
<summary>Losning</summary>

**Optimerad Dockerfile:**
```dockerfile
FROM node:18-slim AS builder

WORKDIR /app

# Kopiera ENDAST dependency-filer forst
COPY package.json package-lock.json ./

# Installera dependencies (cachas om package*.json inte andrats)
RUN npm ci

# Kopiera resten av koden
COPY . .

# Bygg applikationen
RUN npm run build

# Production stage
FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

**Optimerad GitHub Actions:**
```yaml
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myapp:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
    # Alternativt for persistent cache:
    # cache-from: type=registry,ref=myapp:buildcache
    # cache-to: type=registry,ref=myapp:buildcache,mode=max
```

**Resultat:**
- Forsta build: 8 minuter (ingen cache)
- Efterfoljande builds (endast kodandring): 1-2 minuter
- Efterfoljande builds (dependency-andring): 5-6 minuter

</details>

------------------------------------------------------------

## Sammanfattning

| Koncept | Beskrivning | Best Practice |
|---------|-------------|---------------|
| **Image Tagging** | Identifiering av images | SHA + branch + semver |
| **Build Cache** | Snabbare builds | BuildX med type=gha |
| **Security Scanning** | Hitta sarbarheter | Trivy/Snyk i pipeline |
| **Multi-platform** | ARM/AMD64 support | QEMU + Buildx |
| **Registry Push** | Lagra images | GHCR/DockerHub/ECR |
| **Deployment** | Leverans till server | docker compose pull + up |

------------------------------------------------------------

## Nyckelkommandon

```bash
# Lokal testning av CI/CD-liknande build
docker buildx build --cache-from type=local,src=/tmp/cache \\
                    --cache-to type=local,dest=/tmp/cache \\
                    -t myapp:test .

# Scanna image lokalt
docker scout cves myapp:test
trivy image myapp:test

# Multi-platform build lokalt
docker buildx build --platform linux/amd64,linux/arm64 \\
                    -t myapp:multi .

# Tagga for release
docker tag myapp:abc123 myapp:1.0.0
docker tag myapp:abc123 myapp:1.0
docker tag myapp:abc123 myapp:1
docker tag myapp:abc123 myapp:latest

# Push alla taggar
docker push myapp --all-tags
```

------------------------------------------------------------

## Kopplingar

Efter att ha mastrat Docker i CI/CD ar du redo att:

- **Docker Swarm Basics** - Orkestrering for enklare produktionsmiljoer
- **Kubernetes** - Storskalig containerorkestrering
- **GitOps** - Deklarativ infrastruktur med ArgoCD/Flux

Docker i CI/CD ar grundstenen for modern mjukvaruleverans. Med automatiserade pipelines, smart caching och integrerad sakerhet kan du leverera snabbt och sakert - varje gang.
""",
        },
        {
            "title": "Docker Swarm Basics",
            "slug": "docker-swarm-basics",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Swarm Basics

------------------------------------------------------------

## Introduktion

Docker Swarm ar Dockers inbyggda orkestreringslager som gor det mojligt att kora containers over flera servrar med automatisk lastbalansering och failover.

| Scenario | Swarm ger dig |
|----------|---------------|
| Multi-host deploys | Containers fordelade over kluster |
| Hog tillganglighet | Automatisk omstart vid fel |
| Enkel skalning | Justera replicas med ett kommando |
| Integrerad upplevelse | Samma Docker CLI du redan kan |

Swarm ar ett utmarkt val for team som vill ha orkestrering utan komplexiteten hos Kubernetes. Det ar perfekt for smarre till medelstora produktionsmiljoer.

------------------------------------------------------------

## Teori

Swarm mode transformerar Docker fran en container-runtime till en fullstandig orkestreringsplattform:

```
+------------------------------------------------------------+
|                      SWARM CLUSTER                          |
+------------------------------------------------------------+
|                                                             |
|   +-------------+    +-------------+    +-------------+     |
|   |   MANAGER   |    |   MANAGER   |    |   MANAGER   |     |
|   |   (Leader)  |----|  (Follower) |----|  (Follower) |     |
|   +------+------+    +-------------+    +-------------+     |
|          |                                                  |
|          | Raft Consensus                                   |
|          |                                                  |
|   +------v------+    +-------------+    +-------------+     |
|   |   WORKER    |    |   WORKER    |    |   WORKER    |     |
|   | [Task][Task]|    | [Task][Task]|    | [Task][Task]|     |
|   +-------------+    +-------------+    +-------------+     |
|                                                             |
+------------------------------------------------------------+
```

| Begrepp | Beskrivning |
|---------|-------------|
| Manager node | Hanterar klusterstatus och schemalagger tasks |
| Worker node | Kor containers som tilldelats av managers |
| Service | Deklarativ definition av onskad applikation |
| Task | En instans av en container i en service |
| Overlay network | Natverk som spanner over alla noder |

------------------------------------------------------------

## Steg-för-steg Guide

For att starta ett Swarm-kluster maste du forst initiera en manager-nod:

```bash
# Initiera Swarm pa forsta maskinen (blir manager)
docker swarm init --advertise-addr 192.168.1.10

# Output visar join-token for workers
# Swarm initialized: current node is now a manager.
# To add a worker to this swarm, run:
#   docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377
```

| Kommando | Syfte |
|----------|-------|
| docker swarm init | Skapa nytt Swarm-kluster |
| docker swarm join-token worker | Visa token for att lagga till workers |
| docker swarm join-token manager | Visa token for att lagga till managers |
| docker node ls | Lista alla noder i klustret |
| docker swarm leave | Lamna Swarm-klustret |

```bash
# Visa join-token for workers
docker swarm join-token worker

# Visa join-token for extra managers
docker swarm join-token manager

# Pa worker-maskinen - anslut till klustret
docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# Verifiera att noden ar tillagd
docker node ls
# ID           HOSTNAME   STATUS   AVAILABILITY   MANAGER STATUS
# abc123 *     manager1   Ready    Active         Leader
# def456       worker1    Ready    Active
```

------------------------------------------------------------

## Steg-för-steg Guide

I Swarm arbetar du med services istallet for enskilda containers. En service definierar hur manga replicas som ska kora och Swarm hanterar resten:

```
+------------------------------------------------------------+
|                    SERVICES vs CONTAINERS                   |
+------------------------------------------------------------+
|                                                             |
|  docker run (en container):                                 |
|  +-------------+                                            |
|  | Container A |  <-- Manuell hantering                     |
|  +-------------+                                            |
|                                                             |
|  docker service create (managed):                           |
|  +-------------+  +-------------+  +-------------+          |
|  | Replica 1   |  | Replica 2   |  | Replica 3   |          |
|  +------+------+  +------+------+  +------+------+          |
|         |                |                |                 |
|         +-------+--------+--------+-------+                 |
|                 |                                           |
|          +------v------+                                    |
|          | Load        |  <-- Automatisk LB                 |
|          | Balancer    |                                    |
|          +-------------+                                    |
|                                                             |
+------------------------------------------------------------+
```

| Egenskap | docker run | docker service |
|----------|------------|----------------|
| Scope | En container | Flera replicas |
| Skalning | Manuell | Deklarativ |
| Failover | Ingen | Automatisk restart |
| Natverk | Manuell konfiguration | Overlay med inbyggd DNS |
| Updates | Stoppa och starta | Rolling updates |

```bash
# Skapa en service med 3 replicas
docker service create \\
    --name web \\
    --replicas 3 \\
    --publish 80:80 \\
    nginx:alpine

# Lista services
docker service ls

# Se detaljer om en service
docker service inspect web

# Se vilka tasks (containers) som kor
docker service ps web
```

------------------------------------------------------------

## Praktiska Exempel

Skalning i Swarm ar enkelt - du anger bara onskad antal replicas och Swarm hanterar fordelningen over tillgangliga noder:

```bash
# Skala upp till 5 replicas
docker service scale web=5

# Eller anvand update
docker service update --replicas 5 web

# Skala ner
docker service scale web=2

# Skala flera services samtidigt
docker service scale web=5 api=3 worker=10
```

```
+------------------------------------------------------------+
|                  REPLICA DISTRIBUTION                       |
+------------------------------------------------------------+
|                                                             |
|   Fore: web replicas=3                                      |
|   +----------+    +----------+    +----------+              |
|   | Worker 1 |    | Worker 2 |    | Worker 3 |              |
|   | [web.1]  |    | [web.2]  |    | [web.3]  |              |
|   +----------+    +----------+    +----------+              |
|                                                             |
|   Efter: docker service scale web=5                         |
|   +----------+    +----------+    +----------+              |
|   | Worker 1 |    | Worker 2 |    | Worker 3 |              |
|   | [web.1]  |    | [web.2]  |    | [web.3]  |              |
|   | [web.4]  |    |          |    | [web.5]  |              |
|   +----------+    +----------+    +----------+              |
|                                                             |
+------------------------------------------------------------+
```

| Kommando | Beskrivning |
|----------|-------------|
| docker service scale | Andra antal replicas |
| docker service update --replicas | Alternativ metod |
| docker service ps | Visa task-fordelning |
| docker node ps | Visa tasks pa specifik nod |

------------------------------------------------------------

## Vanliga Fallgropar

Swarm stacks lat dig definiera hela applikationer med docker-compose-filer och deploya dem som en enhet:

```yaml
# stack.yml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        failure_action: rollback
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
    networks:
      - frontend

  api:
    image: myapp/api:latest
    deploy:
      replicas: 2
      placement:
        constraints:
          - node.role == worker
    environment:
      - DATABASE_URL=postgres://db:5432/app
    networks:
      - frontend
      - backend

  db:
    image: postgres:15-alpine
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.labels.db == true
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend

networks:
  frontend:
    driver: overlay
  backend:
    driver: overlay
    internal: true

volumes:
  db-data:
```

```bash
# Deploya stack
docker stack deploy -c stack.yml myapp

# Lista stacks
docker stack ls

# Se services i en stack
docker stack services myapp

# Se alla tasks i en stack
docker stack ps myapp

# Ta bort stack
docker stack rm myapp
```

------------------------------------------------------------

## Bästa Praxis

Overlay networks mojliggor kommunikation mellan containers pa olika noder som om de var pa samma host:

```
+------------------------------------------------------------+
|                    OVERLAY NETWORK                          |
+------------------------------------------------------------+
|                                                             |
|   Node 1                    Node 2                          |
|   +------------------+      +------------------+            |
|   | +------+ +------+|      | +------+ +------+|            |
|   | |web.1 | |api.1 ||      | |web.2 | |api.2 ||            |
|   | +--+---+ +--+---+|      | +--+---+ +--+---+|            |
|   +----+--------+----+      +----+--------+----+            |
|        |        |                |        |                 |
|   +----v--------v----------------v--------v----+            |
|   |           OVERLAY: app-network             |            |
|   |   (VXLAN tunnel mellan noder)              |            |
|   +--------------------------------------------+            |
|                                                             |
+------------------------------------------------------------+
```

```bash
# Skapa overlay network (maste vara i swarm mode)
docker network create --driver overlay --attachable app-network

# Skapa encrypted overlay
docker network create \\
    --driver overlay \\
    --opt encrypted \\
    secure-network

# Skapa internal network (ingen extern access)
docker network create \\
    --driver overlay \\
    --internal \\
    backend-network

# Anslut service till network
docker service create \\
    --name api \\
    --network app-network \\
    myapp/api
```

| Network-typ | Anvandningsfall |
|-------------|-----------------|
| overlay | Multi-host kommunikation |
| overlay --encrypted | Krypterad trafik mellan noder |
| overlay --internal | Isolerat backend-natverk |
| ingress | Inbyggd lastbalansering (automatisk) |

------------------------------------------------------------

## Kopplingar

Swarm har inbyggd hantering av kanslig data (secrets) och konfigurationsfiler (configs):

```bash
# Skapa secret fran fil
echo "superSecretPassword" | docker secret create db_password -

# Skapa secret fran fil
docker secret create ssl_cert ./server.crt

# Lista secrets
docker secret ls

# Anvand secret i service
docker service create \\
    --name db \\
    --secret db_password \\
    postgres:15

# I containern finns secret i /run/secrets/db_password
```

```
+------------------------------------------------------------+
|                   SECRETS FLOW                              |
+------------------------------------------------------------+
|                                                             |
|   1. Skapa secret                                           |
|   +----------------+                                        |
|   | db_password    | --> Krypterat i Raft store             |
|   +----------------+                                        |
|                                                             |
|   2. Service far tillgang                                   |
|   +----------------+                                        |
|   | docker service |                                        |
|   | --secret       |                                        |
|   +-------+--------+                                        |
|           |                                                 |
|   3. Monteras i container                                   |
|   +-------v--------+                                        |
|   | /run/secrets/  |                                        |
|   | db_password    | --> Tillganglig som fil                |
|   +----------------+                                        |
|                                                             |
+------------------------------------------------------------+
```

```bash
# Configs for icke-kanslig konfiguration
docker config create nginx_conf ./nginx.conf

# Anvand config i service
docker service create \\
    --name web \\
    --config source=nginx_conf,target=/etc/nginx/nginx.conf \\
    nginx:alpine
```

| Typ | Anvandning | Placering i container |
|-----|------------|----------------------|
| secret | Losenord, API-nycklar, certifikat | /run/secrets/<name> |
| config | Konfigurationsfiler | Valfri target-path |

------------------------------------------------------------

## Nyckelkommandon

Swarm stodjer zero-downtime deploys genom rolling updates:

```bash
# Uppdatera service image
docker service update \\
    --image nginx:1.25 \\
    web

# Konfigurera update-beteende
docker service update \\
    --image nginx:1.25 \\
    --update-parallelism 2 \\
    --update-delay 10s \\
    --update-failure-action rollback \\
    --update-max-failure-ratio 0.25 \\
    web

# Rollback vid problem
docker service rollback web
```

```
+------------------------------------------------------------+
|                  ROLLING UPDATE                             |
+------------------------------------------------------------+
|                                                             |
|   Steg 1: Uppdatera 1/3 (parallelism=1)                    |
|   [v1.0] --> [v1.1]    [v1.0]    [v1.0]                    |
|                                                             |
|   Steg 2: Vanta (delay=10s), sedan 2/3                      |
|   [v1.1]    [v1.0] --> [v1.1]    [v1.0]                    |
|                                                             |
|   Steg 3: Sista replica                                     |
|   [v1.1]    [v1.1]    [v1.0] --> [v1.1]                    |
|                                                             |
|   Resultat: Alla pa v1.1 utan downtime                      |
|                                                             |
+------------------------------------------------------------+
```

| Parameter | Beskrivning |
|-----------|-------------|
| --update-parallelism | Antal tasks att uppdatera samtidigt |
| --update-delay | Tid mellan uppdateringar |
| --update-failure-action | pause, continue, rollback |
| --update-max-failure-ratio | Max andel misslyckade fore stopp |
| --rollback-parallelism | Antal att rollbacka samtidigt |

------------------------------------------------------------

## Referenser

| Aspekt | Docker Swarm | Kubernetes |
|--------|--------------|------------|
| Komplexitet | Enkel setup | Brant inlarningskurva |
| Skalbarhet | Hundratals noder | Tusentals noder |
| Ekosystem | Begransat | Enormt |
| CLI | Docker CLI (bekant) | kubectl (nytt verktyg) |
| Natverk | Overlay (enkelt) | CNI plugins (flexibelt) |
| Storage | Volumes | CSI drivers (avancerat) |
| Config mgmt | Secrets/Configs | ConfigMaps/Secrets + mer |
| Monitoring | Extern | Inbyggt med Metrics Server |
| Community | Mindre | Mycket storre |
| Cloud support | Begransad | Alla stora moln |

```
+------------------------------------------------------------+
|              NAR VALJA VAD?                                  |
+------------------------------------------------------------+
|                                                             |
|   SWARM passar for:                                         |
|   - Sma till medelstora team                                |
|   - Enklare produktionsmiljoer                              |
|   - Snabb setup utan mycket inlarning                       |
|   - Nar du redan kan Docker                                 |
|                                                             |
|   KUBERNETES passar for:                                    |
|   - Storskaliga distribuerade system                        |
|   - Komplexa microservice-arkitekturer                      |
|   - Nar du behover avancerad scheduling                     |
|   - Managed K8s i molnet (EKS, GKE, AKS)                   |
|                                                             |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Skapa ett Swarm-kluster

Initiera ett single-node Swarm-kluster, skapa en nginx-service med 3 replicas, och verifiera att alla tasks kor.

<details>
<summary>Ledtrad</summary>
Anvand docker swarm init for att starta klustret och docker service create med --replicas flaggan.
</details>

<details>
<summary>Losning</summary>

```bash
# Initiera swarm
docker swarm init

# Skapa service med 3 replicas
docker service create \\
    --name web \\
    --replicas 3 \\
    --publish 8080:80 \\
    nginx:alpine

# Verifiera services
docker service ls

# Se alla tasks
docker service ps web

# Testa att det fungerar
curl http://localhost:8080
```

</details>

### Ovning 2: Deploya en stack med secrets

Skapa en stack som innehaller en PostgreSQL-databas med losenordet lagrat som en Swarm secret.

<details>
<summary>Ledtrad</summary>
Skapa forst secret med docker secret create, sedan referera till den i din stack.yml under secrets-sektionen.
</details>

<details>
<summary>Losning</summary>

```bash
# Skapa secret
echo "secretpassword123" | docker secret create postgres_password -

# Skapa stack.yml
cat > stack.yml << 'EOF'
version: "3.8"
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/postgres_password
    secrets:
      - postgres_password
    volumes:
      - db-data:/var/lib/postgresql/data
    deploy:
      replicas: 1

secrets:
  postgres_password:
    external: true

volumes:
  db-data:
EOF

# Deploya stack
docker stack deploy -c stack.yml dbstack

# Verifiera
docker stack services dbstack
docker stack ps dbstack
```

</details>

### Ovning 3: Utfor en rolling update

Uppdatera en service fran nginx:1.24 till nginx:1.25 med rolling update (1 task i taget, 15 sekunder delay) och verifiera att uppdateringen lyckas.

<details>
<summary>Ledtrad</summary>
Anvand docker service update med --update-parallelism och --update-delay flaggorna.
</details>

<details>
<summary>Losning</summary>

```bash
# Skapa initial service med aldre version
docker service create \\
    --name myapp \\
    --replicas 4 \\
    --publish 8080:80 \\
    nginx:1.24

# Verifiera nuvarande version
docker service ps myapp

# Utfor rolling update
docker service update \\
    --image nginx:1.25 \\
    --update-parallelism 1 \\
    --update-delay 15s \\
    --update-failure-action rollback \\
    myapp

# Folj uppdateringen
watch docker service ps myapp

# Verifiera ny version
docker service inspect myapp --pretty | grep Image
```

</details>

------------------------------------------------------------

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Swarm mode | Dockers inbyggda orkestrering |
| Manager/Worker | Nodroller i klustret |
| Services | Deklarativ container-hantering |
| Stacks | Multi-service applikationer |
| Overlay networks | Natverk over flera hosts |
| Secrets/Configs | Saker konfigurationshantering |
| Rolling updates | Zero-downtime deploys |

Swarm ar ett utmarkt val for teams som vill ha containerorkestrering utan Kubernetes komplexitet. Det ar integrerat i Docker, anvander samma CLI, och ger dig high availability, skalning och rolling updates direkt ur ladan.
""",
        },
        {
            "title": "Docker Best Practices Summary",
            "slug": "docker-best-practices-summary",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Best Practices Summary

------------------------------------------------------------

## Introduktion

Best practices ar skillnaden mellan en Docker-deployment som fungerar och en som
ar saker, skalbar och underhallbar. Denna sammanfattning tar alla viktiga
principer fran tidigare moduler och ger dig en komplett checklista.

| Omrade | Utan Best Practices | Med Best Practices |
|--------|---------------------|-------------------|
| Images | 2GB, 500+ CVEs | 50MB, 0 kritiska |
| Sakerhet | Root, alla portar | Non-root, minimal |
| Drift | Manuell restart | Self-healing |
| CI/CD | Flaky builds | Reproducerbara |

------------------------------------------------------------

## Teori Checklista

Varje Dockerfile bor folja dessa regler:

```
+----------------------------------------------------------+
|              DOCKERFILE BEST PRACTICES                   |
+----------------------------------------------------------+
|                                                          |
|  1. BASE IMAGE                                           |
|     +-- Specifik tag (ALDRIG :latest)                    |
|     +-- Minimal variant (slim/alpine)                    |
|     +-- Officiell eller verifierad                       |
|                                                          |
|  2. BUILD OPTIMIZATION                                   |
|     +-- Multi-stage builds                               |
|     +-- Cache-vanlig ordning (deps forst)                |
|     +-- Kombinera RUN-kommandon                          |
|     +-- .dockerignore fil                                |
|                                                          |
|  3. SECURITY                                             |
|     +-- Non-root USER                                    |
|     +-- Inga hardkodade secrets                          |
|     +-- Minimal paket installerade                       |
|                                                          |
|  4. RUNTIME                                              |
|     +-- HEALTHCHECK definierad                           |
|     +-- EXPOSE dokumenterar portar                       |
|     +-- Labels for metadata                              |
|                                                          |
+----------------------------------------------------------+
```

Exempel pa optimerad Dockerfile:

```dockerfile
# Steg 1: Specifik, minimal base
FROM python:3.11-slim AS base

# Steg 2: Labels for metadata
LABEL maintainer="team@example.com"
LABEL version="1.0.0"

# Steg 3: Skapa non-root user tidigt
RUN useradd --create-home --shell /bin/bash appuser

# Steg 4: Installera dependencies forst (cache)
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Steg 5: Kopiera applikationskod
COPY --chown=appuser:appuser . .

# Steg 6: Byt till non-root
USER appuser

# Steg 7: Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \\
    CMD curl -f http://localhost:8000/health || exit 1

# Steg 8: Dokumentera port
EXPOSE 8000

CMD ["python", "app.py"]
```

------------------------------------------------------------

## Steg-för-steg Guide

Hur du bygger, taggar och hanterar images:

| Praxis | Darfor | Exempel |
|--------|--------|---------|
| Slim/Alpine | Mindre attack yta | python:3.11-slim |
| Specifika taggar | Reproducerbarhet | nginx:1.25.3-alpine |
| Scanna for CVE | Hitta sarbarheter | docker scout cves |
| Signera images | Verifiera ursprung | DCT, cosign |
| Multi-arch | Stod ARM + x86 | docker buildx |

```
+----------------------------------------------------------+
|                 IMAGE LIFECYCLE                          |
+----------------------------------------------------------+
|                                                          |
|   Build        Tag           Scan         Push           |
|     |           |             |            |             |
|     v           v             v            v             |
|  +------+   +--------+   +--------+   +----------+       |
|  |Docker|-->|Version |-->|Security|-->|Registry  |       |
|  |build |   |+ SHA   |   |Scanner |   |          |       |
|  +------+   +--------+   +--------+   +----------+       |
|                              |                           |
|                              v                           |
|                    +------------------+                  |
|                    | 0 Critical = OK  |                  |
|                    | Annars: Fix forst|                  |
|                    +------------------+                  |
|                                                          |
+----------------------------------------------------------+
```

Tagga images korrekt:

```bash
# Semantisk version + git SHA
docker build -t myapp:1.2.3 -t myapp:abc123f .

# For produktion - aldrig :latest
docker tag myapp:1.2.3 registry.example.com/myapp:1.2.3

# Scanna innan push
docker scout cves myapp:1.2.3
trivy image myapp:1.2.3

# Push endast efter godkand scan
docker push registry.example.com/myapp:1.2.3
```

------------------------------------------------------------

## Praktiska Exempel

Hur du kor containers sakert i produktion:

```
+----------------------------------------------------------+
|            CONTAINER RUNTIME SETTINGS                    |
+----------------------------------------------------------+
|                                                          |
|  RESURSER            SAKERHET           NATVERK          |
|  +------------+      +------------+     +------------+   |
|  |--memory    |      |--read-only |     |--network   |   |
|  |--cpus      |      |--cap-drop  |     |Isolerade   |   |
|  |--pids-limit|      |--security  |     |            |   |
|  +------------+      +------------+     +------------+   |
|        |                   |                  |          |
|        +-------------------+------------------+          |
|                            |                             |
|                            v                             |
|                  +------------------+                    |
|                  | Saker Container  |                    |
|                  +------------------+                    |
|                                                          |
+----------------------------------------------------------+
```

| Kategori | Flagga | Rekommendation |
|----------|--------|----------------|
| Minne | --memory | Satt alltid limit |
| CPU | --cpus | Begransar CPU |
| PIDs | --pids-limit | Forhindra fork bomb |
| Filesystem | --read-only | Skriv bara till tmpfs |
| Capabilities | --cap-drop ALL | Droppa alla, lagg till behov |
| Restart | --restart | unless-stopped eller on-failure |

```bash
# Produktions-ready container
docker run -d \\
    --name api \\
    --memory=512m \\
    --cpus=1 \\
    --pids-limit=100 \\
    --read-only \\
    --tmpfs /tmp \\
    --cap-drop ALL \\
    --cap-add NET_BIND_SERVICE \\
    --restart unless-stopped \\
    --health-cmd "curl -f http://localhost:8000/health" \\
    --health-interval 30s \\
    myapp:1.2.3
```

------------------------------------------------------------

## Steg-för-steg Guide

Sakra natverkskonfigurationer:

```
+----------------------------------------------------------+
|              NETWORK ARCHITECTURE                        |
+----------------------------------------------------------+
|                                                          |
|                    [Internet]                            |
|                         |                                |
|                         v                                |
|  +--------------------------------------------------+   |
|  |                  frontend-net                     |   |
|  |  +----------+                                     |   |
|  |  |  nginx   | (endast denna exponerad)            |   |
|  |  +----------+                                     |   |
|  +----------|---------------------------------------+   |
|             |                                           |
|             v                                           |
|  +--------------------------------------------------+   |
|  |                  backend-net                      |   |
|  |  +----------+    +----------+                     |   |
|  |  |   api    |--->|  cache   |                     |   |
|  |  +----------+    +----------+                     |   |
|  +----------|---------------------------------------+   |
|             |                                           |
|             v                                           |
|  +--------------------------------------------------+   |
|  |                  db-net (internal)                |   |
|  |  +----------+                                     |   |
|  |  |  postgres| (ingen extern access)               |   |
|  |  +----------+                                     |   |
|  +--------------------------------------------------+   |
|                                                          |
+----------------------------------------------------------+
```

| Praxis | Beskrivning |
|--------|-------------|
| Isolerade natverk | Separera frontend/backend/db |
| Internal natverk | --internal for databaser |
| Bind localhost | -p 127.0.0.1:8080:8080 |
| DNS service discovery | Anvand service-namn |
| Encrypted overlay | Kryptering mellan noder |

```yaml
# docker-compose.yml med natverksisolering
networks:
  frontend:
  backend:
  database:
    internal: true  # Ingen extern access

services:
  nginx:
    networks:
      - frontend
      - backend
    ports:
      - "443:443"

  api:
    networks:
      - backend
      - database
    # Ingen port exponerad externt

  postgres:
    networks:
      - database
    # Isolerad, endast api kan na
```

------------------------------------------------------------

## Praktiska Exempel

Hantera data korrekt:

```
+----------------------------------------------------------+
|               STORAGE TYPER                              |
+----------------------------------------------------------+
|                                                          |
|  +----------------+  +----------------+  +-------------+ |
|  | Named Volumes  |  | Bind Mounts    |  | tmpfs       | |
|  +----------------+  +----------------+  +-------------+ |
|  | Produktion     |  | Development    |  | Temp data   | |
|  | Persistent     |  | Hot reload     |  | Sensitiv    | |
|  | Backup-vanlig  |  | Kod-synk       |  | Ej persist  | |
|  +----------------+  +----------------+  +-------------+ |
|                                                          |
|  Anvandning:                                             |
|  - DB data    --> Named Volume                           |
|  - App kod    --> Bind Mount (dev)                       |
|  - Secrets    --> tmpfs eller Docker secrets             |
|  - Temp filer --> tmpfs                                  |
|                                                          |
+----------------------------------------------------------+
```

| Typ | Anvandning | Backup |
|-----|------------|--------|
| Named volume | Databaser, uploads | docker run --volumes-from backup |
| Bind mount | Dev hot-reload | Ej relevant |
| tmpfs | Sessions, temp | Ej mojlig |
| Secrets | Losenord, certs | Extern hantering |

```bash
# Named volume for persistent data
docker volume create postgres_data
docker run -v postgres_data:/var/lib/postgresql/data postgres

# Backup volume
docker run --rm \\
    -v postgres_data:/source:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/postgres_backup.tar.gz -C /source .

# tmpfs for sensitiv temp-data
docker run --tmpfs /tmp:rw,noexec,nosuid,size=100m myapp
```

------------------------------------------------------------

## Teori

```
+----------------------------------------------------------+
|            DOCKER SECURITY LAYERS                        |
+----------------------------------------------------------+
|                                                          |
|  Layer 1: Image                                          |
|  +----------------------------------------------------+  |
|  | - Minimal base (alpine/distroless)                 |  |
|  | - Scanna for CVE (scout/trivy)                     |  |
|  | - Signera images (DCT/cosign)                      |  |
|  | - Inga secrets i image                             |  |
|  +----------------------------------------------------+  |
|                                                          |
|  Layer 2: Build                                          |
|  +----------------------------------------------------+  |
|  | - Multi-stage (inga build-tools i prod)            |  |
|  | - .dockerignore (uteslut .env, .git)               |  |
|  | - Specifika versioner                              |  |
|  +----------------------------------------------------+  |
|                                                          |
|  Layer 3: Runtime                                        |
|  +----------------------------------------------------+  |
|  | - Non-root user                                    |  |
|  | - Read-only filesystem                             |  |
|  | - Drop capabilities                                |  |
|  | - Resource limits                                  |  |
|  | - Seccomp/AppArmor profiles                        |  |
|  +----------------------------------------------------+  |
|                                                          |
|  Layer 4: Network                                        |
|  +----------------------------------------------------+  |
|  | - Isolerade natverk                                |  |
|  | - Internal for databaser                           |  |
|  | - TLS overallt                                     |  |
|  +----------------------------------------------------+  |
|                                                          |
+----------------------------------------------------------+
```

Saker Dockerfile checklista:

```dockerfile
# SAKERT
FROM python:3.11-slim
RUN useradd -r appuser
USER appuser
COPY --chown=appuser:appuser . .

# OSAKERT - undvik dessa
FROM python:latest          # Ospecifik version
USER root                   # Root i produktion
COPY .env /app/             # Secrets i image
RUN apt-get install -y *    # For manga paket
```

------------------------------------------------------------

## Bästa Praxis

Automatisera Docker-workflows:

```
+----------------------------------------------------------+
|              CI/CD PIPELINE                              |
+----------------------------------------------------------+
|                                                          |
|  +--------+    +--------+    +--------+    +--------+    |
|  |  Lint  |--->| Build  |--->|  Test  |--->|  Scan  |    |
|  |Dockerfile   | Image  |    |Container   | CVE    |    |
|  +--------+    +--------+    +--------+    +--------+    |
|                                                |         |
|                                                v         |
|                              +--------+    +--------+    |
|                              | Deploy |<---| Push   |    |
|                              | Prod   |    |Registry|    |
|                              +--------+    +--------+    |
|                                                          |
|  Gates:                                                  |
|  - Dockerfile lint: hadolint                             |
|  - Image size: Max 500MB                                 |
|  - CVE scan: 0 critical, 0 high                          |
|  - Tests: 100% pass                                      |
|                                                          |
+----------------------------------------------------------+
```

```yaml
# GitHub Actions exempel
name: Docker CI/CD

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Lint Dockerfile
      - name: Lint Dockerfile
        uses: hadolint/hadolint-action@v3.1.0

      # Bygg image
      - name: Build
        run: docker build -t myapp:${{ github.sha }} .

      # Testa
      - name: Test
        run: docker run --rm myapp:${{ github.sha }} pytest

      # Scanna
      - name: Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          severity: CRITICAL,HIGH
          exit-code: 1

      # Push (endast main)
      - name: Push
        if: github.ref == 'refs/heads/main'
        run: |
          docker tag myapp:${{ github.sha }} registry/myapp:latest
          docker push registry/myapp:latest
```

------------------------------------------------------------

## Bästa Praxis

```
+----------------------------------------------------------+
|           OBSERVABILITY STACK                            |
+----------------------------------------------------------+
|                                                          |
|  LOGGING                METRICS              TRACING     |
|  +------------+        +------------+       +----------+ |
|  | Container  |        | Prometheus |       | Jaeger   | |
|  | stdout/err |        | /metrics   |       | traces   | |
|  +-----+------+        +-----+------+       +----+-----+ |
|        |                     |                   |       |
|        v                     v                   v       |
|  +------------+        +------------+       +----------+ |
|  | Fluentd/   |        | Grafana    |       | Grafana  | |
|  | Loki       |        | Dashboards |       | Tempo    | |
|  +------------+        +------------+       +----------+ |
|        |                     |                   |       |
|        +---------------------+-------------------+       |
|                              |                           |
|                              v                           |
|                    +------------------+                  |
|                    |   Unified View   |                  |
|                    |   Alerting       |                  |
|                    +------------------+                  |
|                                                          |
+----------------------------------------------------------+
```

| Omrade | Best Practice |
|--------|---------------|
| Loggar | JSON format till stdout |
| Rotation | max-size + max-file |
| Metrics | /health och /metrics endpoints |
| Alerts | CPU, minne, restart count |
| Dashboards | Container stats i Grafana |

```yaml
# docker-compose.yml med logging
services:
  api:
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
        labels: "service,environment"
    labels:
      - "service=api"
      - "environment=production"
    healthcheck:
      test: curl -f http://localhost:8000/health
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

------------------------------------------------------------

## Vanliga Fallgropar

Innan du gar till produktion, verifiera:

```
+----------------------------------------------------------+
|          PRODUCTION READINESS CHECKLIST                  |
+----------------------------------------------------------+
|                                                          |
|  DOCKERFILE                         STATUS               |
|  [ ] Specifik base image tag        ______               |
|  [ ] Multi-stage build              ______               |
|  [ ] Non-root USER                  ______               |
|  [ ] HEALTHCHECK definierad         ______               |
|  [ ] .dockerignore finns            ______               |
|  [ ] Inga secrets i image           ______               |
|                                                          |
|  IMAGE                                                   |
|  [ ] Storlek under 500MB            ______               |
|  [ ] 0 kritiska CVEs                ______               |
|  [ ] Signerad (valfritt)            ______               |
|  [ ] Taggad med version             ______               |
|                                                          |
|  RUNTIME                                                 |
|  [ ] Memory limit satt              ______               |
|  [ ] CPU limit satt                 ______               |
|  [ ] Restart policy                 ______               |
|  [ ] Read-only filesystem           ______               |
|  [ ] Capabilities droppade          ______               |
|                                                          |
|  NATVERK                                                 |
|  [ ] Isolerade natverk              ______               |
|  [ ] Ingen onodiga portar           ______               |
|  [ ] TLS/SSL konfigurerat           ______               |
|                                                          |
|  OBSERVABILITY                                           |
|  [ ] Centraliserad logging          ______               |
|  [ ] Health endpoint                ______               |
|  [ ] Metrics endpoint               ______               |
|  [ ] Alerting konfigurerat          ______               |
|                                                          |
|  BACKUP/DR                                               |
|  [ ] Volume backup strategi         ______               |
|  [ ] Disaster recovery plan         ______               |
|  [ ] Rollback procedur              ______               |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

Du har fatt denna Dockerfile att granska:

```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
ENV DATABASE_PASSWORD=secret123
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "app.py"]
```

Identifiera alla problem och skriv en forbattrad version.

<details>
<summary>Ledtrad</summary>

Leta efter dessa problem:
1. Base image - ar den specifik?
2. Kor den som root?
3. Finns det secrets i imagen?
4. Ar det optimerat for cache?
5. Saknas nagot viktigt (healthcheck)?

</details>

<details>
<summary>Losning</summary>

Problem identifierade:
1. ubuntu:latest - ospecifik tag
2. Kor som root
3. DATABASE_PASSWORD hardkodad
4. Dalig cache-ordning (COPY . fore pip install)
5. Ingen healthcheck
6. Ingen .dockerignore
7. Full ubuntu istallet for slim

Forbattrad Dockerfile:

```dockerfile
FROM python:3.11-slim

LABEL maintainer="team@example.com"

# Skapa non-root user
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Cache-optimerad ordning
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera app-kod
COPY --chown=appuser:appuser . .

# Byt till non-root
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \\
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

# Secrets via environment vid runtime, inte i image
CMD ["python", "app.py"]
```

Kor med: docker run -e DATABASE_PASSWORD=secret myapp

</details>

------------------------------------------------------------


Skriv docker run kommandot for att kora en container med maximalt security hardening for en web-applikation.

Krav:
- Memory limit 512MB
- CPU limit 1 core
- Read-only filesystem (med /tmp skrivbar)
- Alla capabilities droppade utom NET_BIND_SERVICE
- Restart policy
- Healthcheck

<details>
<summary>Ledtrad</summary>

Anvand dessa flaggor:
- --memory for minneslimit
- --cpus for CPU-limit
- --read-only och --tmpfs
- --cap-drop ALL och --cap-add
- --restart
- --health-cmd

</details>

<details>
<summary>Losning</summary>

```bash
docker run -d \\
    --name secure-webapp \\
    --memory=512m \\
    --cpus=1 \\
    --pids-limit=100 \\
    --read-only \\
    --tmpfs /tmp:rw,noexec,nosuid,size=64m \\
    --cap-drop ALL \\
    --cap-add NET_BIND_SERVICE \\
    --security-opt no-new-privileges:true \\
    --restart unless-stopped \\
    --health-cmd "curl -f http://localhost:8000/health || exit 1" \\
    --health-interval=30s \\
    --health-timeout=10s \\
    --health-retries=3 \\
    -p 127.0.0.1:8000:8000 \\
    webapp:1.0.0
```

Forklaring:
- --memory=512m: Max 512MB RAM
- --cpus=1: Max 1 CPU core
- --pids-limit=100: Max 100 processer (fork bomb skydd)
- --read-only: Inga skrivningar till filesystem
- --tmpfs /tmp: Skrivbar /tmp i minnet
- --cap-drop ALL: Ta bort alla Linux capabilities
- --cap-add NET_BIND_SERVICE: Lagg till endast nodvandig
- --security-opt no-new-privileges: Ingen privilege escalation
- --restart unless-stopped: Starta om automatiskt
- --health-*: Inbyggd healthcheck
- -p 127.0.0.1:8000:8000: Bind endast localhost

</details>

------------------------------------------------------------


Skapa en docker-compose.prod.yml for en 3-tier applikation (nginx, api, postgres) med alla best practices.

Krav:
- Isolerade natverk (frontend, backend, database)
- Resource limits
- Healthchecks
- Logging konfiguration
- Secrets for databas-losenord
- Restart policies

<details>
<summary>Ledtrad</summary>

Struktur:
1. Definiera tre natverk (database som internal)
2. Varje service far endast nodvandiga natverk
3. Anvand deploy.resources for limits
4. Secrets definieras separat och refereras

</details>

<details>
<summary>Losning</summary>

```yaml
# docker-compose.prod.yml
version: "3.8"

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
  database:
    driver: bridge
    internal: true  # Ingen extern access

secrets:
  db_password:
    external: true
  db_user:
    external: true

services:
  nginx:
    image: nginx:1.25-alpine
    networks:
      - frontend
      - backend
    ports:
      - "443:443"
      - "80:80"
    deploy:
      resources:
        limits:
          memory: 128M
          cpus: "0.5"
    healthcheck:
      test: ["CMD", "nginx", "-t"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  api:
    image: myapi:1.0.0
    networks:
      - backend
      - database
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "1"
    healthcheck:
      test: curl -f http://localhost:8000/health
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped
    secrets:
      - db_password
      - db_user
    environment:
      - DB_HOST=postgres
      - DB_NAME=app
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "5"

  postgres:
    image: postgres:15-alpine
    networks:
      - database
    volumes:
      - postgres_data:/var/lib/postgresql/data
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: "2"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER"]
      interval: 30s
      timeout: 10s
      retries: 5
    restart: unless-stopped
    secrets:
      - db_password
      - db_user
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER_FILE=/run/secrets/db_user
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

volumes:
  postgres_data:
```

Skapa secrets innan deploy:
```bash
echo "mypassword" | docker secret create db_password -
echo "myuser" | docker secret create db_user -
```

Kor: docker compose -f docker-compose.prod.yml up -d

</details>

------------------------------------------------------------

## Sammanfattning

| Omrade | Viktigaste Best Practices |
|--------|--------------------------|
| Dockerfile | Specifik tag, multi-stage, non-root, healthcheck |
| Images | Slim/alpine, scanna CVE, signera, versionstagg |
| Runtime | Limits, read-only, cap-drop, restart policy |
| Natverk | Isolerade, internal for DB, bind localhost |
| Storage | Named volumes, backup-strategi |
| Security | Alla lager: image, build, runtime, network |
| CI/CD | Lint, build, test, scan, push pipeline |
| Monitoring | JSON logs, rotation, metrics, alerting |

Docker best practices ar inte valfria i produktion - de ar skillnaden mellan
en deployment som fungerar och en som ar saker, skalbar och underhallbar.
Anvand checklistan innan varje produktions-deploy.

------------------------------------------------------------

## Kopplingar

- **Föregående:** [Docker Best Practices Summary](#) - Sammanfattning av bästa praxis
- **Nästa:** [Docker Development Workflow](#) - Utvecklingsflöden med Docker
- **Relaterat:** [Docker Security](#) - Säkerhetspraxis i detalj
- **Relaterat:** [Docker Performance](#) - Prestandaoptimering

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker build --target prod .` | Multi-stage build till specifik stage |
| `docker scan myimage` | Skanna image för sårbarheter |
| `docker history myimage` | Visa image-lager och storlekar |
| `docker system df` | Visa diskutrymme för Docker |
| `docker system prune -a` | Rensa oanvända resurser |
| `docker-compose config` | Validera compose-fil |
| `docker inspect --format '{{.State.Health}}' container` | Kontrollera health status |
| `docker stats --no-stream` | Visa resursanvändning |

------------------------------------------------------------

## Referenser

- [Docker Best Practices Official Guide](https://docs.docker.com/develop/dev-best-practices/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [12-Factor App Methodology](https://12factor.net/)
- [Container Security Best Practices - NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
""",
        },
        {
            "title": "Docker Development Workflow",
            "slug": "docker-development-workflow",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Development Workflow

------------------------------------------------------------

## Introduktion

Docker Development Workflow handlar om att skapa en effektiv och
reproducerbar utvecklingsmiljo med containers. Istallet for att
installera beroenden direkt pa din maskin kor du allt i isolerade
containers som speglar produktionsmiljon.

```
+----------------------------------------------------------+
|                  DEVELOPER WORKSTATION                    |
+----------------------------------------------------------+
|                                                          |
|  +--------------------+  +--------------------+          |
|  |   VS Code / IDE    |  |   Docker Desktop   |          |
|  |                    |  |                    |          |
|  |  - Dev Containers  |  |  - Engine          |          |
|  |  - Debug attach    |  |  - Compose         |          |
|  |  - Extensions      |  |  - Volumes         |          |
|  +--------------------+  +--------------------+          |
|           |                       |                      |
|           v                       v                      |
|  +--------------------------------------------------+   |
|  |              CONTAINER ENVIRONMENT                |   |
|  +--------------------------------------------------+   |
|  |  +----------+  +----------+  +----------+        |   |
|  |  |   App    |  |    DB    |  |  Redis   |        |   |
|  |  | (hot     |  | (seeded) |  | (cache)  |        |   |
|  |  |  reload) |  |          |  |          |        |   |
|  |  +----------+  +----------+  +----------+        |   |
|  +--------------------------------------------------+   |
|                                                          |
+----------------------------------------------------------+
```

Denna nod ger dig verktygen att:
- Satta upp lokal utveckling med hot reload
- Konfigurera Dev Containers i VS Code
- Debugga applikationer i containers
- Hantera database seeding workflows
- Sakerstalla paritet mellan dev och produktion

------------------------------------------------------------

## Teori

Development workflow med Docker bygger pa flera nyckelkoncept:

| Koncept | Beskrivning | Fordel |
|---------|-------------|--------|
| **Hot Reload** | Kod uppdateras utan rebuild | Snabb iteration |
| **Dev Containers** | IDE kor i container | Konsistent miljo |
| **Volume Mounts** | Lokal kod i container | Live-uppdateringar |
| **Override Files** | Miljospecifik config | Flexibilitet |
| **Debug Ports** | Exponera debugger | Full insyn |

```
Development Workflow Stages:
+----------------------------------------------------------+
|                                                          |
|  [1. Clone]  -->  [2. docker compose up]  -->  [3. Dev]  |
|                                                          |
|       |                    |                      |      |
|       v                    v                      v      |
|  +----------+      +---------------+      +----------+   |
|  | Kod      |      | Containers    |      | Edit     |   |
|  | hamtas   |      | startar med   |      | kod,     |   |
|  | fran     |      | hot reload,   |      | se       |   |
|  | repo     |      | debug ports,  |      | andringar|   |
|  |          |      | seed data     |      | direkt   |   |
|  +----------+      +---------------+      +----------+   |
|                                                          |
+----------------------------------------------------------+
```

Override-filhierarki:

```
docker-compose.yml          <-- Bas-konfiguration
        |
        +-- docker-compose.override.yml  <-- Dev (auto-laddas)
        |
        +-- docker-compose.prod.yml      <-- Prod (explicit -f)
        |
        +-- docker-compose.test.yml      <-- Test (explicit -f)
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: Komplett Dev Environment Setup

```yaml
# docker-compose.yml (bas-konfiguration)
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=app
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
```

```yaml
# docker-compose.override.yml (dev - laddas automatiskt)
services:
  api:
    build:
      target: development
    volumes:
      - .:/app:cached                # Hot reload med caching
      - /app/node_modules            # Bevara node_modules
      - /app/.next                   # Bevara Next.js build
    environment:
      - NODE_ENV=development
      - DEBUG=app:*
    ports:
      - "3000:3000"                  # App port
      - "9229:9229"                  # Debug port
    command: npm run dev

  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./scripts/seed.sql:/docker-entrypoint-initdb.d/01-seed.sql
    ports:
      - "5432:5432"                  # Tillgang fran host

  redis:
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

### Exempel 2: Multi-Stage Dockerfile for Dev och Prod

```dockerfile
# Dockerfile med separata stages
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./

# ============================================
# DEVELOPMENT STAGE
# ============================================
FROM base AS development
RUN npm install
# Ingen COPY av kod - anvand volume mount istallet
EXPOSE 3000 9229
CMD ["npm", "run", "dev"]

# ============================================
# BUILD STAGE
# ============================================
FROM base AS builder
RUN npm ci
COPY . .
RUN npm run build

# ============================================
# PRODUCTION STAGE
# ============================================
FROM node:20-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S nodejs && \\
    adduser -S nodejs -u 1001
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
USER nodejs
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Exempel 3: VS Code Dev Container

```json
// .devcontainer/devcontainer.json
{
  "name": "Full Stack Dev",
  "dockerComposeFile": [
    "../docker-compose.yml",
    "docker-compose.devcontainer.yml"
  ],
  "service": "api",
  "workspaceFolder": "/app",
  "customizations": {
    "vscode": {
      "extensions": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "ms-azuretools.vscode-docker",
        "bradlc.vscode-tailwindcss"
      ],
      "settings": {
        "terminal.integrated.defaultProfile.linux": "bash",
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "esbenp.prettier-vscode"
      }
    }
  },
  "forwardPorts": [3000, 5432, 6379],
  "postCreateCommand": "npm install",
  "remoteUser": "node"
}
```

```yaml
# .devcontainer/docker-compose.devcontainer.yml
services:
  api:
    volumes:
      - ..:/app:cached
      - node_modules:/app/node_modules
    command: sleep infinity

volumes:
  node_modules:
```

------------------------------------------------------------

## Debugging i Containers

Att debugga kod som kor i containers kraver ratt konfiguration.

### Node.js Debugging

```yaml
# docker-compose.override.yml
services:
  api:
    command: node --inspect=0.0.0.0:9229 src/index.js
    ports:
      - "9229:9229"
```

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Docker: Attach to Node",
      "type": "node",
      "request": "attach",
      "port": 9229,
      "address": "localhost",
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/app",
      "restart": true,
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

### Python Debugging

```yaml
# docker-compose.override.yml
services:
  api:
    command: python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn main:app --reload
    ports:
      - "5678:5678"
```

```json
// .vscode/launch.json for Python
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Docker: Python Attach",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "/app"
        }
      ]
    }
  ]
}
```

```
Debug Architecture:
+----------------------------------------------------------+
|  VS Code                                                  |
|  +----------------------------------------------------+  |
|  |  Debug Adapter  <---->  Debug Protocol (DAP)       |  |
|  +----------------------------------------------------+  |
|              |                                           |
|              | Port 9229 (Node) / 5678 (Python)         |
|              v                                           |
+----------------------------------------------------------+
|  Docker Container                                        |
|  +----------------------------------------------------+  |
|  |  --inspect=0.0.0.0:9229   OR   debugpy --listen    |  |
|  |                                                    |  |
|  |  Application Process                               |  |
|  |  - Breakpoints                                     |  |
|  |  - Variable inspection                             |  |
|  |  - Step through code                               |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Database Seeding Workflows

Hantera testdata och seed-scripts for utveckling.

### Automatisk Seeding vid Uppstart

```yaml
# docker-compose.override.yml
services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
      # Scripts kors i alfabetisk ordning
      - ./scripts/init/01-schema.sql:/docker-entrypoint-initdb.d/01-schema.sql
      - ./scripts/init/02-seed.sql:/docker-entrypoint-initdb.d/02-seed.sql
      - ./scripts/init/03-test-users.sql:/docker-entrypoint-initdb.d/03-test-users.sql
```

### Seed Script Exempel

```sql
-- scripts/init/02-seed.sql
-- Kors endast om databasen ar ny (tom pgdata volume)

INSERT INTO users (email, name, role) VALUES
  ('admin@test.local', 'Admin User', 'admin'),
  ('dev@test.local', 'Developer', 'user'),
  ('test@test.local', 'Test User', 'user');

INSERT INTO settings (key, value) VALUES
  ('app.theme', 'dark'),
  ('app.language', 'sv');
```

### Reseed utan Rebuild

```bash
# Aterställ databasen helt
docker compose down -v           # Ta bort volumes
docker compose up -d db          # Starta db (kor init scripts)

# Eller kor seed manuellt
docker compose exec db psql -U postgres -d app -f /seed/data.sql

# Anvand make target
make reseed
```

```makefile
# Makefile
.PHONY: reseed db-shell db-dump db-restore

reseed:
	docker compose down -v
	docker compose up -d db
	@echo "Vantar pa databas..."
	sleep 5
	docker compose up -d

db-shell:
	docker compose exec db psql -U postgres -d app

db-dump:
	docker compose exec db pg_dump -U postgres app > backup.sql

db-restore:
	docker compose exec -T db psql -U postgres app < backup.sql
```

------------------------------------------------------------

## Docker Desktop Tips

Docker Desktop ger extra verktyg for utvecklare.

| Funktion | Beskrivning | Anvandning |
|----------|-------------|------------|
| **Extensions** | Tillagg for Docker | UI for databaser, logs |
| **Dev Environments** | Git-baserade miljoer | Team-delning |
| **Resource Limits** | CPU/Memory | Forhindra overbelastning |
| **Kubernetes** | Inbyggt K8s | Lokal K8s-testning |

```
Docker Desktop Features:
+----------------------------------------------------------+
|  Docker Desktop                                           |
|  +----------------------------------------------------+  |
|  |  Dashboard                                          |  |
|  |  +--------+  +--------+  +--------+  +--------+    |  |
|  |  |Contain-|  | Images |  |Volumes |  |Dev Env |    |  |
|  |  |  ers   |  |        |  |        |  |        |    |  |
|  |  +--------+  +--------+  +--------+  +--------+    |  |
|  +----------------------------------------------------+  |
|  |  Extensions                                         |  |
|  |  +------------+  +------------+  +------------+    |  |
|  |  | Logs       |  | Disk Usage |  | Postgres   |    |  |
|  |  | Explorer   |  | Analyzer   |  | Admin      |    |  |
|  |  +------------+  +------------+  +------------+    |  |
|  +----------------------------------------------------+  |
|  |  Settings                                           |  |
|  |  - Resources: CPUs, Memory, Swap, Disk             |  |
|  |  - Kubernetes: Enable/Disable                      |  |
|  |  - Experimental: Features                          |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+
```

Rekommenderade installningar:
- **CPUs**: 4-6 (lamna 2 for host)
- **Memory**: 8-12 GB (beroende pa projekt)
- **Disk**: 60+ GB for images

------------------------------------------------------------

## Bästa Praxis

Samarbeta effektivt med Docker i team.

### Standardiserad Onboarding

```bash
# README.md instruktioner
git clone <repo>
cd project
cp .env.example .env
docker compose up

# Klart - hela miljön körs
```

### Delad Konfiguration

```
project/
+-- .devcontainer/
|   +-- devcontainer.json      # VS Code Dev Container
|   +-- docker-compose.yml     # Dev Container specifik
+-- docker-compose.yml         # Bas (alla delar)
+-- docker-compose.override.yml # Dev (gitignored eller ej)
+-- docker-compose.prod.yml    # Produktion
+-- docker-compose.test.yml    # CI/CD tester
+-- .env.example               # Env template (committad)
+-- .env                       # Lokala variabler (gitignored)
+-- Makefile                   # Standardiserade kommandon
```

### Git Hooks for Konsistens

```bash
# .husky/pre-commit
#!/bin/sh
docker compose exec -T api npm run lint
docker compose exec -T api npm run test:unit
```

```yaml
# docker-compose.test.yml - for CI
services:
  api:
    build:
      target: development
    command: npm run test:ci
    environment:
      - CI=true
      - DATABASE_URL=postgresql://postgres:password@db:5432/app_test

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=app_test
    tmpfs:
      - /var/lib/postgresql/data  # Snabbare, ingen persist
```

------------------------------------------------------------

## Praktiska Exempel

Minimera skillnader mellan dev och prod.

| Aspekt | Development | Production | Hur matcha |
|--------|-------------|------------|------------|
| **Database** | Postgres:16 | Postgres:16 | Samma version |
| **Node** | node:20 | node:20 | Samma image |
| **Env vars** | .env fil | Secrets manager | Samma nycklar |
| **Volumes** | Bind mounts | Named/None | - |
| **Ports** | Exponerade | Internal | - |

```yaml
# Gemensam bas sakerstaller paritet
# docker-compose.yml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      # Samma env-nycklar i alla miljoer
      - DATABASE_URL
      - REDIS_URL
      - API_SECRET

  db:
    image: postgres:16-alpine  # Samma version som prod
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
```

```
Environment Parity:
+----------------------------------------------------------+
|                                                          |
|  Development          Staging            Production      |
|  +-----------+       +-----------+       +-----------+   |
|  | postgres  |       | postgres  |       | postgres  |   |
|  | :16-alpine|  =    | :16-alpine|  =    | :16-alpine|   |
|  +-----------+       +-----------+       +-----------+   |
|  | node:20   |       | node:20   |       | node:20   |   |
|  | -alpine   |  =    | -alpine   |  =    | -alpine   |   |
|  +-----------+       +-----------+       +-----------+   |
|  | redis:7   |       | redis:7   |       | redis:7   |   |
|  | -alpine   |  =    | -alpine   |  =    | -alpine   |   |
|  +-----------+       +-----------+       +-----------+   |
|                                                          |
|  Skillnader:                                             |
|  - Volume mounts       - CI-deployed     - Cloud managed |
|  - Debug ports         - Test data       - Real secrets  |
|  - Hot reload          - Staging secrets - HA/Replicas   |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Övningar

### Ovning 1: Hot Reload Dev Environment

Skapa en komplett utvecklingsmiljo med hot reload for en
Node.js-applikation.

**Krav:**
- Dockerfile med development och production stages
- docker-compose.yml med api och postgres services
- docker-compose.override.yml med hot reload och debug port
- Verifiera att kodandringar syns utan rebuild

<details>
<summary>Ledtrad</summary>

Anvand multi-stage Dockerfile dar development stage inte kopierar
kod utan forvantar sig volume mount. Override-filen ska mounta
aktuell katalog till /app och exponera port 9229 for debugging.
</details>

<details>
<summary>Losning</summary>

```dockerfile
# Dockerfile
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./

FROM base AS development
RUN npm install
EXPOSE 3000 9229
CMD ["npm", "run", "dev"]

FROM base AS production
RUN npm ci --only=production
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

```yaml
# docker-compose.yml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=app
```

```yaml
# docker-compose.override.yml
services:
  api:
    build:
      target: development
    volumes:
      - .:/app:cached
      - /app/node_modules
    ports:
      - "3000:3000"
      - "9229:9229"
    command: npm run dev

  db:
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Verifiera med:
```bash
docker compose up
# Andra en fil och se att servern startar om
```
</details>

### Ovning 2: VS Code Dev Container Setup

Konfigurera VS Code Dev Containers for ett projekt sa att
hela teamet far samma utvecklingsmiljo.

**Krav:**
- .devcontainer/devcontainer.json
- Inkludera relevanta VS Code extensions
- Konfigurera port forwarding
- Lank till docker-compose.yml

<details>
<summary>Ledtrad</summary>

Skapa .devcontainer-mapp med devcontainer.json. Anvand
dockerComposeFile for att referera till befintlig compose-fil.
Lagg till en docker-compose.devcontainer.yml som overridar
command till sleep infinity.
</details>

<details>
<summary>Losning</summary>

```json
// .devcontainer/devcontainer.json
{
  "name": "Project Dev Environment",
  "dockerComposeFile": [
    "../docker-compose.yml",
    "docker-compose.devcontainer.yml"
  ],
  "service": "api",
  "workspaceFolder": "/app",
  "customizations": {
    "vscode": {
      "extensions": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "ms-azuretools.vscode-docker"
      ],
      "settings": {
        "editor.formatOnSave": true
      }
    }
  },
  "forwardPorts": [3000, 5432],
  "postCreateCommand": "npm install"
}
```

```yaml
# .devcontainer/docker-compose.devcontainer.yml
services:
  api:
    volumes:
      - ..:/app:cached
      - node_modules:/app/node_modules
    command: sleep infinity

volumes:
  node_modules:
```

Anvandning:
1. Oppna VS Code
2. Cmd+Shift+P -> "Dev Containers: Reopen in Container"
3. VS Code startar om inuti containern
</details>

### Ovning 3: Database Seeding Pipeline

Skapa ett komplett database seeding workflow med initiala
data, testanvandare och mojlighet att aterställa.

**Krav:**
- SQL seed scripts som kors vid uppstart
- Makefile targets for reseed och db-shell
- Separata filer for schema och testdata

<details>
<summary>Ledtrad</summary>

Mounta SQL-filer till /docker-entrypoint-initdb.d/ i postgres
containern. Filerna kors i alfabetisk ordning endast om
databasen ar ny. For reseed, ta bort volymen och starta om.
</details>

<details>
<summary>Losning</summary>

```sql
-- scripts/init/01-schema.sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sql
-- scripts/init/02-seed.sql
INSERT INTO users (email, name, role) VALUES
    ('admin@example.com', 'Admin', 'admin'),
    ('user1@example.com', 'User One', 'user'),
    ('user2@example.com', 'User Two', 'user');

INSERT INTO posts (user_id, title, content) VALUES
    (1, 'Welcome', 'Welcome to the platform'),
    (2, 'First Post', 'This is my first post');
```

```yaml
# docker-compose.override.yml
services:
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./scripts/init:/docker-entrypoint-initdb.d:ro
    ports:
      - "5432:5432"

volumes:
  pgdata:
```

```makefile
# Makefile
.PHONY: reseed db-shell db-reset

reseed: db-reset
	docker compose up -d db
	@echo "Vantar pa databas..."
	@sleep 3
	docker compose up -d

db-reset:
	docker compose down -v

db-shell:
	docker compose exec db psql -U postgres -d app

db-logs:
	docker compose logs -f db
```

Kommandon:
```bash
make reseed      # Aterställ allt och seed pa nytt
make db-shell    # SQL prompt
```
</details>

------------------------------------------------------------

## Steg-för-steg Guide

### Steg 1: Sätt upp lokal utvecklingsmiljö

1. **Skapa docker-compose.dev.yml**
   ```yaml
   version: '3.8'
   services:
     app:
       build:
         context: .
         target: development
       volumes:
         - .:/app
         - /app/node_modules
       ports:
         - "3000:3000"
       environment:
         - NODE_ENV=development
   ```

2. **Starta utvecklingsservern**
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

### Steg 2: Hot Reload Konfiguration

1. **Konfigurera volume mounts**
   ```yaml
   volumes:
     - ./src:/app/src  # Endast källkod
     - /app/node_modules  # Undvik att överskrida
   ```

2. **Lägg till nodemon för Node.js**
   ```dockerfile
   # Development stage
   FROM node:18 as development
   RUN npm install -g nodemon
   CMD ["nodemon", "src/index.js"]
   ```

### Steg 3: Debugging i Containers

1. **Exponera debug-port**
   ```yaml
   ports:
     - "9229:9229"  # Node.js debug port
   ```

2. **Starta med debug-flagga**
   ```bash
   docker-compose exec app node --inspect=0.0.0.0:9229 src/index.js
   ```

------------------------------------------------------------

## Vanliga Fallgropar

| Problem | Orsak | Lösning |
|---------|-------|---------|
| Hot reload fungerar inte | Volume mount fel | Använd relativa sökvägar: `./src:/app/src` |
| Långsam filsynk på Mac | osxfs begränsningar | Använd `:delegated` eller Mutagen |
| node_modules saknas | Överskrivs av mount | Lägg till tom volume: `/app/node_modules` |
| Permissions-fel | UID/GID mismatch | Sätt `user: "1000:1000"` i compose |
| Debugger ansluter inte | Port ej exponerad | Lägg till `--inspect=0.0.0.0:9229` |
| Tester hittar inte filer | Working directory fel | Sätt `working_dir: /app` |

------------------------------------------------------------

## Kopplingar

- **Föregående:** [Docker Best Practices Summary](#) - Bästa praxis sammanfattning
- **Nästa:** [Docker Ecosystem & Tools](#) - Ekosystem och verktyg
- **Relaterat:** [Docker Compose Advanced](#) - Avancerade compose-mönster
- **Relaterat:** [Docker Debugging](#) - Felsökning i detalj

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker-compose up --build` | Bygg och starta |
| `docker-compose exec app bash` | Shell i körande container |
| `docker-compose logs -f app` | Följ loggar |
| `docker-compose down -v` | Stoppa och ta bort volumes |
| `docker-compose restart app` | Starta om service |
| `docker volume ls` | Lista volumes |
| `docker-compose config` | Validera compose-fil |
| `docker-compose ps` | Visa körande services |

------------------------------------------------------------

## Referenser

- [Docker Compose Development Guide](https://docs.docker.com/compose/production/)
- [Debugging Node.js in Docker](https://nodejs.org/en/docs/guides/debugging-getting-started/)
- [VS Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)
- [Docker Development Best Practices](https://docs.docker.com/develop/)
- [Mutagen for Fast File Sync](https://mutagen.io/documentation/introduction)

------------------------------------------------------------

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Override Files** | Miljospecifik config utan att andra bas |
| **Volume Mounts** | :cached for prestanda, bevara node_modules |
| **Dev Containers** | VS Code kör i container for konsistens |
| **Debug Ports** | 9229 (Node), 5678 (Python) for attach |
| **Seeding** | /docker-entrypoint-initdb.d/ for automatik |
| **Makefile** | Standardisera kommandon for teamet |
| **Parity** | Samma versioner i dev som prod |

------------------------------------------------------------

## Kopplingar

- **Föregående:** [Docker Best Practices Summary](#) - Sammanfattning av bästa praxis
- **Nästa:** [Docker Development Workflow](#) - Utvecklingsflöden med Docker
- **Relaterat:** [Docker Security](#) - Säkerhetspraxis i detalj
- **Relaterat:** [Docker Performance](#) - Prestandaoptimering

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker build --target prod .` | Multi-stage build till specifik stage |
| `docker scan myimage` | Skanna image för sårbarheter |
| `docker history myimage` | Visa image-lager och storlekar |
| `docker system df` | Visa diskutrymme för Docker |
| `docker system prune -a` | Rensa oanvända resurser |
| `docker-compose config` | Validera compose-fil |
| `docker inspect --format '{{.State.Health}}' container` | Kontrollera health status |
| `docker stats --no-stream` | Visa resursanvändning |

------------------------------------------------------------

## Referenser

- [Docker Best Practices Official Guide](https://docs.docker.com/develop/dev-best-practices/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [12-Factor App Methodology](https://12factor.net/)
- [Container Security Best Practices - NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)

------------------------------------------------------------

## Sammanfattning

Docker Development Workflow ger dig:

| Omrade | Teknik | Resultat |
|--------|--------|----------|
| Hot Reload | Volume mounts + nodemon | Snabb iteration |
| Debugging | Port 9229 + VS Code attach | Full insyn |
| Dev Containers | .devcontainer + compose | Team-konsistens |
| Database | Init scripts + Makefile | Enkel seeding |
| Parity | Samma images/versioner | Farre prod-buggar |

```
Development Workflow Summary:
+----------------------------------------------------------+
|                                                          |
|  1. docker compose up                                    |
|     - Startar alla services                              |
|     - Hot reload aktivt                                  |
|     - Debug ports oppna                                  |
|                                                          |
|  2. Utveckla i VS Code                                   |
|     - Kod andras, app uppdateras                         |
|     - Breakpoints fungerar                               |
|     - Extensions tillgangliga                            |
|                                                          |
|  3. make reseed (vid behov)                              |
|     - Aterställ databas                                  |
|     - Kör seed scripts                                   |
|                                                          |
|  4. docker compose down                                  |
|     - Stanga miljön                                      |
|     - -v for att rensa data                              |
|                                                          |
+----------------------------------------------------------+
```

Med dessa verktyg och workflows far du en produktiv utvecklingsmiljo
som ar isolerad, reproducerbar och nara identisk med produktion.
Hela teamet kan komma igang snabbt med ett enda kommando.
""",
        },
        {
            "title": "Docker Ecosystem & Tools",
            "slug": "docker-ecosystem-tools",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 90,
            "content": """# Docker Ecosystem och Verktyg

## Introduktion

Docker ar inte bara ett enskilt verktyg utan en del av ett storre
ekosystem med alternativa runtimes, build-verktyg, sakerhetsscanners
och orkestreringsplattformar. For att bli en komplett DevOps-ingenjor
behover du forsta hela landskapet.

**Vad du lär dig:**
- Skillnaden mellan Docker Desktop och Docker Engine
- Podman som daemonless alternativ
- Container runtimes under huven
- Build-verktyg for CI/CD
- UI-verktyg for hantering
- Sakerhetsscanners for pipeline
- Orchestration och service mesh

```
+------------------------------------------------------------+
|              CONTAINER EKOSYSTEM OVERSIKT                   |
+------------------------------------------------------------+
|                                                            |
|   UTVECKLING        RUNTIME           PRODUKTION           |
|   +------------+    +------------+    +----------------+   |
|   | Docker     |    | containerd |    | Kubernetes     |   |
|   | Desktop    |--->| CRI-O      |--->| Docker Swarm   |   |
|   | Podman     |    | runc       |    | Nomad          |   |
|   +------------+    +------------+    +----------------+   |
|         |                |                   |             |
|         v                v                   v             |
|   BUILD-VERKTYG    REGISTRIES         SERVICE MESH         |
|   +------------+    +------------+    +----------------+   |
|   | BuildKit   |    | Docker Hub |    | Istio          |   |
|   | Kaniko     |    | Harbor     |    | Linkerd        |   |
|   | Buildah    |    | ECR/GCR    |    | Consul Connect |   |
|   +------------+    +------------+    +----------------+   |
|                                                            |
+------------------------------------------------------------+
```

## Teori

Docker finns i tva huvudvarianter med olika anvandningsomraden.

**Docker Desktop - For utvecklare:**

| Komponent           | Beskrivning                              |
|---------------------|------------------------------------------|
| Docker Engine       | Container runtime inbyggd                |
| Docker Compose      | Multi-container utveckling               |
| Docker Scout        | Inbyggd sarbarhetsscanning               |
| Kubernetes          | Single-node K8s for test                 |
| Extensions          | Plugin-ekosystem                         |
| GUI                 | Grafiskt granssnitt                      |

```bash
# Docker Desktop ar ett komplett paket for Mac/Windows
# Inkluderar allt du behover for lokal utveckling

# Kontrollera Desktop-version
docker version

# Desktop-specifika funktioner
docker extension ls              # Lista installerade extensions
docker scout cves nginx:latest   # Inbyggd sarbarhetsscanning
docker sbom nginx:latest         # Software Bill of Materials
```

**Docker Engine - For servrar:**

| Egenskap            | Beskrivning                              |
|---------------------|------------------------------------------|
| Lightweight         | Endast runtime, ingen GUI                |
| Linux-native        | Kors direkt pa Linux                     |
| Produktion          | Standard for servrar                     |
| CLI-only            | Ingen grafisk overhead                   |
| Daemon-baserad      | dockerd bakgrundsprocess                 |

```bash
# Installation pa Ubuntu/Debian server
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Starta Docker Engine
sudo systemctl start docker
sudo systemctl enable docker

# Verifiera installation
docker run hello-world

# Engine-konfiguration
cat /etc/docker/daemon.json
```

```
+------------------------------------------------------------+
|                DOCKER DESKTOP VS ENGINE                     |
+------------------------------------------------------------+
|                                                            |
|   DOCKER DESKTOP                 DOCKER ENGINE             |
|   +------------------------+     +---------------------+   |
|   | GUI Dashboard          |     | CLI only            |   |
|   | Resource limits        |     | Full system access  |   |
|   | Extensions ecosystem   |     | Lightweight         |   |
|   | Integrated K8s         |     | Production-ready    |   |
|   | Mac/Windows/Linux      |     | Linux-native        |   |
|   | License: Business use  |     | License: Free       |   |
|   +------------------------+     +---------------------+   |
|            |                              |                |
|            v                              v                |
|   Utvecklingsmaskiner            Produktionsservrar        |
|                                                            |
+------------------------------------------------------------+
```

## Steg-för-steg Guide

Podman ar ett daemonless och rootless alternativ till Docker
som blir alltmer populart, sarskilt i enterprise-miljoer.

**Podman vs Docker:**

| Egenskap            | Docker                | Podman                 |
|---------------------|-----------------------|------------------------|
| Arkitektur          | Daemon (dockerd)      | Daemonless             |
| Root-krav           | Kraver root default   | Rootless by default    |
| Systemd             | Separat integration   | Native integration     |
| CLI                 | docker                | podman (kompatibel)    |
| Compose             | docker-compose        | podman-compose         |
| Pods                | Nej (utan Swarm)      | Ja, native             |

```bash
# Podman har samma CLI som Docker
# Du kan alias:a docker till podman

alias docker=podman

# Kora en container med Podman
podman run -d --name webserver -p 8080:80 nginx

# Lista containers
podman ps

# Bygga en image
podman build -t myapp:v1 .

# Rootless containers (standard i Podman)
podman run --user 1000:1000 nginx

# Skapa en pod (Kubernetes-liknande koncept)
podman pod create --name mypod -p 8080:80
podman run -d --pod mypod nginx
podman run -d --pod mypod redis
```

**Podman-specifika funktioner:**

```bash
# Generera Kubernetes YAML fran running containers
podman generate kube mypod > mypod.yaml

# Kor Kubernetes YAML med Podman
podman play kube mypod.yaml

# Systemd integration - generera service-fil
podman generate systemd --name webserver > webserver.service

# Flytta till systemd
mv webserver.service ~/.config/systemd/user/
systemctl --user enable webserver
systemctl --user start webserver
```

```
+------------------------------------------------------------+
|                 PODMAN ARKITEKTUR                          |
+------------------------------------------------------------+
|                                                            |
|   DOCKER                          PODMAN                   |
|   +----------------------+        +---------------------+  |
|   |    docker CLI        |        |    podman CLI       |  |
|   +-----------+----------+        +-----------+---------+  |
|               |                               |            |
|               v                               v            |
|   +-----------+----------+        +-----------+---------+  |
|   |     dockerd          |        |  (ingen daemon)     |  |
|   |   (daemon process)   |        |  Direkt till        |  |
|   +-----------+----------+        |  container runtime  |  |
|               |                   +-----------+---------+  |
|               v                               |            |
|   +-----------+----------+                    v            |
|   |    containerd        |        +-----------+---------+  |
|   +-----------+----------+        |    conmon           |  |
|               |                   |  (per container)    |  |
|               v                   +-----------+---------+  |
|   +-----------+----------+                    |            |
|   |      runc            |                    v            |
|   +----------------------+        +-----------+---------+  |
|                                   |      runc           |  |
|                                   +---------------------+  |
|                                                            |
+------------------------------------------------------------+
```

## Praktiska Exempel

Under Docker finns lager av container runtimes som faktiskt
kor dina containers. Forstaelse av dessa ar viktigt for
felskning och avancerad konfiguration.

**Runtime-hierarkin:**

| Niva                | Exempel               | Ansvar                 |
|---------------------|-----------------------|------------------------|
| High-level          | Docker, Podman        | Anvandargranssnitt     |
| Container runtime   | containerd, CRI-O     | Lifecycle management   |
| Low-level runtime   | runc, crun            | Skapar containers      |
| Kernel              | namespaces, cgroups   | Isolering              |

**containerd:**

```bash
# containerd ar den faktiska container runtime under Docker
# Det ar ett CNCF-projekt

# Direkt interaktion med containerd
sudo ctr images pull docker.io/library/nginx:latest
sudo ctr containers create docker.io/library/nginx:latest nginx
sudo ctr tasks start nginx

# Lista containers via containerd
sudo ctr containers ls

# containerd namespaces
sudo ctr namespaces ls
# default     - containerd default
# moby        - Docker containers
# k8s.io      - Kubernetes containers
```

**CRI-O:**

```bash
# CRI-O ar en lightweight runtime specifikt for Kubernetes
# Implementerar Container Runtime Interface (CRI)

# CRI-O ar inte menat for direkt anvandning
# Det anvands av kubelet i Kubernetes

# Kontrollera CRI-O status
sudo systemctl status crio

# CRI-O konfiguration
cat /etc/crio/crio.conf
```

**runc:**

```bash
# runc ar low-level runtime som skapar containers
# Det ar OCI-kompatibelt (Open Container Initiative)

# Se runc-spec for en container
docker inspect --format '{{.State.Pid}}' mycontainer

# runc anvands internt av containerd
# Du interagerar sallan direkt med runc
```

```
+------------------------------------------------------------+
|              CONTAINER RUNTIME STACK                        |
+------------------------------------------------------------+
|                                                            |
|   +------------------------------------------------------+ |
|   |                DOCKER CLI / PODMAN                   | |
|   +------------------------------------------------------+ |
|                            |                               |
|                            v                               |
|   +------------------------------------------------------+ |
|   |           HIGH-LEVEL RUNTIME                         | |
|   |   containerd (Docker)    |    CRI-O (Kubernetes)     | |
|   +------------------------------------------------------+ |
|                            |                               |
|                            v                               |
|   +------------------------------------------------------+ |
|   |             LOW-LEVEL RUNTIME (OCI)                  | |
|   |        runc (standard)   |   crun (snabbare)         | |
|   +------------------------------------------------------+ |
|                            |                               |
|                            v                               |
|   +------------------------------------------------------+ |
|   |              LINUX KERNEL                            | |
|   |   namespaces | cgroups | seccomp | capabilities      | |
|   +------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

## Bästa Praxis

Det finns flera verktyg for att bygga container images,
vart och ett med sina styrkor for olika anvandningsfall.

**BuildKit:**

```bash
# BuildKit ar den moderna build-motorn i Docker
# Snabbare, sakrare och mer funktionsrik an legacy builder

# Aktivera BuildKit explicit
export DOCKER_BUILDKIT=1
docker build -t myapp:v1 .

# Eller i daemon.json
# { "features": { "buildkit": true } }

# BuildKit-specifika funktioner i Dockerfile
# syntax=docker/dockerfile:1

# Cache mounts for snabbare builds
FROM node:18
RUN --mount=type=cache,target=/root/.npm npm install

# Secret mounts (exponerar inte secrets i layers)
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm install

# SSH mounts for private repos
RUN --mount=type=ssh git clone git@github.com:private/repo.git
```

**Buildx (multi-platform builds):**

```bash
# Buildx ar Docker CLI plugin for avancerade builds
# Kraver BuildKit

# Skapa en builder-instans
docker buildx create --name multiplatform --use

# Bygg for flera plattformar samtidigt
docker buildx build \\
  --platform linux/amd64,linux/arm64,linux/arm/v7 \\
  -t myapp:latest \\
  --push .

# Lista builders
docker buildx ls

# Inspektera en builder
docker buildx inspect multiplatform
```

**Kaniko (CI/CD utan Docker daemon):**

```bash
# Kaniko bygger images i Kubernetes utan Docker daemon
# Perfekt for CI/CD pipelines

# Kaniko som Kubernetes Job
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: kaniko-build
spec:
  template:
    spec:
      containers:
      - name: kaniko
        image: gcr.io/kaniko-project/executor:latest
        args:
        - "--dockerfile=Dockerfile"
        - "--context=git://github.com/user/repo.git"
        - "--destination=registry/image:tag"
      restartPolicy: Never
EOF
```

**Buildah (OCI-native):**

```bash
# Buildah bygger OCI-kompatibla images utan daemon
# Integrerar bra med Podman

# Bygg fran Dockerfile
buildah build-using-dockerfile -t myapp:v1 .

# Eller bygg steg-for-steg (skriptbart)
container=$(buildah from alpine)
buildah run $container apk add nginx
buildah config --port 80 $container
buildah commit $container myapp:v1

# Pusha till registry
buildah push myapp:v1 docker://registry.example.com/myapp:v1
```

```
+------------------------------------------------------------+
|              BUILD-VERKTYG JAMFORELSE                       |
+------------------------------------------------------------+
|                                                            |
|   Verktyg    | Daemon | Multi-plat | CI/CD  | Sarskilt    |
|   -----------|--------|------------|--------|-------------|
|   BuildKit   | Ja     | Via Buildx | Delvis | Standard    |
|   Buildx     | Ja     | Ja         | Ja     | Multi-arch  |
|   Kaniko     | Nej    | Ja         | Ja     | Kubernetes  |
|   Buildah    | Nej    | Ja         | Ja     | Skriptbart  |
|                                                            |
|   REKOMMENDATION:                                          |
|   +------------------------------------------------------+ |
|   | Lokal utveckling:  BuildKit (standard i Docker)      | |
|   | Multi-platform:    Buildx                            | |
|   | Kubernetes CI/CD:  Kaniko                            | |
|   | Podman/Rootless:   Buildah                           | |
|   +------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Vanliga Fallgropar

Grafiska verktyg kan gora container-hantering enklare,
sarskilt for team eller vid felskning.

**Portainer:**

```bash
# Portainer ar ett webbaserat management UI
# Stodjer Docker, Swarm och Kubernetes

# Installera Portainer
docker volume create portainer_data

docker run -d \\
  -p 9443:9443 \\
  --name portainer \\
  --restart=always \\
  -v /var/run/docker.sock:/var/run/docker.sock \\
  -v portainer_data:/data \\
  portainer/portainer-ce:latest

# Oppna https://localhost:9443
# Skapa admin-anvandare vid forsta start
```

**Portainer-funktioner:**

| Funktion            | Beskrivning                              |
|---------------------|------------------------------------------|
| Container mgmt      | Start, stop, logs, shell                 |
| Image mgmt          | Pull, build, push                        |
| Network mgmt        | Skapa och hantera natverk                |
| Volume mgmt         | Hantera persistent storage               |
| Stack deploy        | Docker Compose via GUI                   |
| User management     | Rollbaserad atkomst                      |
| Templates           | App templates for snabb deploy           |

**Lazydocker:**

```bash
# Lazydocker ar ett terminal-baserat UI
# Snabbt och lightweight

# Installation
brew install lazydocker     # macOS
# eller
go install github.com/jesseduffield/lazydocker@latest

# Kor Lazydocker
lazydocker

# Tangentbord:
# [ ] - Vaxla mellan paneler
# d   - Ta bort
# s   - Stop/Start
# r   - Restart
# l   - Visa logs
# e   - Exec shell
# b   - Bulk actions
```

```
+------------------------------------------------------------+
|                LAZYDOCKER GRANSSNITT                        |
+------------------------------------------------------------+
|                                                            |
|   Containers          | Logs                               |
|   ----------------    | --------------------------------   |
|   > nginx      Up     | 2024/01/15 nginx started           |
|     redis      Up     | 2024/01/15 ready to accept         |
|     postgres   Up     | connections on port 80             |
|     app        Up     |                                    |
|                       |                                    |
|   -------------------+------------------------------------  |
|   Images             | Stats                               |
|   ----------------   | CPU: 2.3%  MEM: 45.2MB              |
|   nginx:latest       | NET I/O: 1.2kB / 5.6kB              |
|   redis:alpine       | BLOCK I/O: 0B / 4.1kB               |
|   postgres:15        |                                    |
|                                                            |
|   [d]elete [s]top [r]estart [l]ogs [e]xec [b]ulk          |
+------------------------------------------------------------+
```

**Dry (terminal UI):**

```bash
# Dry ar ett annat terminal UI for Docker
# Fokus pa resursovervakning

# Installation
curl -sSf https://moncho.github.io/dry/dryup.sh | sudo sh

# Kor
dry
```

------------------------------------------------------------

## Övningar

Sakerhetsskanning av container images ar kritiskt i moderna
DevOps-pipelines. Flera verktyg finns, bade open source och kommersiella.

**Trivy (Aqua Security):**

```bash
# Trivy ar ett populart open source scanning-verktyg
# Skannar images, filsystem, git repos, Kubernetes

# Installation
brew install trivy          # macOS
apt-get install trivy       # Debian/Ubuntu

# Skanna en image
trivy image nginx:latest

# Skanna med severity-filter
trivy image --severity HIGH,CRITICAL nginx:latest

# Skanna och faila pa HIGH/CRITICAL (for CI/CD)
trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest

# Skanna lokalt filsystem
trivy fs --security-checks vuln,config /path/to/project

# Skanna Kubernetes manifest
trivy config deployment.yaml

# Output som JSON for vidare processing
trivy image --format json -o results.json nginx:latest
```

**Docker Scout (inbyggt i Docker):**

```bash
# Docker Scout ar inbyggt i Docker Desktop
# Och tillgangligt via CLI

# Analysera en image
docker scout cves nginx:latest

# Visa rekommendationer
docker scout recommendations nginx:latest

# Jamfor tva images
docker scout compare nginx:1.24 nginx:1.25

# SBOM (Software Bill of Materials)
docker scout sbom nginx:latest

# Quickview
docker scout quickview nginx:latest
```

**Snyk:**

```bash
# Snyk ar en kommersiell plattform med gratis tier
# Integrerar med CI/CD och IDEs

# Installation
npm install -g snyk

# Autentisera
snyk auth

# Skanna container image
snyk container test nginx:latest

# Skanna med fix-rekommendationer
snyk container test nginx:latest --file=Dockerfile

# Overvaka kontinuerligt
snyk container monitor nginx:latest
```

**Grype (Anchore):**

```bash
# Grype ar open source fran Anchore
# Snabb och noggrann

# Installation
brew install grype

# Skanna image
grype nginx:latest

# Med severity threshold
grype nginx:latest --fail-on high

# Output som JSON
grype nginx:latest -o json > results.json
```

```
+------------------------------------------------------------+
|           SCANNING-VERKTYG JAMFORELSE                       |
+------------------------------------------------------------+
|                                                            |
|   Verktyg  | Typ       | Styrkor        | Anvandning      |
|   ---------|-----------|----------------|-----------------|
|   Trivy    | OSS       | Snabb, bred    | CI/CD standard  |
|   Scout    | Inbyggd   | Enkel, SBOM    | Desktop users   |
|   Snyk     | SaaS      | Fix-forslag    | Enterprise      |
|   Grype    | OSS       | SBOM-fokus     | Anchore stack   |
|                                                            |
|   CI/CD PIPELINE EXEMPEL:                                  |
|   +------------------------------------------------------+ |
|   |  Build --> Trivy scan --> Push (om OK) --> Deploy   | |
|   |                |                                     | |
|   |                v                                     | |
|   |         [CRITICAL?] --> Fail pipeline               | |
|   +------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Kopplingar

For produktion i skala behovs orchestration - automatisk
hantering av containers over flera servrar.

**Kubernetes (K8s):**

| Koncept             | Beskrivning                              |
|---------------------|------------------------------------------|
| Pod                 | Minsta deployable enhet                  |
| Deployment          | Deklarativ pod-hantering                 |
| Service             | Stabil endpoint for pods                 |
| Ingress             | HTTP routing                             |
| ConfigMap/Secret    | Konfiguration och hemligheter            |
| Namespace           | Logisk separation                        |

```bash
# Kubernetes ar industristandard for container orchestration
# Managed: EKS (AWS), GKE (Google), AKS (Azure)

# Grundlaggande deployment
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Skala
kubectl scale deployment nginx --replicas=5

# Deklarativ med YAML
kubectl apply -f deployment.yaml
```

**Docker Swarm:**

```bash
# Docker Swarm ar inbyggt i Docker
# Enklare an K8s men mindre funktionsrikt

# Initiera swarm
docker swarm init

# Skapa en service
docker service create --name web --replicas 3 -p 80:80 nginx

# Skala
docker service scale web=5

# Lista services
docker service ls

# Deploya stack fran compose-fil
docker stack deploy -c docker-compose.yml myapp
```

**HashiCorp Nomad:**

```bash
# Nomad ar ett alternativ fran HashiCorp
# Enklare an K8s, stodjer inte bara containers

# Exempel job-fil (nomad.hcl)
job "webapp" {
  datacenters = ["dc1"]

  group "web" {
    count = 3

    task "nginx" {
      driver = "docker"
      config {
        image = "nginx:latest"
        ports = ["http"]
      }
    }
  }
}

# Kor job
nomad job run webapp.nomad
```

```
+------------------------------------------------------------+
|           ORCHESTRATION JAMFORELSE                          |
+------------------------------------------------------------+
|                                                            |
|   Plattform   | Komplexitet | Skalbarhet | Ekosystem       |
|   ------------|-------------|------------|-----------------|
|   Kubernetes  | Hog         | Mycket hog | Enormt          |
|   Swarm       | Lag         | Medium     | Docker native   |
|   Nomad       | Medium      | Hog        | HashiCorp       |
|   ECS         | Medium      | Hog        | AWS native      |
|                                                            |
|   VAR SKA DU BORJA?                                        |
|   +------------------------------------------------------+ |
|   | Litet team, snabb start:   Docker Swarm             | |
|   | Enterprise, komplex app:   Kubernetes               | |
|   | HashiCorp-stack:           Nomad                    | |
|   | AWS-native:                ECS/Fargate              | |
|   +------------------------------------------------------+ |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Sammanfattning

Service mesh hanterar kommunikation mellan microservices
med funktioner som traffic management, sakerhet och observability.

**Istio:**

| Komponent           | Funktion                                 |
|---------------------|------------------------------------------|
| Envoy proxy         | Sidecar for varje pod                    |
| Pilot               | Service discovery och config             |
| Citadel             | Certifikat och identitet                 |
| Galley              | Konfigurationsvalidering                 |

```bash
# Istio ar den mest feature-rika service mesh
# Men ocksa mest komplex

# Installation
istioctl install --set profile=demo

# Aktivera sidecar injection for namespace
kubectl label namespace default istio-injection=enabled

# Nu far alla pods en Envoy sidecar automatiskt

# Traffic management exempel
kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: webapp
spec:
  hosts:
  - webapp
  http:
  - route:
    - destination:
        host: webapp
        subset: v1
      weight: 90
    - destination:
        host: webapp
        subset: v2
      weight: 10
EOF
```

**Linkerd:**

```bash
# Linkerd ar enklare och lättare an Istio
# Fokus pa enkelhet och prestanda

# Installation
curl -sL run.linkerd.io/install | sh
linkerd install | kubectl apply -f -

# Injektera i deployment
kubectl get deploy -o yaml | linkerd inject - | kubectl apply -f -

# Dashboard
linkerd dashboard
```

**Service Mesh funktioner:**

```
+------------------------------------------------------------+
|              SERVICE MESH KONCEPT                           |
+------------------------------------------------------------+
|                                                            |
|   UTAN SERVICE MESH:                                       |
|   +--------+          +--------+          +--------+       |
|   | App A  |--------->| App B  |--------->| App C  |       |
|   +--------+          +--------+          +--------+       |
|   (direkt kommunikation, ingen insyn)                      |
|                                                            |
|   MED SERVICE MESH:                                        |
|   +--------+   +-------+   +--------+   +-------+          |
|   | App A  |<->| Proxy |<->| App B  |<->| Proxy |          |
|   +--------+   +---+---+   +--------+   +---+---+          |
|                    |                        |              |
|                    v                        v              |
|              +-----+------------------------+----+         |
|              |         Control Plane             |         |
|              |  (traffic mgmt, security, obs)    |         |
|              +-----------------------------------+         |
|                                                            |
|   FUNKTIONER:                                              |
|   - mTLS mellan services (automatisk kryptering)          |
|   - Traffic splitting (canary, blue-green)                |
|   - Circuit breaker (resiliens)                           |
|   - Distributed tracing (felskning)                       |
|   - Service discovery                                     |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Nyckelkommandon

**Ovning 1: Jamfor Docker och Podman**

Du ska utvardera om Podman ar ett lampligt alternativ for ert team.
Utfor samma operationer med bada verktyg och dokumentera skillnader.

Uppgifter:
1. Kor nginx med Docker och Podman
2. Bygg samma image med bada verktyg
3. Generera Kubernetes YAML fran Podman
4. Jamfor resursutnyttjande

<details>
<summary>Ledtrad</summary>

Podman har samma CLI som Docker. Du kan anvanda `podman info`
for att se systemkonfiguration och `podman generate kube`
for att exportera till Kubernetes-format.
</details>

<details>
<summary>Losning</summary>

```bash
# Steg 1: Kor nginx med Docker
docker run -d --name nginx-docker -p 8080:80 nginx

# Kor nginx med Podman
podman run -d --name nginx-podman -p 8081:80 nginx

# Steg 2: Bygg image med Docker
echo "FROM nginx:alpine" > Dockerfile
echo "COPY index.html /usr/share/nginx/html/" >> Dockerfile
echo "<h1>Test</h1>" > index.html

docker build -t myapp:docker .

# Bygg med Podman
podman build -t myapp:podman .

# Steg 3: Generera Kubernetes YAML
podman generate kube nginx-podman > nginx-pod.yaml
cat nginx-pod.yaml

# Steg 4: Jamfor resurser
docker stats nginx-docker --no-stream
podman stats nginx-podman --no-stream

# Skillnader att notera:
# - Podman kraver ingen daemon
# - Podman kan kora rootless utan extra konfiguration
# - Podman har inbyggd pod-support
```
</details>

---

**Ovning 2: Implementera sarbarhetsscanning i CI/CD**

Du ska lagga till sarbarhetsscanning i en CI/CD-pipeline.
Scannern ska faila pipeline om CRITICAL-sarbarheter hittas.

Krav:
- Anvand Trivy
- Skanna under build-fas
- Faila pa CRITICAL
- Generera rapport

<details>
<summary>Ledtrad</summary>

Trivy har flaggan `--exit-code` for att returnera specifik
exit-kod vid fynd, och `--severity` for att filtrera.
Output kan styras med `--format` flaggan.
</details>

<details>
<summary>Losning</summary>

```yaml
# .github/workflows/build.yml
name: Build and Scan

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Install Trivy
        run: |
          wget https://github.com/aquasecurity/trivy/releases/download/v0.45.0/trivy_0.45.0_Linux-64bit.tar.gz
          tar zxvf trivy_0.45.0_Linux-64bit.tar.gz
          sudo mv trivy /usr/local/bin/

      - name: Scan for CRITICAL vulnerabilities
        run: |
          trivy image \\
            --exit-code 1 \\
            --severity CRITICAL \\
            --format table \\
            myapp:${{ github.sha }}

      - name: Generate full report
        if: always()
        run: |
          trivy image \\
            --format json \\
            --output trivy-report.json \\
            myapp:${{ github.sha }}

      - name: Upload report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: trivy-report
          path: trivy-report.json

# Lokal testning:
# docker build -t myapp:test .
# trivy image --exit-code 1 --severity CRITICAL myapp:test
```
</details>

---

**Ovning 3: Satt upp Portainer for team**

Du ska deploya Portainer for att ge ditt team ett grafiskt
granssnitt for container-hantering.

Krav:
- Persistent data
- HTTPS aktiverat
- Automatisk restart
- Edge Agent for remote hosts (valfritt)

<details>
<summary>Ledtrad</summary>

Portainer kraver en volume for persistent data och tillgang
till Docker socket. Port 9443 ar for HTTPS.
Edge Agent kan konfigureras via Portainer UI efter installation.
</details>

<details>
<summary>Losning</summary>

```bash
# Steg 1: Skapa volume for persistent data
docker volume create portainer_data

# Steg 2: Deploya Portainer CE
docker run -d \\
  --name portainer \\
  --restart=always \\
  -p 9443:9443 \\
  -p 8000:8000 \\
  -v /var/run/docker.sock:/var/run/docker.sock \\
  -v portainer_data:/data \\
  portainer/portainer-ce:latest

# Port 9443: HTTPS Web UI
# Port 8000: Edge Agent (for remote hosts)

# Steg 3: Forsta setup
# 1. Oppna https://localhost:9443
# 2. Skapa admin-anvandare
# 3. Valj "Docker" som environment type
# 4. Connect till local Docker socket

# Steg 4: Edge Agent (valfritt, for remote hosts)
# I Portainer UI:
# 1. Settings -> Environments -> Add environment
# 2. Valj "Edge Agent"
# 3. Kopiera install-kommandot
# 4. Kor pa remote host:

docker run -d \\
  --name portainer_edge_agent \\
  --restart=always \\
  -v /var/run/docker.sock:/var/run/docker.sock \\
  -v /var/lib/docker/volumes:/var/lib/docker/volumes \\
  -e EDGE=1 \\
  -e EDGE_ID=<edge-id> \\
  -e EDGE_KEY=<edge-key> \\
  -e CAP_HOST_MANAGEMENT=1 \\
  portainer/agent:latest

# Docker Compose alternativ:
cat <<EOF > docker-compose.portainer.yml
version: '3.8'
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: always
    ports:
      - "9443:9443"
      - "8000:8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  portainer_data:
EOF

docker compose -f docker-compose.portainer.yml up -d
```
</details>

------------------------------------------------------------

## Referenser

**Verktygslandskapet:**

| Kategori            | Rekommendation                           |
|---------------------|------------------------------------------|
| Utveckling          | Docker Desktop (Mac/Win), Podman (Linux) |
| CI/CD builds        | BuildKit + Kaniko                        |
| Sakerhet            | Trivy i pipeline, Scout lokalt           |
| UI                  | Portainer (team), Lazydocker (personlig) |
| Orchestration       | Kubernetes for produktion                |
| Service mesh        | Linkerd (start), Istio (advanced)        |

```
+------------------------------------------------------------+
|           EKOSYSTEM BESLUTSFLODE                            |
+------------------------------------------------------------+
|                                                            |
|   Behov: Lokal utveckling?                                 |
|          |                                                 |
|          +-- Mac/Windows --> Docker Desktop                |
|          |                                                 |
|          +-- Linux --------> Podman (rootless)             |
|                              eller Docker Engine           |
|                                                            |
|   Behov: CI/CD builds?                                     |
|          |                                                 |
|          +-- Kubernetes env --> Kaniko                     |
|          |                                                 |
|          +-- Docker env -----> BuildKit + Buildx           |
|                                                            |
|   Behov: Produktion?                                       |
|          |                                                 |
|          +-- Skalbarhet --> Kubernetes                     |
|          |                                                 |
|          +-- Enkelhet ----> Docker Swarm                   |
|                                                            |
|   Behov: Microservices kommunikation?                      |
|          |                                                 |
|          +-- Enkel start --> Linkerd                       |
|          |                                                 |
|          +-- Full kontroll -> Istio                        |
|                                                            |
+------------------------------------------------------------+
```

**Nasta steg i din lärande:**
1. Prova Podman som Docker-alternativ
2. Implementera Trivy i din CI/CD
3. Utforska Kubernetes (sarskilt om du inte redan kan det)
4. Testa Linkerd for service mesh koncept

**Resurser:**
- Podman: podman.io
- Trivy: github.com/aquasecurity/trivy
- Kubernetes: kubernetes.io/docs
- Linkerd: linkerd.io/getting-started
""",
        },
        {
            "title": "Docker Certification Path",
            "slug": "docker-certification-path",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# Docker Certification Path

------------------------------------------------------------

## Introduktion

Docker Certified Associate (DCA) ar en av de mest varde-
fulla certifieringarna for container-specialister. Den
validerar praktiska kunskaper och oppnar dorrar till
avancerade roller inom DevOps och molninfrastruktur.

| Fordel | Beskrivning |
|--------|-------------|
| **Validering** | Bevisar hands-on kompetens for arbetsgivare |
| **Karriar** | Hojer lonepotential med 15-25% i snitt |
| **Kunskap** | Strukturerad inlarning tacker alla omraden |
| **Natverk** | Tillgang till Docker certifierad community |
| **Fortroende** | Okar sjalvfortroende i tekniska diskussioner |

```
+----------------------------------------------------------+
|           VARFOR CERTIFIERING MATTERS                    |
+----------------------------------------------------------+
|                                                          |
|   Fore certifiering:        Efter certifiering:          |
|   +-----------------+       +---------------------+      |
|   | "Jag kan Docker"|  -->  | "Jag ar certifierad"|      |
|   | (pastaende)     |       | (bevisat)           |      |
|   +-----------------+       +---------------------+      |
|                                                          |
|   Arbetsgivare:             Arbetsgivare:                |
|   "Hur mycket kan du?"      "Vi vet vad du kan!"         |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Teori

### Varför Docker Certifiering?

Docker Certified Associate (DCA) är en av de mest eftertraktade certifieringarna inom containerteknologi. Den validerar praktiska färdigheter inom:

| Domän | Viktning | Fokusområden |
|-------|----------|--------------|
| Orchestration | 25% | Swarm, services, stacks |
| Image Creation | 20% | Dockerfile, multi-stage, registries |
| Installation & Config | 15% | Docker Engine, storage, networking |
| Networking | 15% | Bridge, overlay, DNS |
| Security | 15% | Content trust, secrets, namespaces |
| Storage & Volumes | 10% | Volume drivers, bind mounts |

### Certifieringslandskapet

```
+------------------------------------------------------------+
|                CONTAINER CERTIFIERINGAR                     |
+------------------------------------------------------------+
|                                                            |
|  DOCKER                    KUBERNETES                       |
|  +------------------+      +------------------+             |
|  | DCA              |      | CKA              |             |
|  | Docker Certified |      | Certified K8s    |             |
|  | Associate        |      | Administrator    |             |
|  +------------------+      +------------------+             |
|                            +------------------+             |
|                            | CKAD             |             |
|                            | Certified K8s    |             |
|                            | App Developer    |             |
|                            +------------------+             |
|                            +------------------+             |
|                            | CKS              |             |
|                            | Certified K8s    |             |
|                            | Security Spec    |             |
|                            +------------------+             |
|                                                            |
|  CLOUD PROVIDER SPECIFIKA                                  |
|  +------------------+  +------------------+                 |
|  | AWS Containers   |  | Azure AKS        |                 |
|  | Specialty        |  | Specialty        |                 |
|  +------------------+  +------------------+                 |
|                                                            |
+------------------------------------------------------------+
```

------------------------------------------------------------

## Praktiska Exempel

### Exempel 1: DCA Exam Lab Setup

```bash
#!/bin/bash
# dca-lab-setup.sh

# Skapa övningsmiljö med Docker Swarm
docker swarm init

# Skapa overlay nätverk
docker network create --driver overlay --attachable dca-net

# Deploy test stack
cat << 'EOF' > dca-stack.yml
version: '3.8'
services:
  web:
    image: nginx:alpine
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
    networks:
      - dca-net
    ports:
      - "80:80"

  api:
    image: node:18-alpine
    deploy:
      replicas: 2
    networks:
      - dca-net

networks:
  dca-net:
    external: true
EOF

docker stack deploy -c dca-stack.yml dca-lab
```

### Exempel 2: Typiska Examfrågor

```bash
# Fråga: Hur skapar du en service med 3 replicas?
docker service create --name web --replicas 3 nginx

# Fråga: Hur uppdaterar du en service till ny image?
docker service update --image nginx:1.25 web

# Fråga: Hur inspekterar du secrets i en stack?
docker secret ls
docker secret inspect my-secret

# Fråga: Hur konfigurerar du resource limits?
docker service create --limit-cpu 0.5 --limit-memory 512M nginx
```

### Exempel 3: Networking Övningar

```bash
# Skapa olika nätverkstyper
docker network create --driver bridge app-bridge
docker network create --driver overlay --scope swarm app-overlay

# Testa DNS resolution
docker run --network app-bridge alpine nslookup web

# Inspektera nätverk
docker network inspect app-overlay --format '{{.IPAM.Config}}'
```

------------------------------------------------------------

## Vanliga Fallgropar

| Område | Vanligt Misstag | Rätt Approach |
|--------|-----------------|---------------|
| Swarm | Glömmer `--attachable` för overlay | Alltid för containers utanför services |
| Secrets | Försöker läsa secret-värde direkt | Secrets exponeras som filer i /run/secrets/ |
| Volumes | Blandar ihop bind mounts och volumes | Volumes: Docker-hanterade. Bind: host-sökvägar |
| Networking | Använder default bridge | Skapa custom networks för DNS |
| Services | Uppdaterar med `docker stop` | Använd `docker service update` |
| DTR | Missar Content Trust setup | `export DOCKER_CONTENT_TRUST=1` |

------------------------------------------------------------

## Övningar

### Övning 1: Swarm Cluster Setup
Skapa ett 3-nod Swarm cluster och deploy en stack med web, api och database services.

<details>
<summary>Ledtråd</summary>

```bash
# Manager node
docker swarm init --advertise-addr <IP>

# Worker nodes
docker swarm join --token <token> <manager-ip>:2377

# Verifiera
docker node ls
```
</details>

### Övning 2: Rolling Update
Konfigurera en service med rolling updates som uppdaterar max 2 containers åt gången med 30 sekunders delay.

<details>
<summary>Lösning</summary>

```bash
docker service create --name web \
  --replicas 6 \
  --update-parallelism 2 \
  --update-delay 30s \
  nginx:1.24

# Uppdatera till ny version
docker service update --image nginx:1.25 web
```
</details>

### Övning 3: Secrets Management
Skapa en service som använder en databas-secret och exponerar den som miljövariabel.

<details>
<summary>Lösning</summary>

```bash
# Skapa secret
echo "supersecret" | docker secret create db_password -

# Skapa service med secret
docker service create --name api \
  --secret source=db_password,target=/run/secrets/db_password \
  myapi:latest
```
</details>

------------------------------------------------------------

## Nyckelkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker swarm init` | Initiera Swarm cluster |
| `docker service create` | Skapa ny service |
| `docker service scale web=5` | Skala service |
| `docker stack deploy -c file.yml` | Deploy stack |
| `docker secret create` | Skapa secret |
| `docker config create` | Skapa config |
| `docker node update --availability drain` | Töm node |
| `docker service rollback` | Återställ service |

------------------------------------------------------------

## Docker Certified Associate (DCA) Oversikt

DCA-tentan bestar av 55 fragor som ska besvaras pa
90 minuter. Fragetyperna inkluderar multiple choice,
multiple select och discrete option multiple choice.

| Doman | Viktning | Nyckelomraden |
|-------|----------|---------------|
| **Orchestration** | 25% | Swarm setup, services, rolling updates, stacks |
| **Image Creation** | 20% | Dockerfile, multi-stage, layers, registries |
| **Installation** | 15% | Engine config, storage drivers, logging |
| **Networking** | 15% | Bridge, overlay, DNS, load balancing |
| **Security** | 15% | Image signing, secrets, RBAC, scanning |
| **Storage** | 10% | Volumes, bind mounts, tmpfs, backup |

```
+----------------------------------------------------------+
|              DCA EXAM STRUCTURE                          |
+----------------------------------------------------------+
|                                                          |
|  Fragor: 55 st          Tid: 90 minuter                  |
|  Godkant: ~65-70%       Kostnad: $195 USD                |
|  Giltighet: 2 ar        Format: Proctored online         |
|                                                          |
+----------------------------------------------------------+
|  DOMANFORDELNING:                                        |
|  +----------------------------------------------------+  |
|  | Orchestration    [#########################] 25%   |  |
|  | Image Creation   [####################] 20%        |  |
|  | Installation     [###############] 15%             |  |
|  | Networking       [###############] 15%             |  |
|  | Security         [###############] 15%             |  |
|  | Storage          [##########] 10%                  |  |
|  +----------------------------------------------------+  |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Steg-för-steg Guide

En strukturerad studieplan hjalper dig maximera din
forberedelsetid och sackerställer att alla omraden tacks.

| Vecka | Fokusomrade | Aktiviteter |
|-------|-------------|-------------|
| 1-2 | Installation & Config | Engine setup, storage drivers, daemon config |
| 3-4 | Images & Registries | Dockerfile best practices, multi-stage builds |
| 5 | Networking | Bridge, overlay, DNS, service discovery |
| 6 | Storage & Volumes | Volume drivers, backup strategier |
| 7 | Orchestration | Swarm cluster, services, stacks, secrets |
| 8 | Security & Review | Image scanning, trust, slutrepetition |

```
+----------------------------------------------------------+
|              8-VECKORS STUDIEPLAN                        |
+----------------------------------------------------------+
|                                                          |
|  Vecka 1-2: Installation & Konfiguration                 |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Engine, drivers, logging          |
|  +-----+-----+                                           |
|       |                                                  |
|       v                                                  |
|  Vecka 3-4: Images & Registries                          |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Dockerfile, multi-stage           |
|  +-----+-----+                                           |
|       |                                                  |
|       v                                                  |
|  Vecka 5: Networking                                     |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Bridge, overlay, DNS              |
|  +-----+-----+                                           |
|       |                                                  |
|       v                                                  |
|  Vecka 6: Storage & Volumes                              |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Volymtyper, backup                |
|  +-----+-----+                                           |
|       |                                                  |
|       v                                                  |
|  Vecka 7: Orchestration (Swarm)                          |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Cluster, services, stacks         |
|  +-----+-----+                                           |
|       |                                                  |
|       v                                                  |
|  Vecka 8: Security & Final Review                        |
|  +-----+-----+                                           |
|  | Lab | Doc |  Fokus: Scanning, trust, repetition       |
|  +-----+-----+                                           |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Referenser

Anvand en kombination av officiell dokumentation,
hands-on labs och practice exams for basta resultat.

| Resurstyp | Rekommendation | Anvandn. |
|-----------|----------------|----------|
| **Officiell dok** | docs.docker.com | Primarreferens |
| **Hands-on lab** | labs.play-with-docker.com | Daglig ovning |
| **Practice exam** | Whizlabs, Udemy practice tests | Varje vecka |
| **Videokurs** | Docker Mastery (Bret Fisher) | Komplement |
| **Bok** | Docker Deep Dive (Nigel Poulton) | Djupdykning |

```bash
# REKOMMENDERADE RESURSER

# 1. Officiell Docker dokumentation (GRATIS)
#    https://docs.docker.com
#    - Laes "Get Started" guide
#    - Studera varje domans sektion

# 2. Play with Docker Labs (GRATIS)
#    https://labs.play-with-docker.com
#    - 4 timmar gratis miljo
#    - Perfekt for Swarm-ovningar

# 3. Docker Certified Associate Study Guide
#    - Officiell studyguide fran Docker
#    - Tacker alla examensdomaner

# 4. Practice Tests
#    - Whizlabs DCA Practice Exams
#    - Udemy DCA Mock Tests
#    - Sikta pa 85%+ innan tentan
```

------------------------------------------------------------

## Hands-on Labs och Ovningar

Praktisk erfarenhet ar det viktigaste for att klara DCA.
Har ar tre ovningar som tacker kritiska examensomraden.

### Ovning 1: Multi-Stage Build och Registry

Skapa en optimerad multi-stage build och pusha till registry.

```bash
# Skapa projektstruktur
mkdir dca-lab && cd dca-lab

# Skapa en Go-applikation
cat > main.go << 'EOF'
package main
import (
    "fmt"
    "net/http"
)
func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "DCA Lab - Multi-Stage Success!")
    })
    http.ListenAndServe(":8080", nil)
}
EOF

# Skapa multi-stage Dockerfile
cat > Dockerfile << 'EOF'
# Stage 1: Build
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY main.go .
RUN go build -o server main.go

# Stage 2: Runtime
FROM alpine:3.18
RUN adduser -D appuser
USER appuser
COPY --from=builder /app/server /server
EXPOSE 8080
CMD ["/server"]
EOF

# UPPGIFT: Bygg imagen och verifiera storleken
# Jamfor med en icke-multi-stage build
```

<details>
<summary>Ledtrad</summary>

For att se skillnaden i storlek, bygg tva versioner:
1. En med multi-stage (anvand Dockerfile ovan)
2. En utan multi-stage (anvand bara golang:1.21-alpine)

Anvand "docker images" for att jamfora storlekarna.
Multi-stage bor vara betydligt mindre (ca 10-15 MB vs 300+ MB).

</details>

<details>
<summary>Losning</summary>

```bash
# Bygg multi-stage version
docker build -t dca-lab:multi-stage .

# Skapa single-stage Dockerfile for jamforelse
cat > Dockerfile.single << 'EOF'
FROM golang:1.21-alpine
WORKDIR /app
COPY main.go .
RUN go build -o server main.go
EXPOSE 8080
CMD ["./server"]
EOF

# Bygg single-stage version
docker build -f Dockerfile.single -t dca-lab:single-stage .

# Jamfor storlekar
docker images | grep dca-lab
# dca-lab   multi-stage   abc123   12MB
# dca-lab   single-stage  def456   320MB

# Kora och testa
docker run -d -p 8080:8080 --name dca-test dca-lab:multi-stage
curl http://localhost:8080
# Output: DCA Lab - Multi-Stage Success!

# Stada upp
docker rm -f dca-test
```

</details>

### Ovning 2: Swarm Cluster med Overlay Network

Satt upp ett Swarm-cluster med overlay network och services.

```bash
# Initialisera Swarm (om inte redan gjort)
docker swarm init

# UPPGIFT:
# 1. Skapa ett overlay network kallat "dca-net"
# 2. Deploya en service med 3 replikor pa detta network
# 3. Verifiera att containrarna kan kommunicera
# 4. Skala servicen till 5 replikor
# 5. Utfor en rolling update till ny version
```

<details>
<summary>Ledtrad</summary>

Anvand foljande kommandon:
- "docker network create --driver overlay" for overlay network
- "docker service create" med --network flaggan
- "docker service scale" for att andra antal replikor
- "docker service update --image" for rolling update

Overlay networks kraver Swarm mode for att fungera.

</details>

<details>
<summary>Losning</summary>

```bash
# 1. Skapa overlay network
docker network create --driver overlay --attachable dca-net

# 2. Deploya service med 3 replikor
docker service create \\
  --name web-app \\
  --replicas 3 \\
  --network dca-net \\
  --publish 80:80 \\
  nginx:1.24

# 3. Verifiera kommunikation
docker service ps web-app
# Alla tasks ska vara "Running"

# Testa internt DNS
docker run --rm --network dca-net alpine \\
  nslookup web-app
# Ska returnera service VIP

# 4. Skala till 5 replikor
docker service scale web-app=5
docker service ps web-app

# 5. Rolling update till ny version
docker service update \\
  --image nginx:1.25 \\
  --update-parallelism 2 \\
  --update-delay 10s \\
  web-app

# Verifiera update
docker service inspect web-app --pretty | grep Image

# Stada upp
docker service rm web-app
docker network rm dca-net
```

</details>

### Ovning 3: Secrets och Config Management

Hantera kanslig data sakerhet med Docker secrets.

```bash
# UPPGIFT:
# 1. Skapa en Docker secret for databaslosenord
# 2. Skapa en Docker config for app-konfiguration
# 3. Deploya en service som anvander bade secret och config
# 4. Verifiera att secreten ar tillganglig i containern
# 5. Rotera secreten utan downtime
```

<details>
<summary>Ledtrad</summary>

Secrets skapas med "docker secret create" och monteras
automatiskt i /run/secrets/ inuti containern.

Configs skapas med "docker config create" och kan
monteras pa valfri sokvag.

For rotation, skapa ny secret och uppdatera servicen.

</details>

<details>
<summary>Losning</summary>

```bash
# 1. Skapa secret for databaslosenord
echo "SuperSecretPassword123" | docker secret create db_password -

# 2. Skapa config for applikation
cat > app.conf << 'EOF'
[database]
host=db.example.com
port=5432
name=myapp
EOF
docker config create app_config app.conf

# 3. Deploya service med secret och config
docker service create \\
  --name secure-app \\
  --secret db_password \\
  --config source=app_config,target=/app/config/app.conf \\
  --replicas 2 \\
  alpine sleep 3600

# 4. Verifiera tillgang i container
docker exec $(docker ps -q -f name=secure-app) \\
  cat /run/secrets/db_password
# Output: SuperSecretPassword123

docker exec $(docker ps -q -f name=secure-app) \\
  cat /app/config/app.conf
# Output: Config-innehallet

# 5. Rotera secret utan downtime
echo "NewSecretPassword456" | docker secret create db_password_v2 -

docker service update \\
  --secret-rm db_password \\
  --secret-add db_password_v2 \\
  secure-app

# Verifiera ny secret
docker exec $(docker ps -q -f name=secure-app) \\
  cat /run/secrets/db_password_v2

# Stada upp
docker service rm secure-app
docker secret rm db_password db_password_v2
docker config rm app_config
```

</details>

------------------------------------------------------------

## Steg-för-steg Guide

Anvand denna checklista for att identifiera omraden
som behover mer fokus innan tentan.

| Doman | Nyckelkoncept | Din niva |
|-------|---------------|----------|
| **Orchestration** | Swarm init, join, services | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Rolling updates, rollback | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Stacks med compose-filer | [ ] Beharskar [ ] Ovar [ ] Ny |
| **Images** | Multi-stage builds | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Layer caching, .dockerignore | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Registry push/pull, tagging | [ ] Beharskar [ ] Ovar [ ] Ny |
| **Networking** | Bridge vs overlay networks | [ ] Beharskar [ ] Ovar [ ] Ny |
| | DNS service discovery | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Port publishing modes | [ ] Beharskar [ ] Ovar [ ] Ny |
| **Security** | Docker Content Trust | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Secrets management | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Image scanning | [ ] Beharskar [ ] Ovar [ ] Ny |
| **Storage** | Volumes vs bind mounts | [ ] Beharskar [ ] Ovar [ ] Ny |
| | Volume drivers | [ ] Beharskar [ ] Ovar [ ] Ny |

```
+----------------------------------------------------------+
|            KUNSKAPSGAP IDENTIFIERING                     |
+----------------------------------------------------------+
|                                                          |
|  Sjalvbedomning per doman:                               |
|                                                          |
|  ORCHESTRATION (25%)                                     |
|  Fragor att testa dig sjalv:                             |
|  - Kan du satta upp Swarm fran scratch?                  |
|  - Forstar du skillnaden pa service och task?            |
|  - Kan du utfora rolling update med rollback?            |
|                                                          |
|  IMAGES (20%)                                            |
|  Fragor att testa dig sjalv:                             |
|  - Kan du optimera Dockerfile for caching?               |
|  - Forstar du multi-stage build strategier?              |
|  - Kan du pusha till privat registry?                    |
|                                                          |
|  NETWORKING (15%)                                        |
|  Fragor att testa dig sjalv:                             |
|  - Nar anvander du overlay vs bridge?                    |
|  - Hur fungerar service discovery?                       |
|  - Vad ar skillnaden pa host och ingress mode?           |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Certifieringens Varde i Karriaren

DCA-certifieringen har konkret varde pa arbetsmarknaden
och oppnar dorrar till mer avancerade positioner.

| Aspekt | Fore DCA | Efter DCA |
|--------|----------|-----------|
| **Lonepotential** | Grundniva | +15-25% okning |
| **Jobbtitlar** | Junior DevOps | Senior DevOps, Container Specialist |
| **Intervjuer** | Maste bevisa kunskap | Redan validerad |
| **Projekt** | Stodroller | Arkitekt/Lead-roller |
| **Kundfortroende** | "Han sager han kan" | "Certifierad expert" |

```
+----------------------------------------------------------+
|            KARRIARVARDE AV DCA                           |
+----------------------------------------------------------+
|                                                          |
|  LONEUTVECKLING:                                         |
|  +-------------------------------------------+           |
|  | Junior DevOps     | $$$        |          |           |
|  | DevOps + DCA      | $$$$$      | +20%     |           |
|  | Senior + DCA      | $$$$$$$    | +35%     |           |
|  | Lead + DCA + CKA  | $$$$$$$$$  | +50%     |           |
|  +-------------------------------------------+           |
|                                                          |
|  JOBBMOJLIGHETER:                                        |
|  - Container Platform Engineer                           |
|  - DevOps Architect                                      |
|  - Site Reliability Engineer (SRE)                       |
|  - Cloud Infrastructure Specialist                       |
|  - Kubernetes Administrator (med CKA)                    |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Bästa Praxis

Strategier for att maximera din prestation pa examensdagen.

| Fas | Tips |
|-----|------|
| **Fore** | Sov gott natten innan, eat breakfast |
| **Under** | Flagga svara fragor, kom tillbaka |
| **Fragor** | Las noggrant, eliminera fel alternativ |
| **Tid** | 90 min / 55 fragor = ~1.6 min per fraga |
| **Efter** | Granska flaggade fragor |

```
+----------------------------------------------------------+
|              TENTADAGEN - STRATEGI                       |
+----------------------------------------------------------+
|                                                          |
|  TIDSLINJE:                                              |
|  +----------------------------------------------------+  |
|  | 0-60 min  | Ga igenom alla fragor, flagga svara   |  |
|  | 60-80 min | Aterga till flaggade fragor           |  |
|  | 80-90 min | Final review, kontrollera svar        |  |
|  +----------------------------------------------------+  |
|                                                          |
|  FRAGESTRATEGI:                                          |
|  1. Las hela fragan noggrant                             |
|  2. Identifiera nyckelord (INTE, ALLTID, BASTA)          |
|  3. Eliminera uppenbort felaktiga alternativ             |
|  4. Valj basta kvarvarande alternativ                    |
|  5. Flagga om osaker, ga vidare                          |
|                                                          |
|  VANLIGA FALLOR:                                         |
|  - Fragor med "NOT" eller "EXCEPT"                       |
|  - Fragor som ber om "BEST" practice                     |
|  - Scenario-baserade fragor med flera ratta svar         |
|  - Fragor om specifika kommandon och flaggor             |
|                                                          |
+----------------------------------------------------------+
```

------------------------------------------------------------

## Kopplingar

DCA ar en utmarkt grund for vidare certifieringar
inom container- och molnekosystemet.

| Certifiering | Fokus | Tid efter DCA |
|--------------|-------|---------------|
| **CKA** | Kubernetes Administration | 2-3 manader |
| **CKAD** | Kubernetes Development | 2-3 manader |
| **CKS** | Kubernetes Security | Efter CKA |
| **AWS DevOps Pro** | AWS + Containers | 3-4 manader |
| **Azure DevOps** | Azure + Containers | 3-4 manader |

```
+----------------------------------------------------------+
|              CERTIFIERINGSVAG EFTER DCA                  |
+----------------------------------------------------------+
|                                                          |
|                    +-------+                             |
|                    |  DCA  |                             |
|                    +---+---+                             |
|                        |                                 |
|           +------------+------------+                    |
|           |                         |                    |
|           v                         v                    |
|      +---------+              +-----------+              |
|      |   CKA   |              | Cloud Cert|              |
|      +---------+              +-----------+              |
|           |                    |         |               |
|           v                    v         v               |
|      +---------+          +-------+ +-------+            |
|      |  CKAD   |          |  AWS  | | Azure |            |
|      +---------+          +-------+ +-------+            |
|           |                                              |
|           v                                              |
|      +---------+                                         |
|      |   CKS   |  <-- Ultimate container security        |
|      +---------+                                         |
|                                                          |
+----------------------------------------------------------+
```

**Rekommenderad vag:**
1. **DCA** - Docker-grunden (du ar har!)
2. **CKA** - Kubernetes ar industristandard
3. **CKAD** - Om du utvecklar for K8s
4. **CKS** - Sakerhet ar alltid efterfragat
5. **Cloud cert** - AWS/Azure/GCP efter behov

------------------------------------------------------------

## Docker Mastery - Modulsammanfattning

Grattis! Du har nu genomfort hela Docker Mastery-modulen.
Har ar en oversikt av allt du har lart dig:

| Node | Amne | Nyckelkunskap |
|------|------|---------------|
| 1 | Introduktion | Containers vs VMs, Docker-arkitektur |
| 2 | Installation | Docker Engine setup pa olika OS |
| 3 | Forsta Container | docker run, exec, logs, rm |
| 4 | Images | Dockerfile, layers, build, push |
| 5 | Multi-stage | Optimerade builds, mindre images |
| 6 | Networking | Bridge, host, overlay, DNS |
| 7 | Volumes | Persistent data, bind mounts |
| 8 | Compose Intro | docker-compose.yml, multi-container |
| 9 | Compose Advanced | Override, profiles, healthchecks |
| 10 | Swarm Intro | Cluster, managers, workers |
| 11 | Swarm Services | Replicated, global, rolling updates |
| 12 | Stacks | Production deployments med compose |
| 13 | Secrets | Kanslig data-hantering |
| 14 | Healthchecks | Container- och servicehalsa |
| 15 | Logging | Log drivers, centraliserad logging |
| 16 | Monitoring | Metrics, Prometheus, Grafana |
| 17 | Security | Image scanning, trust, best practices |
| 18 | CI/CD | Automated builds, GitOps |
| 19 | Avancerat | Buildx, multi-arch, advanced patterns |
| 20 | Certifiering | DCA-forberedelse, karriarvag |

```
+----------------------------------------------------------+
|          DOCKER MASTERY - DIN RESA                       |
+----------------------------------------------------------+
|                                                          |
|  START                                               SLUT|
|    |                                                   | |
|    v                                                   v |
|  +----+  +----+  +----+  +----+  +----+       +----+    |
|  | 1  |->| 2  |->| 3  |->| 4  |->| 5  |->..->| 20 |    |
|  +----+  +----+  +----+  +----+  +----+       +----+    |
|  Intro   Setup   Forsta  Images  Multi-      Cert      |
|                  Run             Stage       Path      |
|                                                          |
|  KUNSKAPSOMRADEN DU BEHARSKAR:                           |
|  +----------------------------------------------------+  |
|  | [x] Container fundamentals                         |  |
|  | [x] Docker CLI och kommandon                       |  |
|  | [x] Image creation och optimering                  |  |
|  | [x] Networking och service discovery               |  |
|  | [x] Data persistens med volumes                    |  |
|  | [x] Multi-container med Compose                    |  |
|  | [x] Orchestration med Swarm                        |  |
|  | [x] Production patterns (secrets, health, logging) |  |
|  | [x] Security best practices                        |  |
|  | [x] CI/CD integration                              |  |
|  | [x] Certifieringsforberedelse                      |  |
|  +----------------------------------------------------+  |
|                                                          |
+----------------------------------------------------------+
```

**Du ar nu redo att:**
- Bygga och deploya containeriserade applikationer
- Designa container-natverksarkitektur
- Hantera persistent data i produktion
- Orkestrera services med Docker Swarm
- Implementera sakerhet och best practices
- Ta Docker Certified Associate-tentan
- Fortsatta till Kubernetes och molncertifieringar

------------------------------------------------------------

## Sammanfattning

| Omrade | Viktigaste insikten |
|--------|---------------------|
| **DCA-tentan** | 55 fragor, 90 min, 6 domaner |
| **Forberedelse** | Hands-on ar viktigare an teori |
| **Studieplan** | 8 veckor strukturerat schema |
| **Resurser** | Play with Docker + practice exams |
| **Karriar** | 15-25% loneokning, nya mojligheter |
| **Nasta steg** | CKA ar naturlig fortsattning |
| **Modulen** | 20 noder = komplett Docker-kunskap |

**Slutord:**
Docker Mastery-modulen har gett dig en solid grund inom
containerteknologi. Fran din forsta "docker run" till
avancerad orchestration och sakerhetspatterns - du har
nu kunskapen som kravs for moderna DevOps-roller.

Ta steget och boka din DCA-tenta. Du ar redo!
""",
        },
    ],
}
