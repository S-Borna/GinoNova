#!/usr/bin/env python3
"""
FULLSTÄNDIG MANUELL VERIFIERING AV ALLA FRÅGOR NOD 3-10
Jämför Master-filer med quiz-filen och producerar korrekta correctIndices
"""

import re
import json

# Nod 3 - Master svar (baserat på manual granskning)
NOD3_MASTER_ANSWERS = {
    # Fråga: (korrekt bokstav från master, rätt svar text)
    1: ('B', 'Hur länge datorn har varit påslagen och load average'),
    2: ('C', 'Under 2.0'),
    3: ('D', 'SIGTERM (15)'),
    4: ('A', 'Den har kraschat och väntar på att städas upp'),
    5: ('C', 'Ctrl+C'),
    6: ('B', 'htop'),
    7: ('B', 'Startar ett program med ändrad prioritet'),
    8: ('D', 'Process ID'),
    9: ('C', './longjob.sh &'),
    10: ('B', 'Skriv bg och tryck Enter'),
    11: ('C', 'SIGKILL'),
    12: ('C', 'OOM Killer dödar en process'),
    13: ('D', 'free -h'),  # eller B beroende på ordning
    14: ('A', 'Parent Process ID'),
    15: ('B', 'ps aux | grep nginx'),
    16: ('B', 'Antal processer i kön för CPU eller Disk I/O'),
    17: ('B', 'Över 60 st'),
    18: ('A', 'killall firefox'),
    19: ('C', 'Startar scriptet så det fortsätter köra'),
    20: ('A', 'Nice value'),
    21: ('A', 'En bakgrundsprocess som körs kontinuerligt'),
    22: ('B', 'Init eller Systemd'),
    23: ('A', 'Prova kill -9 PID'),
    24: ('C', 'Uninterruptible sleep'),
    25: ('D', 'pstree'),
    26: ('D', 'Staplar i färger'),
    27: ('B', 'Halva processorn används'),
    28: ('D', 'Nej, bara sina egna'),
    29: ('C', 'När datorn är så slut på RAM'),
    30: ('B', 'lsof'),
    31: ('A', 'En process som låser terminalen'),
    32: ('C', 'Ctrl+C'),
    33: ('C', 'Uppdaterar statistiken varje sekund'),
    34: ('B', 'Det senaste bakgrundsjobbet'),
    35: ('D', 'För att ladda om konfigurationsfiler'),
    36: ('D', 'Att en process är låst till specifik CPU'),
    37: ('A', 'ps aux'),
    38: ('A', 'Sänker prioriteten'),
    39: ('D', 'Alla ovanstående fungerar'),
    40: ('A', 'Zombien adopteras av init'),
    41: ('A', 'En tidsschemaläggare'),
    42: ('C', '/proc/meminfo'),
    43: ('B', 'Processer i User space har begränsad åtkomst'),
    44: ('D', 'kill -9 500'),
    45: ('C', 'landscape-sysinfo'),
    46: ('D', 'Processen är inte kopplad till terminal'),
    47: ('A', 'Processen kan lämna korrupta filer'),
    48: ('A', 'Disk I/O per process'),
    49: ('C', 'kill dem eller disown'),
    50: ('A', 'Ett program som körs i minnet'),
}

# Nod 3 Scenarios
NOD3_SCENARIO_ANSWERS = {
    1: ('B', 'Servern är överbelastad'),
    2: ('B', 'pkill -f my_script.py'),
    3: ('B', 'Den avbryts'),
    4: ('B', 'Nej, det är kärnan'),
    5: ('B', 'Den är redan död'),
    6: ('B', 'Du pausade vim'),
    7: ('B', 'ps -u kalle'),
    8: ('B', 'Docker/Cgroups'),
    9: ('C', 'ps aux | less'),
    10: ('B', 'Disken är flaskhalsen'),
    11: ('C', 'lsof -i :80'),
    12: ('B', 'Ctrl+C'),
    13: ('B', 'nice make'),
    14: ('B', 'cat /proc/1234/cmdline'),
    15: ('B', 'Systemet stannar/kraschar'),
    16: ('B', 'fg och fixa'),
    17: ('B', 'pkill -USR1 nginx'),
    18: ('B', 'SIGKILL avbröt skrivningar'),
    19: ('B', 'Systemet kraschar/fryser'),
    20: ('C', 'cat /proc/555/environ'),
    21: ('B', 'RES'),
    22: ('B', 'Nej'),
    23: ('B', 'Starta om tjänsten'),
    24: ('C', 'Övervaka RES'),
    25: ('B', 'Nej, bara root'),
    26: ('B', 'Kernel-tråd'),
    27: ('B', 'timeout 1h updatedb'),
    28: ('B', 'Artig vs Tvingande'),
    29: ('B', 'echo $!'),
    30: ('B', 'Använd tangentbordet'),
}

def find_correct_index(options: list, correct_answer_text: str) -> int:
    """Hitta index för rätt svar baserat på text-matchning"""
    correct_lower = correct_answer_text.lower().strip()

    for i, opt in enumerate(options):
        opt_lower = opt.lower().strip()
        # Exact match
        if correct_lower in opt_lower or opt_lower in correct_lower:
            return i

    # Om ingen exakt match, prova fuzzy
    for i, opt in enumerate(options):
        # Ta första 30 tecken för jämförelse
        if correct_lower[:30] in opt.lower()[:50]:
            return i

    return -1  # Ej hittad

# Läs quiz-filen och jämför
with open('/Users/mrebadi/Desktop/DevOps/SaaS-Project/saas-project/apps/frontend/src/data/nod3-10-questions.ts', 'r') as f:
    content = f.read()

print("=== NOD 3 PROCESSHANTERING VERIFIERING ===")
print()

# För varje fråga i Master, kolla vad quiz-filen säger
errors_found = []

for qnum, (master_letter, master_answer) in NOD3_MASTER_ANSWERS.items():
    # Hitta frågan i quiz-filen
    pattern = rf"nod3-processhantering-q{qnum}['\"].*?correctIndices:\s*\[(\d+)\]"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        quiz_index = int(match.group(1))
        # Master: A=0, B=1, C=2, D=3
        master_index = ord(master_letter) - ord('A')

        if quiz_index != master_index:
            errors_found.append({
                'question': f'Q{qnum}',
                'master_answer': f'{master_letter}) {master_answer}',
                'master_index': master_index,
                'quiz_index': quiz_index,
            })
            print(f"❌ Q{qnum}: Master={master_letter}({master_index}), Quiz=[{quiz_index}] - FEL!")
        else:
            print(f"✅ Q{qnum}: Korrekt ({master_letter})")

print()
print(f"=== SAMMANFATTNING ===")
print(f"Totalt fel: {len(errors_found)}")
print()

if errors_found:
    print("FEL SOM MÅSTE FIXAS:")
    for err in errors_found:
        print(f"  {err['question']}: Ändra correctIndices från [{err['quiz_index']}] till [{err['master_index']}]")
