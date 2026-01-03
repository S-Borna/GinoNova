// Hands-On Lab Module - 7 Praktiska Tasks med Markdown Content
// Interfaces

export interface QuizOption {
    text: string;
    correct?: boolean;
    feedback?: string;
}

export interface CompareItem {
    name: string;
    pros: string[];
    cons: string[];
    use_case?: string;
}

export interface ContentBlock {
    type: string;
    title?: string;
    headline?: string;
    explanation?: string;
    code?: string;
    language?: string;
    options?: QuizOption[];
    question?: string;
    hint?: string;
    pro_tip?: string;
    warning?: string;
    warning_level?: string;
    learning_objectives?: string[];
    scenario_title?: string;
    scenario_context?: string;
    scenario_symptoms?: string[];
    scenario_solution?: string;
    challenge_task?: string;
    challenge_commands?: string[];
    expected_output?: string;
    diagram?: string;
    diagram_caption?: string;
    message?: string;
    items?: string[];
    compare_items?: CompareItem[];
    summary_title?: string;
    key_points?: string[];
    next_step?: string;
}

export interface HandsOnTask {
    id: string;
    title: string;
    description: string;
    order_index: number;
    estimated_minutes: number;
    content?: string;  // Markdown content
    content_blocks?: ContentBlock[];
}

export interface HandsOnModule {
    id: string;
    name: string;
    slug: string;
    description: string;
    difficulty: "beginner" | "intermediate" | "advanced" | "expert";
    estimated_hours: number;
    tasks: HandsOnTask[];
}

// ============================================
// SLUG TO ID MAPPING
// ============================================
export const SLUG_TO_ID: Record<string, string> = {
    "handson-onboarding": "handson-1-onboarding",
    "handson-pakethantering-ssh": "handson-2-pakethantering",
    "handson-ssh-brandvagg": "handson-3-ssh-brandvagg",
    "handson-anvandarhantering": "handson-4-anvandarhantering",
    "handson-subnetting": "handson-5-subnetting",
    "handson-docker-containers": "handson-6-docker",
    "handson-block-storage-kryptering": "handson-7-storage",
};

// ============================================
// MARKDOWN CONTENT FOR EACH TASK
// ============================================

