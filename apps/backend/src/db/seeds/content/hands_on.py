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
    "content": r"""# Linux Hands-On: Filsystem & Texteditorer

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

**`pwd`** - Print Working Directory

- Visar din nuvarande position i filsystemet
- Exempel: `/home/username`

**`cd`** - Change Directory

```bash
cd /home/username    # Absolut path (börjar med /)
cd Documents         # Relativ path (från nuvarande position)
cd ..               # Upp en nivå
cd ~                # Till hemmamapp (samma som cd utan argument)
cd                  # Till hemmamapp
cd -                # Till föregående directory
```

**`ls`** - List directory contents

```bash
ls                  # Lista filer i nuvarande mapp
ls /home           # Lista filer i specifik mapp
ls -l              # Long listing format (detaljerad info)
ls -a              # Visa dolda filer (börjar med .)
ls -t              # Sortera efter tid (nyast först)
ls -la             # Kombination av flaggor
ls -lta            # Alla flaggor tillsammans
```

### 🎯 Viktiga Paths

| Path | Beskrivning |
|------|-------------|
| `/` | Root (roten av filsystemet) |
| `/home` | Användares hemmamappar |
| `/etc` | Konfigurationsfiler |
| `/var` | Loggar och varierande data |
| `/bin` | Viktiga program/kommandon |
| `/tmp` | Temporära filer |
| `~` | Din hemmamapp (shortcut) |
| `.` | Nuvarande mapp |
| `..` | Mapp en nivå upp |

---

## 📁 Filhantering

### Skapa & Ta Bort

**`touch`** - Skapa tom fil

```bash
touch myfile.txt
touch file1 file2 file3    # Skapa flera filer
```

**`mkdir`** - Make Directory

```bash
mkdir myfolder
mkdir -p parent/child/grandchild    # Skapa hela strukturer
```

**`rm`** - Remove (radera filer)

```bash
rm myfile.txt
rm -r myfolder              # Recursive (hela mappar)
rm -f myfile.txt            # Force (ingen prompt)
rm -rf myfolder             # Kombinera flaggor
```

⚠️ **VARNING**: `rm` har ingen ångra-funktion och ingen papperskorg!

**`rmdir`** - Remove Directory (endast tomma mappar)

```bash
rmdir emptyfolder
```

### Kopiera & Flytta

**`cp`** - Copy

```bash
cp source.txt destination.txt
cp file.txt backup.txt
cp -r folder1 folder2        # Kopiera mappar
```

**`mv`** - Move (även för att byta namn)

```bash
mv oldname.txt newname.txt   # Byt namn
mv file.txt /home/user/      # Flytta fil
mv folder1 folder2           # Flytta/byt namn på mapp
```

⚠️ **OBS**: `mv` överskriver filer utan varning!

---

## 🔍 Läsa & Söka

### Visa Filinnehåll

**`cat`** - Concatenate (visa hela filen)

```bash
cat myfile.txt
cat file1.txt file2.txt      # Visa flera filer
```

### Pagers (sidvy)

**`less`** - Moderna pager (rekommenderad)

```bash
less myfile.txt
ps aux | less                # Pipe output till less
```

Navigering i `less`:

- `j` / `↓` - Ner en rad
- `k` / `↑` - Upp en rad
- `Space` / `Page Down` - Ner en sida
- `Page Up` - Upp en sida
- `/sökterm` - Sök
- `n` - Nästa sökmatch
- `N` - Föregående sökmatch
- `q` - Avsluta

**`more`** - Äldre pager (begränsad)

- Kan bara scrolla nedåt
- `Space` eller `Enter` för nästa sida

> 💡 **Tips**: "Less does more than more" - använd `less`!

### Söka i Filsystemet

**`find`** - Sök efter filer och mappar

```bash
find                         # Lista allt i nuvarande mapp
find /home                   # Lista allt under /home
find -type f                 # Bara filer
find -type d                 # Bara mappar
find -name "*bash*"          # Sök efter namn med "bash"
```

---

## 📚 Dokumentation

### Man Pages (Manual Pages)

**`man`** - Visa manualsidor

```bash
man ls                       # Manual för ls
man rm                       # Manual för rm
man man                      # Manual för man (viktigt!)
```

#### Man Page Sektioner

| Sektion | Innehåll |
|---------|----------|
| 1 | Kommandon och program |
| 2 | System calls (C-funktioner) |
| 3 | Bibliotek |
| 5 | Filformat |
| 8 | Systemadministration |

Navigering i man pages:

- Samma som i `less` (j/k, space, /, n, q)
- `h` - Hjälp
- `q` - Avsluta

### Info Pages

**`info`** - Alternativ dokumentation

```bash
info info                    # Lär dig info-systemet
info ls                      # Info om ls
```

- Mer strukturerad än man pages
- Länkar mellan sektioner
- `Tab` - Nästa länk
- `Enter` - Följ länk
- `q` - Avsluta

---

## ✏️ Texteditorer

### Vim

**Starta Vim**

```bash
vim myfile.txt
vimtutor                     # Interaktiv tutorial (VIKTIGT!)
```

#### Vim Basics (från vimtutor)

**Lägen:**

- Normal mode (default) - för navigation och kommandon
- Insert mode - för att skriva text
- Command mode - för kommandon som spara/avsluta

**Grundläggande kommandon:**

```vim
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
```

> 🎯 **Kom ihåg**: "How do I exit vim?" → `:q` eller `:q!`

**Vim Swap Files**

- Vim skapar `.swp` filer som backup
- Tas bort automatiskt när du avslutar korrekt
- Kvarstår om Vim kraschar

### Emacs (Frivilligt)

**Installation:**

```bash
# Ubuntu
sudo apt install emacs-nox

# Fedora
sudo dnf install emacs-nox
```

**Starta:**

```bash
emacs
```

Följ den inbyggda tutorialen (Emacs Tutorial) när du startar.

**Viktiga kortkommandon i Bash (Emacs-stil):**

- `Ctrl-A` - Början av rad
- `Ctrl-E` - Slutet av rad
- `Ctrl-K` - Radera resten av raden
- `Ctrl-L` - Rensa skärmen (samma som `clear`)

---

## 💡 Viktiga Koncept

### Absoluta vs Relativa Paths

**Absolut path** - Börjar med `/`

```bash
cd /home/username/Documents  # Fungerar var du än är
ls /etc
```

**Relativ path** - Börjar INTE med `/`

```bash
cd Documents                 # Från nuvarande position
ls ../other-folder          # Relativ till nuvarande
```

### Hidden Files

- Filer som börjar med `.` är "dolda"
- Visas inte med vanligt `ls`
- Använd `ls -a` för att se dem
- Exempel: `.bashrc`, `.viminfo`, `.bash_history`

### Tab Completion

- Tryck `Tab` för att autocomplete kommandon och filnamn
- Dubbel-`Tab` visar alla möjliga alternativ
- Sparar tid och minskar felstavningar!

```bash
cd Doc[TAB]      # Kompletterar till Documents/
ls myf[TAB]      # Kompletterar till myfile om unikt
```

### File Permissions & Ownership

När du kör `ls -l`:

```
drwxr-xr-x 2 username groupname 4096 Nov 13 10:30 Documents
-rw-r--r-- 1 username groupname   29 Nov 13 11:45 myfile.txt
```

- Första kolumnen: Permissions (d=directory, -=file)
- Tredje kolumnen: Ägare
- Femte kolumnen: Storlek (bytes)
- Sista kolumnerna: Datum och filnamn

### Farliga Kommandon ⚠️

```bash
rm -rf /                     # RADERA ALLT (kräver --no-preserve-root)
rm -rf /*                    # RADERA ALLT
rm -rf ~                     # RADERA HELA HEMMAMAP
mv file.txt existing.txt     # Överskriver utan varning
```

**Gyllene regel**: **Think before you type!**

---

## 📋 Cheat Sheet

### Snabbkommando

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `pwd` | Visa nuvarande mapp | `pwd` |
| `cd` | Byt mapp | `cd /home` |
| `ls` | Lista filer | `ls -la` |
| `touch` | Skapa tom fil | `touch file.txt` |
| `mkdir` | Skapa mapp | `mkdir folder` |
| `rm` | Ta bort | `rm file.txt` |
| `cp` | Kopiera | `cp a.txt b.txt` |
| `mv` | Flytta/byt namn | `mv old.txt new.txt` |
| `cat` | Visa fil | `cat file.txt` |
| `less` | Bläddra fil | `less file.txt` |
| `find` | Sök filer | `find -name "*.txt"` |
| `man` | Manual | `man ls` |
| `vim` | Öppna Vim | `vim file.txt` |

### Vim Snabbkommandon

| Kommando | Beskrivning |
|----------|-------------|
| `i` | Insert mode |
| `Esc` | Normal mode |
| `:w` | Spara |
| `:q` | Avsluta |
| `:wq` | Spara och avsluta |
| `:q!` | Avsluta utan spara |
| `h j k l` | Vänster, ner, upp, höger |
| `dd` | Radera rad |
| `u` | Ångra |
| `/text` | Sök efter "text" |

### ls Flaggor

| Flagga | Beskrivning |
|--------|-------------|
| `-l` | Long format (detaljer) |
| `-a` | Visa dolda filer (all) |
| `-t` | Sortera efter tid (time) |
| `-r` | Omvänd ordning (reverse) |
| `-h` | Human readable storlekar |
| `-R` | Recursive (visa undermappar) |

---

## 📖 Studietips för Tentan

### Måste Kunna

1. **Navigering**: `pwd`, `cd`, `ls` med flaggor
2. **Filhantering**: `touch`, `mkdir`, `rm`, `cp`, `mv`
3. **Läsa filer**: `cat`, `less`
4. **Man pages**: Hitta och läsa dokumentation
5. **Vim basics**: Öppna, editera, spara, avsluta

### Viktigt att Förstå

- Skillnad mellan absoluta och relativa paths
- Hur Tab completion fungerar
- Varför man ska tänka innan man kör `rm`
- Hur man navigerar i man pages och less
- Skillnad mellan `.` (nuvarande) och `..` (upp en nivå)

### Praktisk Övning

1. Gör **vimtutor** (minst en gång!)
2. Läs man pages för alla kommandon ovan
3. Öva navigering i filsystemet
4. Skapa, editera och ta bort filer
5. Använd Vim för anteckningar dagligen

### Vanliga Fel att Undvika

- ❌ Glömma att man är i Insert mode i Vim
- ❌ Använda `rm -rf` utan att dubbelkolla
- ❌ Förväxla absoluta och relativa paths
- ❌ Inte läsa man pages när osäker
- ❌ Försöka scrolla i raw TTY (använd `less` istället)

---

## 🎓 Sammanfattning

### Tre Viktiga Lärdomar

1. **RTFM** - Read The Fine Manual
   - Använd `man` och `info` för dokumentation
   - Sök med `/` i man pages

2. **Think Before You Type**
   - Ingen ångra-funktion för `rm`
   - Dubbelkolla innan du kör destruktiva kommandon

3. **Practice Makes Perfect**
   - Använd Linux dagligen
   - Anteckna i Vim
   - Läs man pages regelbundet

---

## 📚 Referenser

- `man man` - Manual för manual pages
- `man ls`, `man cd`, `man rm`, etc. - Specifik dokumentation
- `vimtutor` - Interaktiv Vim tutorial
- `info info` - Info page dokumentation

---
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
    "content": r"""# Linux Pakethantering & SSH-nycklar

## Sammanfattning för Tenta

---

## 📋 Innehållsförteckning

