# ULTIMATE NODE TEMPLATE v2.0

> **DevOpsHub Premium Content Standard**
> **Skapad:** 2025-12-10
> **Baserad på:** Docker Fundamentals & Architecture (referensnod)

---

## SYFTE

Denna mall definierar den EXAKTA strukturen för alla utbildningsnoder i DevOpsHub.
Varje nod ska följa detta format för att säkerställa:

- Konsekvent användarupplevelse
- Pedagogisk progression (berättande stil)
- Praktisk tillämpning med övningar
- Mätbart lärande

---

## FORMATKRAV

### Separatorer

Använd denna separator mellan ALLA huvudsektioner:

```
------------------------------------------------------------
```

(60 bindestreck)

### Språk

- **Svenska** med åäö (inga ASCII-ersättningar)
- **"Du"-form** genomgående
- Tekniska termer på engelska där det är standard
- Kodkommentarer på svenska för förklaringar

### Emojis

- **INGA emojis** i rubriker eller brödtext
- Emojis tillåtna endast i modul-metadata (icon-fältet)

### Diagram

- Använd `+`, `-`, `|` för ASCII-diagram
- INTE Unicode box-drawing tecken (━ ┌ ┐ etc.)

### Ton

- Vänlig mentor, inte akademisk föreläsare
- Engagerande och uppmuntrande
- Använd analogier: "Tänk på det som..."
- Förklara VARFÖR, inte bara VAD

---

## STRUKTURKRAV - 11 OBLIGATORISKA SEKTIONER

```
# [Nodtitel]

------------------------------------------------------------

## Introduktion
(3-4 stycken som fångar intresse och förklarar VARFÖR detta är viktigt)

------------------------------------------------------------

## Teori
(Huvudinnehållet med 6-8 undersektioner, berättande stil, ASCII-diagram)

------------------------------------------------------------

## Steg-för-steg Guide
(Numrerade steg med kodblock och utförliga kommentarer)

------------------------------------------------------------

## Praktiska Exempel
(3-4 realistiska DevOps-scenarios)

------------------------------------------------------------

## Bästa Praxis
(Minst 5 konkreta tips med kodexempel)

------------------------------------------------------------

## Vanliga Fallgropar
(Minst 4 problem med symptom, orsak och lösning)

------------------------------------------------------------

## Övningar
(3 övningar med progression: Grundläggande → Tillämpad → Utmanande)
(Varje övning har: Mål, Uppgift, <details>Ledtråd</details>, <details>Lösning</details>)

------------------------------------------------------------

## Kopplingar
(Hur denna nod relaterar till andra noder i modulen)

------------------------------------------------------------

## Sammanfattning
(Bullet points med det viktigaste - fungerar som cheat sheet)

------------------------------------------------------------

## Nyckelkommandon
(Tabell: Kommando | Beskrivning | Exempel)

------------------------------------------------------------

## Referenser
(Officiell dokumentation, böcker, tutorials)
```

---

## DETALJERADE KRAV PER SEKTION

### 1. Introduktion

**Längd:** 3-4 stycken
**Syfte:** Skapa motivation och förklara relevans

**Innehåll:**

- Börja med ett relaterbart scenario ("Föreställ dig att...")
- Förklara VARFÖR ämnet är viktigt för DevOps
- Beskriv vad användaren kommer lära sig
- Skapa nyfikenhet

### 2. Teori

**Längd:** 6-8 undersektioner med ###
**Syfte:** Djupgående förklaring av koncept

**Innehåll:**

- Använd analogier för abstrakta koncept
- ASCII-diagram för arkitektur och flöden
- Tabeller för jämförelser
- Förklara HUR saker fungerar, inte bara VAD

### 3. Steg-för-steg Guide

**Syfte:** Praktisk genomgång från start till mål

**Format för kodblock:**

```bash
# Vad vi gör och varför
kommando --flagga argument
# Förväntad output:
# [visa output]
```

### 4. Praktiska Exempel

**Antal:** 3-4 scenarios
**Syfte:** Visa verklig användning

**Innehåll:**

- Scenario-beskrivning
- Komplett kod med kommentarer
- Förklaring av resultat

### 5. Bästa Praxis

**Antal:** Minst 5 punkter
**Format:**

