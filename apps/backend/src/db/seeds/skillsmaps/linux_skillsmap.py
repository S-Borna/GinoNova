"""
Linux SkillsMap - 20 Consolidated Nodes
Version: 1.0
Date: 2025-12-01

Pedagogical Style: Akhilesh (Intro → Concept → Commands → Pro Tips → Task)
Each node covers 5-10 related topics in depth.

Structure:
- 20 nodes total
- Each node: ~500-1000 lines of content
- Estimated time per node: 45-90 minutes
- XP per node: 50-100 based on difficulty
"""

from typing import Literal

DifficultyLevel = Literal["beginner", "intermediate", "advanced", "expert"]


# =============================================================================
# LINUX SKILLSMAP METADATA
# =============================================================================

LINUX_SKILLSMAP_INFO = {
    "name": "Linux Mastery",
    "slug": "linux-mastery",
    "description": "Complete Linux system administration - from processes to troubleshooting",
    "total_nodes": 20,
    "estimated_hours": 30,
    "difficulty_range": "beginner to advanced",
    "source": "Consolidated from roadmap.sh/linux (102 topics)",
}


# =============================================================================
# NODE 1: PROCESS MANAGEMENT
# =============================================================================

NODE_01_PROCESS_MANAGEMENT = {
    "node_id": 1,
    "title": "Process Management Mastery",
    "slug": "process-management",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 80,
    "topics_covered": [
        "ps", "top", "htop", "pstree", "kill", "killall", "pkill",
        "nice", "renice", "bg", "fg", "jobs", "nohup", "disown",
        "process states", "signals", "zombie processes", "orphan processes"
    ],
    "content": """# Process Management Mastery

## Varför detta är kritiskt

> "In production, processes are everything. An unresponsive process can bring down an entire service. A runaway process can exhaust server resources. A zombie process can fill your process table. You need to be the process whisperer."

Tänk dig: Det är fredag kväll. Monitoring larmar — CPU:n på din produktionsserver är på 100%. Användare klagar. Din chef ringer. Du har SSH-access men ingen aning om vilket process som orsakar problemet.

**Efter denna node vet du exakt vad du ska göra.**

---

## Vad är en process?

En process är ett körande program. Varje gång du startar ett kommando skapar Linux en ny process.

```
┌─────────────────────────────────────────────────────────────┐
│                        PROCESS                              │
├─────────────────────────────────────────────────────────────┤
│  PID: 1234              │  Unikt process-ID                │
│  PPID: 1                │  Parent process ID               │
│  UID: 1000              │  Användare som äger processen    │
│  State: R (Running)     │  Aktuellt tillstånd              │
│  CPU: 15%               │  Resursanvändning                │
│  MEM: 2.5%              │  Minnesanvändning                │
│  CMD: nginx             │  Kommandot som startade den      │
└─────────────────────────────────────────────────────────────┘
```

### Process States (tillstånd)

```
R - Running     : Processen kör just nu på CPU:n
S - Sleeping    : Väntar på något (I/O, signal)
D - Disk Sleep  : Uninterruptible sleep (väntar på disk)
Z - Zombie      : Avslutad men parent har inte rensat upp
T - Stopped     : Pausad (t.ex. med Ctrl+Z)
```

**Pro Tip:** `D`-state processer kan INTE dödas med `kill -9`. De väntar på hardware och kommer avsluta när I/O är klar (eller reboot krävs).

---

## Kommando 1: ps — Processlista

`ps` visar en snapshot av aktuella processer.

### Grundläggande användning

```bash
# Visa processer i current terminal
ps

# Visa ALLA processer på systemet (standard kombination)
ps aux

# Förklaring av aux:
# a = visa processer från alla användare
# u = user-orienterat format (visa ägare)
# x = visa processer utan kontrollterminaler
```

### Output förklarad

```bash
$ ps aux | head -5
USER       PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1   0.0  0.1 225652  9412 ?        Ss   Dec01   0:03 /sbin/init
root         2   0.0  0.0      0     0 ?        S    Dec01   0:00 [kthreadd]
root         3   0.0  0.0      0     0 ?        I<   Dec01   0:00 [rcu_gp]
www-data  1234  85.2  4.5 892632 45612 ?        R    10:32   5:23 php-fpm
```

| Kolumn | Betydelse |
|--------|-----------|
| USER | Processägare |
| PID | Process ID (unikt) |
| %CPU | CPU-användning |
| %MEM | Minnesanvändning |
| VSZ | Virtual memory size (KB) |
| RSS | Resident Set Size - faktiskt RAM (KB) |
| TTY | Terminal (? = ingen terminal) |
| STAT | State + modifiers |
| START | Starttid |
| TIME | Total CPU-tid |
| COMMAND | Kommandot |

### Praktiska ps-kommandon

```bash
# Hitta processer som äter mest CPU
ps aux --sort=-%cpu | head -10

# Hitta processer som äter mest minne
ps aux --sort=-%mem | head -10

# Hitta en specifik process
ps aux | grep nginx
# Bättre: undvik att matcha grep sig själv
ps aux | grep "[n]ginx"

# Visa processträd
ps auxf

# Visa bara PIDs för ett kommando
pgrep nginx

# Visa PID + kommando
pgrep -a nginx
```

---

## Kommando 2: top — Realtidsövervakning

`top` är den klassiska realtidsövervakaren. Den uppdateras automatiskt.

### Starta top

```bash
# Starta top
top

# Starta med specifik uppdateringsintervall (2 sekunder)
top -d 2

# Starta och visa bara processer för en användare
top -u www-data

# Starta i batch mode (för scripting)
top -b -n 1
```

### Interaktiva kommandon i top

| Tangent | Funktion |
|---------|----------|
| `q` | Avsluta |
| `h` | Hjälp |
| `k` | Döda process (frågar om PID och signal) |
| `r` | Renice (ändra prioritet) |
| `u` | Filtrera på användare |
| `M` | Sortera på minne |
| `P` | Sortera på CPU (default) |
| `c` | Visa full kommandorad |
| `1` | Visa alla CPU-kärnor separat |
| `z` | Färgläge |
| `<` / `>` | Byt sorteringskolumn |

### Förstå top-headern

```
top - 14:32:15 up 5 days,  3:21,  2 users,  load average: 0.52, 0.58, 0.59
Tasks: 256 total,   1 running, 254 sleeping,   0 stopped,   1 zombie
%Cpu(s):  2.3 us,  0.8 sy,  0.0 ni, 96.5 id,  0.3 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :  15921.3 total,   1234.5 free,   8765.4 used,   5921.4 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   6543.2 avail Mem
```

| Mått | Betydelse | Varningsnivå |
|------|-----------|--------------|
| load average | 1/5/15 min CPU-kö | > antal CPU-kärnor = problem |
| us (user) | Tid i user-mode | Hög = applikation arbetar |
| sy (system) | Tid i kernel-mode | Hög = mycket syscalls |
| wa (wait) | Tid att vänta på I/O | > 10% = disk är flaskhals |
| id (idle) | Ledig tid | Låg = CPU är upptagen |
| zombie | Zombie-processer | > 0 = investigate |

---

## Kommando 3: htop — Modern processvisare

`htop` är `top` på steroider. Mer visuell, enklare att använda.

### Installation

```bash
# Ubuntu/Debian
sudo apt install htop

# macOS
brew install htop

# RHEL/CentOS
sudo dnf install htop
```

### htop-fördelar över top

- Scrollbara processlistor
- Musklickbart
- Färgkodade resursmätare
- Trädvy inbyggd
- Enklare att döda/renice processer
- Bättre sökfunktion

### htop-tangenter

| Tangent | Funktion |
|---------|----------|
| `F1` | Hjälp |
| `F2` | Setup (anpassa) |
| `F3` | Sök |
| `F4` | Filter |
| `F5` | Trädvy |
| `F6` | Sortera |
| `F9` | Kill |
| `F10` | Avsluta |
| `Space` | Markera process |
| `U` | Unmarkera alla |

---

## Kommando 4: pstree — Processhierarki

`pstree` visar processer som ett träd — perfekt för att förstå parent-child-relationer.

```bash
# Grundläggande träd
pstree

# Med PIDs
pstree -p

# Visa bara träd för specifik användare
pstree www-data

# Visa träd för specifik process
pstree -p 1234

# Kompakt (slå ihop identiska processer)
pstree -c
```

### Output-exempel

```
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─dockerd───13*[{dockerd}]
        ├─nginx───nginx───2*[nginx]
        ├─sshd───sshd───sshd───bash───pstree
        └─systemd───(sd-pam)
```

**Pro Tip:** Om en process blir zombie, titta på dess parent (PPID) — det är parent som inte städar upp korrekt.

---

## Kill och Signals — Döda processer

### Signal-konceptet

Linux använder **signals** för att kommunicera med processer. En signal är ett meddelande som säger åt processen att göra något.

### Vanliga signals

```bash
# Lista alla signals
kill -l
```

| Signal | Nummer | Betydelse | Beteende |
|--------|--------|-----------|----------|
| SIGHUP | 1 | Hangup | Ofta: reload config |
| SIGINT | 2 | Interrupt (Ctrl+C) | Snäll avslutning |
| SIGQUIT | 3 | Quit | Avsluta med core dump |
| SIGKILL | 9 | Kill | **Tvingad omedelbar död** |
| SIGTERM | 15 | Terminate | Snäll "snälla dö nu" |
| SIGSTOP | 19 | Stop | Pausa processen |
| SIGCONT | 18 | Continue | Återuppta pausad |

### kill-kommandon

```bash
# Skicka SIGTERM (default) - snällt
kill 1234

# Skicka SIGTERM explicit
kill -15 1234
kill -TERM 1234

# Skicka SIGHUP (reload config)
kill -1 1234
kill -HUP 1234

# Skicka SIGKILL (tvingad död) - använd som sista utväg!
kill -9 1234
kill -KILL 1234
```

### killall och pkill

```bash
# Döda alla processer med namn
killall nginx

# Döda med mönster
pkill -f "python script.py"

# Döda processer äldre än 1 timme
pkill -o -u www-data php

# Döda alla processer för en användare (FARLIGT!)
pkill -u baduser
```

### Best Practice för att döda processer

```bash
# 1. Försök SIGTERM först (låt processen städa upp)
kill 1234

# 2. Vänta några sekunder
sleep 5

# 3. Kontrollera om den lever
ps -p 1234

# 4. Om den fortfarande lever, SIGKILL
kill -9 1234
```

**VARNING:** `kill -9` ger INTE processen chans att städa upp. Temporärfiler, halvskrivna filer, öppna connections kan bli korrupta. Använd endast som sista utväg!

---

## Process Priorities — nice & renice

### Förstå Nice-värden

Linux prioriterar processer med "nice"-värden:

```
-20 ←───────────────────────────────→ +19
HÖGST prioritet                LÄGST prioritet
(elak mot andra)               (snäll mot andra)

Default: 0
```

Bara root kan sätta negativa nice-värden (högre prioritet).

### nice — Starta med prioritet

```bash
# Starta process med lägre prioritet (snällare)
nice -n 10 ./backup.sh

# Starta med högre prioritet (kräver root)
sudo nice -n -5 ./important-job.sh

# Default nice (10)
nice ./my-script.sh
```

### renice — Ändra körande process

```bash
# Ändra prioritet för PID
renice 10 -p 1234

# Ändra prioritet för alla processer av en användare
renice 5 -u www-data

# Ändra till högre prioritet (kräver root)
sudo renice -5 -p 1234
```

### Praktiska exempel

```bash
# Backup-jobb ska inte störa produktion
nice -n 19 tar -czf backup.tar.gz /var/data/

# Kritisk databas behöver prioritet
sudo renice -10 -p $(pgrep postgres)
```

---

## Background & Foreground — Jobs Control

### Bakgrundsprocesser

```bash
# Starta i bakgrunden direkt
./long-running-script.sh &

# Flytta körande process till bakgrunden
./script.sh
# Tryck Ctrl+Z (pausar)
bg              # Fortsätter i bakgrunden

# Se bakgrundsjobb
jobs

# Flytta tillbaka till förgrunden
fg
fg %1           # Specifikt jobb nummer 1

# Döda bakgrundsjobb
kill %1
```

### nohup — Överlev logout

```bash
# Processen överlever om du loggar ut
nohup ./script.sh &

# Output går till nohup.out
# Eller specificera fil
nohup ./script.sh > output.log 2>&1 &
```

### disown — Koppla bort från shell

```bash
# Starta process
./script.sh &

# Koppla bort så den överlever shell-death
disown %1

# Eller disown direkt
disown -h %1    # Håll igång men ignorera HUP
```

---

## Zombie och Orphan Processer

### Zombie Process

En **zombie** är en process som har avslutats men vars parent inte har läst dess exit-status.

```bash
# Hitta zombies
ps aux | awk '$8 == "Z"'

# Eller
ps aux | grep defunct
```

**Kan du döda en zombie?** NEJ. Den är redan död! Du måste:
1. Döda parent-processen (så init tar över och städar)
2. Eller vänta på att parent ska göra wait()

### Orphan Process

En **orphan** är en process vars parent har dött. Den adopteras automatiskt av PID 1 (systemd/init).

---

## Felsökning: Praktiska Scenarion

### Scenario 1: Hög CPU

```bash
# 1. Hitta CPU-tjuven
top -o %CPU
# eller
ps aux --sort=-%cpu | head -5

# 2. Identifiera processen
ps -p 1234 -o pid,ppid,user,cmd

# 3. Beslut:
#    - Är det legitimt arbete? Vänta.
#    - Är det en bugg? Kill.
#    - Är det onödigt? Nice ner eller kill.
```

### Scenario 2: Hög minnesanvändning

```bash
# 1. Hitta minnesslukaren
ps aux --sort=-%mem | head -5

# 2. Se detaljerad minnesinfo
pmap -x 1234 | tail -5

# 3. Beslut:
#    - Memory leak? Starta om processen.
#    - Legitim användning? Lägg till mer RAM.
```

### Scenario 3: Process svarar inte

```bash
# 1. Kontrollera state
ps -o pid,stat,cmd -p 1234

# 2. Om D-state (disk sleep):
#    - Vänta. Du kan inte döda den.
#    - Kontrollera disk: dmesg | tail

# 3. Om annan state:
#    - Försök SIGTERM först
kill 1234
sleep 5
#    - Om den lever, SIGKILL
kill -9 1234
```

---

## Praktisk Övning

### Uppgift 1: Process Explorer

```bash
# 1. Öppna två terminaler

# Terminal 1: Starta en CPU-intensiv process
yes > /dev/null &
YESPID=$!
echo "PID: $YESPID"

# Terminal 2: Övervaka
top -p $YESPID

# 3. Ändra prioritet (Terminal 1)
renice 15 -p $YESPID

# 4. Observera förändringen i top

# 5. Döda processen
kill $YESPID
```

### Uppgift 2: Background Jobs

```bash
# 1. Starta långkörande process
sleep 300 &
sleep 600 &
sleep 900 &

# 2. Lista jobb
jobs

# 3. Flytta ett till förgrunden
fg %2

# 4. Pausa det (Ctrl+Z)

# 5. Flytta tillbaka till bakgrunden
bg

# 6. Döda alla
kill %1 %2 %3
```

### Uppgift 3: Hitta och döda

```bash
# 1. Starta 3 sleep-processer
for i in {1..3}; do sleep 1000 & done

# 2. Hitta dem med pgrep
pgrep sleep

# 3. Döda dem alla
pkill sleep

# 4. Verifiera
pgrep sleep  # Ska vara tom
```

---

## Sammanfattning

| Verktyg | Användning |
|---------|------------|
| `ps aux` | Snapshot av alla processer |
| `top` | Realtidsövervakning (klassisk) |
| `htop` | Realtidsövervakning (modern) |
| `pstree` | Processhierarki |
| `pgrep` | Hitta PID med mönster |
| `kill` | Skicka signal till PID |
| `killall` | Döda med namn |
| `pkill` | Döda med mönster |
| `nice` | Starta med prioritet |
| `renice` | Ändra prioritet |
| `jobs` | Lista bakgrundsjobb |
| `bg/fg` | Flytta jobb mellan bg/fg |
| `nohup` | Överlev logout |
| `disown` | Koppla bort från shell |

---

## Nästa Steg

Du har nu full kontroll över Linux-processer. Nästa node: **File System Navigation** — lär dig navigera filsystemet som en expert.
"""
}


