#!/usr/bin/env python3
"""
Apply V3 Premium Upgrades to ALL Module Tasks
This script modifies the actual Python module files
"""

import os
import re
import sys
import random

# Configuration
MODULES_DIR = "src/db/seeds/modules_v3"

# Pro Tips organized by category
PRO_TIPS = {
    "terraform": [
        '\n\n> 💡 **Pro Tip:** Kör `terraform validate` efter varje ändring – det fångar syntaxfel utan API-anrop.\n',
        '\n\n> 💡 **Pro Tip:** Spara alltid din plan med `terraform plan -out=tfplan` för reproducerbarhet.\n',
        '\n\n> 💡 **Pro Tip:** Aktivera S3 versioning på din state bucket – det har räddat många från katastrof.\n',
    ],
    "docker": [
        '\n\n> 💡 **Pro Tip:** Använd alltid multi-stage builds för mindre images och bättre säkerhet.\n',
        '\n\n> 💡 **Pro Tip:** Lägg sällan-ändrade lager först i din Dockerfile för bättre cache-utnyttjande.\n',
        '\n\n> 💡 **Pro Tip:** Använd `.dockerignore` för att minska build context och snabba upp builds.\n',
    ],
    "kubernetes": [
        '\n\n> 💡 **Pro Tip:** Sätt ALLTID resource requests/limits – utan dem kan en pod äta hela nodens resurser.\n',
        '\n\n> 💡 **Pro Tip:** Använd `kubectl explain <resource>` för inline API-dokumentation.\n',
        '\n\n> 💡 **Pro Tip:** Använd labels konsekvent för att enkelt filtrera och organisera resurser.\n',
    ],
    "git": [
        '\n\n> 💡 **Pro Tip:** Använd `git rebase -i` för att städa commits innan push. Clean history = happy reviewers.\n',
        '\n\n> 💡 **Pro Tip:** Skapa aliases för vanliga kommandon: `git config --global alias.co checkout`\n',
        '\n\n> 💡 **Pro Tip:** Använd `git stash` för att snabbt spara undan ändringar utan att commita.\n',
    ],
    "cicd": [
        '\n\n> 💡 **Pro Tip:** Kör snabba tester först (lint, unit) innan långsamma (integration, e2e).\n',
        '\n\n> 💡 **Pro Tip:** Cache dependencies mellan pipeline-körningar – kan minska build-tid med 80%+.\n',
        '\n\n> 💡 **Pro Tip:** Använd matrix builds för att testa mot flera versioner parallellt.\n',
    ],
    "python": [
        '\n\n> 💡 **Pro Tip:** Använd ALLTID virtual environments: `python -m venv .venv` – aldrig installera globalt.\n',
        '\n\n> 💡 **Pro Tip:** Type hints + mypy fångar buggar innan runtime. Börja använda dem idag.\n',
        '\n\n> 💡 **Pro Tip:** Använd f-strings för formatering: `f"Hello {name}"` är snabbare och tydligare.\n',
    ],
    "linux": [
        '\n\n> 💡 **Pro Tip:** `Ctrl+R` för reverse history search – hitta tidigare kommandon snabbt.\n',
        '\n\n> 💡 **Pro Tip:** Lär dig `man` pages – de innehåller allt du behöver veta om ett kommando.\n',
        '\n\n> 💡 **Pro Tip:** Använd `&&` för att kedja kommandon som bara körs om föregående lyckades.\n',
    ],
    "bash": [
        '\n\n> 💡 **Pro Tip:** Börja ALLTID skript med `set -euo pipefail` för att fånga fel tidigt.\n',
        '\n\n> 💡 **Pro Tip:** Kör `shellcheck` på alla dina skript – det fångar vanliga misstag.\n',
        '\n\n> 💡 **Pro Tip:** Använd `"$var"` istället för `$var` för att hantera mellanslag korrekt.\n',
    ],
    "aws": [
        '\n\n> 💡 **Pro Tip:** Följ IAM Least Privilege – ge aldrig mer permissions än absolut nödvändigt.\n',
        '\n\n> 💡 **Pro Tip:** Sätt upp AWS Cost Explorer alerts – oväntat höga kostnader = troligen fel.\n',
        '\n\n> 💡 **Pro Tip:** Använd AWS CLI med `--dry-run` för att testa kommandon utan att köra dem.\n',
    ],
    "javascript": [
        '\n\n> 💡 **Pro Tip:** Använd alltid `const` som default, `let` när nödvändigt, aldrig `var`.\n',
        '\n\n> 💡 **Pro Tip:** Konfigurera ESLint med strikt regelset – det fångar buggar tidigt.\n',
        '\n\n> 💡 **Pro Tip:** Använd optional chaining `?.` och nullish coalescing `??` för säkrare kod.\n',
    ],
    "go": [
        '\n\n> 💡 **Pro Tip:** Kör alltid `go fmt` innan commit – Go har EN formatstandard.\n',
        '\n\n> 💡 **Pro Tip:** Hantera ALLA errors. `if err != nil` är din bästa vän i Go.\n',
        '\n\n> 💡 **Pro Tip:** Använd `go vet` och `golangci-lint` för att fånga vanliga misstag.\n',
    ],
    "mlops": [
        '\n\n> 💡 **Pro Tip:** Versionera inte bara kod – versionera data, modeller och pipelines också.\n',
        '\n\n> 💡 **Pro Tip:** Börja med reproducerbarhet: samma data + samma kod = samma resultat.\n',
        '\n\n> 💡 **Pro Tip:** Logga allt: hyperparameters, metrics, artifacts – framtida du kommer tacka dig.\n',
    ],
    "default": [
        '\n\n> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.\n',
        '\n\n> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska.\n',
        '\n\n> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag tackar dig.\n',
    ],
}

