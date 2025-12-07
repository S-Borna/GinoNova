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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Docker är viktigt |
|----------|-------------------------|
| **Deployment** | Samma container körs identiskt överallt |
| **Skalning** | Spinn upp nya instanser på sekunder |
| **CI/CD** | Bygg en gång, deploya överallt |
| **Microservices** | Isolera tjänster från varandra |
| **Felsökning** | Reproducera produktionsproblem lokalt |

Som DevOps-ingenjör kommer du använda Docker dagligen. Du måste förstå:

- **Vad containers faktiskt är** så du kan felsöka när saker går fel
- **Hur Docker-arkitekturen fungerar** så du vet var problem kan uppstå
- **Skillnaden mellan containers och VMs** så du kan välja rätt verktyg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad är Docker?

Tänk på Docker som en **standardiserad fraktcontainer** för mjukvara. Precis som fraktcontainrar revolutionerade sjöfarten genom att standardisera hur gods transporteras, revolutionerar Docker hur mjukvara levereras.

```
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER KONCEPTET                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Fraktcontainer             Docker Container               │
│   ─────────────────          ──────────────────────         │
│   • Standardstorlek          • Standardformat               │
│   • Fraktas var som helst    • Körs var som helst           │
│   • Innehåll isolerat        • App isolerad                 │
│   • Staplas effektivt        • Resurseffektiv               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container vs Virtual Machine

```
┌─────────────────────────────────────────────────────────────┐
│              VIRTUAL MACHINE (VM)                           │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │  App A   │ │  App B   │ │  App C   │                    │
│  ├──────────┤ ├──────────┤ ├──────────┤                    │
│  │ Guest OS │ │ Guest OS │ │ Guest OS │  ← Varje VM har    │
│  │ (5-10GB) │ │ (5-10GB) │ │ (5-10GB) │    eget OS!        │
│  └──────────┘ └──────────┘ └──────────┘                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Hypervisor (VMware, KVM)               │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    Host OS                          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    CONTAINERS                               │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                    │
│  │  App A   │ │  App B   │ │  App C   │                    │
│  │ (50 MB)  │ │ (100 MB) │ │ (30 MB)  │  ← Bara appen!     │
│  └──────────┘ └──────────┘ └──────────┘                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           Docker Engine (Container Runtime)         │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Host OS (delad kernel)                 │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Jämförelsetabell

| Egenskap | Virtual Machine | Container |
|----------|----------------|-----------|
| **Storlek** | 5-10 GB+ | 50-500 MB |
| **Starttid** | Minuter | Sekunder |
| **Isolation** | Fullständig (egen kernel) | Process-nivå (delad kernel) |
| **Resursanvändning** | Hög (kör helt OS) | Låg (bara appen) |
| **Portabilitet** | Begränsad | Hög |
| **Användningsfall** | Legacy-appar, olika OS | Microservices, modern dev |

**Containers delar Host OS kernel** - det är därför de är så snabba och lätta!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker-arkitekturen

```
┌─────────────────────────────────────────────────────────────┐
│                      DIN TERMINAL                           │
│                    $ docker run nginx                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER CLIENT                            │
│                    (docker CLI)                             │
│        Tar dina kommandon och skickar till daemon           │
└──────────────────────────┬──────────────────────────────────┘
                           │ REST API (unix socket)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER DAEMON                            │
│                     (dockerd)                               │
├──────────┬──────────┬───────────┬──────────────────────────┤
│  Images  │Containers│ Networks  │ Volumes                  │
└──────────┴──────────┴───────────┴──────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  CONTAINER RUNTIME                          │
│                   (containerd)                              │
│          Hanterar container-livscykel                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                        RUNC                                 │
│               Skapar och kör containers                     │
└─────────────────────────────────────────────────────────────┘
```

### Komponentöversikt

| Komponent | Funktion | Fil/Process |
|-----------|----------|-------------|
| **Docker Client** | CLI som du använder | `docker` |
| **Docker Daemon** | Bakgrundsprocess som gör jobbet | `dockerd` |
| **containerd** | Container runtime | `containerd` |
| **runc** | Skapar containers | `runc` |
| **Docker Registry** | Lagrar images | Docker Hub, ECR, etc. |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundläggande kommandon

### Verifiering och Info

| Kommando | Beskrivning |
|----------|-------------|
| `docker version` | Visa client och server version |
| `docker info` | Detaljerad info om Docker-installation |
| `docker system df` | Diskutrymme som Docker använder |

```bash
# Kolla att Docker är installerat och kör
docker version
# Client: Docker Engine - Community
#  Version:           24.0.7
# Server: Docker Engine - Community
#  Version:           24.0.7

docker info
# Containers: 5
# Images: 23
# Storage Driver: overlay2
```

### Dina första kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker run hello-world` | Kör test-container |
| `docker ps` | Lista körande containers |
| `docker ps -a` | Lista ALLA containers |
| `docker images` | Lista lokala images |

```bash
# Kör din första container
docker run hello-world
# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# Hello from Docker!

# Lista containers
docker ps          # Körande containers
docker ps -a       # Alla (även stoppade)

# Lista images
docker images
# REPOSITORY    TAG       IMAGE ID       SIZE
# hello-world   latest    d2c94e258dcb   13.3kB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad händer när du kör "docker run"?

```bash
docker run nginx
```

```
┌─────────────────────────────────────────────────────────────┐
│                   docker run nginx                          │
└──────────────────────────┬──────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 │                 │
┌─────────────────┐        │        ┌────────▼────────┐
│ 1. FINNS IMAGE  │        │        │ 2. PULL IMAGE   │
│    LOKALT?      │──NEJ──▶│        │  från Docker    │
│                 │        │        │  Hub            │
└────────┬────────┘        │        └────────┬────────┘
         │ JA              │                 │
         ▼                 │                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. SKAPA CONTAINER                                          │
│    • Allokera filsystem (writable layer)                    │
│    • Konfigurera nätverk (bridge network)                   │
│    • Sätt upp namespace isolation                           │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. STARTA CONTAINER                                         │
│    • Kör ENTRYPOINT/CMD                                     │
│    • Container är nu igång!                                 │
└─────────────────────────────────────────────────────────────┘
```

### Steg för steg

| Steg | Vad händer | Docker-komponent |
|------|------------|------------------|
| 1 | Kommando tas emot | Docker Client |
| 2 | Kolla om image finns lokalt | Docker Daemon |
| 3 | Pull image om den saknas | Docker Daemon → Registry |
| 4 | Skapa writable layer | Storage Driver |
| 5 | Konfigurera nätverk | Network Driver |
| 6 | Starta container | containerd → runc |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Viktiga Termer

| Term | Beskrivning |
|------|-------------|
| **Image** | Read-only mall/snapshot - receptet |
| **Container** | Körande instans av en image |
| **Registry** | Lagring för images (Docker Hub) |
| **Dockerfile** | Instruktioner för att bygga image |
| **Layer** | Varje steg i en image |
| **Volume** | Persistent data utanför container |
| **Network** | Kommunikation mellan containers |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `permission denied` | Docker kräver sudo | Lägg till user i docker-grupp |
| `Cannot connect to Docker daemon` | dockerd körs inte | `sudo systemctl start docker` |
| `image not found` | Fel image-namn | Kolla stavning på Docker Hub |
| `port already in use` | Annan process på porten | Byt port eller stoppa processen |

```bash
# Fixa permission denied (logout/login efter)
sudo usermod -aG docker $USER

# Starta Docker daemon
sudo systemctl start docker
sudo systemctl enable docker  # Starta vid boot
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Containers ≠ VMs** | Containers delar host OS kernel - mycket lättare |
| **Client-Server** | Docker Client pratar med Docker Daemon via REST API |
| **Images vs Containers** | Images är templates, containers är körande instanser |
| **docker run** | = pull + create + start i ett kommando |

