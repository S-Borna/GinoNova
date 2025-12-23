"""
NOD 1.6: Villkor (if/elif/else/case)
=====================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

VILLKOR_NODE = {
    "title": "Villkor - if/elif/else/case",
    "slug": "villkor-if-elif-else-case",
    "description": "Kontrollera flödet i dina skript med if-satser, testoperatorer och case-satser.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "order_index": 5,
    "content": r"""# Villkor - if/elif/else/case

> **TL;DR:** `if [ villkor ]; then` testar något och kör kod om det är sant. Använd `-eq` för nummer, `==` för strängar, `-f` för filer. Glöm inte mellanslag efter `[` och före `]`!

---

## 📖 TEORI: if-satser

### Grundstruktur

```bash
if [ villkor ]; then
    kommando
fi
```

### Med elif och else

```bash
if [ villkor1 ]; then
    echo "Villkor 1 är sant"
elif [ villkor2 ]; then
    echo "Villkor 2 är sant"
else
    echo "Inget villkor var sant"
fi
```

### ⚠️ KRITISKT: Mellanslag!

```bash
if [ $x -eq 5 ]; then    # ✅ Rätt - mellanslag efter [ och före ]
if [$x -eq 5]; then      # ❌ FEL! - saknar mellanslag
if [ $x -eq 5]; then     # ❌ FEL! - saknar mellanslag före ]
```

---

## 📖 [ ] vs [[ ]]

| Syntax | Typ | Fördelar |
|--------|-----|----------|
| `[ ]` | POSIX | Funkar i alla shells |
| `[[ ]]` | Bash | Kraftfullare, säkrare, rekommenderas |

### Skillnader i praktiken

```bash
# Med [ ] - måste citera variabler
if [ "$namn" = "Lisa" ]; then

# Med [[ ]] - behöver inte citera (men gör det ändå)
if [[ $namn == "Lisa" ]]; then

# [[ ]] stödjer regex!
if [[ $email =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]; then

# [[ ]] stödjer && och || direkt
if [[ $x -gt 5 && $x -lt 10 ]]; then

# [ ] kräver -a och -o (UNDVIK!)
if [ $x -gt 5 -a $x -lt 10 ]; then
```

**Rekommendation:** Använd `[[ ]]` i Bash-skript!

---

## 📖 Strängjämförelser

| Operator | Betydelse | Exempel |
|----------|-----------|---------|
| `=` eller `==` | Lika med | `[[ "$a" == "$b" ]]` |
| `!=` | Inte lika | `[[ "$a" != "$b" ]]` |
| `-z` | Tom sträng (zero) | `[[ -z "$var" ]]` |
| `-n` | Inte tom (non-zero) | `[[ -n "$var" ]]` |
| `<` | Alfabetiskt mindre | `[[ "$a" < "$b" ]]` |
| `>` | Alfabetiskt större | `[[ "$a" > "$b" ]]` |

### Exempel

```bash
namn="Lisa"

# Kolla om variabel är tom
if [[ -z "$namn" ]]; then
    echo "Namn saknas!"
fi

# Kolla om variabel har värde
if [[ -n "$namn" ]]; then
    echo "Namn är: $namn"
fi

# Jämföra strängar
if [[ "$namn" == "Lisa" ]]; then
    echo "Hej Lisa!"
fi
```

### ⚠️ VANLIGT MISSTAG

```bash
# FEL: Använder -eq för strängar
if [[ "$namn" -eq "Lisa" ]]; then    # ❌ -eq är för nummer!

# RÄTT: Använder == för strängar
if [[ "$namn" == "Lisa" ]]; then     # ✅
```

---

## 📖 Nummerjämförelser

| Operator | Betydelse | Matematiskt |
|----------|-----------|-------------|
| `-eq` | Equal (lika) | = |
| `-ne` | Not equal | ≠ |
| `-lt` | Less than | < |
| `-le` | Less than or equal | ≤ |
| `-gt` | Greater than | > |
| `-ge` | Greater than or equal | ≥ |

