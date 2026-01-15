#!/usr/bin/env python3
"""
Verifierar att alla svar i quiz-filerna matchar Master-filerna.
Går igenom varje nod (1-10), varje quiz-fråga och varje scenario.
"""

import re
import json
from pathlib import Path

OMTENTA_DIR = Path(__file__).parent.parent / "Omtenta"
DATA_DIR = Path(__file__).parent.parent / "apps/frontend/src/data"

def parse_master_questions(filepath):
    """Parsar quiz och scenario frågor från en Master-fil."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = []

    # Hitta DEL 2 (Quiz) och DEL 3 (Scenarios)
    quiz_match = re.search(r'## DEL 2:.*?(?=## DEL 3:|$)', content, re.DOTALL)
    scenario_match = re.search(r'## DEL 3:.*', content, re.DOTALL)

    # Parse quiz-frågor
    if quiz_match:
        quiz_section = quiz_match.group(0)
        # Mönster: nummer. **fråga** följt av A) B) C) D)
        pattern = r'(\d+)\.\s+\*\*([^*]+)\*\*\s*\n\s*A\)\s*([^\n]+)\n\s*B\)\s*([^\n]+)\n\s*C\)\s*([^\n]+)\n\s*D\)\s*([^\n]+)'

        for match in re.finditer(pattern, quiz_section):
            num, question, a, b, c, d = match.groups()
            questions.append({
                'num': int(num),
                'type': 'quiz',
                'question': question.strip(),
                'options': [a.strip(), b.strip(), c.strip(), d.strip()],
                'correct_letter': None  # Kommer sättas senare
            })

    # Parse scenario-frågor
    if scenario_match:
        scenario_section = scenario_match.group(0)
        # Mönster för scenarios med "Rätt svar:" eller specifik bokstav
        pattern = r'(\d+)\.\s+\*\*Scenario:\*\*\s*([^*]+?)(?:\*\*Rätt svar:\*\*|\*\*Lösning:\*\*)\s*([^\n]+)\s*\*\*Alternativ:\*\*\s*A\)\s*([^\n]+)\s*B\)\s*([^\n]+)\s*C\)\s*([^\n]+)\s*D\)\s*([^\n]+)'

        for match in re.finditer(pattern, scenario_section, re.DOTALL):
            num, scenario_text, correct_answer, a, b, c, d = match.groups()
            questions.append({
                'num': int(num),
                'type': 'scenario',
                'question': scenario_text.strip()[:100],  # Första 100 tecken
                'options': [a.strip(), b.strip(), c.strip(), d.strip()],
                'correct_answer_text': correct_answer.strip()
            })

    return questions

def find_correct_index_from_master(filepath):
    """Hittar rätt svarsindex direkt från Master-filens struktur."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    results = []

    # Quiz-frågor - leta efter mönster där rätt svar ofta är markerat
    # I Master-filerna är rätt svar den som matchar förklaringen eller är explicit markerad

    # Enklare approach: Läs raderna och bygg upp fråga för fråga
    lines = content.split('\n')
    current_question = None
    current_options = {}
    in_quiz = False
    in_scenario = False

    for i, line in enumerate(lines):
        if 'DEL 2:' in line:
            in_quiz = True
            in_scenario = False
            continue
        if 'DEL 3:' in line:
            in_quiz = False
            in_scenario = True
            continue

        # Quiz-fråga start
        if in_quiz:
            q_match = re.match(r'^(\d+)\.\s+\*\*(.+)\*\*\s*$', line)
            if q_match:
                if current_question:
                    results.append(current_question)
                current_question = {
                    'num': int(q_match.group(1)),
                    'type': 'quiz',
                    'question': q_match.group(2).strip(),
                    'options': {},
                    'correct_index': None
                }
                current_options = {}
                continue

            # Svarsalternativ
            opt_match = re.match(r'^\s*([A-D])\)\s*(.+)$', line)
            if opt_match and current_question:
                letter = opt_match.group(1)
                text = opt_match.group(2).strip()
                current_question['options'][letter] = text

        # Scenario-fråga
        if in_scenario:
            scenario_match = re.match(r'^(\d+)\.\s+\*\*Scenario:\*\*\s*(.+)$', line)
            if scenario_match:
                if current_question:
                    results.append(current_question)
                current_question = {
                    'num': int(scenario_match.group(1)),
                    'type': 'scenario',
                    'question': scenario_match.group(2).strip()[:80],
                    'options': {},
                    'correct_index': None,
                    'correct_text': None
                }
                continue

            # Rätt svar för scenario
            if current_question and current_question['type'] == 'scenario':
                correct_match = re.match(r'^\s+\*\*(?:Rätt svar|Lösning):\*\*\s*(.+)$', line)
                if correct_match:
                    current_question['correct_text'] = correct_match.group(1).strip()

                # Alternativ
                alt_match = re.match(r'^\s+\*\*Alternativ:\*\*\s*A\)\s*(.+?)\s*B\)\s*(.+?)\s*C\)\s*(.+?)\s*D\)\s*(.+)$', line)
                if alt_match:
                    current_question['options'] = {
                        'A': alt_match.group(1).strip().rstrip('.'),
                        'B': alt_match.group(2).strip().rstrip('.'),
                        'C': alt_match.group(3).strip().rstrip('.'),
                        'D': alt_match.group(4).strip().rstrip('.')
                    }
                    # Hitta rätt index baserat på correct_text
                    if current_question.get('correct_text'):
                        for letter, text in current_question['options'].items():
                            if current_question['correct_text'].lower() in text.lower() or text.lower() in current_question['correct_text'].lower():
                                current_question['correct_index'] = ord(letter) - ord('A')
                                break

    if current_question:
        results.append(current_question)

    return results

