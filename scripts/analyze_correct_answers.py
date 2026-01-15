#!/usr/bin/env python3
"""
Fixar correctIndices i quiz-filerna genom att matcha mot flashcards.
"""

import re
from pathlib import Path
from difflib import SequenceMatcher

BASE_DIR = Path(__file__).parent.parent
OMTENTA_DIR = BASE_DIR / "Omtenta"
DATA_DIR = BASE_DIR / "apps/frontend/src/data"

def similar(a, b):
    """Beräkna likhet mellan två strängar."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def clean_text(text):
    """Rensa text för jämförelse."""
    return re.sub(r'[`*\s]+', ' ', text).strip().lower()

def extract_flashcard_answers(master_content):
    """Extrahera fråga -> svar mappning från flashcards."""
    flashcards = {}

    # Hitta DEL 1 (Flashcards)
    flashcard_match = re.search(r'## DEL 1:.*?(?=## DEL 2:|$)', master_content, re.DOTALL)
    if not flashcard_match:
        return flashcards

    flashcard_section = flashcard_match.group(0)

    # Pattern för flashcards: nummer. **Fråga:** text **Svar:** text
    pattern = r'\d+\.\s+\*\*(?:Fråga|Kort svar):\*\*\s*(.+?)\s+\*\*Svar:\*\*\s*(.+?)(?=\n\d+\.\s+\*\*|\n---|$)'

    for match in re.finditer(pattern, flashcard_section, re.DOTALL):
        question = clean_text(match.group(1))
        answer = clean_text(match.group(2))
        flashcards[question] = answer

    return flashcards

def find_correct_option(question_text, options, flashcards):
    """Hitta rätt svarsalternativ baserat på flashcard-svaret."""
    q_clean = clean_text(question_text)

    # Sök efter matchande flashcard
    best_match = None
    best_score = 0

    for flash_q, flash_answer in flashcards.items():
        score = similar(q_clean, flash_q)
        if score > best_score:
            best_score = score
            best_match = flash_answer

    if not best_match or best_score < 0.5:
        return None

    # Hitta vilket alternativ som matchar svaret bäst
    best_option_idx = 0
    best_option_score = 0

    for idx, opt in enumerate(options):
        opt_clean = clean_text(opt)
        score = similar(best_match, opt_clean)

        # Kolla också om svaret innehåller alternativet eller vice versa
        if opt_clean in best_match or best_match in opt_clean:
            score = max(score, 0.8)

        if score > best_option_score:
            best_option_score = score
            best_option_idx = idx

    if best_option_score > 0.3:
        return best_option_idx

    return None

def parse_quiz_questions(master_content):
    """Extrahera quiz-frågor med alternativ från Master-filen."""
    questions = []

    quiz_match = re.search(r'## DEL 2:.*?(?=## DEL 3:|$)', master_content, re.DOTALL)
    if not quiz_match:
        return questions

    quiz_section = quiz_match.group(0)

    # Pattern för quiz-frågor
    pattern = r'(\d+)\.\s+\*\*([^*]+)\*\*\s*\n\s*A\)\s*([^\n]+)\n\s*B\)\s*([^\n]+)\n\s*C\)\s*([^\n]+)\n\s*D\)\s*([^\n]+)'

    for match in re.finditer(pattern, quiz_section):
        questions.append({
            'num': int(match.group(1)),
            'question': match.group(2).strip(),
            'options': [
                match.group(3).strip().rstrip('.'),
                match.group(4).strip().rstrip('.'),
                match.group(5).strip().rstrip('.'),
                match.group(6).strip().rstrip('.')
            ]
        })

    return questions

def parse_scenario_questions(master_content):
    """Extrahera scenario-frågor med rätt svar från Master-filen."""
    scenarios = []

    scenario_match = re.search(r'## DEL 3:.*', master_content, re.DOTALL)
    if not scenario_match:
        return scenarios

    scenario_section = scenario_match.group(0)

    # Pattern för scenarios
    pattern = r'(\d+)\.\s+\*\*Scenario:\*\*\s*(.+?)\*\*(?:Rätt svar|Lösning):\*\*\s*([^\n]+)\s*\*\*Alternativ:\*\*\s*A\)\s*([^.]+)[.\s]*B\)\s*([^.]+)[.\s]*C\)\s*([^.]+)[.\s]*D\)\s*([^.\n]+)'

    for match in re.finditer(pattern, scenario_section, re.DOTALL):
        correct_text = clean_text(match.group(3))
        options = [
            match.group(4).strip(),
            match.group(5).strip(),
            match.group(6).strip(),
            match.group(7).strip()
        ]

        # Hitta vilket alternativ som matchar rätt svar
        correct_idx = 0
        best_score = 0

        for idx, opt in enumerate(options):
            opt_clean = clean_text(opt)
            score = similar(correct_text, opt_clean)
            if opt_clean in correct_text or correct_text in opt_clean:
                score = max(score, 0.8)
            if score > best_score:
                best_score = score
                correct_idx = idx

        scenarios.append({
            'num': int(match.group(1)),
            'scenario': match.group(2).strip()[:60],
            'correct_text': match.group(3).strip(),
            'options': options,
            'correct_idx': correct_idx if best_score > 0.3 else None
        })

    return scenarios

def analyze_nod(nod_num, filename):
    """Analysera en nod och returnera korrigeringar."""
    master_path = OMTENTA_DIR / filename

    if not master_path.exists():
        print(f"❌ NOD {nod_num}: Fil saknas: {filename}")
        return []

    with open(master_path, 'r', encoding='utf-8') as f:
        master_content = f.read()

    corrections = []

    # Extrahera flashcards för att hitta rätt svar
    flashcards = extract_flashcard_answers(master_content)

    # Analysera quiz-frågor
    quiz_questions = parse_quiz_questions(master_content)

    print(f"\n{'='*60}")
    print(f"NOD {nod_num}: {filename}")
    print(f"{'='*60}")
    print(f"Flashcards hittade: {len(flashcards)}")
    print(f"Quiz-frågor: {len(quiz_questions)}")

    for q in quiz_questions:
        correct_idx = find_correct_option(q['question'], q['options'], flashcards)
        if correct_idx is not None:
            letter = chr(ord('A') + correct_idx)
            corrections.append({
                'nod': nod_num,
                'type': 'quiz',
                'num': q['num'],
                'question': q['question'][:50],
                'correct_idx': correct_idx,
                'correct_letter': letter,
                'correct_text': q['options'][correct_idx][:40]
            })
            print(f"  Q{q['num']}: {letter}) {q['options'][correct_idx][:40]}")
        else:
            print(f"  Q{q['num']}: ⚠️ KUNDE INTE HITTA RÄTT SVAR")
            print(f"       Fråga: {q['question'][:50]}")

    # Analysera scenarios
    scenarios = parse_scenario_questions(master_content)
    print(f"\nScenarios: {len(scenarios)}")

    for s in scenarios:
        if s['correct_idx'] is not None:
            letter = chr(ord('A') + s['correct_idx'])
            corrections.append({
                'nod': nod_num,
                'type': 'scenario',
                'num': s['num'],
                'question': s['scenario'][:50],
                'correct_idx': s['correct_idx'],
                'correct_letter': letter,
                'correct_text': s['options'][s['correct_idx']][:40]
            })
            print(f"  S{s['num']}: {letter}) {s['correct_text'][:40]}")
        else:
            print(f"  S{s['num']}: ⚠️ KUNDE INTE MATCHA - '{s['correct_text'][:40]}'")

    return corrections

def main():
    nod_files = {
        3: "Nod3_Processhantering_Master.md",
        4: "Nod4_Natverk_Server_Master.md",
        5: "Nod5_SSH_Kommunikation_Master.md",
        6: "Nod6_Bash_Skript_Master.md",
        7: "Nod7_Bash_Verktyg_Master.md",
        8: "Nod8_Docker_Isolering_Master.md",
        9: "Nod9_Docker_Natverk_Lagring_Master.md",
        10: "Nod10_Docker_Compose_IaC_Master.md"
    }

    all_corrections = []

    for nod_num, filename in nod_files.items():
        corrections = analyze_nod(nod_num, filename)
        all_corrections.extend(corrections)

    # Sammanfattning
    print(f"\n{'='*60}")
    print("SAMMANFATTNING")
    print(f"{'='*60}")
    print(f"Totalt korrigeringar: {len(all_corrections)}")

    # Skriv ut korrigeringar grupperade per nod
    for nod_num in sorted(nod_files.keys()):
        nod_corrections = [c for c in all_corrections if c['nod'] == nod_num]
        if nod_corrections:
            print(f"\nNOD {nod_num}:")
            quiz_corrections = [c for c in nod_corrections if c['type'] == 'quiz']
            scenario_corrections = [c for c in nod_corrections if c['type'] == 'scenario']
            print(f"  Quiz: {len(quiz_corrections)} frågor med rätt svar")
            print(f"  Scenarios: {len(scenario_corrections)} scenarios med rätt svar")

if __name__ == "__main__":
    main()
