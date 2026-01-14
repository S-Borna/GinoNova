"""
NOD: Grundkurs i Bash-skriptprogrammering
=========================================
Skapa robusta bash-skript med korrekt struktur, variabelhantering, argument, flödeskontroll och felhantering
"""

BASH_SKRIPT_NODE = {
    "title": "Grundkurs i Bash-skriptprogrammering",
    "slug": "bash-skript",
    "description": "Skapa robusta bash-skript med korrekt struktur, variabelhantering, argument, flödeskontroll och felhantering",
    "difficulty": "medium",
    "estimated_minutes": 70,
    "xp_reward": 140,
    "order_index": 6,
    "content": r"""# Grundkurs i Bash-skriptprogrammering

Tematiskt fokus: Automatisering och skriptning

## Grundläggande mall: Initialisera skript korrekt

Ett välskrivet bash-skript initieras alltid med en standardmall som säkerställer säker exekvering:

```bash
#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
```

### Shebang-deklarationen (#!)

**Shebang**-raden (även kallad hashbang) instruerar operativsystemet om vilken interpretator som ska köra skriptet.

```bash
#!/bin/bash              # Använder bash
#!/usr/bin/env bash      # Plattformsoberoende - lokaliserar bash via PATH
#!/bin/sh                # POSIX sh (bred kompatibilitet men färre funktioner)
#!/usr/bin/env python3   # För Python-baserade skript
```

**Notera**: Denna rad måste alltid placeras som den ALLRA FÖRSTA raden i skriptfilen.

### Set-kommandots optioner

`set -euo pipefail` etablerar en säker exekveringsmiljö genom tre kritiska flaggor:

```bash
set -e    # Terminera skriptet omedelbart vid fel (kommando returnerar non-zero)
set -u    # Terminera vid försök att använda odefinierade variabler
set -o pipefail  # En pipeline returnerar felkod om NÅGOT kommando i kedjan misslyckas
```

**Individuell förklaring**:

```bash
# -e: Terminera vid kommandofel
set -e
ls /finns/inte   # Exekveringen stoppas här och skriptet avslutas
echo "Detta kommer aldrig att köras"

# -u: Terminera vid referens till odefinerad variabel
set -u
echo "$INTE_DEFINIERAD"  # Genererar fel och terminerar
# Lösning: definiera fallback-värde
echo "${INTE_DEFINIERAD:-fallback}"

# -o pipefail: Pipeline använder felkod från första misslyckade kommandot
false | true  # Utan pipefail: returnerar exit 0
# Med pipefail: returnerar exit 1
```

### IFS (Internal Field Separator)

IFS kontrollerar hur bash delar upp textsträngar i fält.

```bash
# Standard IFS = mellanslag, tab, newline
IFS=$'\n\t'  # Endast newline och tab - säkrare för filnamn med mellanslag
```

**Syfte**: Förhindrar oavsiktlig uppdelning av filnamn som innehåller mellanslag.

### Komplett standardmall med kommentarer

```bash
#!/usr/bin/env bash
#
# Beskrivning: [Beskriv vad skriptet gör]
# Användning: ./skript.sh [argument]
#

set -euo pipefail  # Strikt felkontroll
IFS=$'\n\t'        # Säker textuppdelning

# Dina kommandon placeras här...
```

## Variabler och Export

### Variabeldeklaration

I bash får det INTE finnas mellanslag runt likhetstecknet vid variabeltilldelning:

```bash
# Korrekt syntax
namn="Anna"
ålder=30
sökväg="/home/användare"

# FELAKTIGT - orsakar syntaxfel
namn = "Anna"
```

### Läsa av variabler

```bash
echo $namn
echo ${namn}       # Identiskt men mer explicit
echo "${namn}"     # Bästa praxis - skyddar mot word splitting
```

### Variabelexpansion och manipulering

```bash
# Standardvärden
echo "${VAR:-standard}"      # Använder "standard" om VAR är odefinierad/tom
echo "${VAR:=standard}"      # Som ovan, men tilldelar även VAR värdet "standard"
echo "${VAR:?felmeddelande}" # Terminerar med fel om VAR är odefinierad/tom

# Stränglängd
namn="hejsan"
echo "${#namn}"              # 6

# Delsträngar (substring)
text="hej världen"
echo "${text:0:3}"           # hej
echo "${text:4}"             # världen

# Mönsterersättning
filnamn="dokument.txt"
echo "${filnamn%.txt}"       # dokument (tar bort .txt från slutet)
echo "${filnamn##*.}"        # txt (extraherar filändelse)
```

### Export-funktionalitet

`export` gör en variabel tillgänglig för alla underprocesser:

```bash
# Endast synlig i aktuell shell
namn="Anna"

# Tillgänglig för alla subprocesser
export PATH="/egen/bin:$PATH"

# Deklarera och exportera i ett steg
export API_NYCKEL="hemlig123"

# Visa alla exporterade variabler
export -p

# Ta bort export-status
export -n namn
```

**Kritiskt**: Utan export kan subprocesser inte se variabeln:

```bash
min_var="hej"
bash -c 'echo $min_var'  # Tom output - min_var är inte exporterad

export min_var="hej"
bash -c 'echo $min_var'  # hej
```

## Argument: Använd $0, $1-$9, $#, $@ i skript

Bash tillhandahåller tillgång till skriptargument genom speciella variabler:

```bash
#!/bin/bash
# Spara som: test.sh

echo "Skriptnamn: $0"        # ./test.sh
echo "Första arg: $1"        # Första argumentet
echo "Andra arg: $2"         # Andra argumentet
echo "Totalt antal args: $#" # Antal argument
echo "Alla args: $@"         # Alla argument som enskilda ord
echo "Alla args: $*"         # Alla argument som en sammanslagen sträng
```

**Körexempel**:

```bash
./test.sh arg1 arg2 arg3
# Skriptnamn: ./test.sh
# Första arg: arg1
# Andra arg: arg2
# Totalt antal args: 3
# Alla args: arg1 arg2 arg3
```

### Validera inkommande argument

```bash
#!/bin/bash
set -euo pipefail

# Säkerställ att tillräckligt många argument finns
if [[ $# -lt 2 ]]; then
    echo "Användning: $0 <namn> <ålder>"
    exit 1
fi

namn="$1"
ålder="$2"

echo "Hej $namn, du är $ålder år gammal"
```

### Skillnad mellan $@ och $*

```bash
# $@ - varje argument som separat ord (med citationstecken)
for arg in "$@"; do
    echo "Arg: $arg"
done

# $* - alla argument sammanslagna till en enda sträng
# Påverkas av IFS-variabeln
```

**Rekommendation**: Använd alltid `"$@"` för att bevara argument med mellanslag korrekt.

## Shift: Rotera argumentlistan framåt

`shift` eliminerar det första argumentet och flyttar alla andra ett steg framåt:

```bash
#!/bin/bash

echo "Före shift:"
echo "1: $1, 2: $2, 3: $3"

shift

echo "Efter shift:"
echo "1: $1, 2: $2"
# Det som tidigare var $2 är nu $1
```

**Användningsscenario**: Iterera genom alla argument:

```bash
#!/bin/bash

while [[ $# -gt 0 ]]; do
    echo "Bearbetar: $1"
    shift
done
```

**Med shift N**:

```bash
shift 2   # Hoppar över de första 2 argumenten
```

### Flaggparsning med shift

```bash
#!/bin/bash

utförlig=false
utdatafil=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            utförlig=true
            shift
            ;;
        -o|--output)
            utdatafil="$2"
            shift 2
            ;;
        *)
            echo "Okänd flagga: $1"
            exit 1
            ;;
    esac
done
```

## Read: Hämta användarinput

`read` läser input från användaren eller från standard input.

### Grundläggande read-användning

```bash
#!/bin/bash

# Invänta användarinput
echo "Vad heter du?"
read namn
echo "Hej, $namn!"

# Med prompt på samma rad
read -p "Ange ditt namn: " namn
echo "Hej, $namn!"
```

### Read-alternativ och flaggor

```bash
# -p: Visa prompt
read -p "Skriv namn: " namn

# -s: Tyst läge (döljer input, idealiskt för lösenord)
read -s -p "Ange lösenord: " lösenord
echo ""  # Lägg till radbrytning efter lösenord

# -t: Timeout i sekunder
read -t 5 -p "Snabbt! Ange: " svar || echo "För långsamt!"

# -n: Läs exakt N tecken
read -n 1 -p "Tryck valfri tangent för att fortsätta..."

# -r: Råläge (behandlar inte backslash som escape-tecken)
read -r rad  # Rekommenderas vid filläsning

# -a: Läs till array
read -a ord <<< "ett två tre"
echo "${ord[1]}"  # två
```

### Läsa från fil rad för rad

```bash
# Läs fil rad för rad
while IFS= read -r rad; do
    echo "Rad: $rad"
done < fil.txt

# Med processsubstitution
while IFS= read -r rad; do
    echo "$rad"
done < <(ls -la)
```

### Läsa flera variabler samtidigt

```bash
# Dela upp input i flera variabler
echo "äpple banan citron" | read -r a b c
# OBS: Fungerar inte som förväntat i subshell!

# Använd here-string istället
read -r a b c <<< "äpple banan citron"
echo "$a"  # äpple
echo "$b"  # banan
```

## Flödeskontroll: if/elif/else, [[ ]], for/while-loopar

### If-satser

```bash
#!/bin/bash

# Grundläggande if
if [[ villkor ]]; then
    echo "Sant"
fi

# If-else
if [[ villkor ]]; then
    echo "Sant"
else
    echo "Falskt"
fi

# If-elif-else
if [[ villkor1 ]]; then
    echo "Första"
elif [[ villkor2 ]]; then
    echo "Andra"
else
    echo "Inget av ovanstående"
fi
```

### [[ ]] jämfört med [ ]

**Föredra alltid [[ ]]** - det är bash-specifikt men betydligt säkrare:

```bash
# [[ ]] fördelar:
# - Ingen automatisk word splitting
# - Ingen pathname expansion
# - Inbyggt stöd för regex med =~
# - && och || fungerar direkt

# [ ] är POSIX-kompatibelt men kräver citationstecken
if [ "$var" = "värde" ]; then ...  # Citationstecken nödvändiga
if [[ $var = "värde" ]]; then ...  # Fungerar utan citationstecken
```

### Jämförelseoperatorer

```bash
# Strängjämförelser
[[ $str = "värde" ]]    # Lika med
[[ $str != "värde" ]]   # Inte lika med
[[ -z "$str" ]]         # Tom sträng
[[ -n "$str" ]]         # Icke-tom sträng
[[ $str =~ ^regex$ ]]   # Regex-matchning

# Numeriska jämförelser
[[ $num -eq 5 ]]   # Lika med (equal)
[[ $num -ne 5 ]]   # Inte lika med (not equal)
[[ $num -lt 10 ]]  # Mindre än (less than)
[[ $num -le 10 ]]  # Mindre eller lika (less or equal)
[[ $num -gt 0 ]]   # Större än (greater than)
[[ $num -ge 0 ]]   # Större eller lika (greater or equal)

# Använd (( )) för aritmetiska operationer (mer läsvänligt)
(( num == 5 ))
(( num > 0 && num < 10 ))

# Filtest
[[ -f "$fil" ]]    # Filen existerar
[[ -d "$mapp" ]]   # Mappen existerar
[[ -e "$sökväg" ]] # Existerar (fil eller mapp)
[[ -r "$fil" ]]    # Läsbar
[[ -w "$fil" ]]    # Skrivbar
[[ -x "$fil" ]]    # Körbar
[[ -s "$fil" ]]    # Fil existerar och är inte tom
```

### Logiska operatorer

```bash
# OCH (AND)
[[ villkor1 && villkor2 ]]

# ELLER (OR)
[[ villkor1 || villkor2 ]]

# INTE (NOT)
[[ ! villkor ]]

# Kombinera operatorer
if [[ -f "$fil" && -r "$fil" ]]; then
    cat "$fil"
fi
```

### For-loopar

```bash
# Iterera över lista
for objekt in äpple banan citron; do
    echo "$objekt"
done

# Iterera över array
frukter=("äpple" "banan" "citron")
for frukt in "${frukter[@]}"; do
    echo "$frukt"
done

# C-stil for-loop
for ((i=0; i<10; i++)); do
    echo "$i"
done

# Iterera över filer
for fil in *.txt; do
    echo "Bearbetar $fil"
done

# Loop med kommandoutput
for användare in $(cat /etc/passwd | cut -d: -f1); do
    echo "Användare: $användare"
done
```

### While-loopar

```bash
# Grundläggande while
räknare=0
while [[ $räknare -lt 5 ]]; do
    echo "$räknare"
    ((räknare++))
done

# Oändlig loop
while true; do
    # använd break för att avsluta
    break
done

# Läs fil rad för rad
while IFS= read -r rad; do
    echo "$rad"
done < fil.txt
```

### Until-loop (motsats till while)

```bash
until [[ $räknare -ge 5 ]]; do
    echo "$räknare"
    ((räknare++))
done
```

### Break och Continue

```bash
for i in {1..10}; do
    if [[ $i -eq 5 ]]; then
        continue  # Hoppa över resten av iterationen, fortsätt med nästa
    fi
    if [[ $i -eq 8 ]]; then
        break     # Avsluta loopen helt och hållet
    fi
    echo "$i"
done
# Output: 1 2 3 4 6 7
```

## mktemp: Skapa säkra temporära filer

`mktemp` genererar unika, säkra temporära filer eller kataloger med slumpmässiga namn.

```bash
# Skapa temporär fil
temp_fil=$(mktemp)
echo "Skapad: $temp_fil"
# /tmp/tmp.abc123xyz

# Skapa temporär katalog
temp_mapp=$(mktemp -d)
echo "Skapad katalog: $temp_mapp"

# Med specifikt prefix
temp_fil=$(mktemp /tmp/minapp.XXXXXX)
# X:en ersätts med slumpmässiga tecken

# Med suffix
temp_fil=$(mktemp --suffix=.txt)
```

### Automatisk städning med trap

```bash
#!/bin/bash

# Skapa temporär fil
TEMP_FIL=$(mktemp)

# Registrera städfunktion som exekveras vid exit
trap "rm -f $TEMP_FIL" EXIT

# Använd temporärfilen
echo "data" > "$TEMP_FIL"
cat "$TEMP_FIL"

# Temporärfilen raderas automatiskt när skriptet avslutas
```

## Trap: Signalhantering och städning

`trap` registrerar kommandon som ska exekveras vid specifika signaler.

```bash
# Syntax: trap 'kommandon' SIGNALER

# Städning vid exit (normal avslutning, Ctrl+C, fel)
trap 'echo "Städar upp..."; rm -f $temp_fil' EXIT

# Ignorera Ctrl+C
trap '' SIGINT

# Hantera specifika signaler
trap 'echo "Fångade SIGINT"' SIGINT
trap 'echo "Fångade SIGTERM"' SIGTERM
```

### Vanliga signaler

```bash
EXIT     # När skriptet avslutas (oavsett orsak)
SIGINT   # Ctrl+C (avbryt)
SIGTERM  # Standard termineringssignal
SIGKILL  # Kan inte fångas - omedelbar terminering
SIGHUP   # Terminalen stängs
ERR      # När ett kommando misslyckas (med set -e aktiverat)
```

### Praktiskt städningsmönster

```bash
#!/bin/bash
set -euo pipefail

# Skapa temporära resurser
TEMP_MAPP=$(mktemp -d)
PID_FIL="/var/run/minapp.pid"

städa() {
    echo "Städar upp..."
    rm -rf "$TEMP_MAPP"
    rm -f "$PID_FIL"
}

trap städa EXIT

# Huvudprogram
echo "Arbetar i $TEMP_MAPP"
# ... resten av skriptet

# städa() exekveras automatiskt när skriptet avslutas
```

### Trap med funktioner

```bash
#!/bin/bash

vid_fel() {
    echo "Fel inträffade på rad $1"
    exit 1
}

trap 'vid_fel $LINENO' ERR

# Om något kommando misslyckas, anropas vid_fel med radnumret
```

## Exit-koder: Statuskoder från skript

Exit-koder signalerar om ett kommando lyckades (0) eller misslyckades (icke-noll).

```bash
# Kontrollera senaste kommandots exit-kod
echo $?

# I skript
exit 0    # Framgångsrik exekvering
exit 1    # Allmänt fel
exit 2    # Felaktig användning av kommando

# Vanliga konventioner
# 0: Framgång
# 1: Allmänt fel
# 2: Felaktig kommandoanvändning
# 126: Kommandot hittat men inte körbart
# 127: Kommandot hittades inte
# 128+N: Terminerad av signal N (128+9=137 för SIGKILL)
```

### Använda exit-koder i villkorssatser

```bash
# Kommandots exit-kod avgör if-villkoret
if kommando; then
    echo "Kommandot lyckades"
else
    echo "Kommandot misslyckades"
fi

# Kombinera kommandon med logiska operatorer
kommando1 && kommando2    # kommando2 körs endast om kommando1 lyckas
kommando1 || kommando2    # kommando2 körs endast om kommando1 misslyckas

# Praktiskt exempel
grep -q "mönster" fil && echo "Hittad" || echo "Inte hittad"
```

### Egna exit-koder i funktioner

```bash
#!/bin/bash

validera_input() {
    if [[ -z "$1" ]]; then
        echo "Fel: Ingen input angiven"
        return 1
    fi
    return 0
}

if ! validera_input "$1"; then
    exit 1
fi

echo "Input är giltig: $1"
```

## Praktiskt: Komplett skriptexempel

```bash
#!/usr/bin/env bash
#
# backup.sh - Enkel backup-lösning
# Användning: ./backup.sh <käll_katalog> <backup_katalog>
#

set -euo pipefail
IFS=$'\n\t'

# === Konfiguration ===
readonly SKRIPT_NAMN="$(basename "$0")"
readonly LOGG_FIL="/tmp/${SKRIPT_NAMN}.log"

# === Funktioner ===
logga() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGG_FIL"
}

användning() {
    echo "Användning: $SKRIPT_NAMN <käll_katalog> <backup_katalog>"
    echo "  käll_katalog: Katalog som ska backas upp"
    echo "  backup_katalog: Var backupen ska lagras"
    exit 1
}

städa() {
    logga "Städar upp..."
    # Lägg till städkommandon här vid behov
}

# === Huvudprogram ===
trap städa EXIT

# Validera argument
if [[ $# -ne 2 ]]; then
    användning
fi

KÄLL_KATALOG="$1"
BACKUP_KATALOG="$2"

# Validera källkatalog
if [[ ! -d "$KÄLL_KATALOG" ]]; then
    logga "Fel: Källkatalogen existerar inte: $KÄLL_KATALOG"
    exit 1
fi

# Skapa backup-katalog om den inte finns
mkdir -p "$BACKUP_KATALOG"

# Utför backup
TIDSSTÄMPEL=$(date +%Y%m%d_%H%M%S)
BACKUP_FIL="${BACKUP_KATALOG}/backup_${TIDSSTÄMPEL}.tar.gz"

logga "Initierar backup: $KÄLL_KATALOG -> $BACKUP_FIL"

tar -czf "$BACKUP_FIL" -C "$(dirname "$KÄLL_KATALOG")" "$(basename "$KÄLL_KATALOG")"

logga "Backup slutförd framgångsrikt!"
logga "Backup-storlek: $(du -h "$BACKUP_FIL" | cut -f1)"

exit 0
```

## Viktiga takeaways

- **Standardmall**: `#!/bin/bash` + `set -euo pipefail` + `IFS=$'\n\t'`
- **set -e**: Terminera vid kommandofel
- **set -u**: Terminera vid odefinerad variabel
- **set -o pipefail**: Pipeline returnerar fel om något kommando misslyckas
- **Argument**: $0 (skriptnamn), $1-$9 (argument), $# (antal), $@ (alla)
- **shift**: Flytta argumenten framåt (användbartför flaggparsning)
- **read -p**: Läs input med prompt
- **[[ ]]**: Föredra framför [ ] för villkorstester
- **Numeriska jämförelser**: -eq, -ne, -lt, -le, -gt, -ge (eller använd (( )))
- **mktemp**: Generera säkra temporära filer
- **trap 'städa' EXIT**: Garanterad städning vid avslutning
- **Exit-koder**: 0 = framgång, icke-noll = misslyckande
- **Använd citationstecken**: `"$variabel"` för att hantera mellanslag korrekt

"""
}
