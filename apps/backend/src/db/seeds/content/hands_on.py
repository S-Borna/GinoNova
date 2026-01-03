"""
Hands-On Lab — 7 praktiska övningar för Linux och DevOps
========================================================

Praktiska labbar som testar dina kunskaper i verkliga scenarier.

TASKS:
1. Onboarding - Filsystem & Texteditorer
2. Pakethantering & SSH-nycklar
3. SSH & Brandvägg
4. Användarhantering
5. Subnetting
6. Docker & Containers
7. Block Storage & Kryptering
"""

# =============================================================================
# TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER
# =============================================================================

ONBOARDING_NODE = {
    "title": "Onboarding - Filsystem & Texteditorer",
    "slug": "handson-onboarding",
    "description": "Lär dig navigera i Linux filsystem, skapa och hantera filer, samt använda Nano och Vim texteditorer.",
    "difficulty": "easy",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "order_index": 1,
    "content": r"""# Hands-On 1 – Onboarding 🎯

> **Mål:** Navigera i filsystemet, skapa och hantera filer, bekanta dig med Nano och Vim

---

## Del 1: Filsystemet – Din nya arbetsplats

### 1.1 Navigering

```bash
# Gå till din hemmapp
cd ~

# Visa aktuell sökväg
pwd

# Lista filer (inkl dolda)
ls -la
```

### 1.2 Skapa struktur

```bash
# Skapa en katalog
mkdir projekt

# Skapa flera nivåer på en gång
mkdir -p projekt/scripts/test

# Gå in i katalogen
cd projekt
```

---

## Del 2: Filhantering

### 2.1 Skapa filer

```bash
# Tom fil
touch README.md

# Fil med innehåll
echo "# Mitt projekt" > README.md

# Lägg till text (append)
echo "Version 1.0" >> README.md
```

### 2.2 Visa innehåll

```bash
# Visa allt
cat README.md

# Första/sista raderna
head -5 fil.txt
tail -10 fil.txt

# Interaktiv visning
less stor_fil.txt
```

### 2.3 Kopiera, flytta, ta bort

```bash
# Kopiera
cp fil.txt kopia.txt
cp -r mapp/ backup/

# Flytta/döp om
mv fil.txt ny_namn.txt
mv fil.txt annan_mapp/

# Ta bort
rm fil.txt
rm -r mapp/        # VARNING: ingen ångra!
```

---

## Del 3: Nano – Nybörjarvänlig editor

```bash
nano minscript.sh
```

**Kommandon (visas längst ner):**

| Genväg   | Funktion |
|----------|----------|
| Ctrl+O   | Spara    |
| Ctrl+X   | Avsluta  |
| Ctrl+K   | Klipp rad |
| Ctrl+U   | Klistra in |
| Ctrl+W   | Sök |

**Övning:**
1. Skapa fil: `nano hello.sh`
2. Skriv: `#!/bin/bash` och `echo "Hello World"`
3. Spara: Ctrl+O → Enter
4. Avsluta: Ctrl+X

---

## Del 4: Vim – Proffseditorn

```bash
vim minscript.sh
```

### Vim har två lägen:

| Läge | Tryck | Användning |
|------|-------|------------|
| **Normal** | Esc | Navigera, kommandon |
| **Insert** | i | Skriva text |

**De enda kommandona du behöver:**

| Kommando | Funktion |
|----------|----------|
| `i` | Insert mode (börja skriva) |
| `Esc` | Tillbaka till Normal |
| `:w` | Spara |
| `:q` | Avsluta |
| `:wq` | Spara och avsluta |
| `:q!` | Avsluta UTAN att spara |

**Övning:**
1. Öppna: `vim test.sh`
2. Tryck `i` för Insert
3. Skriv: `#!/bin/bash`
4. Tryck `Esc`
5. Skriv `:wq` och Enter

---

## Del 5: Praktisk övning

### Uppgift: Skapa ett projekt

```bash
# 1. Skapa struktur
mkdir -p ~/devops-lab/{scripts,logs,config}
cd ~/devops-lab

# 2. Skapa README
echo "# DevOps Lab" > README.md
echo "Skapad: $(date)" >> README.md

# 3. Skapa ett script med Nano
nano scripts/info.sh
```

Innehåll för scriptet:
```bash
#!/bin/bash
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Date: $(date)"
```

```bash
# 4. Gör körbart och kör
chmod +x scripts/info.sh
./scripts/info.sh
```

---

## ✅ Checklist

- [ ] Navigera med cd, pwd, ls
- [ ] Skapa kataloger med mkdir -p
- [ ] Hantera filer: touch, cp, mv, rm
- [ ] Redigera med Nano
- [ ] Grundläggande Vim (i, Esc, :wq)
- [ ] Skapa körbart script med chmod +x
"""
}

