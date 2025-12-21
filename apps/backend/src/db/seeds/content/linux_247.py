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

## 🔐 Varför detta är KRITISKT för DevOps

**Tänk dig detta scenario:** Du deployer en app kl 03:00. Allt ser bra ut, men appen startar inte. Du kollar loggarna – "Permission denied". Din SSH-nyckel har fel rättigheter. Databasen kan inte läsa config-filen. Nginx kan inte skriva till loggar.

**Permission-problem är #1 orsaken till deployment-fails.** Lär dig detta ordentligt nu, så slipper du panik mitt i natten.

---

## 🧠 Förstå Linux-rättigheter – Det magiska nummersystemet

Varje fil i Linux har TRE typer av rättigheter för TRE kategorier av användare:

```
┌─────────────────────────────────────────────────────────────────┐
│  -rwxr-xr-x   1   said   devops   4096   Dec 21 10:30   script.sh
│  │└┬┘└┬┘└┬┘       └─┬─┘  └──┬──┘
│  │ │  │  │          │       │
│  │ │  │  └── Others (alla andra)
│  │ │  └───── Group (gruppen)
│  │ └──────── User/Owner (ägaren)
│  └────────── Filtyp (- = fil, d = katalog, l = länk)
└─────────────────────────────────────────────────────────────────┘
```

### De tre rättigheterna:

| Symbol | Nummer | Betydelse | På fil | På katalog |
|--------|--------|-----------|--------|------------|
| `r` | 4 | **R**ead | Läsa innehåll | Lista filer (ls) |
| `w` | 2 | **W**rite | Ändra innehåll | Skapa/ta bort filer |
| `x` | 1 | e**X**ecute | Köra som program | Gå in i katalogen (cd) |

### Så fungerar nummer-systemet:

```
rwx = 4 + 2 + 1 = 7  (full access)
rw- = 4 + 2 + 0 = 6  (läs + skriv)
r-x = 4 + 0 + 1 = 5  (läs + kör)
r-- = 4 + 0 + 0 = 4  (bara läs)
--- = 0 + 0 + 0 = 0  (ingen access)
```

**Exempel: `chmod 755`**
```
7 = rwx (user)    → Ägaren kan ALLT
5 = r-x (group)   → Gruppen kan läsa och köra
5 = r-x (others)  → Alla andra kan läsa och köra
```

---

## 🏆 TOP 10 – Kommandon du MÅSTE kunna

| # | Kommando | Vad det gör | När du använder det |
|---|----------|-------------|---------------------|
| 1 | `chmod 755` | rwxr-xr-x | Scripts, kataloger – körbart för alla |
| 2 | `chmod 644` | rw-r--r-- | Config-filer – läsbart för alla |
| 3 | `chown user:group` | Byt ägare | När app ska äga sina filer |
| 4 | `ls -la` | Visa rättigheter | Felsöka permission denied |
| 5 | `chmod +x` | Lägg till execute | Göra script körbart |
| 6 | `chown -R` | Rekursivt byte | Hela kataloger |
| 7 | `chmod 600` | rw------- | SSH-nycklar, secrets |
| 8 | `umask` | Default permissions | Förstå nya filers rättigheter |
| 9 | `stat` | Detaljerad info | Felsöka djupt |
| 10 | `getfacl/setfacl` | Access Control Lists | Avancerad multi-user |

---

## 🎯 chmod – Ändra rättigheter

### Nybörjare – De tre heliga numren

```bash
# 📁 KATALOGER och 📜 SCRIPTS
chmod 755 deploy.sh              # Alla kan läsa/köra, ägaren kan ändra
chmod 755 /var/www/html          # Webserver-katalog

# 📄 VANLIGA FILER (config, text, etc.)
chmod 644 config.yml             # Alla kan läsa, ägaren kan ändra
chmod 644 /etc/nginx/nginx.conf  # Nginx config

# 🔒 HEMLIGA FILER (nycklar, lösenord)
chmod 600 ~/.ssh/id_rsa          # ENDAST ägaren kan läsa/skriva
chmod 600 .env                   # Environment secrets
```

**💡 Minnesregel:**
- **7**55 = Scripts & kataloger (behöver x för att köras/öppnas)
- **6**44 = Config & dokument (ingen execute behövs)
- **6**00 = Secrets (ingen annan ska se)

### Mellanliggande – Symbolisk notation

```bash
# Ibland enklare att tänka i symboler istället för siffror

chmod +x script.sh               # ⭐ Lägg till execute för ALLA
chmod u+x script.sh              # Lägg till execute BARA för user (u)
chmod g+w fil.txt                # Ge gruppen (g) skrivrättighet
chmod o-r secret.txt             # Ta BORT läsrättighet för others (o)

# Kombinera
chmod u+rwx,g+rx,o+rx script.sh  # Samma som 755

# Vem är vem?
# u = user (ägaren)
# g = group (gruppen)
# o = others (alla andra)
# a = all (alla tre)
```

### Avancerat – Speciella bits

```bash
# SETUID – Kör som filens ägare (farligt men ibland nödvändigt)
chmod u+s /usr/bin/passwd        # Därför kan vanliga users byta lösenord
chmod 4755 script.sh             # 4 = setuid bit

# SETGID – Nya filer ärver gruppens ägarskap
chmod g+s /shared/projekt/       # Bra för team-kataloger
chmod 2755 katalog/              # 2 = setgid bit

# STICKY BIT – Bara ägaren kan ta bort sina filer
chmod +t /tmp                    # Därför kan inte alla ta bort andras filer i /tmp
chmod 1777 /tmp                  # 1 = sticky bit
```

---

## 👤 chown – Ändra ägare

```bash
# GRUNDLÄGGANDE
sudo chown said fil.txt                    # Byt ägare till 'said'
sudo chown said:devops fil.txt             # Byt ägare OCH grupp
sudo chown :devops fil.txt                 # Byt BARA grupp

# REKURSIVT – Hela katalogträd
sudo chown -R www-data:www-data /var/www/  # ⭐ Webserver äger allt

# BEVARA SYMLINKS
sudo chown -h said:devops länk             # Ändra länken, inte målet
```

**⚠️ Vanligt misstag:** Glömmer `sudo`! Endast root kan ändra ägare till andra användare.

---

## 🌐 Verkliga DevOps-scenarier

### Scenario 1: Deploya en webbapp

```bash
# 1. Skapa katalogstruktur
sudo mkdir -p /var/www/myapp
sudo mkdir -p /var/www/myapp/{logs,uploads,static}

# 2. Sätt rätt ägare (webservern måste kunna läsa/skriva)
sudo chown -R www-data:www-data /var/www/myapp

# 3. Sätt rätt permissions
find /var/www/myapp -type d -exec chmod 755 {} \\;  # Kataloger: 755
find /var/www/myapp -type f -exec chmod 644 {} \\;  # Filer: 644

# 4. Uploads behöver skrivrättighet
chmod 775 /var/www/myapp/uploads

# ✅ Nu kan nginx/apache läsa allt, och appen kan skriva till uploads
```

### Scenario 2: SSH-säkerhet (detta MÅSTE vara rätt!)

```bash
# SSH är EXTREMT känslig för fel permissions
# Fel permissions = SSH vägrar fungera! 🚫

chmod 700 ~/.ssh                 # BARA du kan gå in
chmod 600 ~/.ssh/id_rsa          # ⚠️ KRITISKT: Privat nyckel
chmod 644 ~/.ssh/id_rsa.pub      # Publik nyckel kan vara läsbar
chmod 600 ~/.ssh/authorized_keys # Vem som får logga in som dig
chmod 644 ~/.ssh/known_hosts     # Kända servrar

# Felsök SSH-problem:
ls -la ~/.ssh/
# Om id_rsa är INTE 600 → SSH kommer vägra använda den!
```

**💥 True story:** Många deployment-pipelines failar för att CI/CD-servern kopierar SSH-nycklar med fel permissions. Lägg ALLTID till `chmod 600` efter att du kopierar nycklar.

### Scenario 3: Docker & permissions

```bash
# Docker kör ofta som root INUTI containern
# Men filer på host kan ha annan ägare

# Vanligt problem: Container kan inte skriva till volym
# Lösning:
sudo chown -R 1000:1000 /data/app    # UID 1000 = ofta första användaren
# Eller
chmod 777 /data/app                   # 🚫 DÅLIGT men funkar (osäkert)

# Bättre i Dockerfile:
# USER 1000
# RUN chown -R 1000:1000 /app
```

---

## 🔍 Felsökning – När "Permission denied" dyker upp

```bash
# STEG 1: Kolla vad som är fel
ls -la fil_som_inte_funkar.sh
# Output: -rw-r--r-- 1 root root ...
# Problem: Du är inte root och filen är inte körbar!

# STEG 2: Kolla vem du är
whoami                           # Visar din användare
id                               # Visar user, grupper, UIDs

# STEG 3: Detaljerad info
stat fil.txt                     # Visar ALLT om filen
namei -l /sökväg/till/fil        # Visar permissions hela vägen

# STEG 4: Fixa det!
sudo chmod +x script.sh          # Om script inte kan köras
sudo chown $(whoami) fil.txt     # Om du behöver äga filen
```

---

## 🛡️ Säkerhetsprinciper – Best Practices

