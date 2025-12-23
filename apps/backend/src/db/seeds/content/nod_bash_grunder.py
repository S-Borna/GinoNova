"""
NOD 1.1: Bash-grunder & Shebang
================================
Denna nod ska infogas i doe25_tentaplugg.py
"""

BASH_GRUNDER_NODE = {
    "title": "Bash-grunder & Shebang",
    "slug": "bash-grunder-shebang",
    "description": "Förstå vad Bash är, hur skript fungerar, och varför shebang är livsviktigt.",
    "difficulty": "easy",
    "estimated_minutes": 30,
    "xp_reward": 80,
    "order_index": 0,  # Först av alla!
    "content": r"""# Bash-grunder & Shebang

> **TL;DR:** Bash är tolken som förstår dina kommandon. Shebang (#!/bin/bash) berättar för systemet vilken tolk som ska användas. Utan shebang vet datorn inte hur den ska köra ditt skript.

---

## 📖 TEORI: Vad är vad?

### Terminal vs Shell vs Bash

| Begrepp | Vad det är | Analogi |
|---------|-----------|---------|
| **Terminal** | Fönstret du skriver i | TV-apparaten |
| **Shell** | Programmet som tolkar kommandon | TV-kanalen |
| **Bash** | En specifik typ av shell | SVT1 |

```
┌─────────────────────────────────────────┐
│  TERMINAL (fönstret)                    │
│  ┌───────────────────────────────────┐  │
│  │  SHELL (tolken)                   │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │  BASH (en typ av shell)     │  │  │
│  │  │  Förstår dina kommandon     │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

**Viktigt:** Det finns andra shells också: zsh, fish, sh, dash. Men i kursen använder vi **Bash**.

---

## 📖 Vad är ett skript?

Ett skript är en **textfil med kommandon** som körs uppifrån och ner.

Istället för att skriva:
```bash
echo "Hej"
date
pwd
```

...tre gånger om dagen, sparar du det i en fil och kör filen.

**Fördelar med skript:**
- Automatisering (slipper skriva samma sak)
- Reproducerbarhet (samma resultat varje gång)
- Dokumentation (koden visar vad som händer)

---

## 📖 Shebang: Den magiska första raden

### Vad är shebang?

```bash
#!/bin/bash
```

Den här raden MÅSTE vara **först** i skriptet. Den berättar för operativsystemet:
*"Använd programmet /bin/bash för att köra detta skript"*

### Varför behövs shebang?

**Utan shebang:**
```
$ ./mittskript.sh
bash: ./mittskript.sh: cannot execute binary file
```

Systemet vet inte HUR det ska köra filen!

**Med shebang:**
```
$ ./mittskript.sh
Hej världen!
```

Systemet läser första raden, ser `#!/bin/bash`, och vet att Bash ska tolka filen.

### Två sätt att skriva shebang

| Shebang | Förklaring | När använda |
|---------|-----------|-------------|
| `#!/bin/bash` | Hårdkodad sökväg | När du VET att bash finns på /bin/bash |
| `#!/usr/bin/env bash` | Hitta bash automatiskt | **REKOMMENDERAS** - funkar på fler system |

**Använd alltid:** `#!/usr/bin/env bash` (mer portabelt)

---

## 💻 PRAKTISKT: Skapa ditt första skript

### Steg 1: Skapa filen

```bash
nano hej.sh
```

### Steg 2: Skriv innehållet

```bash
#!/usr/bin/env bash
# Mitt första skript - kommentar börjar med #

echo "Hej, jag heter $(whoami)!"
echo "Dagens datum är: $(date)"
echo "Jag befinner mig i: $(pwd)"
```

### Steg 3: Spara och avsluta
- I nano: `Ctrl+O` (spara), `Enter`, `Ctrl+X` (avsluta)

### Steg 4: Gör skriptet körbart

```bash
chmod +x hej.sh
```

**Vad gör chmod +x?**
- `chmod` = change mode (ändra rättigheter)
- `+x` = lägg till execute-rättighet
- Utan detta kan du INTE köra skriptet med `./`

### Steg 5: Kör skriptet

```bash
./hej.sh
```

**Output:**
```
Hej, jag heter student!
Dagens datum är: mån 23 dec 2024 10:30:00 CET
Jag befinner mig i: /home/student
```

---

## 📖 Exit Codes: Lyckades kommandot?

Varje kommando returnerar en **exit code** (avslutningskod):

| Exit code | Betydelse |
|-----------|-----------|
| **0** | Allt gick bra! ✅ |
| **1-255** | Något gick fel ❌ |

### Kolla exit code med $?

```bash
ls /home
echo $?    # Skriver ut: 0 (lyckades)

ls /finns-inte
echo $?    # Skriver ut: 2 (filen finns inte)
```

**$?** innehåller ALLTID exit code från **senaste** kommandot.

### Vanliga exit codes

| Kod | Betydelse |
|-----|-----------|
| 0 | Allt OK |
| 1 | Generellt fel |
| 2 | Felaktig användning (t.ex. fil saknas) |
| 126 | Kan inte köra (permission denied) |
| 127 | Kommandot finns inte |
| 130 | Avbrutet med Ctrl+C |

---

## 📖 Set-flaggor: Gör dina skript robusta

Lägg dessa längst upp i dina skript (efter shebang):

```bash
#!/usr/bin/env bash
set -e    # Avbryt vid fel
set -u    # Fel vid odefinierade variabler
set -x    # Debug-läge (visa varje kommando)
```

### set -e (Exit on Error)

**Utan set -e:**
```bash
#!/usr/bin/env bash
cp fil-som-inte-finns.txt /tmp/    # Misslyckas
echo "Skriptet fortsätter ändå!"    # Körs!
```

**Med set -e:**
```bash
#!/usr/bin/env bash
set -e
cp fil-som-inte-finns.txt /tmp/    # Misslyckas
echo "Detta körs ALDRIG"            # Skriptet avbröts!
```

### set -u (Undefined Variables)

**Utan set -u:**
```bash
#!/usr/bin/env bash
echo "Hej $NAMN"    # Skriver ut "Hej " (tomt, inget fel)
```

**Med set -u:**
```bash
#!/usr/bin/env bash
set -u
echo "Hej $NAMN"    # FEL: NAMN: unbound variable
```

### set -x (Debug)

```bash
#!/usr/bin/env bash
set -x
namn="Lisa"
echo "Hej $namn"
```

**Output:**
```
+ namn=Lisa
+ echo 'Hej Lisa'
Hej Lisa
```

Varje rad visas med `+` innan den körs. **Perfekt för felsökning!**

### Kombinera alla tre

```bash
#!/usr/bin/env bash
set -euo pipefail    # e + u + o pipefail (bonus!)
```

`pipefail` = fånga fel i pipes också (annars bara sista kommandot)

---

## 💻 KOMPLETT EXEMPEL: Robust skript

```bash
#!/usr/bin/env bash
set -euo pipefail

# Mitt robusta skript
# Skapad av: Student
# Datum: 2024-12-23

echo "=== System Information ==="
echo "Användare: $(whoami)"
echo "Hostname: $(hostname)"
echo "Datum: $(date '+%Y-%m-%d %H:%M')"
echo "Katalog: $(pwd)"
echo ""
echo "=== Diskutrymme ==="
df -h / | tail -1
echo ""
echo "Skriptet kördes utan fel!"
```

---

## 🧠 FLASHCARDS (10 st)

| # | Framsida | Baksida |
|---|----------|---------|
| 1 | Vad är shebang? | Första raden i skript: #!/bin/bash |
| 2 | Två shebang-varianter? | #!/bin/bash och #!/usr/bin/env bash |
| 3 | Vilken shebang är mest portabel? | #!/usr/bin/env bash |
| 4 | Kommando för att göra skript körbart? | chmod +x skript.sh |
| 5 | Hur kör man ett skript i aktuell katalog? | ./skript.sh |
| 6 | Vad betyder exit code 0? | Kommandot lyckades |
| 7 | Variabel för senaste exit code? | $? |
| 8 | Vad gör set -e? | Avbryter skript vid fel |
| 9 | Vad gör set -u? | Fel vid odefinierad variabel |
| 10 | Vad gör set -x? | Debug-läge, visar varje kommando |

---

## ❓ QUIZ-FRÅGOR (10 st)

**1. Vad är syftet med shebang (#!/bin/bash)?**
- A) Kommentar som förklarar skriptet
- B) Talar om för systemet vilken tolk som ska användas ✅
- C) Gör skriptet körbart
- D) Definierar en variabel

**2. Vilken shebang rekommenderas för portabilitet?**
- A) #!/bin/bash
- B) #!/usr/bin/env bash ✅
- C) #!/bash
- D) #!bash

**3. Vad gör kommandot `chmod +x skript.sh`?**
- A) Skapar filen skript.sh
- B) Tar bort execute-rättigheter
- C) Lägger till execute-rättigheter ✅
- D) Kör skriptet

**4. Vad betyder exit code 0?**
- A) Ett fel uppstod
- B) Kommandot avbröts
- C) Kommandot lyckades ✅
- D) Filen hittades inte

**5. Vilken variabel innehåller senaste exit code?**
- A) $!
- B) $0
- C) $? ✅
- D) $#

**6. Vad gör `set -e` i ett skript?**
- A) Aktiverar echo
- B) Avbryter vid fel ✅
- C) Exporterar variabler
- D) Sätter environment

**7. Vad händer med `set -u` om du använder en odefinierad variabel?**
- A) Den blir tom
- B) Skriptet fortsätter
- C) Skriptet avbryts med fel ✅
- D) Variabeln sätts till 0

**8. Vad visar `set -x`?**
- A) Exit codes
- B) Varje kommando innan det körs ✅
- C) XML-output
- D) Extra information om filer

**9. Hur kör du ett skript som heter test.sh i aktuell katalog?**
- A) test.sh
- B) run test.sh
- C) ./test.sh ✅
- D) bash/test.sh

**10. Vad är skillnaden mellan terminal och shell?**
- A) Ingen skillnad
- B) Terminal = fönstret, Shell = tolken ✅
- C) Shell = fönstret, Terminal = tolken
- D) Båda är samma som Bash

---

## 🛠️ HANDS-ON ÖVNINGAR

### Övning 1: Skapa och kör ditt första skript
1. Skapa filen `forsta.sh` med nano
2. Lägg till shebang: `#!/usr/bin/env bash`
3. Lägg till: `echo "Mitt första skript fungerar!"`
4. Spara och gör körbart med `chmod +x`
5. Kör med `./forsta.sh`

### Övning 2: Testa exit codes
1. Kör: `ls /home`
2. Kör: `echo $?` (borde visa 0)
3. Kör: `ls /katalog-som-inte-finns`
4. Kör: `echo $?` (borde visa 2)

### Övning 3: Testa set-flaggor
Skapa `test-set.sh`:
```bash
#!/usr/bin/env bash
set -u
echo "Namn: $ODEFINIERAD_VARIABEL"
echo "Denna rad körs aldrig"
```
Kör och se att skriptet avbryts vid den odefinierade variabeln.

---

## ⚠️ VANLIGA MISSTAG

| Misstag | Varför det är fel | Rätt sätt |
|---------|-------------------|-----------|
| Glömmer shebang | Systemet vet inte vilken tolk | Alltid `#!/usr/bin/env bash` först |
| Glömmer chmod +x | Kan inte köra skriptet | `chmod +x skript.sh` |
| Skriver `skript.sh` utan `./` | Bash letar i PATH, inte aktuell katalog | `./skript.sh` |
| Mellanslag runt = i variabler | `namn = "test"` är FEL | `namn="test"` (inga mellanslag!) |
| Ignorerar exit codes | Skript fortsätter trots fel | Använd `set -e` |

---

## 📝 SAMMANFATTNING

```bash
#!/usr/bin/env bash    # 1. Shebang FÖRST
set -euo pipefail      # 2. Gör skriptet robust

# 3. Din kod här
echo "Hej!"

# 4. Spara, chmod +x, kör med ./
```

**Kom ihåg:**
- Shebang = första raden, ALLTID
- chmod +x = gör körbart
- ./ = kör från aktuell katalog
- $? = senaste exit code
- set -e = avbryt vid fel
- set -u = fel vid odefinierad variabel
- set -x = debug-läge

""",
    "quiz": [
        {
            "question": "Vad är syftet med shebang (#!/bin/bash)?",
            "options": [
                "Kommentar som förklarar skriptet",
                "Talar om för systemet vilken tolk som ska användas",
                "Gör skriptet körbart",
                "Definierar en variabel",
            ],
            "correct": 1,
            "explanation": "Shebang berättar för operativsystemet vilket program (tolk) som ska användas för att köra skriptet.",
        },
        {
            "question": "Vilken shebang rekommenderas för bästa portabilitet?",
            "options": ["#!/bin/bash", "#!/usr/bin/env bash", "#!/bash", "#!bash"],
            "correct": 1,
            "explanation": "#!/usr/bin/env bash söker efter bash i PATH och fungerar på fler system där bash kan ligga på olika platser.",
        },
        {
            "question": "Vad gör kommandot chmod +x skript.sh?",
            "options": [
                "Skapar filen skript.sh",
                "Tar bort filen skript.sh",
                "Lägger till execute-rättighet",
                "Kör skriptet",
            ],
            "correct": 2,
            "explanation": "chmod +x lägger till execute-rättighet så att filen kan köras som ett program.",
        },
        {
            "question": "Vad betyder exit code 0?",
            "options": [
                "Ett fel uppstod",
                "Kommandot avbröts av användaren",
                "Kommandot lyckades",
                "Filen hittades inte",
            ],
            "correct": 2,
            "explanation": "Exit code 0 betyder alltid att kommandot kördes utan fel. Alla andra värden (1-255) indikerar fel.",
        },
        {
            "question": "Vilken variabel innehåller senaste kommandots exit code?",
            "options": ["$!", "$0", "$?", "$#"],
            "correct": 2,
            "explanation": "$? innehåller exit code från det senast körda kommandot. 0 = OK, annat = fel.",
        },
        {
            "question": "Vad gör set -e i ett bash-skript?",
            "options": [
                "Aktiverar echo för alla kommandon",
                "Avbryter skriptet om ett kommando misslyckas",
                "Exporterar alla variabler",
                "Sätter encoding till UTF-8",
            ],
            "correct": 1,
            "explanation": "set -e (exit on error) gör att skriptet omedelbart avbryts om något kommando returnerar en exit code som inte är 0.",
        },
        {
            "question": "Vad händer om du använder en odefinierad variabel med set -u?",
            "options": [
                "Variabeln blir tom sträng",
                "Skriptet fortsätter som vanligt",
                "Skriptet avbryts med felmeddelande",
                "Variabeln sätts till 0",
            ],
            "correct": 2,
            "explanation": "set -u gör att skriptet avbryts med fel om du försöker använda en variabel som inte är definierad.",
        },
        {
            "question": "Vad visar set -x när skriptet körs?",
            "options": [
                "Exit codes för varje kommando",
                "Varje kommando med + prefix innan det körs",
                "XML-formaterad output",
                "Extra filinformation",
            ],
            "correct": 1,
            "explanation": "set -x visar varje kommando med + framför innan det körs. Perfekt för debugging!",
        },
        {
            "question": "Hur kör du ett skript som heter app.sh i aktuell katalog?",
            "options": ["app.sh", "run app.sh", "./app.sh", "exec app.sh"],
            "correct": 2,
            "explanation": "./ betyder 'i aktuell katalog'. Utan ./ söker bash i PATH-variabeln istället.",
        },
        {
            "question": "Vad är skillnaden mellan terminal och shell?",
            "options": [
                "Ingen skillnad, samma sak",
                "Terminal är fönstret, shell är programmet som tolkar kommandon",
                "Shell är fönstret, terminal är tolken",
                "Terminal är för Windows, shell är för Linux",
            ],
            "correct": 1,
            "explanation": "Terminal är fönstret/gränssnittet du ser. Shell (t.ex. Bash) är programmet inuti som faktiskt tolkar och kör dina kommandon.",
        },
    ],
}

