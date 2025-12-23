"""
NOD 1.2: Variabler, Quoting & Expansions
=========================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

VARIABLER_QUOTING_NODE = {
    "title": "Variabler, Quoting & Expansions",
    "slug": "variabler-quoting-expansions",
    "description": "Lär dig hantera variabler, förstå quoting-regler och använda expansions som ett proffs.",
    "difficulty": "medium",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "order_index": 1,
    "content": r"""# Variabler, Quoting & Expansions

> **TL;DR:** Variabler lagrar värden. Quoting styr vad som expanderas. Lär dig skillnaden mellan "dubbla" och 'enkla' citattecken - det KOMMER på tentan!

---

## 📖 TEORI: Variabler

### Skapa och använda variabler

```bash
# SKAPA variabel (INGEN mellanslag runt =)
namn="Lisa"           # ✅ Rätt
namn = "Lisa"         # ❌ FEL! Bash tror namn är ett kommando

# ANVÄNDA variabel
echo $namn            # Lisa
echo ${namn}          # Lisa (samma sak, men säkrare)
```

### När behövs ${klamrar}?

| Situation | $namn | ${namn} | Kommentar |
|-----------|-------|---------|-----------|
| Ensam variabel | ✅ `echo $namn` | ✅ `echo ${namn}` | Båda funkar |
| Text direkt efter | ❌ `echo $namnsson` | ✅ `echo ${namn}sson` | Klamrar krävs! |
| I dubbla citattecken | ✅ `echo "$namn"` | ✅ `echo "${namn}"` | Båda funkar |
| I strängar | ❌ `file_$datum.txt` | ✅ `file_${datum}.txt` | Klamrar säkrare |

**Regel:** När i tvivel, använd `${variabel}` - det funkar alltid!

---

## 📖 Miljövariabler vs Lokala variabler

```bash
# LOKAL variabel (finns bara i detta skript)
mitt_namn="Lisa"

# MILJÖVARIABEL (tillgänglig för subprocesser)
export MIN_VAR="tillgänglig överallt"
```

**Skillnaden:**
```bash
#!/usr/bin/env bash
lokal="jag är lokal"
export global="jag är global"

# Kör ett sub-shell
bash -c 'echo "Lokal: $lokal"'    # Tom! Subprocessen ser inte lokal
bash -c 'echo "Global: $global"'  # "jag är global"
```

---

## 📖 Speciella variabler (MEMORERA DESSA!)

### Tabell över speciella variabler

| Variabel | Betydelse | Exempel |
|----------|-----------|---------|
| `$0` | Skriptets namn | `./backup.sh` → `./backup.sh` |
| `$1, $2, $3...` | Positionsargument 1, 2, 3... | `./skript.sh a b` → $1=a, $2=b |
| `$#` | Antal argument | `./skript.sh a b c` → 3 |
| `$@` | Alla argument (separata ord) | Används i loopar |
| `$*` | Alla argument (ett ord) | Sällan användbart |
| `$?` | Exit code från senaste kommando | 0=OK, annat=fel |
| `$$` | Skriptets process-ID (PID) | 12345 |

### Miljövariabler du MÅSTE känna till

| Variabel | Innehåll | Exempel |
|----------|----------|---------|
| `$USER` | Inloggad användare | student |
| `$HOME` | Hemkatalog | /home/student |
| `$PWD` | Aktuell katalog | /home/student/projekt |
| `$PATH` | Sökvägar för kommandon | /usr/bin:/bin:/usr/local/bin |
| `$SHELL` | Aktuell shell | /bin/bash |

### Praktiskt exempel: Visa alla

```bash
#!/usr/bin/env bash
# spara som: visainfo.sh

echo "=== SKRIPT-INFO ==="
echo "Skriptets namn: $0"
echo "Antal argument: $#"
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Alla argument: $@"
echo "Skriptets PID: $$"

echo ""
echo "=== MILJÖVARIABLER ==="
echo "Användare: $USER"
echo "Hemkatalog: $HOME"
echo "Aktuell katalog: $PWD"
```

**Kör:**
```bash
./visainfo.sh hej "på dig"
```

**Output:**
```
=== SKRIPT-INFO ===
Skriptets namn: ./visainfo.sh
Antal argument: 2
Argument 1: hej
Argument 2: på dig
Alla argument: hej på dig
Skriptets PID: 12345

=== MILJÖVARIABLER ===
Användare: student
Hemkatalog: /home/student
Aktuell katalog: /home/student
```

---

## 📖 QUOTING - LIVSVIKTIGT!

### De tre typerna

| Typ | Syntax | Variabler expanderas? | Användning |
|-----|--------|----------------------|------------|
| Dubbla citattecken | `"..."` | ✅ JA | Vanligast - skyddar mellanslag |
| Enkla citattecken | `'...'` | ❌ NEJ | Bokstavlig text |
| Inga citattecken | `...` | ✅ JA | ⚠️ FARLIGT med mellanslag |

### Jämförelse med exempel

