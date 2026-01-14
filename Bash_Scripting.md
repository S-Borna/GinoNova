# Bash Scripting Fundamentals

Fokus: Skriptning och automation

## Boilerplate: Börja varje skript med dessa rader

Varje seriöst bash-skript bör börja med en solid boilerplate:

```bash
#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
```

### Shebang (#!)

**Shebang** (hashbang) talar om för systemet vilken interpreter som ska köra skriptet.

```bash
#!/bin/bash              # Använd bash
#!/usr/bin/env bash      # Portabel - hittar bash i PATH
#!/bin/sh                # POSIX sh (mer portabelt men färre funktioner)
#!/usr/bin/env python3   # Python-skript
```

**Placering**: Måste vara FÖRSTA raden i skriptet.

### Set-flaggorna

`set -euo pipefail` är en säker standardinställning:

```bash
set -e    # Exit direkt vid fel (non-zero exit code)
set -u    # Exit vid användning av odefinierade variabler
set -o pipefail  # Pipeline misslyckas om NÅGOT kommando misslyckas
```

**Individuellt**:

```bash
# -e: Exit vid fel
set -e
ls /does/not/exist   # Skriptet avbryter här
echo "This never runs"

# -u: Exit vid undefined variable
set -u
echo "$UNDEFINED_VAR"  # Exit med fel
# Alternativ: ge default-värde
echo "${UNDEFINED_VAR:-default}"

# -o pipefail: Pipeline returnerar exit code från första fel
false | true  # Utan pipefail: exit 0
# Med pipefail: exit 1
```

### IFS (Internal Field Separator)

IFS bestämmer hur bash delar upp strängar.

```bash
# Default IFS = space, tab, newline
IFS=$'\n\t'  # Bara newline och tab - säkrare för filer med spaces
```

**Varför**: Förhindrar oavsiktlig splittring av filnamn med mellanslag.

### Komplett boilerplate med förklaringar

```bash
#!/usr/bin/env bash
#
# Beskrivning: [Vad skriptet gör]
# Usage: ./script.sh [args]
#

set -euo pipefail  # Strikt felhantering
IFS=$'\n\t'        # Säker orddelning

# Dina kommandon här...
```

## Variabler och Export

### Variabeldeklaration

Variabler i bash har INGET mellanslag runt =:

```bash
# Rätt
name="John"
age=25
path="/home/user"

# FEL - ger syntax error
name = "John"
```

### Läsa variabler

```bash
echo $name
echo ${name}       # Samma sak, men tydligare
echo "${name}"     # Best practice - skyddar mot word splitting
```

### Variable expansion

```bash
# Default-värden
echo "${VAR:-default}"      # Använd "default" om VAR är unset/empty
echo "${VAR:=default}"      # Samma, men sätter också VAR till "default"
echo "${VAR:?error msg}"    # Exit med fel om VAR är unset/empty

# Längd
name="hello"
echo "${#name}"             # 5

# Substrings
text="hello world"
echo "${text:0:5}"          # hello
echo "${text:6}"            # world

# Pattern substitution
filename="document.txt"
echo "${filename%.txt}"     # document (ta bort .txt från slutet)
echo "${filename##*.}"      # txt (extrahera extension)
```

### Export

`export` gör variabeln tillgänglig för child processes:

```bash
# Bara i nuvarande shell
name="John"

# Tillgänglig i subprocesser
export PATH="/custom/bin:$PATH"

# Deklarera och exportera på en rad
export API_KEY="secret123"

# Lista alla exporterade variabler
export -p

# Ta bort export
export -n name
```

**Viktigt**: Utan export ser inte subprocess variabeln:

```bash
my_var="hello"
bash -c 'echo $my_var'  # Tom - my_var är inte exporterad

export my_var="hello"
bash -c 'echo $my_var'  # hello
```

## Arguments: Använd $0, $1-$9, $#, $@ i skript

Bash ger dig tillgång till skript-argument via speciella variabler:

```bash
#!/bin/bash
# Spara som: test.sh

echo "Script name: $0"      # ./test.sh
echo "First argument: $1"    # Första argumentet
echo "Second argument: $2"   # Andra argumentet
echo "Number of args: $#"    # Antal argument
echo "All args: $@"          # Alla argument som separata ord
echo "All args: $*"          # Alla argument som en sträng
```