### Exempel

```bash
ålder=25

if [[ $ålder -lt 18 ]]; then
    echo "Minderårig"
elif [[ $ålder -ge 18 && $ålder -lt 65 ]]; then
    echo "Vuxen"
else
    echo "Pensionär"
fi
```

### Minnesregel

```
-eq = EQual
-ne = Not Equal
-lt = Less Than
-le = Less or Equal
-gt = Greater Than
-ge = Greater or Equal
```

---

## 📖 Filtester (MYCKET VIKTIGT!)

| Operator | Testar | Exempel |
|----------|--------|---------|
| `-e` | Finns (exists) | `[[ -e fil.txt ]]` |
| `-f` | Är vanlig fil (file) | `[[ -f fil.txt ]]` |
| `-d` | Är katalog (directory) | `[[ -d /home ]]` |
| `-r` | Läsbar (readable) | `[[ -r fil.txt ]]` |
| `-w` | Skrivbar (writable) | `[[ -w fil.txt ]]` |
| `-x` | Körbar (executable) | `[[ -x skript.sh ]]` |
| `-s` | Har innehåll (size > 0) | `[[ -s fil.txt ]]` |
| `-L` | Är symbolisk länk | `[[ -L länk ]]` |

### Praktiska exempel

```bash
#!/usr/bin/env bash

# Kolla om fil finns
if [[ -f "/etc/passwd" ]]; then
    echo "passwd finns"
fi

# Kolla om katalog finns
if [[ -d "$HOME/projekt" ]]; then
    echo "Projektkatalogen finns"
else
    mkdir "$HOME/projekt"
    echo "Skapade projektkatalogen"
fi

# Kolla om skript är körbart
if [[ -x "./backup.sh" ]]; then
    ./backup.sh
else
    echo "backup.sh är inte körbart!"
    chmod +x ./backup.sh
fi

# Kolla om loggfil har innehåll
if [[ -s "/var/log/app.log" ]]; then
    echo "Loggen har innehåll"
else
    echo "Loggen är tom"
fi
```

---

## 📖 Logiska operatorer

| Operator | Betydelse | Inom [[ ]] | Mellan kommandon |
|----------|-----------|------------|------------------|
| OCH | Båda sanna | `&&` | `&&` |
| ELLER | Minst en sann | `\|\|` | `\|\|` |
| INTE | Negera | `!` | `!` |

### Exempel

```bash
# OCH - båda villkor måste vara sanna
if [[ $ålder -ge 18 && $har_körkort == "ja" ]]; then
    echo "Du får köra bil"
fi

# ELLER - minst ett villkor sant
if [[ $dag == "lördag" || $dag == "söndag" ]]; then
    echo "Det är helg!"
fi

# INTE - negera villkoret
if [[ ! -f "config.txt" ]]; then
    echo "Config saknas!"
fi

# Kombinera
if [[ -f "$fil" && -r "$fil" && ! -d "$fil" ]]; then
    echo "Filen finns, är läsbar och är inte en katalog"
fi
```

---

## 📖 case-satser

Perfekt för flera alternativ (som switch i andra språk):

### Grundstruktur

```bash
case $variabel in
    mönster1)
        kommando
        ;;
    mönster2)
        kommando
        ;;
    *)
        default-kommando
        ;;
esac
```

### Exempel: Menyval

```bash
#!/usr/bin/env bash
echo "Välj ett alternativ:"
echo "1) Visa filer"
echo "2) Visa datum"
echo "3) Avsluta"
read -p "Val: " val

case $val in
    1)
        ls -la
        ;;
    2)
        date
        ;;
    3)
        echo "Hejdå!"
        exit 0
        ;;
    *)
        echo "Ogiltigt val!"
        exit 1
        ;;
esac
```

### Mönster med OR (|)

