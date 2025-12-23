"""
NOD 1.3: Regular Expressions (Regex)
=====================================
Denna nod ska infogas i doe25_tentaplugg.py under MODUL 1: BASH
"""

REGEX_NODE = {
    "title": "Regular Expressions (Regex)",
    "slug": "regular-expressions-regex",
    "description": "Mönstermatchning med regex - grep, metacharacters och POSIX-klasser.",
    "difficulty": "medium",
    "estimated_minutes": 50,
    "xp_reward": 120,
    "order_index": 2,
    "content": r"""# Regular Expressions (Regex)

> **TL;DR:** Regex är ett språk för att beskriva mönster i text. Med grep söker du efter mönster i filer. Lär dig metacharacters och du kan matcha nästan vad som helst!

---

## 📖 TEORI: Vad är Regex?

Regex (Regular Expressions) är ett **mönsterspråk** för att:
- Söka efter text
- Validera input (e-post, datum, telefonnummer)
- Hitta och ersätta text

**Exempel:** Istället för att söka efter "katt" kan du söka efter "alla ord som börjar med k och slutar med tt".

---

## 📖 Metacharacters - Byggstenarna

### Grundläggande metacharacters

| Tecken | Namn | Matchar | Exempel | Matchar |
|--------|------|---------|---------|---------|
| `.` | Punkt | ETT valfritt tecken | `h.t` | hat, hot, hit, h9t |
| `*` | Asterisk | 0 eller fler av föregående | `ab*c` | ac, abc, abbc, abbbc |
| `+` | Plus | 1 eller fler av föregående | `ab+c` | abc, abbc (EJ ac) |
| `?` | Frågetecken | 0 eller 1 av föregående | `colou?r` | color, colour |
| `^` | Cirkumflex | Början av rad | `^Hej` | Rad som BÖRJAR med "Hej" |
| `$` | Dollar | Slutet av rad | `slut$` | Rad som SLUTAR med "slut" |
| `\` | Backslash | Escape (bokstavlig) | `\.` | Matchar faktisk punkt |

### Visuellt exempel

```
Mönster: h.t
         │││
         ││└── bokstavlig 't'
         │└─── . = valfritt tecken
         └──── bokstavlig 'h'

Matchar: hat ✅  hot ✅  hit ✅  h9t ✅  ht ❌  hoot ❌
```

---

## 📖 Teckenklasser [ ]

Hakparenteser definierar en **uppsättning tillåtna tecken**.

| Syntax | Betydelse | Matchar |
|--------|-----------|---------|
| `[abc]` | a, b eller c | Ett av tecknen a, b, c |
| `[a-z]` | Alla gemener | a, b, c, ... z |
| `[A-Z]` | Alla versaler | A, B, C, ... Z |
| `[0-9]` | Alla siffror | 0, 1, 2, ... 9 |
| `[a-zA-Z]` | Alla bokstäver | a-z och A-Z |
| `[^abc]` | INTE a, b, c | Allt utom a, b, c |
| `[^0-9]` | INTE siffror | Allt utom siffror |

### Exempel

```bash
# Matcha tre siffror
grep "[0-9][0-9][0-9]" fil.txt

# Matcha ord som börjar med stor bokstav
grep "^[A-Z]" fil.txt

# Matcha rader utan siffror
grep "^[^0-9]*$" fil.txt
```

---

## 📖 POSIX-klasser

Fördefinierade teckenklasser (måste vara inuti [[ ]]).

| POSIX-klass | Motsvarar | Matchar |
|-------------|-----------|---------|
| `[[:alpha:]]` | `[a-zA-Z]` | Bokstäver |
| `[[:digit:]]` | `[0-9]` | Siffror |
| `[[:alnum:]]` | `[a-zA-Z0-9]` | Alfanumeriska |
| `[[:space:]]` | `[ \t\n]` | Whitespace |
| `[[:upper:]]` | `[A-Z]` | Versaler |
| `[[:lower:]]` | `[a-z]` | Gemener |
| `[[:punct:]]` | | Skiljetecken |

### Exempel

```bash
# Hitta rader som börjar med bokstav
grep "^[[:alpha:]]" fil.txt

# Hitta rader med bara siffror
grep "^[[:digit:]]*$" fil.txt
```

---

## 📖 Kvantifierare (antal)

| Syntax | Betydelse | BRE | ERE |
|--------|-----------|-----|-----|
| `*` | 0 eller fler | ✅ | ✅ |
| `+` | 1 eller fler | ❌ `\+` | ✅ |
| `?` | 0 eller 1 | ❌ `\?` | ✅ |
| `{n}` | Exakt n | `\{n\}` | `{n}` |
| `{n,}` | n eller fler | `\{n,\}` | `{n,}` |
| `{n,m}` | Mellan n och m | `\{n,m\}` | `{n,m}` |

### Exempel

```bash
# Exakt 3 siffror (ERE)
grep -E "[0-9]{3}" fil.txt

# Telefonnummer: 3 siffror, bindestreck, 7 siffror
grep -E "[0-9]{3}-[0-9]{7}" fil.txt

# 2-4 bokstäver
grep -E "[a-z]{2,4}" fil.txt
```

---

## 📖 BRE vs ERE - VIKTIGT!

| Feature | BRE (Basic) | ERE (Extended) |
|---------|-------------|----------------|
| Kommando | `grep` | `grep -E` eller `egrep` |
| `+` (1+) | `\+` | `+` |
| `?` (0-1) | `\?` | `?` |
| `{n,m}` | `\{n,m\}` | `{n,m}` |
| `( )` gruppering | `\( \)` | `( )` |
| `|` eller | `\|` | `|` |

**Rekommendation:** Använd alltid `grep -E` så slipper du escape-helvetet!

### Jämförelse

```bash
# BRE - måste escape:a
grep "ab\+c" fil.txt
grep "colou\?r" fil.txt
grep "\(hej\|tjena\)" fil.txt

# ERE - rent och snyggt
grep -E "ab+c" fil.txt
grep -E "colou?r" fil.txt
grep -E "(hej|tjena)" fil.txt
```

---

## 📖 grep - Sök i filer

### Grundläggande syntax

```bash
grep [flaggor] "mönster" fil
```

### Viktiga flaggor

| Flagga | Betydelse | Exempel |
|--------|-----------|---------|
| `-E` | Extended regex (ERE) | `grep -E "a{3}" fil` |
| `-i` | Case insensitive | `grep -i "hej" fil` |
| `-v` | Invertera (visa EJ matchande) | `grep -v "^#" fil` |
| `-c` | Räkna matchningar | `grep -c "error" log` |
| `-n` | Visa radnummer | `grep -n "TODO" kod.py` |
| `-r` | Rekursivt i mappar | `grep -r "func" src/` |
| `-l` | Visa bara filnamn | `grep -l "main" *.py` |
| `-o` | Visa bara matchande del | `grep -o "[0-9]+" fil` |
| `-w` | Hela ord | `grep -w "is" fil` |

### Praktiska exempel

```bash
# Hitta alla IP-adresser
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" log.txt

# Hitta rader som INTE är kommentarer
grep -v "^#" config.txt

# Räkna fel i loggfil
grep -c "ERROR" /var/log/syslog

# Hitta TODO i alla Python-filer
grep -rn "TODO" --include="*.py" .

# Case-insensitive sökning
grep -i "error\|warning" log.txt
```

---

## 📖 Regex i Bash med [[ =~ ]]

I Bash kan du använda regex direkt med `=~` operatorn:

```bash
#!/usr/bin/env bash

# Validera e-postadress
email="test@example.com"
if [[ $email =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "✅ Giltig e-post"
else
    echo "❌ Ogiltig e-post"
fi

# Validera datum (YYYY-MM-DD)
datum="2024-12-23"
if [[ $datum =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "✅ Giltigt datumformat"
else
    echo "❌ Ogiltigt datumformat"
fi

# Extrahera matchad grupp
text="Version: 2.5.1"
if [[ $text =~ ([0-9]+\.[0-9]+\.[0-9]+) ]]; then
    echo "Version är: ${BASH_REMATCH[1]}"    # 2.5.1
fi
```

---

## 💻 PRAKTISKA EXEMPEL

### Exempel 1: Validera svenskt personnummer

```bash
#!/usr/bin/env bash
pnr="$1"

# Format: ÅÅMMDD-XXXX
if [[ $pnr =~ ^[0-9]{6}-[0-9]{4}$ ]]; then
    echo "✅ Giltigt format"
else
    echo "❌ Ogiltigt format (ska vara ÅÅMMDD-XXXX)"
fi
```

### Exempel 2: Filtrera loggar

```bash
# Visa bara ERROR och WARNING
grep -E "(ERROR|WARNING)" /var/log/syslog

# Visa rader med tidsstämpel som börjar med 2024
grep -E "^2024-" log.txt

# Hitta IP-adresser och räkna unika
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log | sort -u
```

### Exempel 3: Datumformat YYYY-MM-DD

```
Mönster: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$

^           = Början av rad
[0-9]{4}    = Exakt 4 siffror (år)
-           = Bokstavligt bindestreck
[0-9]{2}    = Exakt 2 siffror (månad)
-           = Bokstavligt bindestreck
[0-9]{2}    = Exakt 2 siffror (dag)
$           = Slutet av rad

Matchar:  2024-12-23 ✅
          2024-1-5 ❌ (behöver 2024-01-05)
          24-12-23 ❌ (behöver fyra siffror för år)
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | . (punkt) i regex matchar? | Ett valfritt tecken |
| 2 | * i regex betyder? | Noll eller fler av föregående |
| 3 | + i regex betyder? | En eller fler av föregående |
| 4 | ^ i regex betyder? | Början av rad |
| 5 | $ i regex betyder? | Slutet av rad |
| 6 | [0-9] matchar? | En siffra 0-9 |
| 7 | [^abc] matchar? | Allt UTOM a, b, c |
| 8 | grep -E aktiverar? | Extended Regular Expressions (ERE) |
| 9 | grep -v gör? | Visar rader som INTE matchar |
| 10 | [[ $var =~ regex ]] testar? | Om variabeln matchar regex |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad matchar regex-mönstret `h.t`?**
- A) Bara "hat"
- B) "hat", "hot", "hit", "h9t" ✅
- C) "ht"
- D) "hoot"

**2. Vad betyder `*` i regex?**
- A) Ett eller fler av föregående
- B) Noll eller fler av föregående ✅
- C) Exakt ett tecken
- D) Valfritt tecken

**3. Vad matchar `^Hej`?**
- A) Rader som innehåller "Hej"
- B) Rader som BÖRJAR med "Hej" ✅
- C) Rader som slutar med "Hej"
- D) Bara ordet "Hej"

**4. Vad matchar `[^0-9]`?**
- A) Alla siffror
- B) Siffror från 0-9
- C) Allt UTOM siffror ✅
- D) Inget

**5. Vilken flagga gör grep case-insensitive?**
- A) -c
- B) -v
- C) -i ✅
- D) -n

**6. Vad gör `grep -v "^#" config.txt`?**
- A) Visar rader som börjar med #
- B) Visar rader som INTE börjar med # ✅
- C) Räknar rader med #
- D) Tar bort # från rader

**7. Vad är skillnaden mellan BRE och ERE?**
- A) Ingen skillnad
- B) ERE kräver escape för + ? { } ✅
- C) BRE kräver escape för + ? { } ✅
- D) BRE är snabbare

**8. Hur aktiverar du ERE i grep?**
- A) grep -B
- B) grep -E ✅
- C) grep -R
- D) grep --extended

**9. Vad matchar `[0-9]{3}`?**
- A) Siffran 3
- B) Tre valfria tecken
- C) Exakt tre siffror ✅
- D) Siffror 0-3

**10. Hur testar du regex i Bash?**
- A) if [[ $var == regex ]]
- B) if [[ $var =~ regex ]] ✅
- C) if [ $var ~ regex ]
- D) if regex $var

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Grep-basics
Skapa `test.txt`:
```
Hej världen
hej sverige
123-456-7890
error: något gick fel
ERROR: kritiskt fel
# detta är en kommentar
```

Testa:
```bash
grep "^[A-Z]" test.txt        # Rader som börjar med versal
grep -i "error" test.txt      # Alla "error" (case-insensitive)
grep -v "^#" test.txt         # Rader som INTE är kommentarer
grep -E "[0-9]{3}" test.txt   # Rader med 3+ siffror
```

### Övning 2: Validera input
Skriv ett skript som tar ett argument och kollar om det är ett giltigt telefonnummer (XXX-XXX-XXXX):

```bash
#!/usr/bin/env bash
if [[ $1 =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
    echo "✅ Giltigt telefonnummer"
else
    echo "❌ Ogiltigt format"
fi
```

### Övning 3: Extrahera IP-adresser
Skapa `log.txt` med:
```
Connection from 192.168.1.100
Failed login from 10.0.0.5
Access granted: 172.16.0.1
```

Kör:
```bash
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" log.txt
```

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Problem | Lösning |
|---------|---------|---------|
| Glömma -E med + | `grep "a+" fil` funkar inte | `grep -E "a+" fil` |
| Förväxla . och \. | `.` matchar allt, inte punkt | `\.` för bokstavlig punkt |
| Glömma ^ och $ | Matchar var som helst i raden | Använd `^...$` för hel rad |
| [A-z] istället för [A-Za-z] | Inkluderar extra tecken | Skriv ut båda explicit |
| Glömma citera mönster | Shell expanderar * etc | `grep "mönster"` med citattecken |

---

## 📝 SAMMANFATTNING

```bash
# METACHARACTERS
.     = ett tecken       ^    = radstart
*     = 0+ föregående    $    = radslut
+     = 1+ föregående    []   = teckenklass
?     = 0-1 föregående   [^]  = negerad klass

# GREP
grep -E "mönster" fil    # ERE (rekommenderas)
grep -i                  # Case insensitive
grep -v                  # Invertera
grep -c                  # Räkna
grep -n                  # Radnummer

# BASH REGEX
if [[ $var =~ ^[0-9]+$ ]]; then
    echo "Bara siffror!"
fi

# VANLIGA MÖNSTER
^[0-9]{4}-[0-9]{2}-[0-9]{2}$    # Datum YYYY-MM-DD
^[a-zA-Z0-9._%+-]+@.*\.[a-z]+$  # E-post (förenklad)
^[0-9]{1,3}(\.[0-9]{1,3}){3}$   # IP-adress
```

"""
}

