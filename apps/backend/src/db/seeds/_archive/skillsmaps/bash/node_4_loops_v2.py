"""
Bash Node 4: Loops & Iteration (V2 Format)
==========================================
Master for, while, until loops and loop control
"""

NODE_BASH_04_LOOPS_V2 = {
    "id": "bash-04-loops",
    "title": "Loops & Iteration",
    "slug": "bash-loops",
    "description": "Master for, while, until loops and loop control",
    "difficulty": "beginner",
    "estimated_minutes": 30,
    "xp_reward": 100,
    "sections": [
        {
            "type": "intro",
            "content": {
                "headline": "Loops & Iteration",
                "hook": "Automation handlar om att inte upprepa dig själv. Loops gör det möjligt.",
                "learning_objectives": [
                    "Använda for-loops för listor och sekvenser",
                    "Använda while och until för villkorsbaserade loops",
                    "Kontrollera loops med break och continue",
                    "Processa filer rad för rad"
                ],
                "prerequisites": ["Bash Conditionals"],
                "estimated_time": "30 minuter",
                "xp_reward": 100
            }
        },
        {
            "type": "concepts",
            "content": {
                "concepts": [
                    {
                        "title": "For Loop - Listor",
                        "explanation": """```bash
# Över en lista
for item in apple banana cherry; do
    echo "Fruit: $item"
done

# Över en array
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# Över filer
for file in *.txt; do
    echo "Processing: $file"
done
```""",
                        "pro_tip": "Använd alltid \"${array[@]}\" med quotes för att hantera element med spaces korrekt"
                    },
                    {
                        "title": "For Loop - Sekvenser",
                        "explanation": """```bash
# C-style loop
for ((i=0; i<10; i++)); do
    echo "Number: $i"
done

# Med seq
for i in $(seq 1 5); do
    echo "Count: $i"
done

# Med brace expansion (snabbare)
for i in {1..5}; do
    echo "Count: $i"
done

# Med steg
for i in {0..100..10}; do
    echo "$i"  # 0, 10, 20, ..., 100
done
```""",
                        "common_mistake": "Brace expansion {1..5} fungerar inte med variabler. Använd seq för dynamiska ranges."
                    },
                    {
                        "title": "While Loop",
                        "explanation": """```bash
# Räkna uppåt
count=0
while (( count < 5 )); do
    echo "Count: $count"
    ((count++))
done

# Läs fil rad för rad
while IFS= read -r line; do
    echo "Line: $line"
done < file.txt

# Oändlig loop
while true; do
    echo "Running..."
    sleep 1
done
```""",
                        "pro_tip": "IFS= och -r i read bevarar whitespace och backslashes korrekt"
                    },
                    {
                        "title": "Until Loop",
                        "explanation": """```bash
# Kör TILLS villkoret är sant
count=0
until (( count >= 5 )); do
    echo "Count: $count"
    ((count++))
done

# Vänta på service
until curl -s http://localhost:8080/health; do
    echo "Waiting for service..."
    sleep 2
done
echo "Service is up!"
```""",
                        "pro_tip": "Until är perfekt för polling och vänta-på-villkor scenarion"
                    },
                    {
                        "title": "Break & Continue",
                        "explanation": """```bash
# break - avsluta loopen helt
for i in {1..10}; do
    if (( i == 5 )); then
        break
    fi
    echo "$i"  # 1, 2, 3, 4
done

# continue - hoppa till nästa iteration
for i in {1..5}; do
    if (( i == 3 )); then
        continue
    fi
    echo "$i"  # 1, 2, 4, 5
done
```""",
                        "common_mistake": "break och continue fungerar endast i loops, inte i funktioner"
                    }
                ]
            }
        },
        {
            "type": "practice",
            "content": {
                "exercises": [
                    {
                        "task": "Loop över filer",
                        "instruction": "Lista alla .sh filer i current directory",
                        "expected_command": "for f in *.sh; do echo \"$f\"; done",
                        "hint": "Använd glob pattern *.sh"
                    },
                    {
                        "task": "Räkna till 5",
                        "instruction": "Använd brace expansion för att skriva ut 1 till 5",
                        "expected_command": "for i in {1..5}; do echo $i; done",
                        "hint": "{start..end} skapar en sekvens"
                    },
                    {
                        "task": "While-loop med räknare",
                        "instruction": "Räkna från 0 till 3 med while",
                        "expected_command": "i=0; while (( i < 4 )); do echo $i; ((i++)); done",
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
                            "question": "Hur loopar du korrekt över en array med spaces i elementen?",
                            "options": [
                                "for item in ${arr[@]}",
                                "for item in \"${arr[@]}\"",
                                "for item in $arr",
                                "for item in arr[]"
                            ],
                            "correct": 1,
                            "explanation": "Quotes runt ${arr[@]} förhindrar word splitting på element med spaces."
                        },
                        {
                            "question": "Vad gör 'continue' i en loop?",
                            "options": [
                                "Avslutar loopen",
                                "Hoppar till nästa iteration",
                                "Pausar loopen",
                                "Startar om loopen"
                            ],
                            "correct": 1,
                            "explanation": "continue hoppar över resten av iterationen och fortsätter med nästa."
                        },
                        {
                            "question": "Vilken syntax läser en fil rad för rad korrekt?",
                            "options": [
                                "for line in file.txt",
                                "while read line < file.txt",
                                "while IFS= read -r line; do ... done < file.txt",
                                "cat file.txt | for line"
                            ],
                            "correct": 2,
                            "explanation": "IFS= bevarar whitespace, -r bevarar backslashes, och redirect sker efter done."
                        }
                    ]
                }
            }
        },
        {
            "type": "challenge",
            "content": {
                "scenario": "Skapa ett script som processar logfiler i en directory",
                "requirements": [
                    "Loopa genom alla .log filer",
                    "Räkna antal rader i varje fil",
                    "Hoppa över filer som är tomma",
                    "Skriv ut totalt antal rader i slutet"
                ],
                "hints": [
                    "wc -l räknar rader",
                    "[[ -s file ]] kollar om fil har innehåll",
                    "continue hoppar över tomma filer"
                ],
                "solution": """#!/usr/bin/env bash
total=0

for logfile in *.log; do
    if [[ ! -s "$logfile" ]]; then
        echo "Skipping empty: $logfile"
        continue
    fi

    lines=$(wc -l < "$logfile")
    echo "$logfile: $lines lines"
    ((total += lines))
done

echo "Total lines: $total"""
            }
        }
    ]
}