```bash
case $svar in
    ja|Ja|JA|j|J)
        echo "Du svarade ja"
        ;;
    nej|Nej|NEJ|n|N)
        echo "Du svarade nej"
        ;;
    *)
        echo "Jag förstod inte"
        ;;
esac
```

### Wildcards i case

```bash
case $filnamn in
    *.txt)
        echo "Textfil"
        ;;
    *.sh)
        echo "Skriptfil"
        ;;
    *.tar.gz|*.tgz)
        echo "Komprimerat arkiv"
        ;;
    *)
        echo "Okänd filtyp"
        ;;
esac
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Validera argument

```bash
#!/usr/bin/env bash

# Kolla att argument finns
if [[ -z "$1" ]]; then
    echo "Användning: $0 <filnamn>"
    exit 1
fi

# Kolla att filen finns
if [[ ! -f "$1" ]]; then
    echo "Fel: $1 finns inte!"
    exit 1
fi

echo "Bearbetar $1..."
```

### Exempel 2: Kräv root

```bash
#!/usr/bin/env bash

# Kolla om vi är root
if [[ "$EUID" -ne 0 ]]; then
    echo "❌ Detta skript måste köras som root!"
    echo "Kör: sudo $0"
    exit 1
fi

echo "✅ Körs som root, fortsätter..."
```

### Exempel 3: Installationsskript

```bash
#!/usr/bin/env bash
set -e

# Detektera OS
case "$(uname -s)" in
    Linux*)
        OS="Linux"
        PKG_MGR="apt-get"
        ;;
    Darwin*)
        OS="Mac"
        PKG_MGR="brew"
        ;;
    *)
        echo "Okänt OS!"
        exit 1
        ;;
esac

echo "Detekterade: $OS"
echo "Pakethanterare: $PKG_MGR"
```

### Exempel 4: Komplett valideringsskript

```bash
#!/usr/bin/env bash
set -euo pipefail

# Funktion för validering
validate_input() {
    local input="$1"

    # Kolla att input inte är tom
    if [[ -z "$input" ]]; then
        echo "Fel: Tom input"
        return 1
    fi

    # Kolla att det är ett nummer
    if [[ ! "$input" =~ ^[0-9]+$ ]]; then
        echo "Fel: Måste vara ett nummer"
        return 1
    fi

    # Kolla intervall
    if [[ "$input" -lt 1 || "$input" -gt 100 ]]; then
        echo "Fel: Måste vara mellan 1-100"
        return 1
    fi

    return 0
}

# Huvudprogram
read -p "Ange ett nummer (1-100): " nummer

if validate_input "$nummer"; then
    echo "✅ $nummer är giltigt!"
else
    exit 1
fi
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Syntax för if-sats? | if [ villkor ]; then ... fi |
| 2 | -eq testar? | Nummer är LIKA |
| 3 | -ne testar? | Nummer är INTE lika |
| 4 | -lt testar? | Nummer är MINDRE än |
| 5 | -gt testar? | Nummer är STÖRRE än |
| 6 | -z "$var" testar? | Om variabeln är TOM |
| 7 | -f fil testar? | Om det är en vanlig FIL |
| 8 | -d sökväg testar? | Om det är en KATALOG |
| 9 | Skillnad [ ] och [[ ]]? | [[ ]] är Bash-specifik, kraftfullare |
| 10 | case avslutas med? | esac (case baklänges) |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilken operator jämför om två nummer är lika?**
- A) ==
- B) =
- C) -eq ✅
- D) -equal

**2. Vad testar `[[ -z "$var" ]]`?**
- A) Om variabeln finns
- B) Om variabeln är tom ✅
- C) Om variabeln är noll
- D) Om variabeln är ett nummer

**3. Vilken operator testar om en fil finns?**
- A) -f
- B) -e ✅
- C) -x
- D) -exists