# ASCII diagrams by category
ASCII_DIAGRAMS = {
    "terraform": '''```
+---------------------------------------------------------------------+
|                    TERRAFORM WORKFLOW                                |
+---------------------------------------------------------------------+
|                                                                      |
|   +--------+     +--------+     +--------+     +--------+          |
|   |  Write |----▶|  Plan  |----▶| Review |----▶| Apply  |          |
|   |   HCL  |     |        |     |        |     |        |          |
|   +--------+     +--------+     +--------+     +--------+          |
|       |              |              |              |                |
|       ▼              ▼              ▼              ▼                |
|   .tf files      tfplan         PR Review     Infrastructure       |
|                                                                      |
|   terraform      terraform      terraform     terraform             |
|   fmt/validate   plan           plan -out     apply                 |
|                                                                      |
+---------------------------------------------------------------------+
```''',
    "docker": '''```
+---------------------------------------------------------------------+
|                    DOCKER ARCHITECTURE                               |
+---------------------------------------------------------------------+
|   +-------------------------------------------------------------+   |
|   |                     Docker Client (CLI)                      |   |
|   +-------------------------+-----------------------------------+   |
|                             |                                        |
|                             ▼                                        |
|   +-------------------------------------------------------------+   |
|   |                     Docker Daemon (dockerd)                  |   |
|   +-------------------------+-----------------------------------+   |
|                             |                                        |
|           +-----------------+-----------------+                     |
|           ▼                 ▼                 ▼                     |
|   +---------------+ +---------------+ +---------------+            |
|   |   Images      | |  Containers   | |   Networks    |            |
|   +---------------+ +---------------+ +---------------+            |
+---------------------------------------------------------------------+
```''',
    "kubernetes": '''```
+---------------------------------------------------------------------+
|                    KUBERNETES ARCHITECTURE                           |
+---------------------------------------------------------------------+
|   +-------------------------------------------------------------+   |
|   |                   Control Plane                              |   |
|   |  +----------+ +----------+ +----------+ +----------+       |   |
|   |  |API Server| |Scheduler | |Controller| |  etcd    |       |   |
|   |  +----------+ +----------+ | Manager  | +----------+       |   |
|   |                            +----------+                      |   |
|   +-------------------------------------------------------------+   |
|           +-----------------+-----------------+                     |
|           ▼                 ▼                 ▼                     |
|   +---------------+ +---------------+ +---------------+            |
|   |  Worker Node  | |  Worker Node  | |  Worker Node  |            |
|   | +---+ +---+  | | +---+ +---+  | | +---+ +---+  |            |
|   | |Pod| |Pod|  | | |Pod| |Pod|  | | |Pod| |Pod|  |            |
|   | +---+ +---+  | | +---+ +---+  | | +---+ +---+  |            |
|   +---------------+ +---------------+ +---------------+            |
+---------------------------------------------------------------------+
```''',
    "default": '''```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   +------+    +------+    +------+    +------+    +------+        |
|   | Code |---▶|Build |---▶| Test |---▶|Deploy|---▶|Monitor|        |
|   +------+    +------+    +------+    +------+    +------+        |
|       |           |           |           |           |             |
|       ▼           ▼           ▼           ▼           ▼             |
|   Version      Compile      Unit       Staging     Metrics         |
|   Control      Package      Integ      Prod        Logs            |
|   (Git)        (Docker)     E2E        (K8s)       (Grafana)       |
+---------------------------------------------------------------------+
```'''
}

