"""
Tentaplugg Linux — 16 noder för komplett tentaförberedelse
DOE25 Linux/Unix Server samt Bash Programmering | Tenta 7 januari 2026
"""

MODULE = {
    "id": "tentaplugg-linux",
    "slug": "tentaplugg-linux",
    "title": "Tentaplugg Linux",
    "description": "Komplett tentaförberedelse för Linux - 16 moduler från subnetting till backup. Allt du behöver för att klara tentan med glans!",
    "icon": "🎯",
    "difficulty": "intermediate",
    "estimated_hours": 20,
    "order_index": 2,
    "tasks": [
        # =============================================================================
        # NOD 1: Subnetting & Nätverk
        # =============================================================================
        {
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

## Övning 1: Gör själv (med facit)

**Uppgift:** Räkna ut allt för **192.168.1.67/26**

Försök själv först, scrolla sedan ner för facit.

.

.

.

.

### Lösning:

**Steg 1:** Host-bitar = 32 - 26 = **6 bitar**

**Steg 2:** Lådor med 6 host-bitar markerade:

```
┌─────┬────┬────┬────┬───┬───┬───┬───┐
│ 128 │ 64 │ 32 │ 16 │ 8 │ 4 │ 2 │ 1 │
├─────┼────┼────┼────┼───┼───┼───┼───┤
│  N  │ N  │ H  │ H  │ H │ H │ H │ H │
└─────┴────┴────┴────┴───┴───┴───┴───┘
```

**Steg 3:** 67 i binärt:

```
67 = 64 + 2 + 1 = 01000011
```

**Steg 4:** Network ID (nolla host-bitar):

```
01 | 000000 → 01000000 = 64
```

**Steg 5:** Broadcast (maxa host-bitar):

```
01 | 111111 → 01111111 = 127
```

**Svar:**

| Fråga | Svar |
|-------|------|
| Network ID | 192.168.1.**64** |
| First Host | 192.168.1.**65** |
| Last Host | 192.168.1.**126** |
| Broadcast | 192.168.1.**127** |
| Antal hosts | 2^6 - 2 = **62** |

---

## Övning 2: Snabbfrågor

Utan att räkna i detalj - använd tabellen:

1. **/27 - hur många hosts?** → 30
2. **/24 - hur många hosts?** → 254
3. **192.168.0.0/24 - vad är broadcast?** → 192.168.0.255 (alla host-bitar = 1)

---

## Vanliga misstag på tentan

> **Varning:** Dessa fel kostar poäng varje år!

| Misstag | Problem | Rätt |
|---------|---------|------|
| Glömmer -2 | Skriver 16 hosts för /28 | 16 - 2 = **14** hosts |
| Fel oktett | Ändrar fel del av IP:n | Titta på var /XX landar |
| Blandar N och H | Nollar fel bitar | N = nätverket (behåll), H = host (ändra) |
| First = Network | Skriver .144 som first host | First = Network **+ 1** |

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
            ],
        },
        # =============================================================================
        # NOD 2: Filsystem & Grundkommandon
        # =============================================================================
        {
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

## Verkligt scenario: Din första dag som DevOps

Du har precis SSH:at in på en produktionsserver. Nginx ger 502-fel.

**Vad gör du?**

1. Kolla loggarna: `/var/log/nginx/error.log`
2. Kolla config: `/etc/nginx/nginx.conf`
3. Kolla om tjänsten kör: `systemctl status nginx`

Men hur visste du var filerna ligger? **Därför att Linux alltid organiserar saker på samma sätt.**

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

**Varför detta spelar roll:**
- Du behöver aldrig gissa var saker ligger
- Alla Linux-system fungerar likadant
- Felsökning blir systematiskt istället för slumpmässigt

---

## De viktiga mapparna - och VARFÖR

### `/etc` - "Configuration Central"

```bash
/etc/passwd          # Alla användare (INTE lösenord!)
/etc/shadow          # Krypterade lösenord (bara root)
/etc/ssh/sshd_config # SSH-serverns config
/etc/nginx/          # Nginx config
/etc/hosts           # Lokal DNS-override
```

**DevOps-användning:** Nästan all server-konfiguration ligger här.

### `/var` - "Saker som ändras"

```bash
/var/log/            # ALLA loggar
/var/log/syslog      # Systemloggen
/var/log/auth.log    # Inloggningsförsök
/var/www/            # Webbserver-filer
```

**DevOps-användning:** Hit går du vid felsökning. Alltid.

### `/home` - "Användarnas grejer"

```bash
/home/anna/          # Annas hem
/home/anna/.bashrc   # Annas shell-config
/home/anna/.ssh/     # Annas SSH-nycklar
```

**DevOps-användning:** Lägg INTE server-filer här. Använd `/opt` eller `/var/www`.

### `/tmp` - "Tillfälligt"

```bash
/tmp/                # Rensas vid omstart!
```

**DevOps-varning:** Lägg ALDRIG viktigt här. Det försvinner.

---

## Navigering - så du inte går vilse

### Grunderna

```bash
pwd                  # "Var är jag?" - Print Working Directory
cd /var/log          # Gå till specifik plats
cd ..                # Upp en nivå
cd ~                 # Hem (samma som cd /home/dittnamn)
cd -                 # Tillbaka till förra katalogen (supersmidigt!)
```

### Prova detta:

```bash
cd /var/log
pwd                  # /var/log
cd ..
pwd                  # /var
cd -
pwd                  # /var/log (!)
```

> **Tips:** `cd -` är som "undo" för navigering. Pendla mellan två mappar snabbt!

---

## Lista filer: `ls` med superkrafter

### Grundläggande

```bash
ls                   # Bara namn
ls -l                # "Long" - alla detaljer
ls -a                # Visa dolda (börjar med .)
ls -la               # Kombinera!
```

### Läsa `ls -l` output:

```
-rw-r--r-- 1 anna devops 4096 Dec 20 10:30 config.txt
│└──┬───┘    │     │      │        │         │
│   │        │     │      │        │         └─ Filnamn
│   │        │     │      │        └─ Datum
│   │        │     │      └─ Storlek (bytes)
│   │        │     └─ Grupp
│   │        └─ Ägare
│   └─ Permissions (mer om detta i Nod 5)
└─ Typ (- = fil, d = katalog, l = länk)
```

### Pro-tips:

```bash
ls -lh               # Human readable (4.0K istället för 4096)
ls -lt               # Sorterat efter tid (nyast först)
ls -lS               # Sorterat efter storlek (störst först)
```

---

## Skapa, kopiera, flytta, ta bort

### Skapa

```bash
touch fil.txt        # Skapa tom fil (eller uppdatera tidsstämpel)
mkdir katalog        # Skapa katalog
mkdir -p a/b/c       # Skapa hela kedjan om den inte finns
```

**Varför `-p`?** Utan den får du fel om `a/` inte finns.

### Kopiera

```bash
cp fil.txt kopia.txt       # Kopiera fil
cp -r katalog/ backup/     # Kopiera katalog (MÅSTE ha -r!)
```

> **Varning:** Utan `-r` kopieras bara själva katalog-entryn, inte innehållet!

### Flytta / Byt namn

```bash
mv gammal.txt ny.txt       # Byt namn
mv fil.txt /annan/plats/   # Flytta
```

**Notera:** `mv` gör båda - det finns inget separat "rename"-kommando.

### Ta bort

```bash
rm fil.txt                 # Ta bort fil
rm -r katalog/             # Ta bort katalog med innehåll
rm -rf katalog/            # Force (frågar ej) - FARLIGT!
```

> **Varning:** `rm -rf /` raderar HELA systemet. Dubbelkolla alltid path:en!

---

## Sökning: find och grep

### `find` - hitta FILER

**Mental modell:** "Leta i filskåpet efter en mapp med visst namn"

```bash
find /var/log -name "*.log"          # Alla .log-filer
find /home -type d -name "config"    # Kataloger som heter config
find /tmp -size +100M                # Filer större än 100MB
find /var -mtime -7                  # Ändrade senaste 7 dagarna
```

**Praktiskt exempel - rensa gamla loggar:**

```bash
find /var/log -name "*.log" -mtime +30 -delete
```

### `grep` - sök I filer

**Mental modell:** "Sök i en boks TEXT efter ett ord"

```bash
grep "error" /var/log/syslog         # Hitta "error" i filen
grep -r "password" /etc/             # Sök rekursivt i alla filer
grep -i "error" fil.txt              # Case-insensitive
grep -n "error" fil.txt              # Visa radnummer
grep -v "debug" fil.txt              # Visa allt UTOM "debug"
```

**Praktiskt exempel - hitta misslyckade inloggningar:**

```bash
grep "Failed password" /var/log/auth.log
```

---

## Pipes och redirection: Kombinera kommandon

### Pipes: Skicka output vidare

```
kommando1 | kommando2 | kommando3
    │           │           │
    └───────────┴───────────┘
    Output blir nästa kommandos input
```

**Exempel:**

```bash
cat /var/log/syslog | grep "error" | head -20
│                       │              │
│                       │              └─ Visa bara första 20
│                       └─ Filtrera på "error"
└─ Läs filen
```

### Redirection: Spara till fil

```bash
echo "text" > fil.txt    # Skriv (SKRIVER ÖVER!)
echo "mer" >> fil.txt    # Lägg till
kommando 2> error.log    # Spara bara errors
kommando &> allt.log     # Spara allt (stdout + stderr)
kommando > /dev/null     # Kasta output (tyst läge)
```

**Verkligt exempel - spara alla fel:**

```bash
./deploy.sh > deploy.log 2>&1
```

Detta sparar BÅDE vanlig output OCH fel till samma fil.

---

## Läsa filer: cat, head, tail, less

```bash
cat fil.txt              # Visa allt (dåligt för stora filer)
head -20 fil.txt         # Första 20 raderna
tail -20 fil.txt         # Sista 20 raderna
tail -f /var/log/syslog  # FÖLJ filen live (ctrl+c för att avsluta)
less fil.txt             # Bläddra (q=quit, /=sök, n=nästa träff)
```

> **Tips:** `tail -f` är DIN BÄSTA VÄN vid felsökning. Kör den i en terminal medan du testar i en annan!

---

## Arkivering med tar

### Minnesregel: **C**reate e**X**tract **T**able

```bash
# SKAPA arkiv
tar -cvf backup.tar katalog/        # Create Verbose File
tar -czvf backup.tar.gz katalog/    # Med gzip-komprimering

# EXTRAHERA
tar -xvf backup.tar                 # Extract
tar -xzvf backup.tar.gz             # Extrahera gzip
tar -xzvf backup.tar.gz -C /mål/    # Till specifik plats

# VISA innehåll (utan att extrahera)
tar -tvf backup.tar                 # Table (lista)
```

**Flaggorna:**
- `c` = Create
- `x` = eXtract
- `t` = Table (visa)
- `v` = Verbose
- `f` = File (måste vara sist före filnamn!)
- `z` = gzip

---

## Diskutrymme

```bash
df -h                    # Visa partitioner och hur fulla de är
du -sh /var/log          # Hur stor är denna mapp?
du -sh *                 # Storlek på allt i nuvarande katalog
```

**Praktiskt:** När disken är full, hitta bovarna:

```bash
du -sh /var/* | sort -h | tail -10
```

---

## Övning 1: Navigering och sökning

**Scenario:** Du ska hitta alla misslyckade SSH-inloggningar på en server.

**Uppgift:**
1. Vilken fil ska du söka i?
2. Skriv kommandot för att hitta rader med "Failed password"
3. Visa bara de 10 senaste

.

.

.

### Lösning:

```bash
# 1. Filen är /var/log/auth.log (på Debian/Ubuntu)
#    eller /var/log/secure (på CentOS/RHEL)

# 2-3. Kombinerat:
grep "Failed password" /var/log/auth.log | tail -10
```

---

## Övning 2: Backup och restore

**Scenario:** Du ska ta backup på `/etc/nginx/` innan du ändrar config.

**Uppgift:**
1. Skapa komprimerad backup med tidsstämpel
2. Lista innehållet utan att extrahera

.

.

.

### Lösning:

```bash
# 1. Skapa backup
tar -czvf nginx-backup-$(date +%Y%m%d).tar.gz /etc/nginx/

# 2. Verifiera innehåll
tar -tzvf nginx-backup-*.tar.gz
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `cp -r` glöms | Kopierar bara katalog-entry, inte innehåll | `cp -r katalog/ backup/` |
| `rm -rf /var/log` | Kan radera för mycket | `rm -rf /var/log/*.old` (var specifik) |
| Blandar `find` och `grep` | `find` hittar filer, `grep` söker i text | Välj rätt verktyg |
| `>` vs `>>` | `>` skriver över! | Använd `>>` för att lägga till |
| Glömmer `/` i path | `cd var` funkar bara om du är i `/` | `cd /var` med absolut path |

---

## Snabbreferens

| Behov | Kommando |
|-------|----------|
| Var är jag? | `pwd` |
| Lista med detaljer | `ls -lah` |
| Kopiera mapp | `cp -r källa/ mål/` |
| Hitta filer | `find /path -name "*.txt"` |
| Sök i filer | `grep "text" fil` |
| Sök rekursivt | `grep -r "text" /path/` |
| Följ logg live | `tail -f /var/log/syslog` |
| Skapa backup | `tar -czvf backup.tar.gz /path/` |
| Kolla diskutrymme | `df -h` |
| Mappstorlek | `du -sh /path/` |

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
                        "Invertera matchning",
                        "Case insensitive",
                    ],
                    "correct": 2,
                    "explanation": "grep -v inverterar matchningen och visar rader som INTE matchar mönstret.",
                },
            ],
        },
        # =============================================================================
        # NOD 3: Bash Scripting Grund
        # =============================================================================
        {
            "title": "Bash Scripting Grund",
            "slug": "bash-scripting-grund",
            "description": "Shebang, variabler, specialvariabler, if-satser och test-operatorer.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 120,
            "order_index": 3,
            "content": r"""# Bash Scripting Grund

> **TL;DR:** Bash-script är automatisering. Istället för att skriva samma 10 kommandon varje dag, skriv dem en gång i ett script och kör det med ett kommando.

---

## Verkligt scenario: Varför script?

Du deployer en app varje dag:

```bash
# Utan script - varje dag:
git pull
npm install
npm run build
pm2 restart app
echo "Deploy klar"
```

**Med script - en gång:**

```bash
./deploy.sh
```

**Det är hela poängen med scripting.**

---

## Shebang: Berätta för systemet VAD som ska köra scriptet

```bash
#!/bin/bash
```

**Vad gör den?** Den första raden säger: "Använd /bin/bash för att tolka detta script."

```
┌──────────────────────────────────────────┐
│  #!/bin/bash    ← "Shebang" (hash-bang)  │
│                                          │
│  # Utan den vet inte systemet vilken     │
│  # tolk som ska användas                 │
└──────────────────────────────────────────┘
```

**Varför det spelar roll:**

```bash
#!/bin/bash      # Bash (vanligast)
#!/bin/sh        # POSIX shell (mer portabelt)
#!/usr/bin/env python3   # Python
```

---

## Göra ett script körbart

```bash
# 1. Skapa filen
nano myscript.sh

# 2. Lägg till innehåll
#!/bin/bash
echo "Hej från mitt script!"

# 3. Gör den körbar
chmod +x myscript.sh

# 4. Kör den
./myscript.sh
```

> **Varning:** Utan `chmod +x` får du "Permission denied"!

---

## Variabler: Lagra värden

### Mental modell: Variabler är etiketter på lådor

```
┌─────────────────┐
│  name="Said"    │  ← Lådans etikett är "name"
│                 │     Innehållet är "Said"
└─────────────────┘
```

### Grundregler

```bash
# RÄTT - inget mellanslag runt =
name="Said"
age=25
server="192.168.1.10"

# FEL - bash tolkar det som kommando + argument
name = "Said"    # ❌ Error: "name: command not found"
```

> **Varning:** INGEN MELLANSLAG runt `=` - detta är den vanligaste nybörjarfeltan!

### Använda variabler

```bash
name="Said"

# Tre sätt (alla funkar)
echo $name           # Said
echo ${name}         # Said (tydligare, rekommenderat)
echo "Hej $name!"    # Hej Said!

# När ${} är NÖDVÄNDIGT:
path="/home"
echo "${path}_backup"    # /home_backup
echo "$path_backup"      # Tom! (letar efter variabeln path_backup)
```

---

## Specialvariabler: Script-argument

**Verkligt scenario:** Du vill skapa ett backup-script som tar filnamn som argument:

```bash
./backup.sh config.txt
```

Hur kommer ditt script åt "config.txt"? **Specialvariabler!**

```bash
#!/bin/bash
# backup.sh

echo "Script: $0"        # backup.sh
echo "Fil att backa: $1" # config.txt
echo "Antal argument: $#" # 1
```

### Alla specialvariabler

```
┌──────┬────────────────────────────────────────────┐
│ $0   │ Scriptets namn                             │
├──────┼────────────────────────────────────────────┤
│ $1   │ Första argumentet                          │
│ $2   │ Andra argumentet                           │
│ $3   │ ... och så vidare                          │
├──────┼────────────────────────────────────────────┤
│ $#   │ ANTAL argument (utan $0)                   │
├──────┼────────────────────────────────────────────┤
│ $@   │ ALLA argument som separata ord             │
│ $*   │ ALLA argument som en enda sträng           │
├──────┼────────────────────────────────────────────┤
│ $?   │ Exit-status från förra kommandot           │
│ $$   │ Scriptets process-ID (PID)                 │
└──────┴────────────────────────────────────────────┘
```

**Exempel med flera argument:**

```bash
./script.sh apple banana cherry

# I scriptet:
# $1 = apple
# $2 = banana
# $3 = cherry
# $# = 3
# $@ = apple banana cherry
```

---

## Exit Status: Hur script pratar med omvärlden

**Koncept:** Varje kommando returnerar ett nummer när det avslutas:
- **0** = Allt gick bra
- **Allt annat** = Något gick fel

```bash
ls /etc/passwd         # Filen finns
echo $?                # 0 (success)

ls /finns/inte         # Filen finns inte
echo $?                # 2 (error - no such file)
```

**Varför det spelar roll - villkorlig exekvering:**

```bash
# Kör nästa BARA om förra lyckades
./build.sh && ./deploy.sh

# Kör nästa BARA om förra misslyckades
./deploy.sh || echo "Deploy failed!" | mail -s "Alert" admin@example.com
```

**I dina egna script:**

```bash
#!/bin/bash
if [ ! -f "$1" ]; then
    echo "Error: Filen finns inte"
    exit 1    # Signalera fel
fi

# ... göra saker ...
exit 0        # Signalera success
```

---

## Command Substitution: Fånga output

**Problem:** Du vill spara dagens datum i en variabel.

**Lösning:** `$(kommando)` kör kommandot och returnerar dess output.

```bash
# Spara output i variabel
today=$(date +%Y-%m-%d)
echo "Dagens datum: $today"    # 2024-12-22

hostname=$(hostname)
user=$(whoami)
echo "Du är $user på $hostname"
```

**Praktiskt exempel - backup med datum:**

```bash
#!/bin/bash
backup_name="backup-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czvf "$backup_name" /etc/nginx
echo "Skapade: $backup_name"
# Output: Skapade: backup-20241222-143052.tar.gz
```

---

## IF-satser: Ta beslut

### Grundstruktur

```bash
if [ villkor ]; then
    # om sant
fi
```

### Med else

```bash
if [ villkor ]; then
    # om sant
else
    # om falskt
fi
```

### Med elif

```bash
if [ villkor1 ]; then
    echo "Villkor 1 sant"
elif [ villkor2 ]; then
    echo "Villkor 2 sant"
else
    echo "Inget matchade"
fi
```

**Verkligt exempel:**

```bash
#!/bin/bash
# check-disk.sh - Varna om disken är full

usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$usage" -gt 90 ]; then
    echo "KRITISKT: Disk $usage% full!"
    exit 2
elif [ "$usage" -gt 70 ]; then
    echo "Varning: Disk $usage% full"
    exit 1
else
    echo "OK: Disk $usage%"
    exit 0
fi
```

---

## Test-operatorer: Vad kan du testa?

### För STRÄNGAR: använd `=`

```bash
name="Said"

[ "$name" = "Said" ]     # Lika med
[ "$name" != "Admin" ]   # Inte lika med
[ -z "$name" ]           # Är TOM? (zero)
[ -n "$name" ]           # Är INTE tom? (non-zero)
```

### För TAL: använd `-eq`, `-lt`, etc.

```bash
age=25

[ "$age" -eq 25 ]    # Equal (lika)
[ "$age" -ne 30 ]    # Not equal (inte lika)
[ "$age" -lt 30 ]    # Less than (mindre än)
[ "$age" -le 25 ]    # Less or equal (mindre eller lika)
[ "$age" -gt 20 ]    # Greater than (större än)
[ "$age" -ge 25 ]    # Greater or equal (större eller lika)
```

> **Viktigt:** `-eq` för tal, `=` för strängar. Blanda inte!

### För FILER: `-f`, `-d`, `-e`, etc.

```bash
[ -f "/etc/passwd" ]     # Är det en FIL?
[ -d "/home" ]           # Är det en KATALOG?
[ -e "/tmp/lock" ]       # EXISTERAR det? (fil eller katalog)
[ -r "/etc/shadow" ]     # Kan jag LÄSA den?
[ -w "/tmp/test" ]       # Kan jag SKRIVA till den?
[ -x "/usr/bin/bash" ]   # Kan jag KÖRA den?
[ -s "/var/log/app.log" ] # Har den INNEHÅLL? (size > 0)
```

**Minnesregel:**
- `-f` = **F**ile
- `-d` = **D**irectory
- `-e` = **E**xists
- `-r`/`-w`/`-x` = **R**ead/**W**rite/e**X**ecute

---

## Kombinera villkor

```bash
# AND - båda måste vara sanna
if [ -f "$fil" ] && [ -r "$fil" ]; then
    echo "Filen finns OCH är läsbar"
fi

# OR - minst ett måste vara sant
if [ "$user" = "root" ] || [ "$user" = "admin" ]; then
    echo "Du har admin-access"
fi

# NOT - invertera
if [ ! -f "$fil" ]; then
    echo "Filen finns INTE"
fi
```

---

## CASE: Multipla val (snyggare än massa elif)

**Istället för:**

```bash
if [ "$1" = "start" ]; then
    echo "Starting..."
elif [ "$1" = "stop" ]; then
    echo "Stopping..."
elif [ "$1" = "restart" ]; then
    echo "Restarting..."
else
    echo "Usage: $0 {start|stop|restart}"
fi
```

**Skriv:**

```bash
case "$1" in
    start)
        echo "Starting..."
        ;;
    stop)
        echo "Stopping..."
        ;;
    restart)
        echo "Restarting..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

**Notera:**
- `;;` avslutar varje block
- `*)` är default (wildcard)
- `esac` avslutar (`case` baklänges)

---

## Övning 1: Argument-hantering

**Uppgift:** Skriv ett script som tar ett filnamn som argument och:
1. Kontrollerar att ett argument gavs
2. Kontrollerar att filen existerar
3. Visar filens storlek

.

.

.

### Lösning:

```bash
#!/bin/bash

# 1. Kontrollera argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# 2. Kontrollera att filen finns
if [ ! -f "$1" ]; then
    echo "Error: '$1' finns inte eller är inte en fil"
    exit 1
fi

# 3. Visa storlek
size=$(ls -lh "$1" | awk '{print $5}')
echo "Filen '$1' är $size stor"
exit 0
```

---

## Övning 2: Service-kontroll

**Uppgift:** Skriv ett script som kontrollerar om nginx körs och:
- Om den körs: visa "Nginx OK"
- Om den inte körs: visa "Nginx NERE" och exit 1

.

.

.

### Lösning:

```bash
#!/bin/bash

if systemctl is-active --quiet nginx; then
    echo "Nginx OK"
    exit 0
else
    echo "Nginx NERE!"
    exit 1
fi
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `name = "Said"` | Mellanslag gör det till kommando | `name="Said"` |
| `[ $var = "x" ]` | Om var är tom → syntax error | `[ "$var" = "x" ]` |
| `if [ $a = 5 ]` | Jämför som sträng | `if [ "$a" -eq 5 ]` |
| `[ -f /etc ]` | -f är för filer | `[ -d /etc ]` för kataloger |
| Glömt `;;` i case | Syntax error | Varje block avslutas med `;;` |
| `echo $?` efter echo | $? visar echos status, inte föregående | Spara: `status=$?` direkt |

---

## Snabbreferens

| Behov | Syntax |
|-------|--------|
| Skapa variabel | `name="value"` (INGA mellanslag!) |
| Använda variabel | `"$name"` eller `"${name}"` |
| Argument 1 | `$1` |
| Antal argument | `$#` |
| Förra exit-status | `$?` |
| Jämför tal | `[ "$a" -eq "$b" ]` |
| Jämför strängar | `[ "$a" = "$b" ]` |
| Fil existerar | `[ -f "$fil" ]` |
| Katalog existerar | `[ -d "$dir" ]` |
| NOT | `[ ! villkor ]` |
| AND | `[ v1 ] && [ v2 ]` |
| OR | `[ v1 ] \|\| [ v2 ]` |

""",
            "quiz": [
                {
                    "question": "Vilken operator jämför två tal för likhet?",
                    "options": ["=", "==", "-eq", "-e"],
                    "correct": 2,
                    "explanation": "-eq (equal) används för numeriska jämförelser. = används för strängar.",
                },
                {
                    "question": "Vad innehåller $# i ett script?",
                    "options": [
                        "Scriptets namn",
                        "Antal argument",
                        "Exit status",
                        "Process ID",
                    ],
                    "correct": 1,
                    "explanation": "$# innehåller antalet argument som skickades till scriptet.",
                },
                {
                    "question": "Vilken test-operator kontrollerar om en fil existerar?",
                    "options": ["-e", "-d", "-f", "-x"],
                    "correct": 2,
                    "explanation": "-f kontrollerar om en regular file existerar. -d är för kataloger, -e för båda.",
                },
            ],
        },
        # =============================================================================
        # NOD 4: Bash Scripting Avancerat
        # =============================================================================
        {
            "title": "Bash Scripting Avancerat",
            "slug": "bash-scripting-avancerat",
            "description": "Loopar (for, while, until), funktioner, select-menyer och read.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 120,
            "order_index": 4,
            "content": r"""# Bash Scripting Avancerat

> **TL;DR:** Loopar låter dig upprepa saker automatiskt. Funktioner låter dig återanvända kod. Tillsammans gör de dina script 10x kraftfullare.

---

## Verkligt scenario: Varför loopar?

**Utan loop - manuellt helvete:**

```bash
./deploy.sh server1
./deploy.sh server2
./deploy.sh server3
./deploy.sh server4
./deploy.sh server5
```

**Med loop - ett kommando:**

```bash
for server in server{1..5}; do
    ./deploy.sh "$server"
done
```

**Det är därför loopar existerar.**

---

## FOR-loop: Gå igenom en lista

### Mental modell

```
┌─────────────────────────────────────────┐
│  for item in LISTA; do                  │
│      gör något med $item                │
│  done                                   │
│                                         │
│  Loopen tar ETT item i taget från LISTAN│
└─────────────────────────────────────────┘
```

### Olika sätt att skapa listan

```bash
# 1. Hårdkodad lista
for frukt in äpple banan citron; do
    echo "Jag gillar $frukt"
done

# 2. Filer i en katalog
for fil in /var/log/*.log; do
    echo "Loggfil: $fil"
done

# 3. Range med {start..slut}
for i in {1..5}; do
    echo "Nummer: $i"
done

# 4. Output från kommando
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "Användare: $user"
done
```

### C-style for (som i Java/C)

```bash
for ((i=0; i<10; i++)); do
    echo "Index: $i"
done
```

**Praktiskt exempel - backup av flera kataloger:**

```bash
#!/bin/bash
DIRS="/etc/nginx /var/www /home/deploy"

for dir in $DIRS; do
    backup_name="$(basename $dir)-$(date +%Y%m%d).tar.gz"
    tar -czvf "/backup/$backup_name" "$dir"
    echo "Backade upp: $dir → $backup_name"
done
```

---

## WHILE-loop: Kör så länge villkoret är sant

### Mental modell

```
┌─────────────────────────────────────────┐
│  while [ VILLKOR ]; do                  │
│      gör saker                          │
│  done                                   │
│                                         │
│  Loopen kör OM OCH OM IGEN så länge     │
│  villkoret är SANT                      │
└─────────────────────────────────────────┘
```

### Grundexempel

```bash
counter=1
while [ $counter -le 5 ]; do
    echo "Räknare: $counter"
    ((counter++))    # Öka med 1
done
```

### Läsa fil rad för rad (SUPERNYTTIGT!)

```bash
while read line; do
    echo "Rad: $line"
done < /etc/hosts
```

**Varför detta funkar:**
- `< /etc/hosts` skickar filens innehåll till loopen
- `read line` läser en rad i taget
- Loopen fortsätter tills filen är slut

**Praktiskt exempel - bearbeta serverlista:**

```bash
#!/bin/bash
# servers.txt innehåller en server per rad

while read server; do
    echo "Pingar $server..."
    if ping -c 1 "$server" &>/dev/null; then
        echo "  ✓ $server är UPPE"
    else
        echo "  ✗ $server är NERE!"
    fi
done < servers.txt
```

---

## UNTIL-loop: Kör tills villkoret blir sant

**Skillnaden mot while:**
- `while` kör SÅ LÄNGE villkoret är sant
- `until` kör TILLS villkoret blir sant

```bash
# While: kör medan counter <= 5
while [ $counter -le 5 ]; do ...

# Until: kör tills counter > 5 (samma sak, annorlunda logik)
until [ $counter -gt 5 ]; do ...
```

**Praktiskt exempel - vänta på att tjänst startar:**

```bash
#!/bin/bash
echo "Väntar på att nginx ska starta..."

until systemctl is-active --quiet nginx; do
    echo "Nginx inte redo, väntar 2 sek..."
    sleep 2
done

echo "Nginx är uppe!"
```

---

## BREAK och CONTINUE: Kontrollera loopen

### break - Hoppa ut ur loopen helt

```bash
for i in {1..100}; do
    if [ $i -eq 5 ]; then
        echo "Hittat! Avbryter."
        break
    fi
    echo "Söker: $i"
done
# Output: Söker: 1, 2, 3, 4, Hittat! Avbryter.
```

### continue - Hoppa till nästa varv

```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue    # Hoppa över 3
    fi
    echo "Nummer: $i"
done
# Output: 1, 2, 4, 5 (3 hoppas över)
```

**Praktiskt exempel - hoppa över kommentarer:**

```bash
while read line; do
    # Hoppa över tomma rader och kommentarer
    [[ -z "$line" || "$line" =~ ^# ]] && continue

    echo "Config: $line"
done < config.txt
```

---

## SELECT: Skapa interaktiva menyer

```bash
#!/bin/bash
PS3="Välj ett alternativ: "    # Prompt-texten

select action in "Starta" "Stoppa" "Status" "Avsluta"; do
    case $action in
        "Starta")
            echo "Startar tjänsten..."
            systemctl start nginx
            ;;
        "Stoppa")
            echo "Stoppar tjänsten..."
            systemctl stop nginx
            ;;
        "Status")
            systemctl status nginx
            ;;
        "Avsluta")
            echo "Hejdå!"
            break
            ;;
        *)
            echo "Ogiltigt val, försök igen"
            ;;
    esac
done
```

**Output:**

```
1) Starta
2) Stoppa
3) Status
4) Avsluta
Välj ett alternativ:
```

---

## SHIFT: Bearbeta argument ett i taget

**Vad shift gör:**

```
FÖRE shift:  $1="a"  $2="b"  $3="c"
EFTER shift: $1="b"  $2="c"  $3=(tom)

Alla argument flyttas ett steg åt vänster.
$1 försvinner, $2 blir nya $1.
```

**Praktiskt exempel - hantera flaggor:**

```bash
#!/bin/bash

while [ $# -gt 0 ]; do
    case "$1" in
        -v|--verbose)
            VERBOSE=true
            ;;
        -f|--file)
            FILE="$2"
            shift    # Extra shift för att hoppa över värdet
            ;;
        *)
            echo "Okänd flagga: $1"
            ;;
    esac
    shift
done

echo "Verbose: $VERBOSE"
echo "File: $FILE"
```

**Körning:**

```bash
./script.sh -v -f config.txt
# Verbose: true
# File: config.txt
```

---

## Funktioner: Återanvändbar kod

### Varför funktioner?

**Utan funktion - upprepning:**

```bash
echo "=== Startar backup ==="
tar -czvf backup1.tar.gz /data
echo "=== Backup klar ==="

echo "=== Startar backup ==="
tar -czvf backup2.tar.gz /config
echo "=== Backup klar ==="
```

**Med funktion - DRY (Don't Repeat Yourself):**

```bash
do_backup() {
    local source="$1"
    local dest="$2"

    echo "=== Startar backup av $source ==="
    tar -czvf "$dest" "$source"
    echo "=== Backup klar ==="
}

do_backup /data backup1.tar.gz
do_backup /config backup2.tar.gz
```

### Syntax

```bash
# Definiera (två sätt, samma resultat)
funktionsnamn() {
    kommandon
}

function funktionsnamn {
    kommandon
}

# Anropa
funktionsnamn
funktionsnamn arg1 arg2
```

### Argument i funktioner

```bash
greet() {
    echo "Hej $1! Du är $2 år."
}

greet "Said" 25
# Output: Hej Said! Du är 25 år.
```

> **Notera:** Funktioner använder `$1`, `$2` etc. precis som script, men det är funktionens egna argument, inte scriptets!

### Returnera värden

```bash
# Return för status (0=ok, annat=fel)
file_exists() {
    if [ -f "$1" ]; then
        return 0
    else
        return 1
    fi
}

# Använda
if file_exists "/etc/passwd"; then
    echo "Filen finns!"
fi
```

**För att returnera TEXT, använd echo:**

```bash
get_ip() {
    hostname -I | awk '{print $1}'
}

my_ip=$(get_ip)
echo "Min IP: $my_ip"
```

---

## LOCAL: Variabler som stannar i funktionen

```bash
name="Global"

test_local() {
    local name="Lokal i funktionen"
    echo "I funktionen: $name"
}

echo "Före: $name"      # Global
test_local              # Lokal i funktionen
echo "Efter: $name"     # Global (oförändrad!)
```

> **Varning:** Utan `local` skriver funktionen över den globala variabeln!

---

## READ: Användarinput

```bash
# Enkel input
read -p "Ditt namn: " name
echo "Hej $name!"

# Tyst input (för lösenord)
read -sp "Lösenord: " password
echo    # Ny rad efter tysta input

# Med timeout (10 sekunder)
if read -t 10 -p "Svara snabbt: " answer; then
    echo "Du svarade: $answer"
else
    echo "Timeout!"
fi

# Läs flera värden
read -p "Förnamn Efternamn: " first last
echo "Hej $first $last!"
```

---

## Övning 1: Loopa igenom servrar

**Uppgift:** Skriv ett script som:
1. Läser servrar från `servers.txt` (en per rad)
2. Pingar varje server
3. Skriver ut vilka som är uppe/nere

.

.

.

### Lösning:

```bash
#!/bin/bash

if [ ! -f "servers.txt" ]; then
    echo "servers.txt saknas!"
    exit 1
fi

while read server; do
    # Hoppa över tomma rader
    [ -z "$server" ] && continue

    if ping -c 1 -W 2 "$server" &>/dev/null; then
        echo "[OK]   $server"
    else
        echo "[NERE] $server"
    fi
done < servers.txt
```

---

## Övning 2: Funktion med validering

**Uppgift:** Skapa en funktion `create_user` som:
1. Tar användarnamn som argument
2. Kontrollerar att argument gavs
3. Kontrollerar att användaren inte redan finns
4. Skapar användaren (simulera med echo)

.

.

.

### Lösning:

```bash
#!/bin/bash

create_user() {
    local username="$1"

    # Validera argument
    if [ -z "$username" ]; then
        echo "Error: Ange användarnamn"
        return 1
    fi

    # Kolla om finns
    if id "$username" &>/dev/null; then
        echo "Error: $username finns redan"
        return 1
    fi

    # Skapa (simulerat)
    echo "Skapar användare: $username"
    # useradd "$username"    # Avkommentera på riktig server
    return 0
}

# Testa
create_user "testuser"
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `for i in 1 2 3 4 5` | Funkar men krångligt | `for i in {1..5}` |
| Oändlig while-loop | Glömt öka räknaren | `((counter++))` i loopen |
| Funktion utan local | Skriver över globala variabler | `local var="value"` |
| `return "text"` | return är bara för statuskod | Använd `echo` för text |
| Glömt `done` | Syntax error | Varje loop avslutas med `done` |
| `read line` utan `<` | Läser från tangentbord | `done < fil.txt` |

---

## Snabbreferens

| Behov | Syntax |
|-------|--------|
| For med lista | `for x in a b c; do ... done` |
| For med range | `for i in {1..10}; do ... done` |
| While | `while [ villkor ]; do ... done` |
| Läs fil | `while read line; do ... done < fil` |
| Until | `until [ villkor ]; do ... done` |
| Hoppa ut | `break` |
| Nästa varv | `continue` |
| Funktion | `namn() { kommandon; }` |
| Lokal variabel | `local var="value"` |
| User input | `read -p "Text: " var` |
| Shift argument | `shift` |

""",
            "quiz": [
                {
                    "question": "Vad gör 'shift' kommandot?",
                    "options": [
                        "Sorterar argument",
                        "Flyttar argument åt vänster",
                        "Lägger till argument",
                        "Tar bort alla argument",
                    ],
                    "correct": 1,
                    "explanation": "shift flyttar alla positionsparametrar ett steg åt vänster. $2 blir $1, osv.",
                },
                {
                    "question": "Vad är skillnaden mellan while och until?",
                    "options": [
                        "Ingen skillnad",
                        "while kör medan sant, until kör tills sant",
                        "until är snabbare",
                        "while kan bara användas med tal",
                    ],
                    "correct": 1,
                    "explanation": "while kör så länge villkoret är sant. until kör tills villkoret blir sant.",
                },
                {
                    "question": "Vad gör 'local' nyckelordet i en funktion?",
                    "options": [
                        "Exporterar variabeln",
                        "Gör variabeln endast tillgänglig i funktionen",
                        "Gör variabeln read-only",
                        "Tar bort variabeln",
                    ],
                    "correct": 1,
                    "explanation": "local skapar en variabel som endast existerar inom funktionen.",
                },
            ],
        },
        # =============================================================================
        # NOD 5: Användare & Rättigheter
        # =============================================================================
        {
            "title": "Användare & Rättigheter",
            "slug": "anvandare-rattigheter",
            "description": "Användarhantering, grupper, chmod, chown, umask och speciella permissions.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "order_index": 5,
            "content": r"""# Användare & Rättigheter

> **TL;DR:** Linux är byggt kring permissions. Varje fil har en ägare, en grupp och rättigheter. Förstå detta och du förstår varför "Permission denied" händer - och hur du fixar det.

---

## Verkligt scenario: Varför permissions spelar roll

Du deployer en webbapp. Nginx ger 403 Forbidden.

**Varför?** Nginx-processen körs som användaren `www-data`, men filerna ägs av `root` och har permissions `700` (bara ägaren kan läsa).

**Lösningen:**

```bash
chown -R www-data:www-data /var/www/app
chmod -R 755 /var/www/app
```

**Nu funkar det.** Nginx kan läsa filerna.

---

## Tre viktiga filer - och vad de innehåller

### `/etc/passwd` - Alla användare

```
said:x:1000:1000:Said Ali:/home/said:/bin/bash
│    │  │    │      │         │          │
│    │  │    │      │         │          └─ Login shell
│    │  │    │      │         └─ Hemkatalog
│    │  │    │      └─ Kommentar (GECOS)
│    │  │    └─ Primary Group ID (GID)
│    │  └─ User ID (UID)
│    └─ "x" betyder lösenord i /etc/shadow
└─ Användarnamn
```

> **Tips:** UID 0 = root. UID 1000+ = vanliga användare.

### `/etc/shadow` - Lösenord (bara root kan läsa)

```
said:$6$abc123...:19500:0:99999:7:::
│         │        │    │   │   │
│         │        │    │   │   └─ Varningsdagar
│         │        │    │   └─ Max dagar mellan byten
│         │        │    └─ Min dagar mellan byten
│         │        └─ Senast ändrat (dagar sedan 1970)
│         └─ Krypterad lösenordshash
└─ Användarnamn
```

### `/etc/group` - Grupper

```
docker:x:999:said,anna
│      │  │     │
│      │  │     └─ Medlemmar (utöver primary group)
│      │  └─ Group ID (GID)
│      └─ Lösenord (sällan använt)
└─ Gruppnamn
```

---

## Skapa och hantera användare

### useradd - Skapa ny användare

```bash
# Grundläggande (GLÖM INTE -m!)
useradd -m username              # -m skapar hemkatalog

# Komplett med shell och grupper
useradd -m -s /bin/bash -G sudo,docker username

# Förklaring av flaggorna:
# -m         Skapa hemkatalog (/home/username)
# -s         Ange shell
# -G         Sekundära grupper (OBS: stor G!)
# -g         Primary group (liten g)
# -c         Kommentar/fullständigt namn
```

> **Varning:** Utan `-m` skapas INGEN hemkatalog!

### passwd - Sätt lösenord

```bash
passwd username          # Som root: sätt lösenord för annan
passwd                   # Byt ditt eget lösenord
```

### usermod - Ändra befintlig användare

```bash
# VIKTIGT: -a betyder "append" (lägg till)
usermod -aG docker said      # Lägg till i docker-gruppen

# Utan -a ERSÄTTS alla grupper!
usermod -G docker said       # ⚠️ FARLIGT: tar bort från alla andra grupper!
```

**Minnesregel:** `-aG` = **A**ppend to **G**roup. Alltid tillsammans!

### userdel - Ta bort användare

```bash
userdel username         # Behåll hemkatalog
userdel -r username      # Ta bort ALLT (hem + mail)
```

---

## Grupper

```bash
# Skapa grupp
groupadd developers

# Visa användarens grupper
groups said                  # developers sudo docker
id said                      # uid=1000(said) gid=1000(said) groups=...

# Lägg till användare i grupp (kom ihåg -aG!)
usermod -aG developers said

# Ta bort grupp
groupdel developers
```

> **Notera:** Ändringar i grupper kräver ny inloggning för att gälla!

---

## Permissions - Så fungerar det

### Mental modell: Tre frågor för varje fil

```
┌────────────────────────────────────────────────────────┐
│  För varje fil frågar Linux:                           │
│                                                        │
│  1. Är du ÄGAREN?      → Använd User-permissions       │
│  2. Är du i GRUPPEN?   → Använd Group-permissions      │
│  3. Inget av ovan?     → Använd Others-permissions     │
│                                                        │
│  Linux stannar vid FÖRSTA matchningen!                 │
└────────────────────────────────────────────────────────┘
```

### Läsa permissions

```bash
ls -l
-rwxr-xr-x 1 said developers 4096 Dec 22 10:00 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └─ Others: r-x (read + execute)
│ │  └─ Group: r-x (read + execute)
│ └─ User/Owner: rwx (read + write + execute)
└─ Typ: - = fil, d = katalog, l = länk
```

### Permissions för filer vs kataloger

| Permission | På FIL | På KATALOG |
|------------|--------|------------|
| **r** (read) | Läsa innehåll | Lista filer (`ls`) |
| **w** (write) | Ändra innehåll | Skapa/ta bort filer |
| **x** (execute) | Köra som program | Gå in i katalogen (`cd`) |

> **Viktigt:** För att öppna en fil i `/home/said/docs/` behöver du `x` på VARJE katalog i sökvägen!

---

## chmod - Ändra permissions

### Oktalt (numeriskt) - Det du MÅSTE kunna

```
r = 4
w = 2
x = 1

Lägg ihop för varje grupp:
rwx = 4+2+1 = 7
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
```

**Vanliga kombinationer:**

```bash
chmod 755 script.sh      # rwxr-xr-x - Script som alla kan köra
chmod 644 config.txt     # rw-r--r-- - Fil som alla kan läsa
chmod 700 ~/.ssh         # rwx------ - Privat katalog
chmod 600 ~/.ssh/id_rsa  # rw------- - SSH-nyckel (MÅSTE vara detta!)
```

### Symboliskt - Lättare att läsa

```bash
chmod u+x script.sh      # User + execute
chmod g-w file.txt       # Group - write
chmod o=r file.txt       # Others = endast read
chmod a+r file.txt       # All + read

# Kombinera
chmod u+x,g-w,o-rwx file
```

### Rekursivt

```bash
chmod -R 755 /var/www/    # Alla filer och mappar
```

> **Varning:** `-R` på fel plats kan förstöra systemet. Dubbelkolla path!

---

## chown - Ändra ägare

```bash
chown said file.txt              # Ändra ägare
chown said:developers file.txt   # Ändra ägare OCH grupp
chown :developers file.txt       # Ändra BARA grupp

# Rekursivt
chown -R www-data:www-data /var/www/
```

---

## umask - Default permissions

**Koncept:** umask är en "mask" som TAR BORT permissions från nya filer.

```
Filer:     666 (max) - umask = default
Kataloger: 777 (max) - umask = default
```

**Exempel med umask 022:**

```
Filer:     666 - 022 = 644 (rw-r--r--)
Kataloger: 777 - 022 = 755 (rwxr-xr-x)
```

```bash
umask                # Visa nuvarande (ofta 022)
umask 077            # Sätt mer restriktiv (filer blir 600)
```

---

## Speciella permissions

### SUID (Set User ID) - Kör som ägaren

```bash
chmod u+s /usr/bin/passwd    # eller chmod 4755
ls -l /usr/bin/passwd
-rwsr-xr-x    # 's' istället för 'x'
```

**Varför det finns:** `passwd` måste skriva till `/etc/shadow` som ägs av root. SUID gör att det körs som root oavsett vem som kör.

### SGID (Set Group ID) - Ärv grupp

```bash
chmod g+s /shared/project/   # eller chmod 2755
```

**Vad det gör:** Alla nya filer i katalogen får automatiskt samma grupp som katalogen - perfekt för delad projektkatalog!

### Sticky Bit - Skydda andras filer

```bash
chmod +t /tmp                # eller chmod 1777
ls -ld /tmp
drwxrwxrwt    # 't' i slutet
```

**Vad det gör:** I `/tmp` kan alla skriva, men du kan bara ta bort DINA EGNA filer.

---

## sudo - Tillfälligt bli root

```bash
sudo kommando                # Kör ett kommando som root
sudo -i                      # Bli root (interaktiv)
sudo -u anna kommando        # Kör som annan användare
```

### sudoers - Vem får sudo?

```bash
# ALLTID redigera med visudo (validerar syntaxen)
sudo visudo

# Syntax:
# VEM    VAR=(SOM VEM) VAD
said    ALL=(ALL:ALL) ALL         # Allt tillåtet med lösenord
%sudo   ALL=(ALL:ALL) ALL         # Gruppen 'sudo' får allt
said    ALL=(ALL) NOPASSWD: ALL   # Utan lösenord (riskfyllt!)
```

---

## Övning 1: Sätta upp delad katalog

**Scenario:** Teamet "developers" ska dela katalogen `/projects/webapp`. Alla i gruppen ska kunna läsa/skriva, nya filer ska ärva gruppen.

**Uppgift:** Skriv kommandona för att sätta upp detta.

.

.

.

### Lösning:

```bash
# 1. Skapa grupp och katalog
sudo groupadd developers
sudo mkdir -p /projects/webapp

# 2. Sätt ägare och grupp
sudo chown root:developers /projects/webapp

# 3. Sätt permissions: rwx för ägare och grupp
sudo chmod 775 /projects/webapp

# 4. SGID så nya filer ärver gruppen
sudo chmod g+s /projects/webapp

# Verifiera
ls -ld /projects/webapp
# drwxrwsr-x ... root developers ... /projects/webapp
```

---

## Övning 2: Felsök "Permission denied"

**Scenario:** Nginx (körs som www-data) ger 403 på `/var/www/site/`.

```bash
ls -la /var/www/site/
drwx------ 2 root root 4096 ... .
-rw------- 1 root root 1234 ... index.html
```

**Uppgift:** Vad är fel? Hur fixar du det?

.

.

.

### Lösning:

**Problem:**
1. Katalogen är 700 (bara root kan `cd` in)
2. Filen är 600 (bara root kan läsa)
3. Ägaren är root, inte www-data

**Fix:**

```bash
# Ändra ägare
sudo chown -R www-data:www-data /var/www/site/

# Ändra permissions
sudo chmod 755 /var/www/site/
sudo chmod 644 /var/www/site/index.html
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `useradd` utan `-m` | Ingen hemkatalog skapas | `useradd -m username` |
| `usermod -G` utan `-a` | Tar bort från ALLA grupper | `usermod -aG group user` |
| chmod 777 | Alla kan allt - säkerhetsrisk | Använd 755 eller 644 |
| Blandar oktal/symbolisk | 755 ≠ u+rwx | Välj en metod |
| Glömmer x på katalog | Kan inte `cd` in | Kataloger behöver x |
| SSH-nyckel med 644 | SSH vägrar starta | `chmod 600 ~/.ssh/id_rsa` |

---

## Snabbreferens

| Värde | Permissions | Användning |
|-------|-------------|------------|
| **755** | rwxr-xr-x | Kataloger, scripts |
| **644** | rw-r--r-- | Vanliga filer |
| **700** | rwx------ | Privata kataloger |
| **600** | rw------- | SSH-nycklar, secrets |
| **775** | rwxrwxr-x | Delade kataloger |
| **4755** | rwsr-xr-x | SUID-program |
| **2775** | rwxrwsr-x | SGID-katalog |
| **1777** | rwxrwxrwt | Sticky (/tmp) |

| Kommando | Vad det gör |
|----------|-------------|
| `useradd -m user` | Skapa användare med hem |
| `usermod -aG grp user` | Lägg till i grupp |
| `chmod 755 fil` | Sätt permissions |
| `chown user:grp fil` | Ändra ägare |
| `groups user` | Visa grupper |
| `id user` | Visa UID, GID, grupper |

""",
            "quiz": [
                {
                    "question": "Vad är chmod 755 i symbolisk form?",
                    "options": ["rw-r--r--", "rwxr-xr-x", "rwx------", "rwxrwxrwx"],
                    "correct": 1,
                    "explanation": "755 = 7(rwx) + 5(r-x) + 5(r-x) = rwxr-xr-x",
                },
                {
                    "question": "Vilket kommando lägger till en användare i gruppen 'docker'?",
                    "options": [
                        "useradd -G docker user",
                        "usermod -aG docker user",
                        "groupadd docker user",
                        "adduser docker user",
                    ],
                    "correct": 1,
                    "explanation": "usermod -aG (append Group) lägger till användaren i gruppen utan att ta bort från andra grupper.",
                },
                {
                    "question": "Vad gör sticky bit på en katalog?",
                    "options": [
                        "Gör katalogen osynlig",
                        "Endast ägare kan ta bort sina egna filer",
                        "Alla kan ta bort alla filer",
                        "Katalogen blir read-only",
                    ],
                    "correct": 1,
                    "explanation": "Sticky bit (t) på kataloger betyder att endast filens ägare kan ta bort filen, även om andra har write-access.",
                },
            ],
        },
        # =============================================================================
        # NOD 6: SSH & Säkerhet
        # =============================================================================
        {
            "title": "SSH & Säkerhet",
            "slug": "ssh-sakerhet",
            "description": "SSH-nycklar, sshd_config, scp och ssh-alias för säker åtkomst.",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "order_index": 6,
            "content": r"""# SSH & Säkerhet

> **TL;DR:** SSH är hur du fjärrstyr servrar säkert. Nycklar istället för lösenord = säkrare OCH smidigare. Lär dig detta så slipper du skriva lösenord 50 gånger om dagen.

---

## Verkligt scenario: Din vardag som DevOps

Du hanterar 10 servrar. Utan SSH-nycklar:

```bash
ssh user@server1    # Skriv lösenord
ssh user@server2    # Skriv lösenord igen
ssh user@server3    # ...och igen
# 50 inloggningar per dag = 50 lösenord
```

**Med SSH-nycklar:**

```bash
ssh prod1           # Direkt in
ssh prod2           # Direkt in
ssh prod3           # Ingen lösenordsprompt
```

**Plus:** Nycklar kan inte gissas eller bruteforceas som lösenord.

---

## Mental modell: Hur SSH-nycklar fungerar

```
┌─────────────────┐                    ┌─────────────────┐
│   DIN DATOR     │                    │    SERVERN      │
│                 │                    │                 │
│  id_ed25519     │                    │ authorized_keys │
│  (PRIVAT)       │───── Bevisar ─────>│ (PUBLIK)        │
│  Behåll hemlig! │     identitet      │ Dela fritt      │
└─────────────────┘                    └─────────────────┘

Privata nyckeln = din signatur (visa ALDRIG för någon)
Publika nyckeln = ditt visitkort (kopiera till alla servrar)
```

---

## Skapa SSH-nyckelpar

### Steg 1: Generera nycklar

```bash
# Rekommenderat: Ed25519 (snabb, säker, kort)
ssh-keygen -t ed25519 -C "said@example.com"

# Alternativ: RSA (äldre, fungerar överallt)
ssh-keygen -t rsa -b 4096 -C "said@example.com"
```

**Vad händer:**

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/said/.ssh/id_ed25519): [ENTER]
Enter passphrase (empty for no passphrase): [valfritt lösenord]
Enter same passphrase again:

Your identification has been saved in /home/said/.ssh/id_ed25519       # PRIVAT
Your public key has been saved in /home/said/.ssh/id_ed25519.pub       # PUBLIK
```

> **Tips:** Passphrase är valfritt men rekommenderat. Det krypterar din privata nyckel.

### Steg 2: Kopiera publika nyckeln till servern

**Metod 1: ssh-copy-id (enklast)**

```bash
ssh-copy-id user@server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server    # Specifik nyckel
```

**Metod 2: Manuellt (om ssh-copy-id inte finns)**

```bash
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

### Steg 3: Testa

```bash
ssh user@server
# Ingen lösenordsprompt = det funkar!
```

---

## Viktiga filer och permissions

```
~/.ssh/
├── id_ed25519           # Privat nyckel - MÅSTE vara 600!
├── id_ed25519.pub       # Publik nyckel - kan vara 644
├── authorized_keys      # Serverns lista över tillåtna nycklar
├── config               # Dina alias och inställningar
└── known_hosts          # Servrar du har anslutit till
```

**KRITISKT - permissions:**

```bash
chmod 700 ~/.ssh                  # Katalogen: bara du
chmod 600 ~/.ssh/id_ed25519       # Privat nyckel: bara du läsa/skriva
chmod 644 ~/.ssh/id_ed25519.pub   # Publik nyckel: alla kan läsa
chmod 600 ~/.ssh/authorized_keys  # Server: bara du
```

> **Varning:** Om privata nyckeln har för öppna permissions, vägrar SSH använda den!

---

## SSH-konfiguration på servern

### Filen: `/etc/ssh/sshd_config`

```bash
sudo nano /etc/ssh/sshd_config
```

### Säkerhetsinställningar (rekommenderat)

```bash
# Byt port från default 22 (minskar botattacker)
Port 2222

# Neka root att logga in direkt
PermitRootLogin no

# STÄNG AV lösenordsinloggning (endast nycklar)
PasswordAuthentication no
PubkeyAuthentication yes

# Begränsa vilka användare som får logga in
AllowUsers said anna deploy

# Max antal misslyckade försök
MaxAuthTries 3

# Timeout för inaktiva sessioner
ClientAliveInterval 300
ClientAliveCountMax 2
```

### Aktivera ändringarna

```bash
# Testa config först (hittar syntax-fel)
sudo sshd -t

# Om OK, starta om
sudo systemctl restart ssh       # Debian/Ubuntu
sudo systemctl restart sshd      # CentOS/Fedora/RHEL
```

> **Varning:** Testa ALLTID i en ny terminal INNAN du stänger den nuvarande. Annars kan du låsa ut dig!

---

## SSH-kommandon du använder dagligen

### Ansluta

```bash
ssh user@server                    # Vanlig anslutning
ssh -p 2222 user@server            # Annan port
ssh -i ~/.ssh/special_key user@server   # Specifik nyckel
```

### Köra kommandon remote

```bash
# Kör ett kommando och se output
ssh user@server "df -h"

# Kör flera kommandon
ssh user@server "cd /var/www && git pull && systemctl restart nginx"

# Interaktivt (starta bash på servern)
ssh -t user@server "sudo su -"
```

### Kopiera filer med SCP

```bash
# Lokal → Server
scp fil.txt user@server:/path/to/
scp -r katalog/ user@server:/path/to/     # Rekursivt

# Server → Lokal
scp user@server:/var/log/app.log ./
scp -r user@server:/backup/ ./local/

# Med annan port (OBS: stort -P!)
scp -P 2222 fil.txt user@server:/path/
```

### Kopiera med rsync (bättre för stora överföringar)

```bash
# Synka katalog (kopierar bara ändringar)
rsync -avz /local/path/ user@server:/remote/path/

# Med progress och annan port
rsync -avz --progress -e "ssh -p 2222" /local/ user@server:/remote/
```

---

## SSH Config: Sluta skriva långa kommandon

**Problemet:**

```bash
ssh -p 2222 -i ~/.ssh/deploy_key deploy@prod.example.com
# Varje. Enda. Gång.
```

**Lösningen:** `~/.ssh/config`

```bash
# ~/.ssh/config

Host prod
    HostName prod.example.com
    User deploy
    Port 2222
    IdentityFile ~/.ssh/deploy_key

Host staging
    HostName staging.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/deploy_key

Host dev
    HostName 192.168.1.50
    User said
    ForwardAgent yes

# Wildcard för alla servrar i ett nätverk
Host 192.168.1.*
    User admin
    IdentityFile ~/.ssh/work_key
```

**Nu kan du:**

```bash
ssh prod           # Istället för den långa raden
scp fil.txt staging:/var/www/
rsync -avz /app/ dev:/home/said/app/
```

---

## SSH Agent: Slipp skriva passphrase

Om du har passphrase på din nyckel:

```bash
# Starta agenten (oftast redan igång)
eval $(ssh-agent)

# Lägg till din nyckel (skriver passphrase EN gång)
ssh-add ~/.ssh/id_ed25519

# Nu kommer alla ssh-kommandon använda agenten
ssh prod    # Ingen prompt!
```

---

## Övning 1: Sätta upp nyckellogin

**Scenario:** Du ska kunna logga in på server `192.168.1.100` som användare `deploy` utan lösenord.

**Uppgift:** Skriv alla steg.

.

.

.

### Lösning:

```bash
# 1. Generera nyckel (om du inte har)
ssh-keygen -t ed25519 -C "my-deploy-key"

# 2. Kopiera till servern
ssh-copy-id deploy@192.168.1.100

# 3. Testa
ssh deploy@192.168.1.100

# 4. (Bonus) Skapa alias i ~/.ssh/config
cat >> ~/.ssh/config << 'EOF'
Host myserver
    HostName 192.168.1.100
    User deploy
    IdentityFile ~/.ssh/id_ed25519
EOF

# 5. Nu funkar:
ssh myserver
```

---

## Övning 2: Härda SSH-server

**Scenario:** Du ska säkra en ny server. Root-login ska nekas, endast nycklar tillåtas.

**Uppgift:** Vilka rader ändrar du i sshd_config?

.

.

.

### Lösning:

```bash
# I /etc/ssh/sshd_config, ändra/lägg till:

PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3

# Sen:
sudo sshd -t                    # Testa config
sudo systemctl restart ssh      # Aktivera
```

> **Varning:** Säkerställ att du har fungerande nyckel-login INNAN du stänger av lösenord!

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| Chmod 644 på privat nyckel | SSH vägrar använda den | `chmod 600 ~/.ssh/id_ed25519` |
| scp -p för port | Litet -p är "preserve" | `scp -P 2222` (stort P) |
| Glömmer restart ssh | Ändringarna gäller inte | `sudo systemctl restart ssh` |
| Stänger av lösenord först | Låser ut sig | Testa nyckel först! |
| PermitRootLogin=no på fel ställe | Kommentar eller fel fil | Kolla /etc/ssh/sshd_config |

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Generera nyckel | `ssh-keygen -t ed25519` |
| Kopiera nyckel | `ssh-copy-id user@server` |
| Anslut | `ssh user@server` |
| Anslut annan port | `ssh -p 2222 user@server` |
| Kopiera fil till server | `scp fil.txt user@server:/path/` |
| Kopiera fil från server | `scp user@server:/path/fil.txt ./` |
| Kopiera katalog | `scp -r katalog/ user@server:` |
| Kör kommando remote | `ssh user@server "kommando"` |
| Testa sshd config | `sudo sshd -t` |
| Restart SSH-server | `sudo systemctl restart ssh` |

""",
            "quiz": [
                {
                    "question": "Vilken SSH-inställning nekar root att logga in?",
                    "options": [
                        "DenyRoot yes",
                        "PermitRootLogin no",
                        "RootLogin false",
                        "AllowRoot no",
                    ],
                    "correct": 1,
                    "explanation": "PermitRootLogin no i /etc/ssh/sshd_config nekar direktinloggning som root.",
                },
                {
                    "question": "Vilket kommando kopierar din publika nyckel till en server?",
                    "options": [
                        "ssh-copy",
                        "scp ~/.ssh/id_ed25519.pub",
                        "ssh-copy-id user@server",
                        "ssh-keygen -c",
                    ],
                    "correct": 2,
                    "explanation": "ssh-copy-id kopierar automatiskt din publika nyckel till serverns authorized_keys.",
                },
                {
                    "question": "Vilken flagga anger en annan port för scp?",
                    "options": ["-p", "-P", "--port", "-port"],
                    "correct": 1,
                    "explanation": "scp använder stort -P för port (ssh använder litet -p). scp -P 2222 fil.txt user@server:",
                },
            ],
        },
        # =============================================================================
        # NOD 7: Firewall
        # =============================================================================
        {
            "title": "Firewall",
            "slug": "firewall",
            "description": "UFW (Ubuntu) och FirewallD (CentOS/Fedora) för nätverkssäkerhet.",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "order_index": 7,
            "content": r"""# Firewall

> **TL;DR:** Brandväggen bestämmer vilken trafik som släpps in och ut. UFW på Ubuntu, FirewallD på CentOS/Fedora. Aktivera den, öppna bara de portar du behöver.

---

## Verkligt scenario: Varför brandvägg?

Du sätter upp en webbserver. Utan brandvägg:

```
┌─────────────────────────────────────────────────────┐
│  INTERNET → ALLA portar öppna → Din server          │
│                                                     │
│  Port 22 (SSH)     ✓ Du vill ha                     │
│  Port 80 (HTTP)    ✓ Du vill ha                     │
│  Port 443 (HTTPS)  ✓ Du vill ha                     │
│  Port 3306 (MySQL) ✗ Borde vara stängd!             │
│  Port 6379 (Redis) ✗ Borde vara stängd!             │
│  Port 5432 (Postgres) ✗ Borde vara stängd!          │
└─────────────────────────────────────────────────────┘
```

**Med brandvägg:**

```
┌─────────────────────────────────────────────────────┐
│  INTERNET → Brandvägg → Endast tillåtna portar      │
│                                                     │
│  ✓ Port 22, 80, 443 → Släpps igenom                 │
│  ✗ Allt annat → Blockeras                           │
└─────────────────────────────────────────────────────┘
```

---

## UFW (Uncomplicated Firewall) - Ubuntu/Debian

UFW är ett enkelt gränssnitt till iptables. "Uncomplicated" = lätt att använda.

### Grundläggande status och kontroll

```bash
# Se status (visar om aktiv + alla regler)
sudo ufw status
sudo ufw status verbose     # Mer detaljer
sudo ufw status numbered    # Med radnummer (för att ta bort)

# Aktivera/Avaktivera
sudo ufw enable             # Slå PÅ brandväggen
sudo ufw disable            # Slå AV

# Varning vid enable
# "Command may disrupt existing ssh connections. Proceed with operation (y|n)?"
# Svara y OM du redan har tillåtit SSH!
```

> **Varning:** Aktivera INTE ufw innan du tillåtit SSH (port 22), annars låser du ut dig!

### Säker ordning för ny server

```bash
# 1. Tillåt SSH FÖRST
sudo ufw allow ssh

# 2. SEN aktivera
sudo ufw enable

# 3. Lägg till andra portar
sudo ufw allow http
sudo ufw allow https
```

### Tillåt trafik

```bash
# By service name (läser /etc/services)
sudo ufw allow ssh          # Port 22
sudo ufw allow http         # Port 80
sudo ufw allow https        # Port 443

# By port number
sudo ufw allow 22
sudo ufw allow 8080

# Specifikt protokoll
sudo ufw allow 22/tcp
sudo ufw allow 53/udp

# Port range
sudo ufw allow 6000:6007/tcp

# Från specifik IP
sudo ufw allow from 192.168.1.100

# Från specifik IP till specifik port
sudo ufw allow from 192.168.1.100 to any port 22

# Från helt subnät
sudo ufw allow from 192.168.1.0/24

# Till specifikt interface
sudo ufw allow in on eth0 to any port 80
```

### Neka trafik

```bash
sudo ufw deny 23            # Telnet - blockera!
sudo ufw deny from 10.0.0.0/8
sudo ufw deny from 192.168.1.50 to any port 22
```

### Ta bort regler

```bash
# Metod 1: Via nummer
sudo ufw status numbered
# Output:
# [1] 22/tcp    ALLOW IN    Anywhere
# [2] 80/tcp    ALLOW IN    Anywhere
# [3] 443/tcp   ALLOW IN    Anywhere

sudo ufw delete 2           # Tar bort regel 2 (port 80)

# Metod 2: Via exakt regel
sudo ufw delete allow http
sudo ufw delete allow 8080/tcp
```

### Default policy

```bash
# Se nuvarande
sudo ufw status verbose

# Sätt default (rekommenderat: deny inkommande, allow utgående)
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Reset (börja om)

```bash
sudo ufw reset              # Raderar ALLA regler!
```

---

## FirewallD - CentOS/Fedora/RHEL

FirewallD använder "zoner" för olika nätverksmiljöer.

### Status

```bash
# Är den igång?
sudo firewall-cmd --state              # running/not running
sudo systemctl status firewalld

# Visa alla regler
sudo firewall-cmd --list-all
sudo firewall-cmd --list-all --zone=public

# Visa öppna portar/services
sudo firewall-cmd --list-ports
sudo firewall-cmd --list-services
```

### Öppna portar/services

```bash
# Tillfälligt (försvinner vid reload/reboot)
sudo firewall-cmd --add-port=8080/tcp
sudo firewall-cmd --add-service=http

# PERMANENT (sparas, kräver --reload för att gälla)
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent

# VIKTIGT: Reload för att aktivera permanenta ändringar!
sudo firewall-cmd --reload
```

> **Viktigt:** `--permanent` sparar regeln men aktiverar den INTE direkt. Du måste köra `--reload`!

### Ta bort regler

```bash
sudo firewall-cmd --remove-port=8080/tcp --permanent
sudo firewall-cmd --remove-service=http --permanent
sudo firewall-cmd --reload
```

### Zoner

FirewallD har olika zoner för olika "trust levels":

```bash
# Lista zoner
sudo firewall-cmd --get-zones
# Output: block dmz drop external home internal public trusted work

# Se aktiv zon
sudo firewall-cmd --get-active-zones

# Se regler för specifik zon
sudo firewall-cmd --zone=public --list-all

# Lägg till service i specifik zon
sudo firewall-cmd --zone=public --add-service=http --permanent
```

**Vanligaste zoner:**
- `public` - Default, öppet nätverk (internet)
- `trusted` - Lita på allt (farligt!)
- `drop` - Blockera allt utan svar

### Rich rules (avancerat)

```bash
# Tillåt specifik IP till port
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port port="22" protocol="tcp" accept' --permanent

# Blockera IP
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="10.0.0.50" reject' --permanent

sudo firewall-cmd --reload
```

---

## UFW vs FirewallD - Snabbjämförelse

| Uppgift | UFW (Ubuntu) | FirewallD (CentOS) |
|---------|--------------|---------------------|
| Status | `ufw status` | `firewall-cmd --state` |
| Aktivera | `ufw enable` | `systemctl start firewalld` |
| Öppna port 80 | `ufw allow 80/tcp` | `firewall-cmd --add-port=80/tcp --permanent && firewall-cmd --reload` |
| Öppna HTTP | `ufw allow http` | `firewall-cmd --add-service=http --permanent && firewall-cmd --reload` |
| Stäng port | `ufw delete allow 80` | `firewall-cmd --remove-port=80/tcp --permanent && firewall-cmd --reload` |
| Visa regler | `ufw status numbered` | `firewall-cmd --list-all` |

---

## Övning 1: Säkra en webbserver

**Scenario:** Du ska sätta upp brandväggen på en ny Ubuntu-server som kör nginx.

**Krav:**
- SSH (port 22) ska vara öppen
- HTTP (port 80) ska vara öppen
- HTTPS (port 443) ska vara öppen
- Allt annat ska blockeras

.

.

.

### Lösning:

```bash
# 1. Tillåt SSH först (så du inte låser ut dig!)
sudo ufw allow ssh

# 2. Aktivera brandväggen
sudo ufw enable

# 3. Tillåt webbtrafik
sudo ufw allow http
sudo ufw allow https

# 4. Verifiera
sudo ufw status
# Status: active
# To                         Action      From
# --                         ------      ----
# 22/tcp                     ALLOW       Anywhere
# 80/tcp                     ALLOW       Anywhere
# 443/tcp                    ALLOW       Anywhere
```

---

## Övning 2: Begränsa databasåtkomst

**Scenario:** MySQL (port 3306) ska bara vara tillgänglig från appservern 192.168.1.50.

**Uppgift:** Skriv UFW-kommandot.

.

.

.

### Lösning:

```bash
# Tillåt BARA från appservern
sudo ufw allow from 192.168.1.50 to any port 3306

# Verifiera
sudo ufw status
# 3306    ALLOW    192.168.1.50
```

Utan detta kommando (eller med `ufw allow 3306`) kan VEM SOM HELST koppla upp sig mot din databas!

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `ufw enable` före `allow ssh` | Låser ut dig från servern | Tillåt SSH först! |
| `firewall-cmd --add-port` utan `--permanent` | Regeln försvinner vid reboot | Lägg till `--permanent` |
| `--permanent` utan `--reload` | Regeln sparas men gäller inte | Kör `--reload` efteråt |
| `ufw allow 3306` | Hela världen kan nå din databas | Begränsa till specifik IP |
| Glömmer protokoll | Kan blockera fel trafik | Ange `/tcp` eller `/udp` |

---

## Snabbreferens UFW

| Uppgift | Kommando |
|---------|----------|
| Status | `sudo ufw status` |
| Aktivera | `sudo ufw enable` |
| Tillåt port | `sudo ufw allow 8080/tcp` |
| Tillåt service | `sudo ufw allow ssh` |
| Tillåt från IP | `sudo ufw allow from 192.168.1.100` |
| Ta bort regel | `sudo ufw delete allow 8080` |
| Ta bort via nummer | `sudo ufw status numbered && sudo ufw delete 2` |
| Reset | `sudo ufw reset` |

## Snabbreferens FirewallD

| Uppgift | Kommando |
|---------|----------|
| Status | `sudo firewall-cmd --state` |
| Lista allt | `sudo firewall-cmd --list-all` |
| Öppna port | `sudo firewall-cmd --add-port=80/tcp --permanent` |
| Öppna service | `sudo firewall-cmd --add-service=http --permanent` |
| Ta bort port | `sudo firewall-cmd --remove-port=80/tcp --permanent` |
| **Reload!** | `sudo firewall-cmd --reload` |

""",
            "quiz": [
                {
                    "question": "Vilket kommando aktiverar UFW?",
                    "options": [
                        "ufw start",
                        "ufw enable",
                        "sudo ufw enable",
                        "systemctl start ufw",
                    ],
                    "correct": 2,
                    "explanation": "sudo ufw enable aktiverar UFW-brandväggen. Glöm inte att tillåta SSH först!",
                },
                {
                    "question": "Vad måste du göra efter --permanent i firewalld?",
                    "options": [
                        "Starta om servern",
                        "Köra firewall-cmd --reload",
                        "Inget, det gäller direkt",
                        "Köra systemctl restart firewalld",
                    ],
                    "correct": 1,
                    "explanation": "--permanent sparar regeln men aktiverar den inte. Du måste köra --reload för att aktivera.",
                },
                {
                    "question": "Hur tar du bort regel nummer 3 i UFW?",
                    "options": [
                        "ufw remove 3",
                        "ufw delete 3",
                        "sudo ufw delete 3",
                        "sudo ufw remove rule 3",
                    ],
                    "correct": 2,
                    "explanation": "sudo ufw delete [nummer] tar bort regeln. Använd 'ufw status numbered' först för att se numren.",
                },
            ],
        },
        # =============================================================================
        # NOD 8: Docker Basics
        # =============================================================================
        {
            "title": "Docker Basics",
            "slug": "docker-basics",
            "description": "Containers, images, volumes och networks - grunderna i Docker.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 120,
            "order_index": 8,
            "content": r"""# Docker Basics

> **TL;DR:** Docker paketerar din app med allt den behöver. "Det funkar på min maskin" blir "det funkar överallt". Lär dig images, containers och volumes så kan du köra vad som helst.

---

## Verkligt scenario: Varför Docker?

**Utan Docker:**

```
Utvecklare: "Det funkar på min maskin!"
Ops: "Men inte på servern..."
Utvecklare: "Du måste installera Python 3.9, Redis, PostgreSQL 14,
             specifika bibliotek, rätt systempaket..."
Ops: "Vi har Python 3.8 och Postgres 13..."
```

**Med Docker:**

```bash
docker compose up
# Allt funkar. Överallt. Varje gång.
```

---

## Mental modell: Images vs Containers

```
┌─────────────────────────────────────────────────────────┐
│  IMAGE = Mall/Recept                                    │
│  • Read-only                                            │
│  • Innehåller OS + app + dependencies                   │
│  • Delas via Docker Hub                                 │
│                                                         │
│  CONTAINER = Körande instans av en image                │
│  • Kan skrivas till (men ändringarna försvinner!)       │
│  • Isolerad process                                     │
│  • Startas, stoppas, tas bort                           │
└─────────────────────────────────────────────────────────┘

Analogi:
IMAGE = Klassrecept (instruktioner)
CONTAINER = Kakan du bakar (resultat av att följa receptet)

Du kan baka många kakor från samma recept!
```

---

## docker run - Starta en container

### Grundsyntax

```bash
docker run [OPTIONS] IMAGE [COMMAND]
```

### Vanligaste flaggorna

```bash
# Interaktivt (som att SSH:a in)
docker run -it ubuntu bash
# -i = interactive (håll stdin öppen)
# -t = tty (ge oss en terminal)

# I bakgrunden (servers, databaser)
docker run -d nginx
# -d = detached (kör i bakgrunden)

# Med eget namn
docker run -d --name mywebserver nginx
# Utan namn får du något som "quirky_einstein"

# Ta bort containern automatiskt när den avslutas
docker run --rm alpine echo "Hello"
# Perfekt för one-off-kommandon

# Alla flaggor kombinerade (vanligt!)
docker run -d --name webapp -p 8080:80 nginx
```

---

## Port Mapping: Exponera containern

### Varför behövs det?

```
┌──────────────────────────────────────────────────────┐
│  UTAN port mapping:                                  │
│                                                      │
│  [Internet] ──X──> [Container på port 80]            │
│                    (ingen kan nå den!)               │
│                                                      │
│  MED port mapping (-p 8080:80):                      │
│                                                      │
│  [Internet] ──> [Host:8080] ──> [Container:80]       │
│                 Mappat!                              │
└──────────────────────────────────────────────────────┘
```

### Syntax

```bash
# -p HOST_PORT:CONTAINER_PORT
docker run -p 8080:80 nginx    # Host 8080 → Container 80
docker run -p 80:80 nginx      # Host 80 → Container 80
docker run -p 3000:3000 node   # Samma port

# Endast localhost (säkrare!)
docker run -p 127.0.0.1:8080:80 nginx

# Flera portar
docker run -p 80:80 -p 443:443 nginx
```

> **Varning:** Docker kringgår UFW/FirewallD! När du exponerar en port är den öppen för världen, oavsett brandväggsregler.

---

## Lista, stoppa, ta bort

### Lista containers

```bash
docker ps              # Bara körande
docker ps -a           # Alla (även stoppade)

# Output:
# CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES
# abc123        nginx  ...      2h ago   Up 2h   80/tcp mywebserver
```

### Stoppa och starta

```bash
docker stop mywebserver     # Graceful stop (SIGTERM)
docker kill mywebserver     # Force stop (SIGKILL)
docker start mywebserver    # Starta igen
docker restart mywebserver  # Stop + Start
```

### Ta bort

```bash
docker rm mywebserver           # Ta bort stoppad container
docker rm -f mywebserver        # Force (tar bort även körande)

# Ta bort ALLA stoppade containers
docker container prune

# Städa ALLT oanvänt (containers, images, networks)
docker system prune
docker system prune -a    # + oanvända images
```

---

## Gå in i en körande container

```bash
# Starta bash i containern
docker exec -it mycontainer bash

# Kör ett kommando utan att gå in
docker exec mycontainer cat /etc/nginx/nginx.conf

# Se loggarna
docker logs mycontainer
docker logs -f mycontainer    # Follow (som tail -f)
docker logs --tail 100 mycontainer   # Sista 100 rader
```

---

## Volumes: Beständig data

### Problemet

```
┌──────────────────────────────────────────────────────┐
│  UTAN volume:                                        │
│                                                      │
│  1. docker run postgres                              │
│  2. Skapa databas, lägg till data                    │
│  3. docker rm postgres                               │
│  4. ALL DATA BORTA! 💀                               │
│                                                      │
│  MED volume:                                         │
│                                                      │
│  1. docker run -v pgdata:/var/lib/postgresql/data    │
│  2. Skapa databas, lägg till data                    │
│  3. docker rm postgres                               │
│  4. Starta ny container med samma volume             │
│  5. DATA KVAR! ✓                                     │
└──────────────────────────────────────────────────────┘
```

### Två typer av volumes

**1. Named volumes (Docker hanterar)**

```bash
# Docker skapar och hanterar
docker volume create mydata
docker run -v mydata:/data alpine

# Eller skapa automatiskt vid run
docker run -v pgdata:/var/lib/postgresql/data postgres
```

**2. Bind mounts (du bestämmer plats)**

```bash
# Din host-path mappas in i containern
docker run -v /home/said/projekt:/app node

# Vanligt: mappa nuvarande katalog
docker run -v $(pwd):/app node
docker run -v "$(pwd)":/app node    # Med citattecken (säkrare)
```

### Hantera volumes

```bash
docker volume ls                  # Lista alla
docker volume inspect mydata      # Visa detaljer
docker volume rm mydata           # Ta bort
docker volume prune               # Ta bort oanvända
```

---

## Networks: Container-kommunikation

### Varför?

```
┌──────────────────────────────────────────────────────┐
│  Scenario: Web + Database                            │
│                                                      │
│  webapp ──────?──────> postgres                      │
│  Hur hittar webapp databasen?                        │
│                                                      │
│  Svar: Skapa ett network!                            │
│                                                      │
│  webapp ────mynet────> postgres                      │
│  Nu kan webapp nå postgres via hostname "postgres"   │
└──────────────────────────────────────────────────────┘
```

### Praktiskt exempel

```bash
# 1. Skapa nätverk
docker network create myapp

# 2. Starta databas i nätverket
docker run -d --name db --network myapp postgres

# 3. Starta webapp i samma nätverk
docker run -d --name web --network myapp -p 8080:80 mywebapp

# 4. Nu kan "web" ansluta till "db" via hostname "db"!
# I webappens kod: postgres://db:5432/mydb
```

### Nätverkstyper

| Typ | Användning |
|-----|------------|
| `bridge` | Default. Containers kan kommunicera via IP eller hostname |
| `host` | Container använder host-nätverket direkt (ingen isolering) |
| `none` | Ingen nätverksåtkomst |

---

## Images: Ladda ner och hantera

```bash
# Ladda ner image (sker automatiskt vid run också)
docker pull nginx
docker pull nginx:1.25          # Specifik version (tag)
docker pull postgres:14-alpine  # Minimal Alpine-baserad

# Lista images
docker images

# Ta bort
docker rmi nginx               # Ta bort image
docker image prune             # Oanvända images
docker image prune -a          # Alla images som ingen container använder
```

---

## Övning 1: Starta en webbserver

**Uppgift:**
1. Starta nginx i bakgrunden
2. Mappa port 8080 på host till port 80 i containern
3. Namnge containern "webtest"

.

.

.

### Lösning:

```bash
docker run -d --name webtest -p 8080:80 nginx

# Verifiera
docker ps
curl localhost:8080

# Städa upp
docker rm -f webtest
```

---

## Övning 2: Databas med beständig data

**Uppgift:**
1. Skapa en volume för PostgreSQL-data
2. Starta PostgreSQL med den volymen
3. Stoppa och ta bort containern
4. Verifiera att volymen finns kvar

.

.

.

### Lösning:

```bash
# 1. Skapa volume
docker volume create pgdata

# 2. Starta postgres
docker run -d \
    --name mydb \
    -e POSTGRES_PASSWORD=secret \
    -v pgdata:/var/lib/postgresql/data \
    postgres:14

# 3. Ta bort containern
docker rm -f mydb

# 4. Volymen finns kvar!
docker volume ls
# pgdata är kvar - data överlevde!

# Starta ny container med samma data:
docker run -d \
    --name mydb2 \
    -e POSTGRES_PASSWORD=secret \
    -v pgdata:/var/lib/postgresql/data \
    postgres:14
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `-p 80:8080` | Fel ordning! | `-p HOST:CONTAINER` = `-p 8080:80` |
| Glömmer `-d` | Terminalen låses | `docker run -d` för bakgrund |
| Ingen volume på db | Data försvinner | `-v pgdata:/var/lib/...` |
| `docker rmi` på körande | Funkar inte | Stoppa containern först |
| Tror brandväggen skyddar | Docker kringgår UFW | Bind till 127.0.0.1 om lokal |

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Kör interaktivt | `docker run -it ubuntu bash` |
| Kör i bakgrund | `docker run -d nginx` |
| Med namn och port | `docker run -d --name web -p 8080:80 nginx` |
| Med volume | `docker run -v mydata:/data nginx` |
| Lista containers | `docker ps -a` |
| Gå in i container | `docker exec -it container bash` |
| Se loggar | `docker logs -f container` |
| Stoppa | `docker stop container` |
| Ta bort | `docker rm container` |
| Städa allt | `docker system prune -a` |

""",
            "quiz": [
                {
                    "question": "Vad gör flaggan -d i docker run?",
                    "options": [
                        "Delete after run",
                        "Detached (bakgrund)",
                        "Debug mode",
                        "Download image",
                    ],
                    "correct": 1,
                    "explanation": "-d (detached) kör containern i bakgrunden så du får tillbaka terminalen.",
                },
                {
                    "question": "Hur mappar du host-port 8080 till container-port 80?",
                    "options": [
                        "-p 80:8080",
                        "-p 8080:80",
                        "-P 8080:80",
                        "--port 8080=80",
                    ],
                    "correct": 1,
                    "explanation": "-p host:container, alltså -p 8080:80 mappar host 8080 till container 80.",
                },
                {
                    "question": "Vad är sant om Docker och firewall?",
                    "options": [
                        "Docker följer alltid UFW-regler",
                        "Docker kringgår UFW/FirewallD",
                        "Docker kräver att firewall är avstängd",
                        "Firewall blockerar alltid Docker",
                    ],
                    "correct": 1,
                    "explanation": "Docker manipulerar iptables direkt och kan kringgå UFW/FirewallD. Var försiktig med port-exponering!",
                },
            ],
        },
        # =============================================================================
        # NOD 9: Docker Compose
        # =============================================================================
        {
            "title": "Docker Compose",
            "slug": "docker-compose",
            "description": "Multi-container-applikationer med docker-compose.yml.",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 120,
            "order_index": 9,
            "content": r"""# Docker Compose

> **TL;DR:** Docker Compose låter dig definiera hela din applikation (web + db + cache + ...) i EN fil. `docker compose up` startar allt. Slut på "jag glömde starta databasen".

---

## Verkligt scenario: Varför Compose?

**Utan Docker Compose:**

```bash
# Varje gång du ska starta projektet...
docker network create myapp
docker run -d --name db --network myapp \
    -v pgdata:/var/lib/postgresql/data \
    -e POSTGRES_PASSWORD=secret \
    postgres:14
docker run -d --name redis --network myapp redis
docker run -d --name web --network myapp \
    -p 8080:3000 \
    -e DATABASE_URL=postgres://db:5432 \
    myapp:latest

# 3 kommandon, lätt att glömma något...
```

**Med Docker Compose:**

```bash
docker compose up -d
# Klart. Allt startar korrekt. Varje gång.
```

---

## Mental modell: docker-compose.yml

```
┌─────────────────────────────────────────────────────────┐
│  docker-compose.yml = Receptbok för din applikation     │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  service:   │  │  service:   │  │  service:   │      │
│  │    web      │  │    db       │  │   redis     │      │
│  │  (nginx)    │  │ (postgres)  │  │  (redis)    │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│         │               │               │               │
│         └───────────────┴───────────────┘               │
│                    network: app                         │
│                                                         │
│              volume: pgdata (beständig)                 │
└─────────────────────────────────────────────────────────┘

Allt definieras i EN YAML-fil.
ETT kommando startar allt.
```

---

## docker-compose.yml - Fullständigt exempel

```yaml
# Fil: docker-compose.yml
version: "3.8"

services:
  # SERVICE 1: Web application
  web:
    image: nginx:alpine
    ports:
      - "8080:80"           # host:container
    volumes:
      - ./html:/usr/share/nginx/html:ro   # bind mount, read-only
    depends_on:
      - api                 # startar EFTER api
    restart: unless-stopped

  # SERVICE 2: API backend
  api:
    build: ./backend        # Bygg från Dockerfile i ./backend
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    restart: unless-stopped

  # SERVICE 3: Database
  db:
    image: postgres:14-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data   # named volume
    restart: unless-stopped

  # SERVICE 4: Cache
  redis:
    image: redis:alpine
    restart: unless-stopped

# Volumes (beständig data)
volumes:
  pgdata:    # Docker hanterar var denna lagras

# Networks (valfritt - Compose skapar automatiskt)
networks:
  default:
    name: myapp-network
```

---

## YAML-grunder (för docker-compose.yml)

```yaml
# KEY: VALUE (kolon + mellanslag!)
name: Said
port: 8080

# LISTA (streck + mellanslag)
ports:
  - "8080:80"
  - "443:443"

# DICTIONARY (nästlad)
environment:
  POSTGRES_USER: said
  POSTGRES_PASSWORD: secret

# ALTERNATIV LISTA-SYNTAX (samma sak)
environment:
  - POSTGRES_USER=said
  - POSTGRES_PASSWORD=secret

# VANLIGT MISSTAG:
ports:
  -"8080:80"     # FEL! Saknas mellanslag efter -
  - "8080:80"    # RÄTT!
```

---

## Compose-kommandon

### Starta och stoppa

```bash
# Starta (måste vara i katalogen med docker-compose.yml)
docker compose up           # Förgrund (se loggar direkt)
docker compose up -d        # Detached (bakgrund)

# Stoppa
docker compose stop         # Stoppa containers (behåll data)
docker compose down         # Stoppa + ta bort containers
docker compose down -v      # + ta bort volumes (VARNING: data försvinner!)
docker compose down --rmi all  # + ta bort images
```

### Status och loggar

```bash
docker compose ps           # Lista alla services
docker compose logs         # Alla loggar
docker compose logs -f      # Follow (som tail -f)
docker compose logs web     # Bara web-servicen
docker compose logs -f --tail=100 api   # Kombinera!
```

### Bygga och skala

```bash
# Bygg/ombygg images
docker compose build        # Bygg alla med 'build:'
docker compose build api    # Bara api-servicen
docker compose up -d --build   # Starta + bygg om

# Skala services
docker compose up -d --scale web=3   # 3 instanser av web
```

### Kör kommandon i service

```bash
docker compose exec db psql -U user mydb   # SQL-prompt
docker compose exec api bash               # Bash i api-containern
docker compose run --rm api python manage.py migrate  # One-off
```

---

## Miljövariabler - Best Practice

### Direkt i compose (OK för icke-känslig)

```yaml
services:
  web:
    environment:
      NODE_ENV: production
      API_URL: http://api:3000
```

### Med .env-fil (REKOMMENDERAT för känslig data)

**docker-compose.yml:**
```yaml
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}  # Hämtas från .env
      POSTGRES_USER: ${DB_USER:-postgres}  # Default om saknas
```

**.env (SAMMA katalog som compose-filen):**
```
DB_PASSWORD=supersecret123
DB_USER=appuser
```

**.gitignore (KRITISKT!):**
```
.env
*.env
.env.*
```

> **Varning:** .env-filen ska ALDRIG committas till git! Lägg till den i .gitignore FÖRST.

---

## depends_on vs healthcheck

### depends_on (bara startordning)

```yaml
services:
  web:
    depends_on:
      - db      # web startar EFTER db
```

**Problem:** db kan ha startat men inte vara REDO att ta emot anslutningar!

### healthcheck (vänta tills redo)

```yaml
services:
  db:
    image: postgres:14
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  web:
    depends_on:
      db:
        condition: service_healthy   # Vänta tills healthcheck OK!
```

---

## Övning 1: Enkel webapp med databas

**Uppgift:**
Skapa docker-compose.yml med:
1. nginx som exponerar port 8080
2. postgres med persistent volume
3. Web ska starta efter db

.

.

.

### Lösning:

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - db

  db:
    image: postgres:14-alpine
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
# Testa
docker compose up -d
docker compose ps
curl localhost:8080
docker compose down
```

---

## Övning 2: Använd miljövariabler

**Uppgift:**
1. Skapa .env-fil med DB_PASSWORD
2. Referera till den i compose
3. Lägg till .env i .gitignore

.

.

.

### Lösning:

**1. .env:**
```
DB_PASSWORD=mysupersecret
```

**2. docker-compose.yml:**
```yaml
version: "3.8"

services:
  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

**3. .gitignore:**
```
.env
```

```bash
# Verifiera att variabeln laddas
docker compose config   # Visar resolved config
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| `docker compose down -v` på prod | Tar bort ALL data! | `docker compose down` (utan -v) |
| Committar .env till git | Läcker credentials | .gitignore FÖRST |
| Tror depends_on väntar | Den väntar bara på start, inte redo | Använd healthcheck |
| YAML utan mellanslag | `- "8080"` ≠ `-"8080"` | Alltid mellanslag efter `-` |
| Glömmer volumes: sektion | Named volumes måste deklareras | Lägg till längst ner |

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Starta allt | `docker compose up -d` |
| Stoppa allt | `docker compose down` |
| Stoppa + radera data | `docker compose down -v` |
| Se status | `docker compose ps` |
| Följ loggar | `docker compose logs -f` |
| Loggar för en service | `docker compose logs api` |
| Bygg om images | `docker compose up -d --build` |
| Kör kommando i service | `docker compose exec db psql` |
| Validera config | `docker compose config` |

""",
            "quiz": [
                {
                    "question": "Vad gör 'docker compose down -v'?",
                    "options": [
                        "Verbose output",
                        "Stoppar och tar bort volumes",
                        "Validerar compose-fil",
                        "Visar version",
                    ],
                    "correct": 1,
                    "explanation": "-v tar även bort namngivna volumes. Utan -v behålls data i volumes. VARNING på produktion!",
                },
                {
                    "question": "Var ska känslig data som lösenord lagras?",
                    "options": [
                        "Direkt i docker-compose.yml",
                        "I en .env-fil (som inte committas)",
                        "Som kommandoradsargument",
                        "I Dockerfile",
                    ],
                    "correct": 1,
                    "explanation": "Känslig data ska lagras i .env-filer som ALDRIG committas till git. Använd ${VARIABEL} i compose.",
                },
                {
                    "question": "Vad är sant om depends_on?",
                    "options": [
                        "Väntar tills servicen är helt redo",
                        "Anger bara startordning, inte redo-status",
                        "Installerar dependencies",
                        "Delar volumes mellan services",
                    ],
                    "correct": 1,
                    "explanation": "depends_on väntar bara på att containern STARTAR, inte att tjänsten är REDO. Använd healthcheck för att vänta ordentligt.",
                },
            ],
        },
        # =============================================================================
        # NOD 10: Systemd
        # =============================================================================
        {
            "title": "Systemd",
            "slug": "systemd",
            "description": "systemctl, journalctl och skapa egna service-filer.",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "order_index": 10,
            "content": r"""# Systemd

> **TL;DR:** Systemd hanterar ALLA tjänster i Linux. `systemctl` startar/stoppar dem, `journalctl` visar loggar. Lär dig skriva egna service-filer och din app startar automatiskt vid boot.

---

## Verkligt scenario: Varför Systemd?

**Utan systemd (gammalt sätt):**

```bash
# SSH in på servern
./start-myapp.sh

# Vad händer om:
# - Du loggar ut? → App dör
# - Servern startar om? → App startar inte
# - App kraschar? → Förblir nere
```

**Med systemd:**

```bash
sudo systemctl enable --now myapp

# Nu:
# - App körs i bakgrunden
# - Startar automatiskt vid boot
# - Startar om automatiskt vid krasch
# - Loggar samlas centralt
```

---

## Mental modell: Hur Systemd fungerar

```
┌─────────────────────────────────────────────────────────┐
│  BOOT-SEKVENS:                                          │
│                                                         │
│  BIOS → Kernel → systemd (PID 1) → Tjänster             │
│                     │                                   │
│                     ├── network.target                  │
│                     ├── sshd.service                    │
│                     ├── nginx.service                   │
│                     ├── postgresql.service              │
│                     └── myapp.service                   │
│                                                         │
│  Systemd är FÖRSTA processen. Den startar allt annat.   │
└─────────────────────────────────────────────────────────┘

Jämför med orkesterledare:
- Systemd = dirigenten
- Services = musiker
- Enable = "du ska vara med på konserten"
- Start = "börja spela nu"
```

---

## systemctl - Hantera tjänster

### Grundläggande kontroll

```bash
# START/STOP/RESTART
sudo systemctl start nginx     # Starta tjänst
sudo systemctl stop nginx      # Stoppa tjänst
sudo systemctl restart nginx   # Stoppa + starta (ny process)
sudo systemctl reload nginx    # Ladda om config (samma process)

# STATUS
systemctl status nginx         # Detaljerad status med senaste loggar
systemctl is-active nginx      # Bara "active" eller "inactive"
systemctl is-enabled nginx     # "enabled" eller "disabled"
```

### Enable vs Start - VIKTIG SKILLNAD

```
┌──────────────────────────────────────────────────────────┐
│  START   = Starta tjänsten NU                           │
│  ENABLE  = Starta tjänsten vid BOOT                     │
│                                                          │
│  Du behöver ofta BÅDA!                                   │
│                                                          │
│  sudo systemctl enable nginx    # Nästa boot            │
│  sudo systemctl start nginx     # Nu                    │
│                                                          │
│  ELLER kombinerat:                                       │
│  sudo systemctl enable --now nginx  # Båda samtidigt!   │
└──────────────────────────────────────────────────────────┘
```

### Lista tjänster

```bash
# Lista alla laddade tjänster
systemctl list-units --type=service

# Bara körande
systemctl list-units --type=service --state=running

# Bara failade
systemctl list-units --type=service --state=failed

# Alla installerade (även icke-laddade)
systemctl list-unit-files --type=service
```

---

## journalctl - Systemloggar

### Varför journalctl?

```
Förr: 100 olika loggfiler i /var/log/
Nu:   journalctl -u nginx (EN plats för allt)
```

### Grundläggande användning

```bash
# Alla loggar (varning: MYCKET!)
journalctl

# Specifik tjänst (VANLIGAST)
journalctl -u nginx
journalctl -u nginx -f          # Follow (som tail -f)

# Senaste X rader
journalctl -u nginx -n 50       # Sista 50 rader
journalctl -u nginx --no-pager  # Utan pager (för scripts)
```

### Filtrera på tid

```bash
# Sedan boot
journalctl -b                   # Nuvarande boot
journalctl -b -1                # Förra boot (debugging efter krasch!)

# Tidsintervall
journalctl --since "1 hour ago"
journalctl --since "2024-01-15 10:00" --until "2024-01-15 12:00"
journalctl --since today
journalctl --since yesterday
```

### Filtrera på prioritet

```bash
# Bara errors och värre
journalctl -p err
journalctl -u nginx -p warning

# Prioriteter: emerg, alert, crit, err, warning, notice, info, debug
```

### Praktiska kombinationer

```bash
# Debug: "Varför startade inte nginx efter reboot?"
journalctl -u nginx -b -p err

# Realtidsövervakning
journalctl -u myapp -f -n 100

# Exportera för analys
journalctl -u nginx --since today > nginx_today.log
```

---

## Skapa egen service-fil

### Varför?

```
Du har byggt en app. Du vill att den:
1. Startar automatiskt vid boot
2. Startar om vid krasch
3. Körs som specifik användare
4. Loggar till journalctl

Lösning: Skapa en service-fil!
```

### Steg-för-steg

**1. Skapa service-filen:**

```bash
sudo nano /etc/systemd/system/myapp.service
```

**2. Innehåll (med förklaringar):**

```ini
[Unit]
Description=My Python Application        # Visas i status
After=network.target                     # Starta EFTER nätverket
After=postgresql.service                 # Och efter postgres
Wants=postgresql.service                 # (mjukt beroende)

[Service]
Type=simple                              # Processen är huvudprocessen
User=appuser                             # KÖR ALDRIG SOM ROOT!
Group=appuser
WorkingDirectory=/opt/myapp              # cd hit först
Environment="PORT=8000"                  # Miljövariabler
EnvironmentFile=/opt/myapp/.env          # Eller läs från fil
ExecStart=/opt/myapp/venv/bin/python app.py   # Kommandot
Restart=always                           # Starta om vid krasch
RestartSec=5                             # Vänta 5 sek innan omstart

# Säkerhet (best practice)
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/opt/myapp/data

[Install]
WantedBy=multi-user.target               # Starta i "normal" mode
```

**3. Aktivera (GLÖM INTE daemon-reload!):**

```bash
# KRITISKT: Systemd måste läsa om filen!
sudo systemctl daemon-reload

# Aktivera och starta
sudo systemctl enable --now myapp

# Verifiera
systemctl status myapp
journalctl -u myapp -f
```

---

## Service-fil sektioner förklarade

### [Unit] - Metadata och beroenden

| Direktiv | Betydelse | Exempel |
|----------|-----------|---------|
| `Description` | Beskrivning (visas i status) | `My Web App` |
| `After` | Starta EFTER dessa (ordning) | `network.target` |
| `Requires` | MÅSTE vara igång (hårt beroende) | `postgresql.service` |
| `Wants` | BÖR vara igång (mjukt beroende) | `redis.service` |

### [Service] - Hur tjänsten körs

| Direktiv | Betydelse | Vanliga värden |
|----------|-----------|----------------|
| `Type` | Processtyp | `simple`, `forking`, `oneshot` |
| `User` | Kör som användare | `www-data`, `appuser` |
| `WorkingDirectory` | Arbetskatalog | `/opt/myapp` |
| `ExecStart` | Startkommando | `/usr/bin/python app.py` |
| `ExecStop` | Stoppkommando (valfritt) | `/opt/myapp/stop.sh` |
| `Restart` | När ska den starta om? | `always`, `on-failure`, `no` |
| `RestartSec` | Sekunder innan omstart | `5` |

### [Install] - Boot-konfiguration

| Direktiv | Betydelse |
|----------|-----------|
| `WantedBy=multi-user.target` | Starta i normalt multi-user mode |
| `WantedBy=graphical.target` | Starta när GUI startar |

---

## Övning 1: Hantera nginx

**Uppgift:**
1. Kontrollera om nginx är installerad och körs
2. Om den körs, se de senaste 20 loggraderna
3. Gör så nginx startar vid boot

.

.

.

### Lösning:

```bash
# 1. Kontrollera status
systemctl status nginx
# eller
systemctl is-active nginx

# 2. Senaste loggar
journalctl -u nginx -n 20

# 3. Aktivera vid boot (om inte redan)
sudo systemctl enable nginx
# Verifiera:
systemctl is-enabled nginx
```

---

## Övning 2: Skapa egen service

**Uppgift:**
Skapa en service som kör ett simpelt Python-script:
- Script: `/opt/demo/app.py`
- Användare: `demo`
- Ska starta om vid krasch
- Ska starta vid boot

.

.

.

### Lösning:

**1. Skapa script (för demo):**
```bash
sudo mkdir -p /opt/demo
sudo useradd -r -s /bin/false demo
echo 'import time
while True:
    print("Running...")
    time.sleep(10)' | sudo tee /opt/demo/app.py
sudo chown -R demo:demo /opt/demo
```

**2. Service-fil:**
```bash
sudo tee /etc/systemd/system/demo.service << 'EOF'
[Unit]
Description=Demo Python App
After=network.target

[Service]
Type=simple
User=demo
WorkingDirectory=/opt/demo
ExecStart=/usr/bin/python3 /opt/demo/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

**3. Aktivera:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now demo
systemctl status demo
journalctl -u demo -f
```

---

## Vanliga misstag på tentan

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| Glömmer `daemon-reload` | Systemd ser inte ändringen | `sudo systemctl daemon-reload` |
| Bara `enable`, inte `start` | Tjänsten startar först vid boot | `enable --now` eller `enable` + `start` |
| Bara `start`, inte `enable` | Tjänsten försvinner vid reboot | Gör båda! |
| `journalctl nginx` | Fel syntax | `journalctl -u nginx` |
| `User=root` i service-fil | Säkerhetsrisk! | Skapa dedikerad användare |
| Relativ path i ExecStart | Funkar inte | Använd ALLTID absolut path |

---

## Snabbreferens

| Uppgift | Kommando |
|---------|----------|
| Starta tjänst | `sudo systemctl start nginx` |
| Stoppa tjänst | `sudo systemctl stop nginx` |
| Starta om | `sudo systemctl restart nginx` |
| Ladda om config | `sudo systemctl reload nginx` |
| Status | `systemctl status nginx` |
| Aktivera vid boot | `sudo systemctl enable nginx` |
| Aktivera + starta nu | `sudo systemctl enable --now nginx` |
| Lista körande | `systemctl list-units --type=service` |
| Visa loggar | `journalctl -u nginx` |
| Följ loggar | `journalctl -u nginx -f` |
| Loggar sedan boot | `journalctl -u nginx -b` |
| Bara errors | `journalctl -u nginx -p err` |
| Ladda om efter ändring | `sudo systemctl daemon-reload` |

""",
            "quiz": [
                {
                    "question": "Vad måste du köra efter att ha ändrat en service-fil?",
                    "options": [
                        "systemctl restart",
                        "systemctl reload",
                        "systemctl daemon-reload",
                        "systemctl refresh",
                    ],
                    "correct": 2,
                    "explanation": "daemon-reload laddar om systemd's konfiguration. Utan det ser systemd inte dina ändringar i service-filer.",
                },
                {
                    "question": "Vilket kommando visar loggar för nginx-tjänsten?",
                    "options": [
                        "cat /var/log/nginx",
                        "journalctl nginx",
                        "journalctl -u nginx",
                        "systemctl logs nginx",
                    ],
                    "correct": 2,
                    "explanation": "journalctl -u (unit) visar loggar för en specifik systemd-tjänst. Glöm inte -u!",
                },
                {
                    "question": "Vad är skillnaden mellan 'enable' och 'start'?",
                    "options": [
                        "Ingen skillnad",
                        "enable = vid boot, start = nu",
                        "start = vid boot, enable = nu",
                        "enable installerar, start konfigurerar",
                    ],
                    "correct": 1,
                    "explanation": "enable gör att tjänsten startar vid boot. start startar den nu. Du behöver ofta båda, eller använd 'enable --now'.",
                },
            ],
        },
        # =============================================================================
        # NOD 11: GREP, SED, AWK - TEXTBEARBETNING
        # =============================================================================
        {
            "title": "grep, sed, awk - Textbearbetning",
            "slug": "grep-sed-awk",
            "content": """
# grep, sed, awk - Textbearbetning i Linux

## TL;DR - Det viktigaste
- **grep** = Sök och filtrera rader som matchar ett mönster
- **sed** = Stream Editor - sök och ersätt text i filer
- **awk** = Kraftfullt för kolumnbaserad data och beräkningar
- De tre amigos av textbearbetning - ofta använda tillsammans med pipes

---

## Varför är textbearbetning så viktigt?

I Linux är **allt text**. Konfigurationsfiler, loggar, output från kommandon - allt är textbaserat. Det betyder att du som sysadmin eller DevOps-ingenjör måste vara expert på att:

1. **Hitta information** i stora textmängder (grep)
2. **Transformera text** automatiskt (sed)
3. **Analysera strukturerad data** som CSV, loggar etc. (awk)

> **Bash Book Kap 5:** "Regular expressions are used by several different Linux commands, including grep and sed."

---

## grep - Global Regular Expression Print

### Grundläggande användning

```bash
# Sök efter ett ord i en fil
grep "error" /var/log/syslog

# Sök i flera filer
grep "error" *.log

# Sök rekursivt i alla filer under en katalog
grep -r "TODO" ./src/
```

### Viktiga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-i` | Case-insensitive | `grep -i "error" log.txt` |
| `-v` | Invertera - visa rader som INTE matchar | `grep -v "debug" log.txt` |
| `-n` | Visa radnummer | `grep -n "error" log.txt` |
| `-c` | Räkna antal matchningar | `grep -c "error" log.txt` |
| `-l` | Visa bara filnamn som matchar | `grep -l "error" *.log` |
| `-r` | Rekursiv sökning | `grep -r "TODO" ./` |
| `-w` | Matcha hela ord | `grep -w "log" file.txt` |
| `-E` | Extended regex (eller använd `egrep`) | `grep -E "error|warn" log.txt` |
| `-o` | Visa bara matchande delen | `grep -o "error" log.txt` |
| `-A n` | Visa n rader EFTER match | `grep -A 3 "error" log.txt` |
| `-B n` | Visa n rader FÖRE match | `grep -B 2 "error" log.txt` |
| `-C n` | Visa n rader före OCH efter | `grep -C 2 "error" log.txt` |

### Praktiska exempel

```bash
# Hitta alla misslyckade SSH-inloggningar
grep "Failed password" /var/log/auth.log

# Hitta processer för en användare (kombinera med ps)
ps aux | grep "nginx"

# Hitta alla IP-adresser i en logg
grep -E "[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}" access.log

# Räkna hur många gånger "error" förekommer
grep -c "error" application.log

# Visa bara unika filer som innehåller "password"
grep -rl "password" /etc/ 2>/dev/null
```

### grep med pipe - Filtrera output

```bash
# Hitta nginx-processer
ps aux | grep nginx

# OBS: Detta visar även själva grep-kommandot!
# Lösning: Filtrera bort grep
ps aux | grep nginx | grep -v grep

# Eller använd hakparenteser-tricket
ps aux | grep [n]ginx
```

---

## sed - Stream Editor

sed läser input rad för rad, applicerar transformationer, och skriver output. Perfekt för automatiserad textredigering.

### Grundläggande syntax

```bash
sed 'kommando' fil
sed -i 'kommando' fil  # -i = "in-place" (ändra filen direkt)
```

### Sök och ersätt (substitution)

```bash
# Syntax: s/sök/ersätt/flaggor

# Ersätt första förekomsten på varje rad
sed 's/gammal/ny/' fil.txt

# Ersätt ALLA förekomster (global)
sed 's/gammal/ny/g' fil.txt

# Case-insensitive ersättning
sed 's/error/ERROR/gi' fil.txt

# Ändra filen direkt (försiktig med detta!)
sed -i 's/localhost/127.0.0.1/g' config.conf

# Med backup innan ändring
sed -i.bak 's/localhost/127.0.0.1/g' config.conf
```

### Radera rader

```bash
# Ta bort rad 5
sed '5d' fil.txt

# Ta bort rad 5-10
sed '5,10d' fil.txt

# Ta bort rader som matchar ett mönster
sed '/^#/d' config.conf      # Ta bort kommentarer
sed '/^$/d' fil.txt          # Ta bort tomma rader

# Ta bort kommentarer OCH tomma rader
sed '/^#/d; /^$/d' config.conf
```

### Visa specifika rader

```bash
# Visa bara rad 5
sed -n '5p' fil.txt

# Visa rad 10-20
sed -n '10,20p' fil.txt

# Visa rader som matchar mönster
sed -n '/error/p' log.txt
```

### Praktiska sed-exempel

```bash
# Byt ut alla tabs mot 4 mellanslag
sed 's/\\t/    /g' fil.txt

# Ta bort trailing whitespace
sed 's/[[:space:]]*$//' fil.txt

# Lägg till text i början av varje rad
sed 's/^/PREFIX: /' fil.txt

# Lägg till text i slutet av varje rad
sed 's/$/ SUFFIX/' fil.txt

# Ändra bara rader som matchar ett mönster
sed '/pattern/s/foo/bar/g' fil.txt
```

---

## awk - Mönstermatchning och databearbetning

awk är ett helt programmeringsspråk för textbearbetning. Det excellerar på **kolumnbaserad data**.

### Grundläggande koncept

```bash
# awk delar automatiskt varje rad i fält (kolumner)
# $0 = hela raden
# $1 = första fältet, $2 = andra, etc.
# NF = antal fält, NR = radnummer
```

### Skriv ut specifika kolumner

```bash
# Skriv ut första kolumnen
awk '{print $1}' fil.txt

# Skriv ut första och tredje kolumnen
awk '{print $1, $3}' fil.txt

# Med formatering
awk '{print $1 " - " $3}' fil.txt
```

### Praktiska awk-exempel

```bash
# Visa användarnamn från /etc/passwd
awk -F: '{print $1}' /etc/passwd

# Hitta stora filer med ls
ls -la | awk '$5 > 1000000 {print $9, $5}'

# Summera en kolumn (t.ex. filstorlekar)
ls -l | awk '{total += $5} END {print "Total:", total}'

# Räkna antal rader
awk 'END {print NR}' fil.txt

# Visa rader längre än 80 tecken
awk 'length > 80' fil.txt
```

### awk med villkor

```bash
# Skriv ut om fält 3 är större än 100
awk '$3 > 100 {print $0}' data.txt

# Skriv ut rader där första fältet är "ERROR"
awk '$1 == "ERROR" {print $0}' log.txt

# Kombinera villkor
awk '$3 > 100 && $4 == "active" {print $1, $2}' data.txt
```

### Field separator (-F)

```bash
# CSV-filer (kommaseparerat)
awk -F, '{print $1, $3}' data.csv

# Kolon-separerat (som /etc/passwd)
awk -F: '{print "User: " $1 ", Shell: " $7}' /etc/passwd

# Tab-separerat
awk -F'\\t' '{print $2}' data.tsv
```

---

## Kombinera grep, sed och awk

Den verkliga kraften kommer när du kombinerar dessa verktyg:

```bash
# Hitta error-rader och extrahera IP-adresser
grep "ERROR" access.log | awk '{print $1}'

# Hitta och räkna unika IP-adresser
grep "404" access.log | awk '{print $1}' | sort | uniq -c | sort -rn

# Ersätt text bara i filer som innehåller ett mönster
grep -l "old_value" *.conf | xargs sed -i 's/old_value/new_value/g'

# Loganalys: Top 10 IP-adresser
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
```

---

## Typiska tentafrågor

**Q: Vad gör kommandot `grep -v "^#" config.conf`?**
A: Visar alla rader som INTE börjar med # (alltså tar bort kommentarer från output)

**Q: Hur ersätter man alla förekomster av "foo" med "bar" i en fil?**
A: `sed 's/foo/bar/g' fil.txt` (g = global, alla förekomster)

**Q: Vad skriver `awk '{print $2}' fil.txt` ut?**
A: Andra kolumnen (fältet) från varje rad

**Q: Vad betyder flaggan -i i sed?**
A: In-place - ändrar filen direkt istället för att skriva till stdout

---

## Sammanfattning

| Verktyg | Bäst för | Minnestrick |
|---------|----------|-------------|
| **grep** | Sök och filtrera | **G**rep = **G**et lines matching |
| **sed** | Sök och ersätt | **S**ed = **S**ubstitute |
| **awk** | Kolumner och beräkningar | **A**wk = **A**nalyze columns |
""",
            "quiz": [
                {
                    "question": "Vad gör kommandot 'grep -v \"error\" log.txt'?",
                    "options": [
                        "Visar rader som innehåller 'error'",
                        "Visar rader som INTE innehåller 'error'",
                        "Visar antal error",
                        "Tar bort rader med error från filen",
                    ],
                    "correct": 1,
                    "explanation": "-v inverterar matchningen. Visar alla rader som INTE matchar mönstret.",
                },
                {
                    "question": "Hur ersätter du ALLA förekomster av 'foo' med 'bar' på varje rad?",
                    "options": [
                        "sed 's/foo/bar/' fil",
                        "sed 's/foo/bar/g' fil",
                        "sed 's/foo/bar/a' fil",
                        "sed 'g/foo/bar/' fil",
                    ],
                    "correct": 1,
                    "explanation": "Flaggan 'g' (global) gör att alla förekomster ersätts, inte bara den första på varje rad.",
                },
                {
                    "question": "Vad skriver 'awk -F: '{print $1}' /etc/passwd' ut?",
                    "options": [
                        "Hela filen",
                        "Första raden",
                        "Användarnamn (första fältet)",
                        "Lösenord",
                    ],
                    "correct": 2,
                    "explanation": "-F: sätter kolon som fältavgränsare. $1 är första fältet, vilket i /etc/passwd är användarnamnet.",
                },
                {
                    "question": "Vad gör 'grep -r \"TODO\" ./'?",
                    "options": [
                        "Söker i aktuell fil",
                        "Söker rekursivt i alla filer under aktuell katalog",
                        "Visar bara filnamn",
                        "Case-insensitive sökning",
                    ],
                    "correct": 1,
                    "explanation": "-r betyder rekursiv sökning - grep letar igenom alla filer i katalogen och alla underkataloger.",
                },
                {
                    "question": "Hur tar man bort alla tomma rader från en fil med sed?",
                    "options": [
                        "sed '/empty/d' fil",
                        "sed 's/^$//' fil",
                        "sed '/^$/d' fil",
                        "sed 'd/^$/' fil",
                    ],
                    "correct": 2,
                    "explanation": "^$ matchar tomma rader (start följt direkt av slut). d = delete. Alltså: ta bort rader som matchar 'tom rad'.",
                },
            ],
        },
        # =============================================================================
        # NOD 12: REGEX - REGULJÄRA UTTRYCK
        # =============================================================================
        {
            "title": "Regex - Reguljära uttryck",
            "slug": "regex",
            "content": """
# Regex - Reguljära uttryck

## TL;DR - Det viktigaste
- Regex = mönster för att matcha text
- `^` = start av rad, `$` = slut av rad
- `.` = vilken tecken som helst, `*` = noll eller fler
- `[]` = teckenklasser, `[^]` = negerad teckenklass
- Används i grep, sed, awk, find och många fler verktyg

---

## Vad är regex?

**Reguljära uttryck** (Regular Expressions, regex) är ett sätt att beskriva textmönster. Istället för att söka efter exakt "error", kan du söka efter "alla rader som börjar med ett datum och innehåller error eller warning".

> **Bash Book Kap 5:** "Regular expressions are a powerful tool for manipulating text and data."

### Varför behöver du kunna regex?

1. **Logganalys** - Hitta specifika mönster i gigabytes av loggar
2. **Datavalidering** - Kontrollera format på email, IP-adresser, etc.
3. **Sök och ersätt** - Avancerad texttransformation med sed
4. **Filtrering** - Grep, awk och många andra verktyg använder regex

---

## Grundläggande metatecken

### Ankare - Var i raden

| Tecken | Betydelse | Exempel |
|--------|-----------|---------|
| `^` | Start av rad | `^Error` matchar "Error" i början |
| `$` | Slut av rad | `done$` matchar "done" i slutet |
| `^$` | Tom rad | Matchar helt tomma rader |

```bash
# Hitta rader som börjar med #
grep "^#" config.conf

# Hitta rader som slutar med ;
grep ";$" script.sh

# Hitta tomma rader
grep "^$" fil.txt
```

### Kvantifierare - Hur många

| Tecken | Betydelse | Exempel |
|--------|-----------|---------|
| `*` | Noll eller fler | `ab*c` matchar "ac", "abc", "abbc" |
| `+` | En eller fler (ERE) | `ab+c` matchar "abc", "abbc" men inte "ac" |
| `?` | Noll eller en (ERE) | `colou?r` matchar "color" och "colour" |
| `{n}` | Exakt n gånger | `a{3}` matchar "aaa" |
| `{n,}` | n eller fler | `a{2,}` matchar "aa", "aaa", "aaaa"... |
| `{n,m}` | Mellan n och m | `a{2,4}` matchar "aa", "aaa", "aaaa" |

> **OBS:** `+`, `?` och `{}` kräver Extended Regular Expressions (ERE).
> Använd `grep -E` eller `egrep` för ERE.

```bash
# Basic regex (BRE) - måste escapa + och ?
grep 'ab\\+c' fil.txt

# Extended regex (ERE) - enklare syntax
grep -E 'ab+c' fil.txt
egrep 'ab+c' fil.txt  # Samma sak
```

### Wildcards och teckenklasser

| Tecken | Betydelse | Exempel |
|--------|-----------|---------|
| `.` | Vilket tecken som helst | `a.c` matchar "abc", "a1c", "a-c" |
| `[abc]` | Ett av tecknen a, b eller c | `[aeiou]` matchar vokaler |
| `[a-z]` | Tecken i intervallet a-z | `[a-z]` matchar små bokstäver |
| `[^abc]` | INTE a, b eller c | `[^0-9]` matchar icke-siffror |
| `[0-9]` | Siffror 0-9 | `[0-9]{3}` matchar tre siffror |

```bash
# Matcha alla filer som börjar med bokstav
ls | grep "^[a-zA-Z]"

# Hitta rader med siffror
grep "[0-9]" fil.txt

# Hitta rader som INTE börjar med siffra
grep "^[^0-9]" fil.txt
```

### POSIX teckenklasser

Dessa fungerar inuti hakparenteser `[[:klass:]]`:

| Klass | Betydelse | Motsvarar |
|-------|-----------|-----------|
| `[[:alpha:]]` | Bokstäver | `[a-zA-Z]` |
| `[[:digit:]]` | Siffror | `[0-9]` |
| `[[:alnum:]]` | Bokstäver och siffror | `[a-zA-Z0-9]` |
| `[[:space:]]` | Whitespace | space, tab, newline |
| `[[:upper:]]` | Stora bokstäver | `[A-Z]` |
| `[[:lower:]]` | Små bokstäver | `[a-z]` |
| `[[:punct:]]` | Skiljetecken | `.,;:!?` etc. |

```bash
# Ta bort alla siffror
sed 's/[[:digit:]]//g' fil.txt

# Hitta ord som börjar med stor bokstav
grep -E '\\b[[:upper:]][[:alpha:]]+\\b' fil.txt
```

---

## Praktiska regex-mönster

### Matcha IP-adresser

```bash
# Enkel IP-matchning (inte perfekt men funkar)
grep -E "[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}" fil.txt

# Förklaring:
# [0-9]{1,3} = 1-3 siffror
# \\. = en punkt (escape-ad eftersom . är metatecken)
```

### Matcha email-adresser

```bash
# Enkel email-matchning
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" fil.txt
```

### Matcha datum (YYYY-MM-DD)

```bash
grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" fil.txt
```

### Matcha MAC-adresser

```bash
grep -E "([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}" fil.txt
```

---

## BRE vs ERE

**BRE** (Basic Regular Expressions) - Standard för grep
**ERE** (Extended Regular Expressions) - `grep -E` eller `egrep`

| Funktion | BRE | ERE |
|----------|-----|-----|
| En eller fler | `\\+` | `+` |
| Noll eller en | `\\?` | `?` |
| Alternativ (or) | Ej tillgänglig | `(cat|dog)` |
| Gruppering | `\\( \\)` | `( )` |
| Kvantifierare | `\\{ \\}` | `{ }` |

```bash
# BRE - krångligare syntax
grep 'http\\(s\\)\\?://' fil.txt

# ERE - enklare syntax
grep -E 'https?://' fil.txt
```

> **Tips:** Använd alltid `grep -E` för att slippa escape-tecken överallt.

---

## Alternativ och gruppering (ERE)

```bash
# Matcha "cat" ELLER "dog"
grep -E "cat|dog" fil.txt

# Matcha "gray" eller "grey"
grep -E "gr(a|e)y" fil.txt

# Matcha filer som slutar på .jpg eller .png
ls | grep -E "\\.(jpg|png)$"
```

---

## Ordgränser

```bash
# \\b = ordgräns (word boundary)

# Matcha ordet "log" men inte "login" eller "catalog"
grep -E "\\blog\\b" fil.txt

# Matcha ord som börjar med "error"
grep -E "\\berror" fil.txt
```

---

## Regex i sed

```bash
# Ersätt alla siffror med X
sed 's/[0-9]/X/g' fil.txt

# Ta bort allt efter # (kommentarer)
sed 's/#.*//' fil.txt

# Extrahera endast siffror
sed 's/[^0-9]//g' fil.txt

# Byt ordning på två ord
echo "hello world" | sed -E 's/(\\w+) (\\w+)/\\2 \\1/'
# Output: world hello
```

### Backreferences

Fånga grupper med `\\(` och `\\)` i BRE eller `(` och `)` i ERE.
Referera tillbaka med `\\1`, `\\2`, etc.

```bash
# Hitta dubblerade ord
grep -E "\\b(\\w+) \\1\\b" fil.txt

# Byt plats på datum YYYY-MM-DD till DD-MM-YYYY
echo "2024-12-22" | sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2})/\\3-\\2-\\1/'
# Output: 22-12-2024
```

---

## Vanliga misstag

### 1. Glömmer escape-tecken

```bash
# FEL - . matchar vilket tecken som helst
grep "192.168.1.1" fil.txt

