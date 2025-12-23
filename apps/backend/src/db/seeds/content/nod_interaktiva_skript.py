"""
NOD 1.7: Interaktiva skript (read, validering)
==============================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

INTERAKTIVA_SKRIPT_NODE = {
    "title": "Interaktiva skript - read & validering",
    "slug": "interaktiva-skript-read-validering",
    "description": "read-kommandot, input-validering och select-menyer för robusta skript.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 120,
    "order_index": 6,
    "content": r"""# Interaktiva skript - read & validering

> **TL;DR:** `read -p "Prompt: " var` läser input. Validera med `[[ -z "$var" ]]` (tom) eller `[[ $var =~ ^[0-9]+$ ]]` (nummer). Loop tills giltig input!

---

## 📖 TEORI: read-kommandot

`read` läser input från användaren och sparar i en variabel.

### Grundläggande syntax

```bash
read variabel
```

### Alla viktiga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-p` | Visa prompt | `read -p "Namn: " namn` |
| `-s` | Silent (dölj input) | `read -s -p "Lösenord: " pass` |
| `-n N` | Läs endast N tecken | `read -n 1 svar` |
| `-t N` | Timeout efter N sekunder | `read -t 5 input` |
| `-r` | Raw (ingen backslash-tolkning) | `read -r line` |
| `-a` | Läs till array | `read -a arr` |

### Exempel: Grundläggande read

```bash
#!/usr/bin/env bash

# Enkel read
echo "Vad heter du?"
read namn
echo "Hej $namn!"

# Med prompt (-p)
read -p "Ange din ålder: " ålder
echo "Du är $ålder år"
```

### Exempel: Silent för lösenord

```bash
#!/usr/bin/env bash

read -s -p "Ange lösenord: " password
echo    # Ny rad efter silent input
echo "Lösenord mottaget (${#password} tecken)"
```

### Exempel: Läs endast 1 tecken

```bash
#!/usr/bin/env bash

read -n 1 -p "Fortsätt? (j/n): " svar
echo    # Ny rad
if [[ "$svar" == "j" ]]; then
    echo "Fortsätter..."
else
    echo "Avbryter."
fi
```

### Exempel: Timeout

```bash
#!/usr/bin/env bash

if read -t 5 -p "Svara inom 5 sekunder: " svar; then
    echo "Du svarade: $svar"
else
    echo "Tiden gick ut!"
fi
```

### Exempel: Läs till array

```bash
#!/usr/bin/env bash

echo "Skriv tre ord (mellanslag mellan):"
read -a ord
echo "Första: ${ord[0]}"
echo "Andra: ${ord[1]}"
echo "Tredje: ${ord[2]}"
```

### Exempel: Läs flera variabler

```bash
#!/usr/bin/env bash

read -p "Förnamn efternamn: " förnamn efternamn
echo "Förnamn: $förnamn"
echo "Efternamn: $efternamn"
```

### ⚠️ Använd alltid -r för säkerhet!

```bash
# Utan -r: backslash tolkas speciellt
echo "test\ndata" | read line      # line = "testndata"

# Med -r: raw input bevaras
echo "test\ndata" | read -r line   # line = "test\ndata"
```

---

## 📖 Validering av input

### Kolla om input är tom

```bash
read -p "Namn: " namn
if [[ -z "$namn" ]]; then
    echo "Fel: Namn får inte vara tomt!"
    exit 1
fi
```

### Kolla om input är ett nummer

```bash
read -p "Ålder: " ålder
if [[ ! "$ålder" =~ ^[0-9]+$ ]]; then
    echo "Fel: Ange ett giltigt nummer!"
    exit 1
fi
```

### Kolla om input är i en lista

```bash
read -p "Välj färg (röd/grön/blå): " färg
if [[ ! "$färg" =~ ^(röd|grön|blå)$ ]]; then
    echo "Fel: Ogiltig färg!"
    exit 1
fi
```

### Kolla ja/nej

```bash
read -p "Är du säker? (ja/nej): " svar
case "$svar" in
    ja|Ja|JA|j|J)
        echo "Fortsätter..."
        ;;
    nej|Nej|NEJ|n|N)
        echo "Avbryter."
        exit 0
        ;;
    *)
        echo "Svar ja eller nej!"
        exit 1
        ;;
esac
```