| Princip | Vad det betyder | Exempel |
|---------|-----------------|---------|
| **Least Privilege** | Ge minimal access | 644 istället för 666 |
| **Aldrig 777** | Alla kan göra allt | 🚫 Säkerhetsrisk |
| **Secrets = 600** | Bara ägaren ser | SSH-nycklar, .env |
| **Webserver-filer** | Läsbar, inte skrivbar | 644 för HTML/CSS/JS |

**⚠️ ALDRIG gör detta:**
```bash
chmod 777 /var/www               # 🚫 Alla kan ändra din webapp
chmod 666 .env                   # 🚫 Alla kan läsa dina secrets
chmod 777 ~/.ssh/id_rsa          # 🚫 SSH kommer vägra + säkerhetsrisk
```

---

## 📋 Quick Reference Card

```bash
# PERMISSIONS CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# FIL/ANVÄNDNING              PERMISSION    KOMMANDO
# ═══════════════════════════════════════════════════════════
# Script som ska köras        rwxr-xr-x     chmod 755
# Config-fil                  rw-r--r--     chmod 644
# SSH privat nyckel           rw-------     chmod 600
# SSH publik nyckel           rw-r--r--     chmod 644
# .env / secrets              rw-------     chmod 600
# Webbkatalog                 rwxr-xr-x     chmod 755
# Upload-katalog              rwxrwxr-x     chmod 775
# /tmp                        rwxrwxrwt     chmod 1777
# ═══════════════════════════════════════════════════════════

# VANLIGA FIXAR
chmod +x script.sh              # Gör körbar
sudo chown -R $USER:$USER ./    # Gör dig till ägare
sudo chown -R www-data:www-data /var/www/  # Webserver äger
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

## 📦 Varför detta är viktigt för DevOps

**Scenario:** Din server har 50GB loggar. Diskutrymmet tar slut. Din backup tar 3 timmar att överföra.

**Lösningen:** Komprimering kan minska 50GB → 5GB, och överföringstiden från 3 timmar → 20 minuter.

I DevOps-världen komprimerar du KONSTANT:
- 📋 **Loggar** – roteras och gzippas automatiskt
- 💾 **Backups** – måste vara komprimerade för att spara utrymme
- 🚀 **Deployments** – artifacts packas och skickas
- 📊 **Data exports** – stora dataset zipas innan överföring

---

## 🧠 Förstå formaten – Vilket ska du använda?

```
┌─────────────────────────────────────────────────────────────────────┐
│ FORMAT        │ KOMPRIMERING │ HASTIGHET  │ NÄR DU ANVÄNDER DET     │
├───────────────┼──────────────┼────────────┼─────────────────────────┤
│ .tar          │ Ingen        │ Snabbast   │ Bara paketera filer     │
│ .tar.gz/.tgz  │ Bra (~70%)   │ Snabb      │ ⭐ STANDARD för Linux   │
│ .tar.bz2      │ Bättre       │ Långsam    │ När storlek är kritisk  │
│ .tar.xz       │ Bäst         │ Långsammast│ Distributionspaket      │
│ .zip          │ Bra          │ Snabb      │ Windows-kompatibilitet  │
│ .gz           │ Bra          │ Snabb      │ Enskilda filer          │
└─────────────────────────────────────────────────────────────────────┘
```

**💡 Tumregel:** Använd `.tar.gz` som default. Det är Linux-standarden.

---

## 🏆 TOP 10 – Kommandon du måste kunna

| # | Kommando | Vad det gör | Minnesregel |
|---|----------|-------------|-------------|
| 1 | `tar -czvf` | **C**reate g**Z**ip **V**erbose **F**ile | "Create Zip Verbose File" |
| 2 | `tar -xzvf` | e**X**tract från .tar.gz | "eXtract" |
| 3 | `tar -tzvf` | Lis**T**a innehåll | "lisT" |
| 4 | `gzip/gunzip` | Komprimera/expandera | Snabb komprimering |
| 5 | `zip -r/unzip` | Windows-format | När du delar med Windows |
| 6 | `tar -xjvf` | Extract .tar.bz2 | **j** = bzip2 |
| 7 | `zcat` | Visa gzippad fil | cat för .gz |
| 8 | `tar --exclude` | Hoppa över filer | Skippa node_modules |
| 9 | `pigz` | Parallell gzip | Multicore-komprimering |
| 10 | `tar -C` | Extract till annan plats | **C**hange directory |

---

## 📦 tar – Tape ARchive (trots namnet, inte bara för band!)

### Skapa arkiv

```bash
# GRUNDLÄGGANDE – Skapa .tar.gz (vanligast!)
tar -czvf backup.tar.gz katalog/
#     │││└─ f = filename (sist! följt av filnamnet)
#     ││└── v = verbose (visa vad som händer)
#     │└─── z = gzip compression
#     └──── c = create (skapa nytt arkiv)

# EXEMPEL
tar -czvf projekt.tar.gz ./mitt-projekt/
# Output:
# mitt-projekt/
# mitt-projekt/package.json
# mitt-projekt/src/
# mitt-projekt/src/index.js
# ...

# UTAN VERBOSE (tyst)
tar -czf backup.tar.gz katalog/
```

### Packa upp arkiv

```bash
# PACKA UPP .tar.gz
tar -xzvf backup.tar.gz
#     └── x = extract (packa upp)

# PACKA UPP TILL SPECIFIK KATALOG
tar -xzvf backup.tar.gz -C /var/www/
#                       └── -C = change to directory first

# BARA SE VAD SOM FINNS I ARKIVET (utan att packa upp)
tar -tzvf backup.tar.gz
#     └── t = list (test/list contents)
```

### Avancerade tar-tricks

```bash
# EXKLUDERA FILER (superviktigt för node_modules!)
tar -czvf projekt.tar.gz ./projekt \\
    --exclude='node_modules' \\
    --exclude='*.log' \\
    --exclude='.git'

# PACKA UPP BARA EN FIL FRÅN ARKIVET
tar -xzvf backup.tar.gz projekt/config.yml

# APPEND (lägg till filer till existerande arkiv) - BARA för .tar, inte .tar.gz!
tar -rvf arkiv.tar nyfil.txt

# MED BZIP2 (bättre komprimering, långsammare)
tar -cjvf arkiv.tar.bz2 katalog/
#     └── j = bzip2
tar -xjvf arkiv.tar.bz2

# MED XZ (bäst komprimering, långsammast)
tar -cJvf arkiv.tar.xz katalog/
#     └── J = xz
tar -xJvf arkiv.tar.xz
```

---

## 🗜️ gzip/gunzip – Komprimera enskilda filer

```bash
# KOMPRIMERA (original försvinner, ersätts med .gz)
gzip access.log                  # → access.log.gz
gzip -k access.log               # -k = keep (behåll originalet)

# EXPANDERA
gunzip access.log.gz             # → access.log
gzip -d access.log.gz            # Samma sak (-d = decompress)

# VISA UTAN ATT EXPANDERA
zcat access.log.gz               # Visar innehållet
zcat access.log.gz | grep ERROR  # Sök i komprimerad logg

# KOMPRIMERINGSGRAD (1-9, default 6)
gzip -9 stort-dataset.json       # Max komprimering (långsamt)
gzip -1 snabb-backup.tar         # Snabbast (mindre komprimering)
```

**💡 DevOps-tips:** Logrotate använder gzip automatiskt. Du kommer se massor av `.log.1.gz`, `.log.2.gz` i `/var/log/`.

---

## 📁 zip/unzip – När du måste dela med Windows-folk

```bash
# SKAPA ZIP (rekursivt för kataloger)
zip -r projekt.zip katalog/
#   └── -r = recursive (inkludera undermappar)

# PACKA UPP
unzip projekt.zip
unzip projekt.zip -d /destination/    # Till specifik plats

# VISA INNEHÅLL
unzip -l projekt.zip                  # Lista utan att packa upp

# EXKLUDERA
zip -r projekt.zip katalog/ -x "*.log" -x "*node_modules*"

# KRYPTERA (om du MÅSTE skicka känslig data)
zip -e hemlig.zip secret.txt          # Frågar efter lösenord
```

---

## 🚀 Verkliga DevOps-scenarier

### Scenario 1: Daglig backup med datum

```bash
#!/bin/bash
# backup.sh - Körs via cron varje natt

DATUM=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"
APP_DIR="/var/www/app"

# Skapa backup med datum i filnamnet
tar -czvf "${BACKUP_DIR}/app_${DATUM}.tar.gz" \\
    --exclude='node_modules' \\
    --exclude='*.log' \\
    --exclude='.git' \\
    "$APP_DIR"

# Resultat: /backups/app_20231221_143022.tar.gz

# Rensa gamla backups (behåll 7 dagar)
find "$BACKUP_DIR" -name "app_*.tar.gz" -mtime +7 -delete
```

### Scenario 2: Deployment artifact

```bash
# I CI/CD pipeline - skapa deployment-paket
cd /build

# Bygg och paketera
npm run build
tar -czvf "release-v${VERSION}.tar.gz" \\
    ./dist \\
    ./package.json \\
    ./package-lock.json

# Ladda upp till artifact storage
aws s3 cp "release-v${VERSION}.tar.gz" s3://artifacts/releases/
```

### Scenario 3: Transferera stora filer snabbt

```bash
# Problem: Kopiera 10GB data över nätverk

# LÅNGSAMT (okomprimerat)
scp -r /data server:/backup/              # 10GB transfer

# SNABBARE (komprimera + pipe direkt)
tar -czf - /data | ssh server "tar -xzf - -C /backup/"
#     └── - betyder stdout/stdin (ingen temp-fil!)