# =============================================================================
# TASK 2: PAKETHANTERING & SSH-NYCKLAR
# =============================================================================

PAKETHANTERING_SSH_NODE = {
    "title": "Pakethantering & SSH-nycklar",
    "slug": "handson-pakethantering-ssh",
    "description": "Hantera paket med APT, generera SSH-nycklar och konfigurera säker nyckel-baserad autentisering.",
    "difficulty": "easy",
    "estimated_minutes": 40,
    "xp_reward": 100,
    "order_index": 1,
    "content": r"""# Hands-On 2 – Pakethantering & SSH-nycklar 🎯

> **Mål:** Hantera paket med APT och sätta upp SSH-nycklar för säker inloggning

---

## Del 1: APT – Advanced Package Tool

### 1.1 Grundläggande kommandon

```bash
# Uppdatera paketlistor (gör ALLTID först)
sudo apt update

# Uppgradera installerade paket
sudo apt upgrade -y

# Sök efter paket
apt search nginx

# Visa info om paket
apt show nginx
```

### 1.2 Installera och ta bort

```bash
# Installera
sudo apt install nginx -y

# Ta bort (behåller config)
sudo apt remove nginx

# Ta bort ALLT (inkl config)
sudo apt purge nginx

# Städa bort oanvända beroenden
sudo apt autoremove
```

### 1.3 Praktisk övning

```bash
# Installera några användbara verktyg
sudo apt update
sudo apt install -y htop tree curl wget

# Testa
htop          # Interaktiv processvisare (q för att avsluta)
tree ~/       # Visa katalogstruktur som träd
```

---

## Del 2: SSH-nycklar

### 2.1 Varför nycklar istället för lösenord?

| Lösenord | SSH-nyckel |
|----------|------------|
| Kan gissas | Omöjligt att gissa |
| Måste skrivas varje gång | Automatisk inloggning |
| Sårbart för brute-force | Säkert mot attacker |

### 2.2 Generera nyckelpar

```bash
# Skapa nycklar (på din LOKALA dator)
ssh-keygen -t ed25519 -C "din@email.com"
```

**Frågor som kommer:**
- **Filnamn:** Tryck Enter för default (~/.ssh/id_ed25519)
- **Passphrase:** Valfritt extra lösenord (rekommenderas)

**Resultat:**
```
~/.ssh/id_ed25519      # PRIVAT nyckel (ALDRIG dela!)
~/.ssh/id_ed25519.pub  # Publik nyckel (kan delas)
```

### 2.3 Kopiera publik nyckel till server

**Metod 1: ssh-copy-id (enklast)**
```bash
ssh-copy-id user@server-ip
```

**Metod 2: Manuellt**
```bash
# Visa din publika nyckel
cat ~/.ssh/id_ed25519.pub

# På servern:
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
# Klistra in nyckeln

chmod 600 ~/.ssh/authorized_keys
```

### 2.4 Testa anslutning

```bash
# Ska fungera utan lösenord nu!
ssh user@server-ip
```

---

## Del 3: SSH Config – Genvägar

Skapa `~/.ssh/config`:

```bash
nano ~/.ssh/config
```

```
Host prod
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519

Host dev
    HostName 192.168.1.101
    User developer
    Port 2222
```

**Användning:**
```bash
# Istället för: ssh deploy@192.168.1.100
ssh prod

# Istället för: ssh -p 2222 developer@192.168.1.101
ssh dev
```

---

## Del 4: Praktisk övning

### Uppgift: Sätt upp komplett SSH

```bash
# 1. Generera nyckel (om du inte har)
ssh-keygen -t ed25519 -C "lab-key"

# 2. Visa dina nycklar
ls -la ~/.ssh/

# 3. Se innehållet i publika nyckeln
cat ~/.ssh/id_ed25519.pub

# 4. Skapa SSH config
nano ~/.ssh/config
```

Lägg till:
```
Host mylab
    HostName <server-ip>
    User <ditt-användarnamn>
    IdentityFile ~/.ssh/id_ed25519
```

```bash
# 5. Sätt rätt rättigheter
chmod 700 ~/.ssh
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

---

## ✅ Checklist

- [ ] Uppdatera paket med apt update/upgrade
- [ ] Installera paket med apt install
- [ ] Generera SSH-nyckelpar med ssh-keygen
- [ ] Förstå skillnaden privat/publik nyckel
- [ ] Konfigurera ~/.ssh/config för genvägar
- [ ] Sätta rätt rättigheter på SSH-filer
"""
}

