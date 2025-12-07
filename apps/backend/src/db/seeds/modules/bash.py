"""
Bash Mastery - Linux-mallen
============================

20 tasks som följer Linux-mallen:
- Varför behöver du kunna detta?
- Så fungerar det
- Bash-kommentarer på VARJE rad
- Key Takeaways
- Inga emojis i headers
- Inga tabeller
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
            "content": """
# Bash Fundamentals & Shell Basics

## Varför behöver du kunna detta?

Bash är standardskalet på Linux och macOS. Varje DevOps-ingenjör använder det dagligen för:

- Systemadministration
- Automation av repetitiva uppgifter
- CI/CD-pipelines
- Container-entrypoints
- Deployment-scripts

Utan Bash-kunskaper är du begränsad till GUI-verktyg och manuellt arbete.

---

## Så fungerar det

Bash (Bourne Again SHell) är både ett kommandoradsgränssnitt och ett scriptspråk. Det tolkar kommandon rad för rad och kan köra dem interaktivt eller från script-filer.

**Shell vs Terminal:**
- **Terminal** - Fönstret som visar text (emulator)
- **Shell** - Programmet som tolkar kommandon (bash, zsh, fish)

---

## Grundläggande kommandon

```bash
# Visa aktuellt skal
echo $SHELL                          # Visar t.ex. /bin/bash

# Visa bash-version
bash --version                       # GNU bash, version X.Y.Z

# Kör kommando
ls -la                               # Listar filer och kataloger

# Kör flera kommandon på en rad
command1 ; command2                  # Kör båda oavsett resultat
command1 && command2                 # Kör command2 endast om command1 lyckas
command1 || command2                 # Kör command2 endast om command1 misslyckas

# Exempel:
mkdir test && cd test                # Skapa katalog och gå in i den
rm file.txt || echo "Filen finns ej" # Skriv meddelande om rm misslyckas
```

---

## Navigering och filhantering

```bash
# Var är jag?
pwd                                  # Print Working Directory

# Ändra katalog
cd /path/to/directory                # Absolut sökväg
cd directory                         # Relativ sökväg
cd ..                                # En nivå upp
cd ~                                 # Hemkatalog
cd -                                 # Föregående katalog

# Lista filer
ls                                   # Enkel lista
ls -l                                # Lång format (detaljer)
ls -la                               # Inkludera dolda filer
ls -lh                               # Human-readable storlekar
ls -lt                               # Sortera efter tid

# Skapa och ta bort
mkdir directory                      # Skapa katalog
mkdir -p path/to/nested/dir          # Skapa hela sökvägen
rmdir directory                      # Ta bort tom katalog
rm file.txt                          # Ta bort fil
rm -r directory                      # Ta bort katalog rekursivt
rm -rf directory                     # Force, ingen bekräftelse (FARLIGT!)
```

---

## Fil- och texthantering

```bash
# Visa filinnehåll
cat file.txt                         # Hela filen
head file.txt                        # Första 10 rader
head -n 20 file.txt                  # Första 20 rader
tail file.txt                        # Sista 10 rader
tail -f file.txt                     # Följ filen (live-uppdatering)

# Skapa filer
touch file.txt                       # Skapa tom fil (eller uppdatera timestamp)
echo "text" > file.txt               # Skriv till fil (överskriver)
echo "more" >> file.txt              # Lägg till i fil (append)

# Kopiera och flytta
cp source.txt dest.txt               # Kopiera fil
cp -r source_dir dest_dir            # Kopiera katalog rekursivt
mv old.txt new.txt                   # Flytta/byt namn
mv file.txt /new/location/           # Flytta till annan plats

# Hitta filer
find /path -name "*.txt"             # Hitta filer med namn
find . -type f -mtime -7             # Filer ändrade senaste 7 dagar
locate filename                      # Snabb sökning (kräver updatedb)
```

---

## Input/Output och redirects

```bash
# Standard streams:
# stdin (0)  - Input
# stdout (1) - Output
# stderr (2) - Fel

# Redirect stdout till fil
ls > files.txt                       # Överskriver
ls >> files.txt                      # Lägger till

# Redirect stderr till fil
command 2> errors.txt                # Endast fel
command 2>> errors.txt               # Lägg till fel

# Redirect båda
command > output.txt 2>&1            # Båda till samma fil
command &> output.txt                # Kortare syntax (bash 4+)

# Ignorera output
command > /dev/null                  # Kasta stdout
command 2> /dev/null                 # Kasta stderr
command &> /dev/null                 # Kasta allt

# Pipe - skicka output till nästa kommando
ls -l | grep ".txt"                  # Filtrera output
cat file.txt | wc -l                 # Räkna rader
ps aux | grep nginx | head -5        # Kedja flera pipes
```

---

## Hjälp och dokumentation

```bash
# Manual-sidor
man ls                               # Fullständig manual för ls
man bash                             # Bash-manualen

# Kort hjälp
command --help                       # De flesta kommandon stödjer detta
help cd                              # Built-in bash-kommandon

# Visa vad ett kommando är
type ls                              # "ls is aliased to..." eller "ls is /bin/ls"
which python                         # Sökväg till körbar fil
whereis bash                         # Alla platser (binary, source, manual)
```

---

## Key Takeaways

1. Bash är standardskalet för Linux/macOS automation
2. `&&` kör nästa kommando endast vid success, `||` vid failure
3. Pipes (`|`) kopplar ihop kommandon för dataflöden
4. Redirects (`>`, `>>`, `2>`) styr output till filer
5. `man` och `--help` för dokumentation
""",
        },
        {
            "title": "Variables & Data Types",
            "slug": "variables-data-types",
            "difficulty": "beginner",
            "content": """
# Variables & Data Types

## Varför behöver du kunna detta?

Variabler är grunden för alla script. De låter dig:

- Lagra värden för återanvändning
- Parametrisera scripts
- Bygga dynamiska kommandon
- Hantera konfiguration

Utan variabler blir scripts hårdkodade och oanvändbara.

---

## Så fungerar det

Bash-variabler är otypade - allt är strängar internt. Aritmetik och arrays hanteras speciellt.

**Namnkonventioner:**
- Börja med bokstav eller underscore
- Endast alfanumeriska tecken och underscore
- Case-sensitive (`VAR` ≠ `var`)
- VERSALER för konstanter/miljövariabler

---

## Skapa och använda variabler

```bash
# Tilldela värde (INGET mellanslag runt =)
name="Alice"                         # Korrekt
name = "Alice"                       # FEL! Tolkas som kommando

# Läsa variabel
echo $name                           # Enkel form
echo "${name}"                       # Med braces (rekommenderas)
echo "Hello, ${name}!"               # Inuti sträng

# Varför braces?
filename="report"
echo "$filename_2024"                # Försöker läsa filename_2024 (finns ej)
echo "${filename}_2024"              # Korrekt: report_2024

# Ta bort variabel
unset name                           # Tar bort variabeln
```

---

## Stränghantering

```bash
# Strängoperationer
str="Hello World"

# Längd
echo ${#str}                         # 11

# Substring
echo ${str:0:5}                      # "Hello" (start:längd)
echo ${str:6}                        # "World" (från position 6)

# Ersättning
echo ${str/World/Bash}               # "Hello Bash" (första)
echo ${str//o/0}                     # "Hell0 W0rld" (alla)

# Ta bort prefix/suffix
filename="backup.tar.gz"
echo ${filename%.gz}                 # "backup.tar" (ta bort kortaste suffix)
echo ${filename%%.*}                 # "backup" (ta bort längsta suffix)
echo ${filename#*.}                  # "tar.gz" (ta bort kortaste prefix)
echo ${filename##*.}                 # "gz" (ta bort längsta prefix)

# Default-värden
echo ${var:-"default"}               # Använd default om var är tom/odefinierad
echo ${var:="default"}               # Sätt OCH returnera default
echo ${var:+"set"}                   # Returnera "set" om var är definierad
echo ${var:?"error msg"}             # Avsluta med fel om var är tom
```

---

## Arrays

```bash
# Skapa array
fruits=("apple" "banana" "cherry")   # Med värden
declare -a numbers                   # Tom array

# Tilldela värden
fruits[0]="apple"                    # Index 0
fruits[3]="date"                     # Index 3 (2 hoppas över)

# Läsa värden
echo ${fruits[0]}                    # "apple"
echo ${fruits[@]}                    # Alla element
echo ${fruits[*]}                    # Alla som en sträng
echo ${#fruits[@]}                   # Antal element
echo ${!fruits[@]}                   # Alla index

# Iterera
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"             # Skriv ut varje frukt
done

# Slice
echo ${fruits[@]:1:2}                # Element 1-2 (banana cherry)

# Lägg till element
fruits+=("elderberry")               # Lägg till i slutet
```

---

## Associativa arrays (dictionaries)

```bash
# Kräver bash 4+
declare -A user                      # Deklarera associativ array

# Tilldela
user[name]="Alice"
user[age]="30"
user[email]="alice@example.com"

# Läsa
echo ${user[name]}                   # "Alice"
echo ${user[@]}                      # Alla värden
echo ${!user[@]}                     # Alla nycklar

# Iterera
for key in "${!user[@]}"; do
    echo "$key: ${user[$key]}"       # Skriv ut nyckel och värde
done

# Kontrollera om nyckel finns
if [[ -v user[name] ]]; then
    echo "Name is set"               # Nyckeln finns
fi
```

---

## Miljövariabler

```bash
# Visa miljövariabler
env                                  # Alla miljövariabler
echo $HOME                           # Hemkatalog
echo $USER                           # Användarnamn
echo $PATH                           # Sökväg för körbara filer
echo $PWD                            # Nuvarande katalog
echo $SHELL                          # Aktivt skal

# Sätta miljövariabel (för child-processer)
export MY_VAR="value"                # Exportera till miljön
MY_VAR="value" command               # Tillfälligt för ett kommando

# Ta bort från miljön
unset MY_VAR                         # Ta bort
export -n MY_VAR                     # Ta bort export (behåll som lokal)

# Ladda från fil
source .env                          # Eller: . .env
# .env innehåller: export VAR="value"
```

---

## Speciella variabler

```bash
# Script-relaterade
echo $0                              # Script-namn
echo $1                              # Första argumentet
echo $2                              # Andra argumentet
echo $#                              # Antal argument
echo $@                              # Alla argument (separata)
echo $*                              # Alla argument (en sträng)
echo $$                              # Process ID (PID) för scriptet
echo $!                              # PID för senaste bakgrundsjobb
echo $?                              # Exit-status för senaste kommando

# Exempel:
# ./script.sh arg1 arg2 arg3
# $0 = ./script.sh
# $1 = arg1
# $2 = arg2
# $# = 3
```

---

## Key Takeaways

1. Ingen space runt `=` vid tilldelning
2. Använd `${var}` för tydlighet och strängmanipulation
3. `[@]` för array-element, `[*]` för en sträng
4. `export` gör variabeln tillgänglig för child-processer
5. `$?` innehåller exit-status för senaste kommando
""",
        },
        {
            "title": "Conditionals & Control Flow",
            "slug": "conditionals-control-flow",
            "difficulty": "beginner",
            "content": """
# Conditionals & Control Flow

## Varför behöver du kunna detta?

Scripts utan logik är bara listor av kommandon. Conditionals låter dig:

- Fatta beslut baserat på villkor
- Hantera olika scenarion
- Validera input
- Bygga robusta scripts

Utan kontrollflöde kan du inte skriva riktiga program.

---

## Så fungerar det

Bash har flera sätt att testa villkor:

- `[ ]` - POSIX test (fungerar i alla skal)
- `[[ ]]` - Bash extended test (mer kraftfull)
- `(( ))` - Aritmetisk utvärdering

`[[ ]]` rekommenderas för Bash-scripts.

---

## If-satser

```bash
# Grundläggande if
if [[ condition ]]; then
    echo "True"                      # Körs om villkoret är sant
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

# Enradig (för enkla fall)
[[ $val -gt 0 ]] && echo "Positive"  # Om sant
[[ $val -lt 0 ]] || echo "Not neg"   # Om falskt
```

---

## Strängjämförelser

```bash
str="hello"

# Equality
[[ $str == "hello" ]]                # Lika med
[[ $str != "world" ]]                # Inte lika med

# Pattern matching (glob)
[[ $str == h* ]]                     # Börjar med h
[[ $str == *lo ]]                    # Slutar med lo
[[ $str == h?llo ]]                  # ? matchar ett tecken

# Regex matching
[[ $str =~ ^[a-z]+$ ]]               # Matchar regex

# Tom/icke-tom
[[ -z $str ]]                        # True om tom (zero length)
[[ -n $str ]]                        # True om icke-tom (non-zero)

# Case-insensitive (bash 4+)
shopt -s nocasematch                 # Aktivera
[[ "HELLO" == "hello" ]]             # True
shopt -u nocasematch                 # Deaktivera
```

---

## Numeriska jämförelser

```bash
num=42

# Jämförelseoperatorer (i [[ ]] eller [ ])
[[ $num -eq 42 ]]                    # Equal
[[ $num -ne 0 ]]                     # Not equal
[[ $num -lt 50 ]]                    # Less than
[[ $num -le 42 ]]                    # Less than or equal
[[ $num -gt 40 ]]                    # Greater than
[[ $num -ge 42 ]]                    # Greater than or equal

# Aritmetisk kontext (enklare syntax)
(( num == 42 ))                      # Equal
(( num != 0 ))                       # Not equal
(( num < 50 ))                       # Less than
(( num <= 42 ))                      # Less than or equal
(( num > 40 ))                       # Greater than
(( num >= 42 ))                      # Greater than or equal

# Kombinera
(( num > 0 && num < 100 ))           # AND
(( num < 0 || num > 100 ))           # OR
```

---

## Filtester

```bash
# Existens
[[ -e /path/to/file ]]               # Existerar (fil eller katalog)
[[ -f /path/to/file ]]               # Är en fil
[[ -d /path/to/dir ]]                # Är en katalog
[[ -L /path/to/link ]]               # Är en symbolisk länk

# Behörigheter
[[ -r /path/to/file ]]               # Readable
[[ -w /path/to/file ]]               # Writable
[[ -x /path/to/file ]]               # Executable

# Storlek
[[ -s /path/to/file ]]               # Storlek > 0 (ej tom)

# Jämförelser mellan filer
[[ file1 -nt file2 ]]                # Newer than (nyare)
[[ file1 -ot file2 ]]                # Older than (äldre)
[[ file1 -ef file2 ]]                # Equal (samma inode)

# Praktiskt exempel
if [[ -f "config.txt" ]]; then
    source config.txt                # Ladda config om den finns
else
    echo "Config saknas!"            # Varning
    exit 1                           # Avsluta med fel
fi
```

---

## Logiska operatorer

```bash
# AND - båda måste vara sanna
[[ -f file.txt && -r file.txt ]]     # Fil finns OCH är läsbar

# OR - minst en måste vara sann
[[ -f file.txt || -f file.bak ]]     # Fil ELLER backup finns

# NOT - negering
[[ ! -f file.txt ]]                  # Fil finns INTE

# Gruppering
[[ ( $a -gt 0 && $a -lt 10 ) || $a -eq 100 ]]

# Alternativ syntax (POSIX)
[ -f file.txt ] && [ -r file.txt ]   # AND med separata tester
[ -f file.txt ] || [ -f file.bak ]   # OR med separata tester
```

