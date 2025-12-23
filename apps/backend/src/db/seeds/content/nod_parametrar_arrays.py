"""
NOD 1.9: Parametrar & Arrays
=============================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

PARAMETRAR_ARRAYS_NODE = {
    "title": "Parametrar & Arrays",
    "slug": "parametrar-arrays",
    "description": "Avancerad parameterhantering och arrays - VG-nivå för skriptprogrammering.",
    "difficulty": "hard",
    "estimated_minutes": 55,
    "xp_reward": 150,
    "order_index": 8,
    "content": r"""# Parametrar & Arrays

> **TL;DR:** `$1`, `$2` är argument. `${var:-default}` ger default-värden. Arrays skapas med `arr=(a b c)` och läses med `${arr[0]}`. Detta är VG-nivå!

---

## 📖 TEORI: Positionsparametrar (repetition)

| Variabel | Betydelse | Exempel |
|----------|-----------|---------|
| `$0` | Skriptets namn | `./backup.sh` |
| `$1` - `$9` | Argument 1-9 | `$1` = första argumentet |
| `${10}` | Argument 10+ | Kräver klamrar! |
| `$#` | Antal argument | Om 3 arg → `$# = 3` |
| `$@` | Alla argument (separata) | I loopar |
| `$*` | Alla argument (ett ord) | Sällan användbart |

### shift - Flytta parametrar

`shift` tar bort `$1` och skiftar alla andra:

```bash
#!/usr/bin/env bash
echo "Före shift: \$1=$1 \$2=$2 \$3=$3"
shift
echo "Efter shift: \$1=$1 \$2=$2 \$3=$3"

# Kör: ./test.sh A B C
# Före shift: $1=A $2=B $3=C
# Efter shift: $1=B $2=C $3=
```

### shift med antal

```bash
shift 2    # Ta bort $1 och $2
```

### Praktiskt: Processa flaggor

```bash
#!/usr/bin/env bash
while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -f|--file)
            FILE="$2"
            shift 2
            ;;
        *)
            echo "Okänt argument: $1"
            shift
            ;;
    esac
done
```

---

## 📖 Parameter Expansion (VG-NIVÅ!)

### Default-värden

| Syntax | Betydelse | Exempel |
|--------|-----------|---------|
| `${var:-default}` | Använd default om var är tom | `${name:-Guest}` |
| `${var:=default}` | Sätt OCH använd default om tom | `${name:=Guest}` |
| `${var:?error}` | Visa error och avbryt om tom | `${file:?Fil krävs!}` |
| `${var:+value}` | Använd value om var INTE är tom | `${debug:+--verbose}` |

### Exempel

```bash
# Default om tom
namn=""
echo "Hej ${namn:-Gäst}"     # Hej Gäst

namn="Lisa"
echo "Hej ${namn:-Gäst}"     # Hej Lisa

# Sätt default
echo "Värde: ${config:=/etc/app.conf}"
echo "Config är nu: $config"  # /etc/app.conf

# Kräv värde
fil="${1:?Användning: $0 <filnamn>}"

# Använd endast om satt
debug="yes"
cmd="myprogram ${debug:+--verbose}"  # myprogram --verbose
```

### Strängmanipulation

| Syntax | Betydelse | Exempel |
|--------|-----------|---------|
| `${#var}` | Längd | `${#name}` → 4 (för "Lisa") |
| `${var^^}` | VERSALER | `${name^^}` → LISA |
| `${var,,}` | gemener | `${NAME,,}` → lisa |
| `${var^}` | Första versal | `${name^}` → Lisa |

### Ta bort delar av strängen

| Syntax | Betydelse | Exempel |
|--------|-----------|---------|
| `${var%pattern}` | Ta bort kortaste från SLUTET | `${fil%.txt}` |
| `${var%%pattern}` | Ta bort längsta från SLUTET | `${path%%/*}` |
| `${var#pattern}` | Ta bort kortaste från BÖRJAN | `${fil#*/}` |
| `${var##pattern}` | Ta bort längsta från BÖRJAN | `${path##*/}` |

