"""
Tentaplugg Linux — 25 noder för komplett tentaförberedelse (MERGAD VERSION)
DOE25 Linux/Unix Server samt Bash Programmering | Tenta 7 januari 2026

STRUKTUR:
- MODUL 0: Linux Grunder (2 noder - från original)
- MODUL 1: BASH (11 noder - nya)
- MODUL 2: LINUX SYSTEM (8 noder - nya)
- MODUL 3: DEVOPS (4 noder - nya)
"""

# =============================================================================
# IMPORTS från individuella nod-filer
# =============================================================================

# MODUL 1: BASH
from .nod_bash_grunder import BASH_GRUNDER_NODE, BASH_GRUNDER_FLASHCARDS
from .nod_variabler_quoting import VARIABLER_QUOTING_NODE, VARIABLER_QUOTING_FLASHCARDS
from .nod_regex import REGEX_NODE, REGEX_FLASHCARDS
from .nod_sed import SED_NODE, SED_FLASHCARDS
from .nod_awk import AWK_NODE, AWK_FLASHCARDS
from .nod_villkor import VILLKOR_NODE, VILLKOR_FLASHCARDS
from .nod_interaktiva_skript import INTERAKTIVA_SKRIPT_NODE, INTERAKTIVA_SKRIPT_FLASHCARDS
from .nod_loopar import LOOPAR_NODE, LOOPAR_FLASHCARDS
from .nod_parametrar_arrays import PARAMETRAR_ARRAYS_NODE, PARAMETRAR_ARRAYS_FLASHCARDS
from .nod_funktioner import FUNKTIONER_NODE, FUNKTIONER_FLASHCARDS
from .nod_signals_traps import SIGNALS_TRAPS_NODE, SIGNALS_TRAPS_FLASHCARDS

# MODUL 2: LINUX SYSTEM
from .nod_users_groups import USERS_GROUPS_NODE, USERS_GROUPS_FLASHCARDS
from .nod_permissions import PERMISSIONS_NODE, PERMISSIONS_FLASHCARDS
from .nod_ssh_hardening import SSH_HARDENING_NODE, SSH_HARDENING_FLASHCARDS
from .nod_ufw import UFW_NODE, UFW_FLASHCARDS
from .nod_firewalld import FIREWALLD_NODE, FIREWALLD_FLASHCARDS
from .nod_lagring import LAGRING_NODE, LAGRING_FLASHCARDS
from .nod_backup_tar import BACKUP_TAR_NODE, BACKUP_TAR_FLASHCARDS
from .nod_systemd import SYSTEMD_NODE, SYSTEMD_FLASHCARDS

# MODUL 3: DEVOPS
from .nod_docker_grunder import DOCKER_GRUNDER_NODE, DOCKER_GRUNDER_FLASHCARDS
from .nod_docker_images import DOCKER_IMAGES_NODE, DOCKER_IMAGES_FLASHCARDS
from .nod_docker_compose import DOCKER_COMPOSE_NODE, DOCKER_COMPOSE_FLASHCARDS
from .nod_git_basics import GIT_BASICS_NODE, GIT_BASICS_FLASHCARDS


# =============================================================================
# MODUL 0: LINUX GRUNDER (från originalet)
# =============================================================================

