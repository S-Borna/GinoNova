"""
NOD 1.8: Loopar (for/while/until)
==================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

LOOPAR_NODE = {
    "title": "Loopar - for/while/until",
    "slug": "loopar-for-while-until",
    "description": "Iterera över listor, filer och sekvenser med for, while och until-loopar.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "order_index": 7,
    "content": r"""# Loopar - for/while/until

> **TL;DR:** `for` loopar över listor/filer. `while` kör så länge villkoret är sant. `until` kör tills villkoret blir sant. Använd `break` för att avbryta och `continue` för att hoppa till nästa.

---

## 📖 TEORI: Tre typer av loopar

| Loop | Kör när | Användning |
|------|---------|------------|
| `for` | För varje element i lista | Iterera över filer, argument, sekvenser |
| `while` | Så länge villkor är SANT | Läsa filer, vänta på villkor |
| `until` | Tills villkor blir SANT | Vänta tills något händer |

---

## 📖 for-loop (lista)

### Grundsyntax

```bash
for variabel in lista; do
    kommando
done
```

### Loopa över lista

```bash
# Lista av ord
for frukt in äpple banan citron; do
    echo "Jag gillar $frukt"
done

# Output:
# Jag gillar äpple
# Jag gillar banan
# Jag gillar citron
```

### Loopa över sekvens

```bash
# Med brace expansion {start..slut}
for i in {1..5}; do
    echo "Nummer: $i"
done

# Med steg {start..slut..steg}
for i in {0..10..2}; do
    echo "$i"  # 0, 2, 4, 6, 8, 10
done

# Med seq-kommandot
for i in $(seq 1 5); do
    echo "$i"
done
```

### Loopa över filer (VANLIGT!)

```bash
# Alla .txt-filer i aktuell katalog
for fil in *.txt; do
    echo "Bearbetar: $fil"
    wc -l "$fil"
done

# Alla filer i en katalog
for fil in /var/log/*; do
    if [[ -f "$fil" ]]; then
        echo "$fil"
    fi
done
```

### Loopa över argument

```bash
#!/usr/bin/env bash
# skript.sh

# "$@" = alla argument som separata ord
for arg in "$@"; do
    echo "Argument: $arg"
done

# Kör: ./skript.sh ett "två tre" fyra
# Output:
# Argument: ett
# Argument: två tre
# Argument: fyra
```

---

## 📖 for-loop (C-style)

För de som gillar C/Java-syntax:

```bash
for ((initiering; villkor; steg)); do
    kommando
done
```

### Exempel

```bash
# Räkna 1-10
for ((i=1; i<=10; i++)); do
    echo "$i"
done

# Räkna nedåt
for ((i=10; i>=0; i--)); do
    echo "$i"
done

# Två variabler
for ((i=0, j=10; i<j; i++, j--)); do
    echo "i=$i, j=$j"
done
```

---

## 📖 while-loop

Kör **så länge villkoret är sant**.

### Grundsyntax

```bash
while [ villkor ]; do
    kommando
done
```

### Räknare

```bash
count=1
while [[ $count -le 5 ]]; do
    echo "Iteration: $count"
    ((count++))
done
```

### Oändlig loop

```bash
while true; do
    echo "Tryck Ctrl+C för att avbryta"
    sleep 1
done
```

### Vänta på villkor

```bash
# Vänta tills fil finns
while [[ ! -f "/tmp/ready.flag" ]]; do
    echo "Väntar på flaggfil..."
    sleep 5
done
echo "Flaggfilen finns! Fortsätter..."
```

---

## 📖 Läsa fil rad för rad (VIKTIGT!)

```bash
while IFS= read -r rad; do
    echo "Rad: $rad"
done < fil.txt
```

### Förklaring

| Del | Betydelse |
|-----|-----------|
| `IFS=` | Behåll leading/trailing whitespace |
| `read -r` | Tolka inte backslash som escape |
| `rad` | Variabel som får radens innehåll |
| `< fil.txt` | Input-redirection |

### Praktiskt exempel: Processa config

```bash
#!/usr/bin/env bash
# Läs config.txt och skapa användare

while IFS=: read -r username uid shell; do
    echo "Skapar användare: $username med UID $uid"
    # useradd -u "$uid" -s "$shell" "$username"
done < users.txt

# users.txt:
# alice:1001:/bin/bash
# bob:1002:/bin/zsh
```

### Läsa från kommando

```bash
# Processa output från kommando
ps aux | while read -r user pid cpu mem rest; do
    if [[ $cpu > 50 ]]; then
        echo "Hög CPU: $user ($pid) - $cpu%"
    fi
done
```

---

## 📖 until-loop

Kör **tills villkoret blir sant** (motsatsen till while).

```bash
until [ villkor ]; do
    kommando
done
```

### Exempel