# Med progress bar (pv måste installeras)
tar -cf - /data | pv | gzip | ssh server "gunzip | tar -xf - -C /backup/"
```

### Scenario 4: Söka i komprimerade loggar

```bash
# Dina loggar är gzippade av logrotate
ls /var/log/nginx/
# access.log
# access.log.1.gz
# access.log.2.gz
# ...

# SÖK I ALLA LOGGAR (både aktiv och komprimerade)
zgrep "404" /var/log/nginx/access.log*      # zgrep kan läsa .gz direkt!
zcat /var/log/nginx/access.log.*.gz | grep "500" | wc -l
```

---

## ⚡ Parallell komprimering – pigz & pbzip2

```bash
# Problem: gzip använder bara EN CPU-kärna
# Lösning: pigz (parallel implementation of gzip)

# Installera
sudo apt install pigz pbzip2

# Använd (drop-in replacement för gzip)
tar -cvf - katalog/ | pigz > backup.tar.gz

# Med tar direkt
tar -I pigz -cvf backup.tar.gz katalog/
#   └── -I = use this compressor

# Parallell bzip2
tar -I pbzip2 -cvf backup.tar.bz2 katalog/

# HASTIGHETSVINST på 8-core server:
# gzip:  100GB → 2 timmar
# pigz:  100GB → 15 minuter 🚀
```

---

## 📋 Quick Reference Card

```bash
# KOMPRIMERING CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# SKAPA ARKIV
tar -czvf arkiv.tar.gz katalog/       # ⭐ Standard
tar -cjvf arkiv.tar.bz2 katalog/      # Bättre komprimering
zip -r arkiv.zip katalog/              # Windows-kompatibelt

# PACKA UPP
tar -xzvf arkiv.tar.gz                 # Här (tar.gz)
tar -xzvf arkiv.tar.gz -C /dest/       # Till annan plats
tar -xjvf arkiv.tar.bz2                # bzip2
unzip arkiv.zip                        # zip

# VISA INNEHÅLL
tar -tzvf arkiv.tar.gz                 # Lista
unzip -l arkiv.zip                     # Lista zip

# KOMPRIMERA ENSKILD FIL
gzip fil.txt                           # → fil.txt.gz
gzip -k fil.txt                        # Behåll original

# VISA KOMPRIMERAD
zcat fil.txt.gz                        # Visa innehåll
zgrep "sök" *.gz                       # Sök i gzippade filer
# ═══════════════════════════════════════════════════════════

# TAR FLAGS MINNESREGEL:
# c = Create     x = eXtract    t = lisT
# z = gZip       j = bzip2      J = xz
# v = Verbose    f = File (ALLTID SIST!)
# C = Change directory before extracting
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

## � Varför detta är FUNDAMENTALT för DevOps

**Scenario:** Du deployer samma app till tre miljöer – dev, staging, prod. Samma kod, men olika databaser, olika API-nycklar, olika konfigurationer.

**Lösningen:** Miljövariabler. Koden läser `$DATABASE_URL` och får rätt värde beroende på var den körs.

**12-Factor App säger:** *"Store config in the environment"*. Det är DevOps-standarden.

```
┌────────────────────────────────────────────────────────────────┐
│  SAMMA KOD                                                     │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  import os                                                │ │
│  │  db = os.environ["DATABASE_URL"]                         │ │
│  └──────────────────────────────────────────────────────────┘ │
│            │              │              │                     │
│            ▼              ▼              ▼                     │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │
│   │    DEV      │ │   STAGING   │ │    PROD     │             │
│   │ localhost   │ │ staging.db  │ │ prod.db.aws │             │
│   └─────────────┘ └─────────────┘ └─────────────┘             │
└────────────────────────────────────────────────────────────────┘
```

---

## 🏆 TOP 10 – Kommandon du måste kunna

| # | Kommando | Vad det gör | När du använder det |
|---|----------|-------------|---------------------|
| 1 | `export VAR=value` | Sätt miljövariabel | Konfigurera appar |
| 2 | `echo $VAR` | Visa värde | Debug och verify |
| 3 | `env` | Visa ALLA variabler | Se hela miljön |
| 4 | `printenv VAR` | Visa specifik | Snabb check |
| 5 | `unset VAR` | Ta bort variabel | Rensa konfiguration |
| 6 | `source ~/.bashrc` | Ladda om config | Applicera ändringar |
| 7 | `VAR=x command` | Temporär för ett kommando | Test utan att ändra |
| 8 | `$PATH` | Kommando-sökvägar | Hitta installerade program |
| 9 | `~/.bashrc` | Permanent config | Variabler som alltid ska finnas |
| 10 | `env -i command` | Kör med tom miljö | Isolera tester |

---

## 🧠 Förstå variabler – Shell vs Environment

Det finns en VIKTIG skillnad:

```bash
# SHELL-VARIABEL (bara i denna session, inte till child-processer)
MY_VAR="hejsan"
echo $MY_VAR                     # → hejsan
bash -c 'echo $MY_VAR'           # → (tomt! child-process ser den inte)

# MILJÖVARIABEL (exporteras till child-processer)
export MY_VAR="hejsan"
echo $MY_VAR                     # → hejsan
bash -c 'echo $MY_VAR'           # → hejsan ✅

# MINNESREGEL:
# export = "gör variabeln synlig för ALLA processer som startar härifrån"
```

---

## 🔧 Sätta och använda variabler

### Grundläggande syntax

```bash
# SÄTTA VARIABLER
export DATABASE_URL="postgres://localhost:5432/mydb"
export NODE_ENV="production"
export DEBUG=true

# ⚠️ VIKTIGT: INGA MELLANSLAG runt =
# RÄTT:  export VAR=value
# FEL:   export VAR = value  ❌

# MED MELLANSLAG I VÄRDET – använd citationstecken
export MESSAGE="Hello World"
export PATH_WITH_SPACES="/My Documents/scripts"

# LÄSA VÄRDEN
echo $DATABASE_URL              # Enkelt
echo "URL är: $DATABASE_URL"    # I text
echo ${DATABASE_URL}            # Explicit syntax
echo "${DATABASE_URL}_suffix"   # När du bygger strängar
```

### Default-värden (superhändigt!)

```bash
# OM VARIABELN INTE ÄR SATT – använd default
echo ${PORT:-8080}              # Om PORT inte finns → 8080
echo ${DB_HOST:-localhost}      # Om DB_HOST inte finns → localhost

# SÄTT VARIABELN OM DEN INTE FINNS
: ${PORT:=8080}                 # Sätter PORT till 8080 om tom
: ${NODE_ENV:=development}      # Default till development

# I SCRIPTS (vanligt mönster)
#!/bin/bash
PORT=${PORT:-8080}
HOST=${HOST:-0.0.0.0}
echo "Starting server on $HOST:$PORT"
```

---

## 📂 Viktiga systemvariabler

```bash
# DESSA FINNS ALLTID
echo $HOME                       # /home/said – din hemkatalog
echo $USER                       # said – ditt användarnamn
echo $SHELL                      # /bin/bash – din shell
echo $PWD                        # /var/www/app – nuvarande katalog
echo $HOSTNAME                   # server01 – maskinens namn
echo $LANG                       # sv_SE.UTF-8 – språkinställning

# DESSA ÄR SPECIELLT VIKTIGA FÖR DEVOPS
echo $PATH                       # Var systemet letar efter kommandon
echo $LD_LIBRARY_PATH            # Var dynamiska bibliotek finns
echo $EDITOR                     # Default editor (vim, nano, etc.)

# PROCESS-RELATERADE
echo $$                          # PID för denna shell
echo $?                          # Exit code från förra kommandot
echo $!                          # PID för senaste background-process
```

### $PATH – Förstå hur kommandon hittas

```bash
# PATH är en kolon-separerad lista av kataloger
echo $PATH
# /usr/local/bin:/usr/bin:/bin:/home/said/bin

# När du skriver "python", söker systemet i ordning:
# 1. /usr/local/bin/python
# 2. /usr/bin/python
# 3. /bin/python
# 4. /home/said/bin/python
# FÖRSTA MATCH vinner!

# LÄGG TILL TILL PATH
export PATH=$PATH:/opt/myapp/bin           # Lägg till sist
export PATH=/opt/myapp/bin:$PATH           # Lägg till först (prioritet!)

# VAR FINNS ETT KOMMANDO?
which python                     # /usr/bin/python
which -a python                  # ALLA python som finns i PATH
type python                      # Mer info om vad det är
```

---

## 💾 Permanenta vs temporära variabler

### Temporär (bara denna session)

```bash
# Försvinner när du stänger terminalen
export MY_VAR="hejsan"
```

### Permanent (för din användare)

```bash
# Lägg i ~/.bashrc (körs vid varje ny terminal)
echo 'export MY_VAR="hejsan"' >> ~/.bashrc
echo 'export PATH=$PATH:/opt/scripts' >> ~/.bashrc

# LADDA OM UTAN ATT ÖPPNA NY TERMINAL
source ~/.bashrc
# eller kortare:
. ~/.bashrc
```

### Systemvida (för alla användare)

```bash
# /etc/environment – enkla VAR=värde (ingen export)
DATABASE_URL=postgres://...

# /etc/profile.d/*.sh – scripts som körs vid login
sudo vi /etc/profile.d/myapp.sh
# export APP_HOME=/opt/myapp
# export PATH=$PATH:$APP_HOME/bin
```

