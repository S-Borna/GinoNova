"""
Linux Mastery Node 4: File Permissions - V2 Interactive Format
"""

LINUX_NODE_4_PERMISSIONS_V2 = {
    "node_id": 4,
    "title": "File Permissions Deep Dive",
    "slug": "file-permissions",
    "description": "Kontrollera access med chmod, chown och ACLs",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "File Permissions",
            "content": {
                "headline": "Permissions är första försvarslinjen",
                "hook": "En felkonfigurerad permission kan exponera känslig data, tillåta obehörig access eller krascha din applikation. I security audits kollas permissions alltid först.",
                "learning_objectives": [
                    "Förstå rwx permissions för user/group/other",
                    "Använda chmod med numerisk och symbolisk notation",
                    "Hantera ägare med chown och chgrp",
                    "Förstå special permissions (SUID, SGID, sticky bit)"
                ],
                "prerequisites": ["File operations basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Permission Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "rwx för User/Group/Other",
                        "explanation": "r=4 (read), w=2 (write), x=1 (execute). Tre kategorier: owner (u), group (g), others (o). 755 = rwxr-xr-x.",
                        "diagram": """
+---------------------------------------------+
| -rwxr-xr-x   1   user   group   file.sh     |
|  |||||||||                                  |
|  |||||||||                                  |
|  |||++++++--- others: r-x (5)              |
|  |||                                        |
|  |+++------ group: r-x (5)                 |
|  |                                          |
|  +--------- owner: rwx (7)                 |
|                                             |
| Numeriskt: 755                              |
+---------------------------------------------+""",
                        "pro_tip": "777 = alla kan allt. Använd ALDRIG på config-filer eller scripts.",
                        "common_mistake": "chmod 777 för att 'fixa' permission-problem. Det är en säkerhetsrisk."
                    },
                    {
                        "title": "Special Permissions",
                        "explanation": "SUID (4xxx) = kör som ägare. SGID (2xxx) = kör som grupp / inherit grupp. Sticky (1xxx) = endast ägare kan ta bort.",
                        "diagram": """
+---------------------------------------------+
| SPECIAL PERMISSIONS                         |
+---------------------------------------------+
| SUID (4xxx) | -rwsr-xr-x | Kör som owner   |
| SGID (2xxx) | -rwxr-sr-x | Kör som group   |
| Sticky(1xxx)| drwxrwxrwt | Endast owner rm |
+---------------------------------------------+
| Exempel:                                    |
| /usr/bin/passwd = SUID (ändrar /etc/shadow)|
| /tmp           = Sticky (alla kan skapa)   |
+---------------------------------------------+""",
                        "pro_tip": "SUID på user scripts är en säkerhetsrisk. Audit med: find / -perm -4000",
                        "common_mistake": "Att sätta SUID utan att förstå implikationerna."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Permissions",
            "content": {
                "exercises": [
                    {
                        "task": "Sätt läs/körbar för alla",
                        "instruction": "Ge script.sh rwx för ägare, rx för andra",
                        "expected_command": "chmod 755 script.sh",
                        "hint": "7=rwx, 5=rx. 755 är standard för scripts."
                    },
                    {
                        "task": "Ta bort write för others",
                        "instruction": "Ta bort skrivrätt för others på config.cfg",
                        "expected_command": "chmod o-w config.cfg",
                        "hint": "o-w = others minus write"
                    },
                    {
                        "task": "Ändra ägare",
                        "instruction": "Sätt www-data som ägare och grupp på /var/www",
                        "expected_command": "chown -R www-data:www-data /var/www",
                        "hint": "-R för recursive, user:group format"
                    },
                    {
                        "task": "Hitta SUID-filer",
                        "instruction": "Lista alla filer med SUID bit satt",
                        "expected_command": "find / -perm -4000 2>/dev/null",
                        "hint": "-perm -4000 hittar SUID"
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
                        {"front": "Vad betyder 644?", "back": "rw-r--r-- : Owner kan läsa/skriva, alla andra kan bara läsa"},
                        {"front": "Vad är sticky bit?", "back": "Bara ägaren av en fil kan ta bort den, även om andra har write på katalogen (t.ex. /tmp)"},
                        {"front": "Vad gör SUID?", "back": "Processen körs med ägarens permissions, inte användarens"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken permission är typisk för webbfiler (läsbar för webserver)?",
                            "options": ["777", "644", "600", "000"],
                            "correct": 1,
                            "explanation": "644 = owner rw, group+others read only. Säkert för webbfiler."
                        },
                        {
                            "question": "Var hittar du /tmp sticky bit?",
                            "options": ["rwx------", "rwxrwxrwx", "rwxrwxrwt", "rwxr-xr-x"],
                            "correct": 2,
                            "explanation": "'t' i slutet visar sticky bit är satt"
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
            "title": "Permissions Challenge",
            "content": {
                "scenario": "Säkra en webbapplikation med korrekta permissions.",
                "requirements": [
                    "Webroot /var/www/app ägs av www-data",
                    "PHP-filer: 644 (läs för alla, write för owner)",
                    "Upload-katalog: 755 med SGID",
                    "Config-filer: 600 (endast owner)"
                ],
                "hints": [
                    "chown -R www-data:www-data",
                    "find -type f för filer, -type d för kataloger",
                    "chmod g+s för SGID"
                ],
                "solution": """# 1. Sätt ägare
chown -R www-data:www-data /var/www/app

# 2. Sätt katalog-permissions (755)
find /var/www/app -type d -exec chmod 755 {} \\;

# 3. Sätt fil-permissions (644)
find /var/www/app -type f -exec chmod 644 {} \\;

# 4. Upload med SGID
chmod 2755 /var/www/app/uploads
# eller
chmod g+s /var/www/app/uploads

# 5. Skydda config (600 = endast owner)
chmod 600 /var/www/app/config/*.php

# 6. Verifiera
ls -la /var/www/app/
ls -la /var/www/app/config/""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