SUBNETTING_NODE = {
    "title": "Subnetting & Nätverk",
    "slug": "subnetting-natverk",
    "description": "Förstå hur IP-adresser delas upp i nätverk - med lådmetoden som fungerar varje gång.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "order_index": 1,
    "content": r"""# Subnetting & Nätverk

> **TL;DR:** En IP-adress är som en postadress - en del säger vilken gata (nätverket), en del säger vilket hus (hosten). Subnetting handlar om att räkna ut var gränsen går.

---

## Varför behöver du kunna detta?

Tänk dig att du jobbar som DevOps och får i uppgift att sätta upp 50 servrar. Din chef säger:

*"Vi har fått nätverket 10.0.0.0/24. Dela upp det i 4 separata segment - ett för webservrar, ett för databaser, ett för monitoring och ett för backup."*

Utan subnetting-kunskaper stirrar du bara på skärmen. Med det kan du direkt säga:

- Webservrar: 10.0.0.0/26 (62 adresser)
- Databaser: 10.0.0.64/26 (62 adresser)
- Monitoring: 10.0.0.128/26 (62 adresser)
- Backup: 10.0.0.192/26 (62 adresser)

**Det kommer frågor på detta på tentan. Garanterat.**

---

## Den mentala modellen: Gatan och husnumret

Tänk på en IP-adress som en svensk postadress:

```
Kungsgatan 147, Stockholm
└─────────┘ └─┘
  GATA     HUS
```

En IP-adress fungerar likadant:

```
192.168.1.147/24
└───────┘ └─┘
 NÄTVERK  HOST
```

**/24 säger:** "De första 24 bitarna är gatunamnet, resten är husnumret."

Alla på samma gata (nätverk) kan prata med varandra direkt. För att nå en annan gata behöver du en router (som en buss mellan stadsdelar).

---

## Lådmetoden - din bästa vän på tentan

Istället för att räkna med binära tal i huvudet, använder vi **lådor**. Varje oktett (de fyra talen i en IP) har 8 lådor:

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
└─────┴────┴────┴────┴───┴───┴───┴───┘
```

> **Tips:** Memorera dessa värden - 128, 64, 32, 16, 8, 4, 2, 1. De kommer ALLTID i denna ordning.

---

## Steg-för-steg: Räkna ut 46.84.126.147/28

Låt oss gå igenom ett helt exempel, långsamt.

### Steg 1: Hur många bitar till host?

```
32 - prefix = host-bitar
32 - 28 = 4 bitar till host
```

**Varför 32?** En IPv4-adress har alltid 32 bitar totalt.

### Steg 2: Rita upp lådorna och markera

Vi har 4 host-bitar, så vi markerar de **sista 4** lådorna som H (host):

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
├─────┼────┼────┼────┼───┼───┼───┼───┤
│  N  │ N  │ N  │ N  │ H │ H │ H │ H │
└─────┴────┴────┴────┴───┴───┴───┴───┘
         NÄTVERK      │    HOST
                      └─ gränsen!
```

**N** = Nätverksdelen (låst, identifierar nätverket)
**H** = Hostdelen (varierar, identifierar enheter)

### Steg 3: Konvertera 147 till lådorna

Vi ska fylla lådorna så summan blir 147:

```
147 = 128 + ?
147 - 128 = 19 kvar

19 = 16 + ?
19 - 16 = 3 kvar

3 = 2 + 1 ✓
```

Så vi sätter 1:or i lådorna 128, 16, 2 och 1:

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
├─────┼────┼────┼────┼───┼───┼───┼───┤
│  1  │ 0  │ 0  │ 1  │ 0 │ 0 │ 1 │ 1 │ = 147 ✓
└─────┴────┴────┴────┴───┴───┴───┴───┘
```

### Steg 4: Hitta Network ID

> **Viktigt:** Network ID = sätt alla host-bitar till 0

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
├─────┼────┼────┼────┼───┼───┼───┼───┤
│  1  │ 0  │ 0  │ 1  │ 0 │ 0 │ 0 │ 0 │  ← host-bitar nollade
└─────┴────┴────┴────┴───┴───┴───┴───┘
         BEHÅLL       │   NOLLAT

128 + 16 = 144
```

**Network ID = 46.84.126.144**

### Steg 5: Hitta Broadcast

> **Viktigt:** Broadcast = sätt alla host-bitar till 1

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
├─────┼────┼────┼────┼───┼───┼───┼───┤
│  1  │ 0  │ 0  │ 1  │ 1 │ 1 │ 1 │ 1 │  ← host-bitar maxade
└─────┴────┴────┴────┴───┴───┴───┴───┘
         BEHÅLL       │   ETTOR

128 + 16 + 8 + 4 + 2 + 1 = 159
```

**Broadcast = 46.84.126.159**

### Steg 6: First Host, Last Host, Next Subnet

Det här är enkelt när du har Network och Broadcast:

| Vad | Formel | Resultat |
|-----|--------|----------|
| First Host | Network + 1 | 144 + 1 = **145** |
| Last Host | Broadcast - 1 | 159 - 1 = **158** |
| Next Subnet | Broadcast + 1 | 159 + 1 = **160** |

> **Varför +1 och -1?** Network-adressen och Broadcast-adressen kan inte användas av enheter. Network ID identifierar nätverket själv, Broadcast används för att skicka till alla.

---

## Komplett svar för 46.84.126.147/28

| Fråga | Svar |
|-------|------|
| Network ID | 46.84.126.**144** |
| First Host | 46.84.126.**145** |
| Last Host | 46.84.126.**158** |
| Broadcast | 46.84.126.**159** |
| Next Subnet | 46.84.126.**160** |
| Antal hosts | 2^4 - 2 = **14** |

---

## Vanliga prefix - memorera detta!

| Prefix | Host-bitar | Adresser | Användbara hosts |
|--------|-----------|----------|------------------|
| /24 | 8 | 256 | 254 |
| /25 | 7 | 128 | 126 |
| /26 | 6 | 64 | 62 |
| /27 | 5 | 32 | 30 |
| /28 | 4 | 16 | 14 |
| /29 | 3 | 8 | 6 |
| /30 | 2 | 4 | 2 |

> **Tips:** /30 med bara 2 hosts används för punkt-till-punkt-länkar mellan routrar.

---

## Snabbreferens för tentan

```
1. Host-bitar = 32 - prefix
2. Rita lådorna: 128|64|32|16|8|4|2|1
3. Markera de sista X som H (host)
4. Network = nolla alla H
5. Broadcast = ettställ alla H
6. First = Network + 1
7. Last = Broadcast - 1
8. Hosts = 2^(host-bitar) - 2
```

---

## 🧠 FLASHCARDS

| Fråga | Svar |
|-------|------|
| Hur beräknas host-bitar? | 32 - prefix (t.ex. 32-28=4) |
| Lådmetoden - värdena? | 128, 64, 32, 16, 8, 4, 2, 1 |
| Network ID beräknas hur? | Nollställ alla host-bitar |
| Broadcast beräknas hur? | Ettställ alla host-bitar |
| First host? | Network ID + 1 |
| Last host? | Broadcast - 1 |
| Antal hosts formel? | 2^(host-bitar) - 2 |
| /24 ger hur många hosts? | 254 |
| /28 ger hur många hosts? | 14 |
| /30 används för? | Punkt-till-punkt-länkar |

""",
    "quiz": [
        {
            "question": "Vad är Network ID för 192.168.1.100/26?",
            "options": [
                "192.168.1.0",
                "192.168.1.64",
                "192.168.1.96",
                "192.168.1.128",
            ],
            "correct": 1,
            "explanation": "Med /26 har vi 6 host-bitar. 100 i binärt är 01100100. Nollställ de 6 sista bitarna: 01000000 = 64.",
        },
        {
            "question": "Hur många hosts ryms i ett /28-nätverk?",
            "options": ["16", "14", "30", "62"],
            "correct": 1,
            "explanation": "2^(32-28) - 2 = 2^4 - 2 = 16 - 2 = 14 hosts.",
        },
        {
            "question": "Vad är Broadcast-adressen för 10.0.0.50/29?",
            "options": ["10.0.0.55", "10.0.0.63", "10.0.0.48", "10.0.0.56"],
            "correct": 0,
            "explanation": "/29 ger 3 host-bitar. Network är 10.0.0.48, Broadcast är 10.0.0.55 (alla host-bitar = 1).",
        },
        {
            "question": "Hur beräknas antal host-bitar?",
            "options": [
                "32 + prefix",
                "32 - prefix",
                "prefix - 32",
                "prefix / 4"
            ],
            "correct": 1,
            "explanation": "Host-bitar = 32 - prefix. För /28: 32 - 28 = 4 host-bitar."
        },
        {
            "question": "Vad är First Host för nätverket 172.16.0.0/24?",
            "options": [
                "172.16.0.0",
                "172.16.0.1",
                "172.16.0.254",
                "172.16.0.255"
            ],
            "correct": 1,
            "explanation": "First Host = Network ID + 1. Network ID är 172.16.0.0, så First Host = 172.16.0.1."
        },
        {
            "question": "Vilken typ av adress är 192.168.1.255 i ett /24-nätverk?",
            "options": [
                "Network ID",
                "First Host",
                "Last Host",
                "Broadcast"
            ],
            "correct": 3,
            "explanation": "I ett /24-nätverk är .255 alltid broadcast-adressen (alla host-bitar = 1)."
        },
        {
            "question": "Hur många användbara hosts finns i ett /30-nätverk?",
            "options": [
                "4",
                "2",
                "6",
                "0"
            ],
            "correct": 1,
            "explanation": "2^2 - 2 = 4 - 2 = 2 hosts. /30 används för punkt-till-punkt-länkar."
        },
        {
            "question": "Vad är lådmetodens värden i ordning?",
            "options": [
                "1, 2, 4, 8, 16, 32, 64, 128",
                "128, 64, 32, 16, 8, 4, 2, 1",
                "256, 128, 64, 32, 16, 8, 4, 2",
                "64, 32, 16, 8, 4, 2, 1, 0"
            ],
            "correct": 1,
            "explanation": "Lådmetodens värden är 128, 64, 32, 16, 8, 4, 2, 1 - från MSB till LSB."
        },
        {
            "question": "Om Network ID är 10.0.0.64 och Broadcast är 10.0.0.127, vad är Last Host?",
            "options": [
                "10.0.0.64",
                "10.0.0.65",
                "10.0.0.126",
                "10.0.0.127"
            ],
            "correct": 2,
            "explanation": "Last Host = Broadcast - 1. 10.0.0.127 - 1 = 10.0.0.126."
        },
        {
            "question": "Varför subtraherar man 2 från 2^host-bitar för att få antal hosts?",
            "options": [
                "För att Router tar 2 adresser",
                "Network ID och Broadcast kan inte användas av hosts",
                "DNS kräver 2 adresser",
                "Det är bara en konvention"
            ],
            "correct": 1,
            "explanation": "Network ID (alla host-bitar = 0) och Broadcast (alla host-bitar = 1) kan inte tilldelas hosts."
        },
    ],
}