### Per-kommando (bara för det kommandot)

```bash
# Variabeln gäller BARA för detta kommando
NODE_ENV=production npm start
DEBUG=true ./myapp
DATABASE_URL=test://db ./migrate

# Kombinera flera
NODE_ENV=production PORT=3000 npm start
```

---

## 🚀 Verkliga DevOps-scenarier

### Scenario 1: .env-filer (12-Factor App)

```bash
# .env fil (ALDRIG committa till git!)
DATABASE_URL=postgres://prod:secret@db.aws.com/app
REDIS_URL=redis://cache.aws.com
SECRET_KEY=super_secret_123
NODE_ENV=production

# Ladda .env-fil i bash-script
#!/bin/bash
set -a                           # Auto-export alla variabler
source .env
set +a

# Eller mer robust:
export $(grep -v '^#' .env | xargs)

# Verifiera
env | grep DATABASE
```

### Scenario 2: Docker & miljövariabler

```bash
# Docker kör med -e för miljövariabler
docker run -e NODE_ENV=production \\
           -e DATABASE_URL=$DATABASE_URL \\
           myapp

# Eller läs från fil
docker run --env-file .env myapp

# docker-compose.yml
# services:
#   app:
#     environment:
#       - NODE_ENV=production
#       - DATABASE_URL
#     env_file:
#       - .env
```

### Scenario 3: CI/CD pipelines

```yaml
# GitHub Actions
jobs:
  deploy:
    env:
      NODE_ENV: production
    steps:
      - run: echo $NODE_ENV
      # Använd secrets (aldrig hårdkoda!)
      - run: ./deploy.sh
        env:
          API_KEY: ${{ secrets.API_KEY }}

# Jenkins
environment {
    DATABASE_URL = credentials('db-url')
}
```

### Scenario 4: Felsök "command not found"

```bash
# Problem: Du installerade något men kan inte hitta det
nvm install 18                   # Installerar node
node --version                   # "command not found" 😱

# Diagnos
echo $PATH                       # Se vad som finns
which node                       # Finns den?

# Lösning: NVM lägger till i PATH, men du måste ladda om
source ~/.nvm/nvm.sh
# Eller lägg i ~/.bashrc så det alltid finns

# VERIFIERING
node --version                   # v18.x.x ✅
```

---

## ⚠️ Säkerhet – ALDRIG committa secrets!

```bash
# ❌ ALDRIG GÖR DETTA
export API_KEY=sk-123456789     # Kan ses i process list!
git add .env                     # ALDRIG committa .env!

# ✅ GÖR DETTA ISTÄLLET
# 1. Lägg .env i .gitignore
echo ".env" >> .gitignore

# 2. Skapa .env.example (mall utan secrets)
# DATABASE_URL=postgres://user:PASSWORD@host/db
# API_KEY=your_key_here

# 3. Använd secrets manager i produktion
# - AWS Secrets Manager
# - HashiCorp Vault
# - GitHub Secrets
# - Docker Secrets
```

---

## 📋 Quick Reference Card

```bash
# MILJÖVARIABLER CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# SÄTTA VARIABLER
export VAR=value                 # Med export → synlig för child
VAR=value                        # Utan export → bara denna shell
VAR=value command                # Bara för det kommandot

# LÄSA VARIABLER
echo $VAR                        # Enkel
echo ${VAR}                      # Explicit
echo ${VAR:-default}             # Med default om tom
printenv VAR                     # Bara miljövariabler

# VISA ALLA
env                              # Alla miljövariabler
env | grep PATTERN               # Filtrera
declare -p                       # Alla variabler (inkl. shell)

# TA BORT
unset VAR                        # Ta bort variabel

# PERMANENTA PLATSER
~/.bashrc                        # Din användare (bash)
~/.profile                       # Din användare (alla shells)
/etc/environment                 # Systemvida
/etc/profile.d/*.sh              # Systemvida scripts

# LADDA OM CONFIG
source ~/.bashrc                 # Ladda om bashrc
. ~/.bashrc                      # Samma sak (kortare)

# LADDA .env-FIL
set -a; source .env; set +a
export $(grep -v '^#' .env | xargs)
# ═══════════════════════════════════════════════════════════
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

## 💾 Varför detta är KRITISKT för DevOps

**03:00 på natten. PagerDuty ringer.**

```
🚨 ALERT: Disk space critical on prod-server-01
   / filesystem at 98% capacity
```

Varje DevOps-ingenjör har varit där. Disken är full. Databasen kan inte skriva. Appen kraschar. Kaos.

**Lär dig detta nu så du kan:**
- 🔍 Snabbt hitta VAD som tar plats
- 🗑️ Rensa upp säkert
- 📊 Övervaka INNAN det blir kritiskt
- 💿 Lägga till mer utrymme

---

## 🏆 TOP 10 – Kommandon du MÅSTE kunna

| # | Kommando | Vad det gör | När du använder det |
|---|----------|-------------|---------------------|
| 1 | `df -h` | Ledigt utrymme per partition | "Hur mycket plats har jag kvar?" |
| 2 | `du -sh` | Katalogstorlek | "Hur stor är denna mappen?" |
| 3 | `lsblk` | Lista diskar & partitioner | "Vilka diskar finns?" |
| 4 | `mount` | Montera filsystem | Göra disk tillgänglig |
| 5 | `umount` | Avmontera | Innan du kopplar bort |
| 6 | `fdisk -l` | Partitionsinformation | Se partitioner i detalj |
| 7 | `mkfs.ext4` | Formatera disk | Ny disk som ska användas |
| 8 | `/etc/fstab` | Permanent montering | Overleva omstart |
| 9 | `ncdu` | Interaktiv diskanalys | Hitta vad som tar plats |
| 10 | `blkid` | Visa UUID för diskar | Identifiera diskar unikt |

---

## 📊 df – Visa diskutrymme ("Disk Free")

```bash
# GRUNDLÄGGANDE
df -h                            # ⭐ Human-readable (GB, MB)
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       100G   75G   25G  75% /
# /dev/sdb1       500G  350G  150G  70% /data
# tmpfs           8.0G  1.2G  6.8G  15% /dev/shm

# 💡 Kolumner förklarade:
# Size  = Total storlek
# Used  = Använt
# Avail = Ledigt
# Use%  = Procent använt (HÅLL UNDER 80%!)
# Mounted on = Var den finns i filsystemet

# FILTRERA OUTPUT
df -h /                          # Bara root-partitionen
df -h /var                       # Var finns /var?
df -h | grep -v tmpfs            # Skippa RAM-baserade

