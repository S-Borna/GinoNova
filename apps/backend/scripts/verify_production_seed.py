#!/usr/bin/env python3
"""
Production Seed Verification Script
====================================
Verifies that all V3 modules and tasks are properly seeded in production.

Usage:
    python scripts/verify_production_seed.py

Environment:
    RAILWAY_API_URL - Production API URL (default: https://saas-project-production-31f8.up.railway.app)
"""

import os
import sys
import json
import urllib.request
import urllib.error

# Configuration
PROD_API_URL = os.environ.get(
    "RAILWAY_API_URL",
    "https://saas-project-production-31f8.up.railway.app"
)

# Expected counts from V3 modules
EXPECTED_MODULES = 18
EXPECTED_TASKS = 443  # From audit

# Module slugs we expect
EXPECTED_SLUGS = [
    "aws-for-devops",
    "ansible-mastery",
    "bash",
    "cicd-mastery",
    "docker-mastery",
    "git-github-mastery",
    "go-programming-mastery",
    "javascript",
    "kubernetes-mastery",
    "linux-mastery",
    "mlops",
    "nodejs",
    "prompt-engineering",
    "python-for-devops",
    "sql-mastery",
    "system-design",
    "terraform-mastery",
    "typescript",
]


def fetch_json(url: str) -> dict:
    """Fetch JSON from URL."""
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON from {url}: {e}")
        return None


def verify_health():
    """Verify API is healthy."""
    print(f"\n🔍 Checking API health at {PROD_API_URL}...")
    health = fetch_json(f"{PROD_API_URL}/health")
    if health and health.get("status") == "healthy":
        print("✅ API is healthy")
        return True
    else:
        print("❌ API is not healthy")
        return False


def verify_modules():
    """Verify all modules exist with tasks."""
    print(f"\n🔍 Fetching modules from {PROD_API_URL}/api/modules...")
    modules = fetch_json(f"{PROD_API_URL}/api/modules")

    if not modules:
        print("❌ Failed to fetch modules")
        return False

    print(f"📊 Found {len(modules)} modules in production")

    problems = []
    total_tasks = 0

    for module in modules:
        slug = module.get("slug", "unknown")
        name = module.get("name", "Unknown")
        task_count = module.get("task_count", 0) or module.get("tasks", 0)

        if task_count == 0:
            # Fetch individual module to get actual task count
            detail = fetch_json(f"{PROD_API_URL}/api/modules/slug/{slug}")
            if detail:
                task_count = len(detail.get("tasks", []))

        total_tasks += task_count

        status = "✅" if task_count > 0 else "❌"
        print(f"  {status} {name}: {task_count} tasks")

        if task_count == 0:
            problems.append(f"{name} has 0 tasks")

    print(f"\n📊 Total tasks in production: {total_tasks}")
    print(f"📊 Expected tasks: {EXPECTED_TASKS}")

    if problems:
        print(f"\n❌ PROBLEMS ({len(problems)}):")
        for p in problems:
            print(f"  - {p}")
        return False

    if total_tasks < EXPECTED_TASKS * 0.9:  # Allow 10% variance
        print(f"\n⚠️  Task count is low! Expected ~{EXPECTED_TASKS}, got {total_tasks}")
        return False

    print("\n✅ All modules have tasks!")
    return True


def verify_sample_content():
    """Verify sample modules have actual content."""
    print("\n🔍 Verifying sample module content...")

    test_modules = ["linux-mastery", "docker-mastery", "kubernetes-mastery"]

    for slug in test_modules:
        module = fetch_json(f"{PROD_API_URL}/api/modules/slug/{slug}")
        if not module:
            print(f"  ❌ {slug}: Failed to fetch")
            continue

        tasks = module.get("tasks", [])
        if not tasks:
            print(f"  ❌ {slug}: No tasks")
            continue

        # Check first task has content
        first_task = tasks[0]
        content = first_task.get("content", "")
        content_len = len(content)

        if content_len > 1000:
            print(f"  ✅ {slug}: {len(tasks)} tasks, first task has {content_len} chars")
        else:
            print(f"  ⚠️  {slug}: {len(tasks)} tasks, first task only {content_len} chars")

    return True


def main():
    """Main verification routine."""
    print("=" * 60)
    print("PRODUCTION SEED VERIFICATION")
    print("=" * 60)

    # Check health
    if not verify_health():
        print("\n❌ VERIFICATION FAILED: API not healthy")
        sys.exit(1)

    # Verify modules
    if not verify_modules():
        print("\n❌ VERIFICATION FAILED: Module issues detected")
        sys.exit(1)

    # Verify content
    verify_sample_content()

    print("\n" + "=" * 60)
    print("✅ PRODUCTION VERIFICATION PASSED")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
