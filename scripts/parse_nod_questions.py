#!/usr/bin/env python3
"""
Parser för Nod-filer till TypeScript quiz-format
Kör: python3 scripts/parse_nod_questions.py
"""

import re
import os
from pathlib import Path

# Nod-mappningar
NOD_FILES = {
    'nod3-processhantering': 'Omtenta/Nod3_Processhantering_Master.md',
    'nod4-natverk': 'Omtenta/Nod4_Natverk_Server_Master.md',
    'nod5-ssh': 'Omtenta/Nod5_SSH_Kommunikation_Master.md',
    'nod6-bash-skript': 'Omtenta/Nod6_Bash_Skript_Master.md',
    'nod7-bash-verktyg': 'Omtenta/Nod7_Bash_Verktyg_Master.md',
    'nod8-docker-isolering': 'Omtenta/Nod8_Docker_Isolering_Master.md',
    'nod9-docker-natverk': 'Omtenta/Nod9_Docker_Natverk_Lagring_Master.md',
    'nod10-docker-compose': 'Omtenta/Nod10_Docker_Compose_IaC_Master.md',
}

def parse_quiz_questions(content: str, topic: str) -> list:
    """Parse quiz questions from markdown content"""
    questions = []

    # Pattern: number. **Question text**\n   A) option\n   B) option\n   C) option\n   D) option
    quiz_pattern = r'(\d+)\.\s+\*\*([^*]+)\*\*\s*\n\s*A\)\s*([^\n]+)\s*\n\s*B\)\s*([^\n]+)\s*\n\s*C\)\s*([^\n]+)\s*\n\s*D\)\s*([^\n]+)'

    matches = re.finditer(quiz_pattern, content, re.MULTILINE)

    for match in matches:
        q_num = match.group(1)
        question = match.group(2).strip()
        options = [
            match.group(3).strip(),
            match.group(4).strip(),
            match.group(5).strip(),
            match.group(6).strip()
        ]

        # Clean up options - remove trailing punctuation, backticks etc
        options = [opt.rstrip('.').strip() for opt in options]

        # Try to determine correct answer (usually first option in unshuffled)
        # For now default to 0 (A) - can be verified later
        correct_idx = 0

        questions.append({
            'id': f'{topic}-q{q_num}',
            'question': question,
            'options': options,
            'correctIndices': [correct_idx],
            'difficulty': 'G' if int(q_num) <= 30 else 'VG',  # First 30 = G, rest = VG
            'topic': topic,
            'type': 'quiz'
        })

    return questions


def parse_scenario_questions(content: str, topic: str) -> list:
    """Parse scenario questions from DEL 3 section"""
    scenarios = []

    # Pattern matches: number. **Scenario:** text **Rätt svar/Lösning:** answer **Alternativ:** A) B) C) D)
    # Using DOTALL to match across newlines
    scenario_pattern = r'(\d+)\.\s+\*\*Scenario:\*\*\s*(.+?)\s*\*\*(?:Rätt svar|Lösning):\*\*\s*(.+?)\s*\*\*[Aa]lternativ:\*\*\s*A\)\s*([^B]+)B\)\s*([^C]+)C\)\s*([^D]+)D\)\s*([^\n]+)'

    matches = re.finditer(scenario_pattern, content, re.DOTALL)

    for match in matches:
        q_num = match.group(1)
        # Clean up multi-line text by replacing newlines with spaces
        scenario_text = ' '.join(match.group(2).strip().split())
        correct_answer = ' '.join(match.group(3).strip().split())
        options = [
            ' '.join(match.group(4).strip().rstrip('.').split()),
            ' '.join(match.group(5).strip().rstrip('.').split()),
            ' '.join(match.group(6).strip().rstrip('.').split()),
            ' '.join(match.group(7).strip().rstrip('.').split())
        ]

        # Find which option matches the correct answer (or is closest)
        correct_idx = 0
        for i, opt in enumerate(options):
            if correct_answer.lower() in opt.lower() or opt.lower() in correct_answer.lower():
                correct_idx = i
                break

        scenarios.append({
            'id': f'{topic}-s{q_num}',
            'question': f'SCENARIO: {scenario_text}',
            'options': options,
            'correctIndices': [correct_idx],
            'explanation': correct_answer,
            'difficulty': 'VG',  # Scenarios are typically harder
            'topic': topic,
            'type': 'scenario'
        })

    return scenarios

def parse_flashcards(content: str, topic: str) -> list:
    """Parse flashcards from markdown content"""
    flashcards = []

    # Pattern: **Fråga:** ... **Svar:** ...
    pattern = r'\d+\.\s+\*\*Fråga:\*\*\s+([^\n]+)\s+\*\*Svar:\*\*\s+([^\n]+)'

    matches = re.finditer(pattern, content, re.MULTILINE)

    for i, match in enumerate(matches, 1):
        question = match.group(1).strip()
        answer = match.group(2).strip()

        # Convert to quiz format (single correct answer)
        flashcards.append({
            'id': f'{topic}-fc{i}',
            'question': question,
            'answer': answer,
            'difficulty': 'G',
            'topic': topic,
        })

    return flashcards