**4. Vad är skillnaden mellan -f och -e?**
- A) Ingen skillnad
- B) -f testar vanlig fil, -e testar om något finns ✅
- C) -e testar vanlig fil, -f testar om något finns
- D) -f är för kataloger

**5. Hur avslutas en case-sats?**
- A) end
- B) done
- C) esac ✅
- D) fi

**6. Vad är fel med `if [$x -eq 5]; then`?**
- A) -eq ska vara ==
- B) Mellanslag saknas efter [ och före ] ✅
- C) then ska vara do
- D) Inget fel

**7. Vad testar `[[ -d "/home" ]]`?**
- A) Om /home finns
- B) Om /home är en katalog ✅
- C) Om /home är en fil
- D) Om /home är tom

**8. Vilken operator används för "större än eller lika med"?**
- A) -gt
- B) -gte
- C) -ge ✅
- D) >=

**9. Hur kombinerar du två villkor med OCH i [[ ]]?**
- A) -a
- B) AND
- C) && ✅
- D) -and

**10. Vad gör `[[ ! -f "fil.txt" ]]`?**
- A) Testar om fil.txt finns
- B) Testar om fil.txt INTE finns ✅
- C) Tar bort fil.txt
- D) Skapar fil.txt

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Filkontroll
Skriv ett skript som:
1. Tar ett filnamn som argument
2. Kontrollerar om filen finns (-e)
3. Om den finns: visa om det är fil (-f) eller katalog (-d)
4. Om det är en fil: visa om den är läsbar (-r), skrivbar (-w), körbar (-x)

```bash
#!/usr/bin/env bash
if [[ -z "$1" ]]; then
    echo "Ange ett filnamn"
    exit 1
fi

if [[ -e "$1" ]]; then
    echo "$1 finns"
    [[ -f "$1" ]] && echo "  - Det är en fil"
    [[ -d "$1" ]] && echo "  - Det är en katalog"
    [[ -r "$1" ]] && echo "  - Läsbar"
    [[ -w "$1" ]] && echo "  - Skrivbar"
    [[ -x "$1" ]] && echo "  - Körbar"
else
    echo "$1 finns inte"
fi
```

### Övning 2: Ålderskontroll
Skriv ett skript som:
1. Frågar efter ålder med `read`
2. Använder if/elif/else för att kategorisera:
   - Under 13: "Barn"
   - 13-19: "Tonåring"
   - 20-64: "Vuxen"
   - 65+: "Senior"

### Övning 3: Meny med case
Skapa en meny som låter användaren välja:
1. Visa datum
2. Visa diskutrymme (df -h)
3. Visa vem som är inloggad (who)
q. Avsluta

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `if [$x -eq 5]` | Saknar mellanslag | `if [ $x -eq 5 ]` |
| `if [ $x == 5 ]` | == för strängar, -eq för nummer | `if [ $x -eq 5 ]` |
| `if [ $var = "" ]` | Fungerar, men oläsligt | `if [ -z "$var" ]` |
| Ocitera variabler | Fel om variabel är tom | `if [ "$var" = "x" ]` |
| `case` utan `;;` | Faller igenom till nästa | Avsluta med `;;` |
| Glömmer `fi` | Syntaxfel | Matcha varje `if` med `fi` |

---

## 📝 SAMMANFATTNING

```bash
# IF-SATS
if [[ villkor ]]; then
    kommando
elif [[ annat ]]; then
    kommando
else
    kommando
fi

# STRÄNGAR
[[ "$a" == "$b" ]]    # Lika
[[ "$a" != "$b" ]]    # Olika
[[ -z "$a" ]]         # Tom
[[ -n "$a" ]]         # Inte tom

# NUMMER
[[ $x -eq $y ]]       # Lika (equal)
[[ $x -ne $y ]]       # Inte lika (not equal)
[[ $x -lt $y ]]       # Mindre (less than)
[[ $x -gt $y ]]       # Större (greater than)
[[ $x -le $y ]]       # Mindre/lika (less or equal)
[[ $x -ge $y ]]       # Större/lika (greater or equal)

# FILER
[[ -e fil ]]          # Finns
[[ -f fil ]]          # Är fil
[[ -d fil ]]          # Är katalog
[[ -r fil ]]          # Läsbar
[[ -w fil ]]          # Skrivbar
[[ -x fil ]]          # Körbar

# CASE
case $var in
    mönster) kommando ;;
    *) default ;;
esac
```

