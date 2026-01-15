/**
 * Certificates and Achievements System
 * Data structures and utilities for gamification
 */

/* ============================================================================
   CERTIFICATE TYPES
   ============================================================================ */

export interface Certificate {
    id: string
    userId: string
    moduleId: string
    moduleName: string
    issuedDate: Date
    verificationCode: string
    skills: string[]
    completionScore?: number
    timeSpent?: number // in hours
}

export interface CertificateShareData {
    certificateId: string
    platform: "linkedin" | "twitter" | "facebook"
    url: string
}

/* ============================================================================
   ACHIEVEMENT TYPES
   ============================================================================ */

export type AchievementRarity = "common" | "rare" | "epic" | "legendary"

export type AchievementCategory =
    | "learning"
    | "consistency"
    | "speed"
    | "mastery"
    | "specialization"
    | "community"
    | "rare"

export interface Achievement {
    id: string
    name: string
    description: string
    icon: string
    rarity: AchievementRarity
    category: AchievementCategory
    xpReward: number
    unlockedAt?: Date
    progress?: {
        current: number
        total: number
    }
}

export interface UserAchievement extends Achievement {
    earnedAt?: Date
    isLocked: boolean
}

/* ============================================================================
   LEADERBOARD TYPES
   ============================================================================ */

export type LeaderboardType =
    | "global-xp"
    | "weekly-progress"
    | "streak-champions"
    | "module-masters"
    | "speed-demons"

export interface LeaderboardEntry {
    rank: number
    userId: string
    userName: string
    userAvatar?: string
    score: number
    change?: number // rank change from previous period
    badge?: string
}

export interface Leaderboard {
    type: LeaderboardType
    title: string
    description: string
    entries: LeaderboardEntry[]
    userRank?: number
    lastUpdated: Date
}

/* ============================================================================
   ACHIEVEMENTS DEFINITIONS
   ============================================================================ */