### Minnesregel

```
#  = Början (# är till vänster på tangentbordet)
%  = Slutet (% är till höger)
#  = Kortaste match
## = Längsta match
```

### Praktiska exempel

```bash
fil="/home/user/dokument/rapport.txt"

# Få filnamnet (ta bort sökväg)
echo "${fil##*/}"          # rapport.txt

# Få katalogen (ta bort filnamn)
echo "${fil%/*}"           # /home/user/dokument

# Ta bort filändelse
echo "${fil%.txt}"         # /home/user/dokument/rapport

# Byt filändelse
echo "${fil%.txt}.pdf"     # /home/user/dokument/rapport.pdf
```

### Substring

```bash
var="Hello World"

echo "${var:0:5}"    # Hello (start:längd)
echo "${var:6}"      # World (från position 6)
echo "${var: -5}"    # World (sista 5, notera mellanslag!)
```

---

## 📖 Arrays (VG-NIVÅ!)

### Skapa array

```bash
# Metod 1: Direkt tilldelning
frukter=(äpple banan citron)

# Metod 2: Index för index
färger[0]="röd"
färger[1]="grön"
färger[2]="blå"

# Metod 3: Från kommando
filer=($(ls *.txt))
```

### Läsa från array

```bash
arr=(ett två tre fyra fem)

echo ${arr[0]}       # ett (första elementet)
echo ${arr[2]}       # tre (tredje elementet)
echo ${arr[-1]}      # fem (sista elementet)
echo ${arr[@]}       # ett två tre fyra fem (alla)
echo ${#arr[@]}      # 5 (antal element)
echo ${!arr[@]}      # 0 1 2 3 4 (alla index)
```

### Loopa över array

```bash
frukter=(äpple banan citron)

# Loopa över värden
for frukt in "${frukter[@]}"; do
    echo "Jag gillar $frukt"
done

# Loopa över index
for i in "${!frukter[@]}"; do
    echo "Index $i: ${frukter[$i]}"
done
```

### ⚠️ Viktigt: Citera "${arr[@]}"!

```bash
filer=("fil ett.txt" "fil två.txt")

# FEL: Utan citattecken - delar på mellanslag
for f in ${filer[@]}; do    # ❌
    echo "$f"
done
# Output: fil, ett.txt, fil, två.txt

# RÄTT: Med citattecken
for f in "${filer[@]}"; do  # ✅
    echo "$f"
done
# Output: fil ett.txt, fil två.txt
```

### Modifiera array

```bash
arr=(a b c)

# Lägg till element
arr+=(d e)              # arr = (a b c d e)

# Ändra element
arr[1]="B"              # arr = (a B c d e)

# Ta bort element
unset arr[2]            # arr = (a B d e), men index 2 är "borta"

# Ta bort hela arrayen
unset arr
```

### Array slicing

```bash
arr=(a b c d e f g)

echo "${arr[@]:2:3}"    # c d e (från index 2, 3 element)
echo "${arr[@]:4}"      # e f g (från index 4 till slut)
echo "${arr[@]::3}"     # a b c (första 3)
```

---

## 📖 Associativa Arrays (Bash 4+)

Arrayer med **namngivna nycklar** istället för nummer:

```bash
# Måste deklareras först!
declare -A users

# Tilldela värden
users[alice]="admin"
users[bob]="developer"
users[charlie]="viewer"

# Läsa
echo ${users[alice]}         # admin
echo ${users[@]}             # alla värden
echo ${!users[@]}            # alla nycklar

# Loopa
for user in "${!users[@]}"; do
    echo "$user är ${users[$user]}"
done
# Output:
# alice är admin
# bob är developer
# charlie är viewer
```

### Praktiskt exempel: Config

```bash
#!/usr/bin/env bash
declare -A config

config[host]="localhost"
config[port]="8080"
config[debug]="true"

echo "Ansluter till ${config[host]}:${config[port]}"
[[ ${config[debug]} == "true" ]] && echo "Debug-läge aktivt"
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Robust argumenthantering

```bash
#!/usr/bin/env bash

