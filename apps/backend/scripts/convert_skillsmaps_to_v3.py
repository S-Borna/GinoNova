#!/usr/bin/env python3
"""
=============================================================================
SKILLSMAPS -> BOOTCAMP V3 CONVERTER
=============================================================================

Converts all skillsmap files (node-based format) to bootcamp_v3 format
(module with embedded tasks).

Source format (skillsmap):
    NODE_01 = {
        "node_id": 1,
        "title": "Docker Intro",
        "content": "..."
    }

Target format (bootcamp_v3):
    {
        "track_slug": "containers",
        "name": "Docker Mastery",
        "tasks": [
            {
                "title": "Docker Intro",
                "difficulty": "easy",
                "estimated_minutes": 45,
                "xp_reward": 100,
                "content": "..."
            }
        ]
    }

Usage:
    python scripts/convert_skillsmaps_to_v3.py

Output:
    Creates src/db/seeds/modules_v3/ directory with converted modules
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Any

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# =============================================================================
# TRACK MAPPINGS
# =============================================================================

SKILLSMAP_TO_TRACK = {
    # Foundation track
    "linux": "foundation",
    "bash": "foundation",
    "git": "foundation",
    "python": "foundation",

    # Cloud & Infrastructure track
    "aws": "cloud-infrastructure",
    "terraform": "cloud-infrastructure",
    "ansible": "cloud-infrastructure",

    # Containers & Orchestration track
    "docker": "containers-orchestration",
    "kubernetes": "containers-orchestration",

    # Platform Engineering track
    "cicd": "platform-engineering",
    "observability": "platform-engineering",
    "sre": "platform-engineering",

    # Advanced/Specialty tracks (new)
    "mlops": "advanced-specialty",
    "system_design": "advanced-specialty",
    "sql": "advanced-specialty",
    "nodejs": "advanced-specialty",
    "javascript": "advanced-specialty",
    "typescript": "advanced-specialty",
    "go": "advanced-specialty",
    "prompt_engineering": "advanced-specialty",
}

# Difficulty mapping based on node position
def get_difficulty(order_index: int, total_nodes: int) -> str:
    """Map node position to difficulty level."""
    progress = order_index / total_nodes
    if progress < 0.25:
        return "easy"
    elif progress < 0.5:
        return "medium"
    elif progress < 0.75:
        return "hard"
    else:
        return "expert"


def get_xp_reward(difficulty: str, estimated_minutes: int) -> int:
    """Calculate XP reward based on difficulty and time."""
    base_xp = {
        "easy": 25,
        "medium": 50,
        "hard": 75,
        "expert": 100,
    }
    time_bonus = estimated_minutes // 10 * 5
    return base_xp.get(difficulty, 50) + time_bonus


# =============================================================================
# CONTENT TRANSFORMER
# =============================================================================

def enhance_content_with_v3_structure(content: str, module_name: str) -> str:
    """
    Enhance content with bootcamp_v3 pedagogical structure if missing.
    Adds OS-specific sections, prerequisites, etc.
    """
    # Check if content already has the structure
    if "## Varför detta är viktigt" in content:
        return content

    # Check if it's already well-structured markdown
    if content.strip().startswith("#") and "```" in content:
        # Content is already structured, just ensure it has sections
        lines = content.split("\n")
        title_line = lines[0] if lines else f"# {module_name}"
        rest = "\n".join(lines[1:]) if len(lines) > 1 else ""

        # Only add structure if it's very minimal
        if len(content) < 500:
            enhanced = f"""{title_line}

## Varför detta är viktigt
Denna kunskap är fundamental för moderna DevOps-praktiker och kommer användas dagligen i ditt arbete.

## Vad du kommer lära dig
- Förstå grundläggande koncept
- Praktiska kommandon och verktyg
- Best practices för produktion

{rest}

## Sammanfattning
Öva dessa koncept regelbundet för att bygga muskelminne.