# RÄTT - escape punkterna
grep "192\\.168\\.1\\.1" fil.txt
```

### 2. Blandar BRE och ERE

```bash
# FEL - + fungerar inte i BRE
grep "ab+c" fil.txt

# RÄTT - använd -E för ERE
grep -E "ab+c" fil.txt
```

### 3. Förväxlar `*` med "ett eller fler"

```bash
# * betyder NOLL eller fler, inte ett eller fler!
grep "ab*c" fil.txt  # Matchar "ac", "abc", "abbc"...

# Använd + för ett eller fler
grep -E "ab+c" fil.txt  # Matchar "abc", "abbc"... men INTE "ac"
```

---

## Sammanfattning - Regex cheat sheet

```
^       Start av rad
$       Slut av rad
.       Vilket tecken som helst
*       Noll eller fler
+       En eller fler (ERE)
?       Noll eller en (ERE)
[]      Teckenklass
[^]     Negerad teckenklass
|       Alternativ (ERE)
()      Gruppering (ERE)
\\b      Ordgräns
\\1      Backreference
```
""",
            "quiz": [
                {
                    "question": "Vad matchar mönstret '^#' ?",
                    "options": [
                        "Rader som innehåller #",
                        "Rader som börjar med #",
                        "Rader som slutar med #",
                        "Tomma rader",
                    ],
                    "correct": 1,
                    "explanation": "^ betyder 'start av rad'. ^# matchar alltså rader som BÖRJAR med #.",
                },
                {
                    "question": "Vad är skillnaden mellan * och + i regex?",
                    "options": [
                        "Ingen skillnad",
                        "* = noll eller fler, + = en eller fler",
                        "* = en eller fler, + = noll eller fler",
                        "* är för siffror, + är för bokstäver",
                    ],
                    "correct": 1,
                    "explanation": "* matchar NOLL eller fler förekomster. + matchar EN eller fler. ab*c matchar 'ac', men ab+c matchar inte 'ac'.",
                },
                {
                    "question": "Vad matchar [^0-9] ?",
                    "options": [
                        "Siffror 0-9",
                        "Tecken som INTE är siffror",
                        "Start av rad följt av siffror",
                        "Endast siffran 0 eller 9",
                    ],
                    "correct": 1,
                    "explanation": "[^...] är en NEGERAD teckenklass. [^0-9] matchar alla tecken som INTE är siffror.",
                },
                {
                    "question": "Hur får du grep att använda Extended Regular Expressions (ERE)?",
                    "options": [
                        "grep -r",
                        "grep -E",
                        "grep -e",
                        "grep --extended",
                    ],
                    "correct": 1,
                    "explanation": "-E aktiverar Extended regex. Du kan också använda egrep som är samma sak som grep -E.",
                },
                {
                    "question": "Vad matchar mönstret 'colou?r' ?",
                    "options": [
                        "Bara 'colour'",
                        "Bara 'color'",
                        "Både 'color' och 'colour'",
                        "Alla ord som innehåller 'colo'",
                    ],
                    "correct": 2,
                    "explanation": "? betyder 'noll eller en'. u? matchar antingen inget u eller ett u. Alltså matchar det både 'color' och 'colour'.",
                },
            ],
        },
        # =============================================================================
        # NOD 13: ARRAYS & PARAMETER EXPANSION
        # =============================================================================
        {
            "title": "Arrays & Parameter Expansion",
            "slug": "arrays-parameter-expansion",
            "content": """
# Arrays & Parameter Expansion i Bash

## TL;DR - Det viktigaste
- **Array** = En variabel som kan hålla flera värden
- Skapa: `arr=(val1 val2 val3)`
- Åtkomst: `${arr[0]}` (index börjar på 0!)
- Alla element: `${arr[@]}`
- **Parameter expansion** = Kraftfulla sätt att manipulera variabler

---

## Varför behöver du arrays?

Tänk dig att du ska loopa igenom en lista av servrar, filer, eller användare. Utan arrays måste du hårdkoda varje värde. Med arrays blir det elegant:

```bash
servers=(web1 web2 db1 db2)
for server in "${servers[@]}"; do
    ssh "$server" "uptime"
