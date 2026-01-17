/**
 * MANPAGE TENTAN - Omfattande Linux/Unix kommandoreferens quiz
 * 265 frågor om bash, pipes, filer, permissions, processer, nätverk, containers m.m.
 *
 * Skapad: 2026-01-17
 * Källa: ManpageTentan.md - Komplett tentamaterial
 * Innehåll: 210 G-frågor + 55 VG-frågor
 */

export interface ManpageTentaQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
}

export const MANPAGE_TENTA_QUESTIONS: ManpageTentaQuestion[] = [
    {
        id: 'manpage-g1',
        question: 'What does | do in bash?',
        options: [
            'Redirects output to a file',
            'Appends output to a file',
            'Redirects stderr',
            'Sends output of one command as input to another',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g2',
        question: 'What does > do?',
        options: [
            'Pipe output',
            'Overwrite a file with output',
            'Redirect stderr',
            'Append output',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g3',
        question: 'What does >> do?',
        options: [
            'Redirect stdin',
            'Pipe',
            'Overwrite',
            'Append',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g4',
        question: 'What does 2> redirect?',
        options: [
            'all output',
            'stdin',
            'stderr',
            'stdout',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g5',
        question: 'Which file descriptor is stdout?',
        options: [
            '1',
            '3',
            '0',
            '2',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g6',
        question: 'What is $??',
        options: [
            'Last command exit status',
            'Shell version',
            'User ID',
            'PID',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g7',
        question: 'Which is a valid variable assignment?',
        options: [
            '$VAR=value',
            'value=VAR',
            'VAR=value',
            'export $VAR',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g8',
        question: 'What does quoting with " allow?',
        options: [
            'No expansion',
            'Command blocking',
            'File locking',
            'Variable expansion',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g9',
        question: 'What does * represent?',
        options: [
            'Numbers only',
            'Any number of characters',
            'Single character',
            'Hidden files only',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g10',
        question: 'What does export VAR do?',
        options: [
            'Makes variable global',
            'Locks variable',
            'Prints variable',
            'Deletes variable',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g11',
        question: 'Which command prints a file to stdout?',
        options: [
            'sort',
            'cat',
            'less',
            'wc',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g12',
        question: 'Which command is best for viewing large files?',
        options: [
            'cat',
            'echo',
            'less',
            'tr',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g13',
        question: 'What does head -n 5 file do?',
        options: [
            'Sorts lines',
            'Shows last 5 lines',
            'Shows first 5 lines',
            'Deletes 5 lines',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g14',
        question: 'What does tail -f do?',
        options: [
            'Follows file updates',
            'Compresses file',
            'Deletes file',
            'Sorts output',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g15',
        question: 'What does wc -l show?',
        options: [
            'Characters',
            'Words',
            'Lines',
            'Bytes',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g16',
        question: 'Which command sorts numerically?',
        options: [
            'uniq',
            'cut',
            'sort -n',
            'sort',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g17',
        question: 'uniq requires input to be:',
        options: [
            'Binary',
            'Compressed',
            'Large',
            'Sorted',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g18',
        question: 'What does cut -d : -f 1 do?',
        options: [
            'Deletes file',
            'Cuts first field using :',
            'Sorts output',
            'Replaces colons',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g19',
        question: 'What does tr a-z A-Z do?',
        options: [
            'Converts lowercase to uppercase',
            'Deletes lowercase',
            'Sorts text',
            'Removes spaces',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g20',
        question: 'Pipes work with:',
        options: [
            'Users',
            'Variables',
            'Files only',
            'Commands',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g21',
        question: 'What does pwd show?',
        options: [
            'Current directory',
            'Root directory',
            'Home directory',
            'Previous directory',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g22',
        question: 'Which flag shows hidden files?',
        options: [
            '-a',
            '-l',
            '-r',
            '-h',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g23',
        question: 'What does cp -r do?',
        options: [
            'Rename files',
            'Copy directories recursively',
            'Copy files only',
            'Remove directories',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g24',
        question: 'What does mv do?',
        options: [
            'Compress files',
            'Move or rename files',
            'Copy files',
            'Delete files',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g25',
        question: 'What does rm -r allow?',
        options: [
            'Remove directories recursively',
            'Remove files only',
            'Restore files',
            'Remove read-only files',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g26',
        question: 'What does mkdir -p do?',
        options: [
            'Deletes directories',
            'Moves directories',
            'Locks directories',
            'Creates parent directories',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g27',
        question: 'rmdir removes:',
        options: [
            'Any directory',
            'Files',
            'Empty directories',
            'Non-empty directories',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g28',
        question: 'What does file show?',
        options: [
            'Size only',
            'Permissions',
            'File type',
            'Owner',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g29',
        question: 'stat shows:',
        options: [
            'Processes',
            'Metadata',
            'Packages',
            'Content',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g30',
        question: 'find / -name test.txt does what?',
        options: [
            'Searches file system',
            'Compresses file',
            'Deletes file',
            'Copies file',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g31',
        question: 'What does permission 755 mean?',
        options: [
            'rwx rwx rwx',
            'rwx r-x r-x',
            'rw- r-- r--',
            'r-- r-- r--',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g32',
        question: 'Which command changes permissions?',
        options: [
            'chown',
            'umask',
            'chgrp',
            'chmod',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g33',
        question: 'Symbolic mode u+x means:',
        options: [
            'Remove execute',
            'Add execute to group',
            'Add execute to user',
            'Remove write',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g34',
        question: 'chown user:group file does what?',
        options: [
            'Changes owner and group',
            'Deletes file',
            'Moves file',
            'Changes permissions',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g35',
        question: 'chgrp changes:',
        options: [
            'Size',
            'Permissions',
            'Group',
            'Owner',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g36',
        question: 'umask affects:',
        options: [
            'Existing files',
            'Ownership',
            'File size',
            'Default permissions',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g37',
        question: 'Default file permission base is:',
        options: [
            '644',
            '777',
            '666',
            '755',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g38',
        question: 'Default directory permission base is:',
        options: [
            '644',
            '666',
            '755',
            '777',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g39',
        question: 'Who can change file ownership?',
        options: [
            'Any user',
            'Group',
            'File owner',
            'Root',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g40',
        question: 'Execute permission on directory allows:',
        options: [
            'Writing files',
            'Deleting directory',
            'Reading files',
            'Entering directory',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g41',
        question: 'Which command creates a user?',
        options: [
            'mkuser',
            'adduser',
            'newuser',
            'useradd',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g42',
        question: 'Remove user and home directory?',
        options: [
            'deluser',
            'userdel -r',
            'rmuser',
            'userdel',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g43',
        question: 'Which command changes password?',
        options: [
            'chpass',
            'login',
            'passwd',
            'usermod',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g44',
        question: 'What does id show?',
        options: [
            'Processes',
            'Disk usage',
            'Permissions',
            'UID and groups',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g45',
        question: 'su does what?',
        options: [
            'Switch user',
            'Suspend',
            'Super update',
            'Shutdown',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g46',
        question: 'sudo allows:',
        options: [
            'Login as root permanently',
            'Create users',
            'Change kernel',
            'Run commands as another user',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g47',
        question: 'sudo configuration is in:',
        options: [
            '/etc/shadow',
            '/etc/sudoers',
            '/etc/passwd',
            '/etc/group',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g48',
        question: 'Which user has UID 0?',
        options: [
            'admin',
            'root',
            'nobody',
            'system',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g49',
        question: 'Groups are defined in:',
        options: [
            '/etc/shadow',
            '/etc/group',
            '/etc/passwd',
            '/etc/users',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g50',
        question: 'passwd without arguments changes:',
        options: [
            'group password',
            'root password',
            'current user password',
            'all passwords',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g51',
        question: 'Which command lists processes?',
        options: [
            'kill',
            'uptime',
            'top',
            'ps',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g52',
        question: 'ps aux shows:',
        options: [
            'Current user only',
            'Network processes',
            'All processes',
            'Only root processes',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g53',
        question: 'Which command sends a signal?',
        options: [
            'exit',
            'kill',
            'end',
            'stop',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g54',
        question: 'Default signal sent by kill is:',
        options: [
            'SIGKILL',
            'SIGSTOP',
            'SIGTERM',
            'SIGINT',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g55',
        question: 'Which signal cannot be caught?',
        options: [
            'SIGKILL',
            'SIGHUP',
            'SIGINT',
            'SIGTERM',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g56',
        question: 'pkill differs by:',
        options: [
            'User',
            'PID',
            'Port',
            'Name',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g57',
        question: 'top shows:',
        options: [
            'Users',
            'Disk usage',
            'Processes in real time',
            'Network stats',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g58',
        question: 'uptime shows:',
        options: [
            'Memory usage',
            'Load average',
            'CPU model',
            'Boot logs',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g59',
        question: 'nice affects:',
        options: [
            'Memory size',
            'Disk IO',
            'Network speed',
            'Process priority',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g60',
        question: 'PID stands for:',
        options: [
            'Program ID',
            'Process ID',
            'Package ID',
            'Permission ID',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g61',
        question: 'Which is a package manager?',
        options: [
            'all of the above',
            'apt',
            'dnf',
            'yum',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g62',
        question: 'apt update does what?',
        options: [
            'Installs packages',
            'Removes packages',
            'Upgrades kernel',
            'Updates package lists',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g63',
        question: 'apt upgrade does what?',
        options: [
            'Updates package lists',
            'Removes packages',
            'Reinstalls OS',
            'Upgrades installed packages',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g64',
        question: 'which ls shows:',
        options: [
            'ls size',
            'ls manual',
            'ls binary path',
            'ls permissions',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g65',
        question: 'whereis shows:',
        options: [
            'Binary, source, man',
            'Only binary',
            'Package version',
            'Running process',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g66',
        question: 'uname -a shows:',
        options: [
            'Disk info',
            'Users',
            'Processes',
            'Kernel info',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g67',
        question: 'df -h shows:',
        options: [
            'Network usage',
            'Disk usage',
            'CPU usage',
            'RAM usage',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g68',
        question: 'du -sh shows:',
        options: [
            'Directory size',
            'RAM free',
            'Disk free',
            'Swap usage',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g69',
        question: 'free shows:',
        options: [
            'Disk space',
            'CPU cores',
            'RAM usage',
            'Network ports',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g70',
        question: 'Human readable flag is:',
        options: [
            '-h',
            '-r',
            '-l',
            '-a',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g71',
        question: 'Which creates a tar archive?',
        options: [
            'tar -z',
            'tar -f',
            'tar -c',
            'tar -x',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g72',
        question: 'Which extracts a tar archive?',
        options: [
            '-f',
            '-v',
            '-c',
            '-x',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g73',
        question: '-f in tar means:',
        options: [
            'fast',
            'follow',
            'force',
            'file',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g74',
        question: 'Which adds gzip compression?',
        options: [
            '-x',
            '-j',
            '-v',
            '-z',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g75',
        question: 'gzip does what?',
        options: [
            'Encrypt file',
            'Compress file',
            'Archive',
            'Delete file',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g76',
        question: 'gunzip does what?',
        options: [
            'Decompress',
            'Archive',
            'Encrypt',
            'Compress',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g77',
        question: 'zip creates:',
        options: [
            'tar archive',
            'zip archive',
            'gzip archive',
            'iso image',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g78',
        question: 'unzip does what?',
        options: [
            'Encrypt',
            'Compress',
            'Extract zip',
            'Delete',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g79',
        question: 'tar archives preserve:',
        options: [
            'Nothing',
            'File order only',
            'Users only',
            'Permissions',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g80',
        question: 'Which is NOT compression?',
        options: [
            'gzip',
            'tar',
            'gunzip',
            'zip',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g81',
        question: 'Which command manages services?',
        options: [
            'service',
            'systemctl',
            'init',
            'journalctl',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g82',
        question: 'Start a service:',
        options: [
            'systemctl boot',
            'systemctl enable',
            'systemctl run',
            'systemctl start',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g83',
        question: 'Enable service at boot:',
        options: [
            'stop',
            'reload',
            'start',
            'enable',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g84',
        question: 'Check service status:',
        options: [
            'systemctl show',
            'systemctl check',
            'systemctl status',
            'systemctl info',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g85',
        question: 'journalctl shows:',
        options: [
            'Users',
            'Logs',
            'Kernel config',
            'Processes',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g86',
        question: 'journalctl -xe shows:',
        options: [
            'Network logs',
            'Errors',
            'Old logs',
            'Disk logs',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g87',
        question: 'systemd is:',
        options: [
            'Package manager',
            'Init system',
            'Shell',
            'Filesystem',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g88',
        question: 'systemd replaces:',
        options: [
            'apt',
            'sysvinit',
            'bash',
            'cron',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g89',
        question: 'Units are defined in:',
        options: [
            '.conf',
            '.unit',
            '.service',
            '.sys',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g90',
        question: 'systemctl stop does what?',
        options: [
            'Restart system',
            'Disable service',
            'Remove service',
            'Stop service',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g91',
        question: 'ping checks:',
        options: [
            'Ports',
            'Speed',
            'Reachability',
            'DNS',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g92',
        question: 'ip a shows:',
        options: [
            'Routes',
            'Users',
            'Ports',
            'Interfaces',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g93',
        question: 'ss replaces:',
        options: [
            'ping',
            'netstat',
            'curl',
            'wget',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g94',
        question: 'curl is mainly used to:',
        options: [
            'Edit files',
            'Compress data',
            'Fetch URLs',
            'Upload files',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g95',
        question: 'wget does what?',
        options: [
            'Port scan',
            'API testing',
            'Download files',
            'DNS lookup',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g96',
        question: 'A container is:',
        options: [
            'Kernel',
            'Filesystem',
            'Isolated process',
            'Virtual machine',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g97',
        question: 'Container localhost refers to:',
        options: [
            'Router',
            'Host',
            'Container itself',
            'Network',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g98',
        question: 'Host can access container via:',
        options: [
            'Port mapping',
            'DNS only',
            'localhost only',
            'SSH only',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g99',
        question: 'Docker volumes are used for:',
        options: [
            'Networking',
            'Logging',
            'Persistence',
            'Security',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g100',
        question: 'Bind mounts differ by:',
        options: [
            'Speed',
            'Host path usage',
            'Encryption',
            'Size',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g101',
        question: 'What does [ -f file ] test?',
        options: [
            'Directory',
            'Executable',
            'Regular file',
            'Empty file',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g102',
        question: 'What command is [ an alias for?',
        options: [
            'if',
            'test',
            'case',
            'expr',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g103',
        question: 'What does shift do in bash?',
        options: [
            'Deletes variables',
            'Exits script',
            'Removes first positional parameter',
            'Sorts arguments',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g104',
        question: '$1 refers to:',
        options: [
            'Script name',
            'First argument',
            'Last argument',
            'Exit code',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g105',
        question: '$0 refers to:',
        options: [
            'First argument',
            'PID',
            'Script name',
            'Exit code',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g106',
        question: 'How do you read user input?',
        options: [
            'input',
            'echo',
            'scan',
            'read',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g107',
        question: 'What does echo $VAR do?',
        options: [
            'Deletes variable',
            'Prints variable value',
            'Exports variable',
            'Sets variable',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g108',
        question: 'What does env show?',
        options: [
            'Environment variables',
            'Users',
            'Files',
            'Processes',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g109',
        question: 'Which variable affects command lookup?',
        options: [
            'HOME',
            'PATH',
            'SHELL',
            'USER',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g110',
        question: 'Exit code 0 means:',
        options: [
            'Error',
            'Success',
            'Interrupt',
            'Warning',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g111',
        question: 'locate is fast because it:',
        options: [
            'Uses cache only',
            'Uses database',
            'Scans disk live',
            'Uses network',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g112',
        question: 'Which command finds files by name in real time?',
        options: [
            'locate',
            'find',
            'whereis',
            'which',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g113',
        question: 'find . -type d finds:',
        options: [
            'Directories',
            'Links',
            'Devices',
            'Files',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g114',
        question: 'find / -name "*.log" does what?',
        options: [
            'Compresses logs',
            'Deletes logs',
            'Finds log files',
            'Prints logs',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g115',
        question: 'Which hides permission errors?',
        options: [
            '| null',
            '> /dev/null',
            '&>/null',
            '2>/dev/null',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g116',
        question: 'which ls outputs:',
        options: [
            'Alias',
            'Package',
            'Man page',
            'Binary path',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g117',
        question: 'whereis ls outputs:',
        options: [
            'Permissions',
            'Binary, man, source',
            'Only binary',
            'PID',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g118',
        question: 'find can search by:',
        options: [
            'Type',
            'Size',
            'All above',
            'Name',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g119',
        question: '-type f means:',
        options: [
            'Folder',
            'Link',
            'FIFO',
            'File',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g120',
        question: 'locate database is updated by:',
        options: [
            'find',
            'locate',
            'cron',
            'updatedb',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g121',
        question: 'ls -l shows:',
        options: [
            'Long listing',
            'Hidden files',
            'Inodes',
            'Sizes only',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g122',
        question: 'ls -h affects:',
        options: [
            'Sorting',
            'Ownership',
            'Permissions',
            'Size format',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g123',
        question: 'File permissions are shown by:',
        options: [
            'ls -l',
            'ls -a',
            'ls -r',
            'ls -t',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g124',
        question: 'file script.sh returns:',
        options: [
            'Content',
            'Owner',
            'Permissions',
            'File type',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g125',
        question: 'Which shows last modification time?',
        options: [
            'stat',
            'ls',
            'file',
            'pwd',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g126',
        question: 'Which is NOT shown by stat?',
        options: [
            'Permissions',
            'Size',
            'Owner',
            'Content',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g127',
        question: 'ls -a includes:',
        options: [
            'Backup files',
            'Executables only',
            'Hidden files',
            'Directories only',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g128',
        question: 'Hidden files start with:',
        options: [
            '~',
            '#',
            '_',
            '.',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g129',
        question: 'ls without flags sorts by:',
        options: [
            'Name',
            'Time',
            'Extension',
            'Size',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g130',
        question: 'Read permission on file allows:',
        options: [
            'Execute',
            'Delete',
            'Modify',
            'Read content',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g131',
        question: 'Write permission on directory allows:',
        options: [
            'Read files',
            'Execute files',
            'Create/delete files',
            'Enter directory',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g132',
        question: 'Execute permission on file allows:',
        options: [
            'Read',
            'Delete',
            'Run file',
            'Write',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g133',
        question: 'Permission 644 means:',
        options: [
            'r-- r-- r--',
            'rw- rw- rw-',
            'rwx r-x r-x',
            'rw- r-- r--',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g134',
        question: 'Who is checked first for permissions?',
        options: [
            'User',
            'Root',
            'Other',
            'Group',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g135',
        question: 'Group permissions apply when:',
        options: [
            'User is in group',
            'User is owner',
            'Never',
            'Always',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g136',
        question: 'chmod 700 file allows access for:',
        options: [
            'Group only',
            'Others only',
            'Everyone',
            'Owner only',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g137',
        question: 'Which permission allows directory listing?',
        options: [
            'r',
            'x',
            'rwx',
            'w',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g138',
        question: 'Which permission allows entering directory?',
        options: [
            'rw',
            'r',
            'x',
            'w',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g139',
        question: 'umask 022 results in file perms:',
        options: [
            '600',
            '666',
            '777',
            '644',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g140',
        question: 'Background process uses:',
        options: [
            '%',
            '!',
            '&',
            '*',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g141',
        question: 'Ctrl+C sends:',
        options: [
            'SIGINT',
            'SIGTERM',
            'SIGKILL',
            'SIGSTOP',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g142',
        question: 'Ctrl+Z sends:',
        options: [
            'SIGINT',
            'SIGSTOP',
            'SIGTERM',
            'SIGKILL',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g143',
        question: 'Resume background job command:',
        options: [
            'fg',
            'jobs',
            'bg',
            'kill',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g144',
        question: 'Bring job to foreground:',
        options: [
            'fg',
            'ps',
            'bg',
            'jobs',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g145',
        question: 'jobs shows:',
        options: [
            'Background jobs',
            'Processes',
            'Cron jobs',
            'System jobs',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g146',
        question: 'Which shows CPU usage?',
        options: [
            'top',
            'du',
            'free',
            'df',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g147',
        question: 'Which kills process by PID?',
        options: [
            'pkill',
            'stop',
            'kill',
            'end',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g148',
        question: 'Load average relates to:',
        options: [
            'Network',
            'Disk',
            'CPU',
            'Memory',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g149',
        question: 'df reports:',
        options: [
            'Disk free space',
            'Directory size',
            'RAM',
            'CPU',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g150',
        question: 'du reports:',
        options: [
            'Directory usage',
            'RAM usage',
            'Swap usage',
            'Disk free',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g151',
        question: 'du -sh gives:',
        options: [
            'Per file',
            'Inodes',
            'All files',
            'Summary',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g152',
        question: 'free shows:',
        options: [
            'Network',
            'CPU',
            'Memory',
            'Disk',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g153',
        question: 'Swap is:',
        options: [
            'Kernel',
            'Cache',
            'Disk backup',
            'Extra RAM on disk',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g154',
        question: 'Which unit is used by free -h?',
        options: [
            'Blocks',
            'Pages',
            'Bytes',
            'Human readable',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g155',
        question: 'Which command shows mounted filesystems?',
        options: [
            'mount',
            'df',
            'du',
            'free',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g156',
        question: 'Root filesystem is mounted at:',
        options: [
            '/',
            '/home',
            '/boot',
            '/root',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g157',
        question: 'Disk usage increasing unexpectedly suggests:',
        options: [
            'Memory leak',
            'Network issue',
            'CPU issue',
            'Log growth',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g158',
        question: 'Inodes exhaustion affects:',
        options: [
            'File creation',
            'File size',
            'CPU',
            'RAM',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g159',
        question: 'tar without compression creates:',
        options: [
            'bz2',
            'zip',
            'gzip',
            'tarball',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g160',
        question: '.tar.gz indicates:',
        options: [
            'tar + gzip',
            'zip',
            'encryption',
            'Two formats',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g161',
        question: 'tar -cvf a.tar dir does:',
        options: [
            'Encrypt',
            'Compress only',
            'Extract',
            'Create archive',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g162',
        question: 'tar -xvf a.tar does:',
        options: [
            'Create',
            'Compress',
            'Extract',
            'List',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g163',
        question: '-v in tar means:',
        options: [
            'Virtual',
            'Verbose',
            'Verify',
            'Version',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g164',
        question: 'Which supports directories easily?',
        options: [
            'gunzip',
            'zip',
            'gzip',
            'tar',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g165',
        question: 'Which is NOT an archive?',
        options: [
            'zip',
            'tar.gz',
            'gzip',
            'tar',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g166',
        question: 'Compression reduces:',
        options: [
            'Security',
            'Ownership',
            'File size',
            'Permissions',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g167',
        question: 'systemctl enable means:',
        options: [
            'Start now',
            'Restart',
            'Reload',
            'Start at boot',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g168',
        question: 'systemctl start means:',
        options: [
            'Enable',
            'Start immediately',
            'Stop',
            'Reload',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g169',
        question: 'systemctl disable means:',
        options: [
            'Kill process',
            'Stop now',
            'Prevent boot start',
            'Remove service',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g170',
        question: 'journalctl without args shows:',
        options: [
            'Errors only',
            'All logs',
            'Service logs only',
            'Kernel logs only',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g171',
        question: 'journalctl -b shows:',
        options: [
            'All boots',
            'Current boot',
            'Errors',
            'Last boot',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g172',
        question: 'journalctl -u ssh shows:',
        options: [
            'Network logs',
            'Kernel logs',
            'Disk logs',
            'SSH logs',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g173',
        question: 'systemd unit types include:',
        options: [
            'service',
            'mount',
            'target',
            'all above',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g174',
        question: 'systemd runs as PID:',
        options: [
            '0',
            '100',
            '2',
            '1',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g175',
        question: 'If PID 1 dies:',
        options: [
            'Restart shell',
            'Restart service',
            'Nothing',
            'System crashes',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g176',
        question: 'Legacy init system is:',
        options: [
            'cron',
            'sysvinit',
            'upstart',
            'bash',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g177',
        question: 'IP address identifies:',
        options: [
            'Host',
            'File',
            'Process',
            'User',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g178',
        question: 'IPv4 uses how many bits?',
        options: [
            '32',
            '16',
            '64',
            '24',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g179',
        question: 'ping uses protocol:',
        options: [
            'ICMP',
            'UDP',
            'HTTP',
            'TCP',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g180',
        question: 'ss shows:',
        options: [
            'Sockets',
            'DNS',
            'Interfaces',
            'Routes',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g181',
        question: 'ip route shows:',
        options: [
            'Ports',
            'Interfaces',
            'DNS',
            'Routing table',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g182',
        question: 'localhost IP is:',
        options: [
            '::1 only',
            '127.0.0.1',
            '192.168.0.1',
            '0.0.0.0',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g183',
        question: 'DNS resolves:',
        options: [
            'User to host',
            'IP to MAC',
            'Name to IP',
            'Port to process',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g184',
        question: '/etc/hosts is used for:',
        options: [
            'Routing',
            'Firewall',
            'DNS server',
            'Local name resolution',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g185',
        question: 'curl is often used for:',
        options: [
            'Email',
            'Browsing',
            'SSH',
            'API testing',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g186',
        question: 'Container is lighter than VM because:',
        options: [
            'Smaller disk',
            'Less RAM',
            'No kernel',
            'No OS',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g187',
        question: 'Container filesystem is:',
        options: [
            'Shared',
            'Encrypted',
            'Persistent by default',
            'Ephemeral',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g188',
        question: 'Docker volume is used to:',
        options: [
            'Secure container',
            'Persist data',
            'Speed up CPU',
            'Network',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g189',
        question: 'Bind mount uses:',
        options: [
            'Host path',
            'Image layer',
            'Docker storage',
            'Volume driver',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g190',
        question: 'Container localhost refers to:',
        options: [
            'Router',
            'Host',
            'Container',
            'Network',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g191',
        question: 'Host can reach container via:',
        options: [
            'DNS only',
            'Exposed port',
            'Container ID',
            'localhost always',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g192',
        question: 'Container stops when:',
        options: [
            'Shell exits',
            'User logs out',
            'Main process exits',
            'Network disconnects',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g193',
        question: 'Container isolation is done via:',
        options: [
            'Namespaces & cgroups',
            'Hypervisor',
            'BIOS',
            'Firmware',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g194',
        question: 'What is Docker primarily?',
        options: [
            'Containerplattform',
            'Pakethanterare',
            'Virtuell maskin',
            'Init-system',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g195',
        question: 'En container är best described as:',
        options: [
            'En komplett OS-instans',
            'En isolerad process',
            'En virtuell disk',
            'En kernelmodul',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g196',
        question: 'Which command lists running containers?',
        options: [
            'docker ps',
            'docker inspect',
            'docker list',
            'docker images',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g197',
        question: 'What shows docker images?',
        options: [
            'Nätverk',
            'Körande containrar',
            'Volymer',
            'Nedladdade images',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g198',
        question: 'What is en Docker image?',
        options: [
            'En körande container',
            'En volym',
            'A template for containers',
            'Ett nätverk',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g199',
        question: 'Which command starts a container?',
        options: [
            'docker exec',
            'docker run',
            'docker pull',
            'docker build',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g200',
        question: 'What happens om huvudprocessen i en container avslutas?',
        options: [
            'Containern stoppas',
            'Containern pausar',
            'Containern fortsätter',
            'Containern startas om automatiskt',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g201',
        question: 'What is flaggan -d till vid docker run?',
        options: [
            'Detached mode',
            'Download image',
            'Debug',
            'Delete on exit',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g202',
        question: 'What does docker pull?',
        options: [
            'Hämtar image',
            'Bygger image',
            'Tar bort image',
            'Startar container',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g203',
        question: 'Where do containrar?',
        options: [
            'I BIOS',
            'På hypervisor',
            'På hostens kernel',
            'I egen kernel',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g204',
        question: 'Which command lists all running processes for all users?',
        options: [
            'ps',
            'top',
            'jobs',
            'ps aux',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g205',
        question: 'What does permission chmod 640 file mean?',
        options: [
            'r-- r-- ---',
            'rw- r-- ---',
            'rw- rw- ---',
            'rwx r-- ---',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g206',
        question: 'You run cmd > out.txt but still see text in terminal. Why?',
        options: [
            'File is empty',
            'cmd kräver sudo',
            'Output goes to stderr',
            'Redirect is incorrect',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g207',
        question: 'Which command shows how much disk space is used per directory?',
        options: [
            'free',
            'du',
            'df',
            'ls -lh',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g208',
        question: 'What is en Docker image?',
        options: [
            'Ett Docker-nätverk',
            'A template for containers',
            'En körande container',
            'Ett Docker-volume',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g209',
        question: 'Why fungerar inte uniq file.txt alltid som förväntat?',
        options: [
            'uniq ignorerar whitespace',
            'File is not sorted',
            'uniq kräver flaggor',
            'File is too large',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g210',
        question: 'Which command starts a container in background?',
        options: [
            'docker pull -d',
            'docker run -d',
            'docker exec -d',
            'docker start -d',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g211',
        question: 'What shows ls -a?',
        options: [
            'Endast kataloger',
            'Filstorlek',
            'Filtyp',
            'Dolda filer',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g212',
        question: 'Which signal kan inte fångas av ett program?',
        options: [
            'SIGKILL',
            'SIGTERM',
            'SIGHUP',
            'SIGINT',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g213',
        question: 'What is the purpose of environment variable $PATH?',
        options: [
            'Styra rättigheter',
            'Lagra miljövariabler',
            'Set command paths',
            'Ange hemkatalog',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g214',
        question: 'Which command pulls a Docker image from registry?',
        options: [
            'docker build',
            'docker pull',
            'docker exec',
            'docker run',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g215',
        question: 'What does execute permission on directory mean?',
        options: [
            'Ta bort katalogen',
            'Gå in i katalogen',
            'Skapa filer',
            'Visa innehåll',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g216',
        question: 'Which command shows system load average?',
        options: [
            'ps',
            'free',
            'uptime',
            'df',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g217',
        question: 'What happens when main process in container exits?',
        options: [
            'Containern fortsätter',
            'Containern pausar',
            'Containern stoppas',
            'Containern startas om automatiskt',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g218',
        question: 'Which command extracts a tar archive?',
        options: [
            'tar -z',
            'tar -c',
            'tar -x',
            'tar -f',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g219',
        question: 'You can list a directory but not enter it. What is missing?',
        options: [
            'r',
            'ägare',
            'x',
            'w',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g220',
        question: 'Which command shows which ports are listening on the system?',
        options: [
            'ip a',
            'ss',
            'curl',
            'ping',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g221',
        question: 'What is Docker volumes främst used for?',
        options: [
            'CPU-begränsning',
            'Persistens',
            'Nätverk',
            'Säkerhet',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g222',
        question: 'Which command changes owner on a file?',
        options: [
            'umask',
            'chgrp',
            'chown',
            'chmod',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g223',
        question: 'What does journalctl?',
        options: [
            'Visar loggar',
            'Startar tjänster',
            'Skapar användare',
            'Hanterar nätverk',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g224',
        question: 'Why can two containers not reach each other via localhost?',
        options: [
            'Fel DNS',
            'Brandvägg',
            'Separata nätverks-namespaces',
            'Ingen routing',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g225',
        question: 'Which command shows binary path for ls?',
        options: [
            'which ls',
            'locate ls',
            'find ls',
            'whereis ls',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g226',
        question: 'What is the difference between apt update and apt upgrade?',
        options: [
            'update hämtar paketlistor',
            'upgrade tar bort paket',
            'Ingen',
            'update kräver reboot',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g227',
        question: 'What does docker ps?',
        options: [
            'Visar images',
            'Visar körande containrar',
            'Visar nätverk',
            'Visar volymer',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g228',
        question: 'Which command sends SIGTERM by default?',
        options: [
            'pkill',
            'kill',
            'end',
            'stop',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g229',
        question: 'What does cut -d: -f1 file?',
        options: [
            'Sorterar filen',
            'Shows first field',
            'Räknar rader',
            'Tar bort kolumn 1',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g230',
        question: 'Which permission controls creation and deletion of files in directory?',
        options: [
            'r',
            'x',
            'w',
            'rwx',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g231',
        question: 'Why should direct root login be avoided?',
        options: [
            'root saknar lösenord',
            'root cannot run commands',
            'root kan inte använda sudo',
            'Harder traceability and higher risk',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g232',
        question: 'Which Docker command runs a command in an already running container?',
        options: [
            'docker exec',
            'docker run',
            'docker start',
            'docker attach',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g233',
        question: 'What does umask 022 mean for new files?',
        options: [
            '755',
            '777',
            '644',
            '600',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g234',
        question: 'Which command shows memory usage?',
        options: [
            'top',
            'free',
            'du',
            'df',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g235',
        question: 'What is a bind mount in Docker?',
        options: [
            'Tillfällig cache',
            'Docker-intern lagring',
            'Krypterad volym',
            'Points to host path',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g236',
        question: 'What is tee used for?',
        options: [
            'Visa och spara output samtidigt',
            'Redirect stderr',
            'Write only to file',
            'Sortera output',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g237',
        question: 'Which command stops a systemd service?',
        options: [
            'service off',
            'systemctl disable',
            'systemctl stop',
            'systemctl kill',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g238',
        question: 'What is the difference between archiving and compression?',
        options: [
            'Sortera vs filtrera',
            'Kryptera vs signera',
            'Samla filer vs minska storlek',
            'Ingen',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g239',
        question: 'Which command shows current directory?',
        options: [
            'ls',
            'pwd',
            'cd',
            'whereis',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g240',
        question: 'Which Docker object is used for network isolation?',
        options: [
            'Image',
            'Container layer',
            'Network',
            'Volume',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g241',
        question: 'What does load average mean?',
        options: [
            'Genomsnitt av körbara/väntande processer',
            'CPU-temperatur',
            'Disk-IO',
            'RAM consumption',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g242',
        question: 'Which command removes a user and their home directory?',
        options: [
            'userdel',
            'userdel -r',
            'rmuser',
            'deluser',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g243',
        question: 'Where do Docker containers run?',
        options: [
            'Hostens kernel',
            'Egen kernel',
            'Hypervisor',
            'BIOS',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg1',
        question: 'Ett kommando skriver både normal output och felmeddelanden. Du vill att inget visas i terminalen men att endast felen sparas i fil.',
        options: [
            'cmd > /dev/null 2> errors.log',
            'cmd &> /dev/null',
            'cmd 2> errors.log',
            'cmd > errors.log',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg2',
        question: 'Efter cmd > out.txt visas fortfarande text i terminalen.',
        options: [
            'Filen saknar write-rättighet',
            'Output skrivs till stderr',
            'Shell tolkar inte redirect',
            'Redirecten sker för sent',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-vg3',
        question: 'Which command visar output på skärmen och skriver samma output till fil?',
        options: [
            'cmd > out.txt | cat',
            'cmd | tee out.txt',
            'cmd 2>&1 > out.txt',
            'cmd >> out.txt',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg4',
        question: 'Which command visar status från senast körda kommando?',
        options: [
            'echo $!',
            'echo $$',
            'echo $0',
            'echo $?',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg5',
        question: 'Why skiljer sig utfallet mellan echo "*.log" och ls*.log?',
        options: [
            'ls använder regex',
            'shell expanderar wildcard före ls',
            'echo filtrerar filer',
            'echo tolkar wildcard',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg6',
        question: 'Du vill visa unika rader och hur många gånger varje förekommer.',
        options: [
            'uniq -c file',
            'uniq file | sort',
            'sort -n file | uniq',
            'sort file | uniq -c',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg7',
        question: 'Why ger uniq file.txt inte alltid förväntat resultat?',
        options: [
            'uniq ignorerar whitespace',
            'filen är inte sorterad',
            'uniq fungerar bara på text',
            'uniq kräver flaggor',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg8',
        question: 'Extrahera kolumn 1 från CSV, sortera numeriskt fallande och visa tre största värdena.',
        options: [
            'cut -d, -f1 data.csv | sort -nr | head -n 3',
            'cut -f1 data.csv | uniq | head -n 3',
            'cut -d, -f1 data.csv | sort | tail -n 3',
            'sort -nr data.csv | cut -f1 | head -n 3',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg9',
        question: 'Why används less för stora filer?',
        options: [
            'Den laddar filen långsammare',
            'Den ändrar inte filens rättigheter',
            'Den läser filen stegvis',
            'Den filtrerar output',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg10',
        question: 'Vad blir effekten av att köra uniq före sort?',
        options: [
            'Inga skillnader',
            'Alla dubbletter tas bort',
            'Kommandot misslyckas',
            'Endast intilliggande dubbletter tas bort',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg11',
        question: 'Du kan lista en katalog men inte gå in i den.',
        options: [
            'Saknar write',
            'Saknar read',
            'Saknar execute',
            'Saknar owner',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg12',
        question: 'Visa alla .conf under /etc utan felutskrifter.',
        options: [
            'find /etc -name "*.conf" 2>/dev/null',
            'find /etc -name "*.conf" &>/dev/null',
            'find /etc -name "*.conf" > /dev/null',
            'find /etc "*.conf"',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg13',
        question: 'Vad krävs för att ta bort en directory med innehåll?',
        options: [
            'sudo alltid',
            'rekursiv borttagning',
            'execute-rätt på filerna',
            'write-rätt på filerna',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg14',
        question: 'Innehållet följer inte med vid kopiering av katalog.',
        options: [
            '-f saknas',
            '-i saknas',
            '-r saknas',
            '-a saknas',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg15',
        question: 'How avgör kommandot file filtyp?',
        options: [
            'Filändelse',
            'Filstorlek',
            'Innehållssignatur',
            'Ägarrättighet',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg16',
        question: 'Ett script är exekverbart men kan inte köras.',
        options: [
            'Scriptet är tomt',
            'Katalog saknar execute',
            'Fel ägare',
            'Saknar read',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg17',
        question: 'What does x på directory?',
        options: [
            'Gå in i katalog',
            'Visa innehåll',
            'Ta bort katalog',
            'Skapa filer',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg18',
        question: 'Vilka permissions gäller om usern tillhör gruppen men inte är owner?',
        options: [
            'other',
            'högsta av alla',
            'user',
            'group',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-vg19',
        question: 'Syftet med umask är att:',
        options: [
            'Ändra befintliga filer',
            'Ändra ägare',
            'Begränsa standardrättigheter',
            'Kryptera filer',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg20',
        question: 'Which directorypermission innebär störst risk?',
        options: [
            'w för other',
            'r för owner',
            'x för group',
            'r för group',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-vg21',
        question: 'Why undviks direkt root-login?',
        options: [
            'root kan inte logga in via ssh',
            'Harder traceability and higher risk',
            'root saknar shell',
            'root saknar PATH',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg22',
        question: 'Skillnad mellan su och sudo:',
        options: [
            'su kräver nätverk',
            'sudo byter permanent användare',
            'su loggar alltid',
            'sudo kan begränsas per kommando',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-vg23',
        question: 'Sudo echo test > file ger permission denied. Varför?',
        options: [
            'redirect sker innan sudo',
            'filen är låst',
            'umask blockerar',
            'sudo fungerar inte med echo',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-vg24',
        question: 'Fel i /etc/sudoers kan leda till:',
        options: [
            'långsam inloggning',
            'korrupt kernel',
            'förlorad admin-åtkomst',
            'stoppad ssh',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-vg25',
        question: 'What does UID 0?',
        options: [
            'Root-behörighet',
            'Ingen inloggning',
            'Systemkonto',
            'Första användaren',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg26',
        question: 'Vad skiljer SIGTERM från SIGKILL?',
        options: [
            'SIGKILL är interaktiv',
            'SIGTERM är långsammare',
            'SIGTERM stoppar kernel',
            'SIGKILL kan inte fångas',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg27',
        question: 'Why bör SIGKILL undvikas?',
        options: [
            'Ingen städning sker',
            'Stoppar nätverk',
            'Fungerar inte alltid',
            'Kräver sudo',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg28',
        question: 'Bakgrundsprocess dör när terminalen stängs.',
        options: [
            'Körs utan sudo',
            'Saknar execute',
            'Får SIGHUP',
            'Saknar PID',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg29',
        question: 'Which verktyg identifierar CPU-belastande process snabbast?',
        options: [
            'top',
            'uptime',
            'kill',
            'ps',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg30',
        question: 'Load average avser:',
        options: [
            'Disk-IO',
            'CPU-temperatur',
            'RAM consumption',
            'Körbara/väntande processer',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg31',
        question: 'Why körs apt update separat från apt upgrade?',
        options: [
            'Upgrade kräver reboot',
            'Upgrade rensar cache',
            'Update installerar',
            'Update hämtar paketlistor',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg32',
        question: 'Installera utan uppdaterade listor riskerar:',
        options: [
            'gamla versioner',
            'långsam installation',
            'trasigt filesystem',
            'låst kernel',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg33',
        question: 'How hittas ls vid körning?',
        options: [
            'alias',
            'Filändelse',
            '$PATH',
            '/etc/hosts',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg34',
        question: 'Tillgängligt diskutrymme skiljer sig p.g.a.:',
        options: [
            'swap',
            'reserverade block',
            'filändelser',
            'umask',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg35',
        question: 'Why används swap trots ledigt RAM?',
        options: [
            'Effektiv minneshantering',
            'Full disk',
            'Felkonfiguration',
            'Låg CPU',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg36',
        question: 'Why används tar tillsammans med gzip?',
        options: [
            'gzip arkiverar',
            'gzip bevarar rättigheter',
            'tar samlar filer',
            'tar krypterar',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg37',
        question: 'Vid extrahering av tar bevaras normalt:',
        options: [
            'endast namn',
            'rättigheter',
            'tidsstämplar aldrig',
            'ägare alltid',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg38',
        question: '.tar.gz innebär:',
        options: [
            'dubbel kompression',
            'kryptering',
            'två arkiv',
            'arkiv + kompression',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg39',
        question: 'När är zip mest lämpligt?',
        options: [
            'Streamad output',
            'Linux-backup',
            'Delning med andra OS',
            'Bevara permissions',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg40',
        question: 'Arkivering jämfört med komprimering:',
        options: [
            'Sortera vs filtrera',
            'Kryptera vs signera',
            'Samla vs minska',
            'Samma sak',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg41',
        question: 'Service startar manuellt men inte vid boot.',
        options: [
            'Saknar reload',
            'Saknar enable',
            'Saknar start',
            'Saknar status',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-vg42',
        question: 'Systemctl enable innebär:',
        options: [
            'Start vid boot',
            'Start nu',
            'Stoppa service',
            'Ta bort service',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-vg43',
        question: 'Första felsökningssteg vid krasch:',
        options: [
            'journalctl + status',
            'reinstall',
            'rm service',
            'reboot',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg44',
        question: 'Why är PID 1 kritisk?',
        options: [
            'Kör nätverk',
            'Kör shell',
            'Hanterar användare',
            'Initierar process-trädet',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg45',
        question: 'Journalctl fördel:',
        options: [
            'Mindre loggar',
            'Kräver GUI',
            'Centraliserad loggning',
            'Snabbare boot',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg46',
        question: 'Why fungerar inte localhost mellan containrar?',
        options: [
            'Ingen routing',
            'Fel DNS',
            'Separata namespaces',
            'Brandvägg',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg47',
        question: 'What does port-mapping?',
        options: [
            'Ändrar IP',
            'Delar nätverk',
            'Exponerar port',
            'Krypterar trafik',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg48',
        question: 'Why är bind mounts känsligare?',
        options: [
            'Krypterade data',
            'Delas inte',
            'Mindre prestanda',
            'Direkt åtkomst till host-path',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg49',
        question: '1. Why är containrar lättare än VM?',
        options: [
            'Mindre disk',
            'Ingen kernel',
            'Mindre RAM',
            'Delad kernel',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg50',
        question: 'What happens to data when container is removed?',
        options: [
            'Krypteras',
            'Allt sparas',
            'Writable layer disappears',
            'Moved to host',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg51',
        question: 'What is the most likely cause?',
        options: [
            'Docker daemon is stopped',
            'Image saknar CMD',
            'Containern körs som root',
            'Port is not published',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg52',
        question: 'Two containers try to communicate via localhost but fail. Why?',
        options: [
            'Each container has own network namespace',
            'DNS saknas',
            'localhost is reserved',
            'Docker blockerar TCP',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg53',
        question: 'You run docker run nginx and the container starts then stops immediately. Why?',
        options: [
            'Ingen CMD körs',
            'Image is corrupt',
            'nginx kräver port mapping',
            'Huvudprocessen avslutas',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg54',
        question: 'What is huvudsyftet med Docker volumes?',
        options: [
            'Isolering av CPU',
            'Säker inloggning',
            'Snabbare nätverk',
            'Persistence outside container lifecycle',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg55',
        question: 'What distinguishes a bind mount from a named volume?',
        options: [
            'Bind mounts points directly to host path',
            'Named volumes delas inte',
            'Named volumes ligger i image',
            'Bind mounts är always read-only',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    }
]

// Export för enkel import i tentasimulator
export const ALL_MANPAGE_TENTA_QUESTIONS = MANPAGE_TENTA_QUESTIONS
