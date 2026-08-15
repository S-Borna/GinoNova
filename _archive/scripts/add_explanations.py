#!/usr/bin/env python3
"""
Lägger till riktiga explanations i manpage-tenta-quiz.ts
"""

import re

def escape_quotes(text: str) -> str:
    """Escape single quotes for TypeScript strings"""
    return text.replace("'", "\\'")

def generate_explanation(question: str, correct_option: str) -> str:
    """Genererar explanation baserat på frågan och rätt svar"""

    q_lower = question.lower()

    # Pipes & Redirection
    if '|' in question or 'pipe' in q_lower:
        return "The pipe operator (|) sends stdout of one command as stdin to another command, enabling command chaining."
    if '>>' in question:
        return "The >> operator redirects stdout and appends to a file, preserving existing content."
    if '>' in question and '>>' not in question:
        return "The > operator redirects stdout to a file, overwriting any existing content."
    if '2>' in question or ('stderr' in q_lower and 'redirect' in q_lower):
        return "File descriptor 2 is stderr. The 2> operator redirects error messages to a file."
    if 'file descriptor' in q_lower and 'stdin' in q_lower:
        return "File descriptor 0 is stdin (standard input), used for reading input data."
    if 'file descriptor' in q_lower and 'stdout' in q_lower:
        return "File descriptor 1 is stdout (standard output), used for normal program output."

    # Variables & Shell
    if '$?' in question:
        return "$? contains the exit status of the last executed command. 0 means success, non-zero indicates an error."
    if 'variable assignment' in q_lower:
        return "Variables in bash are assigned without the $ prefix: VAR=value (no spaces around =)."
    if 'export' in q_lower and 'var' in q_lower:
        return "export makes a variable available to child processes and subshells, not just the current shell."
    if 'quot' in q_lower and '"' in question:
        return 'Double quotes allow variable expansion ($VAR) while preventing word splitting and glob expansion.'
    if '*' in question and ('represent' in q_lower or 'match' in q_lower):
        return "The * wildcard matches zero or more characters in filenames for glob patterns."

    # File viewing/manipulation
    if 'cat' in correct_option.lower() and 'print' in q_lower:
        return "cat reads files and prints their contents to stdout, useful for viewing or piping."
    if 'less' in correct_option.lower():
        return "less is a pager that allows interactive viewing of large files with scrolling, search, and navigation."
    if 'wc' in correct_option.lower() or 'count lines' in q_lower:
        return "wc -l counts the number of lines in a file or stdin."
    if 'head' in correct_option.lower():
        return "head displays the first N lines of a file (default: 10). Use -n to specify line count."
    if 'tail' in correct_option.lower():
        return "tail displays the last N lines of a file. Use -f to follow file changes in real-time (log monitoring)."
    if 'grep' in correct_option.lower():
        return "grep searches for patterns in text using regular expressions. Use -i for case-insensitive, -v to invert match."
    if 'sort' in correct_option.lower():
        return "sort arranges lines in order. Use -n for numeric sorting, -r for reverse, -u for unique."
    if 'uniq' in correct_option.lower() or 'uniq' in q_lower:
        if 'not work' in q_lower or 'fail' in q_lower or 'expected' in q_lower:
            return "uniq only removes adjacent duplicate lines. You must sort input first for reliable deduplication."
        return "uniq removes adjacent duplicate lines. Always sort input first for complete deduplication."
    if 'cut' in correct_option.lower():
        return "cut extracts columns from text. Use -d for delimiter and -f for field numbers (e.g., cut -d: -f1 /etc/passwd)."
    if 'tr' in correct_option.lower():
        return "tr translates or deletes characters from stdin. Example: tr 'a-z' 'A-Z' converts to uppercase."
    if 'sed' in correct_option.lower():
        return "sed is a stream editor for find/replace and text transformations using patterns (e.g., sed 's/old/new/g')."
    if 'awk' in correct_option.lower():
        return "awk processes text field-by-field. Great for column extraction and calculations (e.g., awk '{print $1}')."
    if 'tee' in correct_option.lower():
        return "tee reads stdin and writes to both stdout and files simultaneously, useful in pipelines."

    # Permissions
    if 'chmod' in correct_option.lower():
        return "chmod changes file permissions using numeric (644, 755) or symbolic (u+x, go-w) notation."
    if 'chown' in correct_option.lower():
        return "chown changes file ownership. Syntax: chown user:group file"
    if '644' in q_lower or '755' in q_lower or 'permission bits' in q_lower:
        return "Linux permissions: owner/group/others, each with read(4)/write(2)/execute(1). 755 = rwxr-xr-x, 644 = rw-r--r--."
    if 'execute' in correct_option.lower() and 'directory' in q_lower:
        return "Execute permission (x) on directories allows entering and accessing files within them."
    if 'setuid' in q_lower or 'suid' in q_lower:
        return "SUID (4xxx permissions) makes executables run with the file owner's privileges instead of the executing user's."
    if 'sticky' in q_lower:
        return "Sticky bit (1xxx) on directories restricts deletion: only file owners can delete their own files (used in /tmp)."

    # Processes
    if 'ps' in correct_option.lower():
        return "ps shows process information. Use ps aux for all processes with detailed info, ps -ef for full listing."
    if 'kill' in correct_option.lower() and ('signal' in q_lower or 'terminate' in q_lower):
        return "kill sends signals to processes. Common: -15 (SIGTERM, graceful), -9 (SIGKILL, forceful), -1 (SIGHUP, reload config)."
    if 'sigkill' in q_lower or '9' in correct_option:
        if 'cannot' in q_lower or 'avoid' in q_lower:
            return "SIGKILL (9) cannot be caught, blocked, or ignored. Use as last resort since it prevents cleanup. Prefer SIGTERM first."
        return "SIGKILL (9) forcefully terminates processes and cannot be caught or ignored by programs."
    if 'sigterm' in q_lower or '15' in correct_option:
        return "SIGTERM (15) is the default termination signal. It's graceful, allowing processes to cleanup before exiting."
    if 'top' in correct_option.lower() or 'htop' in correct_option.lower():
        return "top/htop show real-time system stats: CPU, memory, processes. htop has better UI and mouse support."
    if 'background' in q_lower and '&' in correct_option:
        return "Append & to run commands in the background, freeing the terminal. Use jobs to list, fg to foreground."
    if 'nohup' in correct_option.lower():
        return "nohup prevents processes from receiving SIGHUP, allowing them to continue after terminal logout."
    if 'exit code' in q_lower or 'exit status' in q_lower:
        if '0' in correct_option:
            return "Exit code 0 indicates success. Non-zero values (1-255) indicate errors or failures."
        return f"Exit codes indicate command status. 0 = success, non-zero = failure. Check with $? or in if statements."

    # Find & Locate
    if 'find' in correct_option.lower():
        return "find searches the filesystem recursively with powerful filters: -name, -type, -size, -mtime, -exec for actions."
    if 'locate' in correct_option.lower():
        return "locate searches a pre-built database (updated by updatedb) for fast filename lookup. Faster than find but not real-time."
    if 'which' in correct_option.lower():
        return "which shows the full path of executables found in $PATH. Use to verify which version of a command will run."

    # Networking
    if 'ping' in correct_option.lower():
        return "ping tests network connectivity by sending ICMP echo requests. Useful for troubleshooting connectivity issues."
    if 'netstat' in correct_option.lower() or 'ss' in correct_option.lower():
        return "netstat/ss display network connections, routing tables, and listening ports. ss is newer and faster."
    if 'curl' in correct_option.lower():
        return "curl transfers data from/to servers (HTTP, FTP, etc). Supports headers, authentication, POST data, and more."
    if 'wget' in correct_option.lower():
        return "wget downloads files from web servers. Supports recursive downloads, resume, and background operation."
    if 'ssh' in correct_option.lower():
        return "SSH provides secure, encrypted remote shell access and file transfers. Uses public key authentication."
    if 'scp' in correct_option.lower():
        return "scp securely copies files between hosts over SSH. Syntax: scp source user@host:destination"

    # Disk & Storage
    if 'df' in correct_option.lower():
        return "df shows disk space usage for mounted filesystems. Use -h for human-readable sizes, -i for inodes."
    if 'du' in correct_option.lower():
        return "du estimates file/directory space usage. Use -sh for summary, -h for human-readable, --max-depth=1 for one level."
    if 'mount' in correct_option.lower() and 'attach' in correct_option.lower():
        return "mount attaches filesystems to the directory tree. Syntax: mount /dev/sdb1 /mnt/usb"
    if 'umount' in correct_option.lower():
        return "umount detaches filesystems. Fails if filesystem is busy (use lsof or fuser to find processes)."
    if 'lsblk' in correct_option.lower():
        return "lsblk lists block devices (disks, partitions) in a tree format, showing mount points and sizes."
    if 'fdisk' in correct_option.lower():
        return "fdisk is a partition editor for creating, deleting, and modifying disk partitions. Use -l to list."

    # Package Management
    if 'apt install' in correct_option.lower():
        return "apt install downloads and installs packages with dependencies on Debian/Ubuntu systems."
    if 'apt update' in correct_option.lower():
        return "apt update refreshes the package index from repositories. Run before apt upgrade to get latest package info."
    if 'apt upgrade' in correct_option.lower():
        return "apt upgrade installs available updates for installed packages. Use after apt update."
    if 'yum' in correct_option.lower() or 'dnf' in correct_option.lower():
        return "yum/dnf are package managers for Red Hat-based distros (RHEL, CentOS, Fedora). dnf is newer."

    # Docker
    if 'docker run' in correct_option.lower():
        return "docker run creates and starts a container from an image. Common flags: -d (detached), -p (ports), -v (volumes)."
    if 'docker ps' in correct_option.lower():
        return "docker ps lists running containers. Use -a to include stopped containers, -q for IDs only."
    if 'docker images' in correct_option.lower():
        return "docker images lists locally available images with repository, tag, ID, and size."
    if 'docker pull' in correct_option.lower():
        return "docker pull downloads an image from a registry (Docker Hub by default) to local storage."
    if 'docker build' in correct_option.lower():
        return "docker build creates an image from a Dockerfile. Use -t to tag the image with a name."
    if 'from' in correct_option.lower() and 'dockerfile' in q_lower:
        return "FROM specifies the base image for building. Must be the first instruction in a Dockerfile."
    if ('run' in correct_option.lower() or 'cmd' in correct_option.lower()) and 'dockerfile' in q_lower:
        return "RUN executes commands during build (installs packages), CMD defines the default command when container starts."
    if 'container' in q_lower and 'vm' in q_lower:
        if 'kernel' in correct_option.lower():
            return "Containers share the host OS kernel (lightweight), VMs have their own kernel (full isolation but heavier)."
        return "Containers are lightweight and share the host kernel. VMs provide stronger isolation but use more resources."
    if 'volume' in q_lower and 'docker' in q_lower:
        if 'persist' in correct_option.lower():
            return "Docker volumes provide persistent storage that survives container deletion/recreation."
        return "Volumes store data outside container filesystem, enabling persistence and data sharing between containers."
    if 'bind mount' in q_lower:
        if 'host path' in correct_option.lower() or 'host-path' in correct_option.lower():
            return "Bind mounts map a host directory directly into the container, useful for development with live code updates."
        return "Bind mounts link host paths to container paths. Changes are reflected immediately on both sides."
    if 'port' in q_lower and ('-p' in correct_option or 'publish' in correct_option.lower()):
        return "-p maps container ports to host ports, making containerized services accessible externally (e.g., -p 8080:80)."
    if 'container stop' in q_lower or 'stop' in correct_option.lower():
        if 'exit' in correct_option.lower() or 'main process' in correct_option.lower():
            return "Containers stop when their main process (PID 1) exits. Ensure your application runs in foreground."
        return "Containers run as long as their main process (PID 1) is active. When it exits, container stops."

    # Archives
    if 'tar' in correct_option.lower():
        if 'create' in q_lower:
            return "tar -czf creates compressed archives. Options: c (create), z (gzip), f (file). Example: tar -czf backup.tar.gz /data"
        if 'extract' in q_lower:
            return "tar -xzf extracts compressed archives. Options: x (extract), z (gzip), f (file). Example: tar -xzf backup.tar.gz"
        return "tar creates/extracts archives. Common: -czf (create+gzip), -xzf (extract+gzip), -tf (list contents)."
    if 'gzip' in correct_option.lower():
        return "gzip compresses files efficiently. Use gunzip to decompress. Add -k to keep original files."
    if 'zip' in correct_option.lower():
        return "zip creates compressed archives (Windows-compatible). unzip extracts them. Use -r for recursive directory compression."

    # System Info
    if 'uname' in correct_option.lower():
        return "uname displays system information. Use -a for all info, -r for kernel version, -m for machine architecture."
    if 'hostname' in correct_option.lower():
        return "hostname shows or sets the system's hostname. Use -f for FQDN (fully qualified domain name)."
    if 'uptime' in correct_option.lower():
        return "uptime shows how long the system has been running, user count, and load averages."

    # Users & Groups
    if '/etc/passwd' in correct_option.lower() or 'passwd' in correct_option.lower():
        return "/etc/passwd contains user account info: username, UID, GID, home directory, shell. Passwords are in /etc/shadow."
    if 'useradd' in correct_option.lower():
        return "useradd creates new user accounts. Use -m for home directory, -s for shell, -G for groups."
    if 'usermod' in correct_option.lower():
        return "usermod modifies user accounts. Use -aG to add groups, -s to change shell, -L to lock account."
    if 'sudo' in correct_option.lower():
        return "sudo executes commands with superuser privileges. Configured in /etc/sudoers (edit with visudo)."

    # Generic fallback med kontext
    return f"{correct_option} - This is a fundamental Linux/Unix concept for system administration and DevOps."


