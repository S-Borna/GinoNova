"""
Linux Mastery Node 1: Process Management - V2 Interactive Format
"""

LINUX_NODE_1_PROCESS_V2 = {
    "node_id": 1,
    "title": "Process Management Mastery",
    "slug": "process-management",
    "description": "Hantera, övervaka och kontrollera Linux-processer",
    "difficulty": "intermediate",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Process Management",
            "content": {
                "headline": "Bli processernas herre",
                "hook": "En runaway process kan krasha din server. En zombie kan fylla process table. Du behöver veta exakt hur du identifierar och hanterar alla typer av processer.",
                "learning_objectives": [
                    "Förstå processer, PID, states och signaler",
                    "Använda ps, top och htop för monitoring",
                    "Hantera processer med kill, nice och bg/fg",
                    "Felsöka zombie och runaway processer"
                ],
                "prerequisites": ["Linux basics", "Terminal användning"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Process Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "Process States",
                        "explanation": "R (Running), S (Sleeping), D (Disk sleep - kan EJ dödas), Z (Zombie - avslutad men ej städad), T (Stopped/pausad).",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ PROCESS STATES                              │
├─────────────────────────────────────────────┤
│ R - Running     │ Kör på CPU               │
│ S - Sleeping    │ Väntar på I/O            │
│ D - Disk Sleep  │ Uninterruptible (farlig!) │
│ Z - Zombie      │ Död men ej städad        │
│ T - Stopped     │ Pausad (Ctrl+Z)          │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "D-state processer kan INTE dödas med kill -9. De väntar på hardware.",
                        "common_mistake": "Att köra kill -9 direkt istället för SIGTERM först."
                    },
                    {
                        "title": "Signaler",
                        "explanation": "SIGTERM (15) = snäll avslutning, SIGKILL (9) = tvingad död, SIGHUP (1) = reload config, SIGINT (2) = Ctrl+C.",
                        "diagram": """
┌─────────────────────────────────────────────┐
│ SIGNAL   │ NR  │ ANVÄNDNING               │
├─────────────────────────────────────────────┤
│ SIGTERM  │ 15  │ Snäll avslutning (default)│
│ SIGKILL  │  9  │ Tvingad död (sista utväg) │
│ SIGHUP   │  1  │ Reload config             │
│ SIGSTOP  │ 19  │ Pausa process             │
│ SIGCONT  │ 18  │ Fortsätt pausad           │
└─────────────────────────────────────────────┘""",
                        "pro_tip": "Alltid SIGTERM först, vänta, sen SIGKILL om nödvändigt.",
                        "common_mistake": "Kill -9 städar inte upp - temporärfiler kan bli korrupta."
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Process Management",
            "content": {
                "exercises": [
                    {
                        "task": "Lista processer sorterat på CPU",
                        "instruction": "Visa top 10 CPU-hungriga processer",
                        "expected_command": "ps aux --sort=-%cpu | head -10",
                        "hint": "--sort=-%cpu sorterar fallande på CPU"
                    },
                    {
                        "task": "Hitta specifik process",
                        "instruction": "Sök efter alla nginx-processer",
                        "expected_command": "ps aux | grep nginx",
                        "hint": "grep filtrerar output"
                    },
                    {
                        "task": "Döda process snällt",
                        "instruction": "Skicka SIGTERM till PID 1234",
                        "expected_command": "kill 1234",
                        "hint": "kill utan signal = SIGTERM (15)"
                    },
                    {
                        "task": "Starta bakgrundsprocess",
                        "instruction": "Kör script.sh i bakgrunden så det överlever logout",
                        "expected_command": "nohup ./script.sh &",
                        "hint": "nohup ignorerar SIGHUP, & kör i bakgrund"
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
                        {"front": "Vad betyder process state 'Z'?", "back": "Zombie - processen har avslutats men parent har inte städat upp (wait())"},
                        {"front": "Vilken signal skickar kill utan argument?", "back": "SIGTERM (15) - snäll avslutning"},
                        {"front": "Hur kör du ett kommando i bakgrunden?", "back": "Lägg till & i slutet, t.ex. ./script.sh &"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vilken signal kan INTE fångas eller ignoreras?",
                            "options": ["SIGTERM", "SIGKILL", "SIGHUP", "SIGINT"],
                            "correct": 1,
                            "explanation": "SIGKILL (9) kan inte fångas - processen dör omedelbart"
                        },
                        {
                            "question": "Vad gör nice -n 10 ./script.sh?",
                            "options": ["Högre prioritet", "Lägre prioritet", "Samma prioritet", "Stoppar scriptet"],
                            "correct": 1,
                            "explanation": "Positivt nice-värde = lägre prioritet (snällare mot andra)"
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
            "title": "Process Challenge",
            "content": {
                "scenario": "Produktionsservern har hög CPU-load. Hitta och åtgärda problemet.",
                "requirements": [
                    "Identifiera processen som äter mest CPU",
                    "Undersök vad processen gör",
                    "Försök graceful shutdown först",
                    "Forcera avslutning om nödvändigt"
                ],
                "hints": [
                    "ps aux --sort=-%cpu eller top",
                    "cat /proc/PID/cmdline för full command",
                    "kill PID innan kill -9 PID"
                ],
                "solution": """# 1. Identifiera CPU-hungrig process
ps aux --sort=-%cpu | head -5
# eller
top -bn1 | head -15

# 2. Undersök processen (anta PID 5678)
cat /proc/5678/cmdline
ls -la /proc/5678/fd  # öppna filer

# 3. Graceful shutdown först
kill 5678
sleep 5

# 4. Verifiera
ps -p 5678

# 5. Om fortfarande lever, force kill
kill -9 5678""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