const ONBOARDING_CONTENT = `# Linux Hands-On: Filsystem & Texteditorer

## Sammanfattning för Tenta

---

## 📋 Innehållsförteckning

1. [Navigering i Filsystemet](#navigering-i-filsystemet)
2. [Filhantering](#filhantering)
3. [Läsa & Söka](#läsa--söka)
4. [Dokumentation](#dokumentation)
5. [Texteditorer](#texteditorer)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Cheat Sheet](#cheat-sheet)

---

## 🗂️ Navigering i Filsystemet

### Grundkommandon

**\`pwd\`** - Print Working Directory

- Visar din nuvarande position i filsystemet
- Exempel: \`/home/username\`

**\`cd\`** - Change Directory

\`\`\`bash
cd /home/username    # Absolut path (börjar med /)
cd Documents         # Relativ path (från nuvarande position)
cd ..               # Upp en nivå
cd ~                # Till hemmamapp (samma som cd utan argument)
cd                  # Till hemmamapp
cd -                # Till föregående directory
\`\`\`

**\`ls\`** - List directory contents

\`\`\`bash
ls                  # Lista filer i nuvarande mapp
ls /home           # Lista filer i specifik mapp
ls -l              # Long listing format (detaljerad info)
ls -a              # Visa dolda filer (börjar med .)
ls -t              # Sortera efter tid (nyast först)
ls -la             # Kombination av flaggor
ls -lta            # Alla flaggor tillsammans
\`\`\`

### 🎯 Viktiga Paths

| Path | Beskrivning |
|------|-------------|
| \`/\` | Root (roten av filsystemet) |
| \`/home\` | Användares hemmamappar |
| \`/etc\` | Konfigurationsfiler |
| \`/var\` | Loggar och varierande data |
| \`/bin\` | Viktiga program/kommandon |
| \`/tmp\` | Temporära filer |
| \`~\` | Din hemmamapp (shortcut) |
| \`.\` | Nuvarande mapp |
| \`..\` | Mapp en nivå upp |

---

## 📁 Filhantering

### Skapa & Ta Bort

**\`touch\`** - Skapa tom fil

\`\`\`bash
touch myfile.txt
touch file1 file2 file3    # Skapa flera filer
\`\`\`

**\`mkdir\`** - Make Directory

\`\`\`bash
mkdir myfolder
mkdir -p parent/child/grandchild    # Skapa hela strukturer
\`\`\`

**\`rm\`** - Remove (radera filer)

\`\`\`bash
rm myfile.txt
rm -r myfolder              # Recursive (hela mappar)
rm -f myfile.txt            # Force (ingen prompt)
rm -rf myfolder             # Kombinera flaggor
\`\`\`

⚠️ **VARNING**: \`rm\` har ingen ångra-funktion och ingen papperskorg!

**\`rmdir\`** - Remove Directory (endast tomma mappar)

\`\`\`bash
rmdir emptyfolder
\`\`\`

### Kopiera & Flytta

**\`cp\`** - Copy

\`\`\`bash
cp source.txt destination.txt
cp file.txt backup.txt
cp -r folder1 folder2        # Kopiera mappar
\`\`\`

**\`mv\`** - Move (även för att byta namn)

\`\`\`bash
mv oldname.txt newname.txt   # Byt namn
mv file.txt /home/user/      # Flytta fil
mv folder1 folder2           # Flytta/byt namn på mapp
\`\`\`

⚠️ **OBS**: \`mv\` överskriver filer utan varning!

---

## 🔍 Läsa & Söka

### Visa Filinnehåll

**\`cat\`** - Concatenate (visa hela filen)

\`\`\`bash
cat myfile.txt
cat file1.txt file2.txt      # Visa flera filer
\`\`\`

### Pagers (sidvy)

**\`less\`** - Moderna pager (rekommenderad)

\`\`\`bash
less myfile.txt
ps aux | less                # Pipe output till less
\`\`\`

Navigering i \`less\`:

- \`j\` / \`↓\` - Ner en rad
- \`k\` / \`↑\` - Upp en rad
- \`Space\` / \`Page Down\` - Ner en sida
- \`Page Up\` - Upp en sida
- \`/sökterm\` - Sök
- \`n\` - Nästa sökmatch
- \`N\` - Föregående sökmatch
- \`q\` - Avsluta

**\`more\`** - Äldre pager (begränsad)

- Kan bara scrolla nedåt
- \`Space\` eller \`Enter\` för nästa sida

> 💡 **Tips**: "Less does more than more" - använd \`less\`!

### Söka i Filsystemet

**\`find\`** - Sök efter filer och mappar

\`\`\`bash
find                         # Lista allt i nuvarande mapp
find /home                   # Lista allt under /home
find -type f                 # Bara filer
find -type d                 # Bara mappar
find -name "*bash*"          # Sök efter namn med "bash"
\`\`\`

---

## 📚 Dokumentation

### Man Pages (Manual Pages)

**\`man\`** - Visa manualsidor

\`\`\`bash
man ls                       # Manual för ls
man rm                       # Manual för rm
man man                      # Manual för man (viktigt!)
\`\`\`

#### Man Page Sektioner

| Sektion | Innehåll |
|---------|----------|
| 1 | Kommandon och program |
| 2 | System calls (C-funktioner) |
| 3 | Bibliotek |
| 5 | Filformat |
| 8 | Systemadministration |

Navigering i man pages:

- Samma som i \`less\` (j/k, space, /, n, q)
- \`h\` - Hjälp
- \`q\` - Avsluta

### Info Pages

**\`info\`** - Alternativ dokumentation

\`\`\`bash
info info                    # Lär dig info-systemet
info ls                      # Info om ls
\`\`\`

- Mer strukturerad än man pages
- Länkar mellan sektioner
- \`Tab\` - Nästa länk
- \`Enter\` - Följ länk
- \`q\` - Avsluta

---

## ✏️ Texteditorer

### Vim

**Starta Vim**

\`\`\`bash
vim myfile.txt
vimtutor                     # Interaktiv tutorial (VIKTIGT!)
\`\`\`

#### Vim Basics (från vimtutor)

**Lägen:**

- Normal mode (default) - för navigation och kommandon
- Insert mode - för att skriva text
- Command mode - för kommandon som spara/avsluta

**Grundläggande kommandon:**

\`\`\`vim
i          # Insert mode (börja skriva)
Esc        # Tillbaka till Normal mode
:w         # Spara (write)
:q         # Avsluta (quit)
:wq        # Spara och avsluta
:q!        # Avsluta utan att spara
h j k l    # Vänster, ner, upp, höger (i Normal mode)
x          # Radera tecken
dd         # Radera rad
u          # Ångra (undo)
/sökterm   # Sök
n          # Nästa sökmatch
\`\`\`

> 🎯 **Kom ihåg**: "How do I exit vim?" → \`:q\` eller \`:q!\`

**Vim Swap Files**

- Vim skapar \`.swp\` filer som backup
- Tas bort automatiskt när du avslutar korrekt
- Kvarstår om Vim kraschar

### Emacs (Frivilligt)

**Installation:**

\`\`\`bash
# Ubuntu
sudo apt install emacs-nox

# Fedora
sudo dnf install emacs-nox
\`\`\`

**Viktiga kortkommandon i Bash (Emacs-stil):**

- \`Ctrl-A\` - Början av rad
- \`Ctrl-E\` - Slutet av rad
- \`Ctrl-K\` - Radera resten av raden
- \`Ctrl-L\` - Rensa skärmen (samma som \`clear\`)

---

## 💡 Viktiga Koncept

### Absoluta vs Relativa Paths

**Absolut path** - Börjar med \`/\`

\`\`\`bash
cd /home/username/Documents  # Fungerar var du än är
ls /etc
\`\`\`

**Relativ path** - Börjar INTE med \`/\`

\`\`\`bash
cd Documents                 # Från nuvarande position
ls ../other-folder          # Relativ till nuvarande
\`\`\`

### Hidden Files

- Filer som börjar med \`.\` är "dolda"
- Visas inte med vanligt \`ls\`
- Använd \`ls -a\` för att se dem
- Exempel: \`.bashrc\`, \`.viminfo\`, \`.bash_history\`

### Tab Completion

- Tryck \`Tab\` för att autocomplete kommandon och filnamn
- Dubbel-\`Tab\` visar alla möjliga alternativ
- Sparar tid och minskar felstavningar!

\`\`\`bash
cd Doc[TAB]      # Kompletterar till Documents/
ls myf[TAB]      # Kompletterar till myfile om unikt
\`\`\`

### Farliga Kommandon ⚠️

\`\`\`bash
rm -rf /                     # RADERA ALLT (kräver --no-preserve-root)
rm -rf /*                    # RADERA ALLT
rm -rf ~                     # RADERA HELA HEMMAMAP
mv file.txt existing.txt     # Överskriver utan varning
\`\`\`

**Gyllene regel**: **Think before you type!**

---

## 📋 Cheat Sheet

### Snabbkommando

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| \`pwd\` | Visa nuvarande mapp | \`pwd\` |
| \`cd\` | Byt mapp | \`cd /home\` |
| \`ls\` | Lista filer | \`ls -la\` |
| \`touch\` | Skapa tom fil | \`touch file.txt\` |
| \`mkdir\` | Skapa mapp | \`mkdir folder\` |
| \`rm\` | Ta bort | \`rm file.txt\` |
| \`cp\` | Kopiera | \`cp a.txt b.txt\` |
| \`mv\` | Flytta/byt namn | \`mv old.txt new.txt\` |
| \`cat\` | Visa fil | \`cat file.txt\` |
| \`less\` | Bläddra fil | \`less file.txt\` |
| \`find\` | Sök filer | \`find -name "*.txt"\` |
| \`man\` | Manual | \`man ls\` |
| \`vim\` | Öppna Vim | \`vim file.txt\` |

### Vim Snabbkommandon

| Kommando | Beskrivning |
|----------|-------------|
| \`i\` | Insert mode |
| \`Esc\` | Normal mode |
| \`:w\` | Spara |
| \`:q\` | Avsluta |
| \`:wq\` | Spara och avsluta |
| \`:q!\` | Avsluta utan spara |
| \`h j k l\` | Vänster, ner, upp, höger |
| \`dd\` | Radera rad |
| \`u\` | Ångra |
| \`/text\` | Sök efter "text" |
`;