**Användning**:

```bash
./test.sh arg1 arg2 arg3
# Script name: ./test.sh
# First argument: arg1
# Second argument: arg2
# Number of args: 3
# All args: arg1 arg2 arg3
```

### Argumentvalidering

```bash
#!/bin/bash
set -euo pipefail

# Kontrollera antal argument
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <name> <age>"
    exit 1
fi

name="$1"
age="$2"

echo "Hello $name, you are $age years old"
```

### Skillnad mellan $@ och $*

```bash
# $@ - varje argument som separat ord (med quotes)
for arg in "$@"; do
    echo "Arg: $arg"
done

# $* - alla argument som en sträng
# Om IFS är ändrad påverkar det $*
```

**Best practice**: Använd `"$@"` för att bevara argument med mellanslag.

## Shift: Flytta fram argumenten

`shift` tar bort första argumentet och flyttar alla andra ett steg:

```bash
#!/bin/bash

echo "Before shift:"
echo "1: $1, 2: $2, 3: $3"

shift

echo "After shift:"
echo "1: $1, 2: $2"
# Vad som var $2 är nu $1
```

**Användning**: Loop genom alla argument:

```bash
#!/bin/bash

while [[ $# -gt 0 ]]; do
    echo "Processing: $1"
    shift
done
```

**Med shift N**:

```bash
shift 2   # Ta bort de första 2 argumenten
```

### Flag-parsing med shift

```bash
#!/bin/bash

verbose=false
output=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            verbose=true
            shift
            ;;
        -o|--output)
            output="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done
```

## Read: Läs input från användare

`read` läser input från användaren eller från stdin.

### Grundläggande read

```bash
#!/bin/bash

# Vänta på input
echo "What is your name?"
read name
echo "Hello, $name!"

# Med prompt på samma rad
read -p "Enter your name: " name
echo "Hello, $name!"
```

### Read-flaggor

```bash
# -p: Visa prompt
read -p "Enter name: " name

# -s: Silent (visa inte input, för lösenord)
read -s -p "Enter password: " password
echo ""  # Ny rad efter lösenord

# -t: Timeout (sekunder)
read -t 5 -p "Quick! Enter: " answer || echo "Too slow!"

# -n: Läs N tecken
read -n 1 -p "Press any key to continue..."

# -r: Raw mode (behandla inte backslash speciellt)
read -r line  # Best practice för att läsa filer

# -a: Läs till array
read -a words <<< "one two three"
echo "${words[1]}"  # two
```

### Läsa från fil

```bash
# Läs fil rad för rad
while IFS= read -r line; do
    echo "Line: $line"
done < file.txt

# Med process substitution
while IFS= read -r line; do
    echo "$line"
done < <(ls -la)
```

### Läsa flera variabler

```bash
# Dela upp input
echo "apple banana cherry" | read -r a b c
# Fungerar ej som förväntat i subshell!

# Använd here-string istället
read -r a b c <<< "apple banana cherry"
echo "$a"  # apple
echo "$b"  # banana
```

## Flow Control: if/elif/else, [[ ]], for/while loopar

### If-satser

```bash
#!/bin/bash

# Grundläggande if
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
if [[ condition1 ]]; then
    echo "First"
elif [[ condition2 ]]; then
    echo "Second"
else
    echo "Neither"
fi
```

### [[ ]] vs [ ]

**Föredra [[ ]]** - det är bash-specifikt men säkrare:

```bash
# [[ ]] fördelar:
# - Ingen word splitting
# - Ingen pathname expansion
# - Stödjer regex med =~
# - && och || fungerar direkt

# [ ] är POSIX-kompatibelt men kräver quoting
if [ "$var" = "value" ]; then ...  # Quotes krävs
if [[ $var = "value" ]]; then ...  # Fungerar utan quotes
```

### Jämförelser

