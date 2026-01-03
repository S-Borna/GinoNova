#!/usr/bin/env python3
"""
Script to update Hands-On Lab module content.
This can be run manually to update the database with latest content from hands_on.py
"""
import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import seed_content

if __name__ == "__main__":
    print("🔄 Updating Hands-On Lab content...")
    try:
        seed_content()
        print("✅ Content update complete!")
    except Exception as e:
        print(f"❌ Error updating content: {e}")
        sys.exit(1)

