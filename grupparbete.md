# 🐧 Linux Server Automation - Komplett Projektguide

**Kurs:** Linux/Unix Server samt Bash Programmering
**Deadline:** 2026-01-09
**Grupp 3:** Christian, Cebrail, Baraa, Marcus, Said

---

## 📋 Innehållsförteckning

1. [Förberedelser](#1-förberedelser)
2. [Del 1: Användare & Grupper](#del-1-användare--grupper)
3. [Del 2: Systemkonfiguration](#del-2-systemkonfiguration)
4. [Del 3: Docker Installation](#del-3-docker-installation)
5. [Del 4: Socket-script & Systemd](#del-4-socket-script--systemd-service) ⚠️ SVÅRAST
6. [Del 5: Integration - sys-config.sh](#del-5-integration---sys-configsh)
7. [Del 6: Shellcheck & README](#del-6-shellcheck--readme)
8. [Del 7: Sluttest](#del-7-sluttest)

---

## Övergripande förståelse

### Vad ska vi bygga?

```
┌─────────────────────────────────────────────────────────────┐
│                    sys-config.sh                            │
│    (ETT script som gör ALLT när man kör det på ny VM)       │
├─────────────────────────────────────────────────────────────┤
│  1. Skapar användare för varje gruppmedlem                  │
│  2. Skapar gemensam grupp + delad mapp                      │
│  3. Konfigurerar SSH (säker inloggning)                     │
│  4. Installerar firewalld (brandvägg)                       │
│  5. Installerar Docker                                      │
│  6. Installerar vår egen socket-tjänst                      │
└─────────────────────────────────────────────────────────────┘
```

### Filstruktur i ert repo

```
projekt-repo/
├── sys-config.sh          # Huvudscriptet (kör detta för att konfigurera VM)
├── socket-listener.sh     # Bash-script som lyssnar på socket
├── Dockerfile             # Bygger Docker-image med socket-scriptet
├── socket-listener.service # Systemd service-fil
└── README.md              # Dokumentation
```

---

# 1. Förberedelser

## 1.1 Skapa en test-VM

- [ ] **Skapa en ny VM med Ubuntu 24.04**

```bash
# Om du använder Multipass (rekommenderat för snabb testning):
multipass launch 24.04 --name linux-projekt --memory 2G --disk 10G

# Logga in:
multipass shell linux-projekt
```

**VARFÖR?** Vi behöver en ren Ubuntu 24.04 för att testa att scriptet fungerar från scratch.

---

## 1.2 Skapa Git-repo

- [ ] **Gå till git.chas-lab.dev (INTE gitlab.com!)**
- [ ] **Skapa nytt projekt/repo**
- [ ] **Klona till din lokala maskin**

```bash
git clone https://git.chas-lab.dev/<ditt-användarnamn>/<projekt-namn>.git
cd <projekt-namn>
```

**VARFÖR?** Läraren kräver specifikt git.chas-lab.dev. Fel repo = problem vid inlämning.

---

## 1.3 Skapa grundfilerna

- [ ] **Skapa alla filer vi kommer behöva**

```bash
touch sys-config.sh socket-listener.sh Dockerfile socket-listener.service README.md
chmod +x sys-config.sh socket-listener.sh
```

**VARFÖR?** `chmod +x` gör filerna körbara (executable). Utan detta kan man inte köra scripten.

---

# Del 1: Användare & Grupper

## Översikt

```
┌─────────────────────────────────────────────────────────┐
│  KRAV:                                                  │
│  ✓ Skapa en användare per gruppmedlem (5 st)            │
│  ✓ Skapa en gemensam grupp                              │
│  ✓ Lösenord som måste bytas vid första inloggning       │
│  ✓ Delad mapp /opt/<gruppnamn> med rätt rättigheter     │
│  ✓ Alla kan köra sudo utan lösenord                     │
└─────────────────────────────────────────────────────────┘
```

---

## 1.1 Definiera användare och grupp

- [ ] **Förstå vilka användare som ska skapas**

```bash
# Gruppmedlemmar (Grupp 3):
# - Christian
# - Cebrail
# - Baraa
# - Marcus
# - Said

# Vi använder lowercase för användarnamn (Linux-standard)
USERS=("christian" "cebrail" "baraa" "marcus" "said")
GROUP_NAME="grupp3"
SHARED_DIR="/opt/grupp3"
```

**VARFÖR?** Linux användarnamn är case-sensitive och bör vara lowercase för att undvika problem.

---

## 1.2 Skapa gruppen

- [ ] **Kommando för att skapa grupp**

```bash
# Skapa gruppen (om den inte redan finns)
sudo groupadd "$GROUP_NAME" 2>/dev/null || true
```

**FÖRKLARING:**
- `groupadd` - skapar en ny grupp
- `2>/dev/null` - skickar felmeddelanden till "ingenstans" (döljer dem)
- `|| true` - om kommandot misslyckas (gruppen finns redan), fortsätt ändå

**VARFÖR?** Vi vill att scriptet ska kunna köras flera gånger utan att krascha om gruppen redan finns.

---

## 1.3 Skapa användare

- [ ] **Kommando för att skapa en användare**

```bash
# För varje användare:
sudo useradd -m -s /bin/bash -G "$GROUP_NAME" "$username"
```

**FÖRKLARING:**
| Flagga | Betydelse |
|--------|-----------|
| `-m` | Skapa home-katalog (/home/username) |
| `-s /bin/bash` | Sätt bash som default shell |
| `-G grupp3` | Lägg till i gruppen "grupp3" |

**VARFÖR?**
- `-m` behövs för att användaren ska ha någonstans att spara filer
- `-s /bin/bash` ger ett ordentligt shell (utan detta får de kanske /bin/sh)
- `-G` lägger till i extra grupp (utöver deras egen primärgrupp)

---

## 1.4 Sätt lösenord med tvingad ändring

- [ ] **Be om lösenord och sätt det**

```bash
# Fråga användaren som kör scriptet efter lösenord
read -s -p "Ange lösenord för $username: " password
echo  # Ny rad efter lösenordsinmatning

# Sätt lösenordet
echo "$username:$password" | sudo chpasswd

# Tvinga lösenordsbyte vid nästa inloggning
sudo chage -d 0 "$username"
```

**FÖRKLARING:**
| Kommando | Betydelse |
|----------|-----------|
| `read -s` | Läs input utan att visa det (för lösenord) |
| `read -p "text"` | Visa en prompt innan input |
| `chpasswd` | Sätter lösenord (läser från stdin i format user:password) |
| `chage -d 0` | Sätter "senast ändrad" till 0, vilket tvingar byte |

**VARFÖR?**
- `read -s` döljer lösenordet när man skriver (säkerhet)
- `chage -d 0` är tricket för att tvinga lösenordsbyte - det säger att lösenordet är 0 dagar gammalt sedan epoch (1970), vilket systemet tolkar som "förfallet"

---

## 1.5 Skapa delad mapp med SGID

- [ ] **Skapa mappen och sätt rättigheter**

```bash
# Skapa mappen
sudo mkdir -p "$SHARED_DIR"

# Sätt gruppen som ägare
sudo chown root:"$GROUP_NAME" "$SHARED_DIR"

# Sätt rättigheter: rwxrwx--- med SGID
sudo chmod 2770 "$SHARED_DIR"
```

**FÖRKLARING av chmod 2770:**
```
2    7    7    0
│    │    │    │
│    │    │    └── Others: ingen åtkomst (---)
│    │    └─────── Group: full åtkomst (rwx)
│    └──────────── Owner: full åtkomst (rwx)
└───────────────── SGID-bit (set group ID)
```

**VARFÖR SGID (2)?**
- Normalt: när du skapar en fil ägs den av DIN grupp
- Med SGID: nya filer i mappen ärvs automatiskt av mappens grupp
- Detta gör att alla i grupp3 kan läsa/skriva varandras filer i mappen

**VISUALISERING:**
```
Utan SGID:
  said skapar fil → fil ägs av "said:said"
  marcus kan inte redigera filen

Med SGID:
  said skapar fil → fil ägs av "said:grupp3"
  marcus (som är i grupp3) kan redigera filen ✓
```

---

## 1.6 Sudo utan lösenord

- [ ] **Skapa sudoers-fil för gruppen**

```bash
# Skapa fil i /etc/sudoers.d/
echo "%${GROUP_NAME} ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/"$GROUP_NAME"

# Sätt korrekta rättigheter (VIKTIGT!)
sudo chmod 440 /etc/sudoers.d/"$GROUP_NAME"
```

**FÖRKLARING:**
```
%grupp3   ALL=(ALL)  NOPASSWD:  ALL
│         │    │     │          │
│         │    │     │          └── Alla kommandon
│         │    │     └───────────── Utan lösenord
│         │    └─────────────────── Som alla användare
│         └──────────────────────── På alla hosts
└────────────────────────────────── Gruppen grupp3 (% = grupp)
```

**VARFÖR?**
- `/etc/sudoers.d/` är rätt plats för egna sudoers-regler
- `chmod 440` är **KRITISKT** - sudoers-filer med fel rättigheter ignoreras av säkerhetsskäl
- Vi använder `tee` istället för `>` eftersom vi behöver sudo för att skriva till filen

---

## ✅ Komplett kod för Del 1

```bash
#!/bin/bash
# === DEL 1: ANVÄNDARE OCH GRUPPER ===

# Definiera användare och grupp
USERS=("christian" "cebrail" "baraa" "marcus" "said")
GROUP_NAME="grupp3"
SHARED_DIR="/opt/grupp3"

# Skapa gruppen
echo "Skapar grupp: $GROUP_NAME"
sudo groupadd "$GROUP_NAME" 2>/dev/null || true

# Skapa varje användare
for username in "${USERS[@]}"; do
    echo "Skapar användare: $username"

    # Skapa användaren (om den inte finns)
    if ! id "$username" &>/dev/null; then
        sudo useradd -m -s /bin/bash -G "$GROUP_NAME" "$username"
    else
        # Om användaren finns, lägg bara till i gruppen
        sudo usermod -aG "$GROUP_NAME" "$username"
    fi

    # Fråga efter lösenord
    read -s -p "Ange lösenord för $username: " password
    echo

    # Sätt lösenordet
    echo "$username:$password" | sudo chpasswd

    # Tvinga lösenordsbyte vid nästa inloggning
    sudo chage -d 0 "$username"
done

# Skapa delad mapp med SGID
echo "Skapar delad mapp: $SHARED_DIR"
sudo mkdir -p "$SHARED_DIR"
sudo chown root:"$GROUP_NAME" "$SHARED_DIR"
sudo chmod 2770 "$SHARED_DIR"

# Konfigurera sudo utan lösenord
echo "Konfigurerar sudo utan lösenord för $GROUP_NAME"
echo "%${GROUP_NAME} ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/"$GROUP_NAME" > /dev/null
sudo chmod 440 /etc/sudoers.d/"$GROUP_NAME"

echo "Del 1 klar!"
```

---

## 🧪 Verifiera Del 1

- [ ] **Testa att användarna skapades**
```bash
# Lista alla skapade användare
for user in christian cebrail baraa marcus said; do
    id "$user"
done
```

- [ ] **Testa gruppen**
```bash
# Visa gruppens medlemmar
getent group grupp3
```

- [ ] **Testa delad mapp**
```bash
# Kontrollera rättigheter (ska visa "drwxrws---" - notera 's' för SGID)
ls -la /opt/ | grep grupp3
```

- [ ] **Testa sudo utan lösenord**
```bash
# Byt till en av användarna och testa sudo
sudo -u christian sudo whoami
# Ska svara "root" utan att fråga efter lösenord
```

---

# Del 2: Systemkonfiguration

## Översikt

```
┌─────────────────────────────────────────────────────────┐
│  KRAV:                                                  │
│  ✓ Uppdatera alla paket                                 │
│  ✓ SSH-server installerad och körande                   │
│  ✓ SSH på icke-standard port                            │
│  ✓ SSH endast med pubkey (ingen lösenordsinloggning)    │
│  ✓ SSH endast för våra användare                        │
│  ✓ firewalld installerad, startad, enabled              │
│  ✓ Blockera allt inkommande utom SSH-porten             │
│  ✓ Tillåt allt utgående                                 │
│  ✓ Ingen annan brandvägg får köra                       │
└─────────────────────────────────────────────────────────┘
```

---

## 2.1 Uppdatera alla paket

- [ ] **Uppdatera systemet**

```bash
# Uppdatera paketlistan
sudo apt-get update

# Uppgradera alla installerade paket
# -y = svara ja automatiskt
# DEBIAN_FRONTEND=noninteractive = undvik interaktiva prompter
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
```

**VARFÖR `DEBIAN_FRONTEND=noninteractive`?**
- Ibland frågar apt om du vill behålla gamla config-filer etc.
- I ett automatiserat script vill vi undvika sådana frågor
- Denna miljövariabel säger "svara med default på allt"

---

## 2.2 Installera SSH-server

- [ ] **Installera openssh-server**

```bash
sudo apt-get install -y openssh-server
```

**VARFÖR?** Ubuntu Desktop har inte SSH-server installerad som standard (Ubuntu Server har det däremot).

---

## 2.3 Konfigurera SSH

- [ ] **Definiera SSH-port (välj en icke-standard port)**

```bash
SSH_PORT=2222  # Standardporten är 22, vi använder 2222 istället
```

**VARFÖR byta port?**
- Säkerhet genom obscurity (inte perfekt, men hjälper)
- Minskar automatiserade attacker som scannar port 22
- **VIKTIGT:** Välj en port över 1024 och under 65535

---

- [ ] **Skapa SSH-konfiguration**

```bash
# Skapa backup av original-config
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Skapa vår konfiguration
sudo tee /etc/ssh/sshd_config.d/custom.conf > /dev/null << EOF
# Ändra port från standard (22) till vår valda port
Port $SSH_PORT

# Tillåt INTE inloggning med lösenord - endast nycklar
PasswordAuthentication no

# Tillåt pubkey-autentisering
PubkeyAuthentication yes

# Tillåt ENDAST dessa användare att logga in via SSH
AllowUsers christian cebrail baraa marcus said

# Extra säkerhet: tillåt inte root att logga in direkt
PermitRootLogin no
EOF
```

**FÖRKLARING av varje rad:**

| Inställning | Värde | Varför |
|-------------|-------|--------|
| `Port 2222` | Icke-standard | Kravet säger "non-default port" |
| `PasswordAuthentication no` | Av | Kravet säger "Only accept log-in via pubkey" |
| `PubkeyAuthentication yes` | På | Möjliggör SSH-nyckel inloggning |
| `AllowUsers ...` | Våra 5 | Kravet säger "Only allow the users created previously" |
| `PermitRootLogin no` | Av | Best practice - ingen direkt root-access |

---

- [ ] **Starta om SSH-tjänsten**

```bash
sudo systemctl restart sshd
sudo systemctl enable sshd
```

**VARFÖR båda kommandona?**
- `restart` - applicerar ändringarna NU
- `enable` - ser till att SSH startar automatiskt vid boot

---

## 2.4 Ta bort andra brandväggar

- [ ] **Stoppa och ta bort ufw (Ubuntu's default-brandvägg)**

```bash
# Stoppa ufw om den körs
sudo systemctl stop ufw 2>/dev/null || true

# Avaktivera ufw från att starta vid boot
sudo systemctl disable ufw 2>/dev/null || true

# Ta bort ufw helt (valfritt men rekommenderat)
sudo apt-get remove -y ufw 2>/dev/null || true
```

**VARFÖR?**
- Kravet säger "Make sure there is no other firewall service running"
- Ubuntu kommer med `ufw` som standard
- Vi måste ta bort den innan vi installerar `firewalld`

---

## 2.5 Installera och konfigurera firewalld

- [ ] **Installera firewalld**

```bash
sudo apt-get install -y firewalld
```

---

- [ ] **Starta och aktivera firewalld**

```bash
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

---

- [ ] **Konfigurera brandväggsregler**

```bash
# Ta bort eventuella befintliga SSH-regler (som använder port 22)
sudo firewall-cmd --permanent --remove-service=ssh 2>/dev/null || true

# Lägg till vår SSH-port
sudo firewall-cmd --permanent --add-port=${SSH_PORT}/tcp

# Sätt default policy för inkommande till DROP (blockera)
sudo firewall-cmd --permanent --set-default-zone=drop

# I "drop" zonen, lägg till vår SSH-port
sudo firewall-cmd --permanent --zone=drop --add-port=${SSH_PORT}/tcp

# Ladda om för att applicera ändringar
sudo firewall-cmd --reload
```

**FÖRKLARING:**

```
┌────────────────────────────────────────────────┐
│           INTERNET                             │
│               │                                │
│               ▼                                │
│    ┌──────────────────────┐                    │
│    │     firewalld        │                    │
│    │  ┌────────────────┐  │                    │
│    │  │ Zone: drop     │  │                    │
│    │  │                │  │                    │
│    │  │ Port 2222 ✓    │──────► SSH-server    │
│    │  │ Allt annat ✗   │  │                    │
│    │  └────────────────┘  │                    │
│    └──────────────────────┘                    │
│                                                │
│    Utgående: Tillåtet (default)                │
└────────────────────────────────────────────────┘
```

**VARFÖR `drop` zone?**
- `drop` = blockera allt som standard, tillåt endast explicit angivna portar
- Detta är säkrare än att börja med "tillåt allt" och sedan blockera

---

## ✅ Komplett kod för Del 2

```bash
#!/bin/bash
# === DEL 2: SYSTEMKONFIGURATION ===

SSH_PORT=2222
USERS=("christian" "cebrail" "baraa" "marcus" "said")

# Uppdatera system
echo "Uppdaterar system..."
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Installera SSH-server
echo "Installerar SSH-server..."
sudo apt-get install -y openssh-server

# Konfigurera SSH
echo "Konfigurerar SSH på port $SSH_PORT..."
sudo tee /etc/ssh/sshd_config.d/custom.conf > /dev/null << EOF
Port $SSH_PORT
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers ${USERS[*]}
PermitRootLogin no
EOF

# Starta om SSH
sudo systemctl restart sshd
sudo systemctl enable sshd

# Ta bort ufw
echo "Tar bort ufw..."
sudo systemctl stop ufw 2>/dev/null || true
sudo systemctl disable ufw 2>/dev/null || true
sudo apt-get remove -y ufw 2>/dev/null || true

# Installera firewalld
echo "Installerar firewalld..."
sudo apt-get install -y firewalld
sudo systemctl start firewalld
sudo systemctl enable firewalld

# Konfigurera brandvägg
echo "Konfigurerar brandvägg..."
sudo firewall-cmd --permanent --set-default-zone=drop
sudo firewall-cmd --permanent --zone=drop --add-port=${SSH_PORT}/tcp
sudo firewall-cmd --reload

echo "Del 2 klar!"
```

---

## 🧪 Verifiera Del 2

- [ ] **Kontrollera SSH-status och port**
```bash
sudo systemctl status sshd
sudo ss -tlnp | grep sshd
# Ska visa att sshd lyssnar på port 2222
```

- [ ] **Kontrollera firewalld-status**
```bash
sudo systemctl status firewalld
sudo firewall-cmd --list-all
# Ska visa zone: drop och port 2222/tcp
```

- [ ] **Kontrollera att ufw är borta**
```bash
sudo systemctl status ufw
# Ska visa "not found" eller "inactive"
```

---

# Del 3: Docker Installation

## Översikt

```
┌─────────────────────────────────────────────────────────┐
│  KRAV:                                                  │
│  ✓ Installera Docker från OFFICIELLA repot              │
│  ✓ Installera Docker Compose                            │
│  ✓ Våra användare ska kunna köra docker utan sudo       │
└─────────────────────────────────────────────────────────┘
```

---

## 3.1 Installera Docker (officiell metod)

- [ ] **Installera dependencies**

```bash
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

**VARFÖR?**
- `ca-certificates` - för HTTPS-anslutningar
- `curl` - för att ladda ner filer
- `gnupg` - för att verifiera GPG-nycklar
- `lsb-release` - för att identifiera Ubuntu-version

---

- [ ] **Lägg till Dockers GPG-nyckel**

```bash
# Skapa katalog för keyrings
sudo install -m 0755 -d /etc/apt/keyrings

# Ladda ner och spara Docker's GPG-nyckel
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Sätt läsrättigheter
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

**VARFÖR GPG-nyckel?**
- Säkerhet! Verifierar att paketen verkligen kommer från Docker
- Utan detta skulle vem som helst kunna lägga in skadlig kod

---

- [ ] **Lägg till Docker's repository**

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**FÖRKLARING:**
- `dpkg --print-architecture` - ger din CPU-arkitektur (amd64, arm64, etc.)
- `lsb_release -cs` - ger Ubuntu's kodnamn (t.ex. "noble" för 24.04)
- `signed-by=...` - använd GPG-nyckeln för verifiering

---

- [ ] **Installera Docker**

```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**VARFÖR dessa paket?**
| Paket | Vad det är |
|-------|------------|
| `docker-ce` | Docker Community Edition (huvudprogrammet) |
| `docker-ce-cli` | Kommandoradsverktyget |
| `containerd.io` | Container runtime |
| `docker-buildx-plugin` | Modern build-funktionalitet |
| `docker-compose-plugin` | Docker Compose (som plugin, inte standalone) |

---

## 3.2 Låt användare köra Docker utan sudo

- [ ] **Lägg till användare i docker-gruppen**

```bash
for username in "${USERS[@]}"; do
    sudo usermod -aG docker "$username"
done
```

**FÖRKLARING:**
- `usermod -aG docker` = lägg till användaren i gruppen "docker"
- Docker-gruppen skapas automatiskt vid Docker-installation
- Medlemmar i docker-gruppen kan kommunicera med Docker daemon

**VARFÖR?**
- Kravet säger "can run docker cli commands without needing to use sudo"
- Docker daemon körs som root, men socket:en (`/var/run/docker.sock`) ägs av gruppen `docker`

---

## ✅ Komplett kod för Del 3

```bash
#!/bin/bash
# === DEL 3: DOCKER INSTALLATION ===

USERS=("christian" "cebrail" "baraa" "marcus" "said")

echo "Installerar Docker från officiellt repo..."

# Installera dependencies
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Lägg till Dockers GPG-nyckel
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Lägg till Docker repo
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Starta och aktivera Docker
sudo systemctl start docker
sudo systemctl enable docker

# Lägg till användare i docker-gruppen
echo "Lägger till användare i docker-gruppen..."
for username in "${USERS[@]}"; do
    sudo usermod -aG docker "$username"
done

echo "Del 3 klar!"
```

---

## 🧪 Verifiera Del 3

- [ ] **Kontrollera Docker-version**
```bash
docker --version
docker compose version
```

- [ ] **Kontrollera Docker-tjänsten**
```bash
sudo systemctl status docker
```

- [ ] **Testa som en av användarna (efter omloggning)**
```bash
# OBS: Gruppändring kräver omloggning
sudo -u christian newgrp docker
sudo -u christian docker run hello-world
```

---

# Del 4: Socket-script & Systemd Service

## ⚠️ DETTA ÄR DEN SVÅRASTE DELEN ⚠️

```
┌────────────────────────────────────────────────────────────────┐
│  KRAV:                                                         │
│  ✓ Bash-script som lyssnar på en socket                        │
│  ✓ Sparar data från klienter                                   │
│  ✓ Docker-image som kör scriptet                               │
│  ✓ Systemd-service som startar containern                      │
│  ✓ Data ska överleva container-omstart (persistent)            │
└────────────────────────────────────────────────────────────────┘
```

---

## 4.1 Förstå vad vi ska bygga

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Klient ──────► Socket (port) ──────► Script ──────► Fil       │
│                                                                 │
│   Exempel:                                                      │
│   $ echo "Hello" | nc localhost 9999                            │
│                     │                                           │
│                     ▼                                           │
│            socket-listener.sh                                   │
│                     │                                           │
│                     ▼                                           │
│            /data/messages.log                                   │
│            (innehåll: "Hello")                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.2 Socket-listener scriptet

- [ ] **Skapa socket-listener.sh**

```bash
#!/bin/bash
# socket-listener.sh
# Ett script som lyssnar på en TCP-port och sparar mottagen data

# === KONFIGURATION ===
PORT=${LISTEN_PORT:-9999}           # Port att lyssna på (default 9999)
DATA_DIR=${DATA_DIR:-/data}         # Katalog för sparad data
LOG_FILE="$DATA_DIR/messages.log"   # Fil där data sparas

# === FÖRBEREDELSER ===
# Skapa datakatalog om den inte finns
mkdir -p "$DATA_DIR"

# Skapa loggfilen om den inte finns
touch "$LOG_FILE"

echo "Socket listener startar på port $PORT"
echo "Data sparas till $LOG_FILE"

# === HUVUDLOOP ===
# Vi använder socat för att lyssna på en TCP-port
# socat är mer robust än netcat för denna typ av uppgift

while true; do
    # Lyssna på porten och för varje anslutning:
    # 1. Läs data från klienten
    # 2. Lägg till timestamp
    # 3. Spara till loggfil
    socat TCP-LISTEN:"$PORT",reuseaddr,fork SYSTEM:"
        while IFS= read -r line; do
            timestamp=\$(date '+%Y-%m-%d %H:%M:%S')
            echo \"[\$timestamp] \$line\" >> $LOG_FILE
            echo \"Received: \$line\"
        done
    " 2>/dev/null

    # Om socat kraschar, vänta lite och försök igen
    echo "Socat avslutades, startar om om 1 sekund..."
    sleep 1
done
```

**FÖRKLARING:**

| Del | Vad den gör |
|-----|-------------|
| `${LISTEN_PORT:-9999}` | Använd miljövariabel eller default 9999 |
| `socat TCP-LISTEN:...` | Lyssna på TCP-port |
| `reuseaddr` | Tillåt återanvändning av porten direkt |
| `fork` | Hantera flera klienter samtidigt |
| `SYSTEM:"..."` | Kör detta kommando för varje anslutning |
| `while true` | Starta om om något går fel |

**VARFÖR socat istället för netcat?**
- `socat` är mer robust och flexibel
- Enklare att hantera flera samtidiga anslutningar
- Bättre felhantering

---

## 4.3 Dockerfile

- [ ] **Skapa Dockerfile**

```dockerfile
# Dockerfile
# Bygger en image som kör vårt socket-listener script

# Använd Ubuntu som bas
FROM ubuntu:24.04

# Installera socat (för socket-lyssnandet)
RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Skapa datakatalog
RUN mkdir -p /data

# Kopiera vårt script
COPY socket-listener.sh /usr/local/bin/socket-listener.sh

# Gör scriptet körbart
RUN chmod +x /usr/local/bin/socket-listener.sh

# Exponera porten (dokumentation)
EXPOSE 9999

# Sätt datakatalogen som volume-punkt
VOLUME /data

# Kör scriptet när containern startar
ENTRYPOINT ["/usr/local/bin/socket-listener.sh"]
```

**FÖRKLARING:**

| Instruktion | Vad den gör |
|-------------|-------------|
| `FROM ubuntu:24.04` | Basera på samma OS som projektet kräver |
| `RUN apt-get...` | Installera dependencies |
| `COPY` | Kopiera vårt script in i imagen |
| `EXPOSE 9999` | Dokumenterar vilken port (påverkar inte faktisk nätverksconfig) |
| `VOLUME /data` | Markerar /data som en volym-punkt |
| `ENTRYPOINT` | Kommandot som körs när containern startar |

---

## 4.4 Systemd Service-fil

- [ ] **Skapa socket-listener.service**

```ini
# socket-listener.service
# Systemd service-fil för vår socket-listener container

[Unit]
Description=Socket Listener Service
After=docker.service
Requires=docker.service

[Service]
Type=simple
Restart=always
RestartSec=5

# Stoppa och ta bort eventuell gammal container
ExecStartPre=-/usr/bin/docker stop socket-listener
ExecStartPre=-/usr/bin/docker rm socket-listener

# Starta containern
ExecStart=/usr/bin/docker run \
    --name socket-listener \
    --rm \
    -p 9999:9999 \
    -v socket-listener-data:/data \
    socket-listener:latest

# Stoppa containern
ExecStop=/usr/bin/docker stop socket-listener

[Install]
WantedBy=multi-user.target
```

**FÖRKLARING:**

| Sektion/Direktiv | Vad det gör |
|------------------|-------------|
| `[Unit]` | Metadata och beroenden |
| `After=docker.service` | Starta EFTER Docker har startat |
| `Requires=docker.service` | Kräver att Docker körs |
| `[Service]` | Hur tjänsten körs |
| `Type=simple` | Processen i ExecStart ÄR tjänsten |
| `Restart=always` | Starta om automatiskt om den kraschar |
| `ExecStartPre=-...` | Kör FÖRE start. `-` = ignorera fel |
| `-v socket-listener-data:/data` | **PERSISTENT LAGRING!** Docker volume |
| `[Install]` | När ska tjänsten startas |
| `WantedBy=multi-user.target` | Vid normal systemstart |

**VARFÖR `-v socket-listener-data:/data`?**
```
Utan volume:
Container stoppar → Data försvinner ✗

Med named volume:
Container stoppar → Data finns kvar i "socket-listener-data" ✓
Container startar igen → Samma data finns tillgänglig ✓
```

---

## 4.5 Installera tjänsten (i sys-config.sh)

- [ ] **Kod för att installera och starta tjänsten**

```bash
# Bygg Docker-imagen
echo "Bygger Docker-image..."
docker build -t socket-listener:latest /path/to/dockerfile/directory

# Kopiera service-filen till systemd
echo "Installerar systemd-service..."
sudo cp socket-listener.service /etc/systemd/system/

# Ladda om systemd för att hitta nya filen
sudo systemctl daemon-reload

# Aktivera tjänsten (startar vid boot)
sudo systemctl enable socket-listener

# Starta tjänsten nu
sudo systemctl start socket-listener
```

---

## ✅ Komplett kod för Del 4

### socket-listener.sh
```bash
#!/bin/bash
# socket-listener.sh - Lyssnar på TCP-port och sparar data

PORT=${LISTEN_PORT:-9999}
DATA_DIR=${DATA_DIR:-/data}
LOG_FILE="$DATA_DIR/messages.log"

mkdir -p "$DATA_DIR"
touch "$LOG_FILE"

echo "Socket listener startar på port $PORT"
echo "Data sparas till $LOG_FILE"

while true; do
    socat TCP-LISTEN:"$PORT",reuseaddr,fork SYSTEM:"
        while IFS= read -r line; do
            timestamp=\$(date '+%Y-%m-%d %H:%M:%S')
            echo \"[\$timestamp] \$line\" >> $LOG_FILE
            echo \"Received: \$line\"
        done
    " 2>/dev/null

    echo "Startar om om 1 sekund..."
    sleep 1
done
```

### Dockerfile
```dockerfile
FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data

COPY socket-listener.sh /usr/local/bin/socket-listener.sh
RUN chmod +x /usr/local/bin/socket-listener.sh

EXPOSE 9999
VOLUME /data

ENTRYPOINT ["/usr/local/bin/socket-listener.sh"]
```

### socket-listener.service
```ini
[Unit]
Description=Socket Listener Service
After=docker.service
Requires=docker.service

[Service]
Type=simple
Restart=always
RestartSec=5
ExecStartPre=-/usr/bin/docker stop socket-listener
ExecStartPre=-/usr/bin/docker rm socket-listener
ExecStart=/usr/bin/docker run \
    --name socket-listener \
    --rm \
    -p 9999:9999 \
    -v socket-listener-data:/data \
    socket-listener:latest
ExecStop=/usr/bin/docker stop socket-listener

[Install]
WantedBy=multi-user.target
```

---

## 🧪 Verifiera Del 4

- [ ] **Bygg imagen manuellt först**
```bash
docker build -t socket-listener:latest .
```

- [ ] **Testa containern manuellt**
```bash
# Starta containern
docker run -d --name test-socket -p 9999:9999 -v test-data:/data socket-listener:latest

# Skicka data
echo "Test message" | nc localhost 9999

# Kolla att datan sparades
docker exec test-socket cat /data/messages.log

# Städa upp
docker stop test-socket
docker rm test-socket
```

- [ ] **Testa persistence**
```bash
# Starta, skicka data, stoppa
docker run -d --name test1 -p 9999:9999 -v persist-test:/data socket-listener:latest
echo "First message" | nc localhost 9999
docker stop test1 && docker rm test1

# Starta igen med samma volume
docker run -d --name test2 -p 9999:9999 -v persist-test:/data socket-listener:latest
echo "Second message" | nc localhost 9999

# Kolla - båda meddelanden ska finnas!
docker exec test2 cat /data/messages.log

# Städa
docker stop test2 && docker rm test2
docker volume rm persist-test
```

- [ ] **Testa systemd-service**
```bash
# Status
sudo systemctl status socket-listener

# Loggar
sudo journalctl -u socket-listener -f

# Skicka data
echo "Systemd test" | nc localhost 9999
```

---

# Del 5: Integration - sys-config.sh

## Nu sätter vi ihop allt!

- [ ] **Skapa det kompletta sys-config.sh**

```bash
#!/bin/bash
#===============================================================================
# sys-config.sh
#
# Automatiserar konfiguration av Ubuntu 24.04 server
# Grupp 3: Christian, Cebrail, Baraa, Marcus, Said
#
# Användning: sudo ./sys-config.sh
#===============================================================================

set -e  # Avbryt vid fel

#===============================================================================
# KONFIGURATION
#===============================================================================
USERS=("christian" "cebrail" "baraa" "marcus" "said")
GROUP_NAME="grupp3"
SHARED_DIR="/opt/grupp3"
SSH_PORT=2222
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

#===============================================================================
# HJÄLPFUNKTIONER
#===============================================================================
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

error() {
    echo "[ERROR] $1" >&2
    exit 1
}

#===============================================================================
# KONTROLLERA ATT SCRIPTET KÖRS SOM ROOT
#===============================================================================
if [[ $EUID -ne 0 ]]; then
    error "Detta script måste köras som root (använd sudo)"
fi

#===============================================================================
# DEL 1: ANVÄNDARE OCH GRUPPER
#===============================================================================
log "=== DEL 1: Skapar användare och grupper ==="

# Skapa gruppen
log "Skapar grupp: $GROUP_NAME"
groupadd "$GROUP_NAME" 2>/dev/null || true

# Skapa användare
for username in "${USERS[@]}"; do
    log "Skapar användare: $username"

    if ! id "$username" &>/dev/null; then
        useradd -m -s /bin/bash -G "$GROUP_NAME" "$username"
    else
        usermod -aG "$GROUP_NAME" "$username"
    fi

    # Fråga efter lösenord
    read -s -p "Ange lösenord för $username: " password
    echo

    # Sätt lösenord
    echo "$username:$password" | chpasswd

    # Tvinga lösenordsbyte
    chage -d 0 "$username"
done

# Skapa delad mapp
log "Skapar delad mapp: $SHARED_DIR"
mkdir -p "$SHARED_DIR"
chown root:"$GROUP_NAME" "$SHARED_DIR"
chmod 2770 "$SHARED_DIR"

# Konfigurera sudo
log "Konfigurerar sudo utan lösenord"
echo "%${GROUP_NAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/"$GROUP_NAME"
chmod 440 /etc/sudoers.d/"$GROUP_NAME"

#===============================================================================
# DEL 2: SYSTEMKONFIGURATION
#===============================================================================
log "=== DEL 2: Systemkonfiguration ==="

# Uppdatera system
log "Uppdaterar system..."
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Installera SSH
log "Installerar SSH-server..."
apt-get install -y openssh-server

# Konfigurera SSH
log "Konfigurerar SSH..."
cat > /etc/ssh/sshd_config.d/custom.conf << EOF
Port $SSH_PORT
PasswordAuthentication no
PubkeyAuthentication yes
AllowUsers ${USERS[*]}
PermitRootLogin no
EOF

systemctl restart sshd
systemctl enable sshd

# Ta bort ufw
log "Tar bort ufw..."
systemctl stop ufw 2>/dev/null || true
systemctl disable ufw 2>/dev/null || true
apt-get remove -y ufw 2>/dev/null || true

# Installera firewalld
log "Installerar och konfigurerar firewalld..."
apt-get install -y firewalld
systemctl start firewalld
systemctl enable firewalld

# Konfigurera brandvägg
firewall-cmd --permanent --set-default-zone=drop
firewall-cmd --permanent --zone=drop --add-port=${SSH_PORT}/tcp
firewall-cmd --reload

#===============================================================================
# DEL 3: DOCKER
#===============================================================================
log "=== DEL 3: Docker installation ==="

# Installera dependencies
apt-get install -y ca-certificates curl gnupg lsb-release

# Docker GPG-nyckel
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# Docker repo
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Installera Docker
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

systemctl start docker
systemctl enable docker

# Lägg till användare i docker-gruppen
log "Lägger till användare i docker-gruppen..."
for username in "${USERS[@]}"; do
    usermod -aG docker "$username"
done

#===============================================================================
# DEL 4: SOCKET-LISTENER TJÄNST
#===============================================================================
log "=== DEL 4: Socket-listener tjänst ==="

# Bygg Docker-imagen
log "Bygger Docker-image..."
docker build -t socket-listener:latest "$SCRIPT_DIR"

# Installera systemd-service
log "Installerar systemd-service..."
cp "$SCRIPT_DIR/socket-listener.service" /etc/systemd/system/

# Ladda om systemd
systemctl daemon-reload

# Aktivera och starta tjänsten
systemctl enable socket-listener
systemctl start socket-listener

#===============================================================================
# KLART!
#===============================================================================
log "=== INSTALLATION KLAR ==="
log ""
log "Sammanfattning:"
log "  - Användare skapade: ${USERS[*]}"
log "  - Grupp: $GROUP_NAME"
log "  - Delad mapp: $SHARED_DIR"
log "  - SSH-port: $SSH_PORT"
log "  - Socket-listener: port 9999"
log ""
log "OBS: Användare måste logga ut och in för att docker-gruppen ska gälla!"
log "OBS: SSH kräver pubkey-autentisering (lägg till nycklar i ~/.ssh/authorized_keys)"
```

---

# Del 6: Shellcheck & README

## 6.1 Kör Shellcheck

- [ ] **Installera shellcheck**
```bash
sudo apt-get install -y shellcheck
```

- [ ] **Kör shellcheck på alla scripts**
```bash
shellcheck sys-config.sh
shellcheck socket-listener.sh
```

- [ ] **Fixa alla fel och varningar**

**Vanliga shellcheck-varningar och lösningar:**

| Kod | Problem | Lösning |
|-----|---------|---------|
| SC2086 | Variabler utan quotes | Använd "$variable" istället för $variable |
| SC2034 | Oanvänd variabel | Ta bort eller använd variabeln |
| SC2164 | cd utan felhantering | Använd `cd dir || exit` |

---

## 6.2 Skapa README.md

- [ ] **Skapa README.md**

```markdown
# Linux Server Automation - Grupp 3

## Översikt

Detta projekt automatiserar konfigurationen av en Ubuntu 24.04 server.

## Gruppmedlemmar

- Christian
- Cebrail
- Baraa
- Marcus
- Said

## Filer

| Fil | Beskrivning |
|-----|-------------|
| `sys-config.sh` | Huvudscript för systemkonfiguration |
| `socket-listener.sh` | Script som lyssnar på TCP-socket |
| `Dockerfile` | Docker-image för socket-listener |
| `socket-listener.service` | Systemd service-fil |

## Förutsättningar

- Ubuntu 24.04
- Användaren som kör scriptet har sudo-rättigheter
- Internetanslutning
- Git installerat

## Användning

1. Klona repot:
   ```bash
   git clone https://git.chas-lab.dev/grupp3/linux-projekt.git
   cd linux-projekt
   ```

2. Gör scriptet körbart:
   ```bash
   chmod +x sys-config.sh
   ```

3. Kör scriptet som root:
   ```bash
   sudo ./sys-config.sh
   ```

4. Följ instruktionerna och ange lösenord för varje användare.

## Efter installation

- **SSH**: Anslut på port 2222 med pubkey-autentisering
- **Socket-listener**: Skicka data till port 9999
  ```bash
  echo "Hello" | nc localhost 9999
  ```

## Verifiering

Kontrollera att allt fungerar:

```bash
# Användare och grupp
getent group grupp3

# SSH
sudo systemctl status sshd

# Firewalld
sudo firewall-cmd --list-all

# Docker
docker --version

# Socket-listener
sudo systemctl status socket-listener
```
```

---

# Del 7: Sluttest

## Checklista för sluttest

- [ ] **1. Skapa en helt ny VM med Ubuntu 24.04**

- [ ] **2. Logga in och installera git**
```bash
sudo apt-get update && sudo apt-get install -y git
```

- [ ] **3. Klona ert repo**
```bash
git clone https://git.chas-lab.dev/<grupp>/linux-projekt.git
cd linux-projekt
```

- [ ] **4. Följ ENDAST dokumentationen i README.md**

- [ ] **5. Kör scriptet**
```bash
chmod +x sys-config.sh
sudo ./sys-config.sh
```

- [ ] **6. Verifiera varje del:**

### Användare och grupper
```bash
# Alla användare finns
id christian && id cebrail && id baraa && id marcus && id said

# Gruppen finns med alla medlemmar
getent group grupp3

# Delad mapp har rätt rättigheter (drwxrws---)
ls -la /opt/ | grep grupp3

# SGID fungerar (testa att skapa fil)
sudo -u christian touch /opt/grupp3/testfil
ls -la /opt/grupp3/testfil  # Ska visa grupp3 som grupp

# Sudo utan lösenord
sudo -u christian sudo whoami  # Ska svara root utan att fråga
```

### SSH
```bash
# SSH körs på rätt port
sudo ss -tlnp | grep 2222

# Konfigurationen är korrekt
grep -E "^Port|^PasswordAuthentication|^AllowUsers" /etc/ssh/sshd_config.d/custom.conf
```

### Brandvägg
```bash
# firewalld körs
sudo systemctl is-active firewalld

# ufw är borta
sudo systemctl is-active ufw  # Ska misslyckas

# Rätt regler
sudo firewall-cmd --list-all
```

### Docker
```bash
# Docker är installerat
docker --version
docker compose version

# Användare kan köra docker
sudo -u christian docker run hello-world
```

### Socket-listener
```bash
# Tjänsten körs
sudo systemctl is-active socket-listener

# Kan ta emot data
echo "Test $(date)" | nc localhost 9999

# Data sparas persistent
docker exec $(docker ps -q -f name=socket-listener) cat /data/messages.log
```

---

## 🎉 Om allt fungerar - NI ÄR KLARA!

---

# Appendix: Vanliga problem och lösningar

## Problem: "Permission denied" vid körning av script
```bash
# Lösning: Gör scriptet körbart
chmod +x sys-config.sh
```

## Problem: Docker-kommandon kräver sudo efter installation
```bash
# Lösning: Logga ut och in igen för att grupp-ändringen ska gälla
# ELLER kör:
newgrp docker
```

## Problem: SSH-anslutning nekas
```bash
# Kontrollera:
# 1. Rätt port (2222, inte 22)
# 2. Du har lagt till din pubkey i ~/.ssh/authorized_keys
# 3. Brandväggen tillåter porten
```

## Problem: Shellcheck klagar på variabel i heredoc
```bash
# Lösning: Använd \$ för variabler som ska expanderas inuti containern
# Exempel i socket-listener.sh:
timestamp=\$(date '+%Y-%m-%d %H:%M:%S')
```

## Problem: systemd-tjänsten startar inte
```bash
# Debug:
sudo journalctl -u socket-listener -f
# Kolla Docker-loggar:
docker logs socket-listener
```

---

# Tidsuppskattning

| Del | Ungefärlig tid |
|-----|----------------|
| Del 1: Användare & Grupper | 1-2 timmar |
| Del 2: Systemkonfiguration | 2-3 timmar |
| Del 3: Docker | 1 timme |
| Del 4: Socket & Systemd | 3-4 timmar |
| Del 5: Integration | 1-2 timmar |
| Del 6: Shellcheck & README | 1 timme |
| Del 7: Sluttest | 1-2 timmar |
| **TOTALT** | **10-15 timmar** |

---

*Guide skapad för DOE25 - Linux/Unix Server samt Bash Programmering*