#!/usr/bin/env python3
"""
KOMPLETT VERIFIERING OCH FIX AV ALLA NOD 3-10 FRÅGOR

Detta skript går igenom VARJE Master-fil, extraherar rätt svar,
och uppdaterar quiz-filen med korrekta correctIndices.
"""

import re
import os

# Sökvägar
BASE_PATH = '/Users/mrebadi/Desktop/DevOps/SaaS-Project/saas-project'
QUIZ_FILE = f'{BASE_PATH}/apps/frontend/src/data/nod3-10-questions.ts'
OMTENTA_PATH = f'{BASE_PATH}/Omtenta'

# Master-filer
MASTER_FILES = {
    3: 'Nod3_Processhantering_Master.md',
    4: 'Nod4_Natverk_Server_Master.md',
    5: 'Nod5_SSH_Kommunikation_Master.md',
    6: 'Nod6_Bash_Skript_Master.md',
    7: 'Nod7_Bash_Verktyg_Master.md',
    8: 'Nod8_Docker_Isolering_Master.md',
    9: 'Nod9_Docker_Natverk_Lagring_Master.md',
    10: 'Nod10_Docker_Compose_IaC_Master.md',
}

def extract_master_answers(master_content: str) -> dict:
    """
    Extrahera rätt svar från Master-filen.
    Returnerar dict med frågenummer -> (rätt bokstav, rätt svar text)
    """
    answers = {}

    # Hitta DEL 2 (Quiz) sektionen
    quiz_section = re.search(r'## DEL 2.*?(?=## DEL 3|$)', master_content, re.DOTALL)
    if not quiz_section:
        return answers

    quiz_text = quiz_section.group(0)

    # Hitta varje fråga och dess alternativ
    # Mönster: nummer. **Fråga?** sedan A) B) C) D)
    question_pattern = r'(\d+)\.\s*\*\*([^*]+)\*\*\s*\n\s*A\)\s*([^\n]+)\s*\n\s*B\)\s*([^\n]+)\s*\n\s*C\)\s*([^\n]+)\s*\n\s*D\)\s*([^\n]+)'

    for match in re.finditer(question_pattern, quiz_text):
        q_num = int(match.group(1))
        question = match.group(2).strip()
        options = [
            match.group(3).strip(),  # A
            match.group(4).strip(),  # B
            match.group(5).strip(),  # C
            match.group(6).strip(),  # D
        ]

        # Hitta rätt svar - leta efter mönster som indikerar rätt svar
        # Kollar om frågan har ett FACIT-mönster eller om vi måste gissa
        answers[q_num] = {
            'question': question,
            'options': options
        }

    return answers


def extract_facit_answers(master_content: str) -> dict:
    """
    Extrahera svar från FACIT-sektionen (finns i Nod 8-10)
    """
    facit_answers = {}

    facit_section = re.search(r'## FACIT.*?$', master_content, re.DOTALL)
    if not facit_section:
        return facit_answers

    facit_text = facit_section.group(0)

    # Mönster: nummer. **BOKSTAV** (förklaring)
    pattern = r'(\d+)\.\s*\*\*([A-D])\*\*'

    for match in re.finditer(pattern, facit_text):
        q_num = int(match.group(1))
        letter = match.group(2)
        facit_answers[q_num] = letter

    return facit_answers


def letter_to_index(letter: str) -> int:
    """Konvertera A=0, B=1, C=2, D=3"""
    return ord(letter.upper()) - ord('A')


def find_correct_answer_in_quiz(quiz_content: str, nod: int, q_num: int) -> tuple:
    """
    Hitta en specifik fråga i quiz-filen och returnera dess nuvarande correctIndices och options
    """
    # Hitta nod-prefix
    nod_prefixes = {
        3: 'nod3-processhantering',
        4: 'nod4-natverk',
        5: 'nod5-ssh',
        6: 'nod6-bash-skript',
        7: 'nod7-bash-verktyg',
        8: 'nod8-docker-isolering',
        9: 'nod9-docker-natverk',
        10: 'nod10-docker-compose',
    }

    prefix = nod_prefixes.get(nod)
    if not prefix:
        return None, None

    # Sök efter frågan
    pattern = rf"id:\s*'{prefix}-q{q_num}'.*?correctIndices:\s*\[(\d+)\].*?options:\s*\[([^\]]+)\]"
    match = re.search(pattern, quiz_content, re.DOTALL)

    if match:
        current_index = int(match.group(1))
        options_str = match.group(2)
        # Parsa options
        options = re.findall(r"'([^']*)'", options_str)
        return current_index, options

    return None, None


