"""
Linux 24/7 — Komplett Linux för DevOps
======================================

20 lektioner från grunderna till avancerad systemadministration.
Varje lektion innehåller TOP 10 kommandon, progression från nybörjare till avancerat,
och verkliga DevOps-scenarier.
"""

MODULE = {
    # ==========================================================================
    # METADATA
    # ==========================================================================
    "name": "Linux 24/7",
    "slug": "linux-247",
    "description": "Komplett Linux för DevOps – 20 lektioner från grunderna till avancerad systemadministration. TOP 10 kommandon, progression från nybörjare till avancerat, och verkliga DevOps-scenarier.",

    "track_slug": "foundation",
    "order_index": 1,
    "difficulty": "intermediate",
    "estimated_hours": 40,
    "prerequisites": [],
    "icon": "🐧",
    "color": "#FCC624",

    # ==========================================================================
    # TASKS (Nodes) — 20 lektioner
    # ==========================================================================
    "tasks": [
        # ======================================================================
        # NODE 1: File System Essentials
        # ======================================================================
        {
            "title": "File System Essentials",
            "slug": "file-system-essentials",
            "description": "Navigera filsystemet, hantera filer och kataloger, hitta filer och analysera diskutrymme.",
            "difficulty": "easy",
            "estimated_minutes": 60,
            "xp_reward": 100,
            "content": """# 1. File System Essentials

## Varför detta är avgörande för DevOps

Filsystemet är din arbetsyta. Varje dag navigerar du mellan konfigurationsfiler i `/etc`, loggar i `/var/log`, scripts i `/opt` och hemkataloger i `/home`. Behärskar du inte dessa kommandon kommer du att kämpa med allt annat. Det här är grunden som allt annat vilar på.

## 🏆 TOP 10 – Kommandon du använder dagligen

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `ls -lah` | Se alla filer med detaljer och storlekar |
| 2 | `cd -` | Hoppa tillbaka till förra katalogen |
| 3 | `cp -r` | Kopiera kataloger rekursivt |
| 4 | `mv` | Flytta filer eller byt namn |
| 5 | `rm -rf` | Ta bort allt (⚠️ försiktigt!) |
| 6 | `mkdir -p` | Skapa hela katalogstrukturer |
| 7 | `find` | Sök efter filer överallt |
| 8 | `du -sh` | Kolla katalogstorlek |
| 9 | `df -h` | Kolla ledigt diskutrymme |
| 10 | `tail -f` | Följ loggar i realtid |

---

## Navigation – Förflytta dig i filsystemet

### pwd – Var är jag?

```bash
pwd                             # Visar din nuvarande position, t.ex. /home/said/projects
```

### cd – Byt katalog

```bash
# NYBÖRJARE
cd /var/log                     # Gå till en specifik katalog med absolut sökväg
cd ..                           # Gå upp en nivå (från /var/log till /var)
cd                              # Gå direkt till din hemkatalog
cd ~                            # Samma sak – ~ betyder alltid "hem"

# MELLANLIGGANDE
cd -                            # ⭐ Gå tillbaka till FÖRRA katalogen (superviktigt!)
cd ~/projects                   # Gå till projects i hemkatalogen
cd ../..                        # Gå upp två nivåer
cd /var/log && ls               # Gå till katalog OCH lista innehållet

# AVANCERAT
pushd /etc                      # Spara nuvarande plats på en "stack", gå till /etc
popd                            # Hoppa tillbaka till sparad plats
cd "katalog med mellanslag"     # Hantera katalognamn med mellanslag
```

**💡 DevOps-tips:** `cd -` är ovärderligt när du hoppar mellan två kataloger, t.ex. mellan `/etc/nginx` och `/var/log/nginx`.

---

## Lista filer – ls i alla former

```bash
# NYBÖRJARE
ls                              # Enkel lista över filer och kataloger
ls -l                           # "Long" format – visar rättigheter, ägare, storlek, datum
ls -a                           # Visa ALLA filer, även dolda (som börjar med .)
ls -la                          # Kombinera: long + alla filer

# MELLANLIGGANDE
ls -lh                          # Human-readable storlekar (KB, MB, GB istället för bytes)
ls -lah                         # ⭐ FAVORITEN: Allt + läsbart + dolda filer
ls -lt                          # Sortera efter tid (nyaste först)
ls -ltr                         # Sortera efter tid, omvänt (äldst först)
ls -lS                          # Sortera efter storlek (störst först)
ls -R                           # Rekursivt – visa alla undermappar också

# AVANCERAT
ls -lai                         # Visa inode-nummer (för att identifiera hårda länkar)
ls -d */                        # Lista BARA kataloger, inga filer
ls -la *.log                    # Wildcard: visa alla .log-filer
ls -la | grep "^d"              # Visa bara kataloger (börjar med 'd')
ls -la | grep ".conf"           # Visa filer som innehåller .conf
```

**💡 DevOps-scenario:** `ls -lht /var/log` visar dig senast modifierade loggfiler – perfekt för att hitta var aktivitet sker.

---

## Visa filinnehåll – Läs filer på olika sätt

```bash
# NYBÖRJARE
cat fil.txt                     # Visa hela filens innehåll (bäst för små filer)
cat -n fil.txt                  # Samma fast med radnummer
head fil.txt                    # Visa första 10 raderna
tail fil.txt                    # Visa sista 10 raderna

# MELLANLIGGANDE
less fil.txt                    # Bläddra genom filen (q = avsluta, / = sök)
head -n 30 fil.txt              # Visa första 30 raderna
tail -n 50 fil.txt              # Visa sista 50 raderna
tail -f /var/log/syslog         # ⭐ FÖLJ filen live – ny output visas direkt!

# AVANCERAT
tail -F /var/log/app.log        # Som -f men följer även om filen roteras (logrotate)
tail -f fil.log | grep ERROR    # Följ OCH filtrera – visa bara ERROR-rader
tac fil.txt                     # cat baklänges – sista raden först
zcat fil.gz                     # Visa innehåll i gzippad fil utan att packa upp
```

**💡 DevOps-scenario:** `tail -f /var/log/nginx/error.log` är något du kör dagligen för att övervaka fel i realtid.

---

## Kopiera filer – cp

```bash
# NYBÖRJARE
cp fil.txt kopia.txt            # Skapa en kopia av filen
cp fil.txt /backup/             # Kopiera till annan katalog (behåll namn)
cp fil.txt /backup/nytt.txt     # Kopiera med nytt namn

# MELLANLIGGANDE
cp -r katalog/ backup/          # ⭐ Rekursivt – kopiera katalog + allt innehåll
cp -v fil.txt kopia.txt         # Verbose – visa vad som händer
cp -i fil.txt kopia.txt         # Interaktiv – fråga innan överskrivning
cp -p fil.txt kopia.txt         # Preserve – behåll datum och rättigheter

# AVANCERAT
cp -a katalog/ backup/          # Archive mode – bevarar ALLT (rättigheter, länkar, etc.)
cp -u *.txt /backup/            # Update – kopiera bara om källan är nyare
```

**💡 DevOps-scenario:** ALLTID backup innan du ändrar config:
```bash
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d_%H%M%S)
```

---

## Flytta & byt namn – mv

```bash
# NYBÖRJARE
mv fil.txt nytt_namn.txt        # Byt namn på fil
mv fil.txt /annan/katalog/      # Flytta fil till annan plats
mv gammal/ ny/                  # Byt namn på katalog

# MELLANLIGGANDE
mv -v fil.txt /backup/          # Verbose – visa vad som händer
mv -i fil.txt mål.txt           # Interaktiv – fråga innan överskrivning
mv -n fil.txt mål.txt           # No-clobber – överskriv ALDRIG befintlig fil
```

**💡 Tips:** Till skillnad från `cp` behöver `mv` ingen `-r` flagga för kataloger.

---

## Ta bort filer – rm ⚠️

```bash
# NYBÖRJARE
rm fil.txt                      # Ta bort en fil
rm -i fil.txt                   # ⭐ Interaktiv – bekräfta först (rekommenderas!)

# MELLANLIGGANDE
rm -r katalog/                  # Rekursivt – ta bort katalog + innehåll
rm -v fil.txt                   # Verbose – visa vad som tas bort
rm *.log                        # Wildcard – ta bort alla .log-filer

# AVANCERAT (⚠️ EXTREM FÖRSIKTIGHET)
rm -rf katalog/                 # ⚠️ FARLIGASTE KOMMANDOT – Force + Recursive
```

**🛑 SÄKERHETSREGLER:**
1. **ALDRIG:** `rm -rf /` – raderar HELA systemet
2. **ALLTID:** Dubbelkolla sökvägen innan du trycker Enter
3. **TIPS:** Kör `ls` först för att se vad som matchar

---

## Skapa kataloger & filer – mkdir & touch

```bash
# NYBÖRJARE
mkdir projekt                   # Skapa en katalog
touch fil.txt                   # Skapa tom fil (eller uppdatera timestamp)

# MELLANLIGGANDE
mkdir -p parent/child/grand     # ⭐ Skapa hela kedjan av kataloger på en gång
mkdir katalog1 katalog2         # Skapa flera kataloger samtidigt

# AVANCERAT – BRACE EXPANSION
mkdir -p projekt/{src,bin,docs,tests}           # Skapa projektstruktur
touch fil{1..5}.txt             # Skapa fil1.txt, fil2.txt, ... fil5.txt
```

**💡 DevOps-scenario:** Skapa standardprojektstruktur med ett kommando:
```bash
mkdir -p myapp/{src,tests,docs,config,scripts,logs,deploy}
```

---

## Hitta filer – find, locate, which

```bash
# NYBÖRJARE
find . -name "fil.txt"          # Hitta fil i nuvarande katalog + underkataloger
find /var -name "*.log"         # Hitta alla .log-filer under /var
which nginx                     # Var ligger kommandot nginx?

# MELLANLIGGANDE
find . -iname "*.TXT"           # Case-insensitive sökning
find . -type f                  # Hitta bara filer (inte kataloger)
find . -type d                  # Hitta bara kataloger
find /var -mtime -1             # Modifierade senaste 24 timmarna
find /var -mtime +7             # Modifierade för mer än 7 dagar sen

# AVANCERAT
find . -size +100M              # Filer större än 100MB
find . -name "*.tmp" -delete    # ⚠️ Hitta OCH ta bort
find . -name "*.sh" -exec chmod +x {} \\;  # Kör kommando på varje resultat
```

**💡 DevOps-scenarier:**
```bash
find /var/log -name "*.log" -mtime +30 -delete   # Rensa loggar äldre än 30 dagar
find /home -type f -size +500M                    # Hitta stora filer
```

---

## Diskutrymme – df & du

```bash
# NYBÖRJARE
df -h                           # ⭐ Ledigt utrymme (human-readable)
du -sh                          # ⭐ Summary – total storlek på katalogen

# MELLANLIGGANDE
df -hT                          # Med filsystemtyp
du -sh *                        # Storlek på alla items i katalogen
du -h --max-depth=1             # Bara första nivån

# AVANCERAT
du -sh * | sort -h              # Sortera efter storlek
ncdu /var                       # ⭐ Interaktiv diskanalys (installeras separat)
```

**💡 DevOps-scenario:** Hitta vad som äter diskutrymme:
```bash
du -h --max-depth=1 /var | sort -h | tail -10
```

---

## Länkar – ln

```bash
ln -s /path/to/original symlink    # ⭐ Skapa symbolisk länk
ln -sf /new/path symlink           # Force – ersätt befintlig länk
readlink symlink                   # Visa vad länken pekar på
```

**💡 DevOps-användning – versionshantering:**
```bash
ln -sf /opt/app-v2.0 /opt/app-current    # Peka på version 2.0
ln -sf /opt/app-v1.9 /opt/app-current    # Rollback till 1.9
```

---

## Wildcards & Globbing

```bash
*                               # Matchar ALLT (noll eller fler tecken)
?                               # Matchar exakt ETT tecken
[abc]                           # Matchar a, b eller c
[0-9]                           # Matchar en siffra

# EXEMPEL
ls *.txt                        # Alla .txt-filer
rm *.tmp                        # Ta bort alla .tmp-filer
cp /etc/*.conf ~/backup/        # Kopiera alla config-filer
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando visar alla filer inklusive dolda med läsbara storlekar?",
                    "options": ["ls -l", "ls -lah", "ls -a", "dir"],
                    "correct": 1
                },
                {
                    "question": "Vad gör kommandot 'cd -'?",
                    "options": ["Går till hemkatalogen", "Går till root", "Går till förra katalogen", "Skapar katalog"],
                    "correct": 2
                },
                {
                    "question": "Vilket kommando skapar en hel katalogstruktur på en gång?",
                    "options": ["mkdir", "mkdir -p", "touch", "create -r"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 2: Text Processing & Search
        # ======================================================================
        {
            "title": "Text Processing & Search",
            "slug": "text-processing-search",
            "description": "Sök, filtrera och manipulera text med grep, awk, sed och pipes.",
            "difficulty": "medium",
            "estimated_minutes": 60,
            "xp_reward": 120,
            "content": """# 2. Text Processing & Search

## Varför detta är avgörande för DevOps

Loggar, konfigurationsfiler, output från kommandon – allt är text. Din förmåga att snabbt söka, filtrera och manipulera text avgör hur effektiv du är.

## 🏆 TOP 10 – Kommandon du använder dagligen

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `grep -i` | Sök case-insensitive |
| 2 | `grep -r` | Sök rekursivt i kataloger |
| 3 | `grep -A/-B/-C` | Visa kontext runt träffar |
| 4 | `awk '{print $1}'` | Extrahera kolumner |
| 5 | `sed 's/old/new/g'` | Sök och ersätt |
| 6 | `sort | uniq -c` | Sortera och räkna unika |
| 7 | `cut -d',' -f1` | Klipp ut kolumner |
| 8 | `|` (pipe) | Koppla ihop kommandon |
| 9 | `>` och `>>` | Spara output till fil |
| 10 | `wc -l` | Räkna rader |

---

## grep – Sök i text

```bash
# NYBÖRJARE
grep "error" logfile.log        # Sök efter "error" i filen
grep -i "error" logfile.log     # ⭐ Case-insensitive
grep -v "success" logfile.log   # Invertera – visa rader som INTE matchar
grep -n "error" logfile.log     # Visa radnummer för varje träff
grep -c "error" logfile.log     # Räkna antal träffar

# MELLANLIGGANDE
grep -r "error" /var/log/       # ⭐ Rekursiv sökning
grep -A 5 "error" logfile.log   # Visa 5 rader EFTER varje träff
grep -B 5 "error" logfile.log   # Visa 5 rader FÖRE varje träff
grep -C 5 "error" logfile.log   # Visa 5 rader FÖRE och EFTER

# AVANCERAT
grep -E "error|warning" log     # Extended regex – ELLER
grep -w "error" logfile.log     # Hela ord – matchar inte "errors"

# MED PIPES
ps aux | grep nginx             # Hitta nginx-processer
tail -f logfile.log | grep error   # Följ logg och filtrera
```

**💡 DevOps-scenarier:**
```bash
# Hitta fel med kontext
grep -A 10 -B 5 "fatal" /var/log/app.log

# Följ logg i realtid och filtrera
tail -f /var/log/app.log | grep --line-buffered -i error
```

---

## awk – Kolumnbaserad textbearbetning

```bash
# NYBÖRJARE
awk '{print $1}' fil.txt        # Skriv ut första kolumnen
awk '{print $NF}' fil.txt       # Skriv ut SISTA kolumnen
awk '{print $1, $3}' fil.txt    # Skriv ut kolumn 1 och 3

# MELLANLIGGANDE
awk '{print $1}' access.log | sort | uniq -c | sort -rn   # ⭐ Räkna IP-adresser

# MED SEPARATORER
awk -F',' '{print $1}' fil.csv          # Komma som separator (CSV)
awk -F':' '{print $1}' /etc/passwd      # Kolon som separator

# MED VILLKOR
awk '$9 == 404 {print}' access.log      # Visa bara 404-errors
awk '$9 >= 500 {print $1, $9}' access.log   # 5xx errors
```

**💡 DevOps-scenarier:**
```bash
# Top 10 IP-adresser i access log
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10
```

---

## sed – Sök och ersätt

```bash
# NYBÖRJARE
sed 's/gammal/ny/' fil.txt              # Ersätt FÖRSTA förekomsten per rad
sed 's/gammal/ny/g' fil.txt             # ⭐ Ersätt ALLA förekomster

# MELLANLIGGANDE
sed -i 's/gammal/ny/g' fil.txt          # ⭐ In-place – ändra filen direkt!
sed -i.bak 's/gammal/ny/g' fil.txt      # In-place MED backup

# TA BORT RADER
sed '/^#/d' fil.txt                     # Ta bort kommentarsrader
sed '/^$/d' fil.txt                     # Ta bort tomma rader
```

**💡 DevOps-scenarier:**
```bash
# Ändra port i config
sed -i 's/listen 80;/listen 8080;/g' /etc/nginx/nginx.conf
```

---

## sort & uniq – Sortera och räkna

```bash
sort fil.txt                    # Alfabetisk sortering
sort -n fil.txt                 # Numerisk sortering
sort -r fil.txt                 # Reverse
sort -u fil.txt                 # Unique – ta bort dubbletter

uniq -c fil.txt                 # ⭐ Räkna förekomster (kräver sorterad input!)

# KLASSISK PIPELINE
cat access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn | head -10
```

---

## Pipes & Redirection

```bash
# PIPES
command1 | command2             # Output från 1 blir input till 2
ps aux | grep nginx | wc -l     # Pipeline: processer → filtrera → räkna

# REDIRECTION
command > fil.txt               # Skriv output till fil (ÖVERSKRIVER)
command >> fil.txt              # Lägg till i fil (APPEND)
command 2> error.log            # Redirect errors
command > out.log 2>&1          # BÅDE stdout och stderr till samma fil
command 2>/dev/null             # Kasta bort felmeddelanden

# TEE – Visa OCH spara
command | tee fil.txt           # ⭐ Visa output OCH spara till fil
```
""",
            "quiz": [
                {
                    "question": "Vilket grep-alternativ söker case-insensitive?",
                    "options": ["-v", "-i", "-r", "-c"],
                    "correct": 1
                },
                {
                    "question": "Vad gör 'awk '{print $NF}''?",
                    "options": ["Skriver ut första kolumnen", "Skriver ut sista kolumnen", "Skriver ut alla kolumner", "Räknar kolumner"],
                    "correct": 1
                },
                {
                    "question": "Vad gör >> jämfört med >?",
                    "options": ["Överskriver filen", "Lägger till i filen", "Skapar ny fil", "Tar bort filen"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 3: Process Management
        # ======================================================================
        {
            "title": "Process Management",
            "slug": "process-management",
            "description": "Hantera processer, döda hängande program och kör bakgrundsjobb.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 110,
            "content": """# 3. Process Management

## Varför detta är avgörande för DevOps

Processer är hjärtat i varje Linux-system. Du måste kunna se vad som körs, identifiera resurstjuvar, starta och stoppa tjänster, och hantera hängande processer.

## 🏆 TOP 10 – Kommandon du använder dagligen

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `ps aux` | Visa alla processer |
| 2 | `top` / `htop` | Realtidsövervakning |
| 3 | `kill PID` | Avsluta process gracefully |
| 4 | `kill -9 PID` | Tvinga avslut |
| 5 | `pkill namn` | Döda efter processnamn |
| 6 | `pgrep namn` | Hitta PID efter namn |
| 7 | `nohup cmd &` | Kör i bakgrund, överlever logout |
| 8 | `jobs` / `fg` / `bg` | Hantera bakgrundsjobb |
| 9 | `ps aux --sort=-%mem` | Hitta minnesslukare |
| 10 | `systemctl status` | Kontrollera service-status |

---

## Visa processer

```bash
# NYBÖRJARE
ps aux                          # ⭐ ALLA processer på systemet
ps aux | grep nginx             # Hitta nginx-processer

# MELLANLIGGANDE
ps aux --sort=-%cpu | head -10  # ⭐ Top 10 CPU-användare
ps aux --sort=-%mem | head -10  # ⭐ Top 10 minnesanvändare
ps -u www-data                  # Processer för specifik användare

# INTERAKTIVT
top                             # Realtidsövervakning
htop                            # ⭐ Snyggare version (installeras separat)
```

---

## Döda processer

```bash
# NYBÖRJARE
kill 1234                       # ⭐ Skicka SIGTERM (graceful shutdown)
kill -9 1234                    # ⭐ Skicka SIGKILL (force kill)

# MELLANLIGGANDE
kill -HUP 1234                  # SIGHUP – reload config
killall nginx                   # Döda alla processer som heter nginx
pkill nginx                     # Döda processer med "nginx" i namnet
pkill -9 nginx                  # Force kill
```

**Viktiga signaler:**
| Signal | Nummer | Betydelse |
|--------|--------|-----------|
| SIGTERM | 15 | "Snälla avsluta" – processen kan städa upp |
| SIGKILL | 9 | "AVSLUTA NU" – omedelbar död |
| SIGHUP | 1 | "Ladda om config" |

---

## Hitta processer

```bash
pgrep nginx                     # Hitta alla PIDs för nginx
pgrep -l nginx                  # Visa PID OCH namn
pgrep -a nginx                  # Visa PID och HELA kommandoraden

# I SCRIPTS
if pgrep nginx > /dev/null; then
    echo "Nginx is running"
else
    echo "Nginx is NOT running"
fi
```

---

## Bakgrundsjobb

```bash
./long-script.sh &              # Starta i bakgrunden
nohup ./script.sh &             # ⭐ Överlever logout
nohup ./script.sh > output.log 2>&1 &   # Med loggfil

jobs                            # Lista bakgrundsjobb
fg                              # Ta till förgrunden
bg                              # Kör stoppad process i bakgrunden

# WORKFLOW
./long-task.sh                  # Starta
# CTRL+Z                        # Pausa
bg                              # Fortsätt i bakgrunden
```
""",
            "quiz": [
                {
                    "question": "Vad gör 'kill -9 PID'?",
                    "options": ["Graceful shutdown", "Force kill (omedelbar)", "Reload config", "Pausa processen"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando visar top 10 CPU-användare?",
                    "options": ["top", "ps aux", "ps aux --sort=-%cpu | head -10", "htop -c"],
                    "correct": 2
                },
                {
                    "question": "Vad gör 'nohup'?",
                    "options": ["Dödar processen", "Processen överlever logout", "Pausar processen", "Visar processer"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 4: System Information & Monitoring
        # ======================================================================
        {
            "title": "System Information & Monitoring",
            "slug": "system-information-monitoring",
            "description": "Övervaka systemresurser, CPU, minne, disk I/O och kernel-meddelanden.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 90,
            "content": """# 4. System Information & Monitoring

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `uptime` | Ladda och drifttid |
| 2 | `free -h` | Minnesanvändning |
| 3 | `df -h` | Diskutrymme |
| 4 | `top` / `htop` | Realtidsövervakning |
| 5 | `vmstat` | CPU, minne, I/O |
| 6 | `iostat` | Disk I/O-statistik |
| 7 | `uname -a` | Systeminformation |
| 8 | `lscpu` | CPU-information |
| 9 | `lsblk` | Block devices |
| 10 | `dmesg` | Kernel-meddelanden |

```bash
# SYSTEMINFO
uname -a                        # All systeminformation
cat /etc/os-release             # OS-version
hostname -I                     # IP-adress(er)

# DRIFTTID & LAST
uptime                          # ⭐ Drifttid + load average
w                               # Vem är inloggad + vad gör de

# CPU
lscpu                           # ⭐ All CPU-info
nproc                           # Antal kärnor

# MINNE
free -h                         # ⭐ Human-readable
vmstat 1                        # Kontinuerlig minnesövervakning

# DISK I/O
iostat -x 1                     # Extended statistics varje sekund
iotop                           # ⭐ Vilka processer gör disk I/O

# KERNEL
dmesg | tail -50                # Senaste kernel-meddelanden
dmesg | grep -i error           # Bara fel
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando visar minnesanvändning i läsbart format?",
                    "options": ["mem -h", "free -h", "ram -h", "memory"],
                    "correct": 1
                },
                {
                    "question": "Vad visar 'uptime'?",
                    "options": ["Endast tid", "Drifttid + load average", "CPU-användning", "Diskutrymme"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando visar kernel-meddelanden?",
                    "options": ["kernel", "dmesg", "syslog", "klog"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 5: Log Management
        # ======================================================================
        {
            "title": "Log Management",
            "slug": "log-management",
            "description": "Analysera loggar med tail, journalctl, grep och hantera loggrotation.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 110,
            "content": """# 5. Log Management

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `tail -f` | Följ logg i realtid |
| 2 | `journalctl` | Systemd-loggar |
| 3 | `grep -i error` | Sök efter fel |
| 4 | `less` | Bläddra i stora loggar |
| 5 | `zcat` / `zgrep` | Komprimerade loggar |
| 6 | `journalctl -u` | Specifik service |
| 7 | `dmesg` | Kernel-meddelanden |
| 8 | `logrotate` | Hantera loggrotation |
| 9 | `grep -A/-B` | Kontext |
| 10 | `awk + sort + uniq` | Analysera mönster |

```bash
# VIKTIGA LOGGPLATSER
/var/log/syslog                 # Ubuntu/Debian huvudlogg
/var/log/messages               # RHEL/CentOS huvudlogg
/var/log/auth.log               # Autentisering
/var/log/nginx/                 # Nginx

# FÖLJA LOGGAR
tail -f /var/log/syslog         # ⭐ Följ i realtid
tail -F /var/log/app.log        # ⭐ Följer även vid rotation

# JOURNALCTL (systemd)
journalctl -f                   # ⭐ Följ live
journalctl -u nginx             # ⭐ Specifik service
journalctl -u nginx --since "1 hour ago"
journalctl -p err               # Bara errors

# KOMPRIMERADE LOGGAR
zgrep "error" /var/log/syslog.*.gz
```
""",
            "quiz": [
                {
                    "question": "Vad gör 'tail -F' som 'tail -f' inte gör?",
                    "options": ["Visar fler rader", "Följer vid loggrotation", "Filtrerar errors", "Kör snabbare"],
                    "correct": 1
                },
                {
                    "question": "Hur visar du loggar för en specifik systemd-service?",
                    "options": ["tail -f service", "journalctl -u servicename", "cat /var/log/service", "service logs"],
                    "correct": 1
                },
                {
                    "question": "Var ligger vanligtvis auth-loggar på Ubuntu?",
                    "options": ["/var/log/auth.log", "/var/log/secure", "/var/log/login", "/etc/auth.log"],
                    "correct": 0
                }
            ]
        },

        # ======================================================================
        # NODE 6: SSH & Remote Access
        # ======================================================================
        {
            "title": "SSH & Remote Access",
            "slug": "ssh-remote-access",
            "description": "Anslut till fjärrservrar, hantera SSH-nycklar, kopiera filer säkert och skapa tunnlar.",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 120,
            "content": """# 6. SSH & Remote Access

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `ssh user@host` | Anslut |
| 2 | `ssh-keygen` | Skapa SSH-nycklar |
| 3 | `ssh-copy-id` | Kopiera publik nyckel |
| 4 | `scp` | Kopiera filer |
| 5 | `rsync -avz` | Synkronisera filer |
| 6 | `~/.ssh/config` | Genvägar |
| 7 | `ssh -L` | Port forwarding |
| 8 | `ssh -J` | Jump host |
| 9 | `ssh-agent` | Nyckelhantering |
| 10 | `ssh -i` | Specifik nyckel |

```bash
# ANSLUTA
ssh user@192.168.1.100
ssh -p 2222 user@server         # Annan port
ssh user@server 'uptime'        # ⭐ Kör kommando direkt

# NYCKLAR
ssh-keygen -t ed25519 -C "din@email.com"   # ⭐ Skapa nyckel
ssh-copy-id user@server         # ⭐ Kopiera till server

# KOPIERA FILER
scp fil.txt user@server:/path/  # Lokal → Remote
scp -r katalog/ user@server:/   # Rekursivt

# RSYNC (bättre)
rsync -avz katalog/ user@server:/backup/   # ⭐ Synkronisera
rsync -avz --delete katalog/ user@server:/backup/  # Ta bort borttagna

# SSH CONFIG (~/.ssh/config)
Host myserver
    HostName 192.168.1.100
    User admin
    Port 22
# Sedan: ssh myserver

# TUNNEL
ssh -L 3306:localhost:3306 user@server     # Local port forwarding
ssh -J bastion user@internal               # Via jump host
```
""",
            "quiz": [
                {
                    "question": "Vilken nyckeltyp rekommenderas för nya SSH-nycklar?",
                    "options": ["rsa", "dsa", "ed25519", "ecdsa"],
                    "correct": 2
                },
                {
                    "question": "Vad gör ssh-copy-id?",
                    "options": ["Kopierar privat nyckel", "Kopierar publik nyckel till server", "Skapar ny nyckel", "Tar bort nyckel"],
                    "correct": 1
                },
                {
                    "question": "Vilket verktyg är bättre än scp för synkronisering?",
                    "options": ["ftp", "rsync", "wget", "curl"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 7: Firewall Essentials
        # ======================================================================
        {
            "title": "Firewall Essentials",
            "slug": "firewall-essentials",
            "description": "Konfigurera brandvägg med ufw och firewalld, öppna portar och blockera trafik.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 110,
            "content": """# 7. Firewall Essentials

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `ufw status` | Se status |
| 2 | `ufw allow 22` | Öppna SSH |
| 3 | `ufw enable` | Aktivera |
| 4 | `ufw deny` | Blockera |
| 5 | `iptables -L` | Lista regler |
| 6 | `firewall-cmd` | CentOS/RHEL |
| 7 | `ss -tulpn` | Öppna portar |
| 8 | `netstat -tulpn` | Öppna portar |
| 9 | `ufw delete` | Ta bort regel |
| 10 | `ufw reload` | Ladda om |

```bash
# UFW (Ubuntu)
sudo ufw status                 # Status
sudo ufw allow 22               # ⭐ SSH (ALLTID FÖRST!)
sudo ufw allow 80               # HTTP
sudo ufw allow 443              # HTTPS
sudo ufw enable                 # ⭐ Aktivera
sudo ufw deny from 10.0.0.5     # Blockera IP
sudo ufw status numbered        # Med nummer
sudo ufw delete 3               # Ta bort regel 3

# FIREWALLD (CentOS/RHEL)
sudo firewall-cmd --list-all
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload

# SE ÖPPNA PORTAR
ss -tulpn                       # ⭐ TCP + UDP + Listening + PID
ss -tulpn | grep :80            # Vad lyssnar på port 80?
```

**⚠️ VARNING:** Kör ALLTID `ufw allow 22` INNAN `ufw enable`!
""",
            "quiz": [
                {
                    "question": "Vilken port måste ALLTID öppnas innan du aktiverar ufw?",
                    "options": ["80", "443", "22", "3306"],
                    "correct": 2
                },
                {
                    "question": "Vilket kommando visar öppna portar med process-ID?",
                    "options": ["netstat", "ss -tulpn", "ports", "lsof -p"],
                    "correct": 1
                },
                {
                    "question": "Vilken brandvägg används på CentOS/RHEL?",
                    "options": ["ufw", "iptables", "firewalld", "pf"],
                    "correct": 2
                }
            ]
        },

        # ======================================================================
        # NODE 8: Network Basics
        # ======================================================================
        {
            "title": "Network Basics",
            "slug": "network-basics",
            "description": "IP-konfiguration, DNS-uppslagning, testa anslutningar och felsök nätverk.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 110,
            "content": """# 8. Network Basics

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `ip addr` | Visa IP-adresser |
| 2 | `ping` | Testa anslutning |
| 3 | `curl` | HTTP-requests |
| 4 | `ss -tulpn` | Öppna portar |
| 5 | `dig` / `nslookup` | DNS |
| 6 | `traceroute` | Spåra nätväg |
| 7 | `netcat (nc)` | Port-test |
| 8 | `wget` | Ladda ner |
| 9 | `ip route` | Routing |
| 10 | `tcpdump` | Paketanalys |

```bash
# IP-KONFIGURATION
ip addr                         # ⭐ Alla interfaces
ip route                        # Routing-tabell
hostname -I                     # Bara IP-adresser

# TESTA ANSLUTNING
ping -c 4 google.com            # ⭐ 4 paket
traceroute google.com           # Visa nätväg
nc -zv server.com 80            # ⭐ Testa om port är öppen

# DNS
dig google.com                  # ⭐ DNS-lookup
dig google.com +short           # Bara IP
nslookup google.com

# HTTP
curl -I https://google.com      # ⭐ Bara headers
curl -v https://google.com      # Verbose
curl -o fil.html https://site.com/page
wget https://example.com/file.zip
```

**💡 Felsökning "kan inte nå server":**
```bash
ping 8.8.8.8                    # Internet?
dig mysite.com                  # DNS?
nc -zv mysite.com 443           # Port öppen?
curl -I https://mysite.com      # HTTP?
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando testar om en port är öppen?",
                    "options": ["ping", "nc -zv host port", "curl", "dig"],
                    "correct": 1
                },
                {
                    "question": "Vad gör 'dig google.com +short'?",
                    "options": ["Pingar Google", "Visar bara IP-adressen", "Laddar ner sidan", "Visar routing"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando visar alla nätverksinterfaces?",
                    "options": ["ifconfig", "ip addr", "netstat", "network"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 9: Package Management
        # ======================================================================
        {
            "title": "Package Management",
            "slug": "package-management",
            "description": "Installera, uppdatera och ta bort paket med apt, dnf och rpm.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 90,
            "content": """# 9. Package Management

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `apt update` | Uppdatera paketlistor |
| 2 | `apt install` | Installera |
| 3 | `apt upgrade` | Uppgradera |
| 4 | `apt remove` | Ta bort |
| 5 | `apt search` | Sök |
| 6 | `dnf install` | RHEL/CentOS |
| 7 | `apt autoremove` | Rensa |
| 8 | `dpkg -l` | Lista installerade |
| 9 | `rpm -qa` | Lista (RHEL) |
| 10 | `apt show` | Paketinfo |

```bash
# APT (Ubuntu/Debian)
sudo apt update                 # ⭐ Hämta paketlistor
sudo apt upgrade                # Uppgradera alla
sudo apt install nginx          # Installera
sudo apt install -y nginx       # Utan bekräftelse
sudo apt remove nginx           # Ta bort
sudo apt autoremove             # ⭐ Ta bort oanvända beroenden
apt search nginx                # Sök
dpkg -l | grep nginx            # Är det installerat?

# DNF (RHEL/CentOS/Fedora)
sudo dnf update
sudo dnf install nginx
sudo dnf remove nginx
rpm -qa | grep nginx
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando bör köras FÖRE apt install?",
                    "options": ["apt upgrade", "apt update", "apt clean", "apt check"],
                    "correct": 1
                },
                {
                    "question": "Vad gör apt autoremove?",
                    "options": ["Tar bort alla paket", "Tar bort oanvända beroenden", "Uppdaterar paket", "Installerar automatiskt"],
                    "correct": 1
                },
                {
                    "question": "Vilken pakethanterare används på RHEL/CentOS?",
                    "options": ["apt", "yum/dnf", "pacman", "brew"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 10: System Services & systemd
        # ======================================================================
        {
            "title": "System Services & systemd",
            "slug": "system-services-systemd",
            "description": "Starta, stoppa och hantera tjänster med systemctl. Skapa egna services.",
            "difficulty": "medium",
            "estimated_minutes": 55,
            "xp_reward": 130,
            "content": """# 10. System Services & systemd

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `systemctl status` | Kontrollera |
| 2 | `systemctl start` | Starta |
| 3 | `systemctl stop` | Stoppa |
| 4 | `systemctl restart` | Starta om |
| 5 | `systemctl enable` | Autostart |
| 6 | `systemctl disable` | Inaktivera |
| 7 | `systemctl reload` | Ladda om config |
| 8 | `journalctl -u` | Se loggar |
| 9 | `systemctl list-units` | Lista |
| 10 | `systemctl daemon-reload` | Efter ändringar |

```bash
# STATUS
systemctl status nginx          # ⭐ Detaljerad status
systemctl is-active nginx       # Bara active/inactive
systemctl is-enabled nginx      # Startar vid boot?

# KONTROLL
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx     # ⭐ Ladda om config (ingen downtime)

# BOOT
sudo systemctl enable nginx     # ⭐ Autostart vid boot
sudo systemctl disable nginx
sudo systemctl enable --now nginx   # Enable OCH starta

# LISTA
systemctl list-units --type=service
systemctl list-units --failed

# LOGGAR
journalctl -u nginx             # Service-loggar
journalctl -u nginx -f          # Följ live
```

### Skapa egen service

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/run.sh
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload    # ⭐ Efter ändringar!
sudo systemctl enable --now myapp
```
""",
            "quiz": [
                {
                    "question": "Vad gör 'systemctl enable'?",
                    "options": ["Startar tjänsten", "Aktiverar autostart vid boot", "Stoppar tjänsten", "Laddar om config"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando måste köras efter att du ändrat en service-fil?",
                    "options": ["systemctl restart", "systemctl daemon-reload", "systemctl enable", "service reload"],
                    "correct": 1
                },
                {
                    "question": "Vad gör 'systemctl reload' jämfört med restart?",
                    "options": ["Samma sak", "Laddar om config utan downtime", "Startar om hårdare", "Tar bort tjänsten"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 11: File Permissions & Security
        # ======================================================================
        {
            "title": "File Permissions & Security",
            "slug": "file-permissions-security",
            "description": "Förstå och hantera filrättigheter, chmod, chown och säker konfiguration.",
            "difficulty": "medium",
            "estimated_minutes": 50,
            "xp_reward": 120,
            "content": """# 11. File Permissions & Security

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `chmod 755` | Script/katalog |
| 2 | `chmod 644` | Vanlig fil |
| 3 | `chown user:group` | Byt ägare |
| 4 | `ls -la` | Visa rättigheter |
| 5 | `chmod +x` | Gör körbart |
| 6 | `chown -R` | Rekursivt |
| 7 | `chmod 600` | Privat fil |
| 8 | `umask` | Default |
| 9 | `stat` | Detaljerad info |
| 10 | `getfacl/setfacl` | ACLs |

```bash
# FÖRSTÅ RÄTTIGHETER
# -rwxr-xr-x = 755
# r=4, w=2, x=1

# VANLIGA KOMBINATIONER
chmod 755 script.sh             # ⭐ rwxr-xr-x (scripts, kataloger)
chmod 644 config.txt            # ⭐ rw-r--r-- (vanliga filer)
chmod 600 privat.key            # ⭐ rw------- (SSH-nycklar)

# SYMBOLISKT
chmod +x script.sh              # ⭐ Lägg till execute
chmod u+x script.sh             # Bara för user

# ÄGARE
sudo chown nginx:www-data fil.txt
sudo chown -R nginx:www-data /var/www/

# WEBSERVER-SETUP
sudo chown -R www-data:www-data /var/www/html/
find /var/www/html -type d -exec chmod 755 {} \\;
find /var/www/html -type f -exec chmod 644 {} \\;

# SSH-NYCKLAR
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```
""",
            "quiz": [
                {
                    "question": "Vad betyder chmod 755?",
                    "options": ["Alla kan skriva", "rwxr-xr-x (ägare full, andra läs+kör)", "Ingen access", "Endast root"],
                    "correct": 1
                },
                {
                    "question": "Vilken chmod ska SSH privata nycklar ha?",
                    "options": ["755", "644", "600", "777"],
                    "correct": 2
                },
                {
                    "question": "Vad gör 'chown -R'?",
                    "options": ["Tar bort rättigheter", "Byter ägare rekursivt", "Återställer rättigheter", "Läser rättigheter"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 12: Compression & Archives
        # ======================================================================
        {
            "title": "Compression & Archives",
            "slug": "compression-archives",
            "description": "Skapa och packa upp arkiv med tar, gzip, zip och bzip2.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 90,
            "content": """# 12. Compression & Archives

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `tar -czvf` | Skapa .tar.gz |
| 2 | `tar -xzvf` | Packa upp |
| 3 | `tar -tzvf` | Lista innehåll |
| 4 | `gzip/gunzip` | Komprimera |
| 5 | `zip/unzip` | Windows-kompatibelt |
| 6 | `tar -xjvf` | Packa upp .tar.bz2 |
| 7 | `zcat` | Visa gzippad fil |
| 8 | `tar --exclude` | Exkludera |
| 9 | `du -sh arkiv.tar.gz` | Storlek |
| 10 | `pigz` | Parallel gzip |

```bash
# TAR
tar -cvf arkiv.tar katalog/              # Bara tar
tar -czvf arkiv.tar.gz katalog/          # ⭐ Med gzip
tar -cjvf arkiv.tar.bz2 katalog/         # Med bzip2

tar -xzvf arkiv.tar.gz                   # ⭐ Packa upp
tar -xzvf arkiv.tar.gz -C /destination/  # Till specifik plats
tar -tzvf arkiv.tar.gz                   # Lista innehåll

tar -czvf arkiv.tar.gz katalog/ --exclude='*.log'

# GZIP
gzip fil.txt                    # → fil.txt.gz
gunzip fil.txt.gz               # Expandera
zcat fil.txt.gz                 # Visa utan att expandera

# ZIP
zip -r arkiv.zip katalog/       # ⭐ Rekursivt
unzip arkiv.zip
unzip arkiv.zip -d /destination/
```

**💡 Backup med datum:**
```bash
tar -czvf /backup/app_$(date +%Y%m%d_%H%M%S).tar.gz /var/www/app/
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando skapar en .tar.gz fil?",
                    "options": ["tar -xzvf", "tar -czvf", "gzip -c", "zip -r"],
                    "correct": 1
                },
                {
                    "question": "Vad gör 'tar -t'?",
                    "options": ["Skapar arkiv", "Extraherar", "Listar innehåll", "Testar integritet"],
                    "correct": 2
                },
                {
                    "question": "Hur packar du upp till en specifik katalog?",
                    "options": ["tar -xzvf arkiv.tar.gz /dest", "tar -xzvf arkiv.tar.gz -C /dest", "untar -d /dest", "extract --to /dest"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 13: Environment & Variables
        # ======================================================================
        {
            "title": "Environment & Variables",
            "slug": "environment-variables",
            "description": "Hantera miljövariabler, PATH, och konfigurera din shell-miljö.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 90,
            "content": """# 13. Environment & Variables

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `export VAR=value` | Sätt miljövariabel |
| 2 | `echo $VAR` | Visa värde |
| 3 | `env` | Visa alla |
| 4 | `printenv` | Visa specifik |
| 5 | `unset VAR` | Ta bort |
| 6 | `source ~/.bashrc` | Ladda om |
| 7 | `VAR=x command` | Temporär |
| 8 | `$PATH` | Sökväg |
| 9 | `~/.bashrc` | Permanent |
| 10 | `env VAR=x cmd` | Modifierad env |

```bash
# SÄTTA VARIABLER
export DATABASE_URL="postgres://localhost/mydb"
export NODE_ENV=production

# VISA
echo $HOME
env                             # Alla miljövariabler
printenv PATH

# TA BORT
unset MYVAR

# VIKTIGA SYSTEMVARIABLER
$HOME                           # Hemkatalog
$USER                           # Användarnamn
$PATH                           # Sökvägar för kommandon
$PWD                            # Nuvarande katalog

# PERMANENT (lägg i ~/.bashrc)
echo 'export PATH=$PATH:/opt/myapp/bin' >> ~/.bashrc
source ~/.bashrc

# TEMPORÄR
NODE_ENV=development npm start
DEBUG=true ./myapp
```
""",
            "quiz": [
                {
                    "question": "Hur gör du en miljövariabel tillgänglig för child-processer?",
                    "options": ["VAR=value", "export VAR=value", "set VAR=value", "env VAR"],
                    "correct": 1
                },
                {
                    "question": "Var lägger du permanenta miljövariabler för bash?",
                    "options": ["/etc/env", "~/.bashrc", "/var/env", "~/.profile.d"],
                    "correct": 1
                },
                {
                    "question": "Hur laddar du om ~/.bashrc utan att logga ut?",
                    "options": ["reload bash", "source ~/.bashrc", "bash --reload", "exec bashrc"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 14: Disk Management
        # ======================================================================
        {
            "title": "Disk Management",
            "slug": "disk-management",
            "description": "Hantera diskar, partitioner, montering och analysera diskutrymme.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 110,
            "content": """# 14. Disk Management

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `df -h` | Ledigt utrymme |
| 2 | `du -sh` | Katalogstorlek |
| 3 | `lsblk` | Lista diskar |
| 4 | `mount` | Montera |
| 5 | `umount` | Avmontera |
| 6 | `fdisk -l` | Partitioner |
| 7 | `mkfs.ext4` | Formatera |
| 8 | `/etc/fstab` | Permanent montering |
| 9 | `ncdu` | Interaktiv |
| 10 | `blkid` | UUIDs |

```bash
# VISA
df -h                           # ⭐ Ledigt utrymme
df -i                           # Inodes
lsblk                           # ⭐ Diskar och partitioner
lsblk -f                        # Med UUID
blkid                           # UUIDs

# MONTERA
sudo mount /dev/sdb1 /mnt/data
sudo umount /mnt/data

# FORMATERA
sudo mkfs.ext4 /dev/sdb1

# HITTA VAD SOM TAR PLATS
du -h --max-depth=1 / | sort -h | tail -20
ncdu /                          # ⭐ Interaktiv

# PERMANENT MONTERING (/etc/fstab)
UUID=abc123... /mnt/data ext4 defaults 0 2
sudo mount -a                   # Testa fstab
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando visar ledigt diskutrymme?",
                    "options": ["du -h", "df -h", "free -h", "disk -l"],
                    "correct": 1
                },
                {
                    "question": "Var konfigureras permanenta monteringar?",
                    "options": ["/etc/mounts", "/etc/fstab", "/etc/disk.conf", "/var/mount"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando listar diskar och partitioner?",
                    "options": ["fdisk", "lsblk", "diskutil", "parted"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 15: Quick Reference & Workflows
        # ======================================================================
        {
            "title": "Quick Reference & Workflows",
            "slug": "quick-reference-workflows",
            "description": "Dagliga rutiner, hälsokontroller och felsökningsflöden för DevOps.",
            "difficulty": "easy",
            "estimated_minutes": 30,
            "xp_reward": 80,
            "content": """# 15. Quick Reference & Workflows

## Daglig hälsokontroll

```bash
# "Hur mår servern?"
uptime                          # Load + drifttid
free -h                         # Minne
df -h                           # Disk
ps aux --sort=-%cpu | head -5   # CPU-tjuvar
systemctl --failed              # Kraschade services
```

## Felsökningsflöde

```bash
# APP FUNKAR INTE
systemctl status myapp          # Kör den?
journalctl -u myapp -n 50       # Loggar?
ss -tlnp | grep :3000           # Lyssnar?
curl localhost:3000             # Svarar lokalt?

# DISK FULL
df -h                           # Vilken partition?
du -sh /var/*                   # Vad tar plats?
find /var/log -name "*.log" -size +100M

# NÄTVERKSPROBLEM
ping 8.8.8.8                    # Internet?
dig google.com                  # DNS?
ss -tulpn                       # Portar?
sudo ufw status                 # Brandvägg?
```
""",
            "quiz": [
                {
                    "question": "Vilket är första steget vid 'app funkar inte'?",
                    "options": ["Starta om servern", "Kolla systemctl status", "Rensa loggar", "Kontakta support"],
                    "correct": 1
                },
                {
                    "question": "Vid 'disk full', vad kollar du först?",
                    "options": ["df -h för att se vilken partition", "Starta om", "Ta bort /var", "Köp mer disk"],
                    "correct": 0
                },
                {
                    "question": "Vilket kommando visar kraschade services?",
                    "options": ["systemctl status", "systemctl --failed", "service list", "journalctl -e"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 16: Terminal Productivity & Time Savers
        # ======================================================================
        {
            "title": "Terminal Productivity & Time Savers",
            "slug": "terminal-productivity",
            "description": "Bash-tricks, historik, aliases och tangentbordsgenvägar som gör dig snabbare.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 16. Terminal Productivity & Time Savers

## Varför detta är avgörande

Några sekunder per kommando × tusentals kommandon = timmar. Dessa tricks gör dig 2-3x snabbare.

## 🏆 TOP 10 – Tidsbesparare

| # | Trick | Vad det gör |
|---|-------|-------------|
| 1 | `sudo !!` | Kör förra kommandot med sudo |
| 2 | `!$` | Förra kommandots sista argument |
| 3 | `Ctrl+R` | Sök i historik |
| 4 | `cd -` | Tillbaka till förra katalogen |
| 5 | `alias` | Skapa genvägar |
| 6 | `Ctrl+A/E` | Början/slut av rad |
| 7 | `!!:s/old/new` | Kör förra med ersättning |
| 8 | Tab | Autocomplete |
| 9 | `Ctrl+U/K` | Radera till början/slut |
| 10 | `!cmd` | Senaste cmd-kommandot |

---

## Historia-tricks

```bash
# SUDO DET FÖRRA ⭐
apt update                      # Oops, glömde sudo
sudo !!                         # Kör "sudo apt update"

# SENASTE ARGUMENT ⭐
mkdir /very/long/path/name
cd !$                           # cd till det långa path:et

# ALLA ARGUMENT
echo fil1.txt fil2.txt fil3.txt
rm !*                           # rm alla tre

# KÖR FRÅN HISTORIK
!ssh                            # Senaste ssh-kommandot
!123                            # Kommando #123
!!                              # Förra kommandot

# SÖK I HISTORIK ⭐
Ctrl+R                          # Börja skriva, Ctrl+R för nästa träff

# VISA HISTORIK
history | grep ssh
```

---

## Tangentbordsgenvägar

```bash
# NAVIGATION
Ctrl+A                          # ⭐ Början av rad
Ctrl+E                          # ⭐ Slut av rad
Ctrl+←/→                        # Hoppa ord

# RADERING
Ctrl+U                          # ⭐ Radera till början
Ctrl+K                          # Radera till slut
Ctrl+W                          # Radera ord bakåt
Ctrl+Y                          # Klistra in raderat

# KONTROLL
Ctrl+C                          # Avbryt
Ctrl+Z                          # Pausa (fg för fortsätt)
Ctrl+L                          # Clear screen
Ctrl+D                          # Exit
```

---

## Aliases – Dina genvägar

Lägg i `~/.bashrc`:

```bash
# NAVIGATION
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -lah'

# SÄKERHET
alias rm='rm -i'

# BEKVÄMLIGHET
alias c='clear'
alias h='history'
alias update='sudo apt update && sudo apt upgrade -y'
alias ports='ss -tulpn'
alias myip='curl ifconfig.me'

# GIT
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'

# DOCKER
alias d='docker'
alias dc='docker-compose'
alias dps='docker ps'

# LADDA OM
source ~/.bashrc
```

---

## Brace Expansion

```bash
# SKAPA FLERA
touch fil{1..5}.txt             # fil1.txt...fil5.txt
mkdir -p projekt/{src,tests,docs}

# BACKUP-TRICK ⭐
cp config.yaml{,.bak}           # → config.yaml.bak

# BYTA TEXT I FÖRRA
systemctl start ngix            # Typo!
^ngix^nginx                     # Ersätt och kör
```

---

## Kommando-substitution

```bash
# $(command)
echo "Datum: $(date)"
tar -czvf backup_$(date +%Y%m%d).tar.gz /var/www

# I VARIABEL
MY_IP=$(curl -s ifconfig.me)
echo "Min IP: $MY_IP"
```

---

## Logik & kedjning

```bash
command1; command2              # Kör alla
command1 && command2            # ⭐ Kör 2 om 1 lyckas
command1 || command2            # Kör 2 om 1 misslyckas

# EXEMPEL
apt update && apt upgrade       # Vanligt mönster
ping -c1 server || echo "Nere!"
make && make install || echo "Failed"
```
""",
            "quiz": [
                {
                    "question": "Vad gör 'sudo !!'?",
                    "options": ["Visar historik", "Kör förra kommandot med sudo", "Söker i historik", "Avbryter kommando"],
                    "correct": 1
                },
                {
                    "question": "Vilken tangent söker bakåt i bash-historiken?",
                    "options": ["Ctrl+F", "Ctrl+R", "Ctrl+H", "Ctrl+S"],
                    "correct": 1
                },
                {
                    "question": "Vad gör '!$'?",
                    "options": ["Kör senaste kommando", "Senaste argumentet från förra kommandot", "Visar pengar", "Tar bort senaste"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 17: User & Group Management
        # ======================================================================
        {
            "title": "User & Group Management",
            "slug": "user-group-management",
            "description": "Skapa användare, hantera grupper och konfigurera sudo-access.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 110,
            "content": """# 17. User & Group Management

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `useradd` | Skapa användare |
| 2 | `usermod` | Ändra användare |
| 3 | `userdel` | Ta bort |
| 4 | `passwd` | Sätt lösenord |
| 5 | `groupadd` | Skapa grupp |
| 6 | `usermod -aG` | Lägg till i grupp |
| 7 | `id` | Visa user/group |
| 8 | `su` / `sudo` | Byt användare |
| 9 | `visudo` | Redigera sudoers |
| 10 | `groups` | Visa grupper |

---

## Hantera användare

```bash
# SKAPA
sudo useradd -m alice           # ⭐ Med hemkatalog
sudo useradd -m -s /bin/bash alice   # Med bash
sudo adduser alice              # ⭐ Interaktivt (Ubuntu)

# LÖSENORD
sudo passwd alice

# ÄNDRA
sudo usermod -aG sudo alice     # ⭐ Lägg till i sudo-grupp
sudo usermod -aG docker alice

# TA BORT
sudo userdel -r alice           # ⭐ Med hemkatalog

# VISA
id alice                        # UID, GID, grupper
groups alice                    # Grupper
whoami
```

---

## Hantera grupper

```bash
# SKAPA
sudo groupadd developers

# LÄGG TILL ANVÄNDARE ⭐
sudo usermod -aG developers alice   # -a = append!

# TA BORT FRÅN GRUPP
sudo gpasswd -d alice developers

# VISA
groups alice
getent group developers         # Medlemmar
```

**⚠️ OBS:** Gruppändringar kräver ny login!

---

## sudo-access

```bash
# REDIGERA SUDOERS ⭐
sudo visudo

# VANLIGA TILLÄGG
alice ALL=(ALL:ALL) ALL                         # Full sudo
alice ALL=(ALL) NOPASSWD: ALL                   # Utan lösenord
%developers ALL=(ALL) NOPASSWD: /opt/deploy.sh  # Grupp

# BYT TILL ROOT
sudo -i                         # ⭐ Root shell
sudo -u postgres psql           # Som annan användare
```

---

## Praktiskt: Ny teammedlem

```bash
#!/bin/bash
USERNAME="alice"

sudo useradd -m -s /bin/bash $USERNAME
sudo usermod -aG sudo $USERNAME
sudo usermod -aG docker $USERNAME

sudo mkdir -p /home/$USERNAME/.ssh
sudo chmod 700 /home/$USERNAME/.ssh
echo "ssh-ed25519 AAAA..." | sudo tee /home/$USERNAME/.ssh/authorized_keys
sudo chmod 600 /home/$USERNAME/.ssh/authorized_keys
sudo chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh
```
""",
            "quiz": [
                {
                    "question": "Vilken flagga skapar hemkatalog med useradd?",
                    "options": ["-h", "-m", "-d", "-home"],
                    "correct": 1
                },
                {
                    "question": "Vad gör 'usermod -aG sudo alice'?",
                    "options": ["Tar bort från sudo", "Lägger till alice i sudo-gruppen", "Skapar sudo-användare", "Visar sudo-gruppen"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando redigerar sudoers säkert?",
                    "options": ["nano /etc/sudoers", "visudo", "sudo edit", "sudoedit"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 18: Cron Jobs & Task Scheduling
        # ======================================================================
        {
            "title": "Cron Jobs & Task Scheduling",
            "slug": "cron-jobs-scheduling",
            "description": "Schemalägg automatiska jobb med cron och systemd timers.",
            "difficulty": "medium",
            "estimated_minutes": 45,
            "xp_reward": 110,
            "content": """# 18. Cron Jobs & Task Scheduling

## 🏆 TOP 10 – Kommandon

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `crontab -e` | Redigera cron |
| 2 | `crontab -l` | Lista cron |
| 3 | `crontab -r` | Ta bort alla |
| 4 | `/etc/cron.d/` | System cron |
| 5 | `/etc/cron.daily/` | Dagliga scripts |
| 6 | `systemctl status cron` | Status |
| 7 | `journalctl -u cron` | Loggar |
| 8 | `@reboot` | Vid uppstart |
| 9 | `at` | Engångsjobb |
| 10 | `*/5 * * * *` | Var 5:e minut |

---

## Crontab syntax

```
# ┌───────────── minut (0-59)
# │ ┌───────────── timme (0-23)
# │ │ ┌───────────── dag (1-31)
# │ │ │ ┌───────────── månad (1-12)
# │ │ │ │ ┌───────────── veckodag (0-7)
# │ │ │ │ │
# * * * * * kommando

# VANLIGA MÖNSTER
* * * * *     # Varje minut
*/5 * * * *   # ⭐ Var 5:e minut
0 * * * *     # ⭐ Varje hel timme
0 0 * * *     # ⭐ Midnatt varje dag
0 0 * * 0     # Midnatt varje söndag
0 0 1 * *     # Första dagen varje månad

# SPECIALORD
@reboot       # Vid uppstart
@hourly       # Varje timme
@daily        # Varje dag
@weekly       # Varje vecka
```

---

## Hantera crontab

```bash
crontab -e                      # ⭐ Redigera
crontab -l                      # ⭐ Lista
crontab -r                      # Ta bort alla

sudo crontab -u nginx -l        # Annan användares cron
```

---

## Praktiska cron-exempel

```bash
# BACKUP VARJE NATT 02:00
0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1

# RENSA TEMP DAGLIGEN
0 3 * * * find /tmp -type f -mtime +7 -delete

# HEALTH CHECK VAR 5:E MINUT
*/5 * * * * curl -s https://myapp.com/health || echo "DOWN!" | mail admin@example.com

# VID REBOOT
@reboot /opt/myapp/start.sh
```

**⚠️ Viktigt:**
- Använd fullständiga sökvägar
- Redirect output: `>> /var/log/job.log 2>&1`

---

## Systemd Timers (alternativ)

```bash
systemctl list-timers           # ⭐ Lista alla timers
```
""",
            "quiz": [
                {
                    "question": "Vad betyder '*/5 * * * *' i cron?",
                    "options": ["Var 5:e timme", "Var 5:e minut", "Kl 5 varje dag", "5 dagar i veckan"],
                    "correct": 1
                },
                {
                    "question": "Vilket kommando listar dina cron-jobb?",
                    "options": ["cron -l", "crontab -l", "list cron", "cat /etc/cron"],
                    "correct": 1
                },
                {
                    "question": "Vad gör @reboot i crontab?",
                    "options": ["Startar om servern", "Kör vid systemstart", "Kör varje dag", "Tar bort cron"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 19: Shell Scripting Fundamentals
        # ======================================================================
        {
            "title": "Shell Scripting Fundamentals",
            "slug": "shell-scripting-fundamentals",
            "description": "Grunderna i bash-scripting: variabler, villkor, loopar och funktioner.",
            "difficulty": "hard",
            "estimated_minutes": 70,
            "xp_reward": 150,
            "content": """# 19. Shell Scripting Fundamentals

## 🏆 TOP 10 – Koncept

| # | Koncept | Användning |
|---|---------|------------|
| 1 | `#!/bin/bash` | Shebang |
| 2 | Variabler | `VAR="value"` |
| 3 | If-satser | Villkor |
| 4 | For-loopar | Iterera |
| 5 | Funktioner | Återanvändbar kod |
| 6 | Exit codes | `$?`, `exit 1` |
| 7 | `$(command)` | Substitution |
| 8 | Pipes | `|`, `>`, `>>` |
| 9 | `$1`, `$@` | Argument |
| 10 | `set -e` | Avbryt vid fel |

---

## Script-grunderna

```bash
#!/bin/bash
set -euo pipefail               # ⭐ Säkrare scripting

# VARIABLER
NAME="Said"
DATUM=$(date +%Y-%m-%d)
echo "Hello, $NAME"

# SPECIAL-VARIABLER
$0          # Script-namn
$1, $2      # Argument
$#          # Antal argument
$@          # Alla argument
$?          # Exit code
```

---

## If-satser

```bash
#!/bin/bash

if [ "$1" = "start" ]; then
    echo "Starting..."
elif [ "$1" = "stop" ]; then
    echo "Stopping..."
else
    echo "Usage: $0 {start|stop}"
    exit 1
fi

# FIL-TESTER
if [ -f "/etc/passwd" ]; then       # -f = är fil?
    echo "Filen finns"
fi

if [ -d "/var/log" ]; then          # -d = är katalog?
    echo "Katalogen finns"
fi

# STRÄNG-TESTER
if [ -z "$VAR" ]; then              # -z = tom?
    echo "Tom variabel"
fi

# NUMERISKT
if [ "$NUM" -gt 10 ]; then          # -gt = greater than
    echo "Större än 10"
fi
# -eq (equal), -ne (not equal), -lt, -le, -gt, -ge

# LOGIK
if [ -f "$FILE" ] && [ -r "$FILE" ]; then
    echo "Fil finns och är läsbar"
fi
```

---

## Loopar

```bash
#!/bin/bash

# FOR-LOOP (lista)
for server in web1 web2 web3; do
    echo "Checking $server..."
    ssh $server uptime
done

# FOR-LOOP (range)
for i in {1..5}; do
    echo "Nummer: $i"
done

# FOR-LOOP (filer)
for file in /var/log/*.log; do
    echo "Processing: $file"
done

# WHILE-LOOP
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# WHILE READ (fil rad för rad) ⭐
while read -r line; do
    echo "Line: $line"
done < input.txt
```

---

## Funktioner

```bash
#!/bin/bash

greet() {
    local name=$1               # local = bara i funktionen
    echo "Hello, $name!"
}

check_file() {
    if [ -f "$1" ]; then
        return 0                # Success
    else
        return 1                # Failure
    fi
}

# ANVÄNDNING
greet "Said"

if check_file "/etc/passwd"; then
    echo "File exists"
fi
```

---

## Praktiskt deploy-script

```bash
#!/bin/bash
set -euo pipefail

APP_DIR="/var/www/myapp"
BRANCH="${1:-main}"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

backup() {
    log "Creating backup..."
    tar -czvf "/backup/backup_$(date +%Y%m%d).tar.gz" "$APP_DIR"
}

deploy() {
    log "Deploying branch: $BRANCH"
    cd "$APP_DIR"
    git pull origin "$BRANCH"
}

restart() {
    log "Restarting..."
    systemctl reload myapp
}

main() {
    log "Starting deployment"
    backup
    deploy
    restart
    log "Done!"
}

main
```
""",
            "quiz": [
                {
                    "question": "Vad gör 'set -e' i ett bash-script?",
                    "options": ["Aktiverar echo", "Avbryter vid första fel", "Exporterar variabler", "Sätter environment"],
                    "correct": 1
                },
                {
                    "question": "Vad är $1 i ett script?",
                    "options": ["Exit code", "Första argumentet", "Script-namn", "PID"],
                    "correct": 1
                },
                {
                    "question": "Vad testar '[ -f /path ]'?",
                    "options": ["Om path är katalog", "Om path är fil", "Om path är länk", "Om path är körbar"],
                    "correct": 1
                }
            ]
        },

        # ======================================================================
        # NODE 20: Troubleshooting & Debugging
        # ======================================================================
        {
            "title": "Troubleshooting & Debugging",
            "slug": "troubleshooting-debugging",
            "description": "Systematisk felsökning, debug-verktyg och lösningar på vanliga problem.",
            "difficulty": "hard",
            "estimated_minutes": 60,
            "xp_reward": 140,
            "content": """# 20. Troubleshooting & Debugging

## 🏆 TOP 10 – Felsökningsverktyg

| # | Kommando | Användning |
|---|----------|------------|
| 1 | `journalctl` | Systemd-loggar |
| 2 | `dmesg` | Kernel |
| 3 | `strace` | Systemanrop |
| 4 | `lsof` | Öppna filer |
| 5 | `netstat/ss` | Nätverk |
| 6 | `tcpdump` | Paket |
| 7 | `top/htop` | Resurser |
| 8 | `vmstat/iostat` | Statistik |
| 9 | `tail -f` | Loggar |
| 10 | `systemctl status` | Services |

---

## Systematisk felsökning

### 1. Samla information

```bash
systemctl status myapp
journalctl -u myapp -n 50
uptime
free -h
df -h
```

### 2. Isolera problemet

```bash
# NÄTVERK
ping 8.8.8.8                    # Internet?
dig myapp.com                   # DNS?
curl localhost:3000             # App lokalt?
ss -tulpn | grep :3000          # Lyssnar?
sudo ufw status                 # Brandvägg?

# DISK
df -h                           # Fullt?
df -i                           # Inodes?

# PROCESS
pgrep myapp                     # Körs?
ps aux | grep myapp
```

### 3. Djupare analys

```bash
# VAD GÖR PROCESSEN?
strace -p $(pgrep myapp)

# ÖPPNA FILER
lsof -p $(pgrep myapp)
lsof -i :3000                   # Vad använder port 3000?
```

---

## Vanliga problem

### Service startar inte

```bash
systemctl status myapp
journalctl -u myapp -n 100 --no-pager
sudo -u www-data /opt/myapp/start.sh   # Testa manuellt
ls -la /opt/myapp/                      # Permissions?
```

### Disk full

```bash
df -h
du -h --max-depth=1 / | sort -h | tail -20
find / -type f -size +100M 2>/dev/null | head
lsof | grep deleted                     # Deleted but open!
journalctl --vacuum-size=500M           # Rensa loggar
```

### Hög CPU

```bash
top
ps aux --sort=-%cpu | head -10
strace -p PID
```

### Out of memory

```bash
free -h
ps aux --sort=-%mem | head -10
dmesg | grep -i "out of memory"
```

### Nätverksproblem

```bash
# Systematisk checklista:
ip addr                         # Har vi IP?
ping 127.0.0.1                  # Loopback?
ping $(ip route | grep default | awk '{print $3}')  # Gateway?
ping 8.8.8.8                    # Internet?
dig google.com                  # DNS?
nc -zv target.com 443           # Port?
```

---

## Debug-mode

```bash
# BASH
bash -x ./script.sh             # Visa varje kommando
set -x                          # I scriptet

# SSH
ssh -vvv user@server

# CURL
curl -v https://example.com

# NGINX
nginx -t                        # Test config
```

---

## Snabb diagnostik-script

```bash
#!/bin/bash
echo "=== SYSTEM ==="
uptime && free -h && df -h /

echo -e "\\n=== LOAD ==="
ps aux --sort=-%cpu | head -5

echo -e "\\n=== NETWORK ==="
ss -tulpn | grep LISTEN
ping -c 1 8.8.8.8 > /dev/null && echo "Internet: OK" || echo "Internet: FAIL"

echo -e "\\n=== FAILED SERVICES ==="
systemctl --failed

echo -e "\\n=== RECENT ERRORS ==="
journalctl -p err --since "1 hour ago" --no-pager | tail -20
```
""",
            "quiz": [
                {
                    "question": "Vilket kommando visar vilka filer en process har öppna?",
                    "options": ["ps aux", "lsof -p PID", "top", "strace"],
                    "correct": 1
                },
                {
                    "question": "Hur debuggar du ett bash-script rad för rad?",
                    "options": ["bash script.sh", "bash -x script.sh", "debug script.sh", "sh -d script.sh"],
                    "correct": 1
                },
                {
                    "question": "Vad kan 'lsof | grep deleted' avslöja?",
                    "options": ["Raderade filer", "Filer som är raderade men fortfarande öppna (tar diskplats)", "Virus", "Korrupta filer"],
                    "correct": 1
                }
            ]
        },
    ]
}