def generate_typescript(questions: list, topic: str) -> str:
    """Generate TypeScript code for questions"""
    ts_code = f"// ===== {topic.upper().replace('-', ' ')} =====\n"
    ts_code += f"export const {topic.upper().replace('-', '_')}_QUESTIONS: Omtenta2Question[] = [\n"

    for q in questions:
        ts_code += "    {\n"
        ts_code += f"        id: '{q['id']}',\n"
        ts_code += f"        question: '{escape_string(q['question'])}',\n"
        ts_code += f"        options: {format_options(q['options'])},\n"
        ts_code += f"        correctIndices: {q['correctIndices']},\n"
        ts_code += f"        explanation: 'Se flashcard för förklaring.',\n"
        ts_code += f"        difficulty: '{q['difficulty']}',\n"
        ts_code += f"        category: 'Quiz',\n"
        ts_code += f"        topic: '{q['topic']}',\n"
        ts_code += f"        type: 'quiz'\n"
        ts_code += "    },\n"

    ts_code += "]\n"
    return ts_code

def escape_string(s: str) -> str:
    """Escape string for TypeScript"""
    return s.replace("'", "\\'").replace('\n', ' ')

def format_options(options: list) -> str:
    """Format options array for TypeScript"""
    escaped = [f"'{escape_string(opt)}'" for opt in options]
    return f"[{', '.join(escaped)}]"

def main():
    base_path = Path(__file__).parent.parent

    all_questions = {}

    for topic, file_path in NOD_FILES.items():
        full_path = base_path / file_path

        if not full_path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue

        print(f"📖 Parsing {file_path}...")

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        quiz_questions = parse_quiz_questions(content, topic)
        scenario_questions = parse_scenario_questions(content, topic)
        flashcards = parse_flashcards(content, topic)

        # Combine quiz and scenario questions
        all_topic_questions = quiz_questions + scenario_questions

        print(f"   Found {len(quiz_questions)} quiz + {len(scenario_questions)} scenarios = {len(all_topic_questions)} total, {len(flashcards)} flashcards")

        all_questions[topic] = all_topic_questions

    # Generate complete TypeScript output
    output_file = base_path / 'apps/frontend/src/data/nod3-10-questions.ts'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('// AUTO-GENERATED from Nod*_Master.md files\n')
        f.write('// Run: python3 scripts/parse_nod_questions.py\n')
        f.write('// NOTE: Uses inline type to avoid circular imports\n\n')

        # Define inline type to avoid circular import
        f.write('// Inline type (same as Omtenta2Question)\n')
        f.write('interface Nod3to10Question {\n')
        f.write('    id: string\n')
        f.write('    question: string\n')
        f.write('    options: string[]\n')
        f.write('    correctIndices: number[]\n')
        f.write('    explanation: string\n')
        f.write("    difficulty: 'G' | 'VG'\n")
        f.write('    category: string\n')
        f.write('    topic: string\n')
        f.write("    type: 'quiz' | 'scenario'\n")
        f.write('}\n\n')

        for topic, questions in all_questions.items():
            var_name = topic.upper().replace('-', '_') + '_QUESTIONS'
            quiz_count = len([q for q in questions if q['type'] == 'quiz'])
            scenario_count = len([q for q in questions if q['type'] == 'scenario'])
            f.write(f"// ===== {topic.upper().replace('-', ' ')} ({quiz_count} quiz + {scenario_count} scenarios) =====\n")
            f.write(f"export const {var_name}: Nod3to10Question[] = [\n")

            for q in questions:
                explanation = q.get('explanation', 'Se flashcard för förklaring.')
                category = 'Scenario' if q['type'] == 'scenario' else 'Quiz'
                f.write("    {\n")
                f.write(f"        id: '{q['id']}',\n")
                f.write(f"        question: '{escape_string(q['question'])}',\n")
                f.write(f"        options: {format_options(q['options'])},\n")
                f.write(f"        correctIndices: {q['correctIndices']},\n")
                f.write(f"        explanation: '{escape_string(explanation)}',\n")
                f.write(f"        difficulty: '{q['difficulty']}',\n")
                f.write(f"        category: '{category}',\n")
                f.write(f"        topic: '{q['topic']}',\n")
                f.write(f"        type: '{q['type']}'\n")
                f.write("    },\n")

            f.write("]\n\n")

        # Export combined array
        f.write("// Combined export\n")
        f.write("export const ALL_NOD3_TO_10_QUESTIONS: Nod3to10Question[] = [\n")
        for topic in all_questions.keys():
            var_name = topic.upper().replace('-', '_') + '_QUESTIONS'
            f.write(f"    ...{var_name},\n")
        f.write("]\n")

    total = sum(len(qs) for qs in all_questions.values())
    quiz_total = sum(len([q for q in qs if q['type'] == 'quiz']) for qs in all_questions.values())
    scenario_total = sum(len([q for q in qs if q['type'] == 'scenario']) for qs in all_questions.values())
    print(f"\n✅ Generated {output_file}")
    print(f"   Total: {total} questions ({quiz_total} quiz + {scenario_total} scenarios)")

if __name__ == '__main__':
    main()
