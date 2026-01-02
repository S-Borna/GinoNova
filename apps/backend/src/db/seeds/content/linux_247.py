"""
Linux 24/7 - Komplett Linux för DevOps
20 noder från grunden till avancerad systemadministration
"""

MODULE = {
    "id": "linux-247",
    "slug": "linux-247",
    "title": "Linux 24/7",
    "description": "Komplett Linux för DevOps - från grunden till produktion",
    "icon": "terminal",
    "category": "devops",
    "difficulty": "beginner",
    "estimated_hours": 40,
    "tasks": [
        # ======================================================================
        # NODE 1: File System Essentials
        # ======================================================================
        {
            "title": "File System Essentials",
            "slug": "file-system-essentials",
            "description": "Navigera, kopiera, flytta och hantera filer i Linux.",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# 📁 File System Essentials

> **TL;DR:** Navigera med `cd`, lista med `ls -lah`, kopiera med `cp -r`, ta bort med `rm -rf`, hitta med `find`.

---

## 🎯 Varför viktigt för DevOps?

Som DevOps-ingenjör arbetar du konstant med filer:
- Konfigurationsfiler i `/etc`
- Loggar i `/var/log`
- Scripts i `/opt` eller `/home`
- Applikationer i `/var/www`

Dessa kommandon använder du **flera gånger per dag**.

---

## 🧭 Navigation

### cd – Byt katalog
```bash
cd /var/log          # Gå till specifik katalog
cd ..                # Gå upp en nivå
cd ~                 # Gå till hemkatalogen
cd -                 # ⭐ Tillbaka till förra katalogen
cd                   # Samma som cd ~
```

### pwd – Var är jag?
```bash
pwd
# /home/user/projects
```

### ls – Lista filer
```bash
ls                   # Enkel lista
ls -l                # Lång lista med detaljer
ls -la               # Alla filer inkl. dolda
ls -lh               # Human-readable storlekar
ls -lht              # Sorterat efter tid (nyaste först)
ls -lah              # ⭐ FAVORITEN: allt kombinerat
```

---

## 📂 Filoperationer

### cp – Kopiera
```bash
cp fil.txt kopia.txt           # Kopiera fil
cp -r katalog/ backup/         # ⭐ Rekursivt (kataloger)
cp -p fil.txt kopia.txt        # Bevara permissions + timestamp
```

**DevOps-mönster – Backup innan ändring:**
```bash
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak.$(date +%Y%m%d)
```

### mv – Flytta/Byt namn
```bash
mv fil.txt nytt_namn.txt       # Byt namn
mv fil.txt /tmp/               # Flytta
mv katalog1/ katalog2/         # Byt namn på katalog
```

### rm – Ta bort ⚠️
```bash
rm fil.txt                     # Ta bort fil
rm -r katalog/                 # Ta bort katalog
rm -rf katalog/                # ⚠️ Force – DUBBELKOLLA ALLTID!
rm -i fil.txt                  # Interaktiv (frågar först)
```

### mkdir – Skapa katalog
```bash
mkdir projekt                  # Skapa katalog
mkdir -p path/to/katalog       # ⭐ Skapa hela kedjan
```

---

## 🔐 Permissions

### chmod – Ändra rättigheter
```bash
chmod 755 script.sh            # rwxr-xr-x (scripts)
chmod 644 config.txt           # rw-r--r-- (filer)
chmod 600 privat.key           # rw------- (SSH-nycklar)
chmod +x script.sh             # ⭐ Gör körbart
```

**Siffror:** r=4, w=2, x=1

### chown – Ändra ägare
```bash
chown user:group fil.txt
chown -R www-data:www-data /var/www/   # Rekursivt
```

---

## 🔍 Hitta filer

### find – Sök
```bash
find /var/log -name "*.log"           # Hitta .log-filer
find . -type f -size +100M            # Filer > 100MB
find /tmp -mtime -7                   # Ändrade senaste 7 dagarna
find /etc -name "*.conf"              # Konfigurationsfiler
```

### which – Var finns kommandot?
```bash
which nginx          # /usr/sbin/nginx
which python3        # /usr/bin/python3
```

---

## 💾 Diskutrymme

### df – Ledigt utrymme
```bash
df -h                # ⭐ Human-readable
df -hT               # Med filsystemtyp
```

### du – Katalogstorlek
```bash
du -sh katalog/                # Total storlek
du -h --max-depth=1 /var       # ⭐ Storlek per mapp
du -h --max-depth=1 /var | sort -h   # Sorterat
```

---

## 📖 Läsa filer

```bash
cat fil.txt                    # Visa allt
head -n 20 fil.txt             # Första 20 raderna
tail -n 20 fil.txt             # Sista 20 raderna
tail -f /var/log/nginx/error.log   # ⭐ Följ live!
less fil.txt                   # Bläddra (q = avsluta)
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Var är jag? | `pwd` |
| Gå hem | `cd ~` |
| Gå tillbaka | `cd -` |
| Lista allt | `ls -lah` |
| Backup config | `cp fil.conf fil.conf.bak` |
| Kopiera mapp | `cp -r katalog/ backup/` |
| Skapa struktur | `mkdir -p projekt/{src,docs,tests}` |
| Gör körbart | `chmod +x script.sh` |
| Hitta stora filer | `find / -size +100M 2>/dev/null` |
| Kolla disk | `df -h` |
| Storlek per mapp | `du -h --max-depth=1` |
| Följ logg live | `tail -f /var/log/syslog` |

---

## 🧠 Kom ihåg

- `cd -` = hoppa mellan två kataloger
- `ls -lah` = din standardvy
- `cp -r` = rekursivt för kataloger
- `rm -rf` = ⚠️ **dubbelkolla innan Enter!**
- `chmod 755` = script/katalog, `644` = vanlig fil
- `tail -f` = följ loggar i realtid

---

## ✅ Checkpoint (Tenta)

1. Hur går du tillbaka till förra katalogen?
2. Vilket kommando listar alla filer med storlek?
3. Hur kopierar du en hel katalog?
4. Vad betyder chmod 755?
5. Hur hittar du filer större än 100MB?
6. Hur följer du en loggfil i realtid?
""",
            "quiz": [
                {
                    "question": "Hur går du tillbaka till förra katalogen?",
                    "options": ["cd ..", "cd ~", "cd -", "cd /"],
                    "correct": 2,
                },
                {
                    "question": "Vilket kommando listar alla filer inklusive dolda med storlek?",
                    "options": ["ls -l", "ls -a", "ls -lah", "ls -R"],
                    "correct": 2,
                },
                {
                    "question": "Hur kopierar du en hel katalog rekursivt?",
                    "options": [
                        "cp katalog/ backup/",
                        "cp -r katalog/ backup/",
                        "mv katalog/ backup/",
                        "copy -r katalog/ backup/",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad betyder chmod 755?",
                    "options": [
                        "Bara ägare kan läsa",
                        "rwxr-xr-x (ägare: allt, andra: läsa/köra)",
                        "Alla kan skriva",
                        "Filen är dold",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur hittar du filer större än 100MB?",
                    "options": [
                        "ls -size 100M",
                        "find / -size +100M",
                        "du -h 100M",
                        "grep 100M",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur följer du en loggfil i realtid?",
                    "options": [
                        "cat -f logfil",
                        "tail -f logfil",
                        "head -f logfil",
                        "less -f logfil",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 2: Text Processing & Search
        # ======================================================================
        {
            "title": "Text Processing & Search",
            "slug": "text-processing-search",
            "description": "Sök, filtrera och manipulera text med grep, awk, sed.",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# 🔍 Text Processing & Search

> **TL;DR:** Sök med `grep`, extrahera kolumner med `awk`, ersätt med `sed`, räkna med `wc`.

---

## 🎯 Varför viktigt för DevOps?

Loggar, konfigurationsfiler, output – **allt är text**. Din förmåga att snabbt söka, filtrera och manipulera text avgör hur effektiv du är.

---

## 🧭 grep – Sök i text

### Grundläggande
```bash
grep "error" logfile.log        # Sök efter "error"
grep -i "error" logfile.log     # ⭐ Case-insensitive
grep -v "success" logfile.log   # Invertera (INTE matchar)
grep -n "error" logfile.log     # Visa radnummer
grep -c "error" logfile.log     # Räkna träffar
```

### Rekursiv sökning
```bash
grep -r "error" /var/log/       # ⭐ Sök i alla filer
grep -r "TODO" ./src/           # Hitta TODOs i kod
```

### Kontext
```bash
grep -A 5 "error" logfile.log   # 5 rader EFTER träff
grep -B 5 "error" logfile.log   # 5 rader FÖRE träff
grep -C 5 "error" logfile.log   # 5 rader FÖRE och EFTER
```

### Med pipes
```bash
ps aux | grep nginx             # Hitta nginx-processer
cat log.txt | grep -i error     # Filtrera errors
tail -f log.txt | grep error    # ⭐ Följ och filtrera live
```

---

## 🧭 awk – Kolumnbearbetning

```bash
awk '{print $1}' fil.txt        # Första kolumnen
awk '{print $NF}' fil.txt       # Sista kolumnen
awk '{print $1, $3}' fil.txt    # Kolumn 1 och 3
```

### Med separator
```bash
awk -F',' '{print $1}' fil.csv        # CSV (komma)
awk -F':' '{print $1}' /etc/passwd    # Kolon
```

### Praktiskt exempel
```bash
# Top 10 IP-adresser i access log
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
```

---

## 🧭 sed – Sök och ersätt

```bash
sed 's/gammal/ny/' fil.txt            # Ersätt första per rad
sed 's/gammal/ny/g' fil.txt           # ⭐ Ersätt ALLA
sed -i 's/gammal/ny/g' fil.txt        # ⭐ Ändra filen direkt
sed -i.bak 's/gammal/ny/g' fil.txt    # Med backup
```

### Ta bort rader
```bash
sed '/^#/d' fil.txt             # Ta bort kommentarer
sed '/^$/d' fil.txt             # Ta bort tomma rader
```

---

## 🧭 sort & uniq – Sortera och räkna

```bash
sort fil.txt                    # Alfabetisk
sort -n fil.txt                 # Numerisk
sort -r fil.txt                 # Omvänd
sort -u fil.txt                 # Unika (ta bort dubbletter)
```

```bash
sort fil.txt | uniq             # Ta bort dubbletter
sort fil.txt | uniq -c          # ⭐ Räkna förekomster
sort fil.txt | uniq -c | sort -rn   # Sorterat efter antal
```

---

## 🧭 Pipes & Redirection

### Pipes
```bash
command1 | command2             # Output → Input
ps aux | grep nginx | wc -l     # Kedja: processer → filtrera → räkna
```

### Redirection
```bash
command > fil.txt               # Skriv till fil (ÖVERSKRIVER)
command >> fil.txt              # Lägg till (APPEND)
command 2> error.log            # Bara errors
command > out.log 2>&1          # ⭐ Allt till samma fil
command 2>/dev/null             # Ignorera errors
```

### tee – Visa OCH spara
```bash
command | tee fil.txt           # ⭐ Visa + spara
command | tee -a fil.txt        # Visa + append
```

---

## 🧭 wc – Räkna

```bash
wc -l fil.txt                   # Antal rader
wc -w fil.txt                   # Antal ord
wc -c fil.txt                   # Antal bytes
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Sök efter error | `grep -i error logfile.log` |
| Sök rekursivt | `grep -r "pattern" /path/` |
| Visa kontext | `grep -C 5 "error" logfile.log` |
| Följ + filtrera | `tail -f log.txt \\| grep error` |
| Första kolumnen | `awk '{print $1}' fil.txt` |
| Ersätt i fil | `sed -i 's/old/new/g' fil.txt` |
| Räkna rader | `wc -l fil.txt` |
| Top 10 vanligaste | `sort \\| uniq -c \\| sort -rn \\| head` |
| Spara + visa | `command \\| tee output.txt` |

---

## 🧠 Kom ihåg

- `grep -i` = case-insensitive
- `grep -r` = rekursiv sökning
- `grep -C 5` = kontext (5 rader före/efter)
- `awk '{print $1}'` = första kolumnen
- `sed -i 's/old/new/g'` = ersätt i fil
- `sort | uniq -c` = räkna unika
- `>` överskriver, `>>` lägger till

---

## ✅ Checkpoint (Tenta)

1. Hur söker du case-insensitive?
2. Hur söker du rekursivt i alla filer?
3. Hur visar du 5 rader före och efter en träff?
4. Hur extraherar du första kolumnen?
5. Hur ersätter du text direkt i en fil?
6. Hur räknar du unika förekomster?
""",
            "quiz": [
                {
                    "question": "Hur söker du case-insensitive med grep?",
                    "options": ["grep -c", "grep -i", "grep -v", "grep -n"],
                    "correct": 1,
                },
                {
                    "question": "Hur söker du rekursivt i alla filer?",
                    "options": ["grep -a", "grep -R", "grep -r", "grep -f"],
                    "correct": 2,
                },
                {
                    "question": "Hur visar du 5 rader före och efter en träff?",
                    "options": ["grep -A 5", "grep -B 5", "grep -C 5", "grep -5"],
                    "correct": 2,
                },
                {
                    "question": "Hur extraherar du första kolumnen med awk?",
                    "options": [
                        "awk '{print $0}'",
                        "awk '{print $1}'",
                        "awk '{print $NF}'",
                        "awk '{print 1}'",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ersätter du text direkt i en fil med sed?",
                    "options": [
                        "sed 's/old/new/'",
                        "sed -i 's/old/new/g'",
                        "sed -r 's/old/new/'",
                        "sed -e 's/old/new/'",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur räknar du unika förekomster?",
                    "options": ["uniq -c", "sort | uniq -c", "count -u", "wc -u"],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 3: Process Management
        # ======================================================================
        {
            "title": "Process Management",
            "slug": "process-management",
            "description": "Visa, övervaka och hantera processer i Linux.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# ⚙️ Process Management

> **TL;DR:** Visa processer med `ps aux`, döda med `kill`, övervaka med `top/htop`.

---

## 🎯 Varför viktigt för DevOps?

Processer är hjärtat i varje Linux-system. Du måste kunna:
- Se vad som körs
- Identifiera resurstjuvar (CPU/RAM)
- Starta och stoppa tjänster
- Hantera hängande processer

---

## 🧭 Visa processer

### ps – Process Status
```bash
ps                              # Dina processer
ps aux                          # ⭐ ALLA processer
ps aux | grep nginx             # Hitta specifik process
```

### Sortera efter resurs
```bash
ps aux --sort=-%cpu | head -10  # ⭐ Top 10 CPU
ps aux --sort=-%mem | head -10  # ⭐ Top 10 RAM
```

### top / htop – Realtid
```bash
top                             # Realtidsövervakning
htop                            # ⭐ Snyggare (installera separat)
```

**I top:** tryck `q` för att avsluta, `k` för att döda process.

---

## 🧭 Döda processer

### kill – Med PID
```bash
kill 1234                       # ⭐ SIGTERM (snäll avslutning)
kill -9 1234                    # ⭐ SIGKILL (tvinga)
kill -HUP 1234                  # Reload config
```

### Signaler
| Signal | Nummer | Betydelse |
|--------|--------|-----------|
| SIGTERM | 15 | Snäll avslutning (default) |
| SIGKILL | 9 | Tvinga avslut (går ej ignorera) |
| SIGHUP | 1 | Reload config |

### killall / pkill – Med namn
```bash
killall nginx                   # Döda alla nginx
pkill nginx                     # Döda processer med "nginx"
pkill -9 nginx                  # Force kill
```

---

## 🧭 Hitta processer

### pgrep – Hitta PID
```bash
pgrep nginx                     # Bara PID
pgrep -l nginx                  # PID + namn
pgrep -a nginx                  # PID + hela kommandot
```

### I scripts
```bash
if pgrep nginx > /dev/null; then
    echo "Nginx körs"
else
    echo "Nginx körs INTE"
fi
```

---

## 🧭 Bakgrundsjobb

### Starta i bakgrund
```bash
./script.sh &                   # Starta i bakgrund
nohup ./script.sh &             # ⭐ Överlever logout
nohup ./script.sh > log.txt 2>&1 &   # Med loggfil
```

### Hantera jobb
```bash
jobs                            # Lista bakgrundsjobb
fg                              # Ta till förgrund
bg                              # Kör i bakgrund
```

### Workflow
```bash
./long-task.sh                  # Starta
# CTRL+Z                        # Pausa
bg                              # Fortsätt i bakgrund
disown                          # Släpp från terminal
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Visa alla processer | `ps aux` |
| Hitta specifik process | `ps aux \\| grep nginx` |
| Top 10 CPU | `ps aux --sort=-%cpu \\| head -10` |
| Top 10 RAM | `ps aux --sort=-%mem \\| head -10` |
| Realtidsövervakning | `htop` eller `top` |
| Döda process (snällt) | `kill PID` |
| Döda process (tvinga) | `kill -9 PID` |
| Döda alla nginx | `pkill nginx` |
| Hitta PID | `pgrep -a nginx` |
| Kör i bakgrund | `nohup ./script.sh &` |

---

## 🧠 Kom ihåg

- `ps aux` = visa alla processer
- `ps aux --sort=-%cpu` = sortera efter CPU
- `kill PID` = snäll avslutning (SIGTERM)
- `kill -9 PID` = tvinga avslut (SIGKILL)
- `pkill namn` = döda efter namn
- `nohup cmd &` = överlever logout
- `htop` = bästa realtidsverktyget

---

## ✅ Checkpoint (Tenta)

1. Hur visar du alla processer på systemet?
2. Hur hittar du top 10 CPU-användare?
3. Vad är skillnaden mellan kill och kill -9?
4. Hur dödar du alla processer med namnet nginx?
5. Hur startar du ett script som överlever logout?
6. Hur hittar du PID för en process?
""",
            "quiz": [
                {
                    "question": "Hur visar du alla processer på systemet?",
                    "options": ["ps", "ps -a", "ps aux", "ps -all"],
                    "correct": 2,
                },
                {
                    "question": "Hur hittar du top 10 CPU-användare?",
                    "options": [
                        "ps aux | head",
                        "ps aux --sort=-%cpu | head -10",
                        "top -10",
                        "cpu top 10",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad är skillnaden mellan kill och kill -9?",
                    "options": [
                        "Ingen skillnad",
                        "kill är snällare, kill -9 tvingar avslut",
                        "kill -9 är snällare",
                        "kill fungerar bara på root",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur dödar du alla processer med namnet nginx?",
                    "options": ["kill nginx", "pkill nginx", "stop nginx", "end nginx"],
                    "correct": 1,
                },
                {
                    "question": "Hur startar du ett script som överlever logout?",
                    "options": [
                        "./script.sh",
                        "./script.sh &",
                        "nohup ./script.sh &",
                        "bg ./script.sh",
                    ],
                    "correct": 2,
                },
                {
                    "question": "Hur hittar du PID för en process?",
                    "options": [
                        "pid nginx",
                        "pgrep nginx",
                        "findpid nginx",
                        "ps pid nginx",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 4: System Information & Monitoring
        # ======================================================================
        {
            "title": "System Information & Monitoring",
            "slug": "system-information-monitoring",
            "description": "Övervaka systemresurser, CPU, minne och disk.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# 📊 System Information & Monitoring

> **TL;DR:** Kolla load med `uptime`, minne med `free -h`, disk med `df -h`, realtid med `htop`.

---

## 🎯 Varför viktigt för DevOps?

Du måste snabbt kunna svara på:
- Hur belastad är servern?
- Hur mycket minne finns kvar?
- Är disken full?
- Vad är det för system?

---

## 🧭 Systeminformation

### uname – Systeminfo
```bash
uname -a                        # ⭐ All info
uname -r                        # Bara kernel-version
```

### Operativsystem
```bash
cat /etc/os-release             # ⭐ OS-version
hostnamectl                     # Hostname + OS
```

### Hostname & IP
```bash
hostname                        # Servernamn
hostname -I                     # ⭐ IP-adresser
```

---

## 🧭 Load & Uptime

### uptime
```bash
uptime
# 10:30:00 up 45 days, load average: 0.15, 0.20, 0.18
#                                    └── 1min, 5min, 15min
```

**Tumregel:** Load < antal CPU-kärnor = OK

### w – Vem är inloggad?
```bash
w                               # Inloggade + vad de gör
who                             # Bara inloggade
```

---

## 🧭 CPU

### lscpu
```bash
lscpu                           # ⭐ All CPU-info
nproc                           # Antal kärnor
```

---

## 🧭 Minne (RAM)

### free
```bash
free                            # I bytes
free -h                         # ⭐ Human-readable
free -m                         # I MB
```

**Output:**
```
              total        used        free      available
Mem:           16Gi       12Gi       2.0Gi        3.5Gi
```

⚠️ Kolla `available`, inte `free`!

### vmstat
```bash
vmstat 1                        # Uppdatera varje sekund
```

---

## 🧭 Disk

### df – Ledigt utrymme
```bash
df -h                           # ⭐ Human-readable
df -hT                          # Med filsystemtyp
df -h /                         # Bara root
```

### Inodes
```bash
df -i                           # Inodes (kan ta slut!)
```

---

## 🧭 Disk I/O

### iostat
```bash
iostat                          # Översikt
iostat -x 1                     # ⭐ Extended, varje sekund
```

### iotop
```bash
iotop                           # ⭐ Vilka processer gör I/O
```

---

## 🧭 Kernel-meddelanden

### dmesg
```bash
dmesg                           # Alla meddelanden
dmesg | tail -50                # Senaste 50
dmesg | grep -i error           # ⭐ Bara fel
dmesg -T                        # Med läsbar tid
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Vilken OS? | `cat /etc/os-release` |
| Kernel-version | `uname -r` |
| IP-adress | `hostname -I` |
| Load/uptime | `uptime` |
| Antal CPU-kärnor | `nproc` |
| Minne | `free -h` |
| Disk | `df -h` |
| Disk I/O | `iostat -x 1` |
| Kernel-fel | `dmesg \\| grep -i error` |
| Realtid | `htop` |

---

## 🧠 Kom ihåg

- `uptime` = load average (ska vara < antal kärnor)
- `free -h` = kolla `available`, inte `free`
- `df -h` = diskutrymme (varning vid >85%)
- `df -i` = inodes (kan ta slut!)
- `dmesg | grep -i error` = kernel-fel
- `htop` = bästa realtidsverktyget

---

## ✅ Checkpoint (Tenta)

1. Hur kollar du vilken OS-version som körs?
2. Hur ser du load average?
3. Vad ska load average vara under?
4. Hur kollar du ledigt minne?
5. Hur ser du ledigt diskutrymme?
6. Hur hittar du kernel-felmeddelanden?
""",
            "quiz": [
                {
                    "question": "Hur kollar du vilken OS-version som körs?",
                    "options": [
                        "uname -a",
                        "cat /etc/os-release",
                        "os --version",
                        "version",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du load average?",
                    "options": ["load", "uptime", "cpu", "top -l"],
                    "correct": 1,
                },
                {
                    "question": "Vad ska load average vara under?",
                    "options": ["100", "10", "Antal CPU-kärnor", "1.0"],
                    "correct": 2,
                },
                {
                    "question": "Hur kollar du ledigt minne human-readable?",
                    "options": ["mem", "free -h", "memory", "ram -h"],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du ledigt diskutrymme?",
                    "options": ["disk", "df -h", "du -h", "space"],
                    "correct": 1,
                },
                {
                    "question": "Hur hittar du kernel-felmeddelanden?",
                    "options": [
                        "kernel -e",
                        "dmesg | grep -i error",
                        "errors",
                        "log kernel",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 5: Log Management
        # ======================================================================
        {
            "title": "Log Management",
            "slug": "log-management",
            "description": "Läs, följ och analysera systemloggar.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 📋 Log Management

> **TL;DR:** Följ loggar med `tail -f`, systemd-loggar med `journalctl`, sök med `grep`.

---

## 🎯 Varför viktigt för DevOps?

Loggar är din bästa vän vid felsökning:
- Varför kraschade appen?
- Vem loggade in?
- Vad hände kl 03:00?

---

## 🧭 Viktiga loggplatser

| Logg | Plats |
|------|-------|
| System (Ubuntu) | `/var/log/syslog` |
| System (RHEL) | `/var/log/messages` |
| Auth/Login | `/var/log/auth.log` |
| Kernel | `dmesg` eller `/var/log/kern.log` |
| Nginx | `/var/log/nginx/` |
| Apache | `/var/log/apache2/` |

---

## 🧭 Följa loggar i realtid

### tail -f
```bash
tail -f /var/log/syslog         # ⭐ Följ live
tail -f /var/log/nginx/error.log
tail -F /var/log/app.log        # ⭐ Följer även vid rotation
```

### Med filter
```bash
tail -f /var/log/syslog | grep -i error    # ⭐ Bara errors
tail -f /var/log/nginx/access.log | grep 404
```

---

## 🧭 journalctl (systemd)

### Grundläggande
```bash
journalctl                      # Alla loggar
journalctl -f                   # ⭐ Följ live
journalctl -n 100               # Senaste 100 rader
```

### Specifik service
```bash
journalctl -u nginx             # ⭐ Bara nginx
journalctl -u nginx -f          # Följ nginx live
journalctl -u nginx --since "1 hour ago"
```

### Filtrera
```bash
journalctl -p err               # ⭐ Bara errors
journalctl -p warning           # Warnings och uppåt
journalctl --since "2024-01-15"
journalctl --since "09:00" --until "10:00"
```

### Boot
```bash
journalctl -b                   # Denna boot
journalctl -b -1                # Förra boot
```

---

## 🧭 Läsa loggar

```bash
cat /var/log/syslog             # Hela filen
less /var/log/syslog            # Bläddra (q = quit)
head -n 50 /var/log/syslog      # Första 50 rader
tail -n 50 /var/log/syslog      # Sista 50 rader
```

---

## 🧭 Söka i loggar

```bash
grep "error" /var/log/syslog           # Sök error
grep -i "error" /var/log/syslog        # ⭐ Case-insensitive
grep -r "error" /var/log/              # Rekursivt
grep -C 5 "error" /var/log/syslog      # Med kontext
```

---

## 🧭 Komprimerade loggar

```bash
zcat /var/log/syslog.2.gz              # Visa
zgrep "error" /var/log/syslog.*.gz     # ⭐ Sök i komprimerade
zless /var/log/syslog.2.gz             # Bläddra
```

---

## 🧭 Logrotate

Loggar roteras automatiskt för att spara plats:
```
/var/log/syslog
/var/log/syslog.1
/var/log/syslog.2.gz
/var/log/syslog.3.gz
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Följ syslog live | `tail -f /var/log/syslog` |
| Följ + filtrera | `tail -f /var/log/syslog \\| grep error` |
| Service-loggar | `journalctl -u nginx` |
| Följ service live | `journalctl -u nginx -f` |
| Bara errors | `journalctl -p err` |
| Senaste timmen | `journalctl --since "1 hour ago"` |
| Sök i loggar | `grep -i "error" /var/log/syslog` |
| Sök komprimerade | `zgrep "error" /var/log/*.gz` |

---

## 🧠 Kom ihåg

- `tail -f` = följ logg live
- `tail -F` = följer även vid rotation
- `journalctl -u service` = specifik service
- `journalctl -f` = följ systemd live
- `journalctl -p err` = bara errors
- `zgrep` = sök i komprimerade loggar

---

## ✅ Checkpoint (Tenta)

1. Hur följer du en loggfil i realtid?
2. Hur ser du loggar för en specifik service?
3. Hur visar du bara error-meddelanden?
4. Hur söker du i komprimerade loggfiler?
5. Var finns autentiseringsloggar i Ubuntu?
6. Hur följer du en logg som roteras?
""",
            "quiz": [
                {
                    "question": "Hur följer du en loggfil i realtid?",
                    "options": [
                        "cat -f logfil",
                        "tail -f logfil",
                        "follow logfil",
                        "watch logfil",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du loggar för en specifik service med journalctl?",
                    "options": [
                        "journalctl service",
                        "journalctl -u nginx",
                        "journalctl --service nginx",
                        "journalctl nginx",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur visar du bara error-meddelanden med journalctl?",
                    "options": [
                        "journalctl -e",
                        "journalctl -p err",
                        "journalctl --error",
                        "journalctl errors",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur söker du i komprimerade loggfiler?",
                    "options": [
                        "grep file.gz",
                        "zgrep pattern file.gz",
                        "search file.gz",
                        "cat file.gz | grep",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Var finns autentiseringsloggar i Ubuntu?",
                    "options": [
                        "/var/log/syslog",
                        "/var/log/auth.log",
                        "/var/log/login.log",
                        "/var/log/users.log",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur följer du en logg som roteras?",
                    "options": ["tail -f", "tail -F", "tail -r", "tail --rotate"],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 6: SSH & Remote Access
        # ======================================================================
        {
            "title": "SSH & Remote Access",
            "slug": "ssh-remote-access",
            "description": "Säker fjärranslutning och filöverföring.",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# 🔐 SSH & Remote Access

> **TL;DR:** Anslut med `ssh user@host`, kopiera filer med `scp`, synka med `rsync`.

---

## 🎯 Varför viktigt för DevOps?

SSH är din portal till servrar:
- Fjärradministration
- Säker filöverföring
- Automatisering och scripts
- Tunnlar och port forwarding

---

## 🧭 Ansluta

### Grundläggande
```bash
ssh user@192.168.1.100          # Med IP
ssh user@server.example.com     # Med hostname
ssh -p 2222 user@server         # Annan port
```

### Kör kommando direkt
```bash
ssh user@server 'uptime'                    # ⭐ Kör och avsluta
ssh user@server 'df -h && free -h'          # Flera kommandon
```

---

## 🧭 SSH-nycklar (lösenordsfritt)

### Skapa nyckel
```bash
ssh-keygen -t ed25519 -C "din@email.com"    # ⭐ Rekommenderad
ssh-keygen -t rsa -b 4096                   # RSA alternativ
```

### Kopiera till server
```bash
ssh-copy-id user@server         # ⭐ Enklaste sättet
```

### Manuellt
```bash
cat ~/.ssh/id_ed25519.pub | ssh user@server 'cat >> ~/.ssh/authorized_keys'
```

---

## 🧭 SSH Config (~/.ssh/config)

Skapa genvägar:
```bash
# ~/.ssh/config
Host prod
    HostName 192.168.1.100
    User deploy
    Port 22

Host staging
    HostName staging.example.com
    User admin
    IdentityFile ~/.ssh/staging_key
```

Nu kan du köra:
```bash
ssh prod                        # Istället för ssh deploy@192.168.1.100
ssh staging
```

---

## 🧭 Kopiera filer

### scp – Secure Copy
```bash
scp fil.txt user@server:/path/             # Lokal → Remote
scp user@server:/path/fil.txt ./           # Remote → Lokal
scp -r katalog/ user@server:/path/         # ⭐ Rekursivt
```

### rsync – Synkronisera (bättre!)
```bash
rsync -avz katalog/ user@server:/backup/   # ⭐ Synka
rsync -avz --delete src/ user@server:/dst/ # Synka + ta bort borttagna
rsync -avzP large_file user@server:/path/  # Med progress
```

**rsync-flaggor:**
- `-a` = archive (bevarar allt)
- `-v` = verbose
- `-z` = komprimera
- `-P` = progress + partial

---

## 🧭 SSH Tunnlar

### Local Port Forwarding
```bash
ssh -L 3306:localhost:3306 user@server
# Koppla lokal port 3306 → serverns MySQL
```

### Jump Host (Bastion)
```bash
ssh -J bastion user@internal    # Via jump host
```

---

## 🧭 SSH-nycklar permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519     # Privat nyckel
chmod 644 ~/.ssh/id_ed25519.pub # Publik nyckel
chmod 600 ~/.ssh/authorized_keys
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Anslut | `ssh user@server` |
| Annan port | `ssh -p 2222 user@server` |
| Kör kommando | `ssh user@server 'uptime'` |
| Skapa nyckel | `ssh-keygen -t ed25519` |
| Kopiera nyckel | `ssh-copy-id user@server` |
| Kopiera fil → server | `scp fil.txt user@server:/path/` |
| Kopiera mapp | `scp -r katalog/ user@server:/path/` |
| Synka | `rsync -avz src/ user@server:/dst/` |
| Tunnel | `ssh -L 3306:localhost:3306 user@server` |

---

## 🧠 Kom ihåg

- `ssh-keygen -t ed25519` = skapa nyckel
- `ssh-copy-id` = kopiera nyckel till server
- `~/.ssh/config` = genvägar
- `scp -r` = kopiera kataloger
- `rsync -avz` = synka (bättre än scp)
- Privat nyckel = `chmod 600`

---

## ✅ Checkpoint (Tenta)

1. Hur ansluter du till en server på port 2222?
2. Hur skapar du en SSH-nyckel?
3. Hur kopierar du din nyckel till servern?
4. Hur kopierar du en katalog till servern?
5. Vilken är bättre för synkronisering, scp eller rsync?
6. Vilken permission ska privata nycklar ha?
""",
            "quiz": [
                {
                    "question": "Hur ansluter du till en server på port 2222?",
                    "options": [
                        "ssh user@server:2222",
                        "ssh -p 2222 user@server",
                        "ssh user@server --port 2222",
                        "ssh 2222 user@server",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur skapar du en SSH-nyckel (rekommenderat)?",
                    "options": [
                        "ssh-key create",
                        "ssh-keygen -t ed25519",
                        "ssh --generate-key",
                        "create-ssh-key",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kopierar du din publika nyckel till servern?",
                    "options": [
                        "scp ~/.ssh/id_ed25519.pub server:",
                        "ssh-copy-id user@server",
                        "ssh --copy-key server",
                        "copy-key user@server",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kopierar du en katalog till servern med scp?",
                    "options": [
                        "scp katalog/ server:",
                        "scp -r katalog/ user@server:/path/",
                        "scp --dir katalog/ server:",
                        "scp -d katalog/ server:",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vilken är bättre för synkronisering?",
                    "options": ["scp", "rsync", "ftp", "cp"],
                    "correct": 1,
                },
                {
                    "question": "Vilken permission ska privata SSH-nycklar ha?",
                    "options": ["644", "755", "600", "777"],
                    "correct": 2,
                },
            ],
        },
        # ======================================================================
        # NODE 7: Firewall Essentials
        # ======================================================================
        {
            "title": "Firewall Essentials",
            "slug": "firewall-essentials",
            "description": "Konfigurera brandvägg och hantera nätverkssäkerhet.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# 🔥 Firewall Essentials

> **TL;DR:** Hantera brandvägg med `ufw` (Ubuntu) eller `firewall-cmd` (RHEL). Kolla öppna portar med `ss -tulpn`.

---

## 🎯 Varför viktigt för DevOps?

Brandväggen skyddar din server:
- Blockera oönskad trafik
- Öppna bara nödvändiga portar
- Förhindra intrång

⚠️ **VARNING:** Öppna ALLTID SSH (port 22) innan du aktiverar brandväggen!

---

## 🧭 UFW (Ubuntu/Debian)

### Status
```bash
sudo ufw status                 # ⭐ Visa status
sudo ufw status verbose         # Mer detaljer
sudo ufw status numbered        # Med nummer (för delete)
```

### Aktivera/Inaktivera
```bash
sudo ufw enable                 # ⭐ Aktivera
sudo ufw disable                # Inaktivera
```

### Öppna portar
```bash
sudo ufw allow 22               # ⭐ SSH (GÖR DETTA FÖRST!)
sudo ufw allow 80               # HTTP
sudo ufw allow 443              # HTTPS
sudo ufw allow 3000             # Custom port
```

### Blockera
```bash
sudo ufw deny 23                # Blockera port
sudo ufw deny from 10.0.0.5     # Blockera IP
```

### Ta bort regel
```bash
sudo ufw status numbered        # Se nummer
sudo ufw delete 3               # Ta bort regel 3
sudo ufw delete allow 80        # Ta bort specifik regel
```

---

## 🧭 Firewall-cmd (RHEL/CentOS)

### Status
```bash
sudo firewall-cmd --state
sudo firewall-cmd --list-all    # ⭐ Visa allt
```

### Öppna portar
```bash
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload      # ⭐ Ladda om!
```

---

## 🧭 Se öppna portar

### ss (rekommenderad)
```bash
ss -tulpn                       # ⭐ TCP + UDP + Listening + PID
ss -tulpn | grep :80            # Vad lyssnar på port 80?
```

### netstat (äldre)
```bash
netstat -tulpn                  # Samma som ss
```

**Flaggor:**
- `-t` = TCP
- `-u` = UDP
- `-l` = Listening
- `-p` = Process
- `-n` = Numerisk (ingen DNS)

---

## 🧭 Vanliga portar

| Port | Tjänst |
|------|--------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 27017 | MongoDB |

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Visa status | `sudo ufw status` |
| Öppna SSH | `sudo ufw allow 22` |
| Öppna HTTP/HTTPS | `sudo ufw allow 80 && sudo ufw allow 443` |
| Aktivera brandvägg | `sudo ufw enable` |
| Blockera IP | `sudo ufw deny from 10.0.0.5` |
| Ta bort regel | `sudo ufw delete allow 80` |
| Se öppna portar | `ss -tulpn` |
| Vad lyssnar på port? | `ss -tulpn \\| grep :80` |

---

## 🧠 Kom ihåg

- ⚠️ `ufw allow 22` INNAN `ufw enable`!
- `ufw status` = kolla regler
- `ss -tulpn` = se öppna portar
- Port 22 = SSH, 80 = HTTP, 443 = HTTPS
- `firewall-cmd --reload` = glöm inte ladda om!

---

## ✅ Checkpoint (Tenta)

1. Vad måste du göra INNAN du aktiverar brandväggen?
2. Hur öppnar du port 443 med ufw?
3. Hur ser du vilka portar som lyssnar?
4. Vilken port är SSH?
5. Hur blockerar du en specifik IP?
6. Hur tar du bort en ufw-regel?
""",
            "quiz": [
                {
                    "question": "Vad måste du göra INNAN du aktiverar brandväggen?",
                    "options": [
                        "Starta om servern",
                        "Öppna SSH (port 22)",
                        "Installera nginx",
                        "Skapa backup",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur öppnar du port 443 med ufw?",
                    "options": [
                        "ufw open 443",
                        "sudo ufw allow 443",
                        "ufw add 443",
                        "sudo ufw enable 443",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du vilka portar som lyssnar?",
                    "options": ["ports -l", "ss -tulpn", "listen --all", "netstat -a"],
                    "correct": 1,
                },
                {
                    "question": "Vilken port är SSH?",
                    "options": ["80", "443", "22", "21"],
                    "correct": 2,
                },
                {
                    "question": "Hur blockerar du en specifik IP med ufw?",
                    "options": [
                        "ufw block 10.0.0.5",
                        "sudo ufw deny from 10.0.0.5",
                        "ufw reject 10.0.0.5",
                        "sudo ufw stop 10.0.0.5",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur tar du bort en ufw-regel?",
                    "options": [
                        "ufw remove 80",
                        "sudo ufw delete allow 80",
                        "ufw drop 80",
                        "sudo ufw clear 80",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 8: Network Basics
        # ======================================================================
        {
            "title": "Network Basics",
            "slug": "network-basics",
            "description": "Nätverksdiagnostik och felsökning.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 🌐 Network Basics

> **TL;DR:** Kolla IP med `ip addr`, testa anslutning med `ping`, DNS med `dig`, portar med `nc`.

---

## 🎯 Varför viktigt för DevOps?

Nätverksproblem är vanliga:
- "Kan inte nå servern"
- "DNS fungerar inte"
- "Porten är blockerad"

Du måste kunna diagnostisera snabbt!

---

## 🧭 IP-konfiguration

### ip addr
```bash
ip addr                         # ⭐ Visa alla interfaces
ip addr show eth0               # Specifik interface
ip -4 addr                      # Bara IPv4
```

### ip route
```bash
ip route                        # ⭐ Routing-tabell
ip route | grep default         # Default gateway
```

### hostname
```bash
hostname                        # Servernamn
hostname -I                     # ⭐ IP-adresser
```

---

## 🧭 Testa anslutning

### ping
```bash
ping google.com                 # Kontinuerligt
ping -c 4 google.com            # ⭐ 4 paket
ping -c 1 192.168.1.1           # Snabb test
```

### traceroute
```bash
traceroute google.com           # Visa nätväg
traceroute -n google.com        # Utan DNS-lookup
```

---

## 🧭 DNS

### dig (rekommenderad)
```bash
dig google.com                  # ⭐ DNS-lookup
dig google.com +short           # Bara IP
dig @8.8.8.8 google.com         # Använd specifik DNS
dig -x 8.8.8.8                  # Reverse lookup
```

### nslookup
```bash
nslookup google.com             # Enklare DNS-lookup
```

### /etc/resolv.conf
```bash
cat /etc/resolv.conf            # DNS-servrar
```

---

## 🧭 Testa portar

### nc (netcat)
```bash
nc -zv server.com 80            # ⭐ Testa om port är öppen
nc -zv server.com 22            # Testa SSH
nc -zv server.com 1-1000        # Skanna range
```

### curl
```bash
curl -I https://google.com      # ⭐ Bara headers
curl -v https://google.com      # Verbose
curl -o fil.html https://url    # Ladda ner
curl -s ifconfig.me             # ⭐ Din publika IP
```

### wget
```bash
wget https://example.com/file.zip       # Ladda ner
wget -q -O - https://url                # Till stdout
```

---

## 🧭 Felsökningsflöde

När "kan inte nå server":

```bash
# 1. Har vi internet?
ping 8.8.8.8

# 2. Fungerar DNS?
dig google.com

# 3. Kan vi nå servern?
ping server.com

# 4. Är porten öppen?
nc -zv server.com 443

# 5. Svarar tjänsten?
curl -I https://server.com
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Visa IP-adress | `hostname -I` |
| Visa alla interfaces | `ip addr` |
| Testa internet | `ping -c 4 8.8.8.8` |
| DNS-lookup | `dig google.com +short` |
| Testa port | `nc -zv server.com 80` |
| HTTP headers | `curl -I https://url` |
| Min publika IP | `curl -s ifconfig.me` |
| Default gateway | `ip route \\| grep default` |

---

## 🧠 Kom ihåg

- `ip addr` = visa IP
- `ping -c 4` = testa anslutning (4 paket)
- `dig domain +short` = snabb DNS
- `nc -zv host port` = testa port
- `curl -I` = HTTP headers
- Felsök systematiskt: IP → DNS → Ping → Port → HTTP

---

## ✅ Checkpoint (Tenta)

1. Hur visar du serverns IP-adresser?
2. Hur testar du om du har internet?
3. Hur gör du en DNS-lookup?
4. Hur testar du om port 443 är öppen?
5. Hur ser du HTTP-headers?
6. Hur hittar du din publika IP?
""",
            "quiz": [
                {
                    "question": "Hur visar du serverns IP-adresser?",
                    "options": ["ipconfig", "hostname -I", "show ip", "ip show"],
                    "correct": 1,
                },
                {
                    "question": "Hur testar du om du har internet?",
                    "options": [
                        "internet --test",
                        "ping -c 4 8.8.8.8",
                        "test internet",
                        "check network",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur gör du en DNS-lookup?",
                    "options": [
                        "dns google.com",
                        "dig google.com",
                        "lookup google.com",
                        "resolve google.com",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur testar du om port 443 är öppen?",
                    "options": [
                        "port 443 server.com",
                        "nc -zv server.com 443",
                        "test port 443",
                        "check 443",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du HTTP-headers?",
                    "options": [
                        "http headers url",
                        "curl -I url",
                        "headers url",
                        "get -h url",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur hittar du din publika IP?",
                    "options": [
                        "ip public",
                        "curl -s ifconfig.me",
                        "myip",
                        "public-ip",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 9: Package Management
        # ======================================================================
        {
            "title": "Package Management",
            "slug": "package-management",
            "description": "Installera och hantera mjukvara med pakethanterare.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# 📦 Package Management

> **TL;DR:** `apt update && apt install paket` för Debian/Ubuntu, `yum/dnf install paket` för RHEL/CentOS.

---

## 🎯 Varför viktigt för DevOps?

- Installera verktyg och dependencies
- Hålla system uppdaterat (säkerhet!)
- Hantera versioner av mjukvara

---

## 🧭 APT (Debian/Ubuntu)

### Uppdatera
```bash
sudo apt update                 # ⭐ Uppdatera paketlista
sudo apt upgrade                # Uppgradera alla paket
sudo apt update && sudo apt upgrade -y   # ⭐ Combo
```

### Installera
```bash
sudo apt install nginx          # ⭐ Installera paket
sudo apt install -y nginx       # Auto-ja
sudo apt install nginx=1.18.0-0ubuntu1   # Specifik version
```

### Ta bort
```bash
sudo apt remove nginx           # Ta bort (behåll config)
sudo apt purge nginx            # ⭐ Ta bort allt
sudo apt autoremove             # Ta bort oanvända dependencies
```

### Sök & info
```bash
apt search nginx                # Sök paket
apt show nginx                  # ⭐ Info om paket
dpkg -l | grep nginx            # Installerade paket
```

---

## 🧭 YUM/DNF (RHEL/CentOS/Fedora)

### Uppdatera
```bash
sudo yum update                 # RHEL/CentOS 7
sudo dnf update                 # ⭐ RHEL 8+/Fedora
```

### Installera
```bash
sudo dnf install nginx          # ⭐ Installera
sudo dnf install -y nginx       # Auto-ja
```

### Ta bort
```bash
sudo dnf remove nginx           # Ta bort
sudo dnf autoremove             # Oanvända dependencies
```

### Sök & info
```bash
dnf search nginx                # Sök
dnf info nginx                  # ⭐ Info
rpm -qa | grep nginx            # Installerade paket
```

---

## 🧭 Vanliga operationer

### Lista installerade paket
```bash
# Debian/Ubuntu
dpkg -l                         # Alla paket
dpkg -l | wc -l                 # Antal paket

# RHEL/CentOS
rpm -qa
```

### Kolla vilken fil tillhör vilket paket
```bash
# Debian/Ubuntu
dpkg -S /usr/bin/nginx

# RHEL/CentOS
rpm -qf /usr/bin/nginx
```

### Rensa cache
```bash
sudo apt clean                  # Debian/Ubuntu
sudo dnf clean all              # RHEL/CentOS
```

---

## ⚡ Copy-paste lösningar

| Situation | Debian/Ubuntu | RHEL/CentOS |
|-----------|---------------|-------------|
| Uppdatera lista | `sudo apt update` | `sudo dnf check-update` |
| Uppgradera allt | `sudo apt upgrade -y` | `sudo dnf update -y` |
| Installera | `sudo apt install -y nginx` | `sudo dnf install -y nginx` |
| Ta bort | `sudo apt purge nginx` | `sudo dnf remove nginx` |
| Sök paket | `apt search nginx` | `dnf search nginx` |
| Paket-info | `apt show nginx` | `dnf info nginx` |

---

## 🧠 Kom ihåg

- `apt update` = uppdatera lista (gör ALLTID först!)
- `apt install -y` = installera utan frågor
- `apt purge` = ta bort helt (inkl config)
- RHEL 8+: använd `dnf` istället för `yum`
- `-y` flaggan = auto-bekräfta

---

## ✅ Checkpoint (Tenta)

1. Vilket kommando kör du FÖRST innan apt install?
2. Hur installerar du nginx utan interaktiva frågor?
3. Skillnad mellan apt remove och apt purge?
4. Vad använder du istället för yum på RHEL 8+?
5. Hur söker du efter ett paket?
6. Hur tar du bort oanvända dependencies?
""",
            "quiz": [
                {
                    "question": "Vilket kommando kör du FÖRST innan apt install?",
                    "options": [
                        "apt upgrade",
                        "sudo apt update",
                        "apt refresh",
                        "apt sync",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur installerar du nginx utan interaktiva frågor?",
                    "options": [
                        "apt install nginx --quiet",
                        "sudo apt install -y nginx",
                        "apt install nginx --auto",
                        "apt install nginx -f",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad är skillnaden mellan apt remove och apt purge?",
                    "options": [
                        "Ingen skillnad",
                        "purge tar bort config också",
                        "remove är snabbare",
                        "purge kräver sudo",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad använder du istället för yum på RHEL 8+?",
                    "options": [
                        "apt",
                        "dnf",
                        "rpm",
                        "pkg",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur söker du efter ett paket på Debian/Ubuntu?",
                    "options": [
                        "apt find nginx",
                        "apt search nginx",
                        "apt lookup nginx",
                        "apt query nginx",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur tar du bort oanvända dependencies?",
                    "options": [
                        "apt clean",
                        "sudo apt autoremove",
                        "apt prune",
                        "apt gc",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 10: System Services & systemd
        # ======================================================================
        {
            "title": "System Services & systemd",
            "slug": "system-services-systemd",
            "description": "Hantera tjänster med systemctl och läs loggar med journalctl.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# ⚙️ System Services & systemd

> **TL;DR:** `systemctl start/stop/restart tjänst`, `systemctl enable` för autostart, `journalctl` för loggar.

---

## 🎯 Varför viktigt för DevOps?

- Starta/stoppa tjänster (nginx, docker, etc)
- Konfigurera autostart vid boot
- Felsöka varför tjänster inte startar
- Läsa tjänstloggar

---

## 🧭 systemctl – Hantera tjänster

### Grundläggande
```bash
sudo systemctl start nginx      # ⭐ Starta
sudo systemctl stop nginx       # ⭐ Stoppa
sudo systemctl restart nginx    # ⭐ Omstart
sudo systemctl reload nginx     # Ladda om config
```

### Status
```bash
systemctl status nginx          # ⭐ Status + senaste loggar
systemctl is-active nginx       # active/inactive
systemctl is-enabled nginx      # enabled/disabled
```

### Autostart
```bash
sudo systemctl enable nginx     # ⭐ Starta vid boot
sudo systemctl disable nginx    # Starta INTE vid boot
sudo systemctl enable --now nginx   # Enable + start
```

---

## 🧭 Lista tjänster

```bash
systemctl list-units --type=service             # ⭐ Aktiva tjänster
systemctl list-units --type=service --all       # Alla tjänster
systemctl list-unit-files --type=service        # Alla installerade
systemctl list-units --failed                   # ⭐ Misslyckade
```

---

## 🧭 journalctl – Systemloggar

### Visa loggar
```bash
journalctl                              # Alla loggar
journalctl -u nginx                     # ⭐ Specifik tjänst
journalctl -u nginx -f                  # ⭐ Följ live
journalctl -u nginx --since "1 hour ago"
```

### Filtrera
```bash
journalctl -p err                       # Bara errors
journalctl -p err -u nginx              # Errors för nginx
journalctl --since today                # Dagens loggar
journalctl -n 50                        # Senaste 50 rader
```

### Boot-loggar
```bash
journalctl -b                           # Denna boot
journalctl -b -1                        # Förra boot
journalctl --list-boots                 # Lista boots
```

---

## 🧭 Skapa egen tjänst

```bash
sudo nano /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload            # ⭐ Ladda om efter ändring
sudo systemctl enable --now myapp
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Starta tjänst | `sudo systemctl start nginx` |
| Stoppa tjänst | `sudo systemctl stop nginx` |
| Omstart | `sudo systemctl restart nginx` |
| Status | `systemctl status nginx` |
| Enable autostart | `sudo systemctl enable nginx` |
| Enable + start | `sudo systemctl enable --now nginx` |
| Visa loggar | `journalctl -u nginx` |
| Följ loggar live | `journalctl -u nginx -f` |
| Misslyckade tjänster | `systemctl list-units --failed` |

---

## 🧠 Kom ihåg

- `systemctl start/stop/restart` = hantera tjänst
- `systemctl enable` = autostart vid boot
- `systemctl status` = se status + loggar
- `journalctl -u tjänst -f` = följ loggar live
- `daemon-reload` = efter att du ändrat service-fil

---

## ✅ Checkpoint (Tenta)

1. Hur startar du nginx-tjänsten?
2. Hur gör du så nginx startar automatiskt vid boot?
3. Hur ser du status och senaste loggar för nginx?
4. Hur följer du nginx-loggar i realtid?
5. Vad kör du efter att ha ändrat en service-fil?
6. Hur listar du misslyckade tjänster?
""",
            "quiz": [
                {
                    "question": "Hur startar du nginx-tjänsten?",
                    "options": [
                        "nginx start",
                        "sudo systemctl start nginx",
                        "service nginx on",
                        "start nginx",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur gör du så nginx startar automatiskt vid boot?",
                    "options": [
                        "systemctl autostart nginx",
                        "sudo systemctl enable nginx",
                        "systemctl boot nginx",
                        "nginx --autostart",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du status och senaste loggar för nginx?",
                    "options": [
                        "nginx status",
                        "systemctl status nginx",
                        "systemctl info nginx",
                        "nginx --status",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur följer du nginx-loggar i realtid?",
                    "options": [
                        "journalctl nginx --live",
                        "journalctl -u nginx -f",
                        "systemctl logs nginx -f",
                        "tail nginx logs",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad kör du efter att ha ändrat en service-fil?",
                    "options": [
                        "systemctl refresh",
                        "sudo systemctl daemon-reload",
                        "systemctl update",
                        "service reload",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur listar du misslyckade tjänster?",
                    "options": [
                        "systemctl errors",
                        "systemctl list-units --failed",
                        "systemctl --failed",
                        "journalctl --errors",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 11: File Permissions & Security
        # ======================================================================
        {
            "title": "File Permissions & Security",
            "slug": "file-permissions-security",
            "description": "Hantera filrättigheter och ägare med chmod och chown.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 🔐 File Permissions & Security

> **TL;DR:** `chmod 755 fil` för rättigheter, `chown user:group fil` för ägare, `ls -la` för att se.

---

## 🎯 Varför viktigt för DevOps?

- Säkra filer och mappar
- Felsöka "Permission denied"
- Ge rätt användare rätt access
- Förstå rwx-systemet

---

## 🧭 Förstå permissions

### ls -la output
```
-rwxr-xr-x 1 user group 1234 Dec 21 10:00 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └── Others (alla andra)
│ │  └───── Group (gruppmedlemmar)
│ └──────── User/Owner (ägare)
└────────── Filtyp (- = fil, d = mapp)
```

### rwx betydelse
| Bokstav | Siffra | Betydelse |
|---------|--------|-----------|
| r | 4 | Read (läsa) |
| w | 2 | Write (skriva) |
| x | 1 | Execute (köra) |

---

## 🧭 chmod – Ändra rättigheter

### Numeriskt (vanligast)
```bash
chmod 755 script.sh             # ⭐ rwxr-xr-x (vanlig script)
chmod 644 config.txt            # ⭐ rw-r--r-- (vanlig fil)
chmod 600 secrets.txt           # ⭐ rw------- (privat fil)
chmod 700 ~/.ssh                # ⭐ rwx------ (privat mapp)
```

### Symboliskt
```bash
chmod +x script.sh              # ⭐ Lägg till execute
chmod -w fil.txt                # Ta bort write
chmod u+x,g+r fil.sh            # User: +execute, Group: +read
```

### Rekursivt
```bash
chmod -R 755 /var/www           # ⭐ Alla filer i mapp
```

---

## 🧭 chown – Ändra ägare

```bash
sudo chown user fil.txt         # ⭐ Ändra ägare
sudo chown user:group fil.txt   # ⭐ Ändra ägare OCH grupp
sudo chown :group fil.txt       # Bara grupp
sudo chown -R www-data:www-data /var/www   # ⭐ Rekursivt
```

---

## 🧭 Vanliga permission-mönster

| Permission | Siffra | Användning |
|------------|--------|------------|
| rwxr-xr-x | 755 | Script, program, mappar |
| rw-r--r-- | 644 | Vanliga filer, config |
| rw------- | 600 | Privata filer, SSH-nycklar |
| rwx------ | 700 | Privata mappar, ~/.ssh |
| rwxrwxr-x | 775 | Delad mapp för grupp |

---

## 🧭 SSH-specifika permissions

```bash
chmod 700 ~/.ssh                # ⭐ SSH-mapp
chmod 600 ~/.ssh/id_rsa         # ⭐ Privat nyckel
chmod 644 ~/.ssh/id_rsa.pub     # Publik nyckel
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/config
```

---

## 🧭 Felsök "Permission denied"

```bash
# 1. Kolla rättigheter
ls -la fil.txt

# 2. Kolla ägare
ls -la fil.txt | awk '{print $3, $4}'

# 3. Fixa vanliga problem
chmod +x script.sh              # Kan inte köra script
sudo chown $USER:$USER fil      # Fel ägare
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Se rättigheter | `ls -la fil.txt` |
| Gör körbar | `chmod +x script.sh` |
| Standard fil | `chmod 644 fil.txt` |
| Privat fil | `chmod 600 secrets.txt` |
| Privat mapp | `chmod 700 ~/.ssh` |
| Ändra ägare | `sudo chown user:group fil` |
| Rekursivt | `chmod -R 755 /path` |
| SSH privat nyckel | `chmod 600 ~/.ssh/id_rsa` |

---

## 🧠 Kom ihåg

- `755` = rwxr-xr-x (script/mapp)
- `644` = rw-r--r-- (vanlig fil)
- `600` = rw------- (hemlig fil)
- `chmod +x` = gör körbar
- `chown user:group` = ändra ägare
- SSH-nyckel MÅSTE vara 600!

---

## ✅ Checkpoint (Tenta)

1. Hur ser du rättigheter för en fil?
2. Hur gör du ett script körbart?
3. Vilken permission ska en privat SSH-nyckel ha?
4. Hur ändrar du ägare OCH grupp?
5. Vad betyder 755?
6. Hur ändrar du rättigheter rekursivt?
""",
            "quiz": [
                {
                    "question": "Hur ser du rättigheter för en fil?",
                    "options": [
                        "perm fil.txt",
                        "ls -la fil.txt",
                        "chmod --show fil.txt",
                        "stat fil.txt",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur gör du ett script körbart?",
                    "options": [
                        "chmod run script.sh",
                        "chmod +x script.sh",
                        "chmod exec script.sh",
                        "execute script.sh",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vilken permission ska en privat SSH-nyckel ha?",
                    "options": [
                        "755",
                        "600",
                        "644",
                        "777",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ändrar du ägare OCH grupp?",
                    "options": [
                        "chown user+group fil",
                        "sudo chown user:group fil",
                        "chmod user:group fil",
                        "owner user group fil",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad betyder permission 755?",
                    "options": [
                        "rw-rw-rw-",
                        "rwxr-xr-x",
                        "rwx------",
                        "rw-r--r--",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ändrar du rättigheter rekursivt?",
                    "options": [
                        "chmod --all 755 /path",
                        "chmod -R 755 /path",
                        "chmod -r 755 /path",
                        "chmod 755 /path/*",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 12: Compression & Archives
        # ======================================================================
        {
            "title": "Compression & Archives",
            "slug": "compression-archives",
            "description": "Skapa och packa upp arkiv med tar, gzip och zip.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# 📦 Compression & Archives

> **TL;DR:** `tar -czvf arkiv.tar.gz mapp/` för att packa, `tar -xzvf arkiv.tar.gz` för att packa upp.

---

## 🎯 Varför viktigt för DevOps?

- Skapa backups
- Överföra många filer
- Ladda ner och packa upp mjukvara
- Spara diskutrymme

---

## 🧭 tar – Arkivera

### Skapa arkiv
```bash
tar -cvf arkiv.tar mapp/        # Bara arkivera (ingen kompression)
tar -czvf arkiv.tar.gz mapp/    # ⭐ Med gzip-kompression
tar -cjvf arkiv.tar.bz2 mapp/   # Med bzip2 (mer kompakt)
```

### Packa upp
```bash
tar -xvf arkiv.tar              # Packa upp tar
tar -xzvf arkiv.tar.gz          # ⭐ Packa upp tar.gz
tar -xjvf arkiv.tar.bz2         # Packa upp tar.bz2
tar -xzvf arkiv.tar.gz -C /dest # ⭐ Till specifik mapp
```

### Lista innehåll
```bash
tar -tvf arkiv.tar.gz           # ⭐ Visa utan att packa upp
```

### Flaggor förklaring
| Flagga | Betydelse |
|--------|-----------|
| c | Create (skapa) |
| x | Extract (packa upp) |
| v | Verbose (visa filer) |
| f | File (filnamn följer) |
| z | gzip-kompression |
| j | bzip2-kompression |

---

## 🧭 gzip/gunzip – Komprimera enskilda filer

```bash
gzip fil.txt                    # Komprimera → fil.txt.gz
gunzip fil.txt.gz               # Dekomprimera
gzip -k fil.txt                 # Behåll originalet
gzip -d fil.txt.gz              # = gunzip
```

---

## 🧭 zip/unzip – Windows-kompatibelt

```bash
zip arkiv.zip fil1 fil2         # Skapa zip
zip -r arkiv.zip mapp/          # ⭐ Rekursivt (mapp)
unzip arkiv.zip                 # ⭐ Packa upp
unzip arkiv.zip -d /dest        # Till specifik mapp
unzip -l arkiv.zip              # Lista innehåll
```

---

## 🧭 Vanliga scenarion

### Backup av mapp
```bash
tar -czvf backup-$(date +%Y%m%d).tar.gz /var/www
```

### Ladda ner och packa upp
```bash
wget https://example.com/app.tar.gz
tar -xzvf app.tar.gz
```

### Kopiera med komprimering
```bash
tar -czvf - mapp/ | ssh user@server "tar -xzvf - -C /dest"
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Skapa tar.gz | `tar -czvf arkiv.tar.gz mapp/` |
| Packa upp tar.gz | `tar -xzvf arkiv.tar.gz` |
| Packa upp till mapp | `tar -xzvf arkiv.tar.gz -C /dest` |
| Lista innehåll | `tar -tvf arkiv.tar.gz` |
| Skapa zip | `zip -r arkiv.zip mapp/` |
| Packa upp zip | `unzip arkiv.zip` |
| Backup med datum | `tar -czvf backup-$(date +%Y%m%d).tar.gz mapp/` |

---

## 🧠 Kom ihåg

- `tar -czvf` = Create gZip Verbose File
- `tar -xzvf` = eXtract gZip Verbose File
- `-C /path` = packa upp till specifik mapp
- `zip -r` = rekursivt för mappar
- `.tar.gz` = tar + gzip (vanligast i Linux)
- `.zip` = bäst för Windows-kompatibilitet

---

## ✅ Checkpoint (Tenta)

1. Hur skapar du ett tar.gz-arkiv?
2. Hur packar du upp ett tar.gz?
3. Hur packar du upp till en specifik mapp?
4. Hur ser du innehållet utan att packa upp?
5. Hur skapar du en zip rekursivt?
6. Vad betyder flaggorna c, x, z, v, f?
""",
            "quiz": [
                {
                    "question": "Hur skapar du ett tar.gz-arkiv av en mapp?",
                    "options": [
                        "tar -gz mapp/ arkiv.tar.gz",
                        "tar -czvf arkiv.tar.gz mapp/",
                        "gzip -r mapp/ arkiv.tar.gz",
                        "compress mapp/ arkiv.tar.gz",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur packar du upp ett tar.gz-arkiv?",
                    "options": [
                        "tar -unpack arkiv.tar.gz",
                        "tar -xzvf arkiv.tar.gz",
                        "untar arkiv.tar.gz",
                        "gunzip arkiv.tar.gz",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur packar du upp till en specifik mapp?",
                    "options": [
                        "tar -xzvf arkiv.tar.gz --dest /mapp",
                        "tar -xzvf arkiv.tar.gz -C /mapp",
                        "tar -xzvf arkiv.tar.gz > /mapp",
                        "tar -xzvf arkiv.tar.gz -d /mapp",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du innehållet utan att packa upp?",
                    "options": [
                        "tar -list arkiv.tar.gz",
                        "tar -tvf arkiv.tar.gz",
                        "tar --show arkiv.tar.gz",
                        "cat arkiv.tar.gz",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur skapar du en zip av en mapp rekursivt?",
                    "options": [
                        "zip mapp/ arkiv.zip",
                        "zip -r arkiv.zip mapp/",
                        "zip --recursive arkiv.zip mapp/",
                        "zipr arkiv.zip mapp/",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad betyder flaggan 'c' i tar?",
                    "options": [
                        "Compress",
                        "Create",
                        "Copy",
                        "Check",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 13: Environment & Variables
        # ======================================================================
        {
            "title": "Environment & Variables",
            "slug": "environment-variables",
            "description": "Hantera miljövariabler och konfiguration.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# 🌍 Environment & Variables

> **TL;DR:** `export VAR=värde` temporärt, lägg i `~/.bashrc` för permanent, `env` för att visa alla.

---

## 🎯 Varför viktigt för DevOps?

- Konfigurera applikationer (API-nycklar, databas-URL)
- Anpassa shell-beteende
- 12-factor app principer
- Felsöka "command not found"

---

## 🧭 Visa miljövariabler

```bash
env                             # ⭐ Alla miljövariabler
printenv                        # Samma sak
echo $PATH                      # ⭐ Specifik variabel
echo $HOME                      # Hemkatalog
echo $USER                      # Användarnamn
```

---

## 🧭 Sätta variabler

### Temporärt (denna session)
```bash
export MY_VAR="värde"           # ⭐ Exportera (synlig för child processes)
MY_VAR="värde"                  # Bara i nuvarande shell
export PATH="$PATH:/ny/sökväg"  # ⭐ Lägg till i PATH
```

### För ett kommando
```bash
DATABASE_URL="postgres://..." python app.py    # Bara för detta kommando
```

### Permanent
```bash
# Lägg till i ~/.bashrc eller ~/.bash_profile
echo 'export MY_VAR="värde"' >> ~/.bashrc
source ~/.bashrc                # ⭐ Ladda om
```

---

## 🧭 Viktiga systemvariabler

| Variabel | Beskrivning |
|----------|-------------|
| `PATH` | Sökvägar för kommandon |
| `HOME` | Hemkatalog |
| `USER` | Användarnamn |
| `SHELL` | Aktuellt shell |
| `PWD` | Nuvarande katalog |
| `EDITOR` | Standard texteditor |
| `LANG` | Språkinställning |

---

## 🧭 PATH – Speciellt viktigt

```bash
echo $PATH                      # ⭐ Visa PATH
export PATH="$PATH:/ny/sökväg"  # ⭐ Lägg till sist
export PATH="/ny/sökväg:$PATH"  # Lägg till först (högre prio)

# Permanent i ~/.bashrc
echo 'export PATH="$PATH:/opt/myapp/bin"' >> ~/.bashrc
```

---

## 🧭 .env filer (DevOps-standard)

```bash
# .env fil
DATABASE_URL=postgres://localhost/db
API_KEY=secret123
DEBUG=true
```

```bash
# Ladda .env
source .env                     # Enkel laddning
export $(cat .env | xargs)      # Exportera alla
```

---

## 🧭 Bash-konfigurationsfiler

| Fil | När den körs |
|-----|--------------|
| `~/.bashrc` | Interaktiv non-login shell |
| `~/.bash_profile` | Login shell |
| `~/.profile` | Login shell (generell) |
| `/etc/environment` | Systemövergripande |

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Visa alla variabler | `env` |
| Visa specifik | `echo $VAR` |
| Sätt temporärt | `export VAR="värde"` |
| Sätt permanent | `echo 'export VAR="värde"' >> ~/.bashrc` |
| Ladda om bashrc | `source ~/.bashrc` |
| Lägg till i PATH | `export PATH="$PATH:/ny/sökväg"` |
| Ladda .env | `export $(cat .env \\| xargs)` |

---

## 🧠 Kom ihåg

- `export` = gör synlig för child processes
- `~/.bashrc` = permanent för bash
- `source` = ladda om config
- `$PATH` = var shell letar efter kommandon
- .env-filer = standard för app-config
- Glöm inte `source ~/.bashrc` efter ändringar!

---

## ✅ Checkpoint (Tenta)

1. Hur visar du alla miljövariabler?
2. Hur sätter du en variabel temporärt?
3. Hur gör du variabeln permanent?
4. Hur laddar du om ~/.bashrc?
5. Hur lägger du till en sökväg i PATH?
6. Vilken fil editerar du för permanenta bash-variabler?
""",
            "quiz": [
                {
                    "question": "Hur visar du alla miljövariabler?",
                    "options": [
                        "vars",
                        "env",
                        "list env",
                        "show vars",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur sätter du en variabel temporärt?",
                    "options": [
                        "set VAR=värde",
                        'export VAR="värde"',
                        "var VAR värde",
                        "define VAR värde",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur gör du variabeln permanent?",
                    "options": [
                        "export --permanent VAR",
                        "Lägg till i ~/.bashrc",
                        "save VAR",
                        "persist VAR",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur laddar du om ~/.bashrc?",
                    "options": [
                        "reload bashrc",
                        "source ~/.bashrc",
                        "bash --reload",
                        "refresh ~/.bashrc",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur lägger du till en sökväg i PATH?",
                    "options": [
                        'PATH.add("/ny/sökväg")',
                        'export PATH="$PATH:/ny/sökväg"',
                        "addpath /ny/sökväg",
                        "PATH += /ny/sökväg",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vilken fil editerar du för permanenta bash-variabler?",
                    "options": [
                        "/etc/vars",
                        "~/.bashrc",
                        "/var/env",
                        "~/.variables",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 14: Disk Management
        # ======================================================================
        {
            "title": "Disk Management",
            "slug": "disk-management",
            "description": "Hantera diskutrymme, partitioner och montering.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 💾 Disk Management

> **TL;DR:** `df -h` för diskutrymme, `du -sh` för mappstorlek, `lsblk` för diskar, `mount` för att ansluta.

---

## 🎯 Varför viktigt för DevOps?

- "Disk full" är vanligt problem
- Hitta vad som tar plats
- Ansluta och hantera diskar
- Övervaka diskutrymme

---

## 🧭 df – Diskutrymme

```bash
df -h                           # ⭐ Human-readable storlekar
df -h /                         # Specifik partition
df -h | grep -v tmpfs           # Skippa temporära
df -hT                          # Visa filsystemtyp
```

### Tolka output
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       50G   35G   13G  73% /
```

---

## 🧭 du – Mappstorlek

```bash
du -sh /var                     # ⭐ Total storlek på mapp
du -sh *                        # ⭐ Storlek per mapp/fil
du -sh /var/*                   # Undermappar i /var
du -h --max-depth=1 /var        # En nivå djupt
```

### Hitta stora mappar
```bash
du -sh /* 2>/dev/null | sort -hr | head   # ⭐ Största i /
du -sh /var/* | sort -hr | head           # Största i /var
```

---

## 🧭 lsblk – Lista diskar

```bash
lsblk                           # ⭐ Alla diskar och partitioner
lsblk -f                        # Med filsystem-info
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT
```

---

## 🧭 mount/umount – Anslut diskar

```bash
# Visa monterade
mount | grep "^/dev"            # ⭐ Riktiga diskar
findmnt                         # Träd-vy

# Montera
sudo mount /dev/sdb1 /mnt       # Montera disk
sudo mount -o ro /dev/sdb1 /mnt # Read-only

# Avmontera
sudo umount /mnt                # ⭐ Avmontera
sudo umount -l /mnt             # Lazy unmount (om busy)
```

---

## 🧭 /etc/fstab – Automatisk montering

```bash
cat /etc/fstab                  # Visa config
sudo nano /etc/fstab            # Editera
```

```
# Exempel rad i fstab
/dev/sdb1  /data  ext4  defaults  0  2
```

---

## 🧭 Felsök "disk full"

```bash
# 1. Var är disken full?
df -h

# 2. Hitta stora mappar
du -sh /* 2>/dev/null | sort -hr | head

# 3. Gå djupare
du -sh /var/* | sort -hr | head

# 4. Vanliga syndare
du -sh /var/log                 # Loggar
du -sh /tmp                     # Temporära filer
sudo journalctl --disk-usage    # Systemd-loggar

# 5. Rensa
sudo journalctl --vacuum-size=100M  # Rensa systemd-loggar
sudo apt clean                      # Rensa paket-cache
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Visa diskutrymme | `df -h` |
| Mappstorlek | `du -sh /path` |
| Storlek per mapp | `du -sh *` |
| Hitta stora mappar | `du -sh /* 2>/dev/null \\| sort -hr \\| head` |
| Lista diskar | `lsblk` |
| Montera disk | `sudo mount /dev/sdb1 /mnt` |
| Avmontera | `sudo umount /mnt` |
| Rensa systemloggar | `sudo journalctl --vacuum-size=100M` |

---

## 🧠 Kom ihåg

- `df -h` = hur mycket plats finns?
- `du -sh` = hur stor är mappen?
- `lsblk` = vilka diskar finns?
- `sort -hr` = sortera storlek, störst först
- `/var/log` = vanlig syndare för disk full
- Kolla ALLTID med `df -h` först vid diskproblem

---

## ✅ Checkpoint (Tenta)

1. Hur kollar du ledigt diskutrymme?
2. Hur ser du storleken på en mapp?
3. Hur hittar du de största mapparna?
4. Hur listar du alla diskar?
5. Hur monterar du en disk?
6. Var hamnar systemloggar som ofta tar plats?
""",
            "quiz": [
                {
                    "question": "Hur kollar du ledigt diskutrymme?",
                    "options": [
                        "disk --free",
                        "df -h",
                        "free -h",
                        "space -h",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du storleken på en mapp?",
                    "options": [
                        "size /mapp",
                        "du -sh /mapp",
                        "ls -s /mapp",
                        "stat /mapp",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur hittar du de största mapparna i /?",
                    "options": [
                        "find / --largest",
                        "du -sh /* | sort -hr | head",
                        "ls -lS /",
                        "big /",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur listar du alla diskar?",
                    "options": [
                        "disks",
                        "lsblk",
                        "showdisk",
                        "fdisk",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur monterar du en disk?",
                    "options": [
                        "attach /dev/sdb1 /mnt",
                        "sudo mount /dev/sdb1 /mnt",
                        "connect /dev/sdb1 /mnt",
                        "disk mount /dev/sdb1 /mnt",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vilken mapp är vanlig syndare för disk full?",
                    "options": [
                        "/home",
                        "/var/log",
                        "/usr",
                        "/bin",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 15: Quick Reference & Workflows
        # ======================================================================
        {
            "title": "Quick Reference & Workflows",
            "slug": "quick-reference-workflows",
            "description": "Snabbreferens och vanliga arbetsflöden.",
            "difficulty": "easy",
            "estimated_minutes": 30,
            "xp_reward": 100,
            "content": """# 📋 Quick Reference & Workflows

> **TL;DR:** De vanligaste kommandona och arbetsflödena på ett ställe. Bokmärk denna!

---

## 🎯 Varför denna lektion?

- Snabbreferens för dagligt arbete
- Vanliga arbetsflöden samlade
- Copy-paste-färdiga lösningar
- Perfekt att ha bredvid terminalen

---

## 🧭 Dagliga kommandon

### Navigation
```bash
cd /path                        # Gå till mapp
cd ..                           # Upp en nivå
cd ~                            # Hem
cd -                            # Tillbaka till förra mappen
pwd                             # Var är jag?
```

### Filer & mappar
```bash
ls -la                          # Lista allt
mkdir -p mapp/undermapp         # Skapa mappar
cp -r källa/ dest/              # Kopiera mapp
mv fil.txt /ny/plats/           # Flytta
rm -rf mapp/                    # Ta bort (VARNING!)
```

### Visa innehåll
```bash
cat fil.txt                     # Hela filen
head -20 fil.txt                # Första 20 rader
tail -f logg.log                # Följ live
less fil.txt                    # Bläddra (q = quit)
```

---

## 🧭 Sök & hitta

```bash
grep "text" fil.txt             # Sök i fil
grep -r "text" /path/           # Sök rekursivt
find /path -name "*.log"        # Hitta filer
which kommando                  # Var finns kommando?
```

---

## 🧭 System & övervakning

```bash
htop                            # Interaktiv processvy
df -h                           # Diskutrymme
free -h                         # Minne
uptime                          # Load
ps aux | grep nginx             # Hitta process
```

---

## 🧭 Tjänster

```bash
sudo systemctl start nginx      # Starta
sudo systemctl stop nginx       # Stoppa
sudo systemctl restart nginx    # Omstart
systemctl status nginx          # Status
journalctl -u nginx -f          # Loggar live
```

---

## 🧭 Nätverk

```bash
ip addr                         # IP-adresser
ping -c 4 google.com            # Testa anslutning
curl -I https://url             # HTTP headers
nc -zv server 80                # Testa port
dig domain.com +short           # DNS lookup
```

---

## 🧭 Vanliga arbetsflöden

### Deploya en app
```bash
cd /var/www/myapp
git pull origin main
npm install
npm run build
sudo systemctl restart myapp
```

### Felsök "server svarar inte"
```bash
# 1. Körs tjänsten?
systemctl status nginx

# 2. Vilken port?
ss -tlnp | grep nginx

# 3. Brandvägg?
sudo ufw status

# 4. Loggar?
journalctl -u nginx --since "10 min ago"
```

### Felsök "disk full"
```bash
df -h                           # Var är det fullt?
du -sh /* | sort -hr | head     # Vad tar plats?
sudo journalctl --vacuum-size=100M  # Rensa loggar
```

### Ny server setup
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y nginx git curl
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

---

## ⚡ Mega copy-paste tabell

| Behov | Kommando |
|-------|----------|
| Var är jag? | `pwd` |
| Lista filer | `ls -la` |
| Sök text | `grep -r "text" /path/` |
| Hitta fil | `find /path -name "*.txt"` |
| Diskutrymme | `df -h` |
| Mappstorlek | `du -sh /path` |
| Processer | `ps aux \\| grep namn` |
| Starta tjänst | `sudo systemctl start namn` |
| Tjänstloggar | `journalctl -u namn -f` |
| Min IP | `hostname -I` |
| Testa port | `nc -zv server port` |

---

## 🧠 Kom ihåg

- `Tab` = autocomplete
- `Ctrl+C` = avbryt
- `Ctrl+R` = sök historik
- `!!` = förra kommandot
- `sudo !!` = kör förra som root
- `man kommando` = manual

---

## ✅ Checkpoint (Tenta)

1. Hur går du tillbaka till förra mappen?
2. Hur följer du en loggfil i realtid?
3. Hur söker du rekursivt efter text?
4. Hur kollar du status på en tjänst?
5. Hur testar du om en port är öppen?
6. Vad gör Ctrl+R i terminalen?
""",
            "quiz": [
                {
                    "question": "Hur går du tillbaka till förra mappen?",
                    "options": [
                        "cd back",
                        "cd -",
                        "cd ..",
                        "cd previous",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur följer du en loggfil i realtid?",
                    "options": [
                        "cat -f logg.log",
                        "tail -f logg.log",
                        "watch logg.log",
                        "follow logg.log",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur söker du rekursivt efter text?",
                    "options": [
                        "search -r text /path/",
                        'grep -r "text" /path/',
                        "find text /path/",
                        "look -r text /path/",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kollar du status på en tjänst?",
                    "options": [
                        "service nginx info",
                        "systemctl status nginx",
                        "nginx --status",
                        "check nginx",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur testar du om en port är öppen?",
                    "options": [
                        "port test server 80",
                        "nc -zv server 80",
                        "ping server:80",
                        "check port 80",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad gör Ctrl+R i terminalen?",
                    "options": [
                        "Restart terminal",
                        "Sök i kommandohistorik",
                        "Refresh screen",
                        "Run last command",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 16: Terminal Productivity & Time Savers
        # ======================================================================
        {
            "title": "Terminal Productivity & Time Savers",
            "slug": "terminal-productivity-time-savers",
            "description": "Tangentbordsgenvägar, alias och produktivitetstips.",
            "difficulty": "easy",
            "estimated_minutes": 35,
            "xp_reward": 100,
            "content": """# ⚡ Terminal Productivity & Time Savers

> **TL;DR:** `Tab` för autocomplete, `Ctrl+R` för historik, alias för genvägar, `&&` för kedjade kommandon.

---

## 🎯 Varför viktigt för DevOps?

- Jobba snabbare i terminalen
- Färre tangenttryckningar = färre fel
- Automatisera repetitiva uppgifter
- Pro-tips som sparar timmar

---

## 🧭 Tangentbordsgenvägar

### Navigering
| Genväg | Funktion |
|--------|----------|
| `Tab` | ⭐ Autocomplete |
| `Tab Tab` | Visa alla möjligheter |
| `Ctrl+A` | Gå till början av rad |
| `Ctrl+E` | Gå till slutet av rad |
| `Ctrl+U` | Radera från cursor till början |
| `Ctrl+K` | Radera från cursor till slut |
| `Ctrl+W` | Radera ord bakåt |

### Kontroll
| Genväg | Funktion |
|--------|----------|
| `Ctrl+C` | ⭐ Avbryt körande kommando |
| `Ctrl+Z` | Pausa (bg/fg för att återuppta) |
| `Ctrl+D` | Logout / EOF |
| `Ctrl+L` | ⭐ Rensa skärm (= clear) |

---

## 🧭 Historik

```bash
history                         # Visa historik
history | grep ssh              # Sök i historik
!123                            # Kör kommando #123
!!                              # ⭐ Förra kommandot
sudo !!                         # ⭐ Kör förra som sudo
!ssh                            # Senaste kommando som började med "ssh"
```

### Ctrl+R – Interaktiv sökning
```
Ctrl+R → börja skriva → Enter
Ctrl+R igen → nästa match
```

---

## 🧭 Alias – Skapa genvägar

### Temporärt
```bash
alias ll='ls -la'
alias ..='cd ..'
alias update='sudo apt update && sudo apt upgrade -y'
```

### Permanent (~/.bashrc)
```bash
echo "alias ll='ls -la'" >> ~/.bashrc
echo "alias gs='git status'" >> ~/.bashrc
echo "alias dc='docker-compose'" >> ~/.bashrc
source ~/.bashrc
```

### Användbara alias
```bash
alias ll='ls -la'
alias la='ls -A'
alias ..='cd ..'
alias ...='cd ../..'
alias gs='git status'
alias gp='git pull'
alias dc='docker-compose'
alias k='kubectl'
alias ports='ss -tlnp'
alias myip='curl -s ifconfig.me'
```

---

## 🧭 Kedja kommandon

```bash
# && = kör nästa OM förra lyckades
apt update && apt upgrade       # ⭐ Vanligast

# || = kör nästa OM förra misslyckades
ping -c 1 server || echo "Server nere!"

# ; = kör alltid nästa
cd /tmp; ls; pwd                # Kör alla oavsett

# | = pipe output till nästa
ps aux | grep nginx | head      # ⭐ Pipe-kedja
```

---

## 🧭 Brace expansion

```bash
mkdir -p projekt/{src,test,docs}        # Skapar 3 mappar
cp fil.txt{,.bak}                       # ⭐ Kopiera till fil.txt.bak
mv fil.{txt,md}                         # Byt extension
touch file{1..5}.txt                    # file1.txt till file5.txt
```

---

## 🧭 Kommandosubstitution

```bash
echo "Idag är $(date)"                  # ⭐ Kör kommando i sträng
files=$(ls *.txt)                       # Spara output i variabel
tar -czvf backup-$(date +%Y%m%d).tar.gz /data
```

---

## ⚡ Copy-paste lösningar

| Behov | Lösning |
|-------|---------|
| Kör förra som sudo | `sudo !!` |
| Sök historik | `Ctrl+R` |
| Rensa skärm | `Ctrl+L` |
| Avbryt | `Ctrl+C` |
| Skapa backup | `cp fil{,.bak}` |
| Flera mappar | `mkdir {mapp1,mapp2,mapp3}` |
| Kör om lyckas | `cmd1 && cmd2` |
| Dagens datum i filnamn | `$(date +%Y%m%d)` |

---

## 🧠 Kom ihåg

- `Tab` = din bästa vän
- `Ctrl+R` = sök historik
- `!!` = förra kommandot
- `&&` = kör om förra lyckades
- Alias = spara tid på repetitiva kommandon
- `{}` = brace expansion för flera filer/mappar

---

## ✅ Checkpoint (Tenta)

1. Hur autocomplete:ar du ett kommando?
2. Hur söker du i kommandohistoriken?
3. Hur kör du förra kommandot med sudo?
4. Vad gör && mellan kommandon?
5. Hur skapar du ett alias?
6. Hur avbryter du ett körande kommando?
""",
            "quiz": [
                {
                    "question": "Hur autocomplete:ar du ett kommando?",
                    "options": [
                        "Ctrl+A",
                        "Tab",
                        "Enter",
                        "Space",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur söker du i kommandohistoriken?",
                    "options": [
                        "Ctrl+H",
                        "Ctrl+R",
                        "Ctrl+S",
                        "Ctrl+F",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kör du förra kommandot med sudo?",
                    "options": [
                        "sudo last",
                        "sudo !!",
                        "sudo -l",
                        "sudo repeat",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad gör && mellan kommandon?",
                    "options": [
                        "Kör alltid båda",
                        "Kör nästa om förra lyckades",
                        "Kör parallellt",
                        "Kör nästa om förra misslyckades",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur skapar du ett permanent alias?",
                    "options": [
                        "alias --save ll='ls -la'",
                        "Lägg till i ~/.bashrc",
                        "alias -p ll='ls -la'",
                        "save alias ll",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur avbryter du ett körande kommando?",
                    "options": [
                        "Ctrl+X",
                        "Ctrl+C",
                        "Ctrl+Q",
                        "Esc",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 17: User & Group Management
        # ======================================================================
        {
            "title": "User & Group Management",
            "slug": "user-group-management",
            "description": "Hantera användare, grupper och behörigheter.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# 👥 User & Group Management

> **TL;DR:** `useradd` skapar användare, `usermod` ändrar, `groupadd` skapar grupper, `passwd` sätter lösenord.

---

## 🎯 Varför viktigt för DevOps?

- Skapa service-användare för applikationer
- Hantera access till system
- Säkerhet och isolering
- Förstå UID/GID i containers

---

## 🧭 Visa användare & grupper

```bash
whoami                          # ⭐ Vem är jag?
id                              # ⭐ UID, GID och grupper
id username                     # Info om specifik user
groups                          # Mina grupper
groups username                 # Användares grupper
cat /etc/passwd                 # Alla användare
cat /etc/group                  # Alla grupper
```

---

## 🧭 Skapa användare

```bash
sudo useradd username           # Skapa (minimal)
sudo useradd -m username        # ⭐ Med hemkatalog
sudo useradd -m -s /bin/bash username   # ⭐ Med bash
sudo useradd -r -s /usr/sbin/nologin appuser  # ⭐ Service-user
```

### Vanliga flaggor
| Flagga | Betydelse |
|--------|-----------|
| `-m` | Skapa hemkatalog |
| `-s /bin/bash` | Sätt shell |
| `-r` | System/service user |
| `-G grupp` | Lägg till i grupp |
| `-d /path` | Specifik hemkatalog |

---

## 🧭 Ändra användare

```bash
sudo usermod -aG docker username    # ⭐ Lägg till i grupp
sudo usermod -aG sudo username      # Ge sudo-access
sudo usermod -s /bin/bash username  # Ändra shell
sudo usermod -L username            # Lås konto
sudo usermod -U username            # Lås upp konto
```

**⚠️ Viktigt:** Använd ALLTID `-aG` (append) när du lägger till grupper!

---

## 🧭 Ta bort användare

```bash
sudo userdel username           # Ta bort user
sudo userdel -r username        # ⭐ Ta bort + hemkatalog
```

---

## 🧭 Lösenord

```bash
sudo passwd username            # ⭐ Sätt/ändra lösenord
passwd                          # Ändra eget lösenord
sudo passwd -l username         # Lås konto
sudo passwd -u username         # Lås upp
sudo chage -l username          # Lösenordspolicy
```

---

## 🧭 Grupper

```bash
sudo groupadd developers        # ⭐ Skapa grupp
sudo groupdel developers        # Ta bort grupp
sudo gpasswd -a user developers # Lägg till user i grupp
sudo gpasswd -d user developers # Ta bort user från grupp
```

---

## 🧭 sudo-access

```bash
# Lägg till i sudo-gruppen
sudo usermod -aG sudo username      # Debian/Ubuntu
sudo usermod -aG wheel username     # RHEL/CentOS

# Eller editera sudoers
sudo visudo
# Lägg till: username ALL=(ALL) NOPASSWD: ALL
```

---

## 🧭 Service-användare (DevOps-vanligt)

```bash
# Skapa användare för app (ingen login, ingen hemkatalog)
sudo useradd -r -s /usr/sbin/nologin -M appuser

# Ge ägande till app-mapp
sudo chown -R appuser:appuser /opt/myapp

# Kör app som den användaren
sudo -u appuser /opt/myapp/start.sh
```

---

## ⚡ Copy-paste lösningar

| Situation | Kommando |
|-----------|----------|
| Vem är jag? | `whoami` |
| Mina grupper | `id` |
| Skapa user med hemkatalog | `sudo useradd -m -s /bin/bash username` |
| Lägg till i grupp | `sudo usermod -aG grupp username` |
| Sätt lösenord | `sudo passwd username` |
| Skapa grupp | `sudo groupadd gruppnamn` |
| Service-user | `sudo useradd -r -s /usr/sbin/nologin appuser` |
| Ge sudo-access | `sudo usermod -aG sudo username` |

---

## 🧠 Kom ihåg

- `-m` = skapa hemkatalog
- `-aG` = append to group (VIKTIGT!)
- `-r` = system user (för services)
- `/usr/sbin/nologin` = ingen login möjlig
- `visudo` = säker redigering av sudoers
- Logga ut/in efter gruppändringar!

---

## ✅ Checkpoint (Tenta)

1. Hur skapar du en användare med hemkatalog?
2. Hur lägger du till en användare i en grupp?
3. Hur skapar du en service-användare?
4. Hur sätter du lösenord för en användare?
5. Hur ger du en användare sudo-access?
6. Varför är -aG viktigt vid usermod?
""",
            "quiz": [
                {
                    "question": "Hur skapar du en användare med hemkatalog?",
                    "options": [
                        "useradd username",
                        "sudo useradd -m username",
                        "adduser --home username",
                        "create user username",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur lägger du till en användare i en grupp?",
                    "options": [
                        "usermod -g grupp user",
                        "sudo usermod -aG grupp user",
                        "addgroup user grupp",
                        "group add user grupp",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur skapar du en service-användare?",
                    "options": [
                        "useradd --service appuser",
                        "sudo useradd -r -s /usr/sbin/nologin appuser",
                        "adduser --system appuser",
                        "create service appuser",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur sätter du lösenord för en användare?",
                    "options": [
                        "password username",
                        "sudo passwd username",
                        "setpass username",
                        "usermod --password username",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ger du en användare sudo-access på Ubuntu?",
                    "options": [
                        "sudo adduser username",
                        "sudo usermod -aG sudo username",
                        "sudoers add username",
                        "grant sudo username",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Varför är -aG viktigt vid usermod?",
                    "options": [
                        "Det går snabbare",
                        "Det lägger till utan att ta bort andra grupper",
                        "Det kräver mindre behörighet",
                        "Det fungerar på alla system",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 18: Cron Jobs & Task Scheduling
        # ======================================================================
        {
            "title": "Cron Jobs & Task Scheduling",
            "slug": "cron-jobs-task-scheduling",
            "description": "Automatisera uppgifter med schemalagda jobb.",
            "difficulty": "easy",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "content": """# ⏰ Cron Jobs & Task Scheduling

> **TL;DR:** `crontab -e` för att editera, format: `minut timme dag månad veckodag kommando`.

---

## 🎯 Varför viktigt för DevOps?

- Automatisera backups
- Schemalagd logrotation
- Övervakningsskript
- Regelbundna cleanup-jobb

---

## 🧭 Cron-format

```
┌───────────── minut (0-59)
│ ┌───────────── timme (0-23)
│ │ ┌───────────── dag i månad (1-31)
│ │ │ ┌───────────── månad (1-12)
│ │ │ │ ┌───────────── veckodag (0-7, 0 och 7 = söndag)
│ │ │ │ │
* * * * * kommando
```

### Specialtecken
| Tecken | Betydelse |
|--------|-----------|
| `*` | Alla värden |
| `,` | Lista: 1,3,5 |
| `-` | Range: 1-5 |
| `/` | Steg: */15 (var 15:e) |

---

## 🧭 crontab – Hantera jobb

```bash
crontab -e                      # ⭐ Editera mina jobb
crontab -l                      # ⭐ Lista mina jobb
crontab -r                      # Ta bort alla jobb
sudo crontab -u user -e         # Editera annan användares
```

---

## 🧭 Vanliga scheman

```bash
# Varje minut
* * * * * /script.sh

# Var 5:e minut
*/5 * * * * /script.sh

# Varje timme
0 * * * * /script.sh

# Varje dag kl 02:00
0 2 * * * /script.sh            # ⭐ Backups!

# Varje måndag kl 09:00
0 9 * * 1 /script.sh

# Första dagen i månaden
0 0 1 * * /script.sh

# Vardagar kl 08:00
0 8 * * 1-5 /script.sh
```

---

## 🧭 Genvägar (om stöds)

```bash
@reboot /script.sh              # ⭐ Vid uppstart
@hourly /script.sh              # Varje timme
@daily /script.sh               # ⭐ Varje dag 00:00
@weekly /script.sh              # Varje vecka
@monthly /script.sh             # Varje månad
```

---

## 🧭 Best practices

### Använd fullständig sökväg
```bash
# Fel
0 2 * * * backup.sh

# Rätt
0 2 * * * /home/user/scripts/backup.sh
```

### Logga output
```bash
0 2 * * * /script.sh >> /var/log/backup.log 2>&1
```

### Environment
```bash
# Cron har minimal miljö - sätt variabler!
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@example.com

0 2 * * * /backup.sh
```

---

## 🧭 System cron (/etc/cron.*)

```bash
ls /etc/cron.*
/etc/cron.d/           # Individuella filer
/etc/cron.daily/       # ⭐ Körs dagligen
/etc/cron.hourly/      # Körs varje timme
/etc/cron.weekly/      # Körs varje vecka
/etc/cron.monthly/     # Körs varje månad
```

```bash
# Lägg script i rätt mapp (utan extension!)
sudo cp backup.sh /etc/cron.daily/backup
sudo chmod +x /etc/cron.daily/backup
```

---

## 🧭 Felsöka cron

```bash
# Kolla cron-loggar
grep CRON /var/log/syslog
journalctl -u cron

# Testa att skript fungerar manuellt
/home/user/scripts/backup.sh

# Kolla att cron körs
systemctl status cron
```

---

## ⚡ Copy-paste lösningar

| Schema | Cron-expression |
|--------|-----------------|
| Varje minut | `* * * * *` |
| Var 5:e minut | `*/5 * * * *` |
| Varje timme | `0 * * * *` |
| Dagligen 02:00 | `0 2 * * *` |
| Måndagar 09:00 | `0 9 * * 1` |
| Vardagar 08:00 | `0 8 * * 1-5` |
| Vid uppstart | `@reboot` |

---

## 🧠 Kom ihåg

- `crontab -e` = editera jobb
- `crontab -l` = lista jobb
- Minut-Timme-Dag-Månad-Veckodag
- `*/5` = var 5:e
- Använd FULLSTÄNDIG sökväg
- Logga output med `>> logfil 2>&1`
- `@reboot` = kör vid uppstart

---

## ✅ Checkpoint (Tenta)

1. Hur editerar du dina cron-jobb?
2. Hur skriver du "varje dag kl 02:00"?
3. Vad betyder */15 i minut-fältet?
4. Hur kör du något vid systemstart?
5. Varför ska man använda fullständig sökväg?
6. Hur loggar du output från cron-jobb?
""",
            "quiz": [
                {
                    "question": "Hur editerar du dina cron-jobb?",
                    "options": [
                        "cron --edit",
                        "crontab -e",
                        "edit cron",
                        "nano /etc/cron",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur skriver du 'varje dag kl 02:00'?",
                    "options": [
                        "2 0 * * *",
                        "0 2 * * *",
                        "* * 2 * *",
                        "0 0 2 * *",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad betyder */15 i minut-fältet?",
                    "options": [
                        "Vid minut 15",
                        "Var 15:e minut",
                        "15 minuter efter",
                        "Minut 1 och 5",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kör du något vid systemstart?",
                    "options": [
                        "0 0 0 0 0 /script.sh",
                        "@reboot /script.sh",
                        "boot /script.sh",
                        "startup /script.sh",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Varför ska man använda fullständig sökväg i cron?",
                    "options": [
                        "Det går snabbare",
                        "Cron har minimal PATH-miljö",
                        "Det är obligatoriskt",
                        "För säkerhetens skull",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur loggar du output från cron-jobb?",
                    "options": [
                        "/script.sh --log",
                        "/script.sh >> /var/log/fil.log 2>&1",
                        "/script.sh | log",
                        "cron --log /script.sh",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 19: Shell Scripting Fundamentals
        # ======================================================================
        {
            "title": "Shell Scripting Fundamentals",
            "slug": "shell-scripting-fundamentals",
            "description": "Grunderna i att skriva bash-skript.",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# 📜 Shell Scripting Fundamentals

> **TL;DR:** Börja med `#!/bin/bash`, variabler med `$`, if/for för logik, `chmod +x` för att köra.

---

## 🎯 Varför viktigt för DevOps?

- Automatisera repetitiva uppgifter
- Deploy-skript
- Backup-skript
- System-administration

---

## 🧭 Grundstruktur

```bash
#!/bin/bash
# Detta är en kommentar

echo "Hej från mitt skript!"
```

```bash
chmod +x script.sh              # Gör körbar
./script.sh                     # Kör
```

---

## 🧭 Variabler

```bash
# Sätta variabler (INGA mellanslag!)
namn="DevOps"
version=1

# Använda variabler
echo "Hej $namn"
echo "Version: ${version}"

# Läsa input
read -p "Ditt namn: " username
echo "Hej $username"
```

### Speciella variabler
| Variabel | Betydelse |
|----------|-----------|
| `$0` | Skriptnamn |
| `$1, $2...` | Argument 1, 2... |
| `$#` | Antal argument |
| `$@` | Alla argument |
| `$?` | Exit-kod från förra kommandot |
| `$$` | Process-ID |

---

## 🧭 If-satser

```bash
if [ "$1" == "start" ]; then
    echo "Startar..."
elif [ "$1" == "stop" ]; then
    echo "Stoppar..."
else
    echo "Användning: $0 start|stop"
fi
```

### Jämförelser
```bash
# Strängar
[ "$a" == "$b" ]        # Lika
[ "$a" != "$b" ]        # Olika
[ -z "$a" ]             # Tom sträng
[ -n "$a" ]             # Inte tom

# Tal
[ "$a" -eq "$b" ]       # ==
[ "$a" -ne "$b" ]       # !=
[ "$a" -lt "$b" ]       # <
[ "$a" -gt "$b" ]       # >

# Filer
[ -f "$fil" ]           # ⭐ Fil finns
[ -d "$mapp" ]          # ⭐ Mapp finns
[ -x "$fil" ]           # Körbar
```

---

## 🧭 Loopar

### For-loop
```bash
# Lista
for frukt in äpple banan citron; do
    echo "Frukt: $frukt"
done

# Filer
for fil in *.txt; do
    echo "Bearbetar $fil"
done

# Range
for i in {1..5}; do
    echo "Nummer: $i"
done
```

### While-loop
```bash
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

## 🧭 Funktioner

```bash
# Definiera
backup() {
    local source=$1
    local dest=$2
    tar -czvf "$dest" "$source"
    echo "Backup klar!"
}

# Anropa
backup /var/www backup.tar.gz
```

---

## 🧭 Exit-koder

```bash
# Kolla om kommando lyckades
if command; then
    echo "Lyckades"
else
    echo "Misslyckades"
fi

# Eller med $?
command
if [ $? -eq 0 ]; then
    echo "OK"
fi

# Avsluta med kod
exit 0      # Lyckat
exit 1      # Fel
```

---

## 🧭 Praktiskt exempel: Deploy-skript

```bash
#!/bin/bash
set -e  # Avbryt vid fel

APP_DIR="/var/www/myapp"
BACKUP_DIR="/var/backups"

echo "🚀 Startar deploy..."

# Backup
tar -czvf "$BACKUP_DIR/backup-$(date +%Y%m%d).tar.gz" "$APP_DIR"

# Pull nya ändringar
cd "$APP_DIR"
git pull origin main

# Installera dependencies
npm install

# Bygga
npm run build

# Starta om
sudo systemctl restart myapp

echo "✅ Deploy klar!"
```

---

## ⚡ Copy-paste lösningar

| Behov | Kod |
|-------|-----|
| Shebang | `#!/bin/bash` |
| Avbryt vid fel | `set -e` |
| Kolla om fil finns | `if [ -f "$fil" ]; then` |
| Kolla om mapp finns | `if [ -d "$mapp" ]; then` |
| Loop över filer | `for f in *.txt; do` |
| Läsa argument | `$1, $2, $3...` |
| Alla argument | `$@` |
| Exit vid fel | `exit 1` |

---

## 🧠 Kom ihåg

- `#!/bin/bash` = första raden
- `chmod +x` = gör körbar
- Inga mellanslag vid `=`
- `$variabel` eller `${variabel}`
- `set -e` = avbryt vid fel
- `$?` = förra kommandots exit-kod
- `[ -f fil ]` = finns filen?

---

## ✅ Checkpoint (Tenta)

1. Vad ska första raden i ett bash-skript vara?
2. Hur gör du ett skript körbart?
3. Hur kollar du om en fil finns?
4. Hur läser du första argumentet till skriptet?
5. Vad gör set -e?
6. Hur loopar du över alla .txt-filer?
""",
            "quiz": [
                {
                    "question": "Vad ska första raden i ett bash-skript vara?",
                    "options": [
                        "#/bash",
                        "#!/bin/bash",
                        "bash:",
                        "//bin/bash",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur gör du ett skript körbart?",
                    "options": [
                        "run script.sh",
                        "chmod +x script.sh",
                        "exec script.sh",
                        "enable script.sh",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kollar du om en fil finns i bash?",
                    "options": [
                        "if exists $fil",
                        'if [ -f "$fil" ]; then',
                        "if file $fil",
                        "if ($fil)",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur läser du första argumentet till skriptet?",
                    "options": [
                        "$0",
                        "$1",
                        "$arg1",
                        "args[0]",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad gör set -e i ett skript?",
                    "options": [
                        "Aktiverar echo",
                        "Avbryter vid första felet",
                        "Exporterar variabler",
                        "Aktiverar debugging",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur loopar du över alla .txt-filer?",
                    "options": [
                        "loop *.txt",
                        "for f in *.txt; do",
                        "foreach *.txt",
                        "while *.txt",
                    ],
                    "correct": 1,
                },
            ],
        },
        # ======================================================================
        # NODE 20: Troubleshooting & Debugging
        # ======================================================================
        {
            "title": "Troubleshooting & Debugging",
            "slug": "troubleshooting-debugging",
            "description": "Systematisk felsökning och debugging av Linux-system.",
            "difficulty": "easy",
            "estimated_minutes": 45,
            "xp_reward": 100,
            "content": """# 🔧 Troubleshooting & Debugging

> **TL;DR:** Systematisk felsökning: status → loggar → resurser → nätverk → config.

---

## 🎯 Varför viktigt för DevOps?

- Snabbt hitta och lösa problem
- Minimera nedtid
- Förstå vad som gick fel
- Lära sig av incidenter

---

## 🧭 Felsökningsmetodik

```
1. 🔍 Förstå problemet - vad fungerar inte?
2. 📊 Samla info - loggar, status, resurser
3. 🎯 Isolera - var är felet?
4. 🔧 Åtgärda - fixa problemet
5. ✅ Verifiera - fungerar det nu?
6. 📝 Dokumentera - vad lärde vi oss?
```

---

## 🧭 "Tjänsten fungerar inte"

```bash
# 1. Körs tjänsten?
systemctl status nginx

# 2. Försök starta
sudo systemctl start nginx

# 3. Kolla loggar
journalctl -u nginx --since "10 min ago"

# 4. Kolla config
sudo nginx -t                   # Testa config

# 5. Kolla portar
ss -tlnp | grep nginx
```

---

## 🧭 "Kan inte nå servern"

```bash
# 1. Har servern internet?
ping -c 4 8.8.8.8

# 2. Fungerar DNS?
dig google.com

# 3. Kan vi nå målet?
ping -c 4 server.com

# 4. Är porten öppen?
nc -zv server.com 80

# 5. Brandvägg?
sudo ufw status
sudo iptables -L

# 6. Svarar tjänsten?
curl -I http://server.com
```

---

## 🧭 "Servern är långsam"

```bash
# 1. System load
uptime

# 2. CPU-användning
htop
# eller
top -bn1 | head -20

# 3. Minne
free -h

# 4. Disk I/O
iostat
# eller
iotop

# 5. Vilken process tar resurser?
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
```

---

## 🧭 "Disk full"

```bash
# 1. Var är det fullt?
df -h

# 2. Hitta stora mappar
du -sh /* 2>/dev/null | sort -hr | head

# 3. Gå djupare
du -sh /var/* | sort -hr | head

# 4. Vanliga syndare
sudo journalctl --disk-usage
du -sh /var/log
du -sh /tmp

# 5. Rensa
sudo journalctl --vacuum-size=100M
sudo apt clean
```

---

## 🧭 "Process använder för mycket minne/CPU"

```bash
# Hitta processen
ps aux --sort=-%mem | head      # Mest minne
ps aux --sort=-%cpu | head      # Mest CPU

# Döda processen
kill PID                        # Snällt
kill -9 PID                     # Tvinga

# Döda efter namn
pkill processnamn
killall processnamn
```

---

## 🧭 "Kan inte logga in"

```bash
# SSH-problem
ssh -v user@server              # Verbose för debug

# Kolla SSH-tjänsten
systemctl status sshd

# Kolla brandvägg
sudo ufw status
# Se till port 22 är öppen

# Kolla authorized_keys
cat ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

---

## 🧭 Användbara debug-kommandon

```bash
# Systemloggar
journalctl -xe                  # Senaste errors
journalctl -f                   # Följ live
dmesg | tail                    # Kernel-meddelanden

# Nätverk
netstat -tlnp                   # Lyssnade portar
ss -tlnp                        # Samma (nyare)
lsof -i :80                     # Vem använder port 80?

# Filer
lsof +D /path                   # Öppna filer i mapp
strace -p PID                   # Spåra systemanrop
```

---

## ⚡ Copy-paste lösningar

| Problem | Första kommando |
|---------|-----------------|
| Tjänst fungerar inte | `systemctl status tjänst` |
| Kan inte nå server | `ping -c 4 server` |
| Server långsam | `htop` |
| Disk full | `df -h && du -sh /*` |
| Hitta process | `ps aux \\| grep namn` |
| Döda process | `kill PID` |
| Nätverksproblem | `ss -tlnp` |
| Se loggar | `journalctl -u tjänst -f` |

---

## 🧠 Kom ihåg

- Börja ALLTID med `systemctl status`
- Loggar berättar vad som gick fel: `journalctl -u tjänst`
- `htop` för resursövervakning
- `df -h` vid diskproblem
- `ss -tlnp` för nätverksportar
- `-v` för verbose på många kommandon
- Dokumentera vad du hittar!

---

## ✅ Checkpoint (Tenta)

1. Vad kollar du först när en tjänst inte fungerar?
2. Hur ser du de senaste loggarna för nginx?
3. Hur hittar du vilken process som tar mest minne?
4. Hur testar du om en port är öppen?
5. Vad gör du när disken är full?
6. Hur kollar du vilka portar som lyssnar?
""",
            "quiz": [
                {
                    "question": "Vad kollar du först när en tjänst inte fungerar?",
                    "options": [
                        "cat /var/log/syslog",
                        "systemctl status tjänst",
                        "ping tjänst",
                        "htop",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur ser du de senaste loggarna för nginx?",
                    "options": [
                        "cat /var/log/nginx",
                        "journalctl -u nginx",
                        "nginx --logs",
                        "logs nginx",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur hittar du vilken process som tar mest minne?",
                    "options": [
                        "memory --top",
                        "ps aux --sort=-%mem | head",
                        "top memory",
                        "mem -s",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur testar du om en port är öppen?",
                    "options": [
                        "port 80 server",
                        "nc -zv server 80",
                        "test port 80",
                        "ping server:80",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Vad gör du först när disken är full?",
                    "options": [
                        "rm -rf /",
                        "df -h för att se var",
                        "reboot",
                        "format disk",
                    ],
                    "correct": 1,
                },
                {
                    "question": "Hur kollar du vilka portar som lyssnar?",
                    "options": [
                        "ports --list",
                        "ss -tlnp",
                        "listen ports",
                        "show ports",
                    ],
                    "correct": 1,
                },
            ],
        },
    ],
    "groups": [
        {
            "id": "grundlaggande",
            "title": "Grundläggande",
            "subtitle": "Filhantering & Navigation",
            "icon": "FileText",
            "color": "from-emerald-500 to-teal-500",
            "bgGlow": "rgba(16, 185, 129, 0.2)",
            "taskIds": [
                "file-system-essentials",
                "text-processing-basics",
                "pipelines-redirection"
            ]
        },
        {
            "id": "natverk",
            "title": "Nätverk",
            "subtitle": "Nätverkskonfiguration & Diagnostik",
            "icon": "Network",
            "color": "from-cyan-500 to-blue-500",
            "bgGlow": "rgba(6, 182, 212, 0.2)",
            "taskIds": [
                "networking-fundamentals",
                "network-tools",
                "dns-resolution"
            ]
        },
        {
            "id": "sakerhet",
            "title": "Säkerhet",
            "subtitle": "Permissions & Brandväggar",
            "icon": "Shield",
            "color": "from-red-500 to-orange-500",
            "bgGlow": "rgba(239, 68, 68, 0.2)",
            "taskIds": [
                "permissions-ownership",
                "firewall-basics",
                "ssh-security"
            ]
        },
        {
            "id": "system",
            "title": "System",
            "subtitle": "Processhantering & Övervakning",
            "icon": "Settings",
            "color": "from-purple-500 to-violet-500",
            "bgGlow": "rgba(139, 92, 246, 0.2)",
            "taskIds": [
                "process-management",
                "systemd-services",
                "system-monitoring"
            ]
        },
        {
            "id": "automation",
            "title": "Automation",
            "subtitle": "Scripting & Cron Jobs",
            "icon": "Bot",
            "color": "from-amber-500 to-yellow-500",
            "bgGlow": "rgba(245, 158, 11, 0.2)",
            "taskIds": [
                "bash-scripting-basics",
                "cron-scheduling",
                "automation-patterns"
            ]
        },
        {
            "id": "produktivitet",
            "title": "Produktivitet",
            "subtitle": "Vim, Tmux & Verktyg",
            "icon": "Sparkles",
            "color": "from-pink-500 to-rose-500",
            "bgGlow": "rgba(236, 72, 153, 0.2)",
            "taskIds": [
                "vim-essentials",
                "tmux-multiplexing",
                "productivity-tools"
            ]
        }
    ],
}
