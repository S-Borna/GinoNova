# =============================================================================
# BASH MASTERY V3 - BLOCK 1 PART 1: INTRODUCTION & SHELL BASICS
# Noder 1-2 av 20 | Premium Bootcamp-kvalitet
# =============================================================================

NODE_1 = {
    "id": "bash_node_1",
    "title": "Bash Introduction - Shell Fundamentals",
    "slug": "bash-introduction-shell-fundamentals",
    "order_index": 1,
    "estimated_minutes": 45,
    "xp_reward": 100,
    "difficulty": "easy",
    "content": r'''# Bash Introduction - Shell Fundamentals

------------------------------------------------------------

Bash (Bourne Again SHell) ar det mest anvanda skalet i Unix-varlden och en grundlaggande fardighet for alla DevOps-ingenjorer. Att forsta Bash oppnar dorrar till automation, systemadministration och effektiv arbetsflodeskontroll.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor Bash ar viktigt |
|----------|----------------------|
| **Automation** | Automatisera repetitiva uppgifter som deployment, backup och monitoring |
| **CI/CD Pipelines** | Nastan alla CI/CD-verktyg kör Bash-skript for build och deploy |
| **Serveradministration** | Konfigurera, underhalla och felsoka servrar effektivt |
| **Container Management** | Dockerfiles och entrypoint-skript ar ofta Bash-baserade |
| **Infrastructure as Code** | Terraform, Ansible och andra verktyg anvander shell-kommandon |

Du maste forsta:

- **Shellen ar din gateway** - Allt i Linux gar genom shellen
- **Skript sparar tid** - En timmes skriptande kan spara dagar av manuellt arbete
- **Portabilitet** - Bash finns pa nastan alla Unix-system

------------------------------------------------------------

## Shell vs Terminal vs Console

```
+-------------------------------------------------------------------------+
|                    TERMINOLOGI - VIKTIGA SKILLNADER                      |
+-------------------------------------------------------------------------+
|                                                                          |
|  +-----------------------------------------------------------------+    |
|  |                         TERMINAL EMULATOR                        |    |
|  |                    (iTerm2, GNOME Terminal, etc)                 |    |
|  |  +---------------------------------------------------------+    |    |
|  |  |                         SHELL                            |    |    |
|  |  |                   (bash, zsh, fish, etc)                 |    |    |
|  |  |  +-------------------------------------------------+    |    |    |
|  |  |  |              COMMAND PROMPT                      |    |    |    |
|  |  |  |           user@host:~$ _                        |    |    |    |
|  |  |  +-------------------------------------------------+    |    |    |
|  |  +---------------------------------------------------------+    |    |
|  +-----------------------------------------------------------------+    |
|                                                                          |
|  TERMINAL: Programmet som visar text (grafiskt fonster)                 |
|  SHELL: Programmet som tolkar kommandon (bash, zsh, fish)               |
|  CONSOLE: Fysisk terminal (historiskt: skarm + tangentbord)             |
|  PROMPT: Texten som visar att shellen vantar pa input                   |
|                                                                          |
+-------------------------------------------------------------------------+
```

------------------------------------------------------------

## Bash vs Andra Shells

```
+-------------------------------------------------------------------------+
|                        SHELL JAMFORELSE                                  |
+-------------------------------------------------------------------------+
|                                                                          |
|  SHELL       | FORDELAR                    | NACKDELAR                  |
|  ------------+-----------------------------+----------------------------|
|  bash        | Universell, standard        | Aldre syntax               |
|              | Bra dokumentation           | Begransad interaktivitet   |
|              | POSIX-kompatibel            |                            |
|  ------------+-----------------------------+----------------------------|
|  zsh         | Battre autocomplete         | Inte alltid installerad    |
|              | Kraftfulla plugins          | Konfigurationskomplexitet  |
|              | Teman (Oh My Zsh)           |                            |
|  ------------+-----------------------------+----------------------------|
|  fish        | Anvandarvanlighast          | Ej POSIX-kompatibel        |
|              | Syntax highlighting         | Skript ej portabla         |
|              | Web-baserad config          |                            |
|  ------------+-----------------------------+----------------------------|
|  sh (dash)   | Snabbast                    | Minimal funktionalitet     |
|              | POSIX strict                | Saknar moderna features    |
|                                                                          |
|  REKOMMENDATION FOR DEVOPS:                                             |
|  • Skriv skript i bash (portabilitet)                                   |
|  • Anvand zsh/fish for interaktivt arbete                               |
|  • Testa alltid skript med #!/bin/bash                                  |
|                                                                          |
+-------------------------------------------------------------------------+
```

------------------------------------------------------------

## Grundlaggande Kommandon

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `echo` | Skriver ut text | `echo "Hello World"` |
| `pwd` | Visar nuvarande katalog | `pwd` |
| `cd` | Byter katalog | `cd /var/log` |
| `ls` | Listar filer | `ls -la` |
| `cat` | Visar filinnehall | `cat /etc/passwd` |
| `mkdir` | Skapar katalog | `mkdir -p dir/subdir` |
| `rm` | Tar bort filer | `rm -rf directory/` |
| `cp` | Kopierar filer | `cp -r src/ dest/` |
| `mv` | Flyttar/byter namn | `mv old.txt new.txt` |
| `touch` | Skapar tom fil | `touch newfile.txt` |

```bash
# Navigering och utforskning
pwd                          # Var ar jag?
ls -la                       # Visa alla filer med detaljer
cd /var/log                  # Ga till logkatalog
cd ..                        # Ga upp en niva
cd ~                         # Ga till hemkatalog
cd -                         # Ga till foreg katalog

# Filoperationer
mkdir -p projects/devops     # Skapa nestlade kataloger
touch README.md              # Skapa tom fil
cp file.txt backup.txt       # Kopiera fil
mv old.txt new.txt           # Byt namn
rm -rf temp/                 # Ta bort katalog rekursivt
```

------------------------------------------------------------

## Bash Konfigurationsfiler

```
+-------------------------------------------------------------------------+
|                     BASH KONFIGURATIONSFILER                             |
+-------------------------------------------------------------------------+
|                                                                          |
|  FIL                    | NAR DEN LADDAS                                |
|  -----------------------+----------------------------------------------|
|  /etc/profile           | Login shell, alla anvandare                   |
|  /etc/bash.bashrc       | Interactive non-login, alla anvandare        |
|  ~/.bash_profile        | Login shell, specifik anvandare              |
|  ~/.bashrc              | Interactive non-login, specifik anvandare    |
|  ~/.bash_logout         | Vid utloggning                               |
|                                                                          |
|  LADDNINGSORDNING (Login shell):                                        |
|  1. /etc/profile                                                        |
|  2. ~/.bash_profile ELLER ~/.bash_login ELLER ~/.profile                |
|                                                                          |
|  LADDNINGSORDNING (Non-login interactive):                              |
|  1. /etc/bash.bashrc                                                    |
|  2. ~/.bashrc                                                           |
|                                                                          |
|  TIPS: Lagg det mesta i ~/.bashrc och sourca fran ~/.bash_profile       |
|                                                                          |
+-------------------------------------------------------------------------+
```

```bash
# ~/.bashrc - Exempel
# ============================================================

# Alias for bekvamlighet
alias ll='ls -la'
alias ..='cd ..'
alias ...='cd ../..'
alias grep='grep --color=auto'

# Git aliases
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'

# Docker aliases
alias d='docker'
alias dc='docker compose'
alias dps='docker ps'

# Prompt customization
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Path additions
export PATH="$HOME/.local/bin:$PATH"

# Environment variables
export EDITOR=vim
export LANG=en_US.UTF-8
```

------------------------------------------------------------

## Ditt Forsta Bash-skript

```bash
#!/bin/bash
# ============================================================
# hello.sh - Ditt forsta Bash-skript
# ============================================================

# Shebang (#!/bin/bash) talar om vilken tolk som ska anvandas
# Kommentarer borjar med #

# Skriv ut ett meddelande
echo "Hej fran mitt forsta Bash-skript!"

# Visa systeminfo
echo "Hostname: $(hostname)"
echo "Datum: $(date)"
echo "Anvandare: $USER"
echo "Shell: $SHELL"
echo "Hemkatalog: $HOME"
```

```bash
# Skapa och kor skriptet
vim hello.sh           # Skapa filen
chmod +x hello.sh      # Gor exekverbar
./hello.sh             # Kor skriptet

# Alternativa satt att kora
bash hello.sh          # Explicit med bash
source hello.sh        # I nuvarande shell (. hello.sh)
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **Shebang** | `#!/bin/bash` - Forsta raden som anger tolk |
| **Shell** | Kommandotolk som kör instruktioner |
| **Terminal** | Program som visar shell-output |
| **Alias** | Genväg till langre kommandon |
| **PATH** | Lista over kataloger dar shell letar efter program |
| **RC-fil** | Run Commands-fil som kors vid shell-start |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `command not found` | Programmet finns ej i PATH | Kontrollera `which program` eller installera |
| `Permission denied` | Saknar exekveringsrattighet | `chmod +x script.sh` |
| `bad interpreter` | Fel shebang eller Windows-radslut | Använd `dos2unix` eller fixa manuellt |
| `syntax error near unexpected token` | Felaktig syntax | Kontrollera citattecken och paranteser |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Bash ar standarden** | Finns pa 99% av alla Linux-servrar |
| **Shebang ar obligatorisk** | `#!/bin/bash` i alla skript |
| **Alias sparar tid** | Konfigurera i ~/.bashrc |
| **chmod +x** | Kravs for att kora skript direkt |
| **Larande tar tid** | Men avkastningen ar enorm |

**Kom ihag:**

- Bash ar grunden for all DevOps-automation
- Skript ska alltid ha shebang
- Konfigurera din miljo i ~/.bashrc
- Ov genom att automatisera dagliga uppgifter
''',
}

