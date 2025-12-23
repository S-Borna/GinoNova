"""
NOD 1.10: Funktioner
====================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

FUNKTIONER_NODE = {
    "title": "Funktioner",
    "slug": "funktioner",
    "description": "Bash-funktioner: skapande, argument, returvärden och local-variabler.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "order_index": 9,
    "content": r"""# Funktioner i Bash

> **TL;DR:** Funktioner skapas med `func() { ... }`. Argument är `$1`, `$2` etc. Returnera med `return N` (0-255) eller `echo`. Gör variabler lokala med `local`.

---

## 📖 TEORI: Skapa funktioner

### Syntax - Två sätt

```bash
# Sätt 1: Med parenteser (rekommenderas)
funktionsnamn() {
    kommandon
}

# Sätt 2: Med function-keyword
function funktionsnamn {
    kommandon
}
```

### Enkel funktion

```bash
#!/usr/bin/env bash

hälsa() {
    echo "Hej världen!"
}

# Anropa funktionen
hälsa
```

### ⚠️ Viktigt: Definiera INNAN anrop!

```bash
# FEL - funktionen är inte definierad ännu
hälsa          # ❌ Ger fel

hälsa() {
    echo "Hej"
}
```

```bash
# RÄTT - funktionen definieras först
hälsa() {
    echo "Hej"
}

hälsa          # ✅ Fungerar
```

---

## 📖 Argument till funktioner

Funktioner använder **samma** parametersystem som skript!

| Variabel | Betydelse |
|----------|-----------|
| `$1` - `$9` | Argument 1-9 |
| `$@` | Alla argument (separata) |
| `$#` | Antal argument |
| `$0` | Fortfarande skriptnamnet (INTE funktionsnamnet!) |

### Exempel

```bash
#!/usr/bin/env bash

hälsa() {
    echo "Hej $1!"
}

addera() {
    echo $(( $1 + $2 ))
}

visa_alla() {
    echo "Antal argument: $#"
    for arg in "$@"; do
        echo "  - $arg"
    done
}

# Anropa med argument
hälsa "Lisa"            # Hej Lisa!
addera 5 3              # 8
visa_alla ett två tre   # Listar alla
```

### Kräv argument

```bash
backup() {
    local fil="${1:?Användning: backup <fil>}"
    echo "Säkerhetskopierar $fil..."
}

backup              # Fel: Användning: backup <fil>
backup data.txt     # Säkerhetskopierar data.txt...
```

---

## 📖 Returvärden

### return - Exit status (0-255)

`return` fungerar som `exit` för funktioner:

```bash
#!/usr/bin/env bash

fil_finns() {
    if [[ -f "$1" ]]; then
        return 0    # Sant / success
    else
        return 1    # Falskt / failure
    fi
}

# Användning
if fil_finns "/etc/passwd"; then
    echo "Filen finns!"
fi
```

### Kortform

```bash
fil_finns() {
    [[ -f "$1" ]]    # Returnerar automatiskt 0 eller 1
}
```

### return vs exit

| Kommando | Effekt |
|----------|--------|
| `return N` | Avslutar funktionen med status N |
| `exit N` | Avslutar HELA skriptet med status N |

### ⚠️ return kan bara returnera 0-255!

```bash
beräkna() {
    return 1000    # PROBLEM: blir 232 (1000 mod 256)
}
```

---

## 📖 Returnera data med echo

För att returnera **faktiska värden** (inte bara exit status), använd `echo`:

```bash
#!/usr/bin/env bash

addera() {
    local summa=$(( $1 + $2 ))
    echo "$summa"    # "Returnerar" värdet
}

# Fånga output med command substitution
resultat=$(addera 10 20)
echo "Summan är: $resultat"    # Summan är: 30
```

### Kombinera return och echo

```bash
dividera() {
    if [[ $2 -eq 0 ]]; then
        echo "Fel: Division med noll" >&2
        return 1
    fi
    echo $(( $1 / $2 ))
    return 0
}

# Användning
if resultat=$(dividera 10 2); then
    echo "Resultat: $resultat"
else
    echo "Beräkningen misslyckades"
fi
```

---

## 📖 local - Lokala variabler

**Utan `local`:** Variabeln blir global och kan ändras av misstag.

```bash
#!/usr/bin/env bash

namn="Global"

ändra() {
    namn="Ändrad i funktion"    # Ändrar globala!
}

echo "$namn"    # Global
ändra
echo "$namn"    # Ändrad i funktion (OOPS!)
```

**Med `local`:** Variabeln finns bara i funktionen.

