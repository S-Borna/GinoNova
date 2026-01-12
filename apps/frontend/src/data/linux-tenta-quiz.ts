/**
 * LINUX TENTAN - Originalfrågor från verklig Linux/Unix Server & Bash Programming tenta
 * 20 quiz-frågor direkt från tentamaterial
 *
 * Skapad: 2026-01-12
 * Källa: Ursprunglig tenta - Linux/Unix Server & Bash Programming
 */

export interface LinuxTentaQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    scenario?: string
}

export const LINUX_TENTA_QUESTIONS: LinuxTentaQuestion[] = [
    {
        id: 'lintenta-1',
        question: 'In Linux everything is...',
        options: ['A terminal', 'Difficult', 'A file', 'A shell'],
        correctIndex: 2,
        explanation: 'I Linux betraktas allt som en fil - vanliga filer, kataloger, enheter, sockets, etc. Detta är en grundläggande designfilosofi i Unix/Linux.',
        difficulty: 'G',
        category: 'Linux Filosofi'
    },
    {
        id: 'lintenta-2',
        question: 'I have added new storage to my linux server. In which order do I need to create everything needed for an encrypted filesystem?',
        options: [
            'Partitions -> filesystem -> block device -> LUKS encryption',
            'Block device -> partitions -> LUKS encryption -> filesystem',
            'LUKS encryption -> block device -> filesystem -> partitions',
            'LUKS encryption -> block device -> partitions -> filesystem'
        ],
        correctIndex: 1,
        explanation: 'Korrekt ordning är: Block device finns redan → skapa partition → LUKS-kryptera partitionen → skapa filesystem på den krypterade volymen.',
        difficulty: 'VG',
        category: 'Block Storage & Kryptering'
    },
    {
        id: 'lintenta-3',
        question: 'How many hosts can I have in a /27 network?',
        options: ['2⁵', '2⁵ - 2', '2⁴', '2⁶ - 2'],
        correctIndex: 1,
        explanation: '/27 = 32-27 = 5 host bits. 2⁵ = 32 adresser, minus 2 (nätverksadress + broadcast) = 30 användbara hosts.',
        difficulty: 'VG',
        category: 'Subnetting'
    },
    {
        id: 'lintenta-4',
        question: 'How can I access another machine\'s localhost?',
        options: [
            'By adding an entry to /etc/hosts',
            'It\'s not possible',
            'By creating or modifying a file in /etc/netplan/',
            'By opening a listening socket in the target machine'
        ],
        correctIndex: 1,
        explanation: 'localhost (127.0.0.1) är per definition bara tillgänglig på den lokala maskinen. Det går inte att komma åt en annan maskins localhost.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'lintenta-5',
        question: 'DNS is...',
        options: [
            'A service that translates IP addresses into hostnames',
            'A protocol for secure file transfer',
            'A service that translates hostnames into IP addresses',
            'A firewall configuration tool'
        ],
        correctIndex: 2,
        explanation: 'DNS (Domain Name System) översätter hostnames (t.ex. google.com) till IP-adresser (t.ex. 142.250.74.14).',
        difficulty: 'G',
        category: 'DNS'
    },
    {
        id: 'lintenta-6',
        question: 'Bash stands for...',
        options: [
            'Better than Any other SHell',
            'Building Advanced Scripts Hub',
            'Better Ask for Some Help',
            'Bourne Again SHell'
        ],
        correctIndex: 3,
        explanation: 'Bash = Bourne Again SHell, en förbättrad version av den ursprungliga Bourne Shell (sh).',
        difficulty: 'G',
        category: 'Bash'
    },
    {
        id: 'lintenta-7',
        question: 'To link together two processes, passing the output of one as the input for the next, we use...',
        options: ['>', '|', '>>', '2>&1'],
        correctIndex: 1,
        explanation: 'Pipe-operatorn | skickar stdout från ett kommando som stdin till nästa. T.ex. ls | grep txt.',
        difficulty: 'G',
        category: 'Bash'
    },
    {
        id: 'lintenta-8',
        question: 'I\'m writing a bash script, and I want to process the given CLI arguments one by one, removing them from the argument list as I do so. To achieve that, I use...',
        options: ['case', 'shift', 'grep', 'sed'],
        correctIndex: 1,
        explanation: 'shift flyttar positionsparametrarna ($1, $2, etc.) ett steg åt vänster, vilket tar bort $1 och gör att du kan iterera genom alla argument.',
        difficulty: 'VG',
        category: 'Bash Scripting'
    },
    {
        id: 'lintenta-9',
        question: 'A docker container is...',
        options: [
            'A kind of virtual machine',
            'An isolated process',
            'Like a variable, but global',
            'Like a script, but better'
        ],
        correctIndex: 1,
        explanation: 'En Docker container är en isolerad process som kör i sin egen namespace med begränsade resurser. Det är INTE en virtuell maskin.',
        difficulty: 'G',
        category: 'Docker'
    },
    {
        id: 'lintenta-10',
        question: 'In docker there are two types of volumes we can use...',
        options: [
            'Isolated volumes and shared volumes',
            'Bind volumes and named volumes',
            'Unbound volumes and unnamed volumes',
            'It\'s a trick question, there is only 1 kind of volumes'
        ],
        correctIndex: 1,
        explanation: 'Docker har bind volumes (mappar en host-katalog) och named volumes (hanteras av Docker i /var/lib/docker/volumes).',
        difficulty: 'G',
        category: 'Docker'
    },
    {
        id: 'lintenta-11',
        question: 'Which is NOT one of the 3 main IPC (inter-process-communication) methods in Unix?',
        options: ['Pipes', 'Signals', 'Methods', 'Sockets'],
        correctIndex: 2,
        explanation: 'De tre huvudsakliga IPC-metoderna i Unix är: pipes (|), sockets (nätverkskommunikation), och signals (t.ex. SIGTERM, SIGKILL). "Methods" är inte en IPC-metod.',
        difficulty: 'VG',
        category: 'IPC'
    },
    {
        id: 'lintenta-12',
        question: 'When defining a backup strategy, a good practice is to follow the 3-2-1 rule. What does the 2 stand for?',
        options: [
            'To make at least 2 copies of the data',
            'To use at least 2 different media',
            'To wait 2 hours between backups',
            'To store the data in at least 2 different locations'
        ],
        correctIndex: 1,
        explanation: '3-2-1 regeln: 3 kopior av data, 2 olika mediatyper (t.ex. SSD och tape), 1 off-site backup. "2" står för olika mediatyper.',
        difficulty: 'G',
        category: 'Backup'
    },
    {
        id: 'lintenta-13',
        question: 'Which one of the following commands is NOT a package manager?',
        options: ['apt', 'yum', 'curl', 'dnf'],
        correctIndex: 2,
        explanation: 'apt (Debian/Ubuntu), yum (äldre RHEL), dnf (nyare RHEL/Fedora) är alla pakethanterare. curl är ett verktyg för dataöverföring, inte pakethantering.',
        difficulty: 'G',
        category: 'Pakethantering'
    },
    {
        id: 'lintenta-14',
        question: 'What is file descriptor 0 (stdin)?',
        options: ['Standard error', 'Standard input', 'Standard output', 'Standard log'],
        correctIndex: 1,
        explanation: 'De tre standard streams: 0 = stdin (input), 1 = stdout (output), 2 = stderr (error). File descriptor 0 är alltid stdin.',
        difficulty: 'G',
        category: 'Streams'
    },
    {
        id: 'lintenta-15',
        question: 'An IPv4 address is made up of ___ bits divided into ___ bytes',
        options: ['30, 4', '32, 8', '31, 4', '32, 4'],
        correctIndex: 3,
        explanation: 'En IPv4-adress består av 32 bitar, uppdelade i 4 bytes (oktetter). Varje byte representeras som ett tal 0-255.',
        difficulty: 'G',
        category: 'Nätverk'
    },
    {
        id: 'lintenta-16',
        question: 'In a Linux system, I can use the following command to check how much space is left on my disk:',
        options: ['du', 'df', 'space', 'dh'],
        correctIndex: 1,
        explanation: 'df (disk free) visar ledigt utrymme på monterade filsystem. du (disk usage) visar storlek på filer/mappar.',
        difficulty: 'G',
        category: 'Disk'
    },
    {
        id: 'lintenta-17',
        question: 'A container can access the host\'s localhost',
        options: ['True', 'False', 'Only with special configuration', 'Only on Windows'],
        correctIndex: 1,
        explanation: 'En container kan INTE komma åt hostens localhost (127.0.0.1) utan specialkonfiguration (t.ex. host network mode).',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'lintenta-18',
        question: 'The host can access a container\'s localhost',
        options: ['False', 'True', 'Only with port mapping', 'Only on Linux'],
        correctIndex: 1,
        explanation: 'Hosten KAN komma åt en containers localhost genom port-mappning (-p flaggan). Docker skapar NAT-regler för detta.',
        difficulty: 'G',
        category: 'Docker Nätverk'
    },
    {
        id: 'lintenta-19',
        question: 'To send a signal to a process, I can use the following command:',
        options: ['send-signal', 'signal', 'kill', 'signify'],
        correctIndex: 2,
        explanation: 'kill-kommandot skickar signaler till processer. T.ex. kill -9 PID (SIGKILL) eller kill -15 PID (SIGTERM).',
        difficulty: 'G',
        category: 'Processer'
    },
    {
        id: 'lintenta-20',
        question: 'In bash, the syntax [ ] is an alternative way to call a shell builtin command. What is the command called?',
        options: ['check', 'if', 'test', 'evaluate'],
        correctIndex: 2,
        explanation: '[ ] är en synonym för test-kommandot i bash. T.ex. [ -f file ] är samma som test -f file.',
        difficulty: 'VG',
        category: 'Bash'
    }
]

// Export for use in tenta-simulator
export const ALL_LINUX_TENTA_QUESTIONS = LINUX_TENTA_QUESTIONS

// Stats
export const LINUX_TENTA_STATS = {
    totalQuestions: LINUX_TENTA_QUESTIONS.length,
    gQuestions: LINUX_TENTA_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: LINUX_TENTA_QUESTIONS.filter(q => q.difficulty === 'VG').length,
    categories: [...new Set(LINUX_TENTA_QUESTIONS.map(q => q.category))]
}