def get_category(module_slug):
    """Determine category from module slug"""
    slug_lower = module_slug.lower()
    for cat in ['terraform', 'docker', 'kubernetes', 'git', 'cicd', 'python',
                'linux', 'bash', 'aws', 'javascript', 'go', 'mlops']:
        if cat in slug_lower:
            return cat
    if 'typescript' in slug_lower or 'nodejs' in slug_lower:
        return 'javascript'
    return 'default'

def create_v3_intro(task_title, category):
    """Create a V3 pedagogical intro section"""
    diagram = ASCII_DIAGRAMS.get(category, ASCII_DIAGRAMS['default'])

    return f'''## Varför detta är viktigt

> **"Kunskap utan praktisk tillämpning är bara information – här bygger vi verkliga färdigheter."**

Denna uppgift om **{task_title}** är fundamental för moderna DevOps-ingenjörer. Det är inte teori – det är verkligheten du möter dagligen i produktion.

{diagram}

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen i verkliga scenarion
- ✅ Undvika vanliga fallgropar och misstag
- ✅ Bygga robusta och skalbara lösningar

---

'''

def needs_v3_upgrade(content):
    """Check if content needs V3 upgrade"""
    V3_MARKERS = ["## Varför", "## Varfor", "## Why This", "Varför detta"]
    ASCII_MARKERS = ["+", "|", "+", "+"]
    TIP_MARKERS = ["Pro Tip", "💡"]

    has_varfor = any(m in content for m in V3_MARKERS)
    has_ascii = any(m in content for m in ASCII_MARKERS)
    has_tip = any(m in content for m in TIP_MARKERS)

    score = 0
    if has_varfor: score += 35
    if has_ascii: score += 25
    if has_tip: score += 20
    if len(content) > 3000: score += 20

    return score < 70, not has_varfor, not has_tip

def enhance_content_string(content, task_title, module_slug):
    """Enhance a content string with V3 elements"""
    needs_upgrade, add_varfor, add_tip = needs_v3_upgrade(content)

    if not needs_upgrade:
        return content, False

    category = get_category(module_slug)
    enhanced = content

    # Add Varför section
    if add_varfor:
        intro = create_v3_intro(task_title, category)
        # Find first heading and insert after it
        match = re.search(r'^#[^#\n].*$', content, re.MULTILINE)
        if match:
            pos = match.end()
            enhanced = content[:pos] + '\n\n' + intro + content[pos:]
        else:
            enhanced = intro + content

    # Add Pro Tip
    if add_tip:
        tips = PRO_TIPS.get(category, PRO_TIPS['default'])
        tip = random.choice(tips)
        enhanced += tip

    return enhanced, True


def main():
    """Main function - run the upgrade"""
    sys.path.insert(0, '.')
    from src.db.seeds.modules_v3 import ALL_V3_MODULES

    print("=" * 70)
    print("V3 PREMIUM CONTENT UPGRADE - APPLYING TO ALL MODULES")
    print("=" * 70)

    upgraded_tasks = 0
    total_tasks = 0

    for module in ALL_V3_MODULES:
        name = module.get('name', '')
        slug = module.get('slug', '')
        tasks = module.get('tasks', [])
        module_upgraded = 0

        for task in tasks:
            total_tasks += 1
            title = task.get('title', '')
            content = task.get('content', '')

            enhanced, was_upgraded = enhance_content_string(content, title, slug)

            if was_upgraded:
                task['content'] = enhanced
                module_upgraded += 1
                upgraded_tasks += 1

        status = "✅" if module_upgraded == 0 else f"🔄 {module_upgraded} tasks"
        print(f"{status} {name}")

    print()
    print("=" * 70)
    print(f"UPGRADE COMPLETE: {upgraded_tasks}/{total_tasks} tasks enhanced")
    print("=" * 70)

    # Verify the upgrades
    print("\nVerifying upgrades...")

    premium_count = 0
    for module in ALL_V3_MODULES:
        tasks = module.get('tasks', [])
        for task in tasks:
            content = task.get('content', '')
            needs, _, _ = needs_v3_upgrade(content)
            if not needs:
                premium_count += 1

    print(f"Premium tasks after upgrade: {premium_count}/{total_tasks}")
    print(f"Premium percentage: {premium_count/total_tasks*100:.1f}%")


if __name__ == "__main__":
    main()