---

## Case-satser

```bash
# Pattern matching
case $option in
    start)
        echo "Starting..."
        ;;                           # Varje case avslutas med ;;
    stop)
        echo "Stopping..."
        ;;
    restart)
        echo "Restarting..."
        ;;
    *)                               # Default case
        echo "Unknown option: $option"
        exit 1
        ;;
esac

# Multipla patterns
case $input in
    [Yy]|[Yy]es)                     # Y, y, Yes, yes
        echo "Confirmed"
        ;;
    [Nn]|[Nn]o)                      # N, n, No, no
        echo "Cancelled"
        ;;
    *)
        echo "Invalid input"
        ;;
esac

# Pattern med wildcard
case $filename in
    *.txt)
        echo "Text file"
        ;;
    *.sh)
        echo "Shell script"
        ;;
    *.tar.gz|*.tgz)
        echo "Compressed archive"
        ;;
esac
```

---

## Key Takeaways

1. Använd `[[ ]]` istället för `[ ]` i Bash-scripts
2. Strängjämförelse: `==`, `!=`, `-z`, `-n`
3. Numerisk: `-eq`, `-lt`, `-gt` eller `(( ))` för matematisk syntax
4. Filtester: `-f`, `-d`, `-e`, `-r`, `-w`, `-x`
5. `case` är renare än många if-elif för pattern matching
""",
        },
        {
            "title": "Loops & Iteration",
            "slug": "loops-iteration",
            "difficulty": "beginner",
            "content": """
# Loops & Iteration

## Varför behöver du kunna detta?

Loopar automatiserar repetitiva uppgifter. Istället för att skriva samma kommando 100 gånger:

- Processa alla filer i en katalog
- Iterera över server-listor
- Retry-logik vid fel
- Batch-operationer

Utan loopar är automation omöjlig.

---

## Så fungerar det

Bash har tre loop-typer:

- `for` - Iterera över lista
- `while` - Kör medan villkor är sant
- `until` - Kör tills villkor blir sant

---

## For-loopar

```bash
# Iterera över lista
for fruit in apple banana cherry; do
    echo "Fruit: $fruit"             # Skriv ut varje frukt
done

# Iterera över array
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Iterera över filer
for file in *.txt; do
    echo "Processing: $file"         # Varje .txt-fil
done

# Iterera över kommando-output
for user in $(cat users.txt); do
    echo "User: $user"               # Varje rad i filen
done

# C-style for loop
for ((i=0; i<10; i++)); do
    echo "Count: $i"                 # 0-9
done

# Med steg
for ((i=0; i<=100; i+=10)); do
    echo "Value: $i"                 # 0, 10, 20, ..., 100
done
```

---

## Range och sekvenser

```bash
# Brace expansion
for i in {1..5}; do
    echo "Number: $i"                # 1, 2, 3, 4, 5
done

# Med steg
for i in {0..100..10}; do
    echo "Value: $i"                 # 0, 10, 20, ..., 100
done

# Bokstäver
for letter in {a..z}; do
    echo "$letter"                   # a, b, c, ..., z
done

# Seq kommando (mer flexibelt)
for i in $(seq 1 5); do
    echo "$i"                        # 1-5
done

for i in $(seq 0 2 10); do
    echo "$i"                        # 0, 2, 4, 6, 8, 10
done
```

---

## While-loopar

```bash
# Grundläggande while
count=0
while [[ $count -lt 5 ]]; do
    echo "Count: $count"             # 0, 1, 2, 3, 4
    ((count++))                      # Inkrementera
done

# Läsa fil rad för rad
while IFS= read -r line; do
    echo "Line: $line"               # Varje rad i filen
done < file.txt

# Läsa med delimiter
while IFS=: read -r user pass uid gid info home shell; do
    echo "User: $user, Home: $home"  # Parsea /etc/passwd
done < /etc/passwd

# Infinite loop
while true; do
    echo "Running..."
    sleep 1                          # Vänta 1 sekund
    # break för att avsluta
done

# Processa kommando-output rad för rad
ls -1 | while read -r file; do
    echo "File: $file"
done
```

---

## Until-loopar

```bash
# Kör tills villkor är sant
count=0
until [[ $count -ge 5 ]]; do
    echo "Count: $count"             # 0, 1, 2, 3, 4
    ((count++))
done

# Vänta på process
until pgrep -x nginx > /dev/null; do
    echo "Waiting for nginx..."
    sleep 1
done
echo "Nginx is running!"

# Retry-logik
attempts=0
until [[ $attempts -ge 3 ]]; do
    if some_command; then
        echo "Success!"
        break                        # Avsluta loop
    fi
    ((attempts++))
    echo "Attempt $attempts failed, retrying..."
    sleep 2
done
```

---

## Loop-kontroll

```bash
# Break - avsluta loop
for i in {1..10}; do
    if [[ $i -eq 5 ]]; then
        break                        # Avsluta vid 5
    fi
    echo "$i"                        # 1, 2, 3, 4
done

# Continue - hoppa till nästa iteration
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue                     # Hoppa över 3
    fi
    echo "$i"                        # 1, 2, 4, 5
done

# Break från nästlade loopar
for i in {1..3}; do
    for j in {1..3}; do
        if [[ $j -eq 2 ]]; then
            break 2                  # Bryt ur BÅDA looparna
        fi
        echo "$i $j"
    done
done
```

---

## Praktiska loop-exempel

```bash
# Batch-rename filer
for file in *.jpg; do
    mv "$file" "photo_${file}"       # Lägg till prefix
done

# Backup med timestamp
for db in db1 db2 db3; do
    mysqldump "$db" > "${db}_$(date +%Y%m%d).sql"
done

# Parallell ping
for host in server1 server2 server3; do
    ping -c 1 "$host" &              # & kör i bakgrunden
done
wait                                 # Vänta på alla

# Retry med exponential backoff
retry=0
max_retry=5
while [[ $retry -lt $max_retry ]]; do
    if curl -s http://api.example.com; then
        break
    fi
    sleep $((2**retry))              # 1, 2, 4, 8, 16 sekunder
    ((retry++))
done

# Process CSV
while IFS=, read -r name email role; do
    echo "Creating user: $name ($email) with role: $role"
    # create_user "$name" "$email" "$role"
done < users.csv
```

---

## Key Takeaways

1. `for` för känd lista, `while` för villkorsbaserad
2. `{1..10}` för snabb sekvens, `seq` för mer kontroll
3. `IFS= read -r line` för säker rad-för-rad-läsning
4. `break` avslutar loop, `continue` hoppar över iteration
5. `&` och `wait` för parallella operationer
""",
        },
        {
            "title": "Functions & Modularity",
            "slug": "functions-modularity",
            "difficulty": "intermediate",
            "content": """
# Functions & Modularity

## Varför behöver du kunna detta?

Funktioner gör scripts:

- Läsbara och organiserade
- Återanvändbara
- Testbara
- Underhållbara

Utan funktioner blir längre scripts ohanterliga spagetti-kod.

---

## Så fungerar det

Bash-funktioner definieras med `function name()` eller bara `name()`. De kan ta argument, returnera värden (exit codes), och ha lokala variabler.

---

## Definiera funktioner

```bash
# Två sätt att definiera (båda fungerar)
function greet() {
    echo "Hello, $1!"                # $1 = första argumentet
}

say_bye() {
    echo "Goodbye, $1!"
}

# Anropa funktioner
greet "Alice"                        # "Hello, Alice!"
say_bye "Bob"                        # "Goodbye, Bob!"

# Funktion före anrop (obligatoriskt)
# Bash parsar sekventiellt - funktionen måste definieras först
```

---

## Funktionsargument

```bash
process_files() {
    echo "Function: $0"              # Scriptets namn (inte funktionen!)
    echo "First arg: $1"             # Första argumentet
    echo "Second arg: $2"            # Andra argumentet
    echo "All args: $@"              # Alla argument
    echo "Arg count: $#"             # Antal argument
}

process_files "file1.txt" "file2.txt" "file3.txt"

# Med default-värden
greet() {
    local name=${1:-"World"}         # Default till "World"
    echo "Hello, $name!"
}

greet                                # "Hello, World!"
greet "Alice"                        # "Hello, Alice!"
```

---

## Return-värden

```bash
# Exit code (0 = success, 1-255 = error)
is_even() {
    local num=$1
    if (( num % 2 == 0 )); then
        return 0                     # True/success
    else
        return 1                     # False/error
    fi
}

if is_even 4; then
    echo "4 is even"
fi

# Returnera sträng via echo
get_timestamp() {
    echo "$(date +%Y%m%d_%H%M%S)"    # Output blir "return value"
}

timestamp=$(get_timestamp)           # Fånga output
echo "Timestamp: $timestamp"

# Returnera via global variabel (undvik om möjligt)
calculate() {
    RESULT=$(( $1 + $2 ))            # Global variabel
}

calculate 5 3
echo "Result: $RESULT"               # 8
```

---

## Lokala variabler

```bash
# Utan local - globalt scope
bad_function() {
    counter=10                       # Globalt! Läcker ut
}

bad_function
echo $counter                        # 10 (oönskat)

# Med local - lokalt scope
good_function() {
    local counter=10                 # Lokalt för funktionen
    echo "Inside: $counter"
}

good_function
echo $counter                        # Tom (korrekt)

# Best practice: Alltid använd local
process_data() {
    local input="$1"
    local output=""
    local temp_file="/tmp/process_$$"

    # ... processning ...

    echo "$output"
}
```

---

## Rekursion

```bash
# Rekursiv funktion
factorial() {
    local n=$1
    if (( n <= 1 )); then
        echo 1                       # Base case
    else
        local sub=$(factorial $((n-1)))  # Rekursivt anrop
        echo $((n * sub))
    fi
}

echo "5! = $(factorial 5)"           # 120

# Traversera katalog rekursivt
traverse() {
    local dir="$1"
    for item in "$dir"/*; do
        if [[ -d "$item" ]]; then
            echo "DIR: $item"
            traverse "$item"         # Rekursion för subkataloger
        else
            echo "FILE: $item"
        fi
    done
}

traverse "/path/to/directory"
```

---

## Bibliotek och sourcing

```bash
# lib/utils.sh - Återanvändbara funktioner
log_info() {
    echo "[INFO] $(date +%H:%M:%S) $*"
}

log_error() {
    echo "[ERROR] $(date +%H:%M:%S) $*" >&2
}

validate_file() {
    local file="$1"
    if [[ ! -f "$file" ]]; then
        log_error "File not found: $file"
        return 1
    fi
    return 0
}

# main.sh - Använder biblioteket
#!/bin/bash
source lib/utils.sh                  # Ladda funktioner

log_info "Starting script"

if validate_file "config.txt"; then
    log_info "Config found"
else
    exit 1
fi
```

---

## Avancerade mönster

```bash
# Funktion med namngivna argument (via associativ array)
create_user() {
    local -A args
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --name) args[name]="$2"; shift 2 ;;
            --email) args[email]="$2"; shift 2 ;;
            --role) args[role]="${2:-user}"; shift 2 ;;
            *) shift ;;
        esac
    done

    echo "Creating: ${args[name]} (${args[email]}) as ${args[role]}"
}

create_user --name "Alice" --email "alice@example.com" --role "admin"

# Funktion som tar callback
with_retry() {
    local max_attempts=$1
    local callback=$2
    shift 2

    local attempt=1
    while (( attempt <= max_attempts )); do
        if "$callback" "$@"; then
            return 0
        fi
        echo "Attempt $attempt failed, retrying..."
        ((attempt++))
        sleep 1
    done
    return 1
}

download_file() {
    curl -s -o /tmp/file "$1"
}

with_retry 3 download_file "http://example.com/file.zip"
```

---

## Key Takeaways

1. Definiera funktioner före anrop
2. Använd `local` för alla funktionsvariabler
3. `$@` för alla argument, `$#` för antal
4. Return exit codes (0-255), echo för strängar
5. `source` för att ladda bibliotek
""",
        },
        {
            "title": "Input Handling & Arguments",
            "slug": "input-handling-arguments",
            "difficulty": "intermediate",
            "content": """
# Input Handling & Arguments

## Varför behöver du kunna detta?

Bra scripts behöver hantera input korrekt:

- Kommandoradsargument
- Användarinput
- Konfigurationsfiler
- Pipad data

Utan robust input-hantering blir scripts opålitliga och svåranvända.

---

## Så fungerar det

Bash erbjuder flera sätt att ta emot input:

- Positionella argument (`$1`, `$2`)
- Flaggor och options (`-v`, `--verbose`)
- Interaktiv input (`read`)
- Stdin (pipelines)

---

## Positionella argument

```bash
#!/bin/bash
# script.sh arg1 arg2 arg3

echo "Script name: $0"               # ./script.sh
echo "First arg: $1"                 # arg1
echo "Second arg: $2"                # arg2
echo "All args: $@"                  # arg1 arg2 arg3
echo "Arg count: $#"                 # 3

# Shift - flytta argument
echo "Before shift: $1"              # arg1
shift                                # Ta bort $1, $2 blir $1
echo "After shift: $1"               # arg2

# Shift flera
shift 2                              # Ta bort två argument

# Iterera över argument
for arg in "$@"; do
    echo "Processing: $arg"
done
```

---

## Getopts för options

```bash
#!/bin/bash
# Hantera flaggor: -v -f filename -n 10

usage() {
    echo "Usage: $0 [-v] [-f file] [-n number]"
    exit 1
}

verbose=false
filename=""
number=0

while getopts "vf:n:h" opt; do
    case $opt in
        v) verbose=true ;;           # -v (ingen parameter)
        f) filename="$OPTARG" ;;     # -f file (: kräver parameter)
        n) number="$OPTARG" ;;       # -n number
        h) usage ;;
        ?) usage ;;                  # Okänd option
    esac
done

shift $((OPTIND - 1))                # Ta bort processade options

# $@ innehåller nu resterande argument
echo "Verbose: $verbose"
echo "File: $filename"
echo "Number: $number"
echo "Remaining: $@"

# Användning: ./script.sh -v -f data.txt -n 5 extra1 extra2
```

---

## Long options

```bash
#!/bin/bash
# Hantera --verbose --file=name --help

verbose=false
filename=""
output=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            verbose=true
            shift
            ;;
        -f|--file)
            filename="$2"
            shift 2
            ;;
        --file=*)                    # --file=value format
            filename="${1#*=}"       # Ta bort allt före =
            shift
            ;;
        -o|--output)
            output="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 [--verbose] [--file FILE] [--output FILE]"
            exit 0
            ;;
        --)                          # Slut på options
            shift
            break
            ;;
        -*)
            echo "Unknown option: $1"
            exit 1
            ;;
        *)
            break                    # Slut på options
            ;;
    esac
done

echo "Verbose: $verbose"
echo "File: $filename"
echo "Remaining args: $@"
```

---

## Läsa användarinput

