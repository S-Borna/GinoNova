"""
Linux Mastery Node 19: Performance Monitoring - V2 Interactive Format
"""

LINUX_NODE_19_PERFORMANCE_V2 = {
    "node_id": 19,
    "title": "Performance Monitoring",
    "slug": "performance-monitoring",
    "description": "Övervaka CPU, minne, disk och nätverk",
    "difficulty": "advanced",
    "estimated_minutes": 35,
    "xp_reward": 100,
    "sections": [
        {
            "section_id": "intro",
            "type": "intro",
            "title": "Performance Monitoring",
            "content": {
                "headline": "Performance är UX",
                "hook": "En långsam server är en dålig server. Du måste kunna identifiera flaskhalsar - CPU, minne, disk, nätverk. Lär dig se var systemet lider.",
                "learning_objectives": [
                    "Övervaka CPU med top/htop och mpstat",
                    "Analysera minnesanvändning med free och vmstat",
                    "Mäta disk I/O med iostat och iotop",
                    "Identifiera och lösa flaskhalsar"
                ],
                "prerequisites": ["Process management", "Basic system administration"],
                "estimated_time": "2 min",
                "xp_reward": 10
            }
        },
        {
            "section_id": "concepts",
            "type": "concepts",
            "title": "Monitoring Koncept",
            "content": {
                "concepts": [
                    {
                        "title": "top/htop - Process Overview",
                        "explanation": "top visar processer sorterade efter CPU/minne. htop är bättre med färger och mus-stöd. Load average < CPU-kärnor = OK.",
                        "diagram": """
+-----------------------------------------------------+
| LOAD AVERAGE TOLKNING                               |
+-----------------------------------------------------+
| $ uptime                                            |
| load average: 0.52, 0.58, 0.59                     |
|               1min  5min  15min                    |
+-----------------------------------------------------+
| TUMREGEL (för 4-kärnig server):                    |
| < 4.0  | OK, systemet har kapacitet                |
| = 4.0  | 100% belastat, ingen marginal             |
| > 4.0  | Överbelastat, processer köar              |
+-----------------------------------------------------+
| TOP SHORTCUTS:                                      |
| P | Sortera på CPU                                 |
| M | Sortera på minne                               |
| k | Döda process (ange PID)                        |
| q | Avsluta                                        |
+-----------------------------------------------------+""",
                        "pro_tip": "Installera htop - mycket bättre interface än top!",
                        "common_mistake": "Att jämföra load average utan att veta antal CPU-kärnor"
                    },
                    {
                        "title": "free & vmstat - Minnesanalys",
                        "explanation": "free visar minnesanvändning. VIKTIGT: titta på 'available', inte 'free' - buff/cache kan frigöras.",
                        "diagram": """
+-----------------------------------------------------+
| FREE OUTPUT                                         |
+-----------------------------------------------------+
| $ free -h                                           |
|             total   used   free   shared buff/cache |
| Mem:         16G    8.2G   1.2G   512M     5.8G    |
| Swap:         4G      0G     4G                    |
|                                                     |
| available: 6.5G  <- DENNA är viktig!                |
+-----------------------------------------------------+
| buff/cache = används för disk-cache, kan frigöras  |
| available = vad som faktiskt kan användas          |
| swap used > 0 = systemet har ont om RAM            |
+-----------------------------------------------------+
| VMSTAT:                                             |
| vmstat 2    # Snapshot var 2:a sekund              |
| si/so > 0   # Swap in/out = RAM-problem            |
+-----------------------------------------------------+""",
                        "pro_tip": "Om swap används konstant - lägg till mer RAM!",
                        "common_mistake": "Att panika över lågt 'free' - Linux använder RAM som disk-cache"
                    },
                    {
                        "title": "iostat & iotop - Disk I/O",
                        "explanation": "iostat visar disk-statistik. await > 20ms = disken är flaskhals. %util > 80% = disken är mättad.",
                        "diagram": """
+-----------------------------------------------------+
| IOSTAT OUTPUT                                       |
+-----------------------------------------------------+
| $ iostat -xz 1                                      |
| Device  r/s    w/s   rkB/s  wkB/s await  %util     |
| sda    10.5   45.2   420    1808   8.5   25.3     |
+-----------------------------------------------------+
| KOLUMNER:                                           |
| r/s, w/s    | Reads/writes per sekund              |
| rkB/s, wkB/s| KB lästa/skrivna per sekund          |
| await       | Genomsnittlig väntetid (ms)          |
| %util       | Disk-användning i procent            |
+-----------------------------------------------------+
| VARNING:                                            |
| await > 20ms  | Disken är långsam                  |
| %util > 80%   | Disken är mättad                   |
+-----------------------------------------------------+""",
                        "pro_tip": "iotop -o visar vilka processer som gör disk I/O just nu",
                        "common_mistake": "Att ignorera iowait i top - hög iowait = disk-problem, inte CPU"
                    }
                ],
                "estimated_time": "8 min",
                "xp_reward": 15
            }
        },
        {
            "section_id": "practice",
            "type": "practice",
            "title": "Hands-on Performance",
            "content": {
                "exercises": [
                    {
                        "task": "Kolla load average",
                        "instruction": "Visa systemets uptime och load average",
                        "expected_command": "uptime",
                        "hint": "Load average visar 1, 5 och 15 minuters medelvärde"
                    },
                    {
                        "task": "Visa minnesanvändning",
                        "instruction": "Visa RAM och swap-användning i human-readable format",
                        "expected_command": "free -h",
                        "hint": "-h ger GB/MB istället för bytes"
                    },
                    {
                        "task": "Hitta minnesslukare",
                        "instruction": "Lista de 10 processer som använder mest minne",
                        "expected_command": "ps aux --sort=-%mem | head -10",
                        "hint": "--sort=-%mem sorterar på minne, fallande"
                    },
                    {
                        "task": "Övervaka disk I/O",
                        "instruction": "Visa disk I/O statistik med uppdatering varje sekund",
                        "expected_command": "iostat -xz 1",
                        "hint": "-x för extended, -z ignorerar inaktiva diskar"
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
                        {"front": "Vad betyder load average 4.0 på en 2-kärnig server?", "back": "Överbelastat! Dubbelt så många processer väntar som CPUn kan hantera"},
                        {"front": "Varför visar 'free' att nästan allt RAM är använt?", "back": "Linux använder ledigt RAM som disk-cache (buff/cache) - det frigörs vid behov"},
                        {"front": "Vad indikerar hög 'await' i iostat?", "back": "Disken är långsam eller överbelastad - processer väntar på I/O"}
                    ],
                    "multiple_choice": [
                        {
                            "question": "Vad bör du titta på i 'free -h' för att se tillgängligt minne?",
                            "options": ["free-kolumnen", "used-kolumnen", "available-kolumnen", "buff/cache-kolumnen"],
                            "correct": 2,
                            "explanation": "available visar vad som faktiskt kan användas (free + reclaimable cache)"
                        },
                        {
                            "question": "Vad betyder 'wa' (wait) i top/mpstat?",
                            "options": [
                                "CPU väntar på användarinput",
                                "CPU väntar på disk I/O",
                                "CPU väntar på nätverk",
                                "CPU väntar på minne"
                            ],
                            "correct": 1,
                            "explanation": "wa/iowait = procent av tid CPU väntar på disk I/O att slutföra"
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
            "title": "Performance Challenge",
            "content": {
                "scenario": "Servern är långsam. Diagnostisera var flaskhalsen är - CPU, minne eller disk.",
                "requirements": [
                    "Kolla system load och antal CPU-kärnor",
                    "Analysera minnesanvändning och swap",
                    "Kontrollera disk I/O och await-tider",
                    "Identifiera de största resursslukarna"
                ],
                "hints": [
                    "uptime för load, nproc för kärnor",
                    "free -h och vmstat för minne",
                    "iostat -xz 1 för disk",
                    "ps aux --sort=-cpu eller --sort=-%mem"
                ],
                "solution": """# 1. System overview
uptime
# load average: 8.5, 7.2, 6.8
# Om > antal kärnor -> överbelastat

nproc
# 4 (antal CPU-kärnor)
# Load 8.5 på 4 kärnor = kraftigt överbelastat!

# 2. CPU-analys
mpstat -P ALL 1 3
# Kolla %idle per kärna
# Låg idle = CPU-bunden

# 3. Minne
free -h
# Kolla 'available' och 'swap used'
# Swap > 0 konstant = RAM-problem

vmstat 1 5
# si/so > 0 = aktivt swappande (dåligt)

# 4. Disk I/O
iostat -xz 1 3
# await > 20ms = disk är flaskhals
# %util > 80% = disk mättad

# 5. Topp CPU-slukare
ps aux --sort=-%cpu | head -10

# 6. Topp minnesslukare
ps aux --sort=-%mem | head -10

# 7. Disk I/O per process
sudo iotop -o

# DIAGNOS:
# - Hög load + låg CPU idle = CPU-bunden -> skala horisontellt
# - Hög swap usage = RAM-brist -> lägg till minne
# - Hög await/util = disk-bunden -> snabbare disk (SSD)
# - Hög iowait i top = applikation gör för mycket disk I/O""",
                "estimated_time": "10 min",
                "xp_reward": 20
            }
        }
    ]
}