# INODES (antalet filer, inte storlek)
df -i                            # Inode-användning
# Om 100% inodes men disk har plats = för många små filer!
```

### 🚨 Alert-nivåer:

| Procent | Status | Åtgärd |
|---------|--------|--------|
| < 70% | ✅ OK | Inget |
| 70-85% | ⚠️ Varning | Planera städning |
| 85-95% | 🔶 Kritisk | Städa NU |
| > 95% | 🔴 Nöd | Akut – allt kan sluta fungera |

---

## 📦 du – Hitta vad som tar plats ("Disk Usage")

```bash
# GRUNDLÄGGANDE
du -sh katalog/                  # ⭐ Total storlek för en katalog
du -sh /var/log                  # Hur stora är loggarna?
du -sh /home/*                   # Varje användares hemkatalog

# HITTA TJUVARNA – Sortera efter storlek
du -h --max-depth=1 / | sort -h | tail -20
#                │           │         └── Top 20 största
#                │           └── Sortera numeriskt
#                └── Bara en nivå ner (inte rekursivt)

# HITTA STORA FILER DIREKT
find / -type f -size +100M -exec ls -lh {} \\; 2>/dev/null | sort -k5 -h
#                    │                                        └── Sortera på storlek
#                    └── Filer större än 100MB

# VANLIGA PLATSER SOM VÄXER
du -sh /var/log                  # Loggar
du -sh /var/cache                # Cache
du -sh /tmp                      # Temporära filer
du -sh /var/lib/docker           # Docker data
du -sh ~/.local/share/Trash      # Papperskorgen
```

### 🎯 ncdu – Interaktiv diskanalys (INSTALLERA DETTA!)

```bash
# Installera
sudo apt install ncdu            # Debian/Ubuntu
sudo yum install ncdu            # RHEL/CentOS

# Använd
ncdu /                           # ⭐ Starta från root
ncdu /var                        # Analysera /var

# INTERFACE:
# - Använd piltangenter för att navigera
# - Enter för att gå in i katalog
# - d för att ta bort (bekräfta först!)
# - q för att avsluta

# Exportera rapport
ncdu -o rapport.json /
ncdu -f rapport.json             # Läs in igen senare
```

**💡 ncdu är det bästa verktyget för att hitta diskproblem!**

---

## 💿 lsblk & blkid – Förstå dina diskar

```bash
# VISA DISKAR OCH PARTITIONER
lsblk
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   100G  0 disk
# ├─sda1   8:1    0    99G  0 part /
# └─sda2   8:2    0     1G  0 part [SWAP]
# sdb      8:16   0   500G  0 disk
# └─sdb1   8:17   0   500G  0 part /data

# MED FILSYSTEM-INFO
lsblk -f
# NAME   FSTYPE LABEL UUID                                 MOUNTPOINT
# sda1   ext4         a1b2c3d4-...                         /
# sdb1   ext4   data  e5f6g7h8-...                         /data

# VISA UUID (behövs för /etc/fstab)
blkid
# /dev/sda1: UUID="a1b2c3d4-..." TYPE="ext4"
# /dev/sdb1: UUID="e5f6g7h8-..." TYPE="ext4"

blkid /dev/sdb1                  # Specifik disk
```

---

## 🔗 mount & umount – Montera filsystem

```bash
# SE VAD SOM ÄR MONTERAT
mount                            # Alla monteringar
mount | grep "^/dev"             # Bara riktiga diskar
findmnt                          # ⭐ Snyggare output

# MONTERA TILLFÄLLIGT
sudo mount /dev/sdb1 /mnt/data   # Montera partition
sudo mount /dev/cdrom /mnt/cdrom # Montera CD
sudo mount -t nfs server:/share /mnt/nfs  # NFS-share

# AVMONTERA
sudo umount /mnt/data
sudo umount -l /mnt/data         # Lazy unmount (om "device busy")

# ⚠️ "Device is busy"? Hitta processen:
lsof +f -- /mnt/data             # Vem använder den?
fuser -m /mnt/data               # PIDs som använder
```

### /etc/fstab – Permanenta monteringar (överlever omstart)

```bash
# Visa nuvarande
cat /etc/fstab

# FORMAT (kolumner separerade av mellanslag/tab):
# <device>          <mountpoint>  <type>  <options>     <dump> <pass>
# UUID=a1b2c3d4...  /             ext4    defaults      0      1
# UUID=e5f6g7h8...  /data         ext4    defaults      0      2
# /dev/sdb1         /backup       ext4    defaults,nofail 0    2

# 💡 Förklaring:
# device     = UUID eller /dev/xxx (UUID är säkrare!)
# mountpoint = Var den ska monteras
# type       = Filsystemtyp (ext4, xfs, nfs, etc.)
# options    = defaults, nofail, ro, noexec, etc.
# dump       = 0 (ignorera för backup)
# pass       = Boot-check ordning (1=root, 2=andra, 0=skippa)

# LÄGG TILL NY MONTERNING STEG FÖR STEG:
# 1. Hitta UUID
blkid /dev/sdb1
# /dev/sdb1: UUID="e5f6g7h8-..." TYPE="ext4"

# 2. Skapa mount point
sudo mkdir -p /mnt/data

# 3. Lägg till i fstab (FÖRSIKTIGT!)
echo 'UUID=e5f6g7h8-... /mnt/data ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab

# 4. TESTA INNAN OMSTART!
sudo mount -a                    # Montera allt i fstab
echo $?                          # 0 = OK

# ⚠️ FEL I FSTAB = SERVER STARTAR INTE!
# Använd alltid "nofail" för icke-kritiska diskar
```

---

## 🆕 Ny disk – Komplett workflow

```bash
# SCENARIO: Du har lagt till en ny 100GB disk (/dev/sdc)

# STEG 1: Verifiera att disken syns
lsblk
# sdc      8:32   0   100G  0 disk     ← Ny disk, ingen partition

# STEG 2: Skapa partition
sudo fdisk /dev/sdc
# n (new partition)
# p (primary)
# 1 (partition number)
# Enter (default first sector)
# Enter (default last sector = hela disken)
# w (write and exit)

# STEG 3: Formatera
sudo mkfs.ext4 /dev/sdc1
# eller
sudo mkfs.xfs /dev/sdc1          # XFS är bättre för stora filer

# STEG 4: Skapa mount point
sudo mkdir -p /mnt/newdisk

# STEG 5: Montera
sudo mount /dev/sdc1 /mnt/newdisk

# STEG 6: Gör permanent (fstab)
echo "UUID=$(blkid -s UUID -o value /dev/sdc1) /mnt/newdisk ext4 defaults,nofail 0 2" | sudo tee -a /etc/fstab

# STEG 7: Verifiera
df -h /mnt/newdisk
```

---

## 🧹 Rensa diskutrymme – Emergency Cleanup

```bash
#!/bin/bash
# cleanup.sh - Kör när disken är full!

echo "🔍 Analyserar diskutrymme..."
df -h /

echo "\\n📦 Top 10 största kataloger i /var:"
du -h --max-depth=1 /var 2>/dev/null | sort -h | tail -10

echo "\\n🗑️ Rensar systemcache..."
sudo apt clean                   # Rensa apt cache
sudo journalctl --vacuum-size=100M  # Begränsa journal till 100MB

echo "\\n📋 Rensar gamla loggar..."
sudo find /var/log -name "*.gz" -delete
sudo find /var/log -name "*.old" -delete
sudo find /var/log -name "*.[0-9]" -delete

echo "\\n🐳 Rensar Docker (om installerat)..."
docker system prune -af 2>/dev/null || true

echo "\\n🗑️ Rensar temporära filer..."
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

echo "\\n✅ Efter städning:"
df -h /
```

### Vanliga platser som tar plats:

| Plats | Vad det är | Säker att rensa? |
|-------|------------|------------------|
| `/var/log` | Loggar | ✅ Gamla .gz filer |
| `/var/cache/apt` | APT-cache | ✅ `apt clean` |
| `/var/lib/docker` | Docker | ⚠️ `docker system prune` |
| `/tmp` | Temp-filer | ✅ Men kolla först |
| `/home/*/.cache` | User cache | ✅ Men fråga användare |
| `/var/lib/snapd` | Snap-paket | ⚠️ Kan bryta saker |

---

## 📋 Quick Reference Card

```bash
# DISK MANAGEMENT CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# SE UTRYMME
df -h                            # Ledigt per partition
df -h /                          # Bara root
df -i                            # Inodes

# HITTA STORA SAKER
du -sh katalog/                  # Katalogstorlek
du -h --max-depth=1 / | sort -h  # Top directories
ncdu /                           # ⭐ Interaktiv analys

# DISKAR & PARTITIONER
lsblk                            # Lista diskar
lsblk -f                         # Med filsystem
blkid                            # UUID

# MONTERA
sudo mount /dev/sdb1 /mnt/data   # Montera
sudo umount /mnt/data            # Avmontera
mount | grep sdb                 # Se monteringar

# FORMATERA (VARNING: Raderar allt!)
sudo mkfs.ext4 /dev/sdb1         # ext4 format
sudo mkfs.xfs /dev/sdb1          # xfs format

# FSTAB (permanent montering)
# UUID=xxx-xxx /mnt/data ext4 defaults,nofail 0 2
sudo mount -a                    # Testa fstab

# EMERGENCY CLEANUP
sudo apt clean                   # APT cache
sudo journalctl --vacuum-size=100M
docker system prune -af          # Docker cleanup
# ═══════════════════════════════════════════════════════════
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

## 🚑 Varför du BEHÖVER ett systematiskt tillvägagångssätt

**Det är 03:00. PagerDuty ringer. Produktionen är nere.**

Panik? Nej. Du har ett **systematiskt felsökningsflöde**. Du vet exakt var du ska börja och vad du ska kolla. Inom 10 minuter har du hittat problemet.

Det är skillnaden mellan en junior som chansar, och en senior som metodiskt isolerar problemet.

---

## 🏥 Daglig hälsokontroll – "Hur mår servern?"

Kör dessa kommandon varje morgon (eller automatisera dem!):

```bash
# 1. SNABB ÖVERBLICK (30 sekunder)
uptime                          # Load + hur länge servern varit uppe
# Output: 10:30:00 up 45 days, load average: 0.15, 0.20, 0.18
#                               └── Ska vara < antal CPU-kärnor!

free -h                         # RAM-användning
# Output:        total    used    free    available
#   Mem:         16Gi    12Gi    2.0Gi      3.5Gi
#                              └── Om < 500MB → varning!

df -h                           # Diskutrymme
# Output: /dev/sda1  100G   75G   25G  75% /
#                                 └── Om > 85% → fixa!

# 2. PROCESSER (vad jobbar hårt?)
ps aux --sort=-%cpu | head -5   # Top 5 CPU-användare
ps aux --sort=-%mem | head -5   # Top 5 RAM-användare

# 3. SERVICES (något som kraschat?)
systemctl --failed              # Lista alla failade services
# Om något visas → det är ett problem!

# 4. SENASTE ERRORS
journalctl -p err --since "24 hours ago" --no-pager | tail -20
```

### 💡 Pro-tip: Skapa ett diagnostik-script!

```bash
#!/bin/bash
# healthcheck.sh - Kör varje morgon

echo "=== 🖥️  SYSTEM STATUS $(date) ==="
echo ""
echo "📊 Load & Uptime:"
uptime
echo ""
echo "🧠 Memory:"
free -h | grep Mem
echo ""
echo "💾 Disk:"
df -h / | tail -1
echo ""
echo "🔴 Failed Services:"
systemctl --failed --no-pager
echo ""
echo "⚠️  Recent Errors (last hour):"
journalctl -p err --since "1 hour ago" --no-pager | tail -10 || echo "None!"
echo ""
echo "=== ✅ CHECK COMPLETE ==="
```

---

## 🔧 Felsökningsflöden – Systematiska checklists

### 🔴 "Appen funkar inte!"

