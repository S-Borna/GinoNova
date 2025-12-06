"""
Linux Mastery Node 17: Cron & Scheduling - V2 Interactive Format
"""

LINUX_NODE_17_CRON_V2 = {
    "node_id": 17,
    "title": "Cron & Scheduling",
    "slug": "cron-scheduling",
    "description": "Automatisera uppgifter med cron och systemd timers",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Cron & Scheduling",
            "content": {
                "headline": "Automation utan scheduling är manuellt arbete",
                "hook": "Backups kl 03:00, logrotation varje vecka, health checks var 5:e minut. Cron är DevOps-hjärtat - det som får automation att faktiskt köras.",
                "learning_objectives": [
                    "Förstå crontab-syntaxen (* * * * *)",
                    "Skapa och hantera schemalagda jobb",
                    "Använda system cron-kataloger",
                    "Felsöka cron-jobb som inte körs"
                ],
                "prerequisites": ["Bash scripting basics"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Cron Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Crontab Syntax",
                        "explanation": "Fem fält: minut, timme, dag-i-månad, månad, veckodag. * betyder 'alla'. */5 betyder 'var 5:e'.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ CRONTAB SYNTAX                                      │
├─────────────────────────────────────────────────────┤
│ ┌───────────── minut (0-59)                        │
│ │ ┌───────────── timme (0-23)                      │
│ │ │ ┌───────────── dag i månad (1-31)              │
│ │ │ │ ┌───────────── månad (1-12)                  │
│ │ │ │ │ ┌───────────── veckodag (0-6, 0=söndag)    │
│ │ │ │ │ │                                          │
│ * * * * * kommando                                 │
├─────────────────────────────────────────────────────┤
│ EXEMPEL:                                            │
│ * * * * *     │ Varje minut                        │
│ 0 * * * *     │ Varje timme (vid :00)              │
│ 0 3 * * *     │ Kl 03:00 dagligen                  │
│ */5 * * * *   │ Var 5:e minut                      │
│ 0 0 * * 0     │ Varje söndag midnatt               │
│ 0 9 * * 1-5   │ Kl 09:00 måndag-fredag             │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "Använd crontab.guru för att verifiera dina uttryck!",
                        "common_mistake": "Glömma att paths i cron ofta kräver full sökväg (/usr/bin/python, inte python)"
                    },
                    {
                        "title": "Hantera Crontab",
                        "explanation": "crontab -e för att redigera, -l för att lista, -r för att ta bort. Varje användare har sin egen crontab.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ CRONTAB KOMMANDON                                   │
├─────────────────────────────────────────────────────┤
│ crontab -e         │ Redigera din crontab          │
│ crontab -l         │ Lista dina jobb               │
│ crontab -r         │ Ta bort alla jobb             │
│ sudo crontab -u nginx -e │ Annan användares crontab│
├─────────────────────────────────────────────────────┤
│ SPECIAL SYNTAX:                                     │
│ @reboot     │ Kör vid systemstart                  │
│ @hourly     │ Kör varje timme (0 * * * *)          │
│ @daily      │ Kör dagligen (0 0 * * *)             │
│ @weekly     │ Kör varje vecka (0 0 * * 0)          │
│ @monthly    │ Kör varje månad (0 0 1 * *)          │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "@reboot är perfekt för att starta services som inte är systemd-hanterade",
                        "common_mistake": "Att glömma omdirigera output - cron mailar annars allt till användaren"
                    },
                    {
                        "title": "Output & Debugging",
                        "explanation": "Cron-jobb körs utan terminal - de har ingen PATH eller miljövariabler. Logga alltid output för debugging.",
                        "diagram": """
┌─────────────────────────────────────────────────────┐
│ CRON OUTPUT & DEBUGGING                             │
├─────────────────────────────────────────────────────┤
│ # Logga output till fil                             │
│ 0 3 * * * /backup.sh >> /var/log/backup.log 2>&1   │
│                                                     │
│ # Tysta (ingen output)                              │
│ 0 3 * * * /backup.sh > /dev/null 2>&1              │
│                                                     │
│ # Sätt PATH i crontab                               │
│ PATH=/usr/local/bin:/usr/bin:/bin                  │
│ 0 3 * * * backup.sh                                │
├─────────────────────────────────────────────────────┤
│ DEBUG TIPS:                                         │
│ - Kolla /var/log/cron eller journalctl             │
│ - Testa scriptet manuellt först                    │
│ - Använd fulla sökvägar                            │
│ - Sätt MAILTO=email för felmeddelanden             │
└─────────────────────────────────────────────────────┘""",
                        "pro_tip": "2>&1 slår ihop stderr och stdout så du fångar alla meddelanden",
                        "common_mistake": "Scripts som funkar manuellt men inte i cron - ofta PATH-problem!"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Cron",
            "content": {
                "exercises": [
                    {
                        "task": "Lista dina cron-jobb",
                        "instruction": "Visa alla schemalagda jobb för din användare",
                        "expected_command": "crontab -l",
                        "hint": "-l för list"
                    },
                    {
                        "task": "Daglig backup kl 03:00",
                        "instruction": "Skriv cron-uttrycket för att köra /scripts/backup.sh kl 03:00 varje dag",
                        "expected_command": "0 3 * * * /scripts/backup.sh",
                        "hint": "minut=0, timme=3, resten wildcard"
                    },
                    {
                        "task": "Var 5:e minut",
                        "instruction": "Skriv cron-uttrycket för att köra healthcheck.sh var 5:e minut",
                        "expected_command": "*/5 * * * * /scripts/healthcheck.sh",
                        "hint": "*/5 betyder 'delbart med 5'"
                    },
                    {
                        "task": "Måndagar kl 09:00",
                        "instruction": "Skriv cron-uttrycket för weekly-report.sh varje måndag kl 09:00",
                        "expected_command": "0 9 * * 1 /scripts/weekly-report.sh",
                        "hint": "veckodag 1=måndag"
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
                        {"front": "Vad betyder '*/15 * * * *'?", "back": "Kör var 15:e minut (00, 15, 30, 45)"},
                        {"front": "Vad gör @reboot?", "back": "Kör kommandot en gång vid systemstart"},
                        {"front": "Varför fungerar inte mitt script i cron?", "back": "Troligen PATH-problem - använd fulla sökvägar"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad kör '0 0 1 * *'?",
                            "options": [
                                "Varje dag vid midnatt",
                                "Första dagen i varje månad vid midnatt",
                                "Varje timme den första",
                                "En gång om året"
                            ],
                            "correct": 1,
                            "explanation": "minut=0, timme=0, dag=1, månad=alla - första i varje månad vid 00:00"
                        },
                        {
                            "question": "Hur loggar du både stdout och stderr från ett cron-jobb?",
                            "options": [
                                "> log.txt",
                                ">> log.txt 2>&1",
                                "| tee log.txt",
                                "&> log.txt"
                            ],
                            "correct": 1,
                            "explanation": ">> appendar, 2>&1 slår ihop stderr (2) med stdout (1)"
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
            "title": "Cron Challenge",
            "content": {
                "scenario": "Sätt upp automatiserade underhållsjobb för en webbserver.",
                "requirements": [
                    "Daglig backup kl 02:00 med loggning",
                    "Rensa /tmp var 6:e timme",
                    "Veckovis säkerhetsuppdatering söndagar kl 04:00",
                    "Healthcheck var 5:e minut med notifiering vid fel"
                ],
                "hints": [
                    "Använd >> för att logga",
                    "2>&1 fångar errors",
                    "mail -s för notifiering"
                ],
                "solution": """# Öppna crontab
crontab -e

# Lägg till följande jobb:

# PATH för att hitta kommandon
PATH=/usr/local/bin:/usr/bin:/bin

# Daglig backup kl 02:00 med loggning
0 2 * * * /scripts/backup.sh >> /var/log/backup.log 2>&1

# Rensa /tmp var 6:e timme (00:00, 06:00, 12:00, 18:00)
0 */6 * * * find /tmp -type f -mtime +1 -delete >> /var/log/cleanup.log 2>&1

# Veckovis säkerhetsuppdatering söndagar kl 04:00
0 4 * * 0 apt update && apt upgrade -y >> /var/log/updates.log 2>&1

# Healthcheck var 5:e minut - maila vid fel
*/5 * * * * /scripts/healthcheck.sh || echo "Health check failed!" | mail -s "ALERT: Server down" admin@example.com

# ---- healthcheck.sh exempel ----
#!/bin/bash
# /scripts/healthcheck.sh
curl -sf http://localhost/ > /dev/null || exit 1
systemctl is-active --quiet nginx || exit 1
exit 0

# Verifiera att jobben är tillagda
crontab -l""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