```bash
# Räkna till 5
count=1
until [[ $count -gt 5 ]]; do
    echo "$count"
    ((count++))
done

# Vänta tills server svarar
until ping -c 1 server.example.com &>/dev/null; do
    echo "Väntar på server..."
    sleep 5
done
echo "Servern är uppe!"
```

---

## 📖 Loop-kontroll: break & continue

### break - avbryt loopen helt

```bash
for i in {1..100}; do
    if [[ $i -eq 5 ]]; then
        echo "Hittade 5, avbryter!"
        break
    fi
    echo "$i"
done
# Output: 1, 2, 3, 4, Hittade 5, avbryter!
```

### continue - hoppa till nästa iteration

```bash
for i in {1..5}; do
    if [[ $i -eq 3 ]]; then
        continue  # Hoppa över 3
    fi
    echo "$i"
done
# Output: 1, 2, 4, 5 (3 hoppades över)
```

### break med nivå (nästlade loopar)

```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [[ $j -eq 2 ]]; then
            break 2  # Bryt ut ur BÅDA looparna
        fi
        echo "i=$i, j=$j"
    done
done
# Output: i=1, j=1 (sen avbryts båda looparna)
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Skapa användare (från kursen)

```bash
#!/usr/bin/env bash
# Skapa flera användare

for user in Alice Bob Charlie David Evert; do
    if id "$user" &>/dev/null; then
        echo "⚠️ $user finns redan"
    else
        sudo useradd -m -s /bin/bash "$user"
        echo "✅ Skapade $user"
    fi
done
```

### Exempel 2: Lägg till i grupp (från kursen)

```bash
#!/usr/bin/env bash
# Lägg till användare i developers-gruppen

for user in Alice Charlie Evert; do
    sudo usermod -aG developers "$user"
    echo "Lade till $user i developers"
done
```

### Exempel 3: Batch-operationer på filer

```bash
#!/usr/bin/env bash
# Konvertera alla .txt till .bak

for fil in *.txt; do
    if [[ -f "$fil" ]]; then
        cp "$fil" "${fil%.txt}.bak"
        echo "Kopierade $fil → ${fil%.txt}.bak"
    fi
done
```

### Exempel 4: Processa loggar

```bash
#!/usr/bin/env bash
# Räkna errors i alla loggfiler

