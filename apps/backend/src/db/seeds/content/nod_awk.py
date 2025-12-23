"""
NOD 1.5: Awk (Pattern Processing)
==================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

AWK_NODE = {
    "title": "Awk - Pattern Processing",
    "slug": "awk-pattern-processing",
    "description": "Extrahera och bearbeta data med awk - fält, mönster och inbyggda variabler.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "order_index": 4,
    "content": r"""# Awk - Pattern Processing

> **TL;DR:** Awk delar upp varje rad i fält (kolumner). Med `$1`, `$2` etc. plockar du ut exakt den data du vill ha. Perfekt för att bearbeta loggar, CSV-filer och /etc/passwd!

---

## 📖 TEORI: Vad är awk?

**awk** är ett komplett programmeringsspråk för textbearbetning:

- Delar upp rader i **fält** (kolumner)
- Perfekt för **strukturerad data** (CSV, loggar, passwd)
- Kan göra beräkningar och villkor
- Mycket kraftfullare än grep och sed

### Hur awk ser en rad

```
                    $0 (hela raden)
    ┌─────────────────────────────────────────┐
    │ Lisa    25    Stockholm    Developer    │
    └─────────────────────────────────────────┘
       │       │        │           │
      $1      $2       $3          $4
     (fält1) (fält2)  (fält3)    (fält4)
```

Default-separator: **mellanslag** eller **tab**

---

## 📖 Grundläggande syntax

```bash
awk 'mönster {aktion}' fil
```

| Del | Betydelse |
|-----|-----------|
| `mönster` | Vilka rader ska bearbetas (kan utelämnas = alla) |
| `{aktion}` | Vad ska göras med raden |

### De vanligaste kommandona

```bash
# Skriv ut hela filen (som cat)
awk '{print}' fil.txt

# Skriv ut första fältet
awk '{print $1}' fil.txt

# Skriv ut fält 1 och 3
awk '{print $1, $3}' fil.txt

# Skriv ut hela raden
awk '{print $0}' fil.txt
```

---

## 📖 Field Separator (-F)

Default: mellanslag/tab. Ändra med `-F`:

```bash
# /etc/passwd använder : som separator
awk -F: '{print $1}' /etc/passwd

# CSV-filer använder ,
awk -F, '{print $1, $2}' data.csv

# Flera tecken som separator
awk -F'[,;:]' '{print $1}' fil.txt
```

### Visuellt: /etc/passwd

```
root:x:0:0:root:/root:/bin/bash
 │   │ │ │  │     │      │
$1  $2 $3 $4 $5   $6     $7

$1 = root (användarnamn)
$2 = x (lösenord, placeholder)
$3 = 0 (UID)
$4 = 0 (GID)
$5 = root (GECOS/kommentar)
$6 = /root (hemkatalog)
$7 = /bin/bash (shell)
```

---

## 📖 Inbyggda variabler

| Variabel | Betydelse | Exempel |
|----------|-----------|---------|
| `$0` | Hela raden | `awk '{print $0}'` |
| `$1, $2...` | Fält 1, 2... | `awk '{print $1}'` |
| `NF` | Antal fält på raden | `awk '{print NF}'` |
| `NR` | Radnummer (1, 2, 3...) | `awk '{print NR}'` |
| `FS` | Field separator (input) | `awk 'BEGIN{FS=":"}'` |
| `OFS` | Output field separator | `awk 'BEGIN{OFS=","}'` |
| `RS` | Record separator | Default: newline |
| `ORS` | Output record separator | Default: newline |

### Exempel med NF och NR

```bash
# Visa radnummer + rad
awk '{print NR, $0}' fil.txt
# Output:
# 1 första raden
# 2 andra raden
# 3 tredje raden

# Visa antal fält per rad
awk '{print NF, "fält på rad", NR}' fil.txt

# Skriv ut sista fältet (oavsett antal fält)
awk '{print $NF}' fil.txt

# Näst sista fältet
awk '{print $(NF-1)}' fil.txt
```

---

## 📖 Pattern Matching (mönster)

### Regex-mönster

```bash
# Rader som innehåller "error"
awk '/error/ {print}' log.txt

# Rader som börjar med #
awk '/^#/ {print}' config.txt

# Rader som INTE matchar
awk '!/^#/ {print}' config.txt
```

### Villkor på fält

```bash
# Fält 3 större än 100
awk '$3 > 100 {print}' data.txt

# Fält 1 är exakt "Lisa"
awk '$1 == "Lisa" {print}' data.txt

# Fält 2 innehåller "admin"
awk '$2 ~ /admin/ {print}' users.txt

# Fält 2 innehåller INTE "admin"
awk '$2 !~ /admin/ {print}' users.txt
```

### Kombinera villkor

