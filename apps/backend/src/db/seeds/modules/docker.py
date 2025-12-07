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
            "title": "Docker Fundamentals",
            "slug": "docker-fundamentals",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Docker Fundamentals

## ⚡ Snabbinstallation (2 minuter)

Innan vi börjar behöver du Docker installerat. Välj ditt operativsystem:

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🍎 macOS / 🪟 Windows
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Gå till: https://docker.com/products/docker-desktop
# 2. Ladda ner Docker Desktop
# 3. Installera och starta
# 4. Klart!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐧 Linux (Ubuntu/Debian)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

# Kör Docker utan sudo (valfritt men rekommenderat)
sudo usermod -aG docker $USER
# Logga ut och in igen för att ändringen ska gälla
```

**Verifiera installationen:**

```bash
docker --version
# Förväntad output: Docker version 24.x.x eller liknande

docker run hello-world
# Om du ser "Hello from Docker!" är allt klart! ✅
```

---

## 🎯 Varför Docker är viktigt för DevOps

Docker är ett av de viktigaste verktygen i modern DevOps. Här är varför:

| Problem utan Docker | Lösning med Docker |
|--------------------|--------------------|
| "Det fungerade på min dator!" | Samma container körs identiskt överallt |
| Deployment tar timmar | Containers startar på sekunder |
| Varje server konfigureras manuellt | Allt är paketerat i imagen |
| Resursslöseri med VMs | Containers delar OS-kärnan |
| Svårt att skala | Starta fler containers direkt |
| Beroendekonflikter | Varje app isolerad i sin container |

---

## 🐳 Vad är Docker egentligen?

Docker låter dig paketera en applikation tillsammans med **allt den behöver** - kod, runtime, bibliotek, systemverktyg och inställningar - i en portabel enhet som kallas **container**.

Tänk på det som en **standardiserad fraktcontainer** för mjukvara. Precis som fraktcontainrar revolutionerade sjöfarten genom att standardisera transport, revolutionerar Docker hur mjukvara levereras.

```bash
# En container innehåller:
┌─────────────────────────────────────┐
│  🔹 Din applikationskod             │
│  🔹 Runtime (Node, Python, etc)     │
│  🔹 Systembibliotek                 │
│  🔹 Konfigurationsfiler             │
│  🔹 Miljövariabler                  │
└─────────────────────────────────────┘
# Allt paketerat → fungerar överallt!
```

---

## 📦 Containers vs Virtual Machines

Det är viktigt att förstå skillnaden mellan containers och virtual machines (VMs):

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VIRTUAL MACHINE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────┐
│           Din App                    │
├─────────────────────────────────────┤
│      Helt eget OS (Guest OS)         │  ← 1-10 GB bara för OS!
├─────────────────────────────────────┤
│         Hypervisor                   │
├─────────────────────────────────────┤
│          Host OS                     │
├─────────────────────────────────────┤
│         Hardware                     │
└─────────────────────────────────────┘
# Starttid: 1-5 minuter
# RAM per VM: 1-4 GB minimum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONTAINER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────────────────────┐
│           Din App                    │
├─────────────────────────────────────┤
│        Docker Engine                 │  ← MB istället för GB!
├─────────────────────────────────────┤
│          Host OS                     │
├─────────────────────────────────────┤
│         Hardware                     │
└─────────────────────────────────────┘
# Starttid: 1-2 sekunder
# RAM per container: 50-200 MB
```

**Nyckelpunkt:** Containers delar host-systemets OS-kärna. Det är därför de är så snabba och lätta!

**Praktiskt exempel:**

```bash
# Du behöver köra 3 webbservrar:

# Med VMs:
# - 3 separata operativsystem
# - Totalt: ~6-8 GB RAM
# - Starttid: 5-10 minuter

# Med Docker:
# - 3 containers, delad OS-kärna
# - Totalt: ~200 MB RAM
# - Starttid: 3-5 sekunder
```

---

## 🏗️ Docker-arkitekturen

Docker består av flera komponenter som samarbetar:

```bash
┌──────────────────────────────────────────────────────────┐
│                  📱 DOCKER CLIENT                         │
│              (kommandoradsverktyget 'docker')            │
│                                                          │
│   docker run, docker build, docker pull, docker ps...    │
└─────────────────────────┬────────────────────────────────┘
                          │
                          │ REST API (kommunikation)
                          ▼
┌──────────────────────────────────────────────────────────┐
│                  ⚙️ DOCKER DAEMON                         │
│                    (dockerd)                              │
│                                                          │
│   Bakgrundsprocess som gör allt jobb:                    │
│   - Hanterar images                                       │
│   - Skapar/kör containers                                │
│   - Hanterar nätverk och volymer                         │
└─────────────────────────┬────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────┐
│               📦 CONTAINER RUNTIME                        │
│                  (containerd)                             │
│                                                          │
│   Lågnivå-hantering av containers                        │
└──────────────────────────────────────────────────────────┘
```

**Förklaring av komponenterna:**

| Komponent | Vad den gör |
|-----------|-------------|
| **Docker Client** | CLI-verktyget du skriver kommandon i |
| **Docker Daemon** | Bakgrundsprocess som gör allt arbete |
| **Docker Images** | Read-only mallar för containers |
| **Docker Containers** | Körande instanser av images |
| **Docker Hub** | Publik registry för images (som GitHub för kod) |

---

## 🌐 Docker Hub - Appbutiken för containers

Docker Hub är världens största registry för Docker images. Tänk på det som en **appbutik för containers**:

```bash
# Docker Hub innehåller tusentals färdiga images:
# ┌─────────────────────────────────────────────────┐
# │  nginx        - Webbserver                      │
# │  postgres     - PostgreSQL databas              │
# │  redis        - Cache och meddelandehantering   │
# │  node         - Node.js runtime                 │
# │  python       - Python runtime                  │
# │  mysql        - MySQL databas                   │
# │  mongo        - MongoDB databas                 │
# │  ubuntu       - Ubuntu basimage                 │
# └─────────────────────────────────────────────────┘

# Sök efter images
docker search nginx
# Visar alla nginx-relaterade images

# Ladda ner en image
docker pull nginx
# Hämtar officiella nginx-imagen

# Ladda upp din egen image
docker push dittnamn/din-image
# Publicerar till Docker Hub (kräver konto)
```

---

## 🖥️ Docker på olika plattformar

Docker fungerar på alla operativsystem, men bäst på Linux:

| Plattform | Hur Docker körs | Prestanda |
|-----------|-----------------|-----------|
| **Linux** | Direkt på systemet (native) | ⭐⭐⭐⭐⭐ Bäst |
| **macOS** | Via Docker Desktop (liten Linux VM) | ⭐⭐⭐⭐ Bra |
| **Windows** | Via Docker Desktop (WSL2/Hyper-V) | ⭐⭐⭐⭐ Bra |

---

## 🔧 Grundläggande Docker-kommandon

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 INFORMATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docker --version          # Visar Docker-versionen
docker info               # Detaljerad systeminfo

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 IMAGES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docker images             # Lista alla lokala images
docker pull nginx         # Ladda ner nginx-image
docker rmi nginx          # Ta bort en image

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐳 CONTAINERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docker ps                 # Lista körande containers
docker ps -a              # Lista ALLA containers (även stoppade)
docker run nginx          # Skapa och starta en container
docker stop <id>          # Stoppa en container
docker rm <id>            # Ta bort en container

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💡 HJÄLP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docker run --help         # Hjälp för specifikt kommando
docker --help             # Lista alla kommandon
```

---

## 🔄 Vad händer när du kör "docker run"?

```bash
docker run nginx
```

Bakom kulisserna händer detta:

```bash
# Steg 1: Docker Client → Docker Daemon
#         "Hej, jag vill köra nginx!"

# Steg 2: Daemon kollar lokalt
#         "Finns nginx-image på denna dator?"

# Steg 3: Om nej → Ladda ner från Docker Hub
#         "Hämtar nginx:latest från registry..."

# Steg 4: Skapa container
#         "Skapar isolerad miljö med filsystem, nätverk..."

# Steg 5: Starta container
#         "Nginx körs nu i containern!"
```

**Så `docker run` = pull + create + start i ett kommando!**

---

## 🚀 Varför Docker i DevOps-arbetet?

| Traditionellt problem | Docker-lösning |
|----------------------|----------------|
| "Det fungerade på min dator" | Samma image körs överallt |
| Komplexa installationssteg | `docker run` - en rad |
| Konfigurationskaos | Allt i Dockerfile, versionshanterat |
| Långsam deployment | Sekunder istället för timmar |
| Resurshungriga VMs | Lätta containers |
| Svårt att rulla tillbaka | Byt till tidigare image-tag |

```bash
# Före Docker (deployment):
# 1. SSH till server
# 2. Installera dependencies (kan ta timmar)
# 3. Konfigurera miljön
# 4. Starta applikationen
# 5. Hoppas inget går fel...

# Med Docker:
docker pull min-app:v1.2.3
docker run -d min-app:v1.2.3
# Klart på sekunder! ✅
```

---

## ✅ Sammanfattning

| Begrepp | Förklaring |
|---------|------------|
| **Docker** | Plattform för att bygga och köra containers |
| **Container** | Isolerad miljö med app + dependencies |
| **Image** | Read-only mall för att skapa containers |
| **Docker Hub** | Registry för att dela images |
| **Docker Daemon** | Bakgrundsprocess som hanterar allt |
| **Docker Client** | CLI-verktyget du använder |

**Nästa steg:** Nu när du förstår grunderna ska vi dyka djupare i Docker Images!
""",
        },
        {
            "title": "SSH & Remote Access",
            "slug": "ssh-remote-access",
            "difficulty": "easy",
            "estimated_minutes": 50,
            "xp_reward": 80,
            "content": """# SSH & Remote Access

## 🎯 Varför SSH är kritiskt för DevOps

SSH är standardverktyget för att hantera servrar. Som DevOps-ingenjör använder du det dagligen för:

| Användningsområde | Beskrivning |
|-------------------|-------------|
| **Remote server access** | Logga in på servrar över nätverket |
| **Säker filöverföring** | Kopiera filer med SCP och RSYNC |
| **Tunneling** | Skapa säkra kanaler för annan trafik |
| **Remote commands** | Kör kommandon på servrar utan att logga in |
| **Automation** | Skript som hanterar många servrar |
| **Production management** | Hantera produktionsmiljöer säkert |

---

## ⚡ Snabbinstallation

SSH-klienten är oftast förinstallerad. Verifiera:

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍 KONTROLLERA OM SSH FINNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -V
# Förväntad output: OpenSSH_8.x eller liknande

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐧 LINUX - Installera om det saknas
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
sudo apt update && sudo apt install openssh-client -y

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🍎 macOS / 🪟 Windows
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SSH är förinstallerat på macOS
# Windows 10/11: SSH finns i PowerShell eller använd Git Bash
```

---

## 🔌 Grundläggande anslutning

SSH (Secure Shell) skapar en krypterad anslutning till en fjärrdator. Allt du skriver och ser är skyddat från avlyssning.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📡 BASIC CONNECTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh user@hostname
# ssh        = kommandot
# user       = användarnamnet på fjärrdatorn
# @          = separator
# hostname   = servernamn eller IP-adress
# Exempel: ssh alice@server.example.com

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 MED SPECIFIK PORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -p 2222 user@hostname
# -p 2222    = anslut till port 2222 istället för standard (22)
# Vissa servrar använder annan port för ökad säkerhet

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 MED IP-ADRESS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh user@192.168.1.100
# Använd IP-adress direkt när du inte har DNS
# Användbart i lokala nätverk eller vid felsökning

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡ KÖR KOMMANDO REMOTE (utan interaktiv session)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh user@hostname "ls -la"
# Kör kommandot, visa output, stäng anslutningen
# Perfekt för automation och skript!

ssh user@hostname "df -h && free -m"
# Kör flera kommandon med &&
```

---

## 🔍 Verbose-läge för felsökning

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐛 DEBUG-NIVÅER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -v user@hostname      # Verbose - grundläggande debug-info
ssh -vv user@hostname     # Mer detaljerat
ssh -vvv user@hostname    # Maximalt detaljerat - visar ALLT

# Användbart när anslutningen misslyckas
# Visar vilka nycklar som testas, vilka algoritmer som används, etc.
```

---

## 🚪 Avsluta SSH-session

```bash
exit        # Skriv exit
logout      # Eller logout
# Ctrl+D    # Eller tangentbordsgenväg
```

---

## 🔑 SSH-nycklar (säkrare än lösenord)

SSH-nycklar fungerar som ett nyckelpar - en **privat** (hemlig) och en **publik** (kan delas). Det är mycket säkrare än lösenord!

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 GENERERA NYCKLAR - ED25519 (rekommenderat)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh-keygen -t ed25519 -a 100 -C "din@email.com"
# -t ed25519  = nyckeltyp (modern och säker)
# -a 100      = antal krypteringsrundor (mer = säkrare)
# -C          = kommentar (hjälper identifiera nyckeln)

