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
            'Appends output to a file',
            'Redirects stderr',
            'Sends output of one command as input to another',
            'Redirects output to a file',
        ],
        correctIndex: 2,
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
            'Append',
            'Redirect stdin',
            'Pipe',
            'Overwrite',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g4',
        question: 'What does 2> redirect?',
        options: [
            'stderr',
            'stdout',
            'all output',
            'stdin',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-g5',
        question: 'Which file descriptor is stdout?',
        options: [
            '0',
            '3',
            '2',
            '1',
        ],
        correctIndex: 3,
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
            'export $VAR',
            '$VAR=value',
            'VAR=value',
            'value=VAR',
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
            'Variable expansion',
            'No expansion',
            'Command blocking',
            'File locking',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g9',
        question: 'What does * represent?',
        options: [
            'Hidden files only',
            'Numbers only',
            'Any number of characters',
            'Single character',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g10',
        question: 'What does export VAR do?',
        options: [
            'Makes variable global',
            'Deletes variable',
            'Prints variable',
            'Locks variable',
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
            'wc',
            'cat',
            'sort',
            'less',
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
            'echo',
            'tr',
            'cat',
            'less',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g13',
        question: 'What does head -n 5 file do?',
        options: [
            'Sorts lines',
            'Deletes 5 lines',
            'Shows first 5 lines',
            'Shows last 5 lines',
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
            'Sorts output',
            'Follows file updates',
            'Deletes file',
            'Compresses file',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g15',
        question: 'What does wc -l show?',
        options: [
            'Characters',
            'Bytes',
            'Words',
            'Lines',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g16',
        question: 'Which command sorts numerically?',
        options: [
            'cut',
            'sort',
            'sort -n',
            'uniq',
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
            'Large',
            'Sorted',
            'Compressed',
            'Binary',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g18',
        question: 'What does cut -d : -f 1 do?',
        options: [
            'Cuts first field using :',
            'Sorts output',
            'Deletes file',
            'Replaces colons',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g19',
        question: 'What does tr a-z A-Z do?',
        options: [
            'Removes spaces',
            'Deletes lowercase',
            'Sorts text',
            'Converts lowercase to uppercase',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g20',
        question: 'Pipes work with:',
        options: [
            'Files only',
            'Users',
            'Commands',
            'Variables',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g21',
        question: 'What does pwd show?',
        options: [
            'Home directory',
            'Previous directory',
            'Root directory',
            'Current directory',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g22',
        question: 'Which flag shows hidden files?',
        options: [
            '-r',
            '-a',
            '-l',
            '-h',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g23',
        question: 'What does cp -r do?',
        options: [
            'Copy directories recursively',
            'Rename files',
            'Remove directories',
            'Copy files only',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g24',
        question: 'What does mv do?',
        options: [
            'Compress files',
            'Delete files',
            'Copy files',
            'Move or rename files',
        ],
        correctIndex: 3,
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
            'Remove read-only files',
            'Restore files',
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
            'Non-empty directories',
            'Files',
            'Empty directories',
            'Any directory',
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
            'Owner',
            'Permissions',
            'File type',
            'Size only',
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
            'Packages',
            'Content',
            'Metadata',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g30',
        question: 'find / -name test.txt does what?',
        options: [
            'Deletes file',
            'Copies file',
            'Searches file system',
            'Compresses file',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g31',
        question: 'What does permission 755 mean?',
        options: [
            'rwx rwx rwx',
            'rw- r-- r--',
            'rwx r-x r-x',
            'r-- r-- r--',
        ],
        correctIndex: 2,
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
            'chmod',
            'chgrp',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g33',
        question: 'Symbolic mode u+x means:',
        options: [
            'Add execute to group',
            'Remove execute',
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
            'Changes permissions',
            'Changes owner and group',
            'Deletes file',
            'Moves file',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g35',
        question: 'chgrp changes:',
        options: [
            'Permissions',
            'Owner',
            'Size',
            'Group',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g36',
        question: 'umask affects:',
        options: [
            'Default permissions',
            'File size',
            'Ownership',
            'Existing files',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g37',
        question: 'Default file permission base is:',
        options: [
            '755',
            '644',
            '666',
            '777',
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
            '666',
            '755',
            '644',
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
            'Root',
            'File owner',
            'Any user',
            'Group',
        ],
        correctIndex: 0,
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
            'Entering directory',
            'Reading files',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g41',
        question: 'Which command creates a user?',
        options: [
            'newuser',
            'useradd',
            'adduser',
            'mkuser',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g42',
        question: 'Remove user and home directory?',
        options: [
            'rmuser',
            'userdel -r',
            'deluser',
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
            'usermod',
            'passwd',
            'chpass',
            'login',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g44',
        question: 'What does id show?',
        options: [
            'UID and groups',
            'Processes',
            'Permissions',
            'Disk usage',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g45',
        question: 'su does what?',
        options: [
            'Super update',
            'Suspend',
            'Shutdown',
            'Switch user',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g46',
        question: 'sudo allows:',
        options: [
            'Create users',
            'Run commands as another user',
            'Change kernel',
            'Login as root permanently',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g47',
        question: 'sudo configuration is in:',
        options: [
            '/etc/sudoers',
            '/etc/group',
            '/etc/passwd',
            '/etc/shadow',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g48',
        question: 'Which user has UID 0?',
        options: [
            'system',
            'admin',
            'root',
            'nobody',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g49',
        question: 'Groups are defined in:',
        options: [
            '/etc/group',
            '/etc/users',
            '/etc/shadow',
            '/etc/passwd',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g50',
        question: 'passwd without arguments changes:',
        options: [
            'group password',
            'all passwords',
            'current user password',
            'root password',
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
            'top',
            'ps',
            'uptime',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g52',
        question: 'ps aux shows:',
        options: [
            'Network processes',
            'Current user only',
            'Only root processes',
            'All processes',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g53',
        question: 'Which command sends a signal?',
        options: [
            'stop',
            'kill',
            'end',
            'exit',
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
            'SIGTERM',
            'SIGSTOP',
            'SIGINT',
            'SIGKILL',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g55',
        question: 'Which signal cannot be caught?',
        options: [
            'SIGINT',
            'SIGKILL',
            'SIGTERM',
            'SIGHUP',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g56',
        question: 'pkill differs by:',
        options: [
            'User',
            'Name',
            'PID',
            'Port',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g57',
        question: 'top shows:',
        options: [
            'Network stats',
            'Disk usage',
            'Users',
            'Processes in real time',
        ],
        correctIndex: 3,
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
            'Boot logs',
            'CPU model',
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
            'Disk IO',
            'Process priority',
            'Network speed',
            'Memory size',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g60',
        question: 'PID stands for:',
        options: [
            'Permission ID',
            'Package ID',
            'Program ID',
            'Process ID',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g61',
        question: 'Which is a package manager?',
        options: [
            'apt',
            'yum',
            'dnf',
            'all of the above',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g62',
        question: 'apt update does what?',
        options: [
            'Installs packages',
            'Upgrades kernel',
            'Updates package lists',
            'Removes packages',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g63',
        question: 'apt upgrade does what?',
        options: [
            'Removes packages',
            'Updates package lists',
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
            'ls binary path',
            'ls size',
            'ls manual',
            'ls permissions',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g65',
        question: 'whereis shows:',
        options: [
            'Binary, source, man',
            'Package version',
            'Only binary',
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
            'Kernel info',
            'Processes',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g67',
        question: 'df -h shows:',
        options: [
            'Disk usage',
            'CPU usage',
            'Network usage',
            'RAM usage',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g68',
        question: 'du -sh shows:',
        options: [
            'Disk free',
            'RAM free',
            'Swap usage',
            'Directory size',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g69',
        question: 'free shows:',
        options: [
            'Disk space',
            'Network ports',
            'CPU cores',
            'RAM usage',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g70',
        question: 'Human readable flag is:',
        options: [
            '-l',
            '-r',
            '-a',
            '-h',
        ],
        correctIndex: 3,
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
            'tar -x',
            'tar -c',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g72',
        question: 'Which extracts a tar archive?',
        options: [
            '-f',
            '-x',
            '-v',
            '-c',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g73',
        question: '-f in tar means:',
        options: [
            'file',
            'fast',
            'follow',
            'force',
        ],
        correctIndex: 0,
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
            'Delete file',
            'Archive',
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
            'Encrypt',
            'Archive',
            'Compress',
            'Decompress',
        ],
        correctIndex: 3,
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
            'Extract zip',
            'Compress',
            'Delete',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g79',
        question: 'tar archives preserve:',
        options: [
            'Permissions',
            'Users only',
            'Nothing',
            'File order only',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g80',
        question: 'Which is NOT compression?',
        options: [
            'gunzip',
            'tar',
            'zip',
            'gzip',
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
            'journalctl',
            'systemctl',
            'init',
            'service',
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
            'systemctl run',
            'systemctl start',
            'systemctl enable',
            'systemctl boot',
        ],
        correctIndex: 1,
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
            'systemctl check',
            'systemctl status',
            'systemctl show',
            'systemctl info',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g85',
        question: 'journalctl shows:',
        options: [
            'Processes',
            'Logs',
            'Kernel config',
            'Users',
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
            'Disk logs',
            'Errors',
            'Old logs',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g87',
        question: 'systemd is:',
        options: [
            'Filesystem',
            'Package manager',
            'Shell',
            'Init system',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g88',
        question: 'systemd replaces:',
        options: [
            'cron',
            'apt',
            'sysvinit',
            'bash',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g89',
        question: 'Units are defined in:',
        options: [
            '.service',
            '.unit',
            '.conf',
            '.sys',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g90',
        question: 'systemctl stop does what?',
        options: [
            'Disable service',
            'Remove service',
            'Stop service',
            'Restart system',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g91',
        question: 'ping checks:',
        options: [
            'Speed',
            'Ports',
            'DNS',
            'Reachability',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g92',
        question: 'ip a shows:',
        options: [
            'Users',
            'Interfaces',
            'Routes',
            'Ports',
        ],
        correctIndex: 1,
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
            'Compress data',
            'Upload files',
            'Fetch URLs',
            'Edit files',
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
            'DNS lookup',
            'Download files',
            'Port scan',
            'API testing',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g96',
        question: 'A container is:',
        options: [
            'Filesystem',
            'Isolated process',
            'Virtual machine',
            'Kernel',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g97',
        question: 'Container localhost refers to:',
        options: [
            'Host',
            'Container itself',
            'Router',
            'Network',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g98',
        question: 'Host can access container via:',
        options: [
            'SSH only',
            'Port mapping',
            'localhost only',
            'DNS only',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g99',
        question: 'Docker volumes are used for:',
        options: [
            'Networking',
            'Security',
            'Logging',
            'Persistence',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g100',
        question: 'Bind mounts differ by:',
        options: [
            'Size',
            'Speed',
            'Encryption',
            'Host path usage',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g101',
        question: 'What does [ -f file ] test?',
        options: [
            'Executable',
            'Directory',
            'Empty file',
            'Regular file',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g102',
        question: 'What command is [ an alias for?',
        options: [
            'expr',
            'case',
            'test',
            'if',
        ],
        correctIndex: 2,
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
            'Sorts arguments',
            'Removes first positional parameter',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g104',
        question: '$1 refers to:',
        options: [
            'Exit code',
            'First argument',
            'Last argument',
            'Script name',
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
            'Exit code',
            'First argument',
            'Script name',
            'PID',
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
            'echo',
            'scan',
            'read',
            'input',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g107',
        question: 'What does echo $VAR do?',
        options: [
            'Sets variable',
            'Exports variable',
            'Prints variable value',
            'Deletes variable',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g108',
        question: 'What does env show?',
        options: [
            'Environment variables',
            'Files',
            'Users',
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
            'SHELL',
            'USER',
            'PATH',
            'HOME',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g110',
        question: 'Exit code 0 means:',
        options: [
            'Success',
            'Error',
            'Warning',
            'Interrupt',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g111',
        question: 'locate is fast because it:',
        options: [
            'Uses database',
            'Scans disk live',
            'Uses network',
            'Uses cache only',
        ],
        correctIndex: 0,
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
            'which',
            'whereis',
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
            'Prints logs',
            'Compresses logs',
            'Finds log files',
            'Deletes logs',
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
            'Package',
            'Binary path',
            'Alias',
            'Man page',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g117',
        question: 'whereis ls outputs:',
        options: [
            'Permissions',
            'PID',
            'Only binary',
            'Binary, man, source',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g118',
        question: 'find can search by:',
        options: [
            'Size',
            'Type',
            'Name',
            'All above',
        ],
        correctIndex: 3,
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
            'cron',
            'updatedb',
            'locate',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g121',
        question: 'ls -l shows:',
        options: [
            'Hidden files',
            'Inodes',
            'Sizes only',
            'Long listing',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g122',
        question: 'ls -h affects:',
        options: [
            'Size format',
            'Sorting',
            'Permissions',
            'Ownership',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g123',
        question: 'File permissions are shown by:',
        options: [
            'ls -r',
            'ls -a',
            'ls -t',
            'ls -l',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g124',
        question: 'file script.sh returns:',
        options: [
            'Permissions',
            'Content',
            'File type',
            'Owner',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g125',
        question: 'Which shows last modification time?',
        options: [
            'ls',
            'stat',
            'file',
            'pwd',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g126',
        question: 'Which is NOT shown by stat?',
        options: [
            'Size',
            'Owner',
            'Permissions',
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
            'Executables only',
            'Backup files',
            'Directories only',
            'Hidden files',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g128',
        question: 'Hidden files start with:',
        options: [
            '.',
            '_',
            '#',
            '~',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g129',
        question: 'ls without flags sorts by:',
        options: [
            'Extension',
            'Time',
            'Size',
            'Name',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g130',
        question: 'Read permission on file allows:',
        options: [
            'Modify',
            'Delete',
            'Execute',
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
            'Enter directory',
            'Create/delete files',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g132',
        question: 'Execute permission on file allows:',
        options: [
            'Delete',
            'Read',
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
            'rwx r-x r-x',
            'rw- r-- r--',
            'rw- rw- rw-',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g134',
        question: 'Who is checked first for permissions?',
        options: [
            'Group',
            'Root',
            'User',
            'Other',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g135',
        question: 'Group permissions apply when:',
        options: [
            'User is in group',
            'Never',
            'User is owner',
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
            'Owner only',
            'Everyone',
            'Others only',
            'Group only',
        ],
        correctIndex: 0,
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
            'w',
            'rwx',
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
            'x',
            'w',
            'rw',
            'r',
        ],
        correctIndex: 0,
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
            '644',
            '777',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g140',
        question: 'Background process uses:',
        options: [
            '!',
            '*',
            '&',
            '%',
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
            'SIGTERM',
            'SIGSTOP',
            'SIGINT',
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
            'jobs',
            'fg',
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
            'bg',
            'jobs',
            'ps',
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
            'Processes',
            'System jobs',
            'Background jobs',
            'Cron jobs',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g146',
        question: 'Which shows CPU usage?',
        options: [
            'top',
            'df',
            'free',
            'du',
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
            'stop',
            'kill',
            'end',
            'pkill',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g148',
        question: 'Load average relates to:',
        options: [
            'Disk',
            'Memory',
            'CPU',
            'Network',
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
            'Directory size',
            'Disk free space',
            'RAM',
            'CPU',
        ],
        correctIndex: 1,
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
            'Inodes',
            'All files',
            'Per file',
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
            'Disk',
            'CPU',
            'Memory',
            'Network',
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
            'Extra RAM on disk',
            'Disk backup',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g154',
        question: 'Which unit is used by free -h?',
        options: [
            'Human readable',
            'Blocks',
            'Bytes',
            'Pages',
        ],
        correctIndex: 0,
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
            'free',
            'du',
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
            '/root',
            '/home',
            '/',
            '/boot',
        ],
        correctIndex: 2,
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
            'File size',
            'RAM',
            'File creation',
            'CPU',
        ],
        correctIndex: 2,
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
            'Two formats',
            'tar + gzip',
            'zip',
            'encryption',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g161',
        question: 'tar -cvf a.tar dir does:',
        options: [
            'Create archive',
            'Encrypt',
            'Extract',
            'Compress only',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g162',
        question: 'tar -xvf a.tar does:',
        options: [
            'Compress',
            'List',
            'Create',
            'Extract',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g163',
        question: '-v in tar means:',
        options: [
            'Verbose',
            'Version',
            'Virtual',
            'Verify',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g164',
        question: 'Which supports directories easily?',
        options: [
            'zip',
            'gunzip',
            'tar',
            'gzip',
        ],
        correctIndex: 2,
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
            'tar',
            'gzip',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g166',
        question: 'Compression reduces:',
        options: [
            'Ownership',
            'File size',
            'Permissions',
            'Security',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g167',
        question: 'systemctl enable means:',
        options: [
            'Start at boot',
            'Start now',
            'Restart',
            'Reload',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g168',
        question: 'systemctl start means:',
        options: [
            'Enable',
            'Stop',
            'Start immediately',
            'Reload',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g169',
        question: 'systemctl disable means:',
        options: [
            'Remove service',
            'Prevent boot start',
            'Kill process',
            'Stop now',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g170',
        question: 'journalctl without args shows:',
        options: [
            'Kernel logs only',
            'All logs',
            'Errors only',
            'Service logs only',
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
            'Errors',
            'All boots',
            'Current boot',
            'Last boot',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g172',
        question: 'journalctl -u ssh shows:',
        options: [
            'Kernel logs',
            'Network logs',
            'SSH logs',
            'Disk logs',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g173',
        question: 'systemd unit types include:',
        options: [
            'service',
            'all above',
            'mount',
            'target',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g174',
        question: 'systemd runs as PID:',
        options: [
            '1',
            '0',
            '100',
            '2',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-g175',
        question: 'If PID 1 dies:',
        options: [
            'Nothing',
            'Restart service',
            'Restart shell',
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
            'upstart',
            'sysvinit',
            'bash',
            'cron',
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
            'Process',
            'Host',
            'User',
            'File',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g178',
        question: 'IPv4 uses how many bits?',
        options: [
            '24',
            '32',
            '64',
            '16',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g179',
        question: 'ping uses protocol:',
        options: [
            'HTTP',
            'UDP',
            'TCP',
            'ICMP',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g180',
        question: 'ss shows:',
        options: [
            'Sockets',
            'Routes',
            'Interfaces',
            'DNS',
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
            'Routing table',
            'Interfaces',
            'DNS',
        ],
        correctIndex: 1,
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
            '0.0.0.0',
            '192.168.0.1',
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
            'Port to process',
            'IP to MAC',
            'User to host',
            'Name to IP',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'manpage-g184',
        question: '/etc/hosts is used for:',
        options: [
            'Local name resolution',
            'Firewall',
            'Routing',
            'DNS server',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g185',
        question: 'curl is often used for:',
        options: [
            'Email',
            'SSH',
            'API testing',
            'Browsing',
        ],
        correctIndex: 2,
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
            'Ephemeral',
            'Persistent by default',
            'Encrypted',
            'Shared',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g188',
        question: 'Docker volume is used to:',
        options: [
            'Network',
            'Persist data',
            'Speed up CPU',
            'Secure container',
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
            'Volume driver',
            'Docker storage',
            'Image layer',
            'Host path',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-g190',
        question: 'Container localhost refers to:',
        options: [
            'Container',
            'Host',
            'Network',
            'Router',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g191',
        question: 'Host can reach container via:',
        options: [
            'Container ID',
            'DNS only',
            'localhost always',
            'Exposed port',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g192',
        question: 'Container stops when:',
        options: [
            'Network disconnects',
            'User logs out',
            'Main process exits',
            'Shell exits',
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
            'BIOS',
            'Namespaces & cgroups',
            'Hypervisor',
            'Firmware',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g194',
        question: 'What is Docker primarily?',
        options: [
            'Pakethanterare',
            'Init-system',
            'Virtuell maskin',
            'Containerplattform',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g195',
        question: 'A container is best described as:',
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
            'docker inspect',
            'docker ps',
            'docker list',
            'docker images',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g197',
        question: 'What shows docker images?',
        options: [
            'Nätverk',
            'Nedladdade images',
            'Volymer',
            'Körande containrar',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g198',
        question: 'What is en Docker image?',
        options: [
            'Ett nätverk',
            'A template for containers',
            'En volym',
            'En körande container',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g199',
        question: 'Which command starts a container?',
        options: [
            'docker exec',
            'docker build',
            'docker run',
            'docker pull',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g200',
        question: 'What happens om huvudprocessen i en container avslutas?',
        options: [
            'Containern startas om automatiskt',
            'Containern stoppas',
            'Containern fortsätter',
            'Containern pausar',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g201',
        question: 'What is flaggan -d till vid docker run?',
        options: [
            'Delete on exit',
            'Download image',
            'Debug',
            'Detached mode',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g202',
        question: 'What does docker pull?',
        options: [
            'Startar container',
            'Tar bort image',
            'Hämtar image',
            'Bygger image',
        ],
        correctIndex: 2,
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
            'I egen kernel',
            'På hostens kernel',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g204',
        question: 'Which command lists all running processes for all users?',
        options: [
            'ps aux',
            'jobs',
            'ps',
            'top',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-g205',
        question: 'What does permission chmod 640 file mean?',
        options: [
            'r-- r-- ---',
            'rw- rw- ---',
            'rwx r-- ---',
            'rw- r-- ---',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g206',
        question: 'You run cmd > out.txt but still see text in terminal. Why?',
        options: [
            'Redirect is incorrect',
            'File is empty',
            'Output goes to stderr',
            'cmd kräver sudo',
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
            'ls -lh',
            'du',
            'free',
            'df',
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
            'Ett Docker-volume',
            'Ett Docker-nätverk',
            'En körande container',
            'A template for containers',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g209',
        question: 'Why does uniq file.txt not always work as expected?',
        options: [
            'uniq ignorerar whitespace',
            'uniq kräver flaggor',
            'File is not sorted',
            'File is too large',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g210',
        question: 'Which command starts a container in background?',
        options: [
            'docker exec -d',
            'docker run -d',
            'docker pull -d',
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
            'Dolda filer',
            'Endast kataloger',
            'Filstorlek',
            'Filtyp',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g212',
        question: 'Which signal cannot be caught by a program?',
        options: [
            'SIGHUP',
            'SIGKILL',
            'SIGTERM',
            'SIGINT',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-g213',
        question: 'What is the purpose of environment variable $PATH?',
        options: [
            'Lagra miljövariabler',
            'Styra rättigheter',
            'Ange hemkatalog',
            'Set command paths',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Bash Scripting'
    },
    {
        id: 'manpage-g214',
        question: 'Which command pulls a Docker image from registry?',
        options: [
            'docker build',
            'docker exec',
            'docker pull',
            'docker run',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g215',
        question: 'What does execute permission on directory mean?',
        options: [
            'Skapa filer',
            'Gå in i katalogen',
            'Visa innehåll',
            'Ta bort katalogen',
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
            'free',
            'ps',
            'df',
            'uptime',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g217',
        question: 'What happens when main process in container exits?',
        options: [
            'Containern fortsätter',
            'Containern startas om automatiskt',
            'Containern pausar',
            'Containern stoppas',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g218',
        question: 'Which command extracts a tar archive?',
        options: [
            'tar -f',
            'tar -c',
            'tar -x',
            'tar -z',
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
            'x',
            'w',
            'ägare',
            'r',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g220',
        question: 'Which command shows which ports are listening on the system?',
        options: [
            'ss',
            'ip a',
            'curl',
            'ping',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g221',
        question: 'What are Docker volumes primarily used for?',
        options: [
            'Persistens',
            'Nätverk',
            'Security',
            'CPU-begränsning',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g222',
        question: 'Which command changes owner on a file?',
        options: [
            'umask',
            'chown',
            'chmod',
            'chgrp',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g223',
        question: 'What does journalctl?',
        options: [
            'Skapar användare',
            'Hanterar nätverk',
            'Visar loggar',
            'Startar tjänster',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g224',
        question: 'Why can two containers not reach each other via localhost?',
        options: [
            'Separata nätverks-namespaces',
            'Brandvägg',
            'Fel DNS',
            'Ingen routing',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g225',
        question: 'Which command shows binary path for ls?',
        options: [
            'locate ls',
            'whereis ls',
            'which ls',
            'find ls',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g226',
        question: 'What is the difference between apt update and apt upgrade?',
        options: [
            'Ingen',
            'update hämtar paketlistor',
            'upgrade tar bort paket',
            'update kräver reboot',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g227',
        question: 'What does docker ps?',
        options: [
            'Visar nätverk',
            'Visar images',
            'Visar volymer',
            'Visar körande containrar',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g228',
        question: 'Which command sends SIGTERM by default?',
        options: [
            'stop',
            'end',
            'kill',
            'pkill',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-g229',
        question: 'What does cut -d: -f1 file?',
        options: [
            'Shows first field',
            'Tar bort kolumn 1',
            'Sorterar filen',
            'Räknar rader',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g230',
        question: 'Which permission controls creation and deletion of files in directory?',
        options: [
            'w',
            'x',
            'rwx',
            'r',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-g231',
        question: 'Why should direct root login be avoided?',
        options: [
            'root cannot run commands',
            'root kan inte använda sudo',
            'root saknar lösenord',
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
            'docker run',
            'docker attach',
            'docker start',
            'docker exec',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g233',
        question: 'What does umask 022 mean for new files?',
        options: [
            '600',
            '755',
            '777',
            '644',
        ],
        correctIndex: 3,
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
            'df',
            'du',
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
            'Docker-intern lagring',
            'Tillfällig cache',
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
            'Write only to file',
            'Sortera output',
            'Redirect stderr',
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
            'systemctl kill',
            'service off',
            'systemctl stop',
            'systemctl disable',
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
            'Samla filer vs minska storlek',
            'Kryptera vs signera',
            'Ingen',
            'Sortera vs filtrera',
        ],
        correctIndex: 0,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-g239',
        question: 'Which command shows current directory?',
        options: [
            'ls',
            'whereis',
            'cd',
            'pwd',
        ],
        correctIndex: 3,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-g240',
        question: 'Which Docker object is used for network isolation?',
        options: [
            'Container layer',
            'Network',
            'Image',
            'Volume',
        ],
        correctIndex: 1,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-g241',
        question: 'What does load average mean?',
        options: [
            'Genomsnitt av körbara/väntande processer',
            'RAM consumption',
            'Disk-IO',
            'CPU-temperatur',
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
            'rmuser',
            'userdel -r',
            'userdel',
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
            'Hypervisor',
            'Egen kernel',
            'Hostens kernel',
            'BIOS',
        ],
        correctIndex: 2,
        explanation: 'Korrekt svar baserat på Linux/Unix kommandoreferens och best practices.',
        difficulty: 'G',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg1',
        question: 'A command writes both normal output and error messages. You want nothing displayed in terminal but only errors saved to file.',
        options: [
            'cmd > /dev/null 2> errors.log',
            'cmd 2> errors.log',
            'cmd &> /dev/null',
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
            'Redirecten sker för sent',
            'Filen saknar write-rättighet',
            'Shell tolkar inte redirect',
            'Output skrivs till stderr',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Pipes & Redirection'
    },
    {
        id: 'manpage-vg3',
        question: 'Which command displays output on screen and writes same output to file?',
        options: [
            'cmd >> out.txt',
            'cmd | tee out.txt',
            'cmd > out.txt | cat',
            'cmd 2>&1 > out.txt',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg4',
        question: 'Which command shows status from last executed command?',
        options: [
            'echo $0',
            'echo $$',
            'echo $?',
            'echo $!',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg5',
        question: 'Why skiljer sig utfallet mellan echo "*.log" och ls*.log?',
        options: [
            'echo filtrerar filer',
            'echo tolkar wildcard',
            'ls använder regex',
            'shell expanderar wildcard före ls',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg6',
        question: 'You want to display unique lines and how many times each occurs.',
        options: [
            'uniq file | sort',
            'sort -n file | uniq',
            'sort file | uniq -c',
            'uniq -c file',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg7',
        question: 'Why does uniq file.txt not always give expected result?',
        options: [
            'filen är inte sorterad',
            'uniq kräver flaggor',
            'uniq ignorerar whitespace',
            'uniq fungerar bara på text',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg8',
        question: 'Extract column 1 from CSV, sort numerically descending and show three greatest values.',
        options: [
            'cut -d, -f1 data.csv | sort | tail -n 3',
            'cut -d, -f1 data.csv | sort -nr | head -n 3',
            'cut -f1 data.csv | uniq | head -n 3',
            'sort -nr data.csv | cut -f1 | head -n 3',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg9',
        question: 'Why is less used for large files?',
        options: [
            'Den läser filen stegvis',
            'Den ändrar inte filens rättigheter',
            'Den laddar filen långsammare',
            'Den filtrerar output',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg10',
        question: 'What is the effect of running uniq before sort?',
        options: [
            'Alla dubbletter tas bort',
            'Endast intilliggande dubbletter tas bort',
            'Kommandot misslyckas',
            'Inga skillnader',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg11',
        question: 'You can list a directory but not enter it.',
        options: [
            'Missing read permission',
            'Saknar owner',
            'Saknar execute',
            'Saknar write',
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
            'find /etc "*.conf"',
            'find /etc -name "*.conf" > /dev/null',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg13',
        question: 'What is required to remove a directory with contents?',
        options: [
            'rekursiv borttagning',
            'execute-rätt på filerna',
            'sudo alltid',
            'write-rätt på filerna',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg14',
        question: 'Contents not included when copying directory.',
        options: [
            '-a saknas',
            '-r saknas',
            '-f saknas',
            '-i saknas',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg15',
        question: 'How does the file command determine file type?',
        options: [
            'Innehållssignatur',
            'Filstorlek',
            'Filändelse',
            'Ägarrättighet',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg16',
        question: 'A script is executable but cannot be run.',
        options: [
            'Script is empty',
            'Wrong owner',
            'Missing read permission',
            'Directory missing execute',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg17',
        question: 'What does x on directory do?',
        options: [
            'Visa innehåll',
            'Skapa filer',
            'Ta bort katalog',
            'Gå in i katalog',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg18',
        question: 'Which permissions apply if user belongs to group but is not owner?',
        options: [
            'group',
            'user',
            'other',
            'högsta av alla',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-vg19',
        question: 'The purpose of umask is to:',
        options: [
            'Begränsa standardrättigheter',
            'Ändra ägare',
            'Ändra befintliga filer',
            'Kryptera filer',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg20',
        question: 'Which directory permission poses the greatest risk?',
        options: [
            'w för other',
            'x för group',
            'r för owner',
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
            'root saknar shell',
            'Harder traceability and higher risk',
            'root saknar PATH',
        ],
        correctIndex: 2,
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
        question: 'Sudo echo test > file gives permission denied. Why?',
        options: [
            'umask blockerar',
            'redirect sker innan sudo',
            'filen är låst',
            'sudo fungerar inte med echo',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Permissions & Rättigheter'
    },
    {
        id: 'manpage-vg24',
        question: 'Fel i /etc/sudoers kan leda till:',
        options: [
            'långsam inloggning',
            'förlorad admin-åtkomst',
            'stoppad ssh',
            'korrupt kernel',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Användarhantering'
    },
    {
        id: 'manpage-vg25',
        question: 'What does UID 0?',
        options: [
            'Systemkonto',
            'Första användaren',
            'Root-behörighet',
            'Ingen inloggning',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg26',
        question: 'What distinguishes SIGTERM from SIGKILL?',
        options: [
            'SIGKILL är interaktiv',
            'SIGTERM stoppar kernel',
            'SIGKILL cannot be caught',
            'SIGTERM är långsammare',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg27',
        question: 'Why should SIGKILL be avoided?',
        options: [
            'Kräver sudo',
            'Stoppar nätverk',
            'Fungerar inte alltid',
            'Ingen städning sker',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg28',
        question: 'Background process dies when terminal closes.',
        options: [
            'Saknar PID',
            'Körs utan sudo',
            'Får SIGHUP',
            'Saknar execute',
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
            'kill',
            'uptime',
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
            'Körbara/väntande processer',
            'CPU-temperatur',
            'Disk-IO',
            'RAM consumption',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg31',
        question: 'Why is apt update run separately from apt upgrade?',
        options: [
            'Update hämtar paketlistor',
            'Upgrade rensar cache',
            'Update installerar',
            'Upgrade kräver reboot',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg32',
        question: 'Installera utan uppdaterade listor riskerar:',
        options: [
            'gamla versioner',
            'låst kernel',
            'trasigt filesystem',
            'långsam installation',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg33',
        question: 'How is ls found when executed?',
        options: [
            '/etc/hosts',
            '$PATH',
            'alias',
            'Filändelse',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg34',
        question: 'Available disk space differs due to:',
        options: [
            'reserverade block',
            'swap',
            'umask',
            'filändelser',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg35',
        question: 'Why is swap used despite available RAM?',
        options: [
            'Full disk',
            'Felkonfiguration',
            'Låg CPU',
            'Effektiv minneshantering',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg36',
        question: 'Why is tar used together with gzip?',
        options: [
            'tar samlar filer',
            'tar krypterar',
            'gzip bevarar rättigheter',
            'gzip arkiverar',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg37',
        question: 'Vid extrahering av tar bevaras normalt:',
        options: [
            'rättigheter',
            'endast namn',
            'ägare alltid',
            'tidsstämplar aldrig',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg38',
        question: '.tar.gz means:',
        options: [
            'kryptering',
            'arkiv + kompression',
            'dubbel kompression',
            'två arkiv',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg39',
        question: 'When is zip most appropriate?',
        options: [
            'Linux-backup',
            'Bevara permissions',
            'Delning med andra OS',
            'Streamad output',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg40',
        question: 'Archiving compared to compression:',
        options: [
            'Samma sak',
            'Samla vs minska',
            'Kryptera vs signera',
            'Sortera vs filtrera',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg41',
        question: 'Service startar manuellt men inte vid boot.',
        options: [
            'Saknar start',
            'Saknar reload',
            'Saknar status',
            'Saknar enable',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-vg42',
        question: 'Systemctl enable means:',
        options: [
            'Start vid boot',
            'Stoppa service',
            'Start nu',
            'Ta bort service',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Systemd & Services'
    },
    {
        id: 'manpage-vg43',
        question: 'First troubleshooting step on crash:',
        options: [
            'journalctl + status',
            'rm service',
            'reinstall',
            'reboot',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Filer & Kataloger'
    },
    {
        id: 'manpage-vg44',
        question: 'Why is PID 1 critical?',
        options: [
            'Initierar process-trädet',
            'Hanterar användare',
            'Kör shell',
            'Kör nätverk',
        ],
        correctIndex: 0,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Processer & Signaler'
    },
    {
        id: 'manpage-vg45',
        question: 'Journalctl advantage:',
        options: [
            'Snabbare boot',
            'Mindre loggar',
            'Kräver GUI',
            'Centraliserad loggning',
        ],
        correctIndex: 3,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg46',
        question: 'Why fungerar inte localhost mellan containrar?',
        options: [
            'Fel DNS',
            'Separata namespaces',
            'Brandvägg',
            'Ingen routing',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg47',
        question: 'What does port-mapping?',
        options: [
            'Krypterar trafik',
            'Ändrar IP',
            'Exponerar port',
            'Delar nätverk',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Nätverk'
    },
    {
        id: 'manpage-vg48',
        question: 'Why are bind mounts more sensitive?',
        options: [
            'Delas inte',
            'Krypterade data',
            'Direkt åtkomst till host-path',
            'Mindre prestanda',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Disk & Storage'
    },
    {
        id: 'manpage-vg49',
        question: 'Why are containers lighter than VMs?',
        options: [
            'Ingen kernel',
            'Mindre disk',
            'Delad kernel',
            'Mindre RAM',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering'
    },
    {
        id: 'manpage-vg50',
        question: 'What happens to data when container is removed?',
        options: [
            'Allt sparas',
            'Moved to host',
            'Writable layer disappears',
            'Krypteras',
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
            'Port is not published',
            'Containern körs som root',
            'Image saknar CMD',
        ],
        correctIndex: 1,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Linux Grundläggande'
    },
    {
        id: 'manpage-vg52',
        question: 'Two containers try to communicate via localhost but fail. Why?',
        options: [
            'DNS saknas',
            'localhost is reserved',
            'Each container has own network namespace',
            'Docker blockerar TCP',
        ],
        correctIndex: 2,
        explanation: 'VG-nivå: Djupare förståelse av Linux-koncept och avancerade kommandon.',
        difficulty: 'VG',
        category: 'Docker & Containers'
    },
    {
        id: 'manpage-vg53',
        question: 'You run docker run nginx and the container starts then stops immediately. Why?',
        options: [
            'Image is corrupt',
            'Ingen CMD körs',
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
            'Snabbare nätverk',
            'Persistence outside container lifecycle',
            'Säker inloggning',
            'Isolering av CPU',
        ],
        correctIndex: 1,
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