```bash
# Grundläggande read
echo -n "Enter name: "               # -n för ingen newline
read name
echo "Hello, $name!"

# Med prompt
read -p "Enter age: " age            # -p för inbyggd prompt

# Tyst input (lösenord)
read -s -p "Password: " password     # -s för silent
echo                                 # Ny rad efter

# Med timeout
if read -t 5 -p "Quick! Enter code: " code; then
    echo "Code: $code"
else
    echo "Too slow!"
fi

# Med default-värde
read -p "Environment [production]: " env
env=${env:-production}               # Default om tom

# Läsa till array
read -a colors -p "Enter colors: "   # Separerat med mellanslag
echo "First color: ${colors[0]}"
```

---

## Validera input

```bash
# Kontrollera antal argument
if [[ $# -lt 2 ]]; then
    echo "Error: Need at least 2 arguments"
    echo "Usage: $0 source destination"
    exit 1
fi

# Validera att fil finns
if [[ ! -f "$1" ]]; then
    echo "Error: File not found: $1"
    exit 1
fi

# Validera numerisk input
validate_number() {
    local input="$1"
    if [[ ! "$input" =~ ^[0-9]+$ ]]; then
        echo "Error: Not a number: $input"
        return 1
    fi
    return 0
}

# Validera email
validate_email() {
    local email="$1"
    if [[ ! "$email" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$ ]]; then
        echo "Error: Invalid email: $email"
        return 1
    fi
    return 0
}

# Validera med loop
while true; do
    read -p "Enter port (1-65535): " port
    if [[ "$port" =~ ^[0-9]+$ ]] && (( port >= 1 && port <= 65535 )); then
        break
    fi
    echo "Invalid port, try again"
done
```

---

## Läsa från stdin/pipe

```bash
#!/bin/bash
# Stödjer både fil och pipe

# Kontrollera om input kommer från pipe
if [[ -p /dev/stdin ]]; then
    # Läs från pipe
    while IFS= read -r line; do
        echo "Piped: $line"
    done
else
    # Läs från fil (argument)
    while IFS= read -r line; do
        echo "File: $line"
    done < "$1"
fi

# Användning:
# cat data.txt | ./script.sh    # Pipe
# ./script.sh data.txt          # Fil

# Mer robust version
input="${1:-/dev/stdin}"             # Fil eller stdin
while IFS= read -r line; do
    process_line "$line"
done < "$input"
```

---

## Konfigurations-filer

```bash
# config.conf
# KEY=value format
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=myapp

# Ladda config
if [[ -f config.conf ]]; then
    source config.conf               # Ladda variabler
fi

# Säkrare: validera varje rad
while IFS='=' read -r key value; do
    # Hoppa över kommentarer och tomma rader
    [[ $key =~ ^#.*$ ]] && continue
    [[ -z $key ]] && continue

    # Ta bort whitespace
    key=$(echo "$key" | xargs)
    value=$(echo "$value" | xargs)

    # Sätt variabel
    declare "$key=$value"
done < config.conf

echo "Connecting to $DATABASE_HOST:$DATABASE_PORT"
```

---

## Key Takeaways

1. `getopts` för korta options (-v, -f)
2. While-loop för long options (--verbose, --file)
3. `read -p` för prompt, `-s` för lösenord
4. Validera input innan användning
5. Stöd både pipe och filargument för flexibilitet
""",
        },
        {
            "title": "Text Processing (grep, sed, awk)",
            "slug": "text-processing-grep-sed-awk",
            "difficulty": "intermediate",
            "content": """
# Text Processing (grep, sed, awk)

## Varför behöver du kunna detta?

Unix-filosofin: små verktyg som gör en sak bra. Textprocessering är kärnan:

- Sök i loggar (grep)
- Transformera data (sed)
- Extrahera och analysera (awk)

Dessa verktyg är snabbare och mer kraftfulla än de flesta scriptlösningar.

---

## Så fungerar det

**grep** - Global Regular Expression Print. Söker och filtrerar.
**sed** - Stream Editor. Transformerar text.
**awk** - Pattern scanning och processing. Kolumnbaserad analys.

Kombinerade med pipes blir de extremt kraftfulla.

---

## grep - Söka i text

```bash
# Grundläggande sökning
grep "error" logfile.txt             # Rader som innehåller "error"
grep -i "error" logfile.txt          # Case-insensitive
grep -v "debug" logfile.txt          # Invertera (exkludera debug)
grep -n "error" logfile.txt          # Visa radnummer

# Regex
grep -E "error|warning" logfile.txt  # Extended regex (OR)
grep "^Start" logfile.txt            # Rader som börjar med "Start"
grep "end$" logfile.txt              # Rader som slutar med "end"
grep -E "[0-9]{3}" logfile.txt       # Tre siffror i rad

# Filer och kataloger
grep -r "TODO" .                     # Rekursivt i katalog
grep -l "error" *.log                # Lista bara filnamn
grep -c "error" logfile.txt          # Räkna matchande rader

# Context
grep -A 3 "error" logfile.txt        # 3 rader EFTER match
grep -B 2 "error" logfile.txt        # 2 rader FÖRE match
grep -C 2 "error" logfile.txt        # 2 rader före OCH efter

# Praktiska exempel
grep -E "^[0-9]{4}-" access.log      # Rader som börjar med år
grep -oE "[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+" access.log  # Extrahera IP-adresser
ps aux | grep nginx                  # Hitta nginx-processer
```

---

## sed - Stream editor

```bash
# Substitution (s/old/new/)
sed 's/error/ERROR/' file.txt        # Första på varje rad
sed 's/error/ERROR/g' file.txt       # Alla (global)
sed 's/error/ERROR/gi' file.txt      # Case-insensitive

# In-place edit
sed -i 's/old/new/g' file.txt        # Ändra filen direkt
sed -i.bak 's/old/new/g' file.txt    # Med backup (.bak)

# Adressering (vilka rader att ändra)
sed '5s/old/new/' file.txt           # Bara rad 5
sed '1,10s/old/new/' file.txt        # Rad 1-10
sed '/pattern/s/old/new/' file.txt   # Rader som matchar pattern

# Delete (d)
sed '5d' file.txt                    # Ta bort rad 5
sed '1,5d' file.txt                  # Ta bort rad 1-5
sed '/pattern/d' file.txt            # Ta bort rader som matchar
sed '/^$/d' file.txt                 # Ta bort tomma rader
sed '/^#/d' file.txt                 # Ta bort kommentarer

# Print (p) med -n
sed -n '5p' file.txt                 # Skriv bara rad 5
sed -n '10,20p' file.txt             # Rad 10-20
sed -n '/error/p' file.txt           # Rader med error (som grep)

# Praktiska exempel
sed 's/^/    /' file.txt             # Indentera med 4 spaces
sed 's/[[:space:]]*$//' file.txt     # Ta bort trailing whitespace
sed 's/<[^>]*>//g' file.html         # Ta bort HTML-taggar (enkelt)
```

---

## awk - Kolumnbaserad analys

```bash
# Grundläggande syntax: awk 'pattern {action}' file

# Kolumner (default: whitespace-separerade)
awk '{print $1}' file.txt            # Första kolumnen
awk '{print $2, $3}' file.txt        # Kolumn 2 och 3
awk '{print $NF}' file.txt           # Sista kolumnen
awk '{print NF}' file.txt            # Antal kolumner per rad

# Speciella variabler
# $0 = hela raden
# $1, $2... = kolumner
# NR = radnummer
# NF = antal fält
# FS = field separator

# Field separator
awk -F: '{print $1}' /etc/passwd     # Kolon-separerat
awk -F',' '{print $2}' data.csv      # CSV

# Patterns (filter)
awk '/error/' file.txt               # Rader med error
awk '$3 > 100' file.txt              # Kolumn 3 > 100
awk 'NR > 1' file.txt                # Hoppa över header

# BEGIN och END blocks
awk 'BEGIN {print "Start"} {print $1} END {print "Done"}' file.txt

# Beräkningar
awk '{sum += $1} END {print sum}' numbers.txt  # Summa
awk '{sum += $1} END {print sum/NR}' numbers.txt  # Medel
awk 'NR==1 {max=$1} $1>max {max=$1} END {print max}' numbers.txt  # Max
```

---

## Praktiska kombinationer

```bash
# Analysera access-logg
# Format: IP - - [date] "request" status size

# Top 10 IP-adresser
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# Svar per statuskod
awk '{print $9}' access.log | sort | uniq -c | sort -rn

# Genomsnittlig response size
awk '{sum+=$10; count++} END {print sum/count}' access.log

# 404-fel med URL
awk '$9 == 404 {print $7}' access.log | sort | uniq -c | sort -rn

# Extrahera data från JSON (enkelt)
grep '"name":' data.json | sed 's/.*"name": *"\\([^"]*\\)".*/\\1/'

# CSV-manipulation
# Ta kolumn 2 och 4 från CSV
awk -F',' '{print $2","$4}' data.csv

# Byt ordning på kolumner
awk -F',' '{print $3","$1","$2}' data.csv

# Summera kolumn i CSV (hoppa över header)
awk -F',' 'NR>1 {sum+=$3} END {print sum}' sales.csv
```

---

## Key Takeaways

1. `grep -E` för extended regex, `-r` för rekursiv sökning
2. `sed 's/old/new/g'` för ersättning, `-i` för in-place
3. `awk -F:` för delimiter, `$1`, `$NF` för kolumner
4. Kombinera med pipes för kraftfulla one-liners
5. `sort | uniq -c | sort -rn` för frekvensanalys
""",
        },
        {
            "title": "Error Handling & Exit Codes",
            "slug": "error-handling-exit-codes",
            "difficulty": "intermediate",
            "content": """
# Error Handling & Exit Codes

## Varför behöver du kunna detta?

Scripts utan felhantering är farliga. De kan:

- Fortsätta trots kritiska fel
- Ge missvisande status
- Orsaka dataförlust
- Vara omöjliga att felsöka

Robust felhantering är skillnaden mellan hobby-scripts och produktion.

---

## Så fungerar det

Varje kommando returnerar en exit code:

- **0** = Success
- **1-255** = Fel (olika betydelser)

`$?` innehåller senaste kommandots exit code.

---

## Exit codes

```bash
# Kontrollera exit code
ls /exists
echo $?                              # 0 (success)

ls /does-not-exist
echo $?                              # 2 (no such file)

# Sätta exit code i script
exit 0                               # Success
exit 1                               # General error
exit 2                               # Misuse of shell command
exit 126                             # Command not executable
exit 127                             # Command not found
exit 128+N                           # Fatal error signal N

# Definiera egna exit codes
readonly E_SUCCESS=0
readonly E_INVALID_ARGS=1
readonly E_FILE_NOT_FOUND=2
readonly E_PERMISSION_DENIED=3

# Använd i script
if [[ ! -f "$config_file" ]]; then
    echo "Error: Config file not found" >&2
    exit $E_FILE_NOT_FOUND
fi
```

---

## Set options för säkerhet

```bash
#!/bin/bash
# Lägg till i början av varje script

set -e                               # Exit vid första fel
set -u                               # Exit vid odefinierad variabel
set -o pipefail                      # Pipe returnerar fel om något steg fallerar

# Kombinerat (rekommenderas)
set -euo pipefail

# Vad de gör:

# -e: Exit vid fel
set -e
false                                # Script avslutas här
echo "Never reached"

# -u: Odefinierade variabler är fel
set -u
echo $undefined_var                  # Error: unbound variable

# -o pipefail: Pipe-fel propageras
set -o pipefail
false | true                         # Returnerar 1 (första kommandot failade)
echo $?                              # 1

# Utan pipefail:
unset PIPEFAIL
false | true
echo $?                              # 0 (bara sista räknas)
```

---

## Felhantering med trap

```bash
#!/bin/bash

# Cleanup-funktion
cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile_$$           # Ta bort temp-filer
    exit ${1:-1}                     # Exit med given kod eller 1
}

# Sätt trap för signaler
trap cleanup EXIT                    # Körs alltid vid exit
trap cleanup ERR                     # Körs vid fel (med set -e)
trap cleanup SIGINT SIGTERM          # Körs vid Ctrl+C eller kill

# Mer avancerad trap
trap 'echo "Error on line $LINENO"; cleanup' ERR

# Exempel med temp-filer
temp_file=$(mktemp)
trap "rm -f $temp_file" EXIT         # Garanterar cleanup

# Arbeta med temp-filen...
echo "data" > "$temp_file"
process_data "$temp_file"

# Filen tas bort automatiskt oavsett hur scriptet avslutas
```

---

## Manuell felhantering

```bash
# Utan set -e - manuell kontroll
command || {
    echo "Command failed" >&2
    exit 1
}

# Med if
if ! command; then
    echo "Command failed" >&2
    exit 1
fi

# Hantera specifika fel
if ! output=$(command 2>&1); then
    case $? in
        1) echo "General error" ;;
        2) echo "File not found" ;;
        *) echo "Unknown error: $?" ;;
    esac
    exit 1
fi

# Retry-logik
retry() {
    local max_attempts=$1
    shift
    local attempt=1

    while (( attempt <= max_attempts )); do
        if "$@"; then
            return 0
        fi
        echo "Attempt $attempt failed, retrying..." >&2
        ((attempt++))
        sleep 1
    done

    echo "All $max_attempts attempts failed" >&2
    return 1
}

retry 3 curl -s http://example.com
```

---

## Logging och debug

```bash
#!/bin/bash

# Loggfunktioner
log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') $*"
}

log_warn() {
    echo "[WARN] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2
}

log_debug() {
    if [[ "${DEBUG:-false}" == "true" ]]; then
        echo "[DEBUG] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2
    fi
}

# Användning
log_info "Starting process"
log_debug "Variable x = $x"
log_error "Failed to connect"

# Debug mode
# DEBUG=true ./script.sh             # Aktiverar debug-output

# Bash debug mode
set -x                               # Skriv ut varje kommando
set +x                               # Stäng av

# Eller för hela scriptet:
bash -x script.sh                    # Kör med debug
```

---

## Best practices

```bash
#!/bin/bash
set -euo pipefail

# Konstanter
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"

# Cleanup
cleanup() {
    local exit_code=$?
    # Cleanup-logik här
    exit $exit_code
}
trap cleanup EXIT

# Felhantering
die() {
    echo "[ERROR] $*" >&2
    exit 1
}

# Validering
[[ $# -ge 1 ]] || die "Usage: $SCRIPT_NAME <argument>"
[[ -f "$1" ]] || die "File not found: $1"

# Huvudlogik med felhantering
main() {
    log_info "Starting $SCRIPT_NAME"

    if ! process_file "$1"; then
        die "Processing failed"
    fi

    log_info "Completed successfully"
}

main "$@"
```

---

## Key Takeaways

1. `set -euo pipefail` i alla produktionsscripts
2. `$?` innehåller senaste exit code
3. `trap` för cleanup och signalhantering
4. `>&2` för felmeddelanden till stderr
5. Definiera `die()`-funktion för konsekvent felhantering
""",
        },
        {
            "title": "Process Management",
            "slug": "process-management",
            "difficulty": "intermediate",
            "content": """