---

## 📖 Loop tills giltig input (VG-NIVÅ!)

### Mönster: While-loop med validering

```bash
#!/usr/bin/env bash

while true; do
    read -p "Ange ett tal (1-100): " tal

    # Kolla om nummer
    if [[ ! "$tal" =~ ^[0-9]+$ ]]; then
        echo "Fel: Måste vara ett nummer!"
        continue
    fi

    # Kolla range
    if (( tal < 1 || tal > 100 )); then
        echo "Fel: Måste vara mellan 1-100!"
        continue
    fi

    # Giltig input - break
    break
done

echo "Du valde: $tal"
```

### Mönster: Funktion för validerad input

```bash
#!/usr/bin/env bash

get_number() {
    local prompt="$1"
    local min="$2"
    local max="$3"
    local input

    while true; do
        read -p "$prompt" input

        if [[ ! "$input" =~ ^[0-9]+$ ]]; then
            echo "Fel: Ange ett nummer!" >&2
            continue
        fi

        if (( input < min || input > max )); then
            echo "Fel: Måste vara $min-$max!" >&2
            continue
        fi

        echo "$input"
        return 0
    done
}

# Användning
ålder=$(get_number "Din ålder: " 0 150)
echo "Du är $ålder år"
```

### Mönster: Max antal försök

```bash
#!/usr/bin/env bash

MAX_ATTEMPTS=3
attempt=0

while (( attempt < MAX_ATTEMPTS )); do
    read -s -p "Lösenord: " pass
    echo

    if [[ "$pass" == "hemligt" ]]; then
        echo "Rätt lösenord!"
        break
    fi

    (( attempt++ ))
    echo "Fel! Försök $attempt av $MAX_ATTEMPTS"
done

if (( attempt >= MAX_ATTEMPTS )); then
    echo "För många misslyckade försök!"
    exit 1
fi
```

---

## 📖 select - Menyval

`select` skapar automatiskt numrerade menyer:

### Grundläggande select

```bash
#!/usr/bin/env bash

PS3="Välj ett alternativ: "    # Prompten för select

select val in "Starta" "Stoppa" "Status" "Avsluta"; do
    case $val in
        "Starta")
            echo "Startar tjänsten..."
            ;;
        "Stoppa")
            echo "Stoppar tjänsten..."
            ;;
        "Status")
            echo "Visar status..."
            ;;
        "Avsluta")
            echo "Hejdå!"
            break
            ;;
        *)
            echo "Ogiltigt val, försök igen."
            ;;
    esac
done
```

**Output:**
```
1) Starta
2) Stoppa
3) Status
4) Avsluta
Välj ett alternativ: 1
Startar tjänsten...
Välj ett alternativ:
```

### select med REPLY

`$REPLY` innehåller det användaren skrev (numret):

```bash
#!/usr/bin/env bash

options=("Option A" "Option B" "Option C" "Quit")

select opt in "${options[@]}"; do
    echo "Du skrev: $REPLY"
    echo "Du valde: $opt"

    [[ "$opt" == "Quit" ]] && break
done
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: SimpleUserAdd - Shell-val (från kursen)

```bash
#!/usr/bin/env bash

echo "=== Lägg till användare ==="

# Läs användarnamn
while true; do
    read -p "Användarnamn: " username
    if [[ -z "$username" ]]; then
        echo "Fel: Användarnamn krävs!"
        continue
    fi
    if id "$username" &>/dev/null; then
        echo "Fel: Användaren finns redan!"
        continue
    fi
    break
done

# Visa tillgängliga shells
echo ""
echo "Tillgängliga shells:"
grep -v '^#' /etc/shells
echo ""

# Läs shell med default
read -p "Välj shell (tom = /usr/sbin/nologin): " user_shell

if [[ -z "$user_shell" ]]; then
    user_shell="/usr/sbin/nologin"
elif ! grep -q "^$user_shell$" /etc/shells; then
    echo "Fel: Ogiltigt shell!"
    exit 1
fi

echo "Skapar användare: $username med shell: $user_shell"
# useradd -s "$user_shell" "$username"
```

### Exempel 2: Backup-val (från kursen)

```bash
#!/usr/bin/env bash

echo "=== Backup-verktyg ==="
echo ""
echo "Vilken typ av backup?"
echo "1) Full backup"
echo "2) Incremental backup"
echo "3) Differential backup"
echo ""

