"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    DEVOPSHUB TASK CONTENT TEMPLATE v3.0                       ║
║                                                                               ║
║  Denna mall definierar standarden för ALLT pedagogiskt innehåll i DevOpsHub  ║
║  Används för: Bootcamp, SkillsMaps, Modules                                  ║
║                                                                               ║
║  Baserad på: Bootcamp v3.0 pedagogik (Akhilesh-stilen)                       ║
╚═══════════════════════════════════════════════════════════════════════════════╝

STRUKTUR FÖR VARJE TASK:
========================

1. TITEL (H1)
   - Kortfattad, beskrivande
   - Använd emoji för visuell identitet

2. VARFÖR DETTA ÄR VIKTIGT
   - Motivera INNAN du lär ut
   - Koppla till verkliga scenarion
   - Max 3-4 meningar

3. VAD DU KOMMER LÄRA DIG
   - Bullet points (3-5 st)
   - Konkreta, mätbara mål
   - Börja med verb (Förstå, Konfigurera, Implementera)

4. HUVUDINNEHÅLL
   - Sektioner med H2/H3
   - Kod med förklaringar FÖRE och EFTER
   - Diagram (ASCII) där det hjälper
   - Tabeller för jämförelser

5. OS-SPECIFIKA SEKTIONER (där relevant)
   - Använd: <!-- OS:macos --> ... <!-- /OS:macos -->
   - Använd: <!-- OS:windows --> ... <!-- /OS:windows -->
   - Använd: <!-- OS:linux --> ... <!-- /OS:linux -->

6. PRAKTISK ÖVNING
   - Hands-on steg
   - Förväntad output
   - Vanliga fel och lösningar

7. SAMMANFATTNING / NÄSTA STEG
   - Vad har vi lärt oss?
   - Hur kopplar detta till nästa task?

================================================================================
"""

# =============================================================================
# TASK TEMPLATE - KOPIERA DENNA FÖR NYA TASKS
# =============================================================================

TASK_TEMPLATE = {
    "title": "Task Titel Här",
    "slug": "task-slug-here",
    "description": "Kort beskrivning för listvy (max 100 tecken)",
    "difficulty": "beginner",  # beginner | intermediate | advanced | expert
    "xp_reward": 100,
    "estimated_minutes": 30,
    "content": """# 📖 Task Titel Här

## Varför detta är viktigt
Som DevOps-ingenjör kommer du [SPECIFIK SITUATION]. Att förstå [DETTA KONCEPT] är avgörande för [KONKRET NYTTA].

## Vad du kommer lära dig
- Förstå [KONCEPT 1] och varför det används
- Konfigurera [VERKTYG/SYSTEM] för [ANVÄNDNINGSFALL]
- Implementera [PRAKTISK FÄRDIGHET]
- Felsöka vanliga problem med [OMRÅDE]

---

## 📚 Grundläggande koncept

### Vad är [ÄMNE]?

[FÖRKLARING I 2-3 MENINGAR]

```
+-------------------------------------------------------------+
|                     KONCEPTUELLT DIAGRAM                     |
+-------------------------------------------------------------+
|                                                              |
|   [KOMPONENT A] ----▶ [KOMPONENT B] ----▶ [KOMPONENT C]    |
|                                                              |
+-------------------------------------------------------------+
```

### Nyckeltermer

| Term | Förklaring |
|------|------------|
| Term 1 | Vad det betyder |
| Term 2 | Vad det betyder |
| Term 3 | Vad det betyder |

---

## 🛠️ Praktisk implementation

### Steg 1: [BESKRIVNING]

Först behöver vi [FÖRKLARING]:

```bash
# Kommentar som förklarar vad kommandot gör
kommando --flagga värde
```

**Förväntad output:**
```
Output som användaren ska se
```

### Steg 2: [BESKRIVNING]

Nu ska vi [FÖRKLARING]:

```bash
# Kommentar
kommando
```

<!-- OS:macos -->
### macOS-specifikt

På macOS behöver du:

```bash
# macOS-specifikt kommando
brew install paket
```
<!-- /OS:macos -->

<!-- OS:windows -->
### Windows-specifikt (WSL2)

På Windows med WSL2:

```bash
# Windows/WSL2-specifikt
sudo apt install paket
```
<!-- /OS:windows -->