const PAKETHANTERING_SSH_CONTENT = `# Linux Pakethantering & SSH-nycklar

## Sammanfattning för Tenta

---

## 📋 Innehållsförteckning

1. [Systemuppgradering](#systemuppgradering)
2. [Pakethantering - APT (Ubuntu/Debian)](#pakethantering---apt-ubuntudebian)
3. [Pakethantering - DNF (Fedora)](#pakethantering---dnf-fedora)
4. [Lågnivå Pakethantering](#lågnivå-pakethantering)
5. [SSH-nycklar](#ssh-nycklar)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Cheat Sheet](#cheat-sheet)

---

## 🔄 Systemuppgradering

### Ubuntu/Debian (APT)

**Komplett uppgraderingsprocess:**

\`\`\`bash
sudo apt update              # Uppdatera paketdatabasen
sudo apt upgrade             # Uppgradera installerade paket
sudo reboot                  # Starta om (om kärnan uppgraderats)
\`\`\`

**Steg för steg:**

1. **\`sudo apt update\`**
   - Uppdaterar metadata om tillgängliga paket
   - Kontaktar HTTP-tjänster (repositories)
   - Kräver sudo (administratörsrättigheter)

2. **Kontrollera uppgraderingsbara paket:**

   \`\`\`bash
   apt list --upgradable       # Ingen sudo behövs (bara listar)
   \`\`\`

3. **\`sudo apt upgrade\`**
   - Applicerar uppgraderingar
   - Visar översikt innan installation
   - Frågar om bekräftelse (Y/n)

### Fedora (DNF)

**Komplett uppgraderingsprocess:**

\`\`\`bash
sudo dnf check-upgrade       # Kolla tillgängliga uppgraderingar
sudo dnf upgrade             # Uppgradera paket
sudo reboot                  # Starta om (om kärnan uppgraderats)
\`\`\`

**Alternativt med auto-yes:**

\`\`\`bash
sudo dnf upgrade -y          # Svarar ja automatiskt
\`\`\`

---

## 📦 Pakethantering - APT (Ubuntu/Debian)

### Söka Paket

\`\`\`bash
apt search python            # Bred sökning
apt search python | less     # Pipe till less för läsbarhet
\`\`\`

### Visa Paketinformation

\`\`\`bash
apt show adequate            # Visa info om specifikt paket
\`\`\`

### Installera Paket

\`\`\`bash
sudo apt install emacs-nox           # Installera paket
sudo apt install openssh-server      # Installera SSH-server
\`\`\`

### Ta Bort Paket

\`\`\`bash
sudo apt remove emacs-nox            # Ta bort paket
sudo apt autoremove                  # Städa bort oanvända paket
\`\`\`

---

## 🔐 SSH-nycklar

### Vad är SSH?

**SSH** = Secure Shell

- Öppna en shell på ett system utan fysisk tillgång
- Krypterad anslutning
- Används för att komma åt servrar på distans

### SSH-nyckelpar

**Komponenter:**

1. **Privat nyckel** (Private key)
   - Dela **ALDRIG** med någon
   - Bevis på din identitet
   - Sparas lokalt på din dator
   - Exempel: \`~/.ssh/id_ed25519\`

2. **Publik nyckel** (Public key)
   - Helt OK att dela
   - Används för att verifiera din privata nyckel
   - Sparas på servrar du vill komma åt
   - Exempel: \`~/.ssh/id_ed25519.pub\`

### Skapa SSH-nyckelpar

⚠️ **VIKTIGT**: Skapa nyckeln på **din dator**, INTE i VM!

**Kommando:**

\`\`\`bash
ssh-keygen
\`\`\`

**Steg för steg:**

1. **Kör kommando:**

   \`\`\`bash
   ssh-keygen
   \`\`\`

2. **Välj filnamn:** Tryck \`Enter\` för default

3. **Välj passphrase:** Rekommenderat för extra säkerhet

### Krypteringsalgoritmer

**ED25519** (rekommenderad, modern)

\`\`\`bash
ssh-keygen                    # Default på nya system
ssh-keygen -t ed25519        # Explicit
\`\`\`

**RSA** (äldre, längre nycklar)

\`\`\`bash
ssh-keygen -t rsa -b 4096    # Med längre nyckel
\`\`\`

### Hitta Din Nyckel

\`\`\`bash
~/.ssh/id_ed25519           # Privat nyckel
~/.ssh/id_ed25519.pub       # Publik nyckel

# Lista SSH-nycklar:
ls -la ~/.ssh/

# Visa publik nyckel:
cat ~/.ssh/id_ed25519.pub
\`\`\`

---

## 📋 Cheat Sheet

### Pakethantering Jämförelse

| Funktion | Ubuntu/Debian | Fedora |
|----------|--------------|--------|
| Uppdatera metadata | \`sudo apt update\` | \`sudo dnf check-upgrade\` |
| Uppgradera | \`sudo apt upgrade\` | \`sudo dnf upgrade\` |
| Sök paket | \`apt search\` | \`dnf search\` |
| Visa info | \`apt show\` | \`dnf info\` |
| Installera | \`sudo apt install\` | \`sudo dnf install\` |
| Ta bort | \`sudo apt remove\` | \`sudo dnf remove\` |
| Rensa bort | \`sudo apt autoremove\` | \`sudo dnf autoremove\` |

### SSH-nycklar

| Kommando | Beskrivning |
|----------|-------------|
| \`ssh-keygen\` | Skapa nyckelpar |
| \`ssh-keygen -t ed25519\` | Skapa med ED25519 |
| \`cat ~/.ssh/id_ed25519.pub\` | Visa publik nyckel |
| \`ls ~/.ssh/\` | Lista SSH-nycklar |
`;