# Default-värden
OUTPUT_DIR="${OUTPUT_DIR:-./output}"
VERBOSE="${VERBOSE:-false}"

# Kräv minst ett argument
INPUT_FILE="${1:?Användning: $0 <input-fil> [output-dir]}"

# Valfritt andra argument
OUTPUT_DIR="${2:-$OUTPUT_DIR}"

echo "Input: $INPUT_FILE"
echo "Output: $OUTPUT_DIR"
```

### Exempel 2: Filnamnmanipulation

```bash
#!/usr/bin/env bash

for fil in *.jpg; do
    # Få basnamn utan ändelse
    basnamn="${fil%.jpg}"

    # Skapa nytt namn med datum
    datum=$(date +%Y%m%d)
    nytt_namn="${basnamn}_${datum}.jpg"

    echo "Döper om $fil → $nytt_namn"
    mv "$fil" "$nytt_namn"
done
```

### Exempel 3: Array av servrar

```bash
#!/usr/bin/env bash

servers=(
    "web1.example.com"
    "web2.example.com"
    "db1.example.com"
)

for server in "${servers[@]}"; do
    echo "Pingar $server..."
    if ping -c 1 "$server" &>/dev/null; then
        echo "  ✅ $server är uppe"
    else
        echo "  ❌ $server svarar inte"
    fi
done
```

### Exempel 4: Processa flaggor professionellt

```bash
#!/usr/bin/env bash

# Defaults
VERBOSE=false
DRY_RUN=false
OUTPUT_FILE=""

usage() {
    echo "Användning: $0 [-v] [-n] [-o fil] <input>"
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -n|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -o|--output)
            OUTPUT_FILE="${2:?-o kräver ett filnamn}"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        -*)
            echo "Okänd flagga: $1"
            usage
            ;;
        *)
            INPUT_FILE="$1"
            shift
            ;;
    esac
done

# Kräv input
[[ -z "$INPUT_FILE" ]] && usage

echo "Config:"
echo "  Input: $INPUT_FILE"
echo "  Output: ${OUTPUT_FILE:-stdout}"
echo "  Verbose: $VERBOSE"
echo "  Dry-run: $DRY_RUN"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | ${var:-default} gör? | Använder default om var är tom |
| 2 | ${var:=default} gör? | Sätter OCH använder default om tom |
| 3 | ${#var} returnerar? | Längden på strängen |
| 4 | ${var%pattern} gör? | Tar bort kortaste match från SLUTET |
| 5 | ${var##pattern} gör? | Tar bort längsta match från BÖRJAN |
| 6 | Skapa array? | arr=(ett två tre) |
| 7 | Läsa första elementet? | ${arr[0]} |
| 8 | Antal element i array? | ${#arr[@]} |
| 9 | Alla index i array? | ${!arr[@]} |
| 10 | shift gör? | Tar bort $1, skiftar $2→$1 etc |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad returnerar `${name:-Guest}` om $name är tom?**
- A) Felmeddelande
- B) Guest ✅
- C) Tom sträng
- D) name

**2. Vad är skillnaden mellan `:-` och `:=`?**
- A) Ingen skillnad
- B) := sätter också variabeln till default ✅
- C) :- är snabbare
- D) := fungerar bara med nummer

**3. Hur får du längden på en sträng?**
- A) len($var)
- B) ${var.length}
- C) ${#var} ✅
- D) $#var

**4. Vad gör `${fil%.txt}`?**
- A) Lägger till .txt
- B) Tar bort .txt från slutet ✅
- C) Kontrollerar om filen är .txt
- D) Konverterar till .txt

**5. Hur skapar du en array?**
- A) arr = (a b c)
- B) arr=(a b c) ✅
- C) array arr = a, b, c
- D) @arr = (a b c)

**6. Hur läser du tredje elementet i en array?**
- A) ${arr[3]}
- B) ${arr[2]} ✅
- C) $arr[3]
- D) arr(2)

**7. Hur får du alla element i en array?**
- A) ${arr}
- B) ${arr[*]}
- C) ${arr[@]} ✅
- D) Både B och C fungerar ✅

