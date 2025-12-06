"""
Linux Mastery Node 3: File Operations - V2 Interactive Format
"""

LINUX_NODE_3_FILEOPS_V2 = {
    "node_id": 3,
    "title": "File Operations Mastery",
    "slug": "file-operations",
    "description": "Skapa, kopiera, flytta och ta bort filer och kataloger",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "File Operations",
            "content": {
                "headline": "Varje deployment involverar filoperationer",
                "hook": "Ett felaktigt rm -rf kan avsluta karriärer. En saknad -p i mkdir kan krascha deployment. Dessa kommandon är ditt dagliga bröd.",
                "learning_objectives": [
                    "Skapa filer och kataloger med touch och mkdir",
                    "Kopiera och flytta med cp och mv",
                    "Förstå hard links vs soft links",
                    "Säker borttagning med rm"
                ],
                "prerequisites": ["Filesystem navigation"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "File Operation Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Hard Links vs Soft Links",
                        "explanation": "Hard link = samma inode, fil överlever om original tas bort. Soft link (symlink) = pekare till path, går sönder om original försvinner.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ HARD LINK                                   │
│ file1.txt ──┐                               │
│             ├──→ [inode 12345] → data      │
│ file2.txt ──┘                               │
├─────────────────────────────────────────────┤
│ SOFT LINK (symlink)                         │
│ link.txt ──→ "path/to/original.txt"        │
│ (om original tas bort = broken link)        │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Soft links fungerar över filsystem, hard links gör inte det.",
                        "common_mistake": "Att ta bort original-filen och undra varför symlinken är bruten."
                    },
                    {
                        "title": "cp och mv flaggor",
                        "explanation": "-r (recursive), -p (preserve permissions), -i (interactive/bekräfta), -f (force), -v (verbose).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ FLAG │ BETYDELSE                            │
├─────────────────────────────────────────────┤
│ -r   │ Recursive (för kataloger)           │
│ -p   │ Preserve permissions/timestamps     │
│ -i   │ Fråga innan överskrivning           │
│ -f   │ Force (ingen bekräftelse)           │
│ -v   │ Verbose (visa vad som händer)       │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Använd alltid -i med rm tills du är 100% säker.",
                        "common_mistake": "rm -rf / utan att tänka. Många har förlorat hela system."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on File Operations",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa katalogstruktur",
                        "instruction": "Skapa project/src/components i ett kommando",
                        "expected_command": "mkdir -p project/src/components",
                        "hint": "-p skapar parent-kataloger automatiskt"
                    },
                    {
                        "task": "Kopiera med bevarade attribut",
                        "instruction": "Kopiera katalog 'src' till 'backup' med permissions",
                        "expected_command": "cp -rp src backup",
                        "hint": "-r för recursive, -p för preserve"
                    },
                    {
                        "task": "Skapa symlink",
                        "instruction": "Skapa symbolisk länk 'current' till 'v1.0'",
                        "expected_command": "ln -s v1.0 current",
                        "hint": "-s för symbolic/soft link"
                    },
                    {
                        "task": "Säker borttagning",
                        "instruction": "Ta bort katalogen 'old' med bekräftelse",
                        "expected_command": "rm -ri old",
                        "hint": "-i frågar innan varje fil"
                    }
                ],
                "estimated_time": "10 min",
                "xp_reward": 30
            }
        },
        {
            "section_id": "quiz",
            "type": "quiz",
            "title": "Testa dina kunskaper",
            "content": {
                "questions": {
                    "flashcards": [
                        {"front": "Vad gör mkdir -p?", "back": "Skapar parent-kataloger om de inte finns (parents)"},
                        {"front": "Skillnad mellan hard link och soft link?", "back": "Hard link = samma inode. Soft link = pekare till path (kan gå sönder)"},
                        {"front": "Vad gör cp -rp?", "back": "-r recursive (kataloger), -p preserve (permissions, timestamps)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilket kommando skapar en symbolisk länk?",
                            "options": ["ln file link", "ln -s target link", "link -s target", "symlink target link"],
                            "correct": 1,
                            "explanation": "ln -s skapar soft/symbolic link, ln utan -s skapar hard link"
                        },
                        {
                            "question": "Vad händer med en symlink om originalet tas bort?",
                            "options": ["Symlinken raderas också", "Symlinken blir broken/dangling", "Inget händer", "Symlinken behåller datan"],
                            "correct": 1,
                            "explanation": "Symlink pekar på path - om filen försvinner blir länken bruten"
                        }
                    ]
                },
                "passing_score": 0.8,
                "estimated_time": "5 min",
                "xp_reward": 25
            }
        },
        {
            "section_id": "challenge",
            "type": "challenge",
            "title": "File Operations Challenge",
            "content": {
                "scenario": "Sätt upp deployment-struktur med versioner och symlink.",
                "requirements": [
                    "Skapa struktur: /app/releases/v1.0, v2.0, v3.0",
                    "Kopiera sample app till v3.0",
                    "Skapa symlink /app/current → /app/releases/v3.0",
                    "Ta bort gamla releases (v1.0) säkert"
                ],
                "hints": [
                    "mkdir -p för hela strukturen",
                    "ln -sfn för att uppdatera symlink",
                    "rm -ri för säker borttagning"
                ],
                "solution": """# 1. Skapa struktur
mkdir -p /app/releases/{v1.0,v2.0,v3.0}

# 2. Kopiera app (anta sample finns)
cp -rp /sample-app/* /app/releases/v3.0/

# 3. Skapa/uppdatera symlink
ln -sfn /app/releases/v3.0 /app/current
# -s = symbolic, -f = force, -n = no-dereference

# 4. Verifiera symlink
ls -la /app/current

# 5. Ta bort gammal release
rm -ri /app/releases/v1.0""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