# Läs filen
with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parsa och fixa
new_lines = []
i = 0
fixed_count = 0

while i < len(lines):
    line = lines[i]

    if 'explanation:' in line:
        # Samla kontext från föregående rader
        question = ""
        options = []
        correct_idx = -1

        for j in range(i-1, max(0, i-20), -1):
            if 'question:' in lines[j]:
                match = re.search(r"question:\s*['\"]([^'\"]+)['\"]", lines[j])
                if match:
                    question = match.group(1)
            if 'correctIndex:' in lines[j]:
                match = re.search(r'correctIndex:\s*(\d+)', lines[j])
                if match:
                    correct_idx = int(match.group(1))
            # Samla options
            if j > i - 20 and "'" in lines[j] and 'options:' not in lines[j]:
                opt_match = re.search(r"['\"]([^'\"]{3,})['\"]", lines[j])
                if opt_match:
                    opt = opt_match.group(1)
                    if opt not in ['G', 'VG', 'Pipes & Redirection', 'Files', 'Permissions', 'Processes', 'Networking']:
                        options.append(opt)

        # options är i omvänd ordning
        options = options[::-1][:4]

        if question and len(options) == 4 and 0 <= correct_idx < 4:
            correct_option = options[correct_idx]
            new_explanation = escape_quotes(generate_explanation(question, correct_option))
            new_line = re.sub(
                r"explanation:\s*['\"]([^'\"]+)['\"]",
                f"explanation: '{new_explanation}'",
                line
            )
            new_lines.append(new_line)
            fixed_count += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

    i += 1

# Skriv tillbaka
with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"✓ Fixed {fixed_count} explanations in manpage-tenta-quiz.ts")