**Kom ihåg:**
- Docker är **industristandard** för containerisering
- En container innehåller **allt appen behöver** för att köra
- **Samma container** körs identiskt i dev, test och produktion
- Containers startar på **sekunder**, inte minuter
""",
        },
        {
            "title": "Docker Images Deep Dive",
            "slug": "docker-images-deep-dive",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Images Deep Dive

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Images är viktigt |
|----------|-------------------------|
| **Build-tid** | Optimerade images bygger snabbare i CI/CD |
| **Deployment** | Mindre images = snabbare deploys |
| **Säkerhet** | Färre paket = mindre attack-yta |
| **Kostnader** | Mindre images = lägre registry-kostnader |
| **Versionering** | Tags ger spårbarhet och rollback-möjlighet |

Images är grunden för allt i Docker. Du måste förstå:

- **Hur images byggs upp** så du kan optimera storlek och build-tid
- **Layers och caching** så du inte slösar tid på onödiga rebuilds
- **Tagging-strategier** så du kan hantera versioner i produktion

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad är en Docker Image?

Tänk på en image som en **snapshot av ett filsystem** plus metadata om hur containern ska köras. Det är som en mall eller recept - du kan skapa hur många containers som helst från samma image.

```
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER IMAGE                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Image = Filsystem-snapshot + Metadata                     │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │  Filsystem                                          │   │
│   │  • /bin, /usr, /etc (OS-filer)                      │   │
│   │  • /app (din applikation)                           │   │
│   │  • Libraries och dependencies                       │   │
│   └─────────────────────────────────────────────────────┘   │
│   ┌─────────────────────────────────────────────────────┐   │
│   │  Metadata                                           │   │
│   │  • CMD/ENTRYPOINT (vad ska köras)                   │   │
│   │  • ENV (miljövariabler)                             │   │
│   │  • EXPOSE (portar)                                  │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Layers

Varje instruktion i en Dockerfile skapar ett nytt **layer**. Layers stackas ovanpå varandra.

```
┌─────────────────────────────────────────────────────────────┐
│                    IMAGE LAYERS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │  Layer 4: COPY app.py /app/                   [2 KB]│   │
│   │           Ditt app-lager (ändras ofta)              │   │
│   ├─────────────────────────────────────────────────────┤   │
│   │  Layer 3: RUN pip install flask             [50 MB] │   │
│   │           Dependencies (ändras sällan)              │   │
│   ├─────────────────────────────────────────────────────┤   │
│   │  Layer 2: RUN apt-get update && install    [100 MB] │   │
│   │           System packages                           │   │
│   ├─────────────────────────────────────────────────────┤   │
│   │  Layer 1: FROM python:3.11-slim            [150 MB] │   │
│   │           Base image                                │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   Totalt: ~302 MB                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Layer-egenskaper

| Egenskap | Beskrivning |
|----------|-------------|
| **Immutable** | Layers kan inte ändras efter skapande |
| **Shared** | Flera images kan dela samma base layers |
| **Cached** | Oförändrade layers återanvänds vid build |
| **Stacked** | Varje layer bygger på föregående |

**Varje layer är immutable** - ändrar du något skapas ett nytt layer ovanpå.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Arbeta med Images

### Grundläggande kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker pull nginx` | Ladda ner image (latest) |
| `docker pull nginx:1.25` | Ladda ner specifik version |
| `docker images` | Lista lokala images |
| `docker inspect nginx` | Visa metadata som JSON |
| `docker history nginx` | Visa alla layers |
| `docker rmi nginx` | Ta bort image |
| `docker image prune` | Ta bort oanvända images |

```bash
# Ladda ner en image
docker pull nginx                    # Senaste versionen (latest)
docker pull nginx:1.25               # Specifik version
docker pull nginx:1.25-alpine        # Alpine-variant (mindre)

# Lista lokala images
docker images
# REPOSITORY   TAG           IMAGE ID       SIZE
# nginx        latest        a6bd71f48f68   187MB
# nginx        1.25-alpine   2bc7edbc3cf2   42.6MB
# python       3.11-slim     f5cfe5c8b0a1   155MB

# Inspektera en image
docker inspect nginx                 # All metadata som JSON
docker history nginx                 # Visa alla layers

# Ta bort images
docker rmi nginx                     # Ta bort specifik image
docker image prune                   # Ta bort oanvända images
docker image prune -a                # Ta bort ALLA oanvända
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Tagging

```
┌─────────────────────────────────────────────────────────────┐
│                    IMAGE TAG FORMAT                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   docker.io/library/nginx:1.25                              │
│   ────────  ─────── ───── ────                              │
│      │         │      │    │                                │
│      │         │      │    └── Tag (version)                │
│      │         │      └── Repository (image-namn)           │
│      │         └── Namespace (user/org)                     │
│      └── Registry (docker.io är default)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tagging-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker tag nginx:latest nginx:v1.0` | Skapa ny tag |
| `docker tag nginx myregistry.com/nginx:v1.0` | Tag för annat registry |
| `docker push myregistry.com/nginx:v1.0` | Pusha till registry |

```bash
# Tagga en image
docker tag nginx:latest myregistry.com/nginx:v1.0
docker tag nginx:latest nginx:production

# Pusha till registry
docker push myregistry.com/nginx:v1.0
```

### Tagging Best Practices

| Strategi | Exempel | Användning |
|----------|---------|------------|
| **Semantic versioning** | `v1.2.3` | Releases |
| **Git SHA** | `abc123f` | CI/CD builds |
| **Environment** | `production`, `staging` | Miljöer |
| **Date** | `2024-12-07` | Dagliga builds |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Layer Caching

Docker cachar layers för snabbare builds. Om inget ändrats i ett layer, återanvänds cached version.

```
┌─────────────────────────────────────────────────────────────┐
│                    LAYER CACHING                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   DÅLIGT - cache invalideras vid varje kodändring:          │
│   ─────────────────────────────────────────────────         │
│   FROM python:3.11                                          │
│   COPY . /app              ← Ändras ofta                    │
│   RUN pip install ...      ← Måste köras om varje gång!     │
│                                                             │
│   BRA - dependencies cachas separat:                        │
│   ─────────────────────────────────────────────────         │
│   FROM python:3.11                                          │
│   COPY requirements.txt /app/   ← Ändras sällan             │
│   RUN pip install ...           ← CACHAS!                   │
│   COPY . /app                   ← Bara detta körs om        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Caching-regler

| Regel | Förklaring |
|-------|------------|
| **Ordning spelar roll** | Sätt saker som ändras sällan först |
| **COPY invaliderar** | Om filer ändras, invalideras layern |
| **RUN-kommandon** | Samma kommando = cached (om föregående cachat) |
| **--no-cache** | Tvinga ombyggnad utan cache |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image-storlek

Storlek spelar roll för deploy-hastighet och säkerhet.

### Jämförelse av base images

| Image | Storlek | Användning |
|-------|---------|------------|
| `python:3.11` | ~1 GB | Full installation, development |
| `python:3.11-slim` | ~150 MB | Produktion (rekommenderas) |
| `python:3.11-alpine` | ~50 MB | Minimal, kan ha kompatibilitetsproblem |
| `node:20` | ~1 GB | Full installation |
| `node:20-slim` | ~200 MB | Produktion |
| `node:20-alpine` | ~130 MB | Minimal |

```bash
# Jämför storlekar
docker images --format "table {{.Repository}}\\t{{.Tag}}\\t{{.Size}}"

# REPOSITORY   TAG           SIZE
# python       3.11          1.01GB
# python       3.11-slim     155MB
# python       3.11-alpine   51.8MB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `docker pull image:tag` | Ladda ner image |
| `docker images` | Lista images |
| `docker inspect image` | Visa metadata |
| `docker history image` | Visa layers |
| `docker tag src dst` | Skapa tag |
| `docker push image` | Pusha till registry |
| `docker rmi image` | Ta bort image |
| `docker image prune` | Städa oanvända |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `image not found` | Fel namn/tag | Kolla stavning på Docker Hub |
| `no space left on device` | Disk full | `docker image prune -a` |
| `denied: access forbidden` | Ej inloggad | `docker login` |
| `manifest unknown` | Tag finns inte | Kolla tillgängliga tags |

```bash
# Logga in på registry
docker login

# Städa gamla images
docker image prune -a

# Kolla tillgängliga tags
docker search nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Layers** | Images består av read-only layers stackade på varandra |
| **Caching** | Layer caching sparar tid - ordna Dockerfile smart |
| **Tags** | Använd specifika tags i produktion, aldrig `latest` |
| **Storlek** | Slim/Alpine varianter sparar utrymme och ökar säkerhet |

**Kom ihåg:**
- Sätt saker som **ändras sällan först** i Dockerfile
- Använd **slim** eller **alpine** varianter i produktion
- **Tagga alltid** med version, aldrig bara latest
- **Städa regelbundet** med `docker image prune`
""",
        },
        {
            "title": "Container Lifecycle Management",
            "slug": "container-lifecycle-management",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Container Lifecycle Management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Lifecycle Management är viktigt |
|----------|---------------------------------------|
| **Zero-downtime deploys** | Graceful shutdown krävs för rolling updates |
| **Resource management** | Stoppa/ta bort containers som inte behövs |
| **Troubleshooting** | Förstå varför containers crashar |
| **Automation** | Scripts måste hantera container-states |
| **Monitoring** | Övervaka container-hälsa och status |

Containers har en livscykel precis som processer. Du måste förstå:

- **Hur du startar och stoppar** containers korrekt
- **Skillnaden mellan stop och kill** för graceful shutdown
- **Hur du felsöker** containers som beter sig konstigt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container States

```
┌─────────────────────────────────────────────────────────────┐
│                 CONTAINER LIFECYCLE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐                                               │
│   │  IMAGE  │                                               │
│   └────┬────┘                                               │
│        │                                                    │
│        │ docker create                                      │
│        ▼                                                    │
│   ┌─────────┐     docker start      ┌─────────┐            │
│   │ CREATED │ ────────────────────▶ │ RUNNING │            │
│   └─────────┘                       └────┬────┘            │
│        ▲                                 │                  │
│        │                                 │                  │
│        │ docker run                      │                  │
│        │ (create + start)                │                  │
│        │                    ┌────────────┼────────────┐     │
│        │                    │            │            │     │
│        │              docker stop   docker kill   crash     │
│        │              (SIGTERM)     (SIGKILL)               │
│        │                    │            │            │     │
│        │                    ▼            ▼            ▼     │
│        │               ┌─────────────────────────────────┐  │
│        │               │           EXITED                │  │
│        │               │  Exit 0 = OK                    │  │
│        │               │  Exit 1 = Error                 │  │
│        │               │  Exit 137 = SIGKILL/OOM         │  │
│        │               │  Exit 143 = SIGTERM             │  │
│        │               └─────────────────────────────────┘  │
│        │                              │                     │
│        └──────────────────────────────┘                     │
│                    docker start                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### State-översikt

| State | Beskrivning | Hur man kommer dit |
|-------|-------------|-------------------|
| **Created** | Container skapad men ej startad | `docker create` |
| **Running** | Container körs aktivt | `docker start` eller `docker run` |
| **Paused** | Processer frysta | `docker pause` |
| **Exited** | Container har stoppat | `docker stop`, `docker kill`, crash |
| **Dead** | Fel vid borttagning | Sällsynt, rensa manuellt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Starta Containers

### Grundläggande start-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker run nginx` | Kör i förgrunden (blockerar) |
| `docker run -d nginx` | Kör i bakgrunden (detached) |
| `docker run --name web nginx` | Ge containern ett namn |
| `docker run --rm nginx` | Ta bort automatiskt vid stopp |
| `docker run -it ubuntu bash` | Interaktiv terminal |

```bash
# Kör container i förgrunden
docker run nginx                 # Blockerar terminalen, Ctrl+C stoppar

# Kör i bakgrunden (detached)
docker run -d nginx              # Returnerar container ID
# a1b2c3d4e5f6...

# Kör med namn
docker run -d --name webserver nginx

# Kör och ta bort när den stoppar (perfekt för engångsjobb)
docker run --rm nginx

# Kör interaktivt
docker run -it ubuntu bash       # -i = interactive, -t = tty
root@container:/#               # Du är nu inne i containern
```

### Vanliga run-flaggor

| Flagga | Beskrivning | Exempel |
|--------|-------------|---------|
| `-d` | Detached mode (bakgrund) | `docker run -d nginx` |
| `--name` | Ge container namn | `docker run --name web nginx` |
| `--rm` | Ta bort vid stopp | `docker run --rm nginx` |
| `-it` | Interaktiv terminal | `docker run -it ubuntu bash` |
| `-p` | Port mapping | `docker run -p 8080:80 nginx` |
| `-v` | Volume mount | `docker run -v data:/app nginx` |
| `-e` | Miljövariabel | `docker run -e DEBUG=1 nginx` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hantera körande containers

### Övervakningskommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker ps` | Lista körande containers |
| `docker ps -a` | Lista ALLA containers |
| `docker logs web` | Visa loggar |
| `docker logs -f web` | Följ loggar i realtid |
| `docker stats` | CPU, minne, nätverk live |
| `docker top web` | Processer i containern |
| `docker inspect web` | All metadata som JSON |

```bash
# Lista körande containers
docker ps
# CONTAINER ID   IMAGE   COMMAND   STATUS         NAMES
# a1b2c3d4e5f6   nginx   ...       Up 2 minutes   webserver

# Följ loggar
docker logs webserver            # Visa loggar
docker logs -f webserver         # Följ i realtid (som tail -f)
docker logs --tail 100 webserver # Senaste 100 rader
docker logs --since 1h webserver # Senaste timmen

# Kör kommandon i körande container
docker exec webserver ls /etc    # Kör ett kommando
docker exec -it webserver bash   # Öppna shell

# Live-statistik
docker stats
# CONTAINER   CPU %   MEM USAGE    NET I/O
# webserver   0.50%   10MB/256MB   1.5kB/2.1kB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stoppa Containers

### Stop vs Kill

```
┌─────────────────────────────────────────────────────────────┐
│                 STOP vs KILL                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   docker stop                     docker kill               │
│   ───────────                     ───────────               │
│   1. Skickar SIGTERM              1. Skickar SIGKILL        │
│   2. Ger appen tid att städa      2. Dödar direkt           │
│   3. Väntar 10s (default)         3. Ingen cleanup          │
│   4. SIGKILL om ej stoppat        4. Exit code 137          │
│                                                             │
│   ANVÄND FÖR:                     ANVÄND FÖR:               │
│   • Normal shutdown               • Hängda containers       │
│   • Graceful termination          • Debugging               │
│   • Production deploys            • Nödstopp                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Stop-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker stop web` | Graceful stop (SIGTERM + 10s + SIGKILL) |
| `docker stop -t 30 web` | Graceful stop med 30s timeout |
| `docker kill web` | Forcerad stop (SIGKILL direkt) |
| `docker restart web` | Stop + start |
| `docker pause web` | Frys processer |
| `docker unpause web` | Återuppta |

```bash
# Graceful stop (skickar SIGTERM, väntar 10s, sen SIGKILL)
docker stop webserver

# Forcerad stop (SIGKILL direkt)
docker kill webserver

# Stoppa med längre timeout
docker stop -t 30 webserver      # Vänta 30 sekunder

# Starta om
docker restart webserver

# Pausa/återuppta (fryser processer utan att stoppa)
docker pause webserver
docker unpause webserver
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Ta bort Containers

| Kommando | Beskrivning |
|----------|-------------|
| `docker rm web` | Ta bort stoppad container |
| `docker rm -f web` | Forcera borttagning (även körande) |
| `docker container prune` | Ta bort alla stoppade |
| `docker rm -f $(docker ps -aq)` | Ta bort ALLA |

```bash
# Ta bort stoppad container
docker rm webserver

# Forcera borttagning av körande container
docker rm -f webserver

# Ta bort alla stoppade containers
docker container prune
# WARNING! This will remove all stopped containers.
# Are you sure you want to continue? [y/N] y

# Ta bort alla containers (körande och stoppade)
docker rm -f $(docker ps -aq)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Exit Codes

| Exit Code | Betydelse | Vanlig orsak |
|-----------|-----------|--------------|
| **0** | Success | Normal exit, app klar |
| **1** | General error | Applikationsfel |
| **125** | Docker daemon error | Problem med Docker |
| **126** | Command cannot execute | Permission denied |
| **127** | Command not found | Fel CMD/ENTRYPOINT |
| **137** | SIGKILL | `docker kill` eller OOM |
| **143** | SIGTERM | `docker stop` |

```bash
# Kolla exit code
docker inspect webserver --format='{{.State.ExitCode}}'
# 0

# Kolla om OOM (Out Of Memory)
docker inspect webserver --format='{{.State.OOMKilled}}'
# false

# Se hela state
docker inspect webserver --format='{{json .State}}' | jq
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsökning

### Vanliga problem och lösningar

| Problem | Diagnos | Lösning |
|---------|---------|---------|
| Container startar inte | `docker logs container` | Fixa applikationsfel |
| Container crashar direkt | `docker run -it image sh` | Debugga interaktivt |
| Container hänger | `docker stats` | Kolla CPU/minne |
| Exit code 137 | OOM killed | Öka minne med `-m` |
| Exit code 1 | App error | Kolla loggar |

```bash
# Container startar inte? Kolla loggar
docker logs container_name

# Container crashar direkt? Kör interaktivt
docker run -it image_name sh

# Kolla events
docker events                    # Realtids-events
docker events --since 1h         # Senaste timmen

# Debug en körande container
docker exec -it container_name bash
docker exec container_name cat /app/logs/error.log
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `docker run -d image` | Starta i bakgrund |
| `docker ps` | Lista körande |
| `docker ps -a` | Lista alla |
| `docker logs -f name` | Följ loggar |
| `docker exec -it name bash` | Shell i container |
| `docker stop name` | Graceful stop |
| `docker kill name` | Force stop |
| `docker rm name` | Ta bort container |
| `docker container prune` | Städa stoppade |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Stop vs Kill** | Använd `docker stop` för graceful shutdown (SIGTERM) |
| **Kill** | Använd `docker kill` bara när stop inte fungerar |
| **--rm** | Flaggan är perfekt för engångscontainers |
| **Exit codes** | Berättar varför containern stoppade |

**Kom ihåg:**
- Ge containers **namn** med `--name` för enklare hantering
- Använd `docker logs -f` för att **följa loggar** i realtid
- **Exit code 137** betyder ofta Out Of Memory
- `docker exec -it` är din bästa vän vid **debugging**
""",
        },
        {
            "title": "Dockerfile Mastery",
            "slug": "dockerfile-mastery",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Dockerfile Mastery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Dockerfile är viktigt |
|----------|------------------------------|
| **CI/CD Pipelines** | Automatiska builds kräver reproducerbara Dockerfiles |
| **Team-samarbete** | Dockerfile dokumenterar build-processen |
| **Säkerhet** | Optimerade Dockerfiles minskar attack-ytan |
| **Performance** | Smarta Dockerfiles bygger snabbare |
| **Kostnader** | Mindre images = lägre storage/transfer-kostnader |

Dockerfile är receptet för dina images. Du måste kunna:

- **Skriva effektiva Dockerfiles** som bygger snabbt
- **Optimera för storlek och säkerhet**
- **Förstå varje instruktion** så du kan felsöka build-problem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dockerfile Struktur

```
┌─────────────────────────────────────────────────────────────┐
│                    DOCKERFILE                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   # Kommentar                                               │
│   INSTRUKTION argument                                      │
│                                                             │
│   Läses uppifrån och ner                                    │
│   Varje instruktion skapar ett LAYER                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Docker läser Dockerfile uppifrån och ner. Varje instruktion skapar ett nytt layer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dockerfile Instruktioner

### Översikt

| Instruktion | Beskrivning | Skapar layer? |
|-------------|-------------|---------------|
| `FROM` | Base image (måste vara först) | Ja |
| `WORKDIR` | Sätt arbetskatalog | Ja |
| `COPY` | Kopiera filer från host | Ja |
| `ADD` | Kopiera + extrahera/URL | Ja |
| `RUN` | Kör kommando vid build | Ja |
| `ENV` | Sätt miljövariabel | Ja |
| `ARG` | Build-time variabel | Nej |
| `EXPOSE` | Dokumentera port | Nej |
| `USER` | Byt användare | Ja |
| `CMD` | Default startkommando | Nej |
| `ENTRYPOINT` | Fast startkommando | Nej |
| `HEALTHCHECK` | Definiera hälsokontroll | Nej |

### De viktigaste instruktionerna

```dockerfile
# FROM - Välj base image (MÅSTE vara först)
FROM python:3.11-slim

# WORKDIR - Sätt arbetskatalog (skapar om den inte finns)
WORKDIR /app

# COPY - Kopiera filer från host till image
COPY requirements.txt .
COPY src/ ./src/

# RUN - Kör kommandon under build
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl

# ENV - Sätt miljövariabler
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

# EXPOSE - Dokumentera vilken port appen lyssnar på
EXPOSE 8000

# CMD - Default-kommando när container startar
CMD ["python", "app.py"]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## COPY vs ADD

```
┌─────────────────────────────────────────────────────────────┐
│                 COPY vs ADD                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   COPY (REKOMMENDERAS)          ADD (undvik om möjligt)     │
│   ────────────────────          ─────────────────────────   │
│   • Enkel kopiering             • Allt COPY kan              │
│   • Förutsägbart                • Auto-extrahera tar.gz     │
│   • Transparent                 • Ladda ner från URL        │
│                                 • Mer "magi" = svårare att  │
│                                   förstå vad som händer     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Scenario | Använd | Exempel |
|----------|--------|---------|
| Kopiera filer | `COPY` | `COPY app.py /app/` |
| Kopiera directory | `COPY` | `COPY src/ /app/src/` |
| Extrahera tar.gz | `ADD` | `ADD archive.tar.gz /app/` |
| Ladda från URL | `RUN curl` | Förutsägbart över `ADD` |

```dockerfile
# COPY - Enkel kopiering (rekommenderas)
COPY app.py /app/
COPY . /app/

# ADD - Kan mer men undvik om möjligt
ADD archive.tar.gz /app/     # Auto-extraherar
# Undvik: ADD https://...    # Använd RUN curl istället
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## CMD vs ENTRYPOINT

```
┌─────────────────────────────────────────────────────────────┐
│                 CMD vs ENTRYPOINT                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   CMD                           ENTRYPOINT                  │
│   ───                           ──────────                  │
│   • Default kommando            • Fast kommando             │
│   • Kan överskrivas helt        • Körs alltid               │
│   • docker run image X          • CMD blir argument         │
│     → kör X istället            • docker run image X        │
│                                   → kör ENTRYPOINT X        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Exempel

| Dockerfile | `docker run image` | `docker run image test.py` |
|------------|-------------------|---------------------------|
| `CMD ["python", "app.py"]` | `python app.py` | `test.py` (CMD ersatt) |
| `ENTRYPOINT ["python"]` | `python` | `python test.py` |
| `ENTRYPOINT ["python"]` + `CMD ["app.py"]` | `python app.py` | `python test.py` |

```dockerfile
# CMD - Kan överskrivas vid docker run
CMD ["python", "app.py"]
# docker run myimage              → python app.py
# docker run myimage python test.py → python test.py (CMD ignoreras)

# ENTRYPOINT - Körs alltid, CMD blir argument
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myimage              → python app.py
# docker run myimage test.py      → python test.py

# Kombinera för flexibilitet (Django-exempel)
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]
# docker run myimage              → python manage.py runserver
# docker run myimage migrate      → python manage.py migrate
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Optimerad Dockerfile - Best Practices

```dockerfile
# ╔═══════════════════════════════════════════════════════════╗
# ║              OPTIMERAD PRODUCTION DOCKERFILE              ║
# ╚═══════════════════════════════════════════════════════════╝

# 1. Välj minimal base image
FROM python:3.11-slim

# 2. Sätt miljövariabler tidigt (cachas)
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PIP_NO_CACHE_DIR=1

# 3. Skapa non-root user (säkerhet!)
RUN useradd --create-home appuser

# 4. Sätt arbetskatalog
WORKDIR /app

# 5. Kopiera dependencies först (layer caching!)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 6. Kopiera applikationskod (ändras ofta, ska vara sist)
COPY --chown=appuser:appuser . .

# 7. Byt till non-root user
USER appuser

# 8. Dokumentera port
EXPOSE 8000

# 9. Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \\
    CMD curl -f http://localhost:8000/health || exit 1

# 10. Startkommando
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

### Best Practices Checklista

| Practice | Varför |
|----------|--------|
| Minimal base image | Mindre attack-yta, snabbare pulls |
| Non-root user | Säkerhet - begränsa privileges |
| Layer caching | Dependencies före kod |
| .dockerignore | Snabbare builds, mindre images |
| Specifik tag | Reproducerbarhet |
| Healthcheck | Kubernetes/orchestration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-stage Builds

Multi-stage bygger i flera steg och kopierar bara det nödvändiga till final image.

```
┌─────────────────────────────────────────────────────────────┐
│                 MULTI-STAGE BUILD                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Stage 1: BUILD              Stage 2: PRODUCTION           │
│   ──────────────              ───────────────────           │
│   FROM node:18                FROM nginx:alpine             │
│   • Node.js (1GB)             • Bara nginx (40MB)           │
│   • npm, node_modules         • Inga build tools            │
│   • Kompilering               • Bara statiska filer         │
│                                                             │
│   COPY --from=builder                                       │
│   ─────────────────────────────────────▶                    │
│                                                             │
│   Resultat: 1GB → 50MB!                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Resultat: Bara nginx + statiska filer, inte Node.js!
# Image size: ~50MB istället för ~1GB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## .dockerignore

Precis som .gitignore men för Docker builds.

```bash
# .dockerignore - exkludera från COPY/ADD
node_modules
.git
.env
.env.*
*.log
__pycache__
.pytest_cache
.coverage
Dockerfile
docker-compose.yml
.dockerignore
README.md
*.md
.vscode
.idea
```

| Vad | Varför exkludera |
|-----|-----------------|
| `node_modules` | Installeras i container |
| `.git` | Onödig i image |
| `.env` | Säkerhetsrisk |
| `Dockerfile` | Inte del av appen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens - Build-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker build .` | Bygg från Dockerfile |
| `docker build -t name:tag .` | Bygg med tag |
| `docker build -f Dockerfile.prod .` | Specificera fil |
| `docker build --no-cache .` | Bygg utan cache |
| `docker build --target stage .` | Bygg till specifikt stage |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `COPY failed: file not found` | Fil finns inte i context | Kolla sökväg, .dockerignore |
| `RUN command not found` | Fel shell eller program saknas | Installera först med apt/apk |
| `permission denied` | Non-root user | `--chown` eller `chmod` |
| Image blir för stor | För mycket i image | Multi-stage, .dockerignore |
| Build tar lång tid | Dålig layer-ordning | Dependencies före kod |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Layer caching** | Ordning spelar roll - saker som ändras sällan först |
| **Multi-stage** | Minskar image-storlek dramatiskt |
| **Non-root** | Kör alltid som non-root user i produktion |
| **.dockerignore** | Snabbare builds och säkrare images |

**Kom ihåg:**
- **COPY före RUN** när det gäller dependencies
- Använd **slim** eller **alpine** base images
- **Multi-stage** för compiled languages (Go, Rust, Node)
- **.dockerignore** är lika viktigt som .gitignore
""",
        },
        {
            "title": "Docker Networking",
            "slug": "docker-networking",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Networking

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Docker Networking är viktigt |
|----------|-------------------------------------|
| **Microservices** | Tjänster måste kommunicera med varandra |
| **Säkerhet** | Isolera känsliga tjänster (databaser) |
| **Service Discovery** | Hitta tjänster via namn istället för IP |
| **Load Balancing** | Distribuera trafik mellan containers |
| **Multi-host** | Containers på olika servers |

Containers behöver prata med varandra och omvärlden. Du måste förstå:

- **Olika network drivers** och när du använder vilken
- **Hur containers hittar varandra** via DNS
- **Port mapping** för att exponera tjänster

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Network Drivers

```
┌─────────────────────────────────────────────────────────────┐
│                 DOCKER NETWORK DRIVERS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   BRIDGE (default)             HOST                         │
│   ────────────────             ────                         │
│   ┌─────────┐                  Container delar              │
│   │Container│──┐               host's nätverks-             │
│   └─────────┘  │               stack direkt                 │
│   ┌─────────┐  ├─► Bridge ─► Host                           │
│   │Container│──┘                                            │
│   └─────────┘                  NONE                         │
│   Isolerat nätverk             ────                         │
│   på samma host                Ingen nätverks-              │
│                                åtkomst alls                 │
│   OVERLAY                                                   │
│   ───────                      MACVLAN                      │
│   Multi-host nätverk           ───────                      │
│   (Swarm/K8s)                  Direkt på fysiskt            │
│                                nätverk                      │
└─────────────────────────────────────────────────────────────┘
```

### Network Driver-översikt

| Driver | Användning | Isolation |
|--------|------------|-----------|
| **bridge** | Default, containers på samma host | Ja |
| **host** | Performance-kritiskt, ingen port mapping | Nej |
| **none** | Helt isolerad container | Total |
| **overlay** | Multi-host (Docker Swarm) | Ja |
| **macvlan** | Container på fysiskt nätverk | Nej |

```bash
# Bridge (default) - containers på samma host
docker network create mynetwork

# Host - container delar hosts nätverk (ingen isolation)
docker run --network host nginx

# None - ingen nätverksåtkomst
docker run --network none alpine

# Overlay - containers över flera hosts (Swarm/Kubernetes)
docker network create -d overlay myoverlay
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bridge Network

Bridge är default och mest använda. Containers på samma bridge kan prata med varandra.

### Grundläggande kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker network create mynet` | Skapa nätverk |
| `docker network ls` | Lista nätverk |
| `docker network inspect mynet` | Visa detaljer |
| `docker network rm mynet` | Ta bort nätverk |
| `docker network prune` | Ta bort oanvända |

```bash
# Skapa ett nätverk
docker network create backend-net

# Starta containers i nätverket
docker run -d --name db --network backend-net postgres
docker run -d --name api --network backend-net myapi

# Nu kan api nå db via hostname "db"
# Inuti api-containern: ping db → fungerar!

# Lista nätverk
docker network ls
# NETWORK ID     NAME          DRIVER    SCOPE
# a1b2c3d4e5f6   backend-net   bridge    local
# 0e1f2a3b4c5d   bridge        bridge    local

# Inspektera nätverk
docker network inspect backend-net
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container DNS

Docker har inbyggd DNS för containers i samma user-defined nätverk.

```
┌─────────────────────────────────────────────────────────────┐
│                 CONTAINER DNS                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   backend-net (user-defined bridge)                         │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                                                     │   │
│   │  ┌──────────┐         ┌──────────┐                  │   │
│   │  │   api    │ ──────► │ postgres │                  │   │
│   │  │          │  "postgres"         │                  │   │
│   │  └──────────┘         └──────────┘                  │   │
│   │                                                     │   │
│   │  DNS: container-namn resolvas till container IP     │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   "postgres" → 172.18.0.2 (automatiskt!)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Docker har inbyggd DNS för containers i samma nätverk
# Hostname = container name

# Exempel: api behöver nå databas
docker run -d --name postgres --network mynet postgres
docker run -d --name api --network mynet \\
    -e DATABASE_URL=postgresql://postgres:5432/db \\
    myapi

# Inuti api: "postgres" resolvas automatiskt till rätt IP
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Port Mapping

Exponera container-portar till host för extern åtkomst.

```
┌─────────────────────────────────────────────────────────────┐
│                 PORT MAPPING                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   HOST                         CONTAINER                    │
│   ────                         ─────────                    │
│                                                             │
│   localhost:8080  ──────────►  nginx:80                     │
│        │                           │                        │
│        │      -p 8080:80           │                        │
│        │                           │                        │
│   Host port              Container port                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Port Mapping-syntax

| Syntax | Beskrivning |
|--------|-------------|
| `-p 8080:80` | Host 8080 → Container 80 |
| `-p 127.0.0.1:8080:80` | Bara localhost |
| `-p 80` | Random host port → Container 80 |
| `-p 80:80 -p 443:443` | Flera portar |

```bash
# Exponera port till host
docker run -p 8080:80 nginx
#          │    │
#          │    └── Container port (nginx lyssnar på 80)
#          └── Host port (du når via localhost:8080)

# Exponera till specifik IP (säkrare!)
docker run -p 127.0.0.1:8080:80 nginx  # Bara localhost

# Random host port
docker run -p 80 nginx                  # Docker väljer port
docker port container_name              # Se vilken port

# Flera portar
docker run -p 80:80 -p 443:443 nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt exempel: Web App + Databas

```
┌─────────────────────────────────────────────────────────────┐
│                 WEBAPP ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Internet                                                  │
│      │                                                      │
│      │ :8080                                                │
│      ▼                                                      │
│   ┌──────────────────────────────────────────────────┐      │
│   │              webapp-net (bridge)                 │      │
│   │                                                  │      │
│   │   ┌─────────┐           ┌─────────┐             │      │
│   │   │ webapp  │ ────────► │   db    │             │      │
│   │   │ :8000   │  "db"     │ :5432   │             │      │
│   │   └─────────┘           └─────────┘             │      │
│   │       │                      │                  │      │
│   │   EXPONERAD              EJ EXPONERAD           │      │
│   │   (p 8080:8000)          (intern endast)        │      │
│   │                                                  │      │
│   └──────────────────────────────────────────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Scenario: Web app + databas

# 1. Skapa nätverk
docker network create webapp-net

# 2. Starta databas (ingen port exponerad utåt!)
docker run -d \\
    --name db \\
    --network webapp-net \\
    -e POSTGRES_PASSWORD=secret \\
    postgres

# 3. Starta app som pratar med db internt
docker run -d \\
    --name webapp \\
    --network webapp-net \\
    -e DATABASE_HOST=db \\
    -p 8080:8000 \\
    mywebapp

# Resultat:
# - webapp nåbar på localhost:8080
# - db INTE nåbar utifrån (säkrare!)
# - webapp kan nå db via hostname "db"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Network Troubleshooting

| Kommando | Beskrivning |
|----------|-------------|
| `docker network inspect net` | Se nätverk-detaljer |
| `docker exec c1 ping c2` | Testa connectivity |
| `docker exec c1 nslookup c2` | Testa DNS |
| `docker port container` | Se port mappings |
| `docker stats` | Se nätverks I/O |

```bash
# Se vilka nätverk en container är i
docker inspect container_name --format='{{.NetworkSettings.Networks}}'

# Se alla containers i ett nätverk
docker network inspect mynet --format='{{range .Containers}}{{.Name}} {{end}}'

# Testa connectivity från container
docker exec webapp ping db
docker exec webapp curl http://api:8000/health

# Se nätverksstatistik
docker stats --format "table {{.Name}}\\t{{.NetIO}}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Koppla container till flera nätverk

```bash
# Container kan vara i flera nätverk
docker network connect frontend-net webapp
docker network connect backend-net webapp

# Nu kan webapp prata med båda nätverken

# Koppla bort
docker network disconnect frontend-net webapp
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `docker network create name` | Skapa nätverk |
| `docker network ls` | Lista nätverk |
| `docker network inspect name` | Visa detaljer |
| `docker network connect net container` | Anslut container |
| `docker network disconnect net container` | Koppla bort |
| `docker network rm name` | Ta bort nätverk |
| `docker network prune` | Städa oanvända |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Cannot resolve hostname | Olika nätverk | Samma user-defined network |
| Connection refused | Fel port/container nere | Kolla port och status |
| Port already in use | Annan process på porten | Byt host port |
| Network not found | Nätverket finns inte | Skapa eller kolla namn |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **User-defined bridge** | Använd för isolation och DNS |
| **Container DNS** | Containers hittar varandra via namn |
| **Port exposure** | Exponera bara nödvändiga portar |
| **Säkerhet** | `-p 127.0.0.1:8080:80` begränsar till localhost |

**Kom ihåg:**
- Använd **user-defined networks**, inte default bridge
- **Exponera aldrig** databasportar till internet
- **Container-namn** blir DNS-namn automatiskt
- Containers kan vara i **flera nätverk** samtidigt
""",
        },
        {
            "title": "Docker Volumes & Persistence",
            "slug": "docker-volumes-persistence",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Volumes & Persistence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Volumes är viktigt |
|----------|---------------------------|
| **Databaser** | Data måste överleva container restarts |
| **Stateful apps** | Uploads, sessions, cache |
| **Utveckling** | Hot reload utan rebuild |
| **Backup/Restore** | Kunna återställa data |
| **Shared state** | Data mellan containers |

Containers är ephemeral - data försvinner när de tas bort. Du måste förstå:

- **Hur du persisterar data** som databaser och uploads
- **Skillnaden mellan volumes och bind mounts**
- **Backup och restore** av container-data

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Problemet utan volumes

```
┌─────────────────────────────────────────────────────────────┐
│                 DATA UTAN VOLUMES                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. docker run postgres                                    │
│      ┌──────────────────┐                                   │
│      │    PostgreSQL    │                                   │
│      │   ┌──────────┐   │                                   │
│      │   │   DATA   │   │  ← Data i container               │
│      │   └──────────┘   │                                   │
│      └──────────────────┘                                   │
│                                                             │
│   2. docker rm postgres                                     │
│      ┌──────────────────┐                                   │
│      │    BORTTAGEN     │  ← DATA FÖRLORAD!                 │
│      └──────────────────┘                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Starta databas
docker run -d --name db postgres

# Skriv data...
# Stoppa och ta bort
docker rm -f db

# All data är BORTA!
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Tre sätt att persistera data

```
┌─────────────────────────────────────────────────────────────┐
│                 STORAGE OPTIONS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   VOLUMES              BIND MOUNTS          TMPFS           │
│   ───────              ───────────          ─────           │
│   Docker-managed       Host directory       RAM-disk        │
│   /var/lib/docker/     /host/path           Försvinner      │
│   volumes/             Kräver absolut       vid stopp       │
│   Best för prod        path                 Temp-filer      │
│                        Best för dev                         │
│                                                             │
│   ┌────────┐           ┌────────┐           ┌────────┐      │
│   │Volume  │           │Host FS │           │  RAM   │      │
│   │        │           │        │           │        │      │
│   └────────┘           └────────┘           └────────┘      │
│       │                    │                    │           │
│       ▼                    ▼                    ▼           │
│   ┌────────────────────────────────────────────────────┐    │
│   │                   Container                        │    │
│   └────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Typ | Syntax | Användning |
|-----|--------|------------|
| **Volume** | `-v mydata:/app/data` | Produktion, databaser |
| **Bind mount** | `-v /host/path:/container/path` | Utveckling |
| **tmpfs** | `--tmpfs /tmp` | Temp-filer, säkerhet |

```bash
# 1. Volumes (Docker-managed) - REKOMMENDERAS
docker run -v mydata:/var/lib/postgresql/data postgres

# 2. Bind mounts (host path)
docker run -v /host/path:/container/path postgres

# 3. tmpfs (RAM-disk, försvinner vid stopp)
docker run --tmpfs /tmp postgres
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Volumes (Docker-managed)

### Grundläggande kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker volume create name` | Skapa volume |
| `docker volume ls` | Lista volumes |
| `docker volume inspect name` | Visa detaljer |
| `docker volume rm name` | Ta bort volume |
| `docker volume prune` | Ta bort oanvända |

```bash
# Skapa volume
docker volume create dbdata

# Använd volume
docker run -d \\
    --name postgres \\
    -v dbdata:/var/lib/postgresql/data \\
    postgres

# Lista volumes
docker volume ls
# DRIVER    VOLUME NAME
# local     dbdata
# local     redis-data

# Inspektera volume
docker volume inspect dbdata
# [{"Name": "dbdata", "Mountpoint": "/var/lib/docker/volumes/dbdata/_data"}]

# Ta bort volume
docker volume rm dbdata

# Ta bort oanvända volumes
docker volume prune
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bind Mounts

Montera host-katalog direkt i container. Perfekt för utveckling.

```bash
# Montera host-katalog i container
docker run -v $(pwd)/app:/app myimage

# Read-only mount (container kan inte skriva)
docker run -v $(pwd)/config:/etc/app/config:ro myimage

# Användningsområden:
# - Utveckling (live reload)
# - Konfig-filer
# - Loggar du vill nå från host
```

### Bind Mount Options

| Option | Beskrivning |
|--------|-------------|
| `:ro` | Read-only |
| `:rw` | Read-write (default) |
| `:z` | SELinux shared |
| `:Z` | SELinux private |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Volumes vs Bind Mounts

| Egenskap | Volumes | Bind Mounts |
|----------|---------|-------------|
| **Management** | Docker hanterar | Du hanterar |
| **Plattform** | Fungerar överallt | Path-beroende |
| **Backup** | docker-kommandon | Standard backup |
| **Delning** | Mellan containers | Via host |
| **Performance** | Optimerat | Beror på host |
| **Användning** | Produktion | Utveckling |

```
┌─────────────────────────────────────────────────────────────┐
│                 VOLUMES vs BIND MOUNTS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   VOLUMES                       BIND MOUNTS                 │
│   ───────                       ───────────                 │
│   + Docker hanterar lagring     + Kontroll över path        │
│   + Plattformsoberoende         + Bra för utveckling        │
│   + Backup med docker           + Hot reload                │
│   + Dela mellan containers                                  │
│                                 - Host path-beroende        │
│                                 - Permission-problem        │
│                                                             │
│   ANVÄND FÖR:                   ANVÄND FÖR:                 │
│   • Databaser                   • Kod under utveckling      │
│   • Uploads                     • Config-filer              │
│   • Cache                       • Log-filer                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiskt exempel: Persistent Databas

```bash
# Skapa persistent PostgreSQL
docker volume create pgdata

docker run -d \\
    --name postgres \\
    -v pgdata:/var/lib/postgresql/data \\
    -e POSTGRES_PASSWORD=secret \\
    postgres

# Data överlever container restart/removal
docker rm -f postgres
docker run -d --name postgres -v pgdata:/var/lib/postgresql/data postgres
# Data finns kvar!
```

### Vanliga mount points

| Image | Data path |
|-------|-----------|
| **postgres** | `/var/lib/postgresql/data` |
| **mysql** | `/var/lib/mysql` |
| **mongodb** | `/data/db` |
| **redis** | `/data` |
| **elasticsearch** | `/usr/share/elasticsearch/data` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup och Restore

```
┌─────────────────────────────────────────────────────────────┐
│                 BACKUP STRATEGY                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Volume ──► Container ──► tar.gz ──► S3/Backup             │
│                                                             │
│   1. Skapa temp container                                   │
│   2. Montera volume som /source                             │
│   3. Montera backup-dir som /backup                         │
│   4. Kör tar för att komprimera                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Backup volume till tar-fil
docker run --rm \\
    -v pgdata:/source:ro \\
    -v $(pwd):/backup \\
    alpine tar czf /backup/pgdata-backup.tar.gz -C /source .

# Restore från backup
docker run --rm \\
    -v pgdata:/target \\
    -v $(pwd):/backup \\
    alpine tar xzf /backup/pgdata-backup.tar.gz -C /target

# Kopiera fil till/från volume
docker cp localfile.txt container:/path/in/volume/
docker cp container:/path/in/volume/file.txt ./local/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `docker volume create name` | Skapa volume |
| `docker volume ls` | Lista volumes |
| `docker volume inspect name` | Visa detaljer |
| `docker volume rm name` | Ta bort |
| `docker volume prune` | Städa oanvända |
| `-v vol:/path` | Montera volume |
| `-v /host:/path` | Bind mount |
| `-v /host:/path:ro` | Read-only mount |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Permission denied | User mismatch | `--user` eller `chown` |
| Volume busy | Container använder | Stoppa container först |
| Data försvinner | Glömde volume | Kolla `-v` flagga |
| Disk full | Stora volumes | `docker volume prune` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Volumes för prod** | Docker-managed, pålitligt |
| **Bind mounts för dev** | Hot reload, enkel access |
| **Data överlever** | Volumes överlever container removal |
| **Backup viktigt** | Volumes är inte automatiskt säkrade |

**Kom ihåg:**
- **Alltid** använd volumes för databaser
- **Bind mounts** för kod under utveckling
- **Backup regelbundet** - automatisera det
- **docker volume prune** frigör diskutrymme
""",
        },
        {
            "title": "Docker Compose Fundamentals",
            "slug": "docker-compose-fundamentals",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Docker Compose Fundamentals

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Docker Compose är viktigt |
|----------|----------------------------------|
| **Multi-container apps** | Frontend + Backend + DB i en fil |
| **Reproducerbarhet** | Samma setup för alla utvecklare |
| **IaC** | Infrastruktur som kod, versionshantera |
| **Onboarding** | Nya utvecklare kör `docker compose up` |
| **Testing** | Snabbt starta hela test-miljön |

Att köra `docker run` med 10 flaggor för flera containers är opraktiskt. Du behöver:

- **Definiera hela stacken** i en fil
- **Starta allt med ett kommando**
- **Versionshantera infrastrukturen** som kod

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad är Docker Compose?

```
┌─────────────────────────────────────────────────────────────┐
│                 DOCKER COMPOSE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   UTAN Compose:                MED Compose:                 │
│   ────────────                 ───────────                  │
│   docker network create...     docker compose up            │
│   docker run db...                                          │
│   docker run api...            Allt definierat i            │
│   docker run web...            docker-compose.yml           │
│   (många kommandon!)           (en fil, ett kommando!)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Docker Compose låter dig definiera multi-container applikationer i en YAML-fil.

### Utan Compose (jobbigt):
```bash
docker network create mynet
docker run -d --name db --network mynet -v dbdata:/data postgres
docker run -d --name api --network mynet -p 8080:8000 -e DB_HOST=db myapi
```

### Med Compose (enkelt):
```yaml
# docker-compose.yml
services:
  db:
    image: postgres
    volumes:
      - dbdata:/data
  api:
    image: myapi
    ports:
      - "8080:8000"
    environment:
      - DB_HOST=db

volumes:
  dbdata:
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundläggande struktur

```yaml
# docker-compose.yml
services:       # Containers att köra
  service1:
    image: ...
  service2:
    build: ...

volumes:        # Named volumes
  data:

networks:       # Custom networks (optional)
  frontend:
  backend:
```

### Struktur-översikt

| Sektion | Beskrivning |
|---------|-------------|
| `services` | Containers att köra (obligatorisk) |
| `volumes` | Named volumes |
| `networks` | Custom networks |
| `secrets` | Känslig data (Swarm) |
| `configs` | Config-filer (Swarm) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Service-konfiguration

### Alla viktiga options

| Option | Beskrivning | Exempel |
|--------|-------------|---------|
| `image` | Använd befintlig image | `image: nginx:alpine` |
| `build` | Bygg från Dockerfile | `build: ./app` |
| `ports` | Port mapping | `ports: ["8080:80"]` |
| `environment` | Miljövariabler | `environment: [DEBUG=1]` |
| `env_file` | Variabler från fil | `env_file: .env` |
| `volumes` | Mount volumes | `volumes: [./app:/app]` |
| `depends_on` | Start-ordning | `depends_on: [db]` |
| `restart` | Restart policy | `restart: unless-stopped` |
| `networks` | Nätverk | `networks: [backend]` |

```yaml
services:
  webapp:
    # Välj image ELLER build
    image: nginx:alpine
    # ELLER
    build:
      context: ./app
      dockerfile: Dockerfile.prod

    # Port mapping
    ports:
      - "8080:80"
      - "443:443"

    # Miljövariabler
    environment:
      - NODE_ENV=production
      - API_KEY=secret
    env_file:
      - .env

    # Volumes
    volumes:
      - ./app:/app          # Bind mount
      - data:/var/lib/data  # Named volume

    # Dependencies
    depends_on:
      - db
      - redis

    # Restart policy
    restart: unless-stopped

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundläggande kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker compose up` | Starta alla services |
| `docker compose up -d` | Starta i bakgrunden |
| `docker compose down` | Stoppa och ta bort |
| `docker compose down -v` | + ta bort volumes |
| `docker compose ps` | Lista services |
| `docker compose logs` | Visa loggar |
| `docker compose logs -f` | Följ loggar |
| `docker compose build` | Bygg images |
| `docker compose exec service cmd` | Kör kommando |

```bash
# Starta alla services
docker compose up

# Starta i bakgrunden
docker compose up -d

# Stoppa alla services
docker compose down

# Stoppa och ta bort volumes (VARNING: raderar data!)
docker compose down -v

# Se status
docker compose ps
# NAME        SERVICE   STATUS    PORTS
# app-db-1    db        running   5432/tcp
# app-api-1   api       running   0.0.0.0:8000->8000/tcp

# Se loggar
docker compose logs
docker compose logs -f webapp  # Följ specifik service

# Bygg om images
docker compose build
docker compose up --build  # Build + start

# Kör kommando i service
docker compose exec db psql -U postgres
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Komplett exempel: Full Stack App

```
┌─────────────────────────────────────────────────────────────┐
│                 FULL STACK ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Internet                                                  │
│      │                                                      │
│      │ :3000                                                │
│      ▼                                                      │
│   ┌─────────┐    :8000     ┌─────────┐     ┌─────────┐     │
│   │   web   │ ───────────▶ │   api   │ ──▶ │   db    │     │
│   │ (React) │              │(FastAPI)│     │(Postgres│     │
│   └─────────┘              └─────────┘     └─────────┘     │
│                                 │                          │
│                                 ▼                          │
│                            ┌─────────┐                     │
│                            │  redis  │                     │
│                            │ (cache) │                     │
│                            └─────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```yaml
# docker-compose.yml
services:
  # Frontend
  web:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api

  # Backend API
  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./backend:/app  # Hot reload i utveckling

  # Database
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app
    volumes:
      - pgdata:/var/lib/postgresql/data
    # Ingen port exponerad - bara intern access

  # Cache
  redis:
    image: redis:alpine

volumes:
  pgdata:
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `docker compose up -d` | Starta i bakgrund |
| `docker compose down` | Stoppa allt |
| `docker compose ps` | Lista services |
| `docker compose logs -f` | Följ loggar |
| `docker compose exec svc cmd` | Kör i service |
| `docker compose build` | Bygg images |
| `docker compose pull` | Hämta images |
| `docker compose restart svc` | Starta om service |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| `service not found` | Fel service-namn | Kolla stavning i yml |
| `port already in use` | Port upptagen | Byt port eller stoppa process |
| `cannot connect to db` | DB ej startat | Lägg till depends_on |
| `volume permission denied` | User mismatch | Fixa permissions |
| `build failed` | Dockerfile-fel | Kolla build-output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **En fil = hela stacken** | Lätt att versionshantera |
| **Automatiskt nätverk** | Services hittar varandra via namn |
| **depends_on** | Kontrollerar start-ordning |
| **down -v** | Tar bort allt inkl volumes |

**Kom ihåg:**
- Compose är **standard för local development**
- Services **kommunicerar via service-namn**
- Använd **.env** för miljövariabler
- **depends_on** garanterar inte att service är ready
""",
        },
        {
            "title": "Docker Compose Advanced Patterns",
            "slug": "docker-compose-advanced-patterns",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker Compose Advanced Patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför Advanced Compose är viktigt |
|----------|-----------------------------------|
| **Miljöhantering** | Samma kod, olika config för dev/prod |
| **Reliability** | Healthchecks för automatisk recovery |
| **Skalning** | Köra flera instanser av en service |
| **Säkerhet** | Secrets management för känslig data |
| **DRY** | Återanvänd config med YAML anchors |

Grundläggande Compose räcker för utveckling, men produktion kräver mer:

- **Miljöspecifik konfiguration** (dev vs prod)
- **Healthchecks och restart policies**
- **Skalning och load balancing**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multiple Compose Files

```
┌─────────────────────────────────────────────────────────────┐
│                 COMPOSE FILE LAYERING                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   docker-compose.yml          (bas-konfiguration)           │
│          │                                                  │
│          ▼                                                  │
│   docker-compose.override.yml (laddas automatiskt, dev)     │
│          │                                                  │
│          ▼                                                  │
│   docker-compose.prod.yml     (explicit, produktion)        │
│                                                             │
│   Senare filer överskriver tidigare!                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Fil | Laddas | Användning |
|-----|--------|------------|
| `docker-compose.yml` | Alltid | Bas-konfiguration |
| `docker-compose.override.yml` | Automatiskt | Development |
| `docker-compose.prod.yml` | Med `-f` | Production |
| `docker-compose.test.yml` | Med `-f` | Testing |

```yaml
# docker-compose.yml (bas)
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://db:5432/app

# docker-compose.override.yml (dev, laddas automatiskt)
services:
  api:
    volumes:
      - .:/app  # Hot reload
    environment:
      - DEBUG=true

# docker-compose.prod.yml
services:
  api:
    image: myregistry/api:${VERSION}
    restart: always
    deploy:
      replicas: 3
```

```bash
# Development (override laddas automatiskt)
docker compose up

# Production (explicit)
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Healthchecks

Healthchecks låter Docker veta om en service är frisk.

| Parameter | Beskrivning | Default |
|-----------|-------------|---------|
| `test` | Kommando som returnerar 0=healthy | - |
| `interval` | Tid mellan checks | 30s |
| `timeout` | Max tid för check | 30s |
| `retries` | Antal misslyckanden innan unhealthy | 3 |
| `start_period` | Grace period vid start | 0s |

```yaml
services:
  api:
    image: myapi
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Vänta på att dependency är HEALTHY (inte bara started)
  api:
    depends_on:
      db:
        condition: service_healthy
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Environment Variables

| Metod | Syntax | Användning |
|-------|--------|------------|
| Direkt | `VAR=value` | Enkla värden |
| Från host | `VAR=${VAR}` | Runtime config |
| Med default | `VAR=${VAR:-default}` | Fallback |
| Från fil | `env_file: .env` | Många variabler |

```yaml
services:
  api:
    image: myapi
    environment:
      # Direkt värde
      - NODE_ENV=production
      # Från host environment
      - API_KEY=${API_KEY}
      # Med default
      - PORT=${PORT:-8000}

    # Eller från fil
    env_file:
      - .env
      - .env.local  # Överskriver .env
```

```bash
# .env
POSTGRES_PASSWORD=secret
API_KEY=abc123
DEBUG=false
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Profiles

Profiles låter dig gruppera services som startas tillsammans.

```yaml
services:
  api:
    image: myapi
    # Ingen profile = alltid aktiv

  debug-tools:
    image: busybox
    profiles:
      - debug
    # Startas BARA med --profile debug

  monitoring:
    image: prometheus
    profiles:
      - monitoring
      - production
```

```bash
# Bara api (ingen profile angiven)
docker compose up

# api + debug-tools
docker compose --profile debug up

# api + monitoring
docker compose --profile monitoring up

# Flera profiles
docker compose --profile monitoring --profile debug up
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skalning

```yaml
services:
  worker:
    image: myworker
    deploy:
      replicas: 3  # Starta 3 instanser
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
```

```bash
# Skala dynamiskt
docker compose up -d --scale worker=5

# Se status
docker compose ps
# NAME           SERVICE   REPLICAS   STATUS
# app-worker-1   worker    5/5        running
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets

Säkrare än environment variables för känslig data.

```yaml
services:
  api:
    image: myapi
    secrets:
      - db_password
      - api_key

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    environment: API_KEY  # Från host env
```

```bash
# I containern läses secrets från filer:
cat /run/secrets/db_password
cat /run/secrets/api_key
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Extension Fields (YAML anchors)

Återanvänd konfiguration för DRY (Don't Repeat Yourself).

```yaml
# Definiera med x- prefix
x-common-env: &common-env
  LOG_LEVEL: info
  TZ: Europe/Stockholm

x-healthcheck: &default-healthcheck
  interval: 30s
  timeout: 10s
  retries: 3

services:
  api:
    environment:
      <<: *common-env      # Spread anchor
      SERVICE_NAME: api    # Override/add
    healthcheck:
      <<: *default-healthcheck
      test: curl -f http://localhost:8000/health

  worker:
    environment:
      <<: *common-env
      SERVICE_NAME: worker
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Feature | Syntax |
|---------|--------|
| Override fil | `-f compose.yml -f override.yml` |
| Healthcheck | `healthcheck: test: [CMD, ...]` |
| Condition | `depends_on: svc: condition: service_healthy` |
| Profile | `profiles: [debug]` |
| Scale | `--scale worker=5` |
| Secrets | `secrets: [name]` |
| Anchor | `&name` och `<<: *name` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Override files** | Miljöspecifik config utan duplicering |
| **Healthchecks** | Kritiska för automatisk recovery |
| **Profiles** | Gruppera valfria services |
| **Secrets** | Säkrare än environment variables |

**Kom ihåg:**
- **override.yml** laddas automatiskt i development
- **service_healthy** väntar på faktisk health, inte bara start
- **YAML anchors** minskar duplicering
- Använd **secrets** för lösenord, inte env vars
""",
        },
        {
            "title": "Docker Security Best Practices",
            "slug": "docker-security-best-practices",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Security Best Practices

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Risk | Konsekvens |
|------|------------|
| **Root i container** | Container escape → host komprometterad |
| **Stora images** | Fler sårbarheter, större attack surface |
| **Secrets i image** | Läcker i registry, git history |
| **Ingen scanning** | Kända CVEs i produktion |
| **Inga resource limits** | DoS, kraschar andra containers |

Containers är inte automatiskt säkra. Du måste förstå:

- **Vanliga säkerhetsrisker** och hur du undviker dem
- **Principle of least privilege** för containers
- **Image scanning** för sårbarheter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kör ALDRIG som root

```
┌─────────────────────────────────────────────────────────────┐
│              ROOT vs NON-ROOT                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ROOT (default)              NON-ROOT (säkert)             │
│   ──────────────              ─────────────────             │
│   UID 0                       UID 1000+                     │
│   Full host access            Begränsad access              │
│   Container escape risk       Isolerad                      │
│                                                             │
│   Om container komprometteras:                              │
│   Root → Kan skada host       Non-root → Begränsad skada    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```dockerfile
# DÅLIGT - kör som root (default)
FROM python:3.11
COPY app.py /app/
CMD ["python", "/app/app.py"]

# BRA - skapa och använd non-root user
FROM python:3.11
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser
COPY --chown=appuser:appuser app.py .
USER appuser
CMD ["python", "app.py"]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Minimal Base Images

| Image | Storlek | Paket | Säkerhet |
|-------|---------|-------|----------|
| `ubuntu:22.04` | ~77 MB | Många | Lägst |
| `python:3.11` | ~1 GB | Många | Låg |
| `python:3.11-slim` | ~150 MB | Få | Medium |
| `python:3.11-alpine` | ~50 MB | Minimalt | Hög |
| `distroless` | ~20 MB | Endast runtime | Högst |

```dockerfile
# DÅLIGT - full OS med massa onödiga paket
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3

# BRA - minimal image
FROM python:3.11-slim

# BÄST (om möjligt) - distroless
FROM gcr.io/distroless/python3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Använd specifika tags

| Tagging | Exempel | Säkerhet |
|---------|---------|----------|
| **latest** | `python:latest` | Farligt - kan ändras |
| **Major** | `python:3` | Riskabelt |
| **Minor** | `python:3.11` | Bättre |
| **Patch** | `python:3.11.7-slim` | Bra |
| **SHA digest** | `python@sha256:abc...` | Bäst - immutable |

```dockerfile
# DÅLIGT - kan ändras när som helst
FROM python:latest
FROM nginx

# BRA - specifik version
FROM python:3.11.7-slim
FROM nginx:1.25.3-alpine

# BÄST - sha256 digest (immutable)
FROM python@sha256:abc123...
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Read-only filsystem

```bash
# Kör container med read-only root filesystem
docker run --read-only myimage

# Tillåt skrivning till specifika paths
docker run --read-only \\
    --tmpfs /tmp \\
    --tmpfs /var/run \\
    -v logs:/var/log \\
    myimage
```

| Flag | Beskrivning |
|------|-------------|
| `--read-only` | Gör root filesystem read-only |
| `--tmpfs /tmp` | RAM-disk för temp-filer |
| `-v logs:/path` | Persistent volume för loggar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Begränsa capabilities

Linux capabilities ger finkornig kontroll över privilegier.

| Capability | Funktion | Behövs ofta? |
|------------|----------|--------------|
| `NET_BIND_SERVICE` | Bind ports < 1024 | Ibland |
| `CHOWN` | Ändra fil-ägare | Sällan |
| `SETUID/SETGID` | Ändra user/group | Sällan |
| `SYS_ADMIN` | Systemadmin | Aldrig |
| `NET_RAW` | Raw sockets | Sällan |

```bash
# Ta bort alla och lägg till bara det som behövs
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Resource Limits

| Limit | Flag | Beskrivning |
|-------|------|-------------|
| Memory | `--memory=512m` | Max RAM |
| Memory+Swap | `--memory-swap=512m` | Disable swap |
| CPU | `--cpus=0.5` | CPU-tid (0.5 = 50%) |
| PIDs | `--pids-limit=100` | Max processer |

```bash
# Utan limits kan en container ta alla resurser
docker run \\
    --memory=512m \\
    --memory-swap=512m \\
    --cpus=0.5 \\
    --pids-limit=100 \\
    myimage
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          memory: 256M
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Scanning

| Verktyg | Typ | Kommando |
|---------|-----|----------|
| **Docker Scout** | Inbyggt | `docker scout cves myimage` |
| **Trivy** | Open source | `trivy image myimage` |
| **Snyk** | Commercial | `snyk container test myimage` |
| **Grype** | Open source | `grype myimage` |

```bash
# Scanna image för sårbarheter
docker scout cves myimage
docker scout recommendations myimage

# Trivy (populärt open source alternativ)
trivy image myimage

# Snyk
snyk container test myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets Hantering

| Metod | Säkerhet | Användning |
|-------|----------|------------|
| Environment vars | Låg | Synliga i inspect |
| Dockerfile ENV | Låg | Finns i image |
| Docker Secrets | Hög | Fil i /run/secrets |
| External (Vault) | Högst | Enterprise |

```bash
# DÅLIGT - secrets i environment variables
docker run -e DATABASE_PASSWORD=secret123 myimage

# DÅLIGT - secrets i Dockerfile
ENV API_KEY=secret123

# BRA - Docker secrets
docker secret create db_pass ./password.txt
docker run --secret db_pass myimage
# Läses från /run/secrets/db_pass

# BRA - External secret management
# HashiCorp Vault, AWS Secrets Manager, etc.
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Network Security

```bash
# Isolera containers i egna nätverk
docker network create --internal backend
# --internal = ingen internet-access

# Exponera bara nödvändiga portar
docker run -p 127.0.0.1:8080:8080 myimage  # Bara localhost
```

| Network type | Internet | Isolation |
|--------------|----------|-----------|
| `bridge` | Ja | Per-nätverk |
| `--internal` | Nej | Hög |
| `none` | Nej | Total |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Checklist

| Check | Status |
|-------|--------|
| Non-root user | [ ] |
| Minimal base image (slim/alpine/distroless) | [ ] |
| Specifika image tags | [ ] |
| Read-only filesystem där möjligt | [ ] |
| Dropped capabilities | [ ] |
| Resource limits | [ ] |
| No secrets i images/env vars | [ ] |
| Regelbunden image scanning | [ ] |
| Isolerade nätverk | [ ] |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Non-root** | Kör aldrig som root - skapa appuser |
| **Minimal images** | Mindre image = mindre attack surface |
| **Scanning** | Scanna images regelbundet för CVEs |
| **Secrets** | Hör inte hemma i env vars eller Dockerfiles |

**Kom ihåg:**
- Säkerhet är **inte optional** i produktion
- **Defense in depth** - flera lager av skydd
- **Automatisera scanning** i CI/CD pipeline
- **Uppdatera base images** regelbundet
""",
        },
        {
            "title": "Docker in Production",
            "slug": "docker-in-production",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker in Production

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför production-kunskap är kritisk |
|----------|-------------------------------------|
| **Uptime** | Containers måste överleva crashes |
| **Debugging** | Loggar måste vara tillgängliga |
| **Performance** | Resource management för stabilitet |
| **Updates** | Zero-downtime deployments |
| **Recovery** | Backup och restore-strategier |

Att köra Docker lokalt är en sak - produktion är en annan. Du måste förstå:

- **Logging och monitoring** för att veta vad som händer
- **Restart policies** för att hantera crashes
- **Resource management** för stabil drift

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Restart Policies

| Policy | Beteende | Användning |
|--------|----------|------------|
| `no` | Starta aldrig om (default) | Test/debug |
| `always` | Starta alltid om | Kritiska services |
| `unless-stopped` | Som always, men inte om manuellt stoppad | Production |
| `on-failure:N` | Bara vid crash, max N försök | Jobs |

```bash
# Exempel
docker run --restart no myimage           # Ingen restart
docker run --restart always myimage       # Alltid (även vid reboot)
docker run --restart unless-stopped myimage # Production standard
docker run --restart on-failure:5 myimage # Max 5 försök vid crash
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi
    restart: unless-stopped
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logging

| Kommando | Beskrivning |
|----------|-------------|
| `docker logs container` | Visa loggar |
| `docker logs -f container` | Follow (tail -f) |
| `docker logs --tail 100` | Senaste 100 rader |
| `docker logs --since 1h` | Senaste timmen |
| `docker logs -t` | Med timestamps |

```bash
# Se loggar
docker logs container_name
docker logs -f container_name      # Follow
docker logs --tail 100 container_name
docker logs --since 1h container_name
```

### Log Drivers

| Driver | Beskrivning | Användning |
|--------|-------------|------------|
| `json-file` | Default, lokala filer | Development |
| `syslog` | System syslog | Linux servers |
| `fluentd` | Fluentd collector | Centraliserad |
| `awslogs` | AWS CloudWatch | AWS |
| `gcplogs` | Google Cloud Logging | GCP |

```bash
# Konfigurera log driver
docker run --log-driver json-file \\
    --log-opt max-size=10m \\
    --log-opt max-file=3 \\
    myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring

| Kommando | Beskrivning |
|----------|-------------|
| `docker stats` | Live CPU, mem, net |
| `docker stats --no-stream` | Snapshot |
| `docker top container` | Processer |
| `docker inspect` | Full metadata |

```bash
# Real-time stats
docker stats

# Format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Health status
docker inspect --format='{{.State.Health.Status}}' container_name
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Healthchecks

| Parameter | Beskrivning | Default |
|-----------|-------------|---------|
| `--interval` | Tid mellan checks | 30s |
| `--timeout` | Max tid per check | 30s |
| `--retries` | Misslyckanden innan unhealthy | 3 |
| `--start-period` | Grace period vid start | 0s |

```dockerfile
# I Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1
```

```bash
# Vid runtime
docker run --health-cmd="curl -f http://localhost:8000/health" \\
    --health-interval=30s \\
    --health-timeout=3s \\
    --health-retries=3 \\
    myimage

# Kolla health status
docker inspect --format='{{json .State.Health}}' container_name
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Production Docker Compose

```yaml
# docker-compose.prod.yml
services:
  api:
    image: myregistry/api:${VERSION:-latest}
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
    healthcheck:
      test: curl -f http://localhost:8000/health
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    environment:
      - NODE_ENV=production
    secrets:
      - db_password

  db:
    image: postgres:15
    restart: unless-stopped
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: pg_isready -U postgres
      interval: 10s
      timeout: 5s
      retries: 5

secrets:
  db_password:
    external: true

volumes:
  pgdata:
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deployment Strategies

```
┌─────────────────────────────────────────────────────────────┐
│              DEPLOYMENT STRATEGIES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   BLUE-GREEN                  ROLLING UPDATE                │
│   ──────────                  ──────────────                │
│   [Blue v1] ──┐               [v1] [v1] [v1]                │
│               │ Switch        [v2] [v1] [v1]                │
│   [Green v2]──┘               [v2] [v2] [v1]                │
│                               [v2] [v2] [v2]                │
│                                                             │
│   + Instant rollback          + No extra resources          │
│   - Double resources          - Slower rollback             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Blue-Green
docker compose -p myapp-green up -d
curl http://localhost:8081/health
# Byt trafik via load balancer
docker compose -p myapp-blue down

# Rolling (Swarm)
docker service update --image myimage:v2 myservice
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Backup Strategy

| Vad | Hur | Frekvens |
|-----|-----|----------|
| **Volumes** | tar + offsite | Dagligen |
| **Databas** | pg_dump/mysqldump | Var 6:e timme |
| **Config** | Git repo | Vid ändring |

```bash
# Backup volumes
docker run --rm \\
    -v mydata:/source:ro \\
    -v $(pwd)/backups:/backup \\
    alpine tar czf /backup/mydata-$(date +%Y%m%d).tar.gz -C /source .

# Backup databas
docker exec postgres pg_dump -U postgres mydb > backup.sql
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Restart policy** | `unless-stopped` för prod |
| **Healthchecks** | Obligatoriska i produktion |
| **Resource limits** | Förhindrar att en container tar ner allt |
| **Logging** | Centraliserat för felsökning |

**Kom ihåg:**
- **Planera för failure** - containers kommer krascha
- **Automatisera backup** - testa restore regelbundet
- **Monitoring är obligatoriskt** - du kan inte fixa det du inte ser
""",
        },
        {
            "title": "Docker Registry & Image Distribution",
            "slug": "docker-registry-image-distribution",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Registry & Image Distribution

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Varför registry-kunskap är kritisk |
|----------|-----------------------------------|
| **CI/CD** | Automatiserad push/pull i pipelines |
| **Distribution** | Dela images mellan team och miljöer |
| **Säkerhet** | Private registries för känslig kod |
| **Versioning** | Tagging-strategier för rollback |

Images måste lagras och distribueras. Du måste förstå:

- **Hur registries fungerar** och vilka alternativ som finns
- **Push och pull** av images
- **Private registries** för företagsbruk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vad är ett Registry?

Ett registry är en lagringsplats för Docker images. Tänk på det som "npm för containers".

```
┌─────────────────────────────────────────────────────────────┐
│                 IMAGE NAMING CONVENTION                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   registry.example.com / namespace / repository : tag       │
│   ────────────────────   ─────────   ──────────   ───       │
│   Registry URL           User/Org    Image name   Version   │
│   (default: docker.io)                            (latest)  │
│                                                             │
│   Exempel:                                                  │
│   docker.io/library/nginx:1.25                              │
│   ghcr.io/myorg/myapp:v2.0.0                               │
│   123456.dkr.ecr.eu-north-1.amazonaws.com/api:latest       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Registry-typer

| Registry | Typ | Användning |
|----------|-----|------------|
| **Docker Hub** | Public/Private | Default, open source |
| **GitHub GHCR** | Private | GitHub-integrerat |
| **AWS ECR** | Private | AWS-ekosystem |
| **Google GCR** | Private | GCP-ekosystem |
| **Azure ACR** | Private | Azure-ekosystem |
| **Harbor** | Self-hosted | Enterprise on-prem |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker Hub (Public)

| Kommando | Beskrivning |
|----------|-------------|
| `docker login` | Logga in |
| `docker tag img user/img:tag` | Tagga image |
| `docker push user/img:tag` | Pusha till Hub |
| `docker pull user/img:tag` | Pulla från Hub |

```bash
# Logga in
docker login

# Tagga för Docker Hub
docker tag myimage username/myimage:v1.0

# Pusha till Docker Hub
docker push username/myimage:v1.0

# Pulla
docker pull username/myimage:v1.0
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Private Registries

### AWS ECR
```bash
aws ecr get-login-password --region eu-north-1 | \\
    docker login --username AWS --password-stdin 123456789.dkr.ecr.eu-north-1.amazonaws.com

docker tag myimage 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1
docker push 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1
```

### Google Container Registry
```bash
gcloud auth configure-docker
docker tag myimage gcr.io/my-project/myimage:v1
docker push gcr.io/my-project/myimage:v1
```

### Azure Container Registry
```bash
az acr login --name myregistry
docker tag myimage myregistry.azurecr.io/myimage:v1
docker push myregistry.azurecr.io/myimage:v1
```

### GitHub Container Registry
```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag myimage ghcr.io/username/myimage:v1
docker push ghcr.io/username/myimage:v1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Self-hosted Registry

```bash
# Starta eget registry
docker run -d -p 5000:5000 --name registry registry:2

# Använd det
docker tag myimage localhost:5000/myimage:v1
docker push localhost:5000/myimage:v1
docker pull localhost:5000/myimage:v1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Tagging Strategy

| Strategy | Exempel | Användning |
|----------|---------|------------|
| **Semantic** | `1.0.0`, `1.0`, `1` | Release versions |
| **Git SHA** | `abc123f` | CI/CD traceability |
| **Branch** | `main`, `develop` | Dev environments |
| **Timestamp** | `20241207-143022` | Continuous deploys |
| **Latest** | `latest` | UNDVIK i prod! |

```bash
# Bra tagging i CI/CD
myimage:1.2.3              # Semantisk version
myimage:abc123f            # Git commit SHA
myimage:v1.2.3-abc123f     # Kombination (bäst!)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-platform Images

```bash
# Bygg för flera arkitekturer
docker buildx create --name mybuilder --use

docker buildx build \\
    --platform linux/amd64,linux/arm64 \\
    -t myimage:v1 \\
    --push \\
    .

# Inspektera manifest
docker manifest inspect myimage:v1
```

| Platform | Användning |
|----------|------------|
| `linux/amd64` | Standard servers, Intel/AMD |
| `linux/arm64` | AWS Graviton, Apple Silicon |
| `linux/arm/v7` | Raspberry Pi |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Docker Hub** | Public images, open source |
| **Private registry** | Företagets images, känslig kod |
| **Specifika tags** | Aldrig `latest` i produktion |
| **Multi-platform** | ARM/AMD64 kompatibilitet |

**Kom ihåg:**
- **Logga in** innan push/pull till private registries
- **Tagga med SHA** för spårbarhet i CI/CD
- **Multi-platform** för moderna ARM-baserade servers
""",
        },
        {
            "title": "Docker Multi-stage Builds",
            "slug": "docker-multi-stage-builds",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Multi-stage Builds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Problem | Multi-stage lösning |
|---------|---------------------|
| **Stora images** | Bara runtime i final image |
| **Build tools i prod** | Separera build och runtime |
| **Säkerhetsrisk** | Mindre attack surface |
| **Långsam deploy** | Mindre image = snabbare pull |

Build-verktyg och dependencies behövs inte i produktion. Du måste kunna:

- **Separera build och runtime** för mindre images
- **Kopiera artefakter** mellan stages
- **Optimera för säkerhet** genom att exkludera build-verktyg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Problemet utan multi-stage

```dockerfile
# Allt i en stage = stor image med onödiga verktyg
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
# Image innehåller: Node.js, npm, devDependencies, source code, build tools...
# Storlek: ~1 GB
CMD ["node", "dist/index.js"]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-stage lösningen

```
┌─────────────────────────────────────────────────────────────┐
│                 MULTI-STAGE BUILD                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   STAGE 1: builder              STAGE 2: production         │
│   ───────────────               ────────────────────        │
│   FROM node:18                  FROM node:18-slim           │
│   + npm, devDeps                - Bara runtime              │
│   + Source code                 - Compiled code             │
│   + Build tools                 - prod deps only            │
│   = ~1 GB                       = ~150 MB                   │
│                                                             │
│   [Build] ─── COPY --from=builder ───▶ [Production]         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-slim
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/index.js"]
# Image innehåller: Bara runtime + compiled code
# Storlek: ~150 MB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Språkspecifika exempel

### Go (statisk binär)

| Stage | Base image | Storlek |
|-------|------------|---------|
| Build | `golang:1.21` | ~1 GB |
| Prod | `scratch` | ~10-20 MB |

```dockerfile
# Build stage
FROM golang:1.21 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/server

# Production stage - minimal!
FROM scratch
COPY --from=builder /app/server /server
USER 1000
ENTRYPOINT ["/server"]
```

### Python

```dockerfile
# Build stage
FROM python:3.11 AS builder
WORKDIR /app
RUN pip install --user poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt
RUN pip install --user -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
USER nobody
CMD ["python", "app.py"]
```

### React/Frontend

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage - bara statiska filer!
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
# Image storlek: ~25 MB
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Avancerat: Flera stages

```dockerfile
# Base stage med gemensamma dependencies
FROM node:18-slim AS base
WORKDIR /app
COPY package*.json ./

# Development dependencies
FROM base AS dev-deps
RUN npm ci

# Production dependencies
FROM base AS prod-deps
RUN npm ci --omit=dev

# Build
FROM dev-deps AS builder
COPY . .
RUN npm run build

# Test (kan köras separat)
FROM dev-deps AS tester
COPY . .
RUN npm test

# Production
FROM node:18-slim
WORKDIR /app
COPY --from=prod-deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
USER node
CMD ["node", "dist/index.js"]
```

### Bygg specifik stage

```bash
# Bygg bara test stage
docker build --target tester -t myapp:test .

# Bygg prod (default, sista stage)
docker build -t myapp:prod .
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kopiera från externa images

```dockerfile
# Kopiera verktyg från annan image
FROM alpine
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/
COPY --from=hashicorp/terraform:latest /bin/terraform /usr/local/bin/
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Storleksjämförelse

| Språk | Single-stage | Multi-stage | Besparing |
|-------|--------------|-------------|-----------|
| Node.js | ~1 GB | ~150 MB | 85% |
| Go | ~1 GB | ~10 MB | 99% |
| Python | ~1 GB | ~200 MB | 80% |
| React | ~500 MB | ~25 MB | 95% |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Separera stages** | Build vs runtime |
| **COPY --from** | Kopiera mellan stages |
| **Sista FROM** | Blir final image |
| **slim/alpine/scratch** | Minimal prod image |

**Kom ihåg:**
- Multi-stage ger **dramatiskt mindre images**
- Mindre image = **snabbare deploys**
- Mindre image = **mindre attack surface**
- Använd **--target** för att bygga specifik stage
""",
        },
        {
            "title": "Docker Performance Optimization",
            "slug": "docker-performance-optimization",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Performance Optimization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Problem | Kostnad |
|---------|---------|
| **Långsamma builds** | Slöseri med utvecklartid |
| **Stora images** | Långsam deploy, mer lagring |
| **Dålig caching** | Onödiga rebuilds |
| **Resource-hunger** | Instabil drift |

Långsamma builds och stora images kostar tid och pengar. Du måste kunna:

- **Optimera build-tid** genom smart caching
- **Minska image-storlek** för snabbare deploys
- **Förbättra runtime-prestanda**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Build Cache Optimization

```
┌─────────────────────────────────────────────────────────────┐
│                 LAYER CACHING                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Layer 1: FROM python ────────────── [CACHED]              │
│   Layer 2: COPY requirements.txt ──── [CACHED]              │
│   Layer 3: RUN pip install ────────── [CACHED]              │
│   Layer 4: COPY . . ───────────────── [REBUILD] <-- ändring │
│   Layer 5: RUN build ──────────────── [REBUILD]             │
│                                                             │
│   Om Layer N ändras → alla efterföljande rebuilds!          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```dockerfile
# DÅLIGT - cache invalideras vid varje kodändring
FROM python:3.11
COPY . /app
RUN pip install -r requirements.txt

# BRA - dependencies cachas separat
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt  # Cachas om requirements.txt inte ändras
COPY . .
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Layer Order - Bästa praxis

| Ordning | Vad | Ändras |
|---------|-----|--------|
| 1 | Base image | Sällan |
| 2 | System packages | Sällan |
| 3 | Dependencies | Ibland |
| 4 | Application code | Ofta |
| 5 | Build step | Ofta |

```dockerfile
# Ordna från minst till mest ändrade
FROM node:18-slim

# 1. System packages (ändras sällan)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 2. Dependencies (ändras ibland)
COPY package*.json ./
RUN npm ci

# 3. Application code (ändras ofta)
COPY . .

# 4. Build (beror på kod)
RUN npm run build
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Minska antal layers

```dockerfile
# DÅLIGT - 4 layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# BRA - 1 layer
RUN apt-get update && \\
    apt-get install -y \\
        curl \\
        git && \\
    rm -rf /var/lib/apt/lists/*
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## .dockerignore

```bash
# .dockerignore - exkludera onödiga filer från COPY
node_modules
.git
.gitignore
*.md
Dockerfile*
docker-compose*
.env*
__pycache__
*.pyc
.pytest_cache
coverage
dist
build
```

| Fil | Varför exkludera |
|-----|------------------|
| `node_modules` | Installeras i container |
| `.git` | Inte nödvändig, stor |
| `*.md` | Dokumentation |
| `__pycache__` | Python bytecode |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## BuildKit Features

| Feature | Beskrivning |
|---------|-------------|
| Parallella builds | Bygger oberoende stages samtidigt |
| Cache mounts | Cachar paketmanagers mellan builds |
| Secret mounts | Säker hantering av secrets under build |
| SSH mounts | Git clone med SSH keys |

```bash
# Aktivera BuildKit (snabbare builds)
export DOCKER_BUILDKIT=1
docker build .

# Cache mount - cachar paketmanagers
FROM python:3.11
RUN --mount=type=cache,target=/root/.cache/pip \\
    pip install -r requirements.txt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Size Reduction

| Teknik | Besparing |
|--------|-----------|
| Slim base image | 80-90% |
| Multi-stage build | 70-95% |
| --no-cache-dir | 10-20% |
| Clean apt cache | 5-10% |

```dockerfile
# 1. Minimal base image
FROM python:3.11-slim

# 2. Ta bort cache
RUN pip install --no-cache-dir -r requirements.txt

# 3. Städa apt cache
RUN apt-get update && \\
    apt-get install -y curl && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Analysera image-storlek

| Verktyg | Användning |
|---------|------------|
| `docker history` | Se layers och storlekar |
| `dive` | Interaktiv layer-analys |
| `docker scout` | Säkerhet + storlek |

```bash
# Se layers
docker history myimage

# Dive - interaktiv analys
dive myimage

# Docker Scout
docker scout quickview myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Runtime Performance

| Flag | Beskrivning |
|------|-------------|
| `--cpus=2` | Begränsa CPU |
| `--memory=2g` | Begränsa RAM |
| `--memory-swap=2g` | Disable swap |
| `--cpuset-cpus="0,1"` | CPU pinning |

```bash
# Resource limits
docker run \\
    --cpus=2 \\
    --memory=2g \\
    --memory-swap=2g \\
    myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Layer order** | Saker som ändras sällan först |
| **.dockerignore** | Snabbare COPY |
| **BuildKit** | Parallella, snabbare builds |
| **Analysera** | dive/history för optimering |

**Kom ihåg:**
- **Caching är nyckeln** till snabba builds
- **Minimal base image** = mindre storlek
- **BuildKit** är standard i nya Docker
- **Mät före och efter** optimeringar
""",
        },
        {
            "title": "Docker Debugging & Troubleshooting",
            "slug": "docker-debugging-troubleshooting",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Debugging & Troubleshooting

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Vad du behöver |
|----------|----------------|
| **Container kraschar** | Loggar, exit codes |
| **Nätverksproblem** | Connectivity-test |
| **Performance-issue** | Stats, resource usage |
| **Disk full** | System prune |

Containers kommer att krasha och bete sig konstigt. Du måste kunna:

- **Hitta vad som gick fel** via loggar och inspect
- **Debugga körande containers** utan att störa produktion
- **Hantera vanliga problem** snabbt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container startar inte - Felsökningssteg

```
┌─────────────────────────────────────────────────────────────┐
│              TROUBLESHOOTING FLOW                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. docker logs container     ─── Se felmeddelande         │
│              │                                              │
│              ▼                                              │
│   2. docker inspect            ─── Kolla exit code          │
│              │                                              │
│              ▼                                              │
│   3. docker run -it --entrypoint sh ── Debugga interaktivt  │
│              │                                              │
│              ▼                                              │
│   4. docker events             ─── System-level events      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Exit Codes

| Code | Betydelse | Åtgärd |
|------|-----------|--------|
| `0` | Normal exit | OK |
| `1` | Application error | Kolla loggar |
| `137` | OOM/SIGKILL | Öka memory |
| `143` | SIGTERM | Graceful shutdown |
| `126` | Permission denied | Kolla chmod |
| `127` | Command not found | Kolla CMD/ENTRYPOINT |

```bash
# Steg 1: Kolla loggar
docker logs container_name
docker logs --tail 50 container_name

# Steg 2: Kolla exit code
docker inspect container_name --format='{{.State.ExitCode}}'

# Steg 3: Kör interaktivt för att debugga
docker run -it --entrypoint sh myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Inspektera containers

| Kommando | Beskrivning |
|----------|-------------|
| `docker inspect` | All metadata |
| `docker inspect --format` | Specifikt fält |
| `docker top` | Processer |
| `docker stats` | Resource usage |

```bash
# Full metadata
docker inspect container_name

# Specifik info
docker inspect container_name --format='{{.State.Status}}'
docker inspect container_name --format='{{.NetworkSettings.IPAddress}}'
docker inspect container_name --format='{{json .Config.Env}}'

# Processer i container
docker top container_name

# Resource usage
docker stats container_name
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Debugga körande container

| Kommando | Användning |
|----------|------------|
| `docker exec -it container sh` | Öppna shell |
| `docker exec container cmd` | Kör kommando |
| `docker exec -u 0` | Kör som root |

```bash
# Öppna shell i körande container
docker exec -it container_name sh
docker exec -it container_name bash

# Kör kommando utan shell
docker exec container_name cat /etc/hosts
docker exec container_name env

# Som root (om container kör som non-root)
docker exec -u 0 container_name bash
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Nätverksproblem

| Test | Kommando |
|------|----------|
| Kolla IP | `docker inspect --format='{{.NetworkSettings.IPAddress}}'` |
| DNS lookup | `docker exec container nslookup other` |
| Ping | `docker exec container ping other` |
| HTTP | `docker exec container curl http://other:8080` |

```bash
# Kolla container IP
docker inspect container_name --format='{{.NetworkSettings.IPAddress}}'

# Testa connectivity från container
docker exec container_name ping other_container
docker exec container_name curl http://other_container:8080

# Kolla port mappings
docker port container_name
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Disk/Storage problem

| Kommando | Beskrivning |
|----------|-------------|
| `docker system df` | Disk usage |
| `docker system prune` | Städa allt |
| `docker system prune -a` | + oanvända images |
| `docker volume prune` | Städa volumes |

```bash
# Kolla disk usage
docker system df

# Rensa oanvända resurser
docker system prune        # Containers, networks, images
docker system prune -a     # + alla oanvända images
docker system prune --volumes  # + volumes
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## OOM (Out of Memory)

```bash
# Kolla om container blev OOM-killed
docker inspect container_name --format='{{.State.OOMKilled}}'

# Kolla memory limit vs usage
docker stats container_name --no-stream

# Öka memory limit
docker update --memory=2g container_name
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Permission denied | Fel user/permissions | `--user` eller `chown` |
| Port already in use | Port upptagen | Byt port eller stoppa process |
| No space left | Disk full | `docker system prune -a` |
| Cannot connect to daemon | Docker ej startat | `sudo systemctl start docker` |
| OOMKilled | För lite minne | Öka `--memory` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Loggar först** | `docker logs` är din bästa vän |
| **Exit codes** | Berättar varför container stoppade |
| **exec -it** | Debugga körande containers |
| **system prune** | När disken är full |

**Kom ihåg:**
- **Metodisk felsökning** - loggar -> inspect -> exec
- **Exit codes** har betydelse - lär dig dem
- **docker events** visar system-level händelser
- **Städa regelbundet** med prune
""",
        },
        {
            "title": "Docker with CI/CD",
            "slug": "docker-with-cicd",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker with CI/CD

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Docker i CI/CD |
|----------|----------------|
| **Automatisering** | Bygg vid varje push |
| **Konsistens** | Samma image i alla miljöer |
| **Spårbarhet** | SHA-tagging |
| **Säkerhet** | Scanning i pipeline |

Docker och CI/CD hör ihop. Du måste kunna:

- **Bygga och testa** images automatiskt
- **Pusha till registry** från pipeline
- **Deploya** nya versioner automatiskt

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitHub Actions

```yaml
# .github/workflows/docker.yml
name: Docker Build & Push

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: |
            username/myapp:latest
            username/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

variables:
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG

test:
  stage: test
  image: $IMAGE_TAG
  script:
    - npm test

deploy:
  stage: deploy
  script:
    - docker pull $IMAGE_TAG
    - docker stop myapp || true
    - docker rm myapp || true
    - docker run -d --name myapp -p 80:8000 $IMAGE_TAG
  only:
    - main
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Smart Tagging Strategy

| Tag-typ | Exempel | Användning |
|---------|---------|------------|
| Branch | `myapp:main` | Development |
| PR | `myapp:pr-123` | Review |
| Semver | `myapp:1.2.3` | Release |
| SHA | `myapp:abc1234` | Spårbarhet |

```yaml
# GitHub Actions - multiple tags
- name: Docker meta
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: username/myapp
    tags: |
      type=ref,event=branch
      type=ref,event=pr
      type=semver,pattern={{version}}
      type=sha,prefix=
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Layer Caching i CI

| Cache-typ | Beskrivning | Hastighet |
|-----------|-------------|-----------|
| `type=gha` | GitHub Actions cache | Snabb |
| `type=registry` | Registry-based | Persistent |
| `type=local` | Local directory | Snabbast |

```yaml
# GitHub Actions med cache
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: myapp:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Security Scanning i Pipeline

```yaml
# GitHub Actions - Trivy scanning
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: myapp:${{ github.sha }}
    format: 'sarif'
    output: 'trivy-results.sarif'

- name: Upload Trivy scan results
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: 'trivy-results.sarif'
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Multi-platform Builds i CI

```yaml
- name: Set up QEMU
  uses: docker/setup-qemu-action@v3

- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    platforms: linux/amd64,linux/arm64
    push: true
    tags: myapp:latest
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Deploy med Docker Compose

```yaml
deploy:
  stage: deploy
  script:
    - ssh user@server "
        cd /app &&
        docker compose pull &&
        docker compose up -d --remove-orphans
      "
  environment:
    name: production
  only:
    - main
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **SHA-tagging** | Spårbarhet till commit |
| **Layer cache** | Snabbare builds |
| **Security scanning** | Sårbarheter före deploy |
| **Multi-platform** | ARM/AMD64 support |

**Kom ihåg:**
- **Automatisera allt** - bygg, test, scan, deploy
- **Tagga med SHA** för spårbarhet
- **Scanna images** innan de når produktion
- **Cache layers** för snabbare CI/CD
""",
        },
        {
            "title": "Docker Swarm Basics",
            "slug": "docker-swarm-basics",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Swarm Basics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt for DevOps?

| Scenario | Swarm ger dig |
|----------|---------------|
| **Multi-host** | Containers over flera servrar |
| **Skalning** | Enkel replikering |
| **HA** | Automatisk failover |
| **Enkel setup** | Inbyggt i Docker |

Swarm är Dockers inbyggda orkestrering:
- **Köra containers över flera hosts**
- **Förstå orkestreringskoncept** innan Kubernetes
- **Hantera enklare produktionsmiljöer**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Swarm Arkitektur

```
┌─────────────────────────────────────────────────────────┐
│                     SWARM CLUSTER                        │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   MANAGER   │  │   MANAGER   │  │   MANAGER   │      │
│  │   (Leader)  │  │  (Standby)  │  │  (Standby)  │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│         │                                                │
│         ▼ Scheduling & State                            │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   WORKER    │  │   WORKER    │  │   WORKER    │      │
│  │  [Task 1]   │  │  [Task 2]   │  │  [Task 3]   │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────┘
```

| Komponent | Roll |
|-----------|------|
| **Manager** | Hanterar klustret, schemalägger tasks |
| **Worker** | Kör containers/tasks |
| **Service** | Definierar applikationen |
| **Task** | En container-instans |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Initiera Swarm

| Kommando | Beskrivning |
|----------|-------------|
| `docker swarm init` | Initiera manager |
| `docker swarm join-token worker` | Visa join token |
| `docker swarm join` | Anslut worker |
| `docker node ls` | Lista alla noder |

```bash
# Gör denna maskin till manager
docker swarm init

# Visa join token för workers
docker swarm join-token worker

# Lägg till worker (kör på worker-maskinen)
docker swarm join --token SWMTKN-xxx manager-ip:2377

# Lista noder
docker node ls
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Services vs Containers

| Aspekt | `docker run` | `docker service` |
|--------|--------------|------------------|
| Scope | En container | Flera replikor |
| Scaling | Manuellt | `scale=N` |
| Failover | Ingen | Automatisk |
| Nätverk | Manuellt | Overlay |

```bash
# Skapa en service (istället för docker run)
docker service create --name web --replicas 3 -p 8080:80 nginx

# Lista services
docker service ls

# Se tasks (containers) för en service
docker service ps web

# Skala service
docker service scale web=5

# Uppdatera service
docker service update --image nginx:1.25 web

# Ta bort service
docker service rm web
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stacks (Swarm + Compose)

```yaml
# docker-compose.yml (för Swarm)
version: "3.8"
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

| Stack-kommando | Beskrivning |
|----------------|-------------|
| `docker stack deploy` | Deploya stack |
| `docker stack ls` | Lista stacks |
| `docker stack services` | Se services |
| `docker stack rm` | Ta bort stack |

```bash
# Deploya stack
docker stack deploy -c docker-compose.yml mystack

# Lista stacks
docker stack ls

# Se services i stack
docker stack services mystack

# Ta bort stack
docker stack rm mystack
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Rolling Updates

```
Update Process:
┌─────────────────────────────────────────────────────┐
│  Service: web (replicas=3)                          │
│                                                      │
│  [v1.0] ─────> [v1.1] (update 1/3)                 │
│  [v1.0]        [v1.0] (waiting...)                  │
│  [v1.0]        [v1.0] (waiting...)                  │
│                                                      │
│  --update-parallelism 1                             │
│  --update-delay 10s                                 │
└─────────────────────────────────────────────────────┘
```

```bash
# Uppdatera image med rolling update
docker service update \\
    --image nginx:1.25 \\
    --update-parallelism 1 \\
    --update-delay 10s \\
    web

# Rollback om något går fel
docker service rollback web
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Swarm** | Enklare än K8s, inbyggt |
| **Services** | Ersätter containers |
| **Stacks** | Compose för Swarm |
| **Rolling updates** | Zero-downtime deploys |

**Kom ihåg:**
- **Swarm är enklare** än Kubernetes men mindre kraftfullt
- **Services** ersätter containers för skalning
- **Stacks** är Compose-filer för Swarm
- Bra för **mindre produktionsmiljöer**
""",
        },
        {
            "title": "Docker Best Practices Summary",
            "slug": "docker-best-practices-summary",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 75,
            "content": """# Docker Best Practices Summary

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Kategori | Bra praxis = |
|----------|--------------|
| **Dockerfile** | Mindre, säkrare images |
| **Security** | Inga sårbarheter |
| **Production** | Stabil drift |
| **Team** | Konsistens över tid |

En sammanfattning av alla best practices för professionella Dockerfiles och produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Dockerfile Best Practices

| Regel | Varför |
|-------|--------|
| Specifik base tag | Reproducerbarhet |
| Multi-stage builds | Mindre image |
| Minimera layers | Snabbare pulls |
| Cache-ordning | Snabbare builds |
| Non-root user | Säkerhet |
| HEALTHCHECK | Monitoring |
| COPY > ADD | Tydlighet |
| Labels | Metadata |

```dockerfile
# 1. Använd specifik base image tag
FROM python:3.11.7-slim  # Inte python:latest

# 2. Använd multi-stage builds
FROM node:18 AS builder
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# 3. Minimera layers
RUN apt-get update && \\
    apt-get install -y curl && \\
    rm -rf /var/lib/apt/lists/*

# 4. Ordna för cache
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 5. Kör som non-root
RUN useradd --create-home appuser
USER appuser

# 6. Lägg till healthcheck
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health

# 7. Använd COPY istället för ADD
COPY app.py /app/

# 8. Sätt labels
LABEL maintainer="team@example.com"
LABEL version="1.0"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Best Practices

| Regel | Exempel |
|-------|---------|
| Slim/alpine | `python:3.11-slim` |
| Scanna CVE | `docker scout cves` |
| Tag med version+SHA | `myapp:1.2.3-abc123` |
| Signera images | `DOCKER_CONTENT_TRUST=1` |
| Undvik latest | Specifik tag alltid |

```bash
# 1. Använd slim/alpine varianter
FROM python:3.11-slim   # Istället för python:3.11

# 2. Scanna för vulnerabilities
docker scout cves myimage
trivy image myimage

# 3. Tagga med version och SHA
myimage:1.2.3
myimage:abc123f

# 4. Undvik latest i produktion
# Aldrig: docker pull myimage:latest
# Alltid: docker pull myimage:1.2.3

# 5. Signera images (Docker Content Trust)
export DOCKER_CONTENT_TRUST=1
docker push myimage:1.2.3
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container Best Practices

| Regel | Kommando |
|-------|----------|
| Resource limits | `--memory=512m --cpus=0.5` |
| Restart policy | `--restart unless-stopped` |
| Minimal ports | `-p 127.0.0.1:8080:8080` |
| Read-only | `--read-only --tmpfs /tmp` |
| Drop caps | `--cap-drop ALL` |
| Isolerat nätverk | `--network internal` |

```bash
# 1. Sätt resource limits
docker run --memory=512m --cpus=0.5 myimage

# 2. Använd restart policies
docker run --restart unless-stopped myimage

# 3. Exponera bara nödvändiga portar
docker run -p 127.0.0.1:8080:8080 myimage

# 4. Använd read-only filesystem
docker run --read-only --tmpfs /tmp myimage

# 5. Drop capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myimage

# 6. Isolera i nätverk
docker network create --internal backend
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker Compose Best Practices

```yaml
services:
  api:
    image: myapi:${VERSION}  # Använd variabler
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 512M
    healthcheck:
      test: curl -f http://localhost:8000/health
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
    secrets:
      - db_password  # Secrets, inte env vars

secrets:
  db_password:
    external: true
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Checklista

| Dockerfile | Security | Produktion |
|------------|----------|------------|
| Specifik base tag | Image scanning | Restart policy |
| Multi-stage build | No secrets i image | Centraliserad logging |
| Non-root user | Resource limits | Health monitoring |
| Healthcheck | Read-only filesystem | Backup strategy |
| .dockerignore | Dropped capabilities | - |
| Minimala layers | - | - |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Säkerhet först** | Non-root, minimal, scanning |
| **Optimera storlek** | Multi-stage, slim |
| **Optimera cache** | Ordna Dockerfile smart |
| **Checklista** | Följ före deploy |

**Kom ihåg:**
- **Optimera för säkerhet** - non-root, minimal image, scanning
- **Optimera för storlek** - multi-stage, slim images
- **Optimera för cache** - ordna Dockerfile smart
- **Följ checklistan** innan deploy till produktion
""",
        },
        {
            "title": "Docker Development Workflow",
            "slug": "docker-development-workflow",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 70,
            "content": """# Docker Development Workflow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Docker Dev ger dig |
|----------|---------------------|
| **Hot reload** | Ändringar syns direkt |
| **Debugging** | VS Code attach |
| **Miljölikhet** | Dev = Prod |
| **Isolering** | Inga konflikter |

Docker förändrar hur du utvecklar:
- **Sätter upp lokal utvecklingsmiljö** med Docker
- **Hot reload och debugging** i containers
- **Skillnaden mellan dev och prod** konfiguration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Development vs Production

```
Dev Environment:
┌─────────────────────────────────────────────────────┐
│  docker-compose.yml (bas)                           │
│  + docker-compose.override.yml (dev, auto-laddas)  │
│                                                      │
│  - Volume mounts (hot reload)                       │
│  - Debug ports exponerade                           │
│  - DEBUG=true                                       │
└─────────────────────────────────────────────────────┘

Prod Environment:
┌─────────────────────────────────────────────────────┐
│  docker-compose.yml (bas)                           │
│  + docker-compose.prod.yml (explicit)               │
│                                                      │
│  - Built image från registry                        │
│  - Restart policies                                 │
│  - Resource limits                                  │
└─────────────────────────────────────────────────────┘
```

| Fil | Syfte | Automatisk? |
|-----|-------|-------------|
| `docker-compose.yml` | Gemensam bas | Ja |
| `docker-compose.override.yml` | Dev-specifikt | Ja |
| `docker-compose.prod.yml` | Prod-specifikt | Nej (-f) |

```yaml
# docker-compose.yml (bas)
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://db:5432/app

# docker-compose.override.yml (dev - laddas automatiskt)
services:
  api:
    build:
      target: development
    volumes:
      - .:/app           # Hot reload
      - /app/node_modules # Preserve node_modules
    environment:
      - DEBUG=true
    ports:
      - "8000:8000"
      - "9229:9229"      # Debug port

# docker-compose.prod.yml (prod)
services:
  api:
    image: myregistry/api:${VERSION}
    restart: unless-stopped
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hot Reload Setup

```dockerfile
# Dockerfile med dev target
FROM node:18-slim AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Development
FROM base AS development
RUN npm install -g nodemon
CMD ["nodemon", "src/index.js"]

# Production
FROM base AS production
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Användbart dev-kommandon

| Kommando | Beskrivning |
|----------|-------------|
| `docker compose up` | Starta dev |
| `docker compose up --build` | Bygg om + starta |
| `docker compose exec api sh` | Shell i container |
| `docker compose logs -f api` | Följa loggar |
| `docker compose restart api` | Starta om service |

```bash
# Starta dev environment
docker compose up

# Bygg om efter Dockerfile-ändringar
docker compose up --build

# Kör kommando i container
docker compose exec api npm test
docker compose exec api sh

# Se loggar
docker compose logs -f api

# Starta om en service
docker compose restart api
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Debugging i Container

```yaml
# docker-compose.override.yml
services:
  api:
    ports:
      - "9229:9229"  # Node.js debug port
    command: ["node", "--inspect=0.0.0.0:9229", "src/index.js"]
```

```json
// VS Code launch.json
{
  "type": "node",
  "request": "attach",
  "name": "Docker: Attach",
  "port": 9229,
  "address": "localhost",
  "localRoot": "${workspaceFolder}",
  "remoteRoot": "/app"
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Database i Development

```yaml
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=devpassword
      - POSTGRES_DB=app
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # Seed data
    ports:
      - "5432:5432"  # Tillgänglig från host för DB-klient

volumes:
  pgdata:
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Makefile för vanliga tasks

```makefile
# Makefile
.PHONY: dev prod test shell logs

dev:
	docker compose up

prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

test:
	docker compose exec api npm test

shell:
	docker compose exec api sh

logs:
	docker compose logs -f

clean:
	docker compose down -v
	docker system prune -f
```

| Make target | Kommando |
|-------------|----------|
| `make dev` | Starta development |
| `make prod` | Starta production |
| `make test` | Kör tester |
| `make shell` | Shell i container |
| `make logs` | Följa loggar |
| `make clean` | Rensa allt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Override files** | Miljöspecifik config |
| **Volume mounts** | Hot reload |
| **Debug ports** | VS Code attach |
| **Makefile** | Vanliga kommandon |

**Kom ihåg:**
- **Override files** för miljöspecifik config
- **Volume mounts** för hot reload
- **Expose debug ports** för VS Code attach
- **Makefile** för vanliga kommandon
""",
        },
        {
            "title": "Docker Ecosystem & Tools",
            "slug": "docker-ecosystem-tools",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 65,
            "content": """# Docker Ecosystem & Tools

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Kategori | Varför viktigt |
|----------|----------------|
| **Verktyg** | Kompletterar Docker |
| **Alternativ** | Podman, containerd |
| **Scanning** | Säkerhet i pipeline |
| **Orchestration** | Produktion i skala |

Docker är mer än bara Docker Engine:
- **Verktyg som kompletterar Docker**
- **Alternativ och relaterade teknologier**
- **Var Docker passar in i DevOps-landskapet**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker Desktop

| Inkluderar | Beskrivning |
|------------|-------------|
| Docker Engine | Container runtime |
| Docker Compose | Multi-container |
| Docker Scout | Security scanning |
| Kubernetes | Single-node K8s |
| Extensions | Plugins |

```bash
# Bra för lokal utveckling på Mac/Windows
# I produktion: använd Docker Engine direkt på Linux
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Podman (Docker-alternativ)

| Fördel | Beskrivning |
|--------|-------------|
| Daemonless | Ingen bakgrundsprocess |
| Rootless | Säkrare by default |
| Kompatibel | Samma CLI som Docker |

```bash
# Podman - daemonless, rootless containers
# Kompatibel med Docker CLI

podman run nginx           # Samma syntax som docker
podman build -t myimage .  # Samma Dockerfiles
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Scanning Tools

| Verktyg | Typ | Användning |
|---------|-----|------------|
| Docker Scout | Inbyggt | `docker scout cves` |
| Trivy | Open source | `trivy image` |
| Snyk | SaaS | `snyk container test` |
| Grype | Open source | `grype myimage` |

```bash
# Docker Scout (inbyggt)
docker scout cves myimage
docker scout recommendations myimage

# Trivy (open source)
trivy image myimage

# Snyk
snyk container test myimage

# Grype
grype myimage
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Container Registries

| Typ | Exempel |
|-----|---------|
| **Public** | Docker Hub, GHCR, Quay.io |
| **Cloud** | AWS ECR, GCR, ACR |
| **Self-hosted** | Harbor, GitLab, Nexus |

```
Registry Landscape:
┌─────────────────────────────────────────────────────┐
│  PUBLIC          │  CLOUD          │  SELF-HOSTED   │
├──────────────────┼─────────────────┼────────────────┤
│  docker.io       │  AWS ECR        │  Harbor        │
│  ghcr.io         │  Google GCR     │  GitLab CR     │
│  quay.io         │  Azure ACR      │  Nexus         │
└─────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Image Analysis Tools

| Verktyg | Syfte |
|---------|-------|
| Dive | Analysera layers interaktivt |
| docker history | Visa image layers |
| Skopeo | Kopiera mellan registries |

```bash
# Dive - analysera layers
dive myimage

# Docker History
docker history myimage

# Skopeo - kopiera mellan registries
skopeo copy docker://docker.io/nginx docker://myregistry/nginx
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Build Tools

| Verktyg | Användning |
|---------|------------|
| BuildKit | Standard i nya Docker |
| Buildx | Multi-platform |
| Kaniko | K8s utan daemon |
| Buildah | OCI image builder |

```bash
# BuildKit (standard i nya Docker)
DOCKER_BUILDKIT=1 docker build .

# Buildx (multi-platform)
docker buildx build --platform linux/amd64,linux/arm64 .

# Kaniko (build i Kubernetes utan Docker daemon)
# Används i CI/CD pipelines

# Buildah (OCI image builder)
buildah build-using-dockerfile -t myimage .
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Orchestration

| Plattform | Beskrivning |
|-----------|-------------|
| Docker Swarm | Inbyggt, enkelt |
| Kubernetes | Standard, kraftfullt |
| Nomad | HashiCorp alternativ |
| ECS | AWS managed |

```bash
# Docker Swarm - inbyggt i Docker
docker swarm init

# Kubernetes - standard för produktion
kubectl apply -f deployment.yaml

# Nomad - HashiCorp alternativ
nomad job run myapp.nomad

# ECS - AWS managed containers
aws ecs create-service ...
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Monitoring & Logging

| Stack | Syfte |
|-------|-------|
| Prometheus + Grafana | Metrics & visualization |
| ELK | Centraliserad logging |
| Datadog/New Relic | Managed monitoring |
| cAdvisor | Container resource |

```
Monitoring Stack:
┌─────────────────────────────────────────────────────┐
│  METRICS         │  LOGGING        │  APM           │
├──────────────────┼─────────────────┼────────────────┤
│  Prometheus      │  Elasticsearch  │  Datadog       │
│  Grafana         │  Logstash       │  New Relic     │
│  cAdvisor        │  Kibana         │  Jaeger        │
└─────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **Scanning** | Scout/Trivy för CVE |
| **Buildx** | Multi-platform |
| **Kubernetes** | Standard i skala |
| **Harbor** | Self-hosted registry |

**Kom ihåg:**
- **Docker Scout/Trivy** för security scanning
- **Buildx** för multi-platform builds
- **Kubernetes** är standard för större deployments
- **Harbor** för self-hosted registry
""",
        },
        {
            "title": "Docker Certification Path",
            "slug": "docker-certification-path",
            "difficulty": "easy",
            "estimated_minutes": 30,
            "xp_reward": 60,
            "content": """# Docker Certification Path

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varför viktigt för DevOps?

| Scenario | Certifiering ger dig |
|----------|----------------------|
| **CV** | Validerad kunskap |
| **Karriär** | Konkurrenskraft |
| **Kunskap** | Strukturerad inlärning |
| **Företag** | Kvalitetsstämpel |

Docker-certifieringar validerar dina kunskaper:
- **Vilka certifieringar som finns**
- **Vad de täcker**
- **Hur du förbereder dig**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Docker Certified Associate (DCA)

| Område | Procent | Ämnen |
|--------|---------|-------|
| Orchestration | 25% | Swarm, services, stacks |
| Image Management | 20% | Dockerfile, multi-stage, registry |
| Installation | 15% | Engine, storage, logging drivers |
| Networking | 15% | Drivers, DNS, load balancing |
| Security | 15% | Image security, secrets, trust |
| Storage | 10% | Volume types, backup |

```
DCA Exam Overview:
┌─────────────────────────────────────────────────────┐
│  Orchestration (25%)                                │
│  ████████████████████████                           │
├─────────────────────────────────────────────────────┤
│  Image Management (20%)                             │
│  ████████████████████                               │
├─────────────────────────────────────────────────────┤
│  Installation (15%)                                 │
│  ███████████████                                    │
├─────────────────────────────────────────────────────┤
│  Networking (15%)                                   │
│  ███████████████                                    │
├─────────────────────────────────────────────────────┤
│  Security (15%)                                     │
│  ███████████████                                    │
├─────────────────────────────────────────────────────┤
│  Storage (10%)                                      │
│  ██████████                                         │
└─────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Förberedelse

| Metod | Resurs |
|-------|--------|
| Hands-on | Bygg egna images, multi-container, Swarm |
| Dokumentation | docs.docker.com |
| Practice exams | Whizlabs, online tests |
| Labs | Play with Docker, Katacoda |

```bash
# 1. Hands-on erfarenhet (viktigast!)
# - Bygg egna images
# - Sätt upp multi-container apps
# - Deploya till Swarm

# 2. Officiell dokumentation
# docs.docker.com

# 3. Practice exams
# - Whizlabs
# - Practice tests online

# 4. Labs
# - Play with Docker (labs.play-with-docker.com)
# - Katacoda scenarios
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Relaterade Certifieringar

| Certifiering | Fokus | Nivå |
|--------------|-------|------|
| CKA | Kubernetes Admin | Intermediate |
| CKAD | Kubernetes Dev | Intermediate |
| CKS | Kubernetes Security | Advanced |
| AWS DevOps | AWS + Containers | Advanced |
| Azure DevOps | Azure + Containers | Advanced |

```
Certification Path:
┌─────────────────────────────────────────────────────┐
│                                                      │
│  Docker Certified Associate (DCA)                   │
│              │                                       │
│              ▼                                       │
│  ┌─────────────────────────────────────────┐        │
│  │  Kubernetes Path                         │        │
│  │  CKA ──> CKAD ──> CKS                   │        │
│  └─────────────────────────────────────────┘        │
│              │                                       │
│              ▼                                       │
│  Cloud Certifications (AWS/Azure/GCP DevOps)        │
│                                                      │
└─────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Study Checklist

| Ämne | Status |
|------|--------|
| Dockerfile syntax och best practices | |
| Docker Compose för multi-container apps | |
| Docker networking (bridge, host, overlay) | |
| Docker volumes och storage | |
| Docker Swarm basics | |
| Image security och scanning | |
| Registry operations | |
| Logging och monitoring | |
| Troubleshooting containers | |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Punkt | Förklaring |
|-------|------------|
| **DCA** | Bra första certifiering |
| **Hands-on** | Viktigast för inlärning |
| **Kubernetes** | Naturligt nästa steg |
| **Labs** | Play with Docker |

**Kom ihåg:**
- **DCA** är bra första certifiering
- **Hands-on experience** är viktigast
- **Kubernetes-cert** är naturligt nästa steg
- Öva med **Play with Docker** labs
""",
        },
    ],
}