FILSYSTEM_NODE = {
    "title": "Filsystem & Grundkommandon",
    "slug": "filsystem-grundkommandon",
    "description": "Linux filsystemstruktur, navigering, filhantering och sökning.",
    "difficulty": "easy",
    "estimated_minutes": 40,
    "xp_reward": 100,
    "order_index": 2,
    "content": r"""# Filsystem & Grundkommandon

> **TL;DR:** Linux-filsystemet är som ett upp-och-ner-träd med `/` som rot. Lär dig var saker ligger, så hittar du config-filer och loggar utan att googla varje gång.

---

## Mental modell: Filsystemet är ett träd

Tänk på ett upp-och-ner-träd:

```
                    /  (roten - allt börjar här)
                    │
    ┌───────┬───────┼───────┬───────┐
    │       │       │       │       │
   etc     var     home    opt     tmp
    │       │       │
 config   loggar  användare
```

---

## De viktiga mapparna

### `/etc` - Configuration Central

```bash
/etc/passwd          # Alla användare (INTE lösenord!)
/etc/shadow          # Krypterade lösenord (bara root)
/etc/ssh/sshd_config # SSH-serverns config
/etc/nginx/          # Nginx config
/etc/hosts           # Lokal DNS-override
```

### `/var` - Saker som ändras

```bash
/var/log/            # ALLA loggar
/var/log/syslog      # Systemloggen
/var/log/auth.log    # Inloggningsförsök
/var/www/            # Webbserver-filer
```

### `/home` - Användarnas grejer

```bash
/home/anna/          # Annas hem
/home/anna/.bashrc   # Annas shell-config
/home/anna/.ssh/     # Annas SSH-nycklar
```

### `/tmp` - Tillfälligt

```bash
/tmp/                # Rensas vid omstart!
```

---

## Navigering

```bash
pwd                  # Var är jag?
cd /var/log          # Gå till specifik plats
cd ..                # Upp en nivå
cd ~                 # Hem
cd -                 # Tillbaka till förra katalogen
```

---

## Lista filer: ls

```bash
ls                   # Bara namn
ls -l                # Long - alla detaljer
ls -a                # Visa dolda (börjar med .)
ls -la               # Kombinera!
ls -lh               # Human readable
ls -lt               # Sorterat efter tid
```

---

## Skapa, kopiera, flytta, ta bort

```bash
touch fil.txt        # Skapa tom fil
mkdir katalog        # Skapa katalog
mkdir -p a/b/c       # Skapa hela kedjan

cp fil.txt kopia.txt       # Kopiera fil
cp -r katalog/ backup/     # Kopiera katalog (MÅSTE ha -r!)

mv gammal.txt ny.txt       # Byt namn / flytta

rm fil.txt                 # Ta bort fil
rm -r katalog/             # Ta bort katalog med innehåll
```

---

## Sökning: find och grep

### find - hitta FILER

```bash
find /var/log -name "*.log"          # Alla .log-filer
find /home -type d -name "config"    # Kataloger som heter config
find /tmp -size +100M                # Filer större än 100MB
```

### grep - sök I filer

```bash
grep "error" /var/log/syslog         # Hitta "error" i filen
grep -r "password" /etc/             # Sök rekursivt
grep -i "error" fil.txt              # Case-insensitive
grep -n "error" fil.txt              # Visa radnummer
grep -v "debug" fil.txt              # Visa allt UTOM "debug"
```

---

## Pipes och redirection

```bash
cat fil | grep "error" | head -20    # Kedja kommandon

echo "text" > fil.txt    # Skriv (SKRIVER ÖVER!)
echo "mer" >> fil.txt    # Lägg till
kommando 2> error.log    # Spara bara errors
kommando &> allt.log     # Spara allt
```

---

## Läsa filer

```bash
cat fil.txt              # Visa allt
head -20 fil.txt         # Första 20 raderna
tail -20 fil.txt         # Sista 20 raderna
tail -f /var/log/syslog  # FÖLJ filen live
less fil.txt             # Bläddra
```

---

## Arkivering med tar

```bash
# SKAPA arkiv
tar -cvf backup.tar katalog/
tar -czvf backup.tar.gz katalog/    # Med gzip

# EXTRAHERA
tar -xvf backup.tar
tar -xzvf backup.tar.gz

# VISA innehåll
tar -tvf backup.tar
```

---

## Diskutrymme

```bash
df -h                    # Visa partitioner
du -sh /var/log          # Hur stor är mappen?
du -sh *                 # Storlek på allt i katalogen
```

---

## 🧠 FLASHCARDS

| Fråga | Svar |
|-------|------|
| /etc innehåller? | Konfigurationsfiler |
| /var/log innehåller? | Loggfiler |
| /home innehåller? | Användarnas hemkataloger |
| Kopiera katalog? | cp -r källa/ mål/ |
| Hitta filer? | find /path -name "*.txt" |
| Sök i filer? | grep "text" fil |
| Sök rekursivt? | grep -r "text" /path/ |
| Följ logg live? | tail -f /var/log/syslog |
| Skapa backup? | tar -czvf backup.tar.gz /path/ |
| Kolla diskutrymme? | df -h |

""",
    "quiz": [
        {
            "question": "Vilket kommando kopierar en katalog rekursivt?",
            "options": [
                "cp katalog/ backup/",
                "cp -r katalog/ backup/",
                "mv katalog/ backup/",
                "copy -r katalog/ backup/",
            ],
            "correct": 1,
            "explanation": "cp -r (recursive) krävs för att kopiera kataloger med innehåll.",
        },
        {
            "question": "Vad gör kommandot 'tail -f /var/log/syslog'?",
            "options": [
                "Visar första 10 raderna",
                "Visar sista 10 raderna",
                "Följer filen i realtid",
                "Filtrerar loggen",
            ],
            "correct": 2,
            "explanation": "tail -f (follow) visar nya rader i realtid - perfekt för att övervaka loggar.",
        },
        {
            "question": "Vad betyder 'grep -v' flaggan?",
            "options": [
                "Verbose output",
                "Visa radnummer",
                "Invertera matchning (visa EJ matchande)",
                "Case insensitive",
            ],
            "correct": 2,
            "explanation": "grep -v inverterar matchningen och visar rader som INTE matchar mönstret.",
        },
        {
            "question": "Vilken katalog innehåller systemkonfigurationer?",
            "options": [
                "/var",
                "/etc",
                "/home",
                "/opt"
            ],
            "correct": 1,
            "explanation": "/etc (etcetera) innehåller systemkonfigurationer som passwd, shadow, nginx etc."
        },
        {
            "question": "Vad gör kommandot 'mkdir -p a/b/c'?",
            "options": [
                "Skapar bara katalogen c",
                "Skapar hela katalogkedjan a/b/c",
                "Flyttar kataloger",
                "Ger fel om a inte finns"
            ],
            "correct": 1,
            "explanation": "-p (parents) skapar alla överliggande kataloger som behövs."
        },
        {
            "question": "Vad är skillnaden mellan > och >>?",
            "options": [
                "Ingen skillnad",
                "> skriver över, >> lägger till",
                ">> skriver över, > lägger till",
                "> är för filer, >> är för kataloger"
            ],
            "correct": 1,
            "explanation": "> skriver över filen (truncate), >> lägger till i slutet (append)."
        },
        {
            "question": "Hur hittar du alla .log-filer i /var?",
            "options": [
                "grep -r '*.log' /var",
                "find /var -name '*.log'",
                "ls /var/*.log",
                "search /var -type log"
            ],
            "correct": 1,
            "explanation": "find med -name söker filer baserat på namn, stödjer wildcards."
        },
        {
            "question": "Vad visar 'df -h'?",
            "options": [
                "Filstorleka",
                "Diskpartitioner och ledigt utrymme",
                "Kataloginnehåll",
                "Dolda filer"
            ],
            "correct": 1,
            "explanation": "df (disk free) visar filsystem och deras användning. -h gör det human readable."
        },
        {
            "question": "Hur visar du dolda filer med ls?",
            "options": [
                "ls -h",
                "ls -l",
                "ls -a",
                "ls -d"
            ],
            "correct": 2,
            "explanation": "-a (all) visar alla filer inklusive dolda (de som börjar med .)"
        },
        {
            "question": "Vad gör 'tar -czvf backup.tar.gz /data'?",
            "options": [
                "Extraherar backup.tar.gz till /data",
                "Skapar gzip-komprimerad backup av /data",
                "Listar innehållet i backup.tar.gz",
                "Tar bort /data"
            ],
            "correct": 1,
            "explanation": "c=create, z=gzip, v=verbose, f=file. Skapar komprimerad backup."
        },
    ],
}