# Du får frågor:
# 1. Var ska nyckeln sparas? (Enter för default: ~/.ssh/id_ed25519)
# 2. Passphrase? (REKOMMENDERAS - extra säkerhet för nyckeln)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 ALTERNATIV: RSA (om ED25519 inte stöds)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh-keygen -t rsa -b 4096 -a 100 -C "din@email.com"
# -t rsa      = RSA-nyckel (äldre men fungerar överallt)
# -b 4096     = 4096 bitar (minimum för säkerhet idag)
```

**Varför nycklar är bättre än lösenord:**
- Även om någon får din publika nyckel kan de inte logga in
- Längre och mer slumpmässiga än lösenord
- Kan inte gissas med brute-force
- Kan skyddas med passphrase

---

## 📁 Nyckelfiler och rättigheter

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📂 VAR NYCKLARNA SPARAS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
~/.ssh/id_ed25519       # Privat nyckel (HEMLIG!)
~/.ssh/id_ed25519.pub   # Publik nyckel (kan delas)
~/.ssh/id_rsa           # Privat RSA-nyckel
~/.ssh/id_rsa.pub       # Publik RSA-nyckel

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔒 KRITISKA RÄTTIGHETER (SSH vägrar annars!)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
chmod 700 ~/.ssh              # Bara du kan läsa mappen
chmod 600 ~/.ssh/id_ed25519   # Bara du kan läsa privata nyckeln
chmod 644 ~/.ssh/id_ed25519.pub  # Alla kan läsa publika nyckeln
chmod 600 ~/.ssh/authorized_keys  # Serverns lista med tillåtna nycklar
```

---

## 📤 Kopiera publik nyckel till server

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✨ METOD 1: ssh-copy-id (enklast!)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh-copy-id user@hostname
# Kopierar din publika nyckel automatiskt till servern
# Du loggar in med lösenord EN gång, sedan fungerar nyckeln

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 METOD 2: Manuellt med pipe
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cat ~/.ssh/id_ed25519.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✂️ METOD 3: Kopiera och klistra
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cat ~/.ssh/id_ed25519.pub   # Visa din publika nyckel
# Kopiera outputen, logga in på servern, och:
mkdir -p ~/.ssh
echo "KLISTRA-NYCKELN-HÄR" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

---

## ⚙️ SSH Config (spara tid!)

Skapa `~/.ssh/config` för att slippa skriva långa kommandon:

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 EXEMPEL: ~/.ssh/config
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Host production
    HostName 192.168.1.100
    User deploy
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
    ServerAliveCountMax 3

Host staging
    HostName staging.example.com
    User admin
    IdentityFile ~/.ssh/staging_key

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

**Nu kan du ansluta med:**

```bash
ssh production    # Istället för: ssh -p 2222 deploy@192.168.1.100
ssh staging       # Istället för: ssh admin@staging.example.com
```

**Vanliga config-optioner:**

| Option | Beskrivning |
|--------|-------------|
| `HostName` | Serveradress (IP eller domän) |
| `User` | Användarnamn |
| `Port` | SSH-port |
| `IdentityFile` | Vilken nyckel som ska användas |
| `ServerAliveInterval` | Skicka keep-alive var X:e sekund |
| `ServerAliveCountMax` | Max antal missade keep-alive |

---

## 🚇 Port Forwarding (tunnlar)

Port forwarding skapar "hemliga tunnlar" genom SSH - perfekt för att nå tjänster som inte är direkt tillgängliga.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📥 LOCAL PORT FORWARDING (-L)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -L 8080:localhost:3000 user@server
# Din lokala port 8080 → tunnlas till → serverns localhost:3000
# Öppna localhost:8080 i webbläsaren → ser serverns app på port 3000

# Praktiskt exempel: Nå databas som bara lyssnar lokalt
ssh -L 5432:localhost:5432 user@dbserver
# Nu kan du ansluta till localhost:5432 och nå databasen!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📤 REMOTE PORT FORWARDING (-R)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -R 8080:localhost:3000 user@server
# Serverns port 8080 → tunnlas till → din lokala port 3000
# Användbart: Visa lokal utveckling via servern

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 DYNAMIC PORT FORWARDING (-D) - SOCKS Proxy
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -D 1080 user@server
# Skapar SOCKS-proxy på localhost:1080
# All trafik genom proxyn går via SSH-tunneln
# Konfigurera webbläsaren att använda localhost:1080

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 BAKGRUNDSTUNNEL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -f -N -L 5432:localhost:5432 user@dbserver
# -f = kör i bakgrunden
# -N = kör inget kommando (bara tunneln)
```

---

## 📦 SCP - Kopiera filer säkert

SCP (Secure Copy) kopierar filer över SSH - enkelt och krypterat.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⬆️ KOPIERA TILL SERVER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
scp file.txt user@hostname:/path/to/destination
# Kopierar file.txt till servern

scp -r directory/ user@hostname:/path/
# -r = recursive, kopierar hela mappen med innehåll

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⬇️ KOPIERA FRÅN SERVER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
scp user@hostname:/path/to/file.txt ./
# Kopierar fil från servern till nuvarande mapp

scp user@hostname:/home/user/data.txt ~/Downloads/
# Kopierar till specifik mapp

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 MED ANNAN PORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
scp -P 2222 file.txt user@hostname:/path/
# OBS: Stort -P för SCP, litet -p för SSH!
```

---

## 🔄 RSYNC över SSH

RSYNC är smartare än SCP - synkar bara det som ändrats.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔁 SYNKA FILER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
rsync -avz -e ssh local/ user@hostname:/remote/
# -a = archive (behåll permissions, timestamps, etc)
# -v = verbose (visa vad som händer)
# -z = compress (snabbare över nätverket)
# -e ssh = använd SSH för transport

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚫 EXKLUDERA FILER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
rsync -avz --exclude '*.log' --exclude 'node_modules' -e ssh local/ user@hostname:/remote/
```

---

## 🔐 SSH Agent (hantera nycklar)

SSH Agent håller dina nycklar i minnet så du slipper ange passphrase varje gång.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 STARTA OCH ANVÄND AGENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
eval $(ssh-agent)       # Starta agenten
ssh-add ~/.ssh/id_ed25519  # Lägg till nyckel (ange passphrase en gång)
ssh-add -l              # Lista laddade nycklar
ssh-add -d ~/.ssh/id_ed25519  # Ta bort specifik nyckel
ssh-add -D              # Ta bort alla nycklar

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 AGENT FORWARDING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -A user@hostname    # Vidarebefordra din agent till servern
# Nu kan du SSH vidare från servern med dina lokala nycklar!

# Eller i config:
Host server
    ForwardAgent yes
```

---

## 🛡️ Säkerhetstips

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ BEST PRACTICES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Använd starka nycklar
ssh-keygen -t ed25519 -a 100

# 2. Skydda privata nyckeln
chmod 600 ~/.ssh/id_ed25519

# 3. Använd passphrase på nyckeln

# 4. Rotera nycklar regelbundet

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 KNOWN HOSTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ~/.ssh/known_hosts sparar serverns fingeravtryck
# Skyddar mot man-in-the-middle attacker

ssh-keygen -R hostname  # Ta bort gammal host-key
ssh-keyscan hostname    # Hämta serverns host-key
```

---

## 🔧 Felsökning

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ CONNECTION REFUSED
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
systemctl status sshd           # Kör SSH-servern?
ss -tlnp | grep :22            # Lyssnar den på port 22?
sudo ufw status | grep 22       # Blockerar brandväggen?
sudo journalctl -u sshd -n 50   # Vad säger loggarna?

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚫 PERMISSION DENIED
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ls -la ~/.ssh/                  # Rätt permissions?
ls -la ~/.ssh/authorized_keys   # Finns filen? Rätt permissions?
ssh -vvv user@hostname          # Detaljerad debug-info
sudo tail -f /var/log/auth.log  # Serverloggar

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐌 LÅNGSAM ANSLUTNING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -o GSSAPIAuthentication=no user@hostname

# Eller permanent i ~/.ssh/config:
Host *
    GSSAPIAuthentication no
    UseDNS no
```

---

## 🚀 Produktionsmönster

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 AUTOMATISERAD DEPLOY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#!/bin/bash
SERVER="user@production"
APP_DIR="/opt/myapp"

# Synka filer
rsync -avz --exclude 'node_modules' -e ssh ./ $SERVER:$APP_DIR/

# Kör deploy-kommando
ssh $SERVER "cd $APP_DIR && ./deploy.sh"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 ÖVERVAKA FLERA SERVRAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#!/bin/bash
SERVERS=("server1" "server2" "server3")

for server in "${SERVERS[@]}"; do
    if ssh -o ConnectTimeout=5 "$server" "systemctl is-active nginx" &>/dev/null; then
        echo "✓ $server: nginx running"
    else
        echo "✗ $server: nginx down"
    fi
done
```

---

## ✅ Sammanfattning

| Kommando | Beskrivning |
|----------|-------------|
| `ssh user@hostname` | Anslut till server |
| `ssh -p PORT` | Använd specifik port |
| `ssh-keygen` | Generera nycklar |
| `ssh-copy-id` | Kopiera publik nyckel till server |
| `~/.ssh/config` | Klientkonfiguration |
| `-L` | Local port forwarding |
| `-R` | Remote port forwarding |
| `-D` | Dynamic forwarding (SOCKS) |
| `scp` | Säker filkopiering |
| `rsync -e ssh` | Synka över SSH |
| `ssh-agent` | Hantera nycklar i minnet |

**Kom ihåg:**
- 🔒 Skydda privata nycklar (chmod 600)
- 🔑 Använd ED25519 eller RSA 4096
- ⚙️ Använd SSH config för bekvämlighet
- 🧪 Testa anslutningar innan du automatiserar
""",
        },
        {
            "title": "IP-adresser: Privat vs Publik",
            "slug": "ip-addresses-private-public",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# IP-adresser: Privat vs Publik

## 🎯 Varför IP-kunskap är kritiskt för DevOps

IP-adresser är grunden för all nätverkskommunikation. Som DevOps-ingenjör använder du dem för:

| Användningsområde | Beskrivning |
|-------------------|-------------|
| **Cloud infrastructure** | Konfigurera VPC, subnets, routing |
| **Security** | Brandväggsregler, access control |
| **Troubleshooting** | Felsöka nätverksproblem |
| **Load balancing** | Distribuera trafik mellan servrar |
| **Container networking** | Docker och Kubernetes nätverk |
| **Firewall rules** | Tillåta/blockera specifika adresser |

---

## 📊 IP-adress Grunderna

### IPv4 Format

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📐 IPv4 STRUKTUR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IPv4 = 32 bitar = 4 bytes
# Format: xxx.xxx.xxx.xxx (dotted decimal)
# Range: 0.0.0.0 till 255.255.255.255
# Totalt: ~4,3 miljarder adresser

# Exempel:
192.168.1.100
│   │   │  │
│   │   │  └── Host (0-255)
│   │   └── Subnet (0-255)
│   └── Subnet (0-255)
└── Network (0-255)
```

### IPv6 Format

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📐 IPv6 STRUKTUR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# IPv6 = 128 bitar = 16 bytes
# Format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
# Totalt: ~340 undecillion adresser (praktiskt taget oändligt)

# Exempel:
2001:0db8:85a3:0000:0000:8a2e:0370:7334

# Förkortad form (ta bort ledande nollor, :: för sekvens av nollor):
2001:db8:85a3::8a2e:370:7334
```

---

## 🏠 Privata IP-adresser

Privata IP-adresser är som **"interna telefonnummer"** på ett företag - de fungerar bara inom ditt lokala nätverk och kan inte nås direkt från internet. De är gratis att använda och kan återanvändas i olika nätverk.

### RFC 1918 - Privata IP-områden

RFC 1918 definierar tre områden med privata IP-adresser som alla kan använda fritt:

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏢 CLASS A: 10.0.0.0/8 (Stora organisationer)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Range: 10.0.0.0 - 10.255.255.255
# Antal adresser: 16,777,216 (över 16 miljoner!)
# /8 betyder: de första 8 bitarna är fixerade (10.x.x.x)

# Användning: Stora företag, molnleverantörer (AWS, Azure, GCP)
# Exempel: 10.0.0.1, 10.1.2.3, 10.255.255.254

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏬 CLASS B: 172.16.0.0/12 (Medelstora organisationer)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Range: 172.16.0.0 - 172.31.255.255
# Antal adresser: 1,048,576 (över en miljon)
# /12 betyder: de första 12 bitarna är fixerade (172.16-31.x.x)

# Användning: Medelstora företag, avancerade hemnätverk
# Exempel: 172.16.0.1, 172.20.5.10, 172.31.255.254

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏠 CLASS C: 192.168.0.0/16 (Hem och små kontor)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Range: 192.168.0.0 - 192.168.255.255
# Antal adresser: 65,536 (över 65 tusen)
# /16 betyder: de första 16 bitarna är fixerade (192.168.x.x)

# Användning: Hemrouter (standard!), små kontor
# Exempel: 192.168.1.1 (router), 192.168.1.100 (dator)
```

### Sammanfattning privata områden