```bash
# OCH (&&)
awk '$3 > 100 && $4 == "active" {print}' data.txt

# ELLER (||)
awk '$1 == "error" || $1 == "warning" {print}' log.txt
```

---

## 📖 BEGIN och END

Kod som körs **före** och **efter** radbearbetning:

```bash
awk 'BEGIN {kod före} {kod per rad} END {kod efter}' fil
```

### Exempel: Räkna rader

```bash
awk 'BEGIN {print "=== START ==="}
     {print NR, $0}
     END {print "=== SLUT: " NR " rader ==="}' fil.txt
```

**Output:**
```
=== START ===
1 första raden
2 andra raden
3 tredje raden
=== SLUT: 3 rader ===
```

### Exempel: Summa av kolumn

```bash
# data.txt:
# Lisa 100
# Erik 200
# Anna 150

awk '{sum += $2} END {print "Total:", sum}' data.txt
# Output: Total: 450
```

### Exempel: Sätt separator i BEGIN

```bash
awk 'BEGIN {FS=":"; OFS=","} {print $1, $3}' /etc/passwd
# Output: root,0
#         daemon,1
#         ...
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: /etc/passwd

```bash
# Lista alla användarnamn
awk -F: '{print $1}' /etc/passwd

# Lista användare med UID >= 1000 (vanliga användare)
awk -F: '$3 >= 1000 {print $1, $3}' /etc/passwd

# Hitta högsta UID
awk -F: '$3 >= 1000 {print $3}' /etc/passwd | sort -n | tail -1

# Räkna användare med bash som shell
awk -F: '$7 ~ /bash/ {count++} END {print count}' /etc/passwd
```

### Exempel 2: Loggfil-analys

```bash
# access.log:
# 192.168.1.1 - - [23/Dec/2024] "GET /index.html" 200 1234
# 192.168.1.2 - - [23/Dec/2024] "GET /api/users" 404 567

# Extrahera IP-adresser
awk '{print $1}' access.log

# Räkna unika IP:n
awk '{print $1}' access.log | sort -u | wc -l

# Hitta 404-fel
awk '$9 == 404 {print $1, $7}' access.log

# Räkna requests per IP
awk '{ip[$1]++} END {for (i in ip) print i, ip[i]}' access.log
```

### Exempel 3: CSV-bearbetning

```bash
# data.csv:
# namn,ålder,stad
# Lisa,25,Stockholm
# Erik,30,Göteborg

# Skippa header, skriv namn och stad
awk -F, 'NR > 1 {print $1, $3}' data.csv

# Beräkna medelålder
awk -F, 'NR > 1 {sum += $2; count++} END {print "Medel:", sum/count}' data.csv
```

### Exempel 4: Formaterad output

```bash
# Kolumnformaterad output med printf
awk -F: '{printf "%-15s UID: %5d\n", $1, $3}' /etc/passwd

# Output:
# root            UID:     0
# daemon          UID:     1
# student         UID:  1000
```

---

## 📖 printf - Formaterad output

| Format | Betydelse | Exempel |
|--------|-----------|---------|
| `%s` | Sträng | `printf "%s", $1` |
| `%d` | Heltal | `printf "%d", $3` |
| `%f` | Decimaltal | `printf "%.2f", $2` |
| `%-10s` | Vänsterjusterad, 10 tecken | `printf "%-10s", $1` |
| `%5d` | Högerjusterad, 5 siffror | `printf "%5d", $3` |
| `\n` | Ny rad | `printf "%s\n", $1` |
| `\t` | Tab | `printf "%s\t%s\n", $1, $2` |

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | $1 i awk? | Första fältet på raden |
| 2 | $0 i awk? | Hela raden |
| 3 | NF i awk? | Antal fält på raden |
| 4 | NR i awk? | Radnummer |
| 5 | awk -F: gör? | Sätter : som field separator |
| 6 | Sista fältet i awk? | $NF |
| 7 | BEGIN-block? | Körs före första raden |
| 8 | END-block? | Körs efter sista raden |
| 9 | awk '/mönster/' gör? | Matchar rader med mönster |
| 10 | awk '$3 > 10' gör? | Villkor: fält 3 större än 10 |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad skriver `awk '{print $2}'` ut?**
- A) Hela raden
- B) Första fältet
- C) Andra fältet ✅
- D) Radnummer 2

**2. Vad innehåller variabeln NF i awk?**
- A) Antal rader i filen
- B) Antal fält på aktuell rad ✅
- C) Filnamnet
- D) Nästa fält

**3. Hur sätter du : som field separator?**
- A) awk -s: '{print}'
- B) awk -F: '{print}' ✅
- C) awk --sep=: '{print}'
- D) awk '{FS=":"}'

**4. Vad gör `awk 'NR > 1 {print}'`?**
- A) Skriver ut rad 1
- B) Skriver ut alla utom första raden ✅
- C) Skriver ut radnummer
- D) Skriver ut om NR finns

**5. Hur skriver du ut sista fältet oavsett antal fält?**
- A) $LAST
- B) $-1
- C) $NF ✅
- D) ${NF}

**6. Vad gör BEGIN-blocket i awk?**
- A) Körs för varje rad
- B) Körs före första raden bearbetas ✅
- C) Körs efter sista raden
- D) Körs om raden börjar med BEGIN

**7. Vad matchar `awk '/^#/ {print}'`?**
- A) Rader som innehåller #
- B) Rader som börjar med # ✅
- C) Rader som slutar med #
- D) Alla rader med kommentarer

**8. Hur räknar du summan av fält 2?**
- A) awk '{total = $2}' fil
- B) awk '{sum += $2} END {print sum}' fil ✅
- C) awk 'SUM($2)' fil
- D) awk '{print sum($2)}' fil

**9. Vad gör `awk -F: '{print $1}' /etc/passwd`?**
- A) Skriver ut hela passwd
- B) Skriver ut användarnamn ✅
- C) Skriver ut lösenord
- D) Skriver ut UID

**10. Vad är skillnaden mellan print och printf?**
- A) Ingen skillnad
- B) printf tillåter formatering ✅
- C) print är snabbare
- D) printf fungerar bara med siffror

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande fältextraktion
Skapa `data.txt`:
```
Lisa 25 Stockholm
Erik 30 Göteborg
Anna 22 Malmö
```

Kör:
```bash
awk '{print $1}' data.txt           # Namn
awk '{print $1, $3}' data.txt       # Namn och stad
awk '{print NR, $0}' data.txt       # Radnummer + allt
awk '{print $NF}' data.txt          # Sista fältet (stad)
```

### Övning 2: /etc/passwd-analys
```bash
# Lista alla användarnamn
awk -F: '{print $1}' /etc/passwd