done
```

> **Bash Book Kap 10:** "Variables are expanded only when enclosed in double quotes."

---

## Skapa och använda arrays

### Skapa en array

```bash
# Metod 1: Direkt tilldelning
frukt=(äpple banan citron)

# Metod 2: Index för index
färger[0]="röd"
färger[1]="grön"
färger[2]="blå"

# Metod 3: Från kommandoutput
filer=($(ls *.txt))
```

### Åtkomst till element

```bash
# Första elementet (index 0)
echo "${frukt[0]}"    # äpple

# Tredje elementet (index 2)
echo "${frukt[2]}"    # citron

# ALLA element
echo "${frukt[@]}"    # äpple banan citron

# Antal element
echo "${#frukt[@]}"   # 3

# Alla index
echo "${!frukt[@]}"   # 0 1 2
```

### Viktigt: Måsvingar!

```bash
# FEL - utan måsvingar
echo $frukt[0]    # Skriver ut "äpple[0]"

# RÄTT - med måsvingar
echo "${frukt[0]}"    # Skriver ut "äpple"
```

> **OBS:** Utan `{}` tolkar bash `[0]` som vanlig text!

---

## Loopa genom arrays

### Metod 1: for-in loop

```bash
servrar=(web1 web2 db1 db2)

for server in "${servrar[@]}"; do
    echo "Kontrollerar $server..."