# Process Management

## Varför behöver du kunna detta?

Scripts behöver ofta:

- Starta bakgrundsprocesser
- Vänta på processer
- Hantera parallella operationer
- Övervaka och döda processer

Utan processhantering kan du inte bygga robusta automation-lösningar.

---

## Så fungerar det

Unix-processer har:

- **PID** - Process ID
- **PPID** - Parent Process ID
- **State** - Running, Sleeping, Stopped, Zombie

Scripts kan spawna child-processer och kontrollera dem.

---

## Bakgrundsprocesser

```bash
# Starta i bakgrunden
long_command &                       # & kör i bakgrunden
pid=$!                               # PID för senaste bakgrundsprocess

echo "Started process: $pid"

# Vänta på process
wait $pid                            # Vänta på specifik PID
echo "Exit code: $?"

wait                                 # Vänta på ALLA bakgrundsprocesser

# Exempel
./process1.sh &
./process2.sh &
./process3.sh &
wait                                 # Vänta på alla tre

# Med exit codes
./process1.sh &
pid1=$!
./process2.sh &
pid2=$!

wait $pid1 || echo "Process 1 failed"
wait $pid2 || echo "Process 2 failed"
```

---

## Parallell exekvering

```bash
# Parallella operationer
for server in server1 server2 server3; do
    ssh "$server" "uptime" &         # Körs parallellt
done
wait                                 # Vänta på alla

# Med begränsat antal parallella
max_parallel=4
pids=()

for file in *.txt; do
    process_file "$file" &
    pids+=($!)

    # Om vi nått max, vänta på en
    if (( ${#pids[@]} >= max_parallel )); then
        wait "${pids[0]}"
        pids=("${pids[@]:1}")        # Ta bort första
    fi
done
wait                                 # Vänta på resterande

# Med GNU Parallel (om installerat)
parallel process_file ::: *.txt      # Parallelliserar automatiskt
ls *.txt | parallel -j4 process_file # Max 4 parallella
```

---

## Subshells

```bash
# Subshell - kör i egen process
(cd /tmp && ls)                      # cd påverkar inte parent
echo $PWD                            # Fortfarande original

# Variabler i subshell
count=0
(
    count=10                         # Ändrar bara i subshell
    echo "Inside: $count"            # 10
)
echo "Outside: $count"               # 0 (oförändrad)

# Command substitution skapar subshell
result=$(
    cd /tmp
    process_files
    echo "done"
)

# Pipe skapar subshell
count=0
echo "1 2 3" | while read num; do
    ((count++))                      # Subshell!
done
echo "Count: $count"                 # 0 (oförändrad)

# Lösning: process substitution eller here-string
while read num; do
    ((count++))
done <<< "1 2 3"
echo "Count: $count"                 # 3 (korrekt)
```

---

## Processkontroll

```bash
# Hitta processer
ps aux                               # Alla processer
ps aux | grep nginx                  # Filtrera
pgrep nginx                          # PID:ar för nginx
pgrep -f "python script.py"          # Matcha hela kommandoraden
pidof nginx                          # PID för program

# Signaler
kill $pid                            # SIGTERM (graceful)
kill -9 $pid                         # SIGKILL (force)
kill -HUP $pid                       # SIGHUP (reload config)

# Döda alla med namn
pkill nginx                          # Döda alla nginx
pkill -f "python script.py"          # Matcha hela kommandoraden
killall nginx                        # Alternativ

# Kontrollera om process lever
if kill -0 $pid 2>/dev/null; then
    echo "Process is running"
else
    echo "Process is dead"
fi

# Vänta på process död
while kill -0 $pid 2>/dev/null; do
    echo "Waiting for process to die..."
    sleep 1
done
```

---

## Job control

```bash
# Jobs i interaktiv shell
sleep 100 &                          # Starta i bakgrund
jobs                                 # Lista jobs

# Suspendra (Ctrl+Z)
# sleep 100
# ^Z
# [1]+  Stopped  sleep 100

fg                                   # Fortsätt i förgrund
bg                                   # Fortsätt i bakgrund
fg %1                                # Specifikt job

# Disown - ta bort från shell
disown %1                            # Job fortsätter efter logout
nohup command &                      # Ignorera SIGHUP
```

---

## Lås och mutual exclusion

```bash
# Flock för fillåsning
(
    flock -n 9 || { echo "Already running"; exit 1; }

    # Kritisk sektion - bara en instans
    echo "Running exclusively..."
    sleep 10

) 9>/var/lock/myscript.lock

# Enkel PID-fil
PIDFILE="/var/run/myscript.pid"

if [[ -f "$PIDFILE" ]]; then
    pid=$(cat "$PIDFILE")
    if kill -0 "$pid" 2>/dev/null; then
        echo "Already running (PID: $pid)"
        exit 1
    fi
    rm -f "$PIDFILE"                 # Stale pidfile
fi

echo $$ > "$PIDFILE"
trap "rm -f $PIDFILE" EXIT

# Script-logik här...
```

---

## Timeout

```bash
# GNU timeout
timeout 10 long_command              # Max 10 sekunder
timeout 10s command                  # 10 sekunder
timeout 5m command                   # 5 minuter
timeout 2h command                   # 2 timmar

# Med signal
timeout -s SIGKILL 10 command        # Skicka SIGKILL

# Exit code
timeout 5 sleep 10
echo $?                              # 124 = timeout

# Manuell timeout
(
    sleep 30
    kill $$ 2>/dev/null              # Döda parent efter 30s
) &
watchdog_pid=$!

if long_command; then
    kill $watchdog_pid 2>/dev/null   # Avbryt watchdog
fi
```

---

## Key Takeaways

1. `&` för bakgrund, `$!` för senaste PID
2. `wait` för att vänta på bakgrundsprocesser
3. Subshells har egna variabler (påverkar inte parent)
4. `kill -0` för att kontrollera om process lever
5. `flock` eller PID-fil för att förhindra parallella körningar
""",
        },
        {
            "title": "Arrays & Associative Arrays",
            "slug": "arrays-associative-arrays",
            "difficulty": "intermediate",
            "content": """
# Arrays & Associative Arrays

## Varför behöver du kunna detta?

Variabler räcker inte när du hanterar:

- Listor av filer
- Servernamn
- Konfigurationsvärden
- Key-value par

Arrays gör Bash-scripting betydligt kraftfullare.

---

## Så fungerar det

Bash har två array-typer:

- **Indexed arrays** - Numrerade (0, 1, 2...)
- **Associative arrays** - Namngivna nycklar (key=value)

Associative arrays kräver `declare -A`.

---

## Indexed arrays

```bash
# Skapa array
fruits=("apple" "banana" "cherry")   # Array literal
fruits=()                            # Tom array
fruits[0]="apple"                    # Sätt index

# Läsa element
echo "${fruits[0]}"                  # Första (apple)
echo "${fruits[1]}"                  # Andra (banana)
echo "${fruits[-1]}"                 # Sista (cherry)

# Alla element
echo "${fruits[@]}"                  # apple banana cherry
echo "${fruits[*]}"                  # apple banana cherry (som en sträng)

# Längd
echo "${#fruits[@]}"                 # 3 (antal element)
echo "${#fruits[0]}"                 # 5 (längd av "apple")

# Index
echo "${!fruits[@]}"                 # 0 1 2 (alla index)

# Lägga till element
fruits+=("date")                     # Lägg till i slutet
fruits+=("elderberry" "fig")         # Lägg till flera

# Ta bort element
unset fruits[1]                      # Ta bort index 1
# OBS: index 1 försvinner, index 2 blir INTE 1!
```

---

## Loopa över arrays

```bash
# Loopa över värden
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# Loopa med index
for i in "${!fruits[@]}"; do
    echo "Index $i: ${fruits[$i]}"
done

# VIKTIGT: Citera "${array[@]}" för element med mellanslag
files=("file one.txt" "file two.txt")
for file in "${files[@]}"; do        # Rätt
    echo "$file"
done
# Utan citattecken splittras vid mellanslag

# Loopa över range
for i in {0..10}; do
    echo "Number: $i"
done

# C-style
for ((i=0; i<${#fruits[@]}; i++)); do
    echo "${fruits[$i]}"
done
```

---

## Array-operationer

```bash
# Slicing
arr=(a b c d e f g)
echo "${arr[@]:2}"                   # c d e f g (från index 2)
echo "${arr[@]:2:3}"                 # c d e (3 element från index 2)

# Kopiera array
copy=("${arr[@]}")

# Konkatenera arrays
arr1=(1 2 3)
arr2=(4 5 6)
combined=("${arr1[@]}" "${arr2[@]}")
echo "${combined[@]}"                # 1 2 3 4 5 6

# Söka i array
arr=(apple banana cherry)
if [[ " ${arr[*]} " =~ " banana " ]]; then
    echo "Found banana"
fi

# Funktion för att kolla existens
contains() {
    local element="$1"
    shift
    for item; do
        [[ "$item" == "$element" ]] && return 0
    done
    return 1
}

if contains "banana" "${arr[@]}"; then
    echo "Found!"
fi
```

---

## Associative arrays (hash/dict)

```bash
# MÅSTE deklareras först
declare -A user

# Sätta värden
user[name]="John"
user[age]=30
user[email]="john@example.com"

# Eller inline
declare -A colors=(
    [red]="#FF0000"
    [green]="#00FF00"
    [blue]="#0000FF"
)

# Läsa
echo "${user[name]}"                 # John
echo "${colors[red]}"                # #FF0000

# Alla nycklar
echo "${!user[@]}"                   # name age email

# Alla värden
echo "${user[@]}"                    # John 30 john@example.com

# Antal
echo "${#user[@]}"                   # 3

# Kontrollera om nyckel finns
if [[ -v user[name] ]]; then
    echo "Name exists"
fi

# Default-värde
echo "${user[missing]:-default}"     # default (om missing inte finns)
```

---

## Loopa över associative arrays

```bash
declare -A servers=(
    [web]="192.168.1.10"
    [db]="192.168.1.11"
    [cache]="192.168.1.12"
)

# Loopa över nycklar
for role in "${!servers[@]}"; do
    echo "Role: $role, IP: ${servers[$role]}"
done

# Loopa över värden
for ip in "${servers[@]}"; do
    echo "IP: $ip"
done
```

---

## Praktiska exempel

```bash
# Läs fil till array
mapfile -t lines < file.txt          # En rad per element
readarray -t lines < file.txt        # Samma sak

# Kommando-output till array
mapfile -t processes < <(ps aux | awk '{print $11}')

# Argument till array
args=("$@")                          # Alla script-argument

# Skapa array från sträng
str="apple,banana,cherry"
IFS=',' read -ra arr <<< "$str"
echo "${arr[@]}"                     # apple banana cherry

# Joina array till sträng
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

echo "DB Host: ${config[DB_HOST]}"
```

---

## Key Takeaways

1. `declare -A` krävs för associative arrays
2. `"${arr[@]}"` för alla element (med citattecken!)
3. `"${!arr[@]}"` för alla nycklar/index
4. `mapfile -t` för att läsa fil till array
5. `[[ -v arr[key] ]]` för att kolla om nyckel finns
""",
        },
        {
            "title": "String Manipulation",
            "slug": "string-manipulation",
            "difficulty": "intermediate",
            "content": """
# String Manipulation

## Varför behöver du kunna detta?

Stringhantering är konstant:

- Parsa filnamn och sökvägar
- Extrahera data från output
- Validera input
- Transformera text

Bash har kraftfulla inbyggda strängoperationer som undviker externa kommandon.

---

## Så fungerar det

Bash parameter expansion (`${var...}`) ger kraftfulla strängoperationer.

Fördelar över `sed`/`awk`:
- Snabbare (ingen subprocess)
- Enklare syntax för enkla fall
- Inget beroende på externa verktyg

---

## Grundläggande operationer

```bash
str="Hello World"

# Längd
echo "${#str}"                       # 11

# Substring
echo "${str:0:5}"                    # Hello (5 tecken från position 0)
echo "${str:6}"                      # World (från position 6)
echo "${str: -5}"                    # World (5 sista, notera mellanslag)

# Konkatenering
a="Hello"
b="World"
c="$a $b"                            # Hello World
c="${a}${b}"                         # HelloWorld (utan mellanslag)

# Uppercase / Lowercase (Bash 4+)
str="Hello World"
echo "${str^^}"                      # HELLO WORLD (uppercase)
echo "${str,,}"                      # hello world (lowercase)
echo "${str^}"                       # Hello world (första bokstaven upper)
```

---

## Pattern matching & replacement

```bash
# Ersättning
str="hello hello hello"
echo "${str/hello/hi}"               # hi hello hello (första)
echo "${str//hello/hi}"              # hi hi hi (alla)

# Ta bort (ersätt med inget)
echo "${str//hello/}"                # (tar bort alla "hello")

# Prefix/suffix
str="hello.txt.bak"
echo "${str#*.}"                     # txt.bak (ta bort minsta prefix till .)
echo "${str##*.}"                    # bak (ta bort största prefix till .)
echo "${str%.*}"                     # hello.txt (ta bort minsta suffix från .)
echo "${str%%.*}"                    # hello (ta bort största suffix från .)

# Praktiska exempel
filename="document.txt"
echo "${filename%.*}"                # document (utan extension)
echo "${filename##*.}"               # txt (bara extension)

path="/home/user/documents/file.txt"
echo "${path##*/}"                   # file.txt (bara filnamn)
echo "${path%/*}"                    # /home/user/documents (utan filnamn)
```

---

## Default-värden och validering

```bash
# Default om odefinierad eller tom
echo "${var:-default}"               # Använd default, ändra inte var
echo "${var:=default}"               # Sätt var till default
echo "${var:+alternate}"             # alternate om var är satt
echo "${var:?error message}"         # Exit med fel om var är osatt

# Utan kolon - bara odefinierad (tom sträng OK)
echo "${var-default}"                # Default bara om odefinierad

# Praktiskt: miljövariabler med defaults
export DB_HOST="${DB_HOST:-localhost}"
export DB_PORT="${DB_PORT:-5432}"

# Validering
name="${1:?Usage: script.sh <name>}"  # Exit om argument saknas
```

---

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
if [[ "$version" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+) ]]; then
    major="${BASH_REMATCH[1]}"        # 2
    minor="${BASH_REMATCH[2]}"        # 1
    patch="${BASH_REMATCH[3]}"        # 3
fi

