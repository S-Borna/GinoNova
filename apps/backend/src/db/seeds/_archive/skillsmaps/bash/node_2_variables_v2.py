"""
Bash Node 2: Variables & Data Types (V2 Format)
================================================
Master variable declaration, scope, and data handling in Bash
"""

NODE_BASH_02_VARIABLES_V2 = {
    "id": "bash-02-variables",
    "title": "Variables & Data Types",
    "slug": "bash-variables",
    "description": "Master variable declaration, scope, and data handling in Bash",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,
    "sections": [
        {
            "type": "intro",
            "content": {
                "headline": "Variables & Data Types i Bash",
                "hook": "Variabler är hjärtat i varje script. Lär dig hantera data som ett proffs.",
                "learning_objectives": [
                    "Deklarera och använda variabler korrekt",
                    "Förstå skillnaden mellan lokala och globala variabler",
                    "Arbeta med arrays och associativa arrays",
                    "Använda readonly och export korrekt"
                ],
                "prerequisites": ["Bash Introduction"],
                "estimated_time": "30 minuter",
                "xp_reward": 100
            }
        },
        {
            "type": "concepts",
            "content": {
                "concepts": [
                    {
                        "title": "Variabeldeklaration",
                        "explanation": """I Bash deklareras variabler **utan spaces runt =**:

```bash
# Korrekt
name="DevOps"
count=42

# FEL! (Bash tolkar name som kommando)
name = "DevOps"
```

**Använd variabler med $:**
```bash
echo $name
echo ${name}  # Rekommenderas - tydligare
echo "${name}_suffix"  # Nödvändigt vid konkatenering
```""",
                        "common_mistake": "Spaces runt = är det vanligaste felet. Bash tolkar det som ett kommando med argument!"
                    },
                    {
                        "title": "Quoting - Single vs Double",
                        "explanation": """**Single quotes** (literal):
```bash
name="World"
echo 'Hello $name'  # Output: Hello $name
```

**Double quotes** (expansion):
```bash
name="World"
echo "Hello $name"  # Output: Hello World
```

**No quotes** (word splitting):
```bash
files="file1 file2"
ls $files   # Kör: ls file1 file2
ls "$files" # Kör: ls "file1 file2" (EN fil med space)
```""",
                        "pro_tip": "Använd alltid double quotes runt variabler för att undvika word splitting: \"$variable\""
                    },
                    {
                        "title": "Arrays",
                        "explanation": """**Indexed arrays:**
```bash
# Skapa array
fruits=("apple" "banana" "cherry")

# Access element (0-indexerat)
echo ${fruits[0]}    # apple
echo ${fruits[@]}    # Alla element
echo ${#fruits[@]}   # Antal element (3)

# Lägg till element
fruits+=("date")
```

**Associativa arrays (dictionaries):**
```bash
declare -A colors
colors[sky]="blue"
colors[grass]="green"

echo ${colors[sky]}  # blue
echo ${!colors[@]}   # Alla keys
```""",
                        "pro_tip": "Använd declare -a för indexed och declare -A för associativa arrays för tydlighet"
                    },
                    {
                        "title": "Scope: local, export, readonly",
                        "explanation": """```bash
# Global variabel (standard)
global_var="I'm global"

# Lokal variabel (endast i funktionen)
my_func() {
    local local_var="I'm local"
    echo $local_var
}

# Export (tillgänglig för child processes)
export PATH_VAR="/usr/local/bin"

# Readonly (konstant)
readonly PI=3.14159
PI=3  # Error! Cannot modify
```""",
                        "common_mistake": "Glöm inte 'local' i funktioner - annars läcker variabler ut och skapar bugs"
                    }
                ]
            }
        },
        {
            "type": "practice",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa och använd variabler",
                        "instruction": "Skapa en variabel 'project' med värdet 'DevOps' och skriv ut den",
                        "expected_command": "project=\"DevOps\" && echo $project",
                        "hint": "Ingen space runt ="
                    },
                    {
                        "task": "Skapa en array",
                        "instruction": "Skapa en array 'tools' med Docker, Kubernetes och Terraform",
                        "expected_command": "tools=(\"Docker\" \"Kubernetes\" \"Terraform\")",
                        "hint": "Använd parenteser för arrays"
                    },
                    {
                        "task": "Skriv ut array-längd",
                        "instruction": "Visa antalet element i tools-arrayen",
                        "expected_command": "echo ${#tools[@]}",
                        "hint": "# ger längden på array"
                    },
                    {
                        "task": "Exportera en variabel",
                        "instruction": "Exportera en variabel ENV med värdet 'production'",
                        "expected_command": "export ENV=\"production\"",
                        "hint": "export gör variabeln tillgänglig för child processes"
                    }
                ]
            }
        },
        {
            "type": "quiz",
            "content": {
                "questions": {
                    "multiple_choice": [
                        {
                            "question": "Vad är fel med: name = 'DevOps'?",
                            "options": [
                                "Inget fel",
                                "Spaces runt = är inte tillåtna",
                                "Single quotes fungerar inte",
                                "name är reserverat"
                            ],
                            "correct": 1,
                            "explanation": "I Bash får det inte finnas spaces runt =. Bash tolkar annars 'name' som ett kommando."
                        },
                        {
                            "question": "Vad är output av: name='World'; echo 'Hello $name'?",
                            "options": [
                                "Hello World",
                                "Hello $name",
                                "Error",
                                "Hello"
                            ],
                            "correct": 1,
                            "explanation": "Single quotes är literala - ingen variabel-expansion sker."
                        },
                        {
                            "question": "Hur får du längden på en array arr?",
                            "options": [
                                "len(arr)",
                                "${arr.length}",
                                "${#arr[@]}",
                                "arr.size"
                            ],
                            "correct": 2,
                            "explanation": "${#arr[@]} ger antalet element. # betyder längd och @ refererar till alla element."
                        }
                    ]
                }
            }
        },
        {
            "type": "challenge",
            "content": {
                "scenario": "Skapa ett script som hanterar server-konfiguration med variabler",
                "requirements": [
                    "Definiera readonly-konstanter för APP_NAME och VERSION",
                    "Skapa en array med servrar",
                    "Använd associativ array för server-portar",
                    "Loopa genom och skriv ut all info"
                ],
                "hints": [
                    "readonly för konstanter",
                    "declare -A för associativa arrays",
                    "for server in \"${servers[@]}\" för loop"
                ],
                "solution": """#!/usr/bin/env bash
readonly APP_NAME="MyApp"
readonly VERSION="1.0.0"

servers=("web1" "web2" "db1")

declare -A ports
ports[web1]=8080
ports[web2]=8081
ports[db1]=5432

echo "$APP_NAME v$VERSION"
for server in "${servers[@]}"; do
    echo "$server: port ${ports[$server]}"
done"""
            }
        }
    ]
}
