"""
Module 01: Linux Mastery - Complete ILE Content
Phase ILE: Full interactive content for all Module 01 tasks

This file contains interactive content blocks for Linux Fundamentals tasks.
"""

# =============================================================================
# TASK 1: Introduction to Linux / Filesystem Hierarchy
# =============================================================================
TASK_FHS = {
    "title": "Filesystem Hierarchy Standard (FHS)",
    "description": "Understand the Linux directory structure and navigate the filesystem",
    "difficulty": "easy",
    "estimated_minutes": 15,
    "xp_reward": 25,
    "content_blocks": [
        {
            "type": "text",
            "content": """# The Linux Filesystem Hierarchy

Linux organizes files in a **tree structure** starting from the root `/` directory.

## Why This Matters for DevOps
- Configuration files live in predictable locations
- Logs are always in `/var/log`
- Executables follow standard paths
- Understanding this = faster troubleshooting

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `/` | Root - everything starts here |
| `/home` | User home directories |
| `/etc` | System configuration files |
| `/var` | Variable data (logs, databases) |
| `/tmp` | Temporary files |
| `/usr` | User programs and data |
| `/bin` | Essential binaries |
| `/opt` | Optional/third-party software |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# View the root directory structure
$ ls /
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr

# Common locations:
/etc/nginx/       # Nginx configuration
/var/log/         # System logs
/home/ubuntu/     # Ubuntu user's home
/opt/myapp/       # Custom application""",
            "explanation": "The Linux filesystem is consistent across distributions - once you learn it, you can navigate any Linux system."
        },
        {
            "type": "terminal",
            "id": "term-fhs-1",
            "instructions": "Explore the root directory. List all top-level directories:",
            "expected_commands": [
                {
                    "command": "ls /",
                    "regex": "^ls\\s+/?$",
                    "output": "bin   dev  home  lib64  mnt  proc  run   srv  tmp  var\nboot  etc  lib   media  opt  root  sbin  sys  usr",
                    "explanation": "ls / shows all directories at the root level",
                    "allow_variations": True
                }
            ],
            "hints": ["Use ls followed by the root path", "The root path is just a forward slash: /"]
        },
        {
            "type": "quiz",
            "id": "quiz-fhs-1",
            "question": "Where would you find system configuration files like nginx.conf?",
            "options": [
                {"text": "/home", "is_correct": False, "feedback": "/home is for user home directories"},
                {"text": "/etc", "is_correct": True, "feedback": "Correct! /etc contains system-wide configuration files"},
                {"text": "/var", "is_correct": False, "feedback": "/var is for variable data like logs"},
                {"text": "/tmp", "is_correct": False, "feedback": "/tmp is for temporary files that get deleted on reboot"}
            ],
            "explanation": "The /etc directory (short for 'et cetera' or 'editable text configuration') holds all system configuration files.",
            "xp_bonus": 5
        },
        {
            "type": "terminal",
            "id": "term-fhs-2",
            "instructions": "Check what's in the /etc directory:",
            "expected_commands": [
                {
                    "command": "ls /etc",
                    "regex": "^ls\\s+/etc/?$",
                    "output": "apt        hostname    network     resolv.conf  ssh\nfstab      hosts       passwd      shadow       sudoers",
                    "explanation": "This shows configuration files for various system services",
                    "allow_variations": True
                }
            ],
            "hints": ["Use ls with the /etc path", "Try: ls /etc"]
        },
        {
            "type": "checkpoint",
            "title": "🗂️ Filesystem Foundations Complete!",
            "description": "You now understand the Linux directory hierarchy - essential knowledge for every DevOps engineer!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 2: Mount Points and Device Files
# =============================================================================
TASK_MOUNTS = {
    "title": "Mount points and device files",
    "description": "Learn how Linux handles storage devices and mount points",
    "difficulty": "medium",
    "estimated_minutes": 20,
    "xp_reward": 30,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Mount Points and Device Files

In Linux, **everything is a file** - including hardware devices!

## Device Files
- Located in `/dev`
- Block devices: `/dev/sda`, `/dev/nvme0n1`
- Character devices: `/dev/tty`, `/dev/null`

## Mount Points
Storage devices must be **mounted** to a directory to access their contents.

| Device | Typical Mount Point |
|--------|-------------------|
| Root disk | `/` |
| USB drive | `/mnt/usb` or `/media/user/` |
| Network share | `/mnt/nfs` |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# View mounted filesystems
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       50G   15G   35G  30% /
/dev/sdb1      100G   60G   40G  60% /data

# Mount a device
$ sudo mount /dev/sdb1 /mnt/backup

# View mount details
$ mount | grep sda
/dev/sda1 on / type ext4 (rw,relatime)""",
            "explanation": "df -h shows disk usage in human-readable format. mount shows all mounted filesystems."
        },
        {
            "type": "terminal",
            "id": "term-mount-1",
            "instructions": "Check disk space usage on the system:",
            "expected_commands": [
                {
                    "command": "df -h",
                    "regex": "^df\\s+(-h|--human-readable)$",
                    "output": "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1       50G   15G   35G  30% /\ntmpfs           2G     0    2G   0% /tmp",
                    "explanation": "df -h shows all mounted filesystems with disk usage",
                    "allow_variations": True
                }
            ],
            "hints": ["Use df with -h for human-readable sizes", "Try: df -h"]
        },
        {
            "type": "quiz",
            "id": "quiz-mount-1",
            "question": "What does 'mounting' a filesystem mean?",
            "options": [
                {"text": "Formatting the disk", "is_correct": False, "feedback": "Formatting erases and prepares a disk - that's different"},
                {"text": "Making a filesystem accessible at a directory", "is_correct": True, "feedback": "Correct! Mounting attaches a filesystem to a directory path"},
                {"text": "Copying files to a backup", "is_correct": False, "feedback": "That would be a backup operation, not mounting"},
                {"text": "Encrypting the disk", "is_correct": False, "feedback": "Encryption is a separate operation from mounting"}
            ],
            "explanation": "Mounting connects a storage device to a specific directory in the filesystem hierarchy.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "💾 Storage Concepts Mastered!",
            "description": "You understand how Linux manages storage devices and mount points!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 3: Inodes, Hard Links, Symbolic Links
# =============================================================================
TASK_LINKS = {
    "title": "Inodes, hard links, symbolic links",
    "description": "Understand how Linux tracks files and create different types of links",
    "difficulty": "medium",
    "estimated_minutes": 25,
    "xp_reward": 35,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Inodes and Links

## What is an Inode?
Every file in Linux has an **inode** - a data structure containing:
- File metadata (permissions, owner, timestamps)
- Pointers to data blocks on disk
- **NOT** the filename!

Filenames are stored in **directories** and point to inodes.

## Hard Links vs Symbolic Links

| Feature | Hard Link | Symbolic Link |
|---------|-----------|---------------|
| Points to | Inode directly | Filename/path |
| Cross filesystem | ❌ No | ✅ Yes |
| If target deleted | Still works | Broken link |
| For directories | ❌ No | ✅ Yes |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# View inode numbers
$ ls -li
12345 -rw-r--r-- 2 user user 100 Nov 28 file.txt
12345 -rw-r--r-- 2 user user 100 Nov 28 hardlink.txt
67890 lrwxrwxrwx 1 user user   8 Nov 28 symlink.txt -> file.txt

# Create a hard link (same inode!)
$ ln file.txt hardlink.txt

# Create a symbolic link (different inode, points to path)
$ ln -s file.txt symlink.txt""",
            "explanation": "Notice hardlink.txt has the same inode (12345) as file.txt. The '2' shows link count."
        },
        {
            "type": "terminal",
            "id": "term-links-1",
            "instructions": "List files with their inode numbers:",
            "expected_commands": [
                {
                    "command": "ls -li",
                    "regex": "^ls\\s+(-li|-il).*$",
                    "output": "12345 -rw-r--r-- 1 user user 100 Nov 28 file.txt",
                    "explanation": "The -i flag shows inode numbers in the first column",
                    "allow_variations": True
                }
            ],
            "hints": ["Use ls with -l for long format and -i for inodes", "Try: ls -li"]
        },
        {
            "type": "quiz",
            "id": "quiz-links-1",
            "question": "What happens when you delete the original file that a hard link points to?",
            "options": [
                {"text": "The hard link breaks", "is_correct": False, "feedback": "That's what happens with symbolic links!"},
                {"text": "The hard link still works", "is_correct": True, "feedback": "Correct! Hard links share the same inode, so the data persists"},
                {"text": "Both files are deleted", "is_correct": False, "feedback": "No, only the filename is removed, not the data"},
                {"text": "The system crashes", "is_correct": False, "feedback": "No, this is normal filesystem behavior"}
            ],
            "explanation": "Hard links share the same inode. The data is only deleted when ALL hard links are removed (link count reaches 0).",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "🔗 Links Mastered!",
            "description": "You understand inodes and can create both hard and symbolic links!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 4: Process Lifecycle and States
# =============================================================================
TASK_PROCESS = {
    "title": "Process lifecycle and states",
    "description": "Learn how Linux processes work and their different states",
    "difficulty": "medium",
    "estimated_minutes": 20,
    "xp_reward": 35,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Process Lifecycle and States

## What is a Process?
A **process** is a running instance of a program. Every process has:
- **PID** - Process ID (unique number)
- **PPID** - Parent Process ID
- **State** - Current status

## Process States

| State | Symbol | Description |
|-------|--------|-------------|
| Running | R | Actively executing on CPU |
| Sleeping | S | Waiting for an event |
| Disk Sleep | D | Waiting for I/O (uninterruptible) |
| Stopped | T | Paused (e.g., Ctrl+Z) |
| Zombie | Z | Finished but parent hasn't read exit status |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# View all processes
$ ps aux
USER  PID %CPU %MEM    VSZ   RSS TTY STAT START TIME COMMAND
root    1  0.0  0.1   1234  5678 ?   Ss   10:00 0:01 /sbin/init
user 1234  0.5  2.0 123456 78900 pts/0 Sl 10:05 0:30 node app.js

# STAT column meanings:
# S = Sleeping
# R = Running
# l = multi-threaded
# s = session leader""",
            "explanation": "ps aux shows all processes with detailed information including CPU/memory usage."
        },
        {
            "type": "terminal",
            "id": "term-proc-1",
            "instructions": "View running processes on the system:",
            "expected_commands": [
                {
                    "command": "ps aux",
                    "regex": "^ps\\s+(aux|aux .*|ef|ef .*)$",
                    "output": "USER  PID %CPU %MEM COMMAND\nroot    1  0.0  0.1 /sbin/init\nuser 1234 0.5  2.0 node app.js",
                    "explanation": "ps aux shows all processes with CPU and memory usage",
                    "allow_variations": True
                }
            ],
            "hints": ["Use ps with aux flags", "aux = all users, detailed output"]
        },
        {
            "type": "quiz",
            "id": "quiz-proc-1",
            "question": "What does a 'Zombie' (Z) process state indicate?",
            "options": [
                {"text": "The process is frozen", "is_correct": False, "feedback": "That would be Stopped (T) state"},
                {"text": "The process finished but parent hasn't collected exit status", "is_correct": True, "feedback": "Correct! Zombies are finished processes waiting for their parent"},
                {"text": "The process is using too much CPU", "is_correct": False, "feedback": "CPU usage doesn't determine zombie state"},
                {"text": "The process is waiting for user input", "is_correct": False, "feedback": "That would typically be Sleeping (S) state"}
            ],
            "explanation": "Zombie processes have completed execution but their parent process hasn't called wait() to collect the exit status.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "⚙️ Process Fundamentals Complete!",
            "description": "You understand Linux process states and lifecycle!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 5: Job Control
# =============================================================================
TASK_JOBS = {
    "title": "Job control (jobs, fg, bg, nohup)",
    "description": "Master foreground/background processes and job control",
    "difficulty": "medium",
    "estimated_minutes": 20,
    "xp_reward": 30,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Job Control in Linux

## Foreground vs Background
- **Foreground**: Process holds the terminal, you wait for it
- **Background**: Process runs independently, terminal is free

## Key Commands

| Command | Action |
|---------|--------|
| `&` | Start command in background |
| `Ctrl+Z` | Suspend foreground process |
| `jobs` | List background jobs |
| `fg %1` | Bring job 1 to foreground |
| `bg %1` | Resume job 1 in background |
| `nohup` | Keep running after logout |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# Start process in background
$ sleep 100 &
[1] 12345

# Suspend current process
$ vim file.txt
# Press Ctrl+Z
[1]+ Stopped  vim file.txt

# List jobs
$ jobs
[1]+ Stopped  vim file.txt
[2]- Running  sleep 100 &

# Resume in foreground
$ fg %1

# Run something that survives logout
$ nohup ./long_script.sh &""",
            "explanation": "The [1] is the job number, 12345 is the PID. Use %1 to reference job 1."
        },
        {
            "type": "terminal",
            "id": "term-jobs-1",
            "instructions": "List current background jobs:",
            "expected_commands": [
                {
                    "command": "jobs",
                    "regex": "^jobs$",
                    "output": "[1]+ Running   sleep 100 &",
                    "explanation": "jobs lists all background and suspended jobs in the current shell",
                    "allow_variations": False
                }
            ],
            "hints": ["The command to list jobs is simply: jobs"]
        },
        {
            "type": "quiz",
            "id": "quiz-jobs-1",
            "question": "What does nohup do?",
            "options": [
                {"text": "Makes a process use less memory", "is_correct": False, "feedback": "nohup doesn't affect memory usage"},
                {"text": "Keeps a process running after you log out", "is_correct": True, "feedback": "Correct! nohup ignores the hangup signal (SIGHUP)"},
                {"text": "Runs a process with higher priority", "is_correct": False, "feedback": "That would be nice, but no"},
                {"text": "Pauses a running process", "is_correct": False, "feedback": "Ctrl+Z or kill -STOP does that"}
            ],
            "explanation": "nohup (no hang up) prevents a process from being terminated when the terminal session ends.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "🎯 Job Control Mastered!",
            "description": "You can now manage foreground and background processes like a pro!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 6: Signals
# =============================================================================
TASK_SIGNALS = {
    "title": "Signals (SIGTERM, SIGKILL, SIGHUP)",
    "description": "Learn how to send signals to control processes",
    "difficulty": "medium",
    "estimated_minutes": 20,
    "xp_reward": 35,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Linux Signals

Signals are **software interrupts** sent to processes.

## Common Signals

| Signal | Number | Description |
|--------|--------|-------------|
| SIGTERM | 15 | Graceful termination (default) |
| SIGKILL | 9 | Force kill (cannot be caught) |
| SIGHUP | 1 | Hangup - often triggers reload |
| SIGINT | 2 | Interrupt (Ctrl+C) |
| SIGSTOP | 19 | Pause process |
| SIGCONT | 18 | Resume paused process |

## DevOps Usage
- **SIGTERM**: Graceful shutdown (saves state)
- **SIGKILL**: Last resort when process won't stop
- **SIGHUP**: Reload config without restart"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# Send SIGTERM (graceful)
$ kill 12345
$ kill -15 12345   # Same as above
$ kill -TERM 12345 # Same as above

# Force kill (SIGKILL)
$ kill -9 12345
$ kill -KILL 12345

# Reload config (SIGHUP)
$ kill -HUP $(pgrep nginx)

# Kill by name
$ pkill -TERM nginx
$ killall python""",
            "explanation": "Always try SIGTERM first - it allows the process to cleanup. Use SIGKILL only if SIGTERM doesn't work."
        },
        {
            "type": "terminal",
            "id": "term-sig-1",
            "instructions": "List all available signals:",
            "expected_commands": [
                {
                    "command": "kill -l",
                    "regex": "^kill\\s+-l$",
                    "output": " 1) SIGHUP   2) SIGINT   3) SIGQUIT  9) SIGKILL\n15) SIGTERM 18) SIGCONT 19) SIGSTOP 20) SIGTSTP",
                    "explanation": "kill -l lists all signal names and numbers",
                    "allow_variations": False
                }
            ],
            "hints": ["Use kill with the -l flag to list signals"]
        },
        {
            "type": "quiz",
            "id": "quiz-sig-1",
            "question": "Why should you try SIGTERM before SIGKILL?",
            "options": [
                {"text": "SIGTERM is faster", "is_correct": False, "feedback": "Speed isn't the reason"},
                {"text": "SIGKILL costs more CPU", "is_correct": False, "feedback": "CPU usage isn't the concern"},
                {"text": "SIGTERM allows graceful cleanup", "is_correct": True, "feedback": "Correct! SIGTERM lets the process save state and clean up"},
                {"text": "SIGKILL requires root", "is_correct": False, "feedback": "Both can be sent by the process owner"}
            ],
            "explanation": "SIGTERM (15) can be caught by the process, allowing it to save data, close connections, and cleanup. SIGKILL (9) terminates immediately with no cleanup.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "📡 Signal Master!",
            "description": "You understand Linux signals and can control processes effectively!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 7: Process Monitoring
# =============================================================================
TASK_MONITORING = {
    "title": "Process monitoring (ps, top, htop, pgrep)",
    "description": "Master tools for monitoring system processes",
    "difficulty": "medium",
    "estimated_minutes": 25,
    "xp_reward": 40,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Process Monitoring Tools

## Essential Commands

| Tool | Best For |
|------|----------|
| `ps` | Snapshot of processes |
| `top` | Live monitoring (built-in) |
| `htop` | Better top with colors |
| `pgrep` | Find PIDs by name |
| `pidof` | Get PID of a program |

## Key Metrics to Watch
- **%CPU** - CPU usage
- **%MEM** - Memory usage
- **TIME+** - Total CPU time used
- **COMMAND** - What's running"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# Snapshot of processes
$ ps aux | head -5
USER  PID %CPU %MEM COMMAND
root    1  0.0  0.1 /sbin/init
root  123  0.5  1.0 /usr/bin/dockerd

# Find process by name
$ pgrep -a nginx
1234 nginx: master process
1235 nginx: worker process

# Get just the PID
$ pidof nginx
1234 1235

# Live monitoring (press 'q' to quit)
$ top
$ htop  # if installed""",
            "explanation": "pgrep is great for scripts - it returns just PIDs. top/htop are for interactive monitoring."
        },
        {
            "type": "terminal",
            "id": "term-mon-1",
            "instructions": "Find all processes containing 'python' in the name:",
            "expected_commands": [
                {
                    "command": "pgrep -a python",
                    "regex": "^pgrep\\s+(-a\\s+)?python.*$",
                    "output": "1234 python app.py\n1235 python3 server.py",
                    "explanation": "pgrep -a shows PID and full command line",
                    "allow_variations": True
                }
            ],
            "hints": ["Use pgrep to search for processes", "The -a flag shows the full command"]
        },
        {
            "type": "quiz",
            "id": "quiz-mon-1",
            "question": "Which tool is best for getting PIDs in a shell script?",
            "options": [
                {"text": "top", "is_correct": False, "feedback": "top is interactive, not good for scripts"},
                {"text": "htop", "is_correct": False, "feedback": "htop is also interactive"},
                {"text": "pgrep", "is_correct": True, "feedback": "Correct! pgrep outputs clean PIDs perfect for scripts"},
                {"text": "ps aux", "is_correct": False, "feedback": "ps aux outputs too much - you'd need to parse it"}
            ],
            "explanation": "pgrep outputs just PIDs (or PIDs + command with -a), making it ideal for scripting.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "📊 Monitoring Pro!",
            "description": "You can find and monitor any process on a Linux system!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# TASK 8: Systemd Architecture
# =============================================================================
TASK_SYSTEMD = {
    "title": "Systemd architecture",
    "description": "Understand the Linux init system and systemd components",
    "difficulty": "medium",
    "estimated_minutes": 25,
    "xp_reward": 40,
    "content_blocks": [
        {
            "type": "text",
            "content": """# Systemd: The Modern Init System

## What is Systemd?
Systemd is the **init system** for most modern Linux distributions. It:
- Starts the system (PID 1)
- Manages services (daemons)
- Handles logging (journald)
- Controls targets (runlevels)

## Key Components

| Component | Purpose |
|-----------|---------|
| `systemd` | Main process (PID 1) |
| `systemctl` | Control services |
| `journalctl` | View logs |
| `unit files` | Service definitions |"""
        },
        {
            "type": "code",
            "language": "bash",
            "code": """# Service management
$ sudo systemctl start nginx
$ sudo systemctl stop nginx
$ sudo systemctl restart nginx
$ sudo systemctl reload nginx   # Reload config only

# Service status
$ systemctl status nginx
● nginx.service - nginx HTTP server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
   Active: active (running) since Mon 2025-11-28 10:00:00 UTC

# Enable/disable at boot
$ sudo systemctl enable nginx
$ sudo systemctl disable nginx""",
            "explanation": "systemctl is your main tool for managing services. enable/disable affects boot behavior."
        },
        {
            "type": "terminal",
            "id": "term-sys-1",
            "instructions": "Check the status of a service (e.g., ssh or sshd):",
            "expected_commands": [
                {
                    "command": "systemctl status sshd",
                    "regex": "^(sudo\\s+)?systemctl\\s+status\\s+(ssh|sshd)$",
                    "output": "● sshd.service - OpenSSH server daemon\n   Loaded: loaded\n   Active: active (running)",
                    "explanation": "systemctl status shows if a service is running and its recent logs",
                    "allow_variations": True
                }
            ],
            "hints": ["Use systemctl status followed by service name", "Try: systemctl status sshd"]
        },
        {
            "type": "quiz",
            "id": "quiz-sys-1",
            "question": "What's the difference between 'restart' and 'reload'?",
            "options": [
                {"text": "No difference", "is_correct": False, "feedback": "They do different things!"},
                {"text": "restart stops and starts; reload just reloads config", "is_correct": True, "feedback": "Correct! reload is gentler - no downtime"},
                {"text": "reload is faster", "is_correct": False, "feedback": "Speed isn't the main difference"},
                {"text": "restart requires sudo, reload doesn't", "is_correct": False, "feedback": "Both typically require sudo"}
            ],
            "explanation": "reload sends SIGHUP to reload configuration without stopping the service. restart fully stops and starts it.",
            "xp_bonus": 5
        },
        {
            "type": "checkpoint",
            "title": "🚀 Systemd Fundamentals Complete!",
            "description": "You understand how systemd manages Linux services!"
        }
    ],
    "requirements": [
        {"type": "all_terminals_complete"},
        {"type": "all_quizzes_answered"}
    ]
}

# =============================================================================
# EXPORT ALL TASKS
# =============================================================================
MODULE_01_TASKS = {
    "Filesystem Hierarchy Standard (FHS)": TASK_FHS,
    "Mount points and device files": TASK_MOUNTS,
    "Inodes, hard links, symbolic links": TASK_LINKS,
    "Process lifecycle and states": TASK_PROCESS,
    "Job control (jobs, fg, bg, nohup)": TASK_JOBS,
    "Signals (SIGTERM, SIGKILL, SIGHUP)": TASK_SIGNALS,
    "Process monitoring (ps, top, htop, pgrep)": TASK_MONITORING,
    "Systemd architecture": TASK_SYSTEMD,
}


def get_module_01_task(title: str) -> dict:
    """Get a specific task by title"""
    return MODULE_01_TASKS.get(title, {})


def get_all_module_01_tasks() -> list[dict]:
    """Get all Module 01 tasks as a list"""
    return list(MODULE_01_TASKS.values())