# Lista användare med UID >= 1000
awk -F: '$3 >= 1000 {print $1, "UID:", $3}' /etc/passwd

# Räkna totalt antal användare
awk -F: 'END {print "Antal användare:", NR}' /etc/passwd
```

### Övning 3: Beräkna statistik
Skapa `försäljning.txt`:
```
Januari 15000
Februari 18000
Mars 22000
April 19000
```

```bash
# Total försäljning
awk '{sum += $2} END {print "Total:", sum}' försäljning.txt

# Medelvärde
awk '{sum += $2} END {print "Medel:", sum/NR}' försäljning.txt

# Hitta månad med högst försäljning
awk 'BEGIN {max=0} $2 > max {max=$2; månad=$1} END {print månad, max}' försäljning.txt
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| `awk {print $1}` utan citattecken | Shell expanderar | `awk '{print $1}'` |
| Glömmer -F för andra separatorer | Fel fält | `awk -F: '{print $1}'` |
| $NF vs NF | $NF = värdet, NF = numret | Använd $NF för sista fältet |
| Förväxlar NR och NF | NR = rad, NF = fält | NR = Row, NF = Fields |
| Glömmer END för summor | Skriver ut per rad | `END {print sum}` |

---

## 📝 SAMMANFATTNING

```bash
# GRUNDLÄGGANDE
awk '{print $1}' fil          # Första fältet
awk '{print $1, $3}' fil      # Fält 1 och 3
awk '{print $0}' fil          # Hela raden
awk '{print $NF}' fil         # Sista fältet

# SEPARATOR
awk -F: '{print $1}' fil      # : som separator
awk -F, '{print $1}' fil      # , som separator

# VARIABLER
$0=hela raden  $1,$2=fält  NR=radnummer  NF=antal fält

# MÖNSTER
awk '/error/ {print}' fil     # Rader med "error"
awk '$3 > 100 {print}' fil    # Fält 3 > 100
awk 'NR > 1 {print}' fil      # Skippa första raden

# BEGIN/END
awk 'BEGIN {print "Start"} {print} END {print "Slut"}' fil
awk '{sum += $2} END {print sum}' fil    # Summa
```