```bash
# STEG 1: Kör processen överhuvudtaget?
systemctl status myapp
# → active (running) = OK
# → failed = PROBLEM

# STEG 2: Vad säger loggarna?
journalctl -u myapp -n 50 --no-pager
# Sök efter ERROR, Exception, Failed

# STEG 3: Lyssnar den på rätt port?
ss -tlnp | grep :3000
# Om tom output = appen lyssnar inte!

# STEG 4: Kan du nå den lokalt?
curl -v localhost:3000/health
# Timeout? → App hänger
# Connection refused? → App körs inte
# 500 error? → App kraschar vid request

# STEG 5: Kan du nå den externt?
curl -v https://myapp.com/health
# Funkar lokalt men inte externt? → Brandvägg/reverse proxy problem

# STEG 6: Testa att starta manuellt
sudo systemctl stop myapp
sudo -u www-data /opt/myapp/start.sh
# Ser du felet i terminalen nu?
```

### 💾 "Disk full!"

```bash
# STEG 1: Vilken partition är full?
df -h
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       100G   98G   2G   98% /     ← DEN!

# STEG 2: Vad tar plats? (start från root)
du -h --max-depth=1 / 2>/dev/null | sort -h | tail -10
# /var = 50G? Gå djupare!

du -h --max-depth=1 /var | sort -h | tail -10
# /var/log = 45G? Hittat!

# STEG 3: Hitta de stora filerna
find /var/log -type f -size +100M -exec ls -lh {} \\;

# STEG 4: Finns deleted-but-open filer? (sneaky!)
lsof | grep deleted | head -20
# Om ja → restart av den processen frigör utrymmet

# STEG 5: Safe cleanup
sudo journalctl --vacuum-size=500M  # Loggar
sudo apt clean                       # APT cache
docker system prune -af              # Docker (om installerat)
```

### 🌐 "Nätverket funkar inte!"

```bash
# SYSTEMATISK CHECKLISTA (kör i ordning!)

# 1. Har vi IP?
ip addr
# Om ingen IP → DHCP problem eller kabel/wifi

# 2. Funkar loopback?
ping -c 2 127.0.0.1
# Om timeout → systemet är väldigt trasigt

# 3. Kan vi nå gateway?
ping -c 2 $(ip route | grep default | awk '{print $3}')
# Om timeout → lokalt nätverksproblem

# 4. Kan vi nå internet?
ping -c 2 8.8.8.8
# Om timeout → ISP/routing problem

# 5. Fungerar DNS?
dig google.com +short
# Om ingen output → DNS problem
# Testa: cat /etc/resolv.conf

# 6. Kan vi nå specifik tjänst?
nc -zv target-server.com 443
# Om timeout → brandvägg blockerar

# 7. Lokal brandvägg?
sudo ufw status                 # Ubuntu
sudo iptables -L -n             # Alla distros
```

### 🐌 "Servern är långsam!"

```bash
# STEG 1: Vad är load?
uptime
# load average: 10.5, 8.2, 6.1
# Om load > antal CPU-kärnor → ÖVERBELASTAD

# STEG 2: Är det CPU eller wait?
top
# Titta på %us (user) och %wa (I/O wait)
# Hög %us = CPU-intensiv process
# Hög %wa = Disk/IO flaskhals

# STEG 3: Vem använder CPU?
ps aux --sort=-%cpu | head -10

# STEG 4: Vem använder RAM?
ps aux --sort=-%mem | head -10
free -h

# STEG 5: Disk I/O?
iostat -x 1 5
# Om %util > 80% för en disk → I/O flaskhals

# STEG 6: Nätverks-flaskhals?
iftop                           # Kräver installation
# eller
ss -s                           # Nätverksstatistik
```

---

## 📋 Emergency Cheat Sheet

```bash
# 🔴 AKUT: Service nere
systemctl restart myapp && journalctl -u myapp -f

# 💾 AKUT: Disk full
df -h && du -sh /var/* | sort -h && sudo journalctl --vacuum-size=100M

# 🐌 AKUT: Servern hänger
top                              # Se vad som kör
kill -9 PID                      # Döda syndern (sista utväg!)

# 🔥 AKUT: Kan inte logga in
# 1. Prova en annan terminal/SSH-klient
# 2. Kolla om disk är full (kan hindra SSH)
# 3. Använd serverkonsol (AWS Console, etc.)

# 🌐 AKUT: Sidan nere för alla
curl -I https://mysite.com       # Svarar origin?
curl -I https://mysite.com --resolve mysite.com:443:ORIGIN_IP
# Om origin OK → Problem med CDN/load balancer

# 🔐 AKUT: Glömt root-lösenord
# Starta i recovery mode, mount root rw, passwd root
```

---

## 🧰 Din verktygslåda – Memorera dessa!

| Symptom | Första kommando |
|---------|-----------------|
| "Vad kör servern?" | `uptime && free -h && df -h` |
| "Service nere" | `systemctl status NAME` |
| "Vad säger loggarna?" | `journalctl -u NAME -n 100` |
| "Vilken process tar CPU?" | `ps aux --sort=-%cpu | head` |
| "Vilken process tar RAM?" | `ps aux --sort=-%mem | head` |
| "Vad tar diskplats?" | `du -sh /* | sort -h | tail` |
| "Vilka portar lyssnar?" | `ss -tulpn` |
| "Kan jag nå internet?" | `ping 8.8.8.8` |
| "Funkar DNS?" | `dig google.com` |
| "Senaste errors?" | `journalctl -p err --since "1h"` |
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

## 👥 Varför detta är viktigt för DevOps

**Scenario:** Ny utvecklare börjar på måndag. Hon behöver:
- SSH-access till alla servrar
- Kunna köra Docker-kommandon
- Sudo-access för deployment
- Ingå i rätt grupper för filrättigheter

**Om du inte förstår users & groups:**
- 🚫 "Permission denied" överallt
- 🚫 SSH fungerar inte
- 🚫 Docker vägrar köra
- 🚫 Säkerhetsrisker med för bred access

---

## 🧠 Förstå users & groups

```
┌─────────────────────────────────────────────────────────────────┐
│  Linux Security Model                                           │
│  ═══════════════════                                           │
│                                                                  │
│  USER (alice)                                                    │
│    └── UID: 1001                                                │
│    └── Primary Group: alice (GID: 1001)                         │
│    └── Secondary Groups: docker, sudo, developers               │
│                                                                  │
│  När alice skapar en fil:                                       │
│    -rw-r--r-- 1 alice alice ... fil.txt                        │
│                  │      │                                        │
│                  │      └── Group = hennes primary group        │
│                  └── Owner = alice                               │
└─────────────────────────────────────────────────────────────────┘
```

**Viktiga filer:**
| Fil | Innehåller |
|-----|------------|
| `/etc/passwd` | Alla användare (läsbar av alla) |
| `/etc/shadow` | Lösenordshashes (bara root) |
| `/etc/group` | Alla grupper |
| `/etc/sudoers` | Sudo-rättigheter |

---

## 🏆 TOP 10 – Kommandon du måste kunna

| # | Kommando | Vad det gör | När du använder det |
|---|----------|-------------|---------------------|
| 1 | `useradd -m` | Skapa användare med hemkatalog | Ny teammedlem |
| 2 | `usermod -aG` | Lägg till i grupp | Ge Docker/sudo access |
| 3 | `userdel -r` | Ta bort användare + hemkatalog | Person lämnar |
| 4 | `passwd` | Sätt/ändra lösenord | Första login |
| 5 | `groupadd` | Skapa ny grupp | Team-kataloger |
| 6 | `id` | Visa UID, GID, grupper | Felsöka permissions |
| 7 | `groups` | Lista grupptillhörighet | Snabb check |
| 8 | `su -` | Byt till annan användare | Testa som annan |
| 9 | `sudo -i` | Bli root | Admin-uppgifter |
| 10 | `visudo` | Redigera sudoers säkert | Ge sudo-access |

---

## 👤 useradd – Skapa användare

```bash
# GRUNDLÄGGANDE (Undvik detta!)
sudo useradd alice              # Skapar användare utan hemkatalog ❌

# RÄTT SÄTT ⭐
sudo useradd -m -s /bin/bash alice
#            │   └── Shell (bash istället för sh)
#            └── Skapa hemkatalog (/home/alice)

# FULLSTÄNDIGT (bäst för automation)
sudo useradd \\
    -m \\                        # Skapa hemkatalog
    -s /bin/bash \\              # Sätt shell
    -c "Alice Developer" \\      # Kommentar/beskrivning
    -G docker,developers \\      # Extra grupper direkt
    alice

# SÄTT LÖSENORD EFTERÅT
sudo passwd alice
# Eller interaktivt:
echo "alice:password123" | sudo chpasswd

# VERIFIERA
id alice
# uid=1001(alice) gid=1001(alice) groups=1001(alice),999(docker),1002(developers)
```

### useradd flaggor:

| Flagga | Betydelse |
|--------|-----------|
| `-m` | Skapa hemkatalog |
| `-s SHELL` | Sätt login shell |
| `-c "TEXT"` | Kommentar (visas i /etc/passwd) |
| `-G grupp1,grupp2` | Extra grupper |
| `-u UID` | Specifikt UID |
| `-d /path` | Specifik hemkatalog |
| `-e DATUM` | Utgångsdatum (YYYY-MM-DD) |

---

## 🔧 usermod – Ändra användare

```bash
# LÄGG TILL I GRUPP ⭐ (vanligaste!)
sudo usermod -aG docker alice
#            ││
#            │└── Group (lägg till i grupp)
#            └── Append (KRITISKT! Utan -a ersätts alla grupper!)

# FLERA GRUPPER
sudo usermod -aG docker,sudo,developers alice

# ⚠️ VANLIGT MISSTAG:
sudo usermod -G docker alice     # ❌ RADERAR alla andra grupper!
sudo usermod -aG docker alice    # ✅ LÄGGER TILL utan att radera

# ANDRA ÄNDRINGAR
sudo usermod -l newname alice    # Byt användarnamn
sudo usermod -s /bin/zsh alice   # Byt shell
sudo usermod -L alice            # Lås kontot (kan inte logga in)
sudo usermod -U alice            # Lås upp kontot
```

