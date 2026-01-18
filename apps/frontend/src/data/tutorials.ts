/**
 * YouTube Tutorial Database
 * =========================
 * Curerade kvalitets-tutorials för DevOps/Linux-ämnen.
 * Dallas använder denna för att rekommendera relevanta videos.
 * 
 * Alla tutorials är manuellt verifierade för kvalitet.
 */

export interface Tutorial {
  id: string
  title: string
  youtubeId: string
  creator: string
  duration: string // "MM:SS" format
  topics: string[] // Sökbara ämnesord
  modules: string[] // Koppling till plattformens moduler
  difficulty: 'beginner' | 'intermediate' | 'advanced'
  language: 'en' | 'sv'
  description: string
  verified: boolean // Dallas-curerad
}

export interface TutorialCreator {
  name: string
  channel: string
  specialty: string[]
  trusted: boolean
}

// Betrodda creators för DevOps/Linux-tutorials
export const TRUSTED_CREATORS: TutorialCreator[] = [
  // === TIER 1: GULDSTANDARD ===
  {
    name: "NetworkChuck",
    channel: "UCO50cNkYbKwfgV3VQlmqmtw",
    specialty: ["linux", "networking", "docker", "kubernetes", "security"],
    trusted: true
  },
  {
    name: "TechWorld with Nana",
    channel: "UCdngmbVKX1Tgre699-XLlUA",
    specialty: ["devops", "docker", "kubernetes", "ci-cd", "terraform"],
    trusted: true
  },
  {
    name: "Learn Linux TV",
    channel: "UCxQKHvKbmSzGMvUrVtJYnUA",
    specialty: ["linux", "ubuntu", "server-admin", "bash", "systemd"],
    trusted: true
  },
  {
    name: "freeCodeCamp",
    channel: "UC8butISFwT-Wl7EV0hUK0BQ",
    specialty: ["linux", "docker", "git", "python", "devops"],
    trusted: true
  },
  // === TIER 2: BRA KOMPLEMENT ===
  {
    name: "Chris Titus Tech",
    channel: "UCg6gPGh8HU2U01vaFCAsvmQ",
    specialty: ["linux", "windows", "tips", "automation", "desktop"],
    trusted: true
  },
  {
    name: "Fireship",
    channel: "UCsBjURrPoezykLs9EqgamOA",
    specialty: ["docker", "kubernetes", "cloud", "devops-concepts"],
    trusted: true
  },
  {
    name: "The Linux Experiment",
    channel: "UC5UAwBUum7CPN5buc-_N1Fw",
    specialty: ["linux", "desktop", "distros", "news"],
    trusted: true
  },
  {
    name: "tutoriaLinux",
    channel: "UCvA_wgsX6eFAOXI8Rbg_WiQ",
    specialty: ["linux", "sysadmin", "bash", "automation"],
    trusted: true
  },
  // === TIER 3: OFFICIELLA KANALER ===
  {
    name: "The Linux Foundation",
    channel: "UCfX55Sx5hEFjoC3cNs6mCUQ",
    specialty: ["linux", "kernel", "enterprise", "certifications"],
    trusted: true
  },
  {
    name: "Red Hat",
    channel: "UCPZwEbsiWzMTi9sLEE9xOxg",
    specialty: ["rhel", "ansible", "openshift", "enterprise"],
    trusted: true
  },
  {
    name: "Docker",
    channel: "UC76AVf2JkrwjxNKMuPpscHQ",
    specialty: ["docker", "containers", "compose", "official"],
    trusted: true
  }
]

