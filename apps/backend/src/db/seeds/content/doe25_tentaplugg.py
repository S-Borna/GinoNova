"""
DOE25 Tentaplugg — 10 noder för Linux/Unix Server & Bash Programming
Täcker alla kursmål, föreläsningar, hands-on och gruppuppgiften (deliverable).

Målgrupp: YH DevOps-studenter inför tenta 7 januari 2026
Nivå: G → VG
"""

MODULE = {
    "id": "doe25-tentaplugg",
    "slug": "doe25-tentaplugg",
    "title": "DOE25 Tentaplugg",
    "description": "Komplett tentaförberedelse för Linux/Unix Server & Bash Programming. Täcker alla kursmål, föreläsningar och gruppuppgiften.",
    "icon": "🎯",
    "difficulty": "intermediate",
    "estimated_hours": 15,
    "order_index": 2,
    "tasks": [
        # =============================================================================
        # NOD 1: Bash Grunder & Shebang
        # =============================================================================
        {
            "title": "Bash Grunder & Shebang",
            "slug": "bash-grunder-shebang",
            "description": "Shebang, chmod +x, variabler och positionsparametrar - grunden för all Bash-scripting.",
            "difficulty": "easy",
            "estimated_minutes": 25,
            "xp_reward": 50,
            "order_index": 1,
            "content": r"""# Bash Grunder & Shebang

> **TL;DR:** Shebang (`#!/bin/bash`) berättar för systemet vilken tolk som kör skriptet. Utan den vet inte OS att filen ska köras med Bash. `chmod +x` gör skriptet körbart.

---

## 🎯 Varför detta är viktigt

I **gruppuppgiften (deliverable)** ska du skriva ett `sys-config.sh` som automatiserar serversetup. Första raden måste vara korrekt shebang, annars fungerar inget.

**Kursmål:** *Skriva bash-skript för att automatisera vanliga uppgifter.*

---

## 📋 Grunden

### Shebang - Skriptets första rad

```bash
#!/bin/bash
```

| Del | Betydelse |
|-----|-----------|
| `#!` | "Shebang" - signalerar att detta är ett skript |
| `/bin/bash` | Sökvägen till tolken (Bash) |

**Utan shebang?** Systemet vet inte hur filen ska köras.

### Skapa ditt första skript

```bash
# 1. Skapa filen
nano myscript.sh

# 2. Lägg till innehåll
#!/bin/bash
echo "Hello from my script!"

# 3. Gör körbar
chmod +x myscript.sh

# 4. Kör
./myscript.sh
```

---

## 📦 Variabler

### Skapa och använda

```bash
# Skapa (INGEN space runt =)
name="Said"
port=6622

# Använd (med $)
echo "User: $name"
echo "SSH port: $port"
```

⚠️ **Vanligt fel:** `name = "Said"` → FEL (spaces runt =)

### Positionsparametrar

När du kör: `./script.sh arg1 arg2 arg3`

| Variabel | Värde |
|----------|-------|
| `$0` | `./script.sh` (skriptnamnet) |
| `$1` | `arg1` |
| `$2` | `arg2` |
| `$3` | `arg3` |
| `$#` | `3` (antal argument) |
| `$@` | Alla argument separat |
| `$*` | Alla argument som en sträng |
| `$?` | Exit-kod från senaste kommando |

**Exempel från gruppuppgiften:**

```bash
#!/bin/bash
# sys-config.sh

echo "Running sys-config..."
echo "Script name: $0"
echo "Number of args: $#"
```

---

## 🔧 Skillnaden mellan "$@" och "$*"

**Viktigt för VG!**

```bash
#!/bin/bash
echo "Med \$@:"
for arg in "$@"; do
    echo "  Argument: $arg"
done

echo "Med \$*:"
for arg in "$*"; do
    echo "  Argument: $arg"
done
```

Kör: `./script.sh "Hello World" "Goodbye"`

| Metod | Resultat |
|-------|----------|
| `"$@"` | 2 iterationer: "Hello World", "Goodbye" |
| `"$*"` | 1 iteration: "Hello World Goodbye" |

**Regel:** Använd alltid `"$@"` när du loopar över argument!

---

## 📋 Copy-Paste Referens

| Uppgift | Kommando |
|---------|----------|
| Skapa skript | `nano script.sh` |
| Lägg till shebang | `#!/bin/bash` (första raden) |
| Gör körbart | `chmod +x script.sh` |
| Kör skript | `./script.sh` |
| Kör med argument | `./script.sh arg1 arg2` |
| Visa alla argument | `echo "$@"` |
| Antal argument | `echo "$#"` |
| Exit-kod senaste | `echo "$?"` |

---

## ✅ Checkpoint

Innan du går vidare, kan du svara på:

1. Vad är en shebang och varför behövs den?
2. Hur gör du ett skript körbart?
3. Vad är skillnaden mellan `$@` och `$*`?
4. Varför får det inte vara mellanslag runt `=` vid variabeltilldelning?

""",
            "quiz": [
                {
                    "question": "Vad gör första raden #!/bin/bash i ett skript?",
                    "options": [
                        "Det är en kommentar som ignoreras",
                        "Den anger vilken tolk (Bash) som ska exekvera skriptet",
                        "Den skapar en ny Bash-process",
                        "Den importerar Bash-biblioteket",
                    ],
                    "correct": 1,
                    "explanation": "Shebang (#!) anger vilken tolk som ska köra skriptet. Utan den vet inte OS hur filen ska exekveras.",
                },
                {
                    "question": "Vilket kommando gör ett skript körbart?",
                    "options": [
                        "chmod -x script.sh",
                        "chmod +r script.sh",
                        "chmod +x script.sh",
                        "chown +x script.sh",
                    ],
                    "correct": 2,
                    "explanation": "chmod +x lägger till execute-permission (x) på filen så den kan köras direkt.",
                },
                {
                    "question": "Om du kör ./script.sh hello world, vad innehåller $2?",
                    "options": ["hello", "world", "./script.sh", "hello world"],
                    "correct": 1,
                    "explanation": "$1 = hello, $2 = world. $0 är skriptnamnet.",
                },
                {
                    "question": 'Vad är FEL med denna rad: name = "Said"',
                    "options": [
                        "Citattecknen är fel typ",
                        "Variabelnamnet är ogiltigt",
                        "Mellanslag runt = är inte tillåtet",
                        "echo saknas",
                    ],
                    "correct": 2,
                    "explanation": 'I Bash får det INTE vara mellanslag runt =. Korrekt: name="Said"',
                },
                {
                    "question": "Vad returnerar $# om du kör ./script.sh a b c?",
                    "options": ["a b c", "3", "./script.sh", "0"],
                    "correct": 1,
                    "explanation": "$# ger antalet argument (exklusive skriptnamnet). Här: 3 stycken.",
                },
                {
                    "question": 'Du ska loopa över argument som kan innehålla mellanslag. Använder du "$@" eller "$*"?',
                    "options": ["$*", '"$*"', "$@", '"$@"'],
                    "correct": 3,
                    "explanation": '"$@" bevarar varje argument separat även om de innehåller mellanslag. "$*" slår ihop allt till en sträng.',
                },
            ],
        },
        # =============================================================================
        # NOD 2: Textbearbetning (grep, sed, awk)
        # =============================================================================
        {
            "title": "Textbearbetning: grep, sed & awk",
            "slug": "textbearbetning-grep-sed-awk",
            "description": "De tre musketererna för textbearbetning - grep söker, sed ersätter, awk analyserar.",
            "difficulty": "medium",
            "estimated_minutes": 35,
            "xp_reward": 75,
            "order_index": 2,
            "content": r"""# Textbearbetning: grep, sed & awk

> **TL;DR:** `grep` hittar rader som matchar mönster. `sed` ersätter text. `awk` är ett programmeringsspråk för kolumnbaserad data. Tillsammans = superkrafter för logganalys och konfigurationsändringar.

---

## 🎯 Varför detta är viktigt

I **gruppuppgiften** behöver du:
- Söka i config-filer (`grep`)
- Ändra SSH-port i sshd_config (`sed`)
- Parsa output från kommandon (`awk`)

**Kursmål:** *Skriva bash-skript för att automatisera vanliga uppgifter* (Kap 4-6 i Bash Book)

---

## 🔍 grep - Sök efter mönster

### Grundläggande syntax

```bash
grep "mönster" fil
```

### Vanliga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-i` | Ignorera skiftläge | `grep -i "error" log.txt` |
| `-r` | Rekursivt i mappar | `grep -r "TODO" ./src/` |
| `-n` | Visa radnummer | `grep -n "Port" sshd_config` |
| `-v` | Invertera (visa EJ matchande) | `grep -v "^#" config` |
| `-c` | Räkna antal matchningar | `grep -c "error" log.txt` |
| `-E` | Extended regex | `grep -E "error|warning" log.txt` |

### Praktiska exempel

```bash
# Hitta alla som får logga in via SSH (från gruppuppgiften)
grep "AllowUsers" /etc/ssh/sshd_config

# Visa aktiva rader i config (ignorera kommentarer)
grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"

# Sök efter "error" ELLER "failed" i loggar
grep -iE "error|failed" /var/log/syslog

# Räkna misslyckade inloggningar
grep -c "Failed password" /var/log/auth.log
```

---

## ✏️ sed - Stream Editor

### Grundläggande syntax

```bash
sed 's/gammalt/nytt/' fil       # Första på varje rad
sed 's/gammalt/nytt/g' fil      # Alla förekomster
sed -i 's/gammalt/nytt/g' fil   # Ändra filen direkt
```

### Vanliga användningar

```bash
# Byt SSH-port (från gruppuppgiften)
sed -i 's/^#Port 22/Port 6622/' /etc/ssh/sshd_config

# Ta bort alla kommentarsrader
sed '/^#/d' config.txt

# Lägg till text i början av varje rad
sed 's/^/PREFIX: /' fil.txt

# Ersätt endast på rad 5
sed '5s/old/new/' fil.txt
```

### Flaggor för sed

| Flagga | Betydelse |
|--------|-----------|
| `-i` | In-place (ändra filen) |
| `-n` | Tysta output |
| `-e` | Flera kommandon |

### Viktigt för gruppuppgiften

```bash
#!/bin/bash
# Konfigurera SSH-porten

SSH_PORT=6622

# Sätt custom port
sed -i "s/^#Port 22/Port $SSH_PORT/" /etc/ssh/sshd_config
sed -i "s/^Port 22/Port $SSH_PORT/" /etc/ssh/sshd_config

# Verifiera
grep "^Port" /etc/ssh/sshd_config
```

---

## 📊 awk - Textanalys & Kolumner

### Grundläggande syntax

```bash
awk '{print $1}' fil     # Skriv ut kolumn 1
awk '{print $NF}' fil    # Skriv ut sista kolumnen
```

### Inbyggda variabler

| Variabel | Betydelse |
|----------|-----------|
| `$0` | Hela raden |
| `$1, $2...` | Kolumn 1, 2, etc. |
| `$NF` | Sista kolumnen |
| `NR` | Radnummer |
| `NF` | Antal kolumner |
| `FS` | Fältseparator (default: space) |

### Praktiska exempel

```bash
# Lista alla användarnamn från /etc/passwd
awk -F: '{print $1}' /etc/passwd

# Visa användare och deras shells
awk -F: '{print $1, $7}' /etc/passwd

# Hitta användare med bash som shell
awk -F: '$7 ~ /bash/ {print $1}' /etc/passwd

# Summera diskutrymme (kolumn 3)
df -h | awk '{print $3}'

# Visa processer som använder mest minne
ps aux | awk '{print $4, $11}' | sort -rn | head -5
```

### Villkor i awk

```bash
# Visa bara rader där kolumn 3 > 100
awk '$3 > 100 {print $0}' data.txt

# Visa användare med UID > 1000
awk -F: '$3 > 1000 {print $1, $3}' /etc/passwd
```

---

## 🔗 Kombinera verktygen

### Pipeline-magi

```bash
# Hitta de 5 vanligaste felen i loggen
grep -i "error" /var/log/syslog | awk '{print $5}' | sort | uniq -c | sort -rn | head -5

# Lista användare i en grupp (från gruppuppgiften)
grep "^devops:" /etc/group | awk -F: '{print $4}'

# Hitta stora filer och visa storlek + namn
find /var/log -type f -size +10M -exec ls -lh {} \; | awk '{print $5, $9}'
```

### Exempel från gruppuppgiften

```bash
#!/bin/bash
# Kontrollera om användare finns

check_user() {
    local username=$1
    if grep -q "^$username:" /etc/passwd; then
        echo "User $username exists"
        # Visa UID och GID
        grep "^$username:" /etc/passwd | awk -F: '{print "UID:", $3, "GID:", $4}'
    else
        echo "User $username does not exist"
    fi
}

check_user "said"
```

---

## 📋 Copy-Paste Referens

| Uppgift | Kommando |
|---------|----------|
| Sök i fil | `grep "mönster" fil` |
| Sök rekursivt | `grep -r "mönster" mapp/` |
| Ignorera skiftläge | `grep -i "mönster" fil` |
| Ersätt text | `sed 's/old/new/g' fil` |
| Ersätt i fil | `sed -i 's/old/new/g' fil` |
| Första kolumnen | `awk '{print $1}' fil` |
| Custom separator | `awk -F: '{print $1}' fil` |
| Filtrera rader | `awk '$3 > 100' fil` |

---

## ✅ Checkpoint

1. Hur söker du case-insensitive med grep?
2. Vad gör `sed -i`?
3. Hur skriver du ut kolumn 3 med awk?
4. Hur anger du kolon som separator i awk?

""",
            "quiz": [
                {
                    "question": "Vilket kommando söker rekursivt i alla filer efter 'error'?",
                    "options": [
                        "grep 'error' *",
                        "grep -r 'error' .",
                        "find . -name 'error'",
                        "search 'error' -r",
                    ],
                    "correct": 1,
                    "explanation": "grep -r söker rekursivt i alla filer från angiven katalog.",
                },
                {
                    "question": "Vad gör kommandot: sed -i 's/22/6622/' sshd_config",
                    "options": [
                        "Visar rader som innehåller 22",
                        "Ersätter första 22 med 6622 direkt i filen",
                        "Skapar en backup av filen",
                        "Tar bort rader med 22",
                    ],
                    "correct": 1,
                    "explanation": "-i betyder in-place edit - filen ändras direkt. s/22/6622/ ersätter första förekomsten av 22 med 6622.",
                },
                {
                    "question": "Hur skriver du ut kolumn 1 och 3 med awk?",
                    "options": [
                        "awk '{print $1 $3}' fil",
                        "awk '{print $1, $3}' fil",
                        "awk -c '1,3' fil",
                        "awk --columns 1,3 fil",
                    ],
                    "correct": 1,
                    "explanation": "awk '{print $1, $3}' skriver ut kolumn 1 och 3 med mellanslag mellan.",
                },
                {
                    "question": "Vad gör grep -v '^#' config.txt?",
                    "options": [
                        "Visar rader som börjar med #",
                        "Visar rader som INTE börjar med #",
                        "Tar bort alla #-tecken",
                        "Räknar rader med #",
                    ],
                    "correct": 1,
                    "explanation": "-v inverterar matchningen. ^# matchar rader som börjar med #. Alltså visas alla rader som INTE börjar med #.",
                },
                {
                    "question": "Hur anger du kolon som fältseparator i awk?",
                    "options": [
                        "awk -s ':' '{print $1}'",
                        "awk -F: '{print $1}'",
                        "awk --sep=: '{print $1}'",
                        "awk ':' '{print $1}'",
                    ],
                    "correct": 1,
                    "explanation": "-F: sätter field separator till kolon. Viktigt för filer som /etc/passwd.",
                },
                {
                    "question": "Vilket kommando räknar antalet rader som matchar 'error' i log.txt?",
                    "options": [
                        "grep -n 'error' log.txt",
                        "grep -c 'error' log.txt",
                        "grep -l 'error' log.txt",
                        "wc -l 'error' log.txt",
                    ],
                    "correct": 1,
                    "explanation": "grep -c (count) returnerar antalet matchande rader, inte raderna själva.",
                },
            ],
        },
        # =============================================================================
        # NOD 3: Kontrollstrukturer & Best Practices
        # =============================================================================
        {
            "title": "Kontrollstrukturer & Best Practices",
            "slug": "kontrollstrukturer-best-practices",
            "description": "if/else, for, while, case - plus set -euo pipefail och shellcheck för robusta skript.",
            "difficulty": "medium",
            "estimated_minutes": 40,
            "xp_reward": 100,
            "order_index": 3,
            "content": r"""# Kontrollstrukturer & Best Practices

> **TL;DR:** `if` testar villkor, `for` loopar över listor, `while` loopar tills villkor är falskt, `case` är switch-sats. Använd alltid `set -euo pipefail` i början av skript. Kör `shellcheck` innan inlämning!

---

## 🎯 Varför detta är viktigt

I **gruppuppgiften** kräver shellcheck-kravet (5.5) att ditt sys-config.sh är felfritt. Du behöver kontrollstrukturer för att:
- Kolla om användare redan finns
- Loopa över gruppmedlemmar
- Hantera fel

**Kursmål:** *Skriva bash-skript för att automatisera vanliga uppgifter* (Kap 7-9 i Bash Book)

---

## 🛡️ Best Practices - Börja ALLTID med detta

### set -euo pipefail

```bash
#!/bin/bash
set -euo pipefail

# Din kod här...
```

| Option | Betydelse |
|--------|-----------|
| `-e` | Avsluta vid första fel (exit on error) |
| `-u` | Fel om odefinierad variabel används |
| `-o pipefail` | Pipeline misslyckas om något steg misslyckas |

**Utan detta:** Skriptet fortsätter köra även om något går fel!

### Shellcheck

```bash
# Installera
sudo apt install shellcheck

# Kör mot ditt skript
shellcheck sys-config.sh

# Ignorera specifik varning (använd SPARSAMT)
# shellcheck disable=SC2086
```

**Gruppuppgiften kräver:** Inga shellcheck-fel eller varningar!

---

## 🔀 if/else/elif

### Grundläggande syntax

```bash
if [ villkor ]; then
    # kod om sant
elif [ annat_villkor ]; then
    # kod om det andra är sant
else
    # kod om inget stämmer
fi
```

### Test-kommandon

| Test | Betydelse |
|------|-----------|
| `[ -f fil ]` | Filen finns |
| `[ -d mapp ]` | Mappen finns |
| `[ -z "$var" ]` | Variabeln är tom |
| `[ -n "$var" ]` | Variabeln är INTE tom |
| `[ "$a" = "$b" ]` | Strängarna är lika |
| `[ "$a" != "$b" ]` | Strängarna är olika |
| `[ $a -eq $b ]` | Numeriskt lika |
| `[ $a -gt $b ]` | Större än |
| `[ $a -lt $b ]` | Mindre än |

### Exempel från gruppuppgiften

```bash
#!/bin/bash
set -euo pipefail

# Kolla om användare finns innan vi skapar
create_user() {
    local username=$1

    if id "$username" &>/dev/null; then
        echo "User $username already exists, skipping..."
    else
        echo "Creating user $username..."
        useradd -m -s /bin/bash "$username"
    fi
}

# Kolla om vi kör som root
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root"
    exit 1
fi
```

### [[ ]] vs [ ]

```bash
# Moderna Bash - använd [[  ]]
if [[ "$string" == *"pattern"* ]]; then
    echo "Pattern found"
fi

# POSIX-kompatibelt - använd [  ]
if [ "$a" = "$b" ]; then
    echo "Equal"
fi
```

**Tips:** `[[ ]]` är säkrare och kraftfullare, men `[ ]` är mer portabelt.

---

## 🔄 for-loopar

### Loopa över lista

```bash
# Loopa över argument
for arg in "$@"; do
    echo "Processing: $arg"
done

# Loopa över array
users=("christian" "cebrail" "baraa" "marcus" "said")
for user in "${users[@]}"; do
    echo "Creating user: $user"
done

# Loopa över sekvens
for i in {1..5}; do
    echo "Iteration $i"
done

# C-style loop
for ((i=0; i<5; i++)); do
    echo "Index: $i"
done
```

### Exempel från gruppuppgiften

```bash
#!/bin/bash
set -euo pipefail

# Gruppmedlemmar (Group 3)
GROUP_MEMBERS=("christian" "cebrail" "baraa" "marcus" "said")
GROUP_NAME="devops-group3"

# Skapa grupp
groupadd "$GROUP_NAME" 2>/dev/null || echo "Group exists"

# Skapa användare och lägg till i grupp
for member in "${GROUP_MEMBERS[@]}"; do
    if ! id "$member" &>/dev/null; then
        useradd -m -s /bin/bash -G "$GROUP_NAME" "$member"
        echo "Created user: $member"
    else
        usermod -aG "$GROUP_NAME" "$member"
        echo "Added existing user $member to group"
    fi
done
```

---

## 🔁 while-loopar

### Grundläggande syntax

```bash
while [ villkor ]; do
    # kod som körs medan villkoret är sant
done
```

### Läsa fil rad för rad

```bash
# Säkert sätt att läsa fil
while IFS= read -r line; do
    echo "Line: $line"
done < "file.txt"

# Läsa från kommando
while IFS= read -r user; do
    echo "User: $user"
done < <(cut -d: -f1 /etc/passwd)
```

### Vänta på tjänst

```bash
# Vänta tills SSH är uppe
while ! systemctl is-active --quiet sshd; do
    echo "Waiting for SSH..."
    sleep 2
done
echo "SSH is running!"
```

---

## 🎯 case-satser

### Grundläggande syntax

```bash
case "$variable" in
    pattern1)
        # kod
        ;;
    pattern2|pattern3)
        # kod för flera mönster
        ;;
    *)
        # default
        ;;
esac
```

### Exempel: Hantera flaggor

```bash
#!/bin/bash
set -euo pipefail

show_help() {
    echo "Usage: $0 [--install|--remove|--status]"
}

case "${1:-}" in
    --install|-i)
        echo "Installing..."
        ;;
    --remove|-r)
        echo "Removing..."
        ;;
    --status|-s)
        echo "Checking status..."
        ;;
    --help|-h)
        show_help
        ;;
    *)
        echo "Unknown option: ${1:-none}"
        show_help
        exit 1
        ;;
esac
```

---

## 📋 Copy-Paste Referens

| Uppgift | Kommando |
|---------|----------|
| Robust skriptstart | `set -euo pipefail` |
| Kolla fil finns | `if [ -f "/path/file" ]; then` |
| Kolla mapp finns | `if [ -d "/path/dir" ]; then` |
| Kolla användare finns | `if id "user" &>/dev/null; then` |
| Loopa över array | `for item in "${array[@]}"; do` |
| Läsa fil rad för rad | `while IFS= read -r line; do ... done < file` |
| Shellcheck | `shellcheck script.sh` |

---

## ✅ Checkpoint

1. Vad gör `set -e` i början av ett skript?
2. Hur testar du om en fil finns?
3. Vad är skillnaden mellan `[ ]` och `[[ ]]`?
4. Hur loopar du över alla element i en array?

""",
            "quiz": [
                {
                    "question": "Vad gör 'set -e' i ett Bash-skript?",
                    "options": [
                        "Aktiverar debug-läge",
                        "Avslutar skriptet vid första fel",
                        "Exporterar alla variabler",
                        "Aktiverar extended globbing",
                    ],
                    "correct": 1,
                    "explanation": "set -e (exit on error) gör att skriptet avslutas omedelbart om ett kommando returnerar icke-noll status.",
                },
                {
                    "question": "Hur testar du om filen /etc/passwd finns?",
                    "options": [
                        "if [ -e /etc/passwd ]",
                        "if [ -f /etc/passwd ]",
                        "if [ -d /etc/passwd ]",
                        "if exists /etc/passwd",
                    ],
                    "correct": 1,
                    "explanation": "-f testar om det är en vanlig fil. -e testar om något finns (fil eller katalog). -d testar om det är en katalog.",
                },
                {
                    "question": "Vilken syntax loopar korrekt över en array i Bash?",
                    "options": [
                        "for item in $array; do",
                        "for item in ${array}; do",
                        'for item in "${array[@]}"; do',
                        "foreach item in array; do",
                    ],
                    "correct": 2,
                    "explanation": "${array[@]} expanderar alla element. Citattecken bevarar element med mellanslag.",
                },
                {
                    "question": "Vad händer om du använder en odefinierad variabel med 'set -u'?",
                    "options": [
                        "Variabeln sätts till tom sträng",
                        "Skriptet skriver en varning",
                        "Skriptet avslutas med fel",
                        "Ingenting speciellt",
                    ],
                    "correct": 2,
                    "explanation": "set -u gör att skriptet avslutas om du försöker använda en variabel som inte är definierad.",
                },
                {
                    "question": "Hur avslutar du en case-gren i Bash?",
                    "options": ["break", ";;", "end", "done"],
                    "correct": 1,
                    "explanation": "I Bash case-satser avslutas varje gren med ;; (dubbla semikolon).",
                },
                {
                    "question": "Vad gör 'id username &>/dev/null' i ett if-villkor?",
                    "options": [
                        "Visar användarens ID",
                        "Testar om användaren finns (utan output)",
                        "Skapar användaren",
                        "Tar bort användaren",
                    ],
                    "correct": 1,
                    "explanation": "id returnerar 0 om användaren finns, icke-noll annars. &>/dev/null döljer all output.",
                },
            ],
        },
        # =============================================================================
        # NOD 4: Funktioner, Arrays & Signals (VG-nivå)
        # =============================================================================
        {
            "title": "Funktioner, Arrays & Signals",
            "slug": "funktioner-arrays-signals",
            "description": "VG-nivå Bash: Funktioner med returvärden, arrays, och signalhantering med trap",
            "difficulty": "advanced",
            "estimated_minutes": 50,
            "xp_reward": 200,
            "order_index": 3,
            "content": """# 🚀 Funktioner, Arrays & Signals (VG-nivå)

> **Bash Book kap 10-12** - Detta är VG-materialet! Behärskar du detta är du redo för de svårare tentafrågorna.

---

## 📋 TL;DR - Det viktigaste

| Koncept | Syntax | Viktigt att veta |
|---------|--------|------------------|
| **Funktion** | `fname() { ... }` | Ingen datatyp, inga parenteser vid anrop |
| **Returvärde** | `return 0-255` | 0 = OK, använd `$?` för att läsa |
| **Output capture** | `result=$(fname)` | Fånga echo/printf från funktion |
| **Array deklaration** | `arr=("a" "b" "c")` | Index börjar på 0 |
| **Alla element** | `"${arr[@]}"` | MED citattecken! |
| **Array längd** | `${#arr[@]}` | Antal element |
| **trap** | `trap 'cmd' SIGNAL` | Körs vid signal |
| **Cleanup** | `trap cleanup EXIT` | Körs alltid vid avslut |

---

## 🔧 Funktioner i Bash

### Grundläggande syntax

```bash
# Två sätt att definiera (båda fungerar)
function my_func {
    echo "Hello from function"
}

my_func() {
    echo "Hello from function"
}

# Anropa (UTAN parenteser!)
my_func
```

### Funktionsargument

```bash
#!/bin/bash
set -euo pipefail

# Funktioner har sina egna $1, $2, $@
greet() {
    local name="$1"      # local = lokal variabel
    local greeting="${2:-Hello}"  # Default om ej angiven
    echo "$greeting, $name!"
}

# Anropa med argument
greet "Anna"              # Output: Hello, Anna!
greet "Erik" "Hej"        # Output: Hej, Erik!
```

### ⚠️ $@ vs $* - TENTAFRÅGA!

```bash
#!/bin/bash
set -euo pipefail

show_args_at() {
    echo "Med \\$@:"
    for arg in "$@"; do
        echo "  Arg: '$arg'"
    done
}

show_args_star() {
    echo "Med \\$*:"
    for arg in "$*"; do
        echo "  Arg: '$arg'"
    done
}

# Test med: ./script.sh "hello world" foo bar
# $@ ger: 3 argument (bevarar citattecken)
# $* ger: 1 argument (allt som en sträng)
```

| Syntax | Beteende | Antal args för "hello world" foo bar |
|--------|----------|--------------------------------------|
| `"$@"` | Bevarar varje argument separat | 3: "hello world", "foo", "bar" |
| `"$*"` | Slår ihop till en sträng | 1: "hello world foo bar" |
| `$@` | Utan quotes, word splitting | Kan bli 4+ beroende på IFS |

### Returvärden

```bash
#!/bin/bash
set -euo pipefail

# Return ger exit status (0-255)
is_valid_user() {
    local username="$1"
    if id "$username" &>/dev/null; then
        return 0   # Success
    else
        return 1   # Failure
    fi
}

# Använd med if
if is_valid_user "root"; then
    echo "User exists"
else
    echo "User does not exist"
fi

# Eller läs $?
is_valid_user "nobody"
status=$?
echo "Exit status was: $status"
```

### Fånga output från funktion

```bash
#!/bin/bash
set -euo pipefail

# Funktion som "returnerar" data via echo
get_hostname() {
    hostname -f
}

# Fånga output med command substitution
my_host=$(get_hostname)
echo "Hostname: $my_host"

# Funktion med beräkning
calculate_sum() {
    local a="$1"
    local b="$2"
    echo $((a + b))  # Aritmetisk expansion
}

result=$(calculate_sum 10 20)
echo "Sum: $result"  # Output: Sum: 30
```

---

## 📦 Arrays (Bash Book kap 11)

### Skapa arrays

```bash
# Indexerade arrays (startar på 0)
fruits=("apple" "banana" "cherry")
numbers=(1 2 3 4 5)

# Lägg till element
fruits+=("date")

# Explicit index
colors[0]="red"
colors[1]="green"
colors[5]="blue"   # Index 2-4 är tomma
```

### Läsa från arrays

```bash
# Ett element
echo "${fruits[0]}"      # apple
echo "${fruits[1]}"      # banana

# ALLA element - MÅSTE ha quotes!
echo "${fruits[@]}"      # apple banana cherry date

# Antal element
echo "${#fruits[@]}"     # 4

# Alla index
echo "${!fruits[@]}"     # 0 1 2 3
```

### Loopa över array

```bash
#!/bin/bash
set -euo pipefail

servers=("web01" "web02" "db01" "cache01")

# RÄTT sätt - med quotes
for server in "${servers[@]}"; do
    echo "Checking: $server"
    ping -c 1 "$server" &>/dev/null && echo "  UP" || echo "  DOWN"
done

# Med index
for i in "${!servers[@]}"; do
    echo "Server $i: ${servers[$i]}"
done
```

### Array manipulation

```bash
#!/bin/bash
set -euo pipefail

arr=("a" "b" "c" "d" "e")

# Slice (start:längd)
echo "${arr[@]:1:3}"    # b c d (från index 1, 3 element)

# Ta bort element
unset 'arr[2]'          # Tar bort index 2
echo "${arr[@]}"        # a b d e (index 2 är borta)

# Ersätt mönster
files=("file1.txt" "file2.txt" "file3.txt")
echo "${files[@]/.txt/.bak}"  # file1.bak file2.bak file3.bak
```

### Associativa arrays (key-value)

```bash
#!/bin/bash
set -euo pipefail

# MÅSTE deklareras med -A
declare -A user_ports

user_ports["web"]="80"
user_ports["ssh"]="22"
user_ports["https"]="443"

# Läs värde
echo "SSH port: ${user_ports[ssh]}"  # 22

# Alla nycklar
echo "Services: ${!user_ports[@]}"   # web ssh https

# Loopa
for service in "${!user_ports[@]}"; do
    echo "$service uses port ${user_ports[$service]}"
done
```

---

## 🚨 Signaler & trap (Bash Book kap 12)

### Vanliga signaler

| Signal | Nummer | Beskrivning | Kan fångas? |
|--------|--------|-------------|-------------|
| `SIGINT` | 2 | Ctrl+C | Ja |
| `SIGTERM` | 15 | kill (default) | Ja |
| `SIGKILL` | 9 | kill -9 | **NEJ** |
| `SIGHUP` | 1 | Terminal stängs | Ja |
| `EXIT` | - | Skript avslutas | Ja |

### trap - fånga signaler

```bash
#!/bin/bash
set -euo pipefail

# Kör kommando vid signal
trap 'echo "Caught SIGINT!"' SIGINT

echo "Press Ctrl+C..."
sleep 60
```

### Cleanup-funktion (VIKTIGT för tentan!)

```bash
#!/bin/bash
set -euo pipefail

TEMP_FILE=""
PID_FILE="/var/run/myapp.pid"

cleanup() {
    echo "Cleaning up..."
    # Ta bort temp-filer
    [[ -n "$TEMP_FILE" && -f "$TEMP_FILE" ]] && rm -f "$TEMP_FILE"
    # Ta bort PID-fil
    [[ -f "$PID_FILE" ]] && rm -f "$PID_FILE"
    echo "Cleanup complete"
}

# Registrera cleanup för EXIT (körs ALLTID)
trap cleanup EXIT

# Nu kan skriptet göra sitt jobb
TEMP_FILE=$(mktemp)
echo "$$" > "$PID_FILE"

echo "Working with temp file: $TEMP_FILE"
# ... gör saker ...

# cleanup() körs automatiskt när skriptet avslutas
```

### Socket-server med signal handling (Deliverable-relevant!)

```bash
#!/bin/bash
set -euo pipefail

# Globala variabler
SOCKET_PATH="/tmp/my_socket.sock"
RUNNING=true

cleanup() {
    echo "Shutting down..."
    RUNNING=false
    [[ -S "$SOCKET_PATH" ]] && rm -f "$SOCKET_PATH"
    # Döda eventuella bakgrundsprocesser
    jobs -p | xargs -r kill 2>/dev/null
    exit 0
}

# Fånga signaler
trap cleanup SIGINT SIGTERM EXIT

# Skapa socket (kräver netcat/socat i praktiken)
echo "Starting server on $SOCKET_PATH"

# Simulerad server-loop
while $RUNNING; do
    echo "Server running... (Ctrl+C to stop)"
    sleep 5
done
```

### Ignore vs Default

```bash
#!/bin/bash

# Ignorera SIGINT (Ctrl+C gör ingenting)
trap '' SIGINT

# Återställ till default
trap - SIGINT

# Ignorera HUP (keep running after logout)
trap '' SIGHUP
```

---

## 🎯 Checkpoint: Kombinerat exempel

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# Komplett skript med funktioner, arrays, trap
# ============================================

declare -a SERVICES=("nginx" "sshd" "docker")
declare -A SERVICE_STATUS
LOG_FILE="/tmp/service_check.log"

# Cleanup function
cleanup() {
    echo "Exiting gracefully..."
    [[ -f "$LOG_FILE" ]] && rm -f "$LOG_FILE"
}
trap cleanup EXIT

# Funktion: Kontrollera tjänst
check_service() {
    local service="$1"
    if systemctl is-active --quiet "$service" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Funktion: Logga meddelande
log_message() {
    local level="$1"
    local message="$2"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $message" >> "$LOG_FILE"
}

# Huvudlogik
main() {
    log_message "INFO" "Starting service check"

    for service in "${SERVICES[@]}"; do
        if check_service "$service"; then
            SERVICE_STATUS["$service"]="UP"
            log_message "INFO" "$service is running"
        else
            SERVICE_STATUS["$service"]="DOWN"
            log_message "WARN" "$service is not running"
        fi
    done

    # Visa resultat
    echo "=== Service Status ==="
    for svc in "${!SERVICE_STATUS[@]}"; do
        printf "%-10s: %s\\n" "$svc" "${SERVICE_STATUS[$svc]}"
    done
}

# Kör main
main "$@"
```

---

## ⚠️ Vanliga fel

| Fel | Problem | Lösning |
|-----|---------|---------|
| `my_func()` vid anrop | Parenteser ska inte vara där | `my_func` |
| `${array[*]}` i for-loop | Blir en sträng | `"${array[@]}"` |
| Glömt `declare -A` | Associativ array fungerar ej | Alltid `declare -A` |
| `return "text"` | Return tar bara 0-255 | Använd `echo` för text |
| Glömt quotes vid `$@` | Word splitting | `"$@"` |
""",
            "quiz": [
                {
                    "question": "Hur anropar du en funktion 'my_func' i Bash?",
                    "options": ["my_func()", "call my_func", "my_func", "$(my_func)"],
                    "correct": 2,
                    "explanation": "I Bash anropas funktioner utan parenteser. my_func() är deklarationssyntax, inte anrop.",
                },
                {
                    "question": 'Vad är skillnaden mellan "$@" och "$*" i en funktion?',
                    "options": [
                        "Ingen skillnad",
                        "$@ bevarar varje argument separat, $* slår ihop till en sträng",
                        "$* bevarar argument, $@ slår ihop",
                        "$@ fungerar bara i funktioner",
                    ],
                    "correct": 1,
                    "explanation": '"$@" expanderar varje argument som separat ord (bevarar quotes), "$*" slår ihop alla till en enda sträng.',
                },
                {
                    "question": "Hur deklarerar du en associativ array i Bash?",
                    "options": [
                        "assoc_array=()",
                        "declare -a assoc_array",
                        "declare -A assoc_array",
                        "array -assoc assoc_array",
                    ],
                    "correct": 2,
                    "explanation": "Associativa arrays MÅSTE deklareras med 'declare -A'. -a är för vanliga indexerade arrays.",
                },
                {
                    "question": "Vad gör 'trap cleanup EXIT'?",
                    "options": [
                        "Kör cleanup() när användaren trycker Ctrl+C",
                        "Kör cleanup() när skriptet avslutas (oavsett hur)",
                        "Kör cleanup() vid SIGKILL",
                        "Definierar en funktion som heter trap",
                    ],
                    "correct": 1,
                    "explanation": "trap med EXIT kör funktionen när skriptet avslutas, oavsett om det är normalt eller via signal (utom SIGKILL).",
                },
                {
                    "question": "Hur får du antalet element i en array 'arr'?",
                    "options": [
                        "len(arr)",
                        "${arr.length}",
                        "${#arr[@]}",
                        "count ${arr[@]}",
                    ],
                    "correct": 2,
                    "explanation": "${#arr[@]} ger antalet element i arrayen. # före variabelnamn ger längden.",
                },
                {
                    "question": "Vilken signal kan INTE fångas med trap?",
                    "options": [
                        "SIGINT (Ctrl+C)",
                        "SIGTERM (kill)",
                        "SIGKILL (kill -9)",
                        "SIGHUP (terminal close)",
                    ],
                    "correct": 2,
                    "explanation": "SIGKILL (signal 9) kan aldrig fångas eller ignoreras. Det är en 'hård' avslutning som OS hanterar direkt.",
                },
            ],
        },
        # =============================================================================
        # NOD 5: Användare, Grupper & Rättigheter
        # =============================================================================
        {
            "title": "Användare, Grupper & Rättigheter",
            "slug": "anvandare-grupper-rattigheter",
            "description": "Hantera användare, grupper, filrättigheter och sudo - kärnan i Linux-administration",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 175,
            "order_index": 4,
            "content": """# 👥 Användare, Grupper & Rättigheter

> **Kursmål:** "Kunskaper om användarhantering och filrättigheter" + "Färdigheter i att konfigurera användarkonton"
>
> **Deliverable 5.1:** Skapa användare och grupper med rätt behörigheter

---

## 📋 TL;DR - Det viktigaste

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `useradd` | Skapa användare | `useradd -m -s /bin/bash user1` |
| `usermod` | Ändra användare | `usermod -aG docker user1` |
| `userdel` | Ta bort användare | `userdel -r user1` |
| `groupadd` | Skapa grupp | `groupadd developers` |
| `passwd` | Sätt lösenord | `passwd user1` |
| `chmod` | Ändra rättigheter | `chmod 755 script.sh` |
| `chown` | Ändra ägare | `chown user:group file` |
| `id` | Visa användarinfo | `id username` |

---

## 👤 Användarhantering

### Skapa användare - useradd

```bash
# Grundläggande (UTAN hemkatalog)
useradd username

# Rekommenderat sätt (MED hemkatalog och shell)
useradd -m -s /bin/bash username

# Alla vanliga flaggor
useradd -m \\
    -s /bin/bash \\
    -c "Full Name" \\
    -G sudo,docker \\
    -d /home/username \\
    username
```

| Flagga | Beskrivning |
|--------|-------------|
| `-m` | Skapa hemkatalog |
| `-s /bin/bash` | Sätt login shell |
| `-c "comment"` | Beskrivning/fullständigt namn |
| `-G group1,group2` | Lägg till i extra grupper |
| `-d /path` | Ange hemkatalog |
| `-e YYYY-MM-DD` | Kontot går ut detta datum |

### Sätt lösenord

```bash
# Interaktivt
passwd username

# Non-interaktivt (för skript) - MINDRE SÄKERT
echo "username:password" | chpasswd

# Tvinga byte vid första login
passwd -e username
```

### Ändra användare - usermod

```bash
# Lägg till i grupp (BEVARA befintliga grupper med -a)
usermod -aG docker username    # -a = append!

# UTAN -a ersätts ALLA grupper!
usermod -G docker username     # ⚠️ Farligt! Tar bort från andra grupper

# Ändra shell
usermod -s /bin/zsh username

# Lås/lås upp konto
usermod -L username    # Lock
usermod -U username    # Unlock
```

### Ta bort användare

```bash
# Behåll hemkatalog
userdel username

# Ta bort ALLT (hemkatalog + mail spool)
userdel -r username
```

---

## 👥 Grupphantering

### Skapa och hantera grupper

```bash
# Skapa grupp
groupadd developers

# Skapa med specifikt GID
groupadd -g 1500 devops

# Ta bort grupp
groupdel developers

# Visa grupps medlemmar
getent group developers
```

### Viktiga filer

| Fil | Innehåll |
|-----|----------|
| `/etc/passwd` | Användarinformation |
| `/etc/shadow` | Krypterade lösenord |
| `/etc/group` | Gruppinformation |
| `/etc/sudoers` | Sudo-behörigheter |

```bash
# Visa användarinfo från passwd
cat /etc/passwd | grep username
# Format: username:x:UID:GID:comment:home:shell

# Visa gruppmedlemskap
groups username
id username
```

---

## 🔒 Filrättigheter

### Förstå rättighetssträngen

```
-rwxr-xr-- 1 owner group 4096 Dec 21 10:00 file.txt
│├─┤├─┤├─┤
│ │  │  └── Others (alla andra)
│ │  └───── Group (gruppmedlemmar)
│ └──────── User/Owner (ägaren)
└────────── Filtyp (- = fil, d = katalog, l = länk)
```

| Tecken | Betydelse | Värde |
|--------|-----------|-------|
| `r` | Read (läsa) | 4 |
| `w` | Write (skriva) | 2 |
| `x` | Execute (köra) | 1 |
| `-` | Ingen behörighet | 0 |

### chmod - Ändra rättigheter

```bash
# Oktalt (vanligast)
chmod 755 script.sh    # rwxr-xr-x
chmod 644 config.txt   # rw-r--r--
chmod 700 private/     # rwx------

# Symboliskt
chmod u+x script.sh    # Lägg till execute för user
chmod g+w file.txt     # Lägg till write för group
chmod o-r file.txt     # Ta bort read för others
chmod a+r file.txt     # Lägg till read för alla (a = all)
```

### Vanliga chmod-värden

| Värde | Rättigheter | Användning |
|-------|-------------|------------|
| `755` | rwxr-xr-x | Skript, program |
| `644` | rw-r--r-- | Vanliga filer |
| `700` | rwx------ | Privata kataloger |
| `600` | rw------- | Känsliga filer (SSH keys) |
| `777` | rwxrwxrwx | ⚠️ UNDVIK! Säkerhetsrisk |

### chown - Ändra ägare

```bash
# Ändra ägare
chown newowner file.txt

# Ändra ägare och grupp
chown newowner:newgroup file.txt

# Bara grupp
chown :newgroup file.txt
# eller
chgrp newgroup file.txt

# Rekursivt (hela katalogen)
chown -R user:group /path/to/dir/
```

---

## 🔑 Speciella rättigheter

### SetUID, SetGID, Sticky Bit

| Bit | Oktalt | Symboliskt | Effekt |
|-----|--------|------------|--------|
| SetUID | 4000 | `u+s` | Kör som filägare |
| SetGID | 2000 | `g+s` | Kör som gruppägare / ärv grupp |
| Sticky | 1000 | `+t` | Bara ägare kan ta bort |

```bash
# SetGID på katalog (VIKTIGT för delad katalog!)
chmod g+s /shared/project/
# Nya filer ärver gruppägaren

# SetGID med oktal
chmod 2775 /shared/project/

# Sticky bit (används på /tmp)
chmod +t /shared/
chmod 1777 /tmp/
```

### SetGID för projektkataloger (Deliverable-relevant!)

```bash
#!/bin/bash
set -euo pipefail

# Skapa delad projektkatalog
PROJECT_DIR="/opt/project"
GROUP_NAME="developers"

# Skapa grupp och katalog
groupadd -f "$GROUP_NAME"
mkdir -p "$PROJECT_DIR"

# Sätt ägare och grupp
chown root:"$GROUP_NAME" "$PROJECT_DIR"

# SetGID + rwx för grupp
chmod 2775 "$PROJECT_DIR"

# Verifiera
ls -ld "$PROJECT_DIR"
# drwxrwsr-x 2 root developers ... /opt/project
#      ^-- 's' = SetGID aktivt
```

---

## 🛡️ Sudo & Sudoers

### Grundläggande sudo

```bash
# Kör som root
sudo command

# Kör som annan användare
sudo -u otheruser command

# Öppna root-shell
sudo -i

# Visa sudo-behörigheter
sudo -l
```

### Redigera sudoers (ALLTID med visudo!)

```bash
# RÄTT sätt - validerar syntax
sudo visudo

# Eller redigera specifik fil
sudo visudo -f /etc/sudoers.d/developers
```

### Sudoers-syntax

```bash
# Format: WHO WHERE=(AS_WHO) WHAT
# username ALL=(ALL:ALL) ALL

# Ge användare full sudo
username ALL=(ALL:ALL) ALL

# Ge grupp sudo (notera %)
%developers ALL=(ALL:ALL) ALL

# Utan lösenord (för automation)
deploy ALL=(ALL) NOPASSWD: ALL

# Specifika kommandon utan lösenord
backup ALL=(ALL) NOPASSWD: /usr/bin/rsync, /usr/bin/tar
```

### Skapa sudoers-fil för grupp

```bash
#!/bin/bash
set -euo pipefail

# Skapa sudoers-fil för developers
cat > /etc/sudoers.d/developers << 'EOF'
# Allow developers group to run specific commands
%developers ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx
%developers ALL=(ALL) NOPASSWD: /usr/bin/docker *
EOF

# Sätt rätt rättigheter (VIKTIGT!)
chmod 440 /etc/sudoers.d/developers

# Validera
visudo -c
```

---

## 🎯 Checkpoint: Deliverable 5.1 Script

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# User & Group Setup Script
# Deliverable 5.1 - DOE25
# ============================================

GROUP_NAME="devops"
USERS=("alice" "bob" "charlie")
PROJECT_DIR="/opt/devops-project"

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Skapa grupp
create_group() {
    if ! getent group "$GROUP_NAME" &>/dev/null; then
        groupadd "$GROUP_NAME"
        log "Created group: $GROUP_NAME"
    else
        log "Group $GROUP_NAME already exists"
    fi
}

# Skapa användare
create_users() {
    for user in "${USERS[@]}"; do
        if ! id "$user" &>/dev/null; then
            useradd -m -s /bin/bash -G "$GROUP_NAME" "$user"
            echo "${user}:ChangeMe123!" | chpasswd
            passwd -e "$user"  # Tvinga lösenordsbyte
            log "Created user: $user"
        else
            usermod -aG "$GROUP_NAME" "$user"
            log "Added existing user $user to $GROUP_NAME"
        fi
    done
}

# Skapa projektkatalog med SetGID
create_project_dir() {
    mkdir -p "$PROJECT_DIR"
    chown root:"$GROUP_NAME" "$PROJECT_DIR"
    chmod 2775 "$PROJECT_DIR"
    log "Created project directory with SetGID: $PROJECT_DIR"
}

# Skapa sudoers-fil
setup_sudoers() {
    local sudoers_file="/etc/sudoers.d/$GROUP_NAME"
    cat > "$sudoers_file" << EOF
# Sudoers for $GROUP_NAME group
%$GROUP_NAME ALL=(ALL) NOPASSWD: /usr/bin/systemctl status *
%$GROUP_NAME ALL=(ALL) NOPASSWD: /usr/bin/docker ps
EOF
    chmod 440 "$sudoers_file"
    visudo -c && log "Sudoers configured successfully"
}

# Main
main() {
    log "Starting user setup..."
    create_group
    create_users
    create_project_dir
    setup_sudoers

    log "=== Setup Complete ==="
    log "Users: ${USERS[*]}"
    log "Group: $GROUP_NAME"
    log "Project: $PROJECT_DIR"

    # Verifiera
    ls -ld "$PROJECT_DIR"
    getent group "$GROUP_NAME"
}

main "$@"
```

---

## ⚠️ Vanliga fel

| Fel | Problem | Lösning |
|-----|---------|---------|
| `usermod -G` utan `-a` | Tar bort från alla grupper | Alltid `usermod -aG` |
| Redigera `/etc/sudoers` direkt | Syntax-fel = ingen sudo | Använd `visudo` |
| `chmod 777` | Säkerhetsrisk | Använd specifika rättigheter |
| Glömt `chmod 440` på sudoers | Sudo ignorerar filen | `chmod 440 /etc/sudoers.d/*` |
| SetGID funkar inte | Glömt 2 i oktalt | `chmod 2775` inte `775` |
""",
            "quiz": [
                {
                    "question": "Vilket kommando skapar en användare MED hemkatalog?",
                    "options": [
                        "useradd username",
                        "useradd -m username",
                        "adduser username",
                        "createuser username",
                    ],
                    "correct": 1,
                    "explanation": "useradd -m skapar hemkatalogen. Utan -m skapas ingen hemkatalog (på de flesta distros).",
                },
                {
                    "question": "Vad händer om du kör 'usermod -G docker username' (utan -a)?",
                    "options": [
                        "Användaren läggs till i docker-gruppen",
                        "Användaren tas bort från alla andra grupper",
                        "Kommandot misslyckas",
                        "Ingenting händer",
                    ],
                    "correct": 1,
                    "explanation": "Utan -a (append) ersätts ALLA sekundära grupper! Alltid använd 'usermod -aG' för att lägga till.",
                },
                {
                    "question": "Vad betyder chmod 755?",
                    "options": ["rwxrwxrwx", "rwxr-xr-x", "rw-r--r--", "rwx------"],
                    "correct": 1,
                    "explanation": "7=rwx (4+2+1), 5=r-x (4+0+1). Så 755 = rwxr-xr-x. Ägare kan allt, andra kan läsa och köra.",
                },
                {
                    "question": "Vad gör SetGID (chmod g+s) på en katalog?",
                    "options": [
                        "Alla kan köra filer i katalogen",
                        "Nya filer ärver katalogens gruppägare",
                        "Bara ägaren kan ta bort filer",
                        "Katalogen blir osynlig",
                    ],
                    "correct": 1,
                    "explanation": "SetGID på katalog gör att nya filer och kataloger ärver gruppägaren, istället för skaparens primära grupp.",
                },
                {
                    "question": "Hur ska du redigera /etc/sudoers?",
                    "options": [
                        "nano /etc/sudoers",
                        "vim /etc/sudoers",
                        "visudo",
                        "sudo edit /etc/sudoers",
                    ],
                    "correct": 2,
                    "explanation": "Alltid använd visudo! Det validerar syntaxen innan sparning. Syntaxfel i sudoers = ingen kan använda sudo.",
                },
                {
                    "question": "Vilken rättighet ska filer i /etc/sudoers.d/ ha?",
                    "options": ["644", "755", "440", "600"],
                    "correct": 2,
                    "explanation": "Sudoers-filer måste ha 440 (r--r-----). Annars ignoreras de av sudo av säkerhetsskäl.",
                },
            ],
        },
        # =============================================================================
        # NOD 6: SSH Mastery & Säkerhet
        # =============================================================================
        {
            "title": "SSH Mastery & Säkerhet",
            "slug": "ssh-mastery-sakerhet",
            "description": "Konfigurera SSH säkert: nycklar, härdning, port 6622 och AllowUsers",
            "difficulty": "intermediate",
            "estimated_minutes": 45,
            "xp_reward": 175,
            "order_index": 5,
            "content": """# 🔐 SSH Mastery & Säkerhet

> **Kursmål:** "Kunskaper om IT-säkerhet" + "Färdigheter i att säkra Linux-system"
>
> **Deliverable 5.2:** Konfigurera SSH på port 6622 med pubkey auth och härdning

---

## 📋 TL;DR - Det viktigaste

| Koncept | Konfiguration | Varför |
|---------|---------------|--------|
| **Ändra port** | `Port 6622` | Undvik automatiska attacker på 22 |
| **Disable root** | `PermitRootLogin no` | Tvinga sudo-användning |
| **Pubkey only** | `PasswordAuthentication no` | Mycket säkrare än lösenord |
| **AllowUsers** | `AllowUsers alice bob` | Whitelist av användare |
| **Key permissions** | `chmod 600 ~/.ssh/id_*` | SSH vägrar annars |

---

## 🔑 SSH-nycklar

### Generera nyckelpar

```bash
# Modern standard (Ed25519 - rekommenderat!)
ssh-keygen -t ed25519 -C "your_email@example.com"

# RSA (om Ed25519 inte stöds)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Med specifikt filnamn
ssh-keygen -t ed25519 -f ~/.ssh/id_server_name -C "server access"
```

### Nyckelfilernas rättigheter (KRITISKT!)

```bash
# SSH VÄGRAR fungera med fel rättigheter!
chmod 700 ~/.ssh              # Katalogen
chmod 600 ~/.ssh/id_*         # Privata nycklar
chmod 644 ~/.ssh/id_*.pub     # Publika nycklar
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
chmod 600 ~/.ssh/config
```

| Fil | Rättighet | Varför |
|-----|-----------|--------|
| `~/.ssh/` | 700 | Bara ägare får access |
| `id_ed25519` | 600 | Privat nyckel - HEMLIG |
| `id_ed25519.pub` | 644 | Publik nyckel - kan delas |
| `authorized_keys` | 600 | Lista på tillåtna nycklar |

### Kopiera publik nyckel till server

```bash
# Automatiskt (bästa sättet)
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Manuellt
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

# Eller kopiera och klistra in
cat ~/.ssh/id_ed25519.pub
# Klistra in i serverns ~/.ssh/authorized_keys
```

---

## ⚙️ SSH Server-konfiguration

### Huvudkonfigfil: /etc/ssh/sshd_config

```bash
# Öppna för redigering
sudo nano /etc/ssh/sshd_config

# Efter ändringar - ALLTID validera först!
sudo sshd -t
# Om ingen output = OK

# Starta om tjänsten
sudo systemctl restart sshd
```

### Härdad konfiguration (Deliverable 5.2)

```bash
# /etc/ssh/sshd_config

# === GRUNDLÄGGANDE HÄRDNING ===

# Byt port (undvik automatiska attacker)
Port 6622

# Protokoll 2 only (1 är osäkert)
Protocol 2

# Disable root login
PermitRootLogin no

# Pubkey authentication (säkrare än lösenord)
PubkeyAuthentication yes

# DISABLE password authentication
PasswordAuthentication no
PermitEmptyPasswords no

# Disable andra osäkra metoder
ChallengeResponseAuthentication no
KerberosAuthentication no
GSSAPIAuthentication no

# === ANVÄNDARBEGRÄNSNING ===

# Whitelist användare (VIKTIGT!)
AllowUsers alice bob deploy

# Eller whitelist grupper
# AllowGroups sshusers admins

# === EXTRA SÄKERHET ===

# Max inloggningsförsök
MaxAuthTries 3

# Idle timeout (sekunder)
ClientAliveInterval 300
ClientAliveCountMax 2

# Disable X11 forwarding (om ej behövs)
X11Forwarding no

# Disable agent forwarding (om ej behövs)
AllowAgentForwarding no

# Logga mer
LogLevel VERBOSE
```

### Steg-för-steg härdning

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# SSH Hardening Script
# Deliverable 5.2 - DOE25
# ============================================

SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP_FILE="/etc/ssh/sshd_config.backup.$(date +%Y%m%d)"
SSH_PORT="6622"
ALLOWED_USERS="alice bob deploy"

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Backup original
backup_config() {
    if [[ ! -f "$BACKUP_FILE" ]]; then
        cp "$SSHD_CONFIG" "$BACKUP_FILE"
        log "Backup created: $BACKUP_FILE"
    fi
}

# Sätt eller uppdatera en SSH-inställning
set_ssh_option() {
    local key="$1"
    local value="$2"

    if grep -q "^${key}" "$SSHD_CONFIG"; then
        # Ersätt existerande
        sed -i "s/^${key}.*/${key} ${value}/" "$SSHD_CONFIG"
    elif grep -q "^#${key}" "$SSHD_CONFIG"; then
        # Avkommentera och sätt
        sed -i "s/^#${key}.*/${key} ${value}/" "$SSHD_CONFIG"
    else
        # Lägg till
        echo "${key} ${value}" >> "$SSHD_CONFIG"
    fi
    log "Set: ${key} ${value}"
}

# Applicera härdning
harden_ssh() {
    log "Applying SSH hardening..."

    set_ssh_option "Port" "$SSH_PORT"
    set_ssh_option "PermitRootLogin" "no"
    set_ssh_option "PasswordAuthentication" "no"
    set_ssh_option "PubkeyAuthentication" "yes"
    set_ssh_option "PermitEmptyPasswords" "no"
    set_ssh_option "MaxAuthTries" "3"
    set_ssh_option "AllowUsers" "$ALLOWED_USERS"
    set_ssh_option "X11Forwarding" "no"
    set_ssh_option "ClientAliveInterval" "300"
    set_ssh_option "ClientAliveCountMax" "2"
}

# Validera och starta om
apply_changes() {
    log "Validating configuration..."
    if sshd -t; then
        log "Configuration valid!"
        systemctl restart sshd
        log "SSH restarted on port $SSH_PORT"
    else
        log "ERROR: Invalid configuration!"
        cp "$BACKUP_FILE" "$SSHD_CONFIG"
        log "Restored backup"
        exit 1
    fi
}

# Main
main() {
    backup_config
    harden_ssh
    apply_changes

    log "=== SSH Hardening Complete ==="
    log "Port: $SSH_PORT"
    log "Allowed users: $ALLOWED_USERS"
    log "Password auth: DISABLED"

    echo ""
    echo "IMPORTANT: Test new connection before closing this session!"
    echo "ssh -p $SSH_PORT user@hostname"
}

main "$@"
```

---

## 🔌 SSH Client-konfiguration

### ~/.ssh/config (SUPER ANVÄNDBART!)

```bash
# Skapa/redigera
nano ~/.ssh/config

# Exempel på konfiguration
Host myserver
    HostName 192.168.1.100
    User deploy
    Port 6622
    IdentityFile ~/.ssh/id_server

Host production
    HostName prod.example.com
    User admin
    Port 22
    IdentityFile ~/.ssh/id_prod
    ForwardAgent no

Host *
    # Defaults för alla hosts
    ServerAliveInterval 60
    ServerAliveCountMax 3
    AddKeysToAgent yes

# Nu kan du ansluta med:
# ssh myserver
# ssh production
```

### Sätt rätt rättigheter

```bash
chmod 600 ~/.ssh/config
```

---

## 🛡️ SSH-säkerhet i praktiken

### Testa före ändringar!

```bash
# INNAN du ändrar - öppna två terminaler!
# Terminal 1: Din aktiva session (stäng INTE!)
# Terminal 2: För att testa

# Efter ändringar, testa från Terminal 2:
ssh -p 6622 user@server

# Om det funkar - nu kan du stänga Terminal 1
```

### Felsökning

```bash
# Verbose SSH-anslutning
ssh -vvv user@server

# Kontrollera SSH-tjänsten
sudo systemctl status sshd
sudo journalctl -u sshd -f

# Kontrollera vad SSH lyssnar på
sudo ss -tlnp | grep ssh
sudo netstat -tlnp | grep sshd

# Kontrollera brandvägg
sudo ufw status
sudo firewall-cmd --list-all
```

### Vanliga fel och lösningar

| Fel | Orsak | Lösning |
|-----|-------|---------|
| Permission denied (publickey) | Fel rättigheter på nycklar | `chmod 600 ~/.ssh/id_*` |
| Connection refused | Fel port eller tjänst nere | Kontrollera port och `systemctl status sshd` |
| Host key verification failed | Serverns nyckel ändrad | Ta bort gammal rad i `known_hosts` |
| Too many authentication failures | För många nycklar/försök | Använd `-i` för specifik nyckel |

---

## 🔒 SSH med nycklar - Komplett flöde

```bash
# ============================================
# 1. PÅ DIN LOKALA MASKIN
# ============================================

# Generera nyckel
ssh-keygen -t ed25519 -f ~/.ssh/id_devops -C "devops-key"

# Kontrollera att nycklarna skapades
ls -la ~/.ssh/id_devops*

# ============================================
# 2. KOPIERA TILL SERVER
# ============================================

# Alternativ A: ssh-copy-id (enklast)
ssh-copy-id -i ~/.ssh/id_devops.pub user@server

# Alternativ B: Manuellt
ssh user@server "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
cat ~/.ssh/id_devops.pub | ssh user@server "cat >> ~/.ssh/authorized_keys"
ssh user@server "chmod 600 ~/.ssh/authorized_keys"

# ============================================
# 3. TESTA
# ============================================

# Ska fungera utan lösenord
ssh -i ~/.ssh/id_devops user@server

# ============================================
# 4. DISABLE PASSWORD AUTH (efter test!)
# ============================================

# På servern:
sudo sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sshd -t && sudo systemctl restart sshd
```

---

## 🎯 Checkpoint: Deliverable 5.2 Verifiering

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# SSH Configuration Verification
# ============================================

echo "=== SSH Configuration Check ==="

# Kontrollera port
port=$(grep "^Port" /etc/ssh/sshd_config | awk '{print $2}')
echo "SSH Port: ${port:-22 (default)}"

# Kontrollera root login
root=$(grep "^PermitRootLogin" /etc/ssh/sshd_config | awk '{print $2}')
echo "Root Login: ${root:-yes (default)}"

# Kontrollera password auth
passwd=$(grep "^PasswordAuthentication" /etc/ssh/sshd_config | awk '{print $2}')
echo "Password Auth: ${passwd:-yes (default)}"

# Kontrollera allowed users
users=$(grep "^AllowUsers" /etc/ssh/sshd_config | cut -d' ' -f2-)
echo "Allowed Users: ${users:-all (default)}"

# Kontrollera vad SSH lyssnar på
echo ""
echo "=== SSH Listening ==="
ss -tlnp | grep ssh || netstat -tlnp | grep ssh

# Kontrollera tjänststatus
echo ""
echo "=== Service Status ==="
systemctl is-active sshd && echo "SSH is running" || echo "SSH is NOT running"

# Säkerhetsstatus
echo ""
echo "=== Security Score ==="
score=0
[[ "${port:-22}" != "22" ]] && ((score++)) && echo "✅ Non-standard port"
[[ "${root:-yes}" == "no" ]] && ((score++)) && echo "✅ Root login disabled"
[[ "${passwd:-yes}" == "no" ]] && ((score++)) && echo "✅ Password auth disabled"
[[ -n "${users:-}" ]] && ((score++)) && echo "✅ User whitelist configured"

echo ""
echo "Security Score: $score/4"
```

---

## ⚠️ Vanliga fel

| Fel | Problem | Lösning |
|-----|---------|---------|
| Låst ute efter ändringar | Password disabled utan nyckel | Använd konsol/rescue mode |
| SSH startar inte | Syntaxfel i config | `sshd -t` för att validera |
| Nyckel fungerar inte | Fel rättigheter | `chmod 600` på privat nyckel |
| AllowUsers fungerar inte | Fel syntax | Mellanslag mellan användare, inte komma |
""",
            "quiz": [
                {
                    "question": "Vilken rättighet ska din privata SSH-nyckel ha?",
                    "options": ["644", "755", "600", "700"],
                    "correct": 2,
                    "explanation": "Privata nycklar MÅSTE ha 600 (rw-------). SSH vägrar använda nycklar med för öppna rättigheter.",
                },
                {
                    "question": "Vilken SSH-inställning disablar root-inloggning?",
                    "options": [
                        "DisableRoot yes",
                        "PermitRootLogin no",
                        "RootLogin false",
                        "AllowRoot no",
                    ],
                    "correct": 1,
                    "explanation": "PermitRootLogin no förhindrar direktinloggning som root. Användare måste logga in som sig själva och sedan använda sudo.",
                },
                {
                    "question": "Hur kopierar du din publika nyckel till en server?",
                    "options": [
                        "scp ~/.ssh/id_ed25519 user@server:",
                        "ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server",
                        "ssh user@server < ~/.ssh/id_ed25519.pub",
                        "cp ~/.ssh/id_ed25519.pub user@server:",
                    ],
                    "correct": 1,
                    "explanation": "ssh-copy-id kopierar den publika nyckeln (.pub) till serverns authorized_keys och sätter rätt rättigheter automatiskt.",
                },
                {
                    "question": "Vad gör 'AllowUsers alice bob' i sshd_config?",
                    "options": [
                        "Skapar användare alice och bob",
                        "Endast alice och bob får logga in via SSH",
                        "alice och bob får root-access",
                        "Blockerar alice och bob",
                    ],
                    "correct": 1,
                    "explanation": "AllowUsers skapar en whitelist - ENDAST listade användare får ansluta via SSH. Alla andra blockeras.",
                },
                {
                    "question": "Vad ska du ALLTID göra innan du stänger SSH-sessionen efter att ha ändrat sshd_config?",
                    "options": [
                        "Köra sudo reboot",
                        "Testa ny anslutning i annan terminal",
                        "Ta bort gamla nycklar",
                        "Ändra root-lösenordet",
                    ],
                    "correct": 1,
                    "explanation": "Testa ALLTID ny anslutning innan du stänger den aktiva sessionen! Annars kan du låsa ut dig själv.",
                },
                {
                    "question": "Hur validerar du sshd_config innan restart?",
                    "options": [
                        "ssh --validate",
                        "sshd -t",
                        "systemctl check sshd",
                        "cat /etc/ssh/sshd_config | validate",
                    ],
                    "correct": 1,
                    "explanation": "sshd -t testar konfigurationen utan att starta om tjänsten. Ingen output = allt OK.",
                },
            ],
        },
        # =============================================================================
        # NOD 7: Brandväggar & Nätverk
        # =============================================================================
        {
            "title": "Brandväggar: UFW & firewalld",
            "slug": "brandvaggar-ufw-firewalld",
            "description": "Konfigurera brandväggar med UFW (Ubuntu) och firewalld (RHEL/Rocky)",
            "difficulty": "intermediate",
            "estimated_minutes": 40,
            "xp_reward": 175,
            "order_index": 6,
            "content": """# 🔥 Brandväggar: UFW & firewalld

> **Kursmål:** "Kunskaper om IT-säkerhet" + "Färdigheter i att säkra Linux-system"
>
> **Deliverable 5.2:** Konfigurera brandvägg för att tillåta endast nödvändiga portar

---

## 📋 TL;DR - Det viktigaste

| Distro | Brandvägg | Aktivera | Öppna port | Status |
|--------|-----------|----------|------------|--------|
| **Ubuntu/Debian** | UFW | `ufw enable` | `ufw allow 22` | `ufw status` |
| **RHEL/Rocky** | firewalld | `systemctl start firewalld` | `firewall-cmd --add-port=22/tcp --permanent` | `firewall-cmd --list-all` |

---

## 🛡️ UFW (Uncomplicated Firewall)

> Ubuntu, Debian och derivat

### Installation och aktivering

```bash
# Installera (ofta förinstallerat)
sudo apt install ufw

# VIKTIGT: Tillåt SSH INNAN du aktiverar!
sudo ufw allow ssh
# eller
sudo ufw allow 22/tcp

# Aktivera brandväggen
sudo ufw enable

# Kontrollera status
sudo ufw status verbose
```

### Grundläggande kommandon

```bash
# Tillåt port
sudo ufw allow 80/tcp          # HTTP
sudo ufw allow 443/tcp         # HTTPS
sudo ufw allow 6622/tcp        # Custom SSH port

# Tillåt tjänst (från /etc/services)
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# Neka port
sudo ufw deny 23/tcp           # Telnet

# Ta bort regel
sudo ufw delete allow 80/tcp

# Visa status
sudo ufw status numbered       # Med radnummer
sudo ufw status verbose        # Detaljerad
```

### UFW med specifika IP-adresser

```bash
# Tillåt från specifik IP
sudo ufw allow from 192.168.1.100

# Tillåt från subnet
sudo ufw allow from 192.168.1.0/24

# Tillåt från IP till specifik port
sudo ufw allow from 192.168.1.100 to any port 22

# Tillåt från subnet till port
sudo ufw allow from 10.0.0.0/8 to any port 3306
```

### Default policies

```bash
# Se nuvarande policies
sudo ufw status verbose

# Sätt default (rekommenderat)
sudo ufw default deny incoming   # Blockera allt inkommande
sudo ufw default allow outgoing  # Tillåt allt utgående

# Striktare (för servrar)
sudo ufw default deny outgoing   # Blockera även utgående
sudo ufw allow out 80/tcp        # Tillåt HTTP ut
sudo ufw allow out 443/tcp       # Tillåt HTTPS ut
sudo ufw allow out 53            # Tillåt DNS ut
```

### UFW - Komplett serversetup

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# UFW Firewall Setup
# ============================================

log() {
    echo "[UFW] $1"
}

# Reset (om du vill börja om)
# sudo ufw --force reset

log "Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

log "Allowing SSH (port 6622)..."
sudo ufw allow 6622/tcp comment 'SSH custom port'

log "Allowing HTTP/HTTPS..."
sudo ufw allow 80/tcp comment 'HTTP'
sudo ufw allow 443/tcp comment 'HTTPS'

log "Allowing Docker ports from internal network..."
sudo ufw allow from 172.16.0.0/12 to any port 2375 comment 'Docker internal'

log "Enabling UFW..."
sudo ufw --force enable

log "Final status:"
sudo ufw status verbose
```

---

## 🔥 firewalld (RHEL/Rocky/CentOS)

> Red Hat, Rocky Linux, CentOS, Fedora

### Installation och aktivering

```bash
# Installera
sudo dnf install firewalld

# Starta och aktivera
sudo systemctl start firewalld
sudo systemctl enable firewalld

# Kontrollera status
sudo systemctl status firewalld
sudo firewall-cmd --state
```

### Zoner i firewalld

| Zon | Beskrivning | Default trust |
|-----|-------------|---------------|
| `drop` | Droppa allt inkommande | Ingen |
| `block` | Avvisa med meddelande | Ingen |
| `public` | Offentliga nätverk | Låg |
| `work` | Arbetsnätverk | Medium |
| `home` | Hemnätverk | Medium |
| `trusted` | Lita på allt | Full |

```bash
# Visa aktiv zon
firewall-cmd --get-active-zones

# Visa default zon
firewall-cmd --get-default-zone

# Sätt default zon
sudo firewall-cmd --set-default-zone=public

# Lista alla zoner
firewall-cmd --get-zones
```

### Grundläggande kommandon

```bash
# === TILLFÄLLIGA REGLER (försvinner vid restart) ===
sudo firewall-cmd --add-port=80/tcp
sudo firewall-cmd --add-service=http

# === PERMANENTA REGLER (--permanent) ===
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-port=6622/tcp

# VIKTIGT: Reload efter permanenta ändringar!
sudo firewall-cmd --reload

# === TA BORT REGLER ===
sudo firewall-cmd --permanent --remove-port=80/tcp
sudo firewall-cmd --permanent --remove-service=http
sudo firewall-cmd --reload
```

### Visa konfiguration

```bash
# Visa allt i aktiv zon
sudo firewall-cmd --list-all

# Visa specifik zon
sudo firewall-cmd --zone=public --list-all

# Visa endast portar
sudo firewall-cmd --list-ports

# Visa endast tjänster
sudo firewall-cmd --list-services
```

### Rich rules (avancerat)

```bash
# Tillåt från specifik IP
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" accept'

# Tillåt port från subnet
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" port port="3306" protocol="tcp" accept'

# Neka specifik IP
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.50" reject'

# Logga och droppa
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.50" log prefix="BLOCKED: " level="warning" drop'

# Reload!
sudo firewall-cmd --reload
```

### firewalld - Komplett serversetup

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# firewalld Setup Script
# ============================================

log() {
    echo "[firewalld] $1"
}

# Starta firewalld om det inte kör
if ! systemctl is-active --quiet firewalld; then
    log "Starting firewalld..."
    sudo systemctl start firewalld
    sudo systemctl enable firewalld
fi

log "Setting default zone to public..."
sudo firewall-cmd --set-default-zone=public

log "Adding SSH on custom port 6622..."
sudo firewall-cmd --permanent --add-port=6622/tcp

log "Adding HTTP and HTTPS..."
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https

log "Removing default SSH (port 22) if present..."
sudo firewall-cmd --permanent --remove-service=ssh 2>/dev/null || true

log "Adding Docker network access..."
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="172.16.0.0/12" accept'

log "Reloading firewall..."
sudo firewall-cmd --reload

log "Final configuration:"
sudo firewall-cmd --list-all
```

---

## 📊 UFW vs firewalld - Jämförelse

| Uppgift | UFW | firewalld |
|---------|-----|-----------|
| Öppna port 80 | `ufw allow 80/tcp` | `firewall-cmd --permanent --add-port=80/tcp && firewall-cmd --reload` |
| Öppna tjänst | `ufw allow http` | `firewall-cmd --permanent --add-service=http && firewall-cmd --reload` |
| Status | `ufw status` | `firewall-cmd --list-all` |
| Aktivera | `ufw enable` | `systemctl start firewalld` |
| Disable | `ufw disable` | `systemctl stop firewalld` |
| Från IP | `ufw allow from 1.2.3.4` | `--add-rich-rule='...'` |

---

## 🌐 Nätverkskommandon (bonus)

### Visa nätverksstatus

```bash
# Visa lyssnande portar
ss -tlnp                    # TCP
ss -ulnp                    # UDP
ss -tulnp                   # Båda

# Äldre alternativ
netstat -tlnp

# Visa alla anslutningar
ss -tan

# Visa routing
ip route
# eller
route -n

# Visa IP-adresser
ip addr
# eller
ip a
```

### Testa anslutningar

```bash
# Testa om port är öppen
nc -zv hostname 22
nc -zv hostname 80

# Testa med timeout
timeout 5 bash -c "</dev/tcp/hostname/22" && echo "Open" || echo "Closed"

# Visa vilken process använder port
sudo lsof -i :80
sudo fuser 80/tcp
```

---

## 🎯 Checkpoint: Deliverable 5.2 Brandväggssetup

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# Firewall Setup - Works on Ubuntu/Rocky
# Deliverable 5.2 - DOE25
# ============================================

SSH_PORT="6622"
WEB_PORTS=("80" "443")

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Detektera distro och brandvägg
detect_firewall() {
    if command -v ufw &>/dev/null; then
        echo "ufw"
    elif command -v firewall-cmd &>/dev/null; then
        echo "firewalld"
    else
        echo "none"
    fi
}

# UFW setup
setup_ufw() {
    log "Configuring UFW..."

    # Default policies
    sudo ufw default deny incoming
    sudo ufw default allow outgoing

    # SSH
    sudo ufw allow "$SSH_PORT/tcp" comment 'SSH'

    # Web
    for port in "${WEB_PORTS[@]}"; do
        sudo ufw allow "$port/tcp"
    done

    # Aktivera
    sudo ufw --force enable

    log "UFW Status:"
    sudo ufw status numbered
}

# firewalld setup
setup_firewalld() {
    log "Configuring firewalld..."

    # Starta om ej igång
    sudo systemctl start firewalld
    sudo systemctl enable firewalld

    # SSH på custom port
    sudo firewall-cmd --permanent --add-port="$SSH_PORT/tcp"

    # Ta bort default SSH
    sudo firewall-cmd --permanent --remove-service=ssh 2>/dev/null || true

    # Web
    sudo firewall-cmd --permanent --add-service=http
    sudo firewall-cmd --permanent --add-service=https

    # Reload
    sudo firewall-cmd --reload

    log "firewalld Status:"
    sudo firewall-cmd --list-all
}

# Main
main() {
    fw=$(detect_firewall)
    log "Detected firewall: $fw"

    case "$fw" in
        ufw)
            setup_ufw
            ;;
        firewalld)
            setup_firewalld
            ;;
        *)
            log "ERROR: No supported firewall found!"
            exit 1
            ;;
    esac

    log "=== Firewall Setup Complete ==="
    log "SSH Port: $SSH_PORT"
    log "Web Ports: ${WEB_PORTS[*]}"
}

main "$@"
```

---

## ⚠️ Vanliga fel

| Fel | Problem | Lösning |
|-----|---------|---------|
| Låst ute | Aktiverade brandvägg utan SSH-regel | Använd konsol/VNC |
| Regel fungerar inte (firewalld) | Glömde `--permanent` eller `--reload` | Lägg till båda |
| Port öppen men ingen anslutning | Tjänsten lyssnar inte | Kolla med `ss -tlnp` |
| UFW status inactive | Brandväggen ej aktiverad | `ufw enable` |
""",
            "quiz": [
                {
                    "question": "Vad måste du göra INNAN du aktiverar UFW första gången?",
                    "options": [
                        "Starta om servern",
                        "Tillåta SSH-porten",
                        "Installera nginx",
                        "Skapa ny användare",
                    ],
                    "correct": 1,
                    "explanation": "Alltid tillåt SSH innan du aktiverar UFW! Annars låser du ut dig själv från servern.",
                },
                {
                    "question": "Hur öppnar du port 80 permanent i firewalld?",
                    "options": [
                        "firewall-cmd --add-port=80/tcp",
                        "firewall-cmd --permanent --add-port=80/tcp && firewall-cmd --reload",
                        "firewalld open 80",
                        "systemctl allow 80",
                    ],
                    "correct": 1,
                    "explanation": "Du behöver --permanent för att spara och --reload för att aktivera. Utan --permanent försvinner regeln vid restart.",
                },
                {
                    "question": "Vilket kommando visar UFW-status med radnummer?",
                    "options": [
                        "ufw status",
                        "ufw status numbered",
                        "ufw list",
                        "ufw show rules",
                    ],
                    "correct": 1,
                    "explanation": "ufw status numbered visar alla regler med nummer, vilket gör det enkelt att ta bort specifika regler.",
                },
                {
                    "question": "Hur visar du alla brandväggsregler i firewalld?",
                    "options": [
                        "firewall-cmd --status",
                        "firewall-cmd --list-all",
                        "firewalld show",
                        "systemctl status firewalld",
                    ],
                    "correct": 1,
                    "explanation": "firewall-cmd --list-all visar alla regler, portar, tjänster och rich rules i den aktiva zonen.",
                },
                {
                    "question": "Vilka är rekommenderade default policies för en server?",
                    "options": [
                        "allow incoming, allow outgoing",
                        "deny incoming, deny outgoing",
                        "deny incoming, allow outgoing",
                        "allow incoming, deny outgoing",
                    ],
                    "correct": 2,
                    "explanation": "deny incoming (blockera allt in) + allow outgoing (tillåt allt ut) är standard för servrar. Sedan öppnar du specifika portar.",
                },
                {
                    "question": "Vilket kommando visar vilka portar som lyssnar på systemet?",
                    "options": [
                        "ps aux",
                        "ss -tlnp",
                        "cat /etc/services",
                        "ufw status",
                    ],
                    "correct": 1,
                    "explanation": "ss -tlnp visar TCP-portar som lyssnar (-t), med portnummer (-n), och vilken process (-p). Alternativt netstat -tlnp.",
                },
            ],
        },
        # =============================================================================
        # NOD 8: Lagring - Block Storage, LUKS & systemd
        # =============================================================================
        {
            "title": "Lagring: Block Storage, LUKS & systemd",
            "slug": "lagring-block-storage-luks-systemd",
            "description": "Hantera block storage, kryptering med LUKS, och skapa systemd service-filer",
            "difficulty": "advanced",
            "estimated_minutes": 50,
            "xp_reward": 200,
            "order_index": 7,
            "content": """# 💾 Lagring: Block Storage, LUKS & systemd

> **Kursmål:** "Kunskaper om Linux-systemadministration" + "Färdigheter i att hantera lagring"
>
> **Deliverable 5.3:** Konfigurera block storage med kryptering och skapa systemd services

---

## 📋 TL;DR - Det viktigaste

| Koncept | Kommando | Beskrivning |
|---------|----------|-------------|
| **Lista diskar** | `lsblk` | Visa alla block devices |
| **Partitionera** | `fdisk /dev/sdb` | Skapa partitioner |
| **Formatera** | `mkfs.ext4 /dev/sdb1` | Skapa filsystem |
| **Mounta** | `mount /dev/sdb1 /mnt/data` | Anslut filsystem |
| **LUKS skapa** | `cryptsetup luksFormat /dev/sdb1` | Kryptera partition |
| **LUKS öppna** | `cryptsetup open /dev/sdb1 mydata` | Lås upp |
| **systemd service** | `/etc/systemd/system/app.service` | Service-fil |

---

## 💿 Block Storage Basics

### Visa diskar och partitioner

```bash
# Lista alla block devices (BÄSTA kommandot!)
lsblk
# Exempel output:
# NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
# sda      8:0    0   50G  0 disk
# ├─sda1   8:1    0    1G  0 part /boot
# └─sda2   8:2    0   49G  0 part /
# sdb      8:16   0  100G  0 disk

# Med mer detaljer
lsblk -f    # Visa filsystem
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE

# Visa diskinfo
sudo fdisk -l
sudo fdisk -l /dev/sdb

# Visa partitioner
cat /proc/partitions
```

### Partitionera disk med fdisk

```bash
# Starta fdisk
sudo fdisk /dev/sdb

# Vanliga fdisk-kommandon:
# n = new partition (skapa ny)
# p = print (visa partitioner)
# d = delete (ta bort)
# t = type (ändra partitionstyp)
# w = write (spara och avsluta)
# q = quit (avsluta utan att spara)

# Exempel: Skapa en partition som täcker hela disken
# n -> p -> 1 -> Enter -> Enter -> w
```

### Skapa filsystem

```bash
# ext4 (rekommenderat för Linux)
sudo mkfs.ext4 /dev/sdb1

# Med label
sudo mkfs.ext4 -L "mydata" /dev/sdb1

# XFS (bra för stora filer)
sudo mkfs.xfs /dev/sdb1

# Visa filsysteminfo
sudo blkid /dev/sdb1
```

### Mounta filsystem

```bash
# Skapa mount point
sudo mkdir -p /mnt/data

# Mounta
sudo mount /dev/sdb1 /mnt/data

# Verifiera
df -h /mnt/data
mount | grep sdb1

# Unmounta
sudo umount /mnt/data
```

### Permanent mount i /etc/fstab

```bash
# Hämta UUID (säkrare än device name)
sudo blkid /dev/sdb1
# Output: /dev/sdb1: UUID="abc123..." TYPE="ext4"

# Redigera fstab
sudo nano /etc/fstab

# Lägg till rad:
# UUID=abc123...  /mnt/data  ext4  defaults  0  2

# Testa utan reboot
sudo mount -a

# Format för fstab:
# <device/UUID>  <mount point>  <type>  <options>  <dump>  <pass>
```

---

## 🔐 LUKS - Disk Encryption

### Vad är LUKS?

**L**inux **U**nified **K**ey **S**etup - Standard för diskkryptering i Linux.

### Skapa krypterad partition

```bash
#!/bin/bash
set -euo pipefail

DEVICE="/dev/sdb1"
MAPPER_NAME="encrypted_data"
MOUNT_POINT="/mnt/secure"

# 1. Skapa LUKS-container (VARNING: Raderar all data!)
sudo cryptsetup luksFormat "$DEVICE"
# Du måste skriva YES och ange passphrase

# 2. Öppna den krypterade volymen
sudo cryptsetup open "$DEVICE" "$MAPPER_NAME"
# Nu finns /dev/mapper/encrypted_data

# 3. Skapa filsystem på den dekrypterade volymen
sudo mkfs.ext4 "/dev/mapper/$MAPPER_NAME"

# 4. Mounta
sudo mkdir -p "$MOUNT_POINT"
sudo mount "/dev/mapper/$MAPPER_NAME" "$MOUNT_POINT"

echo "Encrypted volume mounted at $MOUNT_POINT"
```

### Hantera LUKS-volymer

```bash
# Öppna (unlock)
sudo cryptsetup open /dev/sdb1 mydata
# Skapar /dev/mapper/mydata

# Stäng (lock)
sudo umount /mnt/secure
sudo cryptsetup close mydata

# Visa status
sudo cryptsetup status mydata

# Visa LUKS header info
sudo cryptsetup luksDump /dev/sdb1
```

### LUKS med keyfile (för automation)

```bash
#!/bin/bash
set -euo pipefail

DEVICE="/dev/sdb1"
KEYFILE="/root/.luks-keyfile"

# Skapa keyfile (256 bytes random data)
sudo dd if=/dev/urandom of="$KEYFILE" bs=256 count=1
sudo chmod 400 "$KEYFILE"

# Lägg till keyfile som alternativ nyckel
sudo cryptsetup luksAddKey "$DEVICE" "$KEYFILE"

# Nu kan du öppna med keyfile istället för passphrase
sudo cryptsetup open "$DEVICE" mydata --key-file "$KEYFILE"
```

### Auto-mount krypterad volym vid boot

```bash
# 1. Lägg till i /etc/crypttab
# <name>  <device>  <keyfile>  <options>
# mydata  UUID=xxx  /root/.luks-keyfile  luks

# 2. Lägg till i /etc/fstab
# /dev/mapper/mydata  /mnt/secure  ext4  defaults  0  2

# Hämta UUID för crypttab:
sudo cryptsetup luksDump /dev/sdb1 | grep UUID
```

---

## ⚙️ systemd Services

### Service-fil struktur

```ini
# /etc/systemd/system/myapp.service

[Unit]
Description=My Application Service
After=network.target
Wants=network-online.target

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
ExecStop=/opt/myapp/stop.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Service Types

| Type | Beskrivning | Användning |
|------|-------------|------------|
| `simple` | Default, processen är tjänsten | De flesta applikationer |
| `forking` | Processen forkar, parent avslutas | Traditionella daemons |
| `oneshot` | Kör en gång, avslutas | Scripts, setup tasks |
| `notify` | Som simple, men skickar signal | systemd-aware apps |

### Skapa en enkel service

```bash
#!/bin/bash
set -euo pipefail

# Skapa service-fil
sudo cat > /etc/systemd/system/mywebapp.service << 'EOF'
[Unit]
Description=My Web Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/python3 /var/www/myapp/app.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

# Säkerhetsinställningar
NoNewPrivileges=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF

# Ladda om systemd
sudo systemctl daemon-reload

# Aktivera och starta
sudo systemctl enable mywebapp
sudo systemctl start mywebapp

# Kontrollera status
sudo systemctl status mywebapp
```

### systemctl kommandon

```bash
# Start/Stop/Restart
sudo systemctl start myapp
sudo systemctl stop myapp
sudo systemctl restart myapp
sudo systemctl reload myapp      # Ladda om config utan restart

# Enable/Disable (autostart)
sudo systemctl enable myapp      # Starta vid boot
sudo systemctl disable myapp     # Starta INTE vid boot

# Status och info
systemctl status myapp
systemctl is-active myapp
systemctl is-enabled myapp
systemctl show myapp             # Alla properties

# Lista tjänster
systemctl list-units --type=service
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service

# Efter ändringar i service-fil
sudo systemctl daemon-reload

# Loggar
journalctl -u myapp              # Alla loggar
journalctl -u myapp -f           # Follow (live)
journalctl -u myapp --since today
journalctl -u myapp -n 50        # Senaste 50 rader
```

### Service med environment variables

```ini
[Service]
# Direkt i service-filen
Environment="PORT=8080"
Environment="DB_HOST=localhost"

# Eller från fil
EnvironmentFile=/etc/myapp/config.env
```

---

## 🎯 Checkpoint: Deliverable 5.3

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# Block Storage + LUKS + systemd Setup
# Deliverable 5.3 - DOE25
# ============================================

# Variabler
DEVICE="/dev/sdb"
PARTITION="${DEVICE}1"
LUKS_NAME="appdata"
MOUNT_POINT="/opt/appdata"
KEYFILE="/root/.luks-key"
SERVICE_NAME="myapp"

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# ============================================
# 1. BLOCK STORAGE SETUP
# ============================================
setup_storage() {
    log "Setting up block storage..."

    # Skapa partition (hela disken)
    echo -e "n\\np\\n1\\n\\n\\nw" | sudo fdisk "$DEVICE" || true

    # Vänta på kernel
    sudo partprobe "$DEVICE"
    sleep 2

    log "Partition created: $PARTITION"
}

# ============================================
# 2. LUKS ENCRYPTION
# ============================================
setup_luks() {
    log "Setting up LUKS encryption..."

    # Skapa keyfile
    if [[ ! -f "$KEYFILE" ]]; then
        sudo dd if=/dev/urandom of="$KEYFILE" bs=256 count=1 2>/dev/null
        sudo chmod 400 "$KEYFILE"
        log "Keyfile created: $KEYFILE"
    fi

    # Formatera med LUKS (keyfile istället för passphrase)
    sudo cryptsetup luksFormat --batch-mode "$PARTITION" "$KEYFILE"
    log "LUKS formatted: $PARTITION"

    # Öppna
    sudo cryptsetup open "$PARTITION" "$LUKS_NAME" --key-file "$KEYFILE"
    log "LUKS opened: /dev/mapper/$LUKS_NAME"

    # Skapa filsystem
    sudo mkfs.ext4 -L "$LUKS_NAME" "/dev/mapper/$LUKS_NAME"
    log "Filesystem created"

    # Mounta
    sudo mkdir -p "$MOUNT_POINT"
    sudo mount "/dev/mapper/$LUKS_NAME" "$MOUNT_POINT"
    log "Mounted at: $MOUNT_POINT"
}

# ============================================
# 3. SYSTEMD SERVICE
# ============================================
create_service() {
    log "Creating systemd service..."

    # Skapa app-katalog och script
    sudo mkdir -p "$MOUNT_POINT/app"

    sudo cat > "$MOUNT_POINT/app/run.sh" << 'SCRIPT'
#!/bin/bash
echo "Application started at $(date)"
while true; do
    echo "Running... $(date)"
    sleep 60
done
SCRIPT
    sudo chmod +x "$MOUNT_POINT/app/run.sh"

    # Skapa service-fil
    sudo cat > "/etc/systemd/system/${SERVICE_NAME}.service" << EOF
[Unit]
Description=My Application on Encrypted Storage
After=network.target
Requires=dev-mapper-${LUKS_NAME}.device

[Service]
Type=simple
User=root
WorkingDirectory=${MOUNT_POINT}/app
ExecStart=${MOUNT_POINT}/app/run.sh
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

    # Aktivera
    sudo systemctl daemon-reload
    sudo systemctl enable "$SERVICE_NAME"
    sudo systemctl start "$SERVICE_NAME"

    log "Service created and started: $SERVICE_NAME"
}

# ============================================
# 4. SETUP CRYPTTAB & FSTAB
# ============================================
setup_automount() {
    log "Setting up auto-mount..."

    # Hämta UUID
    local uuid=$(sudo cryptsetup luksDump "$PARTITION" | grep "UUID" | head -1 | awk '{print $2}')

    # crypttab
    echo "${LUKS_NAME}  UUID=${uuid}  ${KEYFILE}  luks" | sudo tee -a /etc/crypttab

    # fstab
    echo "/dev/mapper/${LUKS_NAME}  ${MOUNT_POINT}  ext4  defaults  0  2" | sudo tee -a /etc/fstab

    log "Auto-mount configured"
}

# ============================================
# 5. VERIFICATION
# ============================================
verify() {
    echo ""
    echo "=== VERIFICATION ==="
    echo ""

    echo "Block device:"
    lsblk "$DEVICE"
    echo ""

    echo "LUKS status:"
    sudo cryptsetup status "$LUKS_NAME"
    echo ""

    echo "Mount:"
    df -h "$MOUNT_POINT"
    echo ""

    echo "Service status:"
    systemctl status "$SERVICE_NAME" --no-pager
    echo ""

    echo "Recent logs:"
    journalctl -u "$SERVICE_NAME" -n 5 --no-pager
}

# Main
main() {
    log "=== Starting Deliverable 5.3 Setup ==="

    setup_storage
    setup_luks
    create_service
    setup_automount
    verify

    log "=== Setup Complete ==="
}

# Kör bara om vi är root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

main "$@"
```

---

## 📚 Snabbreferens

### Block Storage

```bash
lsblk                          # Lista diskar
sudo fdisk /dev/sdb            # Partitionera
sudo mkfs.ext4 /dev/sdb1       # Formatera
sudo mount /dev/sdb1 /mnt/data # Mounta
sudo blkid                     # Visa UUID:s
```

### LUKS

```bash
sudo cryptsetup luksFormat /dev/sdb1           # Kryptera
sudo cryptsetup open /dev/sdb1 name            # Öppna
sudo cryptsetup close name                     # Stäng
sudo cryptsetup luksDump /dev/sdb1             # Info
```

### systemd

```bash
sudo systemctl start|stop|restart service
sudo systemctl enable|disable service
sudo systemctl status service
sudo systemctl daemon-reload
journalctl -u service -f
```

---

## ⚠️ Vanliga fel

| Fel | Problem | Lösning |
|-----|---------|---------|
| Device busy | Disken används | `umount` först, kolla `lsof` |
| LUKS won't open | Fel passphrase/keyfile | Kontrollera keyfile path och permissions |
| Service failed | Fel i service-fil | `journalctl -u service` för detaljer |
| Mount fail after reboot | Fel i fstab | Boot i rescue mode, fixa fstab |
| daemon-reload glömt | Service-ändringar syns ej | Alltid `systemctl daemon-reload` |
""",
            "quiz": [
                {
                    "question": "Vilket kommando visar alla block devices och deras mount points?",
                    "options": ["df -h", "lsblk", "fdisk -l", "mount"],
                    "correct": 1,
                    "explanation": "lsblk visar en hierarkisk vy av alla block devices med storlek, typ och mount points.",
                },
                {
                    "question": "Vad gör 'cryptsetup open /dev/sdb1 mydata'?",
                    "options": [
                        "Krypterar partitionen",
                        "Formaterar partitionen",
                        "Dekrypterar och gör volymen tillgänglig som /dev/mapper/mydata",
                        "Monterar partitionen",
                    ],
                    "correct": 2,
                    "explanation": "cryptsetup open låser upp en LUKS-krypterad volym och skapar en device mapper på /dev/mapper/<name>.",
                },
                {
                    "question": "Var placerar du dina egna systemd service-filer?",
                    "options": [
                        "/lib/systemd/system/",
                        "/etc/systemd/system/",
                        "/usr/lib/systemd/",
                        "/var/systemd/services/",
                    ],
                    "correct": 1,
                    "explanation": "/etc/systemd/system/ är för användarskapade services. /lib/systemd/system/ är för paket-installerade.",
                },
                {
                    "question": "Vad måste du köra efter att ha ändrat en service-fil?",
                    "options": [
                        "systemctl restart",
                        "systemctl reload",
                        "systemctl daemon-reload",
                        "service reload",
                    ],
                    "correct": 2,
                    "explanation": "systemctl daemon-reload gör att systemd läser in ändrade service-filer. Sedan kan du restart:a tjänsten.",
                },
                {
                    "question": "Vilken fil konfigurerar automatisk LUKS-öppning vid boot?",
                    "options": [
                        "/etc/fstab",
                        "/etc/crypttab",
                        "/etc/luks.conf",
                        "/etc/systemd/luks",
                    ],
                    "correct": 1,
                    "explanation": "/etc/crypttab konfigurerar vilka LUKS-volymer som ska öppnas vid boot och med vilken nyckel.",
                },
                {
                    "question": "Hur visar du live-loggar för en systemd service?",
                    "options": [
                        "tail -f /var/log/service.log",
                        "systemctl logs -f service",
                        "journalctl -u service -f",
                        "cat /var/log/syslog | grep service",
                    ],
                    "correct": 2,
                    "explanation": "journalctl -u <service> -f visar loggar för en specifik tjänst med -f för follow (live-uppdatering).",
                },
            ],
        },
        # =============================================================================
        # NOD 9: Docker & Containers
        # =============================================================================
        {
            "title": "Docker & Containers",
            "slug": "docker-containers",
            "description": "Installera Docker, skapa images med Dockerfile, hantera containers och volumes",
            "difficulty": "intermediate",
            "estimated_minutes": 50,
            "xp_reward": 200,
            "order_index": 8,
            "content": """# 🐳 Docker & Containers

> **Kursmål:** "Kunskaper om containerteknologi"
>
> **Deliverable 5.3:** Installera Docker och skapa containeriserade tjänster

---

## 📋 TL;DR - Det viktigaste

| Kommando | Beskrivning |
|----------|-------------|
| `docker run -d nginx` | Starta container i bakgrunden |
| `docker ps` | Visa körande containers |
| `docker ps -a` | Visa ALLA containers |
| `docker images` | Lista images |
| `docker build -t name .` | Bygg image från Dockerfile |
| `docker exec -it container bash` | Gå in i container |
| `docker logs container` | Visa loggar |
| `docker-compose up -d` | Starta med Compose |

---

## 🔧 Docker Installation

### Ubuntu/Debian

```bash
#!/bin/bash
set -euo pipefail

# Installera beroenden
sudo apt update
sudo apt install -y \\
    ca-certificates \\
    curl \\
    gnupg \\
    lsb-release

# Lägg till Dockers GPG-nyckel
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \\
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Lägg till repository
echo \\
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \\
  https://download.docker.com/linux/ubuntu \\
  $(lsb_release -cs) stable" | \\
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installera Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Starta och aktivera
sudo systemctl enable docker
sudo systemctl start docker

# Lägg till användare i docker-gruppen (kräver ny login)
sudo usermod -aG docker $USER

# Verifiera
docker --version
docker compose version
```

### Rocky/RHEL

```bash
#!/bin/bash
set -euo pipefail

# Lägg till Docker repo
sudo dnf config-manager --add-repo \\
    https://download.docker.com/linux/centos/docker-ce.repo

# Installera
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Starta
sudo systemctl enable docker
sudo systemctl start docker

# Användare i docker-gruppen
sudo usermod -aG docker $USER
```

---

## 🏃 Köra Containers

### docker run - grundläggande

```bash
# Enklaste sättet
docker run hello-world

# I bakgrunden (-d = detached)
docker run -d nginx

# Med namn
docker run -d --name my-nginx nginx

# Med port-mapping (-p host:container)
docker run -d -p 8080:80 nginx
# Besök http://localhost:8080

# Med environment variables
docker run -d -e "MYSQL_ROOT_PASSWORD=secret" mysql

# Ta bort när den stannar
docker run --rm nginx echo "Hello"
```

### Port-mapping förklarad

```
-p 8080:80
    │    │
    │    └── Container-port (nginx lyssnar på 80 inuti)
    └─────── Host-port (du ansluter till denna)
```

### Hantera containers

```bash
# Lista körande
docker ps

# Lista ALLA (inklusive stoppade)
docker ps -a

# Stoppa
docker stop my-nginx

# Starta igen
docker start my-nginx

# Starta om
docker restart my-nginx

# Ta bort (måste vara stoppad)
docker rm my-nginx

# Tvinga bort (även om den kör)
docker rm -f my-nginx

# Ta bort alla stoppade containers
docker container prune
```

### Gå in i container

```bash
# Kör bash i körande container
docker exec -it my-nginx bash

# Kör specifikt kommando
docker exec my-nginx cat /etc/nginx/nginx.conf

# Interaktivt med ny container
docker run -it ubuntu bash
```

### Loggar

```bash
# Visa loggar
docker logs my-nginx

# Follow (live)
docker logs -f my-nginx

# Senaste 100 rader
docker logs --tail 100 my-nginx

# Med timestamps
docker logs -t my-nginx
```

---

## 📦 Images

### Hantera images

```bash
# Lista images
docker images

# Ladda ner image
docker pull nginx:latest
docker pull nginx:1.24     # Specifik version

# Ta bort image
docker rmi nginx:latest

# Ta bort oanvända images
docker image prune

# Ta bort ALLA oanvända images
docker image prune -a
```

### Sök images

```bash
# Sök på Docker Hub
docker search nginx

# Visa tags för image (kräver jq)
curl -s "https://hub.docker.com/v2/repositories/library/nginx/tags?page_size=10" | \\
    jq -r '.results[].name'
```

---

## 📄 Dockerfile

### Grundläggande Dockerfile

```dockerfile
# Base image
FROM ubuntu:22.04

# Metadata
LABEL maintainer="your@email.com"
LABEL description="My custom app"

# Sätt environment variables
ENV APP_HOME=/app
ENV PORT=8080

# Installera paket
RUN apt-get update && apt-get install -y \\
    python3 \\
    python3-pip \\
    && rm -rf /var/lib/apt/lists/*

# Skapa app-katalog
WORKDIR $APP_HOME

# Kopiera filer
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# Exponera port
EXPOSE $PORT

# Körs när containern startar
CMD ["python3", "app.py"]
```

### Dockerfile best practices

```dockerfile
# 1. Använd specifik tag, inte :latest
FROM python:3.11-slim

# 2. Kombinera RUN-kommandon
RUN apt-get update && apt-get install -y \\
    package1 \\
    package2 \\
    && rm -rf /var/lib/apt/lists/*

# 3. Kopiera requirements separat för caching
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# 4. Kör inte som root
RUN useradd -m appuser
USER appuser

# 5. Använd ENTRYPOINT + CMD
ENTRYPOINT ["python3"]
CMD ["app.py"]
```

### Bygga image

```bash
# Bygg från current directory
docker build -t myapp .

# Med tag/version
docker build -t myapp:1.0 .

# Med annan Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Visa build-processen utan cache
docker build --no-cache -t myapp .
```

---

## 💾 Volumes & Data

### Typer av data-persistens

| Typ | Kommando | Användning |
|-----|----------|------------|
| **Volume** | `-v mydata:/data` | Docker-hanterad, bäst för DB |
| **Bind mount** | `-v /host/path:/container/path` | Dev, config-filer |
| **tmpfs** | `--tmpfs /tmp` | Temporär data i RAM |

### Volumes (Docker-hanterade)

```bash
# Skapa volume
docker volume create mydata

# Lista volumes
docker volume ls

# Använd volume
docker run -d \\
    -v mydata:/var/lib/mysql \\
    -e MYSQL_ROOT_PASSWORD=secret \\
    mysql

# Inspektera volume
docker volume inspect mydata

# Ta bort volume
docker volume rm mydata

# Ta bort oanvända volumes
docker volume prune
```

### Bind mounts (Host-kataloger)

```bash
# Monta host-katalog
docker run -d \\
    -v /path/on/host:/path/in/container \\
    nginx

# Read-only
docker run -d \\
    -v /path/on/host:/data:ro \\
    myapp

# Exempel: Webb-server med lokal kod
docker run -d \\
    -p 8080:80 \\
    -v $(pwd)/html:/usr/share/nginx/html:ro \\
    nginx
```

---

## 🐙 Docker Compose

### docker-compose.yml exempel

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8080:80"
    environment:
      - NODE_ENV=production
    volumes:
      - ./app:/app
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  pgdata:
```

### Compose-kommandon

```bash
# Starta alla tjänster
docker compose up -d

# Visa status
docker compose ps

# Visa loggar
docker compose logs -f

# Stoppa
docker compose stop

# Stoppa och ta bort
docker compose down

# Ta bort inklusive volumes
docker compose down -v

# Bygg om images
docker compose build
docker compose up -d --build
```

---

## 🎯 Checkpoint: Deliverable - Docker Setup

```bash
#!/bin/bash
set -euo pipefail

# ============================================
# Docker Installation & Verification
# Deliverable 5.3 - DOE25
# ============================================

log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# Installera Docker (Ubuntu)
install_docker_ubuntu() {
    log "Installing Docker on Ubuntu..."

    # Beroenden
    sudo apt update
    sudo apt install -y ca-certificates curl gnupg

    # GPG key
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \\
        sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    # Repo
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \\
        https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \\
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # Install
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

    # Start
    sudo systemctl enable docker
    sudo systemctl start docker

    # User group
    sudo usermod -aG docker "$USER"

    log "Docker installed successfully"
}

# Skapa test-app
create_test_app() {
    log "Creating test application..."

    mkdir -p ~/docker-test
    cd ~/docker-test

    # Dockerfile
    cat > Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
EOF

    # Python app
    cat > app.py << 'EOF'
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from datetime import datetime

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "message": "Docker container is running!"
        }
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    print("Server running on port 5000")
    server.serve_forever()
EOF

    # Docker Compose
    cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000"]
      interval: 30s
      timeout: 10s
      retries: 3
EOF

    log "Test app created in ~/docker-test"
}

# Bygg och kör
build_and_run() {
    log "Building and running..."
    cd ~/docker-test

    docker build -t myapp:test .
    docker run -d --name test-container -p 5000:5000 myapp:test

    sleep 3

    log "Testing endpoint..."
    curl -s http://localhost:5000 | jq .

    log "Container logs:"
    docker logs test-container
}

# Verify
verify() {
    echo ""
    echo "=== VERIFICATION ==="
    echo ""

    echo "Docker version:"
    docker --version
    echo ""

    echo "Docker Compose version:"
    docker compose version
    echo ""

    echo "Running containers:"
    docker ps
    echo ""

    echo "Docker info:"
    docker info | grep -E "Server Version|Storage Driver|Operating System"
}

# Cleanup
cleanup() {
    log "Cleaning up..."
    docker rm -f test-container 2>/dev/null || true
    docker rmi myapp:test 2>/dev/null || true
}

# Main
main() {
    case "${1:-verify}" in
        install)
            install_docker_ubuntu
            ;;
        setup)
            create_test_app
            build_and_run
            ;;
        cleanup)
            cleanup
            ;;
        verify|*)
            verify
            ;;
    esac
}

main "$@"
```

---

## 📚 Snabbreferens

```bash
# === CONTAINERS ===
docker run -d -p 8080:80 --name web nginx
docker ps / docker ps -a
docker stop/start/restart container
docker rm container
docker exec -it container bash
docker logs -f container

# === IMAGES ===
docker images
docker pull image:tag
docker build -t name:tag .
docker rmi image

# === VOLUMES ===
docker volume create/ls/rm name
docker run -v volume:/path image
docker run -v /host:/container image

# === COMPOSE ===
docker compose up -d
docker compose down
docker compose logs -f
docker compose ps

# === CLEANUP ===
docker system prune -a    # ALLT oanvänt
docker container prune    # Stoppade containers
docker image prune -a     # Oanvända images
docker volume prune       # Oanvända volumes
```

---

## ⚠️ Vanliga fel

| Fel | Orsak | Lösning |
|-----|-------|---------|
| permission denied | Ej i docker-gruppen | `usermod -aG docker $USER` + ny login |
| port already in use | Annan process använder porten | `docker ps`, ändra port eller stoppa |
| no space left | Disk full av images/containers | `docker system prune -a` |
| build fails | Fel i Dockerfile | Kolla syntax, COPY-paths |
| volume mount empty | Fel path | Använd absolut path eller $(pwd) |
""",
            "quiz": [
                {
                    "question": "Vilket kommando startar en nginx-container i bakgrunden på port 8080?",
                    "options": [
                        "docker start nginx -p 8080",
                        "docker run -d -p 8080:80 nginx",
                        "docker nginx -d -port 8080",
                        "docker create nginx:8080",
                    ],
                    "correct": 1,
                    "explanation": "-d = detached (bakgrund), -p 8080:80 mappar host port 8080 till container port 80.",
                },
                {
                    "question": "Hur går du in i en körande container för att köra bash?",
                    "options": [
                        "docker bash container",
                        "docker run -it container bash",
                        "docker exec -it container bash",
                        "docker shell container",
                    ],
                    "correct": 2,
                    "explanation": "docker exec kör kommando i KÖRANDE container. -it ger interaktiv terminal.",
                },
                {
                    "question": "Vad gör 'docker run -v mydata:/var/lib/mysql mysql'?",
                    "options": [
                        "Kopierar data från host till container",
                        "Skapar en volume 'mydata' och mountar på /var/lib/mysql",
                        "Tar backup av MySQL",
                        "Kör MySQL utan persistent data",
                    ],
                    "correct": 1,
                    "explanation": "-v volume:path mountar en Docker-hanterad volume. Data persisterar även om containern tas bort.",
                },
                {
                    "question": "Vilket kommando bygger en Docker image från en Dockerfile?",
                    "options": [
                        "docker create -t myapp .",
                        "docker build -t myapp .",
                        "docker image myapp .",
                        "docker make -t myapp .",
                    ],
                    "correct": 1,
                    "explanation": "docker build -t name . bygger image från Dockerfile i current directory och taggar den.",
                },
                {
                    "question": "Vad händer om du kör 'docker compose down -v'?",
                    "options": [
                        "Stoppar containers men behåller volumes",
                        "Stoppar containers och tar bort volumes",
                        "Visar verbose output",
                        "Validerar docker-compose.yml",
                    ],
                    "correct": 1,
                    "explanation": "-v flaggan tar bort associated volumes. Utan -v bevaras volumes för nästa 'up'.",
                },
                {
                    "question": "Hur visar du live-loggar från en container?",
                    "options": [
                        "docker logs container",
                        "docker logs -f container",
                        "docker tail container",
                        "docker output container",
                    ],
                    "correct": 1,
                    "explanation": "-f (follow) visar loggar i realtid, likt tail -f. Utan -f visas befintliga loggar och avslutas.",
                },
            ],
        },
        # =============================================================================
        # NOD 10: Felsökning & Tentasammanfattning
        # =============================================================================
        {
            "title": "🎯 Felsökning & Tentasammanfattning",
            "slug": "felsokning-tentasammanfattning",
            "description": "Det ultimata cheat sheet för tentan - alla kommandon, troubleshooting och kursmål på ett ställe",
            "difficulty": "intermediate",
            "estimated_minutes": 60,
            "xp_reward": 250,
            "order_index": 9,
            "content": """# 🎯 Felsökning & Tentasammanfattning

> **TENTA 7 JANUARI 2026** - Allt du behöver på ett ställe!

---

## 📋 MASTER CHEAT SHEET

### 🐚 Bash Scripting

```bash
#!/bin/bash
set -euo pipefail    # ALLTID! e=exit on error, u=undefined vars, o pipefail

# Variabler
name="value"         # Inga mellanslag vid =
echo "$name"         # Alltid citattecken
echo "${name}"       # Säkrare syntax

# Speciella variabler
$0                   # Script-namn
$1, $2...            # Argument
$#                   # Antal argument
$@                   # Alla argument (separata)
$*                   # Alla argument (en sträng)
$?                   # Exit status från förra kommandot
$$                   # Process ID

# Kommandosubstitution
result=$(command)    # Moderna sättet
result=`command`     # Gammalt, undvik
```

### 📊 Textbearbetning

```bash
# grep - sök
grep "pattern" file
grep -r "pattern" dir/     # Rekursivt
grep -i "pattern" file     # Case insensitive
grep -v "pattern" file     # Invertera (visa ICKE-matchande)
grep -E "regex" file       # Extended regex

# sed - ersätt
sed 's/old/new/' file      # Första på varje rad
sed 's/old/new/g' file     # Alla (global)
sed -i 's/old/new/g' file  # In-place (ändra filen)

# awk - kolumner
awk '{print $1}' file      # Första kolumnen
awk -F: '{print $1}' file  # Med delimiter :
awk '$3 > 100' file        # Villkor
```

### 🔄 Kontrollstrukturer

```bash
# if-satser
if [[ condition ]]; then
    # kod
elif [[ condition ]]; then
    # kod
else
    # kod
fi

# Testoperatorer
[[ -f file ]]        # Fil finns
[[ -d dir ]]         # Katalog finns
[[ -z "$var" ]]      # Variabel tom
[[ -n "$var" ]]      # Variabel INTE tom
[[ $a -eq $b ]]      # Numerisk likhet
[[ "$a" == "$b" ]]   # String likhet

# for-loop
for item in "${array[@]}"; do
    echo "$item"
done

for i in {1..10}; do
    echo "$i"
done

# while-loop
while [[ condition ]]; do
    # kod
done

# case
case "$var" in
    pattern1) cmd ;;
    pattern2|pattern3) cmd ;;
    *) default ;;
esac
```

### 🔧 Funktioner & Arrays

```bash
# Funktion
my_func() {
    local var="$1"   # Lokal variabel
    echo "$var"
    return 0         # Exit status
}
my_func "arg"        # Anropa UTAN ()

# Array
arr=("a" "b" "c")
echo "${arr[0]}"     # Element
echo "${arr[@]}"     # Alla
echo "${#arr[@]}"    # Längd
for item in "${arr[@]}"; do ...; done

# Associativ array
declare -A map
map["key"]="value"
echo "${map[key]}"
```

### 🚨 Signals & trap

```bash
cleanup() {
    rm -f "$TEMP_FILE"
}
trap cleanup EXIT    # Körs ALLTID vid avslut
trap cleanup SIGINT SIGTERM
```

---

## 👥 Användarhantering

```bash
# Skapa användare
useradd -m -s /bin/bash username
passwd username

# Ändra användare (ALLTID -a för append!)
usermod -aG groupname username

# Grupper
groupadd groupname
groups username
id username

# Filer
/etc/passwd          # Användare
/etc/shadow          # Lösenord
/etc/group           # Grupper
/etc/sudoers         # Sudo-behörigheter
```

---

## 🔒 Filrättigheter

```bash
# chmod
chmod 755 file       # rwxr-xr-x
chmod 644 file       # rw-r--r--
chmod 600 file       # rw------- (SSH keys!)
chmod u+x file       # Lägg till execute för user

# Speciella
chmod 2775 dir       # SetGID (g+s)
chmod +t dir         # Sticky bit

# chown
chown user:group file
chown -R user:group dir/

# Oktala värden
# 4=read, 2=write, 1=execute
# 755 = 7(rwx) 5(r-x) 5(r-x)
```

---

## 🔐 SSH

```bash
# Generera nyckel
ssh-keygen -t ed25519 -C "email"

# Kopiera nyckel
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Rättigheter (KRITISKT!)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_*
chmod 644 ~/.ssh/id_*.pub
chmod 600 ~/.ssh/authorized_keys

# /etc/ssh/sshd_config - härdning
Port 6622
PermitRootLogin no
PasswordAuthentication no
AllowUsers alice bob

# Validera och starta om
sshd -t && systemctl restart sshd
```

---

## 🔥 Brandväggar

### UFW (Ubuntu)

```bash
ufw allow 22/tcp
ufw allow ssh
ufw default deny incoming
ufw default allow outgoing
ufw enable
ufw status numbered
```

### firewalld (Rocky/RHEL)

```bash
firewall-cmd --permanent --add-port=22/tcp
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
firewall-cmd --list-all
```

---

## 💾 Lagring

```bash
# Visa diskar
lsblk
lsblk -f             # Med filsystem

# Partitionera
fdisk /dev/sdb

# Formatera
mkfs.ext4 /dev/sdb1

# Mounta
mount /dev/sdb1 /mnt/data
umount /mnt/data

# /etc/fstab (permanent mount)
UUID=xxx  /mnt/data  ext4  defaults  0  2
```

### LUKS

```bash
cryptsetup luksFormat /dev/sdb1
cryptsetup open /dev/sdb1 mydata
mkfs.ext4 /dev/mapper/mydata
mount /dev/mapper/mydata /mnt/secure
cryptsetup close mydata
```

---

## ⚙️ systemd

```bash
# Tjänsthantering
systemctl start|stop|restart service
systemctl enable|disable service
systemctl status service
systemctl daemon-reload     # Efter service-fil ändringar!

# Loggar
journalctl -u service
journalctl -u service -f    # Follow
journalctl -u service --since today

# Service-fil: /etc/systemd/system/myapp.service
[Unit]
Description=My App
After=network.target

[Service]
Type=simple
User=appuser
ExecStart=/path/to/app
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 🐳 Docker

```bash
# Kör container
docker run -d -p 8080:80 --name web nginx
docker run -it ubuntu bash

# Hantera
docker ps                    # Körande
docker ps -a                 # Alla
docker stop|start|rm container
docker exec -it container bash
docker logs -f container

# Images
docker images
docker pull nginx:latest
docker build -t myapp .
docker rmi image

# Volumes
docker volume create mydata
docker run -v mydata:/data image
docker run -v /host/path:/container/path image

# Compose
docker compose up -d
docker compose down
docker compose logs -f

# Cleanup
docker system prune -a
```

---

## 🔍 FELSÖKNING

### Tjänster

```bash
# Tjänst startar inte?
systemctl status service     # Se fel
journalctl -u service -n 50  # Loggar
systemctl cat service        # Visa service-fil

# Syntaxfel i config?
sshd -t                      # SSH
nginx -t                     # Nginx
visudo -c                    # Sudoers
```

### Nätverk

```bash
# Vad lyssnar?
ss -tlnp
netstat -tlnp

# Testa port
nc -zv host port
curl -v http://host:port

# DNS
dig domain
nslookup domain

# Brandvägg blockerar?
ufw status
firewall-cmd --list-all
```

### Disk/Lagring

```bash
# Disk full?
df -h
du -sh /*

# Vad använder disk?
du -sh * | sort -h

# Disk busy?
lsof +D /mnt/data
fuser -m /mnt/data
```

### Processer

```bash
# Hitta process
ps aux | grep name
pgrep -f name

# Döda process
kill PID
kill -9 PID          # Force
pkill -f name
```

---

## 📋 KURSMÅL - CHECKLISTA

### ✅ Kunskaper

| Kursmål | Nod | Nyckelkommandon |
|---------|-----|-----------------|
| 1. Användarhantering | 5 | useradd, usermod -aG, passwd |
| 2. Filrättigheter | 5 | chmod, chown, SetGID |
| 3. IT-säkerhet | 6, 7 | SSH härdning, brandväggar |
| 4. Systemadministration | 8 | lsblk, mount, systemctl |
| 5. Containerteknologi | 9 | docker run/build/compose |

### ✅ Färdigheter

| Kursmål | Nod | Vad du ska kunna |
|---------|-----|------------------|
| 1. Konfigurera användarkonton | 5 | Skript med useradd, grupper |
| 2. Skripta med Bash | 1-4 | set -euo, funktioner, loops |
| 3. Säkra Linux-system | 6, 7 | SSH keys, UFW/firewalld |
| 4. Konfigurera nätverk | 6, 7 | Portar, brandväggsregler |

---

## 🎯 DELIVERABLE CHECKLIST

### 5.1 Users & Groups
- [ ] `groupadd devops`
- [ ] `useradd -m -s /bin/bash -G devops user`
- [ ] Sudoers med `visudo`
- [ ] SetGID på projektkatalog

### 5.2 SSH & Firewall
- [ ] Port 6622
- [ ] PermitRootLogin no
- [ ] PasswordAuthentication no
- [ ] AllowUsers whitelist
- [ ] UFW/firewalld regler

### 5.3 Docker & systemd
- [ ] Docker installerat
- [ ] Dockerfile skapad
- [ ] docker-compose.yml
- [ ] systemd service-fil
- [ ] journalctl fungerar

### 5.4-5.5 README & Shellcheck
- [ ] README.md med instruktioner
- [ ] Alla scripts passerar shellcheck
- [ ] set -euo pipefail överallt

---

## 💡 VANLIGA TENTAFRÅGOR

### Bash
1. **Vad gör `set -euo pipefail`?** → e=exit on error, u=error på undefined vars, o pipefail=exit på pipeline-fel
2. **Skillnad `$@` vs `$*`?** → $@ bevarar separata args, $* slår ihop till en sträng
3. **Hur deklarerar du associativ array?** → `declare -A arr`

### Användare
4. **Hur lägger du till användare i grupp?** → `usermod -aG group user` (ALLTID -a!)
5. **Vad gör SetGID på katalog?** → Nya filer ärver gruppägaren

### SSH
6. **Vilken rättighet ska privat SSH-nyckel ha?** → 600
7. **Hur validerar du sshd_config?** → `sshd -t`

### Brandvägg
8. **Vad måste du göra innan `ufw enable`?** → Tillåta SSH!
9. **firewalld permanent regel?** → `--permanent` + `--reload`

### Docker
10. **Hur går du in i körande container?** → `docker exec -it container bash`
11. **Vad gör `-v mydata:/data`?** → Mountar volume

### systemd
12. **Vad gör du efter att ändra service-fil?** → `systemctl daemon-reload`
13. **Hur ser du service-loggar live?** → `journalctl -u service -f`

---

## 🏆 LYCKA TILL PÅ TENTAN!

Du har nu gått igenom:
- ✅ Bash scripting (shebang, variabler, set -euo pipefail)
- ✅ Textbearbetning (grep, sed, awk)
- ✅ Kontrollstrukturer (if, for, while, case)
- ✅ Funktioner & arrays (VG-nivå)
- ✅ Användarhantering (useradd, chmod, sudo)
- ✅ SSH-säkerhet (nycklar, härdning)
- ✅ Brandväggar (UFW & firewalld)
- ✅ Lagring (LUKS, systemd)
- ✅ Docker (containers, images, compose)

**Pro tips för tentan:**
1. Läs frågan NOGA
2. `set -euo pipefail` i ALLA scripts
3. `usermod -aG` (glöm inte -a!)
4. SSH-nycklar = 600
5. `systemctl daemon-reload` efter ändringar
6. Testa SSH innan du stänger sessionen!

**Du fixar det här! 💪**
""",
            "quiz": [
                {
                    "question": "Vad gör 'set -euo pipefail' i ett Bash-script?",
                    "options": [
                        "Sätter miljövariabler",
                        "Aktiverar debug-läge",
                        "Exit vid fel, error vid undefined vars, fail på pipeline-fel",
                        "Startar interaktivt läge",
                    ],
                    "correct": 2,
                    "explanation": "e=exit on error, u=error på undefined variables, o pipefail=exit om något i pipeline misslyckas.",
                },
                {
                    "question": "Du har ändrat /etc/systemd/system/myapp.service. Vad måste du göra?",
                    "options": [
                        "systemctl restart myapp",
                        "systemctl reload myapp",
                        "systemctl daemon-reload && systemctl restart myapp",
                        "service myapp restart",
                    ],
                    "correct": 2,
                    "explanation": "daemon-reload läser in ändrade service-filer. Sedan restart för att aktivera ändringarna.",
                },
                {
                    "question": "Vilket kommando lägger till användare 'bob' i gruppen 'docker' utan att ta bort från andra grupper?",
                    "options": [
                        "usermod -G docker bob",
                        "usermod -aG docker bob",
                        "useradd -G docker bob",
                        "groupadd docker bob",
                    ],
                    "correct": 1,
                    "explanation": "-a (append) är KRITISKT! Utan -a ersätts alla sekundära grupper.",
                },
                {
                    "question": "SSH fungerar inte efter konfigändring. Vad borde du ha gjort?",
                    "options": [
                        "Kört sshd -t innan restart",
                        "Startat om servern",
                        "Ändrat root-lösenordet",
                        "Installerat om SSH",
                    ],
                    "correct": 0,
                    "explanation": "sshd -t validerar konfigurationen. Alltid testa innan restart för att undvika utelåsning!",
                },
                {
                    "question": "Vad är rätt ordning för att öppna port 443 permanent i firewalld?",
                    "options": [
                        "firewall-cmd --add-port=443/tcp",
                        "firewall-cmd --reload && firewall-cmd --add-port=443/tcp",
                        "firewall-cmd --permanent --add-port=443/tcp && firewall-cmd --reload",
                        "systemctl add-port 443",
                    ],
                    "correct": 2,
                    "explanation": "--permanent sparar regeln, --reload aktiverar den. Utan --permanent försvinner regeln vid restart.",
                },
                {
                    "question": "Din Docker container startar men du kan inte ansluta på port 8080. Vad kollar du först?",
                    "options": [
                        "docker images",
                        "docker ps och kontrollera port-mapping",
                        "docker volume ls",
                        "docker network ls",
                    ],
                    "correct": 1,
                    "explanation": "docker ps visar port-mappings. Kontrollera att -p 8080:80 är korrekt och att containern faktiskt kör.",
                },
            ],
        },
    ],
}