""",
    "quiz": [
        {
            "question": "Vilken operator jämför om två nummer är lika?",
            "options": [
                "==",
                "=",
                "-eq",
                "-equal"
            ],
            "correct": 2,
            "explanation": "-eq (equal) används för nummerjämförelser. == är för strängar."
        },
        {
            "question": "Vad testar [[ -z \"$var\" ]]?",
            "options": [
                "Om variabeln finns definierad",
                "Om variabeln är tom (zero length)",
                "Om variabeln är noll",
                "Om variabeln är ett nummer"
            ],
            "correct": 1,
            "explanation": "-z testar om strängen är tom (zero length). -n testar motsatsen."
        },
        {
            "question": "Vilken operator testar om en fil finns?",
            "options": [
                "-f",
                "-e",
                "-x",
                "-exists"
            ],
            "correct": 1,
            "explanation": "-e (exists) testar om filen/katalogen finns. -f testar om det är en vanlig fil."
        },
        {
            "question": "Vad är skillnaden mellan -f och -e?",
            "options": [
                "Ingen skillnad",
                "-f testar vanlig fil, -e testar om något finns överhuvudtaget",
                "-e testar vanlig fil, -f testar om något finns",
                "-f är för kataloger"
            ],
            "correct": 1,
            "explanation": "-e = exists (fil, katalog, länk etc). -f = file (vanlig fil, inte katalog)."
        },
        {
            "question": "Hur avslutas en case-sats?",
            "options": [
                "end",
                "done",
                "esac",
                "fi"
            ],
            "correct": 2,
            "explanation": "case avslutas med esac (case baklänges). fi avslutar if-satser."
        },
        {
            "question": "Vad är fel med if [$x -eq 5]; then?",
            "options": [
                "-eq ska vara ==",
                "Mellanslag saknas efter [ och före ]",
                "then ska vara do",
                "Inget fel"
            ],
            "correct": 1,
            "explanation": "[ är ett kommando och kräver mellanslag runt sig: [ $x -eq 5 ]"
        },
        {
            "question": "Vad testar [[ -d \"/home\" ]]?",
            "options": [
                "Om /home finns",
                "Om /home är en katalog (directory)",
                "Om /home är en fil",
                "Om /home är tom"
            ],
            "correct": 1,
            "explanation": "-d testar om sökvägen är en katalog (directory)."
        },
        {
            "question": "Vilken operator används för 'större än eller lika med' för nummer?",
            "options": [
                "-gt",
                "-gte",
                "-ge",
                ">="
            ],
            "correct": 2,
            "explanation": "-ge = greater than or equal. >= fungerar inte i [ ] för nummer."
        },
        {
            "question": "Hur kombinerar du två villkor med OCH i [[ ]]?",
            "options": [
                "-a",
                "AND",
                "&&",
                "-and"
            ],
            "correct": 2,
            "explanation": "&& används för OCH i [[ ]]. -a är gammal syntax för [ ] (undvik)."
        },
        {
            "question": "Vad gör [[ ! -f \"fil.txt\" ]]?",
            "options": [
                "Testar om fil.txt finns och är en fil",
                "Testar om fil.txt INTE finns eller inte är en fil",
                "Tar bort fil.txt",
                "Skapar fil.txt"
            ],
            "correct": 1,
            "explanation": "! negerar villkoret. Sant om fil.txt INTE är en vanlig fil."
        }
    ]
}

