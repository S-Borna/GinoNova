#!/usr/bin/env python3
"""
Fixar ManpageTentan - översätter svenska frågor och genererar riktiga explanations
"""

import re
import json

def generate_explanation(question: str, correct_option: str, all_options: list) -> str:
    """Genererar en förklaring baserat på frågan och rätt svar"""

    # Extrahera nyckelord från frågan
    q_lower = question.lower()

    # Pipes & Redirection
    if '|' in question or 'pipe' in q_lower:
        return f"{correct_option} - The pipe operator (|) sends stdout of one command as stdin to another command."
    if '>' in question and '>>' not in question:
        return f"{correct_option} - The > operator redirects stdout to a file, overwriting existing content."
    if '>>' in question:
        return f"{correct_option} - The >> operator redirects stdout to a file, appending to existing content."
    if '2>' in question or 'stderr' in q_lower:
        return f"{correct_option} - File descriptor 2 is stderr. Use 2> to redirect error messages."
    if 'stdin' in q_lower and 'file descriptor' in q_lower:
        return f"{correct_option} - File descriptor 0 is stdin (standard input)."
    if 'stdout' in q_lower and 'file descriptor' in q_lower:
        return f"{correct_option} - File descriptor 1 is stdout (standard output)."

    # Variables & Shell
    if '$?' in question:
        return f"{correct_option} - $? contains the exit status of the last executed command (0 = success, non-zero = error)."
    if 'variable assignment' in q_lower or 'assign' in q_lower:
        return f"{correct_option} - In bash, variables are assigned without $ prefix: VAR=value (no spaces around =)."
    if 'export' in q_lower and 'var' in q_lower:
        return f"{correct_option} - export makes a variable available to child processes/subshells."
    if 'quoting' in q_lower and '"' in question:
        return f"{correct_option} - Double quotes allow variable expansion while preventing word splitting."
    if '*' in question and 'represent' in q_lower:
        return f"{correct_option} - The * wildcard matches zero or more characters in filenames."

    # File commands
    if 'cat' in q_lower or 'print' in q_lower:
        return f"{correct_option} - cat concatenates and prints file contents to stdout."
    if 'less' in q_lower and 'view' in q_lower:
        return f"{correct_option} - less is a pager for viewing large files interactively with scrolling."
    if 'wc -l' in q_lower or 'count lines' in q_lower:
        return f"{correct_option} - wc -l counts the number of lines in a file."
    if 'head' in q_lower:
        return f"{correct_option} - head displays the first N lines of a file (default: 10)."
    if 'tail' in q_lower:
        return f"{correct_option} - tail displays the last N lines of a file (default: 10). Use -f to follow growing files."
    if 'grep' in q_lower:
        return f"{correct_option} - grep searches for patterns in text using regular expressions."
    if 'sort' in q_lower:
        return f"{correct_option} - sort arranges lines alphabetically or numerically. Use -n for numeric, -r for reverse."
    if 'uniq' in q_lower:
        return f"{correct_option} - uniq removes adjacent duplicate lines. Input must be sorted first for reliable results."
    if 'cut' in q_lower:
        return f"{correct_option} - cut extracts columns/fields from text. Use -d for delimiter and -f for field numbers."
    if 'tr' in q_lower:
        return f"{correct_option} - tr translates or deletes characters from stdin."
    if 'sed' in q_lower:
        return f"{correct_option} - sed is a stream editor for text transformations using patterns and commands."
    if 'awk' in q_lower:
        return f"{correct_option} - awk is a text processing tool that operates on fields and records."

    # Permissions
    if 'chmod' in q_lower:
        return f"{correct_option} - chmod changes file permissions. Use numeric (755) or symbolic (u+x) notation."
    if 'chown' in q_lower:
        return f"{correct_option} - chown changes file ownership (user:group)."
    if '644' in question or '755' in question or 'permission' in q_lower:
        return f"{correct_option} - Linux permissions: owner/group/others, each with read(4)/write(2)/execute(1)."
    if 'execute' in q_lower and 'directory' in q_lower:
        return f"{correct_option} - Execute permission on a directory (x) allows entering/accessing it."
    if 'setuid' in q_lower or 'suid' in q_lower:
        return f"{correct_option} - SUID (4xxx) makes executable run with file owner's privileges instead of user's."
    if 'sticky' in q_lower:
        return f"{correct_option} - Sticky bit (1xxx) on directories restricts deletion: only owner can delete their files."

    # Processes
    if 'ps' in q_lower and not 'grep' in q_lower:
        return f"{correct_option} - ps shows process information. Use ps aux for all processes with details."
    if 'kill' in q_lower and 'signal' in q_lower:
        return f"{correct_option} - kill sends signals to processes. Use -9 (SIGKILL) for forceful termination."
    if 'sigkill' in q_lower or 'signal 9' in q_lower:
        return f"{correct_option} - SIGKILL (9) forcefully terminates a process and cannot be caught or ignored."
    if 'sigterm' in q_lower or 'signal 15' in q_lower:
        return f"{correct_option} - SIGTERM (15) is the default graceful termination signal that can be caught."
    if 'top' in q_lower or 'htop' in q_lower:
        return f"{correct_option} - top/htop show real-time system resource usage and running processes."
    if 'background' in q_lower and '&' in question:
        return f"{correct_option} - Append & to run a command in the background, returning shell control immediately."
    if 'exit code' in q_lower or 'exit status' in q_lower:
        return f"{correct_option} - Exit code 0 means success, non-zero indicates an error or failure."

    # Find & Locate
    if 'find' in q_lower:
        return f"{correct_option} - find searches filesystem recursively with powerful filtering options like -name, -type, -size."
    if 'locate' in q_lower:
        return f"{correct_option} - locate searches a pre-built database for fast filename lookup. Update with updatedb."
    if 'which' in q_lower:
        return f"{correct_option} - which shows the full path of executables in PATH."

    # Networking
    if 'ping' in q_lower:
        return f"{correct_option} - ping tests network connectivity by sending ICMP echo requests."
    if 'netstat' in q_lower or 'ss' in q_lower:
        return f"{correct_option} - netstat/ss show network connections, routing tables, and listening ports."
    if 'curl' in q_lower:
        return f"{correct_option} - curl transfers data from/to servers supporting various protocols (HTTP, FTP, etc)."
    if 'wget' in q_lower:
        return f"{correct_option} - wget downloads files from web servers non-interactively."
    if 'ssh' in q_lower:
        return f"{correct_option} - SSH provides secure encrypted remote shell access and file transfers."
    if 'scp' in q_lower:
        return f"{correct_option} - scp securely copies files between hosts over SSH."

    # Disk & Storage
    if 'df' in q_lower:
        return f"{correct_option} - df shows disk space usage for mounted filesystems. Use -h for human-readable format."
    if 'du' in q_lower:
        return f"{correct_option} - du estimates file/directory space usage. Use -sh for summary in human-readable format."
    if 'mount' in q_lower:
        return f"{correct_option} - mount attaches filesystems to the directory tree at a specified mount point."
    if 'umount' in q_lower or 'unmount' in q_lower:
        return f"{correct_option} - umount detaches filesystems from the directory tree."
    if 'lsblk' in q_lower:
        return f"{correct_option} - lsblk lists block devices (disks, partitions) and their mount points."
    if 'fdisk' in q_lower:
        return f"{correct_option} - fdisk is a partition table manipulator for creating/modifying disk partitions."

    # Package Management
    if 'apt install' in q_lower or 'apt-get install' in q_lower:
        return f"{correct_option} - apt install downloads and installs packages and their dependencies on Debian/Ubuntu."
    if 'apt update' in q_lower:
        return f"{correct_option} - apt update refreshes the package index from repositories."
    if 'apt upgrade' in q_lower:
        return f"{correct_option} - apt upgrade installs available updates for installed packages."
    if 'yum' in q_lower or 'dnf' in q_lower:
        return f"{correct_option} - yum/dnf are package managers for Red Hat-based distributions (RHEL, CentOS, Fedora)."

    # Docker
    if 'docker run' in q_lower:
        return f"{correct_option} - docker run creates and starts a new container from an image."
    if 'docker ps' in q_lower:
        return f"{correct_option} - docker ps lists running containers. Use -a to include stopped containers."
    if 'docker images' in q_lower:
        return f"{correct_option} - docker images lists available images in local Docker storage."
    if 'docker pull' in q_lower:
        return f"{correct_option} - docker pull downloads an image from a registry (Docker Hub by default)."
    if 'docker build' in q_lower:
        return f"{correct_option} - docker build creates an image from a Dockerfile."
    if 'dockerfile' in q_lower and 'from' in q_lower:
        return f"{correct_option} - FROM specifies the base image for building a new Docker image."
    if 'dockerfile' in q_lower and ('run' in q_lower or 'cmd' in q_lower):
        return f"{correct_option} - RUN executes commands during image build, CMD defines the default command when container starts."
    if 'container' in q_lower and ('vm' in q_lower or 'virtual machine' in q_lower):
        return f"{correct_option} - Containers share the host kernel (lightweight), VMs have their own kernel (isolated but heavier)."
    if 'volume' in q_lower and 'docker' in q_lower:
        return f"{correct_option} - Docker volumes provide persistent storage that survives container lifecycle."
    if 'bind mount' in q_lower:
        return f"{correct_option} - Bind mounts map a host path directly into the container, useful for development."
    if 'port' in q_lower and ('-p' in question or 'publish' in q_lower):
        return f"{correct_option} - -p maps container ports to host ports, making services accessible externally."

    # Archives
    if 'tar' in q_lower:
        return f"{correct_option} - tar creates/extracts archives. Common: tar -czf (create gzip), tar -xzf (extract gzip)."
    if 'gzip' in q_lower or 'gunzip' in q_lower:
        return f"{correct_option} - gzip compresses files, gunzip decompresses them. Use -k to keep originals."
    if 'zip' in q_lower or 'unzip' in q_lower:
        return f"{correct_option} - zip creates compressed archives, unzip extracts them."

    # Generic fallback med mer kontext
    return f"{correct_option} is correct. This is a fundamental Linux/Unix concept covered in system administration and DevOps."