**8. Vad gör kommandot `shift`?**
- A) Flyttar cursor
- B) Tar bort $1 och skiftar alla parametrar ✅
- C) Sorterar parametrar
- D) Kopierar parametrar

**9. Hur deklarerar du en associativ array?**
- A) declare -A arr ✅
- B) assoc arr
- C) arr={}
- D) hash arr

**10. Vad ger `${path##*/}`?**
- A) Första katalogen i sökvägen
- B) Filnamnet (tar bort hela sökvägen) ✅
- C) Filändelsen
- D) Syntaxfel

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Parameter expansion
Testa dessa i terminalen:
```bash
fil="/home/user/rapport.txt"
echo "${fil##*/}"     # Vad visas?
echo "${fil%/*}"      # Vad visas?
echo "${fil%.txt}.pdf" # Vad visas?

namn=""
echo "${namn:-Okänd}" # Vad visas?
```

### Övning 2: Array-manipulation
```bash
#!/usr/bin/env bash
frukter=(äpple banan citron)
echo "Antal: ${#frukter[@]}"
frukter+=(druva)
echo "Alla: ${frukter[@]}"
for i in "${!frukter[@]}"; do
    echo "[$i] = ${frukter[$i]}"
done
```

### Övning 3: Argumenthantering
Skriv ett skript som:
1. Tar `-v` för verbose
2. Tar `-o fil` för output-fil
3. Tar ett obligatoriskt input-argument
4. Visar hjälp med `-h`

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `${arr[0]}` utan {} | Fungerar inte | Använd alltid `${arr[index]}` |
| `$arr[@]` utan {} | Ger bara första elementet | `${arr[@]}` |
| Glömma citera "${arr[@]}" | Delar på mellanslag | `"${arr[@]}"` |
| `declare -A` glöms | Associativ array funkar inte | Alltid `declare -A` först |
| Förväxla # och % | Fel del tas bort | # = början, % = slut |

---

## 📝 SAMMANFATTNING

```bash
# PARAMETER EXPANSION
${var:-default}    # Använd default om tom
${var:=default}    # Sätt default om tom
${var:?error}      # Fel om tom
${#var}            # Längd
${var%pattern}     # Ta bort från slut (kort)
${var%%pattern}    # Ta bort från slut (lång)
${var#pattern}     # Ta bort från början (kort)
${var##pattern}    # Ta bort från början (lång)

# ARRAYS
arr=(a b c)        # Skapa
${arr[0]}          # Första
${arr[@]}          # Alla
${#arr[@]}         # Antal
${!arr[@]}         # Alla index
arr+=(d)           # Lägg till
unset arr[1]       # Ta bort

# ASSOCIATIVA (Bash 4+)
declare -A map
map[key]="value"
echo ${map[key]}

# SHIFT
shift              # Ta bort $1
shift 2            # Ta bort $1 och $2
```

