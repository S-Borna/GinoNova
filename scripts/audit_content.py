#!/usr/bin/env python3
"""
Content Audit Script - DevOpsHub Content Overhaul FAS 2
Analyzes all tasks for content quality and generates report.

Usage: python scripts/audit_content.py
"""

import json
import sys
from pathlib import Path
from enum import Enum
from dataclasses import dataclass, asdict
from typing import Optional

# Add backend src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "apps" / "backend" / "src"))

from db.seeds.bootcamp_v3_data import BOOTCAMP_MODULES, BOOTCAMP_TRACKS


# =============================================================================
# GENERIC PATTERNS - Placeholder text we need to replace
# =============================================================================

GENERIC_PATTERNS = [
    "This lesson will teach you the fundamentals",
    "Follow along with the examples below",
    "Understanding the basics",
    "Practical applications",
    "Best practices",
    "You've learned the core concepts",
    "Practice these skills to reinforce",
    "Concept 1:",
    "Concept 2:",
    "Concept 3:",
    "[object Object]",
    "Lorem ipsum",
    "TODO",
    "PLACEHOLDER",
    "TBD",
    "Coming soon",
]

# Minimum content length for "complete" status
MIN_CONTENT_LENGTH = 500
MIN_CODE_BLOCKS = 1


class ContentQuality(str, Enum):
    EMPTY = "empty"           # No content at all
    GENERIC = "generic"       # Has placeholder text
    PARTIAL = "partial"       # Has some content but incomplete
    COMPLETE = "complete"     # Full pedagogical content


@dataclass
class TaskAudit:
    """Audit result for a single task."""
    module_slug: str
    module_name: str
    track_slug: str
    order_index: int
    title: str
    quality: ContentQuality
    content_length: int
    word_count: int
    code_block_count: int
    has_real_code: bool
    issues: list[str]
    priority: str  # high, medium, low


def count_code_blocks(content: str) -> int:
    """Count the number of code blocks in markdown content."""
    if not content:
        return 0
    return content.count("```")


def count_words(content: str) -> int:
    """Count words in content."""
    if not content:
        return 0
    return len(content.split())


def has_generic_patterns(content: str) -> list[str]:
    """Check for generic placeholder patterns."""
    if not content:
        return ["no_content"]
    
    found = []
    content_lower = content.lower()
    for pattern in GENERIC_PATTERNS:
        if pattern.lower() in content_lower:
            found.append(pattern)
    return found


def assess_quality(content: Optional[str]) -> tuple[ContentQuality, list[str]]:
    """Assess the quality of task content."""
    issues = []
    
    # No content at all
    if not content or len(content.strip()) < 50:
        return ContentQuality.EMPTY, ["no_content"]
    
    # Check for generic patterns
    generic_found = has_generic_patterns(content)
    if generic_found:
        issues.extend([f"generic:{p[:30]}" for p in generic_found])
    
    # Check content length
    if len(content) < MIN_CONTENT_LENGTH:
        issues.append("too_short")
    
    # Check for code blocks
    code_blocks = count_code_blocks(content)
    if code_blocks < MIN_CODE_BLOCKS * 2:  # Count ``` pairs
        issues.append("no_code_blocks")
    
    # Check for sections
    if "##" not in content:
        issues.append("no_sections")
    
    # Determine quality
    if not content or len(content.strip()) < 50:
        return ContentQuality.EMPTY, issues
    elif generic_found:
        return ContentQuality.GENERIC, issues
    elif len(issues) > 0:
        return ContentQuality.PARTIAL, issues
    else:
        return ContentQuality.COMPLETE, []


def audit_task(module: dict, task: dict, track_slug: str) -> TaskAudit:
    """Audit a single task."""
    content = task.get("content", "")
    quality, issues = assess_quality(content)
    
    # Determine priority based on module order
    module_order = module.get("order_index", 99)
    if module_order <= 3:
        priority = "high"  # Foundation track first 3 modules
    elif module_order <= 7:
        priority = "medium"
    else:
        priority = "low"
    
    # Higher priority for empty/generic
    if quality in [ContentQuality.EMPTY, ContentQuality.GENERIC]:
        if module_order <= 5:
            priority = "critical"
        else:
            priority = "high"
    
    return TaskAudit(
        module_slug=module["slug"],
        module_name=module["name"],
        track_slug=track_slug,
        order_index=task.get("order_index", 0),
        title=task["title"],
        quality=quality,
        content_length=len(content) if content else 0,
        word_count=count_words(content),
        code_block_count=count_code_blocks(content) // 2,
        has_real_code=count_code_blocks(content) >= 2 and "[object Object]" not in (content or ""),
        issues=issues,
        priority=priority,
    )


