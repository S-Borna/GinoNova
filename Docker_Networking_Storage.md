# Docker Networking & Storage

Fokus: Data-persistence och kommunikation mellan containrar

## Storage Strategy: Volumes vs Bind Mounts

### Volumes: Docker-managed (bäst för databaser)

Volumes är Docker-hanterad lagring som överlever container-livslängden.

```bash
# Skapa volume
docker volume create mydata

# Lista volumes
docker volume ls

# Inspektera volume
docker volume inspect mydata

# Använd volume i container
docker run -d -v mydata:/var/lib/mysql mysql

# Eller med --mount (nyare syntax)
docker run -d --mount type=volume,source=mydata,target=/var/lib/mysql mysql
```

**Fördelar**:
- Docker hanterar platsen
- Fungerar på alla plattformar
- Kan delas mellan containers
- Backup och migrering är enkelt

**Användning**: Databaser, persistent data som ska överleva container-livslängden.

```bash
# Exempel: MySQL med volume
docker run -d \
  --name mysql \
  -v mysql_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Data finns kvar även om containern stoppas
docker stop mysql
docker rm mysql
# Volume mysql_data finns fortfarande kvar
```

### Bind Mounts: Mappa lokala mappar (bäst för utveckling)

Bind mounts mappar en katalog från host till container.

```bash
# Bind mount
docker run -d -v /host/path:/container/path nginx

# Eller med --mount
docker run -d --mount type=bind,source=/host/path,target=/container/path nginx

# Read-only bind mount
docker run -d -v /host/path:/container/path:ro nginx
```

**Fördelar**:
- Direkt åtkomst till filer på host
- Ändringar syns omedelbart
- Bra för utveckling

**Nackdelar**:
- Beroende av host-filsystem
- Kan ha prestandaproblem på macOS/Windows

**Användning**: Utveckling, konfigurationsfiler, loggar.

```bash
# Exempel: Utveckling med bind mount
docker run -d \
  --name app \
  -v $(pwd)/src:/app/src \
  -v $(pwd)/config:/app/config:ro \
  myapp

# Ändringar i src/ syns omedelbart i containern
```

### tmpfs Mounts: Temporär lagring i minnet

```bash
# tmpfs mount (endast i minnet)
docker run -d --tmpfs /tmp nginx

# Eller med --mount
docker run -d --mount type=tmpfs,destination=/tmp nginx
```

**Användning**: Temporär data som inte behöver sparas.

## Port Mapping: Skillnaden mellan host-port och container-port

### Grundläggande port mapping

```bash
# Format: -p host_port:container_port
docker run -d -p 8080:80 nginx

# Nu kan du nå containern via localhost:8080
curl http://localhost:8080
```

**Förklaring**:
- **8080**: Port på host (din dator)
- **80**: Port i containern (där nginx lyssnar)

### Olika port mapping-format

```bash
# Specifik host IP och port
docker run -d -p 127.0.0.1:8080:80 nginx
# Bara tillgänglig via localhost:8080

# Alla interfaces (default)
docker run -d -p 8080:80 nginx
# Tillgänglig via alla IP:er på host

# Random host port
docker run -d -p 80 nginx
# Docker väljer en ledig port

# Flera portar
docker run -d -p 8080:80 -p 8443:443 nginx
```

### Visa port mappings

```bash
# Se vilka portar som är mappade
docker port <container_id>

# Eller
docker ps
# PORT kolumnen visar mappningar
```

## Networking: Bridge-nätverk och hur containrar hittar varandra

### Default Bridge Network

Som standard ansluts alla containers till bridge-nätverket.

```bash
# Lista nätverk
docker network ls

# Inspektera bridge network
docker network inspect bridge
```

**Problem med default bridge**:
- Containers kan bara nå varandra via IP-adress
- Ingen DNS-resolution (kan inte använda container-namn)

### Skapa Custom Bridge Network

```bash
# Skapa bridge network
docker network create mynetwork

# Kör containers på samma network
docker run -d --name app1 --network mynetwork nginx
docker run -d --name app2 --network mynetwork nginx

# Nu kan de nå varandra via namn
docker exec app1 ping app2
# Fungerar! app2 löses till IP via DNS
```

**Fördelar**:
- DNS-resolution mellan containers
- Isolering från andra networks
- Enklare kommunikation

### Docker DNS (127.0.0.11)

Docker använder en inbyggd DNS-server på 127.0.0.11 för namnuppslagning mellan containers.

```bash
# I en container på custom network:
cat /etc/resolv.conf
# nameserver 127.0.0.11

# DNS löser container-namn till IP-adresser
ping db
# PING db (172.18.0.3) 56(84) bytes of data

# Fungerar bara på custom networks, INTE på default bridge
```

**Viktigt**:
- Fungerar bara på custom bridge networks, inte på default bridge
- Containers på samma custom network kan nå varandra via namn
- DNS-servern är inbyggd i Docker och hanteras automatiskt

### Container-namnkonflikter

Docker tillåter inte två containers med samma namn.

```bash
# Första containern
docker run -d --name myapp nginx

# Försök skapa en till med samma namn
docker run -d --name myapp nginx
# Error: Conflict. The container name "/myapp" is already in use

# Lösningar:
# 1. Ta bort gamla containern först
docker rm myapp
docker run -d --name myapp nginx

# 2. Använd olika namn
docker run -d --name myapp2 nginx

# 3. Låt Docker generera unikt namn (ingen --name)
docker run -d nginx
# Docker ger ett unikt namn automatiskt
```

