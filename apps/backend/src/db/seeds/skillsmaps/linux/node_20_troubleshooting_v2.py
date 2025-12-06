"""
Linux Mastery Node 20: Linux Troubleshooting - V2 Interactive Format
"""

LINUX_NODE_20_TROUBLESHOOTING_V2 = {
    "node_id": 20,
    "title": "Linux Troubleshooting",
    "slug": "troubleshooting",
    "description": "Systematisk felsökning av Linux-problem",
    "difficulty": "advanced",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Linux Troubleshooting",
            "content": {
                "headline": "Production går ner. Du har 5 minuter.",
                "hook": "Panik hjälper inte - systematisk felsökning gör det. Lär dig den metodiska approachen och verktygslådan som räddar dig när allt brinner.",
                "learning_objectives": [
                    "Använda systematisk troubleshooting-approach",
                    "Diagnostisera vanliga problem (disk, minne, nätverk)",
                    "Använda strace, lsof och tcpdump",
                    "Återhämta från boot-problem"
                ],
                "prerequisites": ["All previous Linux nodes"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Troubleshooting Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Systematisk Approach",
                        "explanation": "Följ alltid samma mönster: IDENTIFY → REPRODUCE → ISOLATE → ANALYZE → FIX → VERIFY → DOCUMENT.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ TROUBLESHOOTING FLOW                                │
├─────────────────────────────────────────────────────┤
│ 1. IDENTIFY    │ Vad är symptomen exakt?           │
│ 2. REPRODUCE   │ Kan du återskapa problemet?       │
│ 3. ISOLATE     │ Var är problemet? (CPU/RAM/disk?) │
│ 4. ANALYZE     │ Varför händer det?                │
│ 5. FIX         │ Åtgärda rotorsaken               │
│ 6. VERIFY      │ Bekräfta att det är fixat         │
│ 7. DOCUMENT    │ Skriv ner för framtiden           │
├─────────────────────────────────────────────────────┤
│ FÖRSTA KOMMANDONA VID INCIDENT:                     │
│ uptime          │ Load average                     │
│ df -h           │ Diskutrymme                       │
│ free -h         │ Minne                             │
│ journalctl -xe  │ Senaste loggar                   │
│ systemctl status│ Tjänsternas status               │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "Dokumentera ALLTID - nästa gång kan samma problem lösas på sekunder!",
                        "common_mistake": "Att börja gissa istället för att samla data systematiskt"
                    },
                    {
                        "title": "Vanliga Problem & Lösningar",
                        "explanation": "De flesta incidenter är disk full, out of memory, eller nätverksproblem. Lär dig dessa utantill.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ PROBLEM → DIAGNOS → LÖSNING                         │
├─────────────────────────────────────────────────────┤
│ DISK FULL:                                          │
│ df -h                 │ Hitta fullt filsystem       │
│ du -sh /* | sort -rh  │ Hitta vad som tar plats     │
│ journalctl --vacuum-size=500M │ Rensa journalloggar│
├─────────────────────────────────────────────────────┤
│ OUT OF MEMORY:                                      │
│ free -h              │ Kolla RAM/swap               │
│ dmesg | grep -i oom  │ Hitta OOM-killed processer   │
│ ps --sort=-%mem      │ Hitta minnesslukare          │
├─────────────────────────────────────────────────────┤
│ CAN'T CONNECT:                                      │
│ systemctl status     │ Kör tjänsten?                │
│ ss -tlnp | grep :80  │ Lyssnar på porten?           │
│ ufw status           │ Firewall blockerar?          │
│ dig domain.com       │ DNS fungerar?                │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "'Cannot allocate memory' i loggar = OOM killer har slagit till",
                        "common_mistake": "Att starta om tjänsten utan att förstå varför den dog"
                    },
                    {
                        "title": "Kraftfulla Debug-verktyg",
                        "explanation": "strace spårar systemanrop, lsof visar öppna filer, tcpdump fångar nätverkstrafik.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ DEBUG TOOLS                                         │
├─────────────────────────────────────────────────────┤
│ STRACE - Vad gör processen?                         │
│ strace -p <PID>              │ Spåra körande process│
│ strace -f ./script.sh        │ Spåra inkl. barn     │
│ strace -e open,read ./app    │ Bara vissa anrop     │
├─────────────────────────────────────────────────────┤
│ LSOF - Öppna filer & sockets                        │
│ lsof -p <PID>      │ Allt processen har öppet      │
│ lsof -i :80        │ Vem använder port 80?         │
│ lsof +L1           │ Raderade men öppna filer      │
├─────────────────────────────────────────────────────┤
│ TCPDUMP - Nätverkstrafik                            │
│ tcpdump -i eth0 port 443                            │
│ tcpdump -i any host 10.0.0.5                        │
│ tcpdump -w capture.pcap      │ Spara till fil      │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "lsof +L1 hittar raderade filer som fortfarande tar diskutrymme!",
                        "common_mistake": "Att inte använda -f med strace när processen forkar"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Troubleshooting",
            "content": {
                "exercises": [
                    {
                        "task": "Quick system check",
                        "instruction": "Visa load, disk och minne i ett svep",
                        "expected_command": "uptime && df -h / && free -h",
                        "hint": "&& kör nästa om föregående lyckas"
                    },
                    {
                        "task": "Hitta vad som lyssnar",
                        "instruction": "Visa vilken process som lyssnar på port 22",
                        "expected_command": "sudo lsof -i :22",
                        "hint": "lsof -i :port visar processer på den porten"
                    },
                    {
                        "task": "Spåra process",
                        "instruction": "Visa systemanrop som process med PID 1234 gör",
                        "expected_command": "sudo strace -p 1234",
                        "hint": "-p för att attacha till körande process"
                    },
                    {
                        "task": "Hitta minnesslukare",
                        "instruction": "Lista top 5 processer sorterade på minnesanvändning",
                        "expected_command": "ps aux --sort=-%mem | head -6",
                        "hint": "--sort=-%mem, head -6 för header + 5 processer"
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
                        {"front": "Vad gör 'lsof +L1'?", "back": "Visar raderade filer som fortfarande är öppna (tar diskutrymme!)"},
                        {"front": "Vad betyder OOM i dmesg?", "back": "Out Of Memory - kernel har dödat processer för att rädda systemet"},
                        {"front": "Första kommandot vid incident?", "back": "uptime/df -h/free -h/journalctl -xe för snabb översikt"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Disken visar full men du har tagit bort stora filer. Varför?",
                            "options": [
                                "Du måste reboota",
                                "Filsystemet är korrupt",
                                "Processer har fortfarande filerna öppna",
                                "Disk-cache behöver tömmas"
                            ],
                            "correct": 2,
                            "explanation": "Raderade filer frigörs inte förrän alla processer stänger dem. lsof +L1 hittar dem!"
                        },
                        {
                            "question": "Hur boota till single user mode från GRUB?",
                            "options": [
                                "Tryck S vid boot",
                                "Redigera kernel-raden och lägg till 'single' eller '1'",
                                "Kör 'systemctl single' innan reboot",
                                "Håll ner Shift"
                            ],
                            "correct": 1,
                            "explanation": "I GRUB, tryck 'e' för att redigera, lägg till 'single' på linux-raden, boot med Ctrl+X"
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
            "title": "Troubleshooting Challenge",
            "content": {
                "scenario": "Webbservern svarar inte. Diagnostisera och åtgärda systematiskt.",
                "requirements": [
                    "Kontrollera att nginx-tjänsten körs",
                    "Verifiera att den lyssnar på rätt port",
                    "Kolla loggar för fel",
                    "Kontrollera firewall och DNS",
                    "Testa anslutning steg för steg"
                ],
                "hints": [
                    "systemctl status nginx",
                    "ss -tlnp | grep :80",
                    "journalctl -u nginx -n 50"
                ],
                "solution": """#!/bin/bash
# Incident Response: Web server down

echo "=== 1. SERVICE STATUS ==="
systemctl status nginx
# Om inactive/failed → journalctl -u nginx för detaljer

echo "=== 2. PORT LISTENING ==="
ss -tlnp | grep -E ':80|:443'
# Om inget → nginx lyssnar inte, kolla config

echo "=== 3. RECENT LOGS ==="
journalctl -u nginx -n 50 --no-pager
# Leta efter error-meddelanden

echo "=== 4. DISK SPACE ==="
df -h /var/log /var/www
# Om fullt → nginx kan inte skriva logs

echo "=== 5. FIREWALL ==="
sudo ufw status | grep -E '80|443'
# Om inte ALLOW → öppna porten

echo "=== 6. DNS CHECK ==="
dig +short mysite.com
# Om fel IP → DNS-problem

echo "=== 7. LOCAL TEST ==="
curl -I localhost
# 200 OK = nginx funkar lokalt

echo "=== 8. EXTERNAL TEST ==="
curl -I http://mysite.com
# Om timeout men lokal funkar → firewall/routing

# VANLIGA LÖSNINGAR:
# Service död:     sudo systemctl restart nginx
# Port occupied:   lsof -i :80 → döda processen
# Disk full:       journalctl --vacuum-size=500M
# Firewall:        sudo ufw allow 80
# Config error:    nginx -t → fixa config

echo "=== 9. RESTART & VERIFY ==="
sudo nginx -t                    # Testa config
sudo systemctl restart nginx     # Starta om
curl -I localhost               # Verifiera""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