# Validera IP-adress (förenklad)
ip="192.168.1.100"
if [[ "$ip" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Valid IP format"
fi
```

---

## Case conversion och transformering

```bash
# Case conversion (Bash 4+)
str="Hello World"

# Hela strängen
echo "${str^^}"                      # HELLO WORLD
echo "${str,,}"                      # hello world

# Specifika tecken
echo "${str^^[aeiou]}"               # HEllO WOrld (vokaler upper)
echo "${str,,[HW]}"                  # hello world (H och W lower)

# Bara första/sista
echo "${str^}"                       # Hello World (första upper)
echo "${str,}"                       # hello World (första lower)

# Transformera med tr
echo "hello" | tr '[:lower:]' '[:upper:]'  # HELLO
echo "HELLO" | tr 'A-Z' 'a-z'              # hello

# Ta bort tecken
echo "hello123" | tr -d '0-9'              # hello

# Squeeze duplicates
echo "hellooo" | tr -s 'o'                 # helo
```

---

## Splitta och joina

```bash
# Splitta sträng på delimiter
str="one:two:three"
IFS=':' read -ra parts <<< "$str"
echo "${parts[0]}"                   # one
echo "${parts[1]}"                   # two

# Joina array till sträng
arr=("one" "two" "three")
joined=$(IFS=':'; echo "${arr[*]}")
echo "$joined"                       # one:two:three

# Splitta på newline
text="line1
line2
line3"
while IFS= read -r line; do
    echo "Line: $line"
done <<< "$text"

# Splitta filepath
path="/home/user/documents/file.txt"
dir=$(dirname "$path")               # /home/user/documents
file=$(basename "$path")             # file.txt
name="${file%.*}"                    # file
ext="${file##*.}"                    # txt
```

---

## Praktiska exempel

```bash
# Slugify (för URL-vänliga strängar)
slugify() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-'
}
slugify "Hello World 123!"           # hello-world-123

# Trim whitespace
trim() {
    local str="$1"
    str="${str#"${str%%[![:space:]]*}"}"  # Leading
    str="${str%"${str##*[![:space:]]}"}"  # Trailing
    echo "$str"
}
trim "  hello  "                     # hello

# Centrera text
center() {
    local text="$1"
    local width="${2:-80}"
    local padding=$(( (width - ${#text}) / 2 ))
    printf "%*s%s\n" $padding "" "$text"
}
center "Title" 40

# Escape för regex
escape_regex() {
    printf '%s\n' "$1" | sed 's/[[\.*^$()+?{|]/\\&/g'
}
```

---

## Key Takeaways

1. `${var#pattern}` och `${var%pattern}` för att ta bort prefix/suffix
2. `${var/old/new}` för ersättning, `//` för alla
3. `${var:-default}` för default-värden
4. `[[ $var =~ regex ]]` med `BASH_REMATCH` för capture groups
5. `${var^^}` och `${var,,}` för case conversion
""",
        },
        {
            "title": "Functions & Scope",
            "slug": "functions-and-scope",
            "difficulty": "intermediate",
            "content": """
# Functions & Scope

## Varför behöver du kunna detta?

Utan funktioner blir scripts:

- Svåra att underhålla
- Fulla av duplicerad kod
- Omöjliga att testa
- Oläsbara

Funktioner är grundläggande för bra scripting.

---

## Så fungerar det

Bash-funktioner:

- Defineras med `name() { ... }` eller `function name { ... }`
- Tar argument via `$1`, `$2`, etc.
- Returnerar exit code (inte värden direkt)
- Delar variabler med parent scope (default)

---

## Definiera funktioner

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

---

## Argument

```bash
process_files() {
    echo "Function name: $0"         # INTE funktionsnamnet!
    echo "FUNCNAME: ${FUNCNAME[0]}"  # process_files
    echo "Argument count: $#"
    echo "All arguments: $@"
    echo "First: $1"
    echo "Second: $2"

    # Loopa över argument
    for file in "$@"; do
        echo "Processing: $file"
    done
}

process_files file1.txt file2.txt

# Shift för att processa argument
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

---

## Return och output

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

# Returnera värden via echo + command substitution
get_timestamp() {
    date +%Y%m%d_%H%M%S
}

timestamp=$(get_timestamp)
echo "Timestamp: $timestamp"

# Returnera via global variabel (undvik om möjligt)
get_user_data() {
    RESULT_NAME="John"
    RESULT_AGE=30
}

get_user_data
echo "Name: $RESULT_NAME, Age: $RESULT_AGE"

# Returnera via nameref (Bash 4.3+)
get_data() {
    local -n result=$1               # Nameref
    result="computed value"
}

get_data myvar
echo "$myvar"                        # computed value
```

---

## Scope - local vs global

```bash
# Default: variabler är globala
var="global"

test_scope() {
    var="changed"                    # Ändrar global!
    new_var="new"                    # Skapar global!
}

test_scope
echo "$var"                          # changed
echo "$new_var"                      # new

# local gör variabeln lokal
var="global"

test_local() {
    local var="local"                # Egen kopia
    echo "Inside: $var"              # local
}

test_local
echo "Outside: $var"                 # global (oförändrad)

# VIKTIGT: Alltid använda local!
correct_function() {
    local temp_file
    local result
    local i

    # Nu läcker inget till global scope
}
```

---

## Recursion

```bash
# Rekursiv funktion
factorial() {
    local n=$1
    if (( n <= 1 )); then
        echo 1
    else
        local sub=$(factorial $((n - 1)))
        echo $((n * sub))
    fi
}

echo "5! = $(factorial 5)"           # 120

# Rekursiv directory traversal
find_files() {
    local dir="$1"
    local pattern="$2"

    for item in "$dir"/*; do
        if [[ -d "$item" ]]; then
            find_files "$item" "$pattern"  # Rekursion
        elif [[ -f "$item" && "$item" == *$pattern* ]]; then
            echo "$item"
        fi
    done
}

find_files "/home/user" ".txt"
```

---

## Best practices

```bash
#!/bin/bash

# Dokumentera funktioner
#######################################
# Beskrivning av vad funktionen gör.
# Globals:
#   CONFIG_FILE - läses
# Arguments:
#   $1 - filnamn att processa
# Outputs:
#   Skriver resultat till stdout
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

    # Logik här...
    echo "Processing $file"
}

# Undvik sido-effekter
# DÅLIGT:
bad_function() {
    cd /tmp                          # Ändrar global state!
    result="value"                   # Global variabel!
}

# BRA:
good_function() {
    local result
    result=$(cd /tmp && do_something)  # Subshell, påverkar inte parent
    echo "$result"
}

# Definiera funktioner först, anropa sist
main() {
    local config
    config=$(parse_config)
    process_data "$config"
}

# Helper-funktioner före main
parse_config() { ... }
process_data() { ... }

# Kör main sist
main "$@"
```

---

## Funktion-bibliotek

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

# main.sh
#!/bin/bash
source "$(dirname "$0")/lib/utils.sh"

log_info "Starting script"
[[ -f "$config" ]] || die "Config not found"
```

---

## Key Takeaways

1. Använd `local` för ALLA variabler i funktioner
2. Returnera värden via `echo` + command substitution
3. `return` är för exit code (0=success), inte värden
4. `${FUNCNAME[0]}` för aktuellt funktionsnamn
5. Dokumentera funktioner med kommentarer
""",
        },
        {
            "title": "Input & Output Redirection",
            "slug": "input-output-redirection",
            "difficulty": "intermediate",
            "content": """
# Input & Output Redirection

## Varför behöver du kunna detta?

Allt i Unix är filer och strömmar:

- Logga output
- Läsa konfiguration
- Kombinera kommandon
- Separera felmeddelanden

Redirection är fundamentalt för effektiv scripting.

---

## Så fungerar det

Tre standard-strömmar:

- **stdin (0)** - Standard input
- **stdout (1)** - Standard output
- **stderr (2)** - Standard error

Redirection styr dessa strömmar till/från filer och pipes.

---

## Grundläggande redirection

```bash
# Output till fil
echo "Hello" > file.txt              # Skriv över
echo "World" >> file.txt             # Append

# Input från fil
while read line; do
    echo "Line: $line"
done < file.txt

# Separera stdout och stderr
command > stdout.txt 2> stderr.txt

# Kombinera stdout och stderr
command > all.txt 2>&1               # Traditionell syntax
command &> all.txt                   # Bash kortform

# Tyst körning (discard output)
command > /dev/null                  # Ignorera stdout
command 2> /dev/null                 # Ignorera stderr
command &> /dev/null                 # Ignorera allt
```

---

## File descriptors

```bash
# Öppna egna file descriptors
exec 3> output.txt                   # FD 3 för skrivning
exec 4< input.txt                    # FD 4 för läsning

echo "Data" >&3                      # Skriv till FD 3
read line <&4                        # Läs från FD 4

exec 3>&-                            # Stäng FD 3
exec 4<&-                            # Stäng FD 4

# Läsa och skriva till samma fil
exec 3<> file.txt                    # Read+write

# Duplicera file descriptor
exec 3>&1                            # FD 3 är kopia av stdout
echo "To FD 3" >&3                   # Går till original stdout

# Swap stdout och stderr
command 3>&1 1>&2 2>&3 3>&-
```

---

## Pipes

```bash
# Grundläggande pipe
cat file.txt | grep "error" | wc -l

# Tee - skriv till fil OCH stdout
command | tee output.txt             # Visa + spara
command | tee -a output.txt          # Append

# Process substitution
diff <(ls dir1) <(ls dir2)           # Jämför output som filer

# Läsa process output
while read -r line; do
    echo "Line: $line"
done < <(find . -name "*.txt")

# Named pipes (FIFO)
mkfifo /tmp/mypipe

# Terminal 1:
cat > /tmp/mypipe

# Terminal 2:
cat < /tmp/mypipe

rm /tmp/mypipe
```

---

## Here documents och here strings

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

# Indenterad (med <<-)
cat <<-EOF
	This is indented
	Tabs are removed
EOF

# Here string - enkel sträng som input
grep "pattern" <<< "search in this string"

read -r first second <<< "hello world"
echo "First: $first"                 # hello
echo "Second: $second"               # world
```

---

## Praktiska patterns

```bash
# Logga med timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a script.log
}

# Separata loggfiler för stdout och stderr
{
    command
} > stdout.log 2> stderr.log

# Kör block med redirection
{
    echo "Step 1"
    do_something
    echo "Step 2"
    do_more
} >> execution.log 2>&1

# Läs fil säkert med backup av stdin
exec 3<&0                            # Spara stdin
exec 0< file.txt                     # Läs från fil
while read line; do
    # Processa
    echo "$line"
done
exec 0<&3                            # Återställ stdin
exec 3<&-                            # Stäng backup

# Fånga exit code från pipe
set -o pipefail
false | true
echo $?                              # 1 (inte 0)
```

---

## Avancerad redirection

```bash
# Redirect baserat på villkor
if [[ "$verbose" == true ]]; then
    exec 3>&1                        # Visa output
else
    exec 3>/dev/null                 # Tyst
fi

echo "Info message" >&3

# Fånga stderr separat
{
    output=$(command 2>&1 1>&3)
    exit_code=$?
} 3>&1

echo "stdout went to terminal"
echo "stderr: $output"

# Logga allt scriptet gör
exec > >(tee -a script.log)
exec 2>&1

# Nu loggas allt automatiskt
echo "This is logged"
error_command                        # Fel loggas också

# Läs password utan echo
read -s -p "Password: " password
echo                                 # Newline efter input
```

---

## Key Takeaways

1. `>` skriver över, `>>` appendar
2. `2>&1` kombinerar stderr med stdout
3. `&> file` är kortform för `> file 2>&1`
4. `< <(command)` för process substitution
5. `<<EOF` för here documents, `<<<` för here strings
""",
        },
        {
            "title": "Debugging Bash Scripts",
            "slug": "debugging-bash-scripts",
            "difficulty": "intermediate",
            "content": """
# Debugging Bash Scripts

## Varför behöver du kunna detta?

Bash-scripts kan vara svåra att felsöka:

- Ingen kompilator fångar fel
- Tysta misslyckanden
- Oväntad variabel-expansion
- Subtila syntaxfel

Goda debug-tekniker sparar timmar av frustration.

---

## Så fungerar det

Bash erbjuder flera debug-lägen:

- **-x (xtrace)** - Visa varje kommando
- **-v (verbose)** - Visa varje rad
- **-e (errexit)** - Avsluta vid fel
- **-u (nounset)** - Fel vid odefinierade variabler

Kombinera med loggning och traps för effektiv debugging.

---

## Debug mode med set

```bash
#!/bin/bash

# Aktivera i script
set -x                               # Trace on
# ... kod som ska debuggas ...
set +x                               # Trace off

# Eller vid körning
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

# DEBUG=true ./script.sh             # Kör med debug
```

---

## Trace output

```bash
# Anpassa trace prefix (PS4)
export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]:-main}: '

# Output blir:
# + script.sh:10:main: echo hello
# + script.sh:15:process_file: cat file.txt

# Mer detaljerad
export PS4='+ $(date "+%Y-%m-%d %H:%M:%S") ${BASH_SOURCE}:${LINENO}: '

# Trace till fil (inte terminal)
exec 4>&2                            # Spara stderr
exec 2> debug.log                    # Redirect stderr
set -x
# ... script ...
set +x
exec 2>&4                            # Återställ stderr
```

---

## Breakpoints och pauser

```bash
# Manuell breakpoint
echo "DEBUG: var=$var, state=$state"
read -p "Press enter to continue..."

# Interaktiv debug-funktion
debug() {
    echo "=== DEBUG ===" >&2
    echo "Line: ${BASH_LINENO[0]}" >&2
    echo "Function: ${FUNCNAME[1]:-main}" >&2
    echo "Variables:" >&2
    declare -p "$@" >&2 2>/dev/null || echo "  (none specified)" >&2
    echo "============" >&2
    read -p "Continue? (y/n/s=shell): " response
    case $response in
        n) exit 1 ;;
        s) bash ;;                   # Öppna interaktiv shell
    esac
}

# Användning
process_data() {
    local data="$1"
    debug data                       # Visa $data och pausa
    # ...
}

# Assert-funktion
assert() {
    local condition="$1"
    local message="${2:-Assertion failed}"

    if ! eval "$condition"; then
        echo "ASSERT FAILED: $message" >&2
        echo "  Condition: $condition" >&2
        echo "  Line: ${BASH_LINENO[0]}" >&2
        exit 1
    fi
}

assert '[[ -f "$config" ]]' "Config file must exist"
assert '[[ $count -gt 0 ]]' "Count must be positive"
```

---

## Vanliga fel och lösningar

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
cat $file                            # Fel: cat my file.txt

# Fix: Citera ALLTID
cat "$file"                          # Rätt: cat "my file.txt"

# Fel: Glob expansion
files="*.txt"
echo $files                          # Expanderar!

# Fix: Array eller citera
files=(*.txt)
echo "${files[@]}"

# Fel: Subshell ändrar inte parent
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

---

## Loggning för debugging

```bash
#!/bin/bash

# Logg-nivåer
LOG_LEVEL="${LOG_LEVEL:-INFO}"

log() {
    local level="$1"
    shift

    local levels="DEBUG INFO WARN ERROR"
    local current_level_num=${levels%%$LOG_LEVEL*}
    local msg_level_num=${levels%%$level*}

    if [[ ${#msg_level_num} -ge ${#current_level_num} ]]; then
        echo "[$level] $(date '+%H:%M:%S') $*" >&2
    fi
}

log_debug() { log DEBUG "$@"; }
log_info()  { log INFO "$@"; }
log_warn()  { log WARN "$@"; }
log_error() { log ERROR "$@"; }

# Användning
log_debug "Variable x = $x"          # Bara vid LOG_LEVEL=DEBUG
log_info "Processing started"
log_error "Failed to connect"

# LOG_LEVEL=DEBUG ./script.sh        # Visa allt
```

---

## Trap för debugging

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
    echo "" >&2
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
    # Cleanup
    rm -f /tmp/script_temp_$$
}

trap trap_exit EXIT
```

---

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

# Eller i scriptet:
#!/bin/bash
# shellcheck disable=SC2034          # Ignored: unused variable

# Integrera med VS Code
# Installera "ShellCheck" extension
```

---

## Key Takeaways

1. `set -x` för trace, `set -euo pipefail` för strict mode
2. `PS4` anpassar trace-output (visa fil, rad, funktion)
3. Citera ALLA variabler: `"$var"`, inte `$var`
4. `trap '...' ERR` för stack trace vid fel
5. Använd ShellCheck för statisk analys
""",
        },
        {
            "title": "Working with APIs (curl)",
            "slug": "working-with-apis-curl",
            "difficulty": "intermediate",
            "content": """
# Working with APIs (curl)

## Varför behöver du kunna detta?

DevOps involverar ständig API-interaktion:

- Hälsokontroller
- CI/CD-webhooks
- Cloud provider APIs
- Monitoring och alerting

curl är det universella verktyget för HTTP-kommunikation.

---

## Så fungerar det

curl (Client URL) skickar HTTP-requests:

- Stödjer alla HTTP-metoder
- Hanterar headers, auth, data
- Kan följa redirects
- Stödjer TLS/SSL

jq är partnern för JSON-parsing.

---

## Grundläggande requests

```bash
# GET request
curl https://api.example.com/users

# Med headers
curl -H "Content-Type: application/json" \\
     -H "Accept: application/json" \\
     https://api.example.com/users

# Tysta progress, visa bara response
curl -s https://api.example.com/users

# Visa headers också
curl -i https://api.example.com/users

# Bara headers (HEAD request)
curl -I https://api.example.com/users

# Verbose (debug)
curl -v https://api.example.com/users
```

---

## POST, PUT, DELETE

```bash
# POST med JSON
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d '{"name": "John", "email": "john@example.com"}' \\
     https://api.example.com/users

# POST från fil
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d @data.json \\
     https://api.example.com/users

# PUT (update)
curl -X PUT \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Jane"}' \\
     https://api.example.com/users/123

# PATCH (partial update)
curl -X PATCH \\
     -H "Content-Type: application/json" \\
     -d '{"status": "active"}' \\
     https://api.example.com/users/123

# DELETE
curl -X DELETE https://api.example.com/users/123
```

---

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

---

## Hantera responses

```bash
# Spara response
curl -s https://api.example.com/users > response.json

# Bara HTTP status code
curl -s -o /dev/null -w "%{http_code}" https://api.example.com/health

# Multiple outputs
curl -s -w "\\nStatus: %{http_code}\\nTime: %{time_total}s\\n" \\
     https://api.example.com/users

# Exit code baserat på HTTP status
curl -f https://api.example.com/users || echo "Request failed"

# Timeout
curl -s --connect-timeout 5 --max-time 10 \\
     https://api.example.com/slow-endpoint
```

---

## JSON med jq

```bash
# Installera jq
brew install jq                      # macOS
apt install jq                       # Ubuntu

# Pretty print
curl -s https://api.example.com/users | jq .

# Extrahera fält
curl -s https://api.example.com/users | jq '.[0].name'

# Flera fält
curl -s https://api.example.com/users | jq '.[] | {name, email}'

# Filtrera
curl -s https://api.example.com/users | jq '.[] | select(.active == true)'

# Längd/count
curl -s https://api.example.com/users | jq length

# Raw output (utan citattecken)
name=$(curl -s https://api.example.com/users/1 | jq -r '.name')

# Bygg ny JSON
curl -s https://api.example.com/users | \\
    jq '[.[] | {id, fullname: .name, mail: .email}]'
```

---

## Praktiska patterns

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

# Paginerad API
fetch_all() {
    local base_url="$1"
    local page=1
    local all_data="[]"

    while true; do
        response=$(curl -s "$base_url?page=$page&limit=100")
        count=$(echo "$response" | jq length)

        if (( count == 0 )); then
            break
        fi

        all_data=$(echo "$all_data $response" | jq -s 'add')
        ((page++))
    done

    echo "$all_data"
}

# Webhook
send_webhook() {
    local url="$1"
    local event="$2"
    local data="$3"

    curl -sf -X POST \\
         -H "Content-Type: application/json" \\
         -d "{\\"event\\": \\"$event\\", \\"data\\": $data}" \\
         "$url"
}

send_webhook "$WEBHOOK_URL" "deploy" '{"version": "1.2.3"}'
```

---

## Error handling

```bash
# Robust API call
api_call() {
    local method="$1"
    local url="$2"
    local data="${3:-}"

    local response
    local http_code

    response=$(curl -s -w "\\n%{http_code}" \\
                    -X "$method" \\
                    -H "Content-Type: application/json" \\
                    -H "Authorization: Bearer $TOKEN" \\
                    ${data:+-d "$data"} \\
                    "$url")

    http_code=$(echo "$response" | tail -1)
    response=$(echo "$response" | sed '$d')

    if (( http_code >= 200 && http_code < 300 )); then
        echo "$response"
        return 0
    else
        echo "API Error: HTTP $http_code" >&2
        echo "$response" >&2
        return 1
    fi
}

# Användning
if result=$(api_call GET "https://api.example.com/users"); then
    echo "Got: $result"
else
    echo "Failed to fetch users"
fi
```

---

## Key Takeaways

1. `-s` för silent, `-f` för fail på HTTP errors
2. `-H` för headers, `-d` för data
3. `-w "%{http_code}"` för att få HTTP status
4. `jq -r` för raw output utan citattecken
5. Kombinera curl + jq för kraftfull API-scripting
""",
        },
        {
            "title": "Script Arguments & Options",
            "slug": "script-arguments-options",
            "difficulty": "intermediate",
            "content": """
# Script Arguments & Options

## Varför behöver du kunna detta?

Professionella scripts behöver:

- Flexibla inputs
- Validerande av argument
- Hjälptext
- Konfigurerbarhet

Argument-parsing gör scripts användbara i olika situationer.

---

## Så fungerar det

Bash ger tillgång till argument via:

- `$1`, `$2`, ... - Positionella argument
- `$@` - Alla argument som array
- `$#` - Antal argument
- `$0` - Scriptnamnet

`getopts` och manuell parsing hanterar options.

---

## Positionella argument

```bash
#!/bin/bash

# Grundläggande användning
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

# Default-värden
output="${3:-output.txt}"            # Default om inte given

# Shift för att processa
while [[ $# -gt 0 ]]; do
    echo "Processing: $1"
    shift                            # Ta bort första, flytta alla
done
```

---

## getopts för short options

```bash
#!/bin/bash

# Syntax: getopts "options" variable
# : efter option = kräver argument

usage() {
    echo "Usage: $0 [-v] [-f file] [-n count] source dest"
    echo "  -v          Verbose mode"
    echo "  -f file     Output file"
    echo "  -n count    Number of iterations"
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
        \\?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
        :)
            echo "Option -$OPTARG requires an argument" >&2
            usage
            ;;
    esac
done

# Flytta förbi options till positionella argument
shift $((OPTIND - 1))

# Nu är $1, $2 de resterande argumenten
source="$1"
dest="$2"

[[ -z "$source" || -z "$dest" ]] && usage

echo "Verbose: $verbose"
echo "Output: ${output_file:-stdout}"
echo "Count: $count"
echo "Source: $source"
echo "Dest: $dest"
```

---

## Long options med case

```bash
#!/bin/bash

usage() {
    cat << EOF
Usage: $0 [OPTIONS] <command>

Options:
    -v, --verbose       Enable verbose output
    -f, --file FILE     Specify output file
    -n, --number NUM    Number of iterations (default: 1)
    -h, --help          Show this help message

Commands:
    start               Start the service
    stop                Stop the service
    status              Show service status

Examples:
    $0 --verbose start
    $0 -f output.log -n 5 start
EOF
    exit 1
}

# Defaults
verbose=false
output_file=""
count=1

# Parse arguments
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
        -n|--number)
            count="$2"
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

# Validera command
command="${1:-}"
case $command in
    start|stop|status)
        echo "Running command: $command"
        ;;
    "")
        echo "Error: command required" >&2
        usage
        ;;
    *)
        echo "Unknown command: $command" >&2
        usage
        ;;
esac
```

---

## Argument-validering

```bash
#!/bin/bash

die() {
    echo "Error: $*" >&2
    exit 1
}

# Validera att fil finns
validate_file() {
    local file="$1"
    local description="${2:-file}"

    [[ -z "$file" ]] && die "$description is required"
    [[ ! -f "$file" ]] && die "$description not found: $file"
    [[ ! -r "$file" ]] && die "$description not readable: $file"
}

# Validera nummer
validate_number() {
    local value="$1"
    local name="$2"
    local min="${3:-}"
    local max="${4:-}"

    [[ ! "$value" =~ ^[0-9]+$ ]] && die "$name must be a number"
    [[ -n "$min" && $value -lt $min ]] && die "$name must be >= $min"
    [[ -n "$max" && $value -gt $max ]] && die "$name must be <= $max"
}

# Validera val från lista
validate_choice() {
    local value="$1"
    local name="$2"
    shift 2
    local valid=("$@")

    for choice in "${valid[@]}"; do
        [[ "$value" == "$choice" ]] && return 0
    done

    die "$name must be one of: ${valid[*]}"
}

# Användning
validate_file "$config_file" "Config file"
validate_number "$port" "Port" 1 65535
validate_choice "$env" "Environment" dev staging prod
```

---

## Interaktiv input

```bash
#!/bin/bash

# Enkel prompt
read -p "Enter your name: " name
echo "Hello, $name!"

# Med default
read -p "Enter port [8080]: " port
port="${port:-8080}"

# Password (dold input)
read -s -p "Enter password: " password
echo                                 # Newline efter password

# Ja/Nej
confirm() {
    local message="${1:-Continue?}"
    read -p "$message [y/N]: " response
    [[ "$response" =~ ^[Yy]$ ]]
}

if confirm "Delete all files?"; then
    echo "Deleting..."
else
    echo "Cancelled"
fi

# Välj från lista
select_option() {
    local prompt="$1"
    shift
    local options=("$@")

    PS3="$prompt "
    select choice in "${options[@]}"; do
        if [[ -n "$choice" ]]; then
            echo "$choice"
            return 0
        fi
        echo "Invalid selection" >&2
    done
}

env=$(select_option "Select environment:" dev staging prod)
echo "Selected: $env"

# Timeout på input
if read -t 10 -p "Enter value (10s timeout): " value; then
    echo "Got: $value"
else
    echo "Timeout!"
fi
```

---

## Komplett exempel

```bash
#!/bin/bash
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Defaults
VERBOSE=false
DRY_RUN=false
CONFIG_FILE=""
OUTPUT_DIR="./output"
LOG_LEVEL="info"

usage() {
    cat << EOF
$SCRIPT_NAME - Process data files

Usage: $SCRIPT_NAME [OPTIONS] <input_file>

Options:
    -v, --verbose           Enable verbose output
    -n, --dry-run           Show what would be done
    -c, --config FILE       Configuration file
    -o, --output DIR        Output directory (default: ./output)
    -l, --log-level LEVEL   Log level: debug, info, warn, error
    -h, --help              Show this help

Examples:
    $SCRIPT_NAME data.csv
    $SCRIPT_NAME --verbose --output /tmp data.csv
    $SCRIPT_NAME -c config.yaml -l debug data.csv
EOF
    exit "${1:-0}"
}

log() {
    [[ "$VERBOSE" == true ]] && echo "[INFO] $*"
}

error() {
    echo "[ERROR] $*" >&2
}

die() {
    error "$@"
    exit 1
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -n|--dry-run)
                DRY_RUN=true
                shift
                ;;
            -c|--config)
                [[ -z "${2:-}" ]] && die "Option $1 requires argument"
                CONFIG_FILE="$2"
                shift 2
                ;;
            -o|--output)
                [[ -z "${2:-}" ]] && die "Option $1 requires argument"
                OUTPUT_DIR="$2"
                shift 2
                ;;
            -l|--log-level)
                [[ -z "${2:-}" ]] && die "Option $1 requires argument"
                LOG_LEVEL="$2"
                shift 2
                ;;
            -h|--help)
                usage 0
                ;;
            -*)
                die "Unknown option: $1"
                ;;
            *)
                INPUT_FILE="$1"
                shift
                break
                ;;
        esac
    done

    [[ -z "${INPUT_FILE:-}" ]] && die "Input file required"
    [[ ! -f "$INPUT_FILE" ]] && die "File not found: $INPUT_FILE"
}

main() {
    parse_args "$@"

    log "Input: $INPUT_FILE"
    log "Output: $OUTPUT_DIR"
    log "Config: ${CONFIG_FILE:-none}"
    log "Log level: $LOG_LEVEL"

    if [[ "$DRY_RUN" == true ]]; then
        echo "DRY RUN - would process $INPUT_FILE"
        exit 0
    fi

    # Huvudlogik här...
    echo "Processing $INPUT_FILE..."
}

main "$@"
```

---

## Key Takeaways

1. `getopts` för enkla short options (-v, -f FILE)
2. Manual case-loop för long options (--verbose)
3. `shift` för att flytta argument-position
4. Validera alla inputs före användning
5. Alltid inkludera --help med exempel
""",
        },
        {
            "title": "Cron Jobs & Scheduling",
            "slug": "cron-jobs-scheduling",
            "difficulty": "intermediate",
            "content": """
# Cron Jobs & Scheduling

## Varför behöver du kunna detta?

Automation kräver schemaläggning:

- Backup varje natt
- Log rotation
- Monitoring-checks
- Rapportgenerering

Cron är standard för Unix-schemaläggning.

---

## Så fungerar det

Cron-daemon kör kommandon enligt schema:

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Veckodag (0-7, 0/7 = söndag)
│ │ │ └──── Månad (1-12)
│ │ └────── Dag i månaden (1-31)
│ └──────── Timme (0-23)
└────────── Minut (0-59)
```

Specialtecken:
- `*` = alla värden
- `*/n` = varje n:te
- `n,m` = specifika värden
- `n-m` = intervall

---

## Crontab-hantering

```bash
# Visa crontab
crontab -l

# Redigera crontab
crontab -e

# Installera från fil
crontab mycrontab.txt

# Ta bort alla cron jobs
crontab -r

# Visa annan användares crontab (kräver root)
crontab -u username -l
```

---

## Cron-uttryck

```bash
# Varje minut
* * * * * /path/to/script.sh

# Varje timme (på minuten)
0 * * * * /path/to/script.sh

# Varje dag kl 03:00
0 3 * * * /path/to/script.sh

# Varje måndag kl 09:00
0 9 * * 1 /path/to/script.sh

# Var 5:e minut
*/5 * * * * /path/to/script.sh

# Varje timme mellan 9-17
0 9-17 * * * /path/to/script.sh

# Måndag-fredag kl 08:30
30 8 * * 1-5 /path/to/script.sh

# Första dagen varje månad
0 0 1 * * /path/to/monthly_backup.sh

# Söndag kl 02:00
0 2 * * 0 /path/to/weekly_task.sh

# Flera tider
0 9,12,15,18 * * * /path/to/script.sh
```

---

## Speciella strängar

```bash
# Istället för numeriska uttryck
@reboot     /path/to/script.sh       # Vid systemstart
@yearly     /path/to/script.sh       # 0 0 1 1 *
@annually   /path/to/script.sh       # Samma som @yearly
@monthly    /path/to/script.sh       # 0 0 1 * *
@weekly     /path/to/script.sh       # 0 0 * * 0
@daily      /path/to/script.sh       # 0 0 * * *
@midnight   /path/to/script.sh       # Samma som @daily
@hourly     /path/to/script.sh       # 0 * * * *
```

---

## Environment och paths

```bash
# Cron har minimal environment!
# Sätt viktiga variabler i crontab

SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@example.com

# Eller i scriptet
#!/bin/bash
export PATH="/usr/local/bin:/usr/bin:/bin"

# Eller source profile
#!/bin/bash
source ~/.bash_profile

# Använd ALLTID absoluta paths
0 3 * * * /home/user/scripts/backup.sh

# Inte:
# 0 3 * * * backup.sh                # Funkar inte!
# 0 3 * * * cd /home/user && ./script.sh  # Riskabelt
```

---

## Output och logging

```bash
# Cron skickar output via mail om MAILTO är satt
MAILTO=admin@example.com
0 3 * * * /path/to/backup.sh

# Tysta (ingen output)
0 3 * * * /path/to/backup.sh > /dev/null 2>&1

# Logga till fil
0 3 * * * /path/to/backup.sh >> /var/log/backup.log 2>&1

# Med timestamp
0 3 * * * /path/to/backup.sh 2>&1 | while read line; do echo "$(date): $line"; done >> /var/log/backup.log

# Bättre: logga i scriptet
#!/bin/bash
exec >> /var/log/backup.log 2>&1
echo "=== Backup started: $(date) ==="
# ... backup logic ...
echo "=== Backup completed: $(date) ==="
```

---

## Script best practices

```bash
#!/bin/bash
# /home/user/scripts/backup.sh
#
# Cron-vänligt backup-script
# Körs: 0 3 * * * /home/user/scripts/backup.sh

set -euo pipefail

# Absoluta paths
readonly SCRIPT_DIR="/home/user/scripts"
readonly LOG_FILE="/var/log/backup.log"
readonly BACKUP_DIR="/backup"
readonly LOCK_FILE="/var/run/backup.lock"

# Logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

# Lås för att förhindra parallella körningar
acquire_lock() {
    if ! mkdir "$LOCK_FILE" 2>/dev/null; then
        log "ERROR: Another instance is running"
        exit 1
    fi
    trap 'rm -rf "$LOCK_FILE"' EXIT
}

# Huvudlogik
main() {
    acquire_lock

    log "Backup started"

    if /usr/bin/rsync -av /data/ "$BACKUP_DIR/"; then
        log "Backup completed successfully"
    else
        log "ERROR: Backup failed with exit code $?"
        exit 1
    fi
}

main "$@"
```

---

## Systemd timers (modern alternativ)

```bash
# /etc/systemd/system/backup.service
[Unit]
Description=Daily backup

[Service]
Type=oneshot
ExecStart=/home/user/scripts/backup.sh
User=user

# /etc/systemd/system/backup.timer
[Unit]
Description=Run backup daily

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
systemctl status backup.timer
journalctl -u backup.service
```

---

## Felsökning

```bash
# Testa script manuellt först!
/path/to/script.sh

# Simulera cron-environment
env -i /bin/bash --noprofile --norc -c '/path/to/script.sh'

# Kontrollera cron-loggar
grep CRON /var/log/syslog
journalctl -u cron

# Kontrollera att cron körs
systemctl status cron

# Testa mail-konfiguration
echo "Test" | mail -s "Cron test" admin@example.com

# Vanliga problem:
# 1. PATH inte satt - använd absoluta paths
# 2. Environment saknas - source profile
# 3. Permissions - chmod +x script.sh
# 4. Line endings - dos2unix script.sh
# 5. Fel i crontab-syntax - kontrollera med crontab.guru
```

---

## Key Takeaways

1. Cron-format: minut timme dag månad veckodag
2. Använd ALLTID absoluta paths i cron jobs
3. Logga output: `>> logfile 2>&1`
4. Använd lås för att förhindra parallella körningar
5. Testa scripts manuellt före schemaläggning
""",
        },
        {
            "title": "Configuration Files",
            "slug": "configuration-files",
            "difficulty": "intermediate",
            "content": """
# Configuration Files

## Varför behöver du kunna detta?

Hardkodade värden är:

- Svåra att ändra
- Osäkra (lösenord i kod)
- Miljöspecifika (dev vs prod)

Konfigurationsfiler separerar inställningar från logik.

---

## Så fungerar det

Vanliga format:

- **ENV-filer** - KEY=VALUE
- **INI-filer** - Sektioner med [header]
- **YAML/JSON** - Strukturerad data

Bash kan parsa enkla format direkt.

---

## ENV-filer (.env)

```bash
# .env fil
DATABASE_URL=postgresql://localhost/myapp
REDIS_HOST=localhost
REDIS_PORT=6379
API_KEY=secret123
DEBUG=true

# Ladda i script
#!/bin/bash

# Säker loading (ignorerar kommentarer och tomma rader)
if [[ -f .env ]]; then
    while IFS='=' read -r key value; do
        # Hoppa över kommentarer och tomma rader
        [[ -z "$key" || "$key" =~ ^# ]] && continue
        # Ta bort quotes
        value="${value%\\"}"
        value="${value#\\"}"
        value="${value%\\'}"
        value="${value#\\'}"
        # Exportera
        export "$key=$value"
    done < .env
fi

# Eller enklare (men osäkrare)
set -a                               # Auto-export
source .env
set +a

# Mest robust: dedikerad funktion
load_env() {
    local file="${1:-.env}"

    if [[ ! -f "$file" ]]; then
        echo "Warning: $file not found" >&2
        return 1
    fi

    while IFS= read -r line || [[ -n "$line" ]]; do
        # Hoppa över tomma och kommentarer
        [[ -z "$line" || "$line" =~ ^[[:space:]]*# ]] && continue

        # Extrahera key=value
        if [[ "$line" =~ ^[[:space:]]*([A-Za-z_][A-Za-z0-9_]*)=(.*)$ ]]; then
            local key="${BASH_REMATCH[1]}"
            local value="${BASH_REMATCH[2]}"

            # Ta bort omgivande quotes
            value="${value#[\"\\']}";
            value="${value%[\"\\']}";

            export "$key=$value"
        fi
    done < "$file"
}

load_env .env
load_env .env.local                  # Override
```

---

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
#!/bin/bash

declare -A config

parse_ini() {
    local file="$1"
    local section=""

    while IFS= read -r line; do
        # Ta bort whitespace
        line="${line##*( )}"
        line="${line%%*( )}"

        # Hoppa över tomma och kommentarer
        [[ -z "$line" || "$line" =~ ^[#;] ]] && continue

        # Sektion
        if [[ "$line" =~ ^\\[(.+)\\]$ ]]; then
            section="${BASH_REMATCH[1]}"
            continue
        fi

        # Key = Value
        if [[ "$line" =~ ^([^=]+)=(.*)$ ]]; then
            local key="${BASH_REMATCH[1]}"
            local value="${BASH_REMATCH[2]}"

            # Trim whitespace
            key="${key##*( )}"
            key="${key%%*( )}"
            value="${value##*( )}"
            value="${value%%*( )}"

            config["${section}_${key}"]="$value"
        fi
    done < "$file"
}

parse_ini config.ini

# Användning
echo "DB Host: ${config[database_host]}"
echo "Redis Port: ${config[redis_port]}"
```

---

## YAML med yq

```bash
# config.yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret

features:
  - caching
  - logging
  - monitoring

# Installera yq
brew install yq                      # macOS
snap install yq                      # Ubuntu

# Läsa värden
yq '.database.host' config.yaml      # localhost
yq '.database.port' config.yaml      # 5432
yq '.features[0]' config.yaml        # caching
yq '.features | length' config.yaml  # 3

# I script
db_host=$(yq '.database.host' config.yaml)
db_port=$(yq '.database.port' config.yaml)

# Uppdatera YAML
yq -i '.database.port = 5433' config.yaml

# Merge configs
yq '. * load("overrides.yaml")' config.yaml
```

---

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

# Läsa
jq '.database.host' config.json      # "localhost"
jq -r '.database.host' config.json   # localhost (raw)
jq '.features[0]' config.json        # "caching"

# I script
db_config=$(jq -r '.database | "\\(.host):\\(.port)"' config.json)
echo "Connecting to $db_config"

# Skapa JSON dynamiskt
jq -n \\
    --arg host "$DB_HOST" \\
    --arg port "$DB_PORT" \\
    '{"database": {"host": $host, "port": ($port | tonumber)}}'
```

---

## Hierarkisk konfiguration

```bash
#!/bin/bash
# Ladda config med override-stöd

# Ordning: defaults -> env-specific -> local
load_config() {
    local env="${APP_ENV:-development}"

    # Base config
    if [[ -f config/default.env ]]; then
        source config/default.env
    fi

    # Environment-specifik
    if [[ -f "config/$env.env" ]]; then
        source "config/$env.env"
    fi

    # Lokal override (gitignored)
    if [[ -f config/local.env ]]; then
        source config/local.env
    fi

    # Environment variables har högst prioritet
    # (redan satta överskrider inte)
}

# Eller med defaults i scriptet
DB_HOST="${DB_HOST:-${CONFIG_DB_HOST:-localhost}}"
DB_PORT="${DB_PORT:-${CONFIG_DB_PORT:-5432}}"

# Validera required config
require_config() {
    local var_name="$1"
    local value="${!var_name:-}"

    if [[ -z "$value" ]]; then
        echo "Error: $var_name is required but not set" >&2
        exit 1
    fi
}

require_config DATABASE_URL
require_config API_KEY
```

---

## Secrets-hantering

```bash
# ALDRIG i version control!
# .gitignore:
# *.env.local
# secrets/

# Alternativ 1: Environment variables (CI/CD)
# Sätts i CI/CD-verktyget, inte i filer

# Alternativ 2: Secrets manager
# AWS Secrets Manager
aws secretsmanager get-secret-value \\
    --secret-id myapp/production | \\
    jq -r '.SecretString' > /tmp/secrets.env

# Alternativ 3: HashiCorp Vault
vault kv get -format=json secret/myapp | \\
    jq -r '.data.data | to_entries | .[] | "\\(.key)=\\(.value)"' > /tmp/secrets.env

# Ladda temporärt
source /tmp/secrets.env
rm /tmp/secrets.env                  # Rensa direkt

# Alternativ 4: Docker secrets
# docker-compose.yml
# secrets:
#   db_password:
#     file: ./secrets/db_password.txt

# I script
DB_PASSWORD="$(cat /run/secrets/db_password)"
```

---

## Template-ersättning

```bash
# config.template
DATABASE_URL=postgresql://${DB_USER}:${DB_PASS}@${DB_HOST}/${DB_NAME}
REDIS_URL=redis://${REDIS_HOST}:${REDIS_PORT}

# Generera config
export DB_USER=admin
export DB_PASS=secret
export DB_HOST=localhost
export DB_NAME=myapp
export REDIS_HOST=localhost
export REDIS_PORT=6379

envsubst < config.template > config.env

# Med default-värden
envsubst < config.template | \\
    sed 's/\\$\\$/PLACEHOLDER/g' | \\
    sed 's/\\${[^}]*}/default/g' | \\
    sed 's/PLACEHOLDER/$/g'

# Eller i Bash direkt
while IFS= read -r line; do
    eval echo "\\"$line\\""
done < config.template > config.env
```

---

## Key Takeaways

1. Separera secrets från config (secrets i miljövariabler)
2. Använd hierarkisk loading: defaults -> env -> local
3. `yq` för YAML, `jq` för JSON, `source` för ENV
4. Validera required config vid uppstart
5. Aldrig committa secrets till version control
""",
        },
        {
            "title": "Production Script Patterns",
            "slug": "production-script-patterns",
            "difficulty": "advanced",
            "content": """
# Production Script Patterns

## Varför behöver du kunna detta?

Produktionsscripts måste vara:

- Pålitliga under alla förhållanden
- Säkra mot race conditions
- Återställningsbara vid fel
- Granskningsbara (audit trail)

Mönstren i denna modul är battle-tested i verklig produktion.

---

## Så fungerar det

Produktionskod följer principer:

- **Defensive programming** - Anta att allt kan gå fel
- **Idempotency** - Säkert att köra flera gånger
- **Atomicity** - Allt lyckas eller inget ändras
- **Observability** - Logga allt viktigt

---

## Script template

```bash
#!/bin/bash
#
# script_name.sh - Description of what this script does
#
# Usage: script_name.sh [OPTIONS] <required_arg>
#
# Author: Your Name
# Date: 2024-01-15
# Version: 1.0.0

set -euo pipefail
IFS=$'\\n\\t'

# =============================================================================
# CONFIGURATION
# =============================================================================

readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_VERSION="1.0.0"

# Directories
readonly LOG_DIR="/var/log/myapp"
readonly TMP_DIR="/tmp/myapp_$$"
readonly LOCK_FILE="/var/run/${SCRIPT_NAME}.lock"

# Defaults
VERBOSE=false
DRY_RUN=false
LOG_LEVEL="INFO"

# =============================================================================
# LOGGING
# =============================================================================

declare -A LOG_LEVELS=([DEBUG]=0 [INFO]=1 [WARN]=2 [ERROR]=3)

log() {
    local level="$1"
    shift
    local msg="$*"
    local timestamp
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

    if [[ ${LOG_LEVELS[$level]} -ge ${LOG_LEVELS[$LOG_LEVEL]} ]]; then
        printf "[%s] [%s] [%s] %s\\n" "$timestamp" "$level" "$$" "$msg" >&2
    fi
}

log_debug() { log DEBUG "$@"; }
log_info()  { log INFO "$@"; }
log_warn()  { log WARN "$@"; }
log_error() { log ERROR "$@"; }

# =============================================================================
# ERROR HANDLING
# =============================================================================

die() {
    log_error "$@"
    exit 1
}

trap_handler() {
    local exit_code=$?
    local line_no=$1

    if [[ $exit_code -ne 0 ]]; then
        log_error "Script failed at line $line_no with exit code $exit_code"
        log_error "Last command: $BASH_COMMAND"
    fi

    cleanup
}

trap 'trap_handler $LINENO' EXIT

# =============================================================================
# CLEANUP
# =============================================================================

cleanup() {
    log_debug "Cleaning up..."

    # Ta bort temp-katalog
    if [[ -d "$TMP_DIR" ]]; then
        rm -rf "$TMP_DIR"
    fi

    # Frigör lås
    if [[ -d "$LOCK_FILE" ]]; then
        rmdir "$LOCK_FILE" 2>/dev/null || true
    fi
}

# =============================================================================
# LOCKING
# =============================================================================

acquire_lock() {
    log_debug "Acquiring lock: $LOCK_FILE"

    if ! mkdir "$LOCK_FILE" 2>/dev/null; then
        die "Another instance is already running (lock: $LOCK_FILE)"
    fi

    # Skriv PID till låsfilen för debugging
    echo "$$" > "$LOCK_FILE/pid"
}

# =============================================================================
# UTILITIES
# =============================================================================

require_command() {
    local cmd="$1"
    if ! command -v "$cmd" &>/dev/null; then
        die "Required command not found: $cmd"
    fi
}

require_root() {
    if [[ $EUID -ne 0 ]]; then
        die "This script must be run as root"
    fi
}

confirm() {
    local msg="${1:-Continue?}"
    read -r -p "$msg [y/N]: " response
    [[ "$response" =~ ^[Yy]$ ]]
}

# =============================================================================
# MAIN LOGIC
# =============================================================================

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS] <argument>

Options:
    -v, --verbose       Enable verbose output
    -n, --dry-run       Show what would be done
    -l, --log-level     Set log level (DEBUG, INFO, WARN, ERROR)
    -h, --help          Show this help
    --version           Show version

Examples:
    $SCRIPT_NAME process file.txt
    $SCRIPT_NAME --verbose --dry-run deploy
EOF
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -v|--verbose)
                VERBOSE=true
                LOG_LEVEL="DEBUG"
                shift
                ;;
            -n|--dry-run)
                DRY_RUN=true
                shift
                ;;
            -l|--log-level)
                LOG_LEVEL="${2^^}"
                shift 2
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            --version)
                echo "$SCRIPT_NAME version $SCRIPT_VERSION"
                exit 0
                ;;
            --)
                shift
                break
                ;;
            -*)
                die "Unknown option: $1"
                ;;
            *)
                break
                ;;
        esac
    done

    # Remaining args
    ARGS=("$@")
}