const SSH_BRANDVAGG_CONTENT = `# SSH & Brandvägg - Hands-On Session

## Konfiguration & Säkerhetsåtgärder

---

## 📋 Innehållsförteckning

1. [Brandväggskonfiguration](#brandväggskonfiguration)
2. [SSH-nycklar för Inloggning](#ssh-nycklar-för-inloggning)
3. [SSH Hardening](#ssh-hardening)
4. [SSH Client Config](#ssh-client-config)
5. [Felsökning](#felsökning)

---

## 🔥 Brandväggskonfiguration

### Ubuntu - UFW (Uncomplicated Firewall)

**Kontrollera status:**

\`\`\`bash
sudo ufw status
# Output: Status: inactive (om inte aktiverad än)
\`\`\`

**Aktivera brandvägg (viktigt att göra EFTER att ha tillåtit SSH!):**

\`\`\`bash
# 1. Tillåt SSH FÖRST (annars låser du ut dig!)
sudo ufw allow 22

# 2. Aktivera brandväggen
sudo ufw enable

# 3. Verifiera
sudo ufw status
\`\`\`

⚠️ **KRITISKT**: Lägg ALLTID till SSH-regel (port 22) INNAN du aktiverar UFW!

---

### Fedora - firewalld

**Kontrollera status:**

\`\`\`bash
systemctl status firewalld.service
# Ska vara: active (running) och enabled
\`\`\`

**Visa brandväggskonfiguration:**

\`\`\`bash
sudo firewall-cmd --list-all
\`\`\`

---

## 🔑 SSH-nycklar för Inloggning

### Kopiera SSH-nyckel till VM

**Från din dator (Mac/Linux/WSL):**

\`\`\`bash
ssh-copy-id -i ~/.ssh/id_ed25519 username@ip-address
\`\`\`

### Manuell kopiering (Windows PowerShell)

\`\`\`bash
# Skapa .ssh-mapp om den inte finns
mkdir -p ~/.ssh

# Editera authorized_keys
vim ~/.ssh/authorized_keys

# Klistra in din publika nyckel
# Spara och stäng (ESC, :wq)
\`\`\`

---

## 🛡️ SSH Hardening

### Skapa Konfigurationsfil

\`\`\`bash
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
\`\`\`

**Filinnehåll:**

\`\`\`
# Ändra port som SSH lyssnar på
Port 6622

# Stäng av lösenordsinloggning
PasswordAuthentication no

# Stäng av root-login
PermitRootLogin no

# Tillåt endast specifika användare
AllowUsers gg
\`\`\`

### Uppdatera Brandvägg för Ny Port

**Ubuntu (UFW):**

\`\`\`bash
sudo ufw allow 6622
sudo ufw status
\`\`\`

**Fedora (firewalld):**

\`\`\`bash
sudo firewall-cmd --add-port=6622/tcp --permanent
sudo firewall-cmd --reload
\`\`\`

### Starta Om SSH-tjänsten

\`\`\`bash
# Ubuntu
sudo systemctl restart ssh.service

# Fedora
sudo systemctl restart sshd.service
\`\`\`

---

## 📝 SSH Client Config

### Förenkla SSH-anslutning

**Skapa/editera:**

\`\`\`bash
vim ~/.ssh/config
\`\`\`

**Exempel konfiguration:**

\`\`\`
Host ubuntu
    HostName 192.168.64.5
    User gg
    Port 6622
    IdentityFile ~/.ssh/id_ed25519

Host fedora
    HostName 192.168.64.6
    User gg
    Port 22
    IdentityFile ~/.ssh/id_ed25519
\`\`\`

**Efter detta:**

\`\`\`bash
ssh ubuntu  # Ansluter till Ubuntu VM
ssh fedora  # Ansluter till Fedora VM
\`\`\`

---

## 🔍 Felsökning

### Problem 1: Permission Denied

\`\`\`bash
# Kontrollera att nyckel finns
cat ~/.ssh/authorized_keys

# Fixa permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
\`\`\`

### Problem 2: Connection Refused

\`\`\`bash
# Kontrollera SSH-tjänsten
systemctl status ssh.service     # Ubuntu
systemctl status sshd.service    # Fedora

# Kolla brandvägg
sudo ufw status                  # Ubuntu
sudo firewall-cmd --list-all    # Fedora
\`\`\`

---

## 📋 Cheat Sheet

### Brandvägg - Snabbkommandon

| Uppgift | Ubuntu (UFW) | Fedora (firewalld) |
|---------|--------------|-------------------|
| Status | \`sudo ufw status\` | \`sudo firewall-cmd --list-all\` |
| Aktivera | \`sudo ufw enable\` | \`systemctl enable --now firewalld\` |
| Tillåt port | \`sudo ufw allow 22\` | \`sudo firewall-cmd --add-port=22/tcp --permanent\` |

### SSH Hardening - Template

\`\`\`bash
# /etc/ssh/sshd_config.d/01-ssh-hardening.conf
Port 6622
PasswordAuthentication no
PermitRootLogin no
AllowUsers username
\`\`\`
`;