def update_correct_index(quiz_content: str, nod: int, q_num: int, new_index: int) -> str:
    """
    Uppdatera correctIndices för en specifik fråga
    """
    nod_prefixes = {
        3: 'nod3-processhantering',
        4: 'nod4-natverk',
        5: 'nod5-ssh',
        6: 'nod6-bash-skript',
        7: 'nod7-bash-verktyg',
        8: 'nod8-docker-isolering',
        9: 'nod9-docker-natverk',
        10: 'nod10-docker-compose',
    }

    prefix = nod_prefixes.get(nod)
    if not prefix:
        return quiz_content

    # Ersätt correctIndices för specifik fråga
    pattern = rf"(id:\s*'{prefix}-q{q_num}'.*?correctIndices:\s*\[)\d+(\])"
    replacement = rf"\g<1>{new_index}\g<2>"

    return re.sub(pattern, replacement, quiz_content, flags=re.DOTALL)


def main():
    print("=" * 60)
    print("KOMPLETT VERIFIERING AV ALLA NOD 3-10 FRÅGOR")
    print("=" * 60)
    print()

    # Läs quiz-filen
    with open(QUIZ_FILE, 'r') as f:
        quiz_content = f.read()

    total_errors = 0
    total_fixed = 0
    all_fixes = []

    for nod, master_file in MASTER_FILES.items():
        print(f"\n{'='*40}")
        print(f"NOD {nod}: {master_file}")
        print(f"{'='*40}")

        master_path = os.path.join(OMTENTA_PATH, master_file)

        if not os.path.exists(master_path):
            print(f"  ⚠️ Master-fil saknas!")
            continue

        with open(master_path, 'r') as f:
            master_content = f.read()

        # Extrahera FACIT om det finns (Nod 8-10)
        facit_answers = extract_facit_answers(master_content)

        if facit_answers:
            print(f"  ✓ FACIT hittad med {len(facit_answers)} svar")

            for q_num, correct_letter in facit_answers.items():
                correct_index = letter_to_index(correct_letter)
                current_index, options = find_correct_answer_in_quiz(quiz_content, nod, q_num)

                if current_index is not None:
                    if current_index != correct_index:
                        print(f"  ❌ Q{q_num}: Master={correct_letter}({correct_index}), Quiz=[{current_index}] - FEL!")
                        quiz_content = update_correct_index(quiz_content, nod, q_num, correct_index)
                        total_errors += 1
                        total_fixed += 1
                        all_fixes.append(f"Nod{nod} Q{q_num}: [{current_index}] -> [{correct_index}] ({correct_letter})")
        else:
            print(f"  ⚠️ Ingen FACIT - måste verifiera manuellt")

            # För Nod 3-7, extrahera från quiz-frågor format
            master_answers = extract_master_answers(master_content)
            print(f"  Hittade {len(master_answers)} frågor i Master")

    print("\n" + "=" * 60)
    print("SAMMANFATTNING")
    print("=" * 60)
    print(f"Totalt fel hittade: {total_errors}")
    print(f"Totalt fixade: {total_fixed}")

    if all_fixes:
        print("\nFixar som gjordes:")
        for fix in all_fixes[:20]:  # Visa max 20
            print(f"  {fix}")
        if len(all_fixes) > 20:
            print(f"  ... och {len(all_fixes) - 20} till")

    # Spara uppdaterad quiz-fil
    if total_fixed > 0:
        with open(QUIZ_FILE, 'w') as f:
            f.write(quiz_content)
        print(f"\n✅ Quiz-fil uppdaterad med {total_fixed} fixar")


if __name__ == '__main__':
    main()