# =============================================================================
# TASK 3: SSH & BRANDVÄGG
# =============================================================================

SSH_BRANDVAGG_NODE = {
    "title": "SSH & Brandvägg",
    "slug": "handson-ssh-brandvagg",
    "description": "Konfigurera SSH-servern säkert och sätt upp UFW brandvägg med korrekta regler.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "order_index": 2,
    "content": r"""# Hands-On 3 – SSH & Brandvägg 🎯

> **Mål:** Konfigurera SSH-servern för säkerhet och sätta upp UFW brandvägg

---

## Del 1: SSH Server Konfiguration

### 1.1 Konfigurera SSHD

```bash
# Backup först!
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Redigera
sudo nano /etc/ssh/sshd_config
```

**Viktiga inställningar:**

```bash
# Byt port (valfritt men rekommenderat)
Port 2222

# Förbjud root-login
PermitRootLogin no

# Endast nyckel-autentisering (efter att nycklar funkar!)
PasswordAuthentication no
PubkeyAuthentication yes

# Begränsa till specifika användare
AllowUsers deploy admin

# Timeout för inaktivitet
ClientAliveInterval 300
ClientAliveCountMax 2
```

### 1.2 Starta om SSH

```bash
# Validera config först!
sudo sshd -t

# Starta om tjänsten
sudo systemctl restart sshd

# Kontrollera status
sudo systemctl status sshd
```

⚠️ **VARNING:** Testa ALLTID i ny terminal innan du stänger den gamla!

---

## Del 2: UFW – Uncomplicated Firewall

### 2.1 Grundläggande setup

```bash
# Installera (ofta redan installerat)
sudo apt install ufw -y

# Se status
sudo ufw status

# Default policy: Blockera allt in, tillåt ut
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### 2.2 Tillåt tjänster

```bash
# SSH (VIKTIGT - gör detta INNAN du aktiverar!)
sudo ufw allow ssh
# eller specifik port
sudo ufw allow 2222/tcp

# Webserver
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
# eller
sudo ufw allow 'Nginx Full'

# Specifik IP
sudo ufw allow from 192.168.1.100

# Port-range
sudo ufw allow 3000:3010/tcp
```

### 2.3 Ta bort regler

```bash
# Visa regler med nummer
sudo ufw status numbered

# Ta bort regel nummer 3
sudo ufw delete 3

# Eller ta bort specifik regel
sudo ufw delete allow 80/tcp
```

### 2.4 Aktivera brandväggen

```bash
# Aktivera (säkerställ att SSH är tillåtet först!)
sudo ufw enable

# Visa status
sudo ufw status verbose
```

---

## Del 3: Praktisk lab – Säkra en server

### Steg 1: Förbered SSH

```bash
# 1. Verifiera att du kan logga in med nyckel
ssh -i ~/.ssh/id_ed25519 user@server

# 2. Backup SSH config
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

### Steg 2: Konfigurera SSH

```bash
sudo nano /etc/ssh/sshd_config
```

Ändra/lägg till:
```
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

### Steg 3: Sätt upp brandvägg

```bash
# Tillåt nya SSH-porten FÖRST
sudo ufw allow 2222/tcp

# Aktivera brandvägg
sudo ufw enable

# Verifiera
sudo ufw status
```

### Steg 4: Starta om SSH

```bash
# Validera config
sudo sshd -t

# Starta om
sudo systemctl restart sshd
```

### Steg 5: Testa (I NY TERMINAL!)

```bash
ssh -p 2222 user@server
```

---

## Del 4: Felsökning

### SSH problem

```bash
# Se SSH loggar
sudo journalctl -u sshd -f

# Testa SSH med verbose
ssh -v user@server

# Kontrollera att sshd lyssnar
sudo ss -tlnp | grep ssh
```

### UFW problem

```bash
# Se alla regler detaljerat
sudo ufw status verbose

# Kontrollera logs
sudo tail -f /var/log/ufw.log

# Tillfälligt inaktivera (för test)
sudo ufw disable
```

---

## ✅ Checklist

- [ ] Ändra SSH-port från default 22
- [ ] Inaktivera root-login
- [ ] Inaktivera lösenords-autentisering
- [ ] Konfigurera UFW default policies
- [ ] Tillåt SSH INNAN brandvägg aktiveras
- [ ] Testa ALLTID i ny terminal
"""
}

