"""
Linux Mastery Node 14: Firewall Management - V2 Interactive Format
"""

LINUX_NODE_14_FIREWALL_V2 = {
    "node_id": 14,
    "title": "Firewall Management",
    "slug": "firewall",
    "description": "Kontrollera nätverkstrafik med ufw och iptables",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Firewall Management",
            "content": {
                "headline": "En server utan firewall är en öppen dörr",
                "hook": "Varje port du lämnar öppen är en potentiell attackvektor. Firewalls är din första försvarslinje - de bestämmer vilken trafik som släpps in och ut.",
                "learning_objectives": [
                    "Konfigurera UFW (Ubuntu Firewall)",
                    "Förstå grundläggande iptables",
                    "Sätta upp säkra default policies",
                    "Tillåta och blockera specifika portar och IP-adresser"
                ],
                "prerequisites": ["Networking basics", "Services management"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Firewall Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "UFW - Uncomplicated Firewall",
                        "explanation": "UFW är standard på Ubuntu. Enkelt interface över iptables. 'deny incoming, allow outgoing' är säker default.",
                        "diagram": """
+-----------------------------------------------------+
| UFW KOMMANDON                                       |
+-----------------------------------------------------+
| sudo ufw status         | Visa status & regler     |
| sudo ufw enable         | Aktivera firewall        |
| sudo ufw disable        | Inaktivera              |
| sudo ufw default deny incoming                      |
| sudo ufw default allow outgoing                     |
| sudo ufw allow 22       | Tillåt SSH              |
| sudo ufw allow ssh      | Samma (service name)    |
| sudo ufw deny 23        | Blockera port           |
| sudo ufw delete allow 80| Ta bort regel           |
+-----------------------------------------------------+""",
                        "pro_tip": "ALLTID tillåt SSH (port 22) INNAN du aktiverar firewall!",
                        "common_mistake": "Att aktivera firewall utan att tillåta SSH - du låser dig ute!"
                    },
                    {
                        "title": "Avancerade UFW-regler",
                        "explanation": "UFW kan filtrera på IP, nätverk, port ranges och application profiles.",
                        "diagram": """
+-----------------------------------------------------+
| AVANCERADE UFW REGLER                               |
+-----------------------------------------------------+
| # Tillåt från specifik IP                          |
| sudo ufw allow from 192.168.1.100                  |
|                                                     |
| # Tillåt nätverk till specifik port                |
| sudo ufw allow from 192.168.1.0/24 to any port 22  |
|                                                     |
| # Port range                                        |
| sudo ufw allow 6000:6007/tcp                       |
|                                                     |
| # Application profiles                              |
| sudo ufw app list                                  |
| sudo ufw allow "Nginx Full"                        |
+-----------------------------------------------------+""",
                        "pro_tip": "'ufw status numbered' visar regelnummer för enkel deletion",
                        "common_mistake": "Att glömma /tcp eller /udp när det är relevant."
                    },
                    {
                        "title": "iptables Grunderna",
                        "explanation": "iptables är det underliggande systemet. INPUT=till server, OUTPUT=från server, FORWARD=genom server.",
                        "diagram": """
+-----------------------------------------------------+
| IPTABLES CHAINS                                     |
+-----------------------------------------------------+
|   Internet                                          |
|       |                                             |
|       ▼                                             |
|   +-----------+                                     |
|   |   INPUT   | -> Trafik TO this server            |
|   +-----------+                                     |
|       |                                             |
|       ▼                                             |
|   [Server processes]                                |
|       |                                             |
|       ▼                                             |
|   +-----------+                                     |
|   |  OUTPUT   | -> Trafik FROM this server          |
|   +-----------+                                     |
|       |                                             |
|       ▼                                             |
|   Internet                                          |
+-----------------------------------------------------+""",
                        "pro_tip": "Använd UFW istället för raw iptables - mycket enklare!",
                        "common_mistake": "Att inte spara iptables-regler - de försvinner vid reboot."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Firewall",
            "content": {
                "exercises": [
                    {
                        "task": "Visa firewall status",
                        "instruction": "Kontrollera om UFW är aktivt och visa alla regler",
                        "expected_command": "sudo ufw status verbose",
                        "hint": "verbose ger mer detaljer"
                    },
                    {
                        "task": "Tillåt SSH",
                        "instruction": "Lägg till regel för att tillåta SSH-anslutningar",
                        "expected_command": "sudo ufw allow ssh",
                        "hint": "Du kan också använda 'allow 22'"
                    },
                    {
                        "task": "Tillåt webbtrafik",
                        "instruction": "Tillåt både HTTP (80) och HTTPS (443)",
                        "expected_command": "sudo ufw allow 80 && sudo ufw allow 443",
                        "hint": "Du kan också använda 'allow http' och 'allow https'"
                    },
                    {
                        "task": "Blockera IP",
                        "instruction": "Blockera all trafik från IP 10.0.0.5",
                        "expected_command": "sudo ufw deny from 10.0.0.5",
                        "hint": "'deny from' blockerar inkommande trafik från IP"
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
                        {"front": "Vad bör vara första regeln du lägger till?", "back": "allow ssh (port 22) - annars låser du dig ute!"},
                        {"front": "Skillnad mellan ufw allow och ufw deny?", "back": "allow släpper igenom trafik, deny blockerar den"},
                        {"front": "Vad betyder 'default deny incoming'?", "back": "Blockera ALL inkommande trafik som inte explicit tillåts"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken ordning ska du göra firewall-setup?",
                            "options": [
                                "enable -> allow ssh -> set defaults",
                                "set defaults -> allow ssh -> enable",
                                "allow ssh -> set defaults -> enable",
                                "Ordningen spelar ingen roll"
                            ],
                            "correct": 1,
                            "explanation": "Sätt defaults, tillåt SSH, sedan enable - annars låser du ut dig!"
                        },
                        {
                            "question": "Hur tar du bort regel nummer 3?",
                            "options": ["ufw remove 3", "ufw delete 3", "ufw drop 3", "ufw rm 3"],
                            "correct": 1,
                            "explanation": "ufw delete [nummer] tar bort regeln på den positionen"
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
            "title": "Firewall Challenge",
            "content": {
                "scenario": "Säkra en webbserver: SSH + HTTP/HTTPS öppet, allt annat stängt.",
                "requirements": [
                    "Sätt säkra default policies",
                    "Tillåt SSH för administration",
                    "Tillåt webbtrafik (80 och 443)",
                    "Tillåt SSH bara från ditt kontor-nätverk (192.168.1.0/24)",
                    "Aktivera firewall och verifiera"
                ],
                "hints": [
                    "Börja med defaults innan specifika regler",
                    "Använd 'from network to any port' syntax",
                    "Kolla status innan och efter enable"
                ],
                "solution": """# 1. Sätt default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Tillåt SSH bara från kontorsnätverket
sudo ufw allow from 192.168.1.0/24 to any port 22

# 3. Tillåt webbtrafik från alla
sudo ufw allow 80
sudo ufw allow 443

# 4. Visa planerade regler innan aktivering
sudo ufw status

# 5. Aktivera
sudo ufw enable

# 6. Verifiera
sudo ufw status verbose

# Output bör visa:
# Default: deny (incoming), allow (outgoing)
# 22/tcp    ALLOW    192.168.1.0/24
# 80/tcp    ALLOW    Anywhere
# 443/tcp   ALLOW    Anywhere

# 7. Testa (från annat nätverk, SSH ska nekas)
# ssh user@server  # Should fail from outside 192.168.1.0/24""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
