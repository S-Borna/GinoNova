"""
Linux Mastery Node 8: User & Group Management - V2 Interactive Format
"""

LINUX_NODE_8_USERS_V2 = {
    "node_id": 8,
    "title": "User & Group Management",
    "slug": "user-group-management",
    "description": "Skapa och hantera användare, grupper och sudo",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "User & Group Management",
            "content": {
                "headline": "Kontrollera vem som får göra vad",
                "hook": "Varje process körs som en användare. Varje fil ägs av en användare. User management är grunden för Linux-säkerhet.",
                "learning_objectives": [
                    "Skapa och ta bort användare med useradd/userdel",
                    "Hantera grupper och gruppmedlemskap",
                    "Konfigurera sudo-rättigheter säkert",
                    "Förstå /etc/passwd, /etc/shadow och /etc/group"
                ],
                "prerequisites": ["File permissions"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "User Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "User & Group Files",
                        "explanation": "/etc/passwd (user info), /etc/shadow (encrypted passwords), /etc/group (grupper). Varje user har UID, varje grupp har GID.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ /etc/passwd                                 │
│ john:x:1000:1000:John Doe:/home/john:/bin/bash│
│  │   │  │    │      │        │         │     │
│  │   │  │    │      │        │         └─shell│
│  │   │  │    │      │        └─home dir      │
│  │   │  │    │      └─comment (GECOS)        │
│  │   │  │    └─primary GID                   │
│  │   │  └─UID                                │
│  │   └─password (x = in shadow)              │
│  └─username                                  │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "UID 0 = root. UIDs under 1000 är ofta system-användare.",
                        "common_mistake": "Att editera passwd/shadow manuellt. Använd useradd/usermod!"
                    },
                    {
                        "title": "sudo & sudoers",
                        "explanation": "sudo kör kommandon som root. /etc/sudoers styr vem som får. Editera ALLTID med visudo (syntax check).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ SUDOERS FORMAT                              │
│ user  host=(runas) commands                 │
├─────────────────────────────────────────────┤
│ john  ALL=(ALL) ALL                         │
│ %sudo ALL=(ALL) ALL                         │
│ deploy ALL=(ALL) NOPASSWD: /bin/systemctl   │
└─────────────────────────────────────────────┘
# % = grupp, NOPASSWD = inget lösenord""",
                        "pro_tip": "Lägg egna regler i /etc/sudoers.d/ istället för att ändra huvudfilen.",
                        "common_mistake": "Att editera sudoers utan visudo - syntax-fel = låst ute!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Users",
            "content": {
                "exercises": [
                    {
                        "task": "Skapa användare",
                        "instruction": "Skapa användare 'deploy' med home-katalog och bash shell",
                        "expected_command": "sudo useradd -m -s /bin/bash deploy",
                        "hint": "-m skapar home, -s sätter shell"
                    },
                    {
                        "task": "Lägg till i grupp",
                        "instruction": "Lägg till 'deploy' i gruppen 'docker'",
                        "expected_command": "sudo usermod -aG docker deploy",
                        "hint": "-aG = append to Groups (behåller andra grupper)"
                    },
                    {
                        "task": "Visa användarinfo",
                        "instruction": "Visa UID, GID och grupper för en användare",
                        "expected_command": "id deploy",
                        "hint": "id visar all identity-info"
                    },
                    {
                        "task": "Sätt sudo utan lösenord",
                        "instruction": "Ge 'deploy' sudo utan lösenord för systemctl",
                        "expected_command": "echo 'deploy ALL=(ALL) NOPASSWD: /bin/systemctl' | sudo tee /etc/sudoers.d/deploy",
                        "hint": "Skapa fil i sudoers.d istället för att ändra huvudfilen"
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
                        {"front": "Vad gör usermod -aG?", "back": "Append to Groups - lägger till användare i grupp utan att ta bort från andra"},
                        {"front": "Varför använda visudo?", "back": "Syntax-validering innan sparning - fel i sudoers = låst ute från sudo"},
                        {"front": "Var lagras krypterade lösenord?", "back": "/etc/shadow (läsbar endast av root)"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken fil innehåller grupp-definitioner?",
                            "options": ["/etc/passwd", "/etc/shadow", "/etc/group", "/etc/users"],
                            "correct": 2,
                            "explanation": "/etc/group innehåller grupp-namn, GID och medlemmar"
                        },
                        {
                            "question": "Vad betyder NOPASSWD i sudoers?",
                            "options": ["Ingen användare", "Tomt lösenord", "Sudo utan lösenord", "Disable user"],
                            "correct": 2,
                            "explanation": "NOPASSWD låter användaren köra sudo utan att ange lösenord"
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
            "title": "User Management Challenge",
            "content": {
                "scenario": "Sätt upp en deployment-användare för CI/CD.",
                "requirements": [
                    "Skapa användare 'cicd' med home och bash",
                    "Lägg till i grupperna 'docker' och 'www-data'",
                    "Ge sudo för systemctl och docker utan lösenord",
                    "Verifiera setup"
                ],
                "hints": [
                    "useradd -m -s /bin/bash",
                    "usermod -aG grupp1,grupp2",
                    "sudoers.d för separata regler"
                ],
                "solution": """# 1. Skapa användare
sudo useradd -m -s /bin/bash -c "CI/CD Deploy User" cicd

# 2. Lägg till i grupper
sudo usermod -aG docker,www-data cicd

# 3. Konfigurera sudo
cat << 'EOF' | sudo tee /etc/sudoers.d/cicd
cicd ALL=(ALL) NOPASSWD: /bin/systemctl, /usr/bin/docker, /usr/bin/docker-compose
EOF
sudo chmod 440 /etc/sudoers.d/cicd

# 4. Verifiera
id cicd
sudo -l -U cicd

# 5. Testa (som cicd)
sudo -u cicd sudo systemctl status nginx""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