# =============================================================================
# TASK 4: ANVÄNDARHANTERING
# =============================================================================

ANVANDARHANTERING_NODE = {
    "title": "Användarhantering",
    "slug": "handson-anvandarhantering",
    "description": "Skapa användare och grupper, tilldela sudo-rättigheter och hantera hemkataloger.",
    "difficulty": "medium",
    "estimated_minutes": 40,
    "xp_reward": 110,
    "order_index": 3,
    "content": r"""# Hands-On 4 – Användarhantering 🎯

> **Mål:** Skapa användare, grupper och hantera behörigheter

---

## Del 1: Användare

### 1.1 Skapa användare

```bash
# Skapa användare med hemmapp
sudo useradd -m -s /bin/bash utvecklare

# Sätt lösenord
sudo passwd utvecklare

# Skapa med fler options
sudo useradd -m -s /bin/bash -c "Deploy User" -G sudo deploy
#          │   │            │                │
#          │   │            │                └── Lägg till i grupp
#          │   │            └── Kommentar/beskrivning
#          │   └── Shell
#          └── Skapa hemmapp
```

### 1.2 Modifiera användare

```bash
# Ändra shell
sudo usermod -s /bin/zsh utvecklare

# Lägg till i grupp
sudo usermod -aG docker utvecklare
#             │
#             └── append (lägg till, ta INTE bort från andra)

# Ändra hemmapp
sudo usermod -d /home/ny_mapp -m utvecklare
```

### 1.3 Ta bort användare

```bash
# Ta bort (behåll hemmapp)
sudo userdel utvecklare

# Ta bort MED hemmapp
sudo userdel -r utvecklare
```

---

## Del 2: Grupper

### 2.1 Hantera grupper

```bash
# Skapa grupp
sudo groupadd webteam

# Ta bort grupp
sudo groupdel webteam

# Se vilka grupper en användare tillhör
groups utvecklare

# Se alla medlemmar i en grupp
getent group webteam
```

### 2.2 Gruppmedlemskap

```bash
# Lägg till användare i grupp
sudo usermod -aG webteam utvecklare

# Sätt primär grupp
sudo usermod -g webteam utvecklare

# Ta bort från grupp
sudo gpasswd -d utvecklare webteam
```

---

## Del 3: Sudo-rättigheter

### 3.1 Lägga till sudo-rättigheter

```bash
# Lägg till i sudo-gruppen
sudo usermod -aG sudo användarnamn

# Eller redigera sudoers (säkrare metod)
sudo visudo
```

### 3.2 Sudoers-filen

```bash
# I /etc/sudoers:

# Användare får köra allt
utvecklare ALL=(ALL:ALL) ALL

# Användare får köra allt utan lösenord
deploy ALL=(ALL) NOPASSWD: ALL

# Användare får bara vissa kommandon
backup ALL=(ALL) NOPASSWD: /usr/bin/rsync, /usr/bin/tar

# Grupp får köra allt
%webteam ALL=(ALL:ALL) ALL
```

### 3.3 Säkrare: sudoers.d

```bash
# Skapa separat fil istället
sudo nano /etc/sudoers.d/deploy
```

```
deploy ALL=(ALL) NOPASSWD: ALL
```

```bash
# Sätt rätt rättigheter
sudo chmod 440 /etc/sudoers.d/deploy
```

---

## Del 4: Praktisk övning

### Uppgift: Sätt upp projektteam

**Scenario:** Skapa ett team med tre användare och rätt behörigheter.

```bash
# 1. Skapa grupp
sudo groupadd devteam

# 2. Skapa användare
sudo useradd -m -s /bin/bash -c "Lead Developer" -G devteam lead
sudo useradd -m -s /bin/bash -c "Backend Dev" -G devteam backend
sudo useradd -m -s /bin/bash -c "Frontend Dev" -G devteam frontend

# 3. Sätt lösenord
sudo passwd lead
sudo passwd backend
sudo passwd frontend

# 4. Ge lead sudo-rättigheter
sudo usermod -aG sudo lead

# 5. Verifiera
id lead
id backend
groups lead
```

### Skapa delad projektmapp

```bash
# Skapa mapp
sudo mkdir -p /var/www/projekt

# Sätt ägarskap till gruppen
sudo chown -R root:devteam /var/www/projekt

# Sätt rättigheter (gruppen kan skriva)
sudo chmod -R 775 /var/www/projekt

# Sätt SGID (nya filer ärver gruppen)
sudo chmod g+s /var/www/projekt
```

---

## Del 5: Viktiga filer

| Fil | Innehåll |
|-----|----------|
| `/etc/passwd` | Användarlista |
| `/etc/shadow` | Krypterade lösenord |
| `/etc/group` | Grupplista |
| `/etc/sudoers` | Sudo-konfiguration |

```bash
# Visa användare
cat /etc/passwd | grep bash

# Visa grupper
cat /etc/group | grep devteam
```

---

## ✅ Checklist

- [ ] Skapa användare med useradd -m -s /bin/bash
- [ ] Skapa och hantera grupper
- [ ] Lägga till användare i grupper med usermod -aG
- [ ] Konfigurera sudo via visudo eller sudoers.d
- [ ] Skapa delad mapp med rätt grupp-rättigheter
"""
}