| Klass | CIDR | Range | Antal adresser | Användning |
|-------|------|-------|----------------|------------|
| A | 10.0.0.0/8 | 10.0.0.0 - 10.255.255.255 | 16,777,216 | Stora företag, cloud |
| B | 172.16.0.0/12 | 172.16.0.0 - 172.31.255.255 | 1,048,576 | Medelstora företag |
| C | 192.168.0.0/16 | 192.168.0.0 - 192.168.255.255 | 65,536 | Hem, små kontor |

### Egenskaper för privata IP

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ FÖRDELAR MED PRIVATA IP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Inte routbara på internet - fungerar bara lokalt
# ♻️ Återanvändbara - samma IP kan finnas i olika nätverk
# 🔒 Säkrare - inte direkt synliga från internet
# 💰 Gratis - ingen registrering behövs
# ⚠️ Kräver NAT för att nå internet
```

### Vanliga privata adresser

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 LOCALHOST (loopback - alltid din egen dator)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
127.0.0.1       # IPv4 localhost
::1             # IPv6 localhost

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚪 VANLIGA GATEWAY-ADRESSER (routern)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
192.168.1.1     # Vanligast för hemrouter
192.168.0.1     # Alternativ
10.0.0.1        # Företagsmiljö
172.16.0.1      # Företagsmiljö

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐳 DOCKER & KUBERNETES DEFAULT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
172.17.0.0/16   # Docker bridge network
10.96.0.0/12    # Kubernetes service CIDR
10.244.0.0/16   # Kubernetes pod CIDR (Flannel)
```

---

## 🌐 Publika IP-adresser

Publika IP-adresser är **globalt unika** och kan nås från var som helst på internet.

### Egenskaper för publika IP

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌍 PUBLIKA IP EGENSKAPER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ Globalt unika - varje IP finns bara en gång i världen
# 🌐 Routbara på internet - kan nås varifrån som helst
# 📝 Registrerade - tilldelas av ISP:er eller cloud providers
# 💰 Kostar pengar - särskilt statiska IP:er
```

### Statisk vs Dynamisk IP

| Typ | Beskrivning | Kostnad | Användning |
|-----|-------------|---------|------------|
| **Statisk** | Ändras aldrig | Extra avgift | Servrar, VPN, DNS |
| **Dynamisk** | Ändras periodiskt | Ingår ofta | Heminternet, mobil |

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📌 STATISK IP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Exempel: 203.0.113.42
# - Ändras aldrig
# - Perfekt för servrar
# - Kostar oftast extra
# - Behövs för: DNS, VPN-endpoints, viktiga tjänster

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 DYNAMISK IP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Ändras vid router-restart eller periodiskt
# - Ingår i internetabonnemang
# - Vanligt för hemmanvändare
# - Kan vara problem om du behöver fast adress
```

---

## 🔄 NAT - Network Address Translation

NAT är som en **"receptionist"** - när någon ringer utifrån ser de bara kontorets huvudnummer (publik IP), men receptionisten vet vilken intern telefon (privat IP) samtalet ska till.

### Hur NAT fungerar

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 NAT VISUALISERAT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Privat nätverk          NAT Router          Internet
# ┌─────────────────┐    ┌───────────┐    ┌─────────────────┐
# │ 192.168.1.10    │───▶│           │───▶│                 │
# │ 192.168.1.11    │───▶│ 203.0.113.1 ───▶│   google.com    │
# │ 192.168.1.12    │───▶│           │───▶│                 │
# └─────────────────┘    └───────────┘    └─────────────────┘
#   (Privata IPs)         (Publik IP)      (Internet)

# Alla enheter delar EN publik IP!
# Routern översätter mellan privat ↔ publik
```

### NAT-processen steg för steg

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⬆️ UTGÅENDE TRAFIK (privat → internet)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Din dator (192.168.1.10) vill besöka google.com
# 2. Routern ändrar "från-adressen" till 203.0.113.1 (publik IP)
# 3. Routern kommer ihåg: "detta paket kom från 192.168.1.10"
# 4. Paketet skickas ut med publik IP
# 5. När svaret kommer → routern vet att skicka till 192.168.1.10

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⬇️ INKOMMANDE TRAFIK (internet → privat)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. Någon från internet försöker nå 203.0.113.1
# 2. Routern måste veta vilken intern dator som ska få paketet
# 3. Kräver: port forwarding ELLER att intern dator initierat först
```

### Fördelar med NAT

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ NAT FÖRDELAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💰 Sparar IP-adresser - många enheter delar en publik IP
# 🔒 Ökar säkerhet - interna datorer är inte direkt synliga
# 🎛️ Enkelt att hantera - bara routern behöver publik IP
```

### NAT-typer

| Typ | Riktning | Användning |
|-----|----------|------------|
| **SNAT** (Source NAT) | Privat → Publik | Utgående anslutningar |
| **DNAT** (Destination NAT) | Publik → Privat | Port forwarding, load balancing |

---

## ☁️ Cloud Provider IP-konfiguration

### AWS

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟠 AWS IP-KONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Privata IPs
# - VPC default: 10.0.0.0/16
# - EC2 instances får automatiskt privat IP
# - Endast åtkomlig inom VPC

# Publika IPs
# - Elastic IP (statisk, reserverad)
# - Auto-assigned public IP (dynamisk)
# - Internet Gateway krävs för internet-åtkomst
```

### Azure

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔵 AZURE IP-KONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Privata IPs
# - VNet default: 10.0.0.0/16
# - VM får automatiskt privat IP
# - Endast åtkomlig inom VNet

# Publika IPs
# - Public IP resource (statisk/dynamisk)
# - Load Balancer IP
# - Application Gateway IP
```

### GCP

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟢 GCP IP-KONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Privata IPs
# - VPC default: 10.128.0.0/9
# - VM får automatiskt privat IP
# - Endast åtkomlig inom VPC

# Publika IPs
# - Static external IP
# - Ephemeral external IP (försvinner vid stop)
# - Load balancer IP
```

---

## 🔍 Kontrollera IP-adresser

### Linux-kommandon

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 VISA ALLA IP-ADRESSER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ip addr show              # Moderna Linux
ifconfig                  # Äldre kommando

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 FILTRERA PÅ IP-VERSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ip -4 addr show           # Endast IPv4
ip -6 addr show           # Endast IPv6

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔌 SPECIFIKT NÄTVERKSKORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ip addr show eth0         # Visa specifik interface
ip addr show ens33        # VMware interface

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 HITTA DIN PUBLIKA IP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
curl ifconfig.me          # Enklast
curl ipinfo.io/ip         # Alternativ
curl icanhazip.com        # Alternativ
curl ipecho.net/plain     # Alternativ

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚦 KOLLA ROUTING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ip route                  # Visa routing-tabell
ip route get 8.8.8.8      # Vilken route används till Google DNS?
```

---

## ⚙️ Konfigurera statisk IP (Linux)

```yaml
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 UBUNTU NETPLAN (/etc/netplan/50-cloud-init.yaml)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
network:
  version: 2
  ethernets:
    eth0:
      addresses:
        - 192.168.1.100/24      # Statisk IP + subnet mask
      routes:
        - to: default
          via: 192.168.1.1      # Gateway (routern)
      nameservers:
        addresses:
          - 8.8.8.8             # Google DNS
          - 8.8.4.4             # Google DNS backup

# Applicera: sudo netplan apply
```

---

## 🛡️ Säkerhetsöverväganden

### Privata IP - säkrare men inte immun

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔒 PRIVATA IP SÄKERHET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ Inte direkt åtkomliga från internet
# ✅ Kräver VPN eller port forwarding
# ✅ Bra för interna tjänster

# ⚠️ MEN - behöver fortfarande brandvägg!
# - Defense in depth
# - Interna hot existerar också
```

### Publika IP - extra försiktighet krävs

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ PUBLIK IP SÄKERHET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❗ Direkt åtkomlig från hela internet
# ❗ Konstant under attack (bots, scanners)
# ❗ Behöver starka brandväggsregler

# 🛡️ Skydda med:
# - Security groups (cloud)
# - iptables/ufw (Linux)
# - Minimera öppna portar
# - Regelbundna uppdateringar
```

---

## ✨ Best Practices

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣ ANVÄND PRIVATA IP FÖR INTERNA TJÄNSTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DB_HOST=10.0.1.50       # Databas på privat IP
CACHE_HOST=10.0.1.51    # Redis på privat IP
APP_HOST=10.0.1.100     # App-server på privat IP

# Endast exponera vad som behövs!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣ ANVÄND LOAD BALANCER FÖR PUBLIK ÅTKOMST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Exponera INTE servrar direkt
# ✅ Använd load balancer med publik IP
# ✅ Servrar stannar på privata IPs

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣ RESERVERA STATISKA IP FÖR KRITISKA TJÄNSTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - DNS-servrar
# - VPN-endpoints
# - Tjänster som behöver brandväggsregler

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣ DOKUMENTERA IP-ANVÄNDNING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Håll koll på vilka IP:er som används
# - Undvik konflikter
# - Använd IP Address Management (IPAM) verktyg
```

---

## ✅ Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Privata IP** | 10.x.x.x, 172.16-31.x.x, 192.168.x.x |
| **Publika IP** | Globalt unika, routbara på internet |
| **NAT** | Översätter privat ↔ publik |
| **Statisk IP** | Ändras aldrig, kostar extra |
| **Dynamisk IP** | Ändras periodiskt, ofta gratis |
| **Localhost** | 127.0.0.1 (alltid din egen dator) |

