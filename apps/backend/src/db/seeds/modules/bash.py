"""
Bash Mastery - Docker-style format
===================================

20 tasks med:
- Unicode separatorer
- ASCII-diagram
- Tabeller for kommandon
- Key Takeaways som tabell
- Kom ihag: bullets
- Svenska, INGA emojis
"""

MODULE = {
    "name": "Bash Mastery",
    "slug": "bash-mastery",
    "description": "Behärska Bash-scripting för automation och systemadministration",
    "icon": "terminal",
    "difficulty": "beginner",
    "estimated_hours": 25,
    "tasks": [
        {
            "title": "Bash Fundamentals & Shell Basics",
            "slug": "bash-fundamentals-shell-basics",
            "difficulty": "beginner",
            "content": """# Bash Fundamentals & Shell Basics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Bash ar kritiskt |
|----------|-------------------------|
| **Automation** | Eliminera repetitiva uppgifter |
| **CI/CD** | Pipelines kors i shell |
| **Containers** | Entrypoints och healthchecks |
| **Deployment** | Release-scripts |
| **Admin** | Systemunderhall |

Bash ar standardskalet pa Linux och macOS - du kommer anvanda det dagligen.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Shell Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                     TERMINAL EMULATOR                       │
│                   (iTerm, GNOME Terminal)                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                      SHELL                          │  │
│   │               (bash, zsh, fish)                     │  │
│   │                                                     │  │
│   │   Input ──► Parser ──► Executor ──► Output         │  │
│   │                                                     │  │
│   └─────────────────────────────────────────────────────┘  │
│                           │                                 │
│                           ▼                                 │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                     KERNEL                          │  │
│   │               (System Calls)                        │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Komponent | Funktion |
|-----------|----------|
| **Terminal** | Fonstret som visar text |
| **Shell** | Tolkar och kor kommandon |
| **Kernel** | Hanterar systemanrop |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Installera och Verifiera

```bash
# Visa aktuellt skal
echo $SHELL

# Bash version
bash --version

# Vilken bash anvands?
which bash
type bash

# Byt till bash (om du anvander annat)
chsh -s /bin/bash
```

| Kommando | Output |
|----------|--------|
| `echo $SHELL` | /bin/bash eller /bin/zsh |
| `bash --version` | GNU bash, version 5.x |
| `which bash` | /bin/bash |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Kommandokedja

```bash
# Sekventiell (kor alla)
command1 ; command2 ; command3

# AND (kor nasta om foregaende lyckas)
command1 && command2

# OR (kor nasta om foregaende misslyckas)
command1 || command2

# Kombinerat
mkdir dir && cd dir || echo "Misslyckades"
```

| Operator | Beteende |
|----------|----------|
| `;` | Kor alltid nasta |
| `&&` | Kor om exit 0 |
| `OR` | Kor om exit != 0 |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Navigering

```bash
# Var ar jag?
pwd

# Andra katalog
cd /path/to/dir      # Absolut
cd directory         # Relativ
cd ..                # Upp
cd ~                 # Hem
cd -                 # Foregaende

# Lista
ls -la               # Alla filer med detaljer
ls -lh               # Human-readable storlekar
ls -lt               # Sortera efter tid
```

| Kommando | Resultat |
|----------|----------|
| `cd ~` | Gar till hemkatalog |
| `cd -` | Vaxlar mellan tva kataloger |
| `ls -la` | Visar dolda filer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filhantering

```bash
# Skapa
touch file.txt
mkdir directory
mkdir -p path/to/nested

# Ta bort
rm file.txt
rm -r directory
rm -rf directory     # FARLIGT - ingen bekraftelse

# Kopiera och flytta
cp source dest
cp -r source_dir dest_dir
mv old.txt new.txt
```

| Flag | Betydelse |
|------|-----------|
| `-r` | Rekursivt |
| `-f` | Force (ingen bekraftelse) |
| `-p` | Skapa hela sokvagen |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## I/O Redirect

```
┌─────────────────────────────────────────────────────────────┐
│                   STANDARD STREAMS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   stdin (0)  ──►  ┌──────────┐  ──►  stdout (1)            │
│                   │ KOMMANDO │                              │
│                   └──────────┘  ──►  stderr (2)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Redirect stdout
command > file.txt       # Overskriv
command >> file.txt      # Append

# Redirect stderr
command 2> errors.txt

# Bada till samma fil
command > output.txt 2>&1
command &> output.txt    # Bash 4+

# Ignorera
command > /dev/null 2>&1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipes

```bash
# Skicka output till nasta kommando
ls -l | grep ".txt"
cat file | wc -l
ps aux | grep nginx | head -5

# Tee - spara OCH visa
command | tee output.txt
command | tee -a output.txt  # Append
```

| Kommando | Funktion |
|----------|----------|
| `grep` | Filtrera rader |
| `wc -l` | Rakna rader |
| `tee` | Forgrena output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Shell** | Kommandotolk, inte terminal |
| **&&** | Kedja beroende kommandon |
| **Pipes** | Koppla output till input |
| **Redirect** | Styr stdout/stderr till fil |
| **man** | Alltid tillganglig dokumentation |

**Kom ihåg:**
- **Bash ar standardskalet** - finns pa alla Linux/Mac
- **&& for beroenden** - kor nasta bara om foregaende lyckas
- **Pipes ar kraftfulla** - bygg datafloden
- **Redirect sparar output** - loggar och resultat
- **man kommando** - forsta stopp for hjalp
""",
        },
        {
            "title": "Variables & Data Types",
            "slug": "variables-data-types",
            "difficulty": "beginner",
            "content": """# Variables & Data Types

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor variabler ar kritiska |
|----------|------------------------------|
| **Konfiguration** | Miljo-specifika varden |
| **Parametrisering** | Atervand scripts |
| **Dynamik** | Bygg kommandon runtime |
| **Secrets** | Hantera credentials |

Utan variabler ar scripts hardkodade och oanvandbara i olika miljoer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bash Variabeltyper

```
┌─────────────────────────────────────────────────────────────┐
│                  BASH VARIABLER                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐          │
│   │  Lokala    │  │  Miljo-    │  │  Speciella │          │
│   │  name=val  │  │  export    │  │  $1 $? $$  │          │
│   └────────────┘  └────────────┘  └────────────┘          │
│                                                             │
│   ┌────────────┐  ┌────────────┐                           │
│   │  Arrays    │  │  Assoc.    │                           │
│   │  arr=(a b) │  │  dict[k]=v │                           │
│   └────────────┘  └────────────┘                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Skapa och Anvanda

```bash
# Tilldela (INGET mellanslag!)
name="Alice"
name = "Alice"    # FEL! Tolkas som kommando

# Lasa
echo $name
echo "${name}"                    # Rekommenderas
echo "Hello, ${name}!"

# Varfor braces?
filename="report"
echo "$filename_2024"             # Soker filename_2024
echo "${filename}_2024"           # report_2024

# Ta bort
unset name
```

| Syntax | Resultat |
|--------|----------|
| `$var` | Variabelns varde |
| `${var}` | Explicit avgrensning |
| `${#var}` | Langd |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stranghantering

```bash
str="Hello World"

# Langd
echo ${#str}                      # 11

# Substring
echo ${str:0:5}                   # "Hello"
echo ${str:6}                     # "World"

# Ersattning
echo ${str/World/Bash}            # "Hello Bash"
echo ${str//o/0}                  # "Hell0 W0rld"

# Ta bort prefix/suffix
filename="backup.tar.gz"
echo ${filename%.gz}              # backup.tar
echo ${filename%%.*}              # backup
echo ${filename#*.}               # tar.gz
echo ${filename##*.}              # gz
```

| Operator | Funktion |
|----------|----------|
| `%` | Ta bort kortaste suffix |
| `%%` | Ta bort langsta suffix |
| `#` | Ta bort kortaste prefix |
| `##` | Ta bort langsta prefix |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Default-varden

```bash
# Om var ar tom/odefinierad
echo ${var:-"default"}            # Anvand default
echo ${var:="default"}            # Satt OCH returnera
echo ${var:+"set"}                # "set" om definierad
echo ${var:?"error msg"}          # Avsluta med fel
```

| Syntax | Beteende |
|--------|----------|
| `:-` | Default om tom |
| `:=` | Tilldela default |
| `:+` | Alternativt varde |
| `:?` | Error om tom |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Arrays

```bash
# Skapa
fruits=("apple" "banana" "cherry")
declare -a numbers

# Tilldela
fruits[0]="apple"
fruits[3]="date"

# Lasa
echo ${fruits[0]}                 # apple
echo ${fruits[@]}                 # Alla element
echo ${#fruits[@]}                # Antal

# Iterera
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Lagg till
fruits+=("elderberry")
```

| Syntax | Resultat |
|--------|----------|
| `[@]` | Alla som separata |
| `[*]` | Alla som en strang |
| `${!arr[@]}` | Alla index |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Associativa Arrays (Bash 4+)

```bash
declare -A user

user[name]="Alice"
user[age]="30"
user[email]="alice@example.com"

# Lasa
echo ${user[name]}
echo ${!user[@]}                  # Alla nycklar

# Iterera
for key in "${!user[@]}"; do
    echo "$key: ${user[$key]}"
done

# Kontrollera nyckel
if [[ -v user[name] ]]; then
    echo "Name is set"
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Miljovariabler

```bash
# Viktiga miljovariabler
echo $HOME                        # Hemkatalog
echo $USER                        # Anvandarnamn
echo $PATH                        # Sokvag for program
echo $PWD                         # Nuvarande katalog
echo $SHELL                       # Aktivt skal

# Exportera
export MY_VAR="value"
MY_VAR="value" command            # Tillfalligt

# Ladda fran fil
source .env
```

| Variabel | Innehall |
|----------|----------|
| `$HOME` | /home/user |
| `$PATH` | Programsokvagar |
| `$PWD` | Nuvarande katalog |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Speciella Variabler

```bash
echo $0                           # Script-namn
echo $1                           # Forsta argument
echo $#                           # Antal argument
echo $@                           # Alla argument (separata)
echo $*                           # Alla argument (en strang)
echo $$                           # Script PID
echo $!                           # Senaste bakgrundsjobb PID
echo $?                           # Exit-status
```

| Variabel | Betydelse |
|----------|-----------|
| `$0` | Script-namn |
| `$1-9` | Positionsargument |
| `$#` | Antal argument |
| `$?` | Senaste exit-kod |
| `$$` | Process ID |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Syntax** | Ingen space runt = |
| **Braces** | ${var} for tydlighet |
| **Arrays** | [@] for separata element |
| **Export** | Gor tillganglig for child |
| **$?** | Senaste exit-status |

**Kom ihåg:**
- **Inga mellanslag** - `var=value` inte `var = value`
- **Anvand ${var}** - undviker tvetydighet
- **export for children** - subprocesser behover det
- **Speciella variabler** - $? ar din basta van for felhantering
- **Arrays med [@]** - iterera korrekt
""",
        },
        {
            "title": "Conditionals & Control Flow",
            "slug": "conditionals-control-flow",
            "difficulty": "beginner",
            "content": """# Conditionals & Control Flow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor conditionals ar kritiska |
|----------|----------------------------------|
| **Validering** | Kontrollera input |
| **Felhantering** | Agera pa fel |
| **Miljo** | Anpassa per environment |
| **Beslut** | Automatisera valsituationer |

Utan kontrollflode kan du inte skriva riktiga program.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Test-kommandon

```
┌─────────────────────────────────────────────────────────────┐
│                   BASH TEST SYNTAX                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   [ ]      POSIX test (fungerar overallt)                  │
│   [[ ]]    Bash extended (rekommenderas)                   │
│   (( ))    Aritmetisk utvardering                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## If-satser

```bash
# Grundlaggande
if [[ condition ]]; then
    echo "True"
fi

# If-else
if [[ condition ]]; then
    echo "True"
else
    echo "False"
fi

# If-elif-else
if [[ $val -eq 1 ]]; then
    echo "One"
elif [[ $val -eq 2 ]]; then
    echo "Two"
else
    echo "Other"
fi

# Enradig
[[ $val -gt 0 ]] && echo "Positive"
[[ $val -lt 0 ]] || echo "Not negative"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Strangjamforelser

```bash
str="hello"

# Equality
[[ $str == "hello" ]]
[[ $str != "world" ]]

# Pattern matching
[[ $str == h* ]]                  # Borjar med h
[[ $str == *lo ]]                 # Slutar med lo

# Tom/icke-tom
[[ -z $str ]]                     # True om tom
[[ -n $str ]]                     # True om icke-tom
```

| Operator | Betydelse |
|----------|-----------|
| `==` | Lika med |
| `!=` | Inte lika |
| `-z` | Zero length |
| `-n` | Non-zero |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Numeriska Jamforelser

```bash
num=42

# Test-syntax
[[ $num -eq 42 ]]                 # Equal
[[ $num -ne 0 ]]                  # Not equal
[[ $num -lt 50 ]]                 # Less than
[[ $num -gt 40 ]]                 # Greater than

# Aritmetisk syntax (enklare)
(( num == 42 ))
(( num < 50 ))
(( num > 0 && num < 100 ))
```

| Operator | Test | Aritmetisk |
|----------|------|------------|
| Lika | `-eq` | `==` |
| Inte lika | `-ne` | `!=` |
| Mindre | `-lt` | `<` |
| Storre | `-gt` | `>` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Filtester

```bash
# Existens
[[ -e /path/to/file ]]            # Existerar
[[ -f /path/to/file ]]            # Ar fil
[[ -d /path/to/dir ]]             # Ar katalog

# Behorigheter
[[ -r /path/to/file ]]            # Readable
[[ -w /path/to/file ]]            # Writable
[[ -x /path/to/file ]]            # Executable

# Storlek
[[ -s /path/to/file ]]            # Storlek > 0
```

| Test | Kontrollerar |
|------|--------------|
| `-e` | Existerar |
| `-f` | Ar vanlig fil |
| `-d` | Ar katalog |
| `-r` | Lasbar |
| `-w` | Skrivbar |
| `-x` | Korbar |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logiska Operatorer

```bash
# AND - bada maste vara sanna
[[ -f file.txt && -r file.txt ]]

# OR - minst en
[[ -f file.txt || -f file.bak ]]

# NOT - negering
[[ ! -f file.txt ]]

# Praktiskt exempel
if [[ -f "config.txt" ]]; then
    source config.txt
else
    echo "Config saknas!"
    exit 1
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case-satser

```bash
case $option in
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
        echo "Unknown: $option"
        exit 1
        ;;
esac

# Multipla patterns
case $input in
    [Yy]|[Yy]es)
        echo "Confirmed"
        ;;
    [Nn]|[Nn]o)
        echo "Cancelled"
        ;;
esac
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **[[ ]]** | Anvand istallet for [ ] |
| **Strang** | == != -z -n |
| **Nummer** | -eq -lt -gt eller (( )) |
| **Filer** | -f -d -e -r -w -x |
| **case** | Renare an manga elif |

**Kom ihåg:**
- **[[ ]] for Bash** - mer kraftfull an [ ]
- **(( )) for matematik** - renare syntax
- **Filtester ofta** - kontrollera innan du agerar
- **case for multipla val** - lattlast
- **&& och OR for enkel logik** - one-liners
""",
        },
        {
            "title": "Loops & Iteration",
            "slug": "loops-iteration",
            "difficulty": "beginner",
            "content": """# Loops & Iteration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor loopar ar kritiska |
|----------|---------------------------|
| **Batch** | Processa manga filer |
| **Deploy** | Rulla ut till servrar |
| **Retry** | Automatisk omforsok |
| **Poll** | Vanta pa status |

Utan loopar ar automation omojlig.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loop-typer

```
┌─────────────────────────────────────────────────────────────┐
│                   BASH LOOPS                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐          │
│   │    for     │  │   while    │  │   until    │          │
│   │  over list │  │  condition │  │  inverse   │          │
│   └────────────┘  └────────────┘  └────────────┘          │
│                                                             │
│   Control: break, continue                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## For-loopar

```bash
# Over lista
for fruit in apple banana cherry; do
    echo "Fruit: $fruit"
done

# Over array
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# Over filer
for file in *.txt; do
    echo "Processing: $file"
done

# C-style
for ((i=0; i<10; i++)); do
    echo "Count: $i"
done

# Med steg
for ((i=0; i<=100; i+=10)); do
    echo "$i"
done
```

| Syntax | Anvandning |
|--------|------------|
| `for x in list` | Iterera over element |
| `for ((...))` | C-style raknare |
| `for file in *.ext` | Glob-pattern |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Range och Sekvenser

```bash
# Brace expansion
for i in {1..5}; do
    echo "$i"                         # 1-5
done

# Med steg
for i in {0..100..10}; do
    echo "$i"                         # 0,10,20...100
done

# Bokstaver
for letter in {a..z}; do
    echo "$letter"
done

# seq kommando
for i in $(seq 1 5); do
    echo "$i"
done

for i in $(seq 0 2 10); do
    echo "$i"                         # 0,2,4,6,8,10
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## While-loopar

```bash
# Grundlaggande
count=0
while [[ $count -lt 5 ]]; do
    echo "Count: $count"
    ((count++))
done

# Lasa fil rad for rad
while IFS= read -r line; do
    echo "Line: $line"
done < file.txt

# Lasa med delimiter
while IFS=: read -r user _ uid _ _ home _; do
    echo "User: $user, Home: $home"
done < /etc/passwd

# Infinite loop
while true; do
    echo "Running..."
    sleep 1
done
```

| Pattern | Anvandning |
|---------|------------|
| `while condition` | Loop tills falskt |
| `while read` | Processa input |
| `while true` | Infinite loop |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Until-loopar

```bash
# Kor tills villkor ar sant
count=0
until [[ $count -ge 5 ]]; do
    echo "Count: $count"
    ((count++))
done

# Vanta pa process
until pgrep -x nginx > /dev/null; do
    echo "Waiting for nginx..."
    sleep 1
done
echo "Nginx is running!"

# Retry-logik
attempts=0
until [[ $attempts -ge 3 ]]; do
    if some_command; then
        break
    fi
    ((attempts++))
    sleep 2
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loop-kontroll

```bash
# break - avsluta loop
for i in {1..10}; do
    if [[ $i -eq 5 ]]; then
        break
    fi
    echo "$i"                         # 1,2,3,4
done

# continue - hoppa till nasta
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue
    fi
    echo "$i"                         # 1,2,4,5
done

# break fran nastlade
for i in {1..3}; do
    for j in {1..3}; do
        if [[ $j -eq 2 ]]; then
            break 2                   # Bryt ur BADA
        fi
    done
done
```

| Kommando | Effekt |
|----------|--------|
| `break` | Avsluta loop |
| `break N` | Bryt N nivaer |
| `continue` | Nasta iteration |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska Exempel

```bash
# Batch-rename
for file in *.jpg; do
    mv "$file" "photo_${file}"
done

# Parallell ping
for host in server1 server2 server3; do
    ping -c 1 "$host" &
done
wait

# Retry med exponential backoff
retry=0
while [[ $retry -lt 5 ]]; do
    if curl -s http://api.example.com; then
        break
    fi
    sleep $((2**retry))
    ((retry++))
done

# Process CSV
while IFS=, read -r name email role; do
    echo "User: $name ($email)"
done < users.csv
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **for** | Kand lista eller sekvens |
| **while** | Villkorsbaserad |
| **until** | Inverterad while |
| **IFS read** | Saker radlasning |
| **break/continue** | Loop-kontroll |

**Kom ihåg:**
- **for for listor** - filer, arrays, sekvenser
- **while for villkor** - okant antal iterationer
- **IFS= read -r** - korrekt radlasning
- **& och wait** - parallellisera
- **break vid success** - undvik onodiga iterationer
""",
        },
        {
            "title": "Functions & Modularity",
            "slug": "functions-modularity",
            "difficulty": "intermediate",
            "content": """# Functions & Modularity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor funktioner ar kritiska |
|----------|-------------------------------|
| **Lasbarhet** | Organiserad kod |
| **Ateranvandning** | DRY-principen |
| **Test** | Isolerade enheter |
| **Underhall** | Enkelt att andra |

Utan funktioner blir langre scripts ohanterlig spaghetti-kod.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Funktionsstruktur

```
┌─────────────────────────────────────────────────────────────┐
│                   BASH FUNCTION                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   function_name() {                                        │
│       local var1="$1"                                      │
│       local var2="$2"                                      │
│                                                             │
│       # logik                                               │
│                                                             │
│       echo "$result"     # Output                          │
│       return 0           # Exit code                       │
│   }                                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Definiera Funktioner

```bash
# Tva satt (likvardig)
function greet() {
    echo "Hello, $1!"
}

say_bye() {
    echo "Goodbye, $1!"
}

# Anropa
greet "Alice"
say_bye "Bob"
```

| Syntax | Beskrivning |
|--------|-------------|
| `function name()` | Explicit |
| `name()` | Kortare |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Argument och Variabler

```bash
process() {
    echo "First: $1"
    echo "Second: $2"
    echo "All: $@"
    echo "Count: $#"
}

process "a" "b" "c"

# Med default
greet() {
    local name=${1:-"World"}
    echo "Hello, $name!"
}

greet              # Hello, World!
greet "Alice"      # Hello, Alice!
```

| Variabel | Innehall |
|----------|----------|
| `$1-9` | Positionsargument |
| `$@` | Alla argument |
| `$#` | Antal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Return och Output

```bash
# Exit code (0 = success)
is_even() {
    local num=$1
    if (( num % 2 == 0 )); then
        return 0
    else
        return 1
    fi
}

if is_even 4; then
    echo "Even"
fi

# Returnera strang via echo
get_timestamp() {
    echo "$(date +%Y%m%d_%H%M%S)"
}

timestamp=$(get_timestamp)
```

| Metod | Anvandning |
|-------|------------|
| `return N` | Exit code 0-255 |
| `echo` | Strangoutput |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Local Variabler

```bash
# UTAN local - lacker ut
bad_function() {
    counter=10
}
bad_function
echo $counter        # 10 (problem!)

# MED local - isolerad
good_function() {
    local counter=10
    echo "Inside: $counter"
}
good_function
echo $counter        # Tom (korrekt)
```

**Best practice:** Anvand ALLTID `local` i funktioner.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bibliotek och Sourcing

```bash
# lib/utils.sh
log_info() {
    echo "[INFO] $(date +%H:%M:%S) $*"
}

log_error() {
    echo "[ERROR] $(date +%H:%M:%S) $*" >&2
}

validate_file() {
    [[ -f "$1" ]] || { log_error "Not found: $1"; return 1; }
}

# main.sh
#!/bin/bash
source lib/utils.sh

log_info "Starting script"
validate_file "config.txt" || exit 1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Avancerade Monster

```bash
# Namngivna argument
create_user() {
    local -A args
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --name) args[name]="$2"; shift 2 ;;
            --email) args[email]="$2"; shift 2 ;;
            *) shift ;;
        esac
    done
    echo "Creating: ${args[name]} (${args[email]})"
}

create_user --name "Alice" --email "alice@example.com"

# Callback-pattern
with_retry() {
    local max=$1 callback=$2
    shift 2
    local attempt=1
    while (( attempt <= max )); do
        "$callback" "$@" && return 0
        ((attempt++))
        sleep 1
    done
    return 1
}

with_retry 3 curl -s http://api.example.com
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Definiera forst** | Innan anrop |
| **local** | Alltid for funktionsvariabler |
| **$@** | Alla argument |
| **return** | Exit code 0-255 |
| **source** | Ladda bibliotek |

**Kom ihåg:**
- **local ar obligatoriskt** - undvik globala lacker
- **echo for strangar** - return for status
- **Sourcing for bibliotek** - ateranvandbar kod
- **Testa funktioner separat** - enklare debugging
- **Dokumentera parametrar** - hjalper framtida dig
""",
        },
        {
            "title": "Input Handling & Arguments",
            "slug": "input-handling-arguments",
            "difficulty": "intermediate",
            "content": """# Input Handling & Arguments

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor input-hantering ar kritisk |
|----------|-----------------------------------|
| **CLI tools** | Anvandarvanlighet |
| **Automation** | Parametriserade scripts |
| **Config** | Miljohantering |
| **Pipelines** | Datafloden |

Utan robust input-hantering blir scripts opalitliga.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Input-metoder

```
┌─────────────────────────────────────────────────────────────┐
│                  BASH INPUT SOURCES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐          │
│   │ Arguments  │  │   Options  │  │   stdin    │          │
│   │  $1 $2 $@  │  │ -v --file  │  │ pipe/read  │          │
│   └────────────┘  └────────────┘  └────────────┘          │
│                                                             │
│   ┌────────────┐  ┌────────────┐                           │
│   │ Config     │  │ Interaktiv │                           │
│   │  source    │  │   read -p  │                           │
│   └────────────┘  └────────────┘                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Positionella Argument

```bash
#!/bin/bash
# ./script.sh arg1 arg2 arg3

echo "Script: $0"
echo "First: $1"
echo "All: $@"
echo "Count: $#"

# Shift
shift                    # $2 blir $1
shift 2                  # Hoppa tva

# Iterera
for arg in "$@"; do
    echo "Processing: $arg"
done
```

| Variabel | Innehall |
|----------|----------|
| `$0` | Script-namn |
| `$1-9` | Argument |
| `$@` | Alla (separata) |
| `$#` | Antal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Getopts (Korta Options)

```bash
#!/bin/bash

usage() {
    echo "Usage: $0 [-v] [-f file] [-n number]"
    exit 1
}

verbose=false
filename=""

while getopts "vf:n:h" opt; do
    case $opt in
        v) verbose=true ;;
        f) filename="$OPTARG" ;;
        n) number="$OPTARG" ;;
        h) usage ;;
        ?) usage ;;
    esac
done

shift $((OPTIND - 1))
```

| Syntax | Betydelse |
|--------|-----------|
| `v` | Flag (ingen param) |
| `f:` | Kraver parameter |
| `OPTARG` | Parametervarde |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Long Options

```bash
#!/bin/bash

verbose=false
filename=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            verbose=true; shift ;;
        -f|--file)
            filename="$2"; shift 2 ;;
        --file=*)
            filename="${1#*=}"; shift ;;
        -h|--help)
            echo "Usage: $0 [--verbose] [--file FILE]"
            exit 0 ;;
        --)
            shift; break ;;
        -*)
            echo "Unknown: $1"; exit 1 ;;
        *)
            break ;;
    esac
done
```

| Pattern | Hantering |
|---------|-----------|
| `--file value` | shift 2 |
| `--file=value` | ${1#*=} |
| `--` | Slut pa options |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Interaktiv Input

```bash
# Grundlaggande
read -p "Enter name: " name

# Tyst (losenord)
read -s -p "Password: " password
echo

# Med timeout
read -t 5 -p "Quick: " response

# Med default
read -p "Env [prod]: " env
env=${env:-prod}

# Till array
read -a items -p "Items: "
echo "First: ${items[0]}"
```

| Flag | Effekt |
|------|--------|
| `-p` | Prompt |
| `-s` | Silent |
| `-t N` | Timeout N sek |
| `-a` | Till array |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Validering

```bash
# Antal argument
if [[ $# -lt 2 ]]; then
    echo "Error: Need 2 args"
    exit 1
fi

# Fil finns
if [[ ! -f "$1" ]]; then
    echo "Error: File not found"
    exit 1
fi

# Numerisk
if [[ ! "$port" =~ ^[0-9]+$ ]]; then
    echo "Error: Not a number"
    exit 1
fi

# Loop tills giltig
while true; do
    read -p "Port (1-65535): " port
    if (( port >= 1 && port <= 65535 )); then
        break
    fi
    echo "Invalid"
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Stdin och Pipes

```bash
#!/bin/bash
# Stodjer bade pipe och fil

if [[ -p /dev/stdin ]]; then
    while IFS= read -r line; do
        echo "Piped: $line"
    done
else
    while IFS= read -r line; do
        echo "File: $line"
    done < "$1"
fi

# Eller mer robust
input="${1:-/dev/stdin}"
while IFS= read -r line; do
    process "$line"
done < "$input"
```

| Test | Sant om |
|------|---------|
| `-p /dev/stdin` | Input ar pipe |
| `-t 0` | stdin ar terminal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Konfigurationsfiler

```bash
# config.conf
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Ladda enkelt
source config.conf

# Sakrare
while IFS='=' read -r key value; do
    [[ $key =~ ^#.*$ ]] && continue
    [[ -z $key ]] && continue
    declare "$key=$value"
done < config.conf

echo "Host: $DATABASE_HOST"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **getopts** | Korta options |
| **while case** | Langa options |
| **read -p** | Interaktiv input |
| **Validera** | Innan anvandning |
| **stdin** | Stod pipes |

**Kom ihåg:**
- **getopts for standard CLI** - bekant for anvandare
- **Validera all input** - trust no one
- **Default-varden** - ${var:-default}
- **Stod pipes** - flexibel integration
- **Help-flag** - alltid -h/--help
""",
        },
        {
            "title": "Text Processing (grep, sed, awk)",
            "slug": "text-processing-grep-sed-awk",
            "difficulty": "intermediate",
            "content": """# Text Processing (grep, sed, awk)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor textprocessering ar kritiskt |
|----------|-------------------------------------|
| **Loggar** | Sok och analysera |
| **Config** | Transformera filer |
| **Data** | Extrahera information |
| **Rapporter** | Aggregera statistik |

Unix-filosofin: sma verktyg som gor en sak bra.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Trion grep/sed/awk

```
┌─────────────────────────────────────────────────────────────┐
│                TEXT PROCESSING TOOLS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐          │
│   │    grep    │  │    sed     │  │    awk     │          │
│   │   SEARCH   │  │ TRANSFORM  │  │  ANALYZE   │          │
│   │   filter   │  │  replace   │  │  columns   │          │
│   └────────────┘  └────────────┘  └────────────┘          │
│                                                             │
│   Input ──► grep ──► sed ──► awk ──► Output               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## grep - Soka

```bash
# Grundlaggande
grep "error" logfile.txt
grep -i "error" logfile.txt          # Case-insensitive
grep -v "debug" logfile.txt          # Invertera
grep -n "error" logfile.txt          # Radnummer

# Regex
grep -E "error|warning" logfile.txt  # OR
grep "^Start" logfile.txt            # Borjar med
grep "end$" logfile.txt              # Slutar med

# Filer
grep -r "TODO" .                     # Rekursivt
grep -l "error" *.log                # Bara filnamn
grep -c "error" logfile.txt          # Rakna

# Context
grep -A 3 "error" log.txt            # 3 rader efter
grep -B 2 "error" log.txt            # 2 rader fore
grep -C 2 "error" log.txt            # Bada
```

| Flag | Effekt |
|------|--------|
| `-i` | Case-insensitive |
| `-v` | Invertera |
| `-E` | Extended regex |
| `-r` | Rekursiv |
| `-c` | Count |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## sed - Transformera

```bash
# Substitution
sed 's/error/ERROR/' file.txt        # Forsta per rad
sed 's/error/ERROR/g' file.txt       # Alla
sed 's/error/ERROR/gi' file.txt      # Case-insensitive

# In-place
sed -i 's/old/new/g' file.txt
sed -i.bak 's/old/new/g' file.txt    # Med backup

# Adressering
sed '5s/old/new/' file.txt           # Rad 5
sed '1,10s/old/new/' file.txt        # Rad 1-10
sed '/pattern/s/old/new/' file.txt   # Matchande rader

# Delete
sed '5d' file.txt                    # Rad 5
sed '/pattern/d' file.txt            # Matchande
sed '/^$/d' file.txt                 # Tomma rader
sed '/^#/d' file.txt                 # Kommentarer

# Print
sed -n '5p' file.txt                 # Bara rad 5
sed -n '10,20p' file.txt             # Rad 10-20
```

| Kommando | Funktion |
|----------|----------|
| `s/a/b/` | Ersatt |
| `d` | Delete |
| `p` | Print |
| `-i` | In-place |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## awk - Analysera

```bash
# Kolumner
awk '{print $1}' file.txt            # Forsta kolumn
awk '{print $NF}' file.txt           # Sista kolumn
awk '{print NF}' file.txt            # Antal kolumner

# Field separator
awk -F: '{print $1}' /etc/passwd
awk -F',' '{print $2}' data.csv

# Patterns
awk '/error/' file.txt               # Filter
awk '$3 > 100' file.txt              # Villkor
awk 'NR > 1' file.txt                # Hoppa header

# Berakningar
awk '{sum += $1} END {print sum}' nums.txt
awk '{sum += $1} END {print sum/NR}' nums.txt
```

| Variabel | Betydelse |
|----------|-----------|
| `$1` | Forsta kolumn |
| `$NF` | Sista kolumn |
| `NR` | Radnummer |
| `NF` | Antal falt |
| `FS` | Field separator |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska Kombinationer

```bash
# Top 10 IP-adresser i logg
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# Statuskoder
awk '{print $9}' access.log | sort | uniq -c | sort -rn

# 404-fel med URL
awk '$9 == 404 {print $7}' access.log | sort | uniq -c

# CSV kolumn 2 och 4
awk -F',' '{print $2","$4}' data.csv

# Summa i CSV (hoppa header)
awk -F',' 'NR>1 {sum+=$3} END {print sum}' sales.csv
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **grep** | Sok och filtrera |
| **sed** | Transformera och ersatt |
| **awk** | Kolumnanalys och berakningar |
| **Pipes** | Kombinera for kraft |
| **uniq -c** | Frekvensanalys |

**Kom ihåg:**
- **grep -E for regex** - kraftfullare an basic
- **sed -i.bak** - alltid backup
- **awk -F for delimiter** - CSV, kolon, etc
- **sort + uniq** - frekvensanalys-pattern
- **head/tail** - begrans output
""",
        },
        {
            "title": "Error Handling & Exit Codes",
            "slug": "error-handling-exit-codes",
            "difficulty": "intermediate",
            "content": """# Error Handling & Exit Codes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor felhantering ar kritisk |
|----------|--------------------------------|
| **Automation** | Scripts maste vara palitliga |
| **CI/CD** | Pipelines maste failas korrekt |
| **Produktion** | Dataforlust vid fel |
| **Debug** | Hitta problem snabbt |

Scripts utan felhantering ar farliga i produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Exit Codes

```
┌─────────────────────────────────────────────────────────────┐
│                   EXIT CODES                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   0       Success                                          │
│   1       General error                                    │
│   2       Misuse of shell command                          │
│   126     Command not executable                           │
│   127     Command not found                                │
│   128+N   Fatal signal N                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Kontrollera exit code
ls /exists && echo $?       # 0
ls /not-exist; echo $?      # 2

# Egna exit codes
readonly E_SUCCESS=0
readonly E_INVALID_ARGS=1
readonly E_FILE_NOT_FOUND=2

if [[ ! -f "$config" ]]; then
    exit $E_FILE_NOT_FOUND
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Set Options

```bash
#!/bin/bash
set -euo pipefail           # Rekommenderas!

# -e: Exit vid forsta fel
set -e
false                       # Script avslutas

# -u: Odefinierade variabler
set -u
echo $undefined             # Error!

# -o pipefail: Pipe-fel propageras
set -o pipefail
false | true                # Exit 1 (inte 0)
```

| Option | Effekt |
|--------|--------|
| `-e` | Exit vid fel |
| `-u` | Error pa undefined |
| `-o pipefail` | Pipe-fel |
| `-x` | Debug output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Trap for Cleanup

```bash
#!/bin/bash

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile_$$
    exit ${1:-1}
}

# Satt trap
trap cleanup EXIT           # Alltid vid exit
trap cleanup ERR            # Vid fel
trap cleanup SIGINT SIGTERM # Ctrl+C eller kill

# Med temp-fil
temp_file=$(mktemp)
trap "rm -f $temp_file" EXIT

echo "data" > "$temp_file"
process "$temp_file"
# Filen tas bort automatiskt
```

| Signal | Trigger |
|--------|---------|
| `EXIT` | Alltid vid exit |
| `ERR` | Vid fel (med -e) |
| `SIGINT` | Ctrl+C |
| `SIGTERM` | kill |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Manuell Felhantering

```bash
# OR for error
command || {
    echo "Failed" >&2
    exit 1
}

# Med if
if ! command; then
    echo "Failed" >&2
    exit 1
fi

# Retry-logik
retry() {
    local max=$1; shift
    local attempt=1
    while (( attempt <= max )); do
        "$@" && return 0
        echo "Attempt $attempt failed" >&2
        ((attempt++))
        sleep 1
    done
    return 1
}

retry 3 curl -s http://api.example.com
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logging

```bash
log_info() {
    echo "[INFO] $(date '+%H:%M:%S') $*"
}

log_error() {
    echo "[ERROR] $(date '+%H:%M:%S') $*" >&2
}

log_debug() {
    [[ "${DEBUG:-}" == "true" ]] && echo "[DEBUG] $*" >&2
}

# Anvandning
log_info "Starting"
log_error "Connection failed"

# Debug mode
DEBUG=true ./script.sh
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best Practice Template

```bash
#!/bin/bash
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0")"

cleanup() {
    local exit_code=$?
    # Cleanup
    exit $exit_code
}
trap cleanup EXIT

die() {
    echo "[ERROR] $*" >&2
    exit 1
}

# Validering
[[ $# -ge 1 ]] || die "Usage: $SCRIPT_NAME <arg>"
[[ -f "$1" ]] || die "File not found: $1"

# Main
main() {
    log_info "Starting"
    process "$1" || die "Failed"
    log_info "Done"
}

main "$@"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **set -euo pipefail** | Alltid i produktion |
| **$?** | Senaste exit code |
| **trap** | Cleanup och signaler |
| **>&2** | Fel till stderr |
| **die()** | Konsekvent felhantering |

**Kom ihåg:**
- **set -euo pipefail** - forsta raden efter shebang
- **trap EXIT** - garantera cleanup
- **>&2 for fel** - separera fran normal output
- **die() funktion** - konsekvent avslut
- **Logga allt** - latt att felsoka
""",
        },
        {
            "title": "Process Management",
            "slug": "process-management",
            "difficulty": "intermediate",
            "content": """# Process Management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor processhantering ar kritiskt |
|----------|-------------------------------------|
| **Parallell deploy** | Deploya till flera servrar samtidigt |
| **Background jobs** | Kora tasks utan att blocka |
| **CI/CD pipelines** | Hantera multipla build-steg |
| **Service management** | Starta, stoppa, overvaka processer |
| **Cleanup** | Sakerstalla att processer avslutas |

Utan processhantering kan du inte bygga robusta automation-losningar.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Process Arkitektur

```
┌─────────────────────────────────────────────────────────────┐
│                    BASH SHELL (parent)                      │
│                         PID: 1234                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌───────────┐   ┌───────────┐   ┌───────────┐            │
│   │ Child 1   │   │ Child 2   │   │ Child 3   │            │
│   │ PID: 1235 │   │ PID: 1236 │   │ PID: 1237 │            │
│   │ PPID:1234 │   │ PPID:1234 │   │ PPID:1234 │            │
│   └───────────┘   └───────────┘   └───────────┘            │
│         │               │               │                   │
│         ▼               ▼               ▼                   │
│      Running        Sleeping        Stopped                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Begrepp | Beskrivning |
|---------|-------------|
| **PID** | Process ID - unikt nummer |
| **PPID** | Parent Process ID |
| **State** | Running, Sleeping, Stopped, Zombie |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Bakgrundsprocesser

```bash
# Starta i bakgrunden
long_command &                       # & kor i bakgrunden
pid=$!                               # PID for senaste bakgrundsprocess

echo "Started process: $pid"

# Vanta pa process
wait $pid                            # Vanta pa specifik PID
echo "Exit code: $?"

wait                                 # Vanta pa ALLA bakgrundsprocesser

# Exempel - tre parallella processer
./process1.sh &
./process2.sh &
./process3.sh &
wait                                 # Vanta pa alla tre

# Med exit codes
./process1.sh &
pid1=$!
./process2.sh &
pid2=$!

wait $pid1 || echo "Process 1 failed"
wait $pid2 || echo "Process 2 failed"
```

| Syntax | Funktion |
|--------|----------|
| `command &` | Kor i bakgrunden |
| `$!` | PID for senaste bakgrundsprocess |
| `wait $pid` | Vanta pa specifik process |
| `wait` | Vanta pa alla bakgrundsprocesser |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Parallell Exekvering

```bash
# Parallella operationer
for server in server1 server2 server3; do
    ssh "$server" "uptime" &         # Kors parallellt
done
wait                                 # Vanta pa alla

# Med begransat antal parallella
max_parallel=4
pids=()

for file in *.txt; do
    process_file "$file" &
    pids+=($!)

    # Om vi natt max, vanta pa en
    if (( ${#pids[@]} >= max_parallel )); then
        wait "${pids[0]}"
        pids=("${pids[@]:1}")        # Ta bort forsta
    fi
done
wait                                 # Vanta pa resterande

# Med GNU Parallel (om installerat)
parallel process_file ::: *.txt      # Parallelliserar automatiskt
ls *.txt | parallel -j4 process_file # Max 4 parallella
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Subshells

```bash
# Subshell - kor i egen process
(cd /tmp && ls)                      # cd paverkar inte parent
echo $PWD                            # Fortfarande original

# Variabler i subshell
count=0
(
    count=10                         # Andrar bara i subshell
    echo "Inside: $count"            # 10
)
echo "Outside: $count"               # 0 (oforandrad)

# Pipe skapar subshell - VARNING!
count=0
echo "1 2 3" | while read num; do
    ((count++))                      # Subshell!
done
echo "Count: $count"                 # 0 (oforandrad)

# Losning: process substitution eller here-string
count=0
while read num; do
    ((count++))
done <<< "1 2 3"
echo "Count: $count"                 # 3 (korrekt)
```

| Problem | Losning |
|---------|---------|
| Pipe skapar subshell | Anvand `while ... done <<< "text"` |
| cd i subshell | Paverkar inte parent |
| Variabler i subshell | Anvand process substitution |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Processkontroll

```bash
# Hitta processer
ps aux                               # Alla processer
ps aux | grep nginx                  # Filtrera
pgrep nginx                          # PID:ar for nginx
pgrep -f "python script.py"          # Matcha hela kommandoraden
pidof nginx                          # PID for program

# Signaler
kill $pid                            # SIGTERM (graceful)
kill -9 $pid                         # SIGKILL (force)
kill -HUP $pid                       # SIGHUP (reload config)

# Doda alla med namn
pkill nginx                          # Doda alla nginx
pkill -f "python script.py"          # Matcha hela kommandoraden
killall nginx                        # Alternativ

# Kontrollera om process lever
if kill -0 $pid 2>/dev/null; then
    echo "Process is running"
else
    echo "Process is dead"
fi
```

| Signal | Betydelse |
|--------|-----------|
| **SIGTERM (15)** | Graceful shutdown |
| **SIGKILL (9)** | Force kill - kan ej ignoreras |
| **SIGHUP (1)** | Reload config |
| **SIGINT (2)** | Ctrl+C interrupt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Job Control och Locking

```bash
# Jobs i interaktiv shell
sleep 100 &                          # Starta i bakgrund
jobs                                 # Lista jobs
fg                                   # Fortsatt i forgrund
bg                                   # Fortsatt i bakgrund
fg %1                                # Specifikt job
disown %1                            # Job fortsatter efter logout
nohup command &                      # Ignorera SIGHUP

# Flock for fillasning
(
    flock -n 9 || { echo "Already running"; exit 1; }
    echo "Running exclusively..."
    sleep 10
) 9>/var/lock/myscript.lock

# Timeout
timeout 10 long_command              # Max 10 sekunder
timeout -s SIGKILL 10 command        # Force kill efter timeout
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **&** | Kor process i bakgrunden |
| **$!** | PID for senaste bakgrundsprocess |
| **wait** | Vanta pa bakgrundsprocesser |
| **kill -0** | Kontrollera om process lever |
| **flock** | Forhindra parallella korningar |

**Kom ihag:**
- Anvand `&` for att kora i bakgrunden
- Fanga PID med `$!` direkt efter start
- Subshells paverkar inte parent-variabler
- `kill -0` testar om process finns utan att doda
- Anvand flock eller PID-fil for mutual exclusion
""",
        },
        {
            "title": "Arrays & Associative Arrays",
            "slug": "arrays-associative-arrays",
            "difficulty": "intermediate",
            "content": """# Arrays & Associative Arrays

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor arrays ar kritiskt |
|----------|---------------------------|
| **Serverlistor** | Iterera over flera hosts |
| **Konfiguration** | Key-value par for settings |
| **Filhantering** | Hantera multipla filer |
| **Arguments** | Samla och processa flaggor |
| **Batch-operationer** | Parallella tasks |

Arrays gor Bash-scripting betydligt kraftfullare och mer strukturerat.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Array-typer

```
┌─────────────────────────────────────────────────────────────┐
│                    BASH ARRAY TYPES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   INDEXED ARRAY              ASSOCIATIVE ARRAY              │
│   ┌───┬───┬───┬───┐          ┌─────────┬─────────┐         │
│   │ 0 │ 1 │ 2 │ 3 │          │ "name"  │ "John"  │         │
│   ├───┼───┼───┼───┤          ├─────────┼─────────┤         │
│   │ a │ b │ c │ d │          │ "age"   │ "30"    │         │
│   └───┴───┴───┴───┘          ├─────────┼─────────┤         │
│                              │ "email" │ "j@e.c" │         │
│   arr=("a" "b" "c")          └─────────┴─────────┘         │
│                              declare -A user                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Typ | Syntax | Anvandning |
|-----|--------|------------|
| **Indexed** | `arr=()` | Numrerad lista |
| **Associative** | `declare -A arr` | Key-value hash |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Indexed Arrays

```bash
# Skapa array
fruits=("apple" "banana" "cherry")   # Array literal
fruits=()                            # Tom array
fruits[0]="apple"                    # Satt index

# Lasa element
echo "${fruits[0]}"                  # Forsta (apple)
echo "${fruits[1]}"                  # Andra (banana)
echo "${fruits[-1]}"                 # Sista (cherry)

# Alla element
echo "${fruits[@]}"                  # apple banana cherry
echo "${fruits[*]}"                  # Som en strang

# Langd
echo "${#fruits[@]}"                 # 3 (antal element)
echo "${#fruits[0]}"                 # 5 (langd av "apple")

# Index
echo "${!fruits[@]}"                 # 0 1 2 (alla index)

# Lagga till element
fruits+=("date")                     # Lagg till i slutet
fruits+=("elderberry" "fig")         # Lagg till flera

# Ta bort element
unset fruits[1]                      # Ta bort index 1
```

| Syntax | Resultat |
|--------|----------|
| `${arr[0]}` | Forsta elementet |
| `${arr[@]}` | Alla element |
| `${#arr[@]}` | Antal element |
| `${!arr[@]}` | Alla index |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Loopa over Arrays

```bash
# Loopa over varden
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Loopa med index
for i in "${!fruits[@]}"; do
    echo "Index $i: ${fruits[$i]}"
done

# VIKTIGT: Citera for element med mellanslag
files=("file one.txt" "file two.txt")
for file in "${files[@]}"; do        # Ratt - citerat
    echo "$file"
done

# C-style loop
for ((i=0; i<${#fruits[@]}; i++)); do
    echo "${fruits[$i]}"
done
```

| Metod | Anvandning |
|-------|------------|
| `for x in "${arr[@]}"` | Varje element |
| `for i in "${!arr[@]}"` | Varje index |
| `for ((i=0;...))` | C-style med counter |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Array-operationer

```bash
# Slicing
arr=(a b c d e f g)
echo "${arr[@]:2}"                   # c d e f g (fran index 2)
echo "${arr[@]:2:3}"                 # c d e (3 element fran 2)

# Kopiera array
copy=("${arr[@]}")

# Konkatenera arrays
arr1=(1 2 3)
arr2=(4 5 6)
combined=("${arr1[@]}" "${arr2[@]}")
echo "${combined[@]}"                # 1 2 3 4 5 6

# Soka i array
arr=(apple banana cherry)
if [[ " ${arr[*]} " =~ " banana " ]]; then
    echo "Found banana"
fi

# Funktion for existens
contains() {
    local element="$1"
    shift
    for item; do
        [[ "$item" == "$element" ]] && return 0
    done
    return 1
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Associative Arrays (Hash/Dict)

```bash
# MASTE deklareras forst
declare -A user

# Satta varden
user[name]="John"
user[age]=30
user[email]="john@example.com"

# Eller inline
declare -A colors=(
    [red]="#FF0000"
    [green]="#00FF00"
    [blue]="#0000FF"
)

# Lasa
echo "${user[name]}"                 # John
echo "${colors[red]}"                # #FF0000

# Alla nycklar
echo "${!user[@]}"                   # name age email

# Alla varden
echo "${user[@]}"                    # John 30 john@example.com

# Antal
echo "${#user[@]}"                   # 3

# Kontrollera om nyckel finns
if [[ -v user[name] ]]; then
    echo "Name exists"
fi

# Default-varde
echo "${user[missing]:-default}"
```

| Operation | Syntax |
|-----------|--------|
| **Deklarera** | `declare -A arr` |
| **Satt** | `arr[key]=value` |
| **Las** | `${arr[key]}` |
| **Nycklar** | `${!arr[@]}` |
| **Finns?** | `[[ -v arr[key] ]]` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska Exempel

```bash
# Las fil till array
mapfile -t lines < file.txt          # En rad per element
readarray -t lines < file.txt        # Samma sak

# Kommando-output till array
mapfile -t processes < <(ps aux | awk '{print $11}')

# Argument till array
args=("$@")                          # Alla script-argument

# Skapa array fran strang
str="apple,banana,cherry"
IFS=',' read -ra arr <<< "$str"
echo "${arr[@]}"                     # apple banana cherry

# Joina array till strang
arr=(apple banana cherry)
IFS=','
joined="${arr[*]}"
echo "$joined"                       # apple,banana,cherry
unset IFS

# Config som associative array
declare -A config
while IFS='=' read -r key value; do
    config[$key]="$value"
done < config.ini
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **declare -A** | Kravs for associative arrays |
| **${arr[@]}** | Alla element (med citattecken!) |
| **${!arr[@]}** | Alla nycklar/index |
| **mapfile -t** | Las fil till array |
| **[[ -v arr[key] ]]** | Kolla om nyckel finns |

**Kom ihag:**
- Citera ALLTID `"${arr[@]}"` for korrekt iteration
- Associative arrays kravs `declare -A` FORE anvandning
- `mapfile -t` ar basta sattet att lasa fil till array
- `${#arr[@]}` ger antal element
- Anvand associative arrays for key-value konfiguration
""",
        },
        {
            "title": "String Manipulation",
            "slug": "string-manipulation",
            "difficulty": "intermediate",
            "content": """# String Manipulation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor stringhantering ar kritiskt |
|----------|-----------------------------------|
| **Filnamn** | Parsa och manipulera paths |
| **Output** | Extrahera data fran kommandon |
| **Validering** | Kontrollera input-format |
| **Konfiguration** | Transformera varden |
| **Logging** | Formatera meddelanden |

Bash har kraftfulla inbyggda strangoperationer - snabbare an externa kommandon.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Parameter Expansion

```
┌─────────────────────────────────────────────────────────────┐
│                  PARAMETER EXPANSION                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ${var}         Variabelns varde                          │
│   ${#var}        Langd av strang                           │
│   ${var:pos}     Substring fran position                   │
│   ${var:pos:len} Substring med langd                       │
│                                                             │
│   ${var#pattern}   Ta bort minsta prefix                   │
│   ${var##pattern}  Ta bort storsta prefix                  │
│   ${var%pattern}   Ta bort minsta suffix                   │
│   ${var%%pattern}  Ta bort storsta suffix                  │
│                                                             │
│   ${var/old/new}   Ersatt forsta                           │
│   ${var//old/new}  Ersatt alla                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Operationer

```bash
str="Hello World"

# Langd
echo "${#str}"                       # 11

# Substring
echo "${str:0:5}"                    # Hello (5 tecken fran 0)
echo "${str:6}"                      # World (fran position 6)
echo "${str: -5}"                    # World (5 sista)

# Konkatenering
a="Hello"
b="World"
c="$a $b"                            # Hello World
c="${a}${b}"                         # HelloWorld

# Uppercase / Lowercase (Bash 4+)
str="Hello World"
echo "${str^^}"                      # HELLO WORLD
echo "${str,,}"                      # hello world
echo "${str^}"                       # Hello world (forsta upper)
```

| Syntax | Resultat |
|--------|----------|
| `${#str}` | Langd av strang |
| `${str:0:5}` | Forsta 5 tecken |
| `${str^^}` | UPPERCASE |
| `${str,,}` | lowercase |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pattern Matching och Replacement

```bash
# Ersattning
str="hello hello hello"
echo "${str/hello/hi}"               # hi hello hello (forsta)
echo "${str//hello/hi}"              # hi hi hi (alla)

# Ta bort (ersatt med inget)
echo "${str//hello/}"                # tar bort alla "hello"

# Prefix/suffix - VIKTIGT for filnamn!
str="hello.txt.bak"
echo "${str#*.}"                     # txt.bak (minsta prefix)
echo "${str##*.}"                    # bak (storsta prefix)
echo "${str%.*}"                     # hello.txt (minsta suffix)
echo "${str%%.*}"                    # hello (storsta suffix)

# Praktiska exempel
filename="document.txt"
echo "${filename%.*}"                # document (utan extension)
echo "${filename##*.}"               # txt (bara extension)

path="/home/user/documents/file.txt"
echo "${path##*/}"                   # file.txt (bara filnamn)
echo "${path%/*}"                    # /home/user/documents
```

| Pattern | Beskrivning |
|---------|-------------|
| `${str#*.}` | Ta bort fram till forsta `.` |
| `${str##*.}` | Ta bort fram till sista `.` |
| `${str%.*}` | Ta bort fran sista `.` |
| `${str%%.*}` | Ta bort fran forsta `.` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Default-varden

```bash
# Default om odefinierad eller tom
echo "${var:-default}"               # Anvand default, andra inte var
echo "${var:=default}"               # Satt var till default
echo "${var:+alternate}"             # alternate om var ar satt
echo "${var:?error message}"         # Exit med fel om osatt

# Utan kolon - bara odefinierad
echo "${var-default}"                # Default bara om odefinierad

# Praktiskt: miljovariabler med defaults
export DB_HOST="${DB_HOST:-localhost}"
export DB_PORT="${DB_PORT:-5432}"

# Validering
name="${1:?Usage: script.sh <name>}"  # Exit om argument saknas
```

| Syntax | Beteende |
|--------|----------|
| `${var:-default}` | Default om tom/osatt |
| `${var:=default}` | Satt och anvand default |
| `${var:+alt}` | alt om satt |
| `${var:?msg}` | Error om osatt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Regex med =~

```bash
# Regex matching
if [[ "hello123" =~ ^[a-z]+[0-9]+$ ]]; then
    echo "Match!"
fi

# Capture groups (BASH_REMATCH)
str="user@example.com"
if [[ "$str" =~ ^([^@]+)@(.+)$ ]]; then
    echo "User: ${BASH_REMATCH[1]}"   # user
    echo "Domain: ${BASH_REMATCH[2]}" # example.com
fi

# Praktiskt: extrahera version
version="v2.1.3-beta"
pattern='^v([0-9]+)[.]([0-9]+)[.]([0-9]+)'
if [[ "$version" =~ $pattern ]]; then
    major="${BASH_REMATCH[1]}"        # 2
    minor="${BASH_REMATCH[2]}"        # 1
    patch="${BASH_REMATCH[3]}"        # 3
fi

# Validera IP-adress (forenklad)
ip="192.168.1.100"
pattern='^[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+$'
if [[ "$ip" =~ $pattern ]]; then
    echo "Valid IP format"
fi
```

| Koncept | Anvandning |
|---------|------------|
| `[[ str =~ regex ]]` | Regex test |
| `BASH_REMATCH[0]` | Hela matchen |
| `BASH_REMATCH[1]` | Forsta capture group |
| Spar pattern i variabel | Undvik escape-problem |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Case Conversion och tr

```bash
# Case conversion (Bash 4+)
str="Hello World"
echo "${str^^}"                      # HELLO WORLD
echo "${str,,}"                      # hello world

# Transformera med tr
echo "hello" | tr '[:lower:]' '[:upper:]'  # HELLO
echo "HELLO" | tr 'A-Z' 'a-z'              # hello

# Ta bort tecken
echo "hello123" | tr -d '0-9'              # hello

# Squeeze duplicates
echo "hellooo" | tr -s 'o'                 # helo
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Splitta och Joina

```bash
# Splitta strang pa delimiter
str="one:two:three"
IFS=':' read -ra parts <<< "$str"
echo "${parts[0]}"                   # one
echo "${parts[1]}"                   # two

# Joina array till strang
arr=("one" "two" "three")
joined=$(IFS=':'; echo "${arr[*]}")
echo "$joined"                       # one:two:three

# Splitta filepath
path="/home/user/documents/file.txt"
dir=$(dirname "$path")               # /home/user/documents
file=$(basename "$path")             # file.txt
name="${file%.*}"                    # file
ext="${file##*.}"                    # txt
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **${var#pattern}** | Ta bort prefix |
| **${var%pattern}** | Ta bort suffix |
| **${var/old/new}** | Ersatt forsta |
| **${var:-default}** | Default-varde |
| **=~ regex** | Pattern matching |

**Kom ihag:**
- `${str##*.}` ger extension fran filnamn
- `${str%.*}` tar bort extension
- Spar regex i variabel for att undvika escape-problem
- Anvand inbyggd parameter expansion over externa kommandon
- `tr` ar bra for teckentransformationer
""",
        },
        {
            "title": "Functions & Scope",
            "slug": "functions-and-scope",
            "difficulty": "intermediate",
            "content": """# Functions & Scope

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor funktioner ar kritiskt |
|----------|------------------------------|
| **Ateranvandning** | Samma kod pa flera stallen |
| **Tydlighet** | Namngivna logiska block |
| **Testbarhet** | Isolerad kod att testa |
| **Underhall** | Andring pa ett stalle |
| **Libraries** | Dela kod mellan scripts |

Funktioner ar grundlaggande for strukturerad scripting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Funktionsstruktur

```
┌─────────────────────────────────────────────────────────────┐
│                    BASH FUNCTION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   function_name() {                                         │
│       local var1="$1"          # Argument 1                 │
│       local var2="$2"          # Argument 2                 │
│                                                             │
│       # Logik                                               │
│       process_something                                     │
│                                                             │
│       echo "result"            # Output via stdout          │
│       return 0                 # Exit code                  │
│   }                                                         │
│                                                             │
│   result=$(function_name arg1 arg2)                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Komponent | Roll |
|-----------|------|
| `$1, $2...` | Positionella argument |
| `local` | Variabel endast i funktionen |
| `echo` | Returnera varde |
| `return` | Exit code (0-255) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Definiera Funktioner

```bash
# Standardsyntax (POSIX-kompatibel)
greet() {
    echo "Hello, $1!"
}

# Alternativ syntax
function greet {
    echo "Hello, $1!"
}

# Med local variables
calculate_sum() {
    local a=$1                       # local = bara i funktionen
    local b=$2
    local sum=$((a + b))
    echo $sum
}

# Anropa
greet "World"                        # Hello, World!
result=$(calculate_sum 5 3)          # 8
```

| Syntax | Anvandning |
|--------|------------|
| `name() { }` | POSIX-kompatibel |
| `function name { }` | Bash-specifik |
| `local var` | Lokal variabel |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Argument

```bash
process_files() {
    echo "FUNCNAME: ${FUNCNAME[0]}"  # process_files
    echo "Argument count: $#"
    echo "All arguments: $@"
    echo "First: $1"
    echo "Second: $2"

    # Loopa over argument
    for file in "$@"; do
        echo "Processing: $file"
    done
}

process_files file1.txt file2.txt

# Shift for att processa argument
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -v|--verbose)
                verbose=true
                shift
                ;;
            -f|--file)
                file="$2"
                shift 2
                ;;
            *)
                echo "Unknown: $1"
                shift
                ;;
        esac
    done
}
```

| Variabel | Innehall |
|----------|----------|
| `$#` | Antal argument |
| `$@` | Alla argument (som array) |
| `$*` | Alla argument (som strang) |
| `${FUNCNAME[0]}` | Funktionens namn |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Return och Output

```bash
# Return = exit code (0-255)
is_even() {
    local num=$1
    if (( num % 2 == 0 )); then
        return 0                     # Success = true
    else
        return 1                     # Failure = false
    fi
}

if is_even 4; then
    echo "4 is even"
fi

# Returnera varden via echo + command substitution
get_timestamp() {
    date +%Y%m%d_%H%M%S
}

timestamp=$(get_timestamp)
echo "Timestamp: $timestamp"

# Returnera via nameref (Bash 4.3+)
get_data() {
    local -n result=$1               # Nameref
    result="computed value"
}

get_data myvar
echo "$myvar"                        # computed value
```

| Metod | Anvandning |
|-------|------------|
| `return N` | Exit code (0=success) |
| `echo result` | Returnera varde via stdout |
| `local -n ref` | Nameref for output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Scope - local vs global

```bash
# Default: variabler ar globala
var="global"

test_scope() {
    var="changed"                    # Andrar global!
    new_var="new"                    # Skapar global!
}

test_scope
echo "$var"                          # changed
echo "$new_var"                      # new

# local gor variabeln lokal
var="global"

test_local() {
    local var="local"                # Egen kopia
    echo "Inside: $var"              # local
}

test_local
echo "Outside: $var"                 # global (oforandrad)

# VIKTIGT: Alltid anvanda local!
correct_function() {
    local temp_file
    local result
    local i
    # Nu lacker inget till global scope
}
```

| Scope | Beteende |
|-------|----------|
| **Global** | Syns overallt (default) |
| **Local** | Bara i funktionen |
| **Export** | Syns i child-processer |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Best Practices

```bash
#!/bin/bash

# Dokumentera funktioner
#######################################
# Beskrivning av vad funktionen gor.
# Arguments:
#   $1 - filnamn att processa
# Returns:
#   0 om success, 1 om fil saknas
#######################################
process_file() {
    local file="$1"

    # Validera input
    if [[ -z "$file" ]]; then
        echo "Error: filename required" >&2
        return 1
    fi

    if [[ ! -f "$file" ]]; then
        echo "Error: file not found: $file" >&2
        return 1
    fi

    echo "Processing $file"
}

# BRA struktur - main pattern
main() {
    local config
    config=$(parse_config)
    process_data "$config"
}

# Helper-funktioner fore main
parse_config() { echo "config"; }
process_data() { echo "data: $1"; }

# Kor main sist
main "$@"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Funktionsbibliotek

```bash
# lib/utils.sh
#!/bin/bash

log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') $*"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2
}

die() {
    log_error "$@"
    exit 1
}

# main.sh - importera bibliotek
#!/bin/bash
source "$(dirname "$0")/lib/utils.sh"

log_info "Starting script"
[[ -f "$config" ]] || die "Config not found"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **local** | Anvand for ALLA variabler |
| **echo** | Returnera varden via stdout |
| **return** | Exit code (0=success) |
| **${FUNCNAME[0]}** | Funktionens namn |
| **source** | Importera funktionsbibliotek |

**Kom ihag:**
- Anvand `local` for ALLA variabler i funktioner
- Returnera varden via `echo` + command substitution
- `return` ar for exit code, inte varden
- Dokumentera funktioner med kommentarer
- Anvand main-pattern for struktur
""",
        },
        {
            "title": "Input & Output Redirection",
            "slug": "input-output-redirection",
            "difficulty": "intermediate",
            "content": """# Input & Output Redirection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor redirection ar kritiskt |
|----------|--------------------------------|
| **Loggning** | Spara output till fil |
| **Pipelines** | Kedja kommandon |
| **Felhantering** | Separera stdout/stderr |
| **Automation** | Input fran filer |
| **Debugging** | Tysta verbose output |

Redirection ar fundamentalt for effektiv Unix/Linux-scripting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Standard Streams

```
┌─────────────────────────────────────────────────────────────┐
│                    STANDARD STREAMS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    stdin (0)  ───►  ┌──────────────┐  ───►  stdout (1)     │
│    (keyboard)       │   COMMAND    │        (terminal)      │
│                     └──────────────┘  ───►  stderr (2)     │
│                                             (terminal)      │
│                                                             │
│    REDIRECT:                                                │
│    command > file       stdout till fil                     │
│    command 2> file      stderr till fil                     │
│    command < file       stdin fran fil                      │
│    command &> file      bade stdout och stderr              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Stream | FD | Default |
|--------|-----|---------|
| **stdin** | 0 | Keyboard |
| **stdout** | 1 | Terminal |
| **stderr** | 2 | Terminal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Redirection

```bash
# Output till fil
echo "Hello" > file.txt              # Skriv over
echo "World" >> file.txt             # Append

# Input fran fil
while read line; do
    echo "Line: $line"
done < file.txt

# Separera stdout och stderr
command > stdout.txt 2> stderr.txt

# Kombinera stdout och stderr
command > all.txt 2>&1               # Traditionell syntax
command &> all.txt                   # Bash kortform

# Tyst korning (discard output)
command > /dev/null                  # Ignorera stdout
command 2> /dev/null                 # Ignorera stderr
command &> /dev/null                 # Ignorera allt
```

| Syntax | Betydelse |
|--------|-----------|
| `>` | Skriv over fil |
| `>>` | Append till fil |
| `<` | Las fran fil |
| `2>` | Redirect stderr |
| `&>` | Redirect bade |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Pipes och Process Substitution

```bash
# Grundlaggande pipe
cat file.txt | grep "error" | wc -l

# Tee - skriv till fil OCH stdout
command | tee output.txt             # Visa + spara
command | tee -a output.txt          # Append

# Process substitution
diff <(ls dir1) <(ls dir2)           # Jamfor output som filer

# Lasa process output
while read -r line; do
    echo "Line: $line"
done < <(find . -name "*.txt")

# Named pipes (FIFO)
mkfifo /tmp/mypipe
cat > /tmp/mypipe &                  # Terminal 1
cat < /tmp/mypipe                    # Terminal 2
rm /tmp/mypipe
```

| Syntax | Funktion |
|--------|----------|
| `cmd1` pipe `cmd2` | Pipe stdout till nasta |
| `tee file` | Skriv till fil och stdout |
| `<(cmd)` | Process substitution |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Here Documents och Here Strings

```bash
# Here document - multi-line input
cat << EOF
This is line 1
This is line 2
Variable: $name
EOF

# Utan variabel-expansion
cat << 'EOF'
Literal: $name (not expanded)
EOF

# Here document till kommando
mysql -u root << EOF
SELECT * FROM users;
UPDATE settings SET value='new';
EOF

# Here string - enkel strang som input
grep "pattern" <<< "search in this string"

read -r first second <<< "hello world"
echo "First: $first"                 # hello
echo "Second: $second"               # world
```

| Syntax | Anvandning |
|--------|------------|
| `<< EOF` | Multi-line input |
| `<< 'EOF'` | Literal (ingen expansion) |
| `<<<` | Enkel strang input |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## File Descriptors

```bash
# Oppna egna file descriptors
exec 3> output.txt                   # FD 3 for skrivning
exec 4< input.txt                    # FD 4 for lasning

echo "Data" >&3                      # Skriv till FD 3
read line <&4                        # Las fran FD 4

exec 3>&-                            # Stang FD 3
exec 4<&-                            # Stang FD 4

# Duplicera file descriptor
exec 3>&1                            # FD 3 ar kopia av stdout
echo "To FD 3" >&3                   # Gar till original stdout
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska Patterns

```bash
# Logga med timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a script.log
}

# Kor block med redirection
{
    echo "Step 1"
    do_something
    echo "Step 2"
} >> execution.log 2>&1

# Fanga exit code fran pipe
set -o pipefail
false | true
echo $?                              # 1 (inte 0)

# Logga allt scriptet gor
exec > >(tee -a script.log)
exec 2>&1
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **>** | Skriv over fil |
| **>>** | Append till fil |
| **2>&1** | Kombinera stderr med stdout |
| **&>** | Kortform for bade |
| **< <(cmd)** | Process substitution |

**Kom ihag:**
- `>` skriver over, `>>` appendar
- `2>&1` kombinerar stderr med stdout
- `&> file` ar kortform for `> file 2>&1`
- `< <(command)` for process substitution
- `<<EOF` for here documents, `<<<` for here strings
""",
        },
        {
            "title": "Debugging Bash Scripts",
            "slug": "debugging-bash-scripts",
            "difficulty": "intermediate",
            "content": """# Debugging Bash Scripts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor debugging ar kritiskt |
|----------|------------------------------|
| **CI/CD-fel** | Pipelines som failar mystiskt |
| **Tysta fel** | Kommandon som inte ger feedback |
| **Variabel-expansion** | Ovantade varden |
| **Race conditions** | Timing-problem |
| **Produktionsissues** | Snabb felskning kravs |

Goda debug-tekniker sparar timmar av frustration.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Debug Modes

```
┌─────────────────────────────────────────────────────────────┐
│                    BASH DEBUG FLAGS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   set -x    (xtrace)     Visa varje kommando fore korning  │
│   set -v    (verbose)    Visa varje rad som lases          │
│   set -e    (errexit)    Avsluta vid fel                   │
│   set -u    (nounset)    Fel vid odefinierade variabler    │
│   set -o pipefail        Pipe failar om nagon del failar   │
│                                                             │
│   STRICT MODE:                                              │
│   set -euo pipefail      # Rekommenderat for produktion    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Flag | Effekt |
|------|--------|
| `-x` | Tracear varje kommando |
| `-e` | Avsluta vid fel |
| `-u` | Fel vid osatt variabel |
| `-o pipefail` | Pipe failar korrekt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Debug med set

```bash
#!/bin/bash

# Aktivera i script
set -x                               # Trace on
# ... kod som ska debuggas ...
set +x                               # Trace off

# Eller vid korning
bash -x script.sh                    # Hela scriptet i debug mode

# Kombinera modes
set -xv                              # Trace + verbose
set -euxo pipefail                   # "Strict mode" med trace

# Debug specifik sektion
debug_section() {
    set -x
    problematic_code
    set +x
}

# Villkorlig debug
if [[ "${DEBUG:-false}" == "true" ]]; then
    set -x
fi

# DEBUG=true ./script.sh             # Kor med debug
```

| Metod | Anvandning |
|-------|------------|
| `set -x` | Aktivera trace |
| `set +x` | Stang av trace |
| `bash -x script.sh` | Kor hela med trace |
| `DEBUG=true ./script.sh` | Villkorlig |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anpassa Trace Output (PS4)

```bash
# Anpassa trace prefix
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]:-main}: '

# Output blir:
# + script.sh:10:main: echo hello
# + script.sh:15:process_file: cat file.txt

# Mer detaljerad med timestamp
export PS4='+ $(date "+%H:%M:%S") ${BASH_SOURCE}:${LINENO}: '

# Trace till fil (inte terminal)
exec 4>&2                            # Spara stderr
exec 2> debug.log                    # Redirect stderr
set -x
# ... script ...
set +x
exec 2>&4                            # Aterstall stderr
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Fel och Losningar

```bash
# Fel: Odefinierad variabel
set -u                               # Aktivera check
echo "$undefined"                    # Error!
# Fix: Default value
echo "${undefined:-default}"

# Fel: Kommando failar tyst
result=$(failing_command)            # Ingen error!
# Fix: Check exit code
if ! result=$(failing_command); then
    echo "Command failed" >&2
    exit 1
fi

# Fel: Mellanslag i variabler
file="my file.txt"
cat $file                            # Fel!
# Fix: Citera ALLTID
cat "$file"                          # Ratt

# Fel: Subshell andrar inte parent
count=0
cat file.txt | while read line; do
    ((count++))
done
echo $count                          # 0!
# Fix: Process substitution
while read line; do
    ((count++))
done < <(cat file.txt)
echo $count                          # Korrekt!
```

| Problem | Losning |
|---------|---------|
| Osatt variabel | `${var:-default}` |
| Tyst fel | `set -e` eller explicit check |
| Mellanslag | Citera alltid: `"$var"` |
| Pipe subshell | Process substitution |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Trap for Debugging

```bash
#!/bin/bash

# Visa rad vid fel
trap 'echo "Error on line $LINENO: $BASH_COMMAND" >&2' ERR

# Stack trace vid fel
trap_handler() {
    local exit_code=$?
    echo "=== ERROR ===" >&2
    echo "Exit code: $exit_code" >&2
    echo "Command: $BASH_COMMAND" >&2
    echo "Line: $LINENO" >&2
    echo "Stack trace:" >&2

    local i=0
    while caller $i; do
        ((i++))
    done >&2

    exit $exit_code
}

trap trap_handler ERR

# Cleanup + debug info
trap_exit() {
    local exit_code=$?
    if [[ $exit_code -ne 0 ]]; then
        echo "Script failed with exit code $exit_code" >&2
    fi
    rm -f /tmp/script_temp_$$
}

trap trap_exit EXIT
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ShellCheck

```bash
# Installera shellcheck
brew install shellcheck              # macOS
apt install shellcheck               # Ubuntu

# Analysera script
shellcheck script.sh

# Ignorera specifik varning
# shellcheck disable=SC2086
echo $unquoted_var

# Integrera med VS Code
# Installera "ShellCheck" extension
```

| ShellCheck | Funktion |
|------------|----------|
| `SC2086` | Quote expansion varning |
| `SC2034` | Unused variable |
| `SC2155` | Declare och assign separat |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **set -x** | Trace varje kommando |
| **set -euo pipefail** | Strict mode |
| **PS4** | Anpassa trace-output |
| **trap ERR** | Stack trace vid fel |
| **ShellCheck** | Statisk analys |

**Kom ihag:**
- Anvand `set -euo pipefail` i produktion
- `PS4` kan visa fil, rad och funktion
- Citera ALLA variabler: `"$var"` inte `$var`
- `trap ERR` ger stack trace vid fel
- Installera ShellCheck i din editor
""",
        },
        {
            "title": "Working with APIs (curl)",
            "slug": "working-with-apis-curl",
            "difficulty": "intermediate",
            "content": """# Working with APIs (curl)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor curl ar kritiskt |
|----------|-------------------------|
| **Health checks** | Verifiera service-status |
| **Webhooks** | Trigga CI/CD events |
| **Cloud APIs** | AWS, GCP, Azure automation |
| **Monitoring** | Metrik och alerting |
| **Debugging** | Testa endpoints |

curl ar det universella verktyget for HTTP-kommunikation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## curl Grundlaggande

```
┌─────────────────────────────────────────────────────────────┐
│                      curl REQUEST                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   curl [options] URL                                        │
│                                                             │
│   OPTIONS:                                                  │
│   -s       Silent (ingen progress)                         │
│   -f       Fail silently pa HTTP error                     │
│   -H       Add header                                       │
│   -d       POST data                                        │
│   -X       HTTP method (GET, POST, PUT, DELETE)            │
│   -o       Output till fil                                  │
│   -w       Format output                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Flag | Funktion |
|------|----------|
| `-s` | Silent - ingen progress |
| `-f` | Fail pa HTTP errors |
| `-H` | Lagg till header |
| `-d` | Skicka data |
| `-X` | HTTP method |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## GET och Diagnostik

```bash
# Enkel GET
curl https://api.example.com/users

# Tysta progress
curl -s https://api.example.com/users

# Med headers
curl -H "Accept: application/json" \\
     https://api.example.com/users

# Visa response headers
curl -i https://api.example.com/users

# Bara headers (HEAD)
curl -I https://api.example.com/users

# Verbose debugging
curl -v https://api.example.com/users
```

| Metod | Anvandning |
|-------|------------|
| `-s` | Script-vanligt |
| `-i` | Se response headers |
| `-I` | Bara headers |
| `-v` | Full debug |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## POST, PUT, DELETE

```bash
# POST med JSON
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d '{"name": "John", "email": "john@example.com"}' \\
     https://api.example.com/users

# POST fran fil
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d @data.json \\
     https://api.example.com/users

# PUT (update)
curl -X PUT \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Jane"}' \\
     https://api.example.com/users/123

# DELETE
curl -X DELETE https://api.example.com/users/123
```

| HTTP Method | Anvandning |
|-------------|------------|
| **GET** | Hamta data |
| **POST** | Skapa ny resurs |
| **PUT** | Uppdatera helt |
| **PATCH** | Uppdatera delvis |
| **DELETE** | Ta bort |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Authentication

```bash
# Basic auth
curl -u username:password https://api.example.com/secure

# Bearer token
curl -H "Authorization: Bearer $TOKEN" \\
     https://api.example.com/users

# API key i header
curl -H "X-API-Key: $API_KEY" \\
     https://api.example.com/data

# OAuth2 token request
curl -X POST \\
     -d "grant_type=client_credentials" \\
     -d "client_id=$CLIENT_ID" \\
     -d "client_secret=$CLIENT_SECRET" \\
     https://auth.example.com/oauth/token
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Response Handling

```bash
# Spara response
curl -s https://api.example.com/users > response.json

# Bara HTTP status code
curl -s -o /dev/null -w "%{http_code}" https://api.example.com/health

# Exit code baserat pa HTTP status
curl -f https://api.example.com/users || echo "Request failed"

# Timeout
curl -s --connect-timeout 5 --max-time 10 \\
     https://api.example.com/slow-endpoint
```

| Write-out | Varde |
|-----------|-------|
| `%{http_code}` | HTTP status |
| `%{time_total}` | Total tid |
| `%{size_download}` | Response-storlek |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSON med jq

```bash
# Installera
brew install jq                      # macOS
apt install jq                       # Ubuntu

# Pretty print
curl -s https://api.example.com/users | jq .

# Extrahera falt
curl -s https://api.example.com/users | jq '.[0].name'

# Filtrera
curl -s https://api.example.com/users | jq '.[] | select(.active == true)'

# Raw output (utan citattecken)
name=$(curl -s https://api.example.com/users/1 | jq -r '.name')

# Langd/count
curl -s https://api.example.com/users | jq length
```

| jq | Funktion |
|-----|----------|
| `.` | Hela objektet |
| `.field` | Specifikt falt |
| `.[]` | Iterera over array |
| `-r` | Raw output |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Health Check Pattern

```bash
# Health check med retry
health_check() {
    local url="$1"
    local max_attempts="${2:-5}"
    local attempt=1

    while (( attempt <= max_attempts )); do
        if curl -sf -o /dev/null "$url"; then
            echo "Health check passed"
            return 0
        fi
        echo "Attempt $attempt failed, retrying..."
        sleep 2
        ((attempt++))
    done

    echo "Health check failed after $max_attempts attempts"
    return 1
}

health_check "https://api.example.com/health"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **-s** | Silent - for scripting |
| **-f** | Fail pa HTTP errors |
| **-w "%{http_code}"** | Hamta status code |
| **jq -r** | Raw JSON output |
| **--max-time** | Timeout |

**Kom ihag:**
- Anvand `-sf` for scripts (silent + fail)
- `-w "%{http_code}"` ger HTTP status
- `jq -r` tar bort citattecken fran output
- Kombinera curl + jq for kraftfull API-scripting
- Inkludera alltid timeout i produktion
""",
        },
        {
            "title": "Script Arguments & Options",
            "slug": "script-arguments-options",
            "difficulty": "intermediate",
            "content": """# Script Arguments & Options

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor argument ar kritiskt |
|----------|----------------------------|
| **Flexibilitet** | Samma script for olika fall |
| **Automation** | CI/CD kan skicka parametrar |
| **Konfiguration** | Override defaults |
| **Dokumentation** | --help visar anvandning |
| **Validering** | Sakerstall korrekt input |

Professionella scripts behover argument-parsing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Argument Variabler

```
┌─────────────────────────────────────────────────────────────┐
│                   SCRIPT ARGUMENTS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ./script.sh arg1 arg2 arg3                                │
│                                                             │
│   $0    = ./script.sh     (script namn)                     │
│   $1    = arg1            (forsta argument)                 │
│   $2    = arg2            (andra argument)                  │
│   $3    = arg3            (tredje argument)                 │
│   $#    = 3               (antal argument)                  │
│   $@    = arg1 arg2 arg3  (alla som array)                  │
│   $*    = "arg1 arg2 arg3" (alla som strang)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Variabel | Innehall |
|----------|----------|
| `$0` | Script-namn |
| `$1-$9` | Positionella argument |
| `$#` | Antal argument |
| `$@` | Alla som array |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Positionella Argument

```bash
#!/bin/bash

# Grundlaggande anvandning
echo "Script: $0"
echo "First arg: $1"
echo "Second arg: $2"
echo "All args: $@"
echo "Arg count: $#"

# Validering
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <source> <destination>" >&2
    exit 1
fi

source="$1"
dest="$2"

# Default-varden
output="${3:-output.txt}"            # Default om ej given

# Shift for att processa
while [[ $# -gt 0 ]]; do
    echo "Processing: $1"
    shift                            # Ta bort forsta
done
```

| Metod | Anvandning |
|-------|------------|
| `${1:-default}` | Default om saknas |
| `shift` | Ta bort forsta argument |
| `$#` | Validera antal |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## getopts for Short Options

```bash
#!/bin/bash

usage() {
    echo "Usage: $0 [-v] [-f file] [-n count] source dest"
    exit 1
}

verbose=false
output_file=""
count=1

while getopts "vf:n:h" opt; do
    case $opt in
        v)
            verbose=true
            ;;
        f)
            output_file="$OPTARG"    # Argument till -f
            ;;
        n)
            count="$OPTARG"
            ;;
        h)
            usage
            ;;
        ?)
            usage
            ;;
    esac
done

# Flytta forbi options
shift $((OPTIND - 1))

source="$1"
dest="$2"
```

| getopts | Betydelse |
|---------|-----------|
| `"vf:n:"` | v utan arg, f och n med arg |
| `$OPTARG` | Argumentets varde |
| `$OPTIND` | Index efter options |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Long Options med case

```bash
#!/bin/bash

verbose=false
output_file=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            verbose=true
            shift
            ;;
        -f|--file)
            output_file="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        -*)
            echo "Unknown option: $1" >&2
            usage
            ;;
        *)
            break                    # Sluta parsa options
            ;;
    esac
done

# Resterande ar positionella
command="${1:-}"
```

| Pattern | Betydelse |
|---------|-----------|
| `-v` eller `--verbose` | Kort eller lang |
| `shift` | Flytta 1 position |
| `shift 2` | Flytta 2 (option + arg) |
| `*)` | Okand option |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Argument Validering

```bash
#!/bin/bash

die() {
    echo "Error: $*" >&2
    exit 1
}

# Validera fil finns
validate_file() {
    local file="$1"
    [[ -z "$file" ]] && die "File required"
    [[ ! -f "$file" ]] && die "Not found: $file"
    [[ ! -r "$file" ]] && die "Not readable: $file"
}

# Validera nummer
validate_number() {
    local value="$1"
    local name="$2"
    local min="${3:-}"
    local max="${4:-}"

    [[ ! "$value" =~ ^[0-9]+$ ]] && die "$name must be number"
    [[ -n "$min" && $value -lt $min ]] && die "$name >= $min"
    [[ -n "$max" && $value -gt $max ]] && die "$name <= $max"
}

# Anvandning
validate_file "$config_file"
validate_number "$port" "Port" 1 65535
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Interaktiv Input

```bash
# Enkel prompt
read -p "Enter name: " name

# Med default
read -p "Port [8080]: " port
port="${port:-8080}"

# Password (dold input)
read -s -p "Password: " password
echo

# Ja/Nej confirm
confirm() {
    read -p "$1 [y/N]: " response
    [[ "$response" =~ ^[Yy]$ ]]
}

if confirm "Continue?"; then
    echo "Proceeding..."
fi

# Timeout
if read -t 10 -p "Value (10s): " value; then
    echo "Got: $value"
else
    echo "Timeout!"
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **getopts** | Short options (-v, -f) |
| **case loop** | Long options (--verbose) |
| **shift** | Flytta argument-position |
| **$OPTARG** | Option-argument varde |
| **--help** | Dokumentera alltid |

**Kom ihag:**
- Anvand getopts for enkla short options
- Manual case-loop for long options
- Validera alla inputs fore anvandning
- Inkludera alltid --help med exempel
- shift tar bort forsta argumentet
""",
        },
        {
            "title": "Cron Jobs & Scheduling",
            "slug": "cron-jobs-scheduling",
            "difficulty": "intermediate",
            "content": """# Cron Jobs & Scheduling

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor cron ar kritiskt |
|----------|-------------------------|
| **Backup** | Automatisk nattlig backup |
| **Monitoring** | Periodiska health checks |
| **Maintenance** | Log rotation, cleanup |
| **Reports** | Dagliga/veckliga rapporter |
| **Sync** | Synkronisera data regelbundet |

Cron ar standard for Unix-schemaläggning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cron Syntax

```
┌───────────────────────────────────────────────────────────┐
│              CRON EXPRESSION FORMAT                       │
├───────────────────────────────────────────────────────────┤
│                                                           │
│   * * * * * command                                       │
│   | | | | |                                               │
│   | | | | +-- Veckodag (0-7, 0/7 = sondag)                │
│   | | | +---- Manad (1-12)                                │
│   | | +------ Dag i manad (1-31)                          │
│   | +-------- Timme (0-23)                                │
│   +---------- Minut (0-59)                                │
│                                                           │
│   Specialtecken:                                          │
│   *   = alla varden                                       │
│   */n = varje n:te                                        │
│   n,m = specifika varden                                  │
│   n-m = intervall                                         │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Crontab-hantering

```bash
# Visa crontab
crontab -l

# Redigera crontab
crontab -e

# Installera fran fil
crontab mycrontab.txt

# Ta bort alla cron jobs
crontab -r

# Visa annan anvandares crontab (root)
crontab -u username -l
```

| Kommando | Funktion |
|----------|----------|
| `crontab -l` | Lista jobb |
| `crontab -e` | Redigera |
| `crontab -r` | Ta bort alla |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga Cron-uttryck

```bash
# Varje minut
* * * * * /path/to/script.sh

# Varje timme (pa minuten)
0 * * * * /path/to/script.sh

# Varje dag kl 03:00
0 3 * * * /path/to/script.sh

# Mandag kl 09:00
0 9 * * 1 /path/to/script.sh

# Var 5:e minut
*/5 * * * * /path/to/script.sh

# Varje timme mellan 9-17
0 9-17 * * * /path/to/script.sh

# Mandag-fredag kl 08:30
30 8 * * 1-5 /path/to/script.sh

# Forsta dagen varje manad
0 0 1 * * /path/to/monthly_backup.sh
```

| Uttryck | Betydelse |
|---------|-----------|
| `0 3 * * *` | Varje dag kl 03:00 |
| `*/5 * * * *` | Var 5:e minut |
| `0 9-17 * * 1-5` | 09-17 mån-fre |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Speciella Strangar

```bash
@reboot     /path/to/script.sh    # Vid systemstart
@yearly     /path/to/script.sh    # 0 0 1 1 *
@monthly    /path/to/script.sh    # 0 0 1 * *
@weekly     /path/to/script.sh    # 0 0 * * 0
@daily      /path/to/script.sh    # 0 0 * * *
@hourly     /path/to/script.sh    # 0 * * * *
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Environment och Paths

```bash
# Cron har minimal environment!
# Satt viktiga variabler i crontab

SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@example.com

# Eller i scriptet
#!/bin/bash
export PATH="/usr/local/bin:/usr/bin:/bin"

# Anvand ALLTID absoluta paths
0 3 * * * /home/user/scripts/backup.sh

# INTE:
# 0 3 * * * backup.sh              # Funkar inte!
```

| Problem | Losning |
|---------|---------|
| PATH saknas | Satt i crontab |
| Relativ path | Anvand absolut |
| Environment | Source profile |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Output och Logging

```bash
# Cron skickar output via mail
MAILTO=admin@example.com
0 3 * * * /path/to/backup.sh

# Tysta (ingen output)
0 3 * * * /path/to/backup.sh > /dev/null 2>&1

# Logga till fil
0 3 * * * /path/to/backup.sh >> /var/log/backup.log 2>&1

# Bättre: logga i scriptet
#!/bin/bash
exec >> /var/log/backup.log 2>&1
echo "=== Backup started: $(date) ==="
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Cron-vanligt Script

```bash
#!/bin/bash
# Cron: 0 3 * * * /home/user/scripts/backup.sh

set -euo pipefail

readonly LOG_FILE="/var/log/backup.log"
readonly LOCK_FILE="/var/run/backup.lock"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

# Las for parallella korningar
acquire_lock() {
    if ! mkdir "$LOCK_FILE" 2>/dev/null; then
        log "ERROR: Another instance running"
        exit 1
    fi
    trap 'rm -rf "$LOCK_FILE"' EXIT
}

main() {
    acquire_lock
    log "Backup started"

    if /usr/bin/rsync -av /data/ /backup/; then
        log "Backup completed"
    else
        log "ERROR: Backup failed"
        exit 1
    fi
}

main "$@"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Systemd Timers (Modern Alternativ)

```bash
# /etc/systemd/system/backup.service
[Unit]
Description=Daily backup

[Service]
Type=oneshot
ExecStart=/home/user/scripts/backup.sh

# /etc/systemd/system/backup.timer
[Timer]
OnCalendar=*-*-* 03:00:00
Persistent=true

[Install]
WantedBy=timers.target

# Aktivera
sudo systemctl enable backup.timer
sudo systemctl start backup.timer

# Status
systemctl list-timers
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Felsökning

```bash
# Testa script manuellt forst!
/path/to/script.sh

# Simulera cron-environment
env -i /bin/bash --noprofile --norc -c '/path/to/script.sh'

# Kontrollera cron-loggar
grep CRON /var/log/syslog
journalctl -u cron

# Kontrollera att cron kors
systemctl status cron
```

| Problem | Losning |
|---------|---------|
| Script kors inte | Kontrollera PATH |
| Ingen output | Logga till fil |
| Permission denied | chmod +x script |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Cron-format** | min tim dag man veckodag |
| **Absoluta paths** | Anvand ALLTID |
| **Logging** | >> logfile 2>&1 |
| **Lock-fil** | Forhindra parallella |
| **Testa forst** | Kor manuellt innan |

**Kom ihag:**
- Cron har minimal environment
- Anvand alltid absoluta paths
- Logga all output till fil
- Anvand lock-fil for langvariga jobb
- Testa scripts manuellt fore schemaläggning
""",
        },
        {
            "title": "Configuration Files",
            "slug": "configuration-files",
            "difficulty": "intermediate",
            "content": """# Configuration Files

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor config ar kritiskt |
|----------|---------------------------|
| **Flexibilitet** | Andra utan att redigera kod |
| **Sakerhet** | Secrets utanfor kod |
| **Miljoer** | Dev vs staging vs prod |
| **Audit** | Versionera konfiguration |
| **Automation** | CI/CD kan overrida |

Konfigurationsfiler separerar installningar fran logik.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Config-format Oversikt

```
┌─────────────────────────────────────────────────────────────┐
│                 CONFIG FILE FORMATS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ENV-filer (.env):      KEY=VALUE                          │
│   INI-filer (.ini):      [section] key=value                │
│   YAML (.yaml/.yml):     Strukturerad data                  │
│   JSON (.json):          JavaScript Object Notation         │
│                                                             │
│   Bash kan parsa ENV/INI direkt                             │
│   YAML/JSON kraver yq/jq verktyg                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ENV-filer (.env)

```bash
# .env fil
DATABASE_URL=postgresql://localhost/myapp
REDIS_HOST=localhost
REDIS_PORT=6379
API_KEY=secret123
DEBUG=true

# Ladda i script - enkel metod
set -a                               # Auto-export
source .env
set +a

# Saker metod (ignorerar kommentarer)
load_env() {
    local file="${1:-.env}"
    [[ ! -f "$file" ]] && return 1

    while IFS='=' read -r key value; do
        [[ -z "$key" || "$key" =~ ^# ]] && continue
        export "$key=$value"
    done < "$file"
}

load_env .env
load_env .env.local                  # Override
```

| Metod | Anvandning |
|-------|------------|
| `source .env` | Enkel men osakrare |
| `load_env()` | Saker med validering |
| `set -a` | Auto-export allt |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## INI-filer

```bash
# config.ini
[database]
host = localhost
port = 5432
name = myapp

[redis]
host = localhost
port = 6379

# Parser
declare -A config

parse_ini() {
    local file="$1"
    local section=""

    while IFS= read -r line; do
        line="${line##*( )}"         # Trim
        [[ -z "$line" || "$line" =~ ^[#] ]] && continue

        # Sektion [header]
        if [[ "$line" =~ ^\\[(.+)\\]$ ]]; then
            section="${BASH_REMATCH[1]}"
            continue
        fi

        # Key = Value
        if [[ "$line" =~ ^([^=]+)=(.*)$ ]]; then
            local key="${BASH_REMATCH[1]// /}"
            local value="${BASH_REMATCH[2]// /}"
            config["${section}_${key}"]="$value"
        fi
    done < "$file"
}

parse_ini config.ini
echo "DB Host: ${config[database_host]}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## YAML med yq

```bash
# config.yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin

# Installera yq
brew install yq                      # macOS
snap install yq                      # Ubuntu

# Lasa varden
yq '.database.host' config.yaml      # localhost
yq '.database.port' config.yaml      # 5432

# I script
db_host=$(yq '.database.host' config.yaml)
db_port=$(yq '.database.port' config.yaml)

# Uppdatera YAML
yq -i '.database.port = 5433' config.yaml
```

| Kommando | Funktion |
|----------|----------|
| `yq '.key'` | Lasa varde |
| `yq -i` | Uppdatera inline |
| `yq '. * load()'` | Merge configs |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## JSON med jq

```bash
# config.json
{
  "database": {
    "host": "localhost",
    "port": 5432
  },
  "features": ["caching", "logging"]
}

# Lasa
jq '.database.host' config.json      # "localhost"
jq -r '.database.host' config.json   # localhost (raw)
jq '.features[0]' config.json        # "caching"

# I script
db_host=$(jq -r '.database.host' config.json)
```

| Flag | Funktion |
|------|----------|
| `-r` | Raw output (utan quotes) |
| `-c` | Compact output |
| `-e` | Exit 1 om null |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Hierarkisk Konfiguration

```bash
#!/bin/bash
# Ladda config med override-stod

load_config() {
    local env="${APP_ENV:-development}"

    # 1. Base config
    [[ -f config/default.env ]] && source config/default.env

    # 2. Environment-specifik
    [[ -f "config/$env.env" ]] && source "config/$env.env"

    # 3. Lokal override (gitignored)
    [[ -f config/local.env ]] && source config/local.env
}

# Defaults i scriptet
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"

# Validera required config
require_config() {
    local var_name="$1"
    [[ -z "${!var_name:-}" ]] && {
        echo "Error: $var_name required" >&2
        exit 1
    }
}

require_config DATABASE_URL
require_config API_KEY
```

| Prioritet | Kalla |
|-----------|-------|
| 1 (lagst) | default.env |
| 2 | environment.env |
| 3 (hogst) | local.env |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Secrets-hantering

```bash
# ALDRIG i version control!
# .gitignore: *.env.local, secrets/

# Alt 1: Environment variables (CI/CD)
# Satts i CI/CD-verktyget

# Alt 2: AWS Secrets Manager
aws secretsmanager get-secret-value \\
    --secret-id myapp/production | \\
    jq -r '.SecretString' > /tmp/secrets.env
source /tmp/secrets.env
rm /tmp/secrets.env                  # Rensa direkt

# Alt 3: Docker secrets
# I container: cat /run/secrets/db_password
DB_PASSWORD="$(cat /run/secrets/db_password)"
```

| Metod | Anvandning |
|-------|------------|
| CI/CD env vars | Enklast |
| Secrets Manager | Production |
| Docker secrets | Containers |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Template-ersattning

```bash
# config.template
DATABASE_URL=postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}

# Generera config
export DB_USER=admin
export DB_PASS=secret
export DB_HOST=localhost

envsubst < config.template > config.env
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **ENV-filer** | KEY=VALUE, source direkt |
| **yq/jq** | YAML/JSON parsing |
| **Hierarki** | defaults -> env -> local |
| **Secrets** | ALDRIG i version control |
| **envsubst** | Template-ersattning |

**Kom ihag:**
- Separera secrets fran config
- Anvand hierarkisk loading for overrides
- yq for YAML, jq for JSON
- Validera required config vid uppstart
- Aldrig committa secrets till git
""",
        },
        {
            "title": "Production Script Patterns",
            "slug": "production-script-patterns",
            "difficulty": "advanced",
            "content": """# Production Script Patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor monster ar kritiskt |
|----------|---------------------------|
| **Palitlighet** | Fungerar under alla forhallanden |
| **Sakerhet** | Undviker race conditions |
| **Aterstallning** | Rollback vid fel |
| **Audit** | Loggning for sparbarhet |
| **Idempotent** | Sakert att kora flera ganger |

Battle-tested monster for verklig produktion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Production Principer

```
┌─────────────────────────────────────────────────────────────┐
│              PRODUCTION SCRIPT PRINCIPLES                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Defensive Programming:                                    │
│   - Anta att allt kan ga fel                                │
│   - Validera all input                                      │
│   - Hantera alla edge cases                                 │
│                                                             │
│   Idempotency:                                              │
│   - Sakert att kora flera ganger                            │
│   - Samma resultat varje gang                               │
│                                                             │
│   Atomicity:                                                │
│   - Allt lyckas eller inget andras                          │
│   - Rollback vid fel                                        │
│                                                             │
│   Observability:                                            │
│   - Logga allt viktigt                                      │
│   - Tydliga felmeddelanden                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Script Template

```bash
#!/bin/bash
# script_name.sh - Description
# Usage: script_name.sh [OPTIONS] <arg>

set -euo pipefail
IFS=$'\\n\\t'

# Configuration
readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
readonly LOG_DIR="/var/log/myapp"
readonly LOCK_FILE="/var/run/${SCRIPT_NAME}.lock"

VERBOSE=false
DRY_RUN=false

# Logging
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >&2; }
die() { log "ERROR: $*"; exit 1; }

# Cleanup
cleanup() {
    [[ -d "$LOCK_FILE" ]] && rmdir "$LOCK_FILE" 2>/dev/null
}
trap cleanup EXIT

# Lock
acquire_lock() {
    mkdir "$LOCK_FILE" 2>/dev/null || die "Already running"
}

# Main
main() {
    acquire_lock
    log "Starting $SCRIPT_NAME"
    # ... logic ...
    log "Completed"
}

main "$@"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Idempotent Operations

```bash
# Idempotent = sakert att kora flera ganger

# Skapa katalog
mkdir -p /path/to/dir                # OK om finns

# Skapa symlink
ln -sf /source /target               # Force overwrite

# Lagg till rad om den inte finns
grep -qxF 'line' file || echo 'line' >> file

# Lagg till i /etc/hosts
add_host_entry() {
    local ip="$1"
    local hostname="$2"
    if ! grep -q "^$ip.*$hostname" /etc/hosts; then
        echo "$ip $hostname" >> /etc/hosts
    fi
}

# Skapa user
ensure_user() {
    local username="$1"
    id "$username" &>/dev/null || useradd -m "$username"
}
```

| Operation | Idempotent metod |
|-----------|-----------------|
| mkdir | `mkdir -p` |
| ln | `ln -sf` |
| Add line | `grep eller echo` |
| Create user | `id eller useradd` |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Atomic Operations

```bash
# Atomic = allt lyckas eller inget andras

# Atomic file write
atomic_write() {
    local target="$1"
    local content="$2"
    local tmp_file

    tmp_file="$(mktemp "${target}.XXXXXX")"
    echo "$content" > "$tmp_file"
    mv "$tmp_file" "$target"         # Atomic move
}

# Atomic config update
update_config() {
    local file="$1"
    local key="$2"
    local value="$3"

    local tmp_file
    tmp_file="$(mktemp)"
    sed "s|^$key=.*|$key=$value|" "$file" > "$tmp_file"

    # Validera fore replace
    validate_config "$tmp_file" || {
        rm "$tmp_file"
        return 1
    }

    mv "$tmp_file" "$file"
}

# Transaction pattern
do_transaction() {
    local backup_dir
    backup_dir="$(mktemp -d)"
    cp -r /data "$backup_dir/"       # Backup

    if ! { op1 && op2 && op3; }; then
        # Rollback
        rm -rf /data
        mv "$backup_dir/data" /data
        return 1
    fi

    rm -rf "$backup_dir"
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Retry Patterns

```bash
# Exponential backoff
retry_with_backoff() {
    local max_attempts=$1
    shift
    local cmd=("$@")

    local attempt=1
    local wait_time=1

    while (( attempt <= max_attempts )); do
        log "Attempt $attempt/$max_attempts"

        if "${cmd[@]}"; then
            return 0
        fi

        if (( attempt < max_attempts )); then
            log "Failed, retry in ${wait_time}s..."
            sleep $wait_time
            wait_time=$((wait_time * 2))
        fi
        ((attempt++))
    done

    log "All $max_attempts attempts failed"
    return 1
}

# Anvandning
retry_with_backoff 5 curl -sf http://api.example.com/health
```

| Backoff | Vanttetid |
|---------|-----------|
| Attempt 1 | 1s |
| Attempt 2 | 2s |
| Attempt 3 | 4s |
| Attempt 4 | 8s |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Health Checks

```bash
health_check() {
    local failures=0

    # Disk space
    local disk_usage
    disk_usage=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
    if (( disk_usage > 90 )); then
        log "Disk usage critical: ${disk_usage}%"
        ((failures++))
    fi

    # Memory
    local mem_available
    mem_available=$(awk '/MemAvailable/ {print $2}' /proc/meminfo)
    if (( mem_available < 1048576 )); then
        log "Low memory: ${mem_available}kB"
        ((failures++))
    fi

    # Service check
    if ! systemctl is-active --quiet nginx; then
        log "nginx not running"
        ((failures++))
    fi

    # API check
    if ! curl -sf http://localhost:8080/health; then
        log "API health failed"
        ((failures++))
    fi

    (( failures == 0 ))
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Logging Library

```bash
declare -A LOG_LEVELS=([DEBUG]=0 [INFO]=1 [WARN]=2 [ERROR]=3)
LOG_LEVEL="${LOG_LEVEL:-INFO}"

log() {
    local level="$1"
    shift
    local timestamp
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

    if [[ ${LOG_LEVELS[$level]} -ge ${LOG_LEVELS[$LOG_LEVEL]} ]]; then
        printf "[%s] [%s] [%s] %s\\n" "$timestamp" "$level" "$$" "$*" >&2
    fi
}

log_debug() { log DEBUG "$@"; }
log_info()  { log INFO "$@"; }
log_warn()  { log WARN "$@"; }
log_error() { log ERROR "$@"; }
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Error Handler med Trap

```bash
trap_handler() {
    local exit_code=$?
    local line_no=$1

    if [[ $exit_code -ne 0 ]]; then
        log_error "Failed at line $line_no"
        log_error "Exit code: $exit_code"
        log_error "Command: $BASH_COMMAND"
    fi

    cleanup
}

trap 'trap_handler $LINENO' EXIT
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **set -euo pipefail** | Fail fast |
| **Idempotent** | Sakert kora flera ganger |
| **Atomic** | temp-fil + mv |
| **Retry** | Exponential backoff |
| **Lock** | mkdir for race conditions |

**Kom ihag:**
- Anvand template med set -euo pipefail
- Idempotent operationer ar sakrare
- Atomic writes med temp-fil + mv
- Retry med exponential backoff
- Locking med mkdir forhindrar race conditions
""",
        },
        {
            "title": "Bash Mastery Project",
            "slug": "bash-mastery-project",
            "difficulty": "advanced",
            "content": """# Bash Mastery Project

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Vad du lar dig |
|----------|----------------|
| **Integration** | Kombinerar ALLA koncept |
| **Production** | Riktig deployment automation |
| **Best Practices** | Error handling, logging, rollback |
| **Portfolio** | Verktyg att visa upp |
| **Erfarenhet** | Som att jobba i verklig produktion |

Bygg ett komplett DevOps-verktyg.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Projektoversikt

```
┌─────────────────────────────────────────────────────────────┐
│           DEPLOYMENT AUTOMATION TOOL                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. Laser konfiguration                                    │
│   2. Validerar environment                                  │
│   3. Kor health checks                                      │
│   4. Utfor deploy med rollback                              │
│   5. Notifierar via webhook                                 │
│                                                             │
│   Struktur:                                                 │
│   deploy-tool/                                              │
│   ├── bin/deploy          # Huvudscript                     │
│   ├── lib/                # Libraries                       │
│   │   ├── config.sh                                         │
│   │   ├── logging.sh                                        │
│   │   ├── health.sh                                         │
│   │   └── deploy.sh                                         │
│   ├── config/             # Konfiguration                   │
│   │   ├── default.env                                       │
│   │   ├── production.env                                    │
│   │   └── staging.env                                       │
│   └── tests/              # Tester                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Del 1: Logging Library

```bash
#!/bin/bash
# lib/logging.sh

declare -A LOG_LEVELS=([DEBUG]=0 [INFO]=1 [WARN]=2 [ERROR]=3)
LOG_LEVEL="${LOG_LEVEL:-INFO}"
LOG_FILE="${LOG_FILE:-/var/log/deploy.log}"

_log() {
    local level="$1"
    shift
    local timestamp
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
    local caller="${FUNCNAME[2]:-main}"

    if [[ ${LOG_LEVELS[$level]:-1} -ge ${LOG_LEVELS[$LOG_LEVEL]:-1} ]]; then
        local msg="[$timestamp] [$level] [$caller] $*"
        echo "$msg" >&2
        echo "$msg" >> "$LOG_FILE" 2>/dev/null || true
    fi
}

log_debug() { _log DEBUG "$@"; }
log_info()  { _log INFO "$@"; }
log_warn()  { _log WARN "$@"; }
log_error() { _log ERROR "$@"; }

die() {
    log_error "$@"
    exit 1
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Del 2: Config Library

```bash
#!/bin/bash
# lib/config.sh

declare -A CONFIG

load_config() {
    local env="${DEPLOY_ENV:-staging}"
    local config_dir="${SCRIPT_DIR}/../config"

    # Ladda i ordning
    _source_env "$config_dir/default.env"
    _source_env "$config_dir/${env}.env"
    _source_env "$config_dir/local.env"

    # Validera required
    _require_config APP_NAME
    _require_config DEPLOY_HOST
    _require_config HEALTH_URL
}

_source_env() {
    local file="$1"
    if [[ -f "$file" ]]; then
        log_debug "Loading: $file"
        while IFS='=' read -r key value; do
            [[ -z "$key" || "$key" =~ ^# ]] && continue
            CONFIG[$key]="$value"
            export "$key=$value"
        done < "$file"
    fi
}

_require_config() {
    local key="$1"
    [[ -z "${CONFIG[$key]:-}" ]] && die "Missing: $key"
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Del 3: Health Check Library

```bash
#!/bin/bash
# lib/health.sh

health_check_all() {
    local failures=0

    log_info "Running health checks..."

    health_check_disk    || ((failures++))
    health_check_memory  || ((failures++))
    health_check_app     || ((failures++))

    if (( failures > 0 )); then
        log_error "Health checks failed: $failures"
        return 1
    fi

    log_info "All health checks passed"
}

health_check_disk() {
    local threshold="${DISK_THRESHOLD:-90}"
    local usage
    usage=$(df -h "${DEPLOY_PATH}" | awk 'NR==2 {print $5}' | tr -d '%')

    (( usage > threshold )) && {
        log_error "Disk: ${usage}% > ${threshold}%"
        return 1
    }

    log_debug "Disk OK: ${usage}%"
}

health_check_app() {
    local url="${HEALTH_URL}"
    local timeout="${HEALTH_TIMEOUT:-10}"

    if curl -sf --max-time "$timeout" "$url" > /dev/null; then
        log_debug "App health OK"
        return 0
    fi

    log_error "App health failed: $url"
    return 1
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Del 4: Deploy Library

```bash
#!/bin/bash
# lib/deploy.sh

deploy() {
    local version="$1"
    local backup_path

    log_info "Deploying: $version"

    # Pre-flight
    pre_deploy_checks || return 1

    # Backup
    backup_path=$(create_backup) || return 1
    log_info "Backup: $backup_path"

    # Deploy
    if ! do_deploy "$version"; then
        log_error "Deploy failed, rolling back..."
        rollback "$backup_path"
        return 1
    fi

    # Validate
    if ! post_deploy_check; then
        log_error "Validation failed, rolling back..."
        rollback "$backup_path"
        return 1
    fi

    log_info "Deploy completed"
    cleanup_old_backups
}

create_backup() {
    local timestamp
    timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_path="${BACKUP_DIR}/${APP_NAME}_${timestamp}"

    ssh "$DEPLOY_HOST" "cp -r '$DEPLOY_PATH' '$backup_path'"
    echo "$backup_path"
}

rollback() {
    local backup_path="$1"
    log_warn "Rolling back to: $backup_path"

    ssh "$DEPLOY_HOST" "
        rm -rf '$DEPLOY_PATH' &&
        mv '$backup_path' '$DEPLOY_PATH'
    "
}

post_deploy_check() {
    local retries="${HEALTH_RETRIES:-5}"
    local wait="${HEALTH_WAIT:-5}"

    log_info "Waiting for app..."

    for ((i=1; i<=retries; i++)); do
        sleep "$wait"
        health_check_app && return 0
        log_debug "Attempt $i/$retries failed"
    done

    return 1
}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Del 5: Huvudscript

```bash
#!/bin/bash
# bin/deploy

set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Ladda libraries
source "$SCRIPT_DIR/../lib/logging.sh"
source "$SCRIPT_DIR/../lib/config.sh"
source "$SCRIPT_DIR/../lib/health.sh"
source "$SCRIPT_DIR/../lib/deploy.sh"

usage() {
    cat << EOF
Usage: deploy [OPTIONS] <command> [args]

Commands:
    deploy <version>    Deploy a version
    rollback <backup>   Rollback to backup
    health              Run health checks
    status              Show status

Options:
    -e, --env ENV       Environment (staging, production)
    -n, --dry-run       Show what would be done
    -v, --verbose       Verbose output
    -h, --help          Show this help
EOF
}

main() {
    local env="staging"
    local dry_run=false

    while [[ $# -gt 0 ]]; do
        case $1 in
            -e|--env)     env="$2"; shift 2 ;;
            -n|--dry-run) dry_run=true; shift ;;
            -v|--verbose) LOG_LEVEL=DEBUG; shift ;;
            -h|--help)    usage; exit 0 ;;
            -*)           die "Unknown: $1" ;;
            *)            break ;;
        esac
    done

    export DEPLOY_ENV="$env"
    load_config

    local command="${1:-}"
    shift || true

    case $command in
        deploy)
            local version="${1:?Version required}"
            [[ "$dry_run" == true ]] && {
                log_info "DRY RUN: Would deploy $version"
                exit 0
            }
            deploy "$version"
            ;;
        rollback)
            rollback "${1:?Backup required}"
            ;;
        health)
            health_check_all
            ;;
        status)
            echo "Env: $DEPLOY_ENV"
            echo "App: $APP_NAME"
            health_check_all && echo "Status: healthy"
            ;;
        *)
            usage
            exit 1
            ;;
    esac
}

main "$@"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Anvandning

```bash
# Kora health checks
./bin/deploy health

# Deploy till staging
./bin/deploy -e staging deploy v1.2.3

# Deploy till production med verbose
./bin/deploy -v -e production deploy v1.2.3

# Dry run
./bin/deploy -n -e production deploy v1.2.3

# Rollback
./bin/deploy rollback /backup/myapp_20240115_030000

# Status
./bin/deploy status
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Libraries** | Separera logik for ateranvandning |
| **Atomic deploy** | Backup + rollback |
| **Health checks** | Fore och efter deploy |
| **Logging** | Strukturerad for debugging |
| **Config** | Hierarkisk med overrides |

**Kom ihag:**
- Separera logik i libraries for ateranvandning
- Atomic deploy med backup och rollback
- Health checks fore och efter deploy
- Strukturerad logging for debugging och audit
- Hierarkisk konfiguration med environment overrides

**Grattis - du har slutfort Bash Mastery!**
""",
        },
    ],
}