# =============================================================================
# TASK 5: SUBNETTING
# =============================================================================

SUBNETTING_NODE = {
    "title": "Subnetting",
    "slug": "handson-subnetting",
    "description": "Beräkna subnät, nätverksadresser och broadcast med lådmetoden - praktiska övningar.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "order_index": 4,
    "content": r"""# Hands-On 5 – Subnetting 🎯

> **Mål:** Förstå och räkna subnät, nätverksadresser och broadcast

---

## Del 1: Grunderna

### 1.1 IP-adressens uppbyggnad

```
192.168.1.147/24
└───────────┘ └┘
IP-adress    Prefix (subnätmask)
```

**Prefixet** bestämmer hur mycket som är nätverk vs host:
- **/24** = 24 bitar för nätverk, 8 bitar för hosts
- **/28** = 28 bitar för nätverk, 4 bitar för hosts

### 1.2 Lådmetoden

**Memorera dessa värden:**

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
└─────┴────┴────┴────┴───┴───┴───┴───┘
   1     2    3    4   5   6   7   8
```

---

## Del 2: Steg-för-steg

### Exempel: 192.168.1.147/26

**Steg 1: Räkna host-bitar**
```
32 - 26 = 6 host-bitar
```

**Steg 2: Blockstorlek**
```
2^6 = 64 adresser per subnät
```

**Steg 3: Hitta subnät-gränser**
```
0, 64, 128, 192, 256 (slut)
     └─ 147 faller här (mellan 128 och 192)
```

**Resultat:**
- **Nätverksadress:** 192.168.1.128
- **Broadcast:** 192.168.1.191 (nästa block - 1)
- **Host-range:** 192.168.1.129 - 192.168.1.190
- **Antal hosts:** 64 - 2 = 62

---

## Del 3: Praktiska övningar

### Övning 1: /28 nätverk

**IP: 10.0.0.147/28**

```
Host-bitar: 32 - 28 = 4
Blockstorlek: 2^4 = 16

Subnät: 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160...
                                              └─ 147 här!

Nätverksadress: 10.0.0.144
Broadcast: 10.0.0.159
Host-range: 10.0.0.145 - 10.0.0.158
Antal hosts: 16 - 2 = 14
```

### Övning 2: /27 nätverk

**IP: 172.16.10.200/27**

```
Host-bitar: 32 - 27 = 5
Blockstorlek: 2^5 = 32

Subnät: 0, 32, 64, 96, 128, 160, 192, 224...
                                └─ 200 här!

Nätverksadress: 172.16.10.192
Broadcast: 172.16.10.223
Host-range: 172.16.10.193 - 172.16.10.222
Antal hosts: 32 - 2 = 30
```

### Övning 3: /22 nätverk (spänner över oktetter)

**IP: 192.168.5.100/22**

```
Host-bitar: 32 - 22 = 10
Blockstorlek: 2^10 = 1024

/22 påverkar tredje oktetten:
1024 / 256 = 4 (varje subnät tar 4 värden i tredje oktetten)

Tredje oktetten: 5
5 / 4 = 1 (rest 1) → start vid 1*4 = 4

Nätverksadress: 192.168.4.0
Broadcast: 192.168.7.255
Host-range: 192.168.4.1 - 192.168.7.254
Antal hosts: 1024 - 2 = 1022
```

---

## Del 4: Subnätmask konvertering

### Prefix till subnätmask

| Prefix | Subnätmask | Hosts |
|--------|------------|-------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

### Räkna ut manuellt

**Exempel: /27**
```
Host-bitar: 32 - 27 = 5
Nätverksdelen i sista oktetten: 8 - 5 = 3 bitar

Nätverksbitar: 128 + 64 + 32 = 224
Subnätmask: 255.255.255.224
```

---

## Del 5: Labba med Linux-verktyg

```bash
# Installera ipcalc
sudo apt install ipcalc -y

# Räkna ut subnät
ipcalc 192.168.1.147/26
```

**Output:**
```
Address:   192.168.1.147
Netmask:   255.255.255.192 = 26
Network:   192.168.1.128/26
Broadcast: 192.168.1.191
HostMin:   192.168.1.129
HostMax:   192.168.1.190
Hosts/Net: 62
```

```bash
# Visa nätverksinfo
ip addr show
ip route
```

---

## Del 6: Tenta-förberedelse

### Snabbmetod för vanliga prefix

| Prefix | Blockstorlek |
|--------|--------------|
| /24 | 256 (hel oktett) |
| /25 | 128 |
| /26 | 64 |
| /27 | 32 |
| /28 | 16 |
| /29 | 8 |
| /30 | 4 |

**Formel:** `Blockstorlek = 2^(32-prefix)`

---

## ✅ Checklist

- [ ] Förstå prefix och host-bitar
- [ ] Räkna ut blockstorlek (2^host-bitar)
- [ ] Hitta nätverksadress och broadcast
- [ ] Beräkna host-range och antal hosts
- [ ] Konvertera prefix ↔ subnätmask
- [ ] Använda ipcalc för verifiering
"""
}