export const ACHIEVEMENTS: Achievement[] = [
    // Learning Milestones
    {
        id: "first-module",
        name: "First Steps",
        description: "Complete your first module",
        icon: "🎯",
        rarity: "common",
        category: "learning",
        xpReward: 100,
    },
    {
        id: "10-modules",
        name: "Learning Champion",
        description: "Complete 10 modules",
        icon: "🏆",
        rarity: "rare",
        category: "learning",
        xpReward: 500,
    },
    {
        id: "25-modules",
        name: "Module Master",
        description: "Complete 25 modules",
        icon: "👑",
        rarity: "epic",
        category: "learning",
        xpReward: 1500,
    },
    {
        id: "first-task",
        name: "Task Tackler",
        description: "Complete your first task",
        icon: "✓",
        rarity: "common",
        category: "learning",
        xpReward: 50,
    },
    {
        id: "100-tasks",
        name: "Task Terminator",
        description: "Complete 100 tasks",
        icon: "💪",
        rarity: "epic",
        category: "learning",
        xpReward: 1000,
    },
    {
        id: "500-tasks",
        name: "Task Titan",
        description: "Complete 500 tasks",
        icon: "⚡",
        rarity: "legendary",
        category: "learning",
        xpReward: 5000,
    },

    // Consistency Streaks
    {
        id: "streak-7",
        name: "Week Warrior",
        description: "Maintain a 7-day learning streak",
        icon: "🔥",
        rarity: "common",
        category: "consistency",
        xpReward: 200,
    },
    {
        id: "streak-30",
        name: "Monthly Marvel",
        description: "Maintain a 30-day learning streak",
        icon: "🌟",
        rarity: "rare",
        category: "consistency",
        xpReward: 1000,
    },
    {
        id: "streak-100",
        name: "Century Champion",
        description: "Maintain a 100-day learning streak",
        icon: "💫",
        rarity: "epic",
        category: "consistency",
        xpReward: 3000,
    },
    {
        id: "streak-365",
        name: "Year Achiever",
        description: "Maintain a 365-day learning streak",
        icon: "🎆",
        rarity: "legendary",
        category: "consistency",
        xpReward: 10000,
    },

    // Speed Achievements
    {
        id: "speed-1day",
        name: "Speed Learner",
        description: "Complete a module in 1 day",
        icon: "⚡",
        rarity: "rare",
        category: "speed",
        xpReward: 300,
    },
    {
        id: "marathon-8hours",
        name: "Marathon Runner",
        description: "Study for 8 hours in one day",
        icon: "🏃",
        rarity: "epic",
        category: "speed",
        xpReward: 800,
    },
    {
        id: "night-owl",
        name: "Night Owl",
        description: "Complete 10 tasks after midnight",
        icon: "🦉",
        rarity: "rare",
        category: "speed",
        xpReward: 400,
    },
    {
        id: "early-bird",
        name: "Early Bird",
        description: "Complete 10 tasks before 6 AM",
        icon: "🌅",
        rarity: "rare",
        category: "speed",
        xpReward: 400,
    },

    // Mastery Achievements
    {
        id: "perfect-score",
        name: "Perfect Score",
        description: "Get 100% on all quizzes in a module",
        icon: "💯",
        rarity: "epic",
        category: "mastery",
        xpReward: 1200,
    },
    {
        id: "quiz-master-50",
        name: "Quiz Master",
        description: "Pass 50 quizzes",
        icon: "🎓",
        rarity: "rare",
        category: "mastery",
        xpReward: 750,
    },
    {
        id: "quiz-legend-100",
        name: "Quiz Legend",
        description: "Pass 100 quizzes",
        icon: "🏅",
        rarity: "epic",
        category: "mastery",
        xpReward: 2000,
    },
    {
        id: "first-try",
        name: "First Try Master",
        description: "Pass 10 quizzes on first attempt",
        icon: "🎯",
        rarity: "rare",
        category: "mastery",
        xpReward: 600,
    },

    // Specializations
    {
        id: "k8s-expert",
        name: "Kubernetes Expert",
        description: "Complete all Kubernetes modules",
        icon: "☸️",
        rarity: "epic",
        category: "specialization",
        xpReward: 2000,
    },
    {
        id: "cloud-master",
        name: "Cloud Master",
        description: "Complete all AWS/Cloud modules",
        icon: "☁️",
        rarity: "epic",
        category: "specialization",
        xpReward: 2000,
    },
    {
        id: "python-pro",
        name: "Python Pro",
        description: "Complete all Python modules",
        icon: "🐍",
        rarity: "epic",
        category: "specialization",
        xpReward: 2000,
    },
    {
        id: "devsecops-guru",
        name: "DevSecOps Guru",
        description: "Complete all security-focused modules",
        icon: "🔒",
        rarity: "legendary",
        category: "specialization",
        xpReward: 3000,
    },
    {
        id: "terraform-titan",
        name: "Terraform Titan",
        description: "Complete all Terraform modules",
        icon: "🔧",
        rarity: "epic",
        category: "specialization",
        xpReward: 2000,
    },
    {
        id: "docker-captain",
        name: "Docker Captain",
        description: "Complete all Docker modules",
        icon: "🐳",
        rarity: "rare",
        category: "specialization",
        xpReward: 1500,
    },
    {
        id: "ci-cd-commander",
        name: "CI/CD Commander",
        description: "Complete all CI/CD modules",
        icon: "🚀",
        rarity: "epic",
        category: "specialization",
        xpReward: 2000,
    },

    // Community Achievements
    {
        id: "helpful-10",
        name: "Helpful Hand",
        description: "Answer 10 questions in forums",
        icon: "🤝",
        rarity: "rare",
        category: "community",
        xpReward: 500,
    },
    {
        id: "mentor-5",
        name: "Mentor",
        description: "Help 5 students complete a module",
        icon: "👨‍🏫",
        rarity: "epic",
        category: "community",
        xpReward: 1500,
    },
    {
        id: "community-star",
        name: "Community Star",
        description: "Receive 100 upvotes on your answers",
        icon: "⭐",
        rarity: "epic",
        category: "community",
        xpReward: 1200,
    },

    // Rare/Special Achievements
    {
        id: "early-adopter",
        name: "Early Adopter",
        description: "Join GinoNova in its first month",
        icon: "🌟",
        rarity: "legendary",
        category: "rare",
        xpReward: 5000,
    },
    {
        id: "beta-tester",
        name: "Beta Tester",
        description: "Participate in beta testing",
        icon: "🧪",
        rarity: "legendary",
        category: "rare",
        xpReward: 3000,
    },
    {
        id: "bug-hunter",
        name: "Bug Hunter",
        description: "Report 5 valid bugs",
        icon: "🐛",
        rarity: "epic",
        category: "rare",
        xpReward: 2000,
    },
    {
        id: "midnight-scholar",
        name: "Midnight Scholar",
        description: "Complete a module between 12 AM - 3 AM",
        icon: "🌙",
        rarity: "rare",
        category: "rare",
        xpReward: 500,
    },
    {
        id: "weekend-warrior",
        name: "Weekend Warrior",
        description: "Complete 10 modules on weekends",
        icon: "🎮",
        rarity: "rare",
        category: "rare",
        xpReward: 800,
    },
]

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