read -n 1 -p "Ditt val (1-3): " choice
echo ""

case $choice in
    1)
        echo "Kör full backup..."
        # tar czf backup_full_$(date +%Y%m%d).tar.gz /data
        ;;
    2)
        echo "Kör incremental backup..."
        # tar czf backup_inc_$(date +%Y%m%d).tar.gz --newer-mtime="1 day ago" /data
        ;;
    3)
        echo "Kör differential backup..."
        ;;
    *)
        echo "Ogiltigt val!"
        exit 1
        ;;
esac
```

### Exempel 3: Komplett installationsskript

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== Installationsguide ==="

# Steg 1: Välj miljö
PS3="Välj miljö: "
select env in "Development" "Staging" "Production" "Avbryt"; do
    case $env in
        "Development"|"Staging"|"Production")
            echo "Vald miljö: $env"
            break
            ;;
        "Avbryt")
            echo "Installation avbruten."
            exit 0
            ;;
        *)
            echo "Ogiltigt val!"
            ;;
    esac
done

# Steg 2: Bekräfta
read -p "Fortsätt installation i $env? (ja/nej): " confirm
if [[ ! "$confirm" =~ ^(ja|j)$ ]]; then
    echo "Avbruten."
    exit 0
fi

# Steg 3: Lösenord
while true; do
    read -s -p "Admin-lösenord: " pass1
    echo
    read -s -p "Bekräfta lösenord: " pass2
    echo

    if [[ "$pass1" != "$pass2" ]]; then
        echo "Lösenorden matchar inte!"
        continue
    fi

    if [[ ${#pass1} -lt 8 ]]; then
        echo "Lösenord måste vara minst 8 tecken!"
        continue
    fi

    break
done

echo "Installation klar!"
```

### Exempel 4: Servicehanterare med select

```bash
#!/usr/bin/env bash

services=("nginx" "mysql" "redis" "docker")

echo "=== Service Manager ==="

PS3="Välj tjänst: "
select service in "${services[@]}" "Avsluta"; do
    [[ "$service" == "Avsluta" ]] && break
    [[ -z "$service" ]] && { echo "Ogiltigt val!"; continue; }

    echo ""
    PS3="Åtgärd för $service: "
    select action in "Start" "Stop" "Restart" "Status" "Tillbaka"; do
        case $action in
            "Start")
                echo "systemctl start $service"
                ;;
            "Stop")
                echo "systemctl stop $service"
                ;;
            "Restart")
                echo "systemctl restart $service"
                ;;
            "Status")
                echo "systemctl status $service"
                ;;
            "Tillbaka")
                break
                ;;
            *)
                echo "Ogiltigt val!"
                ;;
        esac
    done
    PS3="Välj tjänst: "
done

echo "Hejdå!"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | read -p gör? | Visar prompt före input |
| 2 | read -s gör? | Silent mode (döljer input) |
| 3 | read -n 1 gör? | Läser endast 1 tecken |
| 4 | read -t 5 gör? | Timeout efter 5 sekunder |
| 5 | read -a arr gör? | Läser input till array |
| 6 | read -r gör? | Raw mode (bevarar backslash) |
| 7 | [[ -z "$var" ]] kollar? | Om variabeln är tom |
| 8 | Regex för nummer? | ^[0-9]+$ |
| 9 | PS3 i select? | Prompten som visas |
| 10 | $REPLY i select? | Numret användaren skrev |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Hur visar du en prompt med read?**
- A) read "Namn: " namn
- B) read -p "Namn: " namn ✅
- C) read --prompt "Namn: " namn
- D) prompt read "Namn: " namn

**2. Hur döljer du input (t.ex. för lösenord)?**
- A) read -h password
- B) read -s password ✅
- C) read -hidden password
- D) read --silent password

**3. Hur läser du endast ett tecken?**
- A) read -1 char
- B) read -c char
- C) read -n 1 char ✅
- D) read --char char

**4. Vad gör read -t 10?**
- A) Läser 10 tecken
- B) Väntar max 10 sekunder på input ✅
- C) Läser 10 rader
- D) Timeout vid 10 tecken

**5. Hur kollar du om en variabel är tom?**
- A) [[ $var == "" ]]
- B) [[ -z "$var" ]] ✅
- C) [[ -e "$var" ]]
- D) [[ -n "$var" ]]

**6. Vilken regex matchar endast siffror?**
- A) [0-9]*
- B) ^[0-9]+$ ✅
- C) \d+
- D) [digits]

**7. Vad är PS3 i select?**
- A) En variabel för val
- B) Prompten som visas för select ✅
- C) Tredje alternativet
- D) Exit-koden

**8. Vad innehåller $REPLY i select?**
- A) Det valda alternativet
- B) Numret användaren skrev ✅
- C) Index i arrayen
- D) Felmeddelande

**9. Hur bryter du en select-loop?**
- A) exit
- B) quit
- C) break ✅
- D) stop

**10. Varför ska man använda read -r?**
- A) Snabbare läsning
- B) Bevarar backslash-tecken ✅
- C) Läser rekursivt
- D) Rensar buffern

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande read
Skriv ett skript som:
1. Frågar efter namn med prompt
2. Frågar efter ålder
3. Skriver ut "Hej [namn], du är [ålder] år!"

```bash
#!/usr/bin/env bash
# Fyll i
read -p "Ditt namn: " namn
read -p "Din ålder: " ålder
echo "Hej $namn, du är $ålder år!"
```

### Övning 2: Validering
Skriv ett skript som:
1. Frågar efter ett tal mellan 1-10
2. Loopar tills giltigt tal anges
3. Validerar både att det är nummer OCH inom range

```bash
#!/usr/bin/env bash
while true; do
    read -p "Ange tal (1-10): " tal

    # Kolla om nummer
    if [[ ! "$tal" =~ ^[0-9]+$ ]]; then
        echo "Måste vara ett nummer!"
        continue
    fi

    # Kolla range
    if (( tal < 1 || tal > 10 )); then
        echo "Måste vara 1-10!"
        continue
    fi

    break
