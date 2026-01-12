import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

export const FILSYSTEM_V2_QUESTIONS: OmtentaV2Question[] = [
  {
    id: 'omtenta-v2-fs-1',
    question: 'The command to list files is...',
    options: ['dir', 'show', 'ls', 'list'],
    correctIndices: [2],
    explanation: 'ls (list) is the standard Linux command for listing files and directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-2',
    question: 'The command to change directory is...',
    options: ['chdir', 'cd', 'go', 'move'],
    correctIndices: [1],
    explanation: 'cd (change directory) is used to navigate between directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-3',
    question: 'The command to print working directory is...',
    options: ['cwd', 'dir', 'pwd', 'where'],
    correctIndices: [2],
    explanation: 'pwd (print working directory) displays the current directory path.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-4',
    question: 'The command to create a directory is...',
    options: ['md', 'newdir', 'mkdir', 'create'],
    correctIndices: [2],
    explanation: 'mkdir (make directory) creates new directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-5',
    question: 'The command to remove a directory is...',
    options: ['rd', 'deldir', 'rmdir', 'remove'],
    correctIndices: [2],
    explanation: 'rmdir (remove directory) removes empty directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-6',
    question: 'The command to remove a file is...',
    options: ['del', 'delete', 'rm', 'erase'],
    correctIndices: [2],
    explanation: 'rm (remove) deletes files and directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-7',
    question: 'The command to copy a file is...',
    options: ['copy', 'cp', 'cpy', 'duplicate'],
    correctIndices: [1],
    explanation: 'cp (copy) is used to copy files and directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-8',
    question: 'The command to move a file is...',
    options: ['move', 'mv', 'transfer', 'relocate'],
    correctIndices: [1],
    explanation: 'mv (move) moves or renames files and directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-9',
    question: 'The command to create an empty file is...',
    options: ['create', 'new', 'touch', 'make'],
    correctIndices: [2],
    explanation: 'touch creates empty files or updates timestamps on existing files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-10',
    question: 'The symbol ~ means...',
    options: ['Root directory', 'Current directory', 'Home directory', 'Parent directory'],
    correctIndices: [2],
    explanation: 'The tilde (~) represents the current user\'s home directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-11',
    question: 'The symbol . means...',
    options: ['Home directory', 'Current directory', 'Root directory', 'Parent directory'],
    correctIndices: [1],
    explanation: 'A single dot (.) represents the current directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-12',
    question: 'The symbol .. means...',
    options: ['Home directory', 'Current directory', 'Root directory', 'Parent directory'],
    correctIndices: [3],
    explanation: 'Double dots (..) represent the parent directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-13',
    question: 'The symbol / at the start means...',
    options: ['Home directory', 'Current directory', 'Root directory', 'Parent directory'],
    correctIndices: [2],
    explanation: 'A forward slash (/) at the start represents the root directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-14',
    question: 'An absolute path starts with...',
    options: ['~', '.', '/', '..'],
    correctIndices: [2],
    explanation: 'An absolute path always starts with / (the root directory).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-15',
    question: 'A relative path starts from...',
    options: ['Root directory', 'Home directory', 'Current directory', 'Parent directory'],
    correctIndices: [2],
    explanation: 'A relative path is relative to the current working directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-16',
    question: 'The ls flag -l shows...',
    options: ['Hidden files', 'Long format with details', 'List directories only', 'Recursive listing'],
    correctIndices: [1],
    explanation: 'The -l flag shows detailed (long) information about files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-17',
    question: 'The ls flag -a shows...',
    options: ['Long format', 'Hidden files', 'All details', 'Alphabetical order'],
    correctIndices: [1],
    explanation: 'The -a flag shows all files, including hidden files (starting with .).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-18',
    question: 'The ls flag -h shows...',
    options: ['Help', 'Hidden files', 'Human readable sizes', 'Horizontal layout'],
    correctIndices: [2],
    explanation: 'The -h flag shows file sizes in human-readable format (KB, MB, GB).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-19',
    question: 'Hidden files in Linux start with...',
    options: ['_', '-', '.', '~'],
    correctIndices: [2],
    explanation: 'Hidden files in Linux begin with a dot (.) character.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-20',
    question: 'The command to show file content is...',
    options: ['show', 'read', 'cat', 'print'],
    correctIndices: [2],
    explanation: 'cat (concatenate) displays file contents to the terminal.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-21',
    question: 'The command to view file page by page is...',
    options: ['page', 'view', 'less', 'show'],
    correctIndices: [2],
    explanation: 'less allows you to view files one page at a time with navigation.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-22',
    question: 'In less, to quit press...',
    options: ['x', 'e', 'q', 'c'],
    correctIndices: [2],
    explanation: 'Press q to quit the less pager.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-23',
    question: 'In less, to search press...',
    options: ['s', 'f', '/', '?'],
    correctIndices: [2],
    explanation: 'Press / followed by your search term to search forward in less.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-24',
    question: 'The command to show first lines of a file is...',
    options: ['first', 'start', 'head', 'top'],
    correctIndices: [2],
    explanation: 'head displays the first lines of a file (default 10 lines).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-25',
    question: 'The command to show last lines of a file is...',
    options: ['last', 'end', 'tail', 'bottom'],
    correctIndices: [2],
    explanation: 'tail displays the last lines of a file (default 10 lines).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-26',
    question: 'The flag to follow a file in real-time is...',
    options: ['-r', '-l', '-f', '-t'],
    correctIndices: [2],
    explanation: 'tail -f follows a file and shows new content as it\'s added.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-27',
    question: 'The command to count lines in a file is...',
    options: ['count', 'lines', 'wc -l', 'num'],
    correctIndices: [2],
    explanation: 'wc -l (word count with -l flag) counts the number of lines.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-28',
    question: 'The command to search text in files is...',
    options: ['find', 'search', 'grep', 'look'],
    correctIndices: [2],
    explanation: 'grep searches for text patterns within files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-29',
    question: 'The command to find files by name is...',
    options: ['grep', 'search', 'find', 'locate'],
    correctIndices: [2],
    explanation: 'find searches for files based on various criteria including name.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-30',
    question: 'The /etc directory contains...',
    options: ['User files', 'Configuration files', 'Temporary files', 'Log files'],
    correctIndices: [1],
    explanation: '/etc contains system-wide configuration files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-31',
    question: 'The /home directory contains...',
    options: ['System files', 'User home directories', 'Configuration files', 'Log files'],
    correctIndices: [1],
    explanation: '/home contains the home directories of regular users.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-32',
    question: 'The /var directory contains...',
    options: ['User files', 'Configuration files', 'Variable data like logs', 'System binaries'],
    correctIndices: [2],
    explanation: '/var contains variable data including logs, mail, and spool files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-33',
    question: 'The /tmp directory contains...',
    options: ['User files', 'Configuration files', 'Temporary files', 'Log files'],
    correctIndices: [2],
    explanation: '/tmp is for temporary files that may be deleted on reboot.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-34',
    question: 'The /bin directory contains...',
    options: ['User files', 'Essential binaries', 'Configuration files', 'Log files'],
    correctIndices: [1],
    explanation: '/bin contains essential command binaries needed for single-user mode.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-35',
    question: 'The /usr directory contains...',
    options: ['User programs and data', 'User home directories', 'User configuration', 'User logs'],
    correctIndices: [0],
    explanation: '/usr contains user programs, libraries, and documentation.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-36',
    question: 'To go to home directory, type...',
    options: ['cd home', 'cd /', 'cd or cd ~', 'cd ..'],
    correctIndices: [2],
    explanation: 'cd alone or cd ~ takes you to your home directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-37',
    question: 'To go to root directory, type...',
    options: ['cd root', 'cd /', 'cd ~', 'cd ..'],
    correctIndices: [1],
    explanation: 'cd / takes you to the root directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-38',
    question: 'To go up one directory, type...',
    options: ['cd up', 'cd back', 'cd ..', 'cd -'],
    correctIndices: [2],
    explanation: 'cd .. moves up to the parent directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-39',
    question: 'To go to previous directory, type...',
    options: ['cd back', 'cd prev', 'cd -', 'cd ..'],
    correctIndices: [2],
    explanation: 'cd - switches to the previous working directory.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-40',
    question: 'The rm flag -r means...',
    options: ['Read only', 'Recursive', 'Remove all', 'Really delete'],
    correctIndices: [1],
    explanation: 'The -r flag makes rm recursive, allowing it to delete directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-41',
    question: 'The rm flag -f means...',
    options: ['File only', 'Force', 'Fast', 'Full'],
    correctIndices: [1],
    explanation: 'The -f flag forces removal without prompting for confirmation.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-42',
    question: 'The cp flag -r means...',
    options: ['Read only', 'Recursive', 'Replace', 'Remove after'],
    correctIndices: [1],
    explanation: 'The -r flag makes cp recursive, copying directories and their contents.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-43',
    question: 'The mkdir flag -p means...',
    options: ['Permission', 'Create parents', 'Preserve', 'Private'],
    correctIndices: [1],
    explanation: 'The -p flag creates parent directories as needed.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-44',
    question: 'The command to clear terminal is...',
    options: ['cls', 'clear', 'clean', 'wipe'],
    correctIndices: [1],
    explanation: 'clear clears the terminal screen.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-45',
    question: 'The command to show command history is...',
    options: ['hist', 'log', 'history', 'past'],
    correctIndices: [2],
    explanation: 'history displays previously executed commands.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-46',
    question: 'To repeat last command, type...',
    options: ['repeat', 'last', '!!', 'redo'],
    correctIndices: [2],
    explanation: '!! repeats the last executed command.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-47',
    question: 'Tab key is used for...',
    options: ['Indenting', 'Auto-completion', 'Switching windows', 'Creating tabs'],
    correctIndices: [1],
    explanation: 'Tab provides auto-completion for commands, files, and directories.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-48',
    question: 'The man command shows...',
    options: ['Current user', 'Manual pages', 'System information', 'Memory usage'],
    correctIndices: [1],
    explanation: 'man displays the manual pages for commands.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-49',
    question: 'To exit man pages, press...',
    options: ['x', 'e', 'q', 'ESC'],
    correctIndices: [2],
    explanation: 'Press q to quit the man page viewer.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-50',
    question: 'Select all that are text editors (choose 3):',
    options: ['vim', 'cat', 'nano', 'less', 'emacs', 'grep', 'more', 'tail', 'head', 'find'],
    correctIndices: [0, 2, 4],
    explanation: 'vim, nano, and emacs are text editors. cat, less, more are viewers, grep/find are search tools.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-51',
    question: 'To open vim, type...',
    options: ['vi', 'vim filename', 'edit', 'open'],
    correctIndices: [1],
    explanation: 'vim filename opens the specified file in vim editor.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-52',
    question: 'In vim, to enter insert mode press...',
    options: ['e', 'i', 'a', 'o'],
    correctIndices: [1],
    explanation: 'Press i to enter insert mode in vim.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-53',
    question: 'In vim, to exit insert mode press...',
    options: ['q', 'Enter', 'ESC', 'Ctrl+C'],
    correctIndices: [2],
    explanation: 'Press ESC to exit insert mode and return to normal mode.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-54',
    question: 'In vim, to save and quit type...',
    options: [':save', ':exit', ':wq', ':sq'],
    correctIndices: [2],
    explanation: ':wq writes (saves) the file and quits vim.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-55',
    question: 'In vim, to quit without saving type...',
    options: [':exit', ':quit', ':q!', ':x'],
    correctIndices: [2],
    explanation: ':q! quits vim without saving changes (! forces quit).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-56',
    question: 'In vim, to save without quitting type...',
    options: [':save', ':w', ':s', ':write'],
    correctIndices: [1],
    explanation: ':w writes (saves) the file without quitting.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-57',
    question: 'In vim, to delete a line type...',
    options: ['d', 'del', 'dd', 'dl'],
    correctIndices: [2],
    explanation: 'dd deletes the current line in vim.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-58',
    question: 'In vim, to undo type...',
    options: ['z', 'u', 'Ctrl+Z', 'undo'],
    correctIndices: [1],
    explanation: 'Press u to undo the last change in vim.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-59',
    question: 'In vim, to search type...',
    options: ['s', 'f', '/pattern', '?pattern'],
    correctIndices: [2],
    explanation: '/pattern searches forward for the pattern in vim.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-60',
    question: 'The command to show disk space is...',
    options: ['disk', 'space', 'df', 'du'],
    correctIndices: [2],
    explanation: 'df (disk free) shows disk space usage for mounted filesystems.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-61',
    question: 'The command to show directory size is...',
    options: ['disk', 'size', 'du', 'df'],
    correctIndices: [2],
    explanation: 'du (disk usage) shows the size of directories and files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-62',
    question: 'The df flag -h shows...',
    options: ['Help', 'Human readable', 'Hidden', 'Hierarchy'],
    correctIndices: [1],
    explanation: 'The -h flag shows sizes in human-readable format (KB, MB, GB).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-63',
    question: 'The du flag -s shows...',
    options: ['Size', 'Summary', 'Sort', 'Subdirectories'],
    correctIndices: [1],
    explanation: 'The -s flag shows only a summary total instead of per-file details.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-64',
    question: 'The command to link files is...',
    options: ['link', 'ln', 'lnk', 'connect'],
    correctIndices: [1],
    explanation: 'ln creates links between files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-65',
    question: 'A symbolic link is created with...',
    options: ['ln', 'ln -s', 'ln -l', 'ln -h'],
    correctIndices: [1],
    explanation: 'ln -s creates a symbolic (soft) link.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-66',
    question: 'A hard link...',
    options: ['Can link directories', 'Can link across filesystems', 'Points to the same inode', 'Is a copy of the file'],
    correctIndices: [2],
    explanation: 'A hard link points to the same inode as the original file.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-67',
    question: 'A symbolic link...',
    options: ['Points to the inode', 'Points to the path', 'Is a copy', 'Cannot be deleted'],
    correctIndices: [1],
    explanation: 'A symbolic link points to the path/name of the target file.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-68',
    question: 'The command to show file type is...',
    options: ['type', 'file', 'what', 'show'],
    correctIndices: [1],
    explanation: 'file determines and displays the type of a file.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-69',
    question: 'The command to compare files is...',
    options: ['compare', 'diff', 'cmp', 'check'],
    correctIndices: [1],
    explanation: 'diff compares files line by line and shows differences.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-70',
    question: 'The command to sort lines is...',
    options: ['order', 'arrange', 'sort', 'organize'],
    correctIndices: [2],
    explanation: 'sort sorts lines of text files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-71',
    question: 'The command to remove duplicates is...',
    options: ['dedup', 'unique', 'uniq', 'distinct'],
    correctIndices: [2],
    explanation: 'uniq filters out adjacent duplicate lines (often used with sort).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-72',
    question: 'The command to cut columns is...',
    options: ['column', 'slice', 'cut', 'extract'],
    correctIndices: [2],
    explanation: 'cut extracts sections (columns) from each line of files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-73',
    question: 'The command to translate characters is...',
    options: ['translate', 'convert', 'tr', 'change'],
    correctIndices: [2],
    explanation: 'tr translates or deletes characters from input.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-74',
    question: 'The command to reverse lines is...',
    options: ['reverse', 'flip', 'tac', 'rev'],
    correctIndices: [2],
    explanation: 'tac prints lines in reverse order (cat spelled backwards).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-75',
    question: 'cat spelled backwards is...',
    options: ['reverse', 'flip', 'tac', 'rac'],
    correctIndices: [2],
    explanation: 'tac is cat spelled backwards and reverses line order.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-76',
    question: 'The command to print text is...',
    options: ['print', 'say', 'echo', 'write'],
    correctIndices: [2],
    explanation: 'echo prints text or variable values to the terminal.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-77',
    question: 'To redirect output to a file, use...',
    options: ['|', '<', '>', '&'],
    correctIndices: [2],
    explanation: '> redirects output to a file (overwrites existing content).',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-78',
    question: 'To append output to a file, use...',
    options: ['>', '<', '>>', '|'],
    correctIndices: [2],
    explanation: '>> appends output to a file without overwriting.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-79',
    question: 'To pipe output to another command, use...',
    options: ['>', '>>', '|', '&'],
    correctIndices: [2],
    explanation: '| (pipe) sends output of one command as input to another.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-80',
    question: 'The command to show calendar is...',
    options: ['calendar', 'cal', 'date', 'time'],
    correctIndices: [1],
    explanation: 'cal displays a calendar.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-81',
    question: 'The command to show date is...',
    options: ['time', 'cal', 'date', 'now'],
    correctIndices: [2],
    explanation: 'date displays or sets the system date and time.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-82',
    question: 'The command to show who is logged in is...',
    options: ['users', 'logged', 'who', 'login'],
    correctIndices: [2],
    explanation: 'who shows who is currently logged in to the system.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-83',
    question: 'The command to show current user is...',
    options: ['me', 'user', 'whoami', 'current'],
    correctIndices: [2],
    explanation: 'whoami displays the current username.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-84',
    question: 'The command to show system info is...',
    options: ['system', 'info', 'uname', 'sys'],
    correctIndices: [2],
    explanation: 'uname displays system information.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-85',
    question: 'The uname flag -a shows...',
    options: ['Architecture', 'All information', 'About', 'Admin'],
    correctIndices: [1],
    explanation: 'The -a flag shows all available system information.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-86',
    question: 'Select all that are valid paths (choose 4):',
    options: ['/home/user', 'home/user/', './file.txt', 'file.txt/', '/etc/passwd', 'etc/passwd/', '../parent', 'parent../', '/./home', 'home/.'],
    correctIndices: [0, 2, 4, 6],
    explanation: '/home/user, ./file.txt, /etc/passwd, and ../parent are valid paths. Paths ending with / for files or with invalid syntax are incorrect.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-87',
    question: 'The command to show environment variables is...',
    options: ['vars', 'show', 'env', 'list'],
    correctIndices: [2],
    explanation: 'env displays all environment variables.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-88',
    question: 'The PATH variable contains...',
    options: ['Current directory', 'Directories to search for commands', 'User home', 'System root'],
    correctIndices: [1],
    explanation: 'PATH contains a list of directories where the shell looks for commands.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-89',
    question: 'To show a variable value, use...',
    options: ['show $VAR', 'print $VAR', 'echo $VAR', 'var $VAR'],
    correctIndices: [2],
    explanation: 'echo $VAR displays the value of the variable VAR.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-90',
    question: 'The command to set an alias is...',
    options: ['set', 'alias', 'define', 'shortcut'],
    correctIndices: [1],
    explanation: 'alias creates shortcut names for commands.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-91',
    question: 'Aliases are stored in...',
    options: ['/etc/alias', '~/.bashrc', '/var/alias', '~/.alias'],
    correctIndices: [1],
    explanation: 'Aliases are typically defined in ~/.bashrc or ~/.bash_aliases.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-92',
    question: 'The command to reload bashrc is...',
    options: ['reload', 'refresh', 'source ~/.bashrc', 'bash reload'],
    correctIndices: [2],
    explanation: 'source ~/.bashrc (or . ~/.bashrc) reloads the bash configuration.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-93',
    question: 'The tilde expansion ~user means...',
    options: ['Current user home', 'That user\'s home directory', 'Root directory', 'Tmp directory'],
    correctIndices: [1],
    explanation: '~user expands to the home directory of the specified user.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-94',
    question: 'The glob * matches...',
    options: ['One character', 'Zero or more characters', 'Exactly one character', 'Letters only'],
    correctIndices: [1],
    explanation: '* matches zero or more characters in glob patterns.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-95',
    question: 'The glob ? matches...',
    options: ['Zero or more characters', 'Exactly one character', 'One or more characters', 'Numbers only'],
    correctIndices: [1],
    explanation: '? matches exactly one character in glob patterns.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-96',
    question: 'The glob [abc] matches...',
    options: ['The string abc', 'One of a, b, or c', 'Any three characters', 'a followed by b followed by c'],
    correctIndices: [1],
    explanation: '[abc] matches any single character that is a, b, or c.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-97',
    question: '*.txt matches...',
    options: ['Only .txt', 'All files ending in .txt', 'Files containing txt', 'Hidden txt files'],
    correctIndices: [1],
    explanation: '*.txt matches all files with names ending in .txt.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-98',
    question: 'Select all that are in /var (choose 3):',
    options: ['log', 'home', 'mail', 'etc', 'spool', 'bin', 'usr', 'root', 'boot', 'dev'],
    correctIndices: [0, 2, 4],
    explanation: '/var contains log, mail, and spool directories for variable data.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-99',
    question: 'The /dev directory contains...',
    options: ['Development files', 'Device files', 'Developer tools', 'Deleted files'],
    correctIndices: [1],
    explanation: '/dev contains device files representing hardware and virtual devices.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-100',
    question: 'The /proc directory contains...',
    options: ['Programs', 'Processes', 'Process information (virtual)', 'Procedures'],
    correctIndices: [2],
    explanation: '/proc is a virtual filesystem with process and kernel information.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-101',
    question: 'The command to show mounted filesystems is...',
    options: ['mounts', 'mount', 'mounted', 'fs'],
    correctIndices: [1],
    explanation: 'mount shows currently mounted filesystems.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-102',
    question: 'The command to show block devices is...',
    options: ['blocks', 'devices', 'lsblk', 'blk'],
    correctIndices: [2],
    explanation: 'lsblk lists information about block devices.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-103',
    question: 'The touch command on existing file...',
    options: ['Deletes it', 'Updates timestamp', 'Does nothing', 'Creates backup'],
    correctIndices: [1],
    explanation: 'touch on an existing file updates its access and modification timestamps.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-104',
    question: 'The command to concatenate files is...',
    options: ['concat', 'join', 'cat', 'merge'],
    correctIndices: [2],
    explanation: 'cat concatenates files and prints them to standard output.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-105',
    question: 'cat file1 file2 > file3 does...',
    options: ['Copies file1 to file3', 'Copies file2 to file3', 'Combines file1 and file2 into file3', 'Creates three files'],
    correctIndices: [2],
    explanation: 'cat file1 file2 > file3 concatenates file1 and file2 into file3.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-106',
    question: 'The command to split files is...',
    options: ['divide', 'split', 'break', 'separate'],
    correctIndices: [1],
    explanation: 'split divides a file into pieces.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-107',
    question: 'The command to join lines is...',
    options: ['merge', 'combine', 'paste', 'concat'],
    correctIndices: [2],
    explanation: 'paste merges lines of files side by side.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-108',
    question: 'Select all valid ls flags (choose 4):',
    options: ['-l', '-x', '-a', '-b', '-h', '-j', '-t', '-y', '-z', '-w'],
    correctIndices: [0, 2, 4, 6],
    explanation: '-l (long), -a (all), -h (human-readable), and -t (sort by time) are valid ls flags.',
    difficulty: 'VG',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-109',
    question: 'The /boot directory contains...',
    options: ['Boot scripts', 'Kernel and bootloader', 'Boot logs', 'Boot configuration'],
    correctIndices: [1],
    explanation: '/boot contains the Linux kernel and bootloader files.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  },
  {
    id: 'omtenta-v2-fs-110',
    question: 'The /opt directory contains...',
    options: ['Options', 'Optional/third-party software', 'Operating system', 'Output files'],
    correctIndices: [1],
    explanation: '/opt is for optional or third-party software packages.',
    difficulty: 'G',
    category: 'Filsystem & Navigation',
    topic: 'filsystem'
  }
]
