"""
Linux Mastery Node 10: Service Management (systemd) - V2 Interactive Format
"""

LINUX_NODE_10_SERVICES_V2 = {
    "node_id": 10,
    "title": "Service Management (systemd)",
    "slug": "service-management",
    "description": "Hantera systemtjänster med systemctl och journalctl",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Service Management",
            "content": {
                "headline": "Nginx slutade svara - vad gör du?",
                "hook": "Varje webbserver, databas och background service körs som en systemd unit. När nginx inte svarar eller PostgreSQL vägrar starta behöver du systemctl och journalctl.",
                "learning_objectives": [
                    "Starta, stoppa och hantera tjänster med systemctl",
                    "Läsa och analysera loggar med journalctl",
                    "Skapa egna systemd services",
                    "Felsöka tjänster som inte startar"
                ],
                "prerequisites": ["Package management basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Systemd Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "systemctl - Tjänsthantering",
                        "explanation": "systemctl är verktyget för att hantera tjänster. status, start, stop, restart, enable, disable är de viktigaste kommandona.",
                        "diagram": """
+-----------------------------------------------------+
| SYSTEMCTL KOMMANDON                                 |
+-----------------------------------------------------+
| systemctl status nginx    | Visa tjänstens status  |
| systemctl start nginx     | Starta tjänst          |
| systemctl stop nginx      | Stoppa tjänst          |
| systemctl restart nginx   | Starta om              |
| systemctl reload nginx    | Ladda om config        |
| systemctl enable nginx    | Autostart vid boot     |
| systemctl disable nginx   | Ingen autostart        |
| systemctl is-active nginx | Kör den?               |
| systemctl is-enabled nginx| Autostart aktiv?       |
+-----------------------------------------------------+""",
                        "pro_tip": "enable --now kombinerar enable + start i ett kommando!",
                        "common_mistake": "Glömma sudo - de flesta systemctl-kommandon kräver root."
                    },
                    {
                        "title": "journalctl - Systemloggar",
                        "explanation": "journalctl samlar ALLA systemd-loggar på ett ställe. Filtrera per tjänst, tid, prioritet.",
                        "diagram": """
+-----------------------------------------------------+
| JOURNALCTL KOMMANDON                                |
+-----------------------------------------------------+
| journalctl -u nginx       | Loggar för nginx       |
| journalctl -u nginx -f    | Följ live              |
| journalctl -u nginx -n 50 | Senaste 50 rader       |
| journalctl -u nginx -p err| Bara errors            |
| journalctl -u nginx -b    | Sedan boot             |
| journalctl --since "1h"   | Senaste timmen         |
+-----------------------------------------------------+""",
                        "pro_tip": "-f (follow) + -u (unit) = live debugging!",
                        "common_mistake": "Att leta i /var/log/ när journalctl har allt samlat."
                    },
                    {
                        "title": "Skapa egen Service",
                        "explanation": "Unit-filer i /etc/systemd/system/ definierar egna tjänster. Tre sektioner: [Unit], [Service], [Install].",
                        "diagram": """
+-----------------------------------------------------+
| SERVICE UNIT STRUKTUR                               |
+-----------------------------------------------------+
| [Unit]                                              |
| Description=My Application                          |
| After=network.target                               |
|                                                     |
| [Service]                                          |
| Type=simple                                        |
| User=myapp                                         |
| WorkingDirectory=/opt/myapp                        |
| ExecStart=/opt/myapp/run.sh                        |
| Restart=always                                     |
|                                                     |
| [Install]                                          |
| WantedBy=multi-user.target                         |
+-----------------------------------------------------+""",
                        "pro_tip": "Restart=always med RestartSec=5 ger automatisk recovery.",
                        "common_mistake": "Glömma 'systemctl daemon-reload' efter att ändra unit-filer."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Services",
            "content": {
                "exercises": [
                    {
                        "task": "Visa tjänststatus",
                        "instruction": "Kontrollera status för SSH-tjänsten",
                        "expected_command": "systemctl status sshd",
                        "hint": "Vissa system använder 'ssh' istället för 'sshd'"
                    },
                    {
                        "task": "Lista aktiva tjänster",
                        "instruction": "Visa alla körande tjänster",
                        "expected_command": "systemctl list-units --type=service --state=active",
                        "hint": "--type=service filtrerar på tjänster"
                    },
                    {
                        "task": "Se tjänstloggar",
                        "instruction": "Visa de senaste 30 lograderna för nginx",
                        "expected_command": "journalctl -u nginx -n 30",
                        "hint": "-u för unit, -n för antal rader"
                    },
                    {
                        "task": "Starta om tjänst",
                        "instruction": "Starta om nginx-tjänsten",
                        "expected_command": "sudo systemctl restart nginx",
                        "hint": "restart stoppar och startar i ett kommando"
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
                        {"front": "Skillnad mellan restart och reload?", "back": "restart stoppar och startar processen, reload läser om config utan avbrott"},
                        {"front": "Vad gör 'systemctl enable'?", "back": "Konfigurerar tjänsten att starta automatiskt vid boot"},
                        {"front": "Var ligger custom service-filer?", "back": "/etc/systemd/system/"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken journalctl-flagga följer loggar i realtid?",
                            "options": ["-f", "-l", "-r", "-n"],
                            "correct": 0,
                            "explanation": "-f (follow) visar nya loggar kontinuerligt, som tail -f"
                        },
                        {
                            "question": "Vad måste du köra efter att ändra en unit-fil?",
                            "options": ["systemctl reload", "systemctl restart", "systemctl daemon-reload", "service restart"],
                            "correct": 2,
                            "explanation": "daemon-reload läser om alla unit-filer så systemd ser ändringarna"
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
            "title": "Service Challenge",
            "content": {
                "scenario": "Skapa en egen systemd service som kör ett script och startar automatiskt.",
                "requirements": [
                    "Skapa ett script i /opt/myapp/",
                    "Skapa en service unit-fil",
                    "Konfigurera auto-restart vid krasch",
                    "Enable och starta tjänsten",
                    "Verifiera med status och journalctl"
                ],
                "hints": [
                    "Använd Type=simple för enkla scripts",
                    "Restart=always + RestartSec=5",
                    "Glöm inte daemon-reload"
                ],
                "solution": """# 1. Skapa app-katalog och script
sudo mkdir -p /opt/myapp
echo '#!/bin/bash
while true; do
    echo "Heartbeat: $(date)"
    sleep 10
done' | sudo tee /opt/myapp/heartbeat.sh
sudo chmod +x /opt/myapp/heartbeat.sh

# 2. Skapa service unit
cat << 'EOF' | sudo tee /etc/systemd/system/heartbeat.service
[Unit]
Description=Heartbeat Service
After=network.target

[Service]
Type=simple
ExecStart=/opt/myapp/heartbeat.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# 3. Ladda om systemd och starta
sudo systemctl daemon-reload
sudo systemctl enable --now heartbeat

# 4. Verifiera
systemctl status heartbeat
journalctl -u heartbeat -f

# Cleanup
sudo systemctl disable --now heartbeat
sudo rm /etc/systemd/system/heartbeat.service
sudo rm -rf /opt/myapp""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