const ANVANDARHANTERING_CONTENT = `# Linux Användarhantering - Praktisk Övning

## Hands-On Lab: Användare, Grupper & Behörigheter

---

## 📋 Översikt

**Typ:** Praktisk övning (individuellt eller i grupp)
**System:** Valfritt VM (Ubuntu eller Fedora)

---

## 🎯 Scenario

Du arbetar på IT-avdelningen på ett företag och har fått i uppdrag att sätta upp användare på en ny server.

---

## 📝 Kravspecifikation

### Uppgift 1: Skapa Användare

**Skapa användarkonton för följande fem personer:**

1. Alice
2. Bob
3. Charlie
4. David
5. Evert

**Krav:**
- Alla ska ha egna användarkonton
- Användarna ska kunna logga in på systemet

---

### Uppgift 2: Skapa Grupp och Medlemmar

**Skapa en grupp:**
- Gruppnamn: \`developers\`

**Lägg till följande användare i gruppen:**
- Alice
- Charlie
- Evert

**Resultat:**
- Bob och David är INTE med i developers-gruppen
- De är externa konsulter

---

### Uppgift 3: Skapa Projektmapp med Behörigheter

**Skapa mapp:**
- Path: \`/opt/developers\`

**Säkerställ:**
1. **Bara members av developers-gruppen kan komma åt mappen**
2. **Alla filer som skapas i mappen ägs automatiskt av gruppen \`developers\`**

**Tips:**
- Detta löses med special permissions (SGID)
- Sätts med \`chmod g+s\` eller \`chmod 2xxx\`

---

### Uppgift 4: Sätt Utgångsdatum för Konsulter

**Problem:**
- Bob och David är externa konsulter
- Deras uppdrag går ut vid årsskiftet

**Krav:**
- Deras konton ska sluta fungera från och med **1 januari 2026**

---

### Uppgift 5: Tvinga Lösenordsbyte

**Problem:**
- Någon har lånat Everts tangentbord
- De hittade en post-it med hans lösenord

**Krav:**
- Tvinga Evert att byta lösenord vid nästa login

---

## 🔍 Lösningsguide & Tips

### Användbara Kommandon

**Användarhantering:**

\`\`\`bash
useradd          # Skapa användare
usermod          # Modifiera användare
passwd           # Hantera lösenord
userdel          # Ta bort användare
\`\`\`

**Grupphantering:**

\`\`\`bash
groupadd         # Skapa grupp
groupmod         # Modifiera grupp
usermod -aG      # Lägg användare till grupp
gpasswd          # Gruppåtkomst
\`\`\`

**Behörigheter:**

\`\`\`bash
chmod            # Ändra permissions
chown            # Ändra ägare
chgrp            # Ändra grupp
\`\`\`

**Verifiering:**

\`\`\`bash
id username      # Visa användarinfo
groups username  # Visa grupptillhörighet
ls -l            # Visa permissions
getent passwd    # Lista användare
getent group     # Lista grupper
\`\`\`

### Special Permissions

**SGID (Set Group ID):**

\`\`\`bash
chmod g+s /opt/developers        # Sätt SGID
chmod 2770 /opt/developers       # SGID + full access för grupp
\`\`\`

---

## ✅ Verifieringschecklist

### Uppgift 1: Användare skapade?

\`\`\`bash
getent passwd alice
getent passwd bob
getent passwd charlie
getent passwd david
getent passwd evert
\`\`\`

### Uppgift 2: Grupp och medlemmar?

\`\`\`bash
getent group developers
# Output ska visa: developers:x:1001:alice,charlie,evert
\`\`\`

### Uppgift 3: Mapp och behörigheter?

\`\`\`bash
ls -ld /opt/developers
# Output ska visa:
# drwxrws--- ... developers /opt/developers
#      ^
#      SGID-bit (s istället för x)
\`\`\`

### Uppgift 4: Expiration date?

\`\`\`bash
sudo chage -l bob
# Account expires: Jan 01, 2026
\`\`\`

### Uppgift 5: Password expire?

\`\`\`bash
sudo chage -l evert
# Last password change: ... (ska visa att lösenord har expired)
\`\`\`

---

## 💡 Vanliga Fallgropar

### ❌ Fel 1: Glömmer sudo

\`\`\`bash
useradd alice           # ❌ Permission denied
sudo useradd alice      # ✅ Fungerar
\`\`\`

### ❌ Fel 2: Skriver över grupper

\`\`\`bash
usermod -G developers alice    # ❌ Tar bort från andra grupper
usermod -aG developers alice   # ✅ Lägger till i grupp
\`\`\`

### ❌ Fel 3: Glömmer SGID

\`\`\`bash
chmod 770 /opt/developers      # ❌ Filer ärver inte grupp
chmod 2770 /opt/developers     # ✅ SGID satt, filer ärver grupp
\`\`\`
`;