<!-- OS:linux -->
### Linux-specifikt

På Linux:

```bash
# Linux-specifikt kommando
sudo apt install paket
```
<!-- /OS:linux -->

---

## ✅ Praktisk övning

### Uppgift
[BESKRIV VAD ANVÄNDAREN SKA GÖRA]

### Steg-för-steg
1. [FÖRSTA STEGET]
2. [ANDRA STEGET]
3. [TREDJE STEGET]

### Verifiera
Kör detta kommando för att bekräfta att allt fungerar:

```bash
kommando --verify
```

Du bör se:
```
Framgångsrik output
```

### Vanliga problem

**Problem:** [VANLIGT FEL]
**Lösning:** [HUR MAN LÖSER DET]

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
- ✅ [VAD VI LÄRDE OSS 1]
- ✅ [VAD VI LÄRDE OSS 2]
- ✅ [VAD VI LÄRDE OSS 3]

### Nästa steg
I nästa task kommer du lära dig [KOPPLING TILL NÄSTA TASK].
"""
}


# =============================================================================
# MODUL TEMPLATE
# =============================================================================

MODULE_TEMPLATE = {
    "title": "Modul Namn",
    "slug": "modul-slug",
    "description": "Beskrivning av modulen och vad användaren kommer lära sig",
    "icon": "🔧",
    "category": "Kategori",
    "difficulty": "intermediate",
    "estimated_hours": 10,
    "order": 1,
    "prerequisites": [],  # Lista med modul-slugs
    "tasks": [
        # TASK_TEMPLATE-objekt här
    ],
    "labs": [
        # Praktiska labbar (optional)
    ]
}


# =============================================================================
# EXEMPEL: KOMPLETT TASK MED V3-PEDAGOGIK
# =============================================================================

EXAMPLE_TASK_GIT_BASICS = {
    "title": "Git Grundläggande Workflow",
    "slug": "git-basic-workflow",
    "description": "Lär dig det dagliga arbetsflödet med Git",
    "difficulty": "beginner",
    "xp_reward": 100,
    "estimated_minutes": 30,
    "content": """# 🔄 Git Grundläggande Workflow

## Varför detta är viktigt
Som DevOps-ingenjör kommer du använda Git hundratals gånger per dag. Det är grunden för all modern mjukvaruutveckling och CI/CD. Att behärska det dagliga arbetsflödet är lika viktigt som att kunna andas.

## Vad du kommer lära dig
- Förstå Git's tre tillstånd (Working, Staging, Repository)
- Utföra det dagliga arbetsflödet (add, commit, push, pull)
- Skriva bra commit-meddelanden
- Hantera och lösa konflikter

---

## 📚 Git's Tre Tillstånd

Varje fil i Git befinner sig i ett av tre tillstånd:

```
+---------------------------------------------------------------------+
|                        GIT'S TRE TILLSTÅND                          |
+---------------------------------------------------------------------+
|                                                                      |
|   WORKING         --▶    STAGING        --▶    REPOSITORY          |
|   DIRECTORY              AREA                  (.git)               |
|                                                                      |
|   +---------+           +---------+           +---------+          |
|   | Dina    |  git add  | Redo    | git commit| Sparad  |          |
|   | ändringar| -------▶ | att     | ---------▶| historik|          |
|   |         |           | sparas  |           |         |          |
|   +---------+           +---------+           +---------+          |
|                                                                      |
+---------------------------------------------------------------------+
```

| Tillstånd | Beskrivning | Kommando för att flytta |
|-----------|-------------|------------------------|
| Working Directory | Filer du jobbar med just nu | (automatiskt) |
| Staging Area | Filer redo att committas | `git add` |
| Repository | Sparad historik | `git commit` |

---

## 🛠️ Det Dagliga Arbetsflödet

### Steg 1: Kolla status (gör detta OFTA!)

Innan du gör något, kolla alltid var du står:

```bash
# Se vilka filer som ändrats
git status
```

**Förväntad output:**
```
On branch main
Changes not staged for commit:
  modified:   src/app.py

Untracked files:
  src/new_feature.py
```

### Steg 2: Lägg till filer (staging)

```bash
# Lägg till specifik fil
git add src/app.py

# Lägg till alla ändrade filer
git add .

# Interaktivt val av ändringar
git add -p
```