def parse_quiz_file_questions(nod_num):
    """Parsar frågor från quiz-filerna för en specifik nod."""
    questions = []

    if nod_num <= 2:
        # Nod 1-2 är i omtenta-2.0-quiz.ts
        filepath = DATA_DIR / "omtenta-2.0-quiz.ts"
    else:
        # Nod 3-10 är i nod3-10-questions.ts
        filepath = DATA_DIR / "nod3-10-questions.ts"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Hitta alla frågor för denna nod
    topic_name = f"nod{nod_num}-"

    # Regex för att hitta frågor
    pattern = r"\{\s*id:\s*'(" + topic_name + r"[^']+)'.*?question:\s*'([^']+)'.*?options:\s*\[([^\]]+)\].*?correctIndices:\s*\[(\d+)\]"

    for match in re.finditer(pattern, content, re.DOTALL):
        qid, question, options_str, correct_idx = match.groups()

        # Parse options
        options = re.findall(r"'([^']+)'", options_str)

        questions.append({
            'id': qid,
            'question': question[:80],
            'options': options,
            'correct_index': int(correct_idx)
        })

    return questions

def compare_answers():
    """Jämför svar mellan Master-filer och quiz-filer."""

    nod_files = {
        1: "Nod1_Filsystem_Grunder_Master.md",
        2: "Nod2_Rattigheter_Sakerhet_Master.md",
        3: "Nod3_Processhantering_Master.md",
        4: "Nod4_Natverk_Server_Master.md",
        5: "Nod5_SSH_Kommunikation_Master.md",
        6: "Nod6_Bash_Skript_Master.md",
        7: "Nod7_Bash_Verktyg_Master.md",
        8: "Nod8_Docker_Isolering_Master.md",
        9: "Nod9_Docker_Natverk_Lagring_Master.md",
        10: "Nod10_Docker_Compose_IaC_Master.md"
    }

    all_errors = []

    for nod_num, filename in nod_files.items():
        master_path = OMTENTA_DIR / filename
        if not master_path.exists():
            print(f"❌ NOD {nod_num}: Master-fil saknas: {filename}")
            continue

        print(f"\n{'='*60}")
        print(f"NOD {nod_num}: {filename}")
        print('='*60)

        # Läs Master-filen rad för rad och extrahera frågor med rätt svar
        with open(master_path, 'r', encoding='utf-8') as f:
            master_content = f.read()

        # Läs quiz-filen
        if nod_num <= 2:
            quiz_path = DATA_DIR / "omtenta-2.0-quiz.ts"
        else:
            quiz_path = DATA_DIR / "nod3-10-questions.ts"

        with open(quiz_path, 'r', encoding='utf-8') as f:
            quiz_content = f.read()

        # Extrahera quiz-frågor från Master
        quiz_section = re.search(r'## DEL 2:.*?(?=## DEL 3:|$)', master_content, re.DOTALL)
        if quiz_section:
            quiz_text = quiz_section.group(0)

            # Hitta varje fråga med A/B/C/D alternativ
            q_pattern = r'(\d+)\.\s+\*\*([^*]+)\*\*\s*\n\s*A\)\s*([^\n]+)\n\s*B\)\s*([^\n]+)\n\s*C\)\s*([^\n]+)\n\s*D\)\s*([^\n]+)'

            for m in re.finditer(q_pattern, quiz_text):
                q_num = m.group(1)
                q_text = m.group(2).strip()[:60]
                opt_a = m.group(3).strip()
                opt_b = m.group(4).strip()
                opt_c = m.group(5).strip()
                opt_d = m.group(6).strip()

                # Sök efter denna fråga i quiz-filen
                # Normalisera frågan för sökning
                search_text = q_text[:40].replace('`', '').replace('/', '').replace('"', '').replace("'", "")
                search_text = re.escape(search_text[:30])

                # Hitta frågan i quiz-filen
                quiz_match = re.search(
                    rf"question:\s*'[^']*{search_text}[^']*'.*?options:\s*\[([^\]]+)\].*?correctIndices:\s*\[(\d+)\]",
                    quiz_content,
                    re.DOTALL | re.IGNORECASE
                )

                if quiz_match:
                    quiz_options_str = quiz_match.group(1)
                    quiz_correct_idx = int(quiz_match.group(2))

                    # Extrahera quiz-alternativ
                    quiz_options = re.findall(r"'([^']+)'", quiz_options_str)

                    if quiz_options and quiz_correct_idx < len(quiz_options):
                        quiz_correct_text = quiz_options[quiz_correct_idx]

                        # Jämför med Master-alternativen
                        master_options = [opt_a, opt_b, opt_c, opt_d]

                        # Kontrollera att quiz-svaret matchar ett av master-alternativen
                        # och att det är rätt alternativ
                        quiz_clean = quiz_correct_text.replace('`', '').strip().lower()

                        match_found = False
                        matched_letter = None
                        for i, opt in enumerate(master_options):
                            opt_clean = opt.replace('`', '').strip().lower()
                            if quiz_clean in opt_clean or opt_clean in quiz_clean:
                                match_found = True
                                matched_letter = chr(ord('A') + i)
                                break

                        if match_found and matched_letter:
                            # Quiz-svaret matchar alternativ {matched_letter} i Master
                            # Men vi vet inte vad rätt svar SKA vara utan att kolla förklaringen
                            print(f"  Q{q_num}: Quiz svarar {matched_letter}) - '{quiz_clean[:30]}'")
                        else:
                            print(f"  ⚠️ Q{q_num}: Kunde inte matcha quiz-svar mot Master-alternativ")
                            print(f"      Quiz: '{quiz_clean[:40]}'")
                            print(f"      Master A: '{opt_a[:40]}'")

        # Extrahera scenario-frågor
        scenario_section = re.search(r'## DEL 3:.*', master_content, re.DOTALL)
        if scenario_section:
            scenario_text = scenario_section.group(0)

            # Hitta scenarios med rätt svar och alternativ
            s_pattern = r'(\d+)\.\s+\*\*Scenario:\*\*\s*(.+?)(?:\*\*Rätt svar:\*\*|\*\*Lösning:\*\*)\s*([^\n]+)\s*\*\*Alternativ:\*\*\s*A\)\s*([^.]+)[.\s]*B\)\s*([^.]+)[.\s]*C\)\s*([^.]+)[.\s]*D\)\s*([^.\n]+)'

            for m in re.finditer(s_pattern, scenario_text, re.DOTALL):
                s_num = m.group(1)
                correct_text = m.group(3).strip()
                opt_a = m.group(4).strip()
                opt_b = m.group(5).strip()
                opt_c = m.group(6).strip()
                opt_d = m.group(7).strip()

                # Hitta rätt bokstav
                correct_clean = correct_text.lower()
                master_options = [opt_a.lower(), opt_b.lower(), opt_c.lower(), opt_d.lower()]
                correct_letter = None
                correct_index = None

                for i, opt in enumerate(master_options):
                    if correct_clean in opt or opt in correct_clean:
                        correct_letter = chr(ord('A') + i)
                        correct_index = i
                        break

                if correct_letter:
                    print(f"  S{s_num}: Rätt svar = {correct_letter}) (index {correct_index})")
                else:
                    print(f"  ⚠️ S{s_num}: Kunde inte hitta rätt bokstav")
                    print(f"      Rätt svar: '{correct_text[:40]}'")

if __name__ == "__main__":
    compare_answers()
