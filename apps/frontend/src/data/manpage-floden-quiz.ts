/**
 * MANPAGE FLÖDEN - Scenario & Flow questions based on Manpage Tenta (298 original questions)
 * All questions in English with varied correct answer positions
 * 
 * Created: 2026-01-18
 * Source: Mirrors manpage-tenta-quiz.ts with scenario/flow format
 * Content: ~150 scenario questions covering all major categories
 */

export interface ManpageFlodenQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    type: 'scenario' | 'flow'
}

export const MANPAGE_FLODEN_QUESTIONS: ManpageFlodenQuestion[] = [
    // ============================================
    // LINUX GRUNDLÄGGANDE - Scenario Questions (30)
    // ============================================
    {
        id: 'mpflod-s1',
        question: 'Mika asks how to list all files including hidden ones in the current directory. What flag does she need?',
        options: [
            'Use ls -h for hidden files only',
            'Use ls -a to show all files',
            'Use ls -l for long listing mode',
            'Use ls -r for recursive listing'
        ],
        correctIndex: 1,
        explanation: 'ls -a shows all files including hidden ones (files starting with a dot).',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s2',
        question: 'Chrille wants to display manual pages for the grep command. Which command should she use?',
        options: [
            'Run help grep for manual page',
            'Run info grep for manual page',
            'Run manual grep for the page',
            'Run man grep for manual page'
        ],
        correctIndex: 3,
        explanation: 'man command displays manual pages. Usage: man <command>.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s3',
        question: 'Said needs to print only the first 10 lines of a large log file. What command achieves this?',
        options: [
            'Use head command for first lines',
            'Use tail command for first lines',
            'Use top command for first lines',
            'Use first command for top lines'
        ],
        correctIndex: 0,
        explanation: 'head displays the first lines of a file. Default is 10 lines, use -n to specify.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s4',
        question: 'Mika wants to see the last 20 lines of a server log. Which command with what flag?',
        options: [
            'Use head -n 20 for last lines',
            'Use last -n 20 for last lines',
            'Use end -n 20 for last lines',
            'Use tail -n 20 for last lines'
        ],
        correctIndex: 3,
        explanation: 'tail -n 20 displays the last 20 lines of a file.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s5',
        question: 'Chrille needs to search for the word ERROR in multiple log files. What command is best?',
        options: [
            'Use grep ERROR for searching',
            'Use find ERROR for searching',
            'Use search ERROR for pattern',
            'Use look ERROR for the word'
        ],
        correctIndex: 0,
        explanation: 'grep searches for patterns in files. Usage: grep "ERROR" *.log.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s6',
        question: 'Said asks how to count the number of lines in a file. What command and flag?',
        options: [
            'Use count -l for line count',
            'Use lines file for counting',
            'Use wc -l for line counting',
            'Use num -l for line number'
        ],
        correctIndex: 2,
        explanation: 'wc -l counts lines in a file. wc stands for word count.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s7',
        question: 'Mika needs to display disk usage of the current directory. Which command?',
        options: [
            'Use df to show disk usage',
            'Use disk to show usage here',
            'Use usage to display disk use',
            'Use du to show disk usage'
        ],
        correctIndex: 3,
        explanation: 'du (disk usage) shows space used by files and directories.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s8',
        question: 'Axel needs to create a new empty file called notes.txt. What is the simplest command?',
        options: [
            'Use create notes.txt for file',
            'Use touch notes.txt for file',
            'Use new notes.txt for making',
            'Use make notes.txt for file'
        ],
        correctIndex: 1,
        explanation: 'touch creates empty files or updates timestamps of existing files.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s9',
        question: 'Levie wants to display the current working directory path. Which command?',
        options: [
            'Use cwd to print directory',
            'Use pwd to print directory',
            'Use dir to print current path',
            'Use path to show directory'
        ],
        correctIndex: 1,
        explanation: 'pwd (print working directory) displays the current directory path.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s10',
        question: 'Axel needs to clear the terminal screen. What command should she use?',
        options: [
            'Use reset to clear screen now',
            'Use clean to clear the screen',
            'Use clear to clear the screen',
            'Use cls to clear the screen'
        ],
        correctIndex: 2,
        explanation: 'clear clears the terminal screen. Ctrl+L also works.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s11',
        question: 'Levie wants to display the contents of a short file. Which command is appropriate?',
        options: [
            'Use cat to display file content',
            'Use show to display file data',
            'Use print to display content',
            'Use display to show the file'
        ],
        correctIndex: 0,
        explanation: 'cat concatenates and displays file contents.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s12',
        question: 'Your team needs to check which shell they are currently using. What command reveals this?',
        options: [
            'Run shell to show current one',
            'Run which bash to find shell',
            'Run echo $SHELL to show it',
            'Run current to display shell'
        ],
        correctIndex: 2,
        explanation: 'echo $SHELL displays the current shell. Also: echo $0.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s13',
        question: 'Levie wants to see the current date and time. What single command displays this?',
        options: [
            'Use time to show date and time',
            'Use now to show current time',
            'Use clock to display the time',
            'Use date to show date and time'
        ],
        correctIndex: 3,
        explanation: 'date displays the current date and time.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s14',
        question: 'Said needs to find where the python3 binary is located. What command helps?',
        options: [
            'Use which python3 to locate it',
            'Use where python3 to find it',
            'Use locate python3 to find it',
            'Use find python3 to search it'
        ],
        correctIndex: 0,
        explanation: 'which shows the path to a command binary in PATH.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s15',
        question: 'Mika wants to display her username. What command shows the current logged-in user?',
        options: [
            'Use user to show username now',
            'Use whoami to show username',
            'Use me to display the user',
            'Use name to show current user'
        ],
        correctIndex: 1,
        explanation: 'whoami displays the current username.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s16',
        question: 'Chrille wants to see all environment variables. What command displays them all?',
        options: [
            'Use vars to show all of them',
            'Use env to show all of them',
            'Use show to display variables',
            'Use list to print variables'
        ],
        correctIndex: 1,
        explanation: 'env displays all environment variables. Also: printenv.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s17',
        question: 'Chrille needs to display the hostname of the server. What command?',
        options: [
            'Use hostname to display it',
            'Use host to show the name',
            'Use name to show hostname',
            'Use server to display name'
        ],
        correctIndex: 0,
        explanation: 'hostname displays or sets the system hostname.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s18',
        question: 'Axel needs to compare two configuration files for differences. Best command?',
        options: [
            'Use diff to compare two files',
            'Use comp to compare the files',
            'Use compare to check for diff',
            'Use check to find differences'
        ],
        correctIndex: 0,
        explanation: 'diff compares files line by line and shows differences.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s19',
        question: 'Levie wants to sort lines in a file alphabetically. What command?',
        options: [
            'Use order to sort the lines',
            'Use arrange to sort the file',
            'Use sort to order the lines',
            'Use alpha to sort alphabetic'
        ],
        correctIndex: 2,
        explanation: 'sort sorts lines of text files alphabetically by default.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s20',
        question: 'Mika wants to remove duplicate lines from a sorted file. What command?',
        options: [
            'Use unique to remove dupes',
            'Use uniq to remove duplicates',
            'Use dedup to remove the dupes',
            'Use nodupe to remove copies'
        ],
        correctIndex: 1,
        explanation: 'uniq removes adjacent duplicate lines. File must be sorted first.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s21',
        question: 'Mika needs to follow a log file in real-time. What command with what flag?',
        options: [
            'Use follow -f logfile for this',
            'Use watch -f logfile for this',
            'Use tail -f logfile to follow',
            'Use live -f logfile to watch'
        ],
        correctIndex: 2,
        explanation: 'tail -f follows a file in real-time, showing new lines as they appear.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s22',
        question: 'Said asks how to display only unique lines from grep output. What to pipe to?',
        options: [
            'Pipe to unique for filtering',
            'Pipe to distinct for unique',
            'Pipe to sort then uniq combo',
            'Pipe to filter for unique'
        ],
        correctIndex: 2,
        explanation: 'Use sort | uniq to get unique lines. uniq only removes adjacent duplicates.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s23',
        question: 'Axel needs to extract column 2 from a CSV file. What command with delimiter?',
        options: [
            'Use col -d, -f2 for column 2',
            'Use cut -d, -f2 for column 2',
            'Use get -d, -f2 for column 2',
            'Use pick -d, -f2 for column'
        ],
        correctIndex: 1,
        explanation: 'cut -d"," -f2 extracts field 2 using comma as delimiter.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s24',
        question: 'Levie wants to run a command with superuser privileges. What prefix command?',
        options: [
            'Use admin before the command',
            'Use root before the command',
            'Use super before the command',
            'Use sudo before the command'
        ],
        correctIndex: 3,
        explanation: 'sudo runs commands with superuser privileges.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s25',
        question: 'Axel needs to see the type of a file without extension info. What command?',
        options: [
            'Use type filename for info',
            'Use file filename for info',
            'Use kind filename for info',
            'Use what filename for type'
        ],
        correctIndex: 1,
        explanation: 'file determines file type by examining content, not extension.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s26',
        question: 'Levie wants to see the absolute path of a relative path. What command?',
        options: [
            'Use realpath for absolute path',
            'Use abspath for absolute path',
            'Use fullpath to get absolute',
            'Use absolute to get the path'
        ],
        correctIndex: 0,
        explanation: 'realpath resolves and prints the absolute path.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s27',
        question: 'Said wants to display system uptime. What command shows how long the system has been running?',
        options: [
            'Use runtime to show uptime',
            'Use uptime to display info',
            'Use running to show duration',
            'Use time to show system up'
        ],
        correctIndex: 1,
        explanation: 'uptime shows how long the system has been running plus load averages.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s28',
        question: 'Axel needs to display disk space of all mounted filesystems. What command?',
        options: [
            'Use du to show free space',
            'Use disk to show free space',
            'Use df to show free space',
            'Use space to show disk free'
        ],
        correctIndex: 2,
        explanation: 'df (disk free) shows disk space usage of mounted filesystems.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s29',
        question: 'Levie wants human-readable sizes in disk output. What flag makes sizes readable?',
        options: [
            'Use -r for readable format',
            'Use -h for human readable',
            'Use -s for size readable',
            'Use -f for friendly format'
        ],
        correctIndex: 1,
        explanation: '-h flag displays sizes in human-readable format (K, M, G).',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },
    {
        id: 'mpflod-s30',
        question: 'Mika wants to see command history. What command shows previously executed commands?',
        options: [
            'Use past to show commands',
            'Use commands to show history',
            'Use log to show the history',
            'Use history to show commands'
        ],
        correctIndex: 3,
        explanation: 'history displays the command history list.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'scenario'
    },

    // ============================================
    // FILER & KATALOGER - Scenario Questions (20)
    // ============================================
    {
        id: 'mpflod-s31',
        question: 'Axel needs to create a new directory called projects. What command?',
        options: [
            'Use md projects to create it',
            'Use newdir projects to make',
            'Use mkdir projects to create',
            'Use create projects directory'
        ],
        correctIndex: 2,
        explanation: 'mkdir creates directories. Usage: mkdir directory_name.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s32',
        question: 'Chrille needs to create nested directories /a/b/c at once. What flag with mkdir?',
        options: [
            'Use mkdir -r for recursive',
            'Use mkdir -n for nested dirs',
            'Use mkdir -a for all at once',
            'Use mkdir -p for parent dirs'
        ],
        correctIndex: 3,
        explanation: 'mkdir -p creates parent directories as needed.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s33',
        question: 'Levie wants to remove an empty directory. What command is appropriate?',
        options: [
            'Use rmdir for empty directory',
            'Use rd for empty directory',
            'Use deldir for empty dir',
            'Use remove for empty dir'
        ],
        correctIndex: 0,
        explanation: 'rmdir removes empty directories only.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s34',
        question: 'Said needs to remove a directory with files inside. What command and flag?',
        options: [
            'Use rmdir -f to force remove',
            'Use rm -r for recursive delete',
            'Use del -r for recursive del',
            'Use remove -a for all files'
        ],
        correctIndex: 1,
        explanation: 'rm -r removes directories recursively including contents.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s35',
        question: 'Mika wants to copy a file to another location. What command?',
        options: [
            'Use copy source dest for it',
            'Use mv source dest to copy',
            'Use cp source dest to copy',
            'Use dup source dest for it'
        ],
        correctIndex: 2,
        explanation: 'cp copies files or directories. Usage: cp source destination.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s36',
        question: 'Chrille needs to copy a directory with all contents. What flag with cp?',
        options: [
            'Use cp -a for all contents',
            'Use cp -r for recursive copy',
            'Use cp -d for directory copy',
            'Use cp -c for complete copy'
        ],
        correctIndex: 1,
        explanation: 'cp -r copies directories recursively.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s37',
        question: 'Axel wants to move a file to a new location. What command?',
        options: [
            'Use mv source dest to move',
            'Use move source dest to go',
            'Use cp source dest to move',
            'Use transfer source to dest'
        ],
        correctIndex: 0,
        explanation: 'mv moves files or directories. Also used for renaming.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s38',
        question: 'Levie wants to rename a file from old.txt to new.txt. What command?',
        options: [
            'Use rename old.txt new.txt',
            'Use mv old.txt new.txt now',
            'Use rn old.txt new.txt now',
            'Use change old.txt new.txt'
        ],
        correctIndex: 1,
        explanation: 'mv is used for renaming files. Usage: mv oldname newname.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s39',
        question: 'Said needs to delete a file. What command removes files?',
        options: [
            'Use del filename to delete',
            'Use rm filename to remove it',
            'Use remove filename to del',
            'Use delete filename to go'
        ],
        correctIndex: 1,
        explanation: 'rm removes files. Use with caution.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s40',
        question: 'Mika wants to create a symbolic link to a file. What command?',
        options: [
            'Use ln -s target linkname',
            'Use link -s target linkname',
            'Use sym target linkname now',
            'Use mklink target linkname'
        ],
        correctIndex: 0,
        explanation: 'ln -s creates symbolic links. Usage: ln -s target linkname.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s41',
        question: 'Mika needs to find all .log files in /var. What command?',
        options: [
            'Use find /var -name *.log',
            'Use search /var -name *.log',
            'Use locate /var -name *.log',
            'Use look /var -name *.log'
        ],
        correctIndex: 0,
        explanation: 'find searches for files. Use: find /var -name "*.log".',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s42',
        question: 'Said wants to quickly locate a file by name using index. What command?',
        options: [
            'Use find for indexed search',
            'Use search for quick lookup',
            'Use locate for indexed find',
            'Use index for finding files'
        ],
        correctIndex: 2,
        explanation: 'locate uses a prebuilt index for fast file searches.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s43',
        question: 'Axel needs to change to the home directory. What is the shortest command?',
        options: [
            'Use cd ~ to go to home dir',
            'Use cd /home to go there',
            'Use home to change to home',
            'Use cd with no args goes home'
        ],
        correctIndex: 3,
        explanation: 'cd with no arguments changes to home directory. cd ~ also works.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s44',
        question: 'Levie wants to go to the previous directory. What shorthand?',
        options: [
            'Use cd .. for previous dir',
            'Use cd - for previous dir',
            'Use cd back for previous',
            'Use cd prev for previous'
        ],
        correctIndex: 1,
        explanation: 'cd - changes to the previous directory. cd .. goes up one level.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s45',
        question: 'Mika wants to see the directory tree structure. What command?',
        options: [
            'Use ls -tree for structure',
            'Use tree to show structure',
            'Use dir -tree for showing',
            'Use struct to show dirs'
        ],
        correctIndex: 1,
        explanation: 'tree displays directory structure in a tree format.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s46',
        question: 'Chrille needs to check file sizes in current directory. What ls flag?',
        options: [
            'Use ls -s for size display',
            'Use ls -z for size display',
            'Use ls -l for detailed list',
            'Use ls -d for disk sizes'
        ],
        correctIndex: 2,
        explanation: 'ls -l shows long format including file sizes.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s47',
        question: 'Said asks what the tilde ~ represents in paths. What does it mean?',
        options: [
            'Tilde represents root folder',
            'Tilde represents tmp folder',
            'Tilde represents current dir',
            'Tilde represents home folder'
        ],
        correctIndex: 3,
        explanation: '~ (tilde) represents the current users home directory.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s48',
        question: 'Levie wants to find files modified in the last 24 hours. What find option?',
        options: [
            'Use find -mtime -1 for it',
            'Use find -modified 24h ago',
            'Use find -recent 1 day now',
            'Use find -last 24h for it'
        ],
        correctIndex: 0,
        explanation: 'find -mtime -1 finds files modified in the last day.',
        difficulty: 'VG',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s49',
        question: 'Said needs to find files larger than 100MB. What find option?',
        options: [
            'Use find -size +100M for it',
            'Use find -larger 100M files',
            'Use find -big 100M for it',
            'Use find -min 100M for it'
        ],
        correctIndex: 0,
        explanation: 'find -size +100M finds files larger than 100 megabytes.',
        difficulty: 'VG',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },
    {
        id: 'mpflod-s50',
        question: 'Mika wants to execute a command on each found file. What find option?',
        options: [
            'Use find -run cmd for each',
            'Use find -do cmd for each',
            'Use find -cmd for execution',
            'Use find -exec cmd {} for it'
        ],
        correctIndex: 3,
        explanation: 'find -exec command {} \\; executes command on each file.',
        difficulty: 'VG',
        category: 'Filer & Kataloger',
        type: 'scenario'
    },

    // ============================================
    // DOCKER & CONTAINERS - Scenario Questions (20)
    // ============================================
    {
        id: 'mpflod-s51',
        question: 'Mika asks how to list all running containers. What docker command?',
        options: [
            'Use docker list for running',
            'Use docker show for running',
            'Use docker ps for running',
            'Use docker containers list'
        ],
        correctIndex: 2,
        explanation: 'docker ps lists running containers. Add -a for all containers.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s52',
        question: 'Chrille needs to see all containers including stopped ones. What flag?',
        options: [
            'Use docker ps -s for stopped',
            'Use docker ps -a for all',
            'Use docker ps -l for list',
            'Use docker ps -f for full'
        ],
        correctIndex: 1,
        explanation: 'docker ps -a shows all containers including stopped ones.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s53',
        question: 'Levie wants to pull an image from Docker Hub. What command?',
        options: [
            'Use docker get image name',
            'Use docker pull image name',
            'Use docker download imagename',
            'Use docker fetch image name'
        ],
        correctIndex: 1,
        explanation: 'docker pull downloads an image from a registry.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s54',
        question: 'Said needs to build an image from a Dockerfile. What command?',
        options: [
            'Use docker create to build it',
            'Use docker make to build img',
            'Use docker compile to build',
            'Use docker build to make img'
        ],
        correctIndex: 3,
        explanation: 'docker build creates an image from a Dockerfile.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s55',
        question: 'Mika wants to run a container from an image. What command?',
        options: [
            'Use docker start image name',
            'Use docker run image name',
            'Use docker exec image name',
            'Use docker launch image now'
        ],
        correctIndex: 1,
        explanation: 'docker run creates and starts a container from an image.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s56',
        question: 'Mika needs to stop a running container. What command?',
        options: [
            'Use docker stop container id',
            'Use docker halt container id',
            'Use docker end container id',
            'Use docker kill container id'
        ],
        correctIndex: 0,
        explanation: 'docker stop gracefully stops a container.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s57',
        question: 'Said asks how to remove a stopped container. What command?',
        options: [
            'Use docker rm container id',
            'Use docker del container id',
            'Use docker remove container',
            'Use docker delete container'
        ],
        correctIndex: 0,
        explanation: 'docker rm removes stopped containers.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s58',
        question: 'Axel needs to view container logs. What command?',
        options: [
            'Use docker log container id',
            'Use docker output container',
            'Use docker logs container id',
            'Use docker show container log'
        ],
        correctIndex: 2,
        explanation: 'docker logs displays logs from a container.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s59',
        question: 'Levie wants to execute a command inside a running container. What command?',
        options: [
            'Use docker run to execute cmd',
            'Use docker cmd in container',
            'Use docker exec to run inside',
            'Use docker shell to execute'
        ],
        correctIndex: 2,
        explanation: 'docker exec runs a command in a running container.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s60',
        question: 'Axel needs to list all local Docker images. What command?',
        options: [
            'Use docker images for list',
            'Use docker list images now',
            'Use docker show images all',
            'Use docker img list for all'
        ],
        correctIndex: 0,
        explanation: 'docker images lists all local images.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s61',
        question: 'Levie wants to remove a Docker image. What command?',
        options: [
            'Use docker rm image name now',
            'Use docker del image name',
            'Use docker rmi image name',
            'Use docker remove image now'
        ],
        correctIndex: 2,
        explanation: 'docker rmi removes images. Use -f to force.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s62',
        question: 'Chrille needs to map port 80 to 8080 when running container. What flag?',
        options: [
            'Use -p 8080:80 for mapping',
            'Use -P 8080:80 for mapping',
            'Use -m 80:8080 for mapping',
            'Use -port 80:8080 mapping'
        ],
        correctIndex: 0,
        explanation: '-p host:container maps ports. -p 8080:80 maps host 8080 to container 80.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s63',
        question: 'Levie wants to run container in detached mode (background). What flag?',
        options: [
            'Use -b for background mode',
            'Use -d for detached mode',
            'Use -bg for background run',
            'Use -back for background'
        ],
        correctIndex: 1,
        explanation: '-d runs container in detached (background) mode.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s64',
        question: 'Said needs to mount a volume in a container. What flag?',
        options: [
            'Use -v host:container path',
            'Use -m host:container path',
            'Use -vol host:container now',
            'Use -mount host:container'
        ],
        correctIndex: 0,
        explanation: '-v mounts volumes. Usage: -v /host/path:/container/path.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s65',
        question: 'Mika wants to set an environment variable in container. What flag?',
        options: [
            'Use -env VAR=value for it',
            'Use -e VAR=value for env',
            'Use -E VAR=value for env',
            'Use -var VAR=value now'
        ],
        correctIndex: 1,
        explanation: '-e sets environment variables. Usage: -e VAR=value.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s66',
        question: 'Mika needs to name a container. What flag when running?',
        options: [
            'Use -n name for naming it',
            'Use --name name for naming',
            'Use -N name for naming it',
            'Use --container name here'
        ],
        correctIndex: 1,
        explanation: '--name assigns a name to the container.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s67',
        question: 'Said asks how to get an interactive shell in container. What flags?',
        options: [
            'Use -i -t for interactive',
            'Use -s for shell access',
            'Use -sh for shell inside',
            'Use -shell for interactive'
        ],
        correctIndex: 0,
        explanation: '-i (interactive) -t (tty) combined for shell access. Often: -it.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s68',
        question: 'Axel needs to see detailed info about a container. What command?',
        options: [
            'Use docker info container id',
            'Use docker show container id',
            'Use docker inspect container',
            'Use docker details container'
        ],
        correctIndex: 2,
        explanation: 'docker inspect shows detailed container information in JSON.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s69',
        question: 'Levie wants to copy a file from container to host. What command?',
        options: [
            'Use docker copy container:path',
            'Use docker cp container:path',
            'Use docker get container:path',
            'Use docker fetch container:p'
        ],
        correctIndex: 1,
        explanation: 'docker cp copies files between container and host.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },
    {
        id: 'mpflod-s70',
        question: 'Axel needs to restart a stopped container. What command?',
        options: [
            'Use docker run container id',
            'Use docker restart container',
            'Use docker start container id',
            'Use docker resume container'
        ],
        correctIndex: 2,
        explanation: 'docker start starts a stopped container.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'scenario'
    },

    // ============================================
    // PERMISSIONS - Scenario Questions (15)
    // ============================================
    {
        id: 'mpflod-s71',
        question: 'Axel needs to change file permissions. What command?',
        options: [
            'Use chmod to change mode bits',
            'Use perm to change permission',
            'Use mod to modify permissions',
            'Use access to change rights'
        ],
        correctIndex: 0,
        explanation: 'chmod changes file mode (permission) bits.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s72',
        question: 'Said wants to make a script executable. What chmod command?',
        options: [
            'Use chmod x script.sh now',
            'Use chmod +x script.sh now',
            'Use chmod e script.sh now',
            'Use chmod +e script.sh now'
        ],
        correctIndex: 1,
        explanation: 'chmod +x adds execute permission to a file.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s73',
        question: 'Axel needs to set permissions to rwxr-xr-x using numbers. What value?',
        options: [
            'Use chmod 644 for rwxr-xr-x',
            'Use chmod 755 for rwxr-xr-x',
            'Use chmod 775 for rwxr-xr-x',
            'Use chmod 777 for rwxr-xr-x'
        ],
        correctIndex: 1,
        explanation: '755 = rwx(7) r-x(5) r-x(5). 7=4+2+1, 5=4+0+1.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s74',
        question: 'Said needs to change file ownership. What command?',
        options: [
            'Use chown user:group file',
            'Use owner user:group file',
            'Use setowner user:group go',
            'Use chuser user:group file'
        ],
        correctIndex: 0,
        explanation: 'chown changes file owner and group.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s75',
        question: 'Mika wants to change only the group ownership. What command?',
        options: [
            'Use chown :group filename',
            'Use chgroup group filename',
            'Use chgrp group filename go',
            'Use setgroup group filename'
        ],
        correctIndex: 2,
        explanation: 'chgrp changes group ownership of a file.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s76',
        question: 'Mika needs to recursively change permissions. What flag?',
        options: [
            'Use chmod -a for all dirs',
            'Use chmod -r for recursive',
            'Use chmod -R for recursive',
            'Use chmod -d for deep mode'
        ],
        correctIndex: 2,
        explanation: 'chmod -R (capital R) changes permissions recursively.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s77',
        question: 'Said asks what permission 644 means. What is the breakdown?',
        options: [
            '644 means rwxrwxr-- access',
            '644 means rw-rw-rw- access',
            '644 means rw-r--r-- access',
            '644 means r--r--r-- access'
        ],
        correctIndex: 2,
        explanation: '644 = rw-(6) r--(4) r--(4). Owner read+write, others read only.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s78',
        question: 'Axel needs to remove write permission from group. What symbolic mode?',
        options: [
            'Use chmod g-w to remove it',
            'Use chmod -gw to remove it',
            'Use chmod w-g to remove it',
            'Use chmod rg-w to remove it'
        ],
        correctIndex: 0,
        explanation: 'chmod g-w removes write permission from group.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s79',
        question: 'Chrille asks what the setuid bit does on an executable. What is its purpose?',
        options: [
            'Runs as file owner not user',
            'Allows all users to execute',
            'Makes file read-only always',
            'Prevents file from deletion'
        ],
        correctIndex: 0,
        explanation: 'Setuid bit makes executable run as file owner, not executing user.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s80',
        question: 'Axel needs to set the sticky bit on a directory. What command?',
        options: [
            'Use chmod +s directory now',
            'Use chmod +t directory now',
            'Use chmod +k directory now',
            'Use chmod +x directory now'
        ],
        correctIndex: 1,
        explanation: 'chmod +t sets sticky bit. In directories, only owner can delete files.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s81',
        question: 'Mika asks what umask does. What is its function?',
        options: [
            'Sets default permissions mask',
            'Removes all file permissions',
            'Shows current permissions now',
            'Copies permissions to files'
        ],
        correctIndex: 0,
        explanation: 'umask sets the default permission mask for new files.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s82',
        question: 'Chrille needs to see current umask value. What command?',
        options: [
            'Run getmask for the value',
            'Run umask with no arguments',
            'Run showmask for the value',
            'Run mask to display it now'
        ],
        correctIndex: 1,
        explanation: 'umask without arguments displays the current mask.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s83',
        question: 'Axel needs to view file permissions in detail. What ls flag?',
        options: [
            'Use ls -p for permissions',
            'Use ls -a for all details',
            'Use ls -l for long format',
            'Use ls -d for details now'
        ],
        correctIndex: 2,
        explanation: 'ls -l shows long format including permissions.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s84',
        question: 'Chrille asks what r-- permission means for a directory. What can you do?',
        options: [
            'Can read and list contents',
            'Can only see file names list',
            'Can enter and read files ok',
            'Cannot access directory at all'
        ],
        correctIndex: 1,
        explanation: 'r-- on directory: can list names but not access files (need x for that).',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'scenario'
    },
    {
        id: 'mpflod-s85',
        question: 'Said asks what execute permission means on a directory. What does it allow?',
        options: [
            'Can run directory as script',
            'Can enter and access contents',
            'Can list files in directory',
            'Can write new files inside'
        ],
        correctIndex: 1,
        explanation: 'Execute (x) on directory allows entering and accessing its contents.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'scenario'
    },

    // ============================================
    // NÄTVERK - Scenario Questions (15)
    // ============================================
    {
        id: 'mpflod-s86',
        question: 'Axel needs to check network connectivity to a host. What command?',
        options: [
            'Use ping hostname to check it',
            'Use check hostname for test',
            'Use test hostname for ping',
            'Use connect hostname to try'
        ],
        correctIndex: 0,
        explanation: 'ping sends ICMP packets to test connectivity.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s87',
        question: 'Chrille needs to see all network interfaces. What command?',
        options: [
            'Use netstat for interfaces',
            'Use ip addr for interfaces',
            'Use ifshow for interfaces',
            'Use netif for interfaces'
        ],
        correctIndex: 1,
        explanation: 'ip addr shows all network interfaces and addresses.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s88',
        question: 'Axel needs to see listening ports on the system. What command?',
        options: [
            'Use ports -l for listening',
            'Use ss -l for listening sockets',
            'Use listen -p for all ports',
            'Use show -l for listening'
        ],
        correctIndex: 1,
        explanation: 'ss -l shows listening sockets. Add -t for TCP, -u for UDP.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s89',
        question: 'Said needs to trace the route to a destination. What command?',
        options: [
            'Use route hostname for trace',
            'Use path hostname for trace',
            'Use traceroute hostname now',
            'Use trace hostname for path'
        ],
        correctIndex: 2,
        explanation: 'traceroute shows the path packets take to destination.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s90',
        question: 'Axel needs to download a file from URL. What command?',
        options: [
            'Use wget URL to download it',
            'Use get URL to download it',
            'Use download URL to get it',
            'Use fetch URL to download'
        ],
        correctIndex: 0,
        explanation: 'wget downloads files from the web. curl also works.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s91',
        question: 'Mika needs to query DNS for a domain. What command?',
        options: [
            'Use dns domain for query',
            'Use query domain for dns',
            'Use nslookup domain name',
            'Use lookup domain for dns'
        ],
        correctIndex: 2,
        explanation: 'nslookup queries DNS servers. dig is another option.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s92',
        question: 'Levie needs to check what process is using port 80. What command?',
        options: [
            'Use ss -tlnp | grep :80',
            'Use port 80 | grep process',
            'Use check :80 for process',
            'Use find -port 80 process'
        ],
        correctIndex: 0,
        explanation: 'ss -tlnp shows listening TCP ports with process info.',
        difficulty: 'VG',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s93',
        question: 'Axel needs to connect to a remote server via SSH. What command?',
        options: [
            'Use ssh user@hostname now',
            'Use connect user@hostname',
            'Use remote user@hostname',
            'Use login user@hostname'
        ],
        correctIndex: 0,
        explanation: 'ssh user@hostname connects to remote server via SSH.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s94',
        question: 'Said needs to copy a file to a remote server. What command?',
        options: [
            'Use copy file user@host:path',
            'Use scp file user@host:path',
            'Use send file user@host:path',
            'Use push file user@host:path'
        ],
        correctIndex: 1,
        explanation: 'scp securely copies files to/from remote hosts.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s95',
        question: 'Axel needs to see the routing table. What command?',
        options: [
            'Use routes for routing table',
            'Use ip route for the table',
            'Use table for routing info',
            'Use show routes for table'
        ],
        correctIndex: 1,
        explanation: 'ip route shows the routing table.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s96',
        question: 'Chrille needs to test if a port is open on remote host. What command?',
        options: [
            'Use ping host:port for it',
            'Use nc -zv host port test',
            'Use test host:port for it',
            'Use check host:port open'
        ],
        correctIndex: 1,
        explanation: 'nc (netcat) -zv tests if a port is open.',
        difficulty: 'VG',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s97',
        question: 'Chrille needs to view network statistics. What command?',
        options: [
            'Use netstat for statistics',
            'Use stats for network info',
            'Use network for statistics',
            'Use net for statistics now'
        ],
        correctIndex: 0,
        explanation: 'netstat displays network statistics. ss is the modern replacement.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s98',
        question: 'Axel needs to make an HTTP request from command line. What command?',
        options: [
            'Use http URL for request',
            'Use curl URL for request',
            'Use request URL for http',
            'Use get URL for request'
        ],
        correctIndex: 1,
        explanation: 'curl makes HTTP requests and displays response.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s99',
        question: 'Said needs to see ARP table. What command shows MAC to IP mappings?',
        options: [
            'Use arp -a for ARP table',
            'Use mac -a for ARP table',
            'Use ip mac for ARP table',
            'Use show arp for the table'
        ],
        correctIndex: 0,
        explanation: 'arp -a displays the ARP cache.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },
    {
        id: 'mpflod-s100',
        question: 'Axel needs to check DNS configuration file location. Where is it?',
        options: [
            'DNS config is in /etc/dns',
            'DNS config in /etc/resolv.conf',
            'DNS config is in /etc/named',
            'DNS config in /etc/network'
        ],
        correctIndex: 1,
        explanation: '/etc/resolv.conf contains DNS resolver configuration.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'scenario'
    },

    // ============================================
    // FLOW QUESTIONS - 50 questions
    // ============================================
    {
        id: 'mpflod-f1',
        question: 'What is the correct order to find and delete old log files?',
        options: [
            'Delete first then find files',
            'Find files then delete them',
            'List files then find then del',
            'Delete all then find backup'
        ],
        correctIndex: 1,
        explanation: 'Correct order: find files with criteria → verify list → delete with -delete or -exec rm.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'flow'
    },
    {
        id: 'mpflod-f2',
        question: 'What is the correct order to set up a new user with home directory?',
        options: [
            'Create user then create home',
            'Create home then create user',
            'User and home created together',
            'Set password then create user'
        ],
        correctIndex: 2,
        explanation: 'useradd -m creates user and home directory together.',
        difficulty: 'G',
        category: 'Användarhantering',
        type: 'flow'
    },
    {
        id: 'mpflod-f3',
        question: 'What is the correct order for processing text with grep and sort?',
        options: [
            'Sort first then grep the text',
            'Grep first then sort results',
            'Both can be in any order',
            'Neither order is preferred'
        ],
        correctIndex: 1,
        explanation: 'Usually: grep to filter first → sort the filtered results.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f4',
        question: 'What is the correct order for Docker image creation to container?',
        options: [
            'Run then build then Dockerfile',
            'Dockerfile then build then run',
            'Build then Dockerfile then run',
            'Run which does all together'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Write Dockerfile → docker build → docker run.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'flow'
    },
    {
        id: 'mpflod-f5',
        question: 'What is the correct order to change file permissions and verify?',
        options: [
            'Verify first then change perms',
            'Change perms then verify with ls',
            'List then change then relist',
            'Change and verify at same time'
        ],
        correctIndex: 2,
        explanation: 'Best practice: ls -l to see current → chmod to change → ls -l to verify.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'mpflod-f6',
        question: 'What is the correct order for creating compressed backup?',
        options: [
            'Compress then archive the files',
            'Archive then compress in order',
            'Archive and compress together',
            'Verify then archive then zip'
        ],
        correctIndex: 2,
        explanation: 'tar -czvf does both: creates archive and compresses in one command.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering',
        type: 'flow'
    },
    {
        id: 'mpflod-f7',
        question: 'What is the correct order when troubleshooting network connectivity?',
        options: [
            'Check DNS then check local NIC',
            'Check local NIC then gateway',
            'Check gateway then local NIC',
            'Check remote first then local'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Check local interface → gateway → external → DNS.',
        difficulty: 'VG',
        category: 'Nätverk',
        type: 'flow'
    },
    {
        id: 'mpflod-f8',
        question: 'What is the correct order for mounting a filesystem?',
        options: [
            'Mount then create mount point',
            'Create mount point then mount',
            'Mount point created by mount',
            'Filesystem then mount point'
        ],
        correctIndex: 1,
        explanation: 'Create mount point directory first → then mount filesystem to it.',
        difficulty: 'G',
        category: 'Disk & Storage',
        type: 'flow'
    },
    {
        id: 'mpflod-f9',
        question: 'What is the correct order for checking disk space then cleaning?',
        options: [
            'Clean first then check space',
            'Check with df then clean files',
            'Clean then check then clean',
            'Check df after cleaning done'
        ],
        correctIndex: 1,
        explanation: 'Correct order: df to see usage → identify large files → clean → verify.',
        difficulty: 'G',
        category: 'Disk & Storage',
        type: 'flow'
    },
    {
        id: 'mpflod-f10',
        question: 'What is the correct order for editing a file with vim?',
        options: [
            'Edit then open then save file',
            'Open then edit then save file',
            'Save then open then edit file',
            'Open and edit at the same time'
        ],
        correctIndex: 1,
        explanation: 'Correct order: vim filename to open → i to edit → :wq to save and quit.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f11',
        question: 'What is the correct order for starting a systemd service at boot?',
        options: [
            'Start then enable for boot',
            'Enable then start the service',
            'Enable which also starts it',
            'Start which also enables it'
        ],
        correctIndex: 1,
        explanation: 'enable creates boot symlink → start runs it now. Or: enable --now does both.',
        difficulty: 'G',
        category: 'Systemd & Services',
        type: 'flow'
    },
    {
        id: 'mpflod-f12',
        question: 'What is the correct order for pipe processing with head?',
        options: [
            'Output flows left to right',
            'Output flows right to left',
            'All commands run at once',
            'Output flows in both ways'
        ],
        correctIndex: 0,
        explanation: 'Pipes flow left to right: cmd1 | cmd2 | cmd3.',
        difficulty: 'G',
        category: 'Pipes & Redirection',
        type: 'flow'
    },
    {
        id: 'mpflod-f13',
        question: 'What is the correct order for safely stopping a container?',
        options: [
            'Remove then stop container',
            'Stop then remove container',
            'Kill then stop container',
            'Stop which also removes it'
        ],
        correctIndex: 1,
        explanation: 'Correct order: docker stop → docker rm. Stop first, then remove.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'flow'
    },
    {
        id: 'mpflod-f14',
        question: 'What is the correct order for SSH key setup on new server?',
        options: [
            'Copy key then generate keypair',
            'Generate key then copy pubkey',
            'Test first then generate key',
            'Copy key which generates it'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Generate keypair → copy public key to server.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'flow'
    },
    {
        id: 'mpflod-f15',
        question: 'What is the correct order when using find with exec?',
        options: [
            'Execute then find the files',
            'Find files then execute cmd',
            'Find and execute together',
            'Execute first then find done'
        ],
        correctIndex: 2,
        explanation: 'find -exec runs command on each file as found.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'flow'
    },
    {
        id: 'mpflod-f16',
        question: 'What is the correct order for checking and killing a process?',
        options: [
            'Kill then find the process',
            'Find PID then send signal',
            'Signal then find PID to use',
            'Kill which finds it first'
        ],
        correctIndex: 1,
        explanation: 'Correct order: ps or pgrep to find PID → kill PID to terminate.',
        difficulty: 'G',
        category: 'Processer & Signaler',
        type: 'flow'
    },
    {
        id: 'mpflod-f17',
        question: 'What is the correct order for redirect stderr and stdout?',
        options: [
            'Redirect stdout then stderr',
            'Redirect stderr then stdout',
            'Redirect both at same time',
            'Either order works the same'
        ],
        correctIndex: 0,
        explanation: 'For 2>&1: redirect stdout first, then stderr to stdout.',
        difficulty: 'VG',
        category: 'Pipes & Redirection',
        type: 'flow'
    },
    {
        id: 'mpflod-f18',
        question: 'What is the correct order for viewing then editing crontab?',
        options: [
            'Edit then view the crontab',
            'View then edit the crontab',
            'Both view and edit together',
            'Edit which shows current'
        ],
        correctIndex: 1,
        explanation: 'Best practice: crontab -l to view → crontab -e to edit.',
        difficulty: 'G',
        category: 'Systemd & Services',
        type: 'flow'
    },
    {
        id: 'mpflod-f19',
        question: 'What is the correct order for package update on Ubuntu?',
        options: [
            'Upgrade then update the lists',
            'Update lists then upgrade',
            'Install then update lists',
            'Update which also upgrades'
        ],
        correctIndex: 1,
        explanation: 'Correct order: apt update → apt upgrade. Update gets new lists, upgrade installs.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f20',
        question: 'What is the correct order for tar extraction from remote?',
        options: [
            'Extract then download the tar',
            'Download tar then extract it',
            'Stream download and extract',
            'Extract which downloads it'
        ],
        correctIndex: 2,
        explanation: 'Can pipe: curl URL | tar -xzf - extracts while downloading.',
        difficulty: 'VG',
        category: 'Arkiv & Komprimering',
        type: 'flow'
    },
    {
        id: 'mpflod-f21',
        question: 'What is the correct order for setting up Docker network?',
        options: [
            'Connect container then create',
            'Create network then connect',
            'Run which creates network',
            'Connect which creates network'
        ],
        correctIndex: 1,
        explanation: 'Correct order: docker network create → run containers with --network.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'flow'
    },
    {
        id: 'mpflod-f22',
        question: 'What is the correct order for creating symbolic link?',
        options: [
            'Create link then target file',
            'Target file then create link',
            'Link and target at same time',
            'Create link to target in cmd'
        ],
        correctIndex: 1,
        explanation: 'Target must exist first → then create symlink pointing to it.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'flow'
    },
    {
        id: 'mpflod-f23',
        question: 'What is the correct order when chaining commands with &&?',
        options: [
            'All commands run regardless',
            'Second runs only if first ok',
            'Second runs only if first fail',
            'Commands run in parallel mode'
        ],
        correctIndex: 1,
        explanation: '&& runs second command only if first succeeds (exit 0).',
        difficulty: 'G',
        category: 'Bash Scripting',
        type: 'flow'
    },
    {
        id: 'mpflod-f24',
        question: 'What is the correct order for git add and commit flow?',
        options: [
            'Commit then add the changes',
            'Add changes then commit them',
            'Add and commit at same time',
            'Commit which adds everything'
        ],
        correctIndex: 1,
        explanation: 'Correct order: git add → git commit. Stage first, then commit.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f25',
        question: 'What is the correct order for umask effect on new files?',
        options: [
            'File created then mask applied',
            'Mask applied during creation',
            'Mask applies after creation',
            'Mask only affects directories'
        ],
        correctIndex: 1,
        explanation: 'umask is applied when file is created, determining initial permissions.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'mpflod-f26',
        question: 'What is the correct order for wc counting pipeline?',
        options: [
            'Count then filter the text',
            'Filter text then count lines',
            'Count and filter together',
            'Filter which counts auto'
        ],
        correctIndex: 1,
        explanation: 'Usually: grep/filter first → wc -l to count results.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f27',
        question: 'What is the correct order for docker-compose up?',
        options: [
            'Start then build containers',
            'Build then start containers',
            'Up does build and start',
            'Start which builds needed'
        ],
        correctIndex: 2,
        explanation: 'docker-compose up builds if needed → creates → starts containers.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'flow'
    },
    {
        id: 'mpflod-f28',
        question: 'What is the correct order for journalctl log viewing?',
        options: [
            'View all then filter by unit',
            'Filter by unit for specific',
            'View then filter then view',
            'Filter which shows all too'
        ],
        correctIndex: 1,
        explanation: 'journalctl -u service shows logs for specific service unit.',
        difficulty: 'G',
        category: 'Systemd & Services',
        type: 'flow'
    },
    {
        id: 'mpflod-f29',
        question: 'What is the correct order for DNS resolution process?',
        options: [
            'Check DNS server then hosts',
            'Check /etc/hosts then DNS',
            'Check both at the same time',
            'DNS only, hosts not checked'
        ],
        correctIndex: 1,
        explanation: 'Linux checks /etc/hosts first → then DNS servers in resolv.conf.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'flow'
    },
    {
        id: 'mpflod-f30',
        question: 'What is the correct order for setting file ACL?',
        options: [
            'Apply ACL then check it now',
            'Check getfacl then setfacl',
            'Set ACL which shows result',
            'Apply and check at same time'
        ],
        correctIndex: 1,
        explanation: 'Best practice: getfacl to view → setfacl to modify → getfacl to verify.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'mpflod-f31',
        question: 'What is the correct order for xargs processing?',
        options: [
            'Execute then receive input',
            'Receive input then execute',
            'Execute as input arrives',
            'Buffer all then execute'
        ],
        correctIndex: 1,
        explanation: 'xargs reads input (from pipe) → builds and executes commands.',
        difficulty: 'VG',
        category: 'Pipes & Redirection',
        type: 'flow'
    },
    {
        id: 'mpflod-f32',
        question: 'What is the correct order for awk field processing?',
        options: [
            'Process then read each line',
            'Read line then process fields',
            'Process all then output it',
            'Read all then process once'
        ],
        correctIndex: 1,
        explanation: 'awk reads line by line → splits into fields → processes → outputs.',
        difficulty: 'VG',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f33',
        question: 'What is the correct order for adding user to group?',
        options: [
            'Add to group then create user',
            'Create user then add to group',
            'Both happen at same time',
            'Group added when user logs'
        ],
        correctIndex: 1,
        explanation: 'Correct order: useradd creates user → usermod -aG adds to group.',
        difficulty: 'G',
        category: 'Användarhantering',
        type: 'flow'
    },
    {
        id: 'mpflod-f34',
        question: 'What is the correct order for sed substitution?',
        options: [
            'Output then read then replace',
            'Read then replace then output',
            'Replace in all lines at once',
            'Output while reading input'
        ],
        correctIndex: 1,
        explanation: 'sed reads line → applies substitution → outputs modified line.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f35',
        question: 'What is the correct order for checking service status?',
        options: [
            'Check logs then check status',
            'Check status then check logs',
            'Both checked at the same time',
            'Status includes all log info'
        ],
        correctIndex: 1,
        explanation: 'Usually: systemctl status → journalctl for more details.',
        difficulty: 'G',
        category: 'Systemd & Services',
        type: 'flow'
    },
    {
        id: 'mpflod-f36',
        question: 'What is the correct order for tee command processing?',
        options: [
            'Write file then pass through',
            'Pass through and write file',
            'Write only without passing',
            'Pass only without writing'
        ],
        correctIndex: 1,
        explanation: 'tee writes to file AND passes through to stdout simultaneously.',
        difficulty: 'G',
        category: 'Pipes & Redirection',
        type: 'flow'
    },
    {
        id: 'mpflod-f37',
        question: 'What is the correct order for chmod numeric permissions?',
        options: [
            'Other then group then owner',
            'Owner then group then other',
            'Group then owner then other',
            'All three set at same time'
        ],
        correctIndex: 1,
        explanation: 'chmod 755: first digit owner, second group, third other.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'mpflod-f38',
        question: 'What is the correct order for partition and mount?',
        options: [
            'Mount then partition then fs',
            'Partition then fs then mount',
            'Fs then partition then mount',
            'Mount which partitions auto'
        ],
        correctIndex: 1,
        explanation: 'Correct order: partition → create filesystem → mount.',
        difficulty: 'G',
        category: 'Disk & Storage',
        type: 'flow'
    },
    {
        id: 'mpflod-f39',
        question: 'What is the correct order for process signal handling?',
        options: [
            'Process receives then handles',
            'Handler set then signal sent',
            'Signal sent then handler set',
            'Both happen at the same time'
        ],
        correctIndex: 0,
        explanation: 'Process receives signal → signal handler is invoked.',
        difficulty: 'G',
        category: 'Processer & Signaler',
        type: 'flow'
    },
    {
        id: 'mpflod-f40',
        question: 'What is the correct order for reverse DNS lookup?',
        options: [
            'Hostname to IP resolution',
            'IP address to hostname query',
            'Both directions at same time',
            'Hostname resolved from cache'
        ],
        correctIndex: 1,
        explanation: 'Reverse DNS: given IP address → query for hostname.',
        difficulty: 'G',
        category: 'Nätverk',
        type: 'flow'
    },
    {
        id: 'mpflod-f41',
        question: 'What is the correct order for archive extraction verification?',
        options: [
            'Extract then list contents',
            'List contents then extract',
            'List and extract together',
            'Extract which lists auto'
        ],
        correctIndex: 1,
        explanation: 'Best practice: tar -tvf to list first → tar -xvf to extract.',
        difficulty: 'G',
        category: 'Arkiv & Komprimering',
        type: 'flow'
    },
    {
        id: 'mpflod-f42',
        question: 'What is the correct order for checking then deleting file?',
        options: [
            'Delete then check if existed',
            'Check exists then delete it',
            'Delete which checks first',
            'Check and delete at same time'
        ],
        correctIndex: 1,
        explanation: 'Safe practice: test -f or ls to verify → rm to delete.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'flow'
    },
    {
        id: 'mpflod-f43',
        question: 'What is the correct order for grep with context lines?',
        options: [
            'Context shown then match line',
            'Match line then context shown',
            'Match in middle of context',
            'Context only without match'
        ],
        correctIndex: 2,
        explanation: 'grep -C shows context lines before AND after match.',
        difficulty: 'G',
        category: 'Linux Grundläggande',
        type: 'flow'
    },
    {
        id: 'mpflod-f44',
        question: 'What is the correct order for environment variable export?',
        options: [
            'Use in child then export var',
            'Set value then export to child',
            'Export which sets the value',
            'Child inherits without export'
        ],
        correctIndex: 1,
        explanation: 'Set variable → export to make available to child processes.',
        difficulty: 'G',
        category: 'Bash Scripting',
        type: 'flow'
    },
    {
        id: 'mpflod-f45',
        question: 'What is the correct order for docker volume data persistence?',
        options: [
            'Data written then volume mount',
            'Volume mount then data written',
            'Data persists without volume',
            'Volume created after writing'
        ],
        correctIndex: 1,
        explanation: 'Volume must be mounted → then data written inside persists.',
        difficulty: 'G',
        category: 'Docker & Containers',
        type: 'flow'
    },
    {
        id: 'mpflod-f46',
        question: 'What is the correct order for find with type filter?',
        options: [
            'Type filter applied at end',
            'Type filter applied first',
            'Type filter during search',
            'Type filter after results'
        ],
        correctIndex: 2,
        explanation: 'find applies -type during traversal to filter results.',
        difficulty: 'G',
        category: 'Filer & Kataloger',
        type: 'flow'
    },
    {
        id: 'mpflod-f47',
        question: 'What is the correct order for password hash verification?',
        options: [
            'Hash stored then input hashed',
            'Input hashed then compared',
            'Compare then hash the input',
            'Hash and compare at once'
        ],
        correctIndex: 1,
        explanation: 'User input is hashed → compared with stored hash.',
        difficulty: 'VG',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'mpflod-f48',
        question: 'What is the correct order for cron job execution?',
        options: [
            'Job runs then schedule check',
            'Schedule checked then job runs',
            'Job and schedule at same time',
            'Schedule ignored after first'
        ],
        correctIndex: 1,
        explanation: 'cron checks schedule → executes job when time matches.',
        difficulty: 'G',
        category: 'Systemd & Services',
        type: 'flow'
    },
    {
        id: 'mpflod-f49',
        question: 'What is the correct order for shell script execution?',
        options: [
            'Execute then parse the script',
            'Parse script then execute it',
            'Parse and execute each line',
            'Execute without any parsing'
        ],
        correctIndex: 2,
        explanation: 'Shell parses each line → executes → moves to next line.',
        difficulty: 'G',
        category: 'Bash Scripting',
        type: 'flow'
    },
    {
        id: 'mpflod-f50',
        question: 'What is the correct order for background job completion?',
        options: [
            'Job finishes then notify user',
            'Notify user then job finishes',
            'Job runs without any notice',
            'Notify before job starts up'
        ],
        correctIndex: 0,
        explanation: 'Background job runs → completes → shell notifies user.',
        difficulty: 'G',
        category: 'Processer & Signaler',
        type: 'flow'
    }
]

// Export for use in tenta-simulator
export const ALL_MANPAGE_FLODEN_QUESTIONS = MANPAGE_FLODEN_QUESTIONS

// Stats
export const MANPAGE_FLODEN_STATS = {
    totalQuestions: MANPAGE_FLODEN_QUESTIONS.length,
    scenarioQuestions: MANPAGE_FLODEN_QUESTIONS.filter(q => q.type === 'scenario').length,
    flowQuestions: MANPAGE_FLODEN_QUESTIONS.filter(q => q.type === 'flow').length,
    gQuestions: MANPAGE_FLODEN_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: MANPAGE_FLODEN_QUESTIONS.filter(q => q.difficulty === 'VG').length,
    categories: [...new Set(MANPAGE_FLODEN_QUESTIONS.map(q => q.category))]
}