def translate_question(text: str) -> str:
    """Översätter svenska frågor till engelska"""
    # Omfattande översättningar
    translations = {
        # Hela fraser/meningar
        'En container är best described as:': 'A container is best described as:',
        'Why fungerar inte uniq file.txt alltid som förväntat?': 'Why doesn\'t uniq file.txt always work as expected?',
        'Why fungerar inte localhost mellan containrar?': 'Why doesn\'t localhost work between containers?',
        'Which signal kan inte fångas av ett program?': 'Which signal cannot be caught by a program?',
        'What is Docker volumes främst used for?': 'What are Docker volumes primarily used for?',
        'Ett kommando skriver både normal output och felmeddelanden. Du vill att inget visas i terminalen men att endast felen sparas i fil.': 'A command writes both normal output and error messages. You want nothing shown in terminal but only errors saved to file.',
        'Which command visar output på skärmen och skriver samma output till fil?': 'Which command shows output on screen and writes same output to file?',
        'Which command visar status från senast körda kommando?': 'Which command shows status from last executed command?',
        'Du vill visa unika rader och hur många gånger varje förekommer.': 'You want to show unique lines and how many times each occurs.',
        'Why ger uniq file.txt inte alltid förväntat resultat?': 'Why doesn\'t uniq file.txt always give expected result?',
        'Extrahera kolumn 1 från CSV, sortera numeriskt fallande och visa tre största värdena.': 'Extract column 1 from CSV, sort numerically descending and show three largest values.',
        'Du vill läsa filen /var/log/syslog men bara från rad 100.': 'You want to read file /var/log/syslog but only from line 100.',
        'Du behöver räkna antalet unika IP-adresser i access.log.': 'You need to count the number of unique IP addresses in access.log.',
        'Du vill se vilka portar som lyssnar på systemet.': 'You want to see which ports are listening on the system.',
        'En process är fryst och svarar inte på SIGTERM.': 'A process is frozen and doesn\'t respond to SIGTERM.',
        'Du vill starta en process och se till att den fortsätter köra efter logout.': 'You want to start a process and ensure it continues running after logout.',
        'Kommandot tar -czf backup.tar.gz /home gör vad?': 'What does command tar -czf backup.tar.gz /home do?',
        'Vilken fil innehåller användarnamn och UID på Linux?': 'Which file contains usernames and UIDs on Linux?',
        'Kommandot chmod 755 script.sh gör vad?': 'What does command chmod 755 script.sh do?',
        'Du vill ge användaren dave rättighet att köra sudo apt update utan lösenord.': 'You want to give user dave permission to run sudo apt update without password.',

        # Individuella ord (kortare fraser sist)
        'fungerar inte': 'doesn\'t work',
        'kan inte fångas': 'cannot be caught',
        'främst used för': 'primarily used for',
        'visar output på skärmen': 'shows output on screen',
        'visar status från': 'shows status from',
        'senast körda kommando': 'last executed command',
        'användarnamn och UID': 'usernames and UIDs',
        'främst': 'primarily',
        'används för': 'used for',
        'visar': 'shows',
        'används': 'used',
        'containrar': 'containers',
        'mellan': 'between',
        'gånger': 'times',
        'varje': 'each',
        'förekommer': 'occurs',
        'från': 'from',
        'endast': 'only',
        'också': 'also',
        'både': 'both',
        'eller': 'or',
        'och': 'and',
        'är': 'is',
        'inte': 'not',
        'på': 'on',
        'för': 'for',
        'i': 'in',
        'som': 'as',
        'med': 'with',
        'av': 'of',
        'till': 'to',
        'efter': 'after',
        'utan': 'without',
        'En': 'A',
        'ett': 'a',
    }

    result = text
    # Sortera translations efter längd (längst först) för att undvika partial replacements
    for swedish, english in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(swedish, english)

    return result