### ⚠️ Gruppändringar kräver ny login!

```bash
# Alice lade till sig i docker-gruppen men "permission denied"?
sudo usermod -aG docker alice

# Det räcker INTE att köra:
source ~/.bashrc                  # ❌ Hjälper inte

# Alice måste:
# 1. Logga ut helt
# 2. Logga in igen
# ELLER (quick hack):
su - alice                        # Starta ny session
# ELLER:
newgrp docker                     # Aktivera gruppen temporärt
```

---

## 🗑️ userdel – Ta bort användare

```bash
# BARA ANVÄNDARE (behåll hemkatalog)
sudo userdel alice

# ⭐ ANVÄNDARE + HEMKATALOG + MAIL
sudo userdel -r alice
#            └── Remove all (hem + mail spool)

# PRAKTISKT: Avsluta anställd
sudo userdel -r alice
# Eller säkrare: lås först, ta bort senare
sudo usermod -L alice            # Lås direkt
# ... efter backup ...
sudo userdel -r alice
```

---

## 👥 Grupper – Team-samarbete

```bash
# SKAPA GRUPP
sudo groupadd developers
sudo groupadd -g 2000 webteam    # Med specifikt GID

# LÄGG TILL ANVÄNDARE
sudo usermod -aG developers alice
sudo usermod -aG developers bob

# SE GRUPMEDLEMMAR
getent group developers
# developers:x:1002:alice,bob

# TA BORT FRÅN GRUPP
sudo gpasswd -d alice developers

# TA BORT GRUPP
sudo groupdel developers
```

### Praktiskt: Team-katalog

```bash
# Skapa grupp och katalog för ett team
sudo groupadd projekt-x
sudo mkdir -p /opt/projekt-x
sudo chown root:projekt-x /opt/projekt-x
sudo chmod 2775 /opt/projekt-x
#          │
#          └── SetGID: Nya filer ärver gruppen automatiskt

# Lägg till teammedlemmar
sudo usermod -aG projekt-x alice
sudo usermod -aG projekt-x bob

# Nu kan alla i gruppen läsa/skriva i /opt/projekt-x
# OCH nya filer skapas med gruppen projekt-x automatiskt!
```

---

## 🔐 sudo – Privilegierad access

### Ge sudo-access

```bash
# METOD 1: Lägg till i sudo-gruppen (rekommenderat)
sudo usermod -aG sudo alice      # Debian/Ubuntu
sudo usermod -aG wheel alice     # RHEL/CentOS

# METOD 2: Specifik konfiguration via visudo
sudo visudo

# Lägg till en rad:
alice ALL=(ALL:ALL) ALL          # Full sudo med lösenord
alice ALL=(ALL) NOPASSWD: ALL    # ⚠️ Utan lösenord (CI/CD)

# BEGRÄNSAD SUDO (bättre säkerhet)
alice ALL=(ALL) /opt/deploy.sh   # Bara detta script
%developers ALL=(ALL) NOPASSWD: /usr/bin/docker  # Grupp
```

### sudoers syntax förklarad:

```
alice   ALL=(ALL:ALL)  ALL
│       │    │   │     │
│       │    │   │     └── Vilka kommandon (ALL = alla)
│       │    │   └── Som vilka grupper (ALL = alla)
│       │    └── Som vilka användare (ALL = alla, inkl root)
│       └── På vilka hosts (ALL = alla)
└── Vem som får sudo
```

### Byt användare

```bash
# BLI ROOT
sudo -i                          # ⭐ Root shell
sudo su -                        # Alternativ

# KÖR ETT KOMMANDO SOM ROOT
sudo kommando

# BYT TILL ANNAN ANVÄNDARE
sudo -u postgres psql            # Kör psql som postgres
sudo su - alice                  # Bli alice

# VISA DINA SUDO-RÄTTIGHETER
sudo -l
```

---

## 🚀 Praktiskt: Onboarda ny teammedlem

```bash
#!/bin/bash
# onboard.sh - Skapa ny teammedlem
# Användning: sudo ./onboard.sh alice "Alice Developer" "ssh-ed25519 AAAA..."

set -euo pipefail

USERNAME="$1"
FULLNAME="$2"
SSH_KEY="$3"

echo "🆕 Skapar användare: $USERNAME"

# Skapa användare
sudo useradd -m -s /bin/bash -c "$FULLNAME" "$USERNAME"

# Lägg till i nödvändiga grupper
sudo usermod -aG sudo,docker "$USERNAME"

# Konfigurera SSH
SSH_DIR="/home/$USERNAME/.ssh"
sudo mkdir -p "$SSH_DIR"
echo "$SSH_KEY" | sudo tee "$SSH_DIR/authorized_keys" > /dev/null

# Sätt rätt permissions
sudo chmod 700 "$SSH_DIR"
sudo chmod 600 "$SSH_DIR/authorized_keys"
sudo chown -R "$USERNAME:$USERNAME" "$SSH_DIR"

# Tvinga lösenordsbyte vid första login (valfritt)
# sudo chage -d 0 "$USERNAME"

echo "✅ $USERNAME skapad och klar!"
echo "   - Grupper: $(groups $USERNAME | cut -d: -f2)"
echo "   - SSH-nyckel: installerad"
echo "   - Hemkatalog: /home/$USERNAME"
```

---

## 🔍 Felsökning

```bash
# "Permission denied" - men jag lade till mig i gruppen!
id                               # Visa dina AKTIVA grupper
# → Ser du inte docker? Du har inte loggat in på nytt!
# Lösning: Logga ut och in, eller "newgrp docker"

# Användare kan inte logga in
sudo grep alice /etc/passwd      # Finns användaren?
sudo passwd -S alice             # Status (L = locked?)
sudo grep alice /etc/shadow      # Lösenordshash?

# Vem är i en grupp?
getent group docker

# Vilka grupper finns?
cat /etc/group | cut -d: -f1 | sort

# Vem har sudo?
grep -E '%sudo|%wheel' /etc/sudoers
getent group sudo
```

---

## 📋 Quick Reference Card

```bash
# USER MANAGEMENT CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# SKAPA
sudo useradd -m -s /bin/bash alice       # Skapa med hem + bash
sudo passwd alice                         # Sätt lösenord

# ÄNDRA
sudo usermod -aG docker alice            # ⭐ Lägg till i grupp
sudo usermod -aG sudo alice              # Ge sudo-access
sudo usermod -s /bin/zsh alice           # Byt shell
sudo usermod -L alice                    # Lås kontot

# TA BORT
sudo userdel -r alice                    # Med hemkatalog

# GRUPPER
sudo groupadd developers                 # Skapa grupp
getent group developers                  # Visa medlemmar
sudo gpasswd -d alice developers         # Ta bort från grupp

# INFO
id alice                                 # UID, GID, grupper
groups alice                             # Bara grupper
cat /etc/passwd | grep alice             # Användarinfo

# SUDO
sudo visudo                              # Redigera sudoers
sudo -i                                  # Bli root
sudo -u postgres psql                    # Kör som annan
sudo -l                                  # Visa dina rättigheter

# SSH-SETUP FÖR NY ANVÄNDARE
sudo mkdir -p /home/alice/.ssh
sudo chmod 700 /home/alice/.ssh
echo "ssh-ed25519 AAAA..." | sudo tee /home/alice/.ssh/authorized_keys
sudo chmod 600 /home/alice/.ssh/authorized_keys
sudo chown -R alice:alice /home/alice/.ssh
# ═══════════════════════════════════════════════════════════
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

## ⏰ Varför detta är ESSENTIELLT för DevOps

**Tänk dig en värld utan schemalagda jobb:**
- 🚫 Du måste MANUELLT ta backup varje natt kl 02:00
- 🚫 Du måste MANUELLT rensa gamla loggar varje vecka
- 🚫 Du måste MANUELLT köra certifikatförnyelse varje månad
- 🚫 Du måste MANUELLT starta services efter reboot

**Med cron:**
- ✅ Backup körs automatiskt varje natt
- ✅ Loggar rensas automatiskt
- ✅ Certifikat förnyas automatiskt
- ✅ Allt startar vid reboot

**Cron är DevOps-automationens grundsten.**

---

## 🧠 Förstå crontab-syntax

```
┌───────────── minut (0-59)
│ ┌───────────── timme (0-23)
│ │ ┌───────────── dag i månad (1-31)
│ │ │ ┌───────────── månad (1-12)
│ │ │ │ ┌───────────── veckodag (0-7, där 0 och 7 = söndag)
│ │ │ │ │
* * * * * kommando_att_köra
```

### Visuellt exempel:

```
30 2 * * * /opt/backup.sh

30   = minut 30
2    = timme 02 (02:30 på natten)
*    = alla dagar i månaden
*    = alla månader
*    = alla veckodagar