```bash
#!/usr/bin/env bash

namn="Global"

ändra() {
    local namn="Lokal"    # Egen kopia
    echo "I funktionen: $namn"
}

echo "Innan: $namn"     # Global
ändra                   # I funktionen: Lokal
echo "Efter: $namn"     # Global (oförändrad!)
```

### Best practice: ALLTID använd local!

```bash
process_fil() {
    local fil="$1"
    local rad
    local count=0

    while IFS= read -r rad; do
        (( count++ ))
    done < "$fil"

    echo "$count"
}
```

---

## 📖 Avancerade mönster (VG-NIVÅ)

### Rekursion

```bash
#!/usr/bin/env bash

factorial() {
    local n=$1
    if (( n <= 1 )); then
        echo 1
    else
        local prev=$(factorial $(( n - 1 )))
        echo $(( n * prev ))
    fi
}

echo "5! = $(factorial 5)"    # 5! = 120
```

### Funktioner som returnerar arrayer

```bash
#!/usr/bin/env bash

get_users() {
    local -a users=("alice" "bob" "charlie")
    echo "${users[@]}"
}

# Fånga i array
read -ra user_arr <<< "$(get_users)"
echo "Första användaren: ${user_arr[0]}"
```

### Funktioner i funktioner (nested)

```bash
#!/usr/bin/env bash

yttre() {
    inre() {
        echo "Jag är inre"
    }
    echo "Jag är yttre"
    inre
}

yttre
# Output:
# Jag är yttre
# Jag är inre
```

### Funktion som tar en annan funktion som argument

```bash
#!/usr/bin/env bash

kör_för_varje() {
    local func="$1"
    shift
    for item in "$@"; do
        "$func" "$item"
    done
}

visa() {
    echo "Element: $1"
}

kör_för_varje visa äpple banan citron
# Element: äpple
# Element: banan
# Element: citron
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Valideringsfunktioner

```bash
#!/usr/bin/env bash

is_number() {
    [[ "$1" =~ ^[0-9]+$ ]]
}

is_email() {
    [[ "$1" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]
}

is_ip() {
    local ip="$1"
    [[ "$ip" =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
}

# Testa
is_number "42" && echo "42 är ett nummer"
is_email "test@example.com" && echo "Giltig email"
is_ip "192.168.1.1" && echo "Giltig IP"
```

### Exempel 2: Logging-funktioner

```bash
#!/usr/bin/env bash

log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $*"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') - $*" >&2
}

log_debug() {
    [[ "$DEBUG" == "true" ]] && echo "[DEBUG] $*"
}

# Användning
log_info "Startar skriptet"
log_error "Något gick fel"
DEBUG=true log_debug "Variabel x=$x"
```

### Exempel 3: Retry-funktion

```bash
#!/usr/bin/env bash

retry() {
    local max_attempts="${1:-3}"
    local delay="${2:-1}"
    shift 2
    local cmd="$@"

    local attempt=1
    while (( attempt <= max_attempts )); do
        echo "Försök $attempt av $max_attempts..."
        if eval "$cmd"; then
            return 0
        fi
        (( attempt++ ))
        sleep "$delay"
    done

    echo "Misslyckades efter $max_attempts försök"
    return 1
}

# Användning
retry 3 2 curl -s https://api.example.com/health
```

### Exempel 4: Komplett skript med funktioner

```bash
#!/usr/bin/env bash
set -euo pipefail

# === FUNKTIONER ===

usage() {
    cat << EOF
Användning: $0 [options] <file>

Options:
    -v, --verbose    Visa mer information
    -o, --output     Ange output-fil
    -h, --help       Visa denna hjälp

EOF
    exit "${1:-0}"
}

log() {
    local level="$1"
    shift
    echo "[$level] $*"
}

validate_file() {
    local fil="$1"
    if [[ ! -f "$fil" ]]; then
        log ERROR "Filen '$fil' finns inte"
        return 1
    fi
    if [[ ! -r "$fil" ]]; then
        log ERROR "Kan inte läsa '$fil'"
        return 1
    fi
    return 0
}

process_file() {
    local input="$1"
    local output="${2:-/dev/stdout}"

    log INFO "Processar $input..."
    wc -l < "$input" > "$output"
    log INFO "Klar!"
}

# === MAIN ===

main() {
    local verbose=false
    local output_file=""
    local input_file=""

    while [[ $# -gt 0 ]]; do
        case "$1" in
            -v|--verbose) verbose=true; shift ;;
            -o|--output) output_file="$2"; shift 2 ;;
            -h|--help) usage ;;
            -*) log ERROR "Okänd flagga: $1"; usage 1 ;;
            *) input_file="$1"; shift ;;
        esac
    done

    [[ -z "$input_file" ]] && usage 1

    validate_file "$input_file" || exit 1
    process_file "$input_file" "$output_file"
}

