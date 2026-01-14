# Docker Compose & Infrastructure as Code (IaC)

Fokus: Hantera komplexa miljöer med en fil

## YAML Syntax: Indentering och struktur

Docker Compose använder YAML-format. Indentering är kritisk!

```yaml
# docker-compose.yml
version: "3.8"  # Compose file version

services:       # Alla services definieras här
  web:          # Service namn
    image: nginx
    ports:
      - "8080:80"
```

**Viktiga regler**:
- Använd spaces, inte tabs
- Indentering måste vara konsekvent (vanligtvis 2 spaces)
- Kolon (`:`) följs av space
- Listor använder bindestreck (`-`)

```yaml
# RÄTT
services:
  web:
    image: nginx
    ports:
      - "8080:80"
      - "8443:443"

# FEL (fel indentering)
services:
web:
image: nginx
```

## Services: Definiera miljövariabler, nätverk och volymer centralt

### Grundläggande Service Definition

```yaml
version: "3.8"

services:
  web:
    image: nginx:latest
    container_name: my_nginx
    ports:
      - "8080:80"
    environment:
      - NGINX_HOST=example.com
      - NGINX_PORT=80
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - appnet
```

### Miljövariabler

```yaml
services:
  app:
    image: myapp
    # Metod 1: Lista
    environment:
      - DB_HOST=db
      - DB_PASSWORD=secret
      - NODE_ENV=production

    # Metod 2: Dictionary
    environment:
      DB_HOST: db
      DB_PASSWORD: secret
      NODE_ENV: production

    # Metod 3: Fil
    env_file:
      - .env
      - .env.production
```

### Nätverk

```yaml
services:
  web:
    image: nginx
    networks:
      - frontend
      - backend

  db:
    image: mysql
    networks:
      - backend

# Definiera networks
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
```

### Volymer

```yaml
services:
  db:
    image: mysql
    volumes:
      # Named volume
      - db_data:/var/lib/mysql
      # Bind mount
      - ./config:/etc/mysql/conf.d
      # Anonymous volume
      - /tmp

# Definiera volumes
volumes:
  db_data:
    driver: local
```

## Orchestration Lite: Använda depends_on för att styra startordning

`depends_on` säkerställer att services startar i rätt ordning.

```yaml
services:
  web:
    image: nginx
    depends_on:
      - db
      - redis
    # Web startar EFTER db och redis

  db:
    image: mysql

  redis:
    image: redis
```

**OBS**: `depends_on` väntar bara på att containern startar, inte att servicen är redo!

```yaml
# För att vänta på att service är redo, använd healthcheck
services:
  web:
    image: nginx
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
```

## Lifecycle: docker-compose up -d, down och ps

### docker-compose up

```bash
# Starta alla services
docker-compose up

# Starta i bakgrunden (-d = detached)
docker-compose up -d

# Bygga images innan start
docker-compose up --build

# Bygga utan cache
docker-compose build --no-cache

# Bygga specifik service
docker-compose build web

# Bygga och starta utan cache
docker-compose build --no-cache
docker-compose up -d

# Starta specifik service
docker-compose up web

# Starta med override file
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

### docker-compose down

```bash
# Stoppa och ta bort containers
docker-compose down

# Ta bort även volumes
docker-compose down -v

# Ta bort även images
docker-compose down --rmi all
```

### docker-compose ps

```bash
# Visa status för alla services
docker-compose ps

# Detaljerad information
docker-compose ps -a
```

### Andra viktiga kommandon

```bash
# Se logs
docker-compose logs
docker-compose logs -f web  # Följ logs för web service

# Köra kommando i service
docker-compose exec web ls /app
```

### docker-compose exec vs docker exec

```bash
# docker-compose exec: Kör i service som definierats i compose-filen
docker-compose exec web bash

# docker exec: Kör direkt i container (behöver container-ID/namn)
docker exec myapp_web bash

# Skillnad: docker-compose exec använder service-namnet från YAML
# docker exec använder container-namnet (kan vara annorlunda)
```

### Starta/stoppa services

```bash
docker-compose start
docker-compose stop
docker-compose restart web
```

### Skala services

```bash
docker-compose up -d --scale web=3
# Kör 3 instanser av web service

# Eller med docker-compose scale (äldre syntax)
docker-compose scale web=3

# OBS: Container-namn får suffix (_1, _2, _3) när man skalar
# myapp_web_1, myapp_web_2, myapp_web_3
```

## Komplett Exempel: Multi-Service Application

```yaml
version: "3.8"

services:
  # Web server
  web:
    build: .
    container_name: myapp_web
    ports:
      - "8080:80"
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    volumes:
      - ./src:/app/src
      - ./logs:/app/logs
    depends_on:
      - db
      - redis
    networks:
      - appnet
    restart: unless-stopped

  # Database
  db:
    image: mysql:8.0
    container_name: myapp_db
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: myapp
      MYSQL_USER: appuser
      MYSQL_PASSWORD: apppassword
    volumes:
      - db_data:/var/lib/mysql
      - ./db-init:/docker-entrypoint-initdb.d
    networks:
      - appnet
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  redis:
    image: redis:7-alpine
    container_name: myapp_redis
    volumes:
      - redis_data:/data
    networks:
      - appnet
    restart: unless-stopped
    command: redis-server --appendonly yes

  # Worker (background jobs)
  worker:
    build: .
    command: node worker.js
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      - db
      - redis
    networks:
      - appnet
    restart: unless-stopped

