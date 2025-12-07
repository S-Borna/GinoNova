"""
Bash Node 3: Conditionals & Control Flow (V2 Format)
====================================================
Master if/else, case statements, and test operators
"""

NODE_BASH_03_CONDITIONALS_V2 = {
    "id": "bash-03-conditionals",
    "title": "Conditionals & Control Flow",
    "slug": "bash-conditionals",
    "description": "Master if/else, case statements, and test operators",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 120,
    "sections": [
        {
            "type": "intro",
            "content": {
                "headline": "Conditionals & Control Flow",
                "hook": "Villkor styr logiken i dina scripts. Utan dem är scripts bara listor av kommandon.",
                "learning_objectives": [
                    "Använda if/elif/else korrekt",
                    "Förstå test-operatorer för filer och strängar",
                    "Använda case för mönstermatchning",
                    "Kombinera villkor med && och ||"
                ],
                "prerequisites": ["Bash Variables"],
                "estimated_time": "35 minuter",
                "xp_reward": 120
            }
        },
        {
            "type": "concepts",
            "content": {
                "concepts": [
                    {
                        "title": "If/Elif/Else",
                        "explanation": """```bash
if [[ condition ]]; then
    echo "Condition true"
elif [[ other_condition ]]; then
    echo "Other condition true"
else
    echo "All conditions false"
fi
```

**Viktigt:** Alltid spaces innanför `[[ ]]`!

**[[ ]] vs [ ]:**
- `[[ ]]` - Bash-specifik, fler features, säkrare
- `[ ]` - POSIX-kompatibel, begränsad""",
                        "common_mistake": "Glöm inte 'then' efter villkoret och 'fi' för att avsluta!"
                    },
                    {
                        "title": "String-operatorer",
                        "explanation": """```bash
[[ -z "$str" ]]     # True om tom (zero length)
[[ -n "$str" ]]     # True om inte tom (non-zero)
[[ "$a" == "$b" ]]  # String equality
[[ "$a" != "$b" ]]  # String inequality
[[ "$a" < "$b" ]]   # Lexikografisk jämförelse
[[ "$str" =~ regex ]]  # Regex match
```

**Exempel:**
```bash
name="DevOps"
if [[ -n "$name" ]]; then
    echo "Name is set: $name"
fi
```""",
                        "pro_tip": "Använd alltid quotes runt variabler i villkor för att undvika fel med tomma strängar"
                    },
                    {
                        "title": "Numeriska operatorer",
                        "explanation": """```bash
[[ $a -eq $b ]]  # Equal
[[ $a -ne $b ]]  # Not equal
[[ $a -lt $b ]]  # Less than
[[ $a -le $b ]]  # Less or equal
[[ $a -gt $b ]]  # Greater than
[[ $a -ge $b ]]  # Greater or equal
```

**Alternativ med (( )):**
```bash
(( a == b ))
(( a < b ))
(( a >= 10 ))
```""",
                        "pro_tip": "(( )) är tydligare för aritmetik och tillåter vanlig matematisk syntax"
                    },
                    {
                        "title": "Fil-operatorer",
                        "explanation": """```bash
[[ -e "$file" ]]  # Exists
[[ -f "$file" ]]  # Regular file
[[ -d "$dir" ]]   # Directory
[[ -r "$file" ]]  # Readable
[[ -w "$file" ]]  # Writable
[[ -x "$file" ]]  # Executable
[[ -s "$file" ]]  # Size > 0
[[ "$f1" -nt "$f2" ]]  # f1 newer than f2
```

**Exempel:**
```bash
if [[ -f "/etc/passwd" ]]; then
    echo "passwd file exists"
fi
```""",
                        "common_mistake": "Använd -f för filer och -d för directories - de är inte samma sak!"
                    },
                    {
                        "title": "Case Statement",
                        "explanation": """```bash
case "$var" in
    pattern1)
        echo "Matched pattern1"
        ;;
    pattern2|pattern3)
        echo "Matched pattern2 or 3"
        ;;
    *)
        echo "Default case"
        ;;
esac
```

**Wildcards i patterns:**
- `*` - matchar allt
- `?` - matchar ett tecken
- `[abc]` - matchar a, b, eller c""",
                        "pro_tip": "Case är perfekt för menyval och argument-parsing"
                    }
                ]
            }
        },
        {
            "type": "practice",
            "content": {
                "exercises": [
                    {
                        "task": "Kolla om fil existerar",
                        "instruction": "Skriv ett villkor som kollar om /etc/passwd existerar",
                        "expected_command": "[[ -f /etc/passwd ]] && echo 'Exists'",
                        "hint": "-f testar om det är en vanlig fil"
                    },
                    {
                        "task": "Jämför strängar",
                        "instruction": "Kolla om variabeln ENV är satt till 'production'",
                        "expected_command": "[[ \"$ENV\" == \"production\" ]] && echo 'Prod mode'",
                        "hint": "Använd == för strängjämförelse"
                    },
                    {
                        "task": "Numerisk jämförelse",
                        "instruction": "Kolla om variabeln count är större än 10",
                        "expected_command": "(( count > 10 )) && echo 'High count'",
                        "hint": "Använd (( )) för aritmetik"
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
                            "question": "Vilken operator kollar om en fil är en directory?",
                            "options": ["-f", "-d", "-e", "-dir"],
                            "correct": 1,
                            "explanation": "-d testar om path är en directory. -f testar om det är en vanlig fil."
                        },
                        {
                            "question": "Vad gör [[ -z \"$var\" ]]?",
                            "options": [
                                "Kollar om var finns",
                                "Kollar om var är tom",
                                "Kollar om var är ett tal",
                                "Kollar om var är en fil"
                            ],
                            "correct": 1,
                            "explanation": "-z (zero) returnerar true om strängen är tom."
                        },
                        {
                            "question": "Hur avslutar du ett if-statement i Bash?",
                            "options": ["end", "endif", "fi", "}"],
                            "correct": 2,
                            "explanation": "fi (if baklänges) avslutar if-statement i Bash."
                        }
                    ]
                }
            }
        },
        {
            "type": "challenge",
            "content": {
                "scenario": "Skapa ett script som validerar en deployment-miljö",
                "requirements": [
                    "Kolla att config-fil existerar",
                    "Verifiera att ENV är 'staging' eller 'production'",
                    "Kontrollera att port-variabeln är ett nummer > 1024",
                    "Skriv ut status för varje check"
                ],
                "hints": [
                    "Använd -f för fil-check",
                    "Använd case för ENV-validering",
                    "Använd (( )) för numerisk jämförelse"
                ],
                "solution": """#!/usr/bin/env bash
CONFIG="/etc/app/config.yaml"
ENV="${ENV:-staging}"
PORT="${PORT:-8080}"

echo "Validating deployment..."

if [[ -f "$CONFIG" ]]; then
    echo "✓ Config file exists"
else
    echo "✗ Config file missing!"
    exit 1
fi

case "$ENV" in
    staging|production)
        echo "✓ Valid environment: $ENV"
        ;;
    *)
        echo "✗ Invalid environment: $ENV"
        exit 1
        ;;
esac

if (( PORT > 1024 )); then
    echo "✓ Valid port: $PORT"
else
    echo "✗ Port must be > 1024"
    exit 1
fi

echo "All checks passed!"""
            }
        }
    ]
}
