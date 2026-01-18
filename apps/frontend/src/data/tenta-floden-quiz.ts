/**
 * TENTA FLÖDEN - Scenario & Flow questions based on Linux Tenta (20 original questions)
 * All questions in English with varied correct answer positions
 * 
 * Created: 2026-01-18
 * Source: Mirrors linux-tenta-quiz.ts with scenario/flow format
 * Content: 20 scenario questions + 20 flow questions = 40 total
 */

export interface TentaFlodenQuestion {
    id: string
    question: string
    options: [string, string, string, string]
    correctIndex: 0 | 1 | 2 | 3
    explanation: string
    difficulty: 'G' | 'VG'
    category: string
    type: 'scenario' | 'flow'
}

export const TENTA_FLODEN_QUESTIONS: TentaFlodenQuestion[] = [
    // ============================================
    // SCENARIO QUESTIONS (Lisa-style) - 20 questions
    // ============================================
    {
        id: 'tentaflod-s1',
        question: 'Chrille claims /dev/sda1 cannot be a file because it is a disk. He says devices and files are different things. What is correct about Linux philosophy?',
        options: [
            'Chrille is right, devices are separate',
            'Only text documents count as files',
            'In Linux everything is treated as file',
            'Devices use a different system layer'
        ],
        correctIndex: 2,
        explanation: 'In Linux, everything is represented as a file - regular files, directories, devices, sockets, etc. This is a fundamental Unix/Linux design philosophy.',
        difficulty: 'G',
        category: 'Linux Philosophy',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s2',
        question: 'You added a new SSD to your server. Your manager asks about the correct order for setting up encrypted storage. What sequence is correct?',
        options: [
            'LUKS encrypt then create partition',
            'Create filesystem before partitioning',
            'Partition then LUKS then filesystem',
            'Filesystem then block device then LUKS'
        ],
        correctIndex: 2,
        explanation: 'Correct order: Block device exists → create partition → LUKS encrypt the partition → create filesystem on the encrypted volume.',
        difficulty: 'VG',
        category: 'Block Storage & Encryption',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s3',
        question: 'Axel needs to calculate usable hosts for a /27 network. She asks you how many hosts can actually be assigned IP addresses.',
        options: [
            'Exactly 32 hosts can be assigned',
            '30 hosts after network and broadcast',
            '16 hosts due to subnet division',
            '62 hosts using full address space'
        ],
        correctIndex: 1,
        explanation: '/27 = 32-27 = 5 host bits. 2^5 = 32 addresses, minus 2 (network address + broadcast) = 30 usable hosts.',
        difficulty: 'VG',
        category: 'Subnetting',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s4',
        question: 'Levie wants to connect to another servers localhost for debugging. She asks if this is possible using network configuration.',
        options: [
            'Add entry in the /etc/hosts file',
            'Modify files in /etc/netplan folder',
            'Open listening socket on the target',
            'It is not possible by definition'
        ],
        correctIndex: 3,
        explanation: 'localhost (127.0.0.1) is by definition only accessible on the local machine. You cannot access another machines localhost directly.',
        difficulty: 'G',
        category: 'Network',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s5',
        question: 'Said asks what DNS actually does. She thinks it converts IP addresses to hostnames. What is the correct explanation?',
        options: [
            'Protocol for secure file transfers',
            'Firewall configuration service type',
            'Translates hostnames to IP addresses',
            'Converts IP addresses to hostnames'
        ],
        correctIndex: 2,
        explanation: 'DNS (Domain Name System) translates hostnames (e.g., google.com) to IP addresses (e.g., 142.250.74.14).',
        difficulty: 'G',
        category: 'DNS',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s6',
        question: 'Your team lead asks what Bash stands for during a quiz. Some say Better Ask Shell Help. What is the correct expansion?',
        options: [
            'Better than Any other SHell type',
            'Bourne Again SHell from GNU project',
            'Building Advanced Scripts Handler',
            'Basic Advanced Shell for Humans'
        ],
        correctIndex: 1,
        explanation: 'Bash = Bourne Again SHell, an improved version of the original Bourne Shell (sh), developed by GNU.',
        difficulty: 'G',
        category: 'Bash',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s7',
        question: 'Mika wrote cat logfile.txt > grep error and wonders why it fails. What operator should connect these two commands?',
        options: [
            'Use > to redirect output stream',
            'Use >> to append the output data',
            'Use 2>&1 to combine both streams',
            'Use | to pipe output as input'
        ],
        correctIndex: 3,
        explanation: 'The pipe operator | sends stdout from one command as stdin to the next. Example: cat logfile.txt | grep error.',
        difficulty: 'G',
        category: 'Bash',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s8',
        question: 'You are writing a script to process CLI arguments one by one, removing each after processing. Which command achieves this?',
        options: [
            'Use case for pattern matching',
            'Use grep to filter arguments',
            'Use shift to remove first arg',
            'Use sed to edit argument list'
        ],
        correctIndex: 2,
        explanation: 'shift moves positional parameters ($1, $2, etc.) one step left, removing $1 and allowing iteration through all arguments.',
        difficulty: 'VG',
        category: 'Bash Scripting',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s9',
        question: 'Levie tells a customer that Docker containers are small virtual machines. You need to correct her diplomatically. What is technically accurate?',
        options: [
            'A container is an isolated process',
            'Levie is right they are small VMs',
            'Containers and VMs are identical',
            'A container is an advanced script'
        ],
        correctIndex: 0,
        explanation: 'A Docker container is an isolated process running in its own namespace with limited resources. It is NOT a virtual machine.',
        difficulty: 'G',
        category: 'Docker',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s10',
        question: 'Chrille asks about the two types of Docker volumes. He thinks there are isolated and shared volumes. What are the correct types?',
        options: [
            'Only one type of volume exists',
            'Unbound volumes and unnamed ones',
            'Isolated volumes and shared volumes',
            'Bind volumes and named volumes'
        ],
        correctIndex: 3,
        explanation: 'Docker has bind volumes (maps a host directory) and named volumes (managed by Docker in /var/lib/docker/volumes).',
        difficulty: 'G',
        category: 'Docker',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s11',
        question: 'During an exam review, you need to identify which is NOT an IPC method in Unix. The options include pipes, signals, methods, and sockets.',
        options: [
            'Pipes are not an IPC method',
            'Methods is not an IPC method',
            'Signals are not an IPC method',
            'Sockets are not an IPC method'
        ],
        correctIndex: 1,
        explanation: 'The three main IPC methods in Unix are: pipes (|), sockets (network communication), and signals (e.g., SIGTERM, SIGKILL). Methods is not an IPC method.',
        difficulty: 'VG',
        category: 'IPC',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s12',
        question: 'Your manager asks about the 3-2-1 backup rule. Specifically, what does the number 2 represent in this strategy?',
        options: [
            'Make at least 2 copies of data',
            'Wait 2 hours between each backup',
            'Use at least 2 different media',
            'Store data in 2 different places'
        ],
        correctIndex: 2,
        explanation: '3-2-1 rule: 3 copies of data, 2 different media types (e.g., SSD and tape), 1 off-site backup. The 2 represents different media types.',
        difficulty: 'G',
        category: 'Backup',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s13',
        question: 'Mika lists apt, yum, curl, and dnf as package managers. Which one is NOT actually a package manager?',
        options: [
            'apt is not a package manager',
            'yum is not a package manager',
            'dnf is not a package manager',
            'curl is not a package manager'
        ],
        correctIndex: 3,
        explanation: 'apt (Debian/Ubuntu), yum (older RHEL), dnf (newer RHEL/Fedora) are all package managers. curl is a data transfer tool, not package management.',
        difficulty: 'G',
        category: 'Package Management',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s14',
        question: 'Said asks what file descriptor 0 represents. She guesses it might be standard error. What is the correct answer?',
        options: [
            'File descriptor 0 is standard log',
            'File descriptor 0 is standard error',
            'File descriptor 0 is standard output',
            'File descriptor 0 is standard input'
        ],
        correctIndex: 3,
        explanation: 'The three standard streams: 0 = stdin (input), 1 = stdout (output), 2 = stderr (error). File descriptor 0 is always stdin.',
        difficulty: 'G',
        category: 'Streams',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s15',
        question: 'During a networking lecture, you need to explain IPv4 address structure. How many bits divided into how many bytes?',
        options: [
            '30 bits divided into 4 bytes total',
            '32 bits divided into 8 bytes total',
            '31 bits divided into 4 bytes total',
            '32 bits divided into 4 bytes total'
        ],
        correctIndex: 3,
        explanation: 'An IPv4 address consists of 32 bits, divided into 4 bytes (octets). Each byte is represented as a number 0-255.',
        difficulty: 'G',
        category: 'Network',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s16',
        question: 'Axel wants to check free disk space on the server. He asks which command shows remaining disk space.',
        options: [
            'The du command shows disk free',
            'The df command shows disk free',
            'The space command shows disk free',
            'The dh command shows disk free'
        ],
        correctIndex: 1,
        explanation: 'df (disk free) shows free space on mounted filesystems. du (disk usage) shows size of files/folders.',
        difficulty: 'G',
        category: 'Disk',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s17',
        question: 'Axel claims a container can access the hosts localhost directly. Is this statement true or false?',
        options: [
            'True, containers share localhost',
            'False, requires special configuration',
            'Only works on Windows platform',
            'Only with specific Docker version'
        ],
        correctIndex: 1,
        explanation: 'A container CANNOT access the hosts localhost (127.0.0.1) without special configuration (e.g., host network mode).',
        difficulty: 'G',
        category: 'Docker Network',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s18',
        question: 'Said asks if the host can access a containers localhost. What is the correct technical answer?',
        options: [
            'False, host cannot access it',
            'True, through port mapping flag',
            'Only with port mapping enabled',
            'Only on Linux host systems'
        ],
        correctIndex: 1,
        explanation: 'The host CAN access a containers localhost through port mapping (-p flag). Docker creates NAT rules for this.',
        difficulty: 'G',
        category: 'Docker Network',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s19',
        question: 'Levie needs to send a signal to terminate a process. She asks which command is used for sending signals.',
        options: [
            'Use send-signal command for this',
            'Use signal command for process',
            'Use signify command for signals',
            'Use kill command to send signal'
        ],
        correctIndex: 3,
        explanation: 'The kill command sends signals to processes. E.g., kill -9 PID (SIGKILL) or kill -15 PID (SIGTERM).',
        difficulty: 'G',
        category: 'Processes',
        type: 'scenario'
    },
    {
        id: 'tentaflod-s20',
        question: 'In bash scripting, the syntax [ ] is an alternative way to call a builtin command. What command does it represent?',
        options: [
            'It calls the check builtin cmd',
            'It calls the if builtin command',
            'It calls the evaluate command',
            'It calls the test builtin cmd'
        ],
        correctIndex: 3,
        explanation: '[ ] is a synonym for the test command in bash. E.g., [ -f file ] is the same as test -f file.',
        difficulty: 'VG',
        category: 'Bash',
        type: 'scenario'
    },

    // ============================================
    // FLOW QUESTIONS (Order-based) - 20 questions
    // ============================================
    {
        id: 'tentaflod-f1',
        question: 'What is the correct order to set up SSH key authentication from scratch?',
        options: [
            'Copy pubkey then generate keypair',
            'Test connection then set permissions',
            'Generate keypair then copy pubkey',
            'Set permissions then generate keys'
        ],
        correctIndex: 2,
        explanation: 'Correct order: Generate keypair → Copy public key to server → Set correct permissions → Test connection.',
        difficulty: 'G',
        category: 'SSH',
        type: 'flow'
    },
    {
        id: 'tentaflod-f2',
        question: 'What is the correct order when adding encrypted storage to a Linux server?',
        options: [
            'Block device then partitions then LUKS',
            'LUKS then block device then partition',
            'Filesystem then block device then LUKS',
            'Partitions then filesystem then block'
        ],
        correctIndex: 0,
        explanation: 'Correct order: Block device → Create partitions → Apply LUKS encryption → Create filesystem.',
        difficulty: 'VG',
        category: 'Block Storage & Encryption',
        type: 'flow'
    },
    {
        id: 'tentaflod-f3',
        question: 'What is the correct order for building and running a Docker container?',
        options: [
            'docker run then Dockerfile then build',
            'docker build then container then run',
            'Dockerfile then docker build then run',
            'Container runs then Dockerfile then go'
        ],
        correctIndex: 2,
        explanation: 'Correct order: Create Dockerfile → docker build → docker run → container runs.',
        difficulty: 'G',
        category: 'Docker',
        type: 'flow'
    },
    {
        id: 'tentaflod-f4',
        question: 'What is the recommended order for installing packages on Debian/Ubuntu?',
        options: [
            'apt install then apt update done',
            'apt upgrade then apt install done',
            'apt update then apt upgrade then go',
            'Verify first then apt update done'
        ],
        correctIndex: 2,
        explanation: 'Correct order: apt update → apt upgrade → apt install → verify installation.',
        difficulty: 'G',
        category: 'Package Management',
        type: 'flow'
    },
    {
        id: 'tentaflod-f5',
        question: 'What is the correct order for configuring UFW firewall securely?',
        options: [
            'ufw enable then ufw allow ssh go',
            'ufw default deny then allow ssh go',
            'ufw status then ufw enable done',
            'ufw allow ssh then ufw status go'
        ],
        correctIndex: 1,
        explanation: 'Correct order: ufw default deny → ufw allow ssh → ufw enable → ufw status to verify.',
        difficulty: 'G',
        category: 'Firewall',
        type: 'flow'
    },
    {
        id: 'tentaflod-f6',
        question: 'What is the correct order for creating a new user with sudo access?',
        options: [
            'Create user then add to sudo group',
            'Add to group then create user done',
            'Set password then create user done',
            'Verify login then create user done'
        ],
        correctIndex: 0,
        explanation: 'Correct order: useradd/adduser → set password → add to sudo group → verify login.',
        difficulty: 'G',
        category: 'User Management',
        type: 'flow'
    },
    {
        id: 'tentaflod-f7',
        question: 'What is the correct order for troubleshooting a failed systemd service?',
        options: [
            'Restart service then check status go',
            'Check logs then check status first',
            'Check status then check logs next',
            'Edit config then restart service go'
        ],
        correctIndex: 2,
        explanation: 'Correct order: systemctl status → journalctl -u service → fix issue → restart service.',
        difficulty: 'VG',
        category: 'Systemd',
        type: 'flow'
    },
    {
        id: 'tentaflod-f8',
        question: 'What is the correct order for creating a compressed archive with tar?',
        options: [
            'Compress files then create archive go',
            'Create archive then add compression',
            'Add files then compress then archive',
            'Archive and compress in single cmd'
        ],
        correctIndex: 3,
        explanation: 'With tar -czvf: create archive + gzip compression + verbose + filename - all in one command.',
        difficulty: 'G',
        category: 'Archive & Compression',
        type: 'flow'
    },
    {
        id: 'tentaflod-f9',
        question: 'What is the correct order for mounting a new disk partition?',
        options: [
            'Mount then create filesystem then go',
            'Create filesystem then mount it go',
            'Partition then mount then filesystem',
            'Mount then partition then filesystem'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Create partition → Create filesystem (mkfs) → Create mount point → Mount the partition.',
        difficulty: 'VG',
        category: 'Disk & Storage',
        type: 'flow'
    },
    {
        id: 'tentaflod-f10',
        question: 'What is the correct order for safely terminating a process?',
        options: [
            'Send SIGKILL then SIGTERM signal',
            'Send SIGTERM then SIGKILL if need',
            'Check process then send SIGKILL go',
            'Send SIGSTOP then SIGKILL signal'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Try SIGTERM first (allows cleanup) → Wait → Use SIGKILL only if SIGTERM fails.',
        difficulty: 'G',
        category: 'Processes & Signals',
        type: 'flow'
    },
    {
        id: 'tentaflod-f11',
        question: 'What is the correct order for setting up a Docker volume for persistence?',
        options: [
            'Run container then create volume go',
            'Create volume then mount in run cmd',
            'Mount volume then create volume go',
            'Start container then add volume go'
        ],
        correctIndex: 1,
        explanation: 'Correct order: Create volume (docker volume create) → Mount volume when running container (-v flag).',
        difficulty: 'G',
        category: 'Docker',
        type: 'flow'
    },
    {
        id: 'tentaflod-f12',
        question: 'What is the correct order for DNS resolution on a Linux system?',
        options: [
            'Check /etc/hosts then query DNS go',
            'Query DNS server then check hosts',
            'Check cache then query DNS server',
            'Query DNS then check /etc/hosts go'
        ],
        correctIndex: 0,
        explanation: 'Linux checks /etc/hosts first, then queries DNS servers defined in /etc/resolv.conf.',
        difficulty: 'G',
        category: 'DNS',
        type: 'flow'
    },
    {
        id: 'tentaflod-f13',
        question: 'What is the correct order for pipe data processing in bash?',
        options: [
            'Output goes to next cmd as input',
            'Input goes to prev cmd as output',
            'Commands run then output merges go',
            'Output saved then read by next go'
        ],
        correctIndex: 0,
        explanation: 'Pipes: stdout from first command becomes stdin for next command, processed left to right.',
        difficulty: 'G',
        category: 'Bash',
        type: 'flow'
    },
    {
        id: 'tentaflod-f14',
        question: 'What is the correct order for checking network connectivity issues?',
        options: [
            'Check DNS then ping gateway first',
            'Ping localhost then gateway then DNS',
            'Check gateway then ping localhost',
            'Check DNS then localhost then gate'
        ],
        correctIndex: 1,
        explanation: 'Correct order: ping localhost → ping gateway → ping external IP → test DNS resolution.',
        difficulty: 'VG',
        category: 'Network',
        type: 'flow'
    },
    {
        id: 'tentaflod-f15',
        question: 'What is the correct order for permission checking on a file access?',
        options: [
            'Check group then user then other go',
            'Check other then group then user go',
            'Check user then group then other go',
            'Check all permissions at same time'
        ],
        correctIndex: 2,
        explanation: 'Linux checks: Is user owner? → Is user in group? → Apply other permissions. First match wins.',
        difficulty: 'G',
        category: 'Permissions',
        type: 'flow'
    },
    {
        id: 'tentaflod-f16',
        question: 'What is the correct order for systemd service startup at boot?',
        options: [
            'Start service then enable at boot',
            'Enable at boot then start service',
            'Enable at boot to start it now go',
            'Start now which also enables it'
        ],
        correctIndex: 1,
        explanation: 'Enable creates symlink for boot start, Start runs it now. Usually: enable then start, or enable --now.',
        difficulty: 'G',
        category: 'Systemd',
        type: 'flow'
    },
    {
        id: 'tentaflod-f17',
        question: 'What is the correct order when a bash script argument is processed with shift?',
        options: [
            '$2 becomes $1 after shift command',
            '$1 becomes $0 after shift command',
            '$0 becomes $1 after shift command',
            'All arguments are cleared by shift'
        ],
        correctIndex: 0,
        explanation: 'shift removes $1 and moves all other positional parameters down: $2 becomes $1, $3 becomes $2, etc.',
        difficulty: 'VG',
        category: 'Bash Scripting',
        type: 'flow'
    },
    {
        id: 'tentaflod-f18',
        question: 'What is the correct order for extracting a .tar.gz archive?',
        options: [
            'Decompress gzip then extract tar go',
            'Extract tar then decompress gzip go',
            'Both operations happen together go',
            'Decompress only without extracting'
        ],
        correctIndex: 2,
        explanation: 'tar -xzf handles both: -z decompresses gzip, -x extracts tar - done simultaneously in one command.',
        difficulty: 'G',
        category: 'Archive & Compression',
        type: 'flow'
    },
    {
        id: 'tentaflod-f19',
        question: 'What is the correct order for container lifecycle from image to running state?',
        options: [
            'Create container then pull image go',
            'Pull image then create then start go',
            'Start container then pull image go',
            'Run which pulls creates and starts'
        ],
        correctIndex: 3,
        explanation: 'docker run: pulls image if needed → creates container → starts container - all in one command.',
        difficulty: 'G',
        category: 'Docker',
        type: 'flow'
    },
    {
        id: 'tentaflod-f20',
        question: 'What is the correct order for implementing the 3-2-1 backup strategy?',
        options: [
            '3 copies then 2 media then offsite',
            '2 media then 3 copies then offsite',
            '1 offsite then 3 copies then media',
            'Offsite then media then copies done'
        ],
        correctIndex: 0,
        explanation: '3-2-1: Create 3 copies → Store on 2 different media types → Keep 1 copy offsite.',
        difficulty: 'G',
        category: 'Backup',
        type: 'flow'
    }
]

// Export for use in tenta-simulator
export const ALL_TENTA_FLODEN_QUESTIONS = TENTA_FLODEN_QUESTIONS

// Stats
export const TENTA_FLODEN_STATS = {
    totalQuestions: TENTA_FLODEN_QUESTIONS.length,
    scenarioQuestions: TENTA_FLODEN_QUESTIONS.filter(q => q.type === 'scenario').length,
    flowQuestions: TENTA_FLODEN_QUESTIONS.filter(q => q.type === 'flow').length,
    gQuestions: TENTA_FLODEN_QUESTIONS.filter(q => q.difficulty === 'G').length,
    vgQuestions: TENTA_FLODEN_QUESTIONS.filter(q => q.difficulty === 'VG').length,
    categories: [...new Set(TENTA_FLODEN_QUESTIONS.map(q => q.category))]
}
