"""
ILE Sample Content - Interactive Learning Engine Content Blocks
Phase ILE: Sample task with full interactive content for testing

This file contains sample task content with interactive content blocks
for the "Understanding File Permissions" task.
"""

# Sample task with full content blocks for testing
SAMPLE_PERMISSIONS_TASK = {
    "title": "Understanding File Permissions",
    "description": "Learn how Linux file permissions work and practice using chmod",
    "difficulty": "medium",
    "estimated_minutes": 25,
    "xp_reward": 35,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Understanding File Permissions

In Linux, every file has **permissions** that control who can read, write, or execute it.

## Permission Types
- **r** (read) - View contents
- **w** (write) - Modify contents
- **x** (execute) - Run as program

## User Categories
Each file has three permission sets:
1. **Owner (u)** - The user who owns the file
2. **Group (g)** - Users in the file's group
3. **Others (o)** - Everyone else"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """$ ls -la myfile.txt
-rw-r--r-- 1 user group 1024 Nov 28 myfile.txt

# Breaking down -rw-r--r--:
# -   = regular file
# rw- = owner can read+write
# r-- = group can read
# r-- = others can read""",
            "explanation": "The permission string shows access rights for owner, group, and others."
        },
        {
            "type": "terminal",
            "id": "term-1",
            "instructions": "List files with detailed permissions:",
            "expected_commands": [
                {
                    "command": "ls -la",
                    "regex": "^ls\\s+(-la|-al).*$",
                    "output": """total 4
drwxr-xr-x 2 user user 4096 Nov 28 .
-rw-r--r-- 1 user user  123 Nov 28 file.txt""",
                    "explanation": "ls -la shows all files with detailed information",
                    "allow_variations": True
                }
            ],
            "hints": ["Use ls with -l for long format and -a for all files", "Try: ls -la"]
        },
        {
            "type": "quiz",
            "id": "quiz-1",
            "question": "What does the 'x' permission allow?",
            "options": [
                {"text": "Read the file", "is_correct": False, "feedback": "That's 'r' for read."},
                {"text": "Write to the file", "is_correct": False, "feedback": "That's 'w' for write."},
                {"text": "Execute the file", "is_correct": True, "feedback": "Correct! 'x' means execute."},
                {"text": "Delete the file", "is_correct": False, "feedback": "Delete requires write permission on the directory."}
            ],
            "explanation": "The 'x' permission allows running a file as a program or entering a directory.",
            "xp_bonus": 5
        },
        {
            "type": "text",
            "content": """## Changing Permissions with chmod

Use `chmod` to modify permissions:
- **Symbolic**: `chmod u+x file` (add execute for user)
- **Numeric**: `chmod 755 file` (rwxr-xr-x)

### Common Permission Values
| Value | Meaning | Use Case |
|-------|---------|----------|
| 755 | rwxr-xr-x | Scripts, executables |
| 644 | rw-r--r-- | Regular files |
| 600 | rw------- | Private files (SSH keys!) |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# Make script executable
chmod +x script.sh

# Set specific permissions
chmod 755 script.sh   # rwxr-xr-x
chmod 600 secret.txt  # rw------- (private)""",
            "explanation": "755 is common for scripts, 600 for private files like SSH keys"
        },
        {
            "type": "terminal",
            "id": "term-2",
            "instructions": "Create a file and make it executable:",
            "expected_commands": [
                {
                    "command": "touch test.sh",
                    "output": "",
                    "explanation": "Create empty file"
                },
                {
                    "command": "chmod +x test.sh",
                    "regex": "^chmod\\s+(\\+x|u\\+x|755)\\s+test\\.sh$",
                    "output": "",
                    "explanation": "Add execute permission",
                    "allow_variations": True
                }
            ],
            "hints": ["First create the file with touch", "Then use chmod +x to make it executable"]
        },
        {
            "type": "quiz",
            "id": "quiz-2",
            "question": "What does chmod 600 do?",
            "options": [
                {"text": "Makes file readable by everyone", "is_correct": False, "feedback": "600 restricts access, not opens it."},
                {"text": "Makes file read+write for owner only", "is_correct": True, "feedback": "Correct! 6=rw for owner, 0=nothing for group and others."},
                {"text": "Makes file executable", "is_correct": False, "feedback": "No execute bit is set in 600."},
                {"text": "Deletes the file", "is_correct": False, "feedback": "chmod changes permissions, it doesn't delete files."}
            ],
            "explanation": "600 = rw------- (owner read+write, no access for others). Use this for sensitive files like SSH private keys.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "🎉 Permissions Mastered!",
            "description": "You now understand Linux file permissions and can modify them with chmod. This is essential knowledge for DevOps work!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}


def get_sample_permissions_task():
    """Return the sample permissions task with content blocks"""
    return SAMPLE_PERMISSIONS_TASK