```bash
# String comparison
[[ $str = "value" ]]    # Lika
[[ $str != "value" ]]   # Inte lika
[[ -z "$str" ]]         # Tom sträng
[[ -n "$str" ]]         # Inte tom
[[ $str =~ ^regex$ ]]   # Regex match

# Numeric comparison
[[ $num -eq 5 ]]   # Equal
[[ $num -ne 5 ]]   # Not equal
[[ $num -lt 10 ]]  # Less than
[[ $num -le 10 ]]  # Less or equal
[[ $num -gt 0 ]]   # Greater than
[[ $num -ge 0 ]]   # Greater or equal

# Använd (( )) för numeriska jämförelser (läsligare)
(( num == 5 ))
(( num > 0 && num < 10 ))

# File tests
[[ -f "$file" ]]   # Fil existerar
[[ -d "$dir" ]]    # Katalog existerar
[[ -e "$path" ]]   # Existerar (fil eller katalog)
[[ -r "$file" ]]   # Läsbar
[[ -w "$file" ]]   # Skrivbar
[[ -x "$file" ]]   # Körbar
[[ -s "$file" ]]   # Fil existerar och inte tom
```

### Logical operators

```bash
# AND
[[ condition1 && condition2 ]]

# OR
[[ condition1 || condition2 ]]

# NOT
[[ ! condition ]]

# Kombinera
if [[ -f "$file" && -r "$file" ]]; then
    cat "$file"
fi
```

### For loops

```bash
# Loop över lista
for item in apple banana cherry; do
    echo "$item"
done

# Loop över array
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# C-style for loop
for ((i=0; i<10; i++)); do
    echo "$i"
done

# Loop över filer
for file in *.txt; do
    echo "Processing $file"
done

# Loop med kommando-output
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done
```

### While loops

```bash
# Basic while
counter=0
while [[ $counter -lt 5 ]]; do
    echo "$counter"
    ((counter++))
done

# Infinite loop
while true; do
    # break för att avsluta
    break
done

# Läs fil rad för rad
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

### Until loop (motsats till while)

```bash
until [[ $counter -ge 5 ]]; do
    echo "$counter"
    ((counter++))
done
```

### Break och Continue

```bash
for i in {1..10}; do
    if [[ $i -eq 5 ]]; then
        continue  # Hoppa över resten, fortsätt loopen
    fi
    if [[ $i -eq 8 ]]; then
        break     # Avsluta loopen helt
    fi
    echo "$i"
done
# Output: 1 2 3 4 6 7
```

## mktemp: Skapa säkra tempfiler

`mktemp` skapar unika, säkra temporära filer eller mappar.

```bash
# Skapa temp-fil
temp_file=$(mktemp)
echo "Created: $temp_file"
# /tmp/tmp.abc123xyz

# Skapa temp-mapp
temp_dir=$(mktemp -d)
echo "Created dir: $temp_dir"

# Med specifikt prefix
temp_file=$(mktemp /tmp/myapp.XXXXXX)
# X:en ersätts med slumpmässiga tecken

# Med template
temp_file=$(mktemp --suffix=.txt)
```

### Städa upp med trap

```bash
#!/bin/bash

# Skapa temp-fil
TEMP_FILE=$(mktemp)

# Registrera cleanup som körs vid exit
trap "rm -f $TEMP_FILE" EXIT

# Använd temp-filen
echo "data" > "$TEMP_FILE"
cat "$TEMP_FILE"

# Temp-filen rensas automatiskt vid exit
```

## Trap: Hantera signaler och cleanup

`trap` registrerar kommandon som körs vid specifika signaler.

```bash
# Syntax: trap 'commands' SIGNALS

# Cleanup vid exit (normal exit, Ctrl+C, fel)
trap 'echo "Cleaning up..."; rm -f $temp_file' EXIT

# Ignorera Ctrl+C
trap '' SIGINT

# Hantera specifika signaler
trap 'echo "Caught SIGINT"' SIGINT
trap 'echo "Caught SIGTERM"' SIGTERM
```

### Vanliga signaler

```bash
EXIT     # När skriptet avslutas (oavsett hur)
SIGINT   # Ctrl+C (interrupt)
SIGTERM  # Standard termination signal
SIGKILL  # Cannot be trapped - omedelbar avslutning
SIGHUP   # Terminal stängs
ERR      # När kommando misslyckas (med set -e)
```

### Praktiskt cleanup-pattern

```bash
#!/bin/bash
set -euo pipefail

