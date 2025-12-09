# =============================================================================
# BASH MASTERY V3 - BLOCK 2 PART 1: VARIABLES & ARRAYS
# Noder 5-6 av 20 | Premium Bootcamp-kvalitet
# =============================================================================

NODE_5 = {
    "id": "bash_node_5",
    "title": "Variables - From Basic to Advanced",
    "slug": "variables-from-basic-to-advanced",
    "order_index": 5,
    "estimated_minutes": 50,
    "xp_reward": 100,
    "difficulty": "medium",
    "content": r'''# Variables - From Basic to Advanced

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Variabler ar grundbulten i all programmering. I Bash har variabler unika egenskaper som skiljer sig fran andra sprak. Att beharska variabelhantering ar avgörande for robusta DevOps-skript.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Variables ar viktigt |
|----------|----------------------------|
| **Konfiguration** | Miljöspecifika varden (dev/staging/prod) |
| **Dynamiska varden** | Hantera output fran kommandon |
| **Parametrisering** | Återanvandbara skript med argument |
| **Environment** | Kontrollera applikationers beteende |
| **Templating** | Generera konfigurationsfiler |

Du maste forsta:

- **Bash ar otypat** - Allt ar strangar (men kan behandlas som tal)
- **Scope ar viktigt** - Lokala vs globala vs environment variabler
- **Expansion** - Bash har kraftfulla variabel-expansions-features

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Grundlaggande Variabler

```bash
# Tilldelning - INGA SPACES runt =
name="DevOps Engineer"           # Korrekt
name = "value"                   # FEL! Bash tolkar som kommando

# Anvandning - $ prefix
echo $name                       # Funkar
echo "$name"                     # Battre - skyddar mot word splitting
echo "${name}"                   # Bast - tydligt var variabeln slutar

# Viktigt: ${} syntax
version=2
echo "$versiontest"              # FEL: Letar efter $versiontest
echo "${version}test"            # Ratt: 2test

# Radera variabel
unset name

# Kontrollera om satt
if [ -n "$name" ]; then
    echo "name is set to: $name"
fi
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Variabeltyper och Scope

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      VARIABEL SCOPE I BASH                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                    ENVIRONMENT VARIABLES                         │    │
│  │                 Synliga for alla child processes                 │    │
│  │                    export VAR="value"                            │    │
│  │  ┌─────────────────────────────────────────────────────────┐    │    │
│  │  │                  SHELL VARIABLES                         │    │    │
│  │  │              Endast i nuvarande shell                    │    │    │
│  │  │                  VAR="value"                             │    │    │
│  │  │  ┌─────────────────────────────────────────────────┐    │    │    │
│  │  │  │              LOCAL VARIABLES                     │    │    │    │
│  │  │  │          Endast i nuvarande funktion            │    │    │    │
│  │  │  │              local var="value"                  │    │    │    │
│  │  │  └─────────────────────────────────────────────────┘    │    │    │
│  │  └─────────────────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

```bash
# Shell variable - endast i nuvarande shell
MY_VAR="hello"
bash -c 'echo $MY_VAR'          # Tom! Inte exporterad

# Environment variable - synlig for child processes
export MY_VAR="hello"
bash -c 'echo $MY_VAR'          # Output: hello

# Eller direkt vid skapande
export DATABASE_URL="postgres://localhost/db"

# Temporar environment for ett kommando
DATABASE=prod ./deploy.sh       # DATABASE=prod endast for deploy.sh

# Local i funktion
my_function() {
    local count=0                # Endast synlig i funktionen
    count=$((count + 1))
    echo $count
}

# Se alla environment variables
env
printenv

# Se alla variabler (inklusive shell vars)
set
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Speciella Variabler

| Variabel | Beskrivning | Exempel |
|----------|-------------|---------|
| `$0` | Skriptets namn | `./deploy.sh` |
| `$1-$9` | Argument 1-9 | `$1` = forsta arg |
| `${10}` | Argument 10+ | Kraver {} |
| `$#` | Antal argument | `if [ $# -lt 2 ]` |
| `$@` | Alla argument (separat) | `for arg in "$@"` |
| `$*` | Alla argument (en strang) | Anvand sallan |
| `$?` | Exit status fran senaste | `if [ $? -eq 0 ]` |
| `$$` | Nuvarande process PID | Temp-filer: `/tmp/$$` |
| `$!` | Senaste bakgrundsprocess PID | `wait $!` |
| `$_` | Senaste argumentet | |

```bash
#!/bin/bash
# argtest.sh - Demonstrera speciella variabler

echo "Script name: $0"
echo "First arg: $1"
echo "Second arg: $2"
echo "All args: $@"
echo "Number of args: $#"
echo "Process ID: $$"

# Loopa igenom alla argument
for arg in "$@"; do
    echo "Argument: $arg"
done

# Exit status
ls /nonexistent 2>/dev/null
echo "ls exit status: $?"        # 2 (fil finns ej)

ls /tmp
echo "ls exit status: $?"        # 0 (success)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Parameter Expansion

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PARAMETER EXPANSION                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  SYNTAX              │ BESKRIVNING                │ EXEMPEL             │
│  ────────────────────┼────────────────────────────┼───────────────────  │
│  ${var:-default}     │ Default om unset/tom       │ ${NAME:-guest}      │
│  ${var:=default}     │ Set och returnera default  │ ${NAME:=guest}      │
│  ${var:+value}       │ Value om VAR ar satt       │ ${DEBUG:+"-v"}      │
│  ${var:?error}       │ Error om unset/tom         │ ${DB:?required}     │
│  ────────────────────┼────────────────────────────┼───────────────────  │
│  ${#var}             │ Langd                      │ ${#name} → 5        │
│  ${var^}             │ Forsta till uppercase      │ ${name^} → Hello    │
│  ${var^^}            │ Allt till uppercase        │ ${name^^} → HELLO   │
│  ${var,}             │ Forsta till lowercase      │ ${name,} → hELLO    │
│  ${var,,}            │ Allt till lowercase        │ ${name,,} → hello   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

```bash
# Default values
NAME=${1:-"Anonymous"}          # Om $1 saknas, anvand Anonymous
DB_PORT=${DB_PORT:-5432}        # Default port om ej satt
CONFIG=${CONFIG:=/etc/app.conf} # Set OCH returnera default

# Krav pa variabel
DB_HOST=${DB_HOST:?Database host must be set}

# Alternativ om satt (bra for flaggor)
VERBOSE=""
./script.sh ${VERBOSE:+"-v"}    # Tom om VERBOSE ej satt

# String manipulation
filename="document.tar.gz"
echo ${filename%.gz}            # document.tar (ta bort .gz)
echo ${filename%.*}             # document.tar (ta bort sista extension)
echo ${filename%%.*}            # document (ta bort alla extensions)
echo ${filename#*.}             # tar.gz (ta bort fore forsta .)
echo ${filename##*.}            # gz (ta bort fore sista .)

# Substrings
text="Hello World"
echo ${text:0:5}                # Hello (fran pos 0, 5 tecken)
echo ${text:6}                  # World (fran pos 6 till slut)
echo ${text: -5}                # World (sista 5, notera space)

# Ersattning
path="/home/user/docs"
echo ${path/user/admin}         # /home/admin/docs (forsta)
echo ${path//o/0}               # /h0me/user/d0cs (alla)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska Exempel

```bash
#!/bin/bash
# deploy.sh - Praktisk variabelanvandning

# Required variables med error
DB_HOST=${DB_HOST:?Error: DB_HOST must be set}
DB_USER=${DB_USER:?Error: DB_USER must be set}

# Optional med defaults
DB_PORT=${DB_PORT:-5432}
DB_NAME=${DB_NAME:-production}
LOG_LEVEL=${LOG_LEVEL:-info}

# Dynamiska varden
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_${TIMESTAMP}.sql"
HOSTNAME=$(hostname)

# Bygga connection string
CONNECTION="postgresql://${DB_USER}@${DB_HOST}:${DB_PORT}/${DB_NAME}"

echo "Deploying to $HOSTNAME"
echo "Database: $CONNECTION"
echo "Backup file: $BACKUP_FILE"

# Conditional flags
DEBUG=""
[[ $LOG_LEVEL == "debug" ]] && DEBUG="-v"
./run.sh $DEBUG
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Expansion | Beskrivning |
|-----------|-------------|
| `${var:-default}` | Default om tom |
| `${var:=default}` | Set och default |
| `${var:+alt}` | Alt om satt |
| `${var:?msg}` | Error om tom |
| `${#var}` | Langd |
| `${var%pattern}` | Ta bort fran slutet |
| `${var#pattern}` | Ta bort fran borjan |
| `${var/old/new}` | Ersatt forsta |
| `${var//old/new}` | Ersatt alla |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| `command not found` | Space runt = | `var="value"` ej `var = "value"` |
| Tom variabel | Ej exporterad | `export VAR` for child processes |
| Ovaentat varde | Globbing | Quotera: `"$var"` |
| `bad substitution` | Felaktig syntax | Kontrollera ${} syntax |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **Inga spaces** | `var="value"` inte `var = "value"` |
| **Quotera alltid** | `"$var"` for sakerhets skull |
| **${} for tydlighet** | `${var}text` inte `$vartext` |
| **export for children** | Child processes ser endast exporterade |
| **Parameter expansion** | Kraftfull string manipulation |

**Kom ihag:**

- Anvand default values for robusta skript
- export for miljovariabler som behover arvas
- local i funktioner for att undvika sidoeffekter
- ${var:?error} for att tvinga kravda variabler
''',
}

