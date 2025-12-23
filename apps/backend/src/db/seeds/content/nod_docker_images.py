"""
NOD 3.2: Docker Images & Containers
===================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 3: DEVOPS
"""

DOCKER_IMAGES_NODE = {
    "title": "Docker - Images & Containers",
    "slug": "docker-images-containers",
    "description": "Images vs containers, Dockerfile, layers, caching och multi-stage builds.",
    "difficulty": "medium",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "order_index": 2,
    "content": r"""# Docker - Images & Containers

> **TL;DR:** Image = recept (read-only), Container = tillagad rätt (körande instans). Ordningen i Dockerfile avgör caching - **saker som ändras sällan först!**

---

## 📖 TEORI: Image vs Container

### Grundläggande skillnad

| Aspekt | Image | Container |
|--------|-------|-----------|
| Typ | Mall/ritning | Körande instans |
| Läsbarhet | Read-only | Read-write layer ovanpå |
| Delbarhet | Kan delas via registry | Unik per körning |
| Lagring | Registry (Docker Hub) | Lokalt på host |
| Livscykel | Permanent | Skapas och förstörs |

### Analogi

```
┌─────────────────────────────────────────────────┐
│   Image = Receptet                              │
│   Container = Den tillagade rätten              │
│                                                 │
│   Samma recept kan göra MÅNGA rätter!           │
│   docker run nginx → ny container varje gång   │
└─────────────────────────────────────────────────┘
```

### Visualisering

```
       Image (read-only)
┌─────────────────────────┐
│     Layer 3: App        │
├─────────────────────────┤
│     Layer 2: Deps       │
├─────────────────────────┤
│     Layer 1: Base OS    │
└─────────────────────────┘
            │
            │ docker run
            ▼
       Container
┌─────────────────────────┐
│  Container Layer (R/W)  │  ← Ändringar här
├─────────────────────────┤
│     Layer 3: App        │
├─────────────────────────┤
│     Layer 2: Deps       │
├─────────────────────────┤
│     Layer 1: Base OS    │
└─────────────────────────┘
```

---

## 📖 Image-namn och taggar

### Namnstruktur

```
[registry/]repository:tag

Exempel:
docker.io/library/python:3.12-alpine
└───┬────┘ └──┬───┘ └──┬──┘ └───┬────┘
 registry  namespace  image    tag
```

### Vanliga mönster

```bash
# Officiella images (library/)
python              # = docker.io/library/python:latest
python:3.12         # Specifik version
python:3.12-alpine  # Alpine-variant (minimal)
python:3.12-slim    # Slim-variant (utan build-tools)

# Användares images
myuser/myapp:1.0    # = docker.io/myuser/myapp:1.0

# Privat registry
myregistry.com/myapp:latest
```

### ⚠️ VIKTIGT om :latest

```bash
# Om ingen tagg anges = :latest
docker run python        # = python:latest
docker run python:3.12   # ALLTID specifik version i produktion!
```

> "Använd **aldrig** :latest i produktion - det kan ändras när som helst!"

---

## 📖 Hantera images

### Lista och hämta

```bash
# Lista lokala images
docker images
docker image ls

# Detaljerad info
docker image inspect nginx

# Sök på Docker Hub
docker search python

# Ladda ner image
docker pull nginx
docker pull nginx:1.25-alpine

# Visa layers
docker history nginx
```

### Ta bort

```bash
# Ta bort specifik image
docker rmi nginx
docker rmi nginx:1.25

# Ta bort med ID
docker rmi abc123

# Ta bort alla oanvända
docker image prune

# Ta bort ALLA oanvända (även taggade)
docker image prune -a
```

### Registry-operationer

```bash
# Logga in på Docker Hub
docker login

# Tagga för push
docker tag minapp:1.0 myuser/minapp:1.0

# Pusha till registry
docker push myuser/minapp:1.0

# Logga ut
docker logout
```

---

## 📖 Dockerfile - Bygg egen image

### Grundläggande Dockerfile

```dockerfile
# 1. Basimage (MÅSTE vara först)
FROM ubuntu:22.04

# 2. Metadata
LABEL maintainer="student@example.com"
LABEL version="1.0"

# 3. Kör kommandon (varje RUN = nytt layer)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 4. Sätt arbetskatalog
WORKDIR /app

# 5. Kopiera dependencies först (caching!)
COPY requirements.txt .

# 6. Installera dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# 7. Kopiera applikationskod (ändras ofta)
COPY app.py .

# 8. Exponera port (dokumentation)
EXPOSE 8080

# 9. Miljövariabler
ENV APP_ENV=production

# 10. Startkommando
CMD ["python3", "app.py"]
```

### Alla Dockerfile-instruktioner

| Instruktion | Beskrivning | Exempel |
|-------------|-------------|---------|
| FROM | Basimage (MÅSTE vara först) | FROM python:3.12 |
| LABEL | Metadata | LABEL version="1.0" |
| RUN | Kör kommando vid build | RUN apt-get update |
| COPY | Kopiera filer från host | COPY app.py /app/ |
| ADD | Som COPY + extrahera/URL | ADD app.tar.gz /app/ |
| WORKDIR | Sätt arbetskatalog | WORKDIR /app |
| ENV | Sätt miljövariabel | ENV DEBUG=false |
| EXPOSE | Dokumentera port | EXPOSE 8080 |
| CMD | Default-kommando | CMD ["python", "app.py"] |
| ENTRYPOINT | Fast kommando | ENTRYPOINT ["python"] |
| USER | Byt användare | USER appuser |
| VOLUME | Definiera mount-punkt | VOLUME /data |
| ARG | Build-time variabler | ARG VERSION=1.0 |

### CMD vs ENTRYPOINT

```dockerfile
# CMD - kan ersättas vid docker run
CMD ["python", "app.py"]
# docker run myapp              → python app.py
# docker run myapp bash         → bash (ersätter CMD)

# ENTRYPOINT - kan INTE ersättas enkelt
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run myapp              → python app.py
# docker run myapp other.py     → python other.py
```

---

## 📖 Bygga image

### Grundläggande build

```bash
# Bygg från Dockerfile i nuvarande katalog
docker build -t minapp:1.0 .

# -t = tag (namn:version)
# . = build context (nuvarande katalog)
```

### Fler build-alternativ

```bash
# Annan Dockerfile
docker build -f Dockerfile.prod -t minapp:prod .

# Build med argument
docker build --build-arg VERSION=2.0 -t minapp:2.0 .

# Utan cache (tvinga ombygge)
docker build --no-cache -t minapp:1.0 .

# Visa build-historik
docker history minapp:1.0
```

---

## 📖 Layers och Caching (KRITISKT!)

### Varje instruktion = ett layer

```dockerfile
FROM ubuntu:22.04          # Layer 1
RUN apt-get update         # Layer 2
RUN apt-get install vim    # Layer 3
COPY app.py /app/          # Layer 4
```

### Cache-invalidering

När ett layer ändras → **alla efterföljande layers måste byggas om!**

### ❌ DÅLIGT - Cache invalideras vid kodändring

```dockerfile
FROM python:3.12
COPY . /app                    # ← Ändras vid varje kodändring
WORKDIR /app
RUN pip install -r requirements.txt  # ← Måste köras om VARJE GÅNG!
CMD ["python", "app.py"]
```

### ✅ BRA - Dependencies cachas separat

```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .        # ← Ändras sällan
RUN pip install -r requirements.txt  # ← Cachas!
COPY . .                       # ← Bara detta körs om vid kodändring
CMD ["python", "app.py"]
```

### Gyllene regeln

```
┌─────────────────────────────────────────────────┐
│   SAKER SOM ÄNDRAS SÄLLAN FÖRST                │
│   SAKER SOM ÄNDRAS OFTA SIST                   │
│                                                 │
│   1. FROM (basimage)                           │
│   2. RUN apt-get install (system deps)         │
│   3. COPY requirements.txt + pip install       │
│   4. COPY källkod (ändras ofta)                │
│   5. CMD                                        │
└─────────────────────────────────────────────────┘
```

---

## 📖 Multi-stage builds

### Problemet

```dockerfile
# Build-image innehåller allt (gcc, make, headers...)
FROM golang:1.21
WORKDIR /app
COPY . .
RUN go build -o myapp
CMD ["./myapp"]
# Resultat: 1.2 GB image med massa onödigt!
```

### Lösningen: Multi-stage

```dockerfile
# Stage 1: BUILD
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Stage 2: RUNTIME (minimal!)
FROM alpine:latest
COPY --from=builder /app/myapp /usr/local/bin/
CMD ["myapp"]
# Resultat: ~15 MB image!
```

### Fördelarna

> "Build-tools behövs **inte** i runtime. Multi-stage ger **minimal** slutimage!"

| Utan multi-stage | Med multi-stage |
|------------------|-----------------|
| 1.2 GB | 15 MB |
| Innehåller gcc, make, etc | Bara binären |
| Säkerhetsrisk | Minimal attack surface |

### Python-exempel med multi-stage

```dockerfile
# Stage 1: Build dependencies
FROM python:3.12-slim AS builder
WORKDIR /app
RUN pip install --user --no-cache-dir \
    flask \
    gunicorn \
    requests

# Stage 2: Runtime
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

---

## 📖 Interagera med körande container

### Kör kommandon

```bash
# Öppna shell i körande container
docker exec -it container_name bash
docker exec -it container_name sh    # Om bash saknas

# Kör specifikt kommando
docker exec container_name ls /app
docker exec container_name cat /etc/hosts

# Som annan användare
docker exec -u root container_name whoami
```

### Loggar

```bash
# Visa alla loggar
docker logs container_name

# Följ loggar i realtid (-f = follow)
docker logs -f container_name

# Senaste N rader
docker logs --tail 100 container_name

# Med tidsstämplar
docker logs -t container_name

# Sedan viss tid
docker logs --since 1h container_name
```

### Inspektera

```bash
# Detaljerad container-info (JSON)
docker inspect container_name

# Visa processer
docker top container_name

# Resursanvändning (live)
docker stats
docker stats container_name
```

### Kopiera filer

```bash
# Från container till host
docker cp container:/app/data.txt ./local/

# Från host till container
docker cp ./config.json container:/app/

# Hel katalog
docker cp container:/var/log/ ./logs/
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Bygg Python-app

**app.py:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt:**
```
flask==3.0.0
```

**Dockerfile:**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Dependencies först (caching!)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kod sist
COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

**Bygga och köra:**
```bash
# Bygg
docker build -t myflask:1.0 .

# Kör
docker run -d --name flask -p 5000:5000 myflask:1.0

# Testa
curl localhost:5000

# Loggar
docker logs flask
```

### Exempel 2: Multi-stage Node.js

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Stage 2: Runtime
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
```

### Exempel 3: Inspektera och debugga

```bash
# Starta testcontainer
docker run -d --name debug nginx

# Inspektera
docker inspect debug | grep -i ipaddress
docker exec debug cat /etc/nginx/nginx.conf
docker exec -it debug bash

# Inuti containern:
apt-get update && apt-get install -y curl
curl localhost
exit

# Loggar
docker logs debug
docker logs -f debug

# Stats
docker stats debug

# Städa
docker rm -f debug
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Image vs Container? | Image = recept (read-only), Container = körande instans |
| 2 | FROM i Dockerfile? | Anger basimage (MÅSTE vara först) |
| 3 | RUN i Dockerfile? | Kör kommando vid build (skapar layer) |
| 4 | COPY vs ADD? | ADD kan extrahera tar och hämta URL |
| 5 | CMD vs ENTRYPOINT? | CMD kan ersättas, ENTRYPOINT är fast |
| 6 | docker build -t gör? | Bygger image med tag (namn:version) |
| 7 | Varför COPY requirements.txt först? | För att cacha pip install |
| 8 | Multi-stage build fördel? | Minimal slutimage utan build-tools |
| 9 | docker logs -f gör? | Följer loggar i realtid |
| 10 | EXPOSE i Dockerfile? | Dokumenterar port (öppnar INTE) |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är skillnaden mellan image och container?**
- A) Ingen skillnad
- B) Image är körande, container är mall
- C) Image är mall (read-only), container är körande instans ✅
- D) Container lagras i registry

**2. Vilken instruktion MÅSTE vara först i Dockerfile?**
- A) RUN
- B) FROM ✅
- C) WORKDIR
- D) COPY

**3. Varför ska requirements.txt kopieras FÖRE resten av koden?**
- A) Det går snabbare
- B) För att pip install ska cachas ✅
- C) Det är syntax-krav
- D) Annars funkar det inte

**4. Vad gör multi-stage builds?**
- A) Bygger snabbare
- B) Ger minimal slutimage utan build-tools ✅
- C) Kör flera containers
- D) Komprimerar images

**5. Vad gör COPY --from=builder i multi-stage?**
- A) Kopierar från host
- B) Kopierar från tidigare stage ✅
- C) Kopierar från registry
- D) Kopierar till builder

**6. Vilken flagga följer loggar i realtid?**
- A) docker logs -l
- B) docker logs -f ✅
- C) docker logs --follow
- D) docker logs -r

**7. Vad gör EXPOSE i Dockerfile?**
- A) Öppnar porten
- B) Blockerar porten
- C) Dokumenterar vilken port appen använder ✅
- D) Mappar till host

**8. Vad händer när ett layer ändras?**
- A) Bara det layret byggs om
- B) Alla efterföljande layers måste byggas om ✅
- C) Ingenting
- D) Hela imagen cachas

**9. Vad är :latest-taggens problem?**
- A) Den är långsam
- B) Den kan ändras när som helst ✅
- C) Den finns inte alltid
- D) Den är för stor

**10. Hur kopierar du fil från container till host?**
- A) docker copy
- B) docker cp container:/path ./local ✅
- C) docker get container:/path
- D) docker extract

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Image-hantering
```bash
# 1. Lista images
docker images

# 2. Ladda ner specifik version
docker pull python:3.12-alpine

# 3. Visa layers
docker history python:3.12-alpine

# 4. Jämför storlekar
docker images | grep python

# 5. Ta bort
docker rmi python:3.12-alpine
```

### Övning 2: Bygg enkel image
```bash
# 1. Skapa projektmapp
mkdir /tmp/dockertest && cd /tmp/dockertest

# 2. Skapa app
cat > app.py << 'EOF'
print("Hello from my Docker image!")
import sys
print(f"Python version: {sys.version}")
EOF

# 3. Skapa Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.12-alpine
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
EOF

# 4. Bygg
docker build -t mytest:1.0 .

# 5. Kör
docker run --rm mytest:1.0

# 6. Städa
cd && rm -rf /tmp/dockertest
docker rmi mytest:1.0
```

### Övning 3: Inspektera container
```bash
# 1. Starta container
docker run -d --name inspect-test nginx

# 2. Visa processer
docker top inspect-test

# 3. Resursanvändning
docker stats inspect-test --no-stream

# 4. Gå in
docker exec -it inspect-test bash
cat /etc/nginx/nginx.conf
exit

# 5. Kopiera fil
docker cp inspect-test:/etc/nginx/nginx.conf ./

# 6. Städa
docker rm -f inspect-test
rm nginx.conf
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Konsekvens | Lösning |
|---------|------------|---------|
| COPY . först | Cache invalideras vid kodändring | COPY requirements.txt först |
| Använda :latest | Oförutsägbart i produktion | Specifik version alltid |
| Glömma --no-cache-dir | Större image | pip install --no-cache-dir |
| En RUN per kommando | Många onödiga layers | Kombinera med && |

---

## 📝 SAMMANFATTNING

```bash
# IMAGE VS CONTAINER
# Image = recept (read-only mall)
# Container = tillagad rätt (körande instans)

# HANTERA IMAGES
docker images                    # Lista
docker pull nginx:1.25          # Ladda ner
docker rmi nginx                # Ta bort
docker image prune              # Ta bort oanvända

# BYGGA IMAGE
docker build -t minapp:1.0 .    # Bygg
docker history minapp:1.0       # Visa layers

# DOCKERFILE ORDNING (för caching!)
# 1. FROM
# 2. System dependencies (apt-get)
# 3. COPY requirements.txt + pip install
# 4. COPY källkod
# 5. CMD

# MULTI-STAGE
FROM golang AS builder          # Stage 1: build
RUN go build -o app
FROM alpine                     # Stage 2: runtime
COPY --from=builder /app /      # Kopiera från builder

# INTERAGERA
docker exec -it container bash  # Öppna shell
docker logs -f container        # Följ loggar
docker cp container:/path ./    # Kopiera ut
docker stats                    # Resursanvändning

# TAGGAR
python:3.12-alpine  # Använd specifik!
python:latest       # UNDVIK i produktion

# GYLLENE REGEL
# Saker som ändras SÄLLAN → först i Dockerfile
# Saker som ändras OFTA → sist i Dockerfile
```

""",
    "quiz": [
        {
            "question": "Vad är skillnaden mellan image och container?",
            "options": [
                "Ingen skillnad",
                "Image är körande, container är mall",
                "Image är mall (read-only), container är körande instans",
                "Container lagras i registry"
            ],
            "correct": 2,
            "explanation": "Image är en read-only mall/recept. Container är en körande instans med ett write-layer ovanpå."
        },
        {
            "question": "Vilken instruktion MÅSTE vara först i Dockerfile?",
            "options": [
                "RUN",
                "FROM",
                "WORKDIR",
                "COPY"
            ],
            "correct": 1,
            "explanation": "FROM anger basimage och måste alltid vara första instruktionen."
        },
        {
            "question": "Varför ska requirements.txt kopieras FÖRE resten av koden?",
            "options": [
                "Det går snabbare",
                "För att pip install ska cachas",
                "Det är syntax-krav",
                "Annars funkar det inte"
            ],
            "correct": 1,
            "explanation": "Om requirements.txt är oförändrad behöver pip install inte köras om - det cachas!"
        },
        {
            "question": "Vad gör multi-stage builds?",
            "options": [
                "Bygger snabbare",
                "Ger minimal slutimage utan build-tools",
                "Kör flera containers",
                "Komprimerar images"
            ],
            "correct": 1,
            "explanation": "Multi-stage separerar build och runtime, så slutimage blir minimal."
        },
        {
            "question": "Vad gör COPY --from=builder i multi-stage?",
            "options": [
                "Kopierar från host",
                "Kopierar från tidigare stage",
                "Kopierar från registry",
                "Kopierar till builder"
            ],
            "correct": 1,
            "explanation": "--from=builder kopierar från stage med namn 'builder'."
        },
        {
            "question": "Vilken flagga följer loggar i realtid?",
            "options": [
                "docker logs -l",
                "docker logs -f",
                "docker logs --follow",
                "docker logs -r"
            ],
            "correct": 1,
            "explanation": "-f (follow) visar nya loggrader i realtid, som tail -f."
        },
        {
            "question": "Vad gör EXPOSE i Dockerfile?",
            "options": [
                "Öppnar porten",
                "Blockerar porten",
                "Dokumenterar vilken port appen använder",
                "Mappar till host"
            ],
            "correct": 2,
            "explanation": "EXPOSE dokumenterar bara - du måste fortfarande använda -p vid docker run."
        },
        {
            "question": "Vad händer när ett layer ändras?",
            "options": [
                "Bara det layret byggs om",
                "Alla efterföljande layers måste byggas om",
                "Ingenting",
                "Hela imagen cachas"
            ],
            "correct": 1,
            "explanation": "Cache-invalidering - alla layers efter ändringen måste byggas om."
        },
        {
            "question": "Vad är :latest-taggens problem?",
            "options": [
                "Den är långsam",
                "Den kan ändras när som helst",
                "Den finns inte alltid",
                "Den är för stor"
            ],
            "correct": 1,
            "explanation": ":latest är en rörlig tagg - den pekar på senaste version som kan ändras."
        },
        {
            "question": "Hur kopierar du fil från container till host?",
            "options": [
                "docker copy",
                "docker cp container:/path ./local",
                "docker get container:/path",
                "docker extract"
            ],
            "correct": 1,
            "explanation": "docker cp kopierar filer mellan container och host."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
DOCKER_IMAGES_FLASHCARDS = [
    {"front": "Image vs Container?", "back": "Image = recept (read-only), Container = körande instans"},
    {"front": "FROM i Dockerfile?", "back": "Anger basimage (MÅSTE vara först)"},
    {"front": "RUN i Dockerfile?", "back": "Kör kommando vid build (skapar layer)"},
    {"front": "COPY vs ADD?", "back": "ADD kan extrahera tar och hämta URL"},
    {"front": "CMD vs ENTRYPOINT?", "back": "CMD kan ersättas, ENTRYPOINT är fast"},
    {"front": "docker build -t gör?", "back": "Bygger image med tag (namn:version)"},
    {"front": "Varför COPY requirements.txt först?", "back": "För att cacha pip install"},
    {"front": "Multi-stage build fördel?", "back": "Minimal slutimage utan build-tools"},
    {"front": "COPY --from=builder gör?", "back": "Kopierar från tidigare build-stage"},
    {"front": "docker logs -f gör?", "back": "Följer loggar i realtid"},
    {"front": "EXPOSE i Dockerfile?", "back": "Dokumenterar port (öppnar INTE)"},
    {"front": "WORKDIR gör?", "back": "Sätter arbetskatalog i containern"},
    {"front": "ENV i Dockerfile?", "back": "Sätter miljövariabel"},
    {"front": ":latest problemet?", "back": "Kan ändras när som helst"},
    {"front": "docker cp gör?", "back": "Kopierar filer till/från container"},
    {"front": "docker exec -it bash gör?", "back": "Öppnar interaktiv shell i container"},
    {"front": "docker history gör?", "back": "Visar image layers"},
    {"front": "docker image prune gör?", "back": "Tar bort oanvända images"},
    {"front": "Layer-ordning regel?", "back": "Sällan ändrat först, ofta ändrat sist"},
    {"front": "python:3.12-alpine är?", "back": "Minimal Alpine-baserad Python image"},
]