done
echo "Du valde: $tal"
```

### Övning 3: Select-meny
Skapa en meny med select som låter användaren:
1. Visa datum
2. Visa diskutrymme
3. Visa inloggade användare
4. Avsluta

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| Glömma citattecken | Word splitting | Alltid `"$var"` |
| read utan -r | Backslash tolkas | Använd `read -r` |
| Ingen validering | Krasch vid ogiltig input | Loop med validering |
| case utan *) | Ingen fallback | Alltid ha `*) ...` |
| select utan break | Oändlig loop | `break` för att avsluta |

---

## 📝 SAMMANFATTNING

```bash
# READ-FLAGGOR
read var                    # Enkel läsning
read -p "Prompt: " var     # Med prompt
read -s var                # Silent (lösenord)
read -n 1 var              # Endast 1 tecken
read -t 5 var              # Timeout 5 sek
read -r var                # Raw (behåll backslash)
read -a arr                # Till array

# VALIDERING
[[ -z "$var" ]]            # Tom?
[[ -n "$var" ]]            # Inte tom?
[[ "$var" =~ ^[0-9]+$ ]]   # Nummer?
[[ "$var" =~ ^(a|b|c)$ ]]  # I lista?

# LOOP TILLS GILTIG
while true; do
    read -p "Input: " val
    [[ -z "$val" ]] && continue
    break
done

# SELECT-MENY
PS3="Välj: "
select opt in "A" "B" "Quit"; do
    case $opt in
        "A") echo "A" ;;
        "B") echo "B" ;;
        "Quit") break ;;
        *) echo "Ogiltigt" ;;
    esac
