/**
 * OMTENTA V2 - Pakethantering & Bash (110 frågor)
 * EXAKT spegling av Omtenta/Pakethantering_Bash_Quiz_110.md
 */

import { OmtentaV2Question } from './omtenta-v2-ssh-brandvagg'

export const PAKETHANTERING_BASH_V2_QUESTIONS: OmtentaV2Question[] = [
    {
        id: 'omtenta-v2-bash-1',
        question: 'Bash stands for...',
        options: ['Basic Shell', 'Bourne Again Shell', 'Better Advanced Shell', 'Binary Access Shell'],
        correctIndices: [1],
        explanation: 'Bash = Bourne Again Shell.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-2',
        question: 'The first line of a bash script is called...',
        options: ['Header', 'Shebang', 'Hashbang', 'Scriptline'],
        correctIndices: [1],
        explanation: 'Shebang är första raden som anger interpreter.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-3',
        question: 'The shebang for bash is...',
        options: ['#bash', '#!/bash', '#!/bin/bash', '#/bin/bash'],
        correctIndices: [2],
        explanation: '#!/bin/bash är korrekt shebang.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-4',
        question: 'To make a script executable, use...',
        options: ['chmod 644', 'chmod run', 'chmod +x', 'chmod exec'],
        correctIndices: [2],
        explanation: 'chmod +x gör scriptet körbart.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-5',
        question: '$0 in bash refers to...',
        options: ['First argument', 'Script name', 'Exit code', 'Process ID'],
        correctIndices: [1],
        explanation: '$0 är scriptets namn.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-6',
        question: '$1 in bash refers to...',
        options: ['Script name', 'First argument', 'Exit code', 'Process ID'],
        correctIndices: [1],
        explanation: '$1 är första argumentet.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-7',
        question: '$# in bash refers to...',
        options: ['Process ID', 'Exit code', 'Number of arguments', 'Script name'],
        correctIndices: [2],
        explanation: '$# är antalet argument.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-8',
        question: '$? in bash refers to...',
        options: ['Process ID', 'Exit code of last command', 'Number of arguments', 'Script name'],
        correctIndices: [1],
        explanation: '$? är exit-kod från senaste kommando.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-9',
        question: '$$ in bash refers to...',
        options: ['Exit code', 'Current process ID', 'Parent process ID', 'Last argument'],
        correctIndices: [1],
        explanation: '$$ är aktuell process-ID.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-10',
        question: '$@ in bash refers to...',
        options: ['First argument', 'All arguments', 'Last argument', 'Number of arguments'],
        correctIndices: [1],
        explanation: '$@ är alla argument.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-11',
        question: 'Exit code 0 means...',
        options: ['Error', 'Success', 'Warning', 'Undefined'],
        correctIndices: [1],
        explanation: 'Exit 0 = success.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-12',
        question: 'Non-zero exit code means...',
        options: ['Success', 'Error/failure', 'Warning', 'Running'],
        correctIndices: [1],
        explanation: 'Icke-noll exit-kod = fel.',
        difficulty: 'G',
        category: 'Bash Grundläggande',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-13',
        question: 'File descriptor 0 is...',
        options: ['stdout', 'stderr', 'stdin', 'stdlog'],
        correctIndices: [2],
        explanation: 'File descriptor 0 = stdin.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-14',
        question: 'File descriptor 1 is...',
        options: ['stdin', 'stderr', 'stdout', 'stdlog'],
        correctIndices: [2],
        explanation: 'File descriptor 1 = stdout.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-15',
        question: 'File descriptor 2 is...',
        options: ['stdin', 'stdout', 'stderr', 'stdlog'],
        correctIndices: [2],
        explanation: 'File descriptor 2 = stderr.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-16',
        question: 'To redirect stdout to file, use...',
        options: ['<', '>', '2>', '|'],
        correctIndices: [1],
        explanation: '> redirectar stdout till fil.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-17',
        question: 'To redirect stderr to file, use...',
        options: ['>', '<', '2>', '|'],
        correctIndices: [2],
        explanation: '2> redirectar stderr till fil.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-18',
        question: 'To redirect both stdout and stderr, use...',
        options: ['>', '2>', '&>', '|'],
        correctIndices: [2],
        explanation: '&> redirectar både stdout och stderr.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-19',
        question: 'To append to file, use...',
        options: ['>', '>>', '>>>', '+>'],
        correctIndices: [1],
        explanation: '>> appendar till fil.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-20',
        question: 'To pipe output to another command, use...',
        options: ['>', '>>', '|', '&'],
        correctIndices: [2],
        explanation: '| pipar output till nästa kommando.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-21',
        question: 'Select all valid IPC methods (choose 5):',
        options: ['Pipes', 'Cables', 'Signals', 'Wires', 'Sockets', 'Plugs', 'Shared memory', 'Joint memory', 'Message queues', 'Mail queues'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'IPC-metoder: Pipes, Signals, Sockets, Shared memory, Message queues.',
        difficulty: 'VG',
        category: 'IPC',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-22',
        question: 'The command to send signal is...',
        options: ['signal', 'send', 'kill', 'terminate'],
        correctIndices: [2],
        explanation: 'kill skickar signaler till processer.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-23',
        question: 'SIGTERM signal number is...',
        options: ['1', '9', '15', '19'],
        correctIndices: [2],
        explanation: 'SIGTERM = 15.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-24',
        question: 'SIGKILL signal number is...',
        options: ['1', '9', '15', '19'],
        correctIndices: [1],
        explanation: 'SIGKILL = 9.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-25',
        question: 'SIGHUP signal number is...',
        options: ['1', '9', '15', '19'],
        correctIndices: [0],
        explanation: 'SIGHUP = 1.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-26',
        question: 'SIGINT signal number is...',
        options: ['1', '2', '9', '15'],
        correctIndices: [1],
        explanation: 'SIGINT = 2.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-27',
        question: 'Ctrl+C sends...',
        options: ['SIGTERM', 'SIGKILL', 'SIGINT', 'SIGHUP'],
        correctIndices: [2],
        explanation: 'Ctrl+C skickar SIGINT.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-28',
        question: 'Ctrl+Z sends...',
        options: ['SIGINT', 'SIGTERM', 'SIGTSTP', 'SIGKILL'],
        correctIndices: [2],
        explanation: 'Ctrl+Z skickar SIGTSTP (stop).',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-29',
        question: 'kill -9 sends...',
        options: ['SIGTERM', 'SIGKILL', 'SIGINT', 'SIGHUP'],
        correctIndices: [1],
        explanation: 'kill -9 skickar SIGKILL.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-30',
        question: 'SIGKILL can be caught/ignored?',
        options: ['Yes', 'No'],
        correctIndices: [1],
        explanation: 'SIGKILL kan inte fångas eller ignoreras.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-31',
        question: 'SIGTERM can be caught/ignored?',
        options: ['Yes', 'No'],
        correctIndices: [0],
        explanation: 'SIGTERM kan fångas och hanteras.',
        difficulty: 'G',
        category: 'Signaler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-32',
        question: 'To run command in background, add...',
        options: ['#', '@', '&', '%'],
        correctIndices: [2],
        explanation: '& kör kommando i bakgrunden.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-33',
        question: 'To bring job to foreground, use...',
        options: ['front', 'bring', 'fg', 'fore'],
        correctIndices: [2],
        explanation: 'fg tar jobb till förgrunden.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-34',
        question: 'To send job to background, use...',
        options: ['back', 'send', 'bg', 'behind'],
        correctIndices: [2],
        explanation: 'bg skickar jobb till bakgrunden.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-35',
        question: 'To list background jobs, use...',
        options: ['list', 'ps', 'jobs', 'back'],
        correctIndices: [2],
        explanation: 'jobs listar bakgrundsjobb.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-36',
        question: 'To disown a job from terminal, use...',
        options: ['release', 'free', 'disown', 'detach'],
        correctIndices: [2],
        explanation: 'disown frigör jobb från terminalen.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-37',
        question: 'nohup is used to...',
        options: ['Stop a process', 'Run immune to hangup', 'No help available', 'Network operation'],
        correctIndices: [1],
        explanation: 'nohup kör process immun mot hangup.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-38',
        question: 'The test command is same as...',
        options: ['( )', '{ }', '[ ]', '< >'],
        correctIndices: [2],
        explanation: '[ ] är samma som test-kommandot.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-39',
        question: 'In if statement, -eq means...',
        options: ['Not equal', 'Equal (numbers)', 'Equal (strings)', 'Empty'],
        correctIndices: [1],
        explanation: '-eq testar numerisk likhet.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-40',
        question: 'In if statement, -ne means...',
        options: ['New', 'Not equal (numbers)', 'Negative', 'Never'],
        correctIndices: [1],
        explanation: '-ne testar numerisk olikhet.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-41',
        question: 'In if statement, -gt means...',
        options: ['Get', 'Good', 'Greater than', 'Go to'],
        correctIndices: [2],
        explanation: '-gt testar större än.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-42',
        question: 'In if statement, -lt means...',
        options: ['Let', 'List', 'Less than', 'Letter'],
        correctIndices: [2],
        explanation: '-lt testar mindre än.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-43',
        question: 'In if statement, -f tests if...',
        options: ['File is directory', 'File exists and is regular file', 'File is empty', 'File is link'],
        correctIndices: [1],
        explanation: '-f testar om fil existerar och är vanlig fil.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-44',
        question: 'In if statement, -d tests if...',
        options: ['File is deleted', 'Path is directory', 'File is disk', 'File is device'],
        correctIndices: [1],
        explanation: '-d testar om sökväg är katalog.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-45',
        question: 'In if statement, -e tests if...',
        options: ['File is empty', 'File is executable', 'File exists', 'File has errors'],
        correctIndices: [2],
        explanation: '-e testar om fil existerar.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-46',
        question: 'In if statement, -z tests if...',
        options: ['String is not empty', 'String is zero length (empty)', 'String has zeros', 'String is zipped'],
        correctIndices: [1],
        explanation: '-z testar om sträng är tom.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-47',
        question: 'In if statement, -n tests if...',
        options: ['String is not empty', 'String is empty', 'String is null', 'String is new'],
        correctIndices: [0],
        explanation: '-n testar om sträng INTE är tom.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-48',
        question: 'For string equality, use...',
        options: ['-eq', '= or ==', '-se', 'equals'],
        correctIndices: [1],
        explanation: '= eller == för stränglikhet.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-49',
        question: 'For string inequality, use...',
        options: ['-ne', '!=', '-sne', 'notequals'],
        correctIndices: [1],
        explanation: '!= för strängolikhet.',
        difficulty: 'G',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-50',
        question: 'Select all valid test operators (choose 5):',
        options: ['-f', '-file', '-d', '-dir', '-e', '-exist', '-r', '-read', '-w', '-write'],
        correctIndices: [0, 2, 4, 6, 8],
        explanation: 'Giltiga testoperatorer: -f, -d, -e, -r, -w.',
        difficulty: 'VG',
        category: 'Bash Test',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-51',
        question: 'For loop syntax: for i in ...',
        options: ['for i in (1 2 3)', 'for i in 1 2 3', 'for i = 1 to 3', 'for (i in 1 2 3)'],
        correctIndices: [1],
        explanation: 'for i in 1 2 3 är korrekt syntax.',
        difficulty: 'G',
        category: 'Bash Loopar',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-52',
        question: 'While loop runs...',
        options: ['Once', 'Never', 'While condition is true', 'While condition is false'],
        correctIndices: [2],
        explanation: 'While kör medan villkoret är sant.',
        difficulty: 'G',
        category: 'Bash Loopar',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-53',
        question: 'Until loop runs...',
        options: ['Once', 'Never', 'While condition is true', 'Until condition is true'],
        correctIndices: [3],
        explanation: 'Until kör tills villkoret blir sant.',
        difficulty: 'G',
        category: 'Bash Loopar',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-54',
        question: 'To read input in script, use...',
        options: ['input', 'get', 'read', 'scan'],
        correctIndices: [2],
        explanation: 'read läser input.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-55',
        question: 'To read from file line by line...',
        options: ['while read line; do', 'for read line; do', 'read each line; do', 'while line in file; do'],
        correctIndices: [0],
        explanation: 'while read line; do läser rad för rad.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-56',
        question: 'case statement ends with...',
        options: ['end', 'done', 'esac', 'endcase'],
        correctIndices: [2],
        explanation: 'case avslutas med esac.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-57',
        question: 'if statement ends with...',
        options: ['end', 'done', 'fi', 'endif'],
        correctIndices: [2],
        explanation: 'if avslutas med fi.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-58',
        question: 'Function in bash is defined as...',
        options: ['def name()', 'name() { }', 'function name[]', 'func name()'],
        correctIndices: [1],
        explanation: 'name() { } definierar funktion.',
        difficulty: 'G',
        category: 'Bash Funktioner',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-59',
        question: 'Local variable in function uses...',
        options: ['var', 'my', 'local', 'private'],
        correctIndices: [2],
        explanation: 'local skapar lokal variabel.',
        difficulty: 'G',
        category: 'Bash Funktioner',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-60',
        question: 'To return value from function, use...',
        options: ['return', 'output', 'give', 'send'],
        correctIndices: [0],
        explanation: 'return returnerar värde.',
        difficulty: 'G',
        category: 'Bash Funktioner',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-61',
        question: 'Command substitution uses...',
        options: ['{command}', '[command]', '$(command)', '%command%'],
        correctIndices: [2],
        explanation: '$(command) är command substitution.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-62',
        question: 'Old style command substitution uses...',
        options: ["'command'", '"command"', '`command`', '(command)'],
        correctIndices: [2],
        explanation: 'Backticks är gamla stilen.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-63',
        question: 'Arithmetic expansion uses...',
        options: ['$(())', '$((expression))', '$[]', '#{expression}'],
        correctIndices: [1],
        explanation: '$((expression)) för aritmetik.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-64',
        question: 'To assign variable, use...',
        options: ['var = value', '$var = value', 'var=value', 'set var value'],
        correctIndices: [2],
        explanation: 'var=value (utan mellanslag).',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-65',
        question: 'To use variable value, use...',
        options: ['var', '%var%', '$var', '@var'],
        correctIndices: [2],
        explanation: '$var använder variabelns värde.',
        difficulty: 'G',
        category: 'Bash Variabler',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-66',
        question: 'Double quotes allow...',
        options: ['No expansion', 'Variable expansion', 'Glob expansion', 'Nothing special'],
        correctIndices: [1],
        explanation: 'Dubbla citattecken tillåter variabelexpansion.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-67',
        question: 'Single quotes allow...',
        options: ['Variable expansion', 'No expansion (literal)', 'Glob expansion', 'Command expansion'],
        correctIndices: [1],
        explanation: 'Enkla citattecken = literal, ingen expansion.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-68',
        question: 'apt is used on...',
        options: ['RHEL/CentOS', 'Debian/Ubuntu', 'Fedora', 'Arch'],
        correctIndices: [1],
        explanation: 'apt används på Debian/Ubuntu.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-69',
        question: 'yum/dnf is used on...',
        options: ['Debian/Ubuntu', 'RHEL/CentOS/Fedora', 'Arch', 'Alpine'],
        correctIndices: [1],
        explanation: 'yum/dnf används på RHEL/CentOS/Fedora.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-70',
        question: 'pacman is used on...',
        options: ['Debian', 'RHEL', 'Arch', 'Alpine'],
        correctIndices: [2],
        explanation: 'pacman används på Arch.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-71',
        question: 'To install package on Ubuntu...',
        options: ['apt get install', 'apt install', 'apt add', 'apt setup'],
        correctIndices: [1],
        explanation: 'apt install installerar paket.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-72',
        question: 'To update package list on Ubuntu...',
        options: ['apt refresh', 'apt update', 'apt sync', 'apt list'],
        correctIndices: [1],
        explanation: 'apt update uppdaterar paketlistan.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-73',
        question: 'To upgrade packages on Ubuntu...',
        options: ['apt update', 'apt upgrade', 'apt refresh', 'apt up'],
        correctIndices: [1],
        explanation: 'apt upgrade uppgraderar paket.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-74',
        question: 'To remove package on Ubuntu...',
        options: ['apt delete', 'apt remove', 'apt uninstall', 'apt del'],
        correctIndices: [1],
        explanation: 'apt remove tar bort paket.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-75',
        question: 'To search packages on Ubuntu...',
        options: ['apt find', 'apt lookup', 'apt search', 'apt query'],
        correctIndices: [2],
        explanation: 'apt search söker efter paket.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-76',
        question: 'Select all package managers (choose 4):',
        options: ['apt', 'get', 'yum', 'install', 'dnf', 'pkg', 'pacman', 'package', 'manager', 'repo'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Pakethanterare: apt, yum, dnf, pacman.',
        difficulty: 'VG',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-77',
        question: 'dpkg is for...',
        options: ['Debian packages (.deb)', 'RPM packages', 'Tar packages', 'All packages'],
        correctIndices: [0],
        explanation: 'dpkg hanterar .deb-filer.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-78',
        question: 'rpm is for...',
        options: ['Debian packages', 'RPM packages (.rpm)', 'Tar packages', 'All packages'],
        correctIndices: [1],
        explanation: 'rpm hanterar .rpm-filer.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-79',
        question: 'To install .deb file...',
        options: ['apt install file.deb', 'dpkg -i file.deb', 'deb install file', 'install file.deb'],
        correctIndices: [1],
        explanation: 'dpkg -i installerar .deb-fil.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-80',
        question: 'To install .rpm file...',
        options: ['yum install file.rpm', 'rpm -i file.rpm', 'rpm install file', 'install file.rpm'],
        correctIndices: [1],
        explanation: 'rpm -i installerar .rpm-fil.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-81',
        question: '/etc/apt/sources.list contains...',
        options: ['Installed packages', 'Repository URLs', 'Package cache', 'Config files'],
        correctIndices: [1],
        explanation: 'sources.list innehåller repository-URLer.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-82',
        question: 'To clean apt cache...',
        options: ['apt clear', 'apt flush', 'apt clean', 'apt remove cache'],
        correctIndices: [2],
        explanation: 'apt clean rensar cache.',
        difficulty: 'G',
        category: 'Pakethantering',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-83',
        question: 'A process is...',
        options: ['A file', 'A running program', 'A user', 'A command'],
        correctIndices: [1],
        explanation: 'En process är ett körande program.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-84',
        question: 'PID stands for...',
        options: ['Program ID', 'Process ID', 'Parent ID', 'Primary ID'],
        correctIndices: [1],
        explanation: 'PID = Process ID.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-85',
        question: 'PPID stands for...',
        options: ['Primary PID', 'Previous PID', 'Parent Process ID', 'Program PID'],
        correctIndices: [2],
        explanation: 'PPID = Parent Process ID.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-86',
        question: 'The first process (PID 1) is...',
        options: ['kernel', 'bash', 'init/systemd', 'root'],
        correctIndices: [2],
        explanation: 'PID 1 är init/systemd.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-87',
        question: 'To list processes, use...',
        options: ['proc', 'list', 'ps', 'show'],
        correctIndices: [2],
        explanation: 'ps listar processer.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-88',
        question: 'ps aux shows...',
        options: ['Only user processes', 'All processes with details', 'Only system processes', 'Process tree'],
        correctIndices: [1],
        explanation: 'ps aux visar alla processer med detaljer.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-89',
        question: 'To show process tree, use...',
        options: ['ps -tree', 'pstree', 'tree ps', 'ps --tree'],
        correctIndices: [1],
        explanation: 'pstree visar processträd.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-90',
        question: 'To monitor processes in real-time, use...',
        options: ['ps -r', 'top', 'watch ps', 'live ps'],
        correctIndices: [1],
        explanation: 'top visar processer i realtid.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-91',
        question: 'Select all process commands (choose 4):',
        options: ['ps', 'proc', 'top', 'monitor', 'kill', 'stop', 'pgrep', 'find', 'proc', 'list'],
        correctIndices: [0, 2, 4, 6],
        explanation: 'Processkommandon: ps, top, kill, pgrep.',
        difficulty: 'VG',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-92',
        question: 'pgrep finds processes by...',
        options: ['PID', 'Name', 'User', 'Memory'],
        correctIndices: [1],
        explanation: 'pgrep söker processer på namn.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-93',
        question: 'pkill kills processes by...',
        options: ['PID', 'Name', 'User', 'Memory'],
        correctIndices: [1],
        explanation: 'pkill dödar processer på namn.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-94',
        question: 'nice value ranges from...',
        options: ['0 to 100', '1 to 20', '-20 to 19', '-100 to 100'],
        correctIndices: [2],
        explanation: 'Nice-värde: -20 till 19.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-95',
        question: 'Lower nice value means...',
        options: ['Lower priority', 'Higher priority', 'Same priority', 'No priority'],
        correctIndices: [1],
        explanation: 'Lägre nice = högre prioritet.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-96',
        question: 'To change nice value of running process, use...',
        options: ['nice', 'renice', 'setnice', 'priority'],
        correctIndices: [1],
        explanation: 'renice ändrar nice på körande process.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-97',
        question: 'Zombie process is...',
        options: ['A dead process', 'Process that finished but parent didn\'t read exit status', 'A sleeping process', 'A background process'],
        correctIndices: [1],
        explanation: 'Zombie = avslutad men parent läste inte exit-status.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-98',
        question: 'Orphan process is...',
        options: ['A zombie', 'Process whose parent died', 'A sleeping process', 'A system process'],
        correctIndices: [1],
        explanation: 'Orphan = process vars parent dog.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-99',
        question: '/proc filesystem contains...',
        options: ['Procedures', 'Process information', 'Programs', 'Protocols'],
        correctIndices: [1],
        explanation: '/proc innehåller processinformation.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-100',
        question: '/proc/[pid]/cmdline contains...',
        options: ['Process ID', 'Command that started process', 'Process status', 'Process environment'],
        correctIndices: [1],
        explanation: 'cmdline innehåller kommandot som startade processen.',
        difficulty: 'G',
        category: 'Processer',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-101',
        question: 'Linux philosophy: everything is a...',
        options: ['Process', 'Command', 'File', 'User'],
        correctIndices: [2],
        explanation: 'Linux-filosofi: allt är en fil.',
        difficulty: 'G',
        category: 'Linux Filosofi',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-102',
        question: 'Linux philosophy: programs should do...',
        options: ['Many things', 'One thing well', 'Everything', 'Nothing'],
        correctIndices: [1],
        explanation: 'Program ska göra en sak bra.',
        difficulty: 'G',
        category: 'Linux Filosofi',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-103',
        question: 'Linux philosophy: programs should work with...',
        options: ['GUIs', 'Text streams', 'Binary data', 'Databases'],
        correctIndices: [1],
        explanation: 'Program ska arbeta med textströmmar.',
        difficulty: 'G',
        category: 'Linux Filosofi',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-104',
        question: 'Standard streams are stdin, stdout, and...',
        options: ['stdlog', 'stderr', 'stdfile', 'stdpipe'],
        correctIndices: [1],
        explanation: 'stdin, stdout, stderr är standardströmmar.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-105',
        question: 'Select all that are streams (choose 3):',
        options: ['stdin', 'stdinput', 'stdout', 'stdoutput', 'stderr', 'stderror', 'stdlog', 'stdfile', 'stdpipe', 'stddata'],
        correctIndices: [0, 2, 4],
        explanation: 'Strömmar: stdin, stdout, stderr.',
        difficulty: 'VG',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-106',
        question: '/dev/null is used to...',
        options: ['Store nulls', 'Discard output', 'Create nulls', 'Test nulls'],
        correctIndices: [1],
        explanation: '/dev/null kastar output.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-107',
        question: '/dev/zero outputs...',
        options: ['Nothing', 'Continuous zeros', 'Random data', 'Errors'],
        correctIndices: [1],
        explanation: '/dev/zero ger kontinuerliga nollor.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-108',
        question: '/dev/random outputs...',
        options: ['Nothing', 'Zeros', 'Random data', 'Errors'],
        correctIndices: [2],
        explanation: '/dev/random ger slumpdata.',
        difficulty: 'G',
        category: 'Bash I/O',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-109',
        question: 'Here document syntax is...',
        options: ['>EOF', '<EOF', '<<EOF', '>>>EOF'],
        correctIndices: [2],
        explanation: '<<EOF är here document.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    },
    {
        id: 'omtenta-v2-bash-110',
        question: 'Here string syntax is...',
        options: ['<string', '>string', '<<<string', '<<string'],
        correctIndices: [2],
        explanation: '<<<string är here string.',
        difficulty: 'G',
        category: 'Bash Syntax',
        topic: 'pakethantering-bash'
    }
]