## Nästa steg
Fortsätt till nästa lektion för att fördjupa dina kunskaper.
"""
            return enhanced

    return content


# =============================================================================
# SKILLSMAP PARSERS
# =============================================================================

def parse_single_file_skillsmap(filepath: Path) -> dict | None:
    """Parse a single-file skillsmap (e.g., docker_skillsmap.py)."""
    try:
        content = filepath.read_text(encoding="utf-8")

        # Extract module info
        info_match = re.search(
            r'(\w+_SKILLSMAP_INFO|SKILLSMAP_INFO)\s*=\s*\{([^}]+)\}',
            content,
            re.DOTALL
        )

        module_info = {}
        if info_match:
            info_str = "{" + info_match.group(2) + "}"
            # Safe eval for dict
            try:
                # Clean up the string for eval
                clean_str = re.sub(r'#.*$', '', info_str, flags=re.MULTILINE)
                module_info = eval(clean_str)
            except:
                pass

        # Extract nodes
        nodes = []

        # Pattern for NODE_XX = {...}
        node_pattern = re.compile(
            r'NODE_(\d+)_\w+\s*=\s*\{',
            re.MULTILINE
        )

        # Alternative: nodes in list format
        list_pattern = re.compile(
            r'(\w+_NODES|\w+_BLOCK_\d+)\s*=\s*\[',
            re.MULTILINE
        )

        # Try to import and extract
        module_name = filepath.stem
        try:
            # Dynamic import
            import importlib.util
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Look for ALL_NODES or similar
            for attr_name in dir(module):
                if 'NODE' in attr_name.upper() and isinstance(getattr(module, attr_name), (list, dict)):
                    obj = getattr(module, attr_name)
                    if isinstance(obj, list) and len(obj) > 0:
                        nodes.extend(obj)
                    elif isinstance(obj, dict) and 'content' in obj:
                        nodes.append(obj)

                if 'INFO' in attr_name.upper() and isinstance(getattr(module, attr_name), dict):
                    module_info = getattr(module, attr_name)

        except Exception as e:
            print(f"  Warning: Could not import {filepath.name}: {e}")
            return None

        if not nodes:
            print(f"  Warning: No nodes found in {filepath.name}")
            return None

        return {
            "info": module_info,
            "nodes": nodes,
            "source": str(filepath),
        }

    except Exception as e:
        print(f"  Error parsing {filepath}: {e}")
        return None


def parse_directory_skillsmap(dirpath: Path) -> dict | None:
    """Parse a directory-based skillsmap (e.g., mlops/)."""
    try:
        init_file = dirpath / "__init__.py"
        if not init_file.exists():
            return None

        # Import the package
        import importlib.util

        # First, import all block files
        nodes = []
        module_info = {}

        for block_file in sorted(dirpath.glob("block_*.py")):
            try:
                spec = importlib.util.spec_from_file_location(
                    block_file.stem, block_file
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Look for BLOCK_X_NODES
                for attr_name in dir(module):
                    if 'BLOCK' in attr_name.upper() and 'NODE' in attr_name.upper():
                        obj = getattr(module, attr_name)
                        if isinstance(obj, list):
                            nodes.extend(obj)
            except Exception as e:
                print(f"    Warning: Could not load {block_file.name}: {e}")

        # Load __init__.py for metadata
        try:
            spec = importlib.util.spec_from_file_location("__init__", init_file)
            init_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(init_module)

            if hasattr(init_module, 'SKILLSMAP_METADATA'):
                module_info = init_module.SKILLSMAP_METADATA
            if hasattr(init_module, 'ALL_NODES'):
                nodes = init_module.ALL_NODES

        except Exception as e:
            print(f"    Warning: Could not load __init__.py: {e}")

        if not nodes:
            print(f"  Warning: No nodes found in {dirpath.name}/")
            return None

        return {
            "info": module_info,
            "nodes": nodes,
            "source": str(dirpath),
        }

    except Exception as e:
        print(f"  Error parsing {dirpath}: {e}")
        return None


# =============================================================================
# V3 MODULE GENERATOR
# =============================================================================

def convert_to_v3_module(skillsmap_data: dict, skillsmap_name: str) -> dict:
    """Convert parsed skillsmap data to bootcamp_v3 module format."""

    info = skillsmap_data.get("info", {})
    nodes = skillsmap_data.get("nodes", [])

    # Determine track
    track_slug = SKILLSMAP_TO_TRACK.get(skillsmap_name, "advanced-specialty")

    # Module metadata
    module_name = info.get("name") or info.get("title") or skillsmap_name.replace("_", " ").title()
    module_slug = info.get("slug") or skillsmap_name.replace("_", "-").lower()
    module_desc = info.get("description") or f"Master {module_name} from fundamentals to production"
    estimated_hours = info.get("estimated_hours") or len(nodes) * 0.5

    # Convert nodes to tasks
    tasks = []
    total_nodes = len(nodes)

    for idx, node in enumerate(nodes):
        order_index = idx + 1

        # Extract node data (handle different formats)
        if isinstance(node, dict):
            title = node.get("title") or node.get("name") or f"Task {order_index}"
            content = node.get("content") or ""
            est_minutes = node.get("estimated_minutes") or 30
            xp = node.get("xp_reward") or 50
            node_difficulty = node.get("difficulty")
        else:
            continue

        # Calculate difficulty if not specified
        if not node_difficulty:
            node_difficulty = get_difficulty(order_index, total_nodes)

        # Map difficulty strings
        difficulty_map = {
            "easy": "easy",
            "beginner": "easy",
            "medium": "medium",
            "intermediate": "medium",
            "hard": "hard",
            "advanced": "hard",
            "expert": "expert",
        }
        difficulty = difficulty_map.get(node_difficulty, "medium")

        # Calculate XP if not specified
        if not xp or xp < 10:
            xp = get_xp_reward(difficulty, est_minutes)

        # Enhance content with v3 structure
        enhanced_content = enhance_content_with_v3_structure(content, title)

        tasks.append({
            "title": title,
            "difficulty": difficulty,
            "estimated_minutes": est_minutes,
            "xp_reward": xp,
            "content": enhanced_content,
        })

    # Build v3 module
    v3_module = {
        "track_slug": track_slug,
        "order_index": 100,  # Will be adjusted when integrating
        "name": module_name,
        "slug": module_slug,
        "description": module_desc,
        "difficulty": info.get("difficulty", "intermediate"),
        "estimated_hours": estimated_hours,
        "prerequisites": info.get("prerequisites", []),
        "tasks": tasks,
        "labs": [],  # Can be added later
        "project": None,  # Can be added later
    }

    return v3_module


def generate_v3_python_file(module: dict, output_path: Path):
    """Generate a Python file in bootcamp_v3 format."""

    # Escape triple quotes in content
    def escape_content(content: str) -> str:
        return content.replace('"""', '\\"\\"\\"')

    # Build tasks string
    tasks_str = ""
    for task in module["tasks"]:
        escaped_content = escape_content(task["content"])
        tasks_str += f'''
            {{
                "title": "{task['title']}",
                "difficulty": "{task['difficulty']}",
                "estimated_minutes": {task['estimated_minutes']},
                "xp_reward": {task['xp_reward']},
                "content": """{escaped_content}"""
            }},'''

    # Generate file content
    file_content = f'''"""
{module['name']} - Bootcamp v3 Format
Auto-converted from skillsmap format.

Track: {module['track_slug']}
Tasks: {len(module['tasks'])}
Estimated Hours: {module['estimated_hours']}
"""

MODULE_{module['slug'].upper().replace('-', '_')} = {{
    "track_slug": "{module['track_slug']}",
    "order_index": {module['order_index']},
    "name": "{module['name']}",
    "slug": "{module['slug']}",
    "description": """{module['description']}""",
    "difficulty": "{module['difficulty']}",
    "estimated_hours": {module['estimated_hours']},
    "prerequisites": {module['prerequisites']},
    "tasks": [{tasks_str}
    ],
    "labs": [],
}}


def get_module():
    """Returns the module definition."""
    return MODULE_{module['slug'].upper().replace('-', '_')}


def get_tasks():
    """Returns all tasks for this module."""
    return MODULE_{module['slug'].upper().replace('-', '_')}["tasks"]


def get_task_count():
    """Returns the number of tasks."""
    return len(get_tasks())
'''

    output_path.write_text(file_content, encoding="utf-8")


