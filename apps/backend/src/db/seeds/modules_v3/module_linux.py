"""
Linux Mastery - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: foundation
Tasks: 40
Estimated Hours: 30
"""

MODULE_LINUX_MASTERY = {
    "track_slug": "foundation",
    "order_index": 100,
    "name": "Linux Mastery",
    "slug": "linux-mastery",
    "description": """Complete Linux system administration - from processes to troubleshooting""",
    "difficulty": "intermediate",
    "estimated_hours": 30,
    "prerequisites": [],
    "tasks": [
            {
                "title": "Process Management Mastery",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 80,
                "content": r"""# Process Management Mastery

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
            },
            {
                "title": "File System Navigation",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 60,
                "content": r"""# File System Navigation

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
find /var/log -name "*.log" -exec ls -lh {} \;

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
            },
            {
                "title": "File Operations Mastery",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 70,
                "content": r"""# File Operations Mastery

## Varför detta är kritiskt

> "Every deployment, every backup, every configuration change involves file operations. One wrong `rm -rf` can end careers. One missing `-p` in mkdir can break a deployment. Master these commands — they're your daily bread."

---

## Skapa filer och kataloger

### touch — Skapa tomma filer / Uppdatera tidsstämpel

```bash
# Skapa en tom fil
touch newfile.txt

# Skapa flera filer
touch file1.txt file2.txt file3.txt

# Uppdatera tidsstämpel på befintlig fil
touch existing_file.txt

# Sätt specifik tidsstämpel
touch -t 202512011200 file.txt    # ÅÅÅÅMMDDTTMM

# Använd annan fils tidsstämpel
touch -r reference.txt target.txt
```

**Pro Tip:** `touch` skapar INTE filen om den inte existerar och du använder `-c`:
```bash
touch -c maybe_exists.txt   # Skapar INTE om den inte finns
```

### mkdir — Skapa kataloger

```bash
# Skapa en katalog
mkdir projects

# Skapa med mellanliggande kataloger (-p = parents)
mkdir -p projects/webapp/src/components

# Skapa flera kataloger
mkdir dir1 dir2 dir3

# Skapa med specifika permissions
mkdir -m 755 secure_folder

# Verbose (visa vad som skapas)
mkdir -pv deep/nested/structure
```

**KRITISKT:** Alltid använd `-p` i scripts! Utan det misslyckas kommandot om parent inte finns.

```bash
# Script-safe pattern:
mkdir -p /var/log/myapp
mkdir -p /etc/myapp/conf.d
```

---

## Kopiera filer

### cp — Copy

```bash
# Kopiera fil
cp source.txt destination.txt

# Kopiera till katalog
cp file.txt /path/to/directory/

# Kopiera flera filer till katalog
cp file1.txt file2.txt /destination/

# Kopiera katalog rekursivt (-r = recursive)
cp -r source_dir/ destination_dir/

# Bevara alla attribut (-a = archive, bäst för backups)
cp -a source_dir/ backup_dir/

# Interactive (fråga innan överskrivning)
cp -i file.txt /destination/

# Force (skriv över utan att fråga)
cp -f file.txt /destination/

# Verbose
cp -v file.txt /destination/

# Uppdatera bara om source är nyare
cp -u source.txt destination.txt
```

### Vanliga cp-kombinationer

```bash
# Backup-stil kopiering (bevarar allt)
cp -av /source/ /backup/

# Säker kopiering (frågar)
cp -iv important.txt /archive/

# Deployment-kopiering (uppdatera bara ändrade)
cp -ruv ./dist/* /var/www/html/
```

**Viktigt om trailing slash:**
```bash
cp -r folder /dest/       # Kopierar folder TILL dest → /dest/folder/
cp -r folder/ /dest/      # Kopierar INNEHÅLLET i folder → /dest/*
```

---

## Flytta och byt namn

### mv — Move / Rename

```bash
# Byt namn på fil
mv oldname.txt newname.txt

# Flytta till katalog
mv file.txt /path/to/directory/

# Flytta och byt namn
mv file.txt /path/to/directory/newname.txt

# Flytta flera filer
mv file1.txt file2.txt /destination/

# Flytta katalog
mv source_dir/ /new/location/

# Interactive
mv -i file.txt /destination/

# Force
mv -f file.txt /destination/

# Backup before overwrite
mv -b file.txt /destination/    # Skapar file.txt~

# Verbose
mv -v file.txt /destination/
```

**Pro Tip:** `mv` är atomiskt på samma filsystem — det ändrar bara metadata, inte data. Perfekt för:
```bash
# Atomisk deploy
mv /tmp/new_config.yaml /etc/app/config.yaml
```

---

## Ta bort filer och kataloger

### rm — Remove (FARLIGT!)

```bash
# Ta bort fil
rm file.txt

# Ta bort flera filer
rm file1.txt file2.txt file3.txt

# Ta bort med wildcard
rm *.log

# Ta bort katalog rekursivt (-r = recursive)
rm -r directory/

# Force (ingen fråga, ignorera icke-existerande)
rm -f file.txt

# Den FARLIGA kombinationen
rm -rf directory/          # Tar bort ALLT utan att fråga

# Interactive (säkrare)
rm -i file.txt             # Frågar för varje fil

# Interactive för mer än 3 filer
rm -I *.txt

# Verbose
rm -v file.txt
```

### ⚠️ rm -rf VARNINGAR

```bash
# ALDRIG gör detta:
rm -rf /                   # Tar bort ALLT (root protection finns nu)
rm -rf /*                  # Tar bort allt i root
rm -rf $UNDEFINED_VAR/*    # Om variabeln är tom = rm -rf /*

# SÄKRA MÖNSTER:
# Alltid använd fullständig path:
rm -rf /var/log/myapp/temp/*

# Dubbelkolla variabler:
[ -n "$DIR" ] && rm -rf "$DIR"/*

# Eller använd :? för att fånga tom variabel
rm -rf "${DIR:?Variable not set}"/*
```

### rmdir — Ta bort tomma kataloger

```bash
# Ta bort tom katalog
rmdir empty_directory/

# Ta bort parent directories om tomma
rmdir -p path/to/empty/dirs/
```

---

## Länkar (Hard & Soft)

### Förstå Inodes

```
┌─────────────────────────────────────────────────────────────┐
│                    INODE (metadata)                         │
├─────────────────────────────────────────────────────────────┤
│  Inode #: 12345                                            │
│  Type: regular file                                        │
│  Permissions: -rw-r--r--                                   │
│  Owner: user                                               │
│  Size: 4096 bytes                                          │
│  Pointers to data blocks: [block1, block2, ...]            │
└─────────────────────────────────────────────────────────────┘
           │                          │
           │                          │
    ┌──────┴──────┐            ┌──────┴──────┐
    │  file.txt   │            │  link.txt   │
    │  (filename) │            │ (hard link) │
    └─────────────┘            └─────────────┘
```

### Hard Links

Ett hard link är ett ANNAT NAMN för samma inode (samma data).

```bash
# Skapa hard link
ln original.txt hardlink.txt

# Verifiera (samma inode nummer)
ls -li original.txt hardlink.txt
# 12345 -rw-r--r-- 2 user group 100 Dec 1 original.txt
# 12345 -rw-r--r-- 2 user group 100 Dec 1 hardlink.txt
#   ^                ^
#   Samma inode     Link count = 2
```

**Hard link egenskaper:**
- Delar samma inode → exakt samma data
- Om du raderar originalet finns datan kvar (så länge en link finns)
- Kan INTE korsa filsystem
- Kan INTE länka till kataloger (undantag: . och ..)

### Soft Links (Symlinks)

Ett soft link är en PEKARE till ett filnamn (som Windows-genvägar).

```bash
# Skapa symlink
ln -s /path/to/original.txt symlink.txt

# Skapa symlink med relativ path
ln -s ../config/app.yaml current_config.yaml

# Skapa symlink till katalog
ln -s /var/log/nginx logs

# Verifiera
ls -l symlink.txt
# lrwxrwxrwx 1 user group 20 Dec 1 symlink.txt -> /path/to/original.txt
```

**Soft link egenskaper:**
- Pekar på ett FILNAMN, inte inode
- Kan korsa filsystem
- Kan länka till kataloger
- Blir "broken" om target raderas

### Praktiska symlink-mönster

```bash
# Versionshantering med symlinks
ln -s myapp-1.2.3 myapp-current
# Uppgradera:
ln -sfn myapp-1.2.4 myapp-current   # -n = no-dereference for dirs

# Config-hantering
ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/

# Snabbåtkomst
ln -s /var/log/application logs
```

---

## Avancerade operationer

### dd — Disk/Data Duplicator

`dd` kopierar data på låg nivå. Kraftfullt men farligt.

```bash
# Skapa fil med specifik storlek
dd if=/dev/zero of=testfile bs=1M count=100
# 100 MB fil fylld med nollor

# Skapa ISO från CD
dd if=/dev/cdrom of=backup.iso

# Klona hel disk (FÖRSIKTIGT!)
dd if=/dev/sda of=/dev/sdb bs=64K status=progress

# Wipe disk (DESTRUKTIVT!)
dd if=/dev/zero of=/dev/sda bs=1M status=progress
```

**dd parametrar:**
- `if=` : Input file
- `of=` : Output file
- `bs=` : Block size
- `count=` : Antal block
- `status=progress` : Visa progress

---

## Praktiska Övningar

### Övning 1: Katalogstruktur

```bash
# 1. Skapa projektstruktur
mkdir -p myproject/{src,tests,docs,config}
touch myproject/src/main.py
touch myproject/tests/test_main.py
touch myproject/README.md

# 2. Verifiera
tree myproject/

# 3. Kopiera hela strukturen
cp -a myproject/ myproject_backup/
```

### Övning 2: Symlinks

```bash
# 1. Skapa versioner
mkdir -p versions/app-{1.0,1.1,1.2}
echo "v1.0" > versions/app-1.0/version.txt
echo "v1.1" > versions/app-1.1/version.txt
echo "v1.2" > versions/app-1.2/version.txt

# 2. Skapa current symlink
ln -s app-1.2 versions/current

# 3. Läs version
cat versions/current/version.txt

# 4. "Uppgradera" till ny version
ln -sfn app-1.1 versions/current
cat versions/current/version.txt
```

### Övning 3: Säker rensning

```bash
# Skapa testfiler
mkdir -p /tmp/cleanup_test
touch /tmp/cleanup_test/file{1..10}.log
touch /tmp/cleanup_test/keep.txt

# Säker rensning (bara .log filer)
find /tmp/cleanup_test -name "*.log" -type f -delete

# Verifiera
ls /tmp/cleanup_test/
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `touch` | Skapa tom fil / uppdatera tidsstämpel |
| `mkdir -p` | Skapa katalog(er) |
| `cp -a` | Kopiera (archive mode) |
| `mv` | Flytta / byt namn |
| `rm -rf` | Ta bort rekursivt (VARNING!) |
| `ln` | Skapa hard link |
| `ln -s` | Skapa soft link (symlink) |
| `dd` | Lågnivå-kopiering |

---

## Nästa Steg

Du kan nu manipulera filer som ett proffs. Nästa node: **File Permissions** — kontrollera vem som får göra vad med dina filer.
"""
            },
            {
                "title": "File Permissions Deep Dive",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# File Permissions Deep Dive

## Varför detta är kritiskt

> "Permissions are the first line of defense. A misconfigured permission can expose sensitive data, allow unauthorized access, or break your entire application. In security audits, permissions are always checked first."

---

## Förstå Permission-modellen

### Tre kategorier

```
┌──────────────────────────────────────────────────────────────┐
│                    FILE PERMISSIONS                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   OWNER (u)          GROUP (g)         OTHERS (o)           │
│   ─────────          ─────────         ──────────           │
│   Användaren som     Alla användare    Alla andra           │
│   äger filen         i filens grupp    på systemet          │
│                                                              │
│   rwx                rwx               rwx                   │
│   ─┬─                ─┬─               ─┬─                   │
│    │                  │                 │                    │
│    ├─ r = read (läs)  │                 │                    │
│    ├─ w = write       │                 │                    │
│    └─ x = execute     │                 │                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Tolka permissions

```bash
-rwxr-xr-- 1 user group 4096 Dec 1 10:30 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └── Others: r-- (read only)
│ │  └───── Group:  r-x (read + execute)
│ └──────── Owner:  rwx (read + write + execute)
└────────── Type:   - (regular file)

File types:
-  = regular file
d  = directory
l  = symbolic link
c  = character device
b  = block device
s  = socket
p  = named pipe (FIFO)
```

### Vad betyder permissions för...

**Filer:**
| Permission | Betydelse |
|------------|-----------|
| r (read) | Läsa filinnehåll |
| w (write) | Ändra filinnehåll |
| x (execute) | Köra som program |

**Kataloger:**
| Permission | Betydelse |
|------------|-----------|
| r (read) | Lista innehåll (ls) |
| w (write) | Skapa/ta bort filer i katalogen |
| x (execute) | Gå in i katalogen (cd) |

**Pro Tip:** För kataloger är `x` kritiskt — utan det kan du inte ens läsa filer inuti!

---

## chmod — Ändra permissions

### Symboliskt läge

```bash
# Syntax: chmod [who][operation][permission] file

# Who: u (user/owner), g (group), o (others), a (all)
# Operation: + (add), - (remove), = (set exactly)
# Permission: r, w, x

# Lägg till execute för owner
chmod u+x script.sh

# Ta bort write för others
chmod o-w file.txt

# Sätt exakt permissions för group
chmod g=rx file.txt

# Kombinera
chmod u+x,g-w,o-rwx file.txt

# Alla får läsa
chmod a+r file.txt

# Kopiera permissions från user till group
chmod g=u file.txt
```

### Numeriskt (oktalt) läge

```
r = 4
w = 2
x = 1

Kombinera genom addition:
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
--- = 0+0+0 = 0
```

```bash
# chmod [owner][group][others] file

# rwxr-xr-x
chmod 755 script.sh

# rw-r--r--
chmod 644 document.txt

# rw-------
chmod 600 private.key

# rwxrwxrwx (ALDRIG gör detta på produktion)
chmod 777 file.txt
```

### Vanliga permission-kombinationer

| Oktalt | Symboliskt | Användning |
|--------|------------|------------|
| 755 | rwxr-xr-x | Scripts, directories |
| 644 | rw-r--r-- | Vanliga filer |
| 600 | rw------- | SSH-nycklar, secrets |
| 700 | rwx------ | Privata scripts |
| 750 | rwxr-x--- | Group-delade scripts |
| 664 | rw-rw-r-- | Team-delade filer |
| 775 | rwxrwxr-x | Team-delade directories |

### Rekursiv chmod

```bash
# Ändra allt i katalog
chmod -R 755 directory/

# Men det sätter 755 på BÅDE filer och kataloger!
# Bättre: Separera filer och kataloger
find /path -type d -exec chmod 755 {} \;
find /path -type f -exec chmod 644 {} \;
```

---

## chown — Ändra ägare

```bash
# Ändra owner
chown newuser file.txt

# Ändra owner och group
chown newuser:newgroup file.txt

# Ändra bara group
chown :newgroup file.txt
# eller
chgrp newgroup file.txt

# Rekursiv
chown -R www-data:www-data /var/www/

# Bevara symboliska länkar (ändra inte target)
chown -h user:group symlink
```

### Praktiska exempel

```bash
# Web server files
sudo chown -R www-data:www-data /var/www/html/

# App deployment
sudo chown -R deploy:deploy /opt/myapp/

# SSH keys
chown $USER:$USER ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
```

---

## umask — Default permissions

`umask` definierar vilka permissions som SUBTRAHERAS från default.

```bash
# Default:
# Filer: 666 (rw-rw-rw-)
# Kataloger: 777 (rwxrwxrwx)

# Om umask = 022:
# Filer: 666 - 022 = 644 (rw-r--r--)
# Kataloger: 777 - 022 = 755 (rwxr-xr-x)

# Visa nuvarande umask
umask

# Sätt umask
umask 022    # Standard
umask 077    # Strikt (bara owner)
umask 002    # Tillåt group write

# Visa i symboliskt format
umask -S
```

### Permanent umask

```bash
# I ~/.bashrc eller ~/.profile:
umask 027    # Owner: full, Group: rx, Others: inget
```

---

## Special Permissions

### Setuid (SUID)

När en fil med setuid körs, körs den med ÄGARENS rättigheter.

```bash
# Exempel: passwd kan ändra /etc/shadow trots att du inte är root
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#    ^
#    s = setuid är satt

# Sätt setuid
chmod u+s executable
chmod 4755 executable

# Ta bort
chmod u-s executable
```

### Setgid (SGID)

På filer: Körs med gruppens rättigheter.
På kataloger: Nya filer ärver katalogengruppens grupp.

```bash
# På katalog - nya filer får samma grupp
chmod g+s /shared/project/
chmod 2775 /shared/project/

# Verifiera
ls -ld /shared/project/
# drwxrwsr-x 2 user devteam ... /shared/project/
#       ^
#       s = setgid

# Nya filer i denna katalog:
touch /shared/project/newfile
ls -l /shared/project/newfile
# -rw-rw-r-- 1 user devteam ... newfile
#                   ^^^^^^^
#                   Ärvd grupp!
```

### Sticky Bit

På kataloger: Bara ägaren kan radera sina egna filer (även om andra har write).

```bash
# /tmp har sticky bit
ls -ld /tmp
# drwxrwxrwt 15 root root ... /tmp
#          ^
#          t = sticky bit

# Sätt sticky bit
chmod +t /shared/
chmod 1777 /shared/
```

### Sammanfattning special permissions

| Oktalt prefix | Symboliskt | På fil | På katalog |
|---------------|------------|--------|------------|
| 4xxx | u+s | SUID - kör som ägare | (ovanligt) |
| 2xxx | g+s | SGID - kör som grupp | Nya filer ärver grupp |
| 1xxx | +t | (ovanligt) | Sticky - bara ägare raderar |

```bash
# Kombinera: SGID + Sticky
chmod 3775 /shared/

# Full special: SUID + SGID + Sticky
chmod 7755 file   # Ovanligt och ofta osäkert
```

---

## ACL (Access Control Lists)

Standard permissions är ibland inte nog. ACLs ger finare kontroll.

### Se ACLs

```bash
# Kontrollera om ACLs finns
ls -l file.txt
# -rw-rw-r--+ 1 user group ...
#           ^
#           + = ACLs finns

# Visa ACLs
getfacl file.txt
```

### Sätt ACLs

```bash
# Installation (om behövs)
sudo apt install acl

# Ge specifik användare access
setfacl -m u:anna:rwx file.txt

# Ge specifik grupp access
setfacl -m g:developers:rx file.txt

# Default ACL för katalog (ärvs av nya filer)
setfacl -d -m u:anna:rwx /shared/

# Ta bort ACL
setfacl -x u:anna file.txt

# Ta bort ALLA ACLs
setfacl -b file.txt
```

---

## Praktiska Övningar

### Övning 1: Web server permissions

```bash
# Skapa struktur
sudo mkdir -p /var/www/mysite
sudo chown -R www-data:www-data /var/www/mysite

# Sätt permissions
sudo chmod -R 755 /var/www/mysite
sudo find /var/www/mysite -type f -exec chmod 644 {} \;
```

### Övning 2: Shared project folder

```bash
# Skapa delad katalog
sudo mkdir /projects/team
sudo chgrp developers /projects/team
sudo chmod 2775 /projects/team

# Alla i "developers" grupp kan nu:
# - Skapa filer
# - Nya filer tillhör gruppen "developers"
# - Alla kan läsa varandras filer
```

### Övning 3: Säkra SSH

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `chmod 755` | Standard för scripts/dirs |
| `chmod 644` | Standard för filer |
| `chmod 600` | Secrets/private keys |
| `chmod u+s` | SUID |
| `chmod g+s` | SGID |
| `chmod +t` | Sticky bit |
| `chown user:group` | Ändra ägare |
| `umask 022` | Sätt default |
| `setfacl` | Finkorning access |

---

## Nästa Steg

Du behärskar nu Linux-permissions. Nästa node: **Text Processing** — manipulera textdata som ett proffs med grep, sed och awk.
"""
            },
            {
                "title": "Text Processing Power Tools",
                "difficulty": "medium",
                "estimated_minutes": 70,
                "xp_reward": 95,
                "content": r"""# Text Processing Power Tools

## Varför detta är kritiskt

> "In DevOps, logs are your eyes into production. Config files control everything. Data pipelines flow through text. The ability to slice, filter, and transform text is not optional — it's survival."

---

## Grundläggande filvisning

### cat — Concatenate and display

```bash
# Visa fil
cat file.txt

# Visa med radnummer
cat -n file.txt

# Visa med radnummer (bara icke-tomma)
cat -b file.txt

# Visa osynliga tecken
cat -A file.txt

# Konkatenera filer
cat file1.txt file2.txt > combined.txt

# Append till fil
cat newdata.txt >> existing.txt
```

### head & tail — Början och slutet

```bash
# Första 10 raderna (default)
head file.txt

# Första N rader
head -n 20 file.txt
head -20 file.txt

# Sista 10 raderna
tail file.txt

# Sista N rader
tail -n 20 file.txt

# Följ fil i realtid (live logs!)
tail -f /var/log/syslog

# Följ och retry om fil inte finns
tail -F /var/log/app.log

# Följ flera filer
tail -f file1.log file2.log

# Från rad N till slutet
tail -n +100 file.txt   # Från rad 100
```

**Pro Tip:** `tail -f` är din bästa vän för debugging. Kombinera med grep:
```bash
tail -f /var/log/nginx/access.log | grep --line-buffered "ERROR"
```

---

## grep — Global Regular Expression Print

`grep` är det mest använda sökverktyget.

### Grundläggande grep

```bash
# Sök efter mönster
grep "error" logfile.txt

# Case-insensitive
grep -i "error" logfile.txt

# Invertera (visa rader som INTE matchar)
grep -v "debug" logfile.txt

# Visa radnummer
grep -n "error" logfile.txt

# Räkna träffar
grep -c "error" logfile.txt

# Visa bara matchande del
grep -o "error[0-9]*" logfile.txt

# Sök i flera filer
grep "pattern" file1.txt file2.txt

# Rekursiv sökning
grep -r "TODO" ./src/

# Med filnamn
grep -H "pattern" *.txt
```

### grep med regex

```bash
# Extended regex (-E eller egrep)
grep -E "error|warning|critical" log.txt

# Begynnelse av rad
grep "^Start" file.txt

# Slutet av rad
grep "end$" file.txt

# Valfritt tecken
grep "err.r" file.txt    # error, errir, etc

# Upprepa
grep "o\+" file.txt     # En eller fler "o"
grep -E "o+" file.txt    # Samma med -E

# Teckenklasser
grep "[0-9]\+" file.txt     # Siffror
grep "[a-zA-Z]\+" file.txt  # Bokstäver

# Word boundary
grep -w "error" file.txt     # Matchar "error" men inte "errors"
```

### grep kontext

```bash
# Visa N rader efter träff
grep -A 3 "ERROR" log.txt

# Visa N rader före träff
grep -B 3 "ERROR" log.txt

# Visa N rader före OCH efter
grep -C 3 "ERROR" log.txt
```

### Praktiska grep-mönster

```bash
# Hitta IP-adresser
grep -E "\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b" access.log

# Hitta e-postadresser
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" file.txt

# Exkludera kommentarer och tomma rader
grep -v "^#" config.txt | grep -v "^$"

# Hitta funktionsdefinitioner (Python)
grep -E "^def [a-z_]+\(" *.py
```

---

## sed — Stream Editor

`sed` transformerar text rad för rad.

### Substitution (vanligast)

```bash
# Syntax: sed 's/pattern/replacement/flags'

# Ersätt första förekomsten per rad
sed 's/old/new/' file.txt

# Ersätt ALLA förekomster (global)
sed 's/old/new/g' file.txt

# Case-insensitive
sed 's/old/new/gi' file.txt

# Ändra filen på plats (-i)
sed -i 's/old/new/g' file.txt

# Med backup
sed -i.bak 's/old/new/g' file.txt

# Flera substitutioner
sed -e 's/old1/new1/g' -e 's/old2/new2/g' file.txt
```

### sed rad-operationer

```bash
# Ta bort rad 5
sed '5d' file.txt

# Ta bort rader 5-10
sed '5,10d' file.txt

# Ta bort rader som matchar
sed '/pattern/d' file.txt

# Ta bort tomma rader
sed '/^$/d' file.txt

# Ta bort kommentarer och tomma rader
sed '/^#/d; /^$/d' file.txt

# Visa bara rad 5
sed -n '5p' file.txt

# Visa rader 5-10
sed -n '5,10p' file.txt

# Visa rader som matchar
sed -n '/pattern/p' file.txt
```

### sed avancerat

```bash
# Fånga grupper
sed 's/\(.*\)@\(.*\)/User: \1, Domain: \2/' emails.txt

# Med extended regex (-E)
sed -E 's/(.*)@(.*)/User: \1, Domain: \2/' emails.txt

# Lägg till text före rad som matchar
sed '/pattern/i\New line before' file.txt

# Lägg till text efter rad som matchar
sed '/pattern/a\New line after' file.txt
```

---

## awk — Pattern-Action Language

`awk` är ett fullständigt programmeringsspråk för textbearbetning.

### Grundläggande awk

```bash
# Syntax: awk 'pattern { action }' file

# Skriv ut allt (som cat)
awk '{print}' file.txt

# Skriv ut kolumn 1
awk '{print $1}' file.txt

# Skriv ut kolumn 1 och 3
awk '{print $1, $3}' file.txt

# Med annan delimiter
awk -F':' '{print $1}' /etc/passwd

# Skriv ut sista kolumn
awk '{print $NF}' file.txt

# Skriv ut antal fält
awk '{print NF}' file.txt

# Skriv ut radnummer
awk '{print NR": "$0}' file.txt
```

### awk med villkor

```bash
# Villkor före action
awk '$3 > 100 {print $1, $3}' data.txt

# Regex-match
awk '/error/ {print}' log.txt

# Kombinera
awk '/error/ && $3 > 100 {print $1}' log.txt

# Negera
awk '!/comment/ {print}' file.txt
```

### awk inbyggda variabler

| Variabel | Betydelse |
|----------|-----------|
| $0 | Hela raden |
| $1, $2... | Fält 1, 2, ... |
| NF | Antal fält |
| NR | Radnummer |
| FS | Fältseparator (default: mellanslag) |
| OFS | Output fältseparator |
| RS | Radseparator |

### awk praktiska exempel

```bash
# Summera kolumn
awk '{sum += $3} END {print sum}' data.txt

# Genomsnitt
awk '{sum += $3; count++} END {print sum/count}' data.txt

# Unika värden (som uniq)
awk '!seen[$1]++' file.txt

# Byt ordning på kolumner
awk '{print $3, $1, $2}' file.txt

# Formaterad output
awk '{printf "%-10s %5d\n", $1, $2}' file.txt
```

---

## cut, sort, uniq — Klassiska verktyg

### cut — Extrahera fält

```bash
# Extrahera fält med delimiter
cut -d':' -f1 /etc/passwd

# Flera fält
cut -d':' -f1,3 /etc/passwd

# Fält 1 till 3
cut -d':' -f1-3 /etc/passwd

# Extrahera teckenpositioner
cut -c1-10 file.txt
```

### sort — Sortera

```bash
# Alfabetisk sortering
sort file.txt

# Numerisk sortering
sort -n numbers.txt

# Omvänd ordning
sort -r file.txt

# Sortera på kolumn
sort -t':' -k3 -n /etc/passwd

# Unik sortering
sort -u file.txt

# Human-readable storlekar (1K, 2M, etc)
sort -h sizes.txt
```

### uniq — Unika rader

```bash
# OBS: uniq kräver sorterad input!

# Ta bort duplikater
sort file.txt | uniq

# Visa bara duplikater
sort file.txt | uniq -d

# Visa bara unika
sort file.txt | uniq -u

# Räkna förekomster
sort file.txt | uniq -c

# Sortera på antal
sort file.txt | uniq -c | sort -rn
```

---

## tr — Translate characters

```bash
# Ersätt tecken
echo "hello" | tr 'a-z' 'A-Z'    # HELLO

# Ta bort tecken
echo "hello123" | tr -d '0-9'     # hello

# Squeeze upprepningar
echo "hellooo" | tr -s 'o'        # hello

# Ersätt newline med space
tr '\n' ' ' < file.txt

# Ta bort allt utom siffror
echo "abc123xyz" | tr -cd '0-9'   # 123
```

---

## wc — Word Count

```bash
# Allt: rader, ord, tecken
wc file.txt

# Bara rader
wc -l file.txt

# Bara ord
wc -w file.txt

# Bara tecken/bytes
wc -c file.txt
wc -m file.txt    # Tecken (unicode-aware)
```

---

## diff — Jämför filer

```bash
# Standard diff
diff file1.txt file2.txt

# Unified format (som git)
diff -u file1.txt file2.txt

# Side by side
diff -y file1.txt file2.txt

# Ignorera whitespace
diff -w file1.txt file2.txt

# Rekursiv (kataloger)
diff -r dir1/ dir2/
```

---

## Pipeline — Kombinera verktyg

Verklig kraft kommer från att kombinera verktyg!

```bash
# Topp 10 IP-adresser i access log
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Räkna förekomster av HTTP-status
cat access.log | awk '{print $9}' | sort | uniq -c | sort -rn

# Hitta stora filer och sortera
find /var/log -type f -exec du -h {} + | sort -rh | head -20

# Extrahera och räkna fel från log
grep -i error app.log | awk '{print $4}' | sort | uniq -c | sort -rn
```

---

## Praktiska Övningar

### Övning 1: Log-analys

```bash
# Skapa testlog
cat > /tmp/access.log << 'EOF'
192.168.1.1 - - [01/Dec/2025:10:00:00] "GET /index.html" 200 1234
192.168.1.2 - - [01/Dec/2025:10:00:01] "GET /about.html" 200 5678
192.168.1.1 - - [01/Dec/2025:10:00:02] "GET /contact.html" 404 0
192.168.1.3 - - [01/Dec/2025:10:00:03] "POST /api/login" 500 0
192.168.1.1 - - [01/Dec/2025:10:00:04] "GET /index.html" 200 1234
EOF

# 1. Räkna requests per IP
awk '{print $1}' /tmp/access.log | sort | uniq -c | sort -rn

# 2. Hitta alla 500-errors
grep " 500 " /tmp/access.log

# 3. Räkna status-koder
awk '{print $9}' /tmp/access.log | sort | uniq -c
```

---

## Sammanfattning

| Verktyg | Användning |
|---------|------------|
| `grep` | Sök mönster |
| `sed` | Ersätt och transformera |
| `awk` | Kolumnbearbetning |
| `cut` | Extrahera fält |
| `sort` | Sortera |
| `uniq` | Unika värden |
| `tr` | Ersätt tecken |
| `wc` | Räkna rader/ord |
| `diff` | Jämför filer |
| `head/tail` | Början/slutet |

---

## Nästa Steg

Du är nu en text-ninja. Nästa node: **Text Editors** — behärska Vim och Nano för att redigera filer direkt på servern.
"""
            },
            {
                "title": "Text Editors: Vim & Nano",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 75,
                "content": r"""# Text Editors: Vim & Nano

## Varför detta är kritiskt

> "You SSH into a production server. Nano isn't installed. The only editor is Vi. You need to edit a config file NOW. This is not a drill — every DevOps engineer must know at least basic Vim."

---

## Nano — The Friendly Editor

Nano är användarvänlig: alla kommandon visas längst ner.

### Starta Nano

```bash
# Öppna/skapa fil
nano file.txt

# Öppna på specifik rad
nano +15 file.txt

# Read-only
nano -v file.txt

# Med syntax highlighting
nano -Y sh script.sh
```

### Kommandon (visas längst ner)

`^` betyder Ctrl

| Kommando | Funktion |
|----------|----------|
| `^O` | Spara (Write Out) |
| `^X` | Avsluta |
| `^K` | Klipp ut rad |
| `^U` | Klistra in |
| `^W` | Sök |
| `^\` | Sök & ersätt |
| `^G` | Hjälp |
| `^C` | Visa position |
| `^_` | Gå till rad |

### Navigation

| Kommando | Funktion |
|----------|----------|
| `^A` | Början av rad |
| `^E` | Slutet av rad |
| `^Y` | Sida upp |
| `^V` | Sida ner |
| `Alt+\` | Toppen av fil |
| `Alt+/` | Botten av fil |

### Markering

```
Alt+A    → Starta markering
(flytta) → Markera text
^K       → Klipp ut
^U       → Klistra in
```

### ~/.nanorc konfiguration

```bash
cat > ~/.nanorc << 'EOF'
# Visa radnummer
set linenumbers

# Soft wrap (ingen hård radbrytning)
set softwrap

# Tab = 4 spaces
set tabsize 4
set tabstospaces

# Visa cursor-position konstant
set constantshow

# Syntax highlighting
include "/usr/share/nano/*.nanorc"
EOF
```

---

## Vim — The Powerful Editor

Vim är kraftfull men har en inlärningskurva. Det viktigaste: Vim har MODES.

### Modes (KRITISKT att förstå)

```
┌─────────────────────────────────────────────────────────────┐
│                        VIM MODES                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   NORMAL MODE (default)                                     │
│   ──────────────────────                                    │
│   Du startar här. Navigera, ta bort, kopiera.               │
│   Tryck ESC för att återgå hit.                            │
│                                                             │
│           │                                                 │
│           │ i, a, o                                         │
│           ▼                                                 │
│   INSERT MODE                                               │
│   ───────────                                               │
│   Skriv text som vanligt.                                   │
│   Tryck ESC för att gå tillbaka till Normal.               │
│                                                             │
│           │                                                 │
│           │ ESC → :                                         │
│           ▼                                                 │
│   COMMAND MODE                                              │
│   ────────────                                              │
│   Spara, avsluta, söka.                                    │
│   :w, :q, :wq                                              │
│                                                             │
│           │                                                 │
│           │ v, V, Ctrl+v                                    │
│           ▼                                                 │
│   VISUAL MODE                                               │
│   ───────────                                               │
│   Markera text.                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Det viktigaste: Avsluta Vim!

```
:q      → Avsluta (om inga ändringar)
:q!     → Avsluta utan att spara (force)
:w      → Spara
:wq     → Spara och avsluta
ZZ      → Spara och avsluta (snabbare)
```

### In i Insert Mode

| Kommando | Funktion |
|----------|----------|
| `i` | Insert före cursor |
| `I` | Insert i början av rad |
| `a` | Append efter cursor |
| `A` | Append i slutet av rad |
| `o` | Öppna ny rad under |
| `O` | Öppna ny rad över |

### Navigation i Normal Mode

```
h j k l     → Vänster, Ner, Upp, Höger
w           → Nästa ord
b           → Föregående ord
e           → Slutet av ord
0           → Början av rad
$           → Slutet av rad
gg          → Första raden
G           → Sista raden
10G         → Gå till rad 10
Ctrl+f      → Sida framåt
Ctrl+b      → Sida bakåt
```

### Radera i Normal Mode

```
x           → Radera tecken under cursor
X           → Radera tecken före cursor
dd          → Radera rad
dw          → Radera ord
d$          → Radera till slutet av rad
d0          → Radera till början av rad
D           → Samma som d$
5dd         → Radera 5 rader
```

### Kopiera och klistra

```
yy          → Kopiera (yank) rad
yw          → Kopiera ord
y$          → Kopiera till slutet
5yy         → Kopiera 5 rader
p           → Klistra efter
P           → Klistra före
```

### Undo / Redo

```
u           → Undo
Ctrl+r      → Redo
.           → Upprepa senaste kommando
```

### Sök och ersätt

```
/pattern    → Sök framåt
?pattern    → Sök bakåt
n           → Nästa träff
N           → Föregående träff
*           → Sök ord under cursor

:s/old/new/         → Ersätt första på rad
:s/old/new/g        → Ersätt alla på rad
:%s/old/new/g       → Ersätt alla i fil
:%s/old/new/gc      → Med bekräftelse
```

### Visual Mode

```
v           → Markera tecken
V           → Markera rader
Ctrl+v      → Block-markering

(efter markering):
d           → Radera
y           → Kopiera
>           → Indentera
<           → Outdent
```

### ~/.vimrc konfiguration

```bash
cat > ~/.vimrc << 'EOF'
" Visa radnummer
set number

" Relativa radnummer
set relativenumber

" Syntax highlighting
syntax on

" Sök: ignorera case om bara lowercase
set ignorecase
set smartcase

" Highlighta sökträffar
set hlsearch
set incsearch

" Tab = 4 spaces
set tabstop=4
set shiftwidth=4
set expandtab

" Visa matchande parentes
set showmatch

" Visa ruler (position)
set ruler

" Bättre backspace
set backspace=indent,eol,start
EOF
```

### Vim Survival Cheatsheet

```
┌────────────────────────────────────────────────┐
│              VIM SURVIVAL GUIDE                │
├────────────────────────────────────────────────┤
│ ESC        → Tillbaka till Normal mode         │
│ :q!        → PANIC EXIT (utan att spara)       │
│ :wq        → Spara och avsluta                 │
│ i          → Börja skriva                      │
│ dd         → Radera rad                        │
│ u          → Undo                              │
│ /text      → Sök                               │
│ :set nu    → Visa radnummer                    │
└────────────────────────────────────────────────┘
```

---

## Vim vs Nano — När använda vad?

| Situation | Rekommendation |
|-----------|----------------|
| Snabb edit | Nano |
| Nano ej installerat | Vim |
| Stor fil (1000+ rader) | Vim |
| Komplexa sök/ersätt | Vim |
| Remote server | Vim (alltid tillgänglig) |
| Scripting redigering | Vim |

---

## vimtutor — Lär dig Vim

```bash
# Interaktiv Vim-tutorial (30 min)
vimtutor
```

---

## Praktiska Övningar

### Övning 1: Nano basics

```bash
# 1. Skapa fil
nano /tmp/test.txt

# 2. Skriv: "Hello World"
# 3. Spara: Ctrl+O, Enter
# 4. Avsluta: Ctrl+X
```

### Övning 2: Vim basics

```bash
# 1. Öppna
vim /tmp/vimtest.txt

# 2. Tryck i (insert mode)
# 3. Skriv text
# 4. Tryck ESC
# 5. Skriv :wq och Enter
```

### Övning 3: Vim sök/ersätt

```bash
# 1. Skapa testfil
echo -e "foo bar\nfoo baz\nfoo qux" > /tmp/replace.txt

# 2. Öppna i vim
vim /tmp/replace.txt

# 3. Ersätt alla "foo" med "hello"
# Skriv: :%s/foo/hello/g
# Tryck Enter

# 4. Spara och avsluta: :wq
```

---

## Sammanfattning

### Nano

| Kommando | Funktion |
|----------|----------|
| `^O` | Spara |
| `^X` | Avsluta |
| `^W` | Sök |
| `^K` | Klipp rad |
| `^U` | Klistra |

### Vim

| Kommando | Funktion |
|----------|----------|
| `i` | Insert mode |
| `ESC` | Normal mode |
| `:wq` | Spara & avsluta |
| `:q!` | Force quit |
| `dd` | Radera rad |
| `yy` | Kopiera rad |
| `p` | Klistra |
| `u` | Undo |
| `/pattern` | Sök |
| `:%s/a/b/g` | Ersätt alla |

---

## Nästa Steg

Du kan nu redigera filer på vilken server som helst. Nästa node: **I/O Redirection** — dirigera dataflöden med pipes och redirects.
"""
            },
            {
                "title": "I/O Redirection & Pipes",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# I/O Redirection & Pipes

## Varför detta är kritiskt

> "In Unix, everything flows. Data streams in, gets transformed, and streams out. Master redirection and pipes, and you can build complex data pipelines with simple commands."

---

## Förstå Standard Streams

Varje process har tre standard-strömmar:

```
┌─────────────────────────────────────────────────────────────┐
│                     PROCESS                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   stdin (0)  ──────►  [COMMAND]  ──────► stdout (1)        │
│   (input)                │               (output)           │
│                          │                                  │
│                          ▼                                  │
│                     stderr (2)                              │
│                     (errors)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

File Descriptors:
0 = stdin  (standard input)
1 = stdout (standard output)
2 = stderr (standard error)
```

---

## Output Redirection

### Redirect stdout till fil

```bash
# Skriv output till fil (överskriver)
ls -l > filelist.txt

# Append till fil (lägger till)
echo "ny rad" >> logfile.txt

# Explicit file descriptor
ls -l 1> filelist.txt    # Samma som >
```

### Redirect stderr till fil

```bash
# Bara errors till fil
command 2> errors.log

# Suppress errors (skicka till /dev/null)
find / -name "*.conf" 2>/dev/null
```

### Redirect båda

```bash
# stdout och stderr till samma fil
command > output.log 2>&1

# Modernare syntax (bash 4+)
command &> output.log

# stdout och stderr till olika filer
command > output.log 2> errors.log

# Append båda
command >> output.log 2>&1
```

### /dev/null — The Black Hole

```bash
# Kasta bort all output
command > /dev/null

# Kasta bort allt (output + errors)
command > /dev/null 2>&1
command &> /dev/null

# Vanligt mönster: tysta errors
find / -name "secret" 2>/dev/null
```

---

## Input Redirection

### Redirect stdin från fil

```bash
# Läs input från fil
sort < unsorted.txt

# Kombinera input och output
sort < unsorted.txt > sorted.txt

# wc räknar från fil
wc -l < bigfile.txt
```

### Here Documents (heredoc)

```bash
# Multiline input
cat << EOF
Detta är rad 1
Detta är rad 2
Variabel: $HOME
EOF

# Utan variabel-expansion (quote EOF)
cat << 'EOF'
$HOME visas som literal
EOF

# Skriv till fil
cat << EOF > config.txt
server=localhost
port=8080
EOF
```

### Here Strings

```bash
# En rad som input
grep "pattern" <<< "search in this string"

# Med variabel
grep "error" <<< "$log_content"
```

---

## Pipes — Koppla kommandon

Pipe (`|`) skickar stdout från ett kommando till stdin för nästa.

```bash
# Grundläggande pipe
ls -l | grep ".txt"

# Kedja flera
cat access.log | grep "404" | wc -l

# Praktiskt exempel: topp 10 största filer
du -h /var/log/* | sort -rh | head -10
```

### Pipeline-mönster

```bash
# Filtrera → Transformera → Aggregera
cat data.csv | grep "active" | cut -d',' -f2 | sort | uniq -c

# Log-analys
tail -1000 access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head

# Process-sökning
ps aux | grep nginx | grep -v grep
```

---

## tee — Split output

`tee` skriver till fil OCH stdout samtidigt.

```bash
# Skriv till fil och visa
ls -l | tee filelist.txt

# Append istället för överskriva
ls -l | tee -a filelist.txt

# Skriv till flera filer
ls -l | tee file1.txt file2.txt

# I pipeline
cat data.txt | tee backup.txt | grep "important" > filtered.txt
```

### tee med sudo

```bash
# Detta funkar INTE:
sudo echo "text" > /etc/protected.txt    # Redirect körs som user!

# Använd tee istället:
echo "text" | sudo tee /etc/protected.txt

# Append:
echo "text" | sudo tee -a /etc/protected.txt

# Utan output till terminal:
echo "text" | sudo tee /etc/protected.txt > /dev/null
```

---

## xargs — Bygg kommandon från input

`xargs` tar input och använder det som argument till ett kommando.

```bash
# Grundläggande
echo "file1 file2 file3" | xargs rm

# En fil per kommando
find . -name "*.log" | xargs -I {} mv {} {}.bak

# Parallell execution
find . -name "*.jpg" | xargs -P 4 -I {} convert {} -resize 50% small_{}

# Med null-separator (hanterar spaces i filnamn)
find . -name "*.txt" -print0 | xargs -0 grep "pattern"

# Begränsa antal argument
echo {1..100} | xargs -n 10 echo
```

### xargs praktiska exempel

```bash
# Ta bort gamla filer
find /tmp -mtime +7 | xargs rm -f

# Döda processer
pgrep -f "pattern" | xargs kill

# Kopiera matchande filer
find . -name "*.conf" | xargs -I {} cp {} /backup/
```

---

## Process Substitution

Behandla output som en fil.

```bash
# Jämför output från två kommandon
diff <(ls dir1) <(ls dir2)

# Sortera utan temp-fil
sort <(cat file1 file2)

# Flera inputs
paste <(cut -f1 data.txt) <(cut -f3 data.txt)
```

---

## Avancerade Mönster

### Named Pipes (FIFO)

```bash
# Skapa named pipe
mkfifo mypipe

# Terminal 1: Läs från pipe (blockerar)
cat mypipe

# Terminal 2: Skriv till pipe
echo "Hello" > mypipe
```

### File Descriptor Manipulation

```bash
# Öppna fil för läsning på fd 3
exec 3< inputfile.txt
read line <&3
exec 3<&-    # Stäng fd 3

# Öppna fil för skrivning på fd 4
exec 4> outputfile.txt
echo "data" >&4
exec 4>&-    # Stäng fd 4
```

### Swap stdout och stderr

```bash
# Swap 1 och 2
command 3>&1 1>&2 2>&3 3>&-
```

---

## Praktiska Övningar

### Övning 1: Log-filtrering

```bash
# Skapa testlog
cat > /tmp/app.log << 'EOF'
2025-12-01 10:00:00 INFO Starting application
2025-12-01 10:00:01 DEBUG Loading config
2025-12-01 10:00:02 ERROR Database connection failed
2025-12-01 10:00:03 INFO Retrying...
2025-12-01 10:00:04 ERROR Still failing
2025-12-01 10:00:05 INFO Recovered
EOF

# Extrahera bara ERROR-rader till fil
grep "ERROR" /tmp/app.log > /tmp/errors.log

# Räkna errors och visa
grep "ERROR" /tmp/app.log | tee /tmp/errors.log | wc -l
```

### Övning 2: Pipeline Power

```bash
# Hitta de 5 största filerna i /var
sudo find /var -type f -exec du -h {} + 2>/dev/null | sort -rh | head -5

# Unika IP-adresser från log (simulerad)
echo -e "192.168.1.1\n192.168.1.2\n192.168.1.1\n192.168.1.3" | sort | uniq -c | sort -rn
```

### Övning 3: xargs

```bash
# Skapa testfiler
mkdir /tmp/xargs_test
touch /tmp/xargs_test/file{1..5}.txt

# Lägg till innehåll med xargs
ls /tmp/xargs_test/*.txt | xargs -I {} sh -c 'echo "Content of {}" > {}'

# Verifiera
cat /tmp/xargs_test/*.txt
```

---

## Sammanfattning

| Operator | Betydelse |
|----------|-----------|
| `>` | Redirect stdout till fil (överskriver) |
| `>>` | Append stdout till fil |
| `2>` | Redirect stderr till fil |
| `&>` | Redirect stdout + stderr |
| `<` | Input från fil |
| `<<` | Here document |
| `<<<` | Here string |
| `\|` | Pipe (stdout → stdin) |
| `tee` | Split till fil + stdout |
| `xargs` | Bygg kommandon från input |
| `<()` | Process substitution |

---

## Nästa Steg

Du behärskar nu dataflöden i Linux. Nästa node: **User Management** — hantera användare och grupper.
"""
            },
            {
                "title": "User & Group Management",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 80,
                "content": r"""# User & Group Management

## Varför detta är kritiskt

> "Security starts with access control. Who can log in? What can they do? One misconfigured sudo rule can give an attacker root. One forgotten user account is a backdoor waiting to be exploited."

---

## Förstå Användarsystemet

```
┌─────────────────────────────────────────────────────────────┐
│                   LINUX USER MODEL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   /etc/passwd     → Användarinfo (namn, UID, shell)        │
│   /etc/shadow     → Krypterade lösenord                    │
│   /etc/group      → Gruppdefinitioner                      │
│   /etc/gshadow    → Grupplösenord                          │
│                                                             │
│   UID 0           → root (superuser)                       │
│   UID 1-999       → System/service accounts                │
│   UID 1000+       → Vanliga användare                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### /etc/passwd format

```bash
cat /etc/passwd | head -3
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

# Format: username:x:UID:GID:comment:home:shell
```

| Fält | Betydelse |
|------|-----------|
| username | Användarnamn |
| x | Lösenord i /etc/shadow |
| UID | User ID |
| GID | Primary Group ID |
| comment | Fullständigt namn/info |
| home | Hemkatalog |
| shell | Login shell |

---

## Skapa Användare

### useradd — Skapa användare

```bash
# Enkel (ingen hemkatalog, default shell)
sudo useradd john

# Med hemkatalog (-m) och bash shell
sudo useradd -m -s /bin/bash john

# Med specifik UID och GID
sudo useradd -u 1500 -g developers john

# Med kommentar
sudo useradd -m -s /bin/bash -c "John Doe" john

# Med extra grupper
sudo useradd -m -s /bin/bash -G sudo,docker john

# System account (för services)
sudo useradd -r -s /usr/sbin/nologin myservice
```

### Sätt lösenord

```bash
# Interaktivt
sudo passwd john

# Tvinga byte vid nästa login
sudo passwd -e john

# Lås konto
sudo passwd -l john

# Lås upp
sudo passwd -u john

# Se lösenordsstatus
sudo passwd -S john
```

---

## Modifiera Användare

### usermod — Ändra användare

```bash
# Byt shell
sudo usermod -s /bin/zsh john

# Lägg till i grupp (VIKTIGT: -a för append!)
sudo usermod -aG docker john

# VARNING: Utan -a ersätts alla grupper!
sudo usermod -G docker john    # John är nu BARA i docker

# Byt hemkatalog
sudo usermod -d /home/newjohn -m john

# Byt användarnamn
sudo usermod -l newname john

# Lås konto
sudo usermod -L john

# Lås upp
sudo usermod -U john
```

---

## Ta Bort Användare

### userdel — Radera användare

```bash
# Ta bort användare (behåll hemkatalog)
sudo userdel john

# Ta bort användare OCH hemkatalog
sudo userdel -r john

# Force (även om inloggad)
sudo userdel -f john
```

---

## Grupper

### Se grupper

```bash
# Dina grupper
groups

# Annan användares grupper
groups john

# Detaljerad info
id
# uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),27(sudo),999(docker)

id john
```

### Hantera grupper

```bash
# Skapa grupp
sudo groupadd developers

# Med specifik GID
sudo groupadd -g 2000 developers

# Ta bort grupp
sudo groupdel developers

# Byt namn på grupp
sudo groupmod -n newname oldname

# Lägg till användare i grupp
sudo usermod -aG developers john

# Ta bort användare från grupp
sudo gpasswd -d john developers
```

---

## su & sudo

### su — Switch User

```bash
# Byt till root (behöver roots lösenord)
su

# Byt till root med full environment
su -

# Byt till annan användare
su - john

# Kör ett kommando som annan användare
su - john -c "whoami"
```

### sudo — Superuser Do

```bash
# Kör som root
sudo command

# Kör som annan användare
sudo -u john command

# Öppna root shell
sudo -i

# Behåll environment
sudo -E command

# Lista dina sudo-rättigheter
sudo -l

# Redigera sudoers säkert
sudo visudo
```

### /etc/sudoers format

```bash
# Redigera ALLTID med visudo!
sudo visudo

# Format: user/group host=(runas) commands

# Root kan allt
root    ALL=(ALL:ALL) ALL

# Användare i sudo-grupp kan allt
%sudo   ALL=(ALL:ALL) ALL

# John kan köra apt utan lösenord
john    ALL=(ALL) NOPASSWD: /usr/bin/apt

# Developers kan starta/stoppa nginx
%developers ALL=(ALL) /bin/systemctl start nginx, /bin/systemctl stop nginx
```

### Sudoers best practices

```bash
# Skapa fil i /etc/sudoers.d/ istället för att redigera huvud-filen
sudo visudo -f /etc/sudoers.d/developers

# Innehåll:
%developers ALL=(ALL) NOPASSWD: /usr/bin/docker, /usr/bin/docker-compose
```

---

## Praktiska Mönster

### Skapa deployment-användare

```bash
# Skapa användare
sudo useradd -m -s /bin/bash -c "Deploy User" deploy

# Sätt lösenord
sudo passwd deploy

# Lägg till i nödvändiga grupper
sudo usermod -aG sudo,docker deploy

# Konfigurera sudo utan lösenord för deploy
echo "deploy ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/deploy

# Sätt rätt permissions
sudo chmod 440 /etc/sudoers.d/deploy
```

### Skapa service account

```bash
# System account utan login
sudo useradd -r -s /usr/sbin/nologin -d /opt/myapp myapp

# Skapa app-katalog
sudo mkdir -p /opt/myapp
sudo chown myapp:myapp /opt/myapp
```

---

## Praktiska Övningar

### Övning 1: Användare och grupper

```bash
# 1. Skapa grupp
sudo groupadd testgroup

# 2. Skapa användare i gruppen
sudo useradd -m -s /bin/bash -G testgroup testuser

# 3. Verifiera
id testuser
groups testuser

# 4. Cleanup
sudo userdel -r testuser
sudo groupdel testgroup
```

### Övning 2: Sudo-regel

```bash
# 1. Skapa användare
sudo useradd -m -s /bin/bash limited_user

# 2. Ge begränsad sudo
echo "limited_user ALL=(ALL) NOPASSWD: /bin/systemctl status *" | sudo tee /etc/sudoers.d/limited_user
sudo chmod 440 /etc/sudoers.d/limited_user

# 3. Testa (som limited_user)
sudo -u limited_user sudo systemctl status ssh    # Ska funka
sudo -u limited_user sudo systemctl restart ssh   # Ska INTE funka
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `useradd -m -s /bin/bash` | Skapa användare |
| `passwd` | Sätt lösenord |
| `usermod -aG group user` | Lägg till i grupp |
| `userdel -r` | Ta bort användare |
| `groupadd` | Skapa grupp |
| `id` | Visa UID/GID/grupper |
| `su -` | Byt till root |
| `sudo` | Kör som root |
| `visudo` | Redigera sudoers |

---

## Nästa Steg

Du kan nu hantera användare och grupper. Nästa node: **Package Management** — installera och uppdatera programvara.
"""
            },
            {
                "title": "Package Management",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 70,
                "content": r"""# Package Management

## Varför detta är kritiskt

> "The first thing you do on a new server: update packages. The second: install what you need. Package management is how you get software onto Linux — and keep it secure with updates."

---

## Pakethanterare per Distribution

```
┌─────────────────────────────────────────────────────────────┐
│              PACKAGE MANAGERS BY DISTRO                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Debian/Ubuntu          →  apt, apt-get, dpkg             │
│   RHEL/CentOS/Fedora     →  dnf, yum, rpm                  │
│   Arch                   →  pacman                          │
│   Alpine                 →  apk                             │
│   Universal              →  snap, flatpak                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## APT (Debian/Ubuntu)

### Uppdatera paketlistor

```bash
# Hämta senaste paketinfo från repos
sudo apt update

# Uppgradera installerade paket
sudo apt upgrade

# Uppgradera + hantera beroenden (ta bort/lägga till)
sudo apt full-upgrade

# Kombinera (vanligt mönster)
sudo apt update && sudo apt upgrade -y
```

### Installera paket

```bash
# Installera ett paket
sudo apt install nginx

# Installera flera
sudo apt install nginx git curl

# Installera utan att fråga
sudo apt install -y nginx

# Installera specifik version
sudo apt install nginx=1.18.0-0ubuntu1
```

### Ta bort paket

```bash
# Ta bort paket (behåll config)
sudo apt remove nginx

# Ta bort paket + config
sudo apt purge nginx

# Ta bort oanvända dependencies
sudo apt autoremove
```

### Sök och info

```bash
# Sök paket
apt search nginx

# Visa paketinfo
apt show nginx

# Lista installerade paket
apt list --installed

# Lista uppgraderingsbara
apt list --upgradable
```

### dpkg — Low-level

```bash
# Installera .deb-fil
sudo dpkg -i package.deb

# Lista installerade
dpkg -l

# Lista filer i paket
dpkg -L nginx

# Vilket paket äger en fil?
dpkg -S /usr/bin/nginx

# Ta bort paket
sudo dpkg -r nginx
```

---

## DNF/YUM (RHEL/CentOS/Fedora)

```bash
# Uppdatera
sudo dnf update
sudo dnf upgrade

# Installera
sudo dnf install nginx

# Ta bort
sudo dnf remove nginx

# Sök
dnf search nginx

# Info
dnf info nginx

# Lista installerade
dnf list installed

# Rensa cache
sudo dnf clean all
```

### rpm — Low-level

```bash
# Installera .rpm
sudo rpm -ivh package.rpm

# Lista installerade
rpm -qa

# Paketinfo
rpm -qi nginx

# Lista filer i paket
rpm -ql nginx
```

---

## Snap (Universal)

```bash
# Installera
sudo snap install code --classic

# Lista installerade
snap list

# Uppdatera
sudo snap refresh

# Ta bort
sudo snap remove code

# Info
snap info code
```

---

## Repositories

### APT repos

```bash
# Lista repos
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Lägg till repo (PPA)
sudo add-apt-repository ppa:ondrej/php
sudo apt update

# Lägg till GPG-nyckel + repo manuellt
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt update
```

---

## Praktiska Mönster

### Server-setup

```bash
# Initial setup
sudo apt update && sudo apt upgrade -y

# Install essentials
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    htop \
    net-tools \
    unzip
```

### Säkerhetsuppdateringar

```bash
# Bara säkerhetsuppdateringar (Ubuntu)
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades

# Manuellt
sudo apt update
sudo apt upgrade -y
```

---

## Sammanfattning

| Kommando (apt) | Funktion |
|----------------|----------|
| `apt update` | Hämta paketlistor |
| `apt upgrade` | Uppgradera paket |
| `apt install` | Installera |
| `apt remove` | Ta bort |
| `apt purge` | Ta bort + config |
| `apt search` | Sök |
| `apt show` | Info |
| `apt autoremove` | Rensa dependencies |

---

## Nästa Steg

Du kan nu installera programvara. Nästa node: **Service Management** — hantera systemtjänster med systemd.
"""
            },
            {
                "title": "Service Management (systemd)",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# Service Management (systemd)

## Varför detta är kritiskt

> "Every web server, database, and background service runs as a systemd unit. When nginx stops responding, when PostgreSQL won't start — you need systemctl and journalctl to diagnose and fix it."

---

## Förstå systemd

```
┌─────────────────────────────────────────────────────────────┐
│                      SYSTEMD                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PID 1 (init system)                                      │
│      │                                                     │
│      ├── Services (.service)  → nginx, postgresql, sshd   │
│      ├── Sockets (.socket)    → Activation triggers        │
│      ├── Timers (.timer)      → Cron-liknande              │
│      ├── Mounts (.mount)      → Filsystem                  │
│      └── Targets (.target)    → Boot stages                │
│                                                             │
│   Unit files: /etc/systemd/system/                         │
│               /lib/systemd/system/                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## systemctl — Tjänsthantering

### Status och info

```bash
# Visa status
systemctl status nginx

# Lista alla tjänster
systemctl list-units --type=service

# Lista aktiva
systemctl list-units --type=service --state=active

# Lista alla (även inaktiva)
systemctl list-units --type=service --all

# Lista failed
systemctl list-units --failed
```

### Start, stop, restart

```bash
# Starta tjänst
sudo systemctl start nginx

# Stoppa
sudo systemctl stop nginx

# Starta om
sudo systemctl restart nginx

# Ladda om config (utan full restart)
sudo systemctl reload nginx

# Reload eller restart
sudo systemctl reload-or-restart nginx
```

### Enable / Disable (autostart)

```bash
# Starta vid boot
sudo systemctl enable nginx

# Starta inte vid boot
sudo systemctl disable nginx

# Enable + start nu
sudo systemctl enable --now nginx

# Disable + stop nu
sudo systemctl disable --now nginx

# Kontrollera om enabled
systemctl is-enabled nginx
```

### Kolla status

```bash
# Kör tjänsten?
systemctl is-active nginx

# Är den failed?
systemctl is-failed nginx
```

---

## journalctl — Loggar

Alla systemd-loggar samlas i journal.

```bash
# Alla loggar
journalctl

# För specifik tjänst
journalctl -u nginx

# Följ loggar live
journalctl -u nginx -f

# Senaste 100 rader
journalctl -u nginx -n 100

# Sedan senaste boot
journalctl -u nginx -b

# Tidsintervall
journalctl -u nginx --since "2025-12-01" --until "2025-12-01 12:00"

# Senaste timmen
journalctl -u nginx --since "1 hour ago"

# Bara errors
journalctl -u nginx -p err

# Kernel-meddelanden
journalctl -k

# Disk-användning
journalctl --disk-usage

# Rensa gamla loggar
sudo journalctl --vacuum-time=7d
```

---

## Skapa egen Service

### Enkel service

```bash
# Skapa unit-fil
sudo vim /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/run.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Aktivera

```bash
# Ladda om systemd
sudo systemctl daemon-reload

# Enable och starta
sudo systemctl enable --now myapp

# Kolla status
systemctl status myapp
```

### Unit-fil sektioner

| Sektion | Innehåll |
|---------|----------|
| [Unit] | Beskrivning, beroenden |
| [Service] | Hur tjänsten körs |
| [Install] | När den ska startas |

### Service-typer

| Type | Beteende |
|------|----------|
| simple | Processen startar direkt (default) |
| forking | Processen forkar (som traditionella daemons) |
| oneshot | Kör en gång och avslutar |
| notify | Signalerar när redo |

---

## Praktiska Övningar

### Övning 1: Hantera nginx

```bash
# 1. Status
systemctl status nginx

# 2. Stoppa
sudo systemctl stop nginx

# 3. Verifiera
systemctl is-active nginx

# 4. Starta
sudo systemctl start nginx

# 5. Se loggar
journalctl -u nginx -n 20
```

### Övning 2: Egen service

```bash
# Skapa enkel app
sudo mkdir -p /opt/mytest
echo '#!/bin/bash
while true; do
    echo "Running at $(date)" >> /opt/mytest/output.log
    sleep 10
done' | sudo tee /opt/mytest/run.sh

sudo chmod +x /opt/mytest/run.sh

# Skapa service
cat << 'EOF' | sudo tee /etc/systemd/system/mytest.service
[Unit]
Description=My Test Service

[Service]
Type=simple
ExecStart=/opt/mytest/run.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Aktivera
sudo systemctl daemon-reload
sudo systemctl enable --now mytest

# Verifiera
systemctl status mytest
tail -f /opt/mytest/output.log

# Cleanup
sudo systemctl disable --now mytest
sudo rm /etc/systemd/system/mytest.service
sudo rm -rf /opt/mytest
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `systemctl status` | Visa status |
| `systemctl start/stop` | Starta/stoppa |
| `systemctl restart` | Starta om |
| `systemctl reload` | Ladda om config |
| `systemctl enable` | Autostart vid boot |
| `systemctl disable` | Ingen autostart |
| `journalctl -u` | Se loggar |
| `journalctl -f` | Följ loggar live |
| `daemon-reload` | Ladda om unit-filer |

---

## Nästa Steg

Du kan nu hantera tjänster. Nästa node: **Disk & Storage** — partitioner, mount och LVM.
"""
            },
            {
                "title": "Disk & Storage Management",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 90,
                "content": r"""# Disk & Storage Management

## Varför detta är kritiskt

> "Disk full = system down. A full /var/log can crash your database. A full root partition stops everything. You MUST know how to check, manage, and expand storage."

---

## Disk Space Analysis

### df — Disk Free

```bash
# Visa alla filsystem
df

# Human-readable (KB, MB, GB)
df -h

# Visa filsystemtyp
df -T

# Bara ett filsystem
df -h /

# Visa inodes
df -i
```

### Output förklarad

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   15G   32G  32% /
/dev/sda2       200G  150G   40G  79% /home
tmpfs           4.0G     0  4.0G   0% /dev/shm
```

**Varningsnivåer:**
- 80%+ → Börja planera expansion
- 90%+ → Kritiskt, åtgärda nu
- 95%+ → Akut, system kan sluta fungera

### du — Disk Usage

```bash
# Katalogstorlek
du -h /var/log

# Summering
du -sh /var/log

# Sortera på storlek (hitta tjuvar)
du -h /var | sort -rh | head -20

# Max djup
du -h --max-depth=1 /

# Exkludera mönster
du -h --exclude="*.log" /var
```

### Hitta stora filer

```bash
# Filer större än 100MB
find / -type f -size +100M 2>/dev/null

# Topp 20 största filer
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -20

# ncdu (interaktiv)
sudo apt install ncdu
ncdu /
```

---

## Partitioner

### Visa partitioner

```bash
# Lista blockenheter
lsblk

# Detaljerad partitionsinfo
sudo fdisk -l

# Parted
sudo parted -l
```

### lsblk output

```bash
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0   100G  0 disk
├─sda1   8:1    0    50G  0 part /
├─sda2   8:2    0    48G  0 part /home
└─sda3   8:3    0     2G  0 part [SWAP]
sdb      8:16   0   500G  0 disk
└─sdb1   8:17   0   500G  0 part /data
```

### Skapa partition (fdisk)

```bash
# Interaktiv partitionering
sudo fdisk /dev/sdb

# Kommandon i fdisk:
# n → New partition
# p → Primary
# 1 → Partition number
# Enter → Default first sector
# +50G → Size
# w → Write and exit
```

---

## Filsystem

### Skapa filsystem

```bash
# ext4 (standard Linux)
sudo mkfs.ext4 /dev/sdb1

# xfs
sudo mkfs.xfs /dev/sdb1

# FAT32 (USB/kompatibilitet)
sudo mkfs.vfat /dev/sdb1
```

### Kontrollera filsystem

```bash
# Kontrollera och reparera (MÅSTE vara unmounted)
sudo fsck /dev/sdb1

# Force check
sudo fsck -f /dev/sdb1
```

---

## Mount & Unmount

### Tillfällig mount

```bash
# Skapa mount point
sudo mkdir /mnt/data

# Mounta
sudo mount /dev/sdb1 /mnt/data

# Verifiera
mount | grep sdb1
df -h /mnt/data

# Unmount
sudo umount /mnt/data

# Force unmount (om busy)
sudo umount -f /mnt/data

# Lazy unmount (väntar tills fri)
sudo umount -l /mnt/data
```

### Permanent mount (/etc/fstab)

```bash
# Hitta UUID (bättre än device name)
sudo blkid /dev/sdb1
# /dev/sdb1: UUID="abc123-..." TYPE="ext4"

# Redigera fstab
sudo vim /etc/fstab
```

```
# /etc/fstab format:
# <device>                                 <mount>    <type> <options>     <dump> <pass>
UUID=abc123-def456-ghi789                  /data      ext4   defaults      0      2

# Förklaringar:
# defaults = rw,suid,dev,exec,auto,nouser,async
# dump = 0 (ingen backup)
# pass = 2 (fsck ordning, 1 för root, 2 för andra, 0 för skip)
```

```bash
# Testa fstab utan reboot
sudo mount -a

# Om det misslyckas, fixa innan reboot!
```

---

## LVM (Logical Volume Manager)

LVM ger flexibilitet att ändra storlek utan att röra partitioner.

```
┌─────────────────────────────────────────────────────────────┐
│                         LVM STRUCTURE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Physical Disks:    /dev/sda    /dev/sdb    /dev/sdc      │
│                          │           │           │          │
│   Physical Volumes:     pv1        pv2        pv3          │
│                          └───────────┼───────────┘          │
│                                      │                      │
│   Volume Group:            ┌─────── vg_data ───────┐       │
│                            │                       │        │
│   Logical Volumes:     lv_home                 lv_var      │
│                            │                       │        │
│   Mount Points:        /home                   /var        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### LVM-kommandon

```bash
# Skapa Physical Volume
sudo pvcreate /dev/sdb1

# Skapa Volume Group
sudo vgcreate vg_data /dev/sdb1

# Skapa Logical Volume
sudo lvcreate -L 50G -n lv_home vg_data

# Skapa filsystem
sudo mkfs.ext4 /dev/vg_data/lv_home

# Mounta
sudo mount /dev/vg_data/lv_home /home

# Utöka LV
sudo lvextend -L +20G /dev/vg_data/lv_home
sudo resize2fs /dev/vg_data/lv_home    # ext4
# eller
sudo xfs_growfs /home                   # xfs

# Visa info
sudo pvs    # Physical volumes
sudo vgs    # Volume groups
sudo lvs    # Logical volumes
```

---

## Praktiska Övningar

### Övning 1: Diskanalys

```bash
# 1. Visa diskutrymme
df -h

# 2. Hitta vad som tar plats
du -sh /var/*

# 3. Hitta stora filer
sudo find /var -type f -size +10M -exec ls -lh {} \;
```

### Övning 2: Cleanup

```bash
# Rensa gamla kernels (Ubuntu)
sudo apt autoremove

# Rensa apt cache
sudo apt clean

# Rensa journalctl
sudo journalctl --vacuum-time=7d

# Hitta och ta bort .log-filer äldre än 30 dagar
sudo find /var/log -name "*.log" -mtime +30 -delete
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `df -h` | Visa ledigt utrymme |
| `du -sh` | Katalogstorlek |
| `lsblk` | Lista blockenheter |
| `fdisk` | Partitionera |
| `mkfs.ext4` | Skapa filsystem |
| `mount` | Mounta filsystem |
| `umount` | Unmount |
| `/etc/fstab` | Permanent mount |
| `pvs/vgs/lvs` | LVM-info |

---

## Nästa Steg

Du kan nu hantera disk och storage. Nästa node: **Networking Basics** — IP, interfaces och routing.
"""
            },
            {
                "title": "Networking Basics",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 90,
                "content": r"""# Networking Basics

## Varför detta är kritiskt

> "Every modern application is networked. API calls, database connections, load balancers — all depend on networking. When something can't connect, you need to diagnose: Is it DNS? Firewall? Routing? This node gives you the tools."

---

## Network Interfaces

### Visa interfaces

```bash
# Modern (ip command)
ip addr
ip a            # Kortform

# Klassisk (äldre system)
ifconfig

# Bara interface-namn
ip link show

# Specifikt interface
ip addr show eth0
```

### ip addr output

```bash
$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP>
    link/loopback 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    link/ether 00:11:22:33:44:55
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

### Hantera interfaces

```bash
# Stäng av interface
sudo ip link set eth0 down

# Sätt på
sudo ip link set eth0 up

# Sätt IP-adress
sudo ip addr add 192.168.1.100/24 dev eth0

# Ta bort IP
sudo ip addr del 192.168.1.100/24 dev eth0
```

---

## Connectivity Testing

### ping — Test reachability

```bash
# Enkel ping
ping google.com

# Antal paket
ping -c 4 google.com

# Interval (0.2 sek)
ping -i 0.2 google.com

# Quiet (bara sammanfattning)
ping -q -c 10 google.com
```

### traceroute — Path to destination

```bash
# Visa vägen
traceroute google.com

# Använd ICMP (som ping)
traceroute -I google.com

# TCP (om ICMP blockeras)
traceroute -T -p 443 google.com

# mtr (kombinerar ping + traceroute)
mtr google.com
```

---

## Port & Connection Analysis

### ss — Socket Statistics (modern)

```bash
# Visa alla lyssnande portar
ss -tuln

# Förklaring:
# -t = TCP
# -u = UDP
# -l = Listening
# -n = Numeric (visa port-nummer, inte namn)

# Visa etablerade connections
ss -tun

# Med process-info
ss -tulnp

# Specifik port
ss -tuln | grep :80

# Visa alla (inkl. sockets)
ss -a
```

### netstat — Klassiskt (äldre)

```bash
# Samma som ss -tuln
netstat -tuln

# Med processer
netstat -tulnp

# Routing table
netstat -rn
```

---

## Routing

### Visa routes

```bash
# Modern
ip route
ip r

# Klassisk
route -n
netstat -rn
```

### Default gateway

```bash
# Visa default route
ip route | grep default
# default via 192.168.1.1 dev eth0

# Lägg till default route
sudo ip route add default via 192.168.1.1

# Ta bort route
sudo ip route del default
```

---

## Hostname & DNS

### Hostname

```bash
# Visa hostname
hostname

# Visa alla namn
hostnamectl

# Sätt hostname (permanent)
sudo hostnamectl set-hostname myserver

# Tillfälligt
sudo hostname tempname
```

### DNS-lookup

```bash
# Enkel lookup
host google.com

# Detaljerad
dig google.com

# Bara IP
dig +short google.com

# Reverse lookup
dig -x 8.8.8.8

# nslookup (enklare)
nslookup google.com
```

### DNS-konfiguration

```bash
# Nuvarande DNS-servrar
cat /etc/resolv.conf

# I moderna system (systemd-resolved)
resolvectl status

# DNS cache flush
sudo systemd-resolve --flush-caches
```

---

## ARP (Address Resolution Protocol)

```bash
# Visa ARP-cache
arp -a
ip neigh

# Ta bort entry
sudo ip neigh del 192.168.1.1 dev eth0
```

---

## Praktiska Debugging-mönster

### "Jag kan inte nå X"

```bash
# 1. Har jag IP?
ip addr

# 2. Kan jag nå gateway?
ping -c 2 $(ip route | grep default | awk '{print $3}')

# 3. Kan jag nå DNS?
ping -c 2 8.8.8.8

# 4. Fungerar DNS-resolution?
host google.com

# 5. Kan jag nå målet?
ping -c 2 target.com

# 6. Är porten öppen?
nc -zv target.com 443
```

### Kontrollera lyssnande tjänster

```bash
# Vad lyssnar på port 80?
ss -tulnp | grep :80

# Alla lyssnande
ss -tulnp
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `ip addr` | Visa interfaces/IP |
| `ip route` | Visa routing |
| `ping` | Testa connectivity |
| `traceroute` | Visa nätverksväg |
| `ss -tuln` | Lyssnande portar |
| `dig` / `host` | DNS-lookup |
| `hostname` | Visa/sätt hostname |

---

## Nästa Steg

Du har nu grunderna i nätverksdiagnostik. Nästa node: **DNS & Resolution** — fördjupning i DNS.
"""
            },
            {
                "title": "DNS & Name Resolution",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 75,
                "content": r"""# DNS & Name Resolution

## Varför detta är kritiskt

> "DNS is the phone book of the internet. When DNS fails, nothing works — users can't reach your site, services can't connect. Understanding DNS is essential for troubleshooting connectivity issues."

---

## Så fungerar DNS

```
┌─────────────────────────────────────────────────────────────┐
│                     DNS RESOLUTION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   User: "google.com"                                        │
│          │                                                  │
│          ▼                                                  │
│   1. Check /etc/hosts                                       │
│          │ (not found)                                      │
│          ▼                                                  │
│   2. Check local DNS cache                                  │
│          │ (not found)                                      │
│          ▼                                                  │
│   3. Query DNS resolver (/etc/resolv.conf)                  │
│          │                                                  │
│          ▼                                                  │
│   4. Resolver → Root servers → .com → google.com           │
│          │                                                  │
│          ▼                                                  │
│   5. Return IP: 142.250.185.78                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## DNS Records

| Record | Syfte | Exempel |
|--------|-------|---------|
| A | IPv4-adress | example.com → 93.184.216.34 |
| AAAA | IPv6-adress | example.com → 2606:2800:220:1:... |
| CNAME | Alias | www.example.com → example.com |
| MX | Mail server | example.com → mail.example.com |
| TXT | Text (SPF, DKIM) | "v=spf1 include:..." |
| NS | Nameservers | example.com → ns1.example.com |
| PTR | Reverse lookup | IP → hostname |

---

## dig — DNS Information Groper

```bash
# Enkel lookup
dig example.com

# Bara svaret
dig +short example.com

# Specifik record-typ
dig example.com A
dig example.com MX
dig example.com TXT
dig example.com NS

# Alla records
dig example.com ANY

# Fråga specifik DNS-server
dig @8.8.8.8 example.com

# Reverse lookup
dig -x 93.184.216.34

# Trace (visa hela resolution-kedjan)
dig +trace example.com
```

### dig output förklarad

```bash
$ dig example.com

; <<>> DiG 9.16.1 <<>> example.com
;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            3600    IN      A       93.184.216.34

;; Query time: 24 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Dec 01 10:00:00 UTC 2025
;; MSG SIZE  rcvd: 56
```

---

## host & nslookup

### host (enklare)

```bash
# Enkel lookup
host example.com

# Specifik typ
host -t MX example.com
host -t TXT example.com

# Använd specifik DNS
host example.com 8.8.8.8
```

### nslookup (interaktiv)

```bash
# Enkel
nslookup example.com

# Med specifik server
nslookup example.com 8.8.8.8

# Interaktivt läge
nslookup
> set type=MX
> example.com
> exit
```

---

## Lokala DNS-filer

### /etc/hosts

Lokal mappning som kollas FÖRST.

```bash
# Visa
cat /etc/hosts

# Format:
# IP        hostname    [aliases]
127.0.0.1   localhost
192.168.1.10 myserver myserver.local

# Användning:
# - Utveckling: blockera sajter
# - Testing: peka domän till lokal IP
```

```bash
# Lägg till entry
echo "192.168.1.50 testserver" | sudo tee -a /etc/hosts
```

### /etc/resolv.conf

DNS-resolver konfiguration.

```bash
cat /etc/resolv.conf

# Typiskt innehåll:
nameserver 8.8.8.8
nameserver 8.8.4.4
search example.com
```

**OBS:** I moderna system hanteras detta av systemd-resolved:
```bash
# Visa verklig config
resolvectl status

# Flush DNS cache
sudo systemd-resolve --flush-caches
```

---

## DNS Debugging

### "DNS fungerar inte"

```bash
# 1. Testa med IP (bypass DNS)
ping 8.8.8.8
# Funkar? → Problem är DNS, inte nätverk

# 2. Testa DNS-resolution
dig @8.8.8.8 example.com
# Funkar? → Lokal resolver är problemet

# 3. Kolla resolv.conf
cat /etc/resolv.conf

# 4. Testa lokal resolver
dig example.com
```

### Vanliga problem

| Symptom | Trolig orsak |
|---------|--------------|
| "Name or service not known" | DNS-resolution misslyckades |
| Timeout | DNS-server nås ej |
| NXDOMAIN | Domänen finns inte |
| SERVFAIL | DNS-server fel |

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `dig domain` | DNS lookup |
| `dig +short` | Bara IP |
| `dig @8.8.8.8` | Specifik DNS |
| `host domain` | Enkel lookup |
| `/etc/hosts` | Lokal mappning |
| `/etc/resolv.conf` | DNS-servrar |

---

## Nästa Steg

Du förstår nu DNS. Nästa node: **Firewall** — kontrollera nätverkstrafik.
"""
            },
            {
                "title": "Firewall Management",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# Firewall Management

## Varför detta är kritiskt

> "A server without a firewall is an open door. Every port you leave open is a potential attack vector. Firewalls are your first line of defense — they decide what traffic is allowed in and out."

---

## Firewall-verktyg

```
┌─────────────────────────────────────────────────────────────┐
│              LINUX FIREWALL LANDSCAPE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   iptables     → Klassiskt, kraftfullt, komplext           │
│   nftables     → Modern ersättare för iptables             │
│   ufw          → Ubuntu Firewall (frontend för iptables)   │
│   firewalld    → RHEL/CentOS (frontend för nftables)       │
│                                                             │
│   Kernel: netfilter (underliggande)                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## UFW (Uncomplicated Firewall)

Standard på Ubuntu. Enkelt och effektivt.

### Aktivera/inaktivera

```bash
# Status
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered

# Aktivera
sudo ufw enable

# Inaktivera
sudo ufw disable

# Återställ till default
sudo ufw reset
```

### Default policies

```bash
# Neka allt inkommande, tillåt utgående (rekommenderat)
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Tillåt/neka portar

```bash
# Tillåt SSH
sudo ufw allow ssh
sudo ufw allow 22

# Tillåt HTTP/HTTPS
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow http
sudo ufw allow https

# Tillåt port range
sudo ufw allow 6000:6007/tcp

# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100

# Tillåt från nätverk till port
sudo ufw allow from 192.168.1.0/24 to any port 22

# Neka
sudo ufw deny 23

# Neka från IP
sudo ufw deny from 10.0.0.5
```

### Ta bort regler

```bash
# Med nummer
sudo ufw status numbered
sudo ufw delete 2

# Med regel
sudo ufw delete allow 80
```

### Application profiles

```bash
# Lista tillgängliga profiler
sudo ufw app list

# Info om profil
sudo ufw app info "Nginx Full"

# Tillåt application
sudo ufw allow "Nginx Full"
sudo ufw allow "OpenSSH"
```

---

## iptables (klassiskt)

Kraftfullt men komplext. Bra att förstå grunderna.

### Se regler

```bash
# Lista alla regler
sudo iptables -L -n -v

# Lista med radnummer
sudo iptables -L --line-numbers

# Specifik chain
sudo iptables -L INPUT -n -v
```

### Chains

```
┌─────────────────────────────────────────────────────────────┐
│                    IPTABLES CHAINS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   INPUT       → Trafik TO this server                      │
│   OUTPUT      → Trafik FROM this server                    │
│   FORWARD     → Trafik THROUGH this server (routing)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Grundläggande regler

```bash
# Tillåt SSH (port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Tillåt established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Neka allt annat
sudo iptables -A INPUT -j DROP

# Tillåt loopback
sudo iptables -A INPUT -i lo -j ACCEPT
```

### Spara regler

```bash
# Ubuntu
sudo apt install iptables-persistent
sudo netfilter-persistent save

# Manuellt
sudo iptables-save > /etc/iptables/rules.v4
sudo iptables-restore < /etc/iptables/rules.v4
```

---

## firewalld (RHEL/CentOS)

```bash
# Status
sudo firewall-cmd --state
sudo firewall-cmd --list-all

# Aktivera service
sudo systemctl enable --now firewalld

# Tillåt port
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --reload

# Tillåt service
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

# Lista zoner
sudo firewall-cmd --get-zones
sudo firewall-cmd --get-default-zone
```

---

## Praktisk Server-setup

```bash
# 1. Sätt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Tillåt SSH (VIKTIGT - gör först!)
sudo ufw allow ssh

# 3. Tillåt webbtrafik
sudo ufw allow 80
sudo ufw allow 443

# 4. Aktivera
sudo ufw enable

# 5. Verifiera
sudo ufw status
```

---

## Sammanfattning

| Kommando (ufw) | Funktion |
|----------------|----------|
| `ufw status` | Visa status |
| `ufw enable` | Aktivera |
| `ufw allow 22` | Tillåt port |
| `ufw deny 23` | Neka port |
| `ufw delete` | Ta bort regel |
| `ufw reset` | Återställ |

---

## Nästa Steg

Du kan nu konfigurera brandväggar. Nästa node: **SSH & Remote Access** — säker fjärråtkomst.
"""
            },
            {
                "title": "SSH & Remote Access",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# SSH & Remote Access

## Varför detta är kritiskt

> "SSH is how you access servers. Period. Every production server, every cloud instance, every container — you reach them through SSH. Master SSH and you can manage anything, anywhere."

---

## SSH Grunderna

### Ansluta

```bash
# Grundläggande
ssh user@hostname
ssh user@192.168.1.10

# Specifik port
ssh -p 2222 user@hostname

# Med verbose (debugging)
ssh -v user@hostname
ssh -vvv user@hostname    # Extra verbose
```

### SSH-nycklar (bästa praxis)

Lösenord är osäkert. Använd nycklar.

```bash
# Generera nyckelpar
ssh-keygen -t ed25519 -C "your@email.com"

# Alternativ: RSA (äldre men kompatibelt)
ssh-keygen -t rsa -b 4096

# Nycklar sparas i:
# ~/.ssh/id_ed25519      (privat - SKYDDA!)
# ~/.ssh/id_ed25519.pub  (publik - dela fritt)
```

### Kopiera nyckel till server

```bash
# Automatiskt
ssh-copy-id user@hostname

# Manuellt
cat ~/.ssh/id_ed25519.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Permissions (KRITISKT!)

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
```

---

## ~/.ssh/config

Spara inställningar för olika hosts.

```bash
# ~/.ssh/config
Host prod
    HostName production.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key

Host dev
    HostName dev.example.com
    User developer
    Port 2222

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

```bash
# Nu kan du bara skriva:
ssh prod
ssh dev
```

---

## Kopiera filer

### scp — Secure Copy

```bash
# Fil till server
scp file.txt user@hostname:/path/to/destination/

# Fil från server
scp user@hostname:/path/to/file.txt ./local/

# Katalog (rekursiv)
scp -r folder/ user@hostname:/path/

# Med port
scp -P 2222 file.txt user@hostname:/path/
```

### sftp — Interactive

```bash
sftp user@hostname

# Inuti sftp:
ls              # Lista remote
lls             # Lista local
cd /path        # Byt remote dir
lcd /path       # Byt local dir
get file.txt    # Ladda ner
put file.txt    # Ladda upp
exit
```

### rsync — Synkronisering (bäst för backup)

```bash
# Synka katalog (arkiv-läge)
rsync -avz source/ user@hostname:/destination/

# Med delete (spegla exakt)
rsync -avz --delete source/ user@hostname:/destination/

# Torrkörning
rsync -avzn source/ user@hostname:/destination/

# Progress
rsync -avz --progress source/ user@hostname:/destination/
```

---

## Port Forwarding & Tunneling

### Local forwarding

Åtkomst till remote service via lokal port.

```bash
# Syntax: ssh -L local_port:remote_host:remote_port

# Databas på remote server (port 5432) → localhost:5432
ssh -L 5432:localhost:5432 user@dbserver

# Nu kan du ansluta lokalt:
psql -h localhost -p 5432
```

### Remote forwarding

Exponera lokal service till remote.

```bash
# Syntax: ssh -R remote_port:local_host:local_port

# Din lokala port 3000 → remote port 8080
ssh -R 8080:localhost:3000 user@server
```

### Dynamic forwarding (SOCKS proxy)

```bash
# Skapa SOCKS proxy
ssh -D 1080 user@hostname

# Konfigurera browser att använda localhost:1080 som SOCKS proxy
```

---

## SSH-agent

Håll nycklar i minnet så du slipper skriva lösenord.

```bash
# Starta agent
eval $(ssh-agent)

# Lägg till nyckel
ssh-add ~/.ssh/id_ed25519

# Lista nycklar
ssh-add -l

# Ta bort alla
ssh-add -D
```

### Agent forwarding

```bash
# Tillåt servern använda dina lokala nycklar
ssh -A user@server

# I config:
Host server
    ForwardAgent yes
```

---

## SSH Security

### /etc/ssh/sshd_config

```bash
# Viktiga inställningar:
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Port 22    # Överväg att byta

# Efter ändring:
sudo systemctl restart sshd
```

### Best practices

1. **Disable root login**
2. **Disable password auth** (bara nycklar)
3. **Använd ed25519 eller RSA 4096**
4. **Byt port** (security through obscurity)
5. **Använd fail2ban**

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `ssh user@host` | Anslut |
| `ssh-keygen -t ed25519` | Skapa nyckel |
| `ssh-copy-id` | Kopiera nyckel |
| `scp` | Kopiera filer |
| `rsync -avz` | Synkronisera |
| `ssh -L` | Local forwarding |
| `ssh-agent` | Nyckelhantering |

---

## Nästa Steg

Du behärskar nu SSH. Nästa node: **Archiving & Compression** — tar, gzip och backup.
"""
            },
            {
                "title": "Archiving & Compression",
                "difficulty": "easy",
                "estimated_minutes": 40,
                "xp_reward": 65,
                "content": r"""# Archiving & Compression

## Varför detta är kritiskt

> "Backups, deployments, log rotation — all involve archives. A 10GB log file becomes 500MB compressed. Knowing tar is mandatory for any sysadmin."

---

## tar — Tape Archive

`tar` arkiverar filer (samlar till en fil). Kombineras ofta med kompression.

### Skapa arkiv

```bash
# Skapa arkiv (-c = create, -v = verbose, -f = file)
tar -cvf archive.tar folder/

# Med gzip-kompression (-z)
tar -czvf archive.tar.gz folder/

# Med bzip2 (-j) - bättre kompression, långsammare
tar -cjvf archive.tar.bz2 folder/

# Med xz (-J) - bäst kompression, långsammast
tar -cJvf archive.tar.xz folder/
```

### Extrahera arkiv

```bash
# Extrahera
tar -xvf archive.tar

# Extrahera gzip
tar -xzvf archive.tar.gz

# Extrahera bzip2
tar -xjvf archive.tar.bz2

# Extrahera till specifik katalog
tar -xzvf archive.tar.gz -C /destination/

# Lista innehåll (utan att extrahera)
tar -tvf archive.tar.gz
```

### Vanliga mönster

```bash
# Backup av katalog
tar -czvf backup_$(date +%Y%m%d).tar.gz /var/www/

# Exkludera filer
tar -czvf backup.tar.gz --exclude='*.log' --exclude='node_modules' folder/

# Extrahera specifik fil
tar -xzvf archive.tar.gz path/to/file.txt
```

---

## Komprimeringsverktyg

### gzip / gunzip

```bash
# Komprimera (ersätter original)
gzip file.txt           # → file.txt.gz

# Behåll original
gzip -k file.txt

# Dekomprimera
gunzip file.txt.gz
gzip -d file.txt.gz

# Visa info
gzip -l file.txt.gz
```

### bzip2 / bunzip2

```bash
bzip2 file.txt          # → file.txt.bz2
bunzip2 file.txt.bz2
```

### xz

```bash
xz file.txt             # → file.txt.xz
xz -d file.txt.xz
```

### Jämförelse

| Format | Kompression | Hastighet |
|--------|-------------|-----------|
| gzip | Bra | Snabb |
| bzip2 | Bättre | Medium |
| xz | Bäst | Långsam |

---

## zip / unzip

Kompatibelt med Windows.

```bash
# Skapa zip
zip archive.zip file1 file2
zip -r archive.zip folder/

# Extrahera
unzip archive.zip
unzip archive.zip -d /destination/

# Lista innehåll
unzip -l archive.zip

# Lösenordsskydda
zip -e secure.zip file.txt
```

---

## Praktiska Mönster

### Daglig backup

```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czvf /backup/www_$DATE.tar.gz /var/www/html/
find /backup -name "www_*.tar.gz" -mtime +7 -delete
```

### Deployment

```bash
# Skapa release
tar -czvf release-1.2.3.tar.gz --exclude='.git' --exclude='node_modules' .

# Deploy
tar -xzvf release-1.2.3.tar.gz -C /var/www/app/
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `tar -czvf` | Skapa .tar.gz |
| `tar -xzvf` | Extrahera .tar.gz |
| `tar -tvf` | Lista innehåll |
| `gzip` | Komprimera |
| `gunzip` | Dekomprimera |
| `zip -r` | Skapa zip |
| `unzip` | Extrahera zip |

---

## Nästa Steg

Du kan nu arkivera och komprimera. Nästa node: **Cron & Scheduling** — automatisera uppgifter.
"""
            },
            {
                "title": "Cron & Scheduling",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 75,
                "content": r"""# Cron & Scheduling

## Varför detta är kritiskt

> "Automation utan scheduling är manuellt arbete. Backups, logrotation, deployments — allt körs på schema. Cron är DevOps-hjärtat."

---

## Crontab Grunderna

### Syntax

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, 0=Sunday)
│ │ │ │ │
* * * * * command
```

### Hantera crontab

```bash
# Redigera din crontab
crontab -e

# Lista din crontab
crontab -l

# Ta bort alla jobb
crontab -r

# Redigera annan användares (root)
sudo crontab -u nginx -e
```

---

## Vanliga Mönster

```bash
# Varje minut
* * * * * /script.sh

# Varje timme
0 * * * * /script.sh

# Varje dag kl 03:00
0 3 * * * /backup.sh

# Måndag-fredag kl 09:00
0 9 * * 1-5 /report.sh

# Första i varje månad
0 0 1 * * /monthly.sh

# Var 5:e minut
*/5 * * * * /check.sh

# Var 2:a timme
0 */2 * * * /script.sh
```

### Specialuttryck

```bash
@reboot    # Vid start
@yearly    # 0 0 1 1 *
@monthly   # 0 0 1 * *
@weekly    # 0 0 * * 0
@daily     # 0 0 * * *
@hourly    # 0 * * * *
```

---

## System Cron Directories

```bash
/etc/cron.d/        # Systemjobb
/etc/cron.hourly/   # Körs varje timme
/etc/cron.daily/    # Körs varje dag
/etc/cron.weekly/   # Körs varje vecka
/etc/cron.monthly/  # Körs varje månad
```

---

## Praktiskt Exempel

```bash
# Backup varje natt kl 02:00
0 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1

# SSL-cert renewal måndag kl 03:00
0 3 * * 1 certbot renew --quiet

# Disk cleanup söndag kl 04:00
0 4 * * 0 find /tmp -mtime +7 -delete
```

---

## Systemd Timers (Modernt Alternativ)

```bash
# Lista timers
systemctl list-timers

# Skapa timer: /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target

# Aktivera
sudo systemctl enable --now backup.timer
```

---

## Sammanfattning

| Mönster | Betydelse |
|---------|-----------|
| `* * * * *` | Varje minut |
| `0 * * * *` | Varje timme |
| `0 3 * * *` | Kl 03:00 dagligen |
| `*/5 * * * *` | Var 5:e minut |
| `0 0 * * 0` | Söndagar |

---

## Nästa Steg

Du kan nu schemalägga uppgifter. Nästa node: **Log Management** — övervaka och analysera loggar.
"""
            },
            {
                "title": "Log Management & Analysis",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 80,
                "content": r"""# Log Management & Analysis

## Varför detta är kritiskt

> "Loggar är sanningen. När något går fel är loggen ditt vittne. Utan logghantering flyger du blint."

---

## Viktiga Logfiler

```bash
/var/log/syslog       # Generell systemlogg (Debian/Ubuntu)
/var/log/messages     # Generell systemlogg (RHEL/CentOS)
/var/log/auth.log     # Autentisering (Debian/Ubuntu)
/var/log/secure       # Autentisering (RHEL/CentOS)
/var/log/kern.log     # Kernel-meddelanden
/var/log/dmesg        # Boot-meddelanden
/var/log/nginx/       # Nginx-loggar
/var/log/apache2/     # Apache-loggar
```

---

## journalctl (Systemd)

```bash
# Alla loggar
journalctl

# Senaste 100 rader
journalctl -n 100

# Följ live
journalctl -f

# Specifik enhet
journalctl -u nginx.service

# Sedan idag
journalctl --since today

# Tidsintervall
journalctl --since "2024-01-01" --until "2024-01-02"

# Senaste timmen
journalctl --since "1 hour ago"

# Kernel-meddelanden
journalctl -k

# Felmeddelanden
journalctl -p err

# JSON-output
journalctl -o json-pretty
```

---

## Klassisk Logganalys

```bash
# Visa slutet av logg
tail -f /var/log/syslog

# Sök i loggar
grep "error" /var/log/syslog
grep -i "failed" /var/log/auth.log

# Räkna förekomster
grep -c "404" /var/log/nginx/access.log

# Unika IP-adresser
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head

# Topp 10 sökvägar
awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

---

## dmesg - Kernel Loggar

```bash
# Alla kernel-meddelanden
dmesg

# Följ nya meddelanden
dmesg -w

# Med tidsstämplar
dmesg -T

# Fel och varningar
dmesg -l err,warn

# USB-enheter
dmesg | grep -i usb
```

---

## Logrotate

Konfiguration: `/etc/logrotate.d/`

```bash
# Exempel: /etc/logrotate.d/nginx
/var/log/nginx/*.log {
    daily           # Rotera dagligen
    rotate 14       # Behåll 14 filer
    compress        # Komprimera
    delaycompress   # Vänta en cykel
    missingok       # OK om saknas
    notifempty      # Skippa tomma
    create 0640 www-data adm
    sharedscripts
    postrotate
        systemctl reload nginx > /dev/null 2>&1 || true
    endscript
}
```

```bash
# Testa config
sudo logrotate -d /etc/logrotate.conf

# Tvinga rotation
sudo logrotate -f /etc/logrotate.d/nginx
```

---

## Inloggningshistorik

```bash
# Senaste inloggningar
last

# Misslyckade försök
lastb

# Vem är inloggad
who
w

# Användares senaste login
lastlog
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `journalctl -u service` | Service-loggar |
| `journalctl -f` | Följ live |
| `tail -f` | Följ fil |
| `dmesg -T` | Kernel med tid |
| `last` | Inloggningshistorik |
| `logrotate` | Hantera loggfiler |

---

## Nästa Steg

Du kan nu analysera loggar. Nästa node: **Performance Monitoring** — övervaka systemet.
"""
            },
            {
                "title": "Performance Monitoring",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 90,
                "content": r"""# Performance Monitoring

## Varför detta är kritiskt

> "Performance är UX. En långsam server är en dålig server. Du måste kunna identifiera flaskhalsar — CPU, minne, disk, nätverk."

---

## Snabb Överblick

### uptime

```bash
$ uptime
 14:30:01 up 45 days, 3:22, 2 users, load average: 0.52, 0.58, 0.59
#                                                   1m   5m   15m

# Load average:
# < CPU-kärnor = OK
# > CPU-kärnor = Överbelastat
```

### top / htop

```bash
# top - grundläggande
top

# htop - bättre UI
htop

# Viktiga kolumner:
# %CPU - CPU-användning
# %MEM - Minnesanvändning
# TIME+ - Total CPU-tid
# COMMAND - Processnamn

# top shortcuts:
# P - Sortera på CPU
# M - Sortera på minne
# k - Döda process
# q - Avsluta
```

---

## CPU-analys

### mpstat

```bash
# CPU-statistik per kärna
mpstat -P ALL 1

# Förklaring:
# %usr  - User-mode
# %sys  - Kernel-mode
# %iowait - Väntar på I/O
# %idle - Ledig
```

### vmstat

```bash
# Snapshot var 2:a sekund
vmstat 2

# Output förklaring:
# procs: r=runnable, b=blocked
# memory: swpd, free, buff, cache
# swap: si=swap in, so=swap out
# io: bi=blocks in, bo=blocks out
# system: in=interrupts, cs=context switches
# cpu: us, sy, id, wa, st
```

---

## Minnesanalys

### free

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:          15Gi        8.2Gi       1.2Gi       512Mi       5.8Gi       6.5Gi
Swap:          4Gi        0.0Gi       4.0Gi

# Viktigt: Titta på "available", inte "free"
# buff/cache kan frigöras vid behov
```

### Minnesläckor

```bash
# Topp minnesanvändare
ps aux --sort=-%mem | head

# Specifik process
pmap -x <PID>

# Detaljerad
cat /proc/<PID>/status | grep -i mem
```

---

## Diskanalys

### iostat

```bash
# Disk I/O statistik
iostat -xz 1

# Viktiga kolumner:
# r/s, w/s - Reads/writes per sekund
# rkB/s, wkB/s - KB per sekund
# await - Genomsnittlig väntetid (ms)
# %util - Disk-användning
```

### iotop

```bash
# Disk I/O per process
sudo iotop

# Bara aktiva processer
sudo iotop -o
```

---

## Nätverksanalys

```bash
# Nätverksstatistik
sar -n DEV 1

# Bandbredd per interface
nload

# Anslutningar per state
ss -s

# Topp bandbredd per process
nethogs
```

---

## sar - Historisk Data

```bash
# CPU senaste timmen
sar -u

# Minne
sar -r

# Disk I/O
sar -d

# Nätverk
sar -n DEV

# Specifik tid
sar -u -s 10:00:00 -e 12:00:00
```

---

## Sammanfattning

| Resurs | Verktyg |
|--------|---------|
| CPU | top, htop, mpstat |
| Minne | free, vmstat, pmap |
| Disk | iostat, iotop |
| Nätverk | sar, nload, nethogs |
| Historik | sar |

---

## Nästa Steg

Du kan nu övervaka prestanda. Nästa node: **Troubleshooting** — felsökning av problem.
"""
            },
            {
                "title": "Linux Troubleshooting",
                "difficulty": "hard",
                "estimated_minutes": 60,
                "xp_reward": 100,
                "content": r"""# Linux Troubleshooting

## Varför detta är kritiskt

> "Production går ner. Du har 5 minuter att fixa det. Panik hjälper inte — systematisk felsökning gör det. Detta är din troubleshooting-verktygslåda."

---

## Systematisk Approach

```
1. IDENTIFY  → Vad är symptomen?
2. REPRODUCE → Kan du återskapa?
3. ISOLATE   → Var är problemet?
4. ANALYZE   → Varför händer det?
5. FIX       → Åtgärda
6. VERIFY    → Bekräfta fix
7. DOCUMENT  → Skriv ner
```

---

## Vanliga Problem & Lösningar

### "Disk Full"

```bash
# Kolla diskutrymme
df -h

# Hitta stora filer
du -sh /* 2>/dev/null | sort -rh | head

# Hitta stora filer
find / -type f -size +100M 2>/dev/null

# Rensa loggar
journalctl --vacuum-size=500M
truncate -s 0 /var/log/syslog.1

# Hitta raderade filer som fortfarande används
lsof | grep deleted
```

### "Out of Memory"

```bash
# Kolla minne
free -h

# OOM-killed processer
dmesg | grep -i "killed process"
journalctl -k | grep -i oom

# Topp minnesanvändare
ps aux --sort=-%mem | head -10

# Rensa cache (försiktigt!)
sync; echo 3 > /proc/sys/vm/drop_caches
```

### "Can't Connect"

```bash
# Kolla om tjänsten kör
systemctl status nginx

# Kolla lyssnande portar
ss -tlnp | grep :80

# Kolla firewall
sudo iptables -L -n
sudo ufw status

# DNS-problem
dig example.com
nslookup example.com

# Testa anslutning
curl -v http://localhost
telnet localhost 80
nc -zv localhost 80
```

### "Process Hangs"

```bash
# Hitta hängande process
ps aux | grep -i <process>

# Vad gör den?
strace -p <PID>

# Öppna filer
lsof -p <PID>

# Döda
kill <PID>
kill -9 <PID>  # Tvinga

# Alla av en typ
pkill -9 nginx
```

---

## Kraftfulla Verktyg

### strace - Systemanrop

```bash
# Spåra process
strace -p <PID>

# Starta med trace
strace -f ./script.sh

# Bara nätverksanrop
strace -e network ./app

# Med tidsstämplar
strace -t -p <PID>
```

### lsof - Öppna filer

```bash
# Allt som en process har öppet
lsof -p <PID>

# Vem använder en port?
lsof -i :80

# Vem använder en fil?
lsof /var/log/syslog

# Raderade men öppna filer
lsof +L1
```

### tcpdump - Nätverkstrafik

```bash
# All trafik på interface
sudo tcpdump -i eth0

# Specifik port
sudo tcpdump -i any port 443

# Spara till fil
sudo tcpdump -i eth0 -w capture.pcap
```

---

## Boot-problem

### GRUB Recovery

```bash
# I GRUB-menyn, tryck 'e' för att redigera

# Lägg till i linux-raden:
init=/bin/bash

# Eller för single user:
single
# eller
1
```

### Emergency Mode

```bash
# Systemd emergency
systemctl emergency

# Rescue mode
systemctl rescue

# Från GRUB: lägg till
systemd.unit=emergency.target
```

### Filsystem-problem

```bash
# Kolla filsystem (unmounted)
fsck /dev/sda1

# Tvinga check vid boot
touch /forcefsck
# eller
shutdown -rF now
```

---

## Checklista vid Problem

```
□ Kolla loggar: journalctl -xe
□ Kolla disk: df -h
□ Kolla minne: free -h
□ Kolla CPU: top/htop
□ Kolla nätverk: ss -tlnp
□ Kolla processer: ps aux
□ Kolla senaste ändringar: last, history
□ Kolla firewall: iptables -L
□ Kolla DNS: dig/nslookup
□ Kolla tjänster: systemctl status
```

---

## Sammanfattning

| Problem | Första kommando |
|---------|-----------------|
| Disk full | `df -h` |
| Minne slut | `free -h` |
| Kan inte ansluta | `ss -tlnp` |
| Process hänger | `strace -p PID` |
| Boot-problem | GRUB recovery |

---

## Grattis! 🎉

Du har slutfört **Linux Mastery SkillsMap**!

Du kan nu:
- Hantera processer och tjänster
- Navigera och manipulera filer
- Konfigurera användare och behörigheter
- Övervaka och felsöka system
- Automatisera med cron
- Analysera loggar och prestanda

**Nästa steg:** Docker SkillsMap → Containerisering
"""
            },
            {
                "title": "Process Management Mastery",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 80,
                "content": r"""# Process Management Mastery

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
            },
            {
                "title": "File System Navigation",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 60,
                "content": r"""# File System Navigation

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
find /var/log -name "*.log" -exec ls -lh {} \;

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
            },
            {
                "title": "File Operations Mastery",
                "difficulty": "easy",
                "estimated_minutes": 50,
                "xp_reward": 70,
                "content": r"""# File Operations Mastery

## Varför detta är kritiskt

> "Every deployment, every backup, every configuration change involves file operations. One wrong `rm -rf` can end careers. One missing `-p` in mkdir can break a deployment. Master these commands — they're your daily bread."

---

## Skapa filer och kataloger

### touch — Skapa tomma filer / Uppdatera tidsstämpel

```bash
# Skapa en tom fil
touch newfile.txt

# Skapa flera filer
touch file1.txt file2.txt file3.txt

# Uppdatera tidsstämpel på befintlig fil
touch existing_file.txt

# Sätt specifik tidsstämpel
touch -t 202512011200 file.txt    # ÅÅÅÅMMDDTTMM

# Använd annan fils tidsstämpel
touch -r reference.txt target.txt
```

**Pro Tip:** `touch` skapar INTE filen om den inte existerar och du använder `-c`:
```bash
touch -c maybe_exists.txt   # Skapar INTE om den inte finns
```

### mkdir — Skapa kataloger

```bash
# Skapa en katalog
mkdir projects

# Skapa med mellanliggande kataloger (-p = parents)
mkdir -p projects/webapp/src/components

# Skapa flera kataloger
mkdir dir1 dir2 dir3

# Skapa med specifika permissions
mkdir -m 755 secure_folder

# Verbose (visa vad som skapas)
mkdir -pv deep/nested/structure
```

**KRITISKT:** Alltid använd `-p` i scripts! Utan det misslyckas kommandot om parent inte finns.

```bash
# Script-safe pattern:
mkdir -p /var/log/myapp
mkdir -p /etc/myapp/conf.d
```

---

## Kopiera filer

### cp — Copy

```bash
# Kopiera fil
cp source.txt destination.txt

# Kopiera till katalog
cp file.txt /path/to/directory/

# Kopiera flera filer till katalog
cp file1.txt file2.txt /destination/

# Kopiera katalog rekursivt (-r = recursive)
cp -r source_dir/ destination_dir/

# Bevara alla attribut (-a = archive, bäst för backups)
cp -a source_dir/ backup_dir/

# Interactive (fråga innan överskrivning)
cp -i file.txt /destination/

# Force (skriv över utan att fråga)
cp -f file.txt /destination/

# Verbose
cp -v file.txt /destination/

# Uppdatera bara om source är nyare
cp -u source.txt destination.txt
```

### Vanliga cp-kombinationer

```bash
# Backup-stil kopiering (bevarar allt)
cp -av /source/ /backup/

# Säker kopiering (frågar)
cp -iv important.txt /archive/

# Deployment-kopiering (uppdatera bara ändrade)
cp -ruv ./dist/* /var/www/html/
```

**Viktigt om trailing slash:**
```bash
cp -r folder /dest/       # Kopierar folder TILL dest → /dest/folder/
cp -r folder/ /dest/      # Kopierar INNEHÅLLET i folder → /dest/*
```

---

## Flytta och byt namn

### mv — Move / Rename

```bash
# Byt namn på fil
mv oldname.txt newname.txt

# Flytta till katalog
mv file.txt /path/to/directory/

# Flytta och byt namn
mv file.txt /path/to/directory/newname.txt

# Flytta flera filer
mv file1.txt file2.txt /destination/

# Flytta katalog
mv source_dir/ /new/location/

# Interactive
mv -i file.txt /destination/

# Force
mv -f file.txt /destination/

# Backup before overwrite
mv -b file.txt /destination/    # Skapar file.txt~

# Verbose
mv -v file.txt /destination/
```

**Pro Tip:** `mv` är atomiskt på samma filsystem — det ändrar bara metadata, inte data. Perfekt för:
```bash
# Atomisk deploy
mv /tmp/new_config.yaml /etc/app/config.yaml
```

---

## Ta bort filer och kataloger

### rm — Remove (FARLIGT!)

```bash
# Ta bort fil
rm file.txt

# Ta bort flera filer
rm file1.txt file2.txt file3.txt

# Ta bort med wildcard
rm *.log

# Ta bort katalog rekursivt (-r = recursive)
rm -r directory/

# Force (ingen fråga, ignorera icke-existerande)
rm -f file.txt

# Den FARLIGA kombinationen
rm -rf directory/          # Tar bort ALLT utan att fråga

# Interactive (säkrare)
rm -i file.txt             # Frågar för varje fil

# Interactive för mer än 3 filer
rm -I *.txt

# Verbose
rm -v file.txt
```

### ⚠️ rm -rf VARNINGAR

```bash
# ALDRIG gör detta:
rm -rf /                   # Tar bort ALLT (root protection finns nu)
rm -rf /*                  # Tar bort allt i root
rm -rf $UNDEFINED_VAR/*    # Om variabeln är tom = rm -rf /*

# SÄKRA MÖNSTER:
# Alltid använd fullständig path:
rm -rf /var/log/myapp/temp/*

# Dubbelkolla variabler:
[ -n "$DIR" ] && rm -rf "$DIR"/*

# Eller använd :? för att fånga tom variabel
rm -rf "${DIR:?Variable not set}"/*
```

### rmdir — Ta bort tomma kataloger

```bash
# Ta bort tom katalog
rmdir empty_directory/

# Ta bort parent directories om tomma
rmdir -p path/to/empty/dirs/
```

---

## Länkar (Hard & Soft)

### Förstå Inodes

```
┌─────────────────────────────────────────────────────────────┐
│                    INODE (metadata)                         │
├─────────────────────────────────────────────────────────────┤
│  Inode #: 12345                                            │
│  Type: regular file                                        │
│  Permissions: -rw-r--r--                                   │
│  Owner: user                                               │
│  Size: 4096 bytes                                          │
│  Pointers to data blocks: [block1, block2, ...]            │
└─────────────────────────────────────────────────────────────┘
           │                          │
           │                          │
    ┌──────┴──────┐            ┌──────┴──────┐
    │  file.txt   │            │  link.txt   │
    │  (filename) │            │ (hard link) │
    └─────────────┘            └─────────────┘
```

### Hard Links

Ett hard link är ett ANNAT NAMN för samma inode (samma data).

```bash
# Skapa hard link
ln original.txt hardlink.txt

# Verifiera (samma inode nummer)
ls -li original.txt hardlink.txt
# 12345 -rw-r--r-- 2 user group 100 Dec 1 original.txt
# 12345 -rw-r--r-- 2 user group 100 Dec 1 hardlink.txt
#   ^                ^
#   Samma inode     Link count = 2
```

**Hard link egenskaper:**
- Delar samma inode → exakt samma data
- Om du raderar originalet finns datan kvar (så länge en link finns)
- Kan INTE korsa filsystem
- Kan INTE länka till kataloger (undantag: . och ..)

### Soft Links (Symlinks)

Ett soft link är en PEKARE till ett filnamn (som Windows-genvägar).

```bash
# Skapa symlink
ln -s /path/to/original.txt symlink.txt

# Skapa symlink med relativ path
ln -s ../config/app.yaml current_config.yaml

# Skapa symlink till katalog
ln -s /var/log/nginx logs

# Verifiera
ls -l symlink.txt
# lrwxrwxrwx 1 user group 20 Dec 1 symlink.txt -> /path/to/original.txt
```

**Soft link egenskaper:**
- Pekar på ett FILNAMN, inte inode
- Kan korsa filsystem
- Kan länka till kataloger
- Blir "broken" om target raderas

### Praktiska symlink-mönster

```bash
# Versionshantering med symlinks
ln -s myapp-1.2.3 myapp-current
# Uppgradera:
ln -sfn myapp-1.2.4 myapp-current   # -n = no-dereference for dirs

# Config-hantering
ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/

# Snabbåtkomst
ln -s /var/log/application logs
```

---

## Avancerade operationer

### dd — Disk/Data Duplicator

`dd` kopierar data på låg nivå. Kraftfullt men farligt.

```bash
# Skapa fil med specifik storlek
dd if=/dev/zero of=testfile bs=1M count=100
# 100 MB fil fylld med nollor

# Skapa ISO från CD
dd if=/dev/cdrom of=backup.iso

# Klona hel disk (FÖRSIKTIGT!)
dd if=/dev/sda of=/dev/sdb bs=64K status=progress

# Wipe disk (DESTRUKTIVT!)
dd if=/dev/zero of=/dev/sda bs=1M status=progress
```

**dd parametrar:**
- `if=` : Input file
- `of=` : Output file
- `bs=` : Block size
- `count=` : Antal block
- `status=progress` : Visa progress

---

## Praktiska Övningar

### Övning 1: Katalogstruktur

```bash
# 1. Skapa projektstruktur
mkdir -p myproject/{src,tests,docs,config}
touch myproject/src/main.py
touch myproject/tests/test_main.py
touch myproject/README.md

# 2. Verifiera
tree myproject/

# 3. Kopiera hela strukturen
cp -a myproject/ myproject_backup/
```

### Övning 2: Symlinks

```bash
# 1. Skapa versioner
mkdir -p versions/app-{1.0,1.1,1.2}
echo "v1.0" > versions/app-1.0/version.txt
echo "v1.1" > versions/app-1.1/version.txt
echo "v1.2" > versions/app-1.2/version.txt

# 2. Skapa current symlink
ln -s app-1.2 versions/current

# 3. Läs version
cat versions/current/version.txt

# 4. "Uppgradera" till ny version
ln -sfn app-1.1 versions/current
cat versions/current/version.txt
```

### Övning 3: Säker rensning

```bash
# Skapa testfiler
mkdir -p /tmp/cleanup_test
touch /tmp/cleanup_test/file{1..10}.log
touch /tmp/cleanup_test/keep.txt

# Säker rensning (bara .log filer)
find /tmp/cleanup_test -name "*.log" -type f -delete

# Verifiera
ls /tmp/cleanup_test/
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `touch` | Skapa tom fil / uppdatera tidsstämpel |
| `mkdir -p` | Skapa katalog(er) |
| `cp -a` | Kopiera (archive mode) |
| `mv` | Flytta / byt namn |
| `rm -rf` | Ta bort rekursivt (VARNING!) |
| `ln` | Skapa hard link |
| `ln -s` | Skapa soft link (symlink) |
| `dd` | Lågnivå-kopiering |

---

## Nästa Steg

Du kan nu manipulera filer som ett proffs. Nästa node: **File Permissions** — kontrollera vem som får göra vad med dina filer.
"""
            },
            {
                "title": "File Permissions Deep Dive",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# File Permissions Deep Dive

## Varför detta är kritiskt

> "Permissions are the first line of defense. A misconfigured permission can expose sensitive data, allow unauthorized access, or break your entire application. In security audits, permissions are always checked first."

---

## Förstå Permission-modellen

### Tre kategorier

```
┌──────────────────────────────────────────────────────────────┐
│                    FILE PERMISSIONS                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   OWNER (u)          GROUP (g)         OTHERS (o)           │
│   ─────────          ─────────         ──────────           │
│   Användaren som     Alla användare    Alla andra           │
│   äger filen         i filens grupp    på systemet          │
│                                                              │
│   rwx                rwx               rwx                   │
│   ─┬─                ─┬─               ─┬─                   │
│    │                  │                 │                    │
│    ├─ r = read (läs)  │                 │                    │
│    ├─ w = write       │                 │                    │
│    └─ x = execute     │                 │                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Tolka permissions

```bash
-rwxr-xr-- 1 user group 4096 Dec 1 10:30 script.sh
│└┬┘└┬┘└┬┘
│ │  │  └── Others: r-- (read only)
│ │  └───── Group:  r-x (read + execute)
│ └──────── Owner:  rwx (read + write + execute)
└────────── Type:   - (regular file)

File types:
-  = regular file
d  = directory
l  = symbolic link
c  = character device
b  = block device
s  = socket
p  = named pipe (FIFO)
```

### Vad betyder permissions för...

**Filer:**
| Permission | Betydelse |
|------------|-----------|
| r (read) | Läsa filinnehåll |
| w (write) | Ändra filinnehåll |
| x (execute) | Köra som program |

**Kataloger:**
| Permission | Betydelse |
|------------|-----------|
| r (read) | Lista innehåll (ls) |
| w (write) | Skapa/ta bort filer i katalogen |
| x (execute) | Gå in i katalogen (cd) |

**Pro Tip:** För kataloger är `x` kritiskt — utan det kan du inte ens läsa filer inuti!

---

## chmod — Ändra permissions

### Symboliskt läge

```bash
# Syntax: chmod [who][operation][permission] file

# Who: u (user/owner), g (group), o (others), a (all)
# Operation: + (add), - (remove), = (set exactly)
# Permission: r, w, x

# Lägg till execute för owner
chmod u+x script.sh

# Ta bort write för others
chmod o-w file.txt

# Sätt exakt permissions för group
chmod g=rx file.txt

# Kombinera
chmod u+x,g-w,o-rwx file.txt

# Alla får läsa
chmod a+r file.txt

# Kopiera permissions från user till group
chmod g=u file.txt
```

### Numeriskt (oktalt) läge

```
r = 4
w = 2
x = 1

Kombinera genom addition:
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
--- = 0+0+0 = 0
```

```bash
# chmod [owner][group][others] file

# rwxr-xr-x
chmod 755 script.sh

# rw-r--r--
chmod 644 document.txt

# rw-------
chmod 600 private.key

# rwxrwxrwx (ALDRIG gör detta på produktion)
chmod 777 file.txt
```

### Vanliga permission-kombinationer

| Oktalt | Symboliskt | Användning |
|--------|------------|------------|
| 755 | rwxr-xr-x | Scripts, directories |
| 644 | rw-r--r-- | Vanliga filer |
| 600 | rw------- | SSH-nycklar, secrets |
| 700 | rwx------ | Privata scripts |
| 750 | rwxr-x--- | Group-delade scripts |
| 664 | rw-rw-r-- | Team-delade filer |
| 775 | rwxrwxr-x | Team-delade directories |

### Rekursiv chmod

```bash
# Ändra allt i katalog
chmod -R 755 directory/

# Men det sätter 755 på BÅDE filer och kataloger!
# Bättre: Separera filer och kataloger
find /path -type d -exec chmod 755 {} \;
find /path -type f -exec chmod 644 {} \;
```

---

## chown — Ändra ägare

```bash
# Ändra owner
chown newuser file.txt

# Ändra owner och group
chown newuser:newgroup file.txt

# Ändra bara group
chown :newgroup file.txt
# eller
chgrp newgroup file.txt

# Rekursiv
chown -R www-data:www-data /var/www/

# Bevara symboliska länkar (ändra inte target)
chown -h user:group symlink
```

### Praktiska exempel

```bash
# Web server files
sudo chown -R www-data:www-data /var/www/html/

# App deployment
sudo chown -R deploy:deploy /opt/myapp/

# SSH keys
chown $USER:$USER ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
```

---

## umask — Default permissions

`umask` definierar vilka permissions som SUBTRAHERAS från default.

```bash
# Default:
# Filer: 666 (rw-rw-rw-)
# Kataloger: 777 (rwxrwxrwx)

# Om umask = 022:
# Filer: 666 - 022 = 644 (rw-r--r--)
# Kataloger: 777 - 022 = 755 (rwxr-xr-x)

# Visa nuvarande umask
umask

# Sätt umask
umask 022    # Standard
umask 077    # Strikt (bara owner)
umask 002    # Tillåt group write

# Visa i symboliskt format
umask -S
```

### Permanent umask

```bash
# I ~/.bashrc eller ~/.profile:
umask 027    # Owner: full, Group: rx, Others: inget
```

---

## Special Permissions

### Setuid (SUID)

När en fil med setuid körs, körs den med ÄGARENS rättigheter.

```bash
# Exempel: passwd kan ändra /etc/shadow trots att du inte är root
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#    ^
#    s = setuid är satt

# Sätt setuid
chmod u+s executable
chmod 4755 executable

# Ta bort
chmod u-s executable
```

### Setgid (SGID)

På filer: Körs med gruppens rättigheter.
På kataloger: Nya filer ärver katalogengruppens grupp.

```bash
# På katalog - nya filer får samma grupp
chmod g+s /shared/project/
chmod 2775 /shared/project/

# Verifiera
ls -ld /shared/project/
# drwxrwsr-x 2 user devteam ... /shared/project/
#       ^
#       s = setgid

# Nya filer i denna katalog:
touch /shared/project/newfile
ls -l /shared/project/newfile
# -rw-rw-r-- 1 user devteam ... newfile
#                   ^^^^^^^
#                   Ärvd grupp!
```

### Sticky Bit

På kataloger: Bara ägaren kan radera sina egna filer (även om andra har write).

```bash
# /tmp har sticky bit
ls -ld /tmp
# drwxrwxrwt 15 root root ... /tmp
#          ^
#          t = sticky bit

# Sätt sticky bit
chmod +t /shared/
chmod 1777 /shared/
```

### Sammanfattning special permissions

| Oktalt prefix | Symboliskt | På fil | På katalog |
|---------------|------------|--------|------------|
| 4xxx | u+s | SUID - kör som ägare | (ovanligt) |
| 2xxx | g+s | SGID - kör som grupp | Nya filer ärver grupp |
| 1xxx | +t | (ovanligt) | Sticky - bara ägare raderar |

```bash
# Kombinera: SGID + Sticky
chmod 3775 /shared/

# Full special: SUID + SGID + Sticky
chmod 7755 file   # Ovanligt och ofta osäkert
```

---

## ACL (Access Control Lists)

Standard permissions är ibland inte nog. ACLs ger finare kontroll.

### Se ACLs

```bash
# Kontrollera om ACLs finns
ls -l file.txt
# -rw-rw-r--+ 1 user group ...
#           ^
#           + = ACLs finns

# Visa ACLs
getfacl file.txt
```

### Sätt ACLs

```bash
# Installation (om behövs)
sudo apt install acl

# Ge specifik användare access
setfacl -m u:anna:rwx file.txt

# Ge specifik grupp access
setfacl -m g:developers:rx file.txt

# Default ACL för katalog (ärvs av nya filer)
setfacl -d -m u:anna:rwx /shared/

# Ta bort ACL
setfacl -x u:anna file.txt

# Ta bort ALLA ACLs
setfacl -b file.txt
```

---

## Praktiska Övningar

### Övning 1: Web server permissions

```bash
# Skapa struktur
sudo mkdir -p /var/www/mysite
sudo chown -R www-data:www-data /var/www/mysite

# Sätt permissions
sudo chmod -R 755 /var/www/mysite
sudo find /var/www/mysite -type f -exec chmod 644 {} \;
```

### Övning 2: Shared project folder

```bash
# Skapa delad katalog
sudo mkdir /projects/team
sudo chgrp developers /projects/team
sudo chmod 2775 /projects/team

# Alla i "developers" grupp kan nu:
# - Skapa filer
# - Nya filer tillhör gruppen "developers"
# - Alla kan läsa varandras filer
```

### Övning 3: Säkra SSH

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `chmod 755` | Standard för scripts/dirs |
| `chmod 644` | Standard för filer |
| `chmod 600` | Secrets/private keys |
| `chmod u+s` | SUID |
| `chmod g+s` | SGID |
| `chmod +t` | Sticky bit |
| `chown user:group` | Ändra ägare |
| `umask 022` | Sätt default |
| `setfacl` | Finkorning access |

---

## Nästa Steg

Du behärskar nu Linux-permissions. Nästa node: **Text Processing** — manipulera textdata som ett proffs med grep, sed och awk.
"""
            },
            {
                "title": "Text Processing Power Tools",
                "difficulty": "medium",
                "estimated_minutes": 70,
                "xp_reward": 95,
                "content": r"""# Text Processing Power Tools

## Varför detta är kritiskt

> "In DevOps, logs are your eyes into production. Config files control everything. Data pipelines flow through text. The ability to slice, filter, and transform text is not optional — it's survival."

---

## Grundläggande filvisning

### cat — Concatenate and display

```bash
# Visa fil
cat file.txt

# Visa med radnummer
cat -n file.txt

# Visa med radnummer (bara icke-tomma)
cat -b file.txt

# Visa osynliga tecken
cat -A file.txt

# Konkatenera filer
cat file1.txt file2.txt > combined.txt

# Append till fil
cat newdata.txt >> existing.txt
```

### head & tail — Början och slutet

```bash
# Första 10 raderna (default)
head file.txt

# Första N rader
head -n 20 file.txt
head -20 file.txt

# Sista 10 raderna
tail file.txt

# Sista N rader
tail -n 20 file.txt

# Följ fil i realtid (live logs!)
tail -f /var/log/syslog

# Följ och retry om fil inte finns
tail -F /var/log/app.log

# Följ flera filer
tail -f file1.log file2.log

# Från rad N till slutet
tail -n +100 file.txt   # Från rad 100
```

**Pro Tip:** `tail -f` är din bästa vän för debugging. Kombinera med grep:
```bash
tail -f /var/log/nginx/access.log | grep --line-buffered "ERROR"
```

---

## grep — Global Regular Expression Print

`grep` är det mest använda sökverktyget.

### Grundläggande grep

```bash
# Sök efter mönster
grep "error" logfile.txt

# Case-insensitive
grep -i "error" logfile.txt

# Invertera (visa rader som INTE matchar)
grep -v "debug" logfile.txt

# Visa radnummer
grep -n "error" logfile.txt

# Räkna träffar
grep -c "error" logfile.txt

# Visa bara matchande del
grep -o "error[0-9]*" logfile.txt

# Sök i flera filer
grep "pattern" file1.txt file2.txt

# Rekursiv sökning
grep -r "TODO" ./src/

# Med filnamn
grep -H "pattern" *.txt
```

### grep med regex

```bash
# Extended regex (-E eller egrep)
grep -E "error|warning|critical" log.txt

# Begynnelse av rad
grep "^Start" file.txt

# Slutet av rad
grep "end$" file.txt

# Valfritt tecken
grep "err.r" file.txt    # error, errir, etc

# Upprepa
grep "o\+" file.txt     # En eller fler "o"
grep -E "o+" file.txt    # Samma med -E

# Teckenklasser
grep "[0-9]\+" file.txt     # Siffror
grep "[a-zA-Z]\+" file.txt  # Bokstäver

# Word boundary
grep -w "error" file.txt     # Matchar "error" men inte "errors"
```

### grep kontext

```bash
# Visa N rader efter träff
grep -A 3 "ERROR" log.txt

# Visa N rader före träff
grep -B 3 "ERROR" log.txt

# Visa N rader före OCH efter
grep -C 3 "ERROR" log.txt
```

### Praktiska grep-mönster

```bash
# Hitta IP-adresser
grep -E "\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b" access.log

# Hitta e-postadresser
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" file.txt

# Exkludera kommentarer och tomma rader
grep -v "^#" config.txt | grep -v "^$"

# Hitta funktionsdefinitioner (Python)
grep -E "^def [a-z_]+\(" *.py
```

---

## sed — Stream Editor

`sed` transformerar text rad för rad.

### Substitution (vanligast)

```bash
# Syntax: sed 's/pattern/replacement/flags'

# Ersätt första förekomsten per rad
sed 's/old/new/' file.txt

# Ersätt ALLA förekomster (global)
sed 's/old/new/g' file.txt

# Case-insensitive
sed 's/old/new/gi' file.txt

# Ändra filen på plats (-i)
sed -i 's/old/new/g' file.txt

# Med backup
sed -i.bak 's/old/new/g' file.txt

# Flera substitutioner
sed -e 's/old1/new1/g' -e 's/old2/new2/g' file.txt
```

### sed rad-operationer

```bash
# Ta bort rad 5
sed '5d' file.txt

# Ta bort rader 5-10
sed '5,10d' file.txt

# Ta bort rader som matchar
sed '/pattern/d' file.txt

# Ta bort tomma rader
sed '/^$/d' file.txt

# Ta bort kommentarer och tomma rader
sed '/^#/d; /^$/d' file.txt

# Visa bara rad 5
sed -n '5p' file.txt

# Visa rader 5-10
sed -n '5,10p' file.txt

# Visa rader som matchar
sed -n '/pattern/p' file.txt
```

### sed avancerat

```bash
# Fånga grupper
sed 's/\(.*\)@\(.*\)/User: \1, Domain: \2/' emails.txt

# Med extended regex (-E)
sed -E 's/(.*)@(.*)/User: \1, Domain: \2/' emails.txt

# Lägg till text före rad som matchar
sed '/pattern/i\New line before' file.txt

# Lägg till text efter rad som matchar
sed '/pattern/a\New line after' file.txt
```

---

## awk — Pattern-Action Language

`awk` är ett fullständigt programmeringsspråk för textbearbetning.

### Grundläggande awk

```bash
# Syntax: awk 'pattern { action }' file

# Skriv ut allt (som cat)
awk '{print}' file.txt

# Skriv ut kolumn 1
awk '{print $1}' file.txt

# Skriv ut kolumn 1 och 3
awk '{print $1, $3}' file.txt

# Med annan delimiter
awk -F':' '{print $1}' /etc/passwd

# Skriv ut sista kolumn
awk '{print $NF}' file.txt

# Skriv ut antal fält
awk '{print NF}' file.txt

# Skriv ut radnummer
awk '{print NR": "$0}' file.txt
```

### awk med villkor

```bash
# Villkor före action
awk '$3 > 100 {print $1, $3}' data.txt

# Regex-match
awk '/error/ {print}' log.txt

# Kombinera
awk '/error/ && $3 > 100 {print $1}' log.txt

# Negera
awk '!/comment/ {print}' file.txt
```

### awk inbyggda variabler

| Variabel | Betydelse |
|----------|-----------|
| $0 | Hela raden |
| $1, $2... | Fält 1, 2, ... |
| NF | Antal fält |
| NR | Radnummer |
| FS | Fältseparator (default: mellanslag) |
| OFS | Output fältseparator |
| RS | Radseparator |

### awk praktiska exempel

```bash
# Summera kolumn
awk '{sum += $3} END {print sum}' data.txt

# Genomsnitt
awk '{sum += $3; count++} END {print sum/count}' data.txt

# Unika värden (som uniq)
awk '!seen[$1]++' file.txt

# Byt ordning på kolumner
awk '{print $3, $1, $2}' file.txt

# Formaterad output
awk '{printf "%-10s %5d\n", $1, $2}' file.txt
```

---

## cut, sort, uniq — Klassiska verktyg

### cut — Extrahera fält

```bash
# Extrahera fält med delimiter
cut -d':' -f1 /etc/passwd

# Flera fält
cut -d':' -f1,3 /etc/passwd

# Fält 1 till 3
cut -d':' -f1-3 /etc/passwd

# Extrahera teckenpositioner
cut -c1-10 file.txt
```

### sort — Sortera

```bash
# Alfabetisk sortering
sort file.txt

# Numerisk sortering
sort -n numbers.txt

# Omvänd ordning
sort -r file.txt

# Sortera på kolumn
sort -t':' -k3 -n /etc/passwd

# Unik sortering
sort -u file.txt

# Human-readable storlekar (1K, 2M, etc)
sort -h sizes.txt
```

### uniq — Unika rader

```bash
# OBS: uniq kräver sorterad input!

# Ta bort duplikater
sort file.txt | uniq

# Visa bara duplikater
sort file.txt | uniq -d

# Visa bara unika
sort file.txt | uniq -u

# Räkna förekomster
sort file.txt | uniq -c

# Sortera på antal
sort file.txt | uniq -c | sort -rn
```

---

## tr — Translate characters

```bash
# Ersätt tecken
echo "hello" | tr 'a-z' 'A-Z'    # HELLO

# Ta bort tecken
echo "hello123" | tr -d '0-9'     # hello

# Squeeze upprepningar
echo "hellooo" | tr -s 'o'        # hello

# Ersätt newline med space
tr '\n' ' ' < file.txt

# Ta bort allt utom siffror
echo "abc123xyz" | tr -cd '0-9'   # 123
```

---

## wc — Word Count

```bash
# Allt: rader, ord, tecken
wc file.txt

# Bara rader
wc -l file.txt

# Bara ord
wc -w file.txt

# Bara tecken/bytes
wc -c file.txt
wc -m file.txt    # Tecken (unicode-aware)
```

---

## diff — Jämför filer

```bash
# Standard diff
diff file1.txt file2.txt

# Unified format (som git)
diff -u file1.txt file2.txt

# Side by side
diff -y file1.txt file2.txt

# Ignorera whitespace
diff -w file1.txt file2.txt

# Rekursiv (kataloger)
diff -r dir1/ dir2/
```

---

## Pipeline — Kombinera verktyg

Verklig kraft kommer från att kombinera verktyg!

```bash
# Topp 10 IP-adresser i access log
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Räkna förekomster av HTTP-status
cat access.log | awk '{print $9}' | sort | uniq -c | sort -rn

# Hitta stora filer och sortera
find /var/log -type f -exec du -h {} + | sort -rh | head -20

# Extrahera och räkna fel från log
grep -i error app.log | awk '{print $4}' | sort | uniq -c | sort -rn
```

---

## Praktiska Övningar

### Övning 1: Log-analys

```bash
# Skapa testlog
cat > /tmp/access.log << 'EOF'
192.168.1.1 - - [01/Dec/2025:10:00:00] "GET /index.html" 200 1234
192.168.1.2 - - [01/Dec/2025:10:00:01] "GET /about.html" 200 5678
192.168.1.1 - - [01/Dec/2025:10:00:02] "GET /contact.html" 404 0
192.168.1.3 - - [01/Dec/2025:10:00:03] "POST /api/login" 500 0
192.168.1.1 - - [01/Dec/2025:10:00:04] "GET /index.html" 200 1234
EOF

# 1. Räkna requests per IP
awk '{print $1}' /tmp/access.log | sort | uniq -c | sort -rn

# 2. Hitta alla 500-errors
grep " 500 " /tmp/access.log

# 3. Räkna status-koder
awk '{print $9}' /tmp/access.log | sort | uniq -c
```

---

## Sammanfattning

| Verktyg | Användning |
|---------|------------|
| `grep` | Sök mönster |
| `sed` | Ersätt och transformera |
| `awk` | Kolumnbearbetning |
| `cut` | Extrahera fält |
| `sort` | Sortera |
| `uniq` | Unika värden |
| `tr` | Ersätt tecken |
| `wc` | Räkna rader/ord |
| `diff` | Jämför filer |
| `head/tail` | Början/slutet |

---

## Nästa Steg

Du är nu en text-ninja. Nästa node: **Text Editors** — behärska Vim och Nano för att redigera filer direkt på servern.
"""
            },
            {
                "title": "Text Editors: Vim & Nano",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 75,
                "content": r"""# Text Editors: Vim & Nano

## Varför detta är kritiskt

> "You SSH into a production server. Nano isn't installed. The only editor is Vi. You need to edit a config file NOW. This is not a drill — every DevOps engineer must know at least basic Vim."

---

## Nano — The Friendly Editor

Nano är användarvänlig: alla kommandon visas längst ner.

### Starta Nano

```bash
# Öppna/skapa fil
nano file.txt

# Öppna på specifik rad
nano +15 file.txt

# Read-only
nano -v file.txt

# Med syntax highlighting
nano -Y sh script.sh
```

### Kommandon (visas längst ner)

`^` betyder Ctrl

| Kommando | Funktion |
|----------|----------|
| `^O` | Spara (Write Out) |
| `^X` | Avsluta |
| `^K` | Klipp ut rad |
| `^U` | Klistra in |
| `^W` | Sök |
| `^\` | Sök & ersätt |
| `^G` | Hjälp |
| `^C` | Visa position |
| `^_` | Gå till rad |

### Navigation

| Kommando | Funktion |
|----------|----------|
| `^A` | Början av rad |
| `^E` | Slutet av rad |
| `^Y` | Sida upp |
| `^V` | Sida ner |
| `Alt+\` | Toppen av fil |
| `Alt+/` | Botten av fil |

### Markering

```
Alt+A    → Starta markering
(flytta) → Markera text
^K       → Klipp ut
^U       → Klistra in
```

### ~/.nanorc konfiguration

```bash
cat > ~/.nanorc << 'EOF'
# Visa radnummer
set linenumbers

# Soft wrap (ingen hård radbrytning)
set softwrap

# Tab = 4 spaces
set tabsize 4
set tabstospaces

# Visa cursor-position konstant
set constantshow

# Syntax highlighting
include "/usr/share/nano/*.nanorc"
EOF
```

---

## Vim — The Powerful Editor

Vim är kraftfull men har en inlärningskurva. Det viktigaste: Vim har MODES.

### Modes (KRITISKT att förstå)

```
┌─────────────────────────────────────────────────────────────┐
│                        VIM MODES                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   NORMAL MODE (default)                                     │
│   ──────────────────────                                    │
│   Du startar här. Navigera, ta bort, kopiera.               │
│   Tryck ESC för att återgå hit.                            │
│                                                             │
│           │                                                 │
│           │ i, a, o                                         │
│           ▼                                                 │
│   INSERT MODE                                               │
│   ───────────                                               │
│   Skriv text som vanligt.                                   │
│   Tryck ESC för att gå tillbaka till Normal.               │
│                                                             │
│           │                                                 │
│           │ ESC → :                                         │
│           ▼                                                 │
│   COMMAND MODE                                              │
│   ────────────                                              │
│   Spara, avsluta, söka.                                    │
│   :w, :q, :wq                                              │
│                                                             │
│           │                                                 │
│           │ v, V, Ctrl+v                                    │
│           ▼                                                 │
│   VISUAL MODE                                               │
│   ───────────                                               │
│   Markera text.                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Det viktigaste: Avsluta Vim!

```
:q      → Avsluta (om inga ändringar)
:q!     → Avsluta utan att spara (force)
:w      → Spara
:wq     → Spara och avsluta
ZZ      → Spara och avsluta (snabbare)
```

### In i Insert Mode

| Kommando | Funktion |
|----------|----------|
| `i` | Insert före cursor |
| `I` | Insert i början av rad |
| `a` | Append efter cursor |
| `A` | Append i slutet av rad |
| `o` | Öppna ny rad under |
| `O` | Öppna ny rad över |

### Navigation i Normal Mode

```
h j k l     → Vänster, Ner, Upp, Höger
w           → Nästa ord
b           → Föregående ord
e           → Slutet av ord
0           → Början av rad
$           → Slutet av rad
gg          → Första raden
G           → Sista raden
10G         → Gå till rad 10
Ctrl+f      → Sida framåt
Ctrl+b      → Sida bakåt
```

### Radera i Normal Mode

```
x           → Radera tecken under cursor
X           → Radera tecken före cursor
dd          → Radera rad
dw          → Radera ord
d$          → Radera till slutet av rad
d0          → Radera till början av rad
D           → Samma som d$
5dd         → Radera 5 rader
```

### Kopiera och klistra

```
yy          → Kopiera (yank) rad
yw          → Kopiera ord
y$          → Kopiera till slutet
5yy         → Kopiera 5 rader
p           → Klistra efter
P           → Klistra före
```

### Undo / Redo

```
u           → Undo
Ctrl+r      → Redo
.           → Upprepa senaste kommando
```

### Sök och ersätt

```
/pattern    → Sök framåt
?pattern    → Sök bakåt
n           → Nästa träff
N           → Föregående träff
*           → Sök ord under cursor

:s/old/new/         → Ersätt första på rad
:s/old/new/g        → Ersätt alla på rad
:%s/old/new/g       → Ersätt alla i fil
:%s/old/new/gc      → Med bekräftelse
```

### Visual Mode

```
v           → Markera tecken
V           → Markera rader
Ctrl+v      → Block-markering

(efter markering):
d           → Radera
y           → Kopiera
>           → Indentera
<           → Outdent
```

### ~/.vimrc konfiguration

```bash
cat > ~/.vimrc << 'EOF'
" Visa radnummer
set number

" Relativa radnummer
set relativenumber

" Syntax highlighting
syntax on

" Sök: ignorera case om bara lowercase
set ignorecase
set smartcase

" Highlighta sökträffar
set hlsearch
set incsearch

" Tab = 4 spaces
set tabstop=4
set shiftwidth=4
set expandtab

" Visa matchande parentes
set showmatch

" Visa ruler (position)
set ruler

" Bättre backspace
set backspace=indent,eol,start
EOF
```

### Vim Survival Cheatsheet

```
┌────────────────────────────────────────────────┐
│              VIM SURVIVAL GUIDE                │
├────────────────────────────────────────────────┤
│ ESC        → Tillbaka till Normal mode         │
│ :q!        → PANIC EXIT (utan att spara)       │
│ :wq        → Spara och avsluta                 │
│ i          → Börja skriva                      │
│ dd         → Radera rad                        │
│ u          → Undo                              │
│ /text      → Sök                               │
│ :set nu    → Visa radnummer                    │
└────────────────────────────────────────────────┘
```

---

## Vim vs Nano — När använda vad?

| Situation | Rekommendation |
|-----------|----------------|
| Snabb edit | Nano |
| Nano ej installerat | Vim |
| Stor fil (1000+ rader) | Vim |
| Komplexa sök/ersätt | Vim |
| Remote server | Vim (alltid tillgänglig) |
| Scripting redigering | Vim |

---

## vimtutor — Lär dig Vim

```bash
# Interaktiv Vim-tutorial (30 min)
vimtutor
```

---

## Praktiska Övningar

### Övning 1: Nano basics

```bash
# 1. Skapa fil
nano /tmp/test.txt

# 2. Skriv: "Hello World"
# 3. Spara: Ctrl+O, Enter
# 4. Avsluta: Ctrl+X
```

### Övning 2: Vim basics

```bash
# 1. Öppna
vim /tmp/vimtest.txt

# 2. Tryck i (insert mode)
# 3. Skriv text
# 4. Tryck ESC
# 5. Skriv :wq och Enter
```

### Övning 3: Vim sök/ersätt

```bash
# 1. Skapa testfil
echo -e "foo bar\nfoo baz\nfoo qux" > /tmp/replace.txt

# 2. Öppna i vim
vim /tmp/replace.txt

# 3. Ersätt alla "foo" med "hello"
# Skriv: :%s/foo/hello/g
# Tryck Enter

# 4. Spara och avsluta: :wq
```

---

## Sammanfattning

### Nano

| Kommando | Funktion |
|----------|----------|
| `^O` | Spara |
| `^X` | Avsluta |
| `^W` | Sök |
| `^K` | Klipp rad |
| `^U` | Klistra |

### Vim

| Kommando | Funktion |
|----------|----------|
| `i` | Insert mode |
| `ESC` | Normal mode |
| `:wq` | Spara & avsluta |
| `:q!` | Force quit |
| `dd` | Radera rad |
| `yy` | Kopiera rad |
| `p` | Klistra |
| `u` | Undo |
| `/pattern` | Sök |
| `:%s/a/b/g` | Ersätt alla |

---

## Nästa Steg

Du kan nu redigera filer på vilken server som helst. Nästa node: **I/O Redirection** — dirigera dataflöden med pipes och redirects.
"""
            },
            {
                "title": "I/O Redirection & Pipes",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# I/O Redirection & Pipes

## Varför detta är kritiskt

> "In Unix, everything flows. Data streams in, gets transformed, and streams out. Master redirection and pipes, and you can build complex data pipelines with simple commands."

---

## Förstå Standard Streams

Varje process har tre standard-strömmar:

```
┌─────────────────────────────────────────────────────────────┐
│                     PROCESS                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   stdin (0)  ──────►  [COMMAND]  ──────► stdout (1)        │
│   (input)                │               (output)           │
│                          │                                  │
│                          ▼                                  │
│                     stderr (2)                              │
│                     (errors)                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

File Descriptors:
0 = stdin  (standard input)
1 = stdout (standard output)
2 = stderr (standard error)
```

---

## Output Redirection

### Redirect stdout till fil

```bash
# Skriv output till fil (överskriver)
ls -l > filelist.txt

# Append till fil (lägger till)
echo "ny rad" >> logfile.txt

# Explicit file descriptor
ls -l 1> filelist.txt    # Samma som >
```

### Redirect stderr till fil

```bash
# Bara errors till fil
command 2> errors.log

# Suppress errors (skicka till /dev/null)
find / -name "*.conf" 2>/dev/null
```

### Redirect båda

```bash
# stdout och stderr till samma fil
command > output.log 2>&1

# Modernare syntax (bash 4+)
command &> output.log

# stdout och stderr till olika filer
command > output.log 2> errors.log

# Append båda
command >> output.log 2>&1
```

### /dev/null — The Black Hole

```bash
# Kasta bort all output
command > /dev/null

# Kasta bort allt (output + errors)
command > /dev/null 2>&1
command &> /dev/null

# Vanligt mönster: tysta errors
find / -name "secret" 2>/dev/null
```

---

## Input Redirection

### Redirect stdin från fil

```bash
# Läs input från fil
sort < unsorted.txt

# Kombinera input och output
sort < unsorted.txt > sorted.txt

# wc räknar från fil
wc -l < bigfile.txt
```

### Here Documents (heredoc)

```bash
# Multiline input
cat << EOF
Detta är rad 1
Detta är rad 2
Variabel: $HOME
EOF

# Utan variabel-expansion (quote EOF)
cat << 'EOF'
$HOME visas som literal
EOF

# Skriv till fil
cat << EOF > config.txt
server=localhost
port=8080
EOF
```

### Here Strings

```bash
# En rad som input
grep "pattern" <<< "search in this string"

# Med variabel
grep "error" <<< "$log_content"
```

---

## Pipes — Koppla kommandon

Pipe (`|`) skickar stdout från ett kommando till stdin för nästa.

```bash
# Grundläggande pipe
ls -l | grep ".txt"

# Kedja flera
cat access.log | grep "404" | wc -l

# Praktiskt exempel: topp 10 största filer
du -h /var/log/* | sort -rh | head -10
```

### Pipeline-mönster

```bash
# Filtrera → Transformera → Aggregera
cat data.csv | grep "active" | cut -d',' -f2 | sort | uniq -c

# Log-analys
tail -1000 access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head

# Process-sökning
ps aux | grep nginx | grep -v grep
```

---

## tee — Split output

`tee` skriver till fil OCH stdout samtidigt.

```bash
# Skriv till fil och visa
ls -l | tee filelist.txt

# Append istället för överskriva
ls -l | tee -a filelist.txt

# Skriv till flera filer
ls -l | tee file1.txt file2.txt

# I pipeline
cat data.txt | tee backup.txt | grep "important" > filtered.txt
```

### tee med sudo

```bash
# Detta funkar INTE:
sudo echo "text" > /etc/protected.txt    # Redirect körs som user!

# Använd tee istället:
echo "text" | sudo tee /etc/protected.txt

# Append:
echo "text" | sudo tee -a /etc/protected.txt

# Utan output till terminal:
echo "text" | sudo tee /etc/protected.txt > /dev/null
```

---

## xargs — Bygg kommandon från input

`xargs` tar input och använder det som argument till ett kommando.

```bash
# Grundläggande
echo "file1 file2 file3" | xargs rm

# En fil per kommando
find . -name "*.log" | xargs -I {} mv {} {}.bak

# Parallell execution
find . -name "*.jpg" | xargs -P 4 -I {} convert {} -resize 50% small_{}

# Med null-separator (hanterar spaces i filnamn)
find . -name "*.txt" -print0 | xargs -0 grep "pattern"

# Begränsa antal argument
echo {1..100} | xargs -n 10 echo
```

### xargs praktiska exempel

```bash
# Ta bort gamla filer
find /tmp -mtime +7 | xargs rm -f

# Döda processer
pgrep -f "pattern" | xargs kill

# Kopiera matchande filer
find . -name "*.conf" | xargs -I {} cp {} /backup/
```

---

## Process Substitution

Behandla output som en fil.

```bash
# Jämför output från två kommandon
diff <(ls dir1) <(ls dir2)

# Sortera utan temp-fil
sort <(cat file1 file2)

# Flera inputs
paste <(cut -f1 data.txt) <(cut -f3 data.txt)
```

---

## Avancerade Mönster

### Named Pipes (FIFO)

```bash
# Skapa named pipe
mkfifo mypipe

# Terminal 1: Läs från pipe (blockerar)
cat mypipe

# Terminal 2: Skriv till pipe
echo "Hello" > mypipe
```

### File Descriptor Manipulation

```bash
# Öppna fil för läsning på fd 3
exec 3< inputfile.txt
read line <&3
exec 3<&-    # Stäng fd 3

# Öppna fil för skrivning på fd 4
exec 4> outputfile.txt
echo "data" >&4
exec 4>&-    # Stäng fd 4
```

### Swap stdout och stderr

```bash
# Swap 1 och 2
command 3>&1 1>&2 2>&3 3>&-
```

---

## Praktiska Övningar

### Övning 1: Log-filtrering

```bash
# Skapa testlog
cat > /tmp/app.log << 'EOF'
2025-12-01 10:00:00 INFO Starting application
2025-12-01 10:00:01 DEBUG Loading config
2025-12-01 10:00:02 ERROR Database connection failed
2025-12-01 10:00:03 INFO Retrying...
2025-12-01 10:00:04 ERROR Still failing
2025-12-01 10:00:05 INFO Recovered
EOF

# Extrahera bara ERROR-rader till fil
grep "ERROR" /tmp/app.log > /tmp/errors.log

# Räkna errors och visa
grep "ERROR" /tmp/app.log | tee /tmp/errors.log | wc -l
```

### Övning 2: Pipeline Power

```bash
# Hitta de 5 största filerna i /var
sudo find /var -type f -exec du -h {} + 2>/dev/null | sort -rh | head -5

# Unika IP-adresser från log (simulerad)
echo -e "192.168.1.1\n192.168.1.2\n192.168.1.1\n192.168.1.3" | sort | uniq -c | sort -rn
```

### Övning 3: xargs

```bash
# Skapa testfiler
mkdir /tmp/xargs_test
touch /tmp/xargs_test/file{1..5}.txt

# Lägg till innehåll med xargs
ls /tmp/xargs_test/*.txt | xargs -I {} sh -c 'echo "Content of {}" > {}'

# Verifiera
cat /tmp/xargs_test/*.txt
```

---

## Sammanfattning

| Operator | Betydelse |
|----------|-----------|
| `>` | Redirect stdout till fil (överskriver) |
| `>>` | Append stdout till fil |
| `2>` | Redirect stderr till fil |
| `&>` | Redirect stdout + stderr |
| `<` | Input från fil |
| `<<` | Here document |
| `<<<` | Here string |
| `\|` | Pipe (stdout → stdin) |
| `tee` | Split till fil + stdout |
| `xargs` | Bygg kommandon från input |
| `<()` | Process substitution |

---

## Nästa Steg

Du behärskar nu dataflöden i Linux. Nästa node: **User Management** — hantera användare och grupper.
"""
            },
            {
                "title": "User & Group Management",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 80,
                "content": r"""# User & Group Management

## Varför detta är kritiskt

> "Security starts with access control. Who can log in? What can they do? One misconfigured sudo rule can give an attacker root. One forgotten user account is a backdoor waiting to be exploited."

---

## Förstå Användarsystemet

```
┌─────────────────────────────────────────────────────────────┐
│                   LINUX USER MODEL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   /etc/passwd     → Användarinfo (namn, UID, shell)        │
│   /etc/shadow     → Krypterade lösenord                    │
│   /etc/group      → Gruppdefinitioner                      │
│   /etc/gshadow    → Grupplösenord                          │
│                                                             │
│   UID 0           → root (superuser)                       │
│   UID 1-999       → System/service accounts                │
│   UID 1000+       → Vanliga användare                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### /etc/passwd format

```bash
cat /etc/passwd | head -3
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

# Format: username:x:UID:GID:comment:home:shell
```

| Fält | Betydelse |
|------|-----------|
| username | Användarnamn |
| x | Lösenord i /etc/shadow |
| UID | User ID |
| GID | Primary Group ID |
| comment | Fullständigt namn/info |
| home | Hemkatalog |
| shell | Login shell |

---

## Skapa Användare

### useradd — Skapa användare

```bash
# Enkel (ingen hemkatalog, default shell)
sudo useradd john

# Med hemkatalog (-m) och bash shell
sudo useradd -m -s /bin/bash john

# Med specifik UID och GID
sudo useradd -u 1500 -g developers john

# Med kommentar
sudo useradd -m -s /bin/bash -c "John Doe" john

# Med extra grupper
sudo useradd -m -s /bin/bash -G sudo,docker john

# System account (för services)
sudo useradd -r -s /usr/sbin/nologin myservice
```

### Sätt lösenord

```bash
# Interaktivt
sudo passwd john

# Tvinga byte vid nästa login
sudo passwd -e john

# Lås konto
sudo passwd -l john

# Lås upp
sudo passwd -u john

# Se lösenordsstatus
sudo passwd -S john
```

---

## Modifiera Användare

### usermod — Ändra användare

```bash
# Byt shell
sudo usermod -s /bin/zsh john

# Lägg till i grupp (VIKTIGT: -a för append!)
sudo usermod -aG docker john

# VARNING: Utan -a ersätts alla grupper!
sudo usermod -G docker john    # John är nu BARA i docker

# Byt hemkatalog
sudo usermod -d /home/newjohn -m john

# Byt användarnamn
sudo usermod -l newname john

# Lås konto
sudo usermod -L john

# Lås upp
sudo usermod -U john
```

---

## Ta Bort Användare

### userdel — Radera användare

```bash
# Ta bort användare (behåll hemkatalog)
sudo userdel john

# Ta bort användare OCH hemkatalog
sudo userdel -r john

# Force (även om inloggad)
sudo userdel -f john
```

---

## Grupper

### Se grupper

```bash
# Dina grupper
groups

# Annan användares grupper
groups john

# Detaljerad info
id
# uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),27(sudo),999(docker)

id john
```

### Hantera grupper

```bash
# Skapa grupp
sudo groupadd developers

# Med specifik GID
sudo groupadd -g 2000 developers

# Ta bort grupp
sudo groupdel developers

# Byt namn på grupp
sudo groupmod -n newname oldname

# Lägg till användare i grupp
sudo usermod -aG developers john

# Ta bort användare från grupp
sudo gpasswd -d john developers
```

---

## su & sudo

### su — Switch User

```bash
# Byt till root (behöver roots lösenord)
su

# Byt till root med full environment
su -

# Byt till annan användare
su - john

# Kör ett kommando som annan användare
su - john -c "whoami"
```

### sudo — Superuser Do

```bash
# Kör som root
sudo command

# Kör som annan användare
sudo -u john command

# Öppna root shell
sudo -i

# Behåll environment
sudo -E command

# Lista dina sudo-rättigheter
sudo -l

# Redigera sudoers säkert
sudo visudo
```

### /etc/sudoers format

```bash
# Redigera ALLTID med visudo!
sudo visudo

# Format: user/group host=(runas) commands

# Root kan allt
root    ALL=(ALL:ALL) ALL

# Användare i sudo-grupp kan allt
%sudo   ALL=(ALL:ALL) ALL

# John kan köra apt utan lösenord
john    ALL=(ALL) NOPASSWD: /usr/bin/apt

# Developers kan starta/stoppa nginx
%developers ALL=(ALL) /bin/systemctl start nginx, /bin/systemctl stop nginx
```

### Sudoers best practices

```bash
# Skapa fil i /etc/sudoers.d/ istället för att redigera huvud-filen
sudo visudo -f /etc/sudoers.d/developers

# Innehåll:
%developers ALL=(ALL) NOPASSWD: /usr/bin/docker, /usr/bin/docker-compose
```

---

## Praktiska Mönster

### Skapa deployment-användare

```bash
# Skapa användare
sudo useradd -m -s /bin/bash -c "Deploy User" deploy

# Sätt lösenord
sudo passwd deploy

# Lägg till i nödvändiga grupper
sudo usermod -aG sudo,docker deploy

# Konfigurera sudo utan lösenord för deploy
echo "deploy ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/deploy

# Sätt rätt permissions
sudo chmod 440 /etc/sudoers.d/deploy
```

### Skapa service account

```bash
# System account utan login
sudo useradd -r -s /usr/sbin/nologin -d /opt/myapp myapp

# Skapa app-katalog
sudo mkdir -p /opt/myapp
sudo chown myapp:myapp /opt/myapp
```

---

## Praktiska Övningar

### Övning 1: Användare och grupper

```bash
# 1. Skapa grupp
sudo groupadd testgroup

# 2. Skapa användare i gruppen
sudo useradd -m -s /bin/bash -G testgroup testuser

# 3. Verifiera
id testuser
groups testuser

# 4. Cleanup
sudo userdel -r testuser
sudo groupdel testgroup
```

### Övning 2: Sudo-regel

```bash
# 1. Skapa användare
sudo useradd -m -s /bin/bash limited_user

# 2. Ge begränsad sudo
echo "limited_user ALL=(ALL) NOPASSWD: /bin/systemctl status *" | sudo tee /etc/sudoers.d/limited_user
sudo chmod 440 /etc/sudoers.d/limited_user

# 3. Testa (som limited_user)
sudo -u limited_user sudo systemctl status ssh    # Ska funka
sudo -u limited_user sudo systemctl restart ssh   # Ska INTE funka
```

---

## Sammanfattning

| Kommando | Användning |
|----------|------------|
| `useradd -m -s /bin/bash` | Skapa användare |
| `passwd` | Sätt lösenord |
| `usermod -aG group user` | Lägg till i grupp |
| `userdel -r` | Ta bort användare |
| `groupadd` | Skapa grupp |
| `id` | Visa UID/GID/grupper |
| `su -` | Byt till root |
| `sudo` | Kör som root |
| `visudo` | Redigera sudoers |

---

## Nästa Steg

Du kan nu hantera användare och grupper. Nästa node: **Package Management** — installera och uppdatera programvara.
"""
            },
            {
                "title": "Package Management",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 70,
                "content": r"""# Package Management

## Varför detta är kritiskt

> "The first thing you do on a new server: update packages. The second: install what you need. Package management is how you get software onto Linux — and keep it secure with updates."

---

## Pakethanterare per Distribution

```
┌─────────────────────────────────────────────────────────────┐
│              PACKAGE MANAGERS BY DISTRO                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Debian/Ubuntu          →  apt, apt-get, dpkg             │
│   RHEL/CentOS/Fedora     →  dnf, yum, rpm                  │
│   Arch                   →  pacman                          │
│   Alpine                 →  apk                             │
│   Universal              →  snap, flatpak                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## APT (Debian/Ubuntu)

### Uppdatera paketlistor

```bash
# Hämta senaste paketinfo från repos
sudo apt update

# Uppgradera installerade paket
sudo apt upgrade

# Uppgradera + hantera beroenden (ta bort/lägga till)
sudo apt full-upgrade

# Kombinera (vanligt mönster)
sudo apt update && sudo apt upgrade -y
```

### Installera paket

```bash
# Installera ett paket
sudo apt install nginx

# Installera flera
sudo apt install nginx git curl

# Installera utan att fråga
sudo apt install -y nginx

# Installera specifik version
sudo apt install nginx=1.18.0-0ubuntu1
```

### Ta bort paket

```bash
# Ta bort paket (behåll config)
sudo apt remove nginx

# Ta bort paket + config
sudo apt purge nginx

# Ta bort oanvända dependencies
sudo apt autoremove
```

### Sök och info

```bash
# Sök paket
apt search nginx

# Visa paketinfo
apt show nginx

# Lista installerade paket
apt list --installed

# Lista uppgraderingsbara
apt list --upgradable
```

### dpkg — Low-level

```bash
# Installera .deb-fil
sudo dpkg -i package.deb

# Lista installerade
dpkg -l

# Lista filer i paket
dpkg -L nginx

# Vilket paket äger en fil?
dpkg -S /usr/bin/nginx

# Ta bort paket
sudo dpkg -r nginx
```

---

## DNF/YUM (RHEL/CentOS/Fedora)

```bash
# Uppdatera
sudo dnf update
sudo dnf upgrade

# Installera
sudo dnf install nginx

# Ta bort
sudo dnf remove nginx

# Sök
dnf search nginx

# Info
dnf info nginx

# Lista installerade
dnf list installed

# Rensa cache
sudo dnf clean all
```

### rpm — Low-level

```bash
# Installera .rpm
sudo rpm -ivh package.rpm

# Lista installerade
rpm -qa

# Paketinfo
rpm -qi nginx

# Lista filer i paket
rpm -ql nginx
```

---

## Snap (Universal)

```bash
# Installera
sudo snap install code --classic

# Lista installerade
snap list

# Uppdatera
sudo snap refresh

# Ta bort
sudo snap remove code

# Info
snap info code
```

---

## Repositories

### APT repos

```bash
# Lista repos
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Lägg till repo (PPA)
sudo add-apt-repository ppa:ondrej/php
sudo apt update

# Lägg till GPG-nyckel + repo manuellt
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt update
```

---

## Praktiska Mönster

### Server-setup

```bash
# Initial setup
sudo apt update && sudo apt upgrade -y

# Install essentials
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    htop \
    net-tools \
    unzip
```

### Säkerhetsuppdateringar

```bash
# Bara säkerhetsuppdateringar (Ubuntu)
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades

# Manuellt
sudo apt update
sudo apt upgrade -y
```

---

## Sammanfattning

| Kommando (apt) | Funktion |
|----------------|----------|
| `apt update` | Hämta paketlistor |
| `apt upgrade` | Uppgradera paket |
| `apt install` | Installera |
| `apt remove` | Ta bort |
| `apt purge` | Ta bort + config |
| `apt search` | Sök |
| `apt show` | Info |
| `apt autoremove` | Rensa dependencies |

---

## Nästa Steg

Du kan nu installera programvara. Nästa node: **Service Management** — hantera systemtjänster med systemd.
"""
            },
            {
                "title": "Service Management (systemd)",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# Service Management (systemd)

## Varför detta är kritiskt

> "Every web server, database, and background service runs as a systemd unit. When nginx stops responding, when PostgreSQL won't start — you need systemctl and journalctl to diagnose and fix it."

---

## Förstå systemd

```
┌─────────────────────────────────────────────────────────────┐
│                      SYSTEMD                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PID 1 (init system)                                      │
│      │                                                     │
│      ├── Services (.service)  → nginx, postgresql, sshd   │
│      ├── Sockets (.socket)    → Activation triggers        │
│      ├── Timers (.timer)      → Cron-liknande              │
│      ├── Mounts (.mount)      → Filsystem                  │
│      └── Targets (.target)    → Boot stages                │
│                                                             │
│   Unit files: /etc/systemd/system/                         │
│               /lib/systemd/system/                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## systemctl — Tjänsthantering

### Status och info

```bash
# Visa status
systemctl status nginx

# Lista alla tjänster
systemctl list-units --type=service

# Lista aktiva
systemctl list-units --type=service --state=active

# Lista alla (även inaktiva)
systemctl list-units --type=service --all

# Lista failed
systemctl list-units --failed
```

### Start, stop, restart

```bash
# Starta tjänst
sudo systemctl start nginx

# Stoppa
sudo systemctl stop nginx

# Starta om
sudo systemctl restart nginx

# Ladda om config (utan full restart)
sudo systemctl reload nginx

# Reload eller restart
sudo systemctl reload-or-restart nginx
```

### Enable / Disable (autostart)

```bash
# Starta vid boot
sudo systemctl enable nginx

# Starta inte vid boot
sudo systemctl disable nginx

# Enable + start nu
sudo systemctl enable --now nginx

# Disable + stop nu
sudo systemctl disable --now nginx

# Kontrollera om enabled
systemctl is-enabled nginx
```

### Kolla status

```bash
# Kör tjänsten?
systemctl is-active nginx

# Är den failed?
systemctl is-failed nginx
```

---

## journalctl — Loggar

Alla systemd-loggar samlas i journal.

```bash
# Alla loggar
journalctl

# För specifik tjänst
journalctl -u nginx

# Följ loggar live
journalctl -u nginx -f

# Senaste 100 rader
journalctl -u nginx -n 100

# Sedan senaste boot
journalctl -u nginx -b

# Tidsintervall
journalctl -u nginx --since "2025-12-01" --until "2025-12-01 12:00"

# Senaste timmen
journalctl -u nginx --since "1 hour ago"

# Bara errors
journalctl -u nginx -p err

# Kernel-meddelanden
journalctl -k

# Disk-användning
journalctl --disk-usage

# Rensa gamla loggar
sudo journalctl --vacuum-time=7d
```

---

## Skapa egen Service

### Enkel service

```bash
# Skapa unit-fil
sudo vim /etc/systemd/system/myapp.service
```

```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/run.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Aktivera

```bash
# Ladda om systemd
sudo systemctl daemon-reload

# Enable och starta
sudo systemctl enable --now myapp

# Kolla status
systemctl status myapp
```

### Unit-fil sektioner

| Sektion | Innehåll |
|---------|----------|
| [Unit] | Beskrivning, beroenden |
| [Service] | Hur tjänsten körs |
| [Install] | När den ska startas |

### Service-typer

| Type | Beteende |
|------|----------|
| simple | Processen startar direkt (default) |
| forking | Processen forkar (som traditionella daemons) |
| oneshot | Kör en gång och avslutar |
| notify | Signalerar när redo |

---

## Praktiska Övningar

### Övning 1: Hantera nginx

```bash
# 1. Status
systemctl status nginx

# 2. Stoppa
sudo systemctl stop nginx

# 3. Verifiera
systemctl is-active nginx

# 4. Starta
sudo systemctl start nginx

# 5. Se loggar
journalctl -u nginx -n 20
```

### Övning 2: Egen service

```bash
# Skapa enkel app
sudo mkdir -p /opt/mytest
echo '#!/bin/bash
while true; do
    echo "Running at $(date)" >> /opt/mytest/output.log
    sleep 10
done' | sudo tee /opt/mytest/run.sh

sudo chmod +x /opt/mytest/run.sh

# Skapa service
cat << 'EOF' | sudo tee /etc/systemd/system/mytest.service
[Unit]
Description=My Test Service

[Service]
Type=simple
ExecStart=/opt/mytest/run.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Aktivera
sudo systemctl daemon-reload
sudo systemctl enable --now mytest

# Verifiera
systemctl status mytest
tail -f /opt/mytest/output.log

# Cleanup
sudo systemctl disable --now mytest
sudo rm /etc/systemd/system/mytest.service
sudo rm -rf /opt/mytest
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `systemctl status` | Visa status |
| `systemctl start/stop` | Starta/stoppa |
| `systemctl restart` | Starta om |
| `systemctl reload` | Ladda om config |
| `systemctl enable` | Autostart vid boot |
| `systemctl disable` | Ingen autostart |
| `journalctl -u` | Se loggar |
| `journalctl -f` | Följ loggar live |
| `daemon-reload` | Ladda om unit-filer |

---

## Nästa Steg

Du kan nu hantera tjänster. Nästa node: **Disk & Storage** — partitioner, mount och LVM.
"""
            },
            {
                "title": "Disk & Storage Management",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 90,
                "content": r"""# Disk & Storage Management

## Varför detta är kritiskt

> "Disk full = system down. A full /var/log can crash your database. A full root partition stops everything. You MUST know how to check, manage, and expand storage."

---

## Disk Space Analysis

### df — Disk Free

```bash
# Visa alla filsystem
df

# Human-readable (KB, MB, GB)
df -h

# Visa filsystemtyp
df -T

# Bara ett filsystem
df -h /

# Visa inodes
df -i
```

### Output förklarad

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   15G   32G  32% /
/dev/sda2       200G  150G   40G  79% /home
tmpfs           4.0G     0  4.0G   0% /dev/shm
```

**Varningsnivåer:**
- 80%+ → Börja planera expansion
- 90%+ → Kritiskt, åtgärda nu
- 95%+ → Akut, system kan sluta fungera

### du — Disk Usage

```bash
# Katalogstorlek
du -h /var/log

# Summering
du -sh /var/log

# Sortera på storlek (hitta tjuvar)
du -h /var | sort -rh | head -20

# Max djup
du -h --max-depth=1 /

# Exkludera mönster
du -h --exclude="*.log" /var
```

### Hitta stora filer

```bash
# Filer större än 100MB
find / -type f -size +100M 2>/dev/null

# Topp 20 största filer
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -20

# ncdu (interaktiv)
sudo apt install ncdu
ncdu /
```

---

## Partitioner

### Visa partitioner

```bash
# Lista blockenheter
lsblk

# Detaljerad partitionsinfo
sudo fdisk -l

# Parted
sudo parted -l
```

### lsblk output

```bash
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0   100G  0 disk
├─sda1   8:1    0    50G  0 part /
├─sda2   8:2    0    48G  0 part /home
└─sda3   8:3    0     2G  0 part [SWAP]
sdb      8:16   0   500G  0 disk
└─sdb1   8:17   0   500G  0 part /data
```

### Skapa partition (fdisk)

```bash
# Interaktiv partitionering
sudo fdisk /dev/sdb

# Kommandon i fdisk:
# n → New partition
# p → Primary
# 1 → Partition number
# Enter → Default first sector
# +50G → Size
# w → Write and exit
```

---

## Filsystem

### Skapa filsystem

```bash
# ext4 (standard Linux)
sudo mkfs.ext4 /dev/sdb1

# xfs
sudo mkfs.xfs /dev/sdb1

# FAT32 (USB/kompatibilitet)
sudo mkfs.vfat /dev/sdb1
```

### Kontrollera filsystem

```bash
# Kontrollera och reparera (MÅSTE vara unmounted)
sudo fsck /dev/sdb1

# Force check
sudo fsck -f /dev/sdb1
```

---

## Mount & Unmount

### Tillfällig mount

```bash
# Skapa mount point
sudo mkdir /mnt/data

# Mounta
sudo mount /dev/sdb1 /mnt/data

# Verifiera
mount | grep sdb1
df -h /mnt/data

# Unmount
sudo umount /mnt/data

# Force unmount (om busy)
sudo umount -f /mnt/data

# Lazy unmount (väntar tills fri)
sudo umount -l /mnt/data
```

### Permanent mount (/etc/fstab)

```bash
# Hitta UUID (bättre än device name)
sudo blkid /dev/sdb1
# /dev/sdb1: UUID="abc123-..." TYPE="ext4"

# Redigera fstab
sudo vim /etc/fstab
```

```
# /etc/fstab format:
# <device>                                 <mount>    <type> <options>     <dump> <pass>
UUID=abc123-def456-ghi789                  /data      ext4   defaults      0      2

# Förklaringar:
# defaults = rw,suid,dev,exec,auto,nouser,async
# dump = 0 (ingen backup)
# pass = 2 (fsck ordning, 1 för root, 2 för andra, 0 för skip)
```

```bash
# Testa fstab utan reboot
sudo mount -a

# Om det misslyckas, fixa innan reboot!
```

---

## LVM (Logical Volume Manager)

LVM ger flexibilitet att ändra storlek utan att röra partitioner.

```
┌─────────────────────────────────────────────────────────────┐
│                         LVM STRUCTURE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Physical Disks:    /dev/sda    /dev/sdb    /dev/sdc      │
│                          │           │           │          │
│   Physical Volumes:     pv1        pv2        pv3          │
│                          └───────────┼───────────┘          │
│                                      │                      │
│   Volume Group:            ┌─────── vg_data ───────┐       │
│                            │                       │        │
│   Logical Volumes:     lv_home                 lv_var      │
│                            │                       │        │
│   Mount Points:        /home                   /var        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### LVM-kommandon

```bash
# Skapa Physical Volume
sudo pvcreate /dev/sdb1

# Skapa Volume Group
sudo vgcreate vg_data /dev/sdb1

# Skapa Logical Volume
sudo lvcreate -L 50G -n lv_home vg_data

# Skapa filsystem
sudo mkfs.ext4 /dev/vg_data/lv_home

# Mounta
sudo mount /dev/vg_data/lv_home /home

# Utöka LV
sudo lvextend -L +20G /dev/vg_data/lv_home
sudo resize2fs /dev/vg_data/lv_home    # ext4
# eller
sudo xfs_growfs /home                   # xfs

# Visa info
sudo pvs    # Physical volumes
sudo vgs    # Volume groups
sudo lvs    # Logical volumes
```

---

## Praktiska Övningar

### Övning 1: Diskanalys

```bash
# 1. Visa diskutrymme
df -h

# 2. Hitta vad som tar plats
du -sh /var/*

# 3. Hitta stora filer
sudo find /var -type f -size +10M -exec ls -lh {} \;
```

### Övning 2: Cleanup

```bash
# Rensa gamla kernels (Ubuntu)
sudo apt autoremove

# Rensa apt cache
sudo apt clean

# Rensa journalctl
sudo journalctl --vacuum-time=7d

# Hitta och ta bort .log-filer äldre än 30 dagar
sudo find /var/log -name "*.log" -mtime +30 -delete
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `df -h` | Visa ledigt utrymme |
| `du -sh` | Katalogstorlek |
| `lsblk` | Lista blockenheter |
| `fdisk` | Partitionera |
| `mkfs.ext4` | Skapa filsystem |
| `mount` | Mounta filsystem |
| `umount` | Unmount |
| `/etc/fstab` | Permanent mount |
| `pvs/vgs/lvs` | LVM-info |

---

## Nästa Steg

Du kan nu hantera disk och storage. Nästa node: **Networking Basics** — IP, interfaces och routing.
"""
            },
            {
                "title": "Networking Basics",
                "difficulty": "medium",
                "estimated_minutes": 60,
                "xp_reward": 90,
                "content": r"""# Networking Basics

## Varför detta är kritiskt

> "Every modern application is networked. API calls, database connections, load balancers — all depend on networking. When something can't connect, you need to diagnose: Is it DNS? Firewall? Routing? This node gives you the tools."

---

## Network Interfaces

### Visa interfaces

```bash
# Modern (ip command)
ip addr
ip a            # Kortform

# Klassisk (äldre system)
ifconfig

# Bara interface-namn
ip link show

# Specifikt interface
ip addr show eth0
```

### ip addr output

```bash
$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP>
    link/loopback 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    link/ether 00:11:22:33:44:55
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

### Hantera interfaces

```bash
# Stäng av interface
sudo ip link set eth0 down

# Sätt på
sudo ip link set eth0 up

# Sätt IP-adress
sudo ip addr add 192.168.1.100/24 dev eth0

# Ta bort IP
sudo ip addr del 192.168.1.100/24 dev eth0
```

---

## Connectivity Testing

### ping — Test reachability

```bash
# Enkel ping
ping google.com

# Antal paket
ping -c 4 google.com

# Interval (0.2 sek)
ping -i 0.2 google.com

# Quiet (bara sammanfattning)
ping -q -c 10 google.com
```

### traceroute — Path to destination

```bash
# Visa vägen
traceroute google.com

# Använd ICMP (som ping)
traceroute -I google.com

# TCP (om ICMP blockeras)
traceroute -T -p 443 google.com

# mtr (kombinerar ping + traceroute)
mtr google.com
```

---

## Port & Connection Analysis

### ss — Socket Statistics (modern)

```bash
# Visa alla lyssnande portar
ss -tuln

# Förklaring:
# -t = TCP
# -u = UDP
# -l = Listening
# -n = Numeric (visa port-nummer, inte namn)

# Visa etablerade connections
ss -tun

# Med process-info
ss -tulnp

# Specifik port
ss -tuln | grep :80

# Visa alla (inkl. sockets)
ss -a
```

### netstat — Klassiskt (äldre)

```bash
# Samma som ss -tuln
netstat -tuln

# Med processer
netstat -tulnp

# Routing table
netstat -rn
```

---

## Routing

### Visa routes

```bash
# Modern
ip route
ip r

# Klassisk
route -n
netstat -rn
```

### Default gateway

```bash
# Visa default route
ip route | grep default
# default via 192.168.1.1 dev eth0

# Lägg till default route
sudo ip route add default via 192.168.1.1

# Ta bort route
sudo ip route del default
```

---

## Hostname & DNS

### Hostname

```bash
# Visa hostname
hostname

# Visa alla namn
hostnamectl

# Sätt hostname (permanent)
sudo hostnamectl set-hostname myserver

# Tillfälligt
sudo hostname tempname
```

### DNS-lookup

```bash
# Enkel lookup
host google.com

# Detaljerad
dig google.com

# Bara IP
dig +short google.com

# Reverse lookup
dig -x 8.8.8.8

# nslookup (enklare)
nslookup google.com
```

### DNS-konfiguration

```bash
# Nuvarande DNS-servrar
cat /etc/resolv.conf

# I moderna system (systemd-resolved)
resolvectl status

# DNS cache flush
sudo systemd-resolve --flush-caches
```

---

## ARP (Address Resolution Protocol)

```bash
# Visa ARP-cache
arp -a
ip neigh

# Ta bort entry
sudo ip neigh del 192.168.1.1 dev eth0
```

---

## Praktiska Debugging-mönster

### "Jag kan inte nå X"

```bash
# 1. Har jag IP?
ip addr

# 2. Kan jag nå gateway?
ping -c 2 $(ip route | grep default | awk '{print $3}')

# 3. Kan jag nå DNS?
ping -c 2 8.8.8.8

# 4. Fungerar DNS-resolution?
host google.com

# 5. Kan jag nå målet?
ping -c 2 target.com

# 6. Är porten öppen?
nc -zv target.com 443
```

### Kontrollera lyssnande tjänster

```bash
# Vad lyssnar på port 80?
ss -tulnp | grep :80

# Alla lyssnande
ss -tulnp
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `ip addr` | Visa interfaces/IP |
| `ip route` | Visa routing |
| `ping` | Testa connectivity |
| `traceroute` | Visa nätverksväg |
| `ss -tuln` | Lyssnande portar |
| `dig` / `host` | DNS-lookup |
| `hostname` | Visa/sätt hostname |

---

## Nästa Steg

Du har nu grunderna i nätverksdiagnostik. Nästa node: **DNS & Resolution** — fördjupning i DNS.
"""
            },
            {
                "title": "DNS & Name Resolution",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 75,
                "content": r"""# DNS & Name Resolution

## Varför detta är kritiskt

> "DNS is the phone book of the internet. When DNS fails, nothing works — users can't reach your site, services can't connect. Understanding DNS is essential for troubleshooting connectivity issues."

---

## Så fungerar DNS

```
┌─────────────────────────────────────────────────────────────┐
│                     DNS RESOLUTION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   User: "google.com"                                        │
│          │                                                  │
│          ▼                                                  │
│   1. Check /etc/hosts                                       │
│          │ (not found)                                      │
│          ▼                                                  │
│   2. Check local DNS cache                                  │
│          │ (not found)                                      │
│          ▼                                                  │
│   3. Query DNS resolver (/etc/resolv.conf)                  │
│          │                                                  │
│          ▼                                                  │
│   4. Resolver → Root servers → .com → google.com           │
│          │                                                  │
│          ▼                                                  │
│   5. Return IP: 142.250.185.78                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## DNS Records

| Record | Syfte | Exempel |
|--------|-------|---------|
| A | IPv4-adress | example.com → 93.184.216.34 |
| AAAA | IPv6-adress | example.com → 2606:2800:220:1:... |
| CNAME | Alias | www.example.com → example.com |
| MX | Mail server | example.com → mail.example.com |
| TXT | Text (SPF, DKIM) | "v=spf1 include:..." |
| NS | Nameservers | example.com → ns1.example.com |
| PTR | Reverse lookup | IP → hostname |

---

## dig — DNS Information Groper

```bash
# Enkel lookup
dig example.com

# Bara svaret
dig +short example.com

# Specifik record-typ
dig example.com A
dig example.com MX
dig example.com TXT
dig example.com NS

# Alla records
dig example.com ANY

# Fråga specifik DNS-server
dig @8.8.8.8 example.com

# Reverse lookup
dig -x 93.184.216.34

# Trace (visa hela resolution-kedjan)
dig +trace example.com
```

### dig output förklarad

```bash
$ dig example.com

; <<>> DiG 9.16.1 <<>> example.com
;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            3600    IN      A       93.184.216.34

;; Query time: 24 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Dec 01 10:00:00 UTC 2025
;; MSG SIZE  rcvd: 56
```

---

## host & nslookup

### host (enklare)

```bash
# Enkel lookup
host example.com

# Specifik typ
host -t MX example.com
host -t TXT example.com

# Använd specifik DNS
host example.com 8.8.8.8
```

### nslookup (interaktiv)

```bash
# Enkel
nslookup example.com

# Med specifik server
nslookup example.com 8.8.8.8

# Interaktivt läge
nslookup
> set type=MX
> example.com
> exit
```

---

## Lokala DNS-filer

### /etc/hosts

Lokal mappning som kollas FÖRST.

```bash
# Visa
cat /etc/hosts

# Format:
# IP        hostname    [aliases]
127.0.0.1   localhost
192.168.1.10 myserver myserver.local

# Användning:
# - Utveckling: blockera sajter
# - Testing: peka domän till lokal IP
```

```bash
# Lägg till entry
echo "192.168.1.50 testserver" | sudo tee -a /etc/hosts
```

### /etc/resolv.conf

DNS-resolver konfiguration.

```bash
cat /etc/resolv.conf

# Typiskt innehåll:
nameserver 8.8.8.8
nameserver 8.8.4.4
search example.com
```

**OBS:** I moderna system hanteras detta av systemd-resolved:
```bash
# Visa verklig config
resolvectl status

# Flush DNS cache
sudo systemd-resolve --flush-caches
```

---

## DNS Debugging

### "DNS fungerar inte"

```bash
# 1. Testa med IP (bypass DNS)
ping 8.8.8.8
# Funkar? → Problem är DNS, inte nätverk

# 2. Testa DNS-resolution
dig @8.8.8.8 example.com
# Funkar? → Lokal resolver är problemet

# 3. Kolla resolv.conf
cat /etc/resolv.conf

# 4. Testa lokal resolver
dig example.com
```

### Vanliga problem

| Symptom | Trolig orsak |
|---------|--------------|
| "Name or service not known" | DNS-resolution misslyckades |
| Timeout | DNS-server nås ej |
| NXDOMAIN | Domänen finns inte |
| SERVFAIL | DNS-server fel |

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `dig domain` | DNS lookup |
| `dig +short` | Bara IP |
| `dig @8.8.8.8` | Specifik DNS |
| `host domain` | Enkel lookup |
| `/etc/hosts` | Lokal mappning |
| `/etc/resolv.conf` | DNS-servrar |

---

## Nästa Steg

Du förstår nu DNS. Nästa node: **Firewall** — kontrollera nätverkstrafik.
"""
            },
            {
                "title": "Firewall Management",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# Firewall Management

## Varför detta är kritiskt

> "A server without a firewall is an open door. Every port you leave open is a potential attack vector. Firewalls are your first line of defense — they decide what traffic is allowed in and out."

---

## Firewall-verktyg

```
┌─────────────────────────────────────────────────────────────┐
│              LINUX FIREWALL LANDSCAPE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   iptables     → Klassiskt, kraftfullt, komplext           │
│   nftables     → Modern ersättare för iptables             │
│   ufw          → Ubuntu Firewall (frontend för iptables)   │
│   firewalld    → RHEL/CentOS (frontend för nftables)       │
│                                                             │
│   Kernel: netfilter (underliggande)                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## UFW (Uncomplicated Firewall)

Standard på Ubuntu. Enkelt och effektivt.

### Aktivera/inaktivera

```bash
# Status
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered

# Aktivera
sudo ufw enable

# Inaktivera
sudo ufw disable

# Återställ till default
sudo ufw reset
```

### Default policies

```bash
# Neka allt inkommande, tillåt utgående (rekommenderat)
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Tillåt/neka portar

```bash
# Tillåt SSH
sudo ufw allow ssh
sudo ufw allow 22

# Tillåt HTTP/HTTPS
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow http
sudo ufw allow https

# Tillåt port range
sudo ufw allow 6000:6007/tcp

# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100

# Tillåt från nätverk till port
sudo ufw allow from 192.168.1.0/24 to any port 22

# Neka
sudo ufw deny 23

# Neka från IP
sudo ufw deny from 10.0.0.5
```

### Ta bort regler

```bash
# Med nummer
sudo ufw status numbered
sudo ufw delete 2

# Med regel
sudo ufw delete allow 80
```

### Application profiles

```bash
# Lista tillgängliga profiler
sudo ufw app list

# Info om profil
sudo ufw app info "Nginx Full"

# Tillåt application
sudo ufw allow "Nginx Full"
sudo ufw allow "OpenSSH"
```

---

## iptables (klassiskt)

Kraftfullt men komplext. Bra att förstå grunderna.

### Se regler

```bash
# Lista alla regler
sudo iptables -L -n -v

# Lista med radnummer
sudo iptables -L --line-numbers

# Specifik chain
sudo iptables -L INPUT -n -v
```

### Chains

```
┌─────────────────────────────────────────────────────────────┐
│                    IPTABLES CHAINS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   INPUT       → Trafik TO this server                      │
│   OUTPUT      → Trafik FROM this server                    │
│   FORWARD     → Trafik THROUGH this server (routing)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Grundläggande regler

```bash
# Tillåt SSH (port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Tillåt established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Neka allt annat
sudo iptables -A INPUT -j DROP

# Tillåt loopback
sudo iptables -A INPUT -i lo -j ACCEPT
```

### Spara regler

```bash
# Ubuntu
sudo apt install iptables-persistent
sudo netfilter-persistent save

# Manuellt
sudo iptables-save > /etc/iptables/rules.v4
sudo iptables-restore < /etc/iptables/rules.v4
```

---

## firewalld (RHEL/CentOS)

```bash
# Status
sudo firewall-cmd --state
sudo firewall-cmd --list-all

# Aktivera service
sudo systemctl enable --now firewalld

# Tillåt port
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --reload

# Tillåt service
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

# Lista zoner
sudo firewall-cmd --get-zones
sudo firewall-cmd --get-default-zone
```

---

## Praktisk Server-setup

```bash
# 1. Sätt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Tillåt SSH (VIKTIGT - gör först!)
sudo ufw allow ssh

# 3. Tillåt webbtrafik
sudo ufw allow 80
sudo ufw allow 443

# 4. Aktivera
sudo ufw enable

# 5. Verifiera
sudo ufw status
```

---

## Sammanfattning

| Kommando (ufw) | Funktion |
|----------------|----------|
| `ufw status` | Visa status |
| `ufw enable` | Aktivera |
| `ufw allow 22` | Tillåt port |
| `ufw deny 23` | Neka port |
| `ufw delete` | Ta bort regel |
| `ufw reset` | Återställ |

---

## Nästa Steg

Du kan nu konfigurera brandväggar. Nästa node: **SSH & Remote Access** — säker fjärråtkomst.
"""
            },
            {
                "title": "SSH & Remote Access",
                "difficulty": "medium",
                "estimated_minutes": 55,
                "xp_reward": 85,
                "content": r"""# SSH & Remote Access

## Varför detta är kritiskt

> "SSH is how you access servers. Period. Every production server, every cloud instance, every container — you reach them through SSH. Master SSH and you can manage anything, anywhere."

---

## SSH Grunderna

### Ansluta

```bash
# Grundläggande
ssh user@hostname
ssh user@192.168.1.10

# Specifik port
ssh -p 2222 user@hostname

# Med verbose (debugging)
ssh -v user@hostname
ssh -vvv user@hostname    # Extra verbose
```

### SSH-nycklar (bästa praxis)

Lösenord är osäkert. Använd nycklar.

```bash
# Generera nyckelpar
ssh-keygen -t ed25519 -C "your@email.com"

# Alternativ: RSA (äldre men kompatibelt)
ssh-keygen -t rsa -b 4096

# Nycklar sparas i:
# ~/.ssh/id_ed25519      (privat - SKYDDA!)
# ~/.ssh/id_ed25519.pub  (publik - dela fritt)
```

### Kopiera nyckel till server

```bash
# Automatiskt
ssh-copy-id user@hostname

# Manuellt
cat ~/.ssh/id_ed25519.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Permissions (KRITISKT!)

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
```

---

## ~/.ssh/config

Spara inställningar för olika hosts.

```bash
# ~/.ssh/config
Host prod
    HostName production.example.com
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key

Host dev
    HostName dev.example.com
    User developer
    Port 2222

Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

```bash
# Nu kan du bara skriva:
ssh prod
ssh dev
```

---

## Kopiera filer

### scp — Secure Copy

```bash
# Fil till server
scp file.txt user@hostname:/path/to/destination/

# Fil från server
scp user@hostname:/path/to/file.txt ./local/

# Katalog (rekursiv)
scp -r folder/ user@hostname:/path/

# Med port
scp -P 2222 file.txt user@hostname:/path/
```

### sftp — Interactive

```bash
sftp user@hostname

# Inuti sftp:
ls              # Lista remote
lls             # Lista local
cd /path        # Byt remote dir
lcd /path       # Byt local dir
get file.txt    # Ladda ner
put file.txt    # Ladda upp
exit
```

### rsync — Synkronisering (bäst för backup)

```bash
# Synka katalog (arkiv-läge)
rsync -avz source/ user@hostname:/destination/

# Med delete (spegla exakt)
rsync -avz --delete source/ user@hostname:/destination/

# Torrkörning
rsync -avzn source/ user@hostname:/destination/

# Progress
rsync -avz --progress source/ user@hostname:/destination/
```

---

## Port Forwarding & Tunneling

### Local forwarding

Åtkomst till remote service via lokal port.

```bash
# Syntax: ssh -L local_port:remote_host:remote_port

# Databas på remote server (port 5432) → localhost:5432
ssh -L 5432:localhost:5432 user@dbserver

# Nu kan du ansluta lokalt:
psql -h localhost -p 5432
```

### Remote forwarding

Exponera lokal service till remote.

```bash
# Syntax: ssh -R remote_port:local_host:local_port

# Din lokala port 3000 → remote port 8080
ssh -R 8080:localhost:3000 user@server
```

### Dynamic forwarding (SOCKS proxy)

```bash
# Skapa SOCKS proxy
ssh -D 1080 user@hostname

# Konfigurera browser att använda localhost:1080 som SOCKS proxy
```

---

## SSH-agent

Håll nycklar i minnet så du slipper skriva lösenord.

```bash
# Starta agent
eval $(ssh-agent)

# Lägg till nyckel
ssh-add ~/.ssh/id_ed25519

# Lista nycklar
ssh-add -l

# Ta bort alla
ssh-add -D
```

### Agent forwarding

```bash
# Tillåt servern använda dina lokala nycklar
ssh -A user@server

# I config:
Host server
    ForwardAgent yes
```

---

## SSH Security

### /etc/ssh/sshd_config

```bash
# Viktiga inställningar:
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
Port 22    # Överväg att byta

# Efter ändring:
sudo systemctl restart sshd
```

### Best practices

1. **Disable root login**
2. **Disable password auth** (bara nycklar)
3. **Använd ed25519 eller RSA 4096**
4. **Byt port** (security through obscurity)
5. **Använd fail2ban**

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `ssh user@host` | Anslut |
| `ssh-keygen -t ed25519` | Skapa nyckel |
| `ssh-copy-id` | Kopiera nyckel |
| `scp` | Kopiera filer |
| `rsync -avz` | Synkronisera |
| `ssh -L` | Local forwarding |
| `ssh-agent` | Nyckelhantering |

---

## Nästa Steg

Du behärskar nu SSH. Nästa node: **Archiving & Compression** — tar, gzip och backup.
"""
            },
            {
                "title": "Archiving & Compression",
                "difficulty": "easy",
                "estimated_minutes": 40,
                "xp_reward": 65,
                "content": r"""# Archiving & Compression

## Varför detta är kritiskt

> "Backups, deployments, log rotation — all involve archives. A 10GB log file becomes 500MB compressed. Knowing tar is mandatory for any sysadmin."

---

## tar — Tape Archive

`tar` arkiverar filer (samlar till en fil). Kombineras ofta med kompression.

### Skapa arkiv

```bash
# Skapa arkiv (-c = create, -v = verbose, -f = file)
tar -cvf archive.tar folder/

# Med gzip-kompression (-z)
tar -czvf archive.tar.gz folder/

# Med bzip2 (-j) - bättre kompression, långsammare
tar -cjvf archive.tar.bz2 folder/

# Med xz (-J) - bäst kompression, långsammast
tar -cJvf archive.tar.xz folder/
```

### Extrahera arkiv

```bash
# Extrahera
tar -xvf archive.tar

# Extrahera gzip
tar -xzvf archive.tar.gz

# Extrahera bzip2
tar -xjvf archive.tar.bz2

# Extrahera till specifik katalog
tar -xzvf archive.tar.gz -C /destination/

# Lista innehåll (utan att extrahera)
tar -tvf archive.tar.gz
```

### Vanliga mönster

```bash
# Backup av katalog
tar -czvf backup_$(date +%Y%m%d).tar.gz /var/www/

# Exkludera filer
tar -czvf backup.tar.gz --exclude='*.log' --exclude='node_modules' folder/

# Extrahera specifik fil
tar -xzvf archive.tar.gz path/to/file.txt
```

---

## Komprimeringsverktyg

### gzip / gunzip

```bash
# Komprimera (ersätter original)
gzip file.txt           # → file.txt.gz

# Behåll original
gzip -k file.txt

# Dekomprimera
gunzip file.txt.gz
gzip -d file.txt.gz

# Visa info
gzip -l file.txt.gz
```

### bzip2 / bunzip2

```bash
bzip2 file.txt          # → file.txt.bz2
bunzip2 file.txt.bz2
```

### xz

```bash
xz file.txt             # → file.txt.xz
xz -d file.txt.xz
```

### Jämförelse

| Format | Kompression | Hastighet |
|--------|-------------|-----------|
| gzip | Bra | Snabb |
| bzip2 | Bättre | Medium |
| xz | Bäst | Långsam |

---

## zip / unzip

Kompatibelt med Windows.

```bash
# Skapa zip
zip archive.zip file1 file2
zip -r archive.zip folder/

# Extrahera
unzip archive.zip
unzip archive.zip -d /destination/

# Lista innehåll
unzip -l archive.zip

# Lösenordsskydda
zip -e secure.zip file.txt
```

---

## Praktiska Mönster

### Daglig backup

```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czvf /backup/www_$DATE.tar.gz /var/www/html/
find /backup -name "www_*.tar.gz" -mtime +7 -delete
```

### Deployment

```bash
# Skapa release
tar -czvf release-1.2.3.tar.gz --exclude='.git' --exclude='node_modules' .

# Deploy
tar -xzvf release-1.2.3.tar.gz -C /var/www/app/
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `tar -czvf` | Skapa .tar.gz |
| `tar -xzvf` | Extrahera .tar.gz |
| `tar -tvf` | Lista innehåll |
| `gzip` | Komprimera |
| `gunzip` | Dekomprimera |
| `zip -r` | Skapa zip |
| `unzip` | Extrahera zip |

---

## Nästa Steg

Du kan nu arkivera och komprimera. Nästa node: **Cron & Scheduling** — automatisera uppgifter.
"""
            },
            {
                "title": "Cron & Scheduling",
                "difficulty": "medium",
                "estimated_minutes": 45,
                "xp_reward": 75,
                "content": r"""# Cron & Scheduling

## Varför detta är kritiskt

> "Automation utan scheduling är manuellt arbete. Backups, logrotation, deployments — allt körs på schema. Cron är DevOps-hjärtat."

---

## Crontab Grunderna

### Syntax

```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6, 0=Sunday)
│ │ │ │ │
* * * * * command
```

### Hantera crontab

```bash
# Redigera din crontab
crontab -e

# Lista din crontab
crontab -l

# Ta bort alla jobb
crontab -r

# Redigera annan användares (root)
sudo crontab -u nginx -e
```

---

## Vanliga Mönster

```bash
# Varje minut
* * * * * /script.sh

# Varje timme
0 * * * * /script.sh

# Varje dag kl 03:00
0 3 * * * /backup.sh

# Måndag-fredag kl 09:00
0 9 * * 1-5 /report.sh

# Första i varje månad
0 0 1 * * /monthly.sh

# Var 5:e minut
*/5 * * * * /check.sh

# Var 2:a timme
0 */2 * * * /script.sh
```

### Specialuttryck

```bash
@reboot    # Vid start
@yearly    # 0 0 1 1 *
@monthly   # 0 0 1 * *
@weekly    # 0 0 * * 0
@daily     # 0 0 * * *
@hourly    # 0 * * * *
```

---

## System Cron Directories

```bash
/etc/cron.d/        # Systemjobb
/etc/cron.hourly/   # Körs varje timme
/etc/cron.daily/    # Körs varje dag
/etc/cron.weekly/   # Körs varje vecka
/etc/cron.monthly/  # Körs varje månad
```

---

## Praktiskt Exempel

```bash
# Backup varje natt kl 02:00
0 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1

# SSL-cert renewal måndag kl 03:00
0 3 * * 1 certbot renew --quiet

# Disk cleanup söndag kl 04:00
0 4 * * 0 find /tmp -mtime +7 -delete
```

---

## Systemd Timers (Modernt Alternativ)

```bash
# Lista timers
systemctl list-timers

# Skapa timer: /etc/systemd/system/backup.timer
[Unit]
Description=Daily backup timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target

# Aktivera
sudo systemctl enable --now backup.timer
```

---

## Sammanfattning

| Mönster | Betydelse |
|---------|-----------|
| `* * * * *` | Varje minut |
| `0 * * * *` | Varje timme |
| `0 3 * * *` | Kl 03:00 dagligen |
| `*/5 * * * *` | Var 5:e minut |
| `0 0 * * 0` | Söndagar |

---

## Nästa Steg

Du kan nu schemalägga uppgifter. Nästa node: **Log Management** — övervaka och analysera loggar.
"""
            },
            {
                "title": "Log Management & Analysis",
                "difficulty": "medium",
                "estimated_minutes": 50,
                "xp_reward": 80,
                "content": r"""# Log Management & Analysis

## Varför detta är kritiskt

> "Loggar är sanningen. När något går fel är loggen ditt vittne. Utan logghantering flyger du blint."

---

## Viktiga Logfiler

```bash
/var/log/syslog       # Generell systemlogg (Debian/Ubuntu)
/var/log/messages     # Generell systemlogg (RHEL/CentOS)
/var/log/auth.log     # Autentisering (Debian/Ubuntu)
/var/log/secure       # Autentisering (RHEL/CentOS)
/var/log/kern.log     # Kernel-meddelanden
/var/log/dmesg        # Boot-meddelanden
/var/log/nginx/       # Nginx-loggar
/var/log/apache2/     # Apache-loggar
```

---

## journalctl (Systemd)

```bash
# Alla loggar
journalctl

# Senaste 100 rader
journalctl -n 100

# Följ live
journalctl -f

# Specifik enhet
journalctl -u nginx.service

# Sedan idag
journalctl --since today

# Tidsintervall
journalctl --since "2024-01-01" --until "2024-01-02"

# Senaste timmen
journalctl --since "1 hour ago"

# Kernel-meddelanden
journalctl -k

# Felmeddelanden
journalctl -p err

# JSON-output
journalctl -o json-pretty
```

---

## Klassisk Logganalys

```bash
# Visa slutet av logg
tail -f /var/log/syslog

# Sök i loggar
grep "error" /var/log/syslog
grep -i "failed" /var/log/auth.log

# Räkna förekomster
grep -c "404" /var/log/nginx/access.log

# Unika IP-adresser
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head

# Topp 10 sökvägar
awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

---

## dmesg - Kernel Loggar

```bash
# Alla kernel-meddelanden
dmesg

# Följ nya meddelanden
dmesg -w

# Med tidsstämplar
dmesg -T

# Fel och varningar
dmesg -l err,warn

# USB-enheter
dmesg | grep -i usb
```

---

## Logrotate

Konfiguration: `/etc/logrotate.d/`

```bash
# Exempel: /etc/logrotate.d/nginx
/var/log/nginx/*.log {
    daily           # Rotera dagligen
    rotate 14       # Behåll 14 filer
    compress        # Komprimera
    delaycompress   # Vänta en cykel
    missingok       # OK om saknas
    notifempty      # Skippa tomma
    create 0640 www-data adm
    sharedscripts
    postrotate
        systemctl reload nginx > /dev/null 2>&1 || true
    endscript
}
```

```bash
# Testa config
sudo logrotate -d /etc/logrotate.conf

# Tvinga rotation
sudo logrotate -f /etc/logrotate.d/nginx
```

---

## Inloggningshistorik

```bash
# Senaste inloggningar
last

# Misslyckade försök
lastb

# Vem är inloggad
who
w

# Användares senaste login
lastlog
```

---

## Sammanfattning

| Kommando | Funktion |
|----------|----------|
| `journalctl -u service` | Service-loggar |
| `journalctl -f` | Följ live |
| `tail -f` | Följ fil |
| `dmesg -T` | Kernel med tid |
| `last` | Inloggningshistorik |
| `logrotate` | Hantera loggfiler |

---

## Nästa Steg

Du kan nu analysera loggar. Nästa node: **Performance Monitoring** — övervaka systemet.
"""
            },
            {
                "title": "Performance Monitoring",
                "difficulty": "hard",
                "estimated_minutes": 55,
                "xp_reward": 90,
                "content": r"""# Performance Monitoring

## Varför detta är kritiskt

> "Performance är UX. En långsam server är en dålig server. Du måste kunna identifiera flaskhalsar — CPU, minne, disk, nätverk."

---

## Snabb Överblick

### uptime

```bash
$ uptime
 14:30:01 up 45 days, 3:22, 2 users, load average: 0.52, 0.58, 0.59
#                                                   1m   5m   15m

# Load average:
# < CPU-kärnor = OK
# > CPU-kärnor = Överbelastat
```

### top / htop

```bash
# top - grundläggande
top

# htop - bättre UI
htop

# Viktiga kolumner:
# %CPU - CPU-användning
# %MEM - Minnesanvändning
# TIME+ - Total CPU-tid
# COMMAND - Processnamn

# top shortcuts:
# P - Sortera på CPU
# M - Sortera på minne
# k - Döda process
# q - Avsluta
```

---

## CPU-analys

### mpstat

```bash
# CPU-statistik per kärna
mpstat -P ALL 1

# Förklaring:
# %usr  - User-mode
# %sys  - Kernel-mode
# %iowait - Väntar på I/O
# %idle - Ledig
```

### vmstat

```bash
# Snapshot var 2:a sekund
vmstat 2

# Output förklaring:
# procs: r=runnable, b=blocked
# memory: swpd, free, buff, cache
# swap: si=swap in, so=swap out
# io: bi=blocks in, bo=blocks out
# system: in=interrupts, cs=context switches
# cpu: us, sy, id, wa, st
```

---

## Minnesanalys

### free

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:          15Gi        8.2Gi       1.2Gi       512Mi       5.8Gi       6.5Gi
Swap:          4Gi        0.0Gi       4.0Gi

# Viktigt: Titta på "available", inte "free"
# buff/cache kan frigöras vid behov
```

### Minnesläckor

```bash
# Topp minnesanvändare
ps aux --sort=-%mem | head

# Specifik process
pmap -x <PID>

# Detaljerad
cat /proc/<PID>/status | grep -i mem
```

---

## Diskanalys

### iostat

```bash
# Disk I/O statistik
iostat -xz 1

# Viktiga kolumner:
# r/s, w/s - Reads/writes per sekund
# rkB/s, wkB/s - KB per sekund
# await - Genomsnittlig väntetid (ms)
# %util - Disk-användning
```

### iotop

```bash
# Disk I/O per process
sudo iotop

# Bara aktiva processer
sudo iotop -o
```

---

## Nätverksanalys

```bash
# Nätverksstatistik
sar -n DEV 1

# Bandbredd per interface
nload

# Anslutningar per state
ss -s

# Topp bandbredd per process
nethogs
```

---

## sar - Historisk Data

```bash
# CPU senaste timmen
sar -u

# Minne
sar -r

# Disk I/O
sar -d

# Nätverk
sar -n DEV

# Specifik tid
sar -u -s 10:00:00 -e 12:00:00
```

---

## Sammanfattning

| Resurs | Verktyg |
|--------|---------|
| CPU | top, htop, mpstat |
| Minne | free, vmstat, pmap |
| Disk | iostat, iotop |
| Nätverk | sar, nload, nethogs |
| Historik | sar |

---

## Nästa Steg

Du kan nu övervaka prestanda. Nästa node: **Troubleshooting** — felsökning av problem.
"""
            },
            {
                "title": "Linux Troubleshooting",
                "difficulty": "hard",
                "estimated_minutes": 60,
                "xp_reward": 100,
                "content": r"""# Linux Troubleshooting

## Varför detta är kritiskt

> "Production går ner. Du har 5 minuter att fixa det. Panik hjälper inte — systematisk felsökning gör det. Detta är din troubleshooting-verktygslåda."

---

## Systematisk Approach

```
1. IDENTIFY  → Vad är symptomen?
2. REPRODUCE → Kan du återskapa?
3. ISOLATE   → Var är problemet?
4. ANALYZE   → Varför händer det?
5. FIX       → Åtgärda
6. VERIFY    → Bekräfta fix
7. DOCUMENT  → Skriv ner
```

---

## Vanliga Problem & Lösningar

### "Disk Full"

```bash
# Kolla diskutrymme
df -h

# Hitta stora filer
du -sh /* 2>/dev/null | sort -rh | head

# Hitta stora filer
find / -type f -size +100M 2>/dev/null

# Rensa loggar
journalctl --vacuum-size=500M
truncate -s 0 /var/log/syslog.1

# Hitta raderade filer som fortfarande används
lsof | grep deleted
```

### "Out of Memory"

```bash
# Kolla minne
free -h

# OOM-killed processer
dmesg | grep -i "killed process"
journalctl -k | grep -i oom

# Topp minnesanvändare
ps aux --sort=-%mem | head -10

# Rensa cache (försiktigt!)
sync; echo 3 > /proc/sys/vm/drop_caches
```

### "Can't Connect"

```bash
# Kolla om tjänsten kör
systemctl status nginx

# Kolla lyssnande portar
ss -tlnp | grep :80

# Kolla firewall
sudo iptables -L -n
sudo ufw status

# DNS-problem
dig example.com
nslookup example.com

# Testa anslutning
curl -v http://localhost
telnet localhost 80
nc -zv localhost 80
```

### "Process Hangs"

```bash
# Hitta hängande process
ps aux | grep -i <process>

# Vad gör den?
strace -p <PID>

# Öppna filer
lsof -p <PID>

# Döda
kill <PID>
kill -9 <PID>  # Tvinga

# Alla av en typ
pkill -9 nginx
```

---

## Kraftfulla Verktyg

### strace - Systemanrop

```bash
# Spåra process
strace -p <PID>

# Starta med trace
strace -f ./script.sh

# Bara nätverksanrop
strace -e network ./app

# Med tidsstämplar
strace -t -p <PID>
```

### lsof - Öppna filer

```bash
# Allt som en process har öppet
lsof -p <PID>

# Vem använder en port?
lsof -i :80

# Vem använder en fil?
lsof /var/log/syslog

# Raderade men öppna filer
lsof +L1
```

### tcpdump - Nätverkstrafik

```bash
# All trafik på interface
sudo tcpdump -i eth0

# Specifik port
sudo tcpdump -i any port 443

# Spara till fil
sudo tcpdump -i eth0 -w capture.pcap
```

---

## Boot-problem

### GRUB Recovery

```bash
# I GRUB-menyn, tryck 'e' för att redigera

# Lägg till i linux-raden:
init=/bin/bash

# Eller för single user:
single
# eller
1
```

### Emergency Mode

```bash
# Systemd emergency
systemctl emergency

# Rescue mode
systemctl rescue

# Från GRUB: lägg till
systemd.unit=emergency.target
```

### Filsystem-problem

```bash
# Kolla filsystem (unmounted)
fsck /dev/sda1

# Tvinga check vid boot
touch /forcefsck
# eller
shutdown -rF now
```

---

## Checklista vid Problem

```
□ Kolla loggar: journalctl -xe
□ Kolla disk: df -h
□ Kolla minne: free -h
□ Kolla CPU: top/htop
□ Kolla nätverk: ss -tlnp
□ Kolla processer: ps aux
□ Kolla senaste ändringar: last, history
□ Kolla firewall: iptables -L
□ Kolla DNS: dig/nslookup
□ Kolla tjänster: systemctl status
```

---

## Sammanfattning

| Problem | Första kommando |
|---------|-----------------|
| Disk full | `df -h` |
| Minne slut | `free -h` |
| Kan inte ansluta | `ss -tlnp` |
| Process hänger | `strace -p PID` |
| Boot-problem | GRUB recovery |

---

## Grattis! 🎉

Du har slutfört **Linux Mastery SkillsMap**!

Du kan nu:
- Hantera processer och tjänster
- Navigera och manipulera filer
- Konfigurera användare och behörigheter
- Övervaka och felsöka system
- Automatisera med cron
- Analysera loggar och prestanda

**Nästa steg:** Docker SkillsMap → Containerisering
"""
            },
    ],
    "labs": [],
}


def get_module():
    """Returns the module definition."""
    return MODULE_LINUX_MASTERY


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_LINUX_MASTERY["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