SUBNETTING_FLASHCARDS = [
    {"front": "Hur beräknas host-bitar?", "back": "32 - prefix (t.ex. 32-28=4)"},
    {"front": "Lådmetoden - värdena?", "back": "128, 64, 32, 16, 8, 4, 2, 1"},
    {"front": "Network ID beräknas hur?", "back": "Nollställ alla host-bitar"},
    {"front": "Broadcast beräknas hur?", "back": "Ettställ alla host-bitar"},
    {"front": "First host formel?", "back": "Network ID + 1"},
    {"front": "Last host formel?", "back": "Broadcast - 1"},
    {"front": "Antal hosts formel?", "back": "2^(host-bitar) - 2"},
    {"front": "/24 ger hur många hosts?", "back": "254 hosts"},
    {"front": "/28 ger hur många hosts?", "back": "14 hosts"},
    {"front": "/30 används för?", "back": "Punkt-till-punkt-länkar (2 hosts)"},
]

FILSYSTEM_FLASHCARDS = [
    {"front": "/etc innehåller?", "back": "Konfigurationsfiler"},
    {"front": "/var/log innehåller?", "back": "Loggfiler"},
    {"front": "/home innehåller?", "back": "Användarnas hemkataloger"},
    {"front": "/tmp rensas när?", "back": "Vid omstart"},
    {"front": "Kopiera katalog?", "back": "cp -r källa/ mål/"},
    {"front": "Hitta filer?", "back": "find /path -name '*.txt'"},
    {"front": "Sök i fil?", "back": "grep 'text' fil"},
    {"front": "Sök rekursivt?", "back": "grep -r 'text' /path/"},
    {"front": "Följ logg live?", "back": "tail -f /var/log/syslog"},
    {"front": "Skapa tar.gz backup?", "back": "tar -czvf backup.tar.gz /path/"},
]


