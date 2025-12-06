"""
Linux Mastery Node 7: I/O Redirection & Pipes - V2 Interactive Format
"""

LINUX_NODE_7_PIPES_V2 = {
    "node_id": 7,
    "title": "I/O Redirection & Pipes",
    "slug": "io-redirection-pipes",
    "description": "Kontrollera dataflödet mellan kommandon",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "I/O Redirection & Pipes",
            "content": {
                "headline": "Unix filosofi: Små verktyg som gör en sak bra",
                "hook": "Pipes låter dig kombinera enkla verktyg till kraftfulla pipelines. grep | awk | sort | uniq kan göra vad som kräver hundratals rader kod i andra språk.",
                "learning_objectives": [
                    "Redirecta stdout, stderr och stdin",
                    "Bygga pipelines med pipe-operatorn",
                    "Använda tee för split output",
                    "Transformera input med xargs"
                ],
                "prerequisites": ["Text processing basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "I/O Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Redirection Operators",
                        "explanation": "> (stdout till fil), >> (append), 2> (stderr), &> (båda), < (input från fil), | (pipe till nästa kommando).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ REDIRECTION                                 │
├─────────────────────────────────────────────┤
│ cmd > file   │ stdout till fil (överskriver)│
│ cmd >> file  │ stdout append till fil       │
│ cmd 2> file  │ stderr till fil              │
│ cmd &> file  │ stdout + stderr till fil     │
│ cmd < file   │ stdin från fil               │
│ cmd1 | cmd2  │ stdout → stdin (pipe)        │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "2>&1 redirectar stderr till samma ställe som stdout.",
                        "common_mistake": "sudo echo 'text' > /etc/file fungerar inte! Använd: echo 'text' | sudo tee /etc/file"
                    },
                    {
                        "title": "tee & xargs",
                        "explanation": "tee skriver till fil OCH stdout (split stream). xargs bygger kommandon från stdin (t.ex. find | xargs rm).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ TEE - Split output                          │
│ cmd | tee file | cmd2                       │
│       ↓     ↓                               │
│      file  cmd2                             │
├─────────────────────────────────────────────┤
│ XARGS - Build commands                      │
│ find . -name "*.log" | xargs rm             │
│ (kör: rm file1.log file2.log ...)          │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "xargs -I {} låter dig placera argumentet var som helst: xargs -I {} mv {} {}.bak",
                        "common_mistake": "Spaces i filnamn kraschar xargs. Använd find -print0 | xargs -0"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on I/O",
            "content": {
                "exercises": [
                    {
                        "task": "Redirect stdout och stderr",
                        "instruction": "Kör kommando och spara output och errors till separata filer",
                        "expected_command": "find / -name '*.conf' > found.txt 2> errors.txt",
                        "hint": "> för stdout, 2> för stderr"
                    },
                    {
                        "task": "Pipeline för loganalys",
                        "instruction": "Hitta topp 5 IP-adresser i access.log",
                        "expected_command": "awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -5",
                        "hint": "awk extraherar, sort+uniq räknar, sort -rn sorterar numeriskt"
                    },
                    {
                        "task": "Tee för logging",
                        "instruction": "Kör kommando, visa output OCH spara till fil",
                        "expected_command": "ls -la | tee filelist.txt",
                        "hint": "tee skriver till fil och passerar vidare"
                    },
                    {
                        "task": "xargs för batch-operation",
                        "instruction": "Hitta alla .tmp filer och ta bort dem",
                        "expected_command": "find /tmp -name '*.tmp' | xargs rm -f",
                        "hint": "xargs tar input och bygger rm-kommando"
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
                        {"front": "Vad gör 2>&1?", "back": "Redirectar stderr (2) till samma destination som stdout (1)"},
                        {"front": "Skillnad mellan > och >>?", "back": "> överskriver filen, >> lägger till i slutet (append)"},
                        {"front": "Vad gör tee?", "back": "Skriver output till fil OCH skickar vidare till stdout (split stream)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Hur skriver du till en skyddad fil med sudo?",
                            "options": ["sudo echo 'x' > /etc/file", "echo 'x' | sudo tee /etc/file", "sudo > /etc/file echo 'x'", "sudo write 'x' /etc/file"],
                            "correct": 1,
                            "explanation": "Redirect körs som user, inte sudo. tee körs med sudo och kan skriva."
                        },
                        {
                            "question": "Vad gör xargs -I {} i: echo file.txt | xargs -I {} cp {} {}.bak?",
                            "options": ["Ignorerar input", "Skapar tom fil", "Ersätter {} med input", "Parallell körning"],
                            "correct": 2,
                            "explanation": "-I {} definierar placeholder som ersätts med varje input"
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
            "title": "Pipeline Challenge",
            "content": {
                "scenario": "Analysera webserver-loggar för säkerhetsöversikt.",
                "requirements": [
                    "Extrahera alla unika IP-adresser",
                    "Räkna requests per IP",
                    "Hitta IP:er med mer än 100 requests",
                    "Spara resultatet OCH visa i terminalen"
                ],
                "hints": [
                    "awk '{print $1}' för att extrahera IP",
                    "sort | uniq -c för att räkna",
                    "awk '$1 > 100' för att filtrera",
                    "tee för att både visa och spara"
                ],
                "solution": """# Komplett pipeline
awk '{print $1}' /var/log/nginx/access.log | \\
  sort | \\
  uniq -c | \\
  sort -rn | \\
  awk '$1 > 100 {print}' | \\
  tee suspicious_ips.txt

# Breakdown:
# awk '{print $1}'  - Extraherar IP (första fältet)
# sort              - Sorterar (krävs för uniq)
# uniq -c           - Räknar unika
# sort -rn          - Sorterar numeriskt, störst först
# awk '$1 > 100'    - Filtrerar: mer än 100 requests
# tee               - Sparar till fil OCH visar""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
