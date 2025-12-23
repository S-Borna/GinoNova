"""
NOD 1.4: Sed (Stream Editor)
=============================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

SED_NODE = {
    "title": "Sed - Stream Editor",
    "slug": "sed-stream-editor",
    "description": "Textbearbetning med sed - sök och ersätt, radera rader och automatisera textredigering.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "order_index": 3,
    "content": r"""# Sed - Stream Editor

> **TL;DR:** Sed läser text rad för rad och gör ändringar. Perfekt för att söka/ersätta i filer från terminalen. `sed 's/gammalt/nytt/g'` är kommandot du kommer använda mest!

---

## 📖 TEORI: Vad är sed?

**sed** = **S**tream **Ed**itor

- Bearbetar text **rad för rad** (strömmar)
- Ändrar **INTE** originalfilen (om inte `-i` används)
- Perfekt för automatisering i skript
- Mycket snabbare än att öppna filen i nano/vim

### Varför använda sed?

| Situation | Utan sed | Med sed |
|-----------|----------|---------|
| Byt "http" till "https" i 500 filer | Öppna varje fil manuellt... | `sed -i 's/http:/https:/g' *.html` |
| Ta bort kommentarer | Redigera för hand | `sed '/^#/d' config.txt` |
| Uppdatera version i config | Öppna, sök, ändra, spara | `sed -i 's/v1.0/v2.0/g' config.txt` |

---

## 📖 Grundläggande syntax

```bash
sed 'kommando' fil
```

### Det vanligaste: s (substitute)

```
sed 's/sök/ersätt/' fil
     │ │   │
     │ │   └── Vad det ska bli
     │ └────── Vad du söker efter
     └──────── s = substitute (ersätt)
```

### Exempel steg för steg

**Fil: test.txt**
```
Hej världen
hej sverige
Hej igen
```

```bash
# Ersätt "Hej" med "Tjena" (endast FÖRSTA på varje rad)
sed 's/Hej/Tjena/' test.txt
```

**Output:**
```
Tjena världen
hej sverige
Tjena igen
```

⚠️ **OBS:** Originalfilen är OFÖRÄNDRAD! sed skriver till stdout.

---

## 📖 Flaggor efter ersättningen

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `g` | Global - alla förekomster på raden | `s/a/b/g` |
| `i` | Case insensitive | `s/hej/tjena/gi` |
| `p` | Print - skriv ut raden | `s/error/ERROR/p` |
| `2` | Endast andra förekomsten | `s/a/b/2` |

### Jämförelse: med och utan g

**Fil: test.txt**
```
aaa bbb aaa ccc aaa
```

```bash
# Utan g - bara första "aaa" ersätts
sed 's/aaa/XXX/' test.txt
# Output: XXX bbb aaa ccc aaa

# Med g - ALLA "aaa" ersätts
sed 's/aaa/XXX/g' test.txt
# Output: XXX bbb XXX ccc XXX
```

### Case insensitive

```bash
# Ersätt "hej", "Hej", "HEJ", etc.
sed 's/hej/tjena/gi' test.txt
```

---

## 📖 Viktiga kommandoflaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-i` | In-place - ändrar filen direkt! | `sed -i 's/a/b/g' fil` |
| `-i.bak` | In-place med backup | `sed -i.bak 's/a/b/g' fil` |
| `-n` | Suppress output (visa inget) | `sed -n 's/a/b/p' fil` |
| `-E` | Extended regex | `sed -E 's/[0-9]+/NUM/g' fil` |

### ⚠️ VARNING: -i ändrar filen!

```bash
# UTAN -i: visar output, filen orörd
sed 's/hej/tjena/g' test.txt

# MED -i: filen ÄNDRAS permanent!
sed -i 's/hej/tjena/g' test.txt

# SÄKERT: skapa backup först
sed -i.bak 's/hej/tjena/g' test.txt
# Skapar test.txt.bak innan ändring
```

---

## 📖 Adressering - Välj vilka rader

Du kan ange VILKA rader som ska påverkas:

| Adress | Betydelse | Exempel |
|--------|-----------|---------|
| `5` | Rad 5 | `sed '5s/a/b/'` |
| `1,10` | Rad 1-10 | `sed '1,10s/a/b/'` |
| `$` | Sista raden | `sed '$s/a/b/'` |
| `/mönster/` | Rader som matchar | `sed '/error/s/a/b/'` |
| `1,/mönster/` | Från rad 1 till mönster | `sed '1,/END/d'` |

### Exempel

**Fil: config.txt**
```
# Kommentar 1
server=localhost
port=8080
# Kommentar 2
debug=true
```

```bash
# Ändra bara på rad 3
sed '3s/8080/9090/' config.txt

# Ändra rader 2-4
sed '2,4s/=/: /' config.txt

# Ändra bara rader som innehåller "server"
sed '/server/s/localhost/192.168.1.1/' config.txt
```

---

## 📖 Delete (d) - Ta bort rader

```bash
# Ta bort rad 1
sed '1d' fil.txt

# Ta bort sista raden
sed '$d' fil.txt

# Ta bort rad 5-10
sed '5,10d' fil.txt

# Ta bort rader som matchar mönster
sed '/mönster/d' fil.txt
```

### Vanliga användningsfall

```bash
# Ta bort tomma rader
sed '/^$/d' fil.txt

# Ta bort kommentarsrader (börjar med #)
sed '/^#/d' config.txt

# Ta bort rader som innehåller "DEBUG"
sed '/DEBUG/d' logfil.txt

# Ta bort BÅDE tomma rader OCH kommentarer
sed '/^$/d; /^#/d' config.txt
```

---

## 📖 Print (p) med -n

Kombinera `-n` och `p` för att ENDAST visa matchande rader:

```bash
# Visa bara rader som innehåller "error"
sed -n '/error/p' logfil.txt

# Samma som grep! Men sed kan göra mer...
grep "error" logfil.txt
```

### Visa specifika rader

```bash
# Visa rad 5
sed -n '5p' fil.txt

# Visa rad 10-20
sed -n '10,20p' fil.txt

# Visa första och sista raden
sed -n '1p; $p' fil.txt
```

---

## 📖 Olika avgränsare

Du behöver inte använda `/` som avgränsare!

```bash
# Problem: ersätta sökvägar
sed 's/\/home\/user/\/var\/www/' fil   # Escape-helvete! 😵

# Lösning: använd annan avgränsare
sed 's|/home/user|/var/www|' fil       # Mycket lättare! 😊
sed 's#/home/user#/var/www#' fil       # Funkar också
sed 's@/home/user@/var/www@' fil       # Eller detta
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Uppdatera konfigurationsfil

**Före (config.ini):**
```ini
server=localhost
port=8080
debug=false
version=1.0
```

```bash
# Ändra port
sed -i 's/port=8080/port=9090/' config.ini

# Aktivera debug
sed -i 's/debug=false/debug=true/' config.ini

# Uppdatera version
sed -i 's/version=1.0/version=2.0/' config.ini
```

**Efter:**
```ini
server=localhost
port=9090
debug=true
version=2.0
```

### Exempel 2: Rensa loggfil

```bash
# Ta bort DEBUG-rader och tomma rader
sed '/DEBUG/d; /^$/d' app.log > cleaned.log

