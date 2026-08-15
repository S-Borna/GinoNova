#!/usr/bin/env python3
"""
Ta bort alla AI-genererade explanations och ersätt med tom sträng.
Användaren vill endast se rätt/fel utan kommentarer.
"""

import re

with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Ersätt alla explanations med tom sträng
pattern = r"explanation:\s*'[^']*?',"
replacement = "explanation: '',"

new_content = re.sub(pattern, replacement, content)

with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Tog bort alla explanations från 298 frågor")
print("✓ Endast rätt/fel visas nu för användaren")