main() {
    parse_args "$@"

    log_info "Starting $SCRIPT_NAME v$SCRIPT_VERSION"
    log_debug "Arguments: ${ARGS[*]:-none}"

    # Prerequisites
    require_command jq
    require_command curl

    # Locking
    acquire_lock

    # Create temp dir
    mkdir -p "$TMP_DIR"

    # Main logic here...
    if [[ "$DRY_RUN" == true ]]; then
        log_info "DRY RUN - no changes made"
    else
        log_info "Processing..."
        # do_work
    fi

    log_info "Completed successfully"
}

main "$@"
```

---

## Idempotent operations

```bash
# Idempotent = säkert att köra flera gånger

# Skapa katalog
mkdir -p /path/to/dir                # OK om finns

# Skapa symlink
ln -sf /source /target               # Force overwrite

# Lägg till rad om den inte finns
grep -qxF 'line' file || echo 'line' >> file

# Lägg till i /etc/hosts
add_host_entry() {
    local ip="$1"
    local hostname="$2"
    local entry="$ip $hostname"

    if ! grep -q "^$ip.*$hostname" /etc/hosts; then
        echo "$entry" >> /etc/hosts
    fi
}

# Installera paket (apt)
ensure_package() {
    local pkg="$1"
    if ! dpkg -l "$pkg" &>/dev/null; then
        apt-get install -y "$pkg"
    fi
}