const SUBNETTING_CONTENT = `# Subnetting - Praktisk Övningsguide

## Lär dig beräkna subnet för hand

---

## 🎯 Vad är Subnetting?

**Subnetting** = Dela upp ett IP-nätverk i mindre subnät

**Vad vi ska kunna beräkna:**

- **Network Address** - Första adressen i subnätet
- **Broadcast Address** - Sista adressen i subnätet
- **First Host** - Första användbara IP-adressen
- **Last Host** - Sista användbara IP-adressen
- **Next Subnet** - Första adressen i nästa subnät

**Verktyg för övning:**

- 🌐 [subnet-ipv4.com](http://subnet-ipv4.com) - Genererar övningar
- ✋ **Papper och penna** - Lös för hand!

⚠️ **VIKTIGT**: Använd INTE subnet-kalkylatorer! Målet är att förstå logiken.

---

## 📚 Grundläggande Koncept

### IP-adress med CIDR-notation

**Format:** \`IP-adress/prefix\`

**Exempel:** \`192.168.1.0/24\`

### Prefix och Subnet Mask

| CIDR | Subnet Mask | Antal hosts |
|------|-------------|-------------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

### Binära Positioner

**Varje byte har 8 bitar:**

\`\`\`
Position:  128   64   32   16   8   4   2   1
Binär:    [0/1][0/1][0/1][0/1][0/1][0/1][0/1][0/1]
\`\`\`

---

## 🔢 Steg-för-Steg Metod

### Steg 1: Hitta Gränsen

\`/prefix\` anger var network-delen slutar.

### Steg 2: Konvertera till Binärt

**Metod: Subtrahera från vänster till höger**

\`\`\`
Är värdet ≥ 128? Ja → 1, dra av 128
Är resten ≥ 64?  Ja → 1, dra av 64
...fortsätt med 32, 16, 8, 4, 2, 1
\`\`\`

### Steg 3-4: Beräkna Adresser

**Network Address:** Network-delen + alla nollor
**Broadcast Address:** Network-delen + alla ettor
**First Host:** Network + 1
**Last Host:** Broadcast - 1
**Next Subnet:** Addera 1 på sista network-biten

---

## 📖 Exempel: 192.168.1.147/26

**Steg 1: Host-bitar = 32 - 26 = 6**
**Steg 2: Blockstorlek = 2^6 = 64**
**Steg 3: Subnät = 0, 64, 128, 192...**

147 faller i 128-intervallet (mellan 128 och 191)

**Resultat:**
- **Nätverksadress:** 192.168.1.128
- **Broadcast:** 192.168.1.191
- **Host-range:** 192.168.1.129-190
- **Antal hosts:** 62

---

## 💡 Snabbregler

| Prefix | Blockstorlek | Hosts |
|--------|-------------|-------|
| /24 | 256 | 254 |
| /25 | 128 | 126 |
| /26 | 64 | 62 |
| /27 | 32 | 30 |
| /28 | 16 | 14 |
| /29 | 8 | 6 |
| /30 | 4 | 2 |

### Formler

\`\`\`
Host-bitar = 32 - prefix
Blockstorlek = 2^(host-bitar)
Användbara hosts = Blockstorlek - 2
\`\`\`

---

## 🎯 Övning

Öva på [subnet-ipv4.com](http://subnet-ipv4.com) tills du kan lösa utan kalkylator!
`;