```markdown
1. **[Praxis-titel]**
   ```bash
   # Bra - förklaring
   kommando

   # Dåligt - förklaring
   annat-kommando
   ```

```

### 6. Vanliga Fallgropar

**Antal:** Minst 4 problem
**Format:**

```markdown
### Problem X: [Beskrivning]

**Symptom:**
```

[Felmeddelande eller beteende]

```

**Orsak:** [Förklaring]

**Lösning:**
```bash
[Kommando för att fixa]
```

```

### 7. Övningar

**Antal:** Exakt 3 övningar
**Progression:**
1. **Grundläggande** (15-20 XP) - Direkt tillämpning
2. **Tillämpad** (20-25 XP) - Kombinera koncept
3. **Utmanande** (25-30 XP) - Problemlösning

**Format för varje övning:**

```markdown
### Övning X: [Titel] (XX XP)

**Mål:** [Vad ska uppnås]

**Scenario:** [Kontext om relevant]

**Din uppgift:**
1. [Steg 1]
2. [Steg 2]
3. [Steg 3]

<details>
<summary>Ledtråd</summary>

[Tips utan att ge bort svaret]

</details>

<details>
<summary>Lösning</summary>

```bash
# Kommenterad lösning
[Kod]
```

</details>

**Verifikation:** [Hur vet användaren att de lyckats]

```

### 8. Kopplingar

**Syfte:** Visa hur noden passar in i helheten

**Format:**
- Tabell med nästa noder och vad de bygger på
- Lista förkunskaper

### 9. Sammanfattning

**Format:** Bullet points
**Antal:** 5-8 punkter
**Krav:** Ska fungera som ett snabbt "cheat sheet"

### 10. Nyckelkommandon

**Format:** Tabell

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `cmd` | Vad det gör | `cmd -flag` |

### 11. Referenser

**Innehåll:**
- Officiell dokumentation (länkar)
- Rekommenderade böcker
- Hands-on tutorials
- Fördjupningsresurser

---

## KVALITETSKRAV

Innan en nod anses komplett, verifiera:

- [ ] Introduktionen fångar intresse och förklarar relevans
- [ ] Alla koncept har analogier eller förklaringar
- [ ] Varje kodblock har kommentarer
- [ ] ASCII-diagram används för arkitektur
- [ ] Exakt 3 övningar med ökande svårighet
- [ ] Övningar har både ledtråd och lösning i `<details>` tags
- [ ] Vanliga misstag har symptom, orsak OCH lösning
- [ ] Sammanfattning fungerar som cheat sheet
- [ ] Nyckelkommandon-tabell är komplett
- [ ] Inga emojis i rubriker eller text
- [ ] Svenska med åäö (inga ersättningar)
- [ ] Separatorer (60 bindestreck) mellan alla sektioner

---

## METADATA-SCHEMA (för Python-fil)

```python
{
    "title": "Nodtitel",
    "slug": "nod-slug",
    "difficulty": "easy|medium|hard",
    "estimated_minutes": 45,
    "xp_reward": 75,
    "content": """# Nodtitel

------------------------------------------------------------

[Innehåll enligt mallen ovan]
"""
}
```

---

# KOMPLETT EXEMPEL: Docker Fundamentals & Architecture

Nedan följer ett fullständigt exempel på hur en nod ska se ut enligt denna mall.

---

# Docker Fundamentals & Architecture

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
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
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
docker run -d \
  --name dev-postgres \
  -e POSTGRES_USER=devuser \
  -e POSTGRES_PASSWORD=devpassword \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15

# Förklaring:
# -e: Sätter miljövariabler för konfiguration
# -v: Skapar en namngiven volym för att spara data mellan omstarter

# Anslut till databasen
docker exec -it dev-postgres psql -U devuser -d myapp
# Nu kan du köra SQL-kommandon!
# \dt  - visa tabeller
# \q   - avsluta
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

**Verifikation:** Du kan besöka <http://localhost:8080> och se nginx välkommen-sida.

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
docker run -d \
  --name demo-db \
  --network demo-network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=demoapp \
  -v demo-pgdata:/var/lib/postgresql/data \
  postgres:15

# 3. Starta nginx
docker run -d \
  --name demo-web \
  --network demo-network \
  -p 8080:80 \
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

---

*Template version 2.0 - DevOpsHub Premium Content Standard*