# Skapa user
ensure_user() {
    local username="$1"
    if ! id "$username" &>/dev/null; then
        useradd -m "$username"
    fi
}
```

---

## Atomic operations

```bash
# Atomic = allt lyckas eller inget ändras

# Atomic file write
atomic_write() {
    local target="$1"
    local content="$2"
    local tmp_file

    tmp_file="$(mktemp "${target}.XXXXXX")"

    # Skriv till temp
    echo "$content" > "$tmp_file"

    # Atomic move (på samma filesystem)
    mv "$tmp_file" "$target"
}

# Atomic config update
update_config() {
    local file="$1"
    local key="$2"
    local value="$3"

    local tmp_file
    tmp_file="$(mktemp)"

    # Modifiera i temp
    sed "s|^$key=.*|$key=$value|" "$file" > "$tmp_file"

    # Validera
    if ! validate_config "$tmp_file"; then
        rm "$tmp_file"
        return 1
    fi

    # Atomic replace
    mv "$tmp_file" "$file"
}

# Transaction pattern
do_transaction() {
    local backup_dir
    backup_dir="$(mktemp -d)"

    # Backup
    cp -r /data "$backup_dir/"

    # Try operations
    if ! {
        operation1 &&
        operation2 &&
        operation3
    }; then
        # Rollback
        log_error "Transaction failed, rolling back"
        rm -rf /data
        mv "$backup_dir/data" /data
        return 1
    fi

    # Cleanup backup
    rm -rf "$backup_dir"
}
```

---

## Retry patterns

```bash
# Exponential backoff
retry_with_backoff() {
    local max_attempts=$1
    shift
    local cmd=("$@")

    local attempt=1
    local wait_time=1

    while (( attempt <= max_attempts )); do
        log_info "Attempt $attempt/$max_attempts: ${cmd[*]}"

        if "${cmd[@]}"; then
            return 0
        fi

        if (( attempt < max_attempts )); then
            log_warn "Failed, retrying in ${wait_time}s..."
            sleep $wait_time
            wait_time=$((wait_time * 2))  # Exponential
        fi

        ((attempt++))
    done

    log_error "All $max_attempts attempts failed"
    return 1
}

