# Linux Pakethantering & SSH-nycklar

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

⚠️ **Dela ALDRIG din privata nyckel!**

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