# =============================================================================
# FLASHCARDS för study_data
# =============================================================================
BASH_GRUNDER_FLASHCARDS = [
    {
        "front": "Vad är shebang?",
        "back": "Första raden i skript: #!/bin/bash eller #!/usr/bin/env bash",
    },
    {"front": "Shebang - hårdkodad version?", "back": "#!/bin/bash"},
    {"front": "Shebang - portabel version?", "back": "#!/usr/bin/env bash"},
    {"front": "Gör skript körbart?", "back": "chmod +x skript.sh"},
    {"front": "Kör skript i aktuell katalog?", "back": "./skript.sh"},
    {"front": "Exit code 0 betyder?", "back": "Kommandot lyckades"},
    {"front": "Exit code 1-255 betyder?", "back": "Något gick fel"},
    {"front": "Variabel för senaste exit code?", "back": "$?"},
    {"front": "set -e gör vad?", "back": "Avbryter skript vid fel"},
    {"front": "set -u gör vad?", "back": "Fel vid odefinierad variabel"},
    {"front": "set -x gör vad?", "back": "Debug-läge, visar varje kommando"},
    {"front": "Terminal vs Shell?", "back": "Terminal = fönstret, Shell = tolken"},
    {"front": "Vad är Bash?", "back": "En typ av shell (Bourne Again Shell)"},
    {
        "front": "Varför behövs shebang?",
        "back": "Systemet vet vilken tolk som ska köra skriptet",
    },
    {
        "front": "Skript utan chmod +x?",
        "back": "Permission denied - kan ej köras med ./",
    },
    {"front": "Kommentar i bash?", "back": "# Detta är en kommentar"},
    {
        "front": "Robust skript-start?",
        "back": "#!/usr/bin/env bash\\nset -euo pipefail",
    },
    {"front": "Exit code 127?", "back": "Kommandot finns inte"},
    {"front": "Exit code 126?", "back": "Permission denied"},
    {"front": "Exit code 130?", "back": "Avbrutet med Ctrl+C"},
]