""",
    "quiz": [
        {
            "question": "Vad skriver awk '{print $2}' ut?",
            "options": [
                "Hela raden",
                "Första fältet",
                "Andra fältet",
                "Radnummer 2"
            ],
            "correct": 2,
            "explanation": "$2 refererar till det andra fältet (kolumnen) på varje rad."
        },
        {
            "question": "Vad innehåller variabeln NF i awk?",
            "options": [
                "Antal rader i filen",
                "Antal fält på aktuell rad",
                "Filnamnet",
                "Nästa fält"
            ],
            "correct": 1,
            "explanation": "NF = Number of Fields. Innehåller antal fält på den aktuella raden."
        },
        {
            "question": "Hur sätter du : som field separator i awk?",
            "options": [
                "awk -s: '{print}'",
                "awk -F: '{print}'",
                "awk --sep=: '{print}'",
                "awk '{FS=\":\"}'"
            ],
            "correct": 1,
            "explanation": "-F (Field separator) följt av tecknet. -F: sätter kolon som separator."
        },
        {
            "question": "Vad gör awk 'NR > 1 {print}'?",
            "options": [
                "Skriver ut endast rad 1",
                "Skriver ut alla rader utom den första",
                "Skriver ut radnummer",
                "Skriver ut om variabeln NR existerar"
            ],
            "correct": 1,
            "explanation": "NR > 1 är ett villkor: bara rader där radnumret är större än 1 (alltså rad 2 och framåt)."
        },
        {
            "question": "Hur skriver du ut sista fältet oavsett antal fält?",
            "options": [
                "$LAST",
                "$-1",
                "$NF",
                "${NF}"
            ],
            "correct": 2,
            "explanation": "$NF refererar till fält nummer NF, alltså det sista fältet på raden."
        },
        {
            "question": "Vad gör BEGIN-blocket i awk?",
            "options": [
                "Körs för varje rad i filen",
                "Körs en gång före första raden bearbetas",
                "Körs efter sista raden",
                "Körs om raden börjar med ordet BEGIN"
            ],
            "correct": 1,
            "explanation": "BEGIN körs exakt en gång, innan awk börjar läsa filen. Perfekt för att sätta variabler."
        },
        {
            "question": "Vad matchar awk '/^#/ {print}'?",
            "options": [
                "Rader som innehåller # var som helst",
                "Rader som börjar med #",
                "Rader som slutar med #",
                "Alla rader utom de med #"
            ],
            "correct": 1,
            "explanation": "^# är regex för 'börjar med #'. Matchar kommentarsrader."
        },
        {
            "question": "Hur räknar du summan av fält 2 i en fil?",
            "options": [
                "awk '{total = $2}' fil",
                "awk '{sum += $2} END {print sum}' fil",
                "awk 'SUM($2)' fil",
                "awk '{print sum($2)}' fil"
            ],
            "correct": 1,
            "explanation": "+= adderar till variabeln. END-blocket skriver ut totalen efter alla rader."
        },
        {
            "question": "Vad gör awk -F: '{print $1}' /etc/passwd?",
            "options": [
                "Skriver ut hela passwd-filen",
                "Skriver ut användarnamn (första fältet)",
                "Skriver ut lösenord",
                "Skriver ut UID"
            ],
            "correct": 1,
            "explanation": "/etc/passwd har : som separator. $1 är första fältet = användarnamn."
        },
        {
            "question": "Vad är skillnaden mellan print och printf i awk?",
            "options": [
                "Ingen skillnad alls",
                "printf tillåter formaterad output med %s, %d etc",
                "print är snabbare",
                "printf fungerar bara med siffror"
            ],
            "correct": 1,
            "explanation": "printf ger kontroll över formatering: printf \"%-10s %5d\", $1, $2 för kolumner."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
AWK_FLASHCARDS = [
    {"front": "$1 i awk?", "back": "Första fältet på raden"},
    {"front": "$0 i awk?", "back": "Hela raden"},
    {"front": "$NF i awk?", "back": "Sista fältet på raden"},
    {"front": "NF i awk?", "back": "Antal fält på raden (Number of Fields)"},
    {"front": "NR i awk?", "back": "Radnummer (Number of Record)"},
    {"front": "awk -F: gör?", "back": "Sätter : som field separator"},
    {"front": "FS i awk?", "back": "Field Separator (input)"},
    {"front": "OFS i awk?", "back": "Output Field Separator"},
    {"front": "BEGIN-block?", "back": "Körs en gång FÖRE första raden"},
    {"front": "END-block?", "back": "Körs en gång EFTER sista raden"},
    {"front": "awk '/mönster/'?", "back": "Matchar rader som innehåller mönster"},
    {"front": "awk '$3 > 10'?", "back": "Villkor: bearbeta om fält 3 > 10"},
    {"front": "awk 'NR > 1'?", "back": "Skippa första raden (header)"},
    {"front": "Summa av fält 2?", "back": "awk '{s+=$2} END {print s}' fil"},
    {"front": "Räkna rader med mönster?", "back": "awk '/mönster/ {c++} END {print c}'"},
    {"front": "printf vs print?", "back": "printf tillåter formatering (%s, %d, %-10s)"},
    {"front": "awk '{print $1, $3}'?", "back": "Skriver ut fält 1 och 3 med mellanslag"},
    {"front": "Näst sista fältet?", "back": "$(NF-1)"},
    {"front": "Användarnamn från /etc/passwd?", "back": "awk -F: '{print $1}' /etc/passwd"},
    {"front": "UID från /etc/passwd?", "back": "awk -F: '{print $3}' /etc/passwd"},
]
