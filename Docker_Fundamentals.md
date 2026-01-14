# Docker Fundamentals – Isolation & Images

Fokus: Containrar vs Virtuella Maskiner

## Container Architecture: Namespaces och Cgroups

Docker använder Linux-kärnans inbyggda funktioner för isolering:

### Namespaces (isolering)

Namespaces isolerar olika aspekter av systemet:

- **PID namespace**: Isolerade process-ID:n
- **Network namespace**: Eget nätverk
- **Mount namespace**: Eget filsystem
- **UTS namespace**: Eget hostname
- **IPC namespace**: Isolerad inter-process communication
- **User namespace**: Eget användar-ID-rymd

```bash
# Se namespaces för en container
docker inspect <container_id> | grep -i namespace

# Processer i container har isolerade PID
docker exec <container> ps aux
# PID 1 i container är inte PID 1 på host
```

### Cgroups (resursbegränsning)

Cgroups begränsar resursanvändning:

- CPU-användning
- Minne
- I/O
- Nätverk

```bash
# Se cgroup info
docker inspect <container_id> | grep -i cgroup

# Begränsa resurser vid körning
docker run --memory="512m" --cpus="1.0" nginx
```

### Skillnad VM vs Container:

- **VM**: Fullständig virtualisering, egen OS-kärna
- **Container**: Delar hostens OS-kärna, isolerad via namespaces

## Image Layers: Hur Docker cachar lager i en Dockerfile

Docker-images byggs i lager (layers). Varje instruktion i en Dockerfile skapar ett nytt lager.

### Layer Caching

Docker cachar varje lager. Om inget ändrats, återanvänds cachat lager.

```dockerfile
# Layer 1: Base image
FROM ubuntu:20.04

# Layer 2: Install packages (cachad om inget ändras)
RUN apt-get update && apt-get install -y nginx

# Layer 3: Copy files (nytt lager om filer ändras)
COPY app.conf /etc/nginx/

# Layer 4: Expose port (cachad)
EXPOSE 80

# Layer 5: Command (cachad)
CMD ["nginx", "-g", "daemon off;"]
```

**Optimering**: Placera instruktioner som ändras ofta (som COPY) så sent som möjligt i Dockerfile.

```dockerfile
# DÅLIGT: COPY tidigt = cache miss vid varje ändring
FROM node:16
COPY . /app          # Cache miss om någon fil ändras
RUN npm install      # Körs varje gång

# BRA: COPY sent = cache hit för npm install
FROM node:16
RUN npm install      # Cache hit om package.json inte ändrats
COPY . /app          # Bara detta lager byggs om
```

## Basic CLI: run, ps -a, images, rm, rmi, logs -f, exec -it

### docker run

```bash
# Kör en container
docker run nginx

# Kör i bakgrunden (-d = detached)
docker run -d nginx

# Ge container ett namn
docker run -d --name my-nginx nginx

# Mappa portar
docker run -d -p 8080:80 nginx
# Host port 8080 → Container port 80

# Mappa volymer
docker run -d -v /host/path:/container/path nginx

# Miljövariabler
docker run -d -e VAR=value nginx
```

### docker ps

```bash
# Visa körande containers
docker ps
# Visar endast containers som körs just nu

# Visa alla containers (även stoppade)
docker ps -a
# Visar alla containers som någonsin skapats (körs eller stoppade)

# Skillnad:
# docker ps     → Endast körande
# docker ps -a  → Alla (körs + stoppade)

# Formaterad output
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"

# Visa bara ID:n
docker ps -q
```

### docker images

```bash
# Lista alla images
docker images

# Sök images
docker search nginx

# Ta bort image
docker rmi nginx

# Ta bort alla oanvända images
docker image prune -a
```

### docker rm vs docker rmi

**docker rm**: Tar bort en container

```bash
# Ta bort container
docker rm <container_id>
docker rm <container_name>

# Ta bort stoppad container
docker rm my-nginx

# Tvinga bort körande container
docker rm -f my-nginx

# Ta bort alla stoppade containers
docker container prune

# Ta bort flera containers
docker rm container1 container2 container3
```

**docker rmi**: Tar bort en image

```bash
# Ta bort image
docker rmi <image_id>
docker rmi nginx:latest

# Tvinga bort (även om den används)
docker rmi -f nginx:latest

# Ta bort flera images
docker rmi image1 image2 image3

# Ta bort alla oanvända images
docker image prune -a
```

**Viktigt**: `docker rm` tar bort containers, `docker rmi` tar bort images. De är olika saker!