# =============================================================================
# TASK 6: DOCKER & CONTAINERS
# =============================================================================

DOCKER_CONTAINERS_NODE = {
    "title": "Docker & Containers",
    "slug": "handson-docker-containers",
    "description": "Installera Docker, kör containers, bygg images och använd Docker Compose.",
    "difficulty": "medium",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "order_index": 5,
    "content": r"""# Hands-On 6 – Docker & Containers 🎯

> **Mål:** Installera Docker, köra containers, bygga images och använda Compose

---

## Del 1: Installation

### Ubuntu/Debian

```bash
# Installera dependencies
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg

# Lägg till Dockers GPG-nyckel
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Lägg till repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Kör Docker utan sudo
sudo usermod -aG docker $USER
newgrp docker

# Verifiera
docker --version
docker run hello-world
```

---

## Del 2: Grundläggande kommandon

### 2.1 Köra containers

```bash
# Kör interaktivt
docker run -it ubuntu bash

# Kör i bakgrunden (detached)
docker run -d nginx

# Kör med portmappning
docker run -d -p 8080:80 nginx
#              │    │
#              │    └── Container-port
#              └── Host-port

# Kör med namn
docker run -d --name webserver -p 8080:80 nginx
```

### 2.2 Hantera containers

```bash
# Lista körande
docker ps

# Lista alla (inkl stoppade)
docker ps -a

# Stoppa
docker stop webserver

# Starta igen
docker start webserver

# Ta bort
docker rm webserver

# Ta bort körande (force)
docker rm -f webserver
```

### 2.3 Images

```bash
# Lista images
docker images

# Ladda ner image
docker pull nginx:latest

# Ta bort image
docker rmi nginx:latest

# Städa oanvända
docker system prune -a
```

---

## Del 3: Bygga images

### 3.1 Dockerfile

```dockerfile
# Skapa Dockerfile
FROM node:18-alpine

WORKDIR /app

# Kopiera och installera beroenden
COPY package*.json ./
RUN npm install

# Kopiera applikation
COPY . .

# Exponera port
EXPOSE 3000

# Starta app
CMD ["npm", "start"]
```

### 3.2 Bygga och köra

```bash
# Bygg image
docker build -t min-app:1.0 .

# Kör
docker run -d -p 3000:3000 min-app:1.0

# Se logs
docker logs -f <container-id>
```

---

## Del 4: Docker Compose

### 4.1 docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp

volumes:
  pgdata:
```

### 4.2 Compose-kommandon

```bash
# Starta alla tjänster
docker compose up -d

# Se status
docker compose ps

# Se logs
docker compose logs -f

# Stoppa
docker compose down

# Stoppa och ta bort volumes
docker compose down -v
```

---

## Del 5: Praktisk övning

### Uppgift: Sätt upp en webbstack

**1. Skapa projektmapp:**
```bash
mkdir webapp && cd webapp
```

**2. Skapa en enkel app (index.html):**
```html
<!DOCTYPE html>
<html>
<head><title>Docker Lab</title></head>
<body><h1>Hello from Docker!</h1></body>
</html>
```

**3. Skapa Dockerfile:**
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```

**4. Skapa docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8080:80"
    restart: unless-stopped
```

**5. Kör:**
```bash
docker compose up -d
curl http://localhost:8080
```

---

## Del 6: Felsökning

```bash
# Gå in i körande container
docker exec -it <container> bash

# Inspektera container
docker inspect <container>

# Se resursanvändning
docker stats

# Se nätverk
docker network ls
docker network inspect bridge
```

---

## ✅ Checklist

- [ ] Installera Docker
- [ ] Köra containers med docker run
- [ ] Hantera containers: ps, stop, start, rm
- [ ] Bygga images med Dockerfile
- [ ] Använda docker compose
- [ ] Felsöka med exec och logs
"""
}