# Ta bort tidsstämplar (börjar med datum)
sed 's/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} //' app.log
```

### Exempel 3: Uppdatera gruppfil (från kursen)

```bash
# Lägg till användare i grupp
groupname="developers"
username="lisa"
sed -i "s/^$groupname:/$groupname:$username,/" /etc/group
```

### Exempel 4: Konvertera CSV-format

**Före:**
```
namn;ålder;stad
Anna;25;Stockholm
Erik;30;Göteborg
```

```bash
# Byt ; till ,
sed 's/;/,/g' data.csv
```

**Efter:**
```
namn,ålder,stad
Anna,25,Stockholm
Erik,30,Göteborg
```

---

## 📖 Flera kommandon

### Med semikolon

```bash
sed 's/a/A/g; s/b/B/g; s/c/C/g' fil.txt
```

### Med -e

```bash
sed -e 's/a/A/g' -e 's/b/B/g' -e 's/c/C/g' fil.txt
```

### Med sed-skriptfil

**kommandon.sed:**
```
s/a/A/g
s/b/B/g
s/c/C/g
```

```bash
sed -f kommandon.sed fil.txt
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | sed s-kommando syntax? | sed 's/sök/ersätt/' fil |
| 2 | g-flaggan i sed? | Global - ersätt ALLA på raden |
| 3 | sed -i gör? | In-place - ändrar filen direkt |
| 4 | sed -i.bak gör? | Ändrar filen, sparar backup |
| 5 | Ta bort rad 1? | sed '1d' fil |
| 6 | Ta bort tomma rader? | sed '/^$/d' fil |
| 7 | Ta bort kommentarer (#)? | sed '/^#/d' fil |
| 8 | Ersätt bara på rad 5? | sed '5s/sök/ersätt/' fil |
| 9 | Annan avgränsare än /? | sed 's|sök|ersätt|' eller s#sök#ersätt# |
| 10 | sed -n '/mönster/p'? | Visa bara rader som matchar |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad gör kommandot `sed 's/a/b/' fil.txt`?**
- A) Ersätter alla 'a' med 'b'
- B) Ersätter första 'a' på varje rad med 'b' ✅
- C) Tar bort alla 'a'
- D) Lägger till 'b' efter varje 'a'

**2. Vad betyder flaggan `g` i `sed 's/a/b/g'`?**
- A) Gör sökningen global i hela filen
- B) Ersätter alla förekomster på varje rad ✅
- C) Grupperar matchningar
- D) Gör sökningen case insensitive

**3. Vad gör `sed -i 's/test/prod/' config.txt`?**
- A) Visar ändringarna utan att spara
- B) Ändrar filen direkt ✅
- C) Skapar en ny fil
- D) Visar bara matchande rader

**4. Hur tar du bort alla tomma rader med sed?**
- A) sed '/^$/d' fil ✅
- B) sed 's/^$/d' fil
- C) sed 'd/^$/' fil
- D) sed 'empty/d' fil

**5. Vad gör `sed '1,5d' fil.txt`?**
- A) Tar bort rad 1 och rad 5
- B) Tar bort rad 1-5 ✅
- C) Visar rad 1-5
- D) Ersätter rad 1-5

**6. Hur ersätter du text endast på rad 10?**
- A) sed 's/a/b/10' fil
- B) sed '10/s/a/b/' fil
- C) sed '10s/a/b/' fil ✅
- D) sed 's/a/b/' -10 fil

**7. Vad gör `sed -n '/error/p' log.txt`?**
- A) Tar bort rader med "error"
- B) Visar bara rader med "error" ✅
- C) Ersätter "error"
- D) Räknar rader med "error"

**8. Varför använder man `sed 's|/home|/var|'` istället för `/`?**
- A) Det går snabbare
- B) Slipper escape:a / i sökvägar ✅
- C) Det är standard i Linux
- D) Det fungerar med regex

**9. Vad gör `sed '/^#/d' config.txt`?**
- A) Lägger till # i början av rader
- B) Tar bort rader som börjar med # ✅
- C) Ersätter # med tomt
- D) Visar rader som börjar med #

**10. Hur skapar du en backup när du använder -i?**
- A) sed -backup -i 's/a/b/' fil
- B) sed -i.bak 's/a/b/' fil ✅
- C) sed -i --backup 's/a/b/' fil
- D) sed -i 's/a/b/' fil > fil.bak

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grundläggande ersättning
Skapa `test.txt`:
```
Hello World
hello bash
Hello sed
```

Kör dessa och jämför:
```bash
sed 's/Hello/Goodbye/' test.txt      # Första på varje rad
sed 's/Hello/Goodbye/g' test.txt     # Alla
sed 's/hello/goodbye/gi' test.txt    # Case insensitive
```

### Övning 2: Rensa konfigurationsfil
Skapa `config.txt`:
```
# Database settings
host=localhost
port=5432

# Cache settings
cache=true

debug=false
```

