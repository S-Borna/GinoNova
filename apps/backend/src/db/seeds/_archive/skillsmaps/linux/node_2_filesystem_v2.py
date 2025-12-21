"""
Linux Mastery Node 2: File System Navigation - V2 Interactive Format
"""

LINUX_NODE_2_FILESYSTEM_V2 = {
    "node_id": 2,
    "title": "File System Navigation",
    "slug": "file-system-navigation",
    "description": "Navigera Linux filsystemet som en expert",
    "difficulty": "beginner",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "File System Navigation",
            "content": {
                "headline": "Master the filesystem, master Linux",
                "hook": "Linux filsystemet är operativsystemets nervsystem. Varje config, varje logg, varje program har sin plats enligt FHS standarden.",
                "learning_objectives": [
                    "Förstå FHS (Filesystem Hierarchy Standard)",
                    "Navigera effektivt med cd, ls, pwd, find",
                    "Hitta filer med find, locate och which",
                    "Förstå absoluta vs relativa sökvägar"
                ],
                "prerequisites": ["Terminal basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Filesystem Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "FHS - Filesystem Hierarchy Standard",
                        "explanation": "/bin (binaries), /etc (config), /home (users), /var (logs/data), /tmp (temp), /usr (user programs), /opt (third-party).",
                        "diagram": """
+---------------------------------------------+
| /                                           |
+---------------------------------------------+
| /bin    | Essential binaries (ls, cp)      |
| /etc    | System configuration             |
| /home   | User home directories            |
| /var    | Variable data (logs, spool)      |
| /tmp    | Temporary files                  |
| /usr    | User programs                    |
| /opt    | Third-party software             |
+---------------------------------------------+""",
                        "pro_tip": "/etc/passwd = users, /etc/shadow = passwords, /var/log = logs",
                        "common_mistake": "Att inte veta var loggar finns - alltid /var/log/"
                    },
                    {
                        "title": "Absoluta vs Relativa sökvägar",
                        "explanation": "Absolut börjar med / (från root). Relativ börjar från current directory. . = current, .. = parent, ~ = home.",
                        "diagram": """
+---------------------------------------------+
| ABSOLUT                                     |
| /home/user/docs/file.txt                   |
+---------------------------------------------+
| RELATIV (pwd=/home/user)                   |
| docs/file.txt                              |
| ./docs/file.txt                            |
| ../other/file.txt                          |
| ~/docs/file.txt                            |
+---------------------------------------------+""",
                        "pro_tip": "I scripts, använd alltid absoluta sökvägar för förutsägbarhet.",
                        "common_mistake": "Att glömma att ~ bara fungerar i shell, inte i alla program."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Navigation",
            "content": {
                "exercises": [
                    {
                        "task": "Lista filer med detaljer",
                        "instruction": "Visa alla filer (inkl dolda) med storlek human-readable",
                        "expected_command": "ls -lah",
                        "hint": "-l = long, -a = all, -h = human readable"
                    },
                    {
                        "task": "Hitta config-filer",
                        "instruction": "Hitta alla .conf filer i /etc",
                        "expected_command": "find /etc -name '*.conf' 2>/dev/null",
                        "hint": "2>/dev/null döljer permission errors"
                    },
                    {
                        "task": "Hitta kommando-plats",
                        "instruction": "Hitta var nginx-binären finns",
                        "expected_command": "which nginx",
                        "hint": "which söker i PATH"
                    },
                    {
                        "task": "Visa katalogstruktur",
                        "instruction": "Visa trädstruktur av /var/log 2 nivåer djupt",
                        "expected_command": "tree -L 2 /var/log",
                        "hint": "-L begränsar djupet"
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
                        {"front": "Var finns systemkonfiguration?", "back": "/etc - alla config-filer för system och tjänster"},
                        {"front": "Var finns loggar?", "back": "/var/log - systemloggar, apploggar, auth.log etc"},
                        {"front": "Vad gör 'find / -name X'?", "back": "Söker rekursivt från root efter fil med namn X"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken katalog innehåller användarnas hemkataloger?",
                            "options": ["/usr", "/home", "/root", "/var"],
                            "correct": 1,
                            "explanation": "/home innehåller vanliga användares hemkataloger, /root är root-användarens hem"
                        },
                        {
                            "question": "Vad betyder .. i en sökväg?",
                            "options": ["Current directory", "Parent directory", "Home directory", "Root directory"],
                            "correct": 1,
                            "explanation": ".. = parent directory (en nivå upp), . = current directory"
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
            "title": "Filesystem Challenge",
            "content": {
                "scenario": "Du felsöker en webbserver. Hitta relevant information.",
                "requirements": [
                    "Hitta nginx config-fil",
                    "Lista senaste loggarna i /var/log/nginx",
                    "Hitta alla filer större än 100MB",
                    "Visa diskutrymme per katalog"
                ],
                "hints": [
                    "find /etc -name 'nginx*'",
                    "ls -lt för att sortera på tid",
                    "find / -size +100M"
                ],
                "solution": """# 1. Hitta nginx config
find /etc -name 'nginx*' 2>/dev/null
# eller
locate nginx.conf

# 2. Senaste nginx-loggar
ls -lt /var/log/nginx/ | head -10

# 3. Stora filer
find / -type f -size +100M 2>/dev/null

# 4. Diskutrymme per katalog
du -sh /* 2>/dev/null | sort -h""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