### docker logs

```bash
# Visa logs
docker logs <container_id>

# Följ logs i realtid (-f = follow)
docker logs -f <container_id>

# Sista N rader
docker logs --tail 100 <container_id>

# Logs med timestamp
docker logs -t <container_id>
```

### docker exec

```bash
# Kör kommando i körande container
docker exec <container_id> ls /var/www

# Interaktiv terminal (-it = interactive + TTY)
docker exec -it <container_id> /bin/bash
docker exec -it <container_id> /bin/sh

# Förklaring av flaggor:
# -i = interactive (behåll stdin öppen)
# -t = TTY (allokera pseudo-TTY)
# -it = Kombinera båda för interaktiv terminal

# Kör som specifik användare
docker exec -u root -it <container_id> /bin/bash
docker exec -u www-data -it <container_id> /bin/sh

# Kör i bakgrunden (detached)
docker exec -d <container_id> touch /tmp/file.txt

# Miljövariabler
docker exec -e VAR=value <container_id> env

# Kör i specifik arbetskatalog
docker exec -w /app <container_id> pwd
```

**Viktigt**: `docker exec` fungerar bara på körande containers. För stoppade containers, använd `docker start` först.

## Dockerfile Instructions: FROM, RUN, COPY, ADD, WORKDIR, EXPOSE, CMD vs ENTRYPOINT

### FROM

Definierar base image.

```dockerfile
FROM ubuntu:20.04
FROM node:16-alpine
FROM python:3.9-slim
```

### RUN

Kör kommandon under build.

```dockerfile
# Enkelt kommando
RUN apt-get update

# Kedja kommandon (minskar lager)
RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# Varje RUN skapar nytt lager
RUN apt-get update
RUN apt-get install -y nginx  # DÅLIGT: 2 lager
```

### COPY vs ADD

Båda kopierar filer, men ADD har extra funktioner.

```dockerfile
# COPY: Kopiera filer/kataloger från build context
COPY app.py /app/
COPY requirements.txt /app/

# COPY med wildcards
COPY *.txt /app/

# COPY bevarar metadata (rättigheter, tidsstämplar)
COPY --chown=user:group file.txt /app/

# ADD: Kan också ladda ner från URL och extrahera tar
ADD https://example.com/file.tar.gz /tmp/
ADD file.tar.gz /tmp/  # Extraherar automatiskt om det är tar/zip

# ADD kan ladda ner från URL (COPY kan inte)
ADD https://example.com/file.txt /tmp/

# Rekommendation: Använd COPY om du inte behöver ADD:s funktioner
# COPY är mer explicit och förutsägbart
```

**Skillnader**:
- **COPY**: Endast från build context, enklare och mer förutsägbart
- **ADD**: Kan ladda ner från URL, kan extrahera tar/zip automatiskt (kan vara oväntat)

**Best practice**: Använd COPY som standard, använd ADD bara när du behöver ladda ner från URL eller extrahera arkiv.

### WORKDIR

Sätter arbetskatalog för efterföljande instruktioner.

```dockerfile
WORKDIR /app
# Alla efterföljande kommandon körs i /app

RUN pwd  # /app
COPY . .  # Kopierar till /app
```

### EXPOSE

Dokumenterar vilka portar containern lyssnar på (påverkar inte faktisk exponering).

```dockerfile
EXPOSE 80
EXPOSE 443
EXPOSE 8080/tcp
EXPOSE 53/udp
```

**OBS**: EXPOSE exponerar INTE porten automatiskt. Du måste använda `-p` vid `docker run`.

### CMD vs ENTRYPOINT

Båda definierar vad som körs när containern startar.

**CMD**: Standardkommando som kan överridas.

```dockerfile
# Form 1: Exec form (rekommenderat)
CMD ["nginx", "-g", "daemon off;"]

# Form 2: Shell form
CMD nginx -g "daemon off;"

# Kan överridas vid docker run
# docker run nginx /bin/bash  # Överrider CMD
```

**ENTRYPOINT**: Kommando som INTE kan överridas (argument kan läggas till).

```dockerfile
# Exec form
ENTRYPOINT ["nginx", "-g", "daemon off;"]

# Argument läggs till
# docker run nginx -t  # Kör: nginx -g "daemon off;" -t
```

**Kombinera CMD och ENTRYPOINT**:

```dockerfile
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

# docker run nginx → docker-entrypoint.sh nginx -g "daemon off;"
# docker run nginx apache → docker-entrypoint.sh apache
```

