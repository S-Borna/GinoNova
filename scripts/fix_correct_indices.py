#!/usr/bin/env python3
"""
Script som fixar correctIndices i quiz-filerna baserat på extraherade svar från Master-filerna.
"""

import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "apps/frontend/src/data"

def load_correct_answers():
    """Ladda korrekta svar från JSON."""
    json_path = BASE_DIR / "scripts" / "correct_answers.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def fix_nod3_10_questions():
    """Fixa nod3-10-questions.ts."""
    filepath = DATA_DIR / "nod3-10-questions.ts"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    correct_answers = load_correct_answers()

    fixes = 0
    errors = []

    # Processa varje nod 3-10
    for nod_num in range(3, 11):
        nod_data = correct_answers.get(str(nod_num), {})
        quiz_answers = nod_data.get('quiz', {})
        scenario_answers = nod_data.get('scenarios', {})

        nod_prefix = f"nod{nod_num}-"

        # Hitta alla frågor för denna nod
        # Pattern: id: 'nod3-...-qNN' eller id: 'nod3-...-sNN'

        for q_num, correct_idx in quiz_answers.items():
            # Sök efter mönster som matchar quiz-frågor
            # Format: nod3-processhantering-q2
            pattern = rf"(id:\s*'{nod_prefix}[^']+q{q_num}'[^}}]+?correctIndices:\s*\[)(\d+)(\])"

            def replace_idx(m):
                nonlocal fixes
                old_idx = int(m.group(2))
                if old_idx != correct_idx:
                    fixes += 1
                    return f"{m.group(1)}{correct_idx}{m.group(3)}"
                return m.group(0)

            content = re.sub(pattern, replace_idx, content, flags=re.DOTALL)

        for s_num, correct_idx in scenario_answers.items():
            # Format: nod3-processhantering-s1
            pattern = rf"(id:\s*'{nod_prefix}[^']+s{s_num}'[^}}]+?correctIndices:\s*\[)(\d+)(\])"

            def replace_idx(m):
                nonlocal fixes
                old_idx = int(m.group(2))
                if old_idx != correct_idx:
                    fixes += 1
                    return f"{m.group(1)}{correct_idx}{m.group(3)}"
                return m.group(0)

            content = re.sub(pattern, replace_idx, content, flags=re.DOTALL)

    # Spara fixad fil
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"nod3-10-questions.ts: {fixes} fixar applicerade")
    return fixes

def verify_nod10_q4():
    """Verifiera att Nod10 Q4 är fixad."""
    filepath = DATA_DIR / "nod3-10-questions.ts"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Hitta frågan om volym-drivrutin
    match = re.search(r"'Hur anger du att volymen använder en lokal drivrutin\?'.*?correctIndices:\s*\[(\d+)\]", content, re.DOTALL)

    if match:
        idx = int(match.group(1))
        letter = chr(ord('A') + idx)
        print(f"\n✅ Verifiering Nod10 Q4:")
        print(f"   correctIndices: [{idx}] = {letter})")
        if idx == 1:
            print(f"   KORREKT! B) driver: local")
        else:
            print(f"   ⚠️ FEL! Borde vara 1 (B)")
    else:
        print("⚠️ Kunde inte hitta Nod10 Q4")

def main():
    print("=" * 60)
    print("FIXAR CORRECTINDICES I QUIZ-FILERNA")
    print("=" * 60)

    total_fixes = 0

    # Fixa nod3-10
    total_fixes += fix_nod3_10_questions()

    # Verifiera
    verify_nod10_q4()

    print(f"\n{'='*60}")
    print(f"TOTALT: {total_fixes} fixar applicerade")
    print("=" * 60)

if __name__ == "__main__":
    main()