def fix_quiz_file(input_file: str, output_file: str):
    """Läser quiz-filen, fixar explanations (skippar översättning since frågorna redan är på engelska)"""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Om vi hittar en explanation-rad
        if 'explanation:' in line:
            # Gå bakåt för att hitta question, options, och correctIndex
            question = ""
            options = []
            correct_idx = -1

            # Läs bakåt för att samla kontext
            for j in range(i-1, max(0, i-15), -1):
                if 'question:' in lines[j]:
                    match = re.search(r"question:\s*['\"]([^'\"]+)['\"]", lines[j])
                    if match:
                        question = match.group(1)
                if 'correctIndex:' in lines[j]:
                    match = re.search(r'correctIndex:\s*(\d+)', lines[j])
                    if match:
                        correct_idx = int(match.group(1))
                if "'" in lines[j] and 'options' not in lines[j] and 'question' not in lines[j] and 'explanation' not in lines[j]:
                    opt_match = re.search(r"['\"]([^'\"]+)['\"]", lines[j])
                    if opt_match:
                        opt = opt_match.group(1)
                        if opt not in ['G', 'VG'] and len(opt) > 3:
                            options.append(opt)

            # Omvänd ordning på options (de lästes bakåt)
            options = options[::-1][:4]

            if question and len(options) == 4 and correct_idx >= 0 and correct_idx < 4:
                correct_option = options[correct_idx]
                new_explanation = generate_explanation(question, correct_option, options)
                # Ersätt explanationen
                new_line = re.sub(
                    r"explanation:\s*['\"]([^'\"]+)['\"]",
                    f"explanation: '{new_explanation}'",
                    line
                )
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

        i += 1

    # Skriv till output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✓ Fixed {len([l for l in new_lines if 'explanation:' in l])} explanations")


if __name__ == '__main__':
    fix_quiz_file(
        'apps/frontend/src/data/manpage-tenta-quiz.ts',
        'apps/frontend/src/data/manpage-tenta-quiz.ts'
    )