total_errors=0
for logfil in /var/log/*.log; do
    if [[ -r "$logfil" ]]; then
        errors=$(grep -c "ERROR" "$logfil" 2>/dev/null || echo 0)
        echo "$logfil: $errors errors"
        ((total_errors += errors))
    fi
done
echo "Totalt: $total_errors errors"
```

### Exempel 5: Meny med while

```bash
#!/usr/bin/env bash

while true; do
    echo ""
    echo "=== MENY ==="
    echo "1) Visa datum"
    echo "2) Visa filer"
    echo "3) Avsluta"
    read -p "Val: " val

    case $val in
        1) date ;;
        2) ls -la ;;
        3) echo "Hejdå!"; break ;;
        *) echo "Ogiltigt val!" ;;
    esac
done
```

---

## 📖 När använda vilken loop?

| Situation | Loop | Exempel |
|-----------|------|---------|
| Känd lista | `for ... in` | `for f in *.txt` |
| Känt antal | `for ((i=0...))` | `for ((i=0; i<10; i++))` |
| Okänt antal, kör medan sant | `while` | `while [[ $count -lt 10 ]]` |
| Läsa fil rad för rad | `while read` | `while read line` |
| Vänta tills något händer | `until` | `until ping server` |

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | for-loop syntax? | for var in lista; do ... done |
| 2 | while-loop syntax? | while [ villkor ]; do ... done |
| 3 | until-loop syntax? | until [ villkor ]; do ... done |
| 4 | Loopa över alla argument? | for arg in "$@"; do |
| 5 | Loopa över alla .txt-filer? | for f in *.txt; do |
| 6 | Sekvens 1-10? | for i in {1..10}; do |
| 7 | break gör? | Avbryter loopen helt |
| 8 | continue gör? | Hoppar till nästa iteration |
| 9 | Läsa fil rad för rad? | while IFS= read -r rad; do ... done < fil |
| 10 | while vs until? | while: kör medan sant. until: kör tills sant |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är korrekt syntax för en for-loop?**
- A) for i in 1 2 3 { echo $i }
- B) for i in 1 2 3; do echo $i; done ✅
- C) for (i in 1 2 3) do echo $i done
- D) foreach i (1 2 3); echo $i; end

**2. Hur loopar du över alla .sh-filer?**
- A) for f = *.sh
- B) for f in *.sh; do ✅
- C) foreach f *.sh
- D) loop f in *.sh

**3. Vad gör `break`?**
- A) Pausar loopen tillfälligt
- B) Hoppar till nästa iteration
- C) Avbryter loopen helt ✅
- D) Avslutar skriptet

**4. Vad gör `continue`?**
- A) Fortsätter efter loopen
- B) Hoppar till nästa iteration ✅
- C) Avbryter loopen
- D) Väntar på input

**5. Hur läser du en fil rad för rad?**
- A) for rad in fil.txt; do
- B) read fil.txt | while
- C) while IFS= read -r rad; do ... done < fil.txt ✅
- D) cat fil.txt | for rad; do

**6. Vad är skillnaden mellan while och until?**
- A) Ingen skillnad
- B) while kör medan sant, until kör tills sant ✅
- C) until är snabbare
- D) while är för filer, until för nummer

**7. Hur skapar du en sekvens 1-100 i for-loop?**
- A) for i in 1-100
- B) for i in {1..100} ✅
- C) for i in [1,100]
- D) for i in seq(1,100)

**8. Vad gör `break 2`?**
- A) Väntar 2 sekunder
- B) Bryter ur 2 nivåer av nästlade loopar ✅
- C) Kör loopen 2 gånger till
- D) Syntaxfel

**9. Hur loopar du över alla skriptargument?**
- A) for arg in $*
- B) for arg in "$@" ✅
- C) for arg in $ARGS
- D) for arg in arguments

**10. Vad betyder IFS= i `while IFS= read -r`?**
- A) Ignorerar filen
- B) Behåller whitespace i början/slutet av rader ✅
- C) Snabbare läsning
- D) Filseparator

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Räkna filer
Skriv ett skript som räknar antal filer av varje typ i aktuell katalog:
```bash
#!/usr/bin/env bash
txt=0; sh=0; other=0
for f in *; do
    case $f in
        *.txt) ((txt++)) ;;
        *.sh) ((sh++)) ;;
        *) ((other++)) ;;
    esac
done
echo "txt: $txt, sh: $sh, other: $other"
```

### Övning 2: Processa användarlista
Skapa `users.txt`:
```
alice:1001:developers
bob:1002:admins
charlie:1003:developers
```

Skriv skript som läser filen och visar info:
```bash
while IFS=: read -r user uid group; do
    echo "Användare $user (UID: $uid) i grupp $group"
done < users.txt
```

### Övning 3: Vänta på server
Skriv ett skript som väntar tills en server svarar på ping:
```bash
#!/usr/bin/env bash
server="${1:-localhost}"
until ping -c 1 "$server" &>/dev/null; do
    echo "Väntar på $server..."
    sleep 2
done
echo "$server är uppe!"
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `for f in *.txt` utan citattecken | Problem med filnamn med mellanslag | Citera variabeln: `"$f"` |
| Glömmer `done` | Syntaxfel | Matcha varje `do` med `done` |
| `while read` utan `-r` | Backslash tolkas fel | Använd `read -r` |
| Ändra variabel i pipe | Ändringen försvinner | Undvik pipe, använd `< fil` |
| Oändlig loop | Scriptet hänger | Kolla att villkoret kan bli falskt |

---

## 📝 SAMMANFATTNING

```bash
# FOR-LOOP (lista)
for var in lista; do
    echo "$var"
done

# FOR-LOOP (C-style)
for ((i=0; i<10; i++)); do
    echo "$i"
done

# FOR över filer
for f in *.txt; do echo "$f"; done

# FOR över argument
for arg in "$@"; do echo "$arg"; done

# WHILE (kör medan sant)
while [[ $x -lt 10 ]]; do
    ((x++))
done

# UNTIL (kör tills sant)
until [[ $x -ge 10 ]]; do
    ((x++))
done

# LÄSA FIL
while IFS= read -r rad; do
    echo "$rad"
done < fil.txt

# KONTROLL
break      # avbryt loop
continue   # nästa iteration
```

""",
    "quiz": [
        {
            "question": "Vad är korrekt syntax för en for-loop?",
            "options": [
                "for i in 1 2 3 { echo $i }",
                "for i in 1 2 3; do echo $i; done",
                "for (i in 1 2 3) do echo $i done",
                "foreach i (1 2 3); echo $i; end"
            ],
            "correct": 1,
            "explanation": "Bash for-loop: for VAR in LIST; do COMMANDS; done"
        },
        {
            "question": "Hur loopar du över alla .sh-filer i katalogen?",
            "options": [
                "for f = *.sh",
                "for f in *.sh; do",
                "foreach f *.sh",
                "loop f in *.sh"
            ],
            "correct": 1,
            "explanation": "for f in *.sh; do ... done. Glob-mönstret expanderas till alla matchande filer."
        },
        {
            "question": "Vad gör break i en loop?",
            "options": [
                "Pausar loopen tillfälligt",
                "Hoppar till nästa iteration",
                "Avbryter loopen helt och fortsätter efter done",
                "Avslutar hela skriptet"
            ],
            "correct": 2,
            "explanation": "break avbryter loopen helt och körningen fortsätter efter done."
        },
        {
            "question": "Vad gör continue i en loop?",
            "options": [
                "Fortsätter efter loopen",
                "Hoppar till nästa iteration av loopen",
                "Avbryter loopen helt",
                "Väntar på användarinput"
            ],
            "correct": 1,
            "explanation": "continue hoppar över resten av loopkroppen och går till nästa iteration."
        },
        {
            "question": "Hur läser du en fil rad för rad korrekt?",
            "options": [
                "for rad in fil.txt; do",
                "read fil.txt | while",
                "while IFS= read -r rad; do ... done < fil.txt",
                "cat fil.txt | for rad; do"
            ],
            "correct": 2,
            "explanation": "while IFS= read -r rad är rätt sätt. IFS= behåller whitespace, -r hanterar backslash korrekt."
        },
        {
            "question": "Vad är skillnaden mellan while och until?",
            "options": [
                "Ingen praktisk skillnad",
                "while kör medan villkoret är sant, until kör tills villkoret blir sant",
                "until är snabbare",
                "while är för filer, until är för nummer"
            ],
            "correct": 1,
            "explanation": "while fortsätter medan villkoret är sant. until fortsätter tills villkoret blir sant."
        },
        {
            "question": "Hur skapar du en sekvens 1-100 i en for-loop?",
            "options": [
                "for i in 1-100",
                "for i in {1..100}",
                "for i in [1,100]",
                "for i in seq(1,100)"
            ],
            "correct": 1,
            "explanation": "{1..100} är brace expansion som genererar sekvensen 1, 2, 3, ... 100."
        },
        {
            "question": "Vad gör break 2 i nästlade loopar?",
            "options": [
                "Väntar 2 sekunder innan break",
                "Bryter ur 2 nivåer av nästlade loopar",
                "Kör loopen 2 gånger till",
                "Det är ett syntaxfel"
            ],
            "correct": 1,
            "explanation": "break 2 bryter ur två nivåer av nästlade loopar på en gång."
        },
        {
            "question": "Hur loopar du korrekt över alla skriptargument?",
            "options": [
                "for arg in $*",
                "for arg in \"$@\"",
                "for arg in $ARGS",
                "for arg in arguments"
            ],
            "correct": 1,
            "explanation": "\"$@\" ger alla argument som separata ord, även de med mellanslag."
        },
        {
            "question": "Vad betyder IFS= i while IFS= read -r?",
            "options": [
                "Ignorerar filen helt",
                "Behåller whitespace i början och slutet av rader",
                "Gör läsningen snabbare",
                "Sätter filseparatorn"
            ],
            "correct": 1,
            "explanation": "IFS= (tom) gör att leading/trailing whitespace inte tas bort från raderna."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
LOOPAR_FLASHCARDS = [
    {"front": "for-loop syntax (lista)?", "back": "for var in lista; do ... done"},
    {"front": "for-loop syntax (C-style)?", "back": "for ((i=0; i<10; i++)); do ... done"},
    {"front": "while-loop syntax?", "back": "while [ villkor ]; do ... done"},
    {"front": "until-loop syntax?", "back": "until [ villkor ]; do ... done"},
    {"front": "Loopa över alla argument?", "back": "for arg in \"$@\"; do"},
    {"front": "Loopa över alla .txt-filer?", "back": "for f in *.txt; do"},
    {"front": "Sekvens 1-10 i for?", "back": "for i in {1..10}; do"},
    {"front": "Sekvens med steg (0,2,4,6...)?", "back": "for i in {0..10..2}; do"},
    {"front": "break gör?", "back": "Avbryter loopen helt"},
    {"front": "continue gör?", "back": "Hoppar till nästa iteration"},
    {"front": "break 2 gör?", "back": "Bryter ur 2 nivåer av nästlade loopar"},
    {"front": "Läsa fil rad för rad?", "back": "while IFS= read -r rad; do ... done < fil"},
    {"front": "IFS= i read betyder?", "back": "Behåll whitespace i början/slutet"},
    {"front": "read -r betyder?", "back": "Tolka inte backslash som escape"},
    {"front": "while vs until?", "back": "while: kör medan sant. until: kör tills sant"},
    {"front": "Oändlig loop?", "back": "while true; do ... done"},
    {"front": "C-style räkna 1-10?", "back": "for ((i=1; i<=10; i++)); do"},
    {"front": "Vänta på fil?", "back": "while [[ ! -f fil ]]; do sleep 1; done"},
    {"front": "Loopa och räkna?", "back": "count=0; for f in *; do ((count++)); done"},
    {"front": "done matchar?", "back": "do (varje do måste ha en done)"},
]