""",
    "quiz": [
        {
            "question": "Vad returnerar ${name:-Guest} om $name är tom?",
            "options": [
                "Felmeddelande",
                "Guest",
                "Tom sträng",
                "name"
            ],
            "correct": 1,
            "explanation": "${var:-default} returnerar default-värdet om variabeln är tom eller odefinierad."
        },
        {
            "question": "Vad är skillnaden mellan :- och :=?",
            "options": [
                "Ingen skillnad",
                ":= sätter också variabeln till default-värdet",
                ":- är snabbare",
                ":= fungerar bara med nummer"
            ],
            "correct": 1,
            "explanation": ":- bara returnerar default. := både sätter variabeln OCH returnerar värdet."
        },
        {
            "question": "Hur får du längden på en sträng i Bash?",
            "options": [
                "len($var)",
                "${var.length}",
                "${#var}",
                "$#var"
            ],
            "correct": 2,
            "explanation": "${#var} ger längden på strängen i variabeln var."
        },
        {
            "question": "Vad gör ${fil%.txt}?",
            "options": [
                "Lägger till .txt i slutet",
                "Tar bort .txt från slutet",
                "Kontrollerar om filen slutar med .txt",
                "Konverterar filen till .txt-format"
            ],
            "correct": 1,
            "explanation": "% tar bort mönster från slutet. ${fil%.txt} tar bort .txt från variabeln fil."
        },
        {
            "question": "Hur skapar du en array i Bash?",
            "options": [
                "arr = (a b c)",
                "arr=(a b c)",
                "array arr = a, b, c",
                "@arr = (a b c)"
            ],
            "correct": 1,
            "explanation": "Korrekt syntax är arr=(element1 element2 element3) utan mellanslag runt =."
        },
        {
            "question": "Hur läser du tredje elementet i en array?",
            "options": [
                "${arr[3]}",
                "${arr[2]}",
                "$arr[3]",
                "arr(2)"
            ],
            "correct": 1,
            "explanation": "Arrayer är 0-indexerade. Tredje elementet har index 2."
        },
        {
            "question": "Hur får du alla element i en array?",
            "options": [
                "${arr}",
                "${arr[*]}",
                "${arr[@]}",
                "Både B och C fungerar"
            ],
            "correct": 3,
            "explanation": "Både ${arr[@]} och ${arr[*]} ger alla element. @ rekommenderas med citattecken."
        },
        {
            "question": "Vad gör kommandot shift?",
            "options": [
                "Flyttar cursor till nästa rad",
                "Tar bort $1 och skiftar alla parametrar ett steg",
                "Sorterar parametrarna",
                "Kopierar parametrar till en array"
            ],
            "correct": 1,
            "explanation": "shift tar bort $1, sen blir $2 nya $1, $3 nya $2, osv."
        },
        {
            "question": "Hur deklarerar du en associativ array i Bash?",
            "options": [
                "declare -A arr",
                "assoc arr",
                "arr={}",
                "hash arr"
            ],
            "correct": 0,
            "explanation": "declare -A krävs för associativa arrayer i Bash 4+."
        },
        {
            "question": "Vad ger ${path##*/} om path='/home/user/fil.txt'?",
            "options": [
                "home",
                "fil.txt",
                ".txt",
                "/home/user/"
            ],
            "correct": 1,
            "explanation": "## tar bort längsta match från början. */ matchar allt till sista /, kvar blir fil.txt."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
PARAMETRAR_ARRAYS_FLASHCARDS = [
    {"front": "${var:-default} gör?", "back": "Använder default om var är tom"},
    {"front": "${var:=default} gör?", "back": "Sätter OCH använder default om tom"},
    {"front": "${var:?error} gör?", "back": "Visar error och avbryter om tom"},
    {"front": "${var:+value} gör?", "back": "Använder value om var INTE är tom"},
    {"front": "${#var} returnerar?", "back": "Längden på strängen"},
    {"front": "${var%pattern} gör?", "back": "Tar bort kortaste match från SLUTET"},
    {"front": "${var%%pattern} gör?", "back": "Tar bort längsta match från SLUTET"},
    {"front": "${var#pattern} gör?", "back": "Tar bort kortaste match från BÖRJAN"},
    {"front": "${var##pattern} gör?", "back": "Tar bort längsta match från BÖRJAN"},
    {"front": "Skapa array?", "back": "arr=(ett två tre)"},
    {"front": "Första elementet?", "back": "${arr[0]}"},
    {"front": "Alla element?", "back": "${arr[@]}"},
    {"front": "Antal element?", "back": "${#arr[@]}"},
    {"front": "Alla index?", "back": "${!arr[@]}"},
    {"front": "Lägg till i array?", "back": "arr+=(nytt)"},
    {"front": "Ta bort element?", "back": "unset arr[index]"},
    {"front": "shift gör?", "back": "Tar bort $1, skiftar $2→$1"},
    {"front": "shift 2 gör?", "back": "Tar bort $1 och $2"},
    {"front": "Associativ array?", "back": "declare -A arr; arr[nyckel]=\"värde\""},
    {"front": "Minnesregel # vs %?", "back": "# = början (vänster), % = slut (höger)"},
]
