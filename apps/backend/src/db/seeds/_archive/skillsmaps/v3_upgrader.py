#!/usr/bin/env python3
"""
V3 Content Upgrader
Automatiskt uppgraderar SkillsMap-innehåll till V3-standard.
"""

import re

V3_INTRO_TEMPLATE = '''## Varför detta är viktigt

{motivation}

## Vad du kommer lära dig

{learning_objectives}

---

'''

V3_PRACTICAL_TEMPLATE = '''

---

## ✅ Praktisk Övning

### Uppgift
{task_description}

### Verifiera
{verification}

### Vanliga problem

**Problem:** {common_problem}
**Lösning:** {solution}

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
{summary_points}

### Nästa steg
{next_step}
'''


def upgrade_to_v3(content: str, title: str, next_topic: str = "nästa koncept") -> str:
    """
    Uppgraderar befintligt innehåll till V3-standard.
    """
    # Check if already V3
    if "## Varför detta är viktigt" in content and "## Vad du kommer lära dig" in content:
        return content  # Already V3

    # Försök hitta befintlig motivation
    lines = content.split('\n')
    new_lines = []
    found_first_h2 = False

    for i, line in enumerate(lines):
        # Lägg till V3-intro efter första H1
        if line.startswith('# ') and not found_first_h2:
            new_lines.append(line)
            new_lines.append('')
            new_lines.append('## Varför detta är viktigt')
            new_lines.append('')
            new_lines.append(f'Som DevOps-ingenjör behöver du behärska {title.lower()} för att automatisera och effektivisera ditt dagliga arbete.')
            new_lines.append('')
            new_lines.append('## Vad du kommer lära dig')
            new_lines.append('')
            new_lines.append(f'- Förstå grundläggande koncept inom {title.lower()}')
            new_lines.append('- Implementera praktiska lösningar')
            new_lines.append('- Tillämpa best practices')
            new_lines.append('- Felsöka vanliga problem')
            new_lines.append('')
            new_lines.append('---')
            found_first_h2 = True
            continue

        new_lines.append(line)

    # Lägg till V3-avslutning om den saknas
    result = '\n'.join(new_lines)

    if "## 🎯 Sammanfattning" not in result and "## Sammanfattning" not in result:
        result += f'''

---

## 🎯 Sammanfattning

I denna task har du lärt dig:
- ✅ Grunderna i {title.lower()}
- ✅ Praktisk implementation
- ✅ Best practices och vanliga mönster

### Nästa steg
I nästa task lär du dig om {next_topic}.
'''

    return result


if __name__ == "__main__":
    # Test
    test_content = """# Test Title

## Gamla rubriken

Lite innehåll här.

```python
code = "example"
```
"""

    upgraded = upgrade_to_v3(test_content, "Test Title", "nästa koncept")
    print(upgraded)