# =============================================================================
# BYGG MODULEN
# =============================================================================

def _update_order_index(node, index):
    """Uppdatera order_index för en nod"""
    node_copy = node.copy()
    node_copy["order_index"] = index
    return node_copy


MODULE = {
    "id": "tentaplugg-linux",
    "slug": "tentaplugg-linux",
    "title": "Tentaplugg Linux",
    "description": "Komplett tentaförberedelse för DOE25 Linux - 25 noder i 4 moduler: Linux Grunder, Bash, Linux System och DevOps. Allt du behöver för att klara tentan!",
    "icon": "🎯",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "order_index": 2,
    "tasks": [
        # =====================================================================
        # MODUL 0: LINUX GRUNDER (2 noder)
        # =====================================================================
        _update_order_index(SUBNETTING_NODE, 1),
        _update_order_index(FILSYSTEM_NODE, 2),
        
        # =====================================================================
        # MODUL 1: BASH (11 noder)
        # =====================================================================
        _update_order_index(BASH_GRUNDER_NODE, 3),
        _update_order_index(VARIABLER_QUOTING_NODE, 4),
        _update_order_index(REGEX_NODE, 5),
        _update_order_index(SED_NODE, 6),
        _update_order_index(AWK_NODE, 7),
        _update_order_index(VILLKOR_NODE, 8),
        _update_order_index(INTERAKTIVA_SKRIPT_NODE, 9),
        _update_order_index(LOOPAR_NODE, 10),
        _update_order_index(PARAMETRAR_ARRAYS_NODE, 11),
        _update_order_index(FUNKTIONER_NODE, 12),
        _update_order_index(SIGNALS_TRAPS_NODE, 13),
        
        # =====================================================================
        # MODUL 2: LINUX SYSTEM (8 noder)
        # =====================================================================
        _update_order_index(USERS_GROUPS_NODE, 14),
        _update_order_index(PERMISSIONS_NODE, 15),
        _update_order_index(SSH_HARDENING_NODE, 16),
        _update_order_index(UFW_NODE, 17),
        _update_order_index(FIREWALLD_NODE, 18),
        _update_order_index(LAGRING_NODE, 19),
        _update_order_index(BACKUP_TAR_NODE, 20),
        _update_order_index(SYSTEMD_NODE, 21),
        
        # =====================================================================
        # MODUL 3: DEVOPS (4 noder)
        # =====================================================================
        _update_order_index(DOCKER_GRUNDER_NODE, 22),
        _update_order_index(DOCKER_IMAGES_NODE, 23),
        _update_order_index(DOCKER_COMPOSE_NODE, 24),
        _update_order_index(GIT_BASICS_NODE, 25),
    ],
}