**Kom ihåg:**
- 🏠 Använd privata IP:er för interna tjänster
- 🌐 Använd publika IP:er bara när nödvändigt
- 🔒 Skydda alltid publika tjänster med brandvägg
- 📝 Dokumentera din IP-plan
- 🎯 Load balancer framför servrar, inte direkt exponering
""",
        },
        {
            "title": "Portar och Tjänster",
            "slug": "ports-and-services",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Portar och Tjänster

## 🎯 Varför portar är essentiellt för DevOps

Port-kunskap är kritiskt för:

| Användningsområde | Beskrivning |
|-------------------|-------------|
| **Service configuration** | Konfigurera vilka portar tjänster använder |
| **Security** | Brandväggsregler, begränsa åtkomst |
| **Troubleshooting** | Felsöka anslutningsproblem |
| **Load balancing** | Distribuera trafik till rätt portar |
| **Container networking** | Docker port mapping |
| **Service discovery** | Hitta tjänster i nätverk |

---

## 📊 Port Grunderna

### Vad är en port?

En port är som ett **"rumnummer"** på ett hotell - IP-adressen är hotellet (datorn), och porten är vilket rum (programmet) du vill nå.

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 PORT BASICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Port = Communication endpoint
# En "endpoint" - en specifik plats där kommunikation sker
# Tänk på det som en dörr som program kan öppna

# Range: 0 - 65535 (16-bit nummer)
# 2^16 = 65536 möjliga portar
# Mer än tillräckligt för alla program

# IP-adress + Port = Socket
# Identifierar EXAKT vilket program på vilken dator
# Tänk: "Hotell 192.168.1.100, rum 80"

# Exempel:
192.168.1.100:80
│             │
│             └── Port 80 (webbserver)
└── IP-adress (vilken dator)
```

---

## 📋 Port-områden

Portar är uppdelade i tre kategorier:

### Well-known Ports (0 - 1023)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔒 SYSTEM PORTS (0-1023)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡ Reserverade för systemtjänster
# 🔐 Kräver root/admin för att öppna
# 📌 Standardiserade användningar

# Vanliga:
22    # SSH - Secure Shell
80    # HTTP - Web (okrypterad)
443   # HTTPS - Web (krypterad)
53    # DNS - Domain Name System
25    # SMTP - Mail
```

### Registered Ports (1024 - 49151)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 REGISTERED PORTS (1024-49151)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 Registrerade hos IANA
# 🔓 Kräver inte root
# 🎯 Vanliga applikationer

# Vanliga:
3306   # MySQL
5432   # PostgreSQL
27017  # MongoDB
6379   # Redis
8080   # Alternativ HTTP
```

### Dynamic/Private Ports (49152 - 65535)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 EPHEMERAL PORTS (49152-65535)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Tillfälliga (ephemeral)
# 🎲 Tilldelas automatiskt av OS
# 📤 Används för utgående anslutningar

# När du besöker google.com:
# - Din dator använder t.ex. port 52431 (tillfällig)
# - Ansluter till google.com:443
# - Svaret kommer tillbaka till din port 52431
```

### Sammanfattning port-områden

| Kategori | Range | Beskrivning | Root krävs |
|----------|-------|-------------|------------|
| **Well-known** | 0-1023 | Systemtjänster | ✅ Ja |
| **Registered** | 1024-49151 | Applikationer | ❌ Nej |
| **Dynamic** | 49152-65535 | Tillfälliga | ❌ Nej |

---

## 🌐 Vanliga portar att känna till

### Web Services

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 HTTP / HTTPS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
80     # HTTP - okrypterad webbtrafik
443    # HTTPS - krypterad webbtrafik
8080   # Alternativ HTTP (ofta för appar)
8443   # Alternativ HTTPS
8000   # Utvecklingsservrar (Django, etc)
3000   # Node.js/React dev server

# Exempel-URLer:
# http://example.com      → port 80 (implicit)
# https://example.com     → port 443 (implicit)
# http://localhost:8080   → port 8080 (explicit)
```

### Databaser

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗄️ DATABASER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3306   # MySQL / MariaDB
5432   # PostgreSQL
27017  # MongoDB
6379   # Redis
9200   # Elasticsearch (HTTP API)
9300   # Elasticsearch (transport)
```

### Remote Access

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 FJÄRRÅTKOMST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
22     # SSH (standard)
2222   # SSH (alternativ, för säkerhet)
3389   # RDP - Remote Desktop (Windows)
5900   # VNC
```

### E-post

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📧 E-POST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
25     # SMTP (ofta blockerad av ISP)
587    # SMTP med TLS (submission)
465    # SMTP över SSL
143    # IMAP
993    # IMAP över SSL
110    # POP3
995    # POP3 över SSL
```

### DNS

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌍 DNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
53     # DNS (både UDP och TCP)
```

---

## 🔍 Kontrollera portar

### Lista lyssnande portar

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 VISA LYSSNANDE PORTAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Med ss (modern, rekommenderas)
ss -tlnp                 # TCP lyssnande portar
ss -ulnp                 # UDP lyssnande portar
ss -tlnp | grep :80      # Specifik port

# Med netstat (äldre)
netstat -tlnp            # TCP lyssnande portar
netstat -ulnp            # UDP lyssnande portar

# Med lsof
lsof -i :80              # Vad använder port 80?
lsof -i -P -n | grep LISTEN
```

### Testa port-anslutning

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧪 TESTA PORTAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Med telnet
telnet hostname 80
telnet 192.168.1.100 3306

# Med netcat (nc) - snabbast!
nc -zv hostname 80           # TCP
nc -zv 192.168.1.100 3306    # TCP
nc -zv -u hostname 53        # UDP

# Med curl
curl http://hostname:80
curl -v telnet://hostname:3306

# Med nmap (port scanning)
nmap -p 80,443,22 hostname       # Specifika portar
nmap -p 1-1000 hostname          # Port range
```

### Snabbkoll om port är öppen

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡ SNABBTEST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# One-liner
timeout 1 bash -c "</dev/tcp/hostname/80" && echo "Open" || echo "Closed"

# Funktion för återanvändning
check_port() {
    local host=$1
    local port=$2
    timeout 1 bash -c "</dev/tcp/$host/$port" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "✅ Port $port is OPEN on $host"
    else
        echo "❌ Port $port is CLOSED on $host"
    fi
}

# Användning:
check_port google.com 80
check_port localhost 5432
```

---

## 🚇 Port Forwarding

### SSH Local Port Forwarding

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📥 LOCAL PORT FORWARDING (-L)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -L 8080:localhost:80 user@remote-server
# Din lokala port 8080 → remote serverns localhost:80

ssh -L 3306:db-server:3306 user@jump-host
# Din lokala port 3306 → db-server:3306 (via jump-host)

# Användning: Nå databaser bakom brandvägg
```

### SSH Remote Port Forwarding

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📤 REMOTE PORT FORWARDING (-R)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ssh -R 8080:localhost:80 user@remote-server
# Remote serverns port 8080 → din lokala port 80

# Användning: Exponera lokal utveckling via server
```

### Docker Port Mapping

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐳 DOCKER PORT MAPPING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
docker run -p 8080:80 nginx
#          │     │
#          │     └── Container port (nginx lyssnar)
#          └── Host port (du ansluter till)

# Flera portar
docker run -p 8080:80 -p 8443:443 nginx

# Exponera alla portar
docker run -P nginx     # Random host-portar

# Visa port mappings
docker port container_name
```

---

## 🔥 Brandvägg och portar

### UFW (Ubuntu)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛡️ UFW BRANDVÄGG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Tillåt port
sudo ufw allow 80
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Tillåt port-range
sudo ufw allow 8000:9000/tcp

# Blockera port
sudo ufw deny 3306

# Visa status
sudo ufw status
sudo ufw status numbered
```

### firewalld (RHEL/CentOS)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔥 FIREWALLD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Tillåt port
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --reload

# Tillåt tjänst
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

# Lista portar
sudo firewall-cmd --list-ports
```

### iptables

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ IPTABLES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Tillåt port
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Spara regler
sudo iptables-save > /etc/iptables/rules.v4
```

---

## ☁️ Cloud Security Groups

### AWS

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟠 AWS SECURITY GROUP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Inbound rule:
# Type: HTTP
# Protocol: TCP
# Port: 80
# Source: 0.0.0.0/0 (hela internet)

# Outbound rule:
# Type: All traffic
# Protocol: All
# Port: All
# Destination: 0.0.0.0/0
```

### Azure NSG

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔵 AZURE NSG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Inbound rule:
# Name: Allow-HTTP
# Priority: 1000
# Source: Any
# Destination: Any
# Protocol: TCP
# Port: 80
# Action: Allow
```

---

## 🔧 Hantera port-konflikter

### Hitta process som använder port

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍 HITTA PROCESS PÅ PORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Med lsof
sudo lsof -i :80
sudo lsof -i :3306

# Med ss
sudo ss -tlnp | grep :80

# Med fuser
sudo fuser 80/tcp
```

### Döda process på port

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ DÖDA PROCESS PÅ PORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Hitta PID
PID=$(sudo lsof -t -i:80)

# Döda processen
sudo kill $PID          # Graceful
sudo kill -9 $PID       # Force kill

# One-liner
sudo kill $(sudo lsof -t -i:80)
```

---

## ✨ Best Practices

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣ ANVÄND ICKE-STANDARD PORTAR FÖR SÄKERHET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Ändra SSH-port i /etc/ssh/sshd_config:
Port 2222

# Minskar automatiserade attacker

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣ DOKUMENTERA PORT-ANVÄNDNING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Håll lista på:
# - Vilka portar som används
# - Vilka tjänster som använder dem
# - Varför de behövs

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣ MINIMERA ÖPPNA PORTAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Öppna bara nödvändiga portar
# - Stäng oanvända portar
# - Använd brandvägg
# - Principle of least privilege

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣ ANVÄND LOAD BALANCER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Exponera inte alla servrar direkt
# - Load balancer på standard-portar
# - Backend-servrar på privata IP:er
```

---

## ✅ Sammanfattning

| Port-typ | Range | Beskrivning |
|----------|-------|-------------|
| **Well-known** | 0-1023 | Systemtjänster (root krävs) |
| **Registered** | 1024-49151 | Vanliga applikationer |
| **Dynamic** | 49152-65535 | Tillfälliga/ephemeral |

| Vanliga portar | Tjänst |
|---------------|--------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 27017 | MongoDB |

| Kommando | Användning |
|----------|------------|
| `ss -tlnp` | Lista lyssnande portar |
| `nc -zv host port` | Testa port |
| `lsof -i :port` | Vad använder porten? |
| `sudo ufw allow port` | Öppna port i brandvägg |

**Kom ihåg:**
- 🔒 Minimera öppna portar
- 📝 Dokumentera port-användning
- 🛡️ Använd brandvägg alltid
- 🔍 `ss -tlnp` och `nc -zv` är dina vänner
""",
        },
        {
            "title": "Hosts och Hostnames",
            "slug": "hosts-and-hostnames",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Hosts och Hostnames

## 🎯 Varför host-kunskap är kritiskt för DevOps

Host-kunskap är essentiellt för:

| Användningsområde | Beskrivning |
|-------------------|-------------|
| **Service discovery** | Hitta tjänster i nätverket |
| **DNS configuration** | Konfigurera namnupplösning |
| **Load balancing** | Distribuera trafik till rätt servrar |
| **Container orchestration** | Docker, Kubernetes networking |
| **Troubleshooting** | Felsöka nätverksproblem |
| **Service communication** | Tjänster som pratar med varandra |

---

## 🖥️ Vad är en Host?

### Host Definition

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖥️ HOST = VALFRI ENHET PÅ ETT NÄTVERK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Exempel på hosts:
# - Datorer
# - Servrar
# - Routrar
# - Skrivare
# - IoT-enheter
# - Containers
# - Virtuella maskiner
```

### Host Identification

Varje host kan identifieras på flera sätt - tänk på det som olika "namn" för samma enhet:

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍 OLIKA SÄTT ATT IDENTIFIERA EN HOST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. IP-adress (192.168.1.100)
#    → "Gatadressen" - unik nummeradress på nätverket
#    → Vad datorer använder för att hitta varandra

# 2. Hostname (server.example.com)
#    → "Människovänligt namn" - lättare att komma ihåg
#    → DNS konverterar hostname → IP-adress

# 3. MAC-adress (00:1a:2b:3c:4d:5e)
#    → "Serienumret" - unikt för varje nätverkskort
#    → Hårdvarunivå, ändras inte

# Analogi:
# IP-adress    = Gatadressen
# Hostname     = Namnet på huset
# MAC-adress   = Serienumret på dörrlåset
```

---

## 🏷️ Hostnames

### Hostname-typer

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📛 SHORT HOSTNAME
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
hostname
# Output: server1

# Bara maskinens namn, utan domän
# Användbart inom samma domän

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 FQDN (Fully Qualified Domain Name)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
hostname -f
# Output: server1.example.com

# Fullständigt namn = hostname + domän
# Unikt över hela internet!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏢 DOMAIN NAME
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
hostname -d
# Output: example.com

# Bara domändelen
# Flera hosts kan tillhöra samma domän
```

### Sätta hostname

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ ÄNDRA HOSTNAME (Linux systemd)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Sätt short hostname
sudo hostnamectl set-hostname server1

# Sätt FQDN
sudo hostnamectl set-hostname server1.example.com

# Verifiera
hostnamectl

# Alternativ metod (äldre)
sudo hostname server1
echo "server1" | sudo tee /etc/hostname
```

---

## 📁 /etc/hosts-filen

`/etc/hosts` är en lokal "telefonbok" som mappar hostnames till IP-adresser. Den kontrolleras **FÖRE** DNS!

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📖 FORMAT: IP_address   hostname   aliases
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Loopback (alltid med)
127.0.0.1       localhost
127.0.0.1       localhost.localdomain
::1             localhost6

# Egna mappningar
192.168.1.100   server1.example.com server1
192.168.1.101   db.example.com db
10.0.0.50       api.internal api

# Visa innehåll
cat /etc/hosts

# Testa
ping server1
ping db.example.com
```

### Viktigt om /etc/hosts

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚠️ /etc/hosts KONTROLLERAS FÖRE DNS!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Om hostname finns i /etc/hosts:
# → Den IP:n används direkt
# → DNS tillfrågas INTE

# Användningsområden:
# ✅ Lokal utveckling
# ✅ Snabbare åtkomst till vanliga servrar
# ✅ Temporära overrides
# ❌ Inte för produktion i stor skala (använd DNS)
```

---

## 🌐 DNS-upplösning

### Hur DNS fungerar

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 DNS-PROCESSEN STEG FÖR STEG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. Program begär: server1.example.com
#    ↓
# 2. System kollar /etc/hosts FÖRST
#    ↓
# 3. Om inte hittad → frågar DNS-server
#    ↓
# 4. DNS-server returnerar IP-adress
#    ↓
# 5. Program ansluter till IP:n

# Analogi: DNS är som en telefonbok
# Du slår upp namnet (hostname) för att hitta numret (IP)
# Sedan ringer du numret!
```

### DNS Lookup-kommandon

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍 DNS LOOKUP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Med host (enklast)
host server1.example.com
host 192.168.1.100              # Reverse lookup

# Med nslookup
nslookup server1.example.com
nslookup 192.168.1.100

# Med dig (mest detaljerat)
dig server1.example.com
dig +short server1.example.com  # Bara IP:n
dig @8.8.8.8 server1.example.com  # Använd specifik DNS

# Med getent (kontrollerar /etc/hosts också)
getent hosts server1.example.com
```

### DNS-konfiguration

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ /etc/resolv.conf
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# DNS-servrar
nameserver 8.8.8.8       # Google DNS
nameserver 8.8.4.4       # Google DNS backup
nameserver 1.1.1.1       # Cloudflare DNS

# Sökdomäner (så du kan skriva "server1" istället för "server1.example.com")
search example.com internal.local

# Visa
cat /etc/resolv.conf

# Systemd
systemd-resolve --status
```

---

## 🔌 Nätverksinterface

### Interface-namn

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔌 INTERFACE-NAMNKONVENTIONER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Traditionellt
eth0, eth1    # Ethernet
wlan0         # Wireless
lo            # Loopback (127.0.0.1)

# Systemd (predictable naming)
enp3s0        # Ethernet PCI
wlp2s0        # Wireless PCI
ens33         # VMware ethernet
```

### Visa interface-info

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 VISA INTERFACE OCH IP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Lista interfaces
ip link show
ifconfig                # Äldre

# Visa IP-adresser
ip addr show
ip -4 addr show         # Bara IPv4

# Visa routing
ip route show
route -n
```

---

## 🏢 Host-typer

### Server Hosts

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖥️ SERVRAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
web.example.com     → 192.168.1.10    # Webbserver
db.example.com      → 192.168.1.20    # Databas
api.example.com     → 192.168.1.30    # API-server
```

### Nätverksenheter

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 NÄTVERKSENHETER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
gateway.example.com → 192.168.1.1     # Router/Gateway
switch1.example.com                    # Switch
fw.example.com                         # Brandvägg
```

---

## 🔎 Service Discovery

### Statisk konfiguration

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📌 STATISK CONFIG
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Hårdkodad i config
DB_HOST=db.example.com
API_HOST=api.example.com

# /etc/hosts
192.168.1.20 db.example.com
192.168.1.30 api.example.com
```

### DNS-baserad discovery

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 DNS-BASERAD DISCOVERY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Flera A-records för load balancing
api.example.com → 192.168.1.30
api.example.com → 192.168.1.31
api.example.com → 192.168.1.32
# DNS roterar mellan dessa (round-robin)
```

---

## 🐳 Container Hosts

### Docker

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐳 DOCKER HOSTNAMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Sätt container hostname
docker run --hostname mycontainer nginx

# Network alias
docker run --network-alias db mysql

# Custom network (containers kan nå varandra via namn)
docker network create mynetwork
docker run --network mynetwork --name db mysql
docker run --network mynetwork --name app nginx
# app kan nå db via "db"
```

### Kubernetes

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ☸️ KUBERNETES SERVICE NAMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Service name = hostname
# Service: database

# Kort form (samma namespace)
database

# Full FQDN
database.default.svc.cluster.local
```

---

## ☁️ Cloud Hosts

### AWS

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟠 AWS HOSTNAMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Privat DNS
ip-192-168-1-100.ec2.internal

# Publik DNS
ec2-1-2-3-4.compute-1.amazonaws.com
```

### Azure / GCP

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔵 AZURE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
vmname.region.cloudapp.azure.com

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟢 GCP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
instance-name.zone.c.project-id.internal
```

---

## 🧪 Testa host-anslutning

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📡 PING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ping server1.example.com          # Ping hostname
ping 192.168.1.100                # Ping IP
ping -c 4 server1.example.com     # Bara 4 paket

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔀 TRACEROUTE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
traceroute server1.example.com    # Visa vägen
tracepath server1.example.com     # Alternativ

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔌 TESTA PORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
telnet server1.example.com 80     # Testa port 80
nc -zv server1.example.com 80     # Netcat
```

---

## ✨ Best Practices

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣ ANVÄND BESKRIVANDE HOSTNAMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ✅ BRA
web-prod-01.example.com
db-prod-01.example.com
api-staging-01.example.com

# ❌ DÅLIGT
server1
host1
machine1

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣ NAMNKONVENTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Format: {service}-{environment}-{number}.{domain}
# web-prod-01.example.com
# db-staging-02.example.com

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣ ANVÄND DNS I PRODUKTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# /etc/hosts bara för lokal utveckling
# DNS för allt annat

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣ DOKUMENTERA HOST-MAPPNINGAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Hostname → IP-mappningar
# - Syfte med varje host
# - Vilka tjänster som körs
```

---

## ✅ Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Host** | Valfri enhet på nätverket |
| **Hostname** | Människovänligt namn för host |
| **FQDN** | Fullständigt kvalificerat domännamn |
| **DNS** | Översätter hostname → IP |
| **/etc/hosts** | Lokal namnupplösning (före DNS) |
| **Service discovery** | Hitta tjänster via namn |

| Kommando | Användning |
|----------|------------|
| `hostname` | Visa/sätt hostname |
| `hostname -f` | Visa FQDN |
| `cat /etc/hosts` | Visa lokala mappningar |
| `dig hostname` | DNS lookup |
| `host hostname` | Enkel DNS lookup |
| `ping hostname` | Testa anslutning |

**Kom ihåg:**
- 🏷️ Använd beskrivande hostnames
- 📁 /etc/hosts kontrolleras före DNS
- 🌐 Använd DNS i produktion
- 📝 Dokumentera alla host-mappningar
- 🧪 `ping` och `dig` är dina vänner
""",
        },
        {
            "title": "Dataöverföring: Bytes och Bandwidth",
            "slug": "data-transfer-bytes-bandwidth",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 75,
            "content": """# Dataöverföring: Bytes och Bandwidth

## 🎯 Varför data transfer-kunskap är essentiellt för DevOps

Data transfer-kunskap är kritiskt för:

| Användningsområde | Beskrivning |
|-------------------|-------------|
| **Performance optimization** | Optimera överföringshastigheter |
| **Capacity planning** | Planera nätverkskapacitet |
| **Troubleshooting** | Felsöka långsamma nätverk |
| **Cost optimization** | Minimera cloud-kostnader (egress) |
| **Monitoring** | Övervaka bandwidth-användning |
| **Bandwidth management** | Hantera nätverksresurser |

---

## 📊 Dataenheter: Bits vs Bytes

### Den kritiska skillnaden

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 BIT (liten b) = HASTIGHET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Bit (b) = Minsta enheten (0 eller 1)
# Används för: HASTIGHET (data rates, bandwidth)
# Exempel: 100 Mbps = 100 megabit per sekund

# Detta är vad du ser när du mäter internet-hastighet
# ISP:er annonserar i bits: "100 Mbps internet"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 BYTE (stor B) = STORLEK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Byte (B) = 8 bits
# Används för: STORLEK (filstorlekar, lagring)
# Exempel: 100 MB = 100 megabyte

# Detta är vad du ser för filstorlekar
# "1 GB fil" = 1 gigabyte
```

### ⚠️ Viktigt: 1 Byte = 8 bits

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 KONVERTERING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1 Byte = 8 bits
# Så: 100 Mbps (bits) = 12.5 MBps (bytes)
#     100 ÷ 8 = 12.5

# DÄRFÖR kan din "100 Mbps" internet
# INTE överföra 100 MB per sekund!
# Den kan överföra 12.5 MB per sekund

# Detta är en av de vanligaste förvirringarna i nätverk!
```

### Sammanfattning bits vs bytes

| Enhet | Symbol | Användning | Exempel |
|-------|--------|------------|---------|
| **Bit** | b (liten) | Hastighet | 100 M**b**ps |
| **Byte** | B (stor) | Storlek | 100 M**B** fil |
| **Konvertering** | | 1 Byte = 8 bits | |

---

## 📐 Datastorleksenheter

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 STORLEK (Bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Bit (b)       = 1 bit
# Byte (B)      = 8 bits
# Kilobyte (KB) = 1,024 bytes (2^10)
# Megabyte (MB) = 1,024 KB = ~1 miljon bytes
# Gigabyte (GB) = 1,024 MB = ~1 miljard bytes
# Terabyte (TB) = 1,024 GB

# OBS: Ibland används 1,000 istället för 1,024 (decimal vs binär)
```

---

## ⚡ Datahastighetsenheter

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 HASTIGHET (bits per sekund)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# bps  = bits per second
# Kbps = Kilobits per second (1,000 bps)
# Mbps = Megabits per second (1,000,000 bps)
# Gbps = Gigabits per second (1,000,000,000 bps)

# Alternativt (bytes):
# Bps  = Bytes per second
# KBps = Kilobytes per second
# MBps = Megabytes per second
```

---

## 📶 Bandwidth

### Vad är Bandwidth?

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📶 BANDWIDTH = MAXIMAL KAPACITET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Bandwidth är den MAXIMALA dataöverföringshastigheten
# Tänk på det som "vägens bredd"
# - Bredare väg = mer trafik kan passera
# - 100 Mbps = max 100 megabit per sekund

# ⚠️ OBS: Bandwidth är kapacitet, inte "hastighet"!
# Du kan ha hög bandwidth men fortfarande hög latency
```

### Analogi: Motorvägen

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛣️ MOTORVÄGSANALOGI
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Bandwidth = Antal filer på vägen
# - 4-filig motorväg kan hantera mer trafik än 2-filig
# - Men bilarna kör inte nödvändigtvis SNABBARE

# Latency = Hur lång tid att köra sträckan
# - Även på 4-filig väg tar det tid att nå destinationen
# - Hög bandwidth ≠ låg latency!
```

### Vanliga bandwidths

| Miljö | Bandwidth | Användning |
|-------|-----------|------------|
| **Hem (basic)** | 10 Mbps | Surfning, e-post |
| **Hem (standard)** | 50-100 Mbps | Streaming, gaming |
| **Hem (snabbt)** | 1 Gbps | Fiber, flera användare |
| **Datacenter** | 1-10 Gbps | Standard server |
| **Enterprise** | 10-100 Gbps | Hög prestanda |

---

## 🆚 Bandwidth vs Latency

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 SKILLNADEN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Bandwidth = HUR MYCKET data per sekund
# Latency   = HUR LÅNG TID innan data anländer

# Hög bandwidth + hög latency:
# - Kan överföra mycket data
# - Men tar tid att starta
# - Exempel: Satellit-internet

# Låg bandwidth + låg latency:
# - Snabb respons
# - Men begränsad throughput
# - Exempel: Äldre modem med bra ping
```

---

## 🧮 Beräkna överföringstid

### Formeln

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📐 FORMEL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Tid = Storlek / Hastighet

# VIKTIGT: Båda måste vara i samma enhet!
# Storlek i bits, hastighet i bits per sekund
```

### Praktiska exempel

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 EXEMPEL 1: 1 GB fil över 100 Mbps
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Steg 1: Konvertera storlek till bits
# 1 GB = 1,000 MB = 8,000 Mbits (1 byte = 8 bits)

# Steg 2: Beräkna tid
# Tid = 8,000 Mbits / 100 Mbps = 80 sekunder

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 EXEMPEL 2: 10 GB fil över 1 Gbps
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 10 GB = 80,000 Mbits = 80 Gbits
# Tid = 80 Gbits / 1 Gbps = 80 sekunder

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 EXEMPEL 3: 100 MB fil över 10 Mbps
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 100 MB = 800 Mbits
# Tid = 800 Mbits / 10 Mbps = 80 sekunder
```

### Snabbreferens

| Filstorlek | 10 Mbps | 100 Mbps | 1 Gbps |
|------------|---------|----------|--------|
| 100 MB | 80 sek | 8 sek | 0.8 sek |
| 1 GB | 13 min | 80 sek | 8 sek |
| 10 GB | 2.2 tim | 13 min | 80 sek |

---

## 📈 Throughput (faktisk hastighet)

### Teoretisk vs faktisk

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 VERKLIG PRESTANDA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 100 Mbps anslutning:
# - Teoretiskt: 100 Mbps
# - Faktiskt:   ~90-95 Mbps (90-95%)

# Varför? OVERHEAD:
# - Protocol headers (TCP/IP ~40 bytes/paket)
# - Error correction
# - Retransmissions (förlorade paket)
# - Network congestion (trängsel)

# ✅ 90-95% av teoretisk bandwidth är NORMALT!
```

---

## 🔍 Mäta nätverksprestanda

### Hastighetstest

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧪 HASTIGHETSTEST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Med speedtest-cli
speedtest-cli
speedtest-cli --simple

# Med curl (download speed)
curl -o /dev/null -s -w "%{speed_download}\\n" http://speedtest.example.com/file

# Med wget
wget --progress=bar:force http://speedtest.example.com/file
```

### Throughput-test med iperf3

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔬 IPERF3 (professionellt verktyg)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Server (mottagare)
iperf3 -s

# Client (sändare)
iperf3 -c server-ip
iperf3 -c server-ip -t 60     # 60 sekunder
iperf3 -c server-ip -P 4      # 4 parallella strömmar
```

### Övervakningsverktyg

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 MONITORING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# iftop (realtid per interface)
sudo iftop -i eth0

# nethogs (per process)
sudo nethogs

# vnstat (statistik över tid)
vnstat -i eth0
vnstat -h         # Per timme
vnstat -d         # Per dag

# Nätverksstatistik
ip -s link show eth0
cat /proc/net/dev
```

---

## ☁️ Cloud Data Transfer-kostnader

### AWS

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟠 AWS KOSTNADER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Data UT (egress) - KOSTAR PENGAR
# - Första 100 GB/månad: Gratis (vissa regioner)
# - Efter: ~$0.09 per GB

# Data IN (ingress) - GRATIS
# Samma region - GRATIS
# Cross-region - KOSTAR
```

### Azure / GCP

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔵 AZURE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Data UT: Första 5 GB/månad gratis, sedan varierande
# Data IN: Gratis

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🟢 GCP
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Data UT: Första 1 TB/månad gratis, sedan varierande
# Data IN: Gratis
```

---

## 🚀 Optimera dataöverföring

### Komprimering

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗜️ KOMPRIMERA FÖRE ÖVERFÖRING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Komprimera och överför
tar -czf archive.tar.gz files/
scp archive.tar.gz user@server:/path/

# rsync med komprimering
rsync -avz file user@server:/path/
#      -z = compress
```

### Delta-överföring (bara ändringar)

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 ÖVERFÖR BARA ÄNDRINGAR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# rsync skickar bara det som ändrats
rsync -av source/ dest/

# Inkrementella backups
tar --listed-incremental=snapshot.file -czf backup.tar.gz files/
```

### Caching och CDN

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌐 CDN FÖR STATISKT INNEHÅLL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Fördelar:
# - Cache vid edge locations (nära användarna)
# - Minskar load på origin server
# - Minskar egress-kostnader
# - Snabbare för användarna
```

---

## ✨ Best Practices

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣ ÖVERVAKA BANDWIDTH-ANVÄNDNING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Tracka användning över tid
# - Identifiera toppar
# - Planera kapacitet

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣ OPTIMERA DATAÖVERFÖRING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Använd komprimering
# - Aktivera caching
# - Använd CDN för statiskt innehåll
# - Minimera onödig dataöverföring

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣ FÖRSTÅ CLOUD-KOSTNADER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Data UT (egress) kostar pengar
# - Minimera egress
# - Använd samma region när möjligt
# - Cache vid edge

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣ SÄTT UPP LARM
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# - Larma vid hög bandwidth
# - Larma vid ovanliga mönster
# - Övervaka kostnader
```

---

## ✅ Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **Bit (b)** | Minsta enhet, används för hastighet |
| **Byte (B)** | 8 bits, används för storlek |
| **1 Byte** | = 8 bits (kritiskt att komma ihåg!) |
| **Bandwidth** | Maximal överföringshastighet (Mbps) |
| **Throughput** | Faktisk överföringshastighet |
| **Latency** | Fördröjning (ej samma som bandwidth) |

| Verktyg | Användning |
|---------|------------|
| `speedtest-cli` | Testa internet-hastighet |
| `iperf3` | Professionellt throughput-test |
| `iftop` | Realtids bandwidth per interface |
| `vnstat` | Statistik över tid |
| `nethogs` | Bandwidth per process |

**Kom ihåg:**
- 📊 **bits** (liten b) = hastighet, **Bytes** (stor B) = storlek
- 🔢 100 Mbps ≠ 100 MB/s (dividera med 8!)
- 📉 Förvänta dig 90-95% av teoretisk bandwidth
- 💰 Cloud egress kostar pengar - optimera!
- 🗜️ Komprimera data före överföring
""",
        },
        {
            "title": "Subnetting och CIDR",
            "slug": "subnetting-and-cidr",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 85,
            "content": """# Subnetting och CIDR

## Varfor subnetting-kunskap ar kritiskt for DevOps

Subnetting ar grundlaggande for:

| Anvandningsomrade | Beskrivning |
|-------------------|-------------|
| **Cloud VPC design** | Planera natverksarkitektur i AWS/Azure/GCP |
| **Network segmentation** | Dela upp natverk i logiska delar |
| **Security isolation** | Isolera kansliga system |
| **IP address planning** | Effektiv anvandning av IP-adresser |
| **Container networking** | Docker och Kubernetes subnets |
| **Multi-tenant architectures** | Separera kunder/miljoer |

---

## IP-adressens struktur

### IPv4-adress uppdelning

En IPv4-adress bestar av tva delar: natvverksdelen (vilket natverk) och varddelen (vilken specifik dator).

```bash
# ==============================================================
# IP-ADRESS UPPDELNING
# ==============================================================

192.168.1.100

# 192.168.1 = Natvverksdelen (Network portion)
# - Identifierar vilket natverk datorn tillhor
# - Tank pa det som "gatan"
# - Alla datorer med 192.168.1.x ar pa samma natverk
# - Bestams av subnet masken (t.ex. /24)

# 100 = Varddelen (Host portion)
# - Identifierar den specifika datorn
# - Tank pa det som "husnumret"
# - Kan variera fran 1 till 254 (0 och 255 ar reserverade)

# Totalt: 32 bitar
# - 4 bytes (4 x 8 = 32 bitar)
# - ~4.3 miljarder mojliga adresser
```

### Subnet Mask

Subnet mask definierar vilka bitar som ar natvverksdelen vs varddelen:

```bash
# ==============================================================
# SUBNET MASK EXEMPEL
# ==============================================================

# 255.255.255.0 = /24
#   Network:    192.168.1.0
#   Hosts:      192.168.1.1 - 192.168.1.254
#   Broadcast:  192.168.1.255
#   Anvandbara: 254 adresser

# 255.255.0.0 = /16
#   Network:    192.168.0.0
#   Hosts:      192.168.0.1 - 192.168.255.254
#   Anvandbara: 65,534 adresser
```

---

## CIDR-notation

### Vad ar CIDR?

CIDR (Classless Inter-Domain Routing) ar ett kompakt satt att beskriva IP-adress och natmask.

```bash
# ==============================================================
# CIDR FORMAT
# ==============================================================

# Format: IP_address/prefix_length

# Exempel:
192.168.1.0/24
# - 192.168.1.0 = Natverkets adress
# - /24 = De forsta 24 bitarna ar natvverksdelen
# - Ger 256 adresser (254 anvandbara)

10.0.0.0/8
# - 10.0.0.0 = Natverkets adress
# - /8 = De forsta 8 bitarna ar natvverksdelen
# - Ger over 16 miljoner adresser

172.16.0.0/12
# - 172.16.0.0 = Natverkets adress
# - /12 = De forsta 12 bitarna ar natvverksdelen
# - Ger over en miljon adresser
```

### CIDR prefix-langder

| Prefix | Subnet Mask | Antal adresser | Anvandbara |
|--------|-------------|----------------|------------|
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /32 | 255.255.255.255 | 1 | 1 (host route) |

**/24 ar vanligast for subnets**

---

## Vanliga CIDR-block

```bash
# ==============================================================
# PRIVATA RANGES (RFC 1918)
# ==============================================================

10.0.0.0/8          # 10.0.0.0 - 10.255.255.255 (Class A)
172.16.0.0/12       # 172.16.0.0 - 172.31.255.255 (Class B)
192.168.0.0/16      # 192.168.0.0 - 192.168.255.255 (Class C)

# ==============================================================
# SPECIELLA RANGES
# ==============================================================

127.0.0.0/8         # Loopback (localhost)
169.254.0.0/16      # Link-local (auto-assigned)
0.0.0.0/0           # Default route (alla adresser)
```

---

## Subnetting grunderna

### Varfor subnetta?

```bash
# ==============================================================
# FORDELAR MED SUBNETTING
# ==============================================================

# 1. Network segmentation
#    - Dela upp stora natverk i mindre delar

# 2. Security isolation
#    - Separera kansliga system (databaser, admin)

# 3. Better organization
#    - Logisk uppdelning per avdelning/funktion

# 4. Reduced broadcast domains
#    - Minskar broadcast-trafik

# 5. Efficient IP usage
#    - Anvand bara de adresser du behover
```

### Subnet-berakning

```bash
# ==============================================================
# EXEMPEL: DELA UPP 192.168.1.0/24
# ==============================================================

# /24 subnet (original)
# Network:    192.168.1.0
# Netmask:    255.255.255.0
# Hosts:      192.168.1.1 - 192.168.1.254
# Broadcast:  192.168.1.255
# Anvandbara: 254 hosts

# /25 subnet (delat i 2)
# Subnet 1:   192.168.1.0/25   (192.168.1.1 - 192.168.1.126)
# Subnet 2:   192.168.1.128/25 (192.168.1.129 - 192.168.1.254)
# Anvandbara: 126 hosts per subnet

# /26 subnet (delat i 4)
# Subnet 1:   192.168.1.0/26   (192.168.1.1 - 192.168.1.62)
# Subnet 2:   192.168.1.64/26  (192.168.1.65 - 192.168.1.126)
# Subnet 3:   192.168.1.128/26 (192.168.1.129 - 192.168.1.190)
# Subnet 4:   192.168.1.192/26 (192.168.1.193 - 192.168.1.254)
# Anvandbara: 62 hosts per subnet
```

### Subnetting-verktyg

```bash
# ==============================================================
# VERKTYG FOR SUBNET-BERAKNING
# ==============================================================

# Med ipcalc
ipcalc 192.168.1.0/24
ipcalc 192.168.1.0/25
ipcalc 192.168.1.0/26

# Med sipcalc
sipcalc 192.168.1.0/24

# Online-kalkylatorer:
# - subnet-calculator.com
# - ipaddressguide.com
```

---

## VPC Subnetting i Cloud

### AWS VPC Exempel

```bash
# ==============================================================
# AWS VPC DESIGN
# ==============================================================

# VPC: 10.0.0.0/16 (65,536 adresser)

# Subnets:
10.0.1.0/24    # Public subnet (AZ-a)  - Load balancers
10.0.2.0/24    # Private subnet (AZ-a) - App servers
10.0.3.0/24    # Public subnet (AZ-b)  - Load balancers
10.0.4.0/24    # Private subnet (AZ-b) - App servers
10.0.5.0/24    # Database subnet (AZ-a)
10.0.6.0/24    # Database subnet (AZ-b)

# Varfor flera AZ?
# - High availability
# - Fault tolerance
```

### Azure VNet Exempel

```bash
# ==============================================================
# AZURE VNET DESIGN
# ==============================================================

# VNet: 10.0.0.0/16

# Subnets:
10.0.1.0/24    # Frontend
10.0.2.0/24    # Backend
10.0.3.0/24    # Database
10.0.4.0/24    # Gateway subnet
```

### GCP VPC Exempel

```bash
# ==============================================================
# GCP VPC DESIGN
# ==============================================================

# VPC: 10.0.0.0/16

# Subnets (per region):
10.0.1.0/24    # us-east1
10.0.2.0/24    # us-west1
10.0.3.0/24    # eu-west1
```

---

## Subnet-typer

### Public Subnet

```bash
# ==============================================================
# PUBLIC SUBNET
# ==============================================================

# Egenskaper:
# - Har Internet Gateway
# - Kan na internet direkt
# - For: Load balancers, NAT gateways, bastion hosts

# Exempel:
10.0.1.0/24    # Public subnet

# Route table:
# Destination     Target
# 10.0.0.0/16     local
# 0.0.0.0/0       igw-12345 (Internet Gateway)
```

### Private Subnet

```bash
# ==============================================================
# PRIVATE SUBNET
# ==============================================================

# Egenskaper:
# - Ingen direkt internet-atkomst
# - Behover NAT Gateway for utgaende trafik
# - For: Application servers, internal services

# Exempel:
10.0.2.0/24    # Private subnet

# Route table:
# Destination     Target
# 10.0.0.0/16     local
# 0.0.0.0/0       nat-12345 (NAT Gateway)
```

### Database Subnet

```bash
# ==============================================================
# DATABASE SUBNET
# ==============================================================

# Egenskaper:
# - Helt isolerat
# - Ingen internet-atkomst (ingen default route)
# - Endast atkomlig fran application subnets
# - For: Databaser, cache, interna tjanster

# Exempel:
10.0.5.0/24    # Database subnet

# Route table:
# Destination     Target
# 10.0.0.0/16     local
# (ingen 0.0.0.0/0 route!)
```

---

## Route Tables

### Route Table grunderna

```bash
# ==============================================================
# ROUTE TABLE KONCEPT
# ==============================================================

# Varje subnet har en route table
# Definierar var trafik ska skickas

# Default route (0.0.0.0/0):
# - Public subnet:  -> Internet Gateway
# - Private subnet: -> NAT Gateway
# - Database:       -> Ingen (isolerat)

# Local route (alltid med):
# - VPC CIDR -> local (intern VPC-trafik)
```

### Exempel Route Tables

```bash
# ==============================================================
# PUBLIC SUBNET ROUTE TABLE
# ==============================================================
# Destination      Target
# 10.0.0.0/16      local         (VPC internt)
# 0.0.0.0/0        igw-12345     (Internet)

# ==============================================================
# PRIVATE SUBNET ROUTE TABLE
# ==============================================================
# Destination      Target
# 10.0.0.0/16      local         (VPC internt)
# 0.0.0.0/0        nat-12345     (NAT for utgaende)

# ==============================================================
# DATABASE SUBNET ROUTE TABLE
# ==============================================================
# Destination      Target
# 10.0.0.0/16      local         (VPC internt endast)
```

---

## Subnet Sizing

### Planera subnets

```bash
# ==============================================================
# PLANERINGS-OVERVAGANDEN
# ==============================================================

# 1. Antal hosts som behovs
# 2. Framtida tillvaxt
# 3. Reserverade IP:er

# AWS reserverar 5 IP:er per subnet:
# - .0   Network address
# - .1   VPC router
# - .2   DNS
# - .3   Future use
# - .255 Broadcast

# Sa ett /24 subnet har 251 anvandbara (256 - 5)
```

### Vanliga storlekar

| CIDR | Totalt | Anvandbara (AWS) | Bra for |
|------|--------|------------------|---------|
| /28 | 16 | 11 | Sma subnets, point-to-point |
| /27 | 32 | 27 | Sma tjanster |
| /26 | 64 | 59 | Medelstora tjanster |
| /24 | 256 | 251 | Standard, de flesta subnets |
| /23 | 512 | 507 | Stora subnets |
| /22 | 1024 | 1019 | Mycket stora subnets |

---

## Best Practices

```bash
# ==============================================================
# 1. PLANERA FOR TILLVAXT
# ==============================================================
# - Anvand inte hela VPC for ett subnet
# - Lamna rum for expansion
# - Anvand /24 for de flesta subnets

# ==============================================================
# 2. SEGMENTERA PER FUNKTION
# ==============================================================
# Separata subnets for:
# - Public-facing services
# - Application servers
# - Databases
# - Management/admin

# ==============================================================
# 3. ANVAND KONSEKVENT STORLEK
# ==============================================================
# - Samma subnet-storlek nar mojligt
# - Gor hantering enklare
# - Forenklar routing

# ==============================================================
# 4. DOKUMENTERA SUBNET-ANVANDNING
# ==============================================================
# Dokumentera:
# - Subnet syfte
# - IP-ranges
# - Route tables
# - Security groups
```

---

## Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| **CIDR** | IP_address/prefix_length format |
| **/24** | Vanligaste subnet-storleken (256 adresser) |
| **Subnet mask** | Definierar network vs host bits |
| **Public subnet** | Har Internet Gateway |
| **Private subnet** | Behover NAT for internet |
| **Route table** | Styr var trafik gar |

| CIDR | Adresser | Typisk anvandning |
|------|----------|-------------------|
| /8 | 16M | Stora organisationer |
| /16 | 65K | VPC/VNet |
| /24 | 256 | Standard subnet |
| /26 | 64 | Mindre subnet |
| /32 | 1 | Host route |

**Kom ihag:**
- Planera for tillvaxt - anvand inte hela VPC direkt
- Segmentera per funktion (public/private/database)
- Dokumentera alla subnets och deras syfte
- /24 ar standard for de flesta subnets
- AWS reserverar 5 IP:er per subnet
""",
        },
        {
            "title": "Docker Compose Advanced Patterns",
            "slug": "docker-compose-advanced-patterns",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker Compose Advanced Patterns

## Varför behöver du kunna detta?

Grundläggande Compose räcker för utveckling, men produktion kräver mer:

- **Miljöspecifik konfiguration** (dev vs prod)
- **Healthchecks och restart policies**
- **Skalning och load balancing**

---

## Multiple Compose Files

```bash
# Bas-konfiguration
# docker-compose.yml
services:
  api:
    build: .
    environment:
      - DATABASE_URL=postgresql://db:5432/app

# Development overrides
# docker-compose.override.yml (laddas automatiskt)
services:
  api:
    volumes:
      - .:/app  # Hot reload
    environment:
      - DEBUG=true

# Production overrides
# docker-compose.prod.yml
services:
  api:
    image: myregistry/api:${VERSION}
    restart: always
    deploy:
      replicas: 3

# Kör med specifik override
docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

---

## Healthchecks

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

  # Vänta på att dependency är healthy
  api:
    depends_on:
      db:
        condition: service_healthy
```

---

## Environment Variables

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
      - .env.local
```

```bash
# .env
POSTGRES_PASSWORD=secret
API_KEY=abc123
```

---

## Profiles

```yaml
services:
  api:
    image: myapi
    # Alltid aktiv (inget profile)

  debug-tools:
    image: busybox
    profiles:
      - debug
    # Startas bara med: docker compose --profile debug up

  monitoring:
    image: prometheus
    profiles:
      - monitoring
      - production
```

```bash
# Starta med specifika profiles
docker compose --profile debug up
docker compose --profile monitoring --profile debug up
```

---

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
```

---

## Secrets

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
    environment: API_KEY
```

```bash
# I containern läses secrets från:
# /run/secrets/db_password
# /run/secrets/api_key
```

---

## Extension Fields (YAML anchors)

```yaml
# Återanvänd konfiguration
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
      <<: *common-env
      SERVICE_NAME: api
    healthcheck:
      <<: *default-healthcheck
      test: curl -f http://localhost:8000/health

  worker:
    environment:
      <<: *common-env
      SERVICE_NAME: worker
```

---

## Key Takeaways

- Använd **override files** för miljöspecifik config
- **Healthchecks** är kritiska för produktion
- **Profiles** för att gruppera valfria services
- **Secrets** för känslig data (inte environment variables)
""",
        },
        {
            "title": "Docker Security Best Practices",
            "slug": "docker-security-best-practices",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Security Best Practices

## Varför behöver du kunna detta?

Containers är inte automatiskt säkra. Du måste förstå:

- **Vanliga säkerhetsrisker** och hur du undviker dem
- **Principle of least privilege** för containers
- **Image scanning** för sårbarheter

---

## Kör ALDRIG som root

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

---

## Minimal Base Images

```dockerfile
# DÅLIGT - full OS med massa onödiga paket
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3

# BRA - minimal image
FROM python:3.11-slim

# BÄST (om möjligt) - distroless
FROM gcr.io/distroless/python3
```

```bash
# Jämför storlekar:
# ubuntu:22.04     ~77 MB
# python:3.11      ~1 GB
# python:3.11-slim ~150 MB
# distroless       ~50 MB
```

---

## Använd specifika tags

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

---

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

---

## Begränsa capabilities

```bash
# Containers får för många Linux capabilities by default
# Ta bort alla och lägg till bara det som behövs

docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myimage

# Vanliga capabilities:
# NET_BIND_SERVICE - bind to ports < 1024
# CHOWN - change file ownership
# SETUID/SETGID - change user/group ID
```

---

## Resource Limits

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

---

## Image Scanning

```bash
# Scanna image för sårbarheter
docker scout cves myimage
docker scout recommendations myimage

# Trivy (populärt open source alternativ)
trivy image myimage

# Snyk
snyk container test myimage
```

---

## Secrets Hantering

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

---

## Network Security

```bash
# Isolera containers i egna nätverk
docker network create --internal backend
# --internal = ingen internet-access

# Exponera bara nödvändiga portar
docker run -p 127.0.0.1:8080:8080 myimage  # Bara localhost
```

---

## Security Checklist

```bash
# ✅ Non-root user
# ✅ Minimal base image (slim/alpine/distroless)
# ✅ Specifika image tags
# ✅ Read-only filesystem där möjligt
# ✅ Dropped capabilities
# ✅ Resource limits
# ✅ No secrets i images/env vars
# ✅ Regelbunden image scanning
# ✅ Isolerade nätverk
```

---

## Key Takeaways

- **Kör aldrig som root** - skapa en appuser
- **Minimal images** = mindre attack surface
- **Scanna images** regelbundet för CVEs
- **Secrets hör inte hemma** i env vars eller Dockerfiles
""",
        },
        {
            "title": "Docker in Production",
            "slug": "docker-in-production",
            "difficulty": "hard",
            "estimated_minutes": 55,
            "xp_reward": 95,
            "content": """# Docker in Production

## Varför behöver du kunna detta?

Att köra Docker lokalt är en sak - produktion är en annan. Du måste förstå:

- **Logging och monitoring** för att veta vad som händer
- **Restart policies** för att hantera crashes
- **Resource management** för stabil drift

---

## Restart Policies

```bash
# no - starta aldrig om (default)
docker run --restart no myimage

# always - starta alltid om (även vid reboot)
docker run --restart always myimage

# unless-stopped - som always, men inte om manuellt stoppad
docker run --restart unless-stopped myimage

# on-failure - bara vid crash (exit code != 0)
docker run --restart on-failure:5 myimage  # Max 5 försök
```

```yaml
# docker-compose.yml
services:
  api:
    image: myapi
    restart: unless-stopped
```

---

## Logging

```bash
# Se loggar
docker logs container_name
docker logs -f container_name      # Follow
docker logs --tail 100 container_name
docker logs --since 1h container_name

# Log drivers
docker run --log-driver json-file \\
    --log-opt max-size=10m \\
    --log-opt max-file=3 \\
    myimage

# Centraliserad logging (exempel: Fluentd)
docker run --log-driver fluentd \\
    --log-opt fluentd-address=localhost:24224 \\
    myimage
```

---

## Monitoring

```bash
# Real-time stats
docker stats

# Format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Health status
docker inspect --format='{{.State.Health.Status}}' container_name
```

---

## Healthchecks

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

---

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
    # Ingen port exponerad utåt!

secrets:
  db_password:
    external: true

volumes:
  pgdata:
```

---

## Blue-Green Deployment

```bash
# Starta ny version
docker compose -p myapp-green up -d

# Testa att den fungerar
curl http://localhost:8081/health

# Byt trafik (via load balancer/nginx)
# ...

# Ta bort gamla versionen
docker compose -p myapp-blue down
```

---

## Rolling Updates

```bash
# Med Docker Swarm
docker service update --image myimage:v2 myservice

# Med Compose (manuellt)
docker compose pull
docker compose up -d --no-deps --build api
```

---

## Backup Strategy

```bash
# Backup volumes regelbundet
docker run --rm \\
    -v mydata:/source:ro \\
    -v $(pwd)/backups:/backup \\
    alpine tar czf /backup/mydata-$(date +%Y%m%d).tar.gz -C /source .

# Backup databas
docker exec postgres pg_dump -U postgres mydb > backup.sql
```

---

## Key Takeaways

- Använd `restart: unless-stopped` för produktionscontainers
- **Healthchecks** är obligatoriska i produktion
- **Resource limits** förhindrar att en container tar ner allt
- **Centraliserad logging** för att kunna felsöka
""",
        },
        {
            "title": "Docker Registry & Image Distribution",
            "slug": "docker-registry-image-distribution",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Registry & Image Distribution

## Varför behöver du kunna detta?

Images måste lagras och distribueras. Du måste förstå:

- **Hur registries fungerar** och vilka alternativ som finns
- **Push och pull** av images
- **Private registries** för företagsbruk

---

## Vad är ett Registry?

Ett registry är en lagringsplats för Docker images. Tänk på det som "npm för containers".

```bash
# Image naming convention
registry.example.com/namespace/repository:tag
│                    │         │          │
│                    │         │          └── Version (default: latest)
│                    │         └── Image name
│                    └── User/Organization
└── Registry URL (default: docker.io)
```

---

## Docker Hub (Public)

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

---

## Private Registries

```bash
# AWS ECR
aws ecr get-login-password --region eu-north-1 | \\
    docker login --username AWS --password-stdin 123456789.dkr.ecr.eu-north-1.amazonaws.com

docker tag myimage 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1
docker push 123456789.dkr.ecr.eu-north-1.amazonaws.com/myimage:v1

# Google Container Registry
gcloud auth configure-docker
docker tag myimage gcr.io/my-project/myimage:v1
docker push gcr.io/my-project/myimage:v1

# Azure Container Registry
az acr login --name myregistry
docker tag myimage myregistry.azurecr.io/myimage:v1
docker push myregistry.azurecr.io/myimage:v1

# GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag myimage ghcr.io/username/myimage:v1
docker push ghcr.io/username/myimage:v1
```

---

## Self-hosted Registry

```bash
# Starta eget registry
docker run -d -p 5000:5000 --name registry registry:2

# Använd det
docker tag myimage localhost:5000/myimage:v1
docker push localhost:5000/myimage:v1
docker pull localhost:5000/myimage:v1
```

---

## Image Tagging Strategy

```bash
# Semantisk versioning
myimage:1.0.0          # Specifik version
myimage:1.0            # Minor version
myimage:1              # Major version
myimage:latest         # Senaste (undvik i produktion!)

# Git-baserad
myimage:main           # Branch
myimage:abc123f        # Commit SHA
myimage:v1.2.3-abc123f # Version + SHA

# Timestamp
myimage:20241207-143022
```

---

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

---

## Key Takeaways

- **Docker Hub** för public images, **private registry** för företaget
- Använd **specifika tags** i produktion, aldrig `latest`
- **Multi-platform builds** för ARM/AMD64 kompatibilitet
- Logga in innan push/pull till private registries
""",
        },
        {
            "title": "Docker Multi-stage Builds",
            "slug": "docker-multi-stage-builds",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Multi-stage Builds

## Varför behöver du kunna detta?

Build-verktyg och dependencies behövs inte i produktion. Du måste kunna:

- **Separera build och runtime** för mindre images
- **Kopiera artefakter** mellan stages
- **Optimera för säkerhet** genom att exkludera build-verktyg

---

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

---

## Multi-stage lösningen

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

---

## Go Example (statisk binär)

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
# Image storlek: ~10-20 MB (bara binären!)
```

---

## Python Example

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

---

## React/Frontend Example

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

---

## Flera build stages

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

---

## Kopiera från externa images

```dockerfile
# Kopiera verktyg från annan image
FROM alpine
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/
COPY --from=hashicorp/terraform:latest /bin/terraform /usr/local/bin/
```

---

## Key Takeaways

- **Separera build och runtime** - dramatiskt mindre images
- `COPY --from=stage` kopierar filer mellan stages
- Bara **sista FROM** blir den slutliga imagen
- Använd **slim/alpine/scratch** för production stage
""",
        },
        {
            "title": "Docker Performance Optimization",
            "slug": "docker-performance-optimization",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker Performance Optimization

## Varför behöver du kunna detta?

Långsamma builds och stora images kostar tid och pengar. Du måste kunna:

- **Optimera build-tid** genom smart caching
- **Minska image-storlek** för snabbare deploys
- **Förbättra runtime-prestanda**

---

## Build Cache Optimization

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

---

## Layer Order Matters

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

---

## Minska antal layers

```dockerfile
# DÅLIGT - varje RUN skapar ett layer
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# BRA - kombinera till ett layer
RUN apt-get update && \\
    apt-get install -y \\
        curl \\
        git && \\
    rm -rf /var/lib/apt/lists/*
```

---

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
.nyc_output
dist
build
```

---

## BuildKit Features

```bash
# Aktivera BuildKit (snabbare builds)
export DOCKER_BUILDKIT=1
docker build .

# Eller
docker buildx build .

# Cache mount - cachar paketmanagers
FROM python:3.11
RUN --mount=type=cache,target=/root/.cache/pip \\
    pip install -r requirements.txt

# Bind mount - undviker COPY för build-time filer
RUN --mount=type=bind,source=package.json,target=/app/package.json \\
    npm install
```

---

## Image Size Reduction

```dockerfile
# 1. Välj minimal base image
FROM python:3.11-slim  # istället för python:3.11

# 2. Ta bort cache och temp-filer
RUN pip install --no-cache-dir -r requirements.txt

# 3. Ta bort package manager cache
RUN apt-get update && \\
    apt-get install -y curl && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*

# 4. Multi-stage build (kopiera bara det som behövs)
```

---

## Analysera image-storlek

```bash
# Se layers och storlekar
docker history myimage

# Dive - interaktiv analys
dive myimage

# Docker Scout
docker scout quickview myimage
```

---

## Runtime Performance

```bash
# Resource limits
docker run \\
    --cpus=2 \\
    --memory=2g \\
    --memory-swap=2g \\  # Disable swap
    myimage

# CPU pinning (specifika cores)
docker run --cpuset-cpus="0,1" myimage

# Ulimits
docker run --ulimit nofile=65535:65535 myimage
```

---

## Storage Driver

```bash
# Kolla aktuell storage driver
docker info | grep "Storage Driver"

# overlay2 är rekommenderat för de flesta
# Undvik devicemapper och aufs
```

---

## Key Takeaways

- **Ordning spelar roll** - sätt saker som ändras sällan först
- Använd **.dockerignore** för snabbare COPY
- **BuildKit** ger snabbare builds och bättre caching
- **Analysera images** med `dive` eller `docker history`
""",
        },
        {
            "title": "Docker Debugging & Troubleshooting",
            "slug": "docker-debugging-troubleshooting",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Debugging & Troubleshooting

## Varför behöver du kunna detta?

Containers kommer att krasha och bete sig konstigt. Du måste kunna:

- **Hitta vad som gick fel** via loggar och inspect
- **Debugga körande containers** utan att störa produktion
- **Hantera vanliga problem** snabbt

---

## Container startar inte

```bash
# Steg 1: Kolla loggar
docker logs container_name
docker logs --tail 50 container_name

# Steg 2: Kolla exit code
docker inspect container_name --format='{{.State.ExitCode}}'
# 0 = OK, 1 = Error, 137 = OOM/Kill, 143 = SIGTERM

# Steg 3: Kör interaktivt för att debugga
docker run -it --entrypoint sh myimage
docker run -it --entrypoint bash myimage

# Steg 4: Kolla events
docker events --since 10m
```

---

## Inspektera containers

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

---

## Debugga körande container

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

---

## Nätverksproblem

```bash
# Kolla container IP
docker inspect container_name --format='{{.NetworkSettings.IPAddress}}'

# Lista nätverk
docker network ls

# Inspektera nätverk
docker network inspect bridge

# Testa connectivity från container
docker exec container_name ping other_container
docker exec container_name curl http://other_container:8080
docker exec container_name nslookup other_container

# Kolla port mappings
docker port container_name
```

---

## Loggproblem

```bash
# Inga loggar? Appen kanske loggar till fil
docker exec container_name cat /var/log/app.log

# Loggar för stora? Kolla log settings
docker inspect container_name --format='{{json .HostConfig.LogConfig}}'

# Rensa loggar (json-file driver)
truncate -s 0 $(docker inspect --format='{{.LogPath}}' container_name)
```

---

## Disk/Storage problem

```bash
# Kolla disk usage
docker system df

# Detaljerad
docker system df -v

# Rensa oanvända resurser
docker system prune        # Containers, networks, images
docker system prune -a     # + alla oanvända images
docker system prune --volumes  # + volumes

# Kolla volume
docker volume inspect myvolume
```

---

## OOM (Out of Memory)

```bash
# Kolla om container blev OOM-killed
docker inspect container_name --format='{{.State.OOMKilled}}'

# Kolla memory limit vs usage
docker stats container_name --no-stream

# Öka memory limit
docker update --memory=2g container_name
```

---

## Image problem

```bash
# Image finns inte
docker pull myimage:tag  # Pulla explicit

# Kolla image layers
docker history myimage

# Inspektera image
docker inspect myimage

# Verifiera image
docker image inspect myimage --format='{{.Id}}'
```

---

## Debug Dockerfile

```bash
# Bygg med output
DOCKER_BUILDKIT=0 docker build -t myimage .

# Stanna vid specifik stage
docker build --target builder -t myimage-debug .

# Kör en "failed" build interaktivt
# 1. Hitta sista lyckade layer ID i build output
# 2. docker run -it <layer-id> sh
```

---

## Vanliga fel och lösningar

```bash
# "Permission denied"
# → Kolla att USER i Dockerfile har rätt rättigheter
# → Kolla volume permissions

# "Port already in use"
docker ps | grep :8080
docker stop container_using_port

# "No space left on device"
docker system prune -a --volumes

# "Cannot connect to Docker daemon"
sudo systemctl start docker
# Eller: lägg till user i docker-gruppen
```

---

## Key Takeaways

- **Loggar först** - `docker logs` är din bästa vän
- **Exit codes berättar** varför container stoppade
- `docker exec -it` för att **debugga körande containers**
- `docker system prune` när **disken är full**
""",
        },
        {
            "title": "Docker with CI/CD",
            "slug": "docker-with-cicd",
            "difficulty": "hard",
            "estimated_minutes": 50,
            "xp_reward": 90,
            "content": """# Docker with CI/CD

## Varför behöver du kunna detta?

Docker och CI/CD hör ihop. Du måste kunna:

- **Bygga och testa** images automatiskt
- **Pusha till registry** från pipeline
- **Deploya** nya versioner automatiskt

---

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

---

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

---

## Smart Tagging Strategy

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

# Resultat:
# - main branch: myapp:main
# - PR #123: myapp:pr-123
# - Tag v1.2.3: myapp:1.2.3
# - Alltid: myapp:abc1234 (SHA)
```

---

## Layer Caching i CI

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

# Eller registry-based cache
    cache-from: type=registry,ref=myapp:buildcache
    cache-to: type=registry,ref=myapp:buildcache,mode=max
```

---

## Security Scanning i Pipeline

```yaml
# GitHub Actions
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

---

## Multi-platform Builds

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

---

## Deploy with Docker Compose

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

---

## Key Takeaways

- **Tagga med SHA** för spårbarhet
- **Cache layers** för snabbare builds
- **Scanna images** för sårbarheter i pipeline
- **Multi-platform** för ARM/AMD64 stöd
""",
        },
        {
            "title": "Docker Swarm Basics",
            "slug": "docker-swarm-basics",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 80,
            "content": """# Docker Swarm Basics

## Varför behöver du kunna detta?

Swarm är Dockers inbyggda orkestrering. Du behöver förstå det för att:

- **Köra containers över flera hosts**
- **Förstå orkestreringskoncept** innan Kubernetes
- **Hantera enklare produktionsmiljöer**

---

## Vad är Docker Swarm?

Docker Swarm är clustering och orkestrering inbyggt i Docker. Det är enklare än Kubernetes men har färre features.

```bash
# Swarm arkitektur
┌─────────────────────────────────────────────────────┐
│                    Manager Nodes                     │
│  (Hanterar klustret, schemalägger tasks)            │
├─────────────────────────────────────────────────────┤
│                    Worker Nodes                      │
│  (Kör containers/tasks)                              │
└─────────────────────────────────────────────────────┘
```

---

## Initiera Swarm

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

---

## Services

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

---

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

---

## Rolling Updates

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

---

## Key Takeaways

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

## Varför behöver du kunna detta?

En sammanfattning av alla best practices för att skriva professionella Dockerfiles och köra containers i produktion.

---

## Dockerfile Best Practices

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

---

## Image Best Practices

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

---

## Container Best Practices

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

---

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

---

## Checklista

```bash
# Dockerfile
☐ Specifik base image tag
☐ Multi-stage build
☐ Non-root user
☐ Healthcheck
☐ .dockerignore
☐ Minimala layers

# Security
☐ Image scanning
☐ No secrets i image
☐ Resource limits
☐ Read-only filesystem
☐ Dropped capabilities

# Produktion
☐ Restart policy
☐ Centraliserad logging
☐ Health monitoring
☐ Backup strategy
```

---

## Key Takeaways

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

## Varför behöver du kunna detta?

Docker förändrar hur du utvecklar. Du behöver förstå:

- **Hur du sätter upp lokal utvecklingsmiljö** med Docker
- **Hot reload och debugging** i containers
- **Skillnaden mellan dev och prod** konfiguration

---

## Development vs Production

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

---

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

---

## Användbart dev-kommando

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

---

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

---

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

---

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

---

## Key Takeaways

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

## Varför behöver du kunna detta?

Docker är mer än bara Docker Engine. Du behöver känna till:

- **Verktyg som kompletterar Docker**
- **Alternativ och relaterade teknologier**
- **Var Docker passar in i DevOps-landskapet**

---

## Docker Desktop

```bash
# Inkluderar:
# - Docker Engine
# - Docker Compose
# - Docker Scout (security scanning)
# - Kubernetes (single-node)
# - Extensions

# Bra för lokal utveckling på Mac/Windows
# I produktion: använd Docker Engine direkt på Linux
```

---

## Podman (Docker-alternativ)

```bash
# Podman - daemonless, rootless containers
# Kompatibel med Docker CLI

podman run nginx           # Samma syntax som docker
podman build -t myimage .  # Samma Dockerfiles

# Fördelar:
# - Ingen daemon (säkrare)
# - Rootless by default
# - Kompatibel med Docker
```

---

## Image Scanning Tools

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

---

## Container Registries

```bash
# Public
# - Docker Hub (docker.io)
# - GitHub Container Registry (ghcr.io)
# - Quay.io

# Cloud-managed
# - AWS ECR
# - Google Artifact Registry
# - Azure Container Registry

# Self-hosted
# - Harbor
# - GitLab Container Registry
# - Nexus
```

---

## Image Analysis Tools

```bash
# Dive - analysera layers
dive myimage

# Docker History
docker history myimage

# Skopeo - kopiera mellan registries
skopeo copy docker://docker.io/nginx docker://myregistry/nginx
```

---

## Build Tools

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

---

## Orchestration

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

---

## Monitoring & Logging

```bash
# Prometheus + Grafana
# - Metrics collection och visualization

# ELK Stack (Elasticsearch, Logstash, Kibana)
# - Centraliserad logging

# Datadog, New Relic
# - Managed monitoring

# cAdvisor
# - Container resource monitoring
```

---

## Key Takeaways

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

## Varför behöver du kunna detta?

Docker-certifieringar validerar dina kunskaper. Du behöver veta:

- **Vilka certifieringar som finns**
- **Vad de täcker**
- **Hur du förbereder dig**

---

## Docker Certified Associate (DCA)

```bash
# Den primära Docker-certifieringen
# Täcker:

# 1. Orchestration (25%)
# - Swarm setup och management
# - Services och stacks
# - Networking i Swarm

# 2. Image Creation & Management (20%)
# - Dockerfile best practices
# - Multi-stage builds
# - Registry operations

# 3. Installation & Configuration (15%)
# - Docker Engine installation
# - Storage drivers
# - Logging drivers

# 4. Networking (15%)
# - Network drivers
# - DNS och service discovery
# - Load balancing

# 5. Security (15%)
# - Image security
# - Secrets management
# - Content trust

# 6. Storage & Volumes (10%)
# - Volume types
# - Backup strategies
```

---

## Förberedelse

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

---

## Relaterade Certifieringar

```bash
# Kubernetes certifieringar (nästa steg)
# - CKA (Certified Kubernetes Administrator)
# - CKAD (Certified Kubernetes Application Developer)
# - CKS (Certified Kubernetes Security Specialist)

# Cloud certifieringar med container-fokus
# - AWS Certified DevOps Engineer
# - Azure DevOps Engineer Expert
# - Google Professional Cloud DevOps Engineer
```

---

## Study Checklist

```bash
☐ Dockerfile syntax och best practices
☐ Docker Compose för multi-container apps
☐ Docker networking (bridge, host, overlay)
☐ Docker volumes och storage
☐ Docker Swarm basics
☐ Image security och scanning
☐ Registry operations
☐ Logging och monitoring
☐ Troubleshooting containers
```

---

## Key Takeaways

- **DCA** är bra första certifiering
- **Hands-on experience** är viktigast
- **Kubernetes-cert** är naturligt nästa steg
- Öva med **Play with Docker** labs
""",
        },
    ],
}