/**
 * Get achievement by ID
 */
export function getAchievementById(id: string): Achievement | undefined {
    return ACHIEVEMENTS.find((a) => a.id === id)
}

/**
 * Get achievements by category
 */
export function getAchievementsByCategory(category: AchievementCategory): Achievement[] {
    return ACHIEVEMENTS.filter((a) => a.category === category)
}

/**
 * Get achievements by rarity
 */
export function getAchievementsByRarity(rarity: AchievementRarity): Achievement[] {
    return ACHIEVEMENTS.filter((a) => a.rarity === rarity)
}

/**
 * Get rarity color
 */
export function getRarityColor(rarity: AchievementRarity): {
    bg: string
    border: string
    text: string
    glow: string
} {
    const colors = {
        common: {
            bg: "from-zinc-600/25 to-zinc-500/5",
            border: "border-zinc-500/40",
            text: "text-zinc-400",
            glow: "0 0 30px rgba(113, 113, 122, 0.3)",
        },
        rare: {
            bg: "from-blue-600/25 to-blue-500/5",
            border: "border-blue-500/40",
            text: "text-blue-400",
            glow: "0 0 30px rgba(59, 130, 246, 0.4)",
        },
        epic: {
            bg: "from-purple-600/25 to-purple-500/5",
            border: "border-purple-500/40",
            text: "text-purple-400",
            glow: "0 0 30px rgba(139, 92, 246, 0.5)",
        },
        legendary: {
            bg: "from-amber-600/25 to-orange-500/5",
            border: "border-amber-500/40",
            text: "text-amber-400",
            glow: "0 0 40px rgba(245, 158, 11, 0.6)",
        },
    }
    return colors[rarity] || colors.common
}

/**
 * Get category color
 */
export function getCategoryColor(category: AchievementCategory): {
    bg: string
    text: string
} {
    const colors = {
        learning: { bg: "bg-purple-500/20", text: "text-purple-400" },
        consistency: { bg: "bg-orange-500/20", text: "text-orange-400" },
        speed: { bg: "bg-cyan-500/20", text: "text-cyan-400" },
        mastery: { bg: "bg-emerald-500/20", text: "text-emerald-400" },
        specialization: { bg: "bg-blue-500/20", text: "text-blue-400" },
        community: { bg: "bg-pink-500/20", text: "text-pink-400" },
        rare: { bg: "bg-amber-500/20", text: "text-amber-400" },
    }
    return colors[category] || colors.learning
}

/**
 * Generate certificate verification code
 */
export function generateVerificationCode(certificateId: string): string {
    // Simple hash-based verification code
    const hash = certificateId.split("").reduce((acc, char) => {
        const code = char.charCodeAt(0)
        return ((acc << 5) - acc + code) | 0
    }, 0)
    return `DH-${Math.abs(hash).toString(36).toUpperCase().slice(0, 8)}`
}

/**
 * Generate certificate download URL
 */
export function getCertificateDownloadUrl(certificateId: string, format: "png" | "pdf"): string {
    return `/api/certificates/${certificateId}/download?format=${format}`
}

/**
 * Generate LinkedIn share URL
 */
export function getLinkedInShareUrl(certificate: Certificate): string {
    const certUrl = `${window.location.origin}/verify/${certificate.id}`
    const text = `I just earned a certificate in ${certificate.moduleName} from GinoNova! 🎓`
    return `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(certUrl)}&title=${encodeURIComponent(text)}`
}

