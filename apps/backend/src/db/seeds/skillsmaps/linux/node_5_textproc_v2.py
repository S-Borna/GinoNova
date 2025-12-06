"""
Linux Mastery Node 5: Text Processing - V2 Interactive Format
"""

LINUX_NODE_5_TEXTPROC_V2 = {
    "node_id": 5,
    "title": "Text Processing Power Tools",
    "slug": "text-processing",
    "description": "Grep, sed, awk - manipulera text som ett proffs",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Text Processing",
            "content": {
                "headline": "Loggar är dina ögon in i produktion",
                "hook": "I DevOps flödar data genom text - loggar, configs, pipelines. Förmågan att slica, filtrera och transformera text är inte valfri, det är överlevnad.",
                "learning_objectives": [
                    "Använda grep för kraftfull textsökning",
                    "Transformera text med sed",
                    "Bearbeta strukturerad data med awk",
                    "Kombinera tools med pipes"
                ],
                "prerequisites": ["File operations", "Regex basics hjälper"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Text Processing Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "grep - Sök och filtrera",
                        "explanation": "-i (case insensitive), -v (invertera), -r (rekursiv), -n (radnummer), -c (count), -E (extended regex).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ grep FLAGS                                  │
├─────────────────────────────────────────────┤
│ -i  │ Case insensitive                     │
│ -v  │ Invertera (visa EJ matchande)        │
│ -r  │ Rekursiv sökning i kataloger         │
│ -n  │ Visa radnummer                       │
│ -c  │ Räkna matchningar                    │
│ -E  │ Extended regex (egrep)               │
│ -A3 │ Visa 3 rader efter match             │
│ -B3 │ Visa 3 rader före match              │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "tail -f log | grep --line-buffered 'ERROR' för realtids-filtrering.",
                        "common_mistake": "Att glömma -i när man söker - case matters!"
                    },
                    {
                        "title": "sed & awk",
                        "explanation": "sed = stream editor för search/replace. awk = pattern scanning och text processing med fält.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ sed 's/old/new/g' file   # Replace all     │
│ sed -i 's/old/new/g' f   # In-place edit   │
│ sed '/pattern/d' file    # Delete lines    │
├─────────────────────────────────────────────┤
│ awk '{print $1}' file    # Print field 1   │
│ awk -F: '{print $1}'     # Custom delimiter │
│ awk '$3 > 100' file      # Filter by value │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "awk är perfekt för CSV/log-parsing: awk -F',' '{print $2}'",
                        "common_mistake": "Att glömma -i.bak med sed - du förlorar original."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Text Processing",
            "content": {
                "exercises": [
                    {
                        "task": "Sök case-insensitive",
                        "instruction": "Hitta alla rader med 'error' (oavsett case) i logfile",
                        "expected_command": "grep -i 'error' logfile",
                        "hint": "-i = ignore case"
                    },
                    {
                        "task": "Ersätt text",
                        "instruction": "Byt ut 'localhost' mot '127.0.0.1' i config.conf",
                        "expected_command": "sed -i 's/localhost/127.0.0.1/g' config.conf",
                        "hint": "-i för in-place, g för global"
                    },
                    {
                        "task": "Extrahera fält",
                        "instruction": "Skriv ut första fältet (usernames) från /etc/passwd",
                        "expected_command": "awk -F: '{print $1}' /etc/passwd",
                        "hint": "-F: sätter delimiter till kolon"
                    },
                    {
                        "task": "Räkna matchningar",
                        "instruction": "Räkna antal 404-errors i access.log",
                        "expected_command": "grep -c '404' access.log",
                        "hint": "-c = count"
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
                        {"front": "Vad gör grep -v?", "back": "Invertera - visar rader som INTE matchar mönstret"},
                        {"front": "Vad gör sed 's/a/b/g'?", "back": "Ersätter alla 'a' med 'b' (g = global, utan g bara första per rad)"},
                        {"front": "Hur väljer du fält 3 med awk?", "back": "awk '{print $3}' - $1 är första fältet"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilket kommando följer en loggfil i realtid?",
                            "options": ["cat -f", "tail -f", "head -f", "grep -f"],
                            "correct": 1,
                            "explanation": "tail -f 'följer' filen och visar nya rader direkt"
                        },
                        {
                            "question": "Hur gör du sed-ersättning in-place?",
                            "options": ["sed 's/a/b/'", "sed -i 's/a/b/'", "sed -r 's/a/b/'", "sed -e 's/a/b/'"],
                            "correct": 1,
                            "explanation": "-i editerar filen direkt (in-place)"
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
            "title": "Text Processing Challenge",
            "content": {
                "scenario": "Analysera en Apache access log för security review.",
                "requirements": [
                    "Hitta alla 404-errors",
                    "Lista unika IP-adresser som fick 404",
                    "Räkna requests per IP",
                    "Hitta mest aktiva IP"
                ],
                "hints": [
                    "grep '404' för att filtrera",
                    "awk '{print $1}' för IP (första fältet)",
                    "sort | uniq -c för counting"
                ],
                "solution": """# 1. Visa 404-errors
grep ' 404 ' access.log

# 2. Lista unika IP:er med 404
grep ' 404 ' access.log | awk '{print $1}' | sort -u

# 3. Räkna requests per IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# 4. Top 10 mest aktiva
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# 5. Bonus: One-liner för IP med flest 404
grep ' 404 ' access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -1""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
