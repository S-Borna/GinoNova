"""
V2 to Content Blocks Converter
==============================
Converts V2 skillsmap format to content_blocks format for ILE rendering.
"""

import random
from typing import Any


def convert_v2_section_to_blocks(section: dict) -> list[dict]:
    """Convert a single V2 section to content_blocks format."""
    blocks = []
    section_type = section.get("type")
    content = section.get("content", {})

    if section_type == "intro":
        blocks.extend(_convert_intro(content))
    elif section_type == "concepts":
        blocks.extend(_convert_concepts(content))
    elif section_type == "practice":
        blocks.extend(_convert_practice(content))
    elif section_type == "quiz":
        blocks.extend(_convert_quiz(content))
    elif section_type == "challenge":
        blocks.extend(_convert_challenge(content))

    return blocks


def _convert_intro(content: dict) -> list[dict]:
    """Convert intro section to content blocks."""
    blocks = []

    # Headline as header
    if content.get("headline"):
        blocks.append({
            "type": "text",
            "content": f"# {content['headline']}"
        })

    # Hook as engaging text
    if content.get("hook"):
        blocks.append({
            "type": "text",
            "content": f"> 💡 {content['hook']}"
        })

    # Learning objectives
    if content.get("learning_objectives"):
        objectives = "\n".join([f"- {obj}" for obj in content["learning_objectives"]])
        blocks.append({
            "type": "text",
            "content": f"## 🎯 Vad du kommer lära dig\n\n{objectives}"
        })

    # Prerequisites
    if content.get("prerequisites"):
        prereqs = ", ".join(content["prerequisites"])
        blocks.append({
            "type": "text",
            "content": f"**Förkunskaper:** {prereqs}"
        })

    # Estimated time and XP
    time_xp = []
    if content.get("estimated_time"):
        time_xp.append(f"⏱️ {content['estimated_time']}")
    if content.get("xp_reward"):
        time_xp.append(f"⭐ {content['xp_reward']} XP")
    if time_xp:
        blocks.append({
            "type": "text",
            "content": " | ".join(time_xp)
        })

    return blocks


def _convert_concepts(content: dict) -> list[dict]:
    """Convert concepts section to content blocks."""
    blocks = []

    concepts = content.get("concepts", [])
    for concept in concepts:
        # Title
        if concept.get("title"):
            blocks.append({
                "type": "text",
                "content": f"## {concept['title']}"
            })

        # Explanation
        if concept.get("explanation"):
            blocks.append({
                "type": "text",
                "content": concept["explanation"]
            })

        # Diagram (as code block)
        if concept.get("diagram"):
            blocks.append({
                "type": "code",
                "language": "text",
                "code": concept["diagram"],
                "filename": "diagram"
            })

        # Pro tip
        if concept.get("pro_tip"):
            blocks.append({
                "type": "text",
                "content": f"💡 **Pro tip:** {concept['pro_tip']}"
            })

        # Common mistake
        if concept.get("common_mistake"):
            blocks.append({
                "type": "text",
                "content": f"⚠️ **Vanligt misstag:** {concept['common_mistake']}"
            })

    return blocks


def _convert_practice(content: dict) -> list[dict]:
    """Convert practice section to content blocks with terminal exercises."""
    blocks = []

    blocks.append({
        "type": "text",
        "content": "## 🛠️ Praktiska Övningar"
    })

    exercises = content.get("exercises", [])
    for i, exercise in enumerate(exercises, 1):
        # Task description
        task = exercise.get("task", f"Övning {i}")
        instruction = exercise.get("instruction", "")

        blocks.append({
            "type": "text",
            "content": f"### Övning {i}: {task}\n\n{instruction}"
        })

        # Terminal block for the exercise
        expected_cmd = exercise.get("expected_command", "")
        hint = exercise.get("hint", "")

        blocks.append({
            "type": "terminal",
            "title": task,
            "description": instruction,
            "expected_commands": [expected_cmd] if expected_cmd else [],
            "hint": hint,
            "allow_any_command": True
        })

    return blocks