# =============================================================================
# MAIN CONVERTER
# =============================================================================

def main():
    """Main conversion process."""
    print("=" * 70)
    print("SKILLSMAPS -> BOOTCAMP V3 CONVERTER")
    print("=" * 70)

    # Paths
    base_path = Path(__file__).parent.parent
    skillsmaps_path = base_path / "src" / "db" / "seeds" / "skillsmaps"
    output_path = base_path / "src" / "db" / "seeds" / "modules_v3"

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"\nSource: {skillsmaps_path}")
    print(f"Output: {output_path}")
    print()

    converted = []
    failed = []

    # Process single-file skillsmaps
    print("Processing single-file skillsmaps...")
    for filepath in sorted(skillsmaps_path.glob("*_skillsmap.py")):
        name = filepath.stem.replace("_skillsmap", "")
        print(f"  -> {name}...", end=" ")

        data = parse_single_file_skillsmap(filepath)
        if data:
            v3_module = convert_to_v3_module(data, name)
            output_file = output_path / f"module_{name}.py"
            generate_v3_python_file(v3_module, output_file)
            converted.append({
                "name": name,
                "tasks": len(v3_module["tasks"]),
                "file": output_file.name,
            })
            print(f"✅ {len(v3_module['tasks'])} tasks")
        else:
            failed.append(name)
            print("❌ Failed")

    # Process directory-based skillsmaps
    print("\nProcessing directory-based skillsmaps...")
    for dirpath in sorted(skillsmaps_path.iterdir()):
        if dirpath.is_dir() and dirpath.name != "__pycache__":
            name = dirpath.name
            print(f"  -> {name}/...", end=" ")

            data = parse_directory_skillsmap(dirpath)
            if data:
                v3_module = convert_to_v3_module(data, name)
                output_file = output_path / f"module_{name}.py"
                generate_v3_python_file(v3_module, output_file)
                converted.append({
                    "name": name,
                    "tasks": len(v3_module["tasks"]),
                    "file": output_file.name,
                })
                print(f"✅ {len(v3_module['tasks'])} tasks")
            else:
                failed.append(name)
                print("❌ Failed")

    # Generate __init__.py
    init_content = '''"""
Bootcamp v3 Modules - Auto-converted from Skillsmaps
"""

# Import all converted modules
'''

    for item in converted:
        module_var = f"MODULE_{item['name'].upper()}"
        init_content += f"from .module_{item['name']} import {module_var}\n"

    init_content += "\n\n# All modules list\nALL_V3_MODULES = [\n"
    for item in converted:
        module_var = f"MODULE_{item['name'].upper()}"
        init_content += f"    {module_var},\n"
    init_content += "]\n"

    init_content += f"\n\ndef get_all_modules():\n    return ALL_V3_MODULES\n"
    init_content += f"\n\ndef get_module_count():\n    return len(ALL_V3_MODULES)\n"
    init_content += f"\n\ndef get_total_tasks():\n    return sum(len(m['tasks']) for m in ALL_V3_MODULES)\n"

    (output_path / "__init__.py").write_text(init_content, encoding="utf-8")

    # Summary
    print("\n" + "=" * 70)
    print("CONVERSION COMPLETE")
    print("=" * 70)
    print(f"\n✅ Converted: {len(converted)} modules")
    for item in converted:
        print(f"   • {item['name']}: {item['tasks']} tasks -> {item['file']}")

    if failed:
        print(f"\n❌ Failed: {len(failed)} modules")
        for name in failed:
            print(f"   • {name}")

    total_tasks = sum(item["tasks"] for item in converted)
    print(f"\n📊 Total: {len(converted)} modules, {total_tasks} tasks")
    print(f"📁 Output: {output_path}")

    return len(converted), len(failed)


if __name__ == "__main__":
    success, failed = main()
    sys.exit(0 if failed == 0 else 1)