## Praktiskt exempel: Komplett Dockerfile

```dockerfile
# Base image
FROM node:16-alpine

# Metadata
LABEL maintainer="devops@example.com"
LABEL version="1.0"

# Arbetskatalog
WORKDIR /app

# Kopiera package files först (för cache)
COPY package*.json ./

# Installera dependencies
RUN npm ci --only=production

# Kopiera applikationskod
COPY . .

# Exponera port
EXPOSE 3000

# Miljövariabel
ENV NODE_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node healthcheck.js

# Startkommando
CMD ["node", "server.js"]
```

## .dockerignore

.dockerignore fungerar som .gitignore - exkluderar filer från build context.

```
# .dockerignore
node_modules/
.git/
*.log
.env
.DS_Store
*.md
```

**Fördelar**:
- Minskar build context-storlek (snabbare byggen)
- Förhindrar att känslig data (t.ex. .env) hamnar i image
- Minskar image-storlek

**Exempel**:

```dockerfile
# Utan .dockerignore: Kopierar ALLT inklusive node_modules (stort!)
COPY . /app

# Med .dockerignore: node_modules exkluderas, bara relevanta filer kopieras
COPY . /app
```

## docker inspect - Detaljerad information

```bash
# Visa all information om container/image
docker inspect <container_id>
docker inspect <image_id>

# Extrahera specifik information
docker inspect -f '{{.State.Status}}' <container_id>
docker inspect -f '{{.NetworkSettings.IPAddress}}' <container_id>
docker inspect -f '{{.Config.Image}}' <container_id>

# JSON-format (standard)
docker inspect <container_id> | jq .

# Exempel: Hämta IP-adress
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
```

**Användning**: Debugga containers, extrahera konfiguration, se nätverksinställningar, etc.

## docker stats - Realtidsstatistik

```bash
# Visa statistik för alla körande containers
docker stats

# Visa specifik container
docker stats <container_id>

# Uppdatera var N:e sekund
docker stats --no-stream  # En gång, sedan avsluta

# Formaterad output
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

**Vad visas**:
- **CPU %**: CPU-användning
- **Mem Usage / Limit**: Minne använt / begränsning
- **Net I/O**: Nätverks I/O
- **Block I/O**: Disk I/O

**Användning**: Övervaka containerresurser i realtid, identifiera flaskhalsar.

## Dangling Images

Dangling images är images som saknar namn och tagg (visas som `<none>`).

```bash
# Visa dangling images
docker images -f "dangling=true"

# Varför skapas de?
# När du bygger en ny image med samma tag som en befintlig:
docker build -t myapp:latest .
# Den gamla image:n blir "dangling" (saknar tag)

# Ta bort dangling images
docker image prune

# Ta bort alla oanvända images (inklusive dangling)
docker image prune -a
```

**Identifiering**: Dangling images visar `<none>` som namn och tag.

## Bygga och köra

```bash
# Bygg image
docker build -t myapp:1.0 .

# Bygg med cache från specifik image
docker build --cache-from myapp:1.0 -t myapp:1.1 .

# Bygg utan cache
docker build --no-cache -t myapp:1.0 .

# Kör container
docker run -d -p 3000:3000 --name myapp myapp:1.0

# Se logs
docker logs -f myapp

# Stoppa och ta bort
docker stop myapp
docker rm myapp
```

## Viktiga takeaways

- **Namespaces**: Isolerar processer, nätverk, filsystem
- **Cgroups**: Begränsar resursanvändning (CPU, minne, I/O)
- **Image Layers**: Varje Dockerfile-instruktion = nytt lager, cachas separat
- **Layer Optimization**: Placera ändringar sent i Dockerfile för bättre cache
- **docker ps vs docker ps -a**: ps = körande, ps -a = alla (körs + stoppade)
- **docker rm vs docker rmi**: rm = container, rmi = image
- **docker exec -it**: -i = interactive, -t = TTY, krävs för interaktiva terminaler
- **COPY vs ADD**: COPY för filer (rekommenderat), ADD för URL/tar-extraktion
- **.dockerignore**: Exkludera filer från build context (minskar storlek, förbättrar säkerhet)
- **docker inspect**: Visa detaljerad JSON-information om containers/images
- **docker stats**: Övervaka CPU, minne, nätverk, I/O för körande containers i realtid
- **Dangling images**: Images utan namn/tagg (`<none>`), skapas vid rebuild med samma tag
- **CMD vs ENTRYPOINT**: CMD kan överridas, ENTRYPOINT kan inte (men argument kan läggas till)