NODE_6 = {
    "id": "bash_node_6",
    "title": "Arrays - Indexed and Associative",
    "slug": "arrays-indexed-and-associative",
    "order_index": 6,
    "estimated_minutes": 50,
    "xp_reward": 100,
    "difficulty": "medium",
    "content": r'''# Arrays - Indexed and Associative

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bash stodjer bade indexerade och associativa arrays. Dessa datastrukturer ar ovardliga for att hantera listor av servrar, konfigurationer, och komplexa data i DevOps-automation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Varfor viktigt for DevOps?

| Scenario | Varfor Arrays ar viktigt |
|----------|-------------------------|
| **Serverlistor** | Hantera multipla hosts for deployment |
| **Konfigurationsdata** | Lagra key-value pars |
| **Batch-operationer** | Iterera over filer, services, etc |
| **Argument-hantering** | Bearbeta multipla inputs |
| **Datastrukturer** | Organisera komplex information |

Du maste forsta:

- **Indexed arrays** - Numeriska index, borjar fran 0
- **Associative arrays** - Key-value pairs (Bash 4+)
- **Sparse arrays** - Index behover ej vara konsekutiva

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Indexed Arrays

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      INDEXED ARRAY STRUKTUR                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  servers=("web1" "web2" "db1" "db2")                                    │
│                                                                          │
│  Index:    [0]     [1]     [2]     [3]                                  │
│  Value:   "web1"  "web2"  "db1"   "db2"                                 │
│                                                                          │
│  ${servers[0]}    → web1                                                │
│  ${servers[@]}    → web1 web2 db1 db2 (alla element)                    │
│  ${#servers[@]}   → 4 (antal element)                                   │
│  ${!servers[@]}   → 0 1 2 3 (alla index)                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

```bash
# Skapa indexed array
servers=("web1" "web2" "db1" "db2")

# Alternativa satt att skapa
declare -a servers                    # Tom array
servers[0]="web1"
servers[1]="web2"

# Fran kommando-output
files=($(ls *.txt))                   # OBS: Problem med spaces
readarray -t files < <(ls *.txt)      # Battre satt

# Accessa element
echo ${servers[0]}                    # Forsta element
echo ${servers[-1]}                   # Sista element (Bash 4.3+)
echo ${servers[@]}                    # Alla element
echo ${servers[*]}                    # Alla som en strang

# Array langd
echo ${#servers[@]}                   # Antal element
echo ${#servers[0]}                   # Langd av forsta elementet

# Alla index
echo ${!servers[@]}                   # 0 1 2 3

# Slice
echo ${servers[@]:1:2}                # Element 1-2 (web2 db1)
echo ${servers[@]:2}                  # Fran index 2 till slut
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Array Manipulation

```bash
# Lagg till element
servers+=("cache1")                   # Lagg till i slutet
servers+=("cache2" "cache3")          # Lagg till flera

# Ta bort element
unset servers[1]                      # Ta bort index 1 (sparse!)
servers=("${servers[@]}")             # Re-index array

# Ersatt element
servers[0]="newweb1"

# Kopiera array
backup=("${servers[@]}")

# Konkatenera arrays
all_hosts=("${servers[@]}" "${databases[@]}")

# Sortera array (kraver mapfile/readarray)
sorted=($(printf '%s\n' "${servers[@]}" | sort))
# Eller sakrare:
readarray -t sorted < <(printf '%s\n' "${servers[@]}" | sort)

# Filtrera array
web_servers=()
for s in "${servers[@]}"; do
    [[ $s == web* ]] && web_servers+=("$s")
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Iterera Over Arrays

```bash
# Iterera over varden
for server in "${servers[@]}"; do
    echo "Deploying to $server"
    ssh "$server" "systemctl restart app"
done

# VIKTIGT: Anvand "${array[@]}" med quotes!
# Utan quotes: "web 1" blir tva separata varden

# Iterera med index
for i in "${!servers[@]}"; do
    echo "Server $i: ${servers[$i]}"
done

# While-loop med readarray
while IFS= read -r line; do
    servers+=("$line")
done < servers.txt

# Process substitution
while IFS= read -r line; do
    echo "Processing: $line"
done < <(kubectl get pods -o name)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Associative Arrays (Bash 4+)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ASSOCIATIVE ARRAY STRUKTUR                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  declare -A config                                                      │
│  config=([host]="localhost" [port]="5432" [db]="mydb")                 │
│                                                                          │
│  Key:       [host]        [port]      [db]                              │
│  Value:  "localhost"     "5432"     "mydb"                              │
│                                                                          │
│  ${config[host]}     → localhost                                        │
│  ${config[@]}        → localhost 5432 mydb (alla varden)               │
│  ${!config[@]}       → host port db (alla nycklar)                     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

```bash
# Deklarera associative array (KRÄVS!)
declare -A config

# Tilldela varden
config[host]="localhost"
config[port]="5432"
config[database]="production"

# Eller allt pa en gang
declare -A config=(
    [host]="localhost"
    [port]="5432"
    [database]="production"
    [user]="admin"
)

# Accessa varden
echo ${config[host]}              # localhost
echo ${config[@]}                 # Alla varden
echo ${!config[@]}                # Alla nycklar

# Kontrollera om nyckel finns
if [[ -v config[host] ]]; then
    echo "host is set"
fi

# Iterera over associative array
for key in "${!config[@]}"; do
    echo "$key = ${config[$key]}"
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Praktiska DevOps-Exempel

```bash
#!/bin/bash
# deploy_multi.sh - Deploy till flera servrar

declare -A environments=(
    [dev]="dev-server-01.local"
    [staging]="staging-server-01.company.com"
    [prod]="prod-server-01.company.com"
)

declare -a deploy_order=("dev" "staging" "prod")

# Hjalp-funktion
deploy_to() {
    local env=$1
    local server=${environments[$env]}

    echo "Deploying to $env ($server)..."
    ssh "$server" "cd /app && git pull && systemctl restart app"

    if [[ $? -eq 0 ]]; then
        echo "✓ $env deployment successful"
        return 0
    else
        echo "✗ $env deployment failed"
        return 1
    fi
}

# Deploy i ordning
for env in "${deploy_order[@]}"; do
    deploy_to "$env" || {
        echo "Stopping deployment pipeline"
        exit 1
    }
done

echo "All deployments complete!"
```

```bash
#!/bin/bash
# Server inventory med arrays

declare -A server_info

# Las serverinfo fran fil
while IFS='=' read -r key value; do
    server_info[$key]=$value
done < server.conf

# Eller har kodad data
declare -A services=(
    [nginx]="80,443"
    [postgresql]="5432"
    [redis]="6379"
    [app]="8080"
)

# Health check alla services
for service in "${!services[@]}"; do
    ports=${services[$service]}
    echo "Checking $service on ports: $ports"

    IFS=',' read -ra port_array <<< "$ports"
    for port in "${port_array[@]}"; do
        nc -z localhost "$port" && echo "  Port $port: OK" || echo "  Port $port: FAIL"
    done
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Readarray / Mapfile

```bash
# Las fil till array
readarray -t lines < file.txt
# Eller
mapfile -t lines < file.txt

# Las fran kommando
readarray -t pods < <(kubectl get pods -o name)

# Med callback for varje rad
readarray -t -C 'process_line' -c 1 lines < file.txt

# Praktiskt exempel
readarray -t servers < servers.txt
echo "Loaded ${#servers[@]} servers"

for server in "${servers[@]}"; do
    ping -c 1 "$server" > /dev/null && echo "$server: UP" || echo "$server: DOWN"
done
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Snabbreferens

| Syntax | Beskrivning |
|--------|-------------|
| `arr=()` | Tom indexed array |
| `declare -A arr` | Skapa associative array |
| `${arr[@]}` | Alla element |
| `${!arr[@]}` | Alla index/nycklar |
| `${#arr[@]}` | Antal element |
| `arr+=("val")` | Lagg till element |
| `unset arr[i]` | Ta bort element |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| Endast forsta element | Saknar [@] | `"${arr[@]}"` inte `"$arr"` |
| Word splitting | Saknar quotes | `"${arr[@]}"` inte `${arr[@]}` |
| `declare: -A: invalid option` | Bash < 4 | Uppgradera Bash |
| Forlorade element | Spaces i varden | Anvand quotes vid tilldelning |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Key Takeaways

| Koncept | Detalj |
|---------|--------|
| **"${arr[@]}"** | Alltid med quotes och @ |
| **declare -A** | Kravs for associative arrays |
| **readarray** | Sakraste sattet att fylla array |
| **${!arr[@]}** | Alla nycklar/index |
| **Bash 4+** | Associative arrays kräver modern Bash |

**Kom ihag:**

- Quotera alltid array expansions: "${arr[@]}"
- declare -A maste anges fore associative arrays
- Arrays ar 0-indexerade
- readarray/mapfile for att lasa fran filer
- Kontrollera Bash-version om associative arrays behövs
''',
}

BLOCK_2_PART_1_NODES = [NODE_5, NODE_6]