NODE_2 = {
    "id": "bash_node_2",
    "title": "Command Line Mastery - Input, Output & Pipes",
    "slug": "command-line-mastery-input-output-pipes",
    "order_index": 2,
    "estimated_minutes": 50,
    "xp_reward": 100,
    "difficulty": "easy",
    "content": r'''# Command Line Mastery - Input, Output & Pipes

------------------------------------------------------------

Input/Output-omdirigering och pipes ar kärnan i Unix-filosofin. Genom att koppla ihop enkla kommandon skapar du kraftfulla verktyg. Denna kunskap ar fundamental for effektiv DevOps-automation.

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor I/O & Pipes ar viktigt |
|----------|------------------------------|
| **Logganalys** | Filtrera och extrahera data fran gigabytes av loggar |
| **Pipeline-byggande** | Skapa dataflöden mellan verktyg |
| **Felsokning** | Separera stdout och stderr for debugging |
| **Automation** | Mata in data automatiskt till program |
| **Monitoring** | Bearbeta metrics och skapa rapporter |

Du maste forsta:

- **Allt ar en fil** - I Unix ar devices, pipes och processer filer
- **Smá verktyg** - Kombinera specialiserade verktyg for komplexa uppgifter
- **Datafloden** - stdin, stdout, stderr ar dina vanner

------------------------------------------------------------

## Standard Streams

```
+-------------------------------------------------------------------------+
|                      STANDARD STREAMS (File Descriptors)                 |
+-------------------------------------------------------------------------+
|                                                                          |
|                         +-----------------+                             |
|   STDIN (0)            |                 |           STDOUT (1)         |
|   ---------------------▶     PROCESS     +-------------------------▶   |
|   Tangentbord/Fil/Pipe |                 |           Terminal/Fil       |
|                         |                 |                             |
|                         |                 +-------------------------▶   |
|                         +-----------------+           STDERR (2)        |
|                                                       Felmeddelanden    |
|                                                                          |
|  FILE DESCRIPTOR | STREAM  | DEFAULT      | SYMBOL                     |
|  ----------------+---------+--------------+----------------------------|
|  0               | stdin   | Keyboard     | < eller <<                  |
|  1               | stdout  | Terminal     | > eller >> eller 1>        |
|  2               | stderr  | Terminal     | 2> eller 2>>               |
|                                                                          |
|  KOMBINATIONER:                                                         |
|  &>   eller >&   | Bade stdout och stderr                              |
|  2>&1            | Stderr till samma som stdout                         |
|  1>&2            | Stdout till samma som stderr                         |
|                                                                          |
+-------------------------------------------------------------------------+
```

------------------------------------------------------------

## Output Redirection

| Operator | Funktion | Exempel |
|----------|----------|---------|
| `>` | Skriver till fil (skriver over) | `echo "text" > fil.txt` |
| `>>` | Appendar till fil | `echo "mer" >> fil.txt` |
| `2>` | Skriver stderr till fil | `cmd 2> errors.log` |
| `2>>` | Appendar stderr | `cmd 2>> errors.log` |
| `&>` | Bade stdout och stderr | `cmd &> all.log` |
| `2>&1` | Stderr till stdout | `cmd > all.log 2>&1` |

```bash
# Grundlaggande output redirection
echo "Hello" > output.txt        # Skapa/skriv over fil
echo "World" >> output.txt       # Lagg till i slutet

# Separera stdout och stderr
ls /valid /invalid > stdout.txt 2> stderr.txt

# Kombinera stdout och stderr
ls /valid /invalid &> combined.txt
# ELLER (POSIX-kompatibelt)
ls /valid /invalid > combined.txt 2>&1

# Tysta output helt
command > /dev/null 2>&1         # Ignorera all output
command &> /dev/null             # Kortare syntax (bash 4+)

# Praktiskt exempel - logg med tidstampel
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Deployment started" >> deploy.log
```

------------------------------------------------------------

## Input Redirection

| Operator | Funktion | Exempel |
|----------|----------|---------|
| `<` | Las fran fil | `wc -l < file.txt` |
| `<<` | Here Document | `cat << EOF` |
| `<<<` | Here String | `cat <<< "text"` |

```bash
# Las fran fil
wc -l < /var/log/syslog          # Rakna rader
sort < names.txt                  # Sortera fran fil

# Here Document - multiline input
cat << EOF > config.yaml
database:
  host: localhost
  port: 5432
  name: mydb
EOF

# Here Document med variabelexpansion
NAME="DevOps"
cat << EOF
Hello $NAME!
Today is $(date +%A)
EOF

# Here Document UTAN variabelexpansion (quote EOF)
cat << 'EOF'
This $VAR will NOT be expanded
Neither will $(commands)
EOF

# Here String - single line input
grep "error" <<< "This is an error message"

# Kombinera input och output
sort < unsorted.txt > sorted.txt
```

------------------------------------------------------------

## Pipes - Koppla Kommandon

```
+-------------------------------------------------------------------------+
|                         PIPES I AKTION                                   |
+-------------------------------------------------------------------------+
|                                                                          |
|  cat access.log | grep "ERROR" | wc -l                                  |
|                                                                          |
|  +----------+     +----------+     +----------+     +----------+       |
|  |   cat    |     |   grep   |     |    wc    |     |  OUTPUT  |       |
|  |          |----▶|          |----▶|          |----▶|          |       |
|  | Laser    |     | Filtrerar|     |  Raknar  |     |   42     |       |
|  | filen    |     | "ERROR"  |     |  rader   |     |          |       |
|  +----------+     +----------+     +----------+     +----------+       |
|                                                                          |
|  DATAFLODE:                                                             |
|  access.log --▶ alla rader --▶ ERROR-rader --▶ antal --▶ 42            |
|                                                                          |
+-------------------------------------------------------------------------+
```

```bash
# Grundlaggande pipe-anvandning
cat file.txt | grep "pattern"          # Sok i fil
ps aux | grep nginx                     # Hitta processer
ls -la | head -10                       # Forsta 10 rader
history | tail -20                      # Senaste 20 kommandon

# Logganalys med pipes
cat /var/log/nginx/access.log | \
    grep "404" | \
    awk '{print $7}' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10

# Forklaring av ovan:
# 1. cat        - Las loggen
# 2. grep "404" - Filtrera 404-fel
# 3. awk        - Extrahera URL (kolumn 7)
# 4. sort       - Sortera for uniq
# 5. uniq -c    - Rakna unika forekomster
# 6. sort -rn   - Sortera numeriskt, fallande
# 7. head -10   - Visa topp 10

# Praktiska DevOps-pipelines
# Hitta stora filer
find /var -type f -exec du -h {} \; 2>/dev/null | sort -rh | head -20

# Processer som anvander mest minne
ps aux --sort=-%mem | head -10

# Aktiva natverksanslutningar
netstat -tuln | grep LISTEN | awk '{print $4}'
```

------------------------------------------------------------

## Tee - Dela Output

```
+-------------------------------------------------------------------------+
|                         TEE KOMMANDOT                                    |
+-------------------------------------------------------------------------+
|                                                                          |
|  command | tee file.txt | another_command                               |
|                                                                          |
|  +----------+     +----------+     +----------+                        |
|  | command  |----▶|   tee    |----▶| another  |                        |
|  +----------+     +----+-----+     +----------+                        |
|                        |                                                 |
|                        ▼                                                 |
|                   +----------+                                          |
|                   | file.txt |                                          |
|                   +----------+                                          |
|                                                                          |
|  tee skriver till BADE fil och stdout                                   |
|                                                                          |
+-------------------------------------------------------------------------+
```

```bash
# Grundlaggande tee
echo "log entry" | tee logfile.txt         # Visa OCH spara
ls -la | tee filelist.txt | wc -l          # Spara och fortsatt pipe

# Tee med append
echo "more data" | tee -a logfile.txt      # Lagg till, skriv ej over

# Tee till flera filer
echo "data" | tee file1.txt file2.txt file3.txt

# Praktiskt: Se output samtidigt som den sparas
./deploy.sh 2>&1 | tee deploy.log

# Med sudo (vanligt problem)
echo "setting" | sudo tee /etc/config      # Funkar!
# sudo echo "setting" > /etc/config        # Funkar INTE!
```

------------------------------------------------------------

## Xargs - Argument fran Stdin

```bash
# Grundlaggande xargs
echo "file1 file2 file3" | xargs rm        # Ta bort filer
find . -name "*.log" | xargs rm            # Ta bort alla .log

# Med placeholder (-I)
cat urls.txt | xargs -I {} curl {}         # Curl varje URL

# Parallell exekvering (-P)
cat servers.txt | xargs -P 4 -I {} ssh {} "uptime"

# Hantera specialtecken (-0 med find -print0)
find . -name "*.txt" -print0 | xargs -0 grep "pattern"

# Begrans argument per kommando (-n)
echo "a b c d e f" | xargs -n 2 echo
# Output:
# a b
# c d
# e f

# Praktiskt DevOps-exempel
# Ta bort alla stoppade containers
docker ps -aq --filter "status=exited" | xargs docker rm

# Kopiera filer till flera servrar
cat servers.txt | xargs -I {} scp config.yaml {}:/etc/app/
```

------------------------------------------------------------

## Process Substitution

```bash
# Jamfor tva kommandons output
diff <(ls dir1) <(ls dir2)

# Las fran process som fil
while read line; do
    echo "Processing: $line"
done < <(find . -name "*.sh")

# Skriv till process
tar cf >(gzip > archive.tar.gz) files/

# Praktiskt: Jamfor sorterade filer
diff <(sort file1.txt) <(sort file2.txt)

# Kombinera flera kallor
paste <(cut -f1 file1.txt) <(cut -f2 file2.txt)
```

------------------------------------------------------------

## Snabbreferens

| Term | Beskrivning |
|------|-------------|
| **stdin (0)** | Standard input - tangentbord/fil |
| **stdout (1)** | Standard output - terminal/fil |
| **stderr (2)** | Standard error - felmeddelanden |
| **Pipe (|)** | Kopplar stdout till nasta stdin |
| **Redirect (>)** | Skickar output till fil |
| **/dev/null** | Svartt hal - kastar all data |
| **tee** | Forgrenar datastrommen |
| **xargs** | Bygger kommandon fran stdin |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `Broken pipe` | Mottagare stangd | Ignorera (set +o pipefail) eller hantera |
| `Permission denied` | Kan ej skriva till fil | Anvand sudo tee |
| Forlorad stderr | Endast stdout pipas | Anvand 2>&1 fore pipe |
| Tomt resultat | Fel ordning pa redirects | 2>&1 maste komma efter > |

------------------------------------------------------------

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Tre strömmar** | stdin (0), stdout (1), stderr (2) |
| **Pipes ar kraftfulla** | Kombinera enkla verktyg till komplexa losningar |
| **Ordning spelar roll** | 2>&1 maste komma efter > |
| **/dev/null** | Tysta oonskat output |
| **tee for loggning** | Se och spara samtidigt |

**Kom ihag:**

- Anvand pipes for att undvika temporara filer
- Separera alltid stderr for battre felsokning
- xargs ar din van for batch-operationer
- Here documents ar perfekta for konfigurationsfiler
''',
}

BLOCK_1_PART_1_NODES = [NODE_1, NODE_2]