def _convert_quiz(content: dict) -> list[dict]:
    """Convert quiz section to content blocks with randomized answers."""
    blocks = []

    blocks.append({
        "type": "text",
        "content": "## 📝 Kunskapstest"
    })

    questions = content.get("questions", {})

    # Flashcards as text blocks
    flashcards = questions.get("flashcards", [])
    if flashcards:
        blocks.append({
            "type": "text",
            "content": "### Flashcards"
        })
        for card in flashcards:
            blocks.append({
                "type": "text",
                "content": f"**Q:** {card.get('front', '')}\n\n**A:** {card.get('back', '')}"
            })

    # Multiple choice as quiz blocks with RANDOMIZED options
    mc_questions = questions.get("multiple_choice", [])
    for mc in mc_questions:
        question = mc.get("question", "")
        options = mc.get("options", [])
        correct_idx = mc.get("correct", 0)
        explanation = mc.get("explanation", "")

        # Create options with correct flag
        quiz_options = []
        for i, opt in enumerate(options):
            quiz_options.append({
                "text": opt,
                "is_correct": i == correct_idx,
                "feedback": explanation if i == correct_idx else ""
            })

        # RANDOMIZE options order
        random.shuffle(quiz_options)

        blocks.append({
            "type": "quiz",
            "question": question,
            "options": quiz_options,
            "explanation": explanation,
            "xp_bonus": 10
        })

    return blocks


def _convert_challenge(content: dict) -> list[dict]:
    """Convert challenge section to content blocks."""
    blocks = []

    blocks.append({
        "type": "text",
        "content": "## 🏆 Challenge"
    })

    # Scenario
    if content.get("scenario"):
        blocks.append({
            "type": "text",
            "content": f"**Scenario:** {content['scenario']}"
        })

    # Requirements
    if content.get("requirements"):
        reqs = "\n".join([f"- [ ] {req}" for req in content["requirements"]])
        blocks.append({
            "type": "text",
            "content": f"### Krav\n\n{reqs}"
        })

    # Hints (collapsible)
    if content.get("hints"):
        hints = "\n".join([f"- {hint}" for hint in content["hints"]])
        blocks.append({
            "type": "text",
            "content": f"<details>\n<summary>💡 Tips</summary>\n\n{hints}\n</details>"
        })

    # Terminal for challenge
    blocks.append({
        "type": "terminal",
        "title": "Challenge Terminal",
        "description": "Lös challengen i terminalen",
        "allow_any_command": True
    })

    # Solution (hidden)
    if content.get("solution"):
        blocks.append({
            "type": "text",
            "content": f"<details>\n<summary>📖 Lösning</summary>\n\n```bash\n{content['solution']}\n```\n</details>"
        })

    return blocks


def convert_v2_node_to_task(node: dict) -> dict:
    """Convert a full V2 node to task format with content_blocks."""
    content_blocks = []

    for section in node.get("sections", []):
        content_blocks.extend(convert_v2_section_to_blocks(section))

    return {
        "title": node.get("title", ""),
        "slug": node.get("slug", ""),
        "description": node.get("description", ""),
        "difficulty": node.get("difficulty", "intermediate"),
        "estimated_minutes": node.get("estimated_minutes", 30),
        "xp_reward": node.get("xp_reward", 100),
        "content": "",  # Legacy markdown - empty for V2
        "content_blocks": content_blocks,
        "requirements": [],
        "task_tier": "premium",
    }


def load_v2_linux_nodes() -> list[dict]:
    """Load all Linux V2 nodes and convert to tasks."""
    from .linux import ALL_LINUX_V2_NODES
    return [convert_v2_node_to_task(node) for node in ALL_LINUX_V2_NODES]


def load_v2_azure_nodes() -> list[dict]:
    """Load all Azure V2 nodes and convert to tasks."""
    from .azure import ALL_AZURE_V2_NODES
    return [convert_v2_node_to_task(node) for node in ALL_AZURE_V2_NODES]