```bash
namn="Lisa Svensson"

# DUBBLA citattecken - variabler expanderas
echo "Hej $namn"       # Output: Hej Lisa Svensson

# ENKLA citattecken - INGENTING expanderas
echo 'Hej $namn'       # Output: Hej $namn (bokstavligt!)

# INGA citattecken - FARLIGT!
echo Hej $namn         # Funkar... men om namn="fil med mellanslag.txt"?
```

### Varför dubbla citattecken är viktiga

```bash
filnamn="min fil.txt"

# UTAN citattecken - KATASTROF!
rm $filnamn            # Bash ser: rm min fil.txt (TVÅ filer!)

# MED dubbla citattecken - SÄKERT
rm "$filnamn"          # Bash ser: rm "min fil.txt" (EN fil)
```

**REGEL:** Använd ALLTID `"$variabel"` med dubbla citattecken!

### Escape-tecken inom citattecken

```bash
# I dubbla citattecken - backslash fungerar
echo "Priset är \$100"    # Priset är $100

# I enkla citattecken - backslash är bokstavlig
echo 'Priset är \$100'    # Priset är \$100
```

---

## 📖 Command Substitution

Kör ett kommando och fånga resultatet i en variabel.

### Två sätt (använd alltid det första!)

| Syntax | Stil | Rekommenderas? |
|--------|------|----------------|
| `$(kommando)` | Modern | ✅ JA |
| `` `kommando` `` | Gammal (backticks) | ❌ NEJ |

### Praktiska exempel

```bash
# Fånga dagens datum
datum=$(date +%Y-%m-%d)
echo "Idag är det $datum"    # Idag är det 2024-12-23

# Fånga antal filer
antal=$(ls | wc -l)
echo "Det finns $antal filer"

# Fånga användarnamn
vem=$(whoami)
echo "Du är inloggad som $vem"

# BACKUP-SKRIPT (klassiskt tentaexempel!)
backup_namn="backup_$(date +%Y-%m-%d).tar.gz"
echo "$backup_namn"          # backup_2024-12-23.tar.gz
```

### Nästlade kommandon (därför $() är bättre)

```bash
# Med $() - läsbart och nästlingsbart
resultat=$(echo "Filer: $(ls | wc -l)")

# Med backticks - OMÖJLIGT att nästa
resultat=`echo "Filer: \`ls | wc -l\`"`   # Kräver escape - kaos!
```

---

## 📖 Expansions

### Brace Expansion { }

Genererar sekvenser och listor.

```bash
# Lista
echo {a,b,c}           # a b c
echo fil{1,2,3}.txt    # fil1.txt fil2.txt fil3.txt

# Sekvens
echo {1..5}            # 1 2 3 4 5
echo {a..e}            # a b c d e
echo {01..10}          # 01 02 03 04 05 06 07 08 09 10

# Praktiskt: skapa mappar
mkdir -p projekt/{src,bin,docs,tests}

# Praktiskt: backup-filer
cp config.txt{,.backup}    # Kopierar config.txt till config.txt.backup
```

### Tilde Expansion ~

```bash
echo ~              # /home/student (din hemkatalog)
echo ~/dokument     # /home/student/dokument
echo ~root          # /root (roots hemkatalog)
```

### Parameter Expansion ${...}

| Syntax | Betydelse | Exempel |
|--------|-----------|---------|
| `${var:-default}` | Om var tom, använd default | `${namn:-Gäst}` |
| `${var:=default}` | Om var tom, sätt OCH använd default | `${namn:=Gäst}` |
| `${var:?error}` | Om var tom, avbryt med fel | `${fil:?Fil krävs!}` |
| `${#var}` | Längden på variabelns värde | `${#namn}` → 4 |
| `${var^^}` | VERSALER | `${namn^^}` → LISA |
| `${var,,}` | gemener | `${NAMN,,}` → lisa |

**Praktiska exempel:**

```bash
# Default-värde
namn=""
echo "Hej ${namn:-Gäst}"     # Hej Gäst (namn är tom)

namn="Lisa"
echo "Hej ${namn:-Gäst}"     # Hej Lisa (namn har värde)

# Längd
ord="Bash"
echo "Ordet har ${#ord} tecken"    # Ordet har 4 tecken

# Versaler/gemener
text="HejSan"
echo "${text^^}"    # HEJSAN
echo "${text,,}"    # hejsan
```

---

## 💻 KOMPLETT EXEMPEL: Backup-skript