### Steg 3: Committa (spara i historiken)

```bash
# Skriv commit-meddelande
git commit -m "feat: add user authentication endpoint"
```

### 📝 Bra Commit-meddelanden

| Prefix | Användning | Exempel |
|--------|------------|---------|
| `feat:` | Ny funktionalitet | `feat: add login page` |
| `fix:` | Buggfix | `fix: resolve null pointer in user service` |
| `docs:` | Dokumentation | `docs: update API readme` |
| `refactor:` | Kodförbättring | `refactor: simplify auth logic` |
| `test:` | Tester | `test: add unit tests for cart` |

<!-- OS:macos -->
### macOS Tips

Använd VS Code's inbyggda Git-integration:

```bash
# Öppna VS Code med Git-vy
code . && code --goto .git
```

Eller använd GitKraken/Fork för visuell Git.
<!-- /OS:macos -->

<!-- OS:windows -->
### Windows Tips (WSL2)

I WSL2, se till att Git är konfigurerat korrekt:

```bash
# Konfigurera Git för WSL
git config --global core.autocrlf input
```
<!-- /OS:windows -->

---

## ✅ Praktisk Övning

### Uppgift
Skapa ett nytt repo, gör ändringar, och praktisera arbetsflödet.

### Steg-för-steg

1. **Skapa ett test-repo:**
```bash
mkdir git-practice && cd git-practice
git init
```

2. **Skapa en fil och committa:**
```bash
echo "# My Project" > README.md
git add README.md
git commit -m "docs: add initial readme"
```

3. **Gör en ändring och committa igen:**
```bash
echo "This is my first project" >> README.md
git add README.md
git commit -m "docs: add project description"
```

4. **Se din historik:**
```bash
git log --oneline
```

### Verifiera

Du bör se något som:
```
a1b2c3d docs: add project description
e4f5g6h docs: add initial readme
```

### Vanliga problem

**Problem:** `fatal: not a git repository`
**Lösning:** Du är inte i en Git-mapp. Kör `git init` eller `cd` till rätt mapp.

**Problem:** `nothing to commit, working tree clean`
**Lösning:** Du har inga ändringar att committa. Gör en ändring först!

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
- ✅ Git's tre tillstånd och hur filer flyttas mellan dem
- ✅ Det dagliga arbetsflödet: status -> add -> commit
- ✅ Hur man skriver bra commit-meddelanden med konventioner
- ✅ Vanliga problem och hur man löser dem

### Nästa steg
I nästa task lär du dig om **branching** - hur du jobbar med flera versioner samtidigt.
"""
}


# =============================================================================
# VALIDERING - Använd denna för att verifiera att content följer mallen
# =============================================================================

def validate_task_content(task: dict) -> list[str]:
    """
    Validerar att en task följer V3-mallen.
    Returnerar lista med varningar.
    """
    warnings = []
    content = task.get("content", "")

    # Kolla efter obligatoriska sektioner
    required_sections = [
        ("## Varför detta är viktigt", "Saknar 'Varför detta är viktigt' sektion"),
        ("## Vad du kommer lära dig", "Saknar 'Vad du kommer lära dig' sektion"),
        ("```", "Saknar kodexempel"),
    ]

    for pattern, warning in required_sections:
        if pattern not in content:
            warnings.append(warning)

    # Kolla längd
    if len(content) < 2000:
        warnings.append(f"Innehållet är kort ({len(content)} chars). Minimum rekommenderat: 2000")

    # Kolla att det finns bullet points i learning objectives
    if "## Vad du kommer lära dig" in content:
        idx = content.find("## Vad du kommer lära dig")
        section = content[idx:idx+500]
        if "- " not in section:
            warnings.append("Learning objectives saknar bullet points")

    return warnings


# =============================================================================
# ANVÄNDNING
# =============================================================================

if __name__ == "__main__":
    # Validera exemplet
    warnings = validate_task_content(EXAMPLE_TASK_GIT_BASICS)

    if warnings:
        print("⚠️  Varningar:")
        for w in warnings:
            print(f"   - {w}")
    else:
        print("✅ Task följer V3-mallen!")

    print(f"\nContent längd: {len(EXAMPLE_TASK_GIT_BASICS['content'])} tecken")
