"""
Linux Mastery Node 18: Log Management & Analysis - V2 Interactive Format
"""

LINUX_NODE_18_LOGS_V2 = {
    "node_id": 18,
    "title": "Log Management & Analysis",
    "slug": "log-management",
    "description": "journalctl, syslog och logrotate",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Log Management",
            "content": {
                "headline": "Loggar är sanningen",
                "hook": "När något går fel är loggen ditt vittne. Utan logghantering flyger du blint. Lär dig hitta, analysera och rotera loggar effektivt.",
                "learning_objectives": [
                    "Använda journalctl för systemd-loggar",
                    "Hitta och analysera logfiler i /var/log/",
                    "Konfigurera logrotate för rotation",
                    "Felsöka med logganalys"
                ],
                "prerequisites": ["Basic terminal", "grep/awk basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Log Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "journalctl - Systemd Journal",
                        "explanation": "journalctl samlar ALLA systemd-loggar. Filtrera per tjänst (-u), tid (--since), prioritet (-p) eller följ live (-f).",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ JOURNALCTL KOMMANDON                                │
├─────────────────────────────────────────────────────┤
│ journalctl              │ Alla loggar              │
│ journalctl -f           │ Följ live (som tail -f)  │
│ journalctl -u nginx     │ Bara nginx               │
│ journalctl -u nginx -f  │ Följ nginx live          │
│ journalctl -n 100       │ Senaste 100 rader        │
│ journalctl -p err       │ Bara errors              │
│ journalctl -k           │ Kernel-meddelanden       │
├─────────────────────────────────────────────────────┤
│ TIDSFILTER:                                         │
│ --since "1 hour ago"    │ Senaste timmen           │
│ --since today           │ Sedan midnatt            │
│ --since "2024-01-01"    │ Sedan datum              │
│ --until "2024-01-02"    │ Till datum               │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "journalctl -u nginx -p err --since today = nginx-errors idag",
                        "common_mistake": "Att glömma att journalctl behöver sudo för att se alla loggar"
                    },
                    {
                        "title": "Viktiga Loggfiler",
                        "explanation": "/var/log/ innehåller systemloggar. Olika distros har olika filer - lär dig var dina loggar finns!",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ VIKTIGA LOGGFILER                                   │
├─────────────────────────────────────────────────────┤
│ UBUNTU/DEBIAN:                                      │
│ /var/log/syslog       │ Generell systemlogg        │
│ /var/log/auth.log     │ Inloggningar, sudo         │
│ /var/log/kern.log     │ Kernel-meddelanden         │
├─────────────────────────────────────────────────────┤
│ RHEL/CENTOS:                                        │
│ /var/log/messages     │ Generell systemlogg        │
│ /var/log/secure       │ Autentisering              │
├─────────────────────────────────────────────────────┤
│ APPLIKATIONER:                                      │
│ /var/log/nginx/       │ Nginx access/error         │
│ /var/log/apache2/     │ Apache loggar              │
│ /var/log/mysql/       │ MySQL/MariaDB              │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "tail -f /var/log/nginx/error.log för live web-debugging",
                        "common_mistake": "Att inte kolla auth.log vid misstänkt intrång - där syns allt!"
                    },
                    {
                        "title": "Logrotate",
                        "explanation": "logrotate förhindrar att disken blir full. Konfigurerar rotation, komprimering och retention per logg.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ LOGROTATE CONFIG EXEMPEL                            │
│ /etc/logrotate.d/nginx                              │
├─────────────────────────────────────────────────────┤
│ /var/log/nginx/*.log {                              │
│     daily              # Rotera dagligen           │
│     rotate 14          # Behåll 14 filer           │
│     compress           # Komprimera gamla          │
│     delaycompress      # Vänta en cykel            │
│     missingok          # OK om fil saknas          │
│     notifempty         # Skippa tomma              │
│     create 0640 www-data adm                       │
│     postrotate                                      │
│         systemctl reload nginx > /dev/null 2>&1    │
│     endscript                                       │
│ }                                                   │
├─────────────────────────────────────────────────────┤
│ TEST: sudo logrotate -d /etc/logrotate.conf        │
│ FORCE: sudo logrotate -f /etc/logrotate.d/nginx    │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "logrotate -d (debug) visar vad som SKULLE hända utan att göra det",
                        "common_mistake": "Att glömma postrotate-scriptet - nginx behöver reload för att börja skriva till ny fil"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Logs",
            "content": {
                "exercises": [
                    {
                        "task": "Visa systemloggar",
                        "instruction": "Visa de senaste 50 loggraderna från systemd journal",
                        "expected_command": "journalctl -n 50",
                        "hint": "-n anger antal rader"
                    },
                    {
                        "task": "Filtrera på tjänst",
                        "instruction": "Visa loggar för SSH-tjänsten senaste timmen",
                        "expected_command": "journalctl -u sshd --since '1 hour ago'",
                        "hint": "-u för unit/tjänst"
                    },
                    {
                        "task": "Hitta errors",
                        "instruction": "Visa bara error-meddelanden sedan idag",
                        "expected_command": "journalctl -p err --since today",
                        "hint": "-p err filtrerar på prioritet error"
                    },
                    {
                        "task": "Analysera access log",
                        "instruction": "Räkna antal requests per IP i nginx access log",
                        "expected_command": "awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head",
                        "hint": "$1 är första fältet (IP), uniq -c räknar"
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
                        {"front": "Hur följer du loggar live med journalctl?", "back": "journalctl -f (follow)"},
                        {"front": "Var hittar du misslyckade SSH-inloggningar på Ubuntu?", "back": "/var/log/auth.log"},
                        {"front": "Vad gör logrotate?", "back": "Roterar, komprimerar och raderar gamla loggfiler automatiskt"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Hur visar du bara errors för nginx senaste timmen?",
                            "options": [
                                "journalctl nginx errors",
                                "journalctl -u nginx -p err --since '1 hour ago'",
                                "tail -f /var/log/nginx/error.log | grep error",
                                "syslog -u nginx -p error"
                            ],
                            "correct": 1,
                            "explanation": "-u=unit, -p=priority, --since för tidsfilter"
                        },
                        {
                            "question": "Vad betyder 'rotate 7' i logrotate config?",
                            "options": [
                                "Rotera var 7:e dag",
                                "Behåll 7 roterade filer",
                                "Komprimera efter 7 dagar",
                                "Max 7MB per fil"
                            ],
                            "correct": 1,
                            "explanation": "rotate N = behåll N gamla versioner av loggen"
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
            "title": "Log Challenge",
            "content": {
                "scenario": "Servern har problem. Använd loggar för att diagnostisera och analysera.",
                "requirements": [
                    "Hitta alla errors från senaste 24 timmarna",
                    "Identifiera misslyckade SSH-inloggningsförsök",
                    "Hitta top 10 IP-adresser i nginx access log",
                    "Kontrollera kernel-meddelanden för hårdvarufel"
                ],
                "hints": [
                    "journalctl --since för tidsfilter",
                    "grep 'Failed password' i auth.log",
                    "awk + sort + uniq för statistik"
                ],
                "solution": """# 1. Alla errors senaste 24h
journalctl -p err --since "24 hours ago"

# 2. Misslyckade SSH-försök
# Ubuntu/Debian:
grep "Failed password" /var/log/auth.log | tail -20

# Med journalctl:
journalctl -u sshd | grep -i "failed"

# Räkna per IP:
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head

# 3. Top 10 IP i nginx
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10

# 4. Kernel-meddelanden (hårdvarufel)
journalctl -k -p warning
# eller
dmesg -T -l err,warn

# 5. Bonus: Skapa en snabb rapport
echo "=== ERROR SUMMARY ===" > /tmp/error_report.txt
echo "Errors last 24h:" >> /tmp/error_report.txt
journalctl -p err --since "24 hours ago" --no-pager | wc -l >> /tmp/error_report.txt
echo "" >> /tmp/error_report.txt
echo "Failed SSH attempts:" >> /tmp/error_report.txt
grep -c "Failed password" /var/log/auth.log >> /tmp/error_report.txt
cat /tmp/error_report.txt""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
