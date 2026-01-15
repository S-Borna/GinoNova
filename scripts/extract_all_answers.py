#!/usr/bin/env python3
"""
Script som extraherar ALLA korrekta svar från Master-filerna och genererar fixade quiz-filer.
"""

import re
from pathlib import Path
from difflib import SequenceMatcher
import json

BASE_DIR = Path(__file__).parent.parent
OMTENTA_DIR = BASE_DIR / "Omtenta"
DATA_DIR = BASE_DIR / "apps/frontend/src/data"

def similar(a, b):
    """Beräkna likhet mellan två strängar."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def clean_text(text):
    """Rensa text för jämförelse."""
    return re.sub(r'[`*\s]+', ' ', text).strip().lower()

def letter_to_index(letter):
    """Konvertera A/B/C/D till 0/1/2/3."""
    return ord(letter.upper()) - ord('A')

def extract_quiz_facit_format(content):
    """Extrahera facit från formatet: nummer. **BOKSTAV** (förklaring)"""
    facit = {}
    pattern = r'^(\d+)\.\s+\*\*([A-D])\*\*'
    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            num = int(match.group(1))
            letter = match.group(2)
            facit[num] = letter_to_index(letter)
    return facit

def extract_scenario_answers(content):
    """Extrahera rätt svar för scenarios från **Rätt svar:** och matcha mot alternativ."""
    scenarios = {}

    # Hitta scenario-sektionen
    scenario_match = re.search(r'## DEL 3:.*', content, re.DOTALL)
    if not scenario_match:
        return scenarios

    scenario_section = scenario_match.group(0)

    # Pattern för scenarios med rätt svar och alternativ
    # Matchar: nummer. **Scenario:** text **Rätt svar:** svar **Alternativ:** A) ... B) ... C) ... D) ...
    pattern = r'(\d+)\.\s+\*\*Scenario:\*\*\s*(.+?)\*\*(?:Rätt svar|Lösning):\*\*\s*([^\n]+?)\s*\*\*Alternativ:\*\*\s*A\)\s*([^.]+)[.\s]*B\)\s*([^.]+)[.\s]*C\)\s*([^.]+)[.\s]*D\)\s*([^\n.]+)'

    for match in re.finditer(pattern, scenario_section, re.DOTALL):
        num = int(match.group(1))
        correct_text = clean_text(match.group(3))
        options = [
            clean_text(match.group(4)),
            clean_text(match.group(5)),
            clean_text(match.group(6)),
            clean_text(match.group(7))
        ]

        # Hitta vilket alternativ som matchar bäst
        best_idx = 0
        best_score = 0

        for idx, opt in enumerate(options):
            # Beräkna likhet
            score = similar(correct_text, opt)

            # Bonus om de innehåller varandra
            if opt in correct_text or correct_text in opt:
                score = max(score, 0.85)

            # Kolla nyckelord
            correct_words = set(correct_text.split())
            opt_words = set(opt.split())
            common = len(correct_words & opt_words)
            if common >= 2:
                score = max(score, 0.7 + common * 0.05)

            if score > best_score:
                best_score = score
                best_idx = idx

        if best_score >= 0.3:
            scenarios[num] = best_idx
        else:
            # Fallback: Oftast är rätt svar B i scenarios
            print(f"  ⚠️ S{num}: Låg matchning ({best_score:.2f}) - defaultar till B")
            scenarios[num] = 1

    return scenarios

def extract_flashcard_answers(content):
    """Extrahera fråga -> svar från flashcards."""
    flashcards = {}

    flashcard_match = re.search(r'## DEL 1:.*?(?=## DEL 2:|$)', content, re.DOTALL)
    if not flashcard_match:
        return flashcards

    flashcard_section = flashcard_match.group(0)

    # Pattern: nummer. **Fråga:** text **Svar:** text
    pattern = r'\d+\.\s+\*\*(?:Fråga|Kort svar):\*\*\s*(.+?)\s*\*\*Svar:\*\*\s*(.+?)(?=\n\d+\.\s+\*\*|\n---|$)'

    for match in re.finditer(pattern, flashcard_section, re.DOTALL):
        question = clean_text(match.group(1))
        answer = clean_text(match.group(2))
        flashcards[question] = answer

    return flashcards

def extract_quiz_questions(content):
    """Extrahera quiz-frågor med alternativ."""
    questions = []

    quiz_match = re.search(r'## DEL 2:.*?(?=## DEL 3:|$)', content, re.DOTALL)
    if not quiz_match:
        return questions

    quiz_section = quiz_match.group(0)

    # Pattern: nummer. **fråga** A) ... B) ... C) ... D) ...
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

def find_quiz_answer_from_flashcards(question, options, flashcards):
    """Hitta rätt quiz-svar genom att matcha mot flashcards."""
    q_clean = clean_text(question)

    # Hitta bästa matchande flashcard
    best_flash_answer = None
    best_flash_score = 0

    for flash_q, flash_a in flashcards.items():
        score = similar(q_clean, flash_q)
        if score > best_flash_score:
            best_flash_score = score
            best_flash_answer = flash_a

    if not best_flash_answer or best_flash_score < 0.4:
        return None

    # Hitta vilket alternativ som matchar flashcard-svaret
    best_opt_idx = 0
    best_opt_score = 0

    for idx, opt in enumerate(options):
        opt_clean = clean_text(opt)
        score = similar(best_flash_answer, opt_clean)

        if opt_clean in best_flash_answer or best_flash_answer in opt_clean:
            score = max(score, 0.8)

        if score > best_opt_score:
            best_opt_score = score
            best_opt_idx = idx

    if best_opt_score >= 0.35:
        return best_opt_idx

    return None

def process_nod(nod_num, filename):
    """Processa en nod och returnera alla korrekta svar."""
    master_path = OMTENTA_DIR / filename

    if not master_path.exists():
        print(f"❌ NOD {nod_num}: Fil saknas: {filename}")
        return {'quiz': {}, 'scenarios': {}}

    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n{'='*60}")
    print(f"NOD {nod_num}: {filename}")
    print('='*60)

    results = {'quiz': {}, 'scenarios': {}}

    # Kolla om det finns explicit facit (Nod 8-10)
    quiz_facit = extract_quiz_facit_format(content)

    if quiz_facit:
        print(f"✅ Hittade {len(quiz_facit)} quiz-facit i explicit format")
        results['quiz'] = quiz_facit
    else:
        # Använd flashcards för att hitta svar (Nod 1-7)
        flashcards = extract_flashcard_answers(content)
        quiz_questions = extract_quiz_questions(content)

        print(f"📝 {len(flashcards)} flashcards, {len(quiz_questions)} quiz-frågor")

        matched = 0
        for q in quiz_questions:
            answer_idx = find_quiz_answer_from_flashcards(q['question'], q['options'], flashcards)
            if answer_idx is not None:
                results['quiz'][q['num']] = answer_idx
                matched += 1

        print(f"✅ Matchade {matched}/{len(quiz_questions)} quiz-frågor via flashcards")

    # Scenarios - finns i alla noder med **Rätt svar:**
    scenario_answers = extract_scenario_answers(content)
    results['scenarios'] = scenario_answers
    print(f"✅ {len(scenario_answers)} scenario-svar extraherade")

    return results

def main():
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

    all_answers = {}

    for nod_num, filename in nod_files.items():
        answers = process_nod(nod_num, filename)
        all_answers[nod_num] = answers

    # Spara till JSON för debugging
    output_path = BASE_DIR / "scripts" / "correct_answers.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_answers, f, indent=2)

    print(f"\n{'='*60}")
    print("SAMMANFATTNING")
    print('='*60)

    total_quiz = 0
    total_scenarios = 0

    for nod_num in sorted(all_answers.keys()):
        data = all_answers[nod_num]
        quiz_count = len(data['quiz'])
        scenario_count = len(data['scenarios'])
        total_quiz += quiz_count
        total_scenarios += scenario_count
        print(f"NOD {nod_num}: {quiz_count} quiz, {scenario_count} scenarios")

    print(f"\nTOTALT: {total_quiz} quiz-svar, {total_scenarios} scenario-svar")
    print(f"\nSparat till: {output_path}")

if __name__ == "__main__":
    main()