# =============================================================================
# SAMLA ALLA FLASHCARDS
# =============================================================================

ALL_FLASHCARDS = {
    # MODUL 0
    "subnetting-natverk": SUBNETTING_FLASHCARDS,
    "filsystem-grundkommandon": FILSYSTEM_FLASHCARDS,
    
    # MODUL 1: BASH
    "bash-grunder-shebang": BASH_GRUNDER_FLASHCARDS,
    "variabler-quoting-expansions": VARIABLER_QUOTING_FLASHCARDS,
    "regular-expressions-regex": REGEX_FLASHCARDS,
    "sed-stream-editor": SED_FLASHCARDS,
    "awk-pattern-processing": AWK_FLASHCARDS,
    "villkor-if-elif-else-case": VILLKOR_FLASHCARDS,
    "interaktiva-skript-read-validering": INTERAKTIVA_SKRIPT_FLASHCARDS,
    "loopar-for-while-until": LOOPAR_FLASHCARDS,
    "parametrar-arrays": PARAMETRAR_ARRAYS_FLASHCARDS,
    "funktioner-scope": FUNKTIONER_FLASHCARDS,
    "signals-traps": SIGNALS_TRAPS_FLASHCARDS,
    
    # MODUL 2: LINUX SYSTEM
    "users-groups": USERS_GROUPS_FLASHCARDS,
    "permissions-chmod-chown": PERMISSIONS_FLASHCARDS,
    "ssh-hardening": SSH_HARDENING_FLASHCARDS,
    "ufw-firewall": UFW_FLASHCARDS,
    "firewalld": FIREWALLD_FLASHCARDS,
    "lagring-partitioner-lvm": LAGRING_FLASHCARDS,
    "backup-tar-rsync": BACKUP_TAR_FLASHCARDS,
    "systemd-services": SYSTEMD_FLASHCARDS,
    
    # MODUL 3: DEVOPS
    "docker-grunder": DOCKER_GRUNDER_FLASHCARDS,
    "docker-images-dockerfile": DOCKER_IMAGES_FLASHCARDS,
    "docker-compose": DOCKER_COMPOSE_FLASHCARDS,
    "git-basics": GIT_BASICS_FLASHCARDS,
}


# =============================================================================
# EXPORTERA
# =============================================================================

__all__ = ["MODULE", "ALL_FLASHCARDS"]
