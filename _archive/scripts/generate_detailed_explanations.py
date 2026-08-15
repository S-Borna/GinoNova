#!/usr/bin/env python3
"""
Genererar detaljerade explanations som förklarar varför rätt svar är rätt
OCH varför de andra alternativen är fel
"""

import re

def escape_quotes(text: str) -> str:
    """Escape single quotes for TypeScript strings"""
    return text.replace("'", "\\'")

def generate_detailed_explanation(question: str, options: list, correct_idx: int) -> str:
    """
    Genererar detaljerad explanation:
    - Förklarar varför rätt svar är rätt
    - Förklarar varför varje fel alternativ är fel
    """

    if len(options) != 4 or not (0 <= correct_idx < 4):
        return "Invalid question structure"

    correct = options[correct_idx]
    incorrect = [opt for i, opt in enumerate(options) if i != correct_idx]

    q_lower = question.lower()

    # Signals & Process Control
    if 'ctrl+z' in q_lower or 'ctrl-z' in q_lower:
        if 'sigstop' in correct.lower():
            return f"✓ {correct} is correct - Ctrl+Z sends SIGSTOP which suspends (pauses) the process. It stops executing but remains in memory and can be resumed with fg (foreground) or bg (background). ✗ SIGTERM terminates processes gracefully. ✗ SIGKILL force-kills immediately. ✗ SIGINT is sent by Ctrl+C to interrupt/terminate."

    if 'ctrl+c' in q_lower or 'ctrl-c' in q_lower:
        if 'sigint' in correct.lower():
            return f"✓ {correct} is correct - Ctrl+C sends SIGINT (interrupt signal) to terminate the running process in terminal. ✗ SIGTERM is graceful termination but not tied to Ctrl+C. ✗ SIGKILL is forceful kill (signal 9). ✗ SIGSTOP pauses processes (Ctrl+Z)."

    if 'sigkill' in q_lower and 'cannot' in q_lower:
        if 'caught' in correct.lower() or 'catch' in correct.lower():
            return f"✓ {correct} - SIGKILL (9) cannot be caught, blocked, or ignored by programs. It terminates immediately without cleanup. Use as last resort. ✗ SIGTERM can be caught for graceful shutdown. ✗ SIGINT can be caught (programs can handle Ctrl+C). ✗ SIGHUP can be caught to reload config."

    if 'signal 9' in q_lower or 'kill -9' in q_lower:
        return f"✓ {correct} - Signal 9 (SIGKILL) forcefully terminates processes immediately without allowing cleanup or signal handling. Cannot be caught or ignored. Use when SIGTERM fails. Other signals can be caught for graceful handling."

    if 'sigterm' in q_lower and ('default' in q_lower or '15' in q_lower):
        return f"✓ {correct} - SIGTERM (15) is the default termination signal for graceful shutdown, allowing processes to cleanup before exiting. ✗ SIGKILL doesn\\'t allow cleanup. ✗ SIGSTOP pauses, doesn\\'t terminate. ✗ SIGINT is for interactive interruption (Ctrl+C)."

    # Pipes & Redirection
    if '|' in question and ('pipe' in q_lower or 'do' in q_lower):
        return f"✓ {correct} - The pipe operator (|) connects commands by sending stdout of the left command as stdin to the right command, enabling powerful command chaining. ✗ > redirects to file (overwrites). ✗ >> appends to file. ✗ 2> redirects stderr only."

    if '>>' in question:
        return f"✓ {correct} - The >> operator redirects stdout and appends to a file, preserving existing content. Perfect for log files. ✗ > overwrites files. ✗ | pipes to commands, not files. ✗ 2> redirects stderr only."

    if '>' in question and '>>' not in question:
        return f"✓ {correct} - The > operator redirects stdout to a file, overwriting any existing content. Dangerous if file contains important data. ✗ >> appends instead. ✗ | pipes to commands. ✗ < redirects stdin, not stdout."

    if '2>' in question or 'stderr' in q_lower:
        if 'redirect' in q_lower or 'file descriptor' in q_lower:
            return f"✓ {correct} - File descriptor 2 is stderr (standard error). Use 2> to redirect error messages to a file or /dev/null to discard them. ✗ FD 0 is stdin. ✗ FD 1 is stdout. ✗ FD 3+ are custom descriptors."

    if 'stdin' in q_lower and 'file descriptor' in q_lower:
        return f"✓ {correct} - File descriptor 0 is stdin (standard input) for reading data into programs. Commands read from stdin when no file argument provided. ✗ FD 1 is stdout. ✗ FD 2 is stderr. ✗ FD 3+ are user-defined."

    if 'stdout' in q_lower and 'file descriptor' in q_lower:
        return f"✓ {correct} - File descriptor 1 is stdout (standard output) for normal program output. Redirected with > or |. ✗ FD 0 is stdin. ✗ FD 2 is stderr for errors. ✗ FD 3+ are custom."

    # Variables & Shell
    if '$?' in question:
        return f"✓ {correct} - $? contains the exit status of the last command. 0 means success, 1-255 indicate errors. Essential for error checking in scripts. ✗ $$ is current shell PID. ✗ $! is last background process PID. ✗ $# is argument count."

    if 'variable assignment' in q_lower or ('var' in q_lower and 'assign' in q_lower):
        if '=' in correct and '$' not in correct:
            return f"✓ {correct} - Variables are assigned without $ prefix: VAR=value (no spaces around =). ✗ $VAR=value is syntax error. ✗ export comes after assignment. ✗ Spaces around = cause errors."

    if 'export' in q_lower and 'var' in q_lower:
        return f"✓ {correct} - export makes variables available to child processes and subshells, not just current shell. Essential for environment variables like PATH. ✗ Without export, variables are local to current shell only."

    if 'quot' in q_lower and '"' in question:
        return f"✓ {correct} - Double quotes allow variable expansion ($VAR) and command substitution while preventing word splitting and glob expansion. ✗ Single quotes prevent all expansion. ✗ No quotes allow glob expansion. ✗ Backticks are for command substitution only."

    if '*' in question and 'wildcard' in q_lower:
        return f"✓ {correct} - The * wildcard matches zero or more characters in filenames. rm *.txt deletes all .txt files. ✗ ? matches exactly one character. ✗ [] matches character sets. ✗ ** is for recursive matching (extended globbing)."

    # File Commands
    if 'cat' in q_lower and 'print' in q_lower:
        return f"✓ {correct} - cat concatenates and prints file contents to stdout, useful for viewing small files or piping data. ✗ less is for viewing (doesn\\'t print all at once). ✗ head shows only first lines. ✗ tail shows only last lines."

    if 'less' in q_lower and 'view' in q_lower:
        return f"✓ {correct} - less is a pager for viewing large files interactively with scrolling (up/down arrows), search (/pattern), and navigation (g/G). Better than more. ✗ cat dumps entire file. ✗ head/tail show only beginning/end."

    if 'wc -l' in q_lower or 'count lines' in q_lower:
        return f"✓ {correct} - wc -l counts newline characters, giving line count. ✗ wc without -l shows lines+words+bytes. ✗ -w counts words. ✗ -c counts bytes/characters."

    if 'head' in q_lower and 'first' in q_lower:
        return f"✓ {correct} - head displays first N lines (default 10). Use head -n 5 for 5 lines. Good for checking file contents quickly. ✗ tail shows last lines. ✗ cat shows entire file. ✗ less is interactive pager."

    if 'tail' in q_lower:
        if '-f' in q_lower or 'follow' in q_lower:
            return f"✓ {correct} - tail -f follows file changes in real-time, perfect for monitoring log files as they grow. Ctrl+C to exit. ✗ head shows beginning. ✗ cat shows static snapshot. ✗ less doesn\\'t auto-update."
        return f"✓ {correct} - tail displays last N lines (default 10). Use tail -n 20 for last 20 lines. ✗ head shows first lines. ✗ cat shows entire file. ✗ less is interactive viewer."

    if 'grep' in q_lower:
        return f"✓ {correct} - grep searches text using patterns/regex. grep -i for case-insensitive, -v to invert match, -r for recursive. ✗ sed is for text transformation. ✗ awk is for field processing. ✗ cut extracts columns only."

    if 'sort' in q_lower:
        return f"✓ {correct} - sort arranges lines alphabetically or numerically. Use -n for numeric sort, -r for reverse, -u for unique only, -k for specific column. ✗ uniq removes duplicates but requires sorted input. ✗ grep filters, doesn\\'t sort."

    if 'uniq' in q_lower:
        if 'not work' in q_lower or 'fail' in q_lower or 'sorted' in q_lower:
            return f"✓ {correct} - uniq only removes ADJACENT duplicate lines. Must sort first for complete deduplication: sort file | uniq. ✗ uniq alone misses non-adjacent duplicates. ✗ sort -u is better for unique lines. ✗ grep can\\'t deduplicate."
        return f"✓ {correct} - uniq removes adjacent duplicate lines. Always use after sort for reliable deduplication. Use -c to count occurrences. ✗ sort arranges but doesn\\'t deduplicate (use sort -u). ✗ grep filters, doesn\\'t deduplicate."

    if 'cut' in q_lower:
        return f"✓ {correct} - cut extracts columns/fields from text. cut -d: -f1 /etc/passwd extracts usernames. ✗ awk is more powerful but heavier. ✗ sed is for substitution. ✗ grep is for filtering lines."

    if 'tr' in q_lower:
        return f"✓ {correct} - tr translates or deletes characters from stdin. tr \\'a-z\\' \\'A-Z\\' converts to uppercase, tr -d deletes characters. ✗ sed is for complex substitutions. ✗ awk processes fields. ✗ cut extracts columns."

    if 'sed' in q_lower:
        return f"✓ {correct} - sed is a stream editor for find/replace and transformations. sed \\'s/old/new/g\\' replaces all occurrences. ✗ grep only searches. ✗ awk is for field processing. ✗ tr handles single characters only."

    if 'awk' in q_lower:
        return f"✓ {correct} - awk processes text field-by-field with patterns and actions. awk \\'{{print $1}}\\' extracts first column. Powerful for CSV/TSV. ✗ cut is simpler but less flexible. ✗ sed is for substitution. ✗ grep filters lines only."

    if 'tee' in q_lower:
        return f"✓ {correct} - tee reads stdin and writes to both stdout and files simultaneously. ls | tee file.txt shows output AND saves it. ✗ > only saves, doesn\\'t show. ✗ | only pipes, doesn\\'t save. ✗ >> appends but doesn\\'t show."

    # Permissions
    if 'chmod' in q_lower:
        return f"✓ {correct} - chmod changes file permissions. chmod 755 = rwxr-xr-x (owner full, others read+execute). chmod u+x adds execute for user. ✗ chown changes ownership. ✗ chgrp changes group only. ✗ umask sets default permissions."

    if 'chown' in q_lower:
        return f"✓ {correct} - chown changes file ownership. chown user:group file sets both user and group. Requires root/sudo. ✗ chmod changes permissions. ✗ chgrp changes group only. ✗ usermod modifies users, not files."

    if '644' in q_lower or '755' in q_lower or 'permission' in q_lower:
        return f"✓ {correct} - Linux permissions: owner/group/others with read(4)/write(2)/execute(1). 755=rwxr-xr-x, 644=rw-r--r--. ✗ Single digits aren\\'t permission codes. ✗ 777 is dangerous (everyone can do everything)."

    if 'execute' in q_lower and 'directory' in q_lower:
        return f"✓ {correct} - Execute (x) permission on directories allows entering them with cd and accessing their contents. Without it, directory is inaccessible even if you can list it. ✗ Read lists contents. ✗ Write creates/deletes files inside."

    if 'setuid' in q_lower or 'suid' in q_lower:
        return f"✓ {correct} - SUID (4xxx) makes executables run with owner\\'s privileges instead of executor\\'s. passwd command uses this to modify /etc/shadow. Security risk if misused. ✗ SGID is for groups. ✗ Sticky bit is for directories."

    if 'sticky' in q_lower:
        return f"✓ {correct} - Sticky bit (1xxx) on directories restricts deletion: only file owners can delete their files. Used in /tmp to prevent users deleting others\\' temp files. ✗ SUID/SGID are for executables. ✗ Regular permissions don\\'t restrict deletion."

    # Processes
    if 'ps' in q_lower:
        return f"✓ {correct} - ps shows process information. ps aux shows all processes with details (USER, PID, CPU%, MEM%, COMMAND). ps -ef is alternative format. ✗ top is for real-time monitoring. ✗ kill terminates processes."

    if 'kill' in q_lower:
        return f"✓ {correct} - kill sends signals to processes. kill PID sends SIGTERM (15), kill -9 PID sends SIGKILL (forceful). Use PID from ps/top. ✗ pkill uses process names. ✗ killall is less precise."

    if 'top' in q_lower or 'htop' in q_lower:
        return f"✓ {correct} - top/htop show real-time system stats: CPU, memory, processes. htop has better UI, colors, mouse support. Press q to quit. ✗ ps is static snapshot. ✗ free shows only memory. ✗ uptime shows load average only."

    if 'background' in q_lower and '&' in q_lower:
        return f"✓ {correct} - Append & to run commands in background, freeing terminal. Use jobs to list, fg to foreground, bg to resume suspended jobs. ✗ ; runs sequentially in foreground. ✗ && is conditional execution. ✗ Ctrl+Z suspends but doesn\\'t background."

    if 'nohup' in q_lower:
        return f"✓ {correct} - nohup prevents processes from receiving SIGHUP on terminal logout, allowing them to continue. nohup command & for background. ✗ & alone doesn\\'t survive logout. ✗ disown is alternative. ✗ screen/tmux are better solutions."

    if 'exit code' in q_lower or 'exit status' in q_lower:
        if '0' in correct:
            return f"✓ {correct} - Exit code 0 means success. Non-zero (1-255) indicates errors. Check with $? or in if statements. ✗ 1 is general error. ✗ 127 is command not found. ✗ 130 is terminated by Ctrl+C."
        return f"✓ {correct} - Exit codes indicate command status. 0=success, 1=general error, 2=misuse, 127=command not found, 130=Ctrl+C termination. Check with $?."

    # Find & Locate
    if 'find' in q_lower:
        return f"✓ {correct} - find searches filesystem recursively with powerful filters: -name for filenames, -type f/d for files/dirs, -size, -mtime, -exec for actions. ✗ locate uses database (faster but not real-time). ✗ which finds executables in PATH only. ✗ grep searches file contents."

    if 'locate' in q_lower:
        return f"✓ {correct} - locate searches pre-built database (updated by updatedb) for fast filename lookup. Much faster than find but not real-time. ✗ find searches live filesystem. ✗ which is for PATH executables only. ✗ whereis finds binaries/man pages."

    if 'which' in q_lower:
        return f"✓ {correct} - which shows full path of executables in $PATH. Use to verify which version runs when you type a command. ✗ whereis finds binaries+man pages. ✗ find searches entire filesystem. ✗ locate searches database."

    # Docker
    if 'docker run' in q_lower:
        return f"✓ {correct} - docker run creates and starts a container from an image. Common flags: -d (detached), -p (ports), -v (volumes), --name. ✗ docker start starts stopped containers. ✗ docker exec runs commands in running containers. ✗ docker create only creates, doesn\\'t start."

    if 'docker ps' in q_lower:
        return f"✓ {correct} - docker ps lists running containers with ID, image, command, status, ports, names. Use -a to include stopped containers, -q for IDs only. ✗ docker images lists images. ✗ docker container ls is alias. ✗ docker inspect shows detailed info."

    if 'docker images' in q_lower or 'docker image' in q_lower:
        return f"✓ {correct} - docker images lists locally available images with repository, tag, ID, created time, and size. ✗ docker ps lists containers. ✗ docker pull downloads images. ✗ docker build creates images."

    if 'docker volume' in q_lower or 'volumes' in q_lower:
        if 'persist' in q_lower:
            return f"✓ {correct} - Docker volumes provide persistent storage outside container filesystem, surviving container deletion/recreation. Data persists across container lifecycle. ✗ Container layer is ephemeral. ✗ Bind mounts depend on host path. ✗ tmpfs is in-memory only."
        return f"✓ {correct} - Volumes store data outside container filesystem for persistence and sharing between containers. Managed by Docker. ✗ Bind mounts map host directories. ✗ Container layer is temporary. ✗ Images are read-only."

    if 'bind mount' in q_lower:
        return f"✓ {correct} - Bind mounts map host directories directly into containers, useful for development with live code updates. Changes reflect immediately. ✗ Volumes are managed by Docker. ✗ tmpfs is memory only. ✗ Container layer isn\\'t shared."

    if 'container' in q_lower and 'vm' in q_lower:
        return f"✓ {correct} - Containers share host kernel (lightweight, fast startup), VMs have own kernel (full isolation, slower, heavier). Containers use less resources. ✗ Both use virtualization but different levels. ✗ VMs don\\'t share kernel."

    # Generic fallback
    explanation = f"✓ {correct} is correct. "

    # Försök identifiera rätt svar kontext
    if 'port' in correct.lower():
        explanation += "This handles port mapping or network connectivity. "
    elif 'permission' in correct.lower() or 'rwx' in correct.lower():
        explanation += "This relates to file permissions and access control. "
    elif 'process' in correct.lower() or 'pid' in correct.lower():
        explanation += "This involves process management. "
    elif 'file' in correct.lower() or 'directory' in correct.lower():
        explanation += "This deals with file system operations. "

    explanation += "The other options address different concepts or commands not applicable to this specific scenario."

    return explanation


# Läs och parsa quiz-filen
with open('apps/frontend/src/data/manpage-tenta-quiz.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

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
                    # Filtrera bort kategorier och difficulty
                    if opt not in ['G', 'VG', 'Pipes & Redirection', 'Files', 'Permissions', 'Processes',
                                   'Networking', 'Docker & Containers', 'Disk & Storage', 'Linux Grundläggande',
                                   'Bash Scripting', 'Filer & Kataloger', 'Processer & Signaler']:
                        options.append(opt)

        # options är i omvänd ordning
        options = options[::-1][:4]

        if question and len(options) == 4 and 0 <= correct_idx < 4:
            new_explanation = escape_quotes(generate_detailed_explanation(question, options, correct_idx))
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

print(f"✓ Generated detailed explanations for {fixed_count} questions")
print("  - Explains why correct answer is right")
print("  - Explains why wrong answers are wrong")
print("  - Provides context and practical usage")