def run_audit() -> dict:
    """Run the full content audit."""
    results = {
        "summary": {
            "total_tasks": 0,
            "empty": 0,
            "generic": 0,
            "partial": 0,
            "complete": 0,
            "critical_priority": 0,
            "high_priority": 0,
            "medium_priority": 0,
            "low_priority": 0,
        },
        "by_module": {},
        "by_track": {},
        "tasks": [],
        "rewrite_queue": [],
    }
    
    # Build track lookup
    track_map = {t["slug"]: t["name"] for t in BOOTCAMP_TRACKS}
    
    for module in BOOTCAMP_MODULES:
        module_slug = module["slug"]
        track_slug = module["track_slug"]
        
        module_result = {
            "name": module["name"],
            "track": track_slug,
            "total": 0,
            "empty": 0,
            "generic": 0,
            "partial": 0,
            "complete": 0,
            "needs_rewrite": [],
        }
        
        for idx, task in enumerate(module.get("tasks", [])):
            audit = audit_task(module, task, track_slug)
            audit_dict = asdict(audit)
            audit_dict["quality"] = audit.quality.value
            
            results["tasks"].append(audit_dict)
            results["summary"]["total_tasks"] += 1
            module_result["total"] += 1
            
            # Count by quality
            if audit.quality == ContentQuality.EMPTY:
                results["summary"]["empty"] += 1
                module_result["empty"] += 1
                module_result["needs_rewrite"].append(task["title"])
            elif audit.quality == ContentQuality.GENERIC:
                results["summary"]["generic"] += 1
                module_result["generic"] += 1
                module_result["needs_rewrite"].append(task["title"])
            elif audit.quality == ContentQuality.PARTIAL:
                results["summary"]["partial"] += 1
                module_result["partial"] += 1
            else:
                results["summary"]["complete"] += 1
                module_result["complete"] += 1
            
            # Count by priority
            if audit.priority == "critical":
                results["summary"]["critical_priority"] += 1
                results["rewrite_queue"].append({
                    "priority": 1,
                    "module": module_slug,
                    "title": task["title"],
                    "quality": audit.quality.value,
                })
            elif audit.priority == "high":
                results["summary"]["high_priority"] += 1
                results["rewrite_queue"].append({
                    "priority": 2,
                    "module": module_slug,
                    "title": task["title"],
                    "quality": audit.quality.value,
                })
            elif audit.priority == "medium":
                results["summary"]["medium_priority"] += 1
            else:
                results["summary"]["low_priority"] += 1
        
        results["by_module"][module_slug] = module_result
        
        # Track aggregation
        if track_slug not in results["by_track"]:
            results["by_track"][track_slug] = {
                "name": track_map.get(track_slug, track_slug),
                "total": 0,
                "empty": 0,
                "generic": 0,
                "partial": 0,
                "complete": 0,
            }
        
        results["by_track"][track_slug]["total"] += module_result["total"]
        results["by_track"][track_slug]["empty"] += module_result["empty"]
        results["by_track"][track_slug]["generic"] += module_result["generic"]
        results["by_track"][track_slug]["partial"] += module_result["partial"]
        results["by_track"][track_slug]["complete"] += module_result["complete"]
    
    # Sort rewrite queue by priority
    results["rewrite_queue"].sort(key=lambda x: (x["priority"], x["module"]))
    
    return results