### --dns flaggan

Sätt en anpassad DNS-server för en specifik container.

```bash
# Använd specifik DNS-server
docker run -d --dns 8.8.8.8 nginx

# Flera DNS-servrar
docker run -d --dns 8.8.8.8 --dns 1.1.1.1 nginx

# I containern:
cat /etc/resolv.conf
# nameserver 8.8.8.8
# nameserver 1.1.1.1
```

**Användning**: När du behöver använda specifik DNS-server (t.ex. intern DNS) istället för standard.

### Network Types

```bash
# Bridge (default för containers på samma host)
docker network create --driver bridge mynet

# Host (delar hosts nätverk - Linux only)
docker network create --driver host mynet

# None (ingen nätverksanslutning)
docker network create --driver none mynet

# Starta container utan nätverk
docker run --network none nginx
# Containern får ingen IP-adress och saknar nätverksåtkomst
# (förutom loopback 127.0.0.1)

# Overlay (för Docker Swarm, flera hosts)
docker network create --driver overlay mynet
```

## Praktiskt exempel: Web + Database

```bash
# Skapa network
docker network create appnet

# Kör database
docker run -d \
  --name db \
  --network appnet \
  -v db_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Kör web app
docker run -d \
  --name web \
  --network appnet \
  -p 8080:80 \
  -e DB_HOST=db \
  -e DB_PASSWORD=secret \
  myapp

# Web kan nu nå db via "db" (DNS-resolution)
# curl http://localhost:8080 ansluter till db via hostname "db"
```

## Avancerade Storage-tekniker

### Named Volumes med specifik driver

```bash
# Skapa volume med driver
docker volume create --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100 \
  --opt device=:/path/to/nfs \
  nfs-volume
```

### Volume Backup och Restore

```bash
# Backup volume
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/mydata-backup.tar.gz /data

# Restore volume
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu tar xzf /backup/mydata-backup.tar.gz -C /data
```

### Multi-container Volume Sharing

```bash
# Skapa volume
docker volume create shared_data

# Container 1: Skriver data
docker run -d \
  --name writer \
  -v shared_data:/data \
  alpine sh -c "echo 'Hello' > /data/file.txt"

# Container 2: Läser data
docker run --rm \
  -v shared_data:/data \
  alpine cat /data/file.txt
# Output: Hello
```

## Network Troubleshooting

### Testa nätverksanslutning

```bash
# Ping mellan containers
docker exec container1 ping container2

# Testa port
docker exec container1 nc -zv container2 3306

# Se nätverksinfo
docker network inspect mynetwork
```

### Exponera portar mellan containers

```bash
# Containers på samma network behöver INTE port mapping
# De kan nå varandra direkt på container-porten

# Container 1 lyssnar på port 80
docker run -d --name app1 --network mynet nginx

# Container 2 kan nå app1 på port 80 direkt
docker exec app2 curl http://app1:80
# Ingen -p flagga behövs!
```

## Praktiska exempel

### Development Setup

```bash
# Network för utveckling
docker network create devnet

# Database
docker run -d \
  --name dev-db \
  --network devnet \
  -v $(pwd)/db-data:/var/lib/mysql \
  mysql:8.0

# App med hot-reload (bind mount)
docker run -d \
  --name dev-app \
  --network devnet \
  -p 3000:3000 \
  -v $(pwd)/src:/app/src \
  node:16 npm run dev
```

### Production Setup

```bash
# Network för produktion
docker network create prodnet

# Database med volume (persistent)
docker run -d \
  --name prod-db \
  --network prodnet \
  -v prod_db_data:/var/lib/mysql \
  mysql:8.0

# App med read-only filesystem
docker run -d \
  --name prod-app \
  --network prodnet \
  -p 80:3000 \
  --read-only \
  --tmpfs /tmp \
  myapp:latest
```

## Viktiga takeaways

- **Volumes**: Docker-managed, bäst för databaser och persistent data
- **Bind Mounts**: Mappa host-kataloger, bäst för utveckling
- **Bind Mount döljer innehåll**: Om mapp i container redan har filer, döljs de av bind mount
- **Port Mapping**: `-p host:container` exponerar container-port på host
- **Port Publishing**: Skapar iptables-regler automatiskt för att omdirigera trafik
- **Bridge Networks**: Skapa custom network för DNS-resolution mellan containers
- **Docker DNS (127.0.0.11)**: Inbyggd DNS-server för namnuppslagning (fungerar bara på custom networks)
- **Container-namnkonflikter**: Docker tillåter inte två containers med samma namn
- **--dns**: Sätt anpassad DNS-server för specifik container
- **--network none**: Ingen nätverksåtkomst (förutom loopback)
- **IPAM**: Hanterar IP-adresstilldelning i Docker-nätverk (subnet, gateway, IP-range)
- **docker network disconnect**: Koppla bort container från nätverk
- **docker inspect -f**: Extrahera specifik information med Go templates
- **Container Communication**: På samma network kan containers nå varandra via namn
- **Storage Strategy**: Volumes för produktion, bind mounts för utveckling