Kör:
```bash
# Ta bort kommentarer och tomma rader
sed '/^#/d; /^$/d' config.txt
```

### Övning 3: Batch-uppdatering
Skapa flera filer:
```bash
echo "version: 1.0" > app1.conf
echo "version: 1.0" > app2.conf
echo "version: 1.0" > app3.conf

# Uppdatera alla till version 2.0
sed -i 's/version: 1.0/version: 2.0/' *.conf

# Verifiera
cat *.conf
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| Glömmer -i | Filen ändras inte | Använd `sed -i` eller redirect `>` |
| Glömmer g | Bara första ersätts | Lägg till `g`: `s/a/b/g` |
| / i sökvägar | Escape-kaos | Använd annan avgränsare: `s\|sök\|ersätt\|` |
| -i utan backup | Kan inte ångra | Använd `-i.bak` |
| Citattecken fel | Variabler expanderas inte | Använd dubbla citattecken för variabler |

---

## 📝 SAMMANFATTNING

```bash
# GRUNDLÄGGANDE
sed 's/sök/ersätt/' fil        # Första på varje rad
sed 's/sök/ersätt/g' fil       # Alla på varje rad
sed 's/sök/ersätt/gi' fil      # Alla, case insensitive

# ÄNDRA FIL
sed -i 's/sök/ersätt/g' fil    # Ändra filen direkt
sed -i.bak 's/sök/ersätt/g'    # Med backup

# RADERA
sed '1d' fil                   # Ta bort rad 1
sed '$d' fil                   # Ta bort sista raden
sed '/^$/d' fil                # Ta bort tomma rader
sed '/^#/d' fil                # Ta bort kommentarer

# ADRESSERING
sed '5s/a/b/' fil              # Bara rad 5
sed '1,10s/a/b/' fil           # Rad 1-10
sed '/mönster/s/a/b/' fil      # Rader med mönster