def generate_markdown_report(results: dict) -> str:
    """Generate a markdown report from audit results."""
    lines = [
        "# 📊 DevOpsHub Content Audit Report",
        "",
        f"**Generated:** 2025-11-30",
        f"**Total Tasks:** {results['summary']['total_tasks']}",
        "",
        "---",
        "",
        "## 📈 Summary",
        "",
        "| Quality | Count | Percentage |",
        "|---------|-------|------------|",
    ]
    
    total = results["summary"]["total_tasks"]
    for quality in ["complete", "partial", "generic", "empty"]:
        count = results["summary"][quality]
        pct = (count / total * 100) if total > 0 else 0
        emoji = {"complete": "✅", "partial": "🟡", "generic": "🟠", "empty": "🔴"}[quality]
        lines.append(f"| {emoji} {quality.capitalize()} | {count} | {pct:.1f}% |")
    
    lines.extend([
        "",
        "## 🚨 Priority Breakdown",
        "",
        "| Priority | Count | Action |",
        "|----------|-------|--------|",
        f"| 🔴 Critical | {results['summary']['critical_priority']} | Rewrite immediately |",
        f"| 🟠 High | {results['summary']['high_priority']} | Rewrite this sprint |",
        f"| 🟡 Medium | {results['summary']['medium_priority']} | Rewrite next sprint |",
        f"| 🟢 Low | {results['summary']['low_priority']} | Can wait |",
        "",
        "## 📦 By Track",
        "",
    ])
    
    for track_slug, track_data in results["by_track"].items():
        complete_pct = (track_data["complete"] / track_data["total"] * 100) if track_data["total"] > 0 else 0
        needs_work = track_data["empty"] + track_data["generic"]
        lines.append(f"### {track_data['name']}")
        lines.append(f"- Total: {track_data['total']} tasks")
        lines.append(f"- Complete: {track_data['complete']} ({complete_pct:.0f}%)")
        lines.append(f"- Needs rewrite: {needs_work}")
        lines.append("")
    
    lines.extend([
        "## 📋 Rewrite Queue (Top 30)",
        "",
        "| # | Module | Task | Quality |",
        "|---|--------|------|---------|",
    ])
    
    for i, item in enumerate(results["rewrite_queue"][:30], 1):
        lines.append(f"| {i} | {item['module'][:25]} | {item['title'][:35]} | {item['quality']} |")
    
    lines.extend([
        "",
        "---",
        "",
        "*Full details in `content_audit_report.json`*",
    ])
    
    return "\n".join(lines)


def main():
    """Main entry point."""
    print("🔍 Running DevOpsHub Content Audit...")
    print()
    
    results = run_audit()
    
    # Save JSON report
    output_dir = Path(__file__).parent.parent / "content"
    output_dir.mkdir(exist_ok=True)
    
    json_path = output_dir / "content_audit_report.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"📄 JSON report saved: {json_path}")
    
    # Save Markdown report
    md_report = generate_markdown_report(results)
    md_path = output_dir / "rewrite_queue.md"
    with open(md_path, "w") as f:
        f.write(md_report)
    print(f"📝 Markdown report saved: {md_path}")
    
    # Print summary
    print()
    print("=" * 60)
    print("📊 CONTENT AUDIT SUMMARY")
    print("=" * 60)
    print()
    
    total = results["summary"]["total_tasks"]
    complete = results["summary"]["complete"]
    partial = results["summary"]["partial"]
    generic = results["summary"]["generic"]
    empty = results["summary"]["empty"]
    
    print(f"Total Tasks: {total}")
    print(f"  ✅ Complete:  {complete:3d} ({complete/total*100:.1f}%)")
    print(f"  🟡 Partial:   {partial:3d} ({partial/total*100:.1f}%)")
    print(f"  🟠 Generic:   {generic:3d} ({generic/total*100:.1f}%)")
    print(f"  🔴 Empty:     {empty:3d} ({empty/total*100:.1f}%)")
    print()
    print(f"⚠️  NEEDS REWRITE: {generic + empty} tasks")
    print(f"🔴 CRITICAL: {results['summary']['critical_priority']} tasks")
    print()
    
    # Estimated work
    hours_per_task = 1.5  # Average hours to write good content
    total_hours = (generic + empty) * hours_per_task
    print(f"📐 Estimated work: {total_hours:.0f} hours ({total_hours/8:.1f} days)")
    print()


if __name__ == "__main__":
    main()
