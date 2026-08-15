import glob
import re
import json
import os

def parse_markdown_quiz(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the Quiz section
    # Usually starts with ## DEL 2: 50 QUIZ-FRÅGOR or similar
    quiz_section_match = re.search(r'## DEL 2:.*?(\n.*?)(?=## DEL 3|---|$)', content, re.DOTALL)
    if not quiz_section_match:
        return []

    quiz_text = quiz_section_match.group(1)

    # Parse questions
    # Format:
    # 1. **Question?**
    #    A) ...
    #    B) ...
    questions = []

    # Split by lines starting with number dot (e.g. "1. ")
    # But wait, looking at the file, it's "1. **...**"

    # Flexible regex for splitting questions
    # We look for a line starting with digit(s) + dot + space + **
    parts = re.split(r'\n(\d+\.\s+\*\*.*?\*\*)', '\n' + quiz_text)

    # parts[0] is preamble/empty
    # parts[1] is Q1 title
    # parts[2] is Q1 body (options)
    # parts[3] is Q2 title...

    for i in range(1, len(parts), 2):
        if i+1 >= len(parts): break

        q_title_raw = parts[i].strip()
        q_body_raw = parts[i+1]

        # Clean title: "1. **Question**" -> "Question"
        q_text = re.sub(r'^\d+\.\s+\*\*(.*?)\*\*.*', r'\1', q_title_raw)

        # Extract options
        # Look for A) ... B) ...
        # Regex for options: line starting with space + letter + ) or letter + )
        options_found = re.findall(r'^\s*([A-D])\)\s+(.*)', q_body_raw, re.MULTILINE)

        # Structure options as list of strings
        # We need to map 'A', 'B', 'C', 'D' to 0, 1, 2, 3
        # But wait, regex returns [('A', 'Text'), ('B', 'Text')]

        # Sometimes questions might have 3 or 5 options? Standard is 4.

        q_obj = {
            "id": (i // 2) + 1,
            "question": q_text,
            "raw_options": options_found # List of tuples (Letter, Text)
        }
        questions.append(q_obj)

    return questions

files = sorted(glob.glob("Omtenta/Nod*_Master.md"))
all_data = {}

for f in files:
    filename = os.path.basename(f)
    print(f"Processing {filename}...")
    qs = parse_markdown_quiz(f)
    all_data[filename] = qs

with open("quiz_audit.json", "w", encoding='utf-8') as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)

print("Done. Saved to quiz_audit.json")