```bash
#!/usr/bin/env bash
set -euo pipefail

# Konfigurerbart backup-skript
BACKUP_DIR="${1:-/tmp/backups}"          # Argument 1 eller default
SOURCE_DIR="${2:-$HOME/dokument}"        # Argument 2 eller default
DATE=$(date +%Y-%m-%d_%H%M)
BACKUP_NAME="backup_${DATE}.tar.gz"

echo "=== BACKUP STARTAR ==="
echo "Källa: $SOURCE_DIR"
echo "Mål: $BACKUP_DIR"
echo "Filnamn: $BACKUP_NAME"

# Skapa backup-katalog om den inte finns
mkdir -p "$BACKUP_DIR"

# Skapa backup
tar -czf "${BACKUP_DIR}/${BACKUP_NAME}" "$SOURCE_DIR" 2>/dev/null

echo "✅ Backup klar: ${BACKUP_DIR}/${BACKUP_NAME}"
echo "Storlek: $(du -h "${BACKUP_DIR}/${BACKUP_NAME}" | cut -f1)"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Skapa variabel? | namn="värde" (inga mellanslag runt =) |
| 2 | $0 innehåller? | Skriptets namn |
| 3 | $# innehåller? | Antal argument |
| 4 | $@ innehåller? | Alla argument (separata) |
| 5 | $? innehåller? | Exit code från senaste kommando |
| 6 | "dubbla" vs 'enkla' citattecken? | Dubbla: expanderar. Enkla: bokstavligt |
| 7 | Fånga kommandoresultat? | datum=$(date) |
| 8 | ${var:-default} gör? | Använder default om var är tom |
| 9 | Göra variabel global? | export NAMN="värde" |
| 10 | {1..5} genererar? | 1 2 3 4 5 |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vilket är korrekt sätt att skapa en variabel?**
- A) namn = "Lisa"
- B) namn="Lisa" ✅
- C) $namn="Lisa"
- D) set namn="Lisa"

**2. Vad innehåller variabeln $# i ett skript?**
- A) Skriptets namn
- B) Senaste exit code
- C) Antal argument ✅
- D) Process-ID

**3. Vad skriver `echo 'Hej $USER'` ut?**
- A) Hej student
- B) Hej $USER ✅
- C) Hej
- D) Felmeddelande

**4. Vad skriver `echo "Hej $USER"` ut? (om USER=student)**
- A) Hej student ✅
- B) Hej $USER
- C) Hej
- D) Felmeddelande

**5. Hur fångar du resultatet av kommandot `date` i en variabel?**
- A) datum=date
- B) datum=$(date) ✅
- C) datum=$date
- D) $datum=date

**6. Vad gör kommandot `export MIN_VAR="test"`?**
- A) Skapar en lokal variabel
- B) Tar bort variabeln
- C) Gör variabeln tillgänglig för subprocesser ✅
- D) Skriver ut variabeln

**7. Vad genererar `echo {a,b,c}.txt`?**
- A) abc.txt
- B) {a,b,c}.txt
- C) a.txt b.txt c.txt ✅
- D) Felmeddelande

**8. Vad returnerar `${namn:-Gäst}` om $namn är tom?**
- A) Tom sträng
- B) Gäst ✅
- C) namn
- D) Felmeddelande

**9. Vilken variabel innehåller exit code från senaste kommando?**
- A) $!
- B) $#
- C) $? ✅
- D) $$

**10. Varför ska du alltid använda "$variabel" med citattecken?**
- A) Det ser snyggare ut
- B) Skyddar mot problem med mellanslag i värdet ✅
- C) Det går snabbare
- D) Variabeln blir permanent

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Speciella variabler
Skapa `argument.sh`:
```bash
#!/usr/bin/env bash
echo "Skript: $0"
echo "Arg 1: $1"
echo "Arg 2: $2"
echo "Antal: $#"
echo "Alla: $@"
```
Kör: `./argument.sh hej på dig`

### Övning 2: Quoting-skillnader
Kör dessa och jämför:
```bash
namn="Lisa"
echo "Hej $namn"
echo 'Hej $namn'
echo Hej $namn
```

### Övning 3: Backup med datum
Skapa ett skript som:
1. Skapar en variabel med dagens datum: `$(date +%Y-%m-%d)`
2. Skapar ett filnamn: `backup_${datum}.tar.gz`
3. Skriver ut filnamnet

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Varför fel | Rätt sätt |
|---------|-----------|-----------|
| `namn = "test"` | Mellanslag runt = | `namn="test"` |
| `echo $filnamn` utan citattecken | Problem med mellanslag | `echo "$filnamn"` |
| Använda backticks | Gammal syntax, svår att nästa | `$(kommando)` |
| Förväxla $@ och $* | $* slår ihop argument | Använd `"$@"` i loopar |
| Glömma export | Subprocesser ser inte variabeln | `export VAR="värde"` |

---

## 📝 SAMMANFATTNING

```bash
# VARIABLER
namn="värde"              # Skapa (INGA mellanslag!)
echo "$namn"              # Använd (med citattecken!)
export GLOBAL="värde"     # Gör tillgänglig för subprocesser

# SPECIELLA
$0=skriptnamn  $1,$2=argument  $#=antal  $@=alla  $?=exitcode

# QUOTING
"dubbla"  → expanderar variabler
'enkla'   → bokstavlig text
$(cmd)    → kommandosubstitution

# EXPANSIONS
{a,b,c}        → a b c
{1..5}         → 1 2 3 4 5
${var:-def}    → default om tom
```

"""
}