# VISA
sed -n '5p' fil                # Visa rad 5
sed -n '/error/p' fil          # Visa rader med "error"
```

""",
    "quiz": [
        {
            "question": "Vad gör kommandot sed 's/a/b/' fil.txt?",
            "options": [
                "Ersätter alla 'a' med 'b' i filen",
                "Ersätter första 'a' på varje rad med 'b'",
                "Tar bort alla 'a' från filen",
                "Lägger till 'b' efter varje 'a'"
            ],
            "correct": 1,
            "explanation": "Utan g-flaggan ersätter sed bara FÖRSTA förekomsten på varje rad."
        },
        {
            "question": "Vad betyder flaggan g i sed 's/a/b/g'?",
            "options": [
                "Gör sökningen global i hela filen",
                "Ersätter alla förekomster på varje rad",
                "Grupperar matchningar",
                "Gör sökningen case insensitive"
            ],
            "correct": 1,
            "explanation": "g = global, ersätter ALLA förekomster på varje rad, inte bara den första."
        },
        {
            "question": "Vad gör sed -i 's/test/prod/' config.txt?",
            "options": [
                "Visar ändringarna utan att spara",
                "Ändrar filen direkt (in-place)",
                "Skapar en ny fil config_new.txt",
                "Visar bara matchande rader"
            ],
            "correct": 1,
            "explanation": "-i betyder in-place editing. Filen ändras permanent direkt."
        },
        {
            "question": "Hur tar du bort alla tomma rader med sed?",
            "options": [
                "sed '/^$/d' fil",
                "sed 's/^$/d' fil",
                "sed 'd/^$/' fil",
                "sed 'empty/d' fil"
            ],
            "correct": 0,
            "explanation": "^$ matchar tomma rader (start följt direkt av slut). d = delete."
        },
        {
            "question": "Vad gör sed '1,5d' fil.txt?",
            "options": [
                "Tar bort rad 1 och rad 5",
                "Tar bort rad 1 till och med rad 5",
                "Visar rad 1-5",
                "Ersätter rad 1-5 med tomt"
            ],
            "correct": 1,
            "explanation": "1,5 är ett radintervall. d = delete. Alltså: ta bort rad 1-5."
        },
        {
            "question": "Hur ersätter du text endast på rad 10?",
            "options": [
                "sed 's/a/b/10' fil",
                "sed '10/s/a/b/' fil",
                "sed '10s/a/b/' fil",
                "sed 's/a/b/' -10 fil"
            ],
            "correct": 2,
            "explanation": "Radnummer skrivs direkt före kommandot: 10s/a/b/ = ersätt på rad 10."
        },
        {
            "question": "Vad gör sed -n '/error/p' log.txt?",
            "options": [
                "Tar bort rader som innehåller 'error'",
                "Visar bara rader som innehåller 'error'",
                "Ersätter 'error' med tomt",
                "Räknar antal rader med 'error'"
            ],
            "correct": 1,
            "explanation": "-n tystar normal output. p = print. Tillsammans: visa BARA matchande rader."
        },
        {
            "question": "Varför använder man sed 's|/home|/var|' istället för /?",
            "options": [
                "Det går snabbare att köra",
                "Man slipper escape:a / i sökvägar",
                "Det är Linux-standard",
                "Det aktiverar extended regex"
            ],
            "correct": 1,
            "explanation": "När sökmönstret innehåller / är det enklare att använda annan avgränsare som | eller #."
        },
        {
            "question": "Vad gör sed '/^#/d' config.txt?",
            "options": [
                "Lägger till # i början av alla rader",
                "Tar bort rader som börjar med #",
                "Ersätter # med tomt",
                "Visar bara rader som börjar med #"
            ],
            "correct": 1,
            "explanation": "^# matchar rader som börjar med #. d = delete. Tar bort kommentarsrader."
        },
        {
            "question": "Hur skapar du en backup när du använder sed -i?",
            "options": [
                "sed -backup -i 's/a/b/' fil",
                "sed -i.bak 's/a/b/' fil",
                "sed -i --backup 's/a/b/' fil",
                "sed -i 's/a/b/' fil > fil.bak"
            ],
            "correct": 1,
            "explanation": "-i.bak skapar en backup med ändelsen .bak innan filen ändras."
        }
    ]
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
SED_FLASHCARDS = [
    {"front": "sed s-kommando syntax?", "back": "sed 's/sök/ersätt/' fil"},
    {"front": "sed g-flaggan?", "back": "Global - ersätt ALLA på raden"},
    {"front": "sed i-flaggan (efter s)?", "back": "Case insensitive"},
    {"front": "sed -i gör?", "back": "In-place - ändrar filen direkt"},
    {"front": "sed -i.bak gör?", "back": "Ändrar filen, sparar backup först"},
    {"front": "Ta bort rad 1?", "back": "sed '1d' fil"},
    {"front": "Ta bort sista raden?", "back": "sed '$d' fil"},
    {"front": "Ta bort tomma rader?", "back": "sed '/^$/d' fil"},
    {"front": "Ta bort kommentarer (#)?", "back": "sed '/^#/d' fil"},
    {"front": "Ersätt bara på rad 5?", "back": "sed '5s/sök/ersätt/' fil"},
    {"front": "Ersätt rad 1-10?", "back": "sed '1,10s/sök/ersätt/' fil"},
    {"front": "Annan avgränsare än /?", "back": "sed 's|sök|ersätt|' eller s#sök#ersätt#"},
    {"front": "sed -n gör?", "back": "Suppress output - visa inget automatiskt"},
    {"front": "sed -n '/mönster/p'?", "back": "Visa bara rader som matchar mönster"},
    {"front": "sed -E gör?", "back": "Extended regex (som grep -E)"},
    {"front": "Flera sed-kommandon?", "back": "sed 's/a/b/; s/c/d/' eller sed -e 's/a/b/' -e 's/c/d/'"},
    {"front": "Ersätt på rader med mönster?", "back": "sed '/mönster/s/sök/ersätt/' fil"},
    {"front": "Visa rad 5?", "back": "sed -n '5p' fil"},
    {"front": "Visa rad 10-20?", "back": "sed -n '10,20p' fil"},
    {"front": "sed ändrar originalfil?", "back": "NEJ, om inte -i används!"},
]