# =============================================================================
# TASK 7: BLOCK STORAGE & KRYPTERING
# =============================================================================

BLOCK_STORAGE_KRYPTERING_NODE = {
    "title": "Block Storage & Kryptering",
    "slug": "handson-block-storage-kryptering",
    "description": "Hantera diskar med LVM, skapa filsystem och konfigurera LUKS-kryptering.",
    "difficulty": "hard",
    "estimated_minutes": 60,
    "xp_reward": 150,
    "order_index": 6,
    "content": r"""# Hands-On 7 – Block Storage & Kryptering 🎯

> **Mål:** Hantera diskar, LVM och sätta upp LUKS-kryptering

---

## Del 1: Diskar och partitioner

### 1.1 Se diskar

```bash
# Lista block devices
lsblk

# Detaljerad info
sudo fdisk -l

# Diskutrymme
df -h
```

**Output (lsblk):**
```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0    20G  0 disk
├─sda1   8:1    0   512M  0 part /boot
└─sda2   8:2    0  19.5G  0 part /
sdb      8:16   0    10G  0 disk
```

### 1.2 Partitionera ny disk

```bash
# Använd fdisk
sudo fdisk /dev/sdb
```

**Interaktiva kommandon:**
- `n` – Skapa ny partition
- `p` – Primär partition
- `1` – Partitionsnummer
- Enter – Första sektor (default)
- Enter – Sista sektor (hela disken)
- `w` – Skriv och avsluta

### 1.3 Skapa filsystem

```bash
# ext4 (vanligast för Linux)
sudo mkfs.ext4 /dev/sdb1

# XFS (bra för stora filer)
sudo mkfs.xfs /dev/sdb1
```

### 1.4 Mounta

```bash
# Skapa mount-punkt
sudo mkdir /mnt/data

# Mounta
sudo mount /dev/sdb1 /mnt/data

# Permanent mount (fstab)
echo '/dev/sdb1 /mnt/data ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

---

## Del 2: LVM – Logical Volume Manager

### 2.1 Varför LVM?

- **Flexibilitet:** Ändra storlek utan omstart
- **Snapshots:** Ta backup av volumes
- **Spanning:** Kombinera flera diskar

### 2.2 LVM-struktur

```
┌─────────────────────────────────────┐
│          Logical Volumes (LV)       │  ← Filsystem här
│     /dev/vg_data/lv_files           │
├─────────────────────────────────────┤
│          Volume Group (VG)          │  ← Pool av disk-space
│              vg_data                │
├─────────────────────────────────────┤
│       Physical Volumes (PV)         │  ← Fysiska diskar
│    /dev/sdb1        /dev/sdc1       │
└─────────────────────────────────────┘
```

### 2.3 Skapa LVM

```bash
# Installera verktyg
sudo apt install lvm2 -y

# 1. Skapa Physical Volume
sudo pvcreate /dev/sdb1

# 2. Skapa Volume Group
sudo vgcreate vg_data /dev/sdb1

# 3. Skapa Logical Volume (5GB)
sudo lvcreate -L 5G -n lv_files vg_data

# 4. Skapa filsystem
sudo mkfs.ext4 /dev/vg_data/lv_files

# 5. Mounta
sudo mkdir /mnt/files
sudo mount /dev/vg_data/lv_files /mnt/files
```

### 2.4 LVM-kommandon

```bash
# Visa info
sudo pvs          # Physical volumes
sudo vgs          # Volume groups
sudo lvs          # Logical volumes

# Utöka LV
sudo lvextend -L +2G /dev/vg_data/lv_files

# Utöka filsystem (ext4)
sudo resize2fs /dev/vg_data/lv_files

# Utöka filsystem (xfs)
sudo xfs_growfs /mnt/files
```

---

## Del 3: LUKS Kryptering

### 3.1 Varför kryptera?

- **Datasäkerhet:** Skyddar vid fysisk stöld
- **Compliance:** Krav i många branscher
- **Enkel hantering:** Transparent för applikationer

### 3.2 Sätt upp LUKS

```bash
# Installera verktyg
sudo apt install cryptsetup -y

# Formattera partition med LUKS
sudo cryptsetup luksFormat /dev/sdb1
```

⚠️ **VARNING:** Detta raderar ALL data på partitionen!

```bash
# Öppna krypterad disk
sudo cryptsetup luksOpen /dev/sdb1 krypterad_disk
# Skapar: /dev/mapper/krypterad_disk

# Skapa filsystem
sudo mkfs.ext4 /dev/mapper/krypterad_disk

# Mounta
sudo mkdir /mnt/secure
sudo mount /dev/mapper/krypterad_disk /mnt/secure
```

### 3.3 Stänga krypterad disk

```bash
# Avmontera
sudo umount /mnt/secure

# Stäng LUKS
sudo cryptsetup luksClose krypterad_disk
```

### 3.4 Automatisk mount vid boot

**1. Hitta UUID:**
```bash
sudo blkid /dev/sdb1
```

**2. Skapa nyckel-fil:**
```bash
sudo dd if=/dev/urandom of=/root/.luks-key bs=512 count=4
sudo chmod 400 /root/.luks-key

# Lägg till nyckel till LUKS
sudo cryptsetup luksAddKey /dev/sdb1 /root/.luks-key
```

**3. Konfigurera /etc/crypttab:**
```bash
# UUID=<disk-uuid> /root/.luks-key luks
krypterad_disk UUID=<din-uuid> /root/.luks-key luks
```

**4. Konfigurera /etc/fstab:**
```bash
/dev/mapper/krypterad_disk /mnt/secure ext4 defaults 0 2
```

---

## Del 4: Praktisk övning

### Uppgift: LVM + LUKS kombination

```bash
# 1. Skapa LUKS på partition
sudo cryptsetup luksFormat /dev/sdb1
sudo cryptsetup luksOpen /dev/sdb1 crypt_pv

# 2. Använd som LVM Physical Volume
sudo pvcreate /dev/mapper/crypt_pv
sudo vgcreate vg_secure /dev/mapper/crypt_pv
sudo lvcreate -L 4G -n lv_data vg_secure

# 3. Skapa filsystem och mounta
sudo mkfs.ext4 /dev/vg_secure/lv_data
sudo mkdir /mnt/secure_data
sudo mount /dev/vg_secure/lv_data /mnt/secure_data

# 4. Verifiera
df -h /mnt/secure_data
sudo lvs vg_secure
```

---

## ✅ Checklist

- [ ] Lista diskar med lsblk och fdisk -l
- [ ] Skapa partitioner med fdisk
- [ ] Skapa filsystem med mkfs
- [ ] Förstå LVM: PV → VG → LV
- [ ] Skapa och utöka LVM volumes
- [ ] Sätta upp LUKS-kryptering
- [ ] Kombinera LUKS med LVM
"""
}

# =============================================================================
# MODULE DEFINITION
# =============================================================================

MODULE = {
    "name": "Hands-On Lab",
    "slug": "hands-on-lab",
    "description": "Praktiska labbar som tar dig från grunderna till avancerade Linux- och DevOps-koncept genom hands-on övningar.",
    "icon": "🔬",
    "order_index": 2,
    "category": "practical",
    "difficulty": "intermediate",
    "estimated_hours": 6,
    "tasks": [
        ONBOARDING_NODE,
        PAKETHANTERING_SSH_NODE,
        SSH_BRANDVAGG_NODE,
        ANVANDARHANTERING_NODE,
        SUBNETTING_NODE,
        DOCKER_CONTAINERS_NODE,
        BLOCK_STORAGE_KRYPTERING_NODE,
    ]
}