= "Kör /opt/backup.sh kl 02:30 varje natt"
```

---

## 🏆 TOP 10 – Kommandon och mönster

| # | Kommando/Mönster | Vad det gör |
|---|------------------|-------------|
| 1 | `crontab -e` | ⭐ Redigera dina cron-jobb |
| 2 | `crontab -l` | ⭐ Lista dina cron-jobb |
| 3 | `*/5 * * * *` | Var 5:e minut |
| 4 | `0 * * * *` | Varje hel timme |
| 5 | `0 0 * * *` | Midnatt varje dag |
| 6 | `@reboot` | Vid systemstart |
| 7 | `@daily` | En gång per dag (midnatt) |
| 8 | `>> /var/log/job.log 2>&1` | Logga output |
| 9 | `/etc/cron.d/` | System-cron (som root) |
| 10 | `systemctl status cron` | Kolla att cron körs |

---

## 📅 Vanliga scheman med förklaring

```bash
# VARJE MINUT (för testing – ta bort sen!)
* * * * *                        # Varje minut

# VAR X:E MINUT
*/5 * * * *                      # ⭐ Var 5:e minut
*/15 * * * *                     # Var 15:e minut
*/30 * * * *                     # Varannan halvtimme

# SPECIFIK TID
30 8 * * *                       # 08:30 varje dag
0 9 * * 1-5                      # 09:00 måndag-fredag
0 */2 * * *                      # Varannan timme på heltimme

# DAGLIGEN
0 0 * * *                        # ⭐ Midnatt varje dag
0 2 * * *                        # ⭐ 02:00 varje natt (bra för backup)
0 6 * * *                        # 06:00 varje morgon

# VECKOVIS
0 0 * * 0                        # Midnatt varje söndag
0 0 * * 1                        # Midnatt varje måndag
0 9 * * 5                        # 09:00 varje fredag

# MÅNADSVIS
0 0 1 * *                        # Första dagen i varje månad
0 0 15 * *                       # 15:e varje månad

# ÅRLIGEN
0 0 1 1 *                        # 1 januari, midnatt

# SPECIALORD (lättare att läsa)
@reboot                          # ⭐ Vid systemstart
@hourly                          # Varje hel timme (= 0 * * * *)
@daily                           # Midnatt (= 0 0 * * *)
@weekly                          # Söndagsmidnatt (= 0 0 * * 0)
@monthly                         # Första i månaden (= 0 0 1 * *)
@annually                        # 1 januari (= 0 0 1 1 *)
```

### 🧮 Minnesregel:

```
"Minut Timme Dag Månad Veckodag"
   M     T    D    M      V

Tänk: "Min Tabell Delas Med Vänner"
```

---

## 🛠️ Hantera dina cron-jobb

```bash
# VISA DINA JOBB
crontab -l

# REDIGERA (öppnar i default editor)
crontab -e

# TA BORT ALLA JOBB (⚠️ försiktigt!)
crontab -r

# SE ANNAN ANVÄNDARES CRON (kräver root)
sudo crontab -u www-data -l
sudo crontab -u nginx -e

# KOLLA ATT CRON KÖRS
systemctl status cron            # Ubuntu/Debian
systemctl status crond           # CentOS/RHEL

# SE CRON-LOGGAR
grep CRON /var/log/syslog        # Ubuntu
journalctl -u cron               # Systemd
tail -f /var/log/cron            # CentOS
```

---

## 🚀 Praktiska cron-jobb (kopiera och anpassa!)

### Backup varje natt

```bash
# Cron-entry:
0 2 * * * /opt/scripts/backup.sh >> /var/log/backup.log 2>&1

# backup.sh:
#!/bin/bash
set -e
BACKUP_DIR="/backup"
APP_DIR="/var/www/myapp"
DATE=$(date +%Y%m%d_%H%M%S)

echo "Starting backup at $(date)"
tar -czvf "${BACKUP_DIR}/app_${DATE}.tar.gz" "$APP_DIR"

# Behåll bara de senaste 7 dagarna
find "$BACKUP_DIR" -name "app_*.tar.gz" -mtime +7 -delete
echo "Backup complete at $(date)"
```

### Health check var 5:e minut

```bash
*/5 * * * * /opt/scripts/healthcheck.sh >> /var/log/healthcheck.log 2>&1

# healthcheck.sh:
#!/bin/bash
URL="https://myapp.com/health"
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$RESPONSE" != "200" ]; then
    echo "[$(date)] ALERT: Health check failed! Status: $RESPONSE"
    # Skicka alert
    curl -X POST "https://hooks.slack.com/..." -d '{"text":"App is down!"}'
fi
```

### Rensa gamla filer

```bash
# Rensa temp varje dag kl 03:00
0 3 * * * find /tmp -type f -mtime +7 -delete

# Rensa gamla loggar
0 4 * * * find /var/log -name "*.log.gz" -mtime +30 -delete

# Rensa Docker
0 5 * * 0 docker system prune -af >> /var/log/docker-cleanup.log 2>&1
```

### Starta app vid reboot

```bash
@reboot /opt/myapp/start.sh >> /var/log/myapp-startup.log 2>&1

# Eller med delay (vänta på nätverk etc):
@reboot sleep 30 && /opt/myapp/start.sh
```

### Certifikatförnyelse (Let's Encrypt)

```bash
# Kör två gånger per dag (certbot förnyar bara om det behövs)
0 0,12 * * * certbot renew --quiet && systemctl reload nginx
```

---

## ⚠️ Vanliga misstag och lösningar

### 1. Glömd output-redirect

```bash
# ❌ DÅLIGT: Output försvinner, inga loggar vid fel
0 2 * * * /opt/backup.sh

# ✅ BRA: Logga stdout OCH stderr
0 2 * * * /opt/backup.sh >> /var/log/backup.log 2>&1
```

### 2. Relativa sökvägar

```bash
# ❌ DÅLIGT: Cron har inte samma PATH som din terminal
0 2 * * * backup.sh
0 2 * * * ./scripts/backup.sh

# ✅ BRA: Använd alltid absoluta sökvägar
0 2 * * * /opt/scripts/backup.sh
```

### 3. Glömd shebang i scriptet

```bash
# ❌ DÅLIGT: Script utan shebang kan faila i cron
echo "hello"

# ✅ BRA: Alltid shebang först
#!/bin/bash
echo "hello"
```

### 4. Environment-variabler saknas

```bash
# Cron har minimal miljö! Sätt variabler explicit:
PATH=/usr/local/bin:/usr/bin:/bin
NODE_ENV=production

0 2 * * * /opt/scripts/app-job.sh

# Eller ladda din profil i scriptet:
#!/bin/bash
source /home/deploy/.bashrc
/opt/myapp/job.sh
```

### 5. Permissions på scriptet

```bash
# ❌ Script utan execute-permission körs inte
# ✅ Fixa:
chmod +x /opt/scripts/backup.sh
```

---

## 📁 System-cron (/etc/cron.d/)

För system-jobb (istället för användar-crontab):

```bash
# /etc/cron.d/myapp-backup

# Format: MIN TIM DAG MÅN VEC ANVÄNDARE KOMMANDO
0 2 * * * root /opt/scripts/backup.sh >> /var/log/backup.log 2>&1
*/5 * * * * www-data /opt/myapp/healthcheck.sh
```

**Skillnader mot crontab:**
- Filer i `/etc/cron.d/` istället för `crontab -e`
- Måste ange ANVÄNDARE som ska köra jobbet
- Bra för deployment/automation (kan versionshanteras)

---

## 🔍 Felsökning

```bash
# JOBBET KÖRDES ALDRIG?
# 1. Kolla att cron körs
systemctl status cron

# 2. Kolla loggar
grep CRON /var/log/syslog | tail -20
# Eller
journalctl -u cron --since "1 hour ago"

# 3. Kolla syntax
crontab -l                       # Ser det rätt ut?

# 4. Testa scriptet manuellt som rätt användare
sudo -u www-data /opt/scripts/backup.sh
# Funkar det? Om inte, fixa scriptet först!

# 5. Kolla att output-fil är skrivbar
ls -la /var/log/backup.log
touch /var/log/backup.log        # Kan du skapa den?

# JOBBET KÖRDES MEN FAILADE?
# Kolla din loggfil!
cat /var/log/backup.log
# Ingen loggfil? Du glömde redirecta output!
```

---

## 📋 Quick Reference Card

```bash
# CRON CHEAT SHEET
# ═══════════════════════════════════════════════════════════
# HANTERA CRON
crontab -l                       # Lista jobb
crontab -e                       # Redigera jobb
crontab -r                       # Ta bort alla

# SYNTAX
# MIN TIM DAG MÅN VEC kommando
# *   *   *   *   *

# VANLIGA MÖNSTER
*/5 * * * *                      # Var 5:e minut
0 * * * *                        # Varje timme
0 0 * * *                        # Midnatt varje dag
0 2 * * *                        # 02:00 varje natt
0 0 * * 0                        # Varje söndag
0 0 1 * *                        # Första i månaden

# SPECIALORD
@reboot                          # Vid uppstart
@daily                           # Dagligen
@weekly                          # Veckovis
@monthly                         # Månadsvis

# ALLTID LOGGA OUTPUT!
0 2 * * * /script.sh >> /var/log/job.log 2>&1

# SYSTEM-CRON (/etc/cron.d/filnamn)
# MIN TIM DAG MÅN VEC USER kommando
0 2 * * * root /script.sh >> /var/log/job.log 2>&1

# FELSÖK
systemctl status cron            # Körs cron?
grep CRON /var/log/syslog        # Loggar
sudo -u USER /script.sh          # Testa manuellt
# ═══════════════════════════════════════════════════════════
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