# Networks
networks:
  appnet:
    driver: bridge

  # External network (finns redan, skapas inte av Compose)
  external_net:
    external: true
    name: existing_network

# Volumes
volumes:
  db_data:
    driver: local
  redis_data:
    driver: local
```

## External Networks vs Compose-created Networks

### Compose-created networks: Skapas automatiskt av Docker Compose

```yaml
networks:
  appnet:
    driver: bridge
# Skapas när du kör docker-compose up
# Tas bort när du kör docker-compose down (om -v används)
```

### External networks: Finns redan, skapas inte av Compose

```yaml
networks:
  external_net:
    external: true
    name: existing_network
# Använder befintligt nätverk
# Tas INTE bort vid docker-compose down
```

**Användning**: När du vill använda ett nätverk som skapats manuellt eller av annat Compose-projekt.

## Environment-Specific Compose Files

### docker-compose.yml (Development)

```yaml
version: "3.8"

services:
  web:
    build: .
    volumes:
      - ./src:/app/src  # Hot reload
    environment:
      - NODE_ENV=development
```

### docker-compose.prod.yml (Production)

```yaml
version: "3.8"

services:
  web:
    image: myapp:latest
    # Inga volumes (read-only)
    environment:
      - NODE_ENV=production
    restart: always
```

```bash
# Development
docker-compose up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### docker-compose.override.yml

Docker Compose läser automatiskt `docker-compose.override.yml` om den finns och mergar den med huvudfilen.

```yaml
# docker-compose.yml (huvudfil)
version: "3.8"
services:
  web:
    image: nginx
    ports:
      - "80:80"

# docker-compose.override.yml (automatiskt laddad)
version: "3.8"
services:
  web:
    volumes:
      - ./src:/app/src  # Läggs till i huvudfilen
    environment:
      - DEBUG=true      # Läggs till i huvudfilen
```

**Användning**:
- Lokal utveckling (bind mounts, debug-portar)
- Miljöspecifika inställningar
- Överskriver eller lägger till inställningar från huvudfilen

**Viktigt**: `docker-compose.override.yml` läses automatiskt - du behöver inte ange `-f` flaggan.

## Immutable Infrastructure

Immutable Infrastructure innebär att containrar är oföränderliga. Istället för att ändra i en körande container, bygger du en ny image och ersätter containern.

### Koncept

```bash
# ❌ DÅLIGT: Ändra i körande container
docker exec myapp apt-get install newpackage
docker exec myapp nano /etc/config

# ✅ BRA: Bygg ny image och ersätt
docker-compose build myapp
docker-compose up -d --no-deps myapp
```

### Praktiskt exempel

```yaml
services:
  web:
    build: .
    # Om du behöver ändra något:
    # 1. Ändra Dockerfile eller kod
    # 2. docker-compose build web
    # 3. docker-compose up -d --no-deps web
    # Containern ersätts med ny image
```

**Fördelar**:
- Reproducerbarhet (samma image = samma resultat)
- Enklare rollback (använd gammal image)
- Versionering (varje image är versionerad)
- Säkerhet (ingen risk för drift i körande containers)

## Best Practices

### 1. Använd .env-filer

Docker Compose läser automatiskt `.env`-filen i samma mapp.

```bash
# .env (i samma mapp som docker-compose.yml)
DB_PASSWORD=secret
REDIS_PASSWORD=secret
DB_HOST=db
```

```yaml
services:
  db:
    environment:
      MYSQL_PASSWORD: ${DB_PASSWORD}  # Läses från .env
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}

  web:
    environment:
      - DB_HOST=${DB_HOST}  # Läses från .env
```

**Viktigt**:
- `.env`-filen läses automatiskt av Docker Compose
- Använd `${VAR}` syntax i docker-compose.yml
- `.env` bör INTE committas till git (lägg till i .gitignore)
- Skapa `.env.example` med placeholder-värden för dokumentation

### 2. Health Checks

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### 3. Resource Limits

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 512M
        reservations:
          cpus: "0.25"
          memory: 256M
```

### 4. Logging Configuration

```yaml
services:
  web:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## Viktiga takeaways

- **YAML Syntax**: Spaces för indentering, konsekvent struktur
- **Services**: Definiera miljövariabler, nätverk och volymer centralt
- **.env-filen**: Läses automatiskt av Docker Compose, använd `${VAR}` syntax
- **docker-compose.override.yml**: Läses automatiskt och mergas med huvudfilen (för lokal utveckling)
- **docker-compose exec vs docker exec**: exec använder service-namn, docker exec använder container-namn
- **docker-compose build --no-cache**: Bygga images utan cache
- **restart: always vs unless-stopped**: always startar alltid, unless-stopped respekterar manuell stoppning
- **docker-compose scale / --scale**: Skala services till flera instanser
- **External networks**: Använd befintliga nätverk (tas inte bort vid down)
- **Immutable Infrastructure**: Bygg ny image istället för att ändra i körande container
- **depends_on**: Styr startordning (men väntar inte på att service är redo)
- **docker-compose up -d**: Starta i bakgrunden
- **docker-compose down**: Stoppa och ta bort (använd `-v` för volumes, `--rmi all` för images)
- **docker-compose ps**: Visa status för services i projektet
- **Multi-file**: Använd olika compose-filer för olika miljöer
- **Infrastructure as Code**: Hela miljön definierad i versionerade filer