# =============================================================================
# NODE 2: FILE SYSTEM NAVIGATION
# =============================================================================

NODE_02_FILE_SYSTEM_NAVIGATION = {
    "node_id": 2,
    "title": "File System Navigation",
    "slug": "file-system-navigation",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 60,
    "topics_covered": [
        "cd", "ls", "pwd", "tree", "find", "locate", "which", "whereis",
        "file", "stat", "FHS", "directory structure", "absolute vs relative paths"
    ],
    "content": """# File System Navigation

## Varför detta är kritiskt

> "The Linux file system is not just folders and files — it's the operating system's central nervous system. Every configuration, every log, every program lives in a predictable location. Master the filesystem, and you master Linux."

---

## FHS — Filesystem Hierarchy Standard

Linux följer FHS (Filesystem Hierarchy Standard). Alla distros har samma grundstruktur:

```
/
├── bin/        → Essential binaries (ls, cp, mv)
├── boot/       → Boot files, kernel
├── dev/        → Device files
├── etc/        → Configuration files (etcetera)
├── home/       → User home directories
├── lib/        → Shared libraries
├── media/      → Removable media mount points
├── mnt/        → Temporary mount points
├── opt/        → Optional/third-party software
├── proc/       → Virtual filesystem for processes
├── root/       → Root user's home
├── run/        → Runtime data
├── sbin/       → System binaries (admin commands)
├── srv/        → Service data
├── sys/        → Virtual filesystem for kernel
├── tmp/        → Temporary files
├── usr/        → User programs and data
│   ├── bin/    → User binaries
│   ├── lib/    → User libraries
│   ├── local/  → Locally installed software
│   └── share/  → Shared data (docs, icons)
└── var/        → Variable data (logs, caches)
    ├── log/    → Log files
    ├── cache/  → Application caches
    └── www/    → Web server files
```

### DevOps-kritiska directories

| Directory | Vad du hittar där | Varför det spelar roll |
|-----------|-------------------|------------------------|
| `/etc` | Konfiguration | Alla app-configs |
| `/var/log` | Loggar | Debugging, monitoring |
| `/tmp` | Temp-filer | Rensar vid reboot |
| `/opt` | Third-party apps | Docker, custom apps |
| `/home` | Användardata | Backup target |

---

## Grundläggande Navigation

### pwd — Print Working Directory

```bash
# Var är jag?
pwd
# /home/username

# Alltid absolut sökväg
```

### cd — Change Directory

```bash
# Gå till specifik katalog
cd /var/log

# Gå hem
cd          # eller
cd ~        # eller
cd $HOME

# Gå till föregående katalog
cd -

# Gå upp ett steg
cd ..

# Gå upp två steg
cd ../..

# Relativ vs absolut
cd documents        # Relativ (från nuvarande position)
cd /home/user/documents  # Absolut (från root)
```

**Pro Tip:** Tab-completion fungerar med `cd`. Skriv första bokstäverna och tryck Tab!

### ls — List Directory Contents

```bash
# Grundläggande
ls

# Alla filer (inklusive dolda)
ls -a

# Long format (detaljer)
ls -l

# Human-readable storlekar
ls -lh

# Sortera på tid (nyast först)
ls -lt

# Sortera på storlek (störst först)
ls -lS

# Rekursiv (alla subdirectories)
ls -R

# Kombinera vanliga flaggor
ls -lah
```

### Förstå ls -l output

```
-rw-r--r-- 1 user group 4.0K Dec  1 10:30 file.txt
│├──┼──┼──┤ │  │    │     │      │         │
││  │  │  │ │  │    │     │      │         └── Filename
││  │  │  │ │  │    │     │      └── Modification time
││  │  │  │ │  │    │     └── Size
││  │  │  │ │  │    └── Group owner
││  │  │  │ │  └── User owner
││  │  │  │ └── Hard link count
││  │  │  └── Others permissions (r-x)
││  │  └── Group permissions (r-x)
││  └── User permissions (rwx)
│└── File type (- = file, d = dir, l = link)
```

---

## Avancerad Navigation

### tree — Visa katalogstruktur

```bash
# Installation
sudo apt install tree    # Ubuntu/Debian
brew install tree        # macOS

# Grundläggande
tree

# Begränsa djup
tree -L 2

# Visa bara directories
tree -d

# Inkludera dolda filer
tree -a

# Visa storlekar
tree -sh

# Ignorera mönster
tree -I "node_modules|.git"
```

### find — Hitta filer

`find` är det mest kraftfulla sökverktyget.

```bash
# Grundläggande syntax
find [path] [options] [expression]

# Hitta fil med exakt namn
find /home -name "config.yaml"

# Case-insensitive
find /home -iname "config.yaml"

# Hitta kataloger
find /var -type d -name "log"

# Hitta filer
find /var -type f -name "*.log"

# Hitta filer större än 100MB
find / -type f -size +100M

# Hitta filer ändrade senaste 24h
find /var/log -mtime -1

# Hitta filer äldre än 30 dagar
find /tmp -mtime +30

# Hitta och radera (FÖRSIKTIGT!)
find /tmp -type f -mtime +30 -delete

# Hitta och kör kommando
find /var/log -name "*.log" -exec ls -lh {} \\;

# Hitta med permissions
find / -perm 777 -type f
```

### locate — Snabb sökning

`locate` använder en databas och är mycket snabbare än `find`.

```bash
# Installation
sudo apt install mlocate    # Ubuntu/Debian

# Uppdatera databasen
sudo updatedb

# Sök
locate nginx.conf

# Case-insensitive
locate -i NGINX.CONF

# Begränsa antal resultat
locate -n 10 nginx
```

**find vs locate:**
- `find`: Sök live i filsystemet, långsam men alltid aktuell
- `locate`: Sök i databas, snabb men kan vara föråldrad

---

## Hitta kommandon

### which — Hitta körbar fil

```bash
# Var ligger python?
which python
# /usr/bin/python

# Alla matchningar
which -a python
```

### whereis — Hitta binär, source, man

```bash
whereis nginx
# nginx: /usr/sbin/nginx /usr/share/nginx /usr/share/man/man8/nginx.8.gz
```

### type — Vad är kommandot?

```bash
type ls
# ls is aliased to `ls --color=auto'

type cd
# cd is a shell builtin

type find
# find is /usr/bin/find
```

---

## Fil-information

### file — Identifiera filtyp

```bash
file /bin/ls
# /bin/ls: ELF 64-bit LSB pie executable...

file /etc/passwd
# /etc/passwd: ASCII text

file image.jpg
# image.jpg: JPEG image data...

file mystery_file
# mystery_file: gzip compressed data...
```

### stat — Detaljerad fil-metadata

```bash
stat file.txt
#   File: file.txt
#   Size: 4096       Blocks: 8          IO Block: 4096   regular file
# Device: 802h/2050d Inode: 1234567     Links: 1
# Access: (0644/-rw-r--r--)  Uid: ( 1000/user)   Gid: ( 1000/user)
# Access: 2025-12-01 10:30:00
# Modify: 2025-12-01 09:15:00
# Change: 2025-12-01 09:15:00
#  Birth: -
```

| Tidsstämpel | Betydelse |
|-------------|-----------|
| Access (atime) | Senast läst |
| Modify (mtime) | Senast ändrad (innehåll) |
| Change (ctime) | Senast ändrad (metadata) |

---

## Praktiska Övningar

### Övning 1: Utforska systemet

```bash
# 1. Gå till rotkatalogen
cd /

# 2. Lista alla top-level directories
ls -l

# 3. Hitta alla .conf-filer i /etc
find /etc -name "*.conf" 2>/dev/null | head -20

# 4. Visa träd för /etc med max 2 nivåer
tree -L 2 /etc
```

### Övning 2: Hitta stora filer

```bash
# 1. Hitta filer större än 50MB
find / -type f -size +50M 2>/dev/null

# 2. Hitta de 10 största filerna
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -10
```

### Övning 3: Navigation efficiency

```bash
# 1. Skapa alias för vanliga directories
echo 'alias logs="cd /var/log"' >> ~/.bashrc
echo 'alias etc="cd /etc"' >> ~/.bashrc
source ~/.bashrc

# 2. Nu kan du bara skriva:
logs    # → går till /var/log
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `pwd` | Visa nuvarande katalog |
| `cd` | Byt katalog |
| `ls` | Lista innehåll |
| `tree` | Visa katalogträd |
| `find` | Sök filer live |
| `locate` | Snabbsök i databas |
| `which` | Hitta körbar |
| `whereis` | Hitta bin/source/man |
| `file` | Identifiera filtyp |
| `stat` | Detaljerad metadata |

---

## Nästa Steg

Du kan nu navigera Linux-filsystemet effektivt. Nästa node: **File Operations** — lär dig manipulera filer och kataloger.
"""
}


# =============================================================================
# ALL NODES COLLECTION
# =============================================================================

LINUX_SKILLSMAP_NODES = [
    NODE_01_PROCESS_MANAGEMENT,
    NODE_02_FILE_SYSTEM_NAVIGATION,
    # NODE_03_FILE_OPERATIONS (to be added)
    # NODE_04_FILE_PERMISSIONS (to be added)
    # ... up to NODE_20
]


# =============================================================================
# HELPER FUNCTION
# =============================================================================

def get_linux_skillsmap_summary():
    """Return summary of Linux SkillsMap progress."""
    total_nodes = 20
    completed_nodes = len(LINUX_SKILLSMAP_NODES)
    return {
        "name": LINUX_SKILLSMAP_INFO["name"],
        "total_nodes": total_nodes,
        "completed_nodes": completed_nodes,
        "progress_percent": (completed_nodes / total_nodes) * 100,
        "remaining_nodes": total_nodes - completed_nodes,
    }


if __name__ == "__main__":
    summary = get_linux_skillsmap_summary()
    print(f"Linux SkillsMap: {summary['completed_nodes']}/{summary['total_nodes']} nodes ({summary['progress_percent']:.0f}%)")