main "$@"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Skapa funktion? | namn() { kommandon; } |
| 2 | Första argumentet i funktion? | $1 |
| 3 | Antal argument i funktion? | $# |
| 4 | return vs exit? | return avslutar funktion, exit avslutar skript |
| 5 | return kan returnera? | Endast 0-255 (exit status) |
| 6 | Returnera text från funktion? | echo "värde" |
| 7 | Fånga funktions output? | var=$(funktionsnamn) |
| 8 | Lokal variabel i funktion? | local var="värde" |
| 9 | Varför local? | Undviker att ändra globala variabler |
| 10 | Kolla om funktion lyckades? | if funktionsnamn; then ... fi |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilken syntax skapar en funktion korrekt?**
- A) function hälsa[] { echo "Hej"; }
- B) hälsa() { echo "Hej"; } ✅
- C) def hälsa() { echo "Hej"; }
- D) hälsa = function() { echo "Hej"; }

**2. Hur får du tredje argumentet i en funktion?**
- A) $arg3
- B) $[3]
- C) $3 ✅
- D) args[2]

**3. Vad är max returvärde med return?**
- A) 100
- B) 255 ✅
- C) 999
- D) Ingen gräns

**4. Hur returnerar du en textsträng från en funktion?**
- A) return "text"
- B) echo "text" ✅
- C) yield "text"
- D) output "text"

**5. Vad gör `local` i en funktion?**
- A) Gör funktionen privat
- B) Gör variabeln endast tillgänglig i funktionen ✅
- C) Låser variabeln
- D) Exporterar variabeln

**6. Hur fångar du output från en funktion?**
- A) var = funktionsnamn
- B) var=$(funktionsnamn) ✅
- C) funktionsnamn > var
- D) funktionsnamn | var

**7. Vad returnerar en funktion om inget return anges?**
- A) 0
- B) 1
- C) Exit status från sista kommandot ✅
- D) Undefined

**8. Var måste funktionen definieras?**
- A) I början av filen
- B) Före första anropet ✅
- C) Efter alla variabler
- D) Spelar ingen roll

**9. Vad händer om du kör `return 300`?**
- A) Returnerar 300
- B) Ger error
- C) Returnerar 300 mod 256 = 44 ✅
- D) Returnerar 255

**10. Hur kontrollerar du om en funktion lyckades?**
- A) if [[ funktionsnamn ]]; then
- B) if funktionsnamn; then ✅
- C) if result = funktionsnamn; then
- D) try funktionsnamn; catch

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Enkel funktion
Skapa en funktion som tar ett namn och skriver ut "Hej, [namn]!":
```bash
#!/usr/bin/env bash
# Skriv din funktion här
hälsa() {
    # Fyll i
}

hälsa "Lisa"    # Ska skriva "Hej, Lisa!"
```

### Övning 2: Beräkningsfunktion
Skapa en funktion `kvadrat` som returnerar kvadraten av ett tal:
```bash
#!/usr/bin/env bash

kvadrat() {
    # Fyll i
}

resultat=$(kvadrat 7)
echo "7 * 7 = $resultat"    # Ska skriva "7 * 7 = 49"
```

### Övning 3: Validering med local
Skriv `is_positive` som returnerar 0 om talet är positivt:
```bash
#!/usr/bin/env bash

is_positive() {
    local num="$1"
    # Fyll i (returnera 0 om >0, annars 1)
}

if is_positive 42; then
    echo "42 är positivt"
fi
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `return "text"` | return tar bara nummer | Använd `echo "text"` |
| Glömma local | Variabler blir globala | `local var="värde"` |
| Anropa före definition | Funktion finns inte | Definiera funktioner först |
| `$0` i funktion | Ger skriptnamn, inte funktionsnamn | Finns ingen FUNCNAME i posix |
| `exit` i funktion | Avslutar hela skriptet | Använd `return` |

---

## 📝 SAMMANFATTNING

```bash
# SKAPA FUNKTION
namn() {
    kommandon
}

# ARGUMENT
$1 $2 $3    # Första, andra, tredje
$@          # Alla argument
$#          # Antal

# RETURN
return 0    # Success (0-255 endast)
return 1    # Failure

# RETURNERA DATA
echo "värde"                    # I funktionen
resultat=$(funktionsnamn)       # Fånga output

# LOKALA VARIABLER
local var="värde"
local -a arr=(a b c)    # Lokal array

# BEST PRACTICE
func() {
    local arg="${1:?Argument krävs}"
    local result=""

    # ... logik ...

    echo "$result"
    return 0
}
```

"""
}