const DOCKER_CONTENT = `# Docker & Containers - Hands-On Guide

## Från installation till första container på 30 minuter

---

## 🎯 Varför Docker?

### Container vs VM

**Virtual Machine (VM):**
- Flera GB
- Eget OS och kernel
- Långsam start

**Container:**
- 25 KB - 80 MB
- Delar host kernel
- Snabb start (sekunder)

### Konkret Exempel

**Python Hello World:**
- VM: Flera GB
- Container: 25 KB

---

## 🔧 Installation - Ubuntu

\`\`\`bash
# 1. Rensa gamla versioner
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2. Update och dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl

# 3. Lägg till Docker's repository
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \\
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \\
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \\
  https://download.docker.com/linux/ubuntu \\
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \\
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Installera Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io \\
  docker-buildx-plugin docker-compose-plugin

# 5. Testa
sudo docker run hello-world
\`\`\`

---

## ⚡ Fix: Docker utan sudo

\`\`\`bash
# Lägg till dig i docker-gruppen
sudo usermod -aG docker $USER

# Logga ut och in igen
exit
# (SSH in igen)

# Testa utan sudo
docker run hello-world
\`\`\`

---

## 🚀 Grundläggande Kommandon

### docker run

\`\`\`bash
# Grundläggande
docker run hello-world

# Med specifik version
docker run python:3.14-alpine

# Interaktiv session
docker run -it python:3.14-alpine

# Interaktiv + auto-remove
docker run -it --rm python:3.14-alpine

# Bakgrund med namn
docker run -d --name my-app nginx
\`\`\`

### Vanliga Flaggor

| Flagga | Betydelse |
|--------|-----------|
| \`-i\` | Interactive |
| \`-t\` | TTY |
| \`-it\` | Interaktiv session |
| \`--rm\` | Ta bort vid exit |
| \`--name\` | Ge namn |
| \`-d\` | Detached (bakgrund) |
| \`-p\` | Port mapping |

### Hantera containers

\`\`\`bash
docker ps           # Visa körande
docker ps -a        # Visa ALLA
docker stop name    # Stoppa
docker start name   # Starta
docker rm name      # Ta bort

docker container prune  # Ta bort alla stoppade
\`\`\`

### Hantera images

\`\`\`bash
docker images       # Lista images
docker rmi image    # Ta bort image
docker image prune  # Ta bort oanvända
\`\`\`

---

## 💡 Praktiska Exempel

### Testa olika Python-versioner

\`\`\`bash
docker run -it --rm python:3.9-alpine
docker run -it --rm python:3.13-alpine
docker run -it --rm python:3.14-alpine
\`\`\`

### Container Lifecycle

\`\`\`bash
# 1. Starta med namn
docker run -it --name test-python python:3.14-alpine

# 2. Container stoppades vid exit
docker ps -a

# 3. Starta om
docker start -i test-python

# 4. Ta bort
docker rm test-python
\`\`\`

---

## 📋 Cheat Sheet

\`\`\`bash
# Kör container
docker run [OPTIONS] IMAGE[:TAG]

# Interaktiv
docker run -it IMAGE

# Interaktiv + auto-remove
docker run -it --rm IMAGE

# Med namn
docker run --name NAMN IMAGE

# Lista körande
docker ps

# Lista alla
docker ps -a

# Stoppa/starta
docker stop NAMN
docker start NAMN

# Ta bort
docker rm NAMN
docker container prune
\`\`\`

---

## 🎯 Viktiga Koncept

### Images vs Containers

**Image:** Mall/blueprint, läses från disk
**Container:** Körande instans av image

### Layers & Storage

Images delar **layers** - därför tar flera images lite extra plats.
`;

const STORAGE_KRYPTERING_CONTENT = `# Block Storage & Kryptering

## Hands-On Demonstration: Disk, Partition, Encryption, Filesystem

---

## 🏗️ Hierarkin - Övergripande

\`\`\`
┌─────────────────────────────────────┐
│   FYSISK DISK (Hårdvara)            │
│   /dev/sdb (5 GB)                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   PARTITION                          │
│   /dev/sdb1 (5 GB)                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   KRYPTERING (Valfritt)             │
│   /dev/mapper/cryptodisk            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   FILSYSTEM                          │
│   ext4                               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   MOUNT POINT                        │
│   /mnt                               │
└─────────────────────────────────────┘
\`\`\`

⚠️ **VIKTIGT**: Ordningen är kritisk och kan inte ändras!

---

## 💿 Lägga till en Ny Disk

### Verifiera Ny Disk

\`\`\`bash
lsblk
\`\`\`

**Output exempel:**

\`\`\`
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   24G  0 part /
sdb      8:16   0    5G  0 disk
\`\`\`

---

## 🔧 Partitionering med fdisk

\`\`\`bash
sudo fdisk /dev/sdb
\`\`\`

⚠️ **VARNING**: Dubbelkolla att du anger rätt disk!

### Steg-för-Steg

1. \`g\` - Skapa GPT partition table
2. \`n\` - New partition (alla defaults)
3. \`w\` - Write (spara ändringar)

---

## 🔐 Kryptering med LUKS

### Kryptera Partitionen

\`\`\`bash
sudo cryptsetup luksFormat /dev/sdb1
\`\`\`

⚠️ **VARNING**: Dubbelkolla partition! Fel partition = dataförlust!

- Skriv **YES** i VERSALER
- Lösenordet syns INTE när du skriver
- **Det finns INGET sätt att återställa lösenordet!**

### Öppna Krypterad Volym

\`\`\`bash
sudo cryptsetup open /dev/sdb1 cryptodisk
\`\`\`

---

## 📁 Skapa Filsystem

\`\`\`bash
sudo mkfs.ext4 /dev/mapper/cryptodisk
\`\`\`

---

## 🔗 Mount och Unmount

### Mount

\`\`\`bash
sudo mount /dev/mapper/cryptodisk /mnt
\`\`\`

### Unmount

\`\`\`bash
sudo umount /mnt
\`\`\`

### Stänga Krypterad Volym

\`\`\`bash
# 1. Unmount först
sudo umount /mnt

# 2. Stäng krypterad volym
sudo cryptsetup close cryptodisk
\`\`\`

---

## 📖 Kommandoreferens

### Disk Management

| Kommando | Beskrivning |
|----------|-------------|
| \`lsblk\` | Lista block devices |
| \`fdisk\` | Partitionera disk |

### Kryptering

| Kommando | Beskrivning |
|----------|-------------|
| \`cryptsetup luksFormat\` | Kryptera partition |
| \`cryptsetup open\` | Öppna volym |
| \`cryptsetup close\` | Stäng volym |

### Filsystem

| Kommando | Beskrivning |
|----------|-------------|
| \`mkfs.ext4\` | Skapa ext4-filsystem |
| \`mount\` | Montera filsystem |
| \`umount\` | Avmontera |
| \`df -h\` | Visa diskutrymme |

---

## 🎓 Komplett Process

\`\`\`bash
# 1. Partitionera
sudo fdisk /dev/sdb
# g, n, w

# 2. Kryptera
sudo cryptsetup luksFormat /dev/sdb1
# YES, lösenord

# 3. Öppna
sudo cryptsetup open /dev/sdb1 cryptodisk

# 4. Filsystem
sudo mkfs.ext4 /dev/mapper/cryptodisk

# 5. Mounta
sudo mount /dev/mapper/cryptodisk /mnt

# 6. Använd
cd /mnt
sudo touch secret-file

# 7. Stäng
sudo umount /mnt
sudo cryptsetup close cryptodisk
\`\`\`
`;