# Användning
retry_with_backoff 5 curl -sf http://api.example.com/health

# Circuit breaker
declare -i FAILURE_COUNT=0
readonly FAILURE_THRESHOLD=5
readonly RESET_TIMEOUT=60

circuit_call() {
    local cmd=("$@")

    if (( FAILURE_COUNT >= FAILURE_THRESHOLD )); then
        log_warn "Circuit breaker OPEN - skipping call"
        return 1
    fi

    if "${cmd[@]}"; then
        FAILURE_COUNT=0
        return 0
    else
        ((FAILURE_COUNT++))
        log_warn "Failure count: $FAILURE_COUNT/$FAILURE_THRESHOLD"
        return 1
    fi
}
```

---

## Health checks

```bash
# Omfattande health check
health_check() {
    local failures=0

    # Disk space
    local disk_usage
    disk_usage=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
    if (( disk_usage > 90 )); then
        log_error "Disk usage critical: ${disk_usage}%"
        ((failures++))
    fi

    # Memory
    local mem_available
    mem_available=$(awk '/MemAvailable/ {print $2}' /proc/meminfo)
    if (( mem_available < 1048576 )); then  # < 1GB
        log_error "Low memory: ${mem_available}kB available"
        ((failures++))
    fi

    # Service check
    if ! systemctl is-active --quiet nginx; then
        log_error "nginx is not running"
        ((failures++))
    fi

    # API check
    if ! curl -sf http://localhost:8080/health; then
        log_error "API health check failed"
        ((failures++))
    fi

    if (( failures > 0 )); then
        return 1
    fi

    log_info "All health checks passed"
    return 0
}
```

---

## Key Takeaways

1. Använd template med set -euo pipefail, logging, cleanup
2. Idempotent: säkert att köra flera gånger
3. Atomic: temp-fil + mv för säkra uppdateringar
4. Retry med exponential backoff för nätverksoperationer
5. Lås med mkdir för att förhindra race conditions
""",
        },
        {
            "title": "Bash Mastery Project",
            "slug": "bash-mastery-project",
            "difficulty": "advanced",
            "content": """
# Bash Mastery Project

## Varför behöver du kunna detta?

Detta projekt integrerar ALLT du lärt dig:

- Script-struktur och best practices
- Error handling och logging
- API-integration
- Konfigurationshantering
- Produktionsmönster

Bygg ett komplett DevOps-verktyg.

---

## Projektöversikt

Bygg ett **Deployment Automation Tool** som:

1. Läser konfiguration
2. Validerar environment
3. Kör health checks
4. Utför deploy med rollback
5. Notifierar via webhook

---

## Del 1: Struktur

```bash
deploy-tool/
├── bin/
│   └── deploy                       # Huvudscript
├── lib/
│   ├── config.sh                    # Konfigurationshantering
│   ├── logging.sh                   # Loggfunktioner
│   ├── health.sh                    # Health checks
│   ├── deploy.sh                    # Deploy-logik
│   └── notify.sh                    # Notifikationer
├── config/
│   ├── default.env                  # Defaults
│   ├── production.env               # Prod config
│   └── staging.env                  # Staging config
├── templates/
│   └── notify.json                  # Webhook template
└── tests/
    └── test_deploy.sh               # Tester
```

---

## Del 2: Logging library

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

---

## Del 3: Config library

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
    _source_env "$config_dir/local.env"  # Gitignored

    # Validera required
    _require_config APP_NAME
    _require_config DEPLOY_HOST
    _require_config DEPLOY_PATH
    _require_config HEALTH_URL
}

_source_env() {
    local file="$1"
    if [[ -f "$file" ]]; then
        log_debug "Loading config: $file"
        while IFS='=' read -r key value; do
            [[ -z "$key" || "$key" =~ ^# ]] && continue
            value="${value%\\"}"
            value="${value#\\"}"
            CONFIG[$key]="$value"
            export "$key=$value"
        done < "$file"
    fi
}

_require_config() {
    local key="$1"
    if [[ -z "${CONFIG[$key]:-}" ]]; then
        die "Required config missing: $key"
    fi
}

get_config() {
    local key="$1"
    local default="${2:-}"
    echo "${CONFIG[$key]:-$default}"
}
```

---

## Del 4: Health check library

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
    return 0
}

health_check_disk() {
    local threshold="${DISK_THRESHOLD:-90}"
    local usage
    usage=$(df -h "${DEPLOY_PATH}" | awk 'NR==2 {print $5}' | tr -d '%')

    if (( usage > threshold )); then
        log_error "Disk usage too high: ${usage}% > ${threshold}%"
        return 1
    fi

    log_debug "Disk usage OK: ${usage}%"
    return 0
}

health_check_memory() {
    local threshold="${MEMORY_THRESHOLD:-1048576}"  # 1GB in KB
    local available
    available=$(awk '/MemAvailable/ {print $2}' /proc/meminfo 2>/dev/null || echo "0")

    if (( available < threshold )); then
        log_error "Low memory: ${available}KB available"
        return 1
    fi

    log_debug "Memory OK: ${available}KB available"
    return 0
}

health_check_app() {
    local url="${HEALTH_URL}"
    local timeout="${HEALTH_TIMEOUT:-10}"

    if curl -sf --max-time "$timeout" "$url" > /dev/null; then
        log_debug "App health OK"
        return 0
    fi

    log_error "App health check failed: $url"
    return 1
}
```

---

## Del 5: Deploy library

```bash
#!/bin/bash
# lib/deploy.sh

deploy() {
    local version="$1"
    local backup_path

    log_info "Deploying version: $version"

    # Pre-flight checks
    pre_deploy_checks || return 1

    # Backup
    backup_path=$(create_backup) || return 1
    log_info "Backup created: $backup_path"

    # Deploy
    if ! do_deploy "$version"; then
        log_error "Deploy failed, rolling back..."
        rollback "$backup_path"
        return 1
    fi

    # Post-deploy validation
    if ! post_deploy_check; then
        log_error "Post-deploy check failed, rolling back..."
        rollback "$backup_path"
        return 1
    fi

    log_info "Deploy completed successfully"
    cleanup_old_backups
    return 0
}

pre_deploy_checks() {
    log_info "Running pre-deploy checks..."

    # Kontrollera att host är nåbar
    if ! ssh -o ConnectTimeout=5 "$DEPLOY_HOST" "echo ok" &>/dev/null; then
        log_error "Cannot connect to deploy host"
        return 1
    fi

    # Kontrollera diskutrymme
    health_check_disk || return 1

    return 0
}

create_backup() {
    local timestamp
    timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_path="${BACKUP_DIR:-/backup}/${APP_NAME}_${timestamp}"

    log_debug "Creating backup: $backup_path"

    ssh "$DEPLOY_HOST" "cp -r '$DEPLOY_PATH' '$backup_path'" || return 1

    echo "$backup_path"
}

do_deploy() {
    local version="$1"
    local artifact="${ARTIFACT_URL}/${version}.tar.gz"

    log_debug "Downloading: $artifact"

    ssh "$DEPLOY_HOST" "
        cd '$DEPLOY_PATH' &&
        curl -sfL '$artifact' | tar xz &&
        ./scripts/post-deploy.sh
    "
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

    log_info "Waiting for app to be healthy..."

    for ((i=1; i<=retries; i++)); do
        sleep "$wait"

        if health_check_app; then
            return 0
        fi

        log_debug "Health check attempt $i/$retries failed"
    done

    return 1
}

cleanup_old_backups() {
    local keep="${BACKUP_KEEP:-5}"

    log_debug "Cleaning up old backups, keeping last $keep"

    ssh "$DEPLOY_HOST" "
        ls -t '${BACKUP_DIR:-/backup}/${APP_NAME}_'* 2>/dev/null |
        tail -n +$((keep+1)) |
        xargs rm -rf
    " 2>/dev/null || true
}
```

---

## Del 6: Huvudscript

```bash
#!/bin/bash
# bin/deploy

set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ladda libraries
source "$SCRIPT_DIR/../lib/logging.sh"
source "$SCRIPT_DIR/../lib/config.sh"
source "$SCRIPT_DIR/../lib/health.sh"
source "$SCRIPT_DIR/../lib/deploy.sh"
source "$SCRIPT_DIR/../lib/notify.sh"

usage() {
    cat << EOF
Usage: deploy [OPTIONS] <command> [args]

Commands:
    deploy <version>    Deploy a version
    rollback <backup>   Rollback to backup
    health              Run health checks
    status              Show current status

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

    # Parse global options
    while [[ $# -gt 0 ]]; do
        case $1 in
            -e|--env)     env="$2"; shift 2 ;;
            -n|--dry-run) dry_run=true; shift ;;
            -v|--verbose) LOG_LEVEL=DEBUG; shift ;;
            -h|--help)    usage; exit 0 ;;
            -*)           die "Unknown option: $1" ;;
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

            if [[ "$dry_run" == true ]]; then
                log_info "DRY RUN: Would deploy $version"
                exit 0
            fi

            deploy "$version"
            notify_deploy "$version" "success"
            ;;

        rollback)
            local backup="${1:?Backup path required}"
            rollback "$backup"
            ;;

        health)
            health_check_all
            ;;

        status)
            echo "Environment: $DEPLOY_ENV"
            echo "App: $APP_NAME"
            echo "Host: $DEPLOY_HOST"
            health_check_all && echo "Status: healthy" || echo "Status: unhealthy"
            ;;

        *)
            usage
            exit 1
            ;;
    esac
}

main "$@"
```

---

## Key Takeaways

1. Separera logik i libraries för återanvändning
2. Atomic deploy med backup och rollback
3. Health checks före och efter deploy
4. Notifiering vid success/failure
5. Strukturerad logging för debugging och audit
""",
        },
    ],
}