// Curerade tutorials - alla verifierade och relevanta
export const TUTORIALS: Tutorial[] = [
  // ============================================
  // LINUX BASICS
  // ============================================
  {
    id: "linux-basics-1",
    title: "Linux for Hackers (and everyone) // FREE Course for Beginners",
    youtubeId: "VbEx7B_PTOE",
    creator: "NetworkChuck",
    duration: "3:41:52",
    topics: ["linux", "basics", "terminal", "commands", "bash", "beginners"],
    modules: ["linux-basics", "linux-mastery"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett nybörjarkurs i Linux - från installation till avancerade kommandon",
    verified: true
  },
  {
    id: "linux-basics-2", 
    title: "Linux Directories Explained in 100 Seconds",
    youtubeId: "42iQKuQodW4",
    creator: "Fireship",
    duration: "2:22",
    topics: ["linux", "filesystem", "directories", "fhs", "structure"],
    modules: ["linux-basics", "linux-filesystem"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb översikt av Linux-filsystemets struktur",
    verified: true
  },
  
  // ============================================
  // FILE PERMISSIONS
  // ============================================
  {
    id: "permissions-1",
    title: "Linux File Permissions in 5 Minutes",
    youtubeId: "D-VqgvBMV7g",
    creator: "tutoriaLinux",
    duration: "5:37",
    topics: ["permissions", "chmod", "chown", "rwx", "file-permissions", "linux"],
    modules: ["linux-permissions", "security-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb och tydlig förklaring av Linux filrättigheter",
    verified: true
  },
  {
    id: "permissions-2",
    title: "Linux Permissions | chmod, chown, chgrp",
    youtubeId: "ngJG6Ix5FR4",
    creator: "Learn Linux TV",
    duration: "18:12",
    topics: ["permissions", "chmod", "chown", "chgrp", "octal", "symbolic"],
    modules: ["linux-permissions"],
    difficulty: "beginner",
    language: "en",
    description: "Djupgående genomgång av chmod, chown och chgrp",
    verified: true
  },

  // ============================================
  // DOCKER
  // ============================================
  {
    id: "docker-1",
    title: "Docker Tutorial for Beginners [FULL COURSE in 3 Hours]",
    youtubeId: "3c-iBn73dDE",
    creator: "TechWorld with Nana",
    duration: "2:46:14",
    topics: ["docker", "containers", "images", "dockerfile", "compose", "devops"],
    modules: ["docker-fundamentals", "docker-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett Docker-kurs från grunden till produktion",
    verified: true
  },
  {
    id: "docker-2",
    title: "Docker in 100 Seconds",
    youtubeId: "Gjnup-PuquQ",
    creator: "Fireship",
    duration: "2:10",
    topics: ["docker", "containers", "overview", "quick"],
    modules: ["docker-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Ultra-snabb intro till Docker-koncept",
    verified: true
  },
  {
    id: "docker-3",
    title: "you need to learn Docker RIGHT NOW!! // Docker Containers 101",
    youtubeId: "eGz9DS-aIeY",
    creator: "NetworkChuck",
    duration: "23:25",
    topics: ["docker", "containers", "intro", "why-docker"],
    modules: ["docker-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Varför Docker är viktigt och hur du kommer igång",
    verified: true
  },

  // ============================================
  // KUBERNETES
  // ============================================
  {
    id: "k8s-1",
    title: "Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]",
    youtubeId: "X48VuDVv0do",
    creator: "TechWorld with Nana",
    duration: "3:36:52",
    topics: ["kubernetes", "k8s", "pods", "deployments", "services", "orchestration"],
    modules: ["kubernetes-basics", "k8s-fundamentals"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett Kubernetes-kurs för nybörjare",
    verified: true
  },
  {
    id: "k8s-2",
    title: "Kubernetes Explained in 100 Seconds",
    youtubeId: "PziYflu8cB8",
    creator: "Fireship",
    duration: "2:36",
    topics: ["kubernetes", "k8s", "overview", "containers"],
    modules: ["kubernetes-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb intro till vad Kubernetes är",
    verified: true
  },

  // ============================================
  // CI/CD & DevOps
  // ============================================
  {
    id: "cicd-1",
    title: "DevOps CI/CD Explained in 100 Seconds",
    youtubeId: "scEDHsr3APg",
    creator: "Fireship",
    duration: "2:27",
    topics: ["cicd", "ci", "cd", "devops", "pipeline", "automation"],
    modules: ["ci-cd-basics", "devops-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb förklaring av CI/CD-koncept",
    verified: true
  },
  {
    id: "cicd-2",
    title: "GitHub Actions Tutorial - Basic Concepts and CI/CD Pipeline with Docker",
    youtubeId: "R8_veQiYBjI",
    creator: "TechWorld with Nana",
    duration: "32:32",
    topics: ["github-actions", "cicd", "pipeline", "docker", "automation"],
    modules: ["ci-cd-basics", "github-actions"],
    difficulty: "intermediate",
    language: "en",
    description: "Praktisk guide till GitHub Actions CI/CD",
    verified: true
  },

  // ============================================
  // GIT
  // ============================================
  {
    id: "git-1",
    title: "Git and GitHub for Beginners - Crash Course",
    youtubeId: "RGOj5yH7evk",
    creator: "freeCodeCamp",
    duration: "1:08:29",
    topics: ["git", "github", "version-control", "branches", "merge", "basics"],
    modules: ["git-basics", "version-control"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett crash course i Git och GitHub",
    verified: true
  },
  {
    id: "git-2",
    title: "Git Explained in 100 Seconds",
    youtubeId: "hwP7WQkmECE",
    creator: "Fireship",
    duration: "2:19",
    topics: ["git", "version-control", "quick"],
    modules: ["git-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Ultra-snabb intro till Git",
    verified: true
  },

  // ============================================
  // BASH & SCRIPTING
  // ============================================
  {
    id: "bash-1",
    title: "Bash Scripting Tutorial for Beginners",
    youtubeId: "tK9Oc6AEnR4",
    creator: "freeCodeCamp",
    duration: "2:14:37",
    topics: ["bash", "scripting", "shell", "automation", "linux"],
    modules: ["bash-scripting", "linux-automation"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett kurs i Bash-scripting",
    verified: true
  },
  {
    id: "bash-2",
    title: "Bash in 100 Seconds",
    youtubeId: "I4EWvMFj37g",
    creator: "Fireship",
    duration: "2:35",
    topics: ["bash", "shell", "quick", "overview"],
    modules: ["bash-scripting"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb intro till Bash",
    verified: true
  },

  // ============================================
  // NETWORKING
  // ============================================
  {
    id: "networking-1",
    title: "Computer Networking Course - Network Engineering",
    youtubeId: "qiQR5rTSshw",
    creator: "freeCodeCamp",
    duration: "1:20:14",
    topics: ["networking", "tcp", "ip", "dns", "http", "subnetting"],
    modules: ["networking-basics", "network-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Grundläggande nätverkskurs",
    verified: true
  },
  {
    id: "networking-2",
    title: "Subnetting Made Easy",
    youtubeId: "ecCuyq-Wprc",
    creator: "NetworkChuck",
    duration: "22:31",
    topics: ["subnetting", "networking", "ip", "cidr", "subnet-mask"],
    modules: ["networking-basics", "subnetting"],
    difficulty: "intermediate",
    language: "en",
    description: "Förenklad guide till subnetting",
    verified: true
  },

  // ============================================
  // SSH & SECURITY
  // ============================================
  {
    id: "ssh-1",
    title: "How SSH Works",
    youtubeId: "5JvLV2-ngCI",
    creator: "tutoriaLinux",
    duration: "8:34",
    topics: ["ssh", "security", "encryption", "keys", "authentication"],
    modules: ["ssh-basics", "security-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Hur SSH faktiskt fungerar",
    verified: true
  },
  {
    id: "ssh-2",
    title: "SSH Crash Course | Basics, Keys & Port Forwarding",
    youtubeId: "hQWRp-FdTpc",
    creator: "Traversy Media",
    duration: "29:11",
    topics: ["ssh", "keys", "port-forwarding", "tunneling", "security"],
    modules: ["ssh-basics", "ssh-advanced"],
    difficulty: "beginner",
    language: "en",
    description: "Praktisk SSH-guide med port forwarding",
    verified: true
  },

  // ============================================
  // SYSTEMD & PROCESS MANAGEMENT
  // ============================================
  {
    id: "systemd-1",
    title: "Understanding Systemd",
    youtubeId: "N1vgvhiyq0E",
    creator: "Learn Linux TV",
    duration: "25:44",
    topics: ["systemd", "services", "init", "linux", "daemon"],
    modules: ["linux-advanced", "process-management"],
    difficulty: "intermediate",
    language: "en",
    description: "Djupgående guide till Systemd",
    verified: true
  },

  // ============================================
  // TERRAFORM & IaC
  // ============================================
  {
    id: "terraform-1",
    title: "Terraform Course - Automate your AWS cloud infrastructure",
    youtubeId: "SLB_c_ayRMo",
    creator: "freeCodeCamp",
    duration: "2:23:30",
    topics: ["terraform", "iac", "aws", "infrastructure", "automation"],
    modules: ["terraform-basics", "infrastructure-as-code"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett Terraform-kurs med AWS",
    verified: true
  },
  {
    id: "terraform-2",
    title: "Terraform in 100 Seconds",
    youtubeId: "tomUWcQ0P3k",
    creator: "Fireship",
    duration: "2:31",
    topics: ["terraform", "iac", "quick", "overview"],
    modules: ["terraform-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb intro till Terraform",
    verified: true
  },

  // ============================================
  // ANSIBLE
  // ============================================
  {
    id: "ansible-1",
    title: "Ansible Full Course | Ansible Tutorial For Beginners",
    youtubeId: "9Ua2b06oAr4",
    creator: "TechWorld with Nana",
    duration: "1:38:30",
    topics: ["ansible", "automation", "configuration-management", "playbooks"],
    modules: ["ansible-basics", "configuration-management"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett Ansible-kurs",
    verified: true
  },

  // ============================================
  // CHRIS TITUS TECH - PRAKTISKA LINUX-TIPS
  // ============================================
  {
    id: "ctt-1",
    title: "Linux Tips & Tricks Every User Should Know",
    youtubeId: "ZNNqkeeOdrk",
    creator: "Chris Titus Tech",
    duration: "15:42",
    topics: ["linux", "tips", "tricks", "productivity", "terminal"],
    modules: ["linux-basics", "linux-tips"],
    difficulty: "beginner",
    language: "en",
    description: "Praktiska tips för effektivare Linux-användning",
    verified: true
  },
  {
    id: "ctt-2",
    title: "The Linux Starter Pack - Everything You Need",
    youtubeId: "mdyCTThABHw",
    creator: "Chris Titus Tech",
    duration: "18:33",
    topics: ["linux", "beginners", "setup", "getting-started"],
    modules: ["linux-basics"],
    difficulty: "beginner",
    language: "en",
    description: "Allt du behöver för att komma igång med Linux",
    verified: true
  },

  // ============================================
  // THE LINUX EXPERIMENT - NEWS & TUTORIALS
  // ============================================
  {
    id: "tle-1",
    title: "Linux Terminal for Beginners",
    youtubeId: "2PGnYjbYuUo",
    creator: "The Linux Experiment",
    duration: "20:15",
    topics: ["linux", "terminal", "beginners", "commands"],
    modules: ["linux-basics", "terminal"],
    difficulty: "beginner",
    language: "en",
    description: "Introduktion till Linux-terminalen",
    verified: true
  },

  // ============================================
  // OFFICIELLA KANALER
  // ============================================
  {
    id: "docker-official-1",
    title: "Docker 101 Tutorial",
    youtubeId: "iqqDU2crIEQ",
    creator: "Docker",
    duration: "12:08",
    topics: ["docker", "containers", "official", "basics"],
    modules: ["docker-fundamentals"],
    difficulty: "beginner",
    language: "en",
    description: "Officiell Docker intro-tutorial",
    verified: true
  },
  {
    id: "redhat-ansible-1",
    title: "Ansible 101",
    youtubeId: "fHO1X93e4WA",
    creator: "Red Hat",
    duration: "45:22",
    topics: ["ansible", "automation", "rhel", "official"],
    modules: ["ansible-basics", "configuration-management"],
    difficulty: "beginner",
    language: "en",
    description: "Officiell Red Hat Ansible-intro",
    verified: true
  },

  // ============================================
  // REGEX - Reguljära Uttryck
  // ============================================
  {
    id: "regex-1",
    title: "Regular Expressions (Regex) Tutorial",
    youtubeId: "sa-TUpSx1JA",
    creator: "freeCodeCamp",
    duration: "1:26:35",
    topics: ["regex", "regular-expressions", "pattern-matching", "grep", "sed"],
    modules: ["bash-scripting", "text-processing"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett regex-kurs - från grunder till avancerat",
    verified: true
  },
  {
    id: "regex-2",
    title: "Regular Expressions (RegEx) in 100 Seconds",
    youtubeId: "sXQxhojSdZM",
    creator: "Fireship",
    duration: "2:16",
    topics: ["regex", "quick", "overview"],
    modules: ["bash-scripting"],
    difficulty: "beginner",
    language: "en",
    description: "Snabb intro till regex-koncept",
    verified: true
  },

  // ============================================
  // SED - Stream Editor
  // ============================================
  {
    id: "sed-1",
    title: "Sed Tutorial - Linux Command Line",
    youtubeId: "nXLnx8ncZyE",
    creator: "Learn Linux TV",
    duration: "32:18",
    topics: ["sed", "stream-editor", "text-processing", "linux", "bash"],
    modules: ["bash-scripting", "text-processing"],
    difficulty: "intermediate",
    language: "en",
    description: "Djupgående sed-tutorial med praktiska exempel",
    verified: true
  },
  {
    id: "sed-2",
    title: "Sed - An Introduction to the UNIX Stream Editor",
    youtubeId: "EACe7aiGczw",
    creator: "tutoriaLinux",
    duration: "18:45",
    topics: ["sed", "unix", "text-manipulation", "scripting"],
    modules: ["bash-scripting"],
    difficulty: "intermediate",
    language: "en",
    description: "Praktisk intro till sed",
    verified: true
  },

  // ============================================
  // AWK - Text Processing
  // ============================================
  {
    id: "awk-1",
    title: "Awk Tutorial - Linux Command Line",
    youtubeId: "oPEnvuj9QrI",
    creator: "Learn Linux TV",
    duration: "28:42",
    topics: ["awk", "text-processing", "data-extraction", "linux", "bash"],
    modules: ["bash-scripting", "text-processing"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett awk-guide för textbearbetning",
    verified: true
  },
  {
    id: "awk-2",
    title: "AWK - The Basics",
    youtubeId: "9YOZmI-zWok",
    creator: "tutoriaLinux",
    duration: "15:33",
    topics: ["awk", "basics", "text-processing"],
    modules: ["bash-scripting"],
    difficulty: "beginner",
    language: "en",
    description: "Grundläggande awk-intro",
    verified: true
  },

  // ============================================
  // ANVÄNDARHANTERING - Users & Groups
  // ============================================
  {
    id: "users-1",
    title: "Linux User Management - Complete Guide",
    youtubeId: "19WOD_3T6D4",
    creator: "Learn Linux TV",
    duration: "24:56",
    topics: ["users", "groups", "useradd", "usermod", "passwd", "linux"],
    modules: ["linux-admin", "user-management"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett guide till användarhantering i Linux",
    verified: true
  },
  {
    id: "users-2",
    title: "Linux Users and Groups",
    youtubeId: "b-9j2jiNLzQ",
    creator: "tutoriaLinux",
    duration: "12:18",
    topics: ["users", "groups", "permissions", "linux"],
    modules: ["linux-admin"],
    difficulty: "beginner",
    language: "en",
    description: "Användare och grupper förklarade",
    verified: true
  },

  // ============================================
  // UFW & FIREWALLD - Brandväggar
  // ============================================
  {
    id: "ufw-1",
    title: "UFW Firewall - How to Configure Ubuntu's Firewall",
    youtubeId: "-CzvPjZ9hp8",
    creator: "Learn Linux TV",
    duration: "21:33",
    topics: ["ufw", "firewall", "ubuntu", "security", "iptables"],
    modules: ["linux-security", "networking"],
    difficulty: "beginner",
    language: "en",
    description: "Komplett UFW-guide för Ubuntu",
    verified: true
  },
  {
    id: "firewall-1",
    title: "Linux Firewall Tutorial | iptables, firewalld, ufw",
    youtubeId: "XtRXm4FFK7Q",
    creator: "NetworkChuck",
    duration: "18:42",
    topics: ["firewall", "iptables", "firewalld", "ufw", "security"],
    modules: ["linux-security", "networking"],
    difficulty: "intermediate",
    language: "en",
    description: "Jämförelse av Linux-brandväggar",
    verified: true
  },
  {
    id: "firewalld-1",
    title: "Firewalld - Configure the Linux Firewall",
    youtubeId: "sMnXzhuVKKs",
    creator: "Learn Linux TV",
    duration: "26:14",
    topics: ["firewalld", "rhel", "centos", "firewall", "zones"],
    modules: ["linux-security", "rhel"],
    difficulty: "intermediate",
    language: "en",
    description: "Firewalld för RHEL/CentOS",
    verified: true
  },

  // ============================================
  // LVM & STORAGE - Lagring
  // ============================================
  {
    id: "lvm-1",
    title: "LVM (Logical Volume Management) - Complete Tutorial",
    youtubeId: "scMkYQxBtJ4",
    creator: "Learn Linux TV",
    duration: "35:22",
    topics: ["lvm", "storage", "volumes", "partitions", "linux"],
    modules: ["linux-storage", "disk-management"],
    difficulty: "intermediate",
    language: "en",
    description: "Komplett LVM-guide från grunden",
    verified: true
  },
  {
    id: "storage-1",
    title: "Linux Storage & File Systems Explained",
    youtubeId: "BV0-EPUYuQc",
    creator: "tutoriaLinux",
    duration: "22:45",
    topics: ["storage", "filesystem", "ext4", "xfs", "partitions"],
    modules: ["linux-storage"],
    difficulty: "intermediate",
    language: "en",
    description: "Filsystem och lagring i Linux",
    verified: true
  },

  // ============================================
  // BACKUP & RSYNC
  // ============================================
  {
    id: "backup-1",
    title: "Linux Backup with rsync",
    youtubeId: "oS5uH0mzMTg",
    creator: "Learn Linux TV",
    duration: "19:28",
    topics: ["backup", "rsync", "restore", "data-protection", "linux"],
    modules: ["linux-admin", "backup"],
    difficulty: "beginner",
    language: "en",
    description: "Backup-strategier med rsync",
    verified: true
  },
  {
    id: "backup-2",
    title: "How to Backup Linux - tar, rsync, and beyond",
    youtubeId: "l8_c2QUZD9w",
    creator: "Chris Titus Tech",
    duration: "14:33",
    topics: ["backup", "tar", "rsync", "linux", "restore"],
    modules: ["linux-admin"],
    difficulty: "beginner",
    language: "en",
    description: "Praktiska backup-metoder",
    verified: true
  },

  // ============================================
  // SIGNALER & TRAPS - Bash Advanced
  // ============================================
  {
    id: "signals-1",
    title: "Bash Scripting - Traps and Signals",
    youtubeId: "3FKwfCsEkz0",
    creator: "tutoriaLinux",
    duration: "11:42",
    topics: ["signals", "traps", "bash", "scripting", "sigint", "sigterm"],
    modules: ["bash-advanced", "scripting"],
    difficulty: "intermediate",
    language: "en",
    description: "Hantera signaler i bash-skript",
    verified: true
  },
  {
    id: "signals-2",
    title: "Linux Processes and Signals",
    youtubeId: "ls5cGi12kGw",
    creator: "Learn Linux TV",
    duration: "16:55",
    topics: ["processes", "signals", "kill", "ps", "linux"],
    modules: ["process-management"],
    difficulty: "intermediate",
    language: "en",
    description: "Processer och signaler i Linux",
    verified: true
  },

  // ============================================
  // CRON & SCHEDULING
  // ============================================
  {
    id: "cron-1",
    title: "Cron Jobs - Linux Task Scheduling",
    youtubeId: "v952m13p-b4",
    creator: "Learn Linux TV",
    duration: "18:22",
    topics: ["cron", "crontab", "scheduling", "automation", "linux"],
    modules: ["linux-admin", "automation"],
    difficulty: "beginner",
    language: "en",
    description: "Automatisera med cron",
    verified: true
  },
  {
    id: "cron-2",
    title: "you need to learn CRON JOBS",
    youtubeId: "QZJ1drMQz1A",
    creator: "NetworkChuck",
    duration: "15:18",
    topics: ["cron", "automation", "scheduling", "linux"],
    modules: ["linux-admin"],
    difficulty: "beginner",
    language: "en",
    description: "NetworkChuck förklarar cron",
    verified: true
  }
]

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

/**
 * Hitta tutorials baserat på ämne/topic
 */
export function findTutorialsByTopic(topic: string): Tutorial[] {
  const normalizedTopic = topic.toLowerCase().trim()
  return TUTORIALS.filter(t => 
    t.topics.some(tp => tp.includes(normalizedTopic) || normalizedTopic.includes(tp)) ||
    t.title.toLowerCase().includes(normalizedTopic)
  ).sort((a, b) => {
    // Prioritera kortare videos för snabb learning
    const aDuration = parseDuration(a.duration)
    const bDuration = parseDuration(b.duration)
    return aDuration - bDuration
  })
}

/**
 * Hitta tutorials kopplade till en modul
 */
export function findTutorialsByModule(moduleSlug: string): Tutorial[] {
  return TUTORIALS.filter(t => 
    t.modules.some(m => m === moduleSlug || m.includes(moduleSlug) || moduleSlug.includes(m))
  )
}

/**
 * Parse duration string to seconds
 */
function parseDuration(duration: string): number {
  const parts = duration.split(':').map(Number)
  if (parts.length === 3) {
    return parts[0] * 3600 + parts[1] * 60 + parts[2]
  } else if (parts.length === 2) {
    return parts[0] * 60 + parts[1]
  }
  return 0
}

/**
 * Generera YouTube embed URL
 */
export function getYouTubeEmbedUrl(youtubeId: string): string {
  return `https://www.youtube.com/embed/${youtubeId}`
}

/**
 * Generera YouTube watch URL
 */
export function getYouTubeWatchUrl(youtubeId: string): string {
  return `https://www.youtube.com/watch?v=${youtubeId}`
}

/**
 * Generera YouTube thumbnail URL
 */
export function getYouTubeThumbnail(youtubeId: string, quality: 'default' | 'medium' | 'high' | 'max' = 'medium'): string {
  const qualityMap = {
    default: 'default',
    medium: 'mqdefault',
    high: 'hqdefault',
    max: 'maxresdefault'
  }
  return `https://img.youtube.com/vi/${youtubeId}/${qualityMap[quality]}.jpg`
}

/**
 * Dallas-formaterad tutorial-rekommendation
 */
export function formatTutorialForDallas(tutorial: Tutorial): string {
  return `📺 **${tutorial.title}**
👤 ${tutorial.creator} | ⏱️ ${tutorial.duration}
🎯 ${tutorial.difficulty === 'beginner' ? 'Nybörjare' : tutorial.difficulty === 'intermediate' ? 'Mellannivå' : 'Avancerad'}
🔗 https://youtube.com/watch?v=${tutorial.youtubeId}`
}

/**
 * Få tutorials för Dallas att rekommendera baserat på fråga
 */
export function getTutorialsForQuery(query: string): Tutorial[] {
  const words = query.toLowerCase().split(/\s+/)
  const matches = new Map<string, { tutorial: Tutorial; score: number }>()

  for (const tutorial of TUTORIALS) {
    let score = 0
    
    // Check topics
    for (const topic of tutorial.topics) {
      for (const word of words) {
        if (topic.includes(word) || word.includes(topic)) {
          score += 2
        }
      }
    }
    
    // Check title
    for (const word of words) {
      if (tutorial.title.toLowerCase().includes(word)) {
        score += 1
      }
    }

    if (score > 0) {
      matches.set(tutorial.id, { tutorial, score })
    }
  }

  return Array.from(matches.values())
    .sort((a, b) => b.score - a.score)
    .slice(0, 3)
    .map(m => m.tutorial)
}