// ============================================
// HANDS-ON LAB MODULE - 7 TASKS
// ============================================

export const HANDSON_MODULE: HandsOnModule = {
    id: "hands-on-lab",
    name: "Hands-On Lab",
    slug: "hands-on-lab",
    description: "Praktiska labbar som tar dig från grunderna till avancerade Linux- och DevOps-koncept",
    difficulty: "intermediate",
    estimated_hours: 6,
    tasks: [
        // ============================================
        // TASK 1: ONBOARDING - FILSYSTEM & TEXTEDITORER
        // ============================================
        {
            id: "handson-1-onboarding",
            title: "Onboarding - Filsystem & Texteditorer",
            description: "Navigera i Linux filsystem, skapa och hantera filer, samt använda Nano och Vim",
            order_index: 0,
            estimated_minutes: 45,
            content: ONBOARDING_CONTENT,
        },
        // ============================================
        // TASK 2: PAKETHANTERING & SSH-NYCKLAR
        // ============================================
        {
            id: "handson-2-pakethantering",
            title: "Pakethantering & SSH-nycklar",
            description: "Hantera paket med APT och sätta upp SSH-nycklar för säker inloggning",
            order_index: 1,
            estimated_minutes: 40,
            content: PAKETHANTERING_SSH_CONTENT,
        },
        // ============================================
        // TASK 3: SSH & BRANDVÄGG
        // ============================================
        {
            id: "handson-3-ssh-brandvagg",
            title: "SSH & Brandvägg",
            description: "Konfigurera SSH-servern säkert och sätta upp UFW brandvägg",
            order_index: 2,
            estimated_minutes: 50,
            content: SSH_BRANDVAGG_CONTENT,
        },
        // ============================================
        // TASK 4: ANVÄNDARHANTERING
        // ============================================
        {
            id: "handson-4-anvandarhantering",
            title: "Användarhantering",
            description: "Skapa användare, grupper och hantera behörigheter",
            order_index: 3,
            estimated_minutes: 40,
            content: ANVANDARHANTERING_CONTENT,
        },
        // ============================================
        // TASK 5: SUBNETTING
        // ============================================
        {
            id: "handson-5-subnetting",
            title: "Subnetting",
            description: "Beräkna subnät, nätverksadresser och broadcast",
            order_index: 4,
            estimated_minutes: 45,
            content: SUBNETTING_CONTENT,
        },
        // ============================================
        // TASK 6: DOCKER & CONTAINERS
        // ============================================
        {
            id: "handson-6-docker",
            title: "Docker & Containers",
            description: "Installera Docker, köra containers, bygga images och använda Compose",
            order_index: 5,
            estimated_minutes: 60,
            content: DOCKER_CONTENT,
        },
        // ============================================
        // TASK 7: BLOCK STORAGE & KRYPTERING
        // ============================================
        {
            id: "handson-7-storage",
            title: "Block Storage & Kryptering",
            description: "Hantera diskar, LVM och sätta upp LUKS-kryptering",
            order_index: 6,
            estimated_minutes: 60,
            content: STORAGE_KRYPTERING_CONTENT,
        }
    ]
};

// ============================================
// HELPER FUNCTIONS
// ============================================

export function getHandsOnTaskById(id: string): HandsOnTask | undefined {
    // Check direct ID match
    const directMatch = HANDSON_MODULE.tasks.find(task => task.id === id);
    if (directMatch) return directMatch;

    // Check slug mapping
    const mappedId = SLUG_TO_ID[id];
    if (mappedId) {
        return HANDSON_MODULE.tasks.find(task => task.id === mappedId);
    }

    return undefined;
}

export function getAllHandsOnTasks(): HandsOnTask[] {
    return HANDSON_MODULE.tasks;
}

export function getHandsOnTotalEstimatedMinutes(): number {
    return HANDSON_MODULE.tasks.reduce((total, task) => total + task.estimated_minutes, 0);
}
