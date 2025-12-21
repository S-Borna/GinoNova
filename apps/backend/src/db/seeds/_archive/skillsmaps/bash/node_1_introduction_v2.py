"""
Bash Node 1: Introduction & Script Execution (V2 Format)
========================================================
Master the foundation of shell scripting — from shebang to execution
"""

NODE_BASH_01_INTRODUCTION_V2 = {
    "id": "bash-01-introduction",
    "title": "Bash Introduction & Script Execution",
    "slug": "bash-introduction",
    "description": "Master the foundation of shell scripting — from shebang to execution",
    "difficulty": "beginner",
    "estimated_minutes": 25,
    "xp_reward": 100,
    "sections": [
        {
            "type": "intro",
            "content": {
                "headline": "Bash Introduction & Script Execution",
                "hook": "The shell is your gateway to Unix power. Master it, and you control the machine.",
                "learning_objectives": [
                    "Förstå vad Bash är och varför det är viktigt för DevOps",
                    "Skriva och köra ditt första Bash-script",
                    "Förstå skillnaden mellan olika exekveringsmetoder",
                    "Använda shebang korrekt för portabilitet"
                ],
                "prerequisites": ["Grundläggande terminalkunskap"],
                "estimated_time": "25 minuter",
                "xp_reward": 100
            }
        },
        {
            "type": "concepts",
            "content": {
                "concepts": [
                    {
                        "title": "Vad är Bash?",
                        "explanation": """**Bash** (Bourne Again SHell) är:
- En **command interpreter** som läser och exekverar kommandon
- Ett **programmeringsspråk** för automation
- **Standard-shell** på de flesta Linux-distributioner och macOS

Varje DevOps-ingenjör spenderar timmar i terminalen. Bash är ditt primära verktyg för automation.""",
                        "pro_tip": "Kolla din nuvarande shell med `echo $SHELL` och Bash-version med `bash --version`"
                    },
                    {
                        "title": "Shebang-raden",
                        "explanation": """**Shebang** (`#!`) talar om för systemet vilken interpreter som ska användas:

```bash
#!/bin/bash           # Kör med Bash
#!/usr/bin/env bash   # Mer portabelt - hittar bash i PATH (rekommenderas!)
#!/bin/sh             # POSIX shell - mer portabelt men färre features
```

**Varför `#!/usr/bin/env bash`?**
- Bash kan finnas på `/bin/bash`, `/usr/local/bin/bash` eller annorstädes
- `env` söker i PATH och hittar rätt
- Essentiellt för cross-platform scripts""",
                        "common_mistake": "Glöm inte shebang! Utan den vet systemet inte hur scriptet ska köras."
                    },
                    {
                        "title": "Exekveringsmetoder",
                        "explanation": """Det finns tre sätt att köra ett script:

```bash
# Metod 1: Direkt exekvering (kräver execute-permission)
chmod +x script.sh
./script.sh

# Metod 2: Explicit interpreter (ingen permission behövs)
bash script.sh

# Metod 3: Source (kör i nuvarande shell)
source script.sh
. script.sh  # Kortform
```

**Kritisk skillnad:**
- `./script.sh` — Kör i en **subshell** (isolerat)
- `source script.sh` — Kör i **current shell** (påverkar din miljö)""",
                        "pro_tip": "Använd `source` när du vill att variabler från scriptet ska finnas kvar efter exekvering"
                    }
                ]
            }
        },
        {
            "type": "practice",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa ditt första script",
                        "instruction": "Skapa ett script som heter hello.sh med korrekt shebang",
                        "expected_command": "echo '#!/usr/bin/env bash' > hello.sh && echo 'echo Hello DevOps!' >> hello.sh",
                        "hint": "Använd echo med >> för att lägga till rader"
                    },
                    {
                        "task": "Gör scriptet körbart",
                        "instruction": "Sätt execute-permission på scriptet",
                        "expected_command": "chmod +x hello.sh",
                        "hint": "chmod +x ger execute-permission"
                    },
                    {
                        "task": "Kör scriptet",
                        "instruction": "Exekvera scriptet med ./",
                        "expected_command": "./hello.sh",
                        "hint": "./ kör scriptet i current directory"
                    },
                    {
                        "task": "Debugga ett script",
                        "instruction": "Kör scriptet i debug-mode för att se varje kommando",
                        "expected_command": "bash -x hello.sh",
                        "hint": "-x flaggan visar varje kommando som exekveras"
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
                            "question": "Vilken shebang är mest portabel för Bash-scripts?",
                            "options": [
                                "#!/bin/bash",
                                "#!/usr/bin/env bash",
                                "#!/bin/sh",
                                "#!bash"
                            ],
                            "correct": 1,
                            "explanation": "#!/usr/bin/env bash söker efter bash i PATH vilket fungerar på olika system där bash kan vara installerat på olika platser."
                        },
                        {
                            "question": "Vad är skillnaden mellan ./script.sh och source script.sh?",
                            "options": [
                                "Ingen skillnad",
                                "./script.sh kör i subshell, source kör i current shell",
                                "source är snabbare",
                                "./script.sh kräver ingen permission"
                            ],
                            "correct": 1,
                            "explanation": "source (eller .) kör scriptet i din nuvarande shell vilket betyder att variabler och ändringar finns kvar efteråt."
                        },
                        {
                            "question": "Hur kontrollerar du syntax i ett script utan att köra det?",
                            "options": [
                                "bash --check script.sh",
                                "bash -n script.sh",
                                "bash --verify script.sh",
                                "check script.sh"
                            ],
                            "correct": 1,
                            "explanation": "bash -n (noexec) parsar scriptet och hittar syntaxfel utan att faktiskt köra det."
                        }
                    ]
                }
            }
        },
        {
            "type": "challenge",
            "content": {
                "scenario": "Du ska skapa ett professionellt script-skelett med bästa praxis",
                "requirements": [
                    "Använd portabel shebang",
                    "Lägg till script-header med beskrivning",
                    "Definiera en main-funktion",
                    "Använd strict mode (set -euo pipefail)"
                ],
                "hints": [
                    "set -e avslutar vid fel",
                    "set -u avslutar vid odefinierade variabler",
                    "set -o pipefail fångar fel i pipes"
                ],
                "solution": """#!/usr/bin/env bash
#
# Script: template.sh
# Description: Professional script template
# Author: DevOps Engineer
#

set -euo pipefail

main() {
    echo "Script starting..."
    # Din logik här
}

main "$@\""""
            }
        }
    ]
}