# Skapa temporära resurser
TEMP_DIR=$(mktemp -d)
PID_FILE="/var/run/myapp.pid"

cleanup() {
    echo "Cleaning up..."
    rm -rf "$TEMP_DIR"
    rm -f "$PID_FILE"
}

trap cleanup EXIT

# Huvudskript
echo "Working in $TEMP_DIR"
# ... resten av skriptet

# cleanup() körs automatiskt när skriptet avslutas
```

### Trap med funktioner

```bash
#!/bin/bash

on_error() {
    echo "Error occurred on line $1"
    exit 1
}

trap 'on_error $LINENO' ERR

# Om något misslyckas, körs on_error med radnummer
```

## Exit codes: Returnera status från skript

Exit codes indikerar om ett kommando lyckades (0) eller misslyckades (non-zero).

```bash
# Kontrollera senaste exit code
echo $?

# I skript
exit 0    # Framgång
exit 1    # Generellt fel
exit 2    # Felaktigt användning

# Vanliga konventioner
# 0: Success
# 1: General error
# 2: Misuse of command
# 126: Command found but not executable
# 127: Command not found
# 128+N: Terminated by signal N (128+9=137 för SIGKILL)
```

### Använda exit codes i villkor

```bash
# Kommandos exit code avgör if-villkor
if command; then
    echo "Command succeeded"
else
    echo "Command failed"
fi

# Kombinera kommandon
command1 && command2    # command2 körs bara om command1 lyckas
command1 || command2    # command2 körs bara om command1 misslyckas

# Praktiskt exempel
grep -q "pattern" file && echo "Found" || echo "Not found"
```

### Manuell exit code

```bash
#!/bin/bash

validate_input() {
    if [[ -z "$1" ]]; then
        echo "Error: No input provided"
        return 1
    fi
    return 0
}

if ! validate_input "$1"; then
    exit 1
fi

echo "Input is valid: $1"
```

## Praktiskt: Komplett skript-exempel

```bash
#!/usr/bin/env bash
#
# backup.sh - Simple backup script
# Usage: ./backup.sh <source_dir> <backup_dir>
#

set -euo pipefail
IFS=$'\n\t'

# === Configuration ===
readonly SCRIPT_NAME="$(basename "$0")"
readonly LOG_FILE="/tmp/${SCRIPT_NAME}.log"

# === Functions ===
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

usage() {
    echo "Usage: $SCRIPT_NAME <source_dir> <backup_dir>"
    echo "  source_dir: Directory to backup"
    echo "  backup_dir: Where to store backup"
    exit 1
}

cleanup() {
    log "Cleaning up..."
    # Add cleanup commands here
}

# === Main ===
trap cleanup EXIT

# Validate arguments
if [[ $# -ne 2 ]]; then
    usage
fi

SOURCE_DIR="$1"
BACKUP_DIR="$2"

# Validate source directory
if [[ ! -d "$SOURCE_DIR" ]]; then
    log "Error: Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

# Create backup directory if needed
mkdir -p "$BACKUP_DIR"

# Perform backup
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"

log "Starting backup: $SOURCE_DIR -> $BACKUP_FILE"

tar -czf "$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"

log "Backup completed successfully!"
log "Backup size: $(du -h "$BACKUP_FILE" | cut -f1)"

exit 0
```

## Viktiga takeaways

- **Boilerplate**: `#!/bin/bash` + `set -euo pipefail` + `IFS=$'\n\t'`
- **set -e**: Avbryt vid fel
- **set -u**: Avbryt vid undefined variable
- **set -o pipefail**: Pipeline misslyckas om något kommando misslyckas
- **Arguments**: $0 (script), $1-$9 (args), $# (antal), $@ (alla)
- **shift**: Flytta fram argumenten (för flag-parsing)
- **read -p**: Läs input med prompt
- **[[ ]]**: Föredra över [ ] för villkor
- **Numerisk jämförelse**: -eq, -ne, -lt, -le, -gt, -ge (eller använd (( )))
- **mktemp**: Skapa säkra temp-filer
- **trap 'cleanup' EXIT**: Garanterad cleanup
- **Exit codes**: 0 = success, non-zero = failure
- **Använd quotes**: `"$variable"` för att hantera spaces
