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
from .nod_bash_grunder import BASH_GRUNDER_NODE
from .nod_variabler_quoting import VARIABLER_QUOTING_NODE
from .nod_regex import REGEX_NODE
from .nod_sed import SED_NODE
from .nod_awk import AWK_NODE
from .nod_villkor import VILLKOR_NODE
from .nod_interaktiva_skript import INTERAKTIVA_SKRIPT_NODE
from .nod_loopar import LOOPAR_NODE
from .nod_parametrar_arrays import PARAMETRAR_ARRAYS_NODE
from .nod_funktioner import FUNKTIONER_NODE
from .nod_signals_traps import SIGNALS_TRAPS_NODE

# MODUL 2: LINUX SYSTEM
from .nod_users_groups import USERS_GROUPS_NODE
from .nod_permissions import PERMISSIONS_NODE
from .nod_ssh_hardening import SSH_HARDENING_NODE
from .nod_ufw import UFW_NODE
from .nod_firewalld import FIREWALLD_NODE
from .nod_lagring import LAGRING_NODE
from .nod_backup_tar import BACKUP_TAR_NODE
from .nod_systemd import SYSTEMD_NODE

# MODUL 3: DEVOPS
from .nod_docker_grunder import DOCKER_GRUNDER_NODE
from .nod_docker_images import DOCKER_IMAGES_NODE
from .nod_docker_compose import DOCKER_COMPOSE_NODE
from .nod_git_basics import GIT_BASICS_NODE


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

"""
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

"""
}




# =============================================================================
# BYGG MODULEN
# =============================================================================

def _update_order_index(node, index):
    """Uppdatera order_index för en nod"""
    node_copy = node.copy()
    node_copy["order_index"] = index
    return node_copy


MODULE = {
    "id": "doe25-tenta",
    "slug": "doe25-tenta",
    "title": "DOE25 Tentaplugg",
    "description": "Komplett tentaplugg med 25 tasks: Linux Grunder, Bash Scripting, System Administration & DevOps. Allt du behöver för att klara tentan!",
    "icon": "📝",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "order_index": 1,
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
# EXPORTERA
# =============================================================================

__all__ = ["MODULE"]