done
```

### Metod 2: C-style for loop

```bash
for ((i=0; i<${#servrar[@]}; i++)); do
    echo "Server $i: ${servrar[$i]}"
done
```

### Viktigt: Dubbla citattecken!

```bash
# Problem: filer med mellanslag
filer=("min fil.txt" "din fil.txt")

# FEL - utan citattecken (word splitting)
for f in ${filer[@]}; do
    echo "$f"
done
# Skriver: min, fil.txt, din, fil.txt (4 iterationer!)

# RÄTT - med citattecken
for f in "${filer[@]}"; do
    echo "$f"
done
# Skriver: min fil.txt, din fil.txt (2 iterationer)
```

---

## Modifiera arrays

### Lägg till element

```bash
frukt=(äpple banan)

# Lägg till i slutet
frukt+=(citron)
echo "${frukt[@]}"  # äpple banan citron

# Lägg till på specifikt index
frukt[5]="druva"
echo "${frukt[@]}"  # äpple banan citron druva
echo "${!frukt[@]}" # 0 1 2 5 (index kan ha hål!)
```

### Ta bort element

```bash
# Ta bort specifikt element
unset frukt[1]
echo "${frukt[@]}"  # äpple citron druva

# Ta bort hela arrayen
unset frukt
```

### Slicing (delarray)

```bash
arr=(a b c d e f g)

# Element 2-4 (offset:length)
echo "${arr[@]:2:3}"    # c d e

# Från element 3 till slutet
echo "${arr[@]:3}"      # d e f g
```

---

## Parameter Expansion - Variabelmanipulation

Parameter expansion låter dig manipulera variabelvärden utan externa kommandon.

### Standardvärden

```bash
# ${var:-default} - Använd default om var är odefinierad eller tom
namn=""
echo "${namn:-Okänd}"   # Okänd

# ${var:=default} - Sätt OCH använd default
echo "${namn:=Gäst}"    # Gäst
echo "$namn"            # Gäst (nu satt!)

# ${var:?error} - Visa fel om var är odefinierad
echo "${obligatorisk:?Variabeln måste sättas!}"
```

### Strängmanipulation

```bash
fil="/home/user/dokument/rapport.txt"

# Ta bort prefix (från början)
echo "${fil#*/}"        # home/user/dokument/rapport.txt
echo "${fil##*/}"       # rapport.txt (längsta match)

# Ta bort suffix (från slutet)
echo "${fil%/*}"        # /home/user/dokument
echo "${fil%%/*}"       # (tom - allt efter första /)

# Minnestrick:
# # = från början (# är före $ på tangentbordet)
# % = från slutet (% är efter $ på tangentbordet)
```

### Sök och ersätt

```bash
text="foo bar foo baz foo"

# Ersätt första förekomsten
echo "${text/foo/FOO}"      # FOO bar foo baz foo

# Ersätt ALLA förekomster
echo "${text//foo/FOO}"     # FOO bar FOO baz FOO

# Ta bort (ersätt med ingenting)
echo "${text//foo/}"        # bar baz
```

### Stränglängd och substrings

```bash
text="Hello World"

# Längd
echo "${#text}"             # 11

# Substring (offset:length)
echo "${text:0:5}"          # Hello
echo "${text:6}"            # World
echo "${text: -5}"          # World (OBS: mellanslag före -)
```

### Case conversion (Bash 4+)

```bash
text="Hello World"

# Gör allt till stora bokstäver
echo "${text^^}"            # HELLO WORLD

# Gör allt till små bokstäver
echo "${text,,}"            # hello world

# Första bokstaven stor
echo "${text^}"             # Hello World

# Första bokstaven liten
echo "${text,}"             # hello World
```

---

## Praktiska exempel

### Exempel 1: Backup-skript med array

```bash
#!/bin/bash
# Backup viktiga kataloger

dirs=(/etc /home /var/log)
backup_dir="/backup/$(date +%Y%m%d)"

mkdir -p "$backup_dir"

for dir in "${dirs[@]}"; do
    name="${dir##*/}"  # Ta ut katalognamnet
    tar -czf "$backup_dir/$name.tar.gz" "$dir"
    echo "Backupade $dir till $name.tar.gz"
done
```

### Exempel 2: Validera filnamn

```bash
#!/bin/bash

fil="$1"

# Kolla om det är en .txt-fil
if [[ "${fil##*.}" == "txt" ]]; then
    echo "Det är en textfil"
else
    echo "Det är inte en textfil"
fi

# Byt filändelse
ny_fil="${fil%.txt}.md"
echo "Ny fil: $ny_fil"
```

### Exempel 3: Serverlista med config

```bash
#!/bin/bash

# Definiera servrar med roller
declare -A servers
servers[web1]="nginx"
servers[db1]="postgresql"
servers[cache1]="redis"

for server in "${!servers[@]}"; do
    service="${servers[$server]}"
    echo "Server $server kör $service"
done
```

---

## Associativa arrays (Bash 4+)

Vanliga arrays använder numeriska index. Associativa arrays använder **strängar** som nycklar.

```bash
# Deklarera associativ array
declare -A person

person[namn]="Anna"
person[ålder]="30"
person[stad]="Stockholm"

# Åtkomst
echo "${person[namn]}"        # Anna

# Alla nycklar
echo "${!person[@]}"          # namn ålder stad

# Alla värden
echo "${person[@]}"           # Anna 30 Stockholm
```

---

## Sammanfattning - Parameter Expansion Cheat Sheet

```
${var:-default}     Använd default om var är tom
${var:=default}     Sätt och använd default
${var:+alt}         Använd alt om var har värde
${var:?error}       Visa fel om var är tom

${#var}             Längd av sträng
${var:pos:len}      Substring

${var#pattern}      Ta bort kortaste prefix-match
${var##pattern}     Ta bort längsta prefix-match
${var%pattern}      Ta bort kortaste suffix-match
${var%%pattern}     Ta bort längsta suffix-match

${var/old/new}      Ersätt första
${var//old/new}     Ersätt alla

${var^}             Första bokstaven stor
${var^^}            Alla stora
${var,}             Första bokstaven liten
${var,,}            Alla små
```
""",
            "quiz": [
                {
                    "question": "Hur skriver du ut ALLA element i en array?",
                    "options": [
                        "echo $arr",
                        "echo ${arr}",
                        "echo ${arr[@]}",
                        "echo arr[@]",
                    ],
                    "correct": 2,
                    "explanation": "${arr[@]} expanderar till alla element. Utan @ får du bara första elementet.",
                },
                {
                    "question": "Vad returnerar ${#arr[@]} ?",
                    "options": [
                        "Längden på första elementet",
                        "Antal element i arrayen",
                        "Sista index i arrayen",
                        "Summan av alla element",
                    ],
                    "correct": 1,
                    "explanation": "# ger längd. Med [@] räknar den antal element i hela arrayen.",
                },
                {
                    "question": "Vad gör ${var:-default} ?",
                    "options": [
                        "Sätter var till 'default'",
                        "Returnerar 'default' om var är tom, annars var",
                        "Tar bort 'default' från var",
                        "Lägger till 'default' efter var",
                    ],
                    "correct": 1,
                    "explanation": ":- betyder 'använd default om variabeln är odefinierad eller tom'. Variabeln ändras INTE.",
                },
                {
                    "question": "Om fil='/path/to/file.txt', vad ger ${fil##*/} ?",
                    "options": [
                        "/path/to/file.txt",
                        "/path/to",
                        "file.txt",
                        ".txt",
                    ],
                    "correct": 2,
                    "explanation": "## tar bort längsta prefix som matchar */. Det tar bort allt fram till och med sista /.",
                },
                {
                    "question": "Varför ska man använda 'dubbla citattecken' runt ${arr[@]}?",
                    "options": [
                        "Det är syntaxkrav",
                        "För att bevara element med mellanslag",
                        "Det gör loopen snabbare",
                        "För att undvika säkerhetsrisker",
                    ],
                    "correct": 1,
                    "explanation": "Utan citattecken sker 'word splitting' - element med mellanslag delas upp. Med citattecken bevaras de som ett element.",
                },
            ],
        },
        # =============================================================================
        # NOD 14: DOCKERFILE & DOCKER BUILD
        # =============================================================================
        {
            "title": "Dockerfile & Docker Build",
            "slug": "dockerfile-docker-build",
            "content": """
# Dockerfile & Docker Build

## TL;DR - Det viktigaste
- **Dockerfile** = Recept för att bygga en Docker-image
- `docker build -t namn:tag .` = Bygg image från Dockerfile
- Viktiga instruktioner: FROM, RUN, COPY, WORKDIR, EXPOSE, CMD
- Varje instruktion skapar ett **lager** (layer)
- Optimera genom att minimera lager och använda .dockerignore

---

## Vad är en Dockerfile?

En Dockerfile är en textfil med instruktioner för hur Docker ska bygga en **image**. Tänk på det som ett recept:

- **Base image** = Grundingrediensen (FROM)
- **Instruktioner** = Stegen i receptet (RUN, COPY, etc.)
- **Resultat** = En färdig image du kan köra som container

> **Från grupparbetet:** "Presentationen skall inkludera demonstration av att bygga en Docker-image med docker build."

---

## Grundläggande Dockerfile

```dockerfile
# Börja från en bas-image
FROM ubuntu:22.04

# Sätt arbetskatalog
WORKDIR /app

# Kopiera filer från host till container
COPY . .

# Kör kommandon (installera dependencies)
RUN apt-get update && apt-get install -y python3

# Exponera port
EXPOSE 8080

# Kommando som körs när containern startar
CMD ["python3", "app.py"]
```

---

## Viktiga instruktioner

### FROM - Bas-image

```dockerfile
# Alltid först! Vilken image ska vi bygga på?
FROM ubuntu:22.04
FROM python:3.11-slim
FROM node:18-alpine
FROM nginx:latest
```

**Alpine** = Minimal Linux (~5MB). Perfekt för små images.
**Slim** = Mindre variant utan onödiga paket.

### WORKDIR - Arbetskatalog

```dockerfile
# Sätter katalogen för alla efterföljande kommandon
WORKDIR /app

# Om katalogen inte finns skapas den
WORKDIR /home/user/project
```

### COPY och ADD

```dockerfile
# Kopiera filer från host till container
COPY . .                    # Kopiera allt till WORKDIR
COPY package.json .         # Kopiera specifik fil
COPY src/ /app/src/         # Kopiera katalog

# ADD har extra funktioner (men COPY rekommenderas)
ADD https://example.com/file.tar.gz /tmp/   # Kan ladda ner
ADD archive.tar.gz /app/                     # Packar upp automatiskt
```

> **Best practice:** Använd COPY istället för ADD om du inte behöver de extra funktionerna.

### RUN - Kör kommandon

```dockerfile
# Kör kommandon under bygget
RUN apt-get update
RUN apt-get install -y nginx

# BÄTTRE: Kombinera för färre lager
RUN apt-get update && apt-get install -y \\
    nginx \\
    curl \\
    vim \\
    && rm -rf /var/lib/apt/lists/*
```

### ENV - Miljövariabler

```dockerfile
# Sätt miljövariabler
ENV NODE_ENV=production
ENV PORT=3000

# Kan användas i efterföljande kommandon
RUN echo "Running in $NODE_ENV mode"
```

### EXPOSE - Dokumentera portar

```dockerfile
# Dokumenterar vilka portar containern lyssnar på
EXPOSE 80
EXPOSE 443

# OBS: Exponerar INTE automatiskt - det är dokumentation!
# Du måste fortfarande använda -p vid docker run
```

### CMD och ENTRYPOINT

```dockerfile
# CMD - Standardkommando (kan överskrivas)
CMD ["python", "app.py"]
CMD ["npm", "start"]

# ENTRYPOINT - Huvudkommando (svårare att överskrida)
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argument till ENTRYPOINT
```

**Skillnad:**
- `docker run myimage` → kör CMD
- `docker run myimage other.py` → ersätter CMD med "other.py"
- Med ENTRYPOINT: `docker run myimage other.py` → kör "python other.py"

---

## docker build - Bygg image

### Grundläggande syntax

```bash
# Bygg image från Dockerfile i aktuell katalog
docker build .

# Med namn och tagg
docker build -t myapp:1.0 .

# Från en specifik Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .
```

### Taggar

```bash
# Taggformat: namn:version
docker build -t myapp:latest .
docker build -t myapp:1.0.0 .
docker build -t username/myapp:v2 .

# Flera taggar samtidigt
docker build -t myapp:latest -t myapp:1.0 .
```

### Build context

Punkten (.) i `docker build .` är **build context** - katalogen som Docker har tillgång till.

```bash
# Build context = aktuell katalog
docker build -t myapp .

# Build context = annan katalog
docker build -t myapp ./src
```

---

## Optimera din Dockerfile

### 1. Ordning spelar roll (layer caching)

Docker cachar lager. Om ett lager ändras, byggs alla efterföljande om.

```dockerfile
# DÅLIGT - kopierar allt först (ingen cache vid kodändringar)
COPY . .
RUN npm install

# BRA - dependencies ändras sällan, kod ändras ofta
COPY package*.json ./
RUN npm install
COPY . .
```

### 2. Minimera lager

```dockerfile
# DÅLIGT - 4 lager
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN rm -rf /var/lib/apt/lists/*

# BRA - 1 lager
RUN apt-get update && apt-get install -y \\
    python3 \\
    pip \\
    && rm -rf /var/lib/apt/lists/*
```

### 3. Använd .dockerignore

Skapa `.dockerignore` för att exkludera filer från build context:

```
# .dockerignore
node_modules
.git
.env
*.log
__pycache__
.DS_Store
```

### 4. Multi-stage builds

Bygg i en image, kopiera resultatet till en minimal image:

```dockerfile
# Stage 1: Bygg
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Produktion (minimal image)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Praktiska exempel

### Python-applikation

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Installera dependencies först (bättre caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera kod
COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

### Node.js-applikation

```dockerfile
FROM node:18-alpine

WORKDIR /app

# Dependencies först
COPY package*.json ./
RUN npm ci --only=production

# Kod sedan
COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

### Nginx med custom config

```dockerfile
FROM nginx:alpine

# Ta bort default config
RUN rm /etc/nginx/conf.d/default.conf

# Lägg till egen config
COPY nginx.conf /etc/nginx/conf.d/

# Kopiera statiska filer
COPY html/ /usr/share/nginx/html/

EXPOSE 80
```

---

## Vanliga kommandon

```bash
# Bygg image
docker build -t myapp:1.0 .

# Lista images
docker images

# Kör container från image
docker run -d -p 8080:80 myapp:1.0

# Ta bort image
docker rmi myapp:1.0

# Visa image-lager
docker history myapp:1.0

# Inspektera image
docker inspect myapp:1.0
```

---

## Vanliga misstag

### 1. Glömmer .dockerignore
```bash
# node_modules kopieras in = långsam build + stor image
COPY . .
```

### 2. Kör som root
```dockerfile
# Skapa och använd en icke-root användare
RUN useradd -m appuser
USER appuser
```

### 3. Hardkodade secrets
```dockerfile
# FEL - secrets i image!
ENV DB_PASSWORD=hemligt123

# RÄTT - skicka in vid körning
# docker run -e DB_PASSWORD=xxx myapp
```

---

## Sammanfattning

| Instruktion | Syfte |
|-------------|-------|
| `FROM` | Bas-image |
| `WORKDIR` | Sätt arbetskatalog |
| `COPY` | Kopiera filer |
| `RUN` | Kör kommandon |
| `ENV` | Miljövariabler |
| `EXPOSE` | Dokumentera portar |
| `CMD` | Standardkommando |
| `ENTRYPOINT` | Huvudkommando |
""",
            "quiz": [
                {
                    "question": "Vad gör instruktionen 'FROM python:3.11-slim'?",
                    "options": [
                        "Installerar Python 3.11",
                        "Anger bas-image för bygget",
                        "Laddar ner Python-dokumentation",
                        "Skapar en Python-container",
                    ],
                    "correct": 1,
                    "explanation": "FROM anger vilken bas-image som ska användas. Alla Dockerfiles börjar med FROM.",
                },
                {
                    "question": "Varför ska man kopiera package.json separat FÖRE resten av koden?",
                    "options": [
                        "Det är syntaxkrav",
                        "För att undvika säkerhetsproblem",
                        "För att utnyttja Docker layer caching",
                        "För att package.json alltid måste vara först",
                    ],
                    "correct": 2,
                    "explanation": "Docker cachar lager. Om du kopierar package.json först och kör npm install, behöver det lagret bara byggas om när dependencies ändras - inte vid varje kodändring.",
                },
                {
                    "question": "Vad är skillnaden mellan CMD och ENTRYPOINT?",
                    "options": [
                        "Ingen skillnad",
                        "CMD kan lätt överskrivas, ENTRYPOINT är mer fast",
                        "ENTRYPOINT är för Python, CMD är för Node",
                        "CMD kör före ENTRYPOINT",
                    ],
                    "correct": 1,
                    "explanation": "CMD är standardkommandot som lätt ersätts med argument vid docker run. ENTRYPOINT är huvudkommandot som alltid körs.",
                },
                {
                    "question": "Vad gör 'docker build -t myapp:1.0 .' ?",
                    "options": [
                        "Kör en container",
                        "Bygger image med namn 'myapp' och tagg '1.0'",
                        "Laddar ner en image",
                        "Tar bort en image",
                    ],
                    "correct": 1,
                    "explanation": "-t sätter namn:tagg. Punkten anger build context (aktuell katalog där Dockerfile finns).",
                },
                {
                    "question": "Vad är syftet med en multi-stage build?",
                    "options": [
                        "Att bygga för flera operativsystem",
                        "Att minska den slutliga image-storleken",
                        "Att köra flera containrar samtidigt",
                        "Att använda flera programmeringsspråk",
                    ],
                    "correct": 1,
                    "explanation": "Multi-stage låter dig bygga i en stor image med alla verktyg, men kopiera bara resultatet till en minimal produktions-image.",
                },
            ],
        },
        # =============================================================================
        # NOD 15: GIT - VERSIONSHANTERING
        # =============================================================================
        {
            "title": "Git - Versionshantering",
            "slug": "git-versionshantering",
            "content": """
# Git - Versionshantering

## TL;DR - Det viktigaste
- **git init** = Skapa nytt repo
- **git add** = Staga ändringar
- **git commit** = Spara ändringarna
- **git push/pull** = Synka med remote
- **git branch/merge** = Arbeta med grenar

---

## Varför Git?

Git är det dominerande **versionshanteringssystemet** i IT-världen. Som DevOps-ingenjör kommer du att:

1. **Versionera kod** - Spåra varje ändring
2. **Samarbeta** - Flera personer på samma kodbas
3. **Rollback** - Gå tillbaka till tidigare version om något går fel
4. **CI/CD** - Git-commits triggar automatisk deploy

> **Kursmål 8:** "Beskriva och motivera användningen av Git och dess verktyg"

---

## Grundläggande koncept

### Repository (repo)
En katalog som Git spårar. Innehåller `.git/`-mappen.

### Working directory
Dina lokala filer som du jobbar med.

### Staging area (index)
Mellansteg där du samlar ändringar innan commit.

### Commit
En "snapshot" av dina ändringar med meddelande.

```
Working Dir  →  Staging  →  Local Repo  →  Remote Repo
    ↓            ↓             ↓              ↓
 redigera    git add      git commit      git push
```

---

## Konfigurera Git

```bash
# Sätt ditt namn och email (krävs för commits)
git config --global user.name "Ditt Namn"
git config --global user.email "din@email.se"

# Visa konfiguration
git config --list

# Sätt default branch-namn
git config --global init.defaultBranch main
```

---

## Starta ett repo

### Alternativ 1: Nytt repo

```bash
# Skapa nytt repo i aktuell katalog
git init

# Skapa repo i ny katalog
git init projektnamn
```

### Alternativ 2: Klona existerande

```bash
# Klona från GitHub/GitLab
git clone https://github.com/user/repo.git

# Klona till specifik katalog
git clone https://github.com/user/repo.git min-katalog
```

---

## Det dagliga arbetsflödet

### 1. Kolla status

```bash
git status

# Kortare format
git status -s
```

### 2. Staga ändringar (add)

```bash
# Staga specifik fil
git add fil.txt

# Staga alla ändringar
git add .
git add -A

# Staga bara modifierade filer (inte nya)
git add -u
```

### 3. Commita

```bash
# Commit med meddelande
git commit -m "Lägg till inloggningsfunktion"

# Staga och commita i ett steg (bara modifierade filer)
git commit -am "Fixa bugg i login"
```

### 4. Se historik

```bash
# Visa commit-historik
git log

# Kompakt format
git log --oneline

# Med graf (visar branches)
git log --oneline --graph --all
```

---

## Arbeta med remote

### Lägg till remote

```bash
# Lägg till remote (vanligtvis "origin")
git remote add origin https://github.com/user/repo.git

# Visa remotes
git remote -v
```

### Push och pull

```bash
# Pusha till remote (första gången)
git push -u origin main

# Efterföljande push
git push

# Hämta ändringar
git pull

# Bara hämta utan merge
git fetch
```

---

## Branches (grenar)

Branches låter dig arbeta på features isolerat.

### Hantera branches

```bash
# Visa branches
git branch

# Skapa ny branch
git branch feature-login

# Byt till branch
git checkout feature-login

# Skapa OCH byt i ett kommando
git checkout -b feature-login

# Nyare syntax (Git 2.23+)
git switch feature-login
git switch -c ny-branch  # Skapa och byt
```

### Merge branches

```bash
# Byt till main
git checkout main

# Merga feature-branch in i main
git merge feature-login

# Ta bort branch efter merge
git branch -d feature-login
```

---

## Hantera ändringar

### Ångra ändringar

```bash
# Ångra ändringar i working directory
git checkout -- fil.txt
git restore fil.txt          # Nyare syntax

# Unstage fil
git reset HEAD fil.txt
git restore --staged fil.txt  # Nyare syntax

# Ångra senaste commit (behåll ändringar)
git reset --soft HEAD~1

# Ångra senaste commit (ta bort ändringar)
git reset --hard HEAD~1
```

### Se skillnader

```bash
# Skillnad mellan working dir och staging
git diff

# Skillnad mellan staging och senaste commit
git diff --staged

# Skillnad mellan två commits
git diff abc123 def456
```

### Stash - Spara tillfälligt

```bash
# Spara undan ändringar
git stash

# Visa stash-lista
git stash list

# Återställ senaste stash
git stash pop

# Återställ specifik stash
git stash apply stash@{2}
```

---

## .gitignore

Fil som berättar för Git vilka filer som ska ignoreras:

```bash
# .gitignore exempel

# Ignorera node_modules
node_modules/

# Ignorera alla .log-filer
*.log

# Ignorera .env-filer (känslig data!)
.env
.env.local

# Ignorera build-output
dist/
build/

# Ignorera OS-filer
.DS_Store
Thumbs.db

# Ignorera Python-cache
__pycache__/
*.pyc
```

---

## Praktiska scenarion

### Scenario 1: Börja nytt projekt

```bash
mkdir projekt && cd projekt
git init
echo "# Mitt Projekt" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin https://github.com/user/projekt.git
git push -u origin main
```

### Scenario 2: Feature branch workflow

```bash
# 1. Skapa feature branch
git checkout -b feature/user-auth

# 2. Gör ändringar och commita
git add .
git commit -m "Add user authentication"

# 3. Pusha branchen
git push -u origin feature/user-auth

# 4. Skapa Pull Request på GitHub

# 5. Efter merge, uppdatera lokal main
git checkout main
git pull

# 6. Ta bort lokal feature branch
git branch -d feature/user-auth
```

### Scenario 3: Fixa merge conflict

```bash
# Efter git merge eller git pull med konflikt:
git status  # Visa filer med konflikter

# Öppna fil och fixa konflikten manuellt
# Leta efter: <<<<<<< HEAD, =======, >>>>>>>

# När fixad:
git add konflikt-fil.txt
git commit -m "Resolve merge conflict"
```

---

## Viktiga flaggor

| Kommando | Flagga | Betydelse |
|----------|--------|-----------|
| `git add` | `-A` | Alla ändringar |
| `git commit` | `-m` | Commit-meddelande |
| `git commit` | `-a` | Staga modifierade |
| `git log` | `--oneline` | Kompakt format |
| `git push` | `-u` | Sätt upstream |
| `git branch` | `-d` | Delete branch |
| `git checkout` | `-b` | Skapa och byt |

---

## Vanliga misstag

### 1. Commit utan add

```bash
# FEL - ändringar inte stagade
git commit -m "Fix"  # Inget händer!

# RÄTT
git add .
git commit -m "Fix"
```

### 2. Push utan pull

```bash
# Om remote har nya commits:
git push  # Rejected!

# Lösning:
git pull  # Hämta först
git push  # Sedan push
```

### 3. Känslig data i commit

```bash
# Om du råkar commita .env:
# FLYTTA INTE BARA TILL .gitignore - den finns kvar i historiken!

# Rensa från historik (avancerat):
git filter-branch --force --index-filter \\
  "git rm --cached --ignore-unmatch .env" HEAD
```

---

## Sammanfattning

```
git init              Skapa repo
git clone URL         Klona repo
git add FILE          Staga fil
git commit -m "MSG"   Commita
git push              Pusha till remote
git pull              Hämta från remote
git branch NAME       Skapa branch
git checkout NAME     Byt branch
git merge NAME        Merga branch
git log --oneline     Visa historik
git status            Visa status
```
""",
            "quiz": [
                {
                    "question": "Vad gör kommandot 'git add .' ?",
                    "options": [
                        "Committar alla filer",
                        "Stagar alla ändringar i aktuell katalog",
                        "Skapar en ny branch",
                        "Laddar ner från remote",
                    ],
                    "correct": 1,
                    "explanation": "git add stagar filer för commit. Punkten (.) betyder 'alla filer i aktuell katalog och underkataloger'.",
                },
                {
                    "question": "Vilken ordning är korrekt för att spara ändringar?",
                    "options": [
                        "commit → add → push",
                        "push → add → commit",
                        "add → commit → push",
                        "commit → push → add",
                    ],
                    "correct": 2,
                    "explanation": "Först stagar du (add), sedan committar du lokalt (commit), sedan pushar du till remote (push).",
                },
                {
                    "question": "Vad gör 'git checkout -b feature'?",
                    "options": [
                        "Tar bort branch 'feature'",
                        "Skapar och byter till ny branch 'feature'",
                        "Mergar 'feature' in i main",
                        "Visar historik för 'feature'",
                    ],
                    "correct": 1,
                    "explanation": "-b betyder 'branch'. checkout -b skapar en ny branch och byter till den i ett kommando.",
                },
                {
                    "question": "Vad är syftet med .gitignore?",
                    "options": [
                        "Ignorera commits från andra användare",
                        "Tala om vilka filer Git ska ignorera",
                        "Ignorera merge-konflikter",
                        "Dölja git-historik",
                    ],
                    "correct": 1,
                    "explanation": ".gitignore listar filer och mappar som Git ska ignorera - t.ex. node_modules, .env, build-output.",
                },
                {
                    "question": "Vad gör 'git pull'?",
                    "options": [
                        "Pushar ändringar till remote",
                        "Hämtar och mergar ändringar från remote",
                        "Tar bort remote",
                        "Visar remote-konfiguration",
                    ],
                    "correct": 1,
                    "explanation": "git pull = git fetch + git merge. Den hämtar ändringar från remote och mergar dem in i din lokala branch.",
                },
            ],
        },
        # =============================================================================
        # NOD 16: BACKUP & ARKIVERING
        # =============================================================================
        {
            "title": "Backup & Arkivering",
            "slug": "backup-arkivering",
            "content": """
# Backup & Arkivering i Linux

## TL;DR - Det viktigaste
- **tar** = Packa ihop filer till ett arkiv
- **gzip/bzip2** = Komprimera arkiv
- **rsync** = Synka och kopiera filer effektivt
- **LUKS** = Kryptera diskar och partitioner
- **3-2-1 regeln**: 3 kopior, 2 olika media, 1 offsite

---

## Varför backup?

"Data som inte är backupade är data du är villig att förlora."

Som sysadmin/DevOps är backup **kritiskt**:
1. **Hårdvarufel** - Diskar dör
2. **Mänskliga misstag** - `rm -rf /` händer
3. **Ransomware** - Krypterade filer utan backup = katastrof
4. **Krav** - Många regelverk kräver backup (GDPR, etc.)

> **Kursmål:** Hands-on session med Restic backup visade automatiserad backup.

---

## tar - Tape ARchive

tar packar ihop flera filer till **ett arkiv**. Kombineras ofta med komprimering.

### Skapa arkiv

```bash
# Skapa arkiv (c = create, v = verbose, f = file)
tar -cvf arkiv.tar katalog/

# Med gzip-komprimering (.tar.gz eller .tgz)
tar -czvf arkiv.tar.gz katalog/

# Med bzip2-komprimering (.tar.bz2)
tar -cjvf arkiv.tar.bz2 katalog/

# Med xz-komprimering (.tar.xz) - bäst komprimering
tar -cJvf arkiv.tar.xz katalog/
```

### Packa upp arkiv

```bash
# Packa upp (x = extract)
tar -xvf arkiv.tar

# Packa upp gzip
tar -xzvf arkiv.tar.gz

# Packa upp till specifik katalog
tar -xzvf arkiv.tar.gz -C /mål/katalog/
```

### Lista innehåll

```bash
# Visa vad arkivet innehåller (t = list)
tar -tvf arkiv.tar.gz
```

### Vanliga flaggor

| Flagga | Betydelse |
|--------|-----------|
| `-c` | Create (skapa arkiv) |
| `-x` | Extract (packa upp) |
| `-t` | List (visa innehåll) |
| `-v` | Verbose (visa progress) |
| `-f` | File (ange filnamn) |
| `-z` | Gzip komprimering |
| `-j` | Bzip2 komprimering |
| `-J` | Xz komprimering |
| `-C` | Change directory (mål) |
| `-p` | Preserve permissions |

### Minnestrick för tar

```
C = Create
X = eXtract
T = lisT

z = gzip (som "zip")
j = bzip2 (j = "2" ser ut som j)
```

---

## rsync - Remote Sync

rsync är det smartaste sättet att kopiera filer. Den överför bara **skillnaden** mellan källa och mål.

### Grundläggande användning

```bash
# Synka katalog (notera trailing slash!)
rsync -av källa/ mål/

# Utan trailing slash = kopierar katalogen själv
rsync -av källa mål/   # Skapar mål/källa/

# Visa progress
rsync -av --progress källa/ mål/
```

### Viktiga flaggor

| Flagga | Betydelse |
|--------|-----------|
| `-a` | Archive mode (bevarar allt) |
| `-v` | Verbose |
| `-z` | Komprimera under överföring |
| `-r` | Rekursiv |
| `--delete` | Ta bort filer i mål som inte finns i källa |
| `--dry-run` | Testa utan att ändra |
| `--progress` | Visa överföringsinfo |
| `-e ssh` | Använd SSH |

### rsync över SSH

```bash
# Till remote server
rsync -avz källa/ user@server:/backup/

# Från remote server
rsync -avz user@server:/data/ lokal_katalog/

# Med specifik SSH-port
rsync -avz -e "ssh -p 2222" källa/ user@server:/mål/
```

### Praktiska rsync-exempel

```bash
# Backup hemkatalog
rsync -av --progress ~/ /backup/home/

# Synka och ta bort gamla filer i mål
rsync -av --delete källa/ mål/

# Testa först (dry-run)
rsync -av --dry-run --delete källa/ mål/

# Exkludera vissa filer
rsync -av --exclude='*.log' --exclude='cache/' källa/ mål/
```

---

## Backup-strategier

### 3-2-1 Regeln

- **3** kopior av datan
- **2** olika lagringsmedia (disk + band/cloud)
- **1** kopia offsite (annan plats/cloud)

### Full vs Inkrementell backup

**Full backup:**
- Kopierar allt varje gång
- Enkelt att återställa
- Tar mycket plats och tid

**Inkrementell backup:**
- Kopierar bara ändringar sedan förra backupen
- Snabbt och platseffektivt
- Kräver full + alla inkrement för återställning

### Exempel: Daglig backup-script

```bash
#!/bin/bash
# backup.sh

BACKUP_SRC="/home /etc /var/www"
BACKUP_DST="/backup"
DATE=$(date +%Y%m%d)

# Skapa backup
for dir in $BACKUP_SRC; do
    name=$(basename "$dir")
    tar -czf "$BACKUP_DST/${name}_${DATE}.tar.gz" "$dir"
done

# Ta bort backups äldre än 30 dagar
find "$BACKUP_DST" -name "*.tar.gz" -mtime +30 -delete

echo "Backup klar: $DATE"
```

---

## LUKS - Linux Unified Key Setup

LUKS är standard för **diskkryptering** i Linux.

### Varför kryptering?

- **Stulna laptops** - Data skyddad utan lösenord
- **Kasserade diskar** - Ingen kan läsa gammal data
- **Compliance** - Många regelverk kräver kryptering

### LUKS-kommandon

```bash
# Formatera partition med LUKS
sudo cryptsetup luksFormat /dev/sdb1

# Öppna krypterad partition
sudo cryptsetup open /dev/sdb1 krypterad_disk

# Nu finns den på /dev/mapper/krypterad_disk
# Skapa filsystem
sudo mkfs.ext4 /dev/mapper/krypterad_disk

# Montera
sudo mount /dev/mapper/krypterad_disk /mnt/secure

# Stäng när klar
sudo umount /mnt/secure
sudo cryptsetup close krypterad_disk
```

### LUKS-workflow

```
1. cryptsetup luksFormat  →  Kryptera partition
2. cryptsetup open        →  "Lås upp" (skapar /dev/mapper/namn)
3. mount                  →  Montera som vanligt
4. ... använd ...
5. umount                 →  Avmontera
6. cryptsetup close       →  "Lås" igen
```

### Hantera LUKS-nycklar

```bash
# Lägg till backup-lösenord (max 8 key slots)
sudo cryptsetup luksAddKey /dev/sdb1

# Ta bort lösenord
sudo cryptsetup luksRemoveKey /dev/sdb1

# Visa info om LUKS-header
sudo cryptsetup luksDump /dev/sdb1
```

---

## Praktiska backup-scenarier

### Scenario 1: Webbserver backup

```bash
#!/bin/bash
# Backup webbserver

DATE=$(date +%Y%m%d_%H%M)
BACKUP_DIR="/backup/$DATE"

mkdir -p "$BACKUP_DIR"

# Backup webbfiler
tar -czf "$BACKUP_DIR/www.tar.gz" /var/www/

# Backup databas
mysqldump --all-databases > "$BACKUP_DIR/mysql.sql"
gzip "$BACKUP_DIR/mysql.sql"

# Backup nginx-config
tar -czf "$BACKUP_DIR/nginx.tar.gz" /etc/nginx/

# Synka till offsite
rsync -avz "$BACKUP_DIR/" backup@offsite:/backup/
```

### Scenario 2: Inkrementell med rsync

```bash
#!/bin/bash
# Inkrementell backup med hard links

BACKUP_SRC="/home"
BACKUP_DST="/backup"
DATE=$(date +%Y%m%d)
LATEST="$BACKUP_DST/latest"

# Skapa backup med hard links till senaste
rsync -av --link-dest="$LATEST" "$BACKUP_SRC/" "$BACKUP_DST/$DATE/"

# Uppdatera "latest" symlink
rm -f "$LATEST"
ln -s "$BACKUP_DST/$DATE" "$LATEST"
```

---

## Restore - Återställning

En backup är värdelös om du inte kan återställa!

### Återställ från tar

```bash
# Återställ allt
tar -xzvf backup.tar.gz -C /

# Återställ enskild fil
tar -xzvf backup.tar.gz path/till/fil.txt

# Lista först för att se vad som finns
tar -tzvf backup.tar.gz | grep "sökord"
```

### Återställ med rsync

```bash
# Från backup till original plats
rsync -av /backup/home/ /home/

# Dry-run först!
rsync -av --dry-run /backup/home/ /home/
```

---

## Vanliga misstag

### 1. Testar aldrig restore

```bash
# Schemalägg restore-test!
# Backup utan restore-test = falsk trygghet
```

### 2. Glömmer trailing slash i rsync

```bash
# MED slash - kopierar innehållet
rsync -av källa/ mål/

# UTAN slash - kopierar katalogen
rsync -av källa mål/  # Skapar mål/källa/
```

### 3. Backup på samma disk

```bash
# FEL - om disken dör förlorar du allt
cp -r /data /data_backup

# RÄTT - annan disk/server
rsync -av /data/ /mnt/extern_disk/backup/
rsync -av /data/ backup@remote:/backup/
```

---

## Sammanfattning

| Verktyg | Användning |
|---------|------------|
| `tar -czvf` | Skapa komprimerat arkiv |
| `tar -xzvf` | Packa upp arkiv |
| `rsync -av` | Synka/kopiera effektivt |
| `cryptsetup` | LUKS-kryptering |

| Koncept | Förklaring |
|---------|------------|
| 3-2-1 | 3 kopior, 2 media, 1 offsite |
| Full backup | Allt varje gång |
| Inkrementell | Bara ändringar |
| LUKS | Diskkryptering |
""",
            "quiz": [
                {
                    "question": "Vad gör kommandot 'tar -xzvf arkiv.tar.gz'?",
                    "options": [
                        "Skapar ett komprimerat arkiv",
                        "Packar upp ett gzip-komprimerat arkiv",
                        "Listar innehållet i arkivet",
                        "Komprimerar en katalog",
                    ],
                    "correct": 1,
                    "explanation": "x = extract, z = gzip, v = verbose, f = file. Alltså: packa upp ett gzip-komprimerat arkiv.",
                },
                {
                    "question": "Vad är fördelen med rsync jämfört med cp?",
                    "options": [
                        "rsync är snabbare på att kopiera nya filer",
                        "rsync överför bara skillnaden mellan källa och mål",
                        "rsync komprimerar automatiskt",
                        "rsync kräver mindre diskutrymme",
                    ],
                    "correct": 1,
                    "explanation": "rsync jämför källa och mål och överför bara ändrade delar. Perfekt för backup då det sparar tid och bandbredd.",
                },
                {
                    "question": "Vad innebär 3-2-1 regeln för backup?",
                    "options": [
                        "3 dagars intervall, 2 veckor retention, 1 månad arkiv",
                        "3 kopior, 2 olika media, 1 kopia offsite",
                        "3 servrar, 2 datacenter, 1 cloud",
                        "3 full, 2 inkrementell, 1 differential",
                    ],
                    "correct": 1,
                    "explanation": "3-2-1: Ha 3 kopior av din data, på 2 olika typer av media, med 1 kopia på annan fysisk plats.",
                },
                {
                    "question": "Vad används LUKS till?",
                    "options": [
                        "Backup-schemaläggning",
                        "Filkomprimering",
                        "Diskkryptering",
                        "Nätverksövervakning",
                    ],
                    "correct": 2,
                    "explanation": "LUKS (Linux Unified Key Setup) är standard för diskkryptering i Linux. Skyddar data på viloläge.",
                },
                {
                    "question": "Varför ska man köra 'rsync --dry-run' först?",
                    "options": [
                        "För att synka snabbare",
                        "För att komprimera data",
                        "För att se vad som kommer hända utan att ändra",
                        "För att kryptera överföringen",
                    ],
                    "correct": 2,
                    "explanation": "--dry-run visar vad rsync SKULLE göra utan att faktiskt ändra något. Perfekt för att verifiera innan --delete!",
                },
            ],
        },
    ],
}