1. [Systemuppgradering](#systemuppgradering)
2. [Pakethantering - APT (Ubuntu/Debian)](#pakethantering---apt-ubuntudebian)
3. [Pakethantering - DNF (Fedora)](#pakethantering---dnf-fedora)
4. [Lågnivå Pakethantering](#lågnivå-pakethantering)
5. [SSH-nycklar](#ssh-nycklar)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Man Pages att Läsa](#man-pages-att-läsa)
8. [Cheat Sheet](#cheat-sheet)

---

## 🔄 Systemuppgradering

### Ubuntu/Debian (APT)

**Komplett uppgraderingsprocess:**

```bash
sudo apt update              # Uppdatera paketdatabasen
sudo apt upgrade             # Uppgradera installerade paket
sudo reboot                  # Starta om (om kärnan uppgraderats)
```

**Steg för steg:**

1. **`sudo apt update`**
   - Uppdaterar metadata om tillgängliga paket
   - Kontaktar HTTP-tjänster (repositories)
   - Kräver sudo (administratörsrättigheter)
   - Frågar efter lösenord (visas inte när du skriver)

2. **Kontrollera uppgraderingsbara paket:**

   ```bash
   apt list --upgradable       # Ingen sudo behövs (bara listar)
   ```

3. **`sudo apt upgrade`**
   - Applicerar uppgraderingar
   - Visar översikt innan installation
   - Frågar om bekräftelse (Y/n) - `Y` är default
   - Laddar ner och installerar paket

**Efter uppgradering:**

- Om kärnan uppgraderas: **starta om systemet**
- Vissa services startas om automatiskt
- Andra får "deferred" - startas inte om automatiskt

### Fedora (DNF)

**Komplett uppgraderingsprocess:**

```bash
sudo dnf check-upgrade       # Kolla tillgängliga uppgraderingar
sudo dnf upgrade             # Uppgradera paket
sudo reboot                  # Starta om (om kärnan uppgraderats)
```

**Alternativt med auto-yes:**

```bash
sudo dnf upgrade -y          # Svarar ja automatiskt
```

**Skillnader från APT:**

- `check-upgrade` istället för `update` + `list --upgradable`
- Default svar är `N` (nej) - måste skriva `y` explicit
- Flaggan `-y` automatiserar ja-svar

### Verifiera Uppgradering

**Exit codes:**

```bash
echo $?                      # Visa exit code från senaste kommando
```

- `0` = Allt gick bra ✅
- Annat än `0` = Något gick fel ❌

> 💡 **Tips**: `$?` refererar **alltid** till senaste kommandot

### 🔄 Kernel (Kärnan)

**Viktigt att veta:**

- Kärnan laddas vid boot och körs från minnet
- Även efter uppgradering använder systemet gamla kärnan tills omstart
- Vid boot: välj senaste kärnan (default)
- Fedora sparar 3 senaste kärnor som backup

**Bootmeny efter kernel-uppgradering:**

```
1. Fedora Linux (6.17.7)     ← Senaste (välj denna)
2. Fedora Linux (6.17.1)     ← Föregående
3. Fedora Linux (6.16.x)     ← Äldre backup
```

---

## 📦 Pakethantering - APT (Ubuntu/Debian)

### Söka Paket

**`apt search`** - Sök efter paket

```bash
apt search python            # Bred sökning
apt search python | less     # Pipe till less för läsbarhet
apt search emacs             # Sök efter emacs-relaterat
```

**Sökningen matchar:**

- Paketnamn
- Kort beskrivning
- Lång beskrivning (även om inte synlig i listan)

### Visa Paketinformation

**`apt show`** - Detaljerad information om paket

```bash
apt show adequate            # Visa info om specifikt paket
```

**Visar:**

- Version
- Maintainer (ansvarig)
- Bug report URL
- Dependencies (beroenden)
- Recommends (rekommenderade paket)
- Homepage/Repository
- Storlek
- Beskrivning (kort + lång)

### Installera Paket

**`apt install`** - Installera paket

```bash
sudo apt install emacs-nox           # Installera paket
sudo apt install openssh-server      # Installera SSH-server
```

**Installation av dependencies:**

- APT installerar automatiskt alla beroenden
- Beroenden markeras som "automatically installed"

### Ta Bort Paket

**`apt remove`** - Ta bort paket

```bash
sudo apt remove emacs-nox            # Ta bort paket
```

**Viktigt:**

- Dependencies tas INTE bort automatiskt
- Visar meddelande: "packages were automatically installed and are no longer required"

**`apt autoremove`** - Ta bort oanvända dependencies

```bash
sudo apt autoremove                  # Städa bort oanvända paket
```

**Hur det fungerar:**

- APT håller koll på dependencies som en graf
- Om inga paket längre beror på ett dependency → oanvänd
- `autoremove` tar bort alla oanvända dependencies
- Paket installerade manuellt tas INTE bort

### Kombinera Kommandon

**Semicolon (;)** - Separera kommandon

```bash
sudo apt update; sudo apt upgrade        # Kör båda efter varandra
sudo apt update; sudo apt upgrade -y     # Med auto-yes
```

---

## 🎯 Pakethantering - DNF (Fedora)

### Söka Paket

**`dnf search`** - Sök efter paket

```bash
dnf search python            # Sök paket
dnf search python | less     # Med less för läsbarhet
```

⚠️ **Varning**: Kör inte `dnf search` samtidigt som `dnf upgrade` körs - kan ge "file fail" error

### Visa Paketinformation

**`dnf info`** - Detaljerad information

```bash
dnf info python3
```

**Visar:**

- Name
- Version (ex: 3.14)
- Release (ex: 2) - paketversion för Fedora
- Size
- Source (RPM-fil)
- Repository
- Summary
- Description
- Project URL

### Installera Paket

**`dnf install`** - Installera paket

```bash
sudo dnf install emacs-nox
sudo dnf install emacs-nox -y         # Med auto-yes
```

### Ta Bort Paket

**`dnf remove`** - Ta bort paket

```bash
sudo dnf remove emacs-nox
```

**`dnf autoremove`** - Ta bort oanvända dependencies

```bash
sudo dnf autoremove
```

### Räkna Paket

**Kombinera med verktyg:**

```bash
dnf check-upgrade | wc -l             # Räkna rader
```

- `wc` = word count
- `-l` = räkna linjer/rader
- Exempel output: `123` paket att uppgradera

---

## 🔧 Lågnivå Pakethantering

### DPKG (Debian/Ubuntu)

**DPKG** = Debian Package Manager (lågnivå)

**Vanliga kommandon:**

```bash
dpkg -i package.deb          # Install - installera .deb-fil
dpkg -r package              # Remove - ta bort paket
dpkg -l                      # List - lista installerade paket
dpkg -l | grep pattern       # Sök bland installerade
```

**Flaggor i detalj:**

- `-i` eller `--install` - Installera paket från .deb-fil
- `-r` eller `--remove` - Ta bort paket
- `-l` - Lista paket som matchar pattern

**Skillnad APT vs DPKG:**

| Funktion | APT | DPKG |
|----------|-----|------|
| Hantera dependencies | ✅ Ja | ❌ Nej |
| Ladda ner paket | ✅ Ja | ❌ Nej |
| Installera lokala .deb | ✅ Ja | ✅ Ja |
| Nivå | Hög | Låg |

### RPM (Red Hat/Fedora)

**RPM** = Red Hat Package Manager (lågnivå)

**Vanliga kommandon:**

```bash
rpm -ivh package.rpm         # Install med verbose och progress
rpm -e package               # Erase - ta bort paket
rpm -qa                      # Query all - lista alla paket
```

**Flaggor i detalj:**

- `-i` - Install
- `-v` - Verbose (mer output)
- `-h` - Hash (visa progressbar med 50 hash-markeringar)
- `-e` - Erase (ta bort)
- `-q` - Query (fråga/söka)
- `-a` - All (alla installerade paket)

**Exempel kombinationer:**

```bash
rpm -ivh package.rpm         # Installera med feedback
rpm -qa | grep python        # Lista alla Python-paket
```

**Skillnad DNF vs RPM:**

| Funktion | DNF | RPM |
|----------|-----|-----|
| Hantera dependencies | ✅ Ja | ❌ Nej |
| Ladda ner paket | ✅ Ja | ❌ Nej |
| Installera lokala .rpm | ✅ Ja | ✅ Ja |
| Nivå | Hög | Låg |

**Man Page Sektion för RPM:**

- RPM finns i **Section 8** - System Administration Commands
- Section 8 innehåller administrativa verktyg (usually only for root)

---

## 🔐 SSH-nycklar

### Vad är SSH?

**SSH** = Secure Shell

- Öppna en shell på ett system utan fysisk tillgång
- Krypterad anslutning
- Används för att komma åt servrar på distans

**Användningsområden:**

- Servrar i serverhall
- Cloud-resurser (VM i molnet)
- Remote development
- Deployment

### SSH-nyckelpar

**Komponenter:**

1. **Privat nyckel** (Private key)
   - Dela **ALDRIG** med någon
   - Bevis på din identitet
   - Sparas lokalt på din dator
   - Exempel: `~/.ssh/id_ed25519`

2. **Publik nyckel** (Public key)
   - Helt OK att dela
   - Används för att verifiera din privata nyckel
   - Sparas på servrar du vill komma åt
   - Exempel: `~/.ssh/id_ed25519.pub`

### Skapa SSH-nyckelpar

⚠️ **VIKTIGT**: Skapa nyckeln på **din dator**, INTE i VM!

**Kommando:**

```bash
ssh-keygen
```

**Steg för steg:**

1. **Kör kommando:**

   ```bash
   ssh-keygen
   ```

2. **Välj filnamn:**

   ```
   Enter file in which to save the key (/home/user/.ssh/id_ed25519):
   ```

   - Tryck `Enter` för default (rekommenderat)
   - Eller ange egen path

3. **Välj passphrase (lösenord):**

   ```
   Enter passphrase (empty for no passphrase):
   ```

   - **Rekommenderat**: Välj ett lösenord
   - Extra säkerhetslager
   - Skyddar om någon får tillgång till filen

4. **Upprepa passphrase:**

   ```
   Enter same passphrase again:
   ```

5. **Klar!**

   ```
   Your identification has been saved in /home/user/.ssh/id_ed25519
   Your public key has been saved in /home/user/.ssh/id_ed25519.pub
   ```

### Krypteringsalgoritmer

**ED25519** (rekommenderad, modern)

```bash
ssh-keygen                    # Default på nya system
ssh-keygen -t ed25519        # Explicit
```

**RSA** (äldre, längre nycklar)

```bash
ssh-keygen -t rsa
ssh-keygen -t rsa -b 4096    # Med längre nyckel
```

**Elliptic Curve (EC)**

```bash
ssh-keygen -t ecdsa
```

> 💡 **Rekommendation**: Använd ED25519 eller RSA 4096-bit

### Hitta Din Nyckel

**Default location:**

```bash
~/.ssh/id_ed25519           # Privat nyckel
~/.ssh/id_ed25519.pub       # Publik nyckel
```

**Lista SSH-nycklar:**

```bash
ls -la ~/.ssh/
```

**Visa publik nyckel:**

```bash
cat ~/.ssh/id_ed25519.pub
```

**Exempel output:**

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILongstringofcharacters... user@hostname
```

### SSH-nyckel Format

**Publik nyckel består av:**

1. Algoritm (ex: `ssh-ed25519` eller `ssh-rsa`)
2. Nyckeldata (lång sträng av tecken)
3. Kommentar (vanligtvis `user@hostname`)

**Privat nyckel:**

```
-----BEGIN OPENSSH PRIVATE KEY-----
...massa krypterad data...
-----END OPENSSH PRIVATE KEY-----
```

⚠️ **Dela ALDRIG din privata nyckel!

### Flera Nycklar

**Du kan ha flera nyckelpar:**

```bash
~/.ssh/
├── id_ed25519          # Första paret (privat)
├── id_ed25519.pub      # Första paret (publik)
├── id_rsa              # Andra paret (privat)
├── id_rsa.pub          # Andra paret (publik)
└── known_hosts         # Servrar du anslutit till
```

**Användningsfall:**

- En nyckel för jobbet
- En nyckel för privat
- En nyckel per projekt

### Passphrase - Varför?

**Utan passphrase:**

- ❌ Om någon får filen → full tillgång
- ❌ Stulen laptop = komprometterade servrar

**Med passphrase:**

- ✅ Extra säkerhetslager
- ✅ Även om filen stjäls → behöver lösenord
- ✅ Tid att revokera nyckel om laptop stjäls

### SSH i Windows

**Metod 1: PowerShell/CMD**

```powershell
ssh-keygen                    # Samma kommando
```

**Hitta nyckel:**

```powershell
dir C:\Users\username\.ssh\
type C:\Users\username\.ssh\id_ed25519.pub
```

**Metod 2: WSL (Windows Subsystem for Linux)**

```bash
ssh-keygen                    # I WSL terminal
cat ~/.ssh/id_ed25519.pub
```

### SSH i Mac/Linux

**Skapa nyckel:**

```bash
ssh-keygen
```

**Visa nyckel:**

```bash
cat ~/.ssh/id_ed25519.pub
```

---

## 💡 Viktiga Koncept

### Pakethanterare - Hierarki

**Hög-nivå (APT/DNF):**

- Hanterar dependencies automatiskt
- Laddar ner paket från repositories
- Enklare att använda
- Rekommenderad för dagligt bruk

**Låg-nivå (DPKG/RPM):**

- Hanterar enskilda paket
- Hanterar INTE dependencies
- Kräver manuell hantering
- För avancerade användare

### Dependencies (Beroenden)

**Vad är dependencies?**

- Bibliotek eller paket som ett program behöver
- Installeras automatiskt av APT/DNF
- Markeras som "automatically installed"

**Hur spårning fungerar:**

```
Emacs (installerad manuellt)
  ├─→ Bibliotek A (dependency)
  ├─→ Bibliotek B (dependency)
  └─→ Bibliotek C (dependency)
```

**Efter `apt remove emacs`:**

- Emacs tas bort
- Dependencies finns kvar (used by other packages?)
- Om inga andra paket beror på dem → oanvända
- `apt autoremove` städar bort oanvända

### Repository (Repo)

**Vad är en repository?**

- Server med paket
- APT/DNF laddar ner paket härifrån
- Metadata om tillgängliga paket

**Default repositories:**

- Ubuntu: Ubuntu's officiella repos
- Fedora: Fedora's officiella repos

**Tredjepartsrepos:**

- Kan läggas till manuellt
- Ger tillgång till fler paket
- Används mindre numera

### Konfigurationsfiler

**APT:**

- `/etc/apt/apt.conf` - huvudkonfiguration (ofta tom)
- `/etc/apt/apt.conf.d/` - konfiguration i delade filer

**DNF:**

- `/etc/dnf/dnf.conf` - huvudkonfiguration

**Vad kan konfigureras?**

- Default beteende
- Vilka repos som används
- Timeout-värden
- Cache-inställningar
- Mycket mer...

### Exit Codes

**Koncept:**

- Varje kommando returnerar en exit code
- `0` = Success
- Annat än `0` = Error

**Kolla exit code:**

```bash
command_here
echo $?                      # Visa exit code
```

**Exempel:**

```bash
sudo apt update
echo $?                      # Output: 0 (success)

sudo apt install nonexistent
echo $?                      # Output: 100 (error)
```

---

## 📚 Man Pages att Läsa

### 🔴 Obligatoriska (Fedora)

```bash
man dnf                      # Huvudkommando
man dnf.conf                 # Konfiguration (Section 5)
man rpm                      # Lågnivå pakethantering (Section 8)
```

**Kolla även:**

- See Also-sektionen i man pages
- Olika subkommandon har egna man pages:

  ```bash
  man dnf-upgrade
  man dnf-check-upgrade
  ```

**Hitta RPM man page:**

```bash
man -k rpm                   # Sök efter rpm i man pages
apropos rpm                  # Samma som man -k
```

Output visar: `rpm(8)` - Section 8 = System Administration

### 🔵 Obligatoriska (Ubuntu)

```bash
man apt                      # Huvudkommando
man apt.conf                 # Konfiguration (Section 5)
man dpkg                     # Lågnivå pakethantering
```

**Kolla även:**

- See Also-sektionen
- Relaterade kommandon

### Man Sections - Påminnelse

| Section | Innehåll | Exempel |
|---------|----------|---------|
| 1 | Kommandon och program | ls, cd, apt, dnf |
| 2 | System calls | fork, exec |
| 3 | Bibliotek | printf (C) |
| 5 | **Filformat** | apt.conf, dnf.conf |
| 8 | **Systemadministration** | rpm |

### Söka i Man Pages

**`man -k` / `apropos`** - Sök genom alla man pages

```bash
man -k rpm                   # Hitta alla man pages om rpm
apropos printf               # Samma som man -k
```

**I man page:**

```bash
/search_term                 # Sök framåt
n                           # Nästa match
N                           # Föregående match
```

---

## 📋 Cheat Sheet

### Systemuppgradering

| System | Kolla Uppdateringar | Uppgradera | Auto-Yes |
|--------|-------------------|------------|----------|
| Ubuntu | `sudo apt update && apt list --upgradable` | `sudo apt upgrade` | `sudo apt upgrade -y` |
| Fedora | `sudo dnf check-upgrade` | `sudo dnf upgrade` | `sudo dnf upgrade -y` |

### Pakethantering Jämförelse

| Funktion | Ubuntu/Debian | Fedora |
|----------|--------------|--------|
| Uppdatera metadata | `sudo apt update` | `sudo dnf check-upgrade` |
| Uppgradera | `sudo apt upgrade` | `sudo dnf upgrade` |
| Sök paket | `apt search` | `dnf search` |
| Visa info | `apt show` | `dnf info` |
| Installera | `sudo apt install` | `sudo dnf install` |
| Ta bort | `sudo apt remove` | `sudo dnf remove` |
| Rensa bort | `sudo apt autoremove` | `sudo dnf autoremove` |

### Lågnivå Pakethantering

| Funktion | Debian | Red Hat |
|----------|--------|---------|
| Installera | `dpkg -i file.deb` | `rpm -ivh file.rpm` |
| Ta bort | `dpkg -r package` | `rpm -e package` |
| Lista alla | `dpkg -l` | `rpm -qa` |

### SSH-nycklar

| Kommando | Beskrivning |
|----------|-------------|
| `ssh-keygen` | Skapa nyckelpar |
| `ssh-keygen -t ed25519` | Skapa med ED25519 |
| `ssh-keygen -t rsa -b 4096` | Skapa RSA 4096-bit |
| `cat ~/.ssh/id_ed25519.pub` | Visa publik nyckel |
| `ls ~/.ssh/` | Lista SSH-nycklar |

### Viktiga Paths

| System | SSH-nycklar | APT config | DNF config |
|--------|------------|------------|-----------|
| Standard | `~/.ssh/` | `/etc/apt/apt.conf.d/` | `/etc/dnf/dnf.conf` |

### Användbara Kommandon

```bash
echo $?                      # Exit code från senaste kommando
command1; command2           # Kör kommandon sekventiellt
command | wc -l              # Räkna rader i output
command | grep pattern       # Filtrera output
command | less               # Visa output i pager
```

---

## 🎯 Studietips för Tentan

### Måste Kunna

1. **Uppgradera system** (både Ubuntu och Fedora)
2. **Skillnad mellan `apt update` och `apt upgrade`**
3. **Sök, visa, installera, ta bort paket**
4. **`autoremove` - vad gör det och varför?**
5. **Skapa SSH-nyckelpar**
6. **Skillnad privat vs publik nyckel**
7. **Varför använda passphrase?**

### Viktigt att Förstå

- **Dependencies** - vad är det och hur fungerar det?
- **Skillnad hög-nivå vs låg-nivå** pakethanterare
- **När ska man starta om?** (efter kernel-uppgradering)
- **Exit codes** - vad betyder 0 vs annat värde?
- **Repository** - vad är det?
- **Man page sections** - speciellt 5 och 8

### Praktisk Övning

1. **Uppgradera dina VM regelbundet** (veckovis)

   ```bash
   # Ubuntu
   sudo apt update && sudo apt upgrade -y

   # Fedora
   sudo dnf upgrade -y
   ```

2. **Öva på att söka och installera paket**

   ```bash
   apt search python | less
   apt show python3
   sudo apt install package
   ```

3. **Läs man pages** för alla kommandon

   ```bash
   man apt
   man dnf
   man dpkg
   man rpm
   ```

4. **Skapa SSH-nyckel** om du inte har

   ```bash
   ssh-keygen -t ed25519
   cat ~/.ssh/id_ed25519.pub
   ```

### Vanliga Fel att Undvika

- ❌ Glömma `sudo apt update` innan `apt upgrade`
- ❌ Glömma att dependencies finns kvar efter `remove`
- ❌ Dela privat SSH-nyckel
- ❌ Skapa SSH-nyckel i VM istället för på datorn
- ❌ Glömma passphrase på SSH-nyckel
- ❌ Inte starta om efter kernel-uppgradering

### Felsökning Tips

**Problem: "Cannot open lock file, permission denied"**

- ✅ Lösning: Lägg till `sudo` före kommandot

**Problem: DNF/APT hänger sig**

- ✅ Lösning: Vänta, kör inte flera pakethanterare samtidigt

**Problem: Kan inte hitta paket**

- ✅ Lösning: Kör `sudo apt update` / `sudo dnf check-upgrade` först

**Problem: Hittar inte SSH-nyckel**

- ✅ Lösning: Kolla i `~/.ssh/` (Windows: `C:\Users\username\.ssh\`)

---

## 🔍 Kommandoexempel med Förklaring

### Exempel 1: Komplett Uppgradering (Ubuntu)

```bash
# 1. Uppdatera paketdatabasen
sudo apt update
# Output: "26 packages can be upgraded"

# 2. Lista vad som kan uppgraderas (valfritt)
apt list --upgradable
# Visar lista med paket

# 3. Uppgradera
sudo apt upgrade
# Frågar om bekräftelse: "Do you want to continue? [Y/n]"
# Tryck Enter eller skriv y

# 4. Verifiera att allt gick bra
echo $?
# Output: 0 (success)
```

### Exempel 2: Installera och Ta Bort (Fedora)

```bash
# Sök efter paket
dnf search emacs | less

# Visa info om paket
dnf info emacs-nox

# Installera
sudo dnf install emacs-nox
# Output: "Is this ok [y/N]:" - måste skriva y

# Verifiera att det är installerat
dnf list installed | grep emacs

# Ta bort
sudo dnf remove emacs-nox

# Städa dependencies
sudo dnf autoremove
```

### Exempel 3: SSH-nyckel

```bash
# Skapa nyckel
ssh-keygen
# Tryck Enter för default path
# Ange passphrase (rekommenderat)

# Lista nycklar
ls -la ~/.ssh/
# Output visar id_ed25519 och id_ed25519.pub

# Visa publik nyckel
cat ~/.ssh/id_ed25519.pub
# Kopiera hela output och dela med administratör

# Windows (CMD)
type C:\Users\username\.ssh\id_ed25519.pub
```

---

## 📝 Sammanfattning

### Tre Viktiga Lärdomar

1. **Håll systemet uppdaterat**
   - Kör `apt update && apt upgrade` (Ubuntu) eller `dnf upgrade` (Fedora) regelbundet
   - Starta om efter kernel-uppgraderingar
   - Använd `-y` för att automatisera

2. **Förstå pakethantering**
   - Hög-nivå (APT/DNF) för daglig användning
   - Låg-nivå (DPKG/RPM) för speciella fall
   - `autoremove` för att städa dependencies
   - Läs man pages för djupare förståelse

3. **SSH-nycklar är viktiga**
   - Skapa på **din dator**, inte i VM
   - Använd **passphrase** för säkerhet
   - Dela **endast publik** nyckel
   - En nyckel för hela utbildningen

### Rutiner att Etablera

**Veckovis:**

```bash
# Ubuntu
sudo apt update && sudo apt upgrade -y && sudo reboot

# Fedora
sudo dnf upgrade -y && sudo reboot
```

**Vid behov:**

- Sök paket innan installation
- Läs man pages för nya kommandon
- Verifiera exit codes (`echo $?`)
- Städa med `autoremove` efter avinstallationer

### Nästa Steg

1. ✅ Skapa SSH-nyckel (om inte gjort)
2. ✅ Dela publik nyckel med lärare
3. ✅ Läs man pages: `apt`, `dnf`, `dpkg`, `rpm`, `apt.conf`, `dnf.conf`
4. ✅ Uppgradera båda VM:ar
5. ✅ Läs Kapitel 3 i kursboken
6. ✅ Använd handledning vid frågor

---

## 🆘 Resurser

**Man Pages:**

```bash
man apt              # APT huvudkommando
man dnf              # DNF huvudkommando
man dpkg             # DPKG för .deb-filer
man rpm              # RPM för .rpm-filer
man apt.conf         # APT konfiguration
man dnf.conf         # DNF konfiguration
man ssh-keygen       # SSH-nyckelgenerering
```

**Söka hjälp:**

```bash
man -k keyword       # Sök bland alla man pages
apropos keyword      # Samma som man -k
command --help       # Kort hjälptext
```

**Exit Codes:**

```bash
echo $?              # Senaste kommandots resultat
```

---

**Lycka till på tentan! 🚀**

*Skapad utifrån föreläsning om Linux Pakethantering & SSH-nycklar*
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
    "content": r"""# SSH & Brandvägg - Hands-On Session

## Konfiguration & Säkerhetsåtgärder

---

## 📋 Innehållsförteckning

1. [Brandväggskonfiguration](#brandväggskonfiguration)
2. [SSH-nycklar för Inloggning](#ssh-nycklar-för-inloggning)
3. [SSH Hardening](#ssh-hardening)
4. [SSH Client Config](#ssh-client-config)
5. [Felsökning](#felsökning)
6. [Viktiga Koncept](#viktiga-koncept)
7. [Cheat Sheet](#cheat-sheet)

---

## 🔥 Brandväggskonfiguration

### Ubuntu - UFW (Uncomplicated Firewall)

**Kontrollera status:**

```bash
sudo ufw status
# Output: Status: inactive (om inte aktiverad än)
```

**Aktivera brandvägg (viktigt att göra EFTER att ha tillåtit SSH!):**

```bash
# 1. Tillåt SSH FÖRST (annars låser du ut dig!)
sudo ufw allow 22

# 2. Aktivera brandväggen
sudo ufw enable
# Varning: "Command may disrupt existing SSH connection"
# Svara: yes

# 3. Verifiera
sudo ufw status
```

**Output efter aktivering:**

```
Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere
22 (v6)                    ALLOW       Anywhere (v6)
```

**Standardbeteende:**

- **Incoming:** Deny (default) - Blockera allt inkommande
- **Outgoing:** Allow (default) - Tillåt allt utgående

⚠️ **KRITISKT**: Lägg ALLTID till SSH-regel (port 22) INNAN du aktiverar UFW!

---

### Fedora - firewalld

**Kontrollera status:**

```bash
systemctl status firewalld.service
# Ska vara: active (running) och enabled
```

**Om den inte körs:**

```bash
sudo systemctl enable --now firewalld.service
```

**Visa brandväggskonfiguration:**

```bash
sudo firewall-cmd --list-all
```

**Output exempel:**

```
public (active)
  target: default
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  ...
```

**Vad betyder detta?**

- `cockpit` - Webbinterface för serveradministration (port 9090)
- `dhcpv6-client` - DHCP för IPv6
- `ssh` - SSH-server (port 22)

**Bra att veta:**

- SSH är redan tillåtet by default i Fedora
- Brandväggen är redan aktiv
- Ingen konfiguration behövdes för grundläggande SSH-åtkomst

---

## 🔑 SSH-nycklar för Inloggning

### Kopiera SSH-nyckel till VM

**Från din dator (Mac/Linux/WSL):**

```bash
ssh-copy-id -i ~/.ssh/id_ed25519 username@ip-address
```

**Exempel:**

```bash
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.5
```

**Vad gör kommandot?**

1. Läser din **privata** nyckel (för att få rätt publik nyckel)
2. Kopierar **publika** nyckeln till servern
3. Lägger till den i `~/.ssh/authorized_keys` på servern

### Manuell kopiering (Windows PowerShell)

**Om `ssh-copy-id` inte finns (Windows):**

**Steg 1: Visa din publika nyckel**

```powershell
type C:\Users\username\.ssh\id_ed25519.pub
```

**Steg 2: Kopiera hela output**

**Steg 3: På servern (Ubuntu/Fedora)**

```bash
# Skapa .ssh-mapp om den inte finns
mkdir -p ~/.ssh

# Editera authorized_keys
vim ~/.ssh/authorized_keys

# Klistra in din publika nyckel
# Spara och stäng (ESC, :wq)
```

### Verifiera att det fungerar

**Hitta authorized_keys:**

```bash
cat ~/.ssh/authorized_keys
```

**Ska innehålla:**

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILongstring... user@hostname
```

**Testa inloggning:**

```bash
ssh username@ip-address
# Ska fråga efter passphrase för nyckel, INTE lösenord för användare
```

⚠️ **VIKTIGT**:

- Gör detta för **BÅDE Ubuntu OCH Fedora**
- Om du inte har nyckel i authorized_keys kommer du låsas ute när vi stänger av lösenordsinloggning!

---

## 🛡️ SSH Hardening

### Varför Hardening?

**Säkerhetsåtgärder för SSH:**

1. **Byt port** - Minska automatiska attackförsök
2. **Stäng av lösenord** - Endast SSH-nycklar
3. **Stäng av root-login** - Root ska aldrig logga in direkt
4. **Begränsa användare** - Whitelist vem som får logga in

### Skapa Konfigurationsfil

**På både Ubuntu och Fedora:**

```bash
# Skapa konfigurationsfil
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
```

**Filinnehåll:**

```
# Ändra port som SSH lyssnar på
Port 6622

# Stäng av lösenordsinloggning
PasswordAuthentication no

# Stäng av root-login
PermitRootLogin no

# Tillåt endast specifika användare
AllowUsers gg
```

**Anpassa:**

- `Port` - Välj valfri port (undvik 22, 80, 443, etc.)
- `AllowUsers` - Ditt användarnamn

### Varför `.d`-mappar?

**Fördelar med `/etc/ssh/sshd_config.d/`:**

- Huvudfilen (`/etc/ssh/sshd_config`) förblir orörd
- Enkelt att se vad som ändrats
- Enkelt att dela mellan system
- Enkelt att ta bort/inaktivera

**Include-direktiv i huvudfilen:**

```bash
Include /etc/ssh/sshd_config.d/*.conf
```

**Namngivning:**

- `01-` prefix anger ordning
- `.conf` suffix krävs för att inkluderas

---

### Uppdatera Brandvägg för Ny Port

⚠️ **VIKTIGT**: Lägg till nya porten INNAN du startar om SSH!

**Ubuntu (UFW):**

```bash
# Tillåt ny port
sudo ufw allow 6622

# Verifiera
sudo ufw status
```

**Fedora (firewalld):**

```bash
# Lägg till port (permanent)
sudo firewall-cmd --add-port=6622/tcp --permanent

# Ladda om regler
sudo firewall-cmd --reload

# Verifiera
sudo firewall-cmd --list-all
```

---

### Starta Om SSH-tjänsten

**Ubuntu:**

```bash
sudo systemctl restart ssh.service
```

**Fedora:**

```bash
sudo systemctl restart sshd.service
```

⚠️ **Notera skillnaden**: `ssh.service` vs `sshd.service`

**Verifiera att tjänsten körs:**

```bash
# Ubuntu
systemctl status ssh.service

# Fedora
systemctl status sshd.service
```

---

### Testa Ny Konfiguration

**Från din dator:**

```bash
# Med ny port
ssh -p 6622 username@ip-address

# Om det inte fungerar
ssh username@ip-address  # Prova gamla porten (22)
```

**Kontrollera vilken port SSH lyssnar på:**

```bash
ss -tulpn | grep ssh
# Eller
sudo ss -tulpn | grep 22
```

**Output exempel:**

```
tcp   LISTEN 0  128  0.0.0.0:6622  0.0.0.0:*
```

---

### Ta Bort Gamla Brandväggsregler

**När nya porten fungerar:**

**Ubuntu:**

```bash
# Lista regler med nummer
sudo ufw status numbered

# Output exempel:
# [1] 22          ALLOW IN    Anywhere
# [2] 6622        ALLOW IN    Anywhere
# [3] 22 (v6)     ALLOW IN    Anywhere (v6)
# [4] 6622 (v6)   ALLOW IN    Anywhere (v6)

# Ta bort regel (börja med högsta nummer!)
sudo ufw delete 3
sudo ufw delete 1
```

**Fedora:**

```bash
# Ta bort SSH-service (port 22)
sudo firewall-cmd --remove-service=ssh --permanent
sudo firewall-cmd --reload
```

---

## 📝 SSH Client Config

### Förenkla SSH-anslutning

**Problem:**

```bash
# Jobbigt att skriva varje gång
ssh -i ~/.ssh/id_ed25519 -p 6622 gg@192.168.64.5
```

**Lösning: SSH Config**

**Skapa/editera:**

```bash
vim ~/.ssh/config
```

**Exempel konfiguration:**

```
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
```

**Efter detta:**

```bash
ssh ubuntu  # Ansluter till Ubuntu VM
ssh fedora  # Ansluter till Fedora VM
```

**Fördelar:**

- Enklare kommandon
- Inget att komma ihåg
- Centraliserad konfiguration

**Läs mer:**

```bash
man 5 ssh_config
```

---

## 🔍 Felsökning

### Problem 1: Permission Denied efter SSH-copy-id

**Symptom:**

```bash
ssh username@ip-address
# Permission denied (publickey)
```

**Lösning:**

```bash
# Kontrollera att nyckel finns
cat ~/.ssh/authorized_keys

# Om tom eller fel - kopiera manuellt
# Se "Manuell kopiering" ovan
```

---

### Problem 2: Connection Refused

**Symptom:**

```bash
ssh username@ip-address
# Connection refused
```

**Möjliga orsaker:**

**1. SSH-tjänsten körs inte**

```bash
systemctl status ssh.service     # Ubuntu
systemctl status sshd.service    # Fedora

# Starta om om nödvändigt
sudo systemctl restart ssh.service
```

**2. Fel port**

```bash
# Prova med explicit port
ssh -p 6622 username@ip-address
```

**3. Brandvägg blockerar**

```bash
# Ubuntu
sudo ufw status

# Fedora
sudo firewall-cmd --list-all
```

---

### Problem 3: Låst Ute Efter Konfigurationsändring

**Symptom:**

- Kan inte logga in efter att ha ändrat SSH-config
- Connection refused eller timeout

**Lösning via VM-konsol (TTY):**

**Steg 1: Logga in via VirtualBox-konsolen**

- Öppna VM-fönstret
- Logga in direkt (inte via SSH)

**Steg 2: Återställ konfiguration**

```bash
# Ta bort eller kommentera din config
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf

# Eller ta bort filen helt
sudo rm /etc/ssh/sshd_config.d/01-ssh-hardening.conf

# Starta om SSH
sudo systemctl restart ssh.service  # Ubuntu
sudo systemctl restart sshd.service # Fedora
```

**Steg 3: Återställ brandvägg**

```bash
# Ubuntu - lägg till port 22
sudo ufw allow 22

# Fedora - lägg till SSH-service
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --reload
```

---

### Problem 4: SSH-tjänst Startar Inte

**Symptom:**

```bash
sudo systemctl restart sshd.service
# Job for sshd.service failed
```

**Diagnos:**

```bash
# Kontrollera status
systemctl status sshd.service

# Visa loggar
journalctl -u sshd.service -n 50
```

**Vanliga fel:**

**1. Typo i config**

```
# Fel:
Port 662 2  # Mellanslag
PasswordAuthentication yes no  # Två värden

# Rätt:
Port 6622
PasswordAuthentication no
```

**2. Permission denied på port**

```
# SELinux (Fedora) blockerar icke-standard portar
# Lösning: Använd port 22 eller konfigurera SELinux
```

---

### Problem 5: Authorized Keys Fungerar Inte

**Symptom:**

- Frågar fortfarande efter lösenord
- Nyckeln är i authorized_keys

**Kontrollera permissions:**

```bash
# .ssh-mappen
ls -ld ~/.ssh
# Ska vara: drwx------ (700)

# authorized_keys
ls -l ~/.ssh/authorized_keys
# Ska vara: -rw------- (600)
```

**Fixa permissions:**

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

---

## 💡 Viktiga Koncept

### Brandvägg - Koncept

**Varför brandvägg?**

- Skyddar mot oönskade anslutningar
- Begränsar attack-yta
- Kontrollerar in- och utgående trafik

**Default-politik:**

- **Deny incoming** - Blockera allt inkommande (säkert)
- **Allow outgoing** - Tillåt allt utgående (bekvämt)

**Explicit tillåt:**

- Bara öppna de portar som behövs
- Mindre attack-yta = säkrare system

### SSH-nycklar vs Lösenord

**Lösenord:**

- ❌ Kan gissas/bruteforcas
- ❌ Kan läcka (post-it notes!)
- ❌ Svaga lösenord vanliga
- ❌ Samma lösenord överallt

**SSH-nycklar:**

- ✅ Extremt svåra att knäcka
- ✅ Unika per dator
- ✅ Kan ha passphrase som extra skydd
- ✅ Kan revokeras utan att ändra lösenord

### Konfigurationsfiler i Linux

**Allt är en fil:**

```
/etc/ssh/sshd_config          # Huvudkonfiguration
/etc/ssh/sshd_config.d/       # Tilläggskonfiguration
```

**Fördelar:**

- Versionshanterbart (Git)
- Enkelt att kopiera mellan system
- Enkelt att automatisera
- Tydligt vad som ändrats

### `.d`-mappar

**Koncept:**

- Huvudfil inkluderar alla `.conf`-filer från `.d`-mapp
- Enkelt att lägga till/ta bort konfiguration
- Ingen risk att förstöra huvudfil

**Exempel:**

```
/etc/ssh/sshd_config.d/
├── 01-ssh-hardening.conf
├── 02-port-forwarding.conf
└── 03-custom-settings.conf
```

### Port Numbers

**Välkända portar (1-1023):**

- 22 - SSH
- 80 - HTTP
- 443 - HTTPS

**Registrerade portar (1024-49151):**

- Används av specifika tjänster

**Dynamiska portar (49152-65535):**

- Tillfälliga/privata portar

**Välj port för SSH:**

- Undvik välkända portar
- Exempel: 6622, 2222, 22000
- Kontrollera att porten inte används: `ss -tulpn | grep port`

---

## 📋 Cheat Sheet

### Brandvägg - Snabbkommandon

| Uppgift | Ubuntu (UFW) | Fedora (firewalld) |
|---------|--------------|-------------------|
| Status | `sudo ufw status` | `sudo firewall-cmd --list-all` |
| Aktivera | `sudo ufw enable` | `systemctl enable --now firewalld` |
| Tillåt port | `sudo ufw allow 22` | `sudo firewall-cmd --add-port=22/tcp --permanent` |
| Ta bort port | `sudo ufw delete allow 22` | `sudo firewall-cmd --remove-port=22/tcp --permanent` |
| Ladda om | - | `sudo firewall-cmd --reload` |
| Lista med nummer | `sudo ufw status numbered` | - |

### SSH - Snabbkommandon

| Uppgift | Kommando |
|---------|----------|
| Kopiera nyckel | `ssh-copy-id -i ~/.ssh/id_ed25519 user@host` |
| Logga in | `ssh user@host` |
| Logga in (annan port) | `ssh -p 6622 user@host` |
| Visa authorized keys | `cat ~/.ssh/authorized_keys` |
| Kontrollera SSH-status | `systemctl status ssh.service` (Ubuntu) |
|  | `systemctl status sshd.service` (Fedora) |
| Starta om SSH | `sudo systemctl restart ssh.service` |
| Visa SSH-loggar | `journalctl -u sshd.service -n 50` |
| Kolla vilken port | `ss -tulpn | grep ssh` |

### SSH Config - Exempel

```bash
# ~/.ssh/config
Host shortname
    HostName 192.168.1.100
    User username
    Port 6622
    IdentityFile ~/.ssh/id_ed25519
```

### SSH Hardening - Template

```bash
# /etc/ssh/sshd_config.d/01-ssh-hardening.conf
Port 6622
PasswordAuthentication no
PermitRootLogin no
AllowUsers username
```

---

## ⚠️ Viktiga Säkerhetsregler

### Regel 1: Alltid Brandvägg Först

```bash
# ✅ RÄTT ordning:
sudo ufw allow 22          # 1. Tillåt SSH
sudo ufw enable            # 2. Aktivera brandvägg

# ❌ FEL ordning:
sudo ufw enable            # 1. Aktivera brandvägg
sudo ufw allow 22          # 2. För sent - utlåst!
```

### Regel 2: Testa Innan Du Tar Bort

```bash
# ✅ RÄTT:
sudo ufw allow 6622        # 1. Lägg till ny port
sudo systemctl restart ssh # 2. Starta om SSH
ssh -p 6622 user@host      # 3. TESTA att det fungerar
sudo ufw delete allow 22   # 4. Ta bort gammal port

# ❌ FEL:
sudo ufw delete allow 22   # 1. Ta bort gammal port
sudo ufw allow 6622        # 2. För sent om något är fel!
```

### Regel 3: Ha Alltid Backup-åtkomst

- **Ha VM-konsolen tillgänglig** (VirtualBox-fönster)
- **Testa från separat terminal** innan du stänger nuvarande
- **Dokumentera vad du gör** så du kan ångra

### Regel 4: En Ändring i Taget

```bash
# ✅ RÄTT:
1. Byt port -> Testa -> Fungerar
2. Stäng av lösenord -> Testa -> Fungerar
3. Begränsa användare -> Testa -> Fungerar

# ❌ FEL:
1. Byt allt samtidigt -> Fungerar inte -> Vet inte vad som är fel
```

---

## 🎓 Lösningsguide - Steg för Steg

### Ubuntu - Komplett Setup

```bash
# 1. BRANDVÄGG
sudo ufw allow 22
sudo ufw enable
sudo ufw status

# 2. SSH-NYCKEL
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.5

# 3. SSH HARDENING
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
# Lägg till:
# Port 6622
# PasswordAuthentication no
# PermitRootLogin no
# AllowUsers gg

# 4. UPPDATERA BRANDVÄGG
sudo ufw allow 6622

# 5. STARTA OM SSH
sudo systemctl restart ssh.service

# 6. TESTA (från din dator)
ssh -p 6622 gg@192.168.64.5

# 7. TA BORT GAMMAL PORT
sudo ufw status numbered
sudo ufw delete [nummer för port 22]

# 8. CLIENT CONFIG (valfritt)
vim ~/.ssh/config
# Host ubuntu
#     HostName 192.168.64.5
#     User gg
#     Port 6622
#     IdentityFile ~/.ssh/id_ed25519
```

### Fedora - Komplett Setup

```bash
# 1. BRANDVÄGG (redan aktiv)
sudo firewall-cmd --list-all

# 2. SSH-NYCKEL
ssh-copy-id -i ~/.ssh/id_ed25519 gg@192.168.64.6

# 3. SSH HARDENING
sudo vim /etc/ssh/sshd_config.d/01-ssh-hardening.conf
# Lägg till:
# PasswordAuthentication no
# PermitRootLogin no
# AllowUsers gg
# OBS: Skippa Port på Fedora (SELinux-problem)

# 4. STARTA OM SSH
sudo systemctl restart sshd.service

# 5. TESTA
ssh gg@192.168.64.6

# 6. CLIENT CONFIG (valfritt)
vim ~/.ssh/config
# Host fedora
#     HostName 192.168.64.6
#     User gg
#     IdentityFile ~/.ssh/id_ed25519
```

---

## 🔧 Verifiering

### Kontrollera Att Allt Fungerar

**1. Brandvägg är aktiv**

```bash
# Ubuntu
sudo ufw status
# Ska visa: Status: active

# Fedora
sudo firewall-cmd --list-all
# Ska visa active zones
```

**2. SSH-nyckel fungerar**

```bash
ssh user@host
# Ska fråga efter passphrase för NYCKEL
# INTE lösenord för ANVÄNDARE
```

**3. Lösenord INTE fungerar**

```bash
# Prova logga in utan nyckel
ssh -o PubkeyAuthentication=no user@host
# Ska ge: Permission denied
```

**4. Root kan INTE logga in**

```bash
ssh root@host
# Ska ge: Permission denied
```

**5. Rätt port används**

```bash
ss -tulpn | grep ssh
# Ubuntu: Ska visa port 6622
# Fedora: Ska visa port 22
```

---

## 📚 Man Pages att Läsa

**SSH:**

```bash
man 5 ssh_config        # SSH client configuration
man 5 sshd_config       # SSH daemon configuration
man ssh-keygen          # Generate SSH keys
man ssh-copy-id         # Copy keys to server
```

**Brandvägg:**

```bash
man ufw                 # Ubuntu firewall
man firewall-cmd        # Fedora firewall
```

**System:**

```bash
man systemctl           # Service management
man journalctl          # Log viewing
```

---

## 🎯 Sammanfattning

### Vad Vi Gjorde

**1. Brandväggar**

- ✅ Aktiverat UFW på Ubuntu
- ✅ Verifierat firewalld på Fedora
- ✅ Tillåtit SSH-port (22)

**2. SSH-nycklar**

- ✅ Kopierat publik nyckel till servrar
- ✅ Kan logga in med nyckel istället för lösenord

**3. SSH Hardening**

- ✅ Bytt port (endast Ubuntu, SELinux-problem på Fedora)
- ✅ Stängt av lösenordsinloggning
- ✅ Stängt av root-login
- ✅ Begränsat tillåtna användare

**4. Bonus**

- ✅ Lärt oss om `.d`-mappar
- ✅ Lärt oss om SSH client config
- ✅ Förstått varför konfiguration-som-filer är bra

### Nyckelpunkter

**Säkerhet i lager:**

1. Brandvägg - Första försvaret
2. SSH-nycklar - Stark autentisering
3. Begränsad åtkomst - Minsta möjliga rättigheter
4. Icke-standard port - Mindre buller från bots

**Alltid:**

- Testa innan du tar bort gamla regler
- Ha backup-åtkomst (VM-konsol)
- En ändring i taget
- Dokumentera vad du gör

### Nästa Steg

1. ✅ Öva på SSH client config (`~/.ssh/config`)
2. ✅ Läs relevanta man pages
3. ✅ Kom på handledning om problem
4. ✅ Fortsätt använda SSH för alla VM-anslutningar

---

## 🆘 Om Du Behöver Hjälp

**Handledning:**

- Torsdagar 10-12 (huvudtid)
- Torsdagar eftermiddag (med Martin)

**Vanliga problem:**

- Låst ute: Använd VM-konsol (VirtualBox-fönster)
- Glömt port: Kolla i config-fil
- Nyckel fungerar inte: Kolla permissions (700/.ssh, 600/authorized_keys)

**Loggar för felsökning:**

```bash
# SSH-loggar
journalctl -u sshd.service -f

# Följ i realtid
tail -f /var/log/auth.log  # Ubuntu
```

---

**Bra jobbat med hands-on! 🚀**

*Konfiguration är en fil - ändra filen, starta om tjänsten, klar!*
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
    "content": r"""# Linux Användarhantering - Praktisk Övning

## Hands-On Lab: Användare, Grupper & Behörigheter

---

## 📋 Översikt

**Typ:** Praktisk övning (individuellt eller i grupp)
**Deadline:** Ingen fast deadline
**Obligatoriskt:** Nej (men starkt rekommenderat för lärande)
**System:** Valfritt VM (Ubuntu eller Fedora)
**Inlämning:** Via Slack

---

## 🎯 Scenario

Du arbetar på IT-avdelningen på ett företag och har fått i uppdrag att sätta upp användare på en ny server. Du har fått en kravlista som du ska implementera.

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

- Gruppnamn: `developers`

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

- Path: `/opt/developers`

**Säkerställ:**

1. **Bara members av developers-gruppen kan komma åt mappen**
   - Bob och David ska inte kunna komma åt den

2. **Alla filer som skapas i mappen ägs automatiskt av gruppen `developers`**
   - INTE av användarens primära grupp
   - Alla i gruppen kan komma åt alla filer by default

**Tips:**

- Detta löses med special permissions (SGID)
- Tänk på både directory permissions och group ownership

---

### Uppgift 4: Sätt Utgångsdatum för Konsulter

**Problem:**

- Bob och David är externa konsulter
- Deras uppdrag går ut vid årsskiftet

**Krav:**

- Deras konton ska sluta fungera från och med **1 januari 2026**
- Efter detta datum ska de inte kunna logga in

**Tips:**

- Läs `man usermod`
- Leta efter flaggor relaterade till expiration/expire

---

### Uppgift 5: Tvinga Lösenordsbyte

**Problem:**

- Någon har lånat Everts tangentbord
- De hittade en post-it med hans lösenord under tangentbordet
- Detta bryter mot företagets säkerhetspolicy
- Lösenordet betraktas som läckt

**Krav:**

- Tvinga Evert att byta lösenord vid nästa login
- Han ska inte kunna använda det gamla lösenordet

**Tips:**

- Läs `man passwd`
- Leta efter flaggor för password expiration/aging

---

## 📤 Inlämning

### Format

**Skicka via Slack:**

En lista med kommandon som löser varje uppgift:

```
Uppgift 1: Skapa användare
- sudo useradd alice
- sudo useradd bob
... etc

Uppgift 2: Skapa grupp och medlemmar
- sudo groupadd developers
... etc

Uppgift 3: Projektmapp och behörigheter
... etc

Uppgift 4: Utgångsdatum för konsulter
... etc

Uppgift 5: Tvinga lösenordsbyte
... etc
```

### Grupparbete

**Om ni jobbar i grupp:**

- En person skickar lösningen
- Ange **alla gruppmedlemmar** i meddelandet
- Exempel: "Löst av: Alice, Bob och Charlie"

**Viktigt:**

- Även om ni får hjälp, **förstå varje kommando**
- Kopiera inte bara - lär dig vad varje del gör
- Alla i gruppen ska kunna förklara lösningen

### Vad Ni INTE Behöver

- ❌ Inget skript krävs (men är ett plus!)
- ❌ Behöver inte köra alla kommandon i en fil
- ❌ Ingen automatisering nödvändig

**Ni kan:**

- ✅ Köra kommandon direkt i terminalen
- ✅ Anteckna kommandon vid sidan om
- ✅ Skicka kommandon som text
- ✅ (Bonus) Skapa ett skript som löser allt

---

## 🔍 Lösningsguide & Tips

### Användbara Kommandon

**Användarhantering:**

```bash
useradd          # Skapa användare
usermod          # Modifiera användare
passwd           # Hantera lösenord
userdel          # Ta bort användare
```

**Grupphantering:**

```bash
groupadd         # Skapa grupp
groupmod         # Modifiera grupp
usermod -aG      # Lägg användare till grupp
gpasswd          # Gruppåtkomst
```

**Behörigheter:**

```bash
chmod            # Ändra permissions
chown            # Ändra ägare
chgrp            # Ändra grupp
```

**Verifiering:**

```bash
id username      # Visa användarinfo
groups username  # Visa grupptillhörighet
ls -l            # Visa permissions
getent passwd    # Lista användare
getent group     # Lista grupper
```

### Viktiga Man Pages

```bash
man useradd      # Skapa användare
man usermod      # Modifiera användare (Uppgift 4!)
man passwd       # Lösenordshantering (Uppgift 5!)
man groupadd     # Skapa grupper
man chmod        # Permissions
man chown        # Ownership
```

### Special Permissions

**SGID (Set Group ID):**

- Används för Uppgift 3
- Gör att filer skapade i mappen ärver gruppägande
- Sätts med `chmod g+s` eller `chmod 2xxx`

**Exempel:**

```bash
chmod g+s /opt/developers        # Sätt SGID
chmod 2770 /opt/developers       # SGID + full access för grupp
```

### Tänk På

**Uppgift 1: Skapa användare**

- Använd `useradd` eller `adduser`
- Kanske vill ni sätta lösenord med `passwd`

**Uppgift 2: Grupper**

- Skapa gruppen först
- Lägg till användare med `usermod -aG`
- Verifiera med `groups username`

**Uppgift 3: Mapp och behörigheter**

- Skapa mappen: `mkdir /opt/developers`
- Sätt gruppägande: `chgrp developers /opt/developers`
- Sätt SGID: `chmod g+s /opt/developers`
- Sätt permissions: `chmod 770 /opt/developers`
  - 7 (owner): rwx
  - 7 (group): rwx
  - 0 (other): ---

**Uppgift 4: Expiration date**

- `usermod` har en flagga för expire date
- Datumet ska vara 2026-01-01
- Format: YYYY-MM-DD

**Uppgift 5: Force password change**

- `passwd` kan sätta password expiration
- Leta efter "expire" i man page
- Användaren tvingas byta vid nästa login

---

## ✅ Verifieringschecklist

### Uppgift 1: Användare skapade?

```bash
getent passwd alice
getent passwd bob
getent passwd charlie
getent passwd david
getent passwd evert
# Alla ska finnas i listan
```

### Uppgift 2: Grupp och medlemmar?

```bash
getent group developers
# Output ska visa: developers:x:1001:alice,charlie,evert

groups alice    # Ska inkludera developers
groups charlie  # Ska inkludera developers
groups evert    # Ska inkludera developers
groups bob      # Ska INTE inkludera developers
groups david    # Ska INTE inkludera developers
```

### Uppgift 3: Mapp och behörigheter?

```bash
ls -ld /opt/developers
# Output ska visa:
# drwxrws--- ... developers /opt/developers
#      ^
#      SGID-bit (s istället för x)

# Testa skapa fil som alice
sudo -u alice touch /opt/developers/test.txt
ls -l /opt/developers/test.txt
# Filen ska ägas av gruppen developers

# Testa åtkomst som bob (ska INTE fungera)
sudo -u bob ls /opt/developers
# Ska ge "Permission denied"
```

### Uppgift 4: Expiration date?

```bash
sudo chage -l bob
# Account expires: Jan 01, 2026

sudo chage -l david
# Account expires: Jan 01, 2026
```

### Uppgift 5: Password expire?

```bash
sudo chage -l evert
# Last password change: ... (ska visa att lösenord har expired)

# Eller prova logga in som evert
sudo -u evert bash
# Ska fråga om nytt lösenord
```

---

## 🎓 Lärandemål

Efter att ha genomfört denna övning ska du kunna:

1. ✅ Skapa och hantera användarkonton
2. ✅ Skapa och hantera grupper
3. ✅ Lägga till användare i grupper
4. ✅ Sätta och förstå file permissions
5. ✅ Använda special permissions (SGID)
6. ✅ Sätta utgångsdatum för användarkonton
7. ✅ Tvinga lösenordsbyte
8. ✅ Verifiera konfiguration
9. ✅ Läsa och förstå man pages

---

## 🚀 Steg-för-Steg Process

### Rekommenderad Arbetsordning

1. **Läs igenom hela uppgiften först**
   - Förstå vad som krävs
   - Identifiera vilka kommandon du behöver

2. **Börja med att läsa relevanta man pages**

   ```bash
   man useradd
   man usermod
   man groupadd
   man chmod
   man passwd
   ```

3. **Kolla inspelningen igen vid behov**
   - Om något är oklart
   - För att se praktiska exempel

4. **Jobba genom uppgifterna i ordning**
   - En uppgift i taget
   - Verifiera innan du går vidare

5. **Testa varje steg**
   - Använd verifieringskommandona
   - Se till att allt fungerar som det ska

6. **Dokumentera dina kommandon**
   - Anteckna vad du kör
   - Kommentera varför

7. **Skicka in när du är klar**
   - Via Slack
   - Inkludera alla gruppmedlemmar om tillämpligt

---

## 💡 Vanliga Fallgropar

### ❌ Fel 1: Glömmer sudo

```bash
useradd alice           # ❌ Permission denied
sudo useradd alice      # ✅ Fungerar
```

### ❌ Fel 2: Skriver över grupper

```bash
usermod -G developers alice    # ❌ Tar bort från andra grupper
usermod -aG developers alice   # ✅ Lägger till i grupp
```

### ❌ Fel 3: Glömmer SGID

```bash
chmod 770 /opt/developers      # ❌ Filer ärver inte grupp
chmod 2770 /opt/developers     # ✅ SGID satt, filer ärver grupp
# Eller
chmod g+s /opt/developers      # ✅ Sätt SGID explicit
```

### ❌ Fel 4: Fel datumformat

```bash
usermod --expiredate 01-01-2026 bob    # ❌ Fel format
usermod --expiredate 2026-01-01 bob    # ✅ YYYY-MM-DD
```

### ❌ Fel 5: Fel permission kommando för lösenord

```bash
passwd --expire evert           # ✅ Rätt kommando
chage -E 0 evert               # ✅ Alternativ metod
usermod --expire evert         # ❌ Fel kommando för lösenord
```

---

## 📚 Referensmaterial

### Viktiga Koncept från Föreläsningen

**Användare:**

- Varje person har eget konto
- Hanteras med `useradd`, `usermod`, `userdel`
- Lösenord hanteras med `passwd`

**Grupper:**

- Samlingar av användare
- Underlättar behörighetshantering
- Varje användare har en primär grupp
- Kan vara medlem i flera grupper

**Permissions:**

- Read (r), Write (w), Execute (x)
- För Owner, Group, Others
- Representeras som tre siffror (ex: 770)

**Special Permissions:**

- SGID (2000): Filer ärver gruppägande
- SUID (4000): Körs som filägare
- Sticky bit (1000): Bara ägare kan radera

**Account Expiration:**

- Användarkonton kan sättas att sluta fungera vid visst datum
- Hanteras med `usermod` eller `chage`

**Password Expiration:**

- Tvinga användare att byta lösenord
- Hanteras med `passwd` eller `chage`

---

## 🔧 Exempelkommandon (utan lösning)

**Dessa är exempel på kommandostruktur, inte kompletta lösningar:**

```bash
# Skapa användare (exempel struktur)
sudo useradd [options] username

# Lägg till i grupp (exempel struktur)
sudo usermod -aG groupname username

# Skapa mapp (exempel struktur)
sudo mkdir /path/to/directory

# Sätt permissions (exempel struktur)
sudo chmod [permissions] /path/to/directory

# Sätt gruppägande (exempel struktur)
sudo chgrp groupname /path/to/directory

# Sätt utgångsdatum (exempel struktur)
sudo usermod --expiredate YYYY-MM-DD username

# Tvinga lösenordsbyte (exempel struktur)
sudo passwd [option] username
```

---

## 🎯 Sammanfattning

**Uppgift:** Konfigurera användarhantering på en server

**Krav:**

1. ✅ 5 användare (Alice, Bob, Charlie, David, Evert)
2. ✅ 1 grupp (developers) med 3 medlemmar (Alice, Charlie, Evert)
3. ✅ 1 mapp (/opt/developers) med:
   - Endast developers-gruppen har åtkomst
   - SGID så filer ärver gruppägande
4. ✅ 2 konsulter (Bob, David) med utgångsdatum 2026-01-01
5. ✅ 1 användare (Evert) som måste byta lösenord vid nästa login

**Verktyg:**

- `useradd`, `usermod`, `passwd`
- `groupadd`, `gpasswd`
- `chmod`, `chown`, `chgrp`
- Man pages som guider

**Inlämning:**

- Slack
- Lista med kommandon per uppgift
- Ange gruppmedlemmar om tillämpligt

**Mål:**

- Praktisera allt från dagens föreläsning
- Förstå användarhantering i verkliga scenarion
- Kunna sätta upp och hantera användare professionellt

---

## 🆘 Om Du Fastnar

1. **Läs man pages**

   ```bash
   man useradd
   man usermod
   man passwd
   man chmod
   ```

2. **Kolla inspelningen igen**
   - Går igenom varje koncept praktiskt
   - Visar exempel

3. **Använd verifieringskommandon**

   ```bash
   id username
   groups username
   ls -l directory
   ```

4. **Fråga på handledning**
   - Torsdagar finns handledning
   - Ingen fråga är för enkel

5. **Jobba med klasskompis**
   - Diskutera lösningar
   - Förklara för varandra
   - Men se till att båda förstår

---

**Lycka till med övningen! 🚀**

*En praktisk övning i Linux-systemadministration*

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
    "content": r"""# Subnetting - Praktisk Övningsguide

## Lär dig beräkna subnet för hand

---

## 📋 Innehållsförteckning

1. [Vad är Subnetting?](#vad-är-subnetting)
2. [Grundläggande Koncept](#grundläggande-koncept)
3. [Steg-för-Steg Metod](#steg-för-steg-metod)
4. [Exempel från Föreläsningen](#exempel-från-föreläsningen)
5. [Snabbregler & Tips](#snabbregler--tips)
6. [Övning](#övning)
7. [Cheat Sheet](#cheat-sheet)

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

**Format:** `IP-adress/prefix`

**Exempel:** `192.168.1.0/24`

- IP-adress: `192.168.1.0`
- Prefix: `/24` (subnet mask)

### Prefix och Subnet Mask

| CIDR | Subnet Mask | Antal nätverk | Antal hosts |
|------|-------------|---------------|-------------|
| /8 | 255.0.0.0 | 1 byte | 16,777,214 |
| /16 | 255.255.0.0 | 2 bytes | 65,534 |
| /24 | 255.255.255.0 | 3 bytes | 254 |
| /25 | 255.255.255.128 | 3.5 bytes | 126 |
| /26 | 255.255.255.192 | 3.75 bytes | 62 |
| /27 | 255.255.255.224 | ~3.875 bytes | 30 |
| /28 | 255.255.255.240 | ~3.9375 bytes | 14 |
| /29 | 255.255.255.248 | ~3.96875 bytes | 6 |
| /30 | 255.255.255.252 | ~3.984375 bytes | 2 |

### Network vs Host-delen

En IP-adress består av två delar:

- **Network-delen** - Identifierar nätverket
- **Host-delen** - Identifierar enheten i nätverket

**Prefix anger var gränsen går:**

```
192.168.1.100/24
└─ Network ─┘└ Host ┘
   (24 bits)  (8 bits)
```

### Binära Positioner

**Varje byte har 8 bitar:**

```
Position:  1    2    4    8    16   32   64   128
Binär:    [0/1][0/1][0/1][0/1][0/1][0/1][0/1][0/1]
```

**Exempel: 192 i binärt**

```
128 + 64 = 192
[1] [1] [0] [0] [0] [0] [0] [0]
```

---

## 🔢 Steg-för-Steg Metod

### Steg 1: Hitta Gränsen

**Given:** IP-adress/prefix (ex: `192.168.1.100/26`)

**Beräkna var network-delen slutar:**

- Totalt: 32 bitar (4 bytes × 8 bits)
- Prefix: `/26` betyder 26 bitar för network

**Räkna:**

- Byte 1: Bit 1-8 (8 bitar)
- Byte 2: Bit 9-16 (16 bitar totalt)
- Byte 3: Bit 17-24 (24 bitar totalt)
- Byte 4: Bit 25-32

**Gränsen vid /26:**

- 24 bitar täcker 3 hela bytes
- 26 - 24 = 2 bitar in i byte 4
- Gränsen går efter bit 26

```
Byte 1    Byte 2    Byte 3    Byte 4
[8 bits]  [8 bits]  [8 bits]  [8 bits]
[─────────────────26 bits────────]│[6 bits]
        Network-delen            │ Host-delen
```

### Steg 2: Konvertera till Binärt

**Metod: Subtrahera från vänster till höger**

**För varje byte:**

1. Jämför med 128 - Större eller lika? → 1, annars → 0
2. Om ja: subtrahera 128
3. Jämför resten med 64
4. Om ja: subtrahera 64
5. Fortsätt: 32, 16, 8, 4, 2, 1

**Exempel: Konvertera 192**

```
Är 192 ≥ 128? Ja → 1, resten: 192-128=64
Är 64 ≥ 64?   Ja → 1, resten: 64-64=0
Är 0 ≥ 32?    Nej → 0
Är 0 ≥ 16?    Nej → 0
Är 0 ≥ 8?     Nej → 0
Är 0 ≥ 4?     Nej → 0
Är 0 ≥ 2?     Nej → 0
Är 0 ≥ 1?     Nej → 0

Resultat: 11000000 = 192
```

### Steg 3: Fyll i Network-delen

**Konvertera alla bytes fram till gränsen:**

För `/26`:

- Byte 1, 2, 3: Konvertera helt
- Byte 4: Konvertera bara första 2 bitar

### Steg 4: Beräkna Adresser

**Network Address:**

- Network-delen (som den är)
- Host-delen: **Alla nollor**

**Broadcast Address:**

- Network-delen (som den är)
- Host-delen: **Alla ettor**

**First Host:**

- Network Address + 1
- Eller: Network-delen + `00000001`

**Last Host:**

- Broadcast Address - 1
- Eller: Network-delen + `11111110`

**Next Subnet:**

- Addera 1 på sista biten i network-delen
- Host-delen: alla nollor

### Steg 5: Konvertera Tillbaka till Decimal

**Metod: Addera alla positioner med 1**

**Exempel:**

```
Binärt:    1 1 0 0 0 0 0 0
Position: 128 64 32 16 8 4 2 1
Värde:    128+64 = 192
```

---

## 📖 Exempel från Föreläsningen

### Exempel 1: 137.92.49.86/17

**Steg 1: Hitta gränsen**

```
/17 = 8 + 8 + 1
Gränsen går efter bit 17 (i byte 3)
```

**Steg 2: Konvertera till binärt**

**Byte 1: 137**

```
137 ≥ 128? Ja → 1, rest: 9
9 ≥ 64?    Nej → 0
9 ≥ 32?    Nej → 0
9 ≥ 16?    Nej → 0
9 ≥ 8?     Ja → 1, rest: 1
1 ≥ 4?     Nej → 0
1 ≥ 2?     Nej → 0
1 ≥ 1?     Ja → 1, rest: 0

137 = 10001001
```

**Byte 2: 92**

```
92 ≥ 128?  Nej → 0
92 ≥ 64?   Ja → 1, rest: 28
28 ≥ 32?   Nej → 0
28 ≥ 16?   Ja → 1, rest: 12
12 ≥ 8?    Ja → 1, rest: 4
4 ≥ 4?     Ja → 1, rest: 0
0 ≥ 2?     Nej → 0
0 ≥ 1?     Nej → 0

92 = 01011100
```

**Byte 3: 49 (endast första biten behövs för /17)**

```
49 ≥ 128?  Nej → 0
49 ≥ 64?   Nej → 0
49 ≥ 32?   Ja → 1, rest: 17
...fortsätt om nödvändigt

49 = 00110001 (men vi bryr oss bara om första biten: 0)
```

**Byte 4: 86** (host-delen, ignorera för network)

**Steg 3: Binär representation**

```
Byte 1      Byte 2      Byte 3    Byte 4
10001001 . 01011100 . 0│??????? . ????????
         Network (17)  │    Host (15)
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
10001001 . 01011100 . 00000000 . 00000000
= 137.92.0.0/17
```

**Broadcast Address:**

```
10001001 . 01011100 . 01111111 . 11111111
= 137.92.127.255/17

Byte 3: 01111111 = 64+32+16+8+4+2+1 = 127
Byte 4: 11111111 = 128+64+32+16+8+4+2+1 = 255
```

**First Host:**

```
Network + 1 = 137.92.0.1/17
```

**Last Host:**

```
Broadcast - 1 = 137.92.127.254/17
```

**Next Subnet:**

```
Network-delen + 1 (på bit 17):
10001001 . 01011100 . 1│0000000 . 00000000
= 137.92.128.0/17
```

---

### Exempel 2: 200.0.250.59/27

**Steg 1: Hitta gränsen**

```
/27 = 8 + 8 + 8 + 3
Gränsen går efter bit 27 (3 bitar in i byte 4)
```

**Steg 2-3: Konvertera och identifiera**

**Bytes 1-3:** Helt i network (konvertera alla)

```
200 = 11001000
0   = 00000000
250 = 11111010
```

**Byte 4: 59** (först 3 bitar för network)

```
59 ≥ 128?  Nej → 0
59 ≥ 64?   Nej → 0
59 ≥ 32?   Ja → 1, rest: 27

Första 3 bitar: 001
```

**Binär representation:**

```
11001000 . 00000000 . 11111010 . 001│?????
              Network (27)           │ Host (5)
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
11001000 . 00000000 . 11111010 . 00100000
Byte 4: 00100000 = 32
= 200.0.250.32/27
```

**Broadcast Address:**

```
11001000 . 00000000 . 11111010 . 00111111
Byte 4: 00111111 = 32+16+8+4+2+1 = 63
= 200.0.250.63/27
```

**First Host:**

```
= 200.0.250.33/27
```

**Last Host:**

```
= 200.0.250.62/27
```

**Next Subnet:**

```
Network-delen + 1:
11001000 . 00000000 . 11111010 . 01000000
Byte 4: 01000000 = 64
= 200.0.250.64/27
```

---

### Exempel 3: 194.184.226.53/29

**Steg 1: Hitta gränsen**

```
/29 = 32 - 29 = 3 bitar för host
Gränsen går efter bit 29 (5 bitar in i byte 4)
```

**Steg 2-3: Konvertera**

**Bytes 1-3:** (Helt i network)

```
194 = 11000010
184 = 10111000
226 = 11100010
```

**Byte 4: 53** (första 5 bitar för network)

```
53 = 00110101
Network: 00110│
Host:         │101
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
194.184.226 . 00110000
Byte 4: 00110000 = 32+16 = 48
= 194.184.226.48/29
```

**Broadcast Address:**

```
194.184.226 . 00110111
Byte 4: 00110111 = 32+16+4+2+1 = 55
= 194.184.226.55/29
```

**First Host:**

```
= 194.184.226.49/29
```

**Last Host:**

```
= 194.184.226.54/29
```

**Next Subnet:**

```
194.184.226 . 00111000
Byte 4: 00111000 = 32+16+8 = 56
= 194.184.226.56/29
```

---

## 💡 Snabbregler & Tips

### Snabbmetod för Binär Konvertering

**Kom ihåg positionerna:**

```
128  64  32  16  8  4  2  1
```

**För varje position från vänster till höger:**

1. Kan jag dra av detta värde?
2. Om JA → sätt 1, dra av värdet
3. Om NEJ → sätt 0, gå vidare

### Läsning av Binärt till Decimal

**Addera bara positioner med 1:**

```
Binärt:    1  0  1  1  0  1  0  1
Position: 128 64 32 16  8  4  2  1
Summera:  128+0+32+16+0+4+0+1 = 181
```

### Genvägar

**Network Address:**

- Bytes före gränsen: Ändras inte
- Byte vid gränsen: Behåll network-bitar, nollställ host-bitar
- Bytes efter gränsen: Alla nollor

**Broadcast Address:**

- Bytes före gränsen: Ändras inte
- Byte vid gränsen: Behåll network-bitar, ettor i host-bitar
- Bytes efter gränsen: Alla ettor (255)

**First Host:**

- Network Address + 1 (alltid)

**Last Host:**

- Broadcast Address - 1 (alltid)

**Next Subnet:**

- Addera 1 på sista network-biten
- Kan påverka föregående bytes om det blir "overflow"

### Minnesregler

**Alla nollor i host → Network**
**Alla ettor i host → Broadcast**
**Network + 1 → First Host**
**Broadcast - 1 → Last Host**
**Network + subnet size → Next Subnet**

### Vanliga CIDR-värden

| CIDR | Sista Byte Range | Subnet Size | Hosts |
|------|------------------|-------------|-------|
| /24 | 0-255 | 256 | 254 |
| /25 | 0-127, 128-255 | 128 | 126 |
| /26 | 0-63, 64-127, ... | 64 | 62 |
| /27 | 0-31, 32-63, ... | 32 | 30 |
| /28 | 0-15, 16-31, ... | 16 | 14 |
| /29 | 0-7, 8-15, ... | 8 | 6 |
| /30 | 0-3, 4-7, ... | 4 | 2 |

---

## 🎓 Övning

### Övningsverktyg

**Rekommenderat:** [subnet-ipv4.com](http://subnet-ipv4.com)

**Inställningar:**

- Genererar slumpmässiga IP/CIDR
- Visa/dölj lösning
- Olika svårighetsgrader

### Övningsprocess

1. **Få en övningsuppgift** från subnet-ipv4.com
2. **Lös för hand** på papper
3. **Kontrollera svaret** på webbplatsen
4. **Repetera** tills du känner dig säker

### Vad att Öva På

**Steg 1: Grundläggande (/24, /16, /8)**

- Gränsen går mellan bytes
- Enklare att visualisera

**Steg 2: Medel (/25, /26, /27)**

- Gränsen går inom sista byten
- Vanligaste i praktiken

**Steg 3: Avancerat (/28, /29, /30)**

- Mycket små subnät
- Precision krävs

**Steg 4: Udda Gränser (/17, /23, /19)**

- Gränsen inte vid "runda" värden
- Testa din förståelse

### Målet

**Kunna lösa utan:**

- ❌ Kalkylator för binär konvertering
- ❌ Subnet-kalkylator
- ❌ Googling

**Med endast:**

- ✅ Papper
- ✅ Penna
- ✅ Din hjärna

### När Är Du Klar?

**Du är redo när du kan:**

1. Snabbt identifiera var gränsen går
2. Konvertera decimal ↔ binär utan att tänka
3. Beräkna alla 5 värden konsekvent rätt
4. Förklara varför varje steg fungerar

---

## 📋 Cheat Sheet

### Process - Kort Sammanfattning

```
1. Hitta gränsen
   /prefix → Räkna bits → Markera var network slutar

2. Konvertera till binärt
   Decimal → Binär (subtraktionsmetoden)

3. Fyll i network-delen
   Konvertera bytes fram till gränsen

4. Beräkna adresser:
   Network   = Network-delen + 00000...
   Broadcast = Network-delen + 11111...
   First     = Network + 1
   Last      = Broadcast - 1
   Next      = Network-delen + 1 (på network-position)

5. Konvertera tillbaka
   Binär → Decimal (additionsmetoden)
```

### Binär Konvertering - Snabbguide

**Decimal → Binär:**

```
For varje position (128, 64, 32, 16, 8, 4, 2, 1):
  Om (värde ≥ position):
    Sätt 1
    värde = värde - position
  Annars:
    Sätt 0
```

**Binär → Decimal:**

```
For varje position med 1:
  Addera positionens värde
Summan = decimal värde
```

### CIDR Snabbreferens

| CIDR | Network Bits | Host Bits | Subnet Size |
|------|--------------|-----------|-------------|
| /8 | 8 | 24 | 16,777,216 |
| /16 | 16 | 16 | 65,536 |
| /24 | 24 | 8 | 256 |
| /25 | 25 | 7 | 128 |
| /26 | 26 | 6 | 64 |
| /27 | 27 | 5 | 32 |
| /28 | 28 | 4 | 16 |
| /29 | 29 | 3 | 8 |
| /30 | 30 | 2 | 4 |

### Minneslappar

**Beräkna host-bits:**

```
Host bits = 32 - CIDR
Exempel: /27 → 32-27 = 5 host bits
```

**Beräkna subnet size:**

```
Subnet size = 2^(host bits)
Exempel: 5 host bits → 2^5 = 32
```

**Beräkna användbara hosts:**

```
Användbara = Subnet size - 2
(minus network och broadcast)
Exempel: 32 - 2 = 30 hosts
```

---

## 🎯 Vanliga Misstag

### Misstag 1: Fel Gräns

❌ **Fel:**

```
/25 → Gränsen i byte 3
```

✅ **Rätt:**

```
/25 → 24 bits i första 3 bytes + 1 bit i byte 4
Gränsen går i byte 4
```

### Misstag 2: Glömmer Binär Konvertering

❌ **Fel:**

```
Network för 192.168.1.100/26
= 192.168.1.0 (gissar)
```

✅ **Rätt:**

```
Konvertera 100 till binärt: 01100100
26 bits = 24 + 2
Network: 192.168.1.01000000 = 192.168.1.64
```

### Misstag 3: Broadcast är Inte Alltid .255

❌ **Fel:**

```
Broadcast för något/26 = x.x.x.255
```

✅ **Rätt:**

```
/26 → 6 host bits
Broadcast beror på var subnet börjar
Kan vara .63, .127, .191, eller .255
```

### Misstag 4: Next Subnet

❌ **Fel:**

```
Next subnet = Network + 1
```

✅ **Rätt:**

```
Next subnet = Network + subnet size
Eller: Broadcast + 1
```

---

## 📚 Sammanfattning

### Vad Vi Lärde Oss

1. ✅ Konvertera decimal ↔ binär
2. ✅ Identifiera network/host-gränsen
3. ✅ Beräkna network address
4. ✅ Beräkna broadcast address
5. ✅ Beräkna first/last host
6. ✅ Beräkna next subnet

### Nyckelpunkter

**Subnetting är:**

- Logiskt, inte svårt
- Baserat på binär aritmetik
- Följer fasta regler
- Övar gör mästare

**Reglerna:**

1. Gränsen bestäms av CIDR (/prefix)
2. Network = network-delen + nollor
3. Broadcast = network-delen + ettor
4. First = Network + 1
5. Last = Broadcast - 1
6. Next = Network + subnet size

### Nästa Steg

1. 📝 Öva på [subnet-ipv4.com](http://subnet-ipv4.com)
2. 🎯 Börja med enkla (/24, /16)
3. 📈 Arbeta upp till svårare (/27, /29, /17)
4. 🔁 Repetera tills det sitter
5. ⏱️ Öka hastighet med övning

### Tips för Framgång

- **Öva varje dag** - Även 10 minuter hjälper
- **Använd papper** - Ingen shortcuts
- **Förstå varför** - Inte bara hur
- **Gör misstag** - Lär från dem
- **Testa dig själv** - Utan lösning först

---

**Lycka till med subnetträningen! 🚀**

*Matematik är bara ett verktyg - logik är din superkraft!*

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
    "content": r"""# Docker & Containers - Hands-On Guide

## Från installation till första container på 30 minuter

---

## 📋 Innehållsförteckning

1. [Varför Docker?](#varför-docker)
2. [Installation - Ubuntu](#installation---ubuntu)
3. [Installation - Fedora](#installation---fedora)
4. [Fix: Docker utan sudo](#fix-docker-utan-sudo)
5. [Grundläggande Kommandon](#grundläggande-kommandon)
6. [Praktiska Exempel](#praktiska-exempel)
7. [Felsökning](#felsökning)
8. [Cheat Sheet](#cheat-sheet)

---

## 🎯 Varför Docker?

### Container vs VM

**Virtual Machine (VM):**

```
┌─────────────────────┐
│  Applikation        │
│  Python 3.12        │
│  Bibliotek          │
├─────────────────────┤
│  Guest OS (Ubuntu)  │  ← Flera GB
│  Kernel             │
├─────────────────────┤
│  Hypervisor         │
├─────────────────────┤
│  Host OS            │
└─────────────────────┘
```

**Container:**

```
┌─────────────────────┐
│  Applikation        │
│  Python 3.12        │
│  Bibliotek          │  ← 25 KB - 80 MB
├─────────────────────┤
│  Host OS Kernel     │  ← Delad!
└─────────────────────┘
```

### Konkret Exempel från Lektionen

**Python Hello World:**

- VM: Flera GB (helt OS)
- Container: 25 KB

**Python 3.14 Alpine:**

- VM: Flera GB
- Container: 73 MB

### Varför Containers Vinner

✅ **Versionshantering:**

- Kör 5 olika Python-versioner samtidigt
- Ingen konflikt med OS:ets version
- Inga panikuppdateringar när OS uppdaterar

✅ **Effektivitet:**

- Delar kernel med host
- Bara det du behöver, inget mer
- Snabb start (sekunder vs minuter)

✅ **Isolation:**

- Varje app i sin egen miljö
- Dependencies krockar inte
- Enklare säkerhet

---

## 🔧 Installation - Ubuntu

### Steg 1: Rensa Gamla Versioner

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

**Om du får:** "No packages found" → Perfekt! Fortsätt.

### Steg 2: Sätt upp Docker's Repository

**Varför?** Docker's egna repos är mer up-to-date än Ubuntu's.

```bash
# Update och installera dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl

# Skapa directory för GPG-nycklar
sudo install -m 0755 -d /etc/apt/keyrings

# Ladda ner Docker's GPG-nyckel (verifierar paket är äkta)
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Lägg till Docker's repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Uppdatera mot nya repository
sudo apt-get update
```

### Steg 3: Installera Docker

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

**Vad installeras?**

- `docker-ce` - Docker Engine
- `docker-ce-cli` - Kommandoradsverktyg
- `containerd.io` - Container runtime
- `docker-buildx-plugin` - Bygga images
- `docker-compose-plugin` - Multi-container appar

### Steg 4: Verifiera Installation

```bash
# Kolla att docker finns
which docker
# Output: /usr/bin/docker

# Kolla Docker-servicen
systemctl status docker.service
```

**Du ska se:**

- ● docker.service - Docker Application Container Engine
- Active: **active (running)**
- Enabled: **enabled**

**Om servicen inte är igång:**

```bash
sudo systemctl start docker.service
sudo systemctl enable docker.service
```

### Steg 5: Testa

```bash
sudo docker run hello-world
```

**Du ska se:**

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## 🔧 Installation - Fedora

### Samma Koncept, Andra Kommandon

**Dokumentation:** <https://docs.docker.com/engine/install/fedora/>

```bash
# 1. Ta bort gamla versioner
sudo dnf remove docker docker-client docker-client-latest \
  docker-common docker-latest docker-latest-logrotate \
  docker-logrotate docker-selinux docker-engine-selinux docker-engine

# 2. Sätt upp repository
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo \
  https://download.docker.com/linux/fedora/docker-ce.repo

# 3. Installera Docker
sudo dnf install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin

# 4. Starta Docker
sudo systemctl start docker
sudo systemctl enable docker

# 5. Testa
sudo docker run hello-world
```

---

## ⚡ Fix: Docker utan sudo

### Problemet

```bash
docker run hello-world
# permission denied while trying to connect to the Docker daemon socket
```

### Varför?

Docker lyssnar på en **Unix socket** (`/var/run/docker.sock`).
Bara `root` och medlemmar i gruppen `docker` får koppla till den.

### Lösningen

```bash
# Se alla grupper du är med i
id

# Lägg till dig själv i docker-gruppen
sudo usermod -aG docker $USER

# ALTERNATIVT (samma sak):
sudo gpasswd -a $USER docker

# Logga ut och in igen
exit
# (SSH in igen)

# Verifiera att docker-gruppen finns
id
# Du ska se "docker" i listan

# Testa utan sudo
docker run hello-world
# Success! 🎉
```

**VIKTIGT:** Du MÅSTE logga ut och in igen för att ändringen ska gälla!

---

## 🚀 Grundläggande Kommandon

### docker run - Starta Container

**Syntax:**

```bash
docker run [OPTIONS] IMAGE[:TAG] [COMMAND]
```

**Grundläggande:**

```bash
# Kör hello-world
docker run hello-world

# Kör med specifik tag/version
docker run python:3.14-alpine

# Kör med namn
docker run --name my-container python:3.14-alpine
```

**Vanliga Flaggor:**

| Flagga | Betydelse | Användning |
|--------|-----------|------------|
| `-i` | Interactive | Håll stdin öppen |
| `-t` | TTY | Allokera pseudo-terminal |
| `-it` | Kombinerat | Interaktiv session (båda ovan) |
| `--rm` | Remove | Ta bort container vid exit |
| `--name` | Namnge | Ge containern ett namn |
| `-d` | Detached | Kör i bakgrunden |

**Exempel:**

```bash
# Interaktiv Python-shell (stanna i containern)
docker run -it python:3.14-alpine

# Interaktiv, ta bort när klar
docker run -it --rm python:3.14-alpine

# Bakgrund med namn
docker run -d --name my-app nginx
```

### docker ps - Lista Containers

```bash
# Visa körande containers
docker ps

# Visa ALLA (även stoppade)
docker ps -a
```

**Output:**

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    NAMES
abc123def456   python    "python"  2 min ago Up 2 min  eager_tesla
```

### docker images - Lista Images

```bash
# Visa nedladdade images
docker images
# ELLER
docker image ls
```

**Output:**

```
REPOSITORY   TAG      IMAGE ID      CREATED      SIZE
python       3.14     abc123def     2 days ago   73MB
hello-world  latest   def456abc     3 weeks ago  25KB
```

### docker rm - Ta Bort Container

```bash
# Ta bort en stoppad container (med namn)
docker rm blissful_bell

# Ta bort med container ID
docker rm abc123def456

# Ta bort alla stoppade containers
docker container prune
```

### docker rmi - Ta Bort Image

```bash
# Ta bort en image
docker rmi python:3.12-alpine

# Ta bort alla oanvända images
docker image prune
```

### docker stop/start/restart

```bash
# Stoppa en körande container
docker stop my-container

# Starta en stoppad container
docker start my-container

# Starta om
docker restart my-container
```

---

## 💡 Praktiska Exempel

### Exempel 1: Testa Olika Python-Versioner

**Problem:** Du har Python 3.12 på din maskin, men behöver testa kod i 3.9, 3.10, 3.13, 3.14.

**Lösning med Docker:**

```bash
# Python 3.9
docker run -it --rm python:3.9-alpine
# Python 3.9.25

# Python 3.10
docker run -it --rm python:3.10-alpine
# Python 3.10.x

# Python 3.13
docker run -it --rm python:3.13-alpine
# Python 3.13.x

# Python 3.14 (senaste)
docker run -it --rm python:3.14-alpine
# Python 3.14.1
```

**Utan Docker:**

- Installera flera Python-versioner manuellt
- Hantera PATH
- Potentiella konflikter
- Röra med OS:ets Python = Farligt!

**Med Docker:**

- En rad kod
- Noll konflikter
- Noll påverkan på host

### Exempel 2: Image Tags

**Koncept:** Ett image kan ha flera **tags** (versioner).

**Format:** `image:tag`

```bash
# Utan tag = latest (default)
docker run python
# = docker run python:latest

# Med specifik tag
docker run python:3.14-alpine
docker run python:3.13
docker run python:3.12-slim
```

**Vanliga Tag-typer:**

| Tag | Betydelse |
|-----|-----------|
| `latest` | Senaste versionen (default) |
| `3.14` | Specifik version |
| `3.14-alpine` | Version + Alpine Linux (mindre) |
| `3.14-slim` | Version + minimal Debian |
| `3.14.1` | Exakt patch-version |

**Best Practice:** Använd **specifika tags** i produktion!

```bash
# ❌ Dåligt (kan ändras)
docker run python:latest

# ✅ Bra (förutsägbart)
docker run python:3.14.1-alpine
```

### Exempel 3: Container Lifecycle

```bash
# 1. Starta en container MED namn
docker run -it --name test-python python:3.14-alpine

# (Inne i containern, kör Python-kod)
>>> print("Hello Docker!")
>>> exit()

# 2. Container stoppades när du exitade
docker ps
# Tom lista

docker ps -a
# test-python   Exited (0) 2 seconds ago

# 3. Starta om samma container
docker start -i test-python
# (Inne igen!)

# 4. Stoppa från host (annat terminal)
docker stop test-python

# 5. Ta bort
docker rm test-python
```

### Exempel 4: Auto-Remove

**Problem:** Du vill bara testa något snabbt, vill inte städa efter dig.

**Lösning:**

```bash
# MED --rm flaggan
docker run -it --rm --name temp-test python:3.14-alpine

# (Inne i containern)
>>> print("Temporär container!")
>>> exit()

# Container är AUTOMATISKT BORTA
docker ps -a
# Ingen "temp-test"!
```

---

## 🔍 Felsökning

### Problem 1: Kan inte nå Internet från Container

**Symptom:**

```bash
docker run -it ubuntu
apt-get update
# Err: Could not resolve archive.ubuntu.com
```

**Diagnos:**

```bash
# 1. Kolla network interfaces
ip addr

# 2. Kolla routes
ip route

# 3. Testa internet från host
ping google.com
```

**Lösning (från lektionen):**

NAT-interface har ingen IP-adress → DHCP inte startad.

```bash
# Starta DHCP på NAT-interface
sudo dhclient enp0s8
# (byt enp0s8 mot ditt NAT-interface namn)

# Verifiera
ip addr
# Ser du IP på NAT-interface?

ip route
# Ser du default via NAT?

# Testa
ping 8.8.8.8
ping google.com
```

### Problem 2: DNS fungerar inte

**Symptom:**

```bash
docker run hello-world
# Error: Could not resolve docker registry
```

**Lösning:**

```bash
# Ändra DNS i resolv.conf
sudo nano /etc/resolv.conf

# Lägg till:
nameserver 8.8.8.8
nameserver 1.1.1.1
```

### Problem 3: "Unit docker.service could not be found"

**På Fedora:**

**Fel:**

```bash
systemctl status docker.services
# Unit docker.services could not be found
```

**Rätt:**

```bash
systemctl status docker.service
# (Notera: .service INTE .services)
```

### Problem 4: Permission Denied (igen och igen)

**Lösning:**

```bash
# Dubbelkolla att du är i docker-gruppen
id | grep docker

# Om inte:
sudo usermod -aG docker $USER

# Logga ut och in HELT
exit
# SSH in igen

# Testa
docker run hello-world
```

---

## 📋 Cheat Sheet

### Installation

```bash
# Ubuntu - One-liner (efter dependencies)
sudo apt-get install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin

# Fedora - One-liner
sudo dnf install docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

### Användarrättigheter

```bash
# Lägg till dig själv i docker-gruppen
sudo usermod -aG docker $USER
# Logga ut och in igen!
```

### Grundläggande Kommandon

```bash
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

# Lista images
docker images

# Stoppa container
docker stop NAMN/ID

# Starta container
docker start NAMN/ID

# Ta bort container
docker rm NAMN/ID

# Ta bort alla stoppade
docker container prune

# Ta bort image
docker rmi IMAGE:TAG
```

### Vanliga Images

```bash
# Hello World (test)
docker run hello-world

# Python (olika versioner)
docker run -it --rm python:3.14-alpine
docker run -it --rm python:3.13
docker run -it --rm python:3.9

# Ubuntu (för testing)
docker run -it --rm ubuntu

# Nginx (web server)
docker run -d -p 80:80 nginx
```

### Flaggor - Snabbguide

```bash
-i          # Interactive (håll stdin öppen)
-t          # TTY (terminal)
-it         # Kombinerat (interaktiv session)
--rm        # Ta bort vid exit
--name      # Ge namn
-d          # Detached (bakgrund)
-p 80:80    # Port mapping (host:container)
-v /path    # Volume (persistent data)
```

---

## 🎯 Viktiga Koncept

### Images vs Containers

**Image:**

- Mall/blueprint
- Läses från disk
- Kan användas om och om igen
- Tar diskutrymme

**Container:**

- Körande instans av image
- Kan ha många containers från samma image
- Tar MINIMAL extra diskutrymme (bara ändringar)
- Tar RAM när den kör

**Analogi:**

- Image = Klass
- Container = Objekt/instans

### Layers & Storage

**Varför 8 images tar bara ~300 MB?**

Images delar **layers**:

```
python:3.14-alpine    73 MB
  ├─ Alpine base      5 MB   ← Delad
  ├─ Python deps      50 MB  ← Delad
  └─ Python 3.14      18 MB

python:3.13-alpine    70 MB
  ├─ Alpine base      5 MB   ← SAMMA! Ingen extra diskplats
  ├─ Python deps      50 MB  ← SAMMA!
  └─ Python 3.13      15 MB  ← Bara DENNA är ny
```

**Resultat:**

- Första imagen: 73 MB
- Andra imagen: +15 MB (inte +70 MB!)

### Container Disk Usage

När du kör `docker container prune`:

```
Total reclaimed space: 8 MB
```

**Varför så lite?**

- Containers **delar** image-data
- Bara **ändringar** sparas per container
- En stoppad container = några MB av diff

---

## 🚀 Nästa Steg

### Måndagens Lektion (Fördjupning)

Vi kommer lära oss:

- Port mapping (exponera services)
- Volumes (persistent data)
- Networks (containers som pratar)
- Docker Compose (multi-container apps)
- Bygga egna images

### Förberedelser

**Gör klart till måndag:**

1. ✅ Docker installerat på **minst 1 VM** (helst båda)
2. ✅ Kan köra `docker run` utan sudo
3. ✅ Testat basic commands
4. ✅ (Frivilligt) Installera Docker Desktop på Mac/PC

### Övningar

**Testa själv:**

```bash
# 1. Kör olika Python-versioner
docker run -it --rm python:3.9-alpine
docker run -it --rm python:3.14-alpine

# 2. Kör Ubuntu och installera något
docker run -it --rm ubuntu
# apt-get update && apt-get install curl

# 3. Kolla disk usage
docker images
docker ps -a

# 4. Städa
docker container prune
docker image prune
```

---

### Nyckelpunkter

**Containers är:**

- Lightweight (KB till MB, inte GB)
- Isolerade (egen miljö per app)
- Portabla (samma överallt)
- Versionshanterbara (specifika tags)

**Docker är:**

- Framtiden för deployment
- Standard i DevOps
- Grunden för Kubernetes
- Viktigt för er LIA

### Långsiktig Plan

1. **Linux-kursen (nu):** Docker basics
2. **DevOps-kursen:** Kubernetes + CI/CD
3. **Fördjupning:** Drifta Kubernetes
4. **LIA:** Använd från dag 1!

---

*"Containers are like Lego blocks - små, modulära, och går att kombinera hur som helst!"*

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
    "content": r"""# Block Storage & Kryptering
## Hands-On Demonstration: Disk, Partition, Encryption, Filesystem

---

## 📋 Innehållsförteckning

1. [Hierarkin - Övergripande](#hierarkin---övergripande)
2. [Lägga till en Ny Disk](#lägga-till-en-ny-disk)
3. [Partitionering med fdisk](#partitionering-med-fdisk)
4. [Kryptering med LUKS](#kryptering-med-luks)
5. [Skapa Filsystem](#skapa-filsystem)
6. [Mount och Unmount](#mount-och-unmount)
7. [Obligatorisk Assignment](#obligatorisk-assignment)
8. [Viktiga Koncept](#viktiga-koncept)
9. [Kommandoreferens](#kommandoreferens)

---

## 🏗️ Hierarkin - Övergripande

### Lagren från Hårdvara till Tillgänglig Data

```
┌─────────────────────────────────────┐
│   FYSISK DISK (Hårdvara)            │
│   /dev/sdb (5 GB)                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   PARTITION                          │
│   /dev/sdb1 (5 GB)                  │
│   (Logisk uppdelning av disk)       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   KRYPTERING (Valfritt)             │
│   /dev/mapper/cryptodisk            │
│   (LUKS-krypterad volym)            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   FILSYSTEM                          │
│   ext4                               │
│   (Organiserar filer och mappar)    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   MOUNT POINT                        │
│   /mnt                               │
│   (Tillgängligt i filträdet)        │
└─────────────────────────────────────┘
```

### Varför Denna Ordning?

1. **Disk (Device)** - Fysisk eller virtuell hårdvara
2. **Partition** - Logisk uppdelning (även om bara en partition)
3. **Kryptering** - Säkerhetslager (valfritt)
4. **Filsystem** - Struktur för data
5. **Mount Point** - Åtkomstpunkt i filträdet

⚠️ **VIKTIGT**: Ordningen är kritisk och kan inte ändras!

---

## 💿 Lägga till en Ny Disk

### I VirtualBox

**Steg 1: Stäng av VM**
```bash
sudo systemctl poweroff
```

**Steg 2: VirtualBox Settings**
1. Högerklicka på VM → Settings
2. Storage → Controller: SATA
3. Klicka på "+" för att lägga till disk
4. "Create new disk" → VDI → Dynamically allocated
5. Storlek: 5 GB (eller valfri storlek)
6. OK

**Steg 3: Starta VM**
```bash
# Starta utan GUI
```

### Verifiera Ny Disk

**Lista alla block devices:**
```bash
lsblk
```

**Output exempel:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1G  0 part /boot
└─sda2   8:2    0   24G  0 part /
sdb      8:16   0    5G  0 disk
sr0     11:0    1 1024M  0 rom
```

**Förklaring:**
- `sda` - Första disken (25 GB, root-disk)
  - `sda1` - Boot-partition (1 GB)
  - `sda2` - Root-partition (24 GB)
- `sdb` - **Nya disken** (5 GB, omonterad)
- `sr0` - Virtuell CD/DVD-läsare

**Kontrollera device-filer:**
```bash
ls -l /dev/sd*
```

**Output:**
```
brw-rw---- 1 root disk 8,  0 Nov 28 10:00 /dev/sda
brw-rw---- 1 root disk 8,  1 Nov 28 10:00 /dev/sda1
brw-rw---- 1 root disk 8,  2 Nov 28 10:00 /dev/sda2
brw-rw---- 1 root disk 8, 16 Nov 28 10:00 /dev/sdb
```

- `b` = **Block device**
- `rw-rw----` = Permissions
- `/dev/sdb` = Hela disken
- Inga partitioner på `sdb` än

---

## 🔧 Partitionering med fdisk

### Varför Partitionera?

**Även för en partition:**
- Best practice att alltid partitionera
- Möjliggör framtida uppdelning
- Struktur och organisation

**Kommando:**
```bash
sudo fdisk /dev/sdb
```

⚠️ **VARNING**: Dubbelkolla att du anger rätt disk! Fel disk = dataförlust!

### fdisk - Interaktiv Session

**Viktiga kommandon i fdisk:**

| Kommando | Funktion |
|----------|----------|
| `m` | Visa hjälp |
| `p` | Print (visa partitioner) |
| `g` | Skapa GPT partition table |
| `n` | New partition |
| `w` | Write (spara ändringar) |
| `q` | Quit (avsluta utan att spara) |

### Steg-för-Steg Partitionering

**Steg 1: Starta fdisk**
```bash
sudo fdisk /dev/sdb
```

**Output:**
```
Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x...

Command (m for help):
```

**Steg 2: Skapa GPT Partition Table**
```
Command (m for help): g
```

**Output:**
```
Created a new GPT disklabel (GUID Partition Table).
```

**Steg 3: Visa nuvarande status**
```
Command (m for help): p
```

**Output:**
```
Disk /dev/sdb: 5 GiB
...
Disk identifier: ...

No partitions found
```

**Steg 4: Skapa ny partition**
```
Command (m for help): n
```

**Dialog:**
```
Partition number (1-128, default 1): [Enter]
First sector (2048-..., default 2048): [Enter]
Last sector (..., default ...): [Enter]

Created a new partition 1 of type 'Linux filesystem' and of size 5 GiB.
```

**Förklaring:**
- Partition number: 1 (default är bra)
- First sector: 2048 (default är bra)
- Last sector: Default tar hela disken

**Steg 5: Verifiera partition**
```
Command (m for help): p
```

**Output:**
```
Device     Start      End  Sectors Size Type
/dev/sdb1   2048 10485759 10483712   5G Linux filesystem
```

**Steg 6: Spara ändringar**
```
Command (m for help): w
```

**Output:**
```
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

⚠️ **VIKTIGT**: Ändringar sparas INTE förrän du trycker `w`!

### Verifiera Partitionen

```bash
lsblk
```

**Output:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb      8:16   0    5G  0 disk
└─sdb1   8:17   0    5G  0 part
```

Nu har vi en partition! ✅

---

## 🔐 Kryptering med LUKS

### Vad är LUKS?

**LUKS** = Linux Unified Key Setup
- Standard för disk-kryptering i Linux
- Krypterar hela partitioner
- Lösenordsskyddad
- Transparent kryptering/dekryptering

### cryptsetup - Huvudkommando

**Subkommandon:**
- `luksFormat` - Initiera LUKS-partition
- `open` - Öppna (dekryptera) volym
- `close` - Stäng (kryptera) volym
- `status` - Visa status

### Kryptera Partitionen

**Kommando:**
```bash
sudo cryptsetup luksFormat /dev/sdb1
```

⚠️ **VARNING**: Dubbelkolla partition! Fel partition = dataförlust!

**Dialog:**
```
WARNING!
========
This will overwrite data on /dev/sdb1 irrevocably.

Are you sure? (Type 'yes' in capital letters): YES

Enter passphrase for /dev/sdb1: [skriv lösenord]
Verify passphrase: [upprepa lösenord]
```

**Viktiga punkter:**
- Måste skriva **`YES`** i VERSALER
- Lösenordet syns INTE när du skriver (säkerhet)
- Lösenordslängden döljs för säkerhet (metadata)
- **Det finns INGET sätt att återställa lösenordet!**

### Varför Syns Inte Lösenordet?

**Säkerhet:**
- Längden på lösenordet är metadata
- Metadata hjälper vid lösenordsknäckning
- Ingen visuell feedback = säkrare

**Exempel:**
```
Synligt: ********  (8 tecken)
→ Angripare vet: "Lösenord är 8 tecken"

Osynligt:
→ Angripare vet: "Okänd längd"
```

### Öppna Krypterad Volym

**Kommando:**
```bash
sudo cryptsetup open /dev/sdb1 cryptodisk
```

**Förklaring:**
- `/dev/sdb1` - Partition att öppna
- `cryptodisk` - Namn på dekrypterad volym (välj själv)

**Dialog:**
```
Enter passphrase for /dev/sdb1: [lösenord]
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt
```

- `sdb1` = Krypterad partition
- `cryptodisk` = Dekrypterad volym (type: `crypt`)

### Device-fil för Krypterad Volym

```bash
ls -l /dev/mapper/cryptodisk
```

**Output:**
```
lrwxrwxrwx 1 root root 7 Nov 28 10:30 /dev/mapper/cryptodisk -> ../dm-0
```

- Länk till `/dev/dm-0`
- `dm` = Device Mapper

```bash
ls -l /dev/dm-0
```

**Output:**
```
brw-rw---- 1 root disk 253, 0 Nov 28 10:30 /dev/dm-0
```

- Block device (`b`)
- Används för att skapa filsystem

---

## 📁 Skapa Filsystem

### mkfs - Make Filesystem

**Kommando:**
```bash
sudo mkfs.ext4 /dev/mapper/cryptodisk
```

**Förklaring:**
- `mkfs.ext4` - Skapa ext4-filsystem
- `/dev/mapper/cryptodisk` - På krypterad volym

**Output:**
```
mke2fs 1.46.5 (30-Dec-2021)
Creating filesystem with 1310720 4k blocks and 327680 inodes
Filesystem UUID: ...
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```

**Nu har vi:**
- ✅ Disk
- ✅ Partition
- ✅ Kryptering
- ✅ Filsystem

### Varför ext4?

**Ext4 (Extended File System 4):**
- Standard i de flesta Linux-distributioner
- Journaling (återhämtning vid krasch)
- Lost+Found för återhämtning
- Snabb och pålitlig

**Andra alternativ:**
- `ext3` - Äldre version
- `xfs` - Bra för stora filer
- `btrfs` - Avancerad (snapshots, compression)
- `fat32` - Windows-kompatibel
- `ntfs` - Windows native

---

## 🔗 Mount och Unmount

### Vad är Mount?

**Mount** = Göra ett filsystem tillgängligt i filträdet

**Koncept:**
```
Innan mount:
/mnt/  [tom mapp]

Efter mount av cryptodisk till /mnt:
/mnt/  [cryptodisk innehåll]
```

### Mount-kommandot

**Syntax:**
```bash
sudo mount [device] [mount-point]
```

**Exempel:**
```bash
sudo mount /dev/mapper/cryptodisk /mnt
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt /mnt
```

Nu är `cryptodisk` monterad på `/mnt`! ✅

### Undersöka Monterad Volym

```bash
ls -la /mnt
```

**Output:**
```
total 24
drwxr-xr-x  3 root root  4096 Nov 28 10:35 .
drwxr-xr-x 19 root root  4096 Nov 28 10:00 ..
drwx------  2 root root 16384 Nov 28 10:35 lost+found
```

**lost+found:**
- Speciell mapp i ext4
- För journaling och återhämtning
- Används vid filsystem-krasch
- Mer pålitligt: Ha backups och RAID!

### Skapa Filer på Krypterad Volym

```bash
sudo touch /mnt/my-secret-encrypted-file
```

```bash
ls -l /mnt
```

**Output:**
```
drwx------  2 root root 16384 Nov 28 10:35 lost+found
-rw-r--r--  1 root root     0 Nov 28 10:40 my-secret-encrypted-file
```

**Innehåll i fil:**
```bash
echo "This is secret!" | sudo tee /mnt/my-secret-encrypted-file
cat /mnt/my-secret-encrypted-file
```

**Output:**
```
This is secret!
```

### Filen är Inte Krypterad?

**Viktigt att förstå:**
- Filen på disk ÄR krypterad (nollor och ettor)
- Kryptering/dekryptering sker transparent vid läs/skriv
- När volymen är "öppen" (monterad) → data tillgänglig
- När volymen är "stängd" (krypterad) → data otillgänglig

**Visualisering:**
```
DISK (fysiskt):
[Krypterade nollor och ettor - ej läsbart]

↓ cryptsetup open (med lösenord)

RAM (dekrypterat):
[This is secret! - läsbart]
```

### df - Disk Free

**Visa monterade filsystem:**
```bash
df -h
```

**Output:**
```
Filesystem              Size  Used Avail Use% Mounted on
/dev/mapper/cryptodisk  5.0G   24M  4.7G   1% /mnt
/dev/sda2                24G  5.5G  17G  25% /
```

**Förklaring:**
- `-h` = Human-readable (GB, MB istället för bytes)
- Visar bara monterade filsystem
- Krypterad disk visas när monterad

### Unmount

**Kommando:**
```bash
sudo umount /mnt
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME          MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sdb             8:16   0    5G  0 disk
└─sdb1          8:17   0    5G  0 part
  └─cryptodisk 253:0    0    5G  0 crypt
```

Mount point borta! Men `cryptodisk` finns kvar (öppen).

```bash
ls /mnt
```

**Output:**
```
(tom eller ursprungligt innehåll)
```

### Mount "Tar Över" en Mapp

**Koncept:**

```bash
# Skapa fil i /mnt (inte monterad)
sudo touch /mnt/myfile
ls /mnt
# Output: myfile

# Montera cryptodisk på /mnt
sudo mount /dev/mapper/cryptodisk /mnt
ls /mnt
# Output: lost+found  my-secret-encrypted-file
# myfile är "gömd"

# Unmount
sudo umount /mnt
ls /mnt
# Output: myfile
# myfile tillbaka!
```

**Analogi - Heltäckningsmatta:**
- Stengolv = `/mnt/myfile`
- Matta = Monterad volym
- Mattan täcker golvet temporärt
- Ta bort mattan → golvet synligt igen

### Stänga Krypterad Volym

**Fel ordning (fails):**
```bash
sudo cryptsetup close cryptodisk
# Error: Device cryptodisk is still in use
```

**Rätt ordning:**
```bash
# 1. Unmount först
sudo umount /mnt

# 2. Stäng krypterad volym
sudo cryptsetup close cryptodisk
```

**Verifiera:**
```bash
lsblk
```

**Output:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb      8:16   0    5G  0 disk
└─sdb1   8:17   0    5G  0 part
```

`cryptodisk` borta! Volymen är nu krypterad och ej tillgänglig. ✅

---

## 📋 Obligatorisk Assignment

### Uppgiftsbeskrivning

**Skapa ett automatiskt backup-system:**

1. **Backup-verktyg:** Restic
2. **Källa:** Ubuntu VM (hemmamapp eller del av)
3. **Destination:** Fedora VM (eller tvärtom)
4. **Automation:** systemd timer + service
5. **Trigger:** 5 minuter efter boot
6. **Inlämning:** Git repo på `git.chasslab.dev`

### Komponenter

**1. Systemd Service**
- Kör restic backup
- Definierar vad som ska köras

**2. Systemd Timer**
- Triggar service
- 5 minuter efter boot
- `OnBootSec=5min`

**3. Restic**
- Backup-verktyg
- Inkrementella backups
- Kryptering
- Deduplicering

### GitLab - git.chasslab.dev

**Registrera dig:**
1. Gå till: https://git.chasslab.dev
2. Registrera med **@chassutbildning.se** email
3. Vänta på godkännande (1 arbetsdag)

**Skapa repo:**
1. New Project
2. Project name: `linux-backup` (eller valfritt)
3. Private eller Public (din val)
4. Create project

**Innehåll i repo:**
```
backup-system/
├── README.md              # Dokumentation
├── backup.service         # Systemd service-fil
├── backup.timer           # Systemd timer-fil
└── scripts/
    └── backup.sh          # Backup-script (om du vill)
```

### Inlämning

**Vad ska lämnas in:**
- ✅ Länk till Git repo på `git.chasslab.dev`

**Vad ska INTE lämnas in:**
- ❌ Dokument
- ❌ Text
- ❌ Zipfiler
- ❌ Screenshots

**Deadline:**
- Slutet av kursen
- Obligatoriskt för betyg
- Börja tidigt!

### Varför Detta är Viktigt

**Praktisk användning:**
- När ni får molnservrar kommer de resettas ibland
- Automatiska backups = ingen dataförlust
- Systemd automation = "set it and forget it"

**Lärande:**
- Systemd timers och services
- Backup-strategi
- Git för versionhantering
- Automation

---

## 💡 Viktiga Koncept

### Block Devices

**Vad är en Block Device?**
- Hanterar data i "block" (chunks)
- Random access (kan läsa vilken del som helst)
- Exempel: Hårddiskar, USB-stickor, SD-kort

**Identifiering:**
```bash
ls -l /dev/sdb
# brw-rw---- ... /dev/sdb
# ↑
# b = Block device
```

**Jämförelse:**
- Block device (`b`) - Hårddisk, USB
- Character device (`c`) - Keyboard, mouse
- Directory (`d`) - Mapp
- Regular file (`-`) - Vanlig fil

### Allt är en Fil

**Linux-filosofi:**
- Disk = Fil (`/dev/sdb`)
- Partition = Fil (`/dev/sdb1`)
- Krypterad volym = Fil (`/dev/mapper/cryptodisk`)

**Varför?**
- Enhetligt interface
- Samma kommandon för allt
- Flexibilitet

### Kryptering - Software vs Hardware

**Software Encryption (LUKS):**
- Kryptering sker i OS
- Data på disk: Alltid krypterad
- Data i minne: Dekrypterad
- Minimal overhead

**När är data säker?**
- ✅ Disk stulen (utan lösenord)
- ✅ Dator avstängd
- ❌ Dator på och volym öppen
- ❌ Någon har lösenordet

### Sync - Säkerställ Skrivningar

**Problem:**
- Skrivningar kan cachas (köas)
- USB bortkopplad innan skrivet = korrupt data

**Lösning:**
```bash
sudo sync
```

**Vad gör sync?**
- Tvingar alla cachade skrivningar att slutföras
- Säkerställer att data är på disk
- Bra innan unmount eller bortkoppling

**Bästa praxis:**
```bash
# 1. Synka cachade skrivningar
sudo sync

# 2. Unmount
sudo umount /mnt

# 3. Säkert att koppla bort
```

### Lost+Found

**Vad är lost+found?**
- Speciell mapp i ext4 (journaled filesystem)
- Återhämtning vid filsystem-krasch
- Innehåller "hittade" filer vid fsck

**Pålitlighet:**
- ⚠️ Inte 100% pålitlig
- ✅ Bättre: Regelbundna backups
- ✅ Bättre: RAID för redundans

---

## 📖 Kommandoreferens

### Disk Management

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `lsblk` | Lista block devices | `lsblk` |
| `fdisk` | Partitionera disk | `sudo fdisk /dev/sdb` |
| `parted` | Alternativ till fdisk | `sudo parted /dev/sdb` |

### Kryptering

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `cryptsetup luksFormat` | Kryptera partition | `sudo cryptsetup luksFormat /dev/sdb1` |
| `cryptsetup open` | Öppna krypterad volym | `sudo cryptsetup open /dev/sdb1 name` |
| `cryptsetup close` | Stäng krypterad volym | `sudo cryptsetup close name` |
| `cryptsetup status` | Visa status | `sudo cryptsetup status name` |

### Filsystem

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `mkfs.ext4` | Skapa ext4-filsystem | `sudo mkfs.ext4 /dev/sdb1` |
| `mkfs.xfs` | Skapa xfs-filsystem | `sudo mkfs.xfs /dev/sdb1` |
| `mkfs.fat` | Skapa FAT-filsystem | `sudo mkfs.fat -F 32 /dev/sdb1` |

### Mount

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `mount` | Montera filsystem | `sudo mount /dev/sdb1 /mnt` |
| `umount` | Avmontera filsystem | `sudo umount /mnt` |
| `df` | Visa monterade filsystem | `df -h` |
| `sync` | Synka cachade skrivningar | `sudo sync` |

---

## 🎓 Steg-för-Steg Sammanfattning

### Komplett Process

**1. Lägg till disk i VirtualBox**
```
VirtualBox → Settings → Storage → Add Disk (5 GB)
```

**2. Verifiera disk**
```bash
lsblk
# Hitta ny disk (t.ex. sdb)
```

**3. Partitionera**
```bash
sudo fdisk /dev/sdb
# g (GPT table)
# n (new partition, alla defaults)
# w (write)
```

**4. Kryptera partition**
```bash
sudo cryptsetup luksFormat /dev/sdb1
# Skriv YES
# Ange lösenord (2 gånger)
```

**5. Öppna krypterad volym**
```bash
sudo cryptsetup open /dev/sdb1 cryptodisk
# Ange lösenord
```

**6. Skapa filsystem**
```bash
sudo mkfs.ext4 /dev/mapper/cryptodisk
```

**7. Montera**
```bash
sudo mount /dev/mapper/cryptodisk /mnt
```

**8. Använd**
```bash
cd /mnt
sudo touch secret-file
echo "Secret data" | sudo tee secret-file
```

**9. Avmontera (när klar)**
```bash
sudo umount /mnt
sudo cryptsetup close cryptodisk
```

---

## ⚠️ Säkerhetsvarningar

### Kritiska Punkter

**1. Rätt Disk/Partition**
```bash
# ✅ RÄTT
sudo fdisk /dev/sdb  # Ny disk

# ❌ FEL
sudo fdisk /dev/sda  # Root disk - FÖRSTÖR SYSTEMET!
```

**Alltid dubbelkolla med:**
```bash
lsblk
# Hitta rätt disk INNAN du kör kommandon
```

**2. Lösenord för LUKS**
- ❌ Finns INGET sätt att återställa
- ✅ Spara i lösenordshanterare
- ✅ Välj något du kommer ihåg
- ⚠️ Förlorat lösenord = förlorad data

**3. Unmount Innan Close**
```bash
# ✅ RÄTT ordning
sudo umount /mnt
sudo cryptsetup close cryptodisk

# ❌ FEL ordning
sudo cryptsetup close cryptodisk  # Fails!
sudo umount /mnt
```

**4. Sync Innan Unmount**
```bash
# ✅ SÄKERT
sudo sync
sudo umount /mnt

# ❌ RISKABELT
sudo umount /mnt  # Cachad data kan förloras
```

---

## 🎯 Sammanfattning

### Vad Vi Lärde Oss

1. ✅ Hierarkin: Disk → Partition → Encryption → Filesystem → Mount
2. ✅ Lägga till virtuella diskar i VirtualBox
3. ✅ Partitionera med fdisk
4. ✅ Kryptera med LUKS (cryptsetup)
5. ✅ Skapa filsystem (mkfs.ext4)
6. ✅ Montera och avmontera
7. ✅ Förstå mount points och hur de fungerar

### Nyckelpunkter

**Ordningen är Viktig:**
1. Device först
2. Partition på device
3. Kryptering på partition (valfritt)
4. Filsystem på kryptering/partition
5. Mount för att göra tillgängligt

**Säkerhet:**
- LUKS krypterar data på disk
- Lösenord MÅSTE kommas ihåg
- Data säker när volym stängd
- Data tillgänglig när volym öppen

**Mount Points:**
- `/mnt` - Manuella mounts
- `/media` - Automatiska mounts (USB, CD)
- Mount "tar över" en mapp temporärt

### Praktisk Tillämpning

**Assignment:**
- Automatisk backup med restic
- Systemd timer (5 min efter boot)
- Systemd service (kör backup)
- Git repo på git.chasslab.dev

**Varför Viktigt:**
- Backups = Ingen dataförlust
- Automation = Mindre manuellt arbete
- Systemd = Standard i Linux

### Nästa Steg

1. 📝 Registrera på git.chasslab.dev
2. 🔧 Börja planera backup-system
3. 📖 Läs man pages:
   - `man cryptsetup`
   - `man mount`
   - `man lsblk`
   - `man fdisk`
4. 🎯 Börja med assignment (deadline: kursslutet)

---

## 📚 Man Pages att Läsa

**Disk & Partition:**
```bash
man lsblk
man fdisk
man parted
```

**Kryptering:**
```bash
man cryptsetup
man cryptsetup-luksFormat
```

**Filsystem:**
```bash
man mkfs
man mkfs.ext4
man mount
man umount
```

**Övrigt:**
```bash
man df
man sync
```

---

**Lycka till med disk management och kryptering! 🔐**

*Allt är en fil - även dina hemligheter (när de är krypterade)!*

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