/**
 * Generate Twitter share URL
 */
export function getTwitterShareUrl(certificate: Certificate): string {
    const certUrl = `${window.location.origin}/verify/${certificate.id}`
    const text = `I just earned a certificate in ${certificate.moduleName} from @DevOpsHub! 🎓 ${certUrl}`
    return `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`
}

/**
 * Calculate completion percentage
 */
export function calculateCompletionPercentage(current: number, total: number): number {
    if (total === 0) return 0
    return Math.round((current / total) * 100)
}

/**
 * Format date for certificate
 */
export function formatCertificateDate(date: Date): string {
    return new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
    }).format(date)
}

/**
 * Get mock certificates (for demo purposes)
 */
export function getMockCertificates(userId: string): Certificate[] {
    return [
        {
            id: "cert-001",
            userId,
            moduleId: "k8s-fundamentals",
            moduleName: "Kubernetes Fundamentals",
            issuedDate: new Date("2024-01-15"),
            verificationCode: generateVerificationCode("cert-001"),
            skills: ["Kubernetes", "Container Orchestration", "Pods", "Services"],
            completionScore: 95,
            timeSpent: 12,
        },
        {
            id: "cert-002",
            userId,
            moduleId: "docker-mastery",
            moduleName: "Docker Mastery",
            issuedDate: new Date("2024-02-10"),
            verificationCode: generateVerificationCode("cert-002"),
            skills: ["Docker", "Containerization", "Docker Compose", "Networking"],
            completionScore: 98,
            timeSpent: 8,
        },
        {
            id: "cert-003",
            userId,
            moduleId: "aws-cloud",
            moduleName: "AWS Cloud Fundamentals",
            issuedDate: new Date("2024-03-05"),
            verificationCode: generateVerificationCode("cert-003"),
            skills: ["AWS", "EC2", "S3", "Lambda", "Cloud Computing"],
            completionScore: 92,
            timeSpent: 15,
        },
    ]
}

/**
 * Get mock user achievements (for demo purposes)
 */
export function getMockUserAchievements(): UserAchievement[] {
    const now = new Date()
    return ACHIEVEMENTS.map((achievement, index) => ({
        ...achievement,
        isLocked: index > 15, // First 15 unlocked
        earnedAt: index <= 15 ? new Date(now.getTime() - Math.random() * 30 * 24 * 60 * 60 * 1000) : undefined,
        progress:
            index > 15 && achievement.id.includes("100")
                ? { current: Math.floor(Math.random() * 50), total: 100 }
                : index > 15 && achievement.id.includes("50")
                    ? { current: Math.floor(Math.random() * 30), total: 50 }
                    : index > 15 && achievement.id.includes("10")
                        ? { current: Math.floor(Math.random() * 7), total: 10 }
                        : undefined,
    }))
}

/**
 * Get mock leaderboard data
 */
export function getMockLeaderboard(type: LeaderboardType): Leaderboard {
    const titles = {
        "global-xp": "Global XP Leaders",
        "weekly-progress": "Weekly Progress Champions",
        "streak-champions": "Longest Learning Streaks",
        "module-masters": "Most Modules Completed",
        "speed-demons": "Fastest Learners",
    }

    const descriptions = {
        "global-xp": "Top learners by total XP earned",
        "weekly-progress": "Most active learners this week",
        "streak-champions": "Longest consecutive learning streaks",
        "module-masters": "Most modules completed overall",
        "speed-demons": "Fastest average module completion time",
    }

    // Generate mock entries
    const entries: LeaderboardEntry[] = Array.from({ length: 100 }, (_, i) => ({
        rank: i + 1,
        userId: `user-${i + 1}`,
        userName: `DevOps Learner ${i + 1}`,
        userAvatar: undefined,
        score: 10000 - i * 50 - Math.floor(Math.random() * 50),
        change: Math.floor(Math.random() * 21) - 10, // -10 to +10
        badge: i === 0 ? "🥇" : i === 1 ? "🥈" : i === 2 ? "🥉" : undefined,
    }))

    return {
        type,
        title: titles[type],
        description: descriptions[type],
        entries,
        userRank: 42, // Mock user rank
        lastUpdated: new Date(),
    }
}