done
```

""",
    "quiz": [
        {
            "question": "Hur visar du en prompt med read?",
            "options": [
                "read \"Namn: \" namn",
                "read -p \"Namn: \" namn",
                "read --prompt \"Namn: \" namn",
                "prompt read \"Namn: \" namn"
            ],
            "correct": 1,
            "explanation": "Flaggan -p (prompt) visar en text innan input läses."
        },
        {
            "question": "Hur döljer du input (t.ex. för lösenord)?",
            "options": [
                "read -h password",
                "read -s password",
                "read -hidden password",
                "read --silent password"
            ],
            "correct": 1,
            "explanation": "Flaggan -s (silent) döljer det användaren skriver."
        },
        {
            "question": "Hur läser du endast ett tecken?",
            "options": [
                "read -1 char",
                "read -c char",
                "read -n 1 char",
                "read --char char"
            ],
            "correct": 2,
            "explanation": "-n N läser exakt N tecken. -n 1 läser alltså ett tecken."
        },
        {
            "question": "Vad gör read -t 10?",
            "options": [
                "Läser 10 tecken",
                "Väntar max 10 sekunder på input",
                "Läser 10 rader",
                "Timeout vid 10 tecken"
            ],
            "correct": 1,
            "explanation": "-t sätter timeout i sekunder. Efter 10 sek returneras felkod."
        },
        {
            "question": "Hur kollar du om en variabel är tom?",
            "options": [
                "[[ $var == \"\" ]]",
                "[[ -z \"$var\" ]]",
                "[[ -e \"$var\" ]]",
                "[[ -n \"$var\" ]]"
            ],
            "correct": 1,
            "explanation": "-z testar om strängen är zero length (tom). -n testar motsatsen."
        },
        {
            "question": "Vilken regex matchar endast siffror?",
            "options": [
                "[0-9]*",
                "^[0-9]+$",
                "\\d+",
                "[digits]"
            ],
            "correct": 1,
            "explanation": "^[0-9]+$ matchar strängar som ENDAST innehåller en eller fler siffror."
        },
        {
            "question": "Vad är PS3 i select?",
            "options": [
                "En variabel för val",
                "Prompten som visas för select",
                "Tredje alternativet",
                "Exit-koden"
            ],
            "correct": 1,
            "explanation": "PS3 är den speciella variabeln som styr prompten i select-satser."
        },
        {
            "question": "Vad innehåller $REPLY i select?",
            "options": [
                "Det valda alternativets text",
                "Numret användaren skrev",
                "Index i arrayen",
                "Felmeddelande"
            ],
            "correct": 1,
            "explanation": "$REPLY innehåller råinput (numret). Variabeln i select innehåller texten."
        },
        {
            "question": "Hur bryter du en select-loop?",
            "options": [
                "exit",
                "quit",
                "break",
                "stop"
            ],
            "correct": 2,
            "explanation": "break avslutar select-loopen precis som i andra loopar."
        },
        {
            "question": "Varför ska man använda read -r?",
            "options": [
                "Snabbare läsning",
                "Bevarar backslash-tecken",
                "Läser rekursivt",
                "Rensar buffern"
            ],
            "correct": 1,
            "explanation": "-r (raw) förhindrar att backslash tolkas som escape-tecken."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
INTERAKTIVA_SKRIPT_FLASHCARDS = [
    {"front": "read -p gör?", "back": "Visar prompt före input"},
    {"front": "read -s gör?", "back": "Silent mode (döljer input)"},
    {"front": "read -n 1 gör?", "back": "Läser endast 1 tecken"},
    {"front": "read -t 5 gör?", "back": "Timeout efter 5 sekunder"},
    {"front": "read -a arr gör?", "back": "Läser input till array"},
    {"front": "read -r gör?", "back": "Raw mode (bevarar backslash)"},
    {"front": "[[ -z \"$var\" ]] kollar?", "back": "Om variabeln är tom"},
    {"front": "[[ -n \"$var\" ]] kollar?", "back": "Om variabeln INTE är tom"},
    {"front": "Regex för endast nummer?", "back": "^[0-9]+$"},
    {"front": "PS3 i select?", "back": "Prompten som visas"},
    {"front": "$REPLY i select?", "back": "Numret användaren skrev"},
    {"front": "Loop tills giltig input?", "back": "while true; do ... break; done"},
    {"front": "Avsluta select?", "back": "break"},
    {"front": "Kombinera -s och -p?", "back": "read -s -p \"Pass: \" var"},
    {"front": "Läs flera variabler?", "back": "read var1 var2 var3"},
    {"front": "Default om timeout?", "back": "if read -t 5 var; then ... else ... fi"},
    {"front": "case * i select?", "back": "Fångar ogiltiga val"},
    {"front": "Validera ja/nej?", "back": "[[ \"$var\" =~ ^(ja|nej)$ ]]"},
    {"front": "Kolla om nummer i range?", "back": "(( num >= min && num <= max ))"},
    {"front": "Echo efter read -s?", "back": "Behövs för ny rad (input visas inte)"},
]
