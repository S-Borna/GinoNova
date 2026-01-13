/**
 * ============================================================================
 * COMMUNITY TYPES — Data Structures
 * ============================================================================
 */

export interface Thread {
    id: string
    title: string
    content: string
    authorId: string
    author: {
        id: string
        name: string
        avatar?: string
        reputation: number
    }
    categoryId: string
    category: Category
    tags: string[]
    views: number
    replyCount: number
    upvotes: number
    downvotes: number
    isPinned: boolean
    isLocked: boolean
    hasAcceptedAnswer: boolean
    createdAt: Date
    updatedAt: Date
    lastActivityAt: Date
}

export interface Reply {
    id: string
    threadId: string
    content: string
    authorId: string
    author: {
        id: string
        name: string
        avatar?: string
        reputation: number
    }
    parentReplyId?: string
    upvotes: number
    downvotes: number
    isAccepted: boolean
    createdAt: Date
    updatedAt: Date
    replies?: Reply[]
}

export interface Category {
    id: string
    name: string
    slug: string
    description: string
    icon: string
    color: string
    gradient: string
    threadCount: number
    postCount: number
}

export interface UserProfile {
    id: string
    name: string
    username: string
    email: string
    avatar?: string
    banner?: string
    bio?: string
    reputation: number
    reputationLevel: string
    badges: string[]
    joinDate: Date
    lastSeen: Date
    stats: {
        postsCreated: number
        repliesCreated: number
        upvotesReceived: number
        bestAnswers: number
        modulesCompleted: number
        certificatesEarned: number
        learningStreak: number
    }
    socialLinks?: {
        github?: string
        linkedin?: string
        twitter?: string
        website?: string
    }
}

export interface Notification {
    id: string
    userId: string
    type: NotificationType
    title: string
    message: string
    link?: string
    read: boolean
    createdAt: Date
    metadata?: Record<string, any>
}

export type NotificationType =
    | "reply"
    | "upvote"
    | "best_answer"
    | "mention"
    | "achievement"
    | "module_release"
    | "direct_message"

export interface Message {
    id: string
    senderId: string
    receiverId: string
    content: string
    read: boolean
    createdAt: Date
    sender: {
        id: string
        name: string
        avatar?: string
    }
    receiver: {
        id: string
        name: string
        avatar?: string
    }
}

export interface Conversation {
    id: string
    participants: {
        id: string
        name: string
        avatar?: string
        lastSeen: Date
    }[]
    lastMessage: Message
    unreadCount: number
    updatedAt: Date
}

export interface ModerationAction {
    id: string
    type: "ban" | "warn" | "delete" | "lock" | "pin" | "move"
    targetType: "thread" | "reply" | "user"
    targetId: string
    moderatorId: string
    reason: string
    createdAt: Date
}

export interface Report {
    id: string
    reportedBy: string
    targetType: "thread" | "reply" | "user"
    targetId: string
    reason: string
    status: "pending" | "reviewed" | "resolved"
    createdAt: Date
}

// Mock data categories
export const CATEGORIES: Category[] = [
    {
        id: "general",
        name: "General Discussion",
        slug: "general",
        description: "General DevOps discussions and topics",
        icon: "💬",
        color: "text-blue-400",
        gradient: "from-blue-500 to-cyan-600",
        threadCount: 234,
        postCount: 1567,
    },
    {
        id: "docker",
        name: "Docker & Containers",
        slug: "docker",
        description: "Containerization with Docker and related technologies",
        icon: "🐳",
        color: "text-cyan-400",
        gradient: "from-cyan-500 to-blue-600",
        threadCount: 189,
        postCount: 1423,
    },
    {
        id: "kubernetes",
        name: "Kubernetes",
        slug: "kubernetes",
        description: "Container orchestration and K8s discussions",
        icon: "☸️",
        color: "text-purple-400",
        gradient: "from-purple-500 to-blue-600",
        threadCount: 156,
        postCount: 1234,
    },
    {
        id: "cicd",
        name: "CI/CD Pipelines",
        slug: "cicd",
        description: "Continuous Integration and Deployment",
        icon: "🔄",
        color: "text-emerald-400",
        gradient: "from-emerald-500 to-teal-600",
        threadCount: 145,
        postCount: 1098,
    },
    {
        id: "terraform",
        name: "Terraform & IaC",
        slug: "terraform",
        description: "Infrastructure as Code with Terraform",
        icon: "🏗️",
        color: "text-purple-400",
        gradient: "from-purple-500 to-violet-600",
        threadCount: 123,
        postCount: 987,
    },
    {
        id: "aws",
        name: "AWS Cloud",
        slug: "aws",
        description: "Amazon Web Services discussions",
        icon: "☁️",
        color: "text-orange-400",
        gradient: "from-orange-500 to-amber-600",
        threadCount: 167,
        postCount: 1345,
    },
    {
        id: "linux",
        name: "Linux & Shell",
        slug: "linux",
        description: "Linux administration and shell scripting",
        icon: "🐧",
        color: "text-yellow-400",
        gradient: "from-yellow-500 to-orange-600",
        threadCount: 198,
        postCount: 1567,
    },
    {
        id: "python",
        name: "Python & Automation",
        slug: "python",
        description: "Python scripting and automation",
        icon: "🐍",
        color: "text-blue-400",
        gradient: "from-blue-500 to-indigo-600",
        threadCount: 134,
        postCount: 1023,
    },
    {
        id: "career",
        name: "Career Advice",
        slug: "career",
        description: "DevOps career guidance and job discussions",
        icon: "💼",
        color: "text-amber-400",
        gradient: "from-amber-500 to-yellow-600",
        threadCount: 89,
        postCount: 567,
    },
    {
        id: "projects",
        name: "Show Your Projects",
        slug: "projects",
        description: "Showcase your DevOps projects",
        icon: "🚀",
        color: "text-pink-400",
        gradient: "from-pink-500 to-rose-600",
        threadCount: 112,
        postCount: 445,
    },
    {
        id: "help",
        name: "Help & Support",
        slug: "help",
        description: "Get help with your DevOps challenges",
        icon: "🆘",
        color: "text-red-400",
        gradient: "from-red-500 to-pink-600",
        threadCount: 267,
        postCount: 1890,
    },
    {
        id: "off-topic",
        name: "Off-Topic",
        slug: "off-topic",
        description: "Anything goes (within community guidelines)",
        icon: "🎉",
        color: "text-purple-400",
        gradient: "from-purple-500 to-pink-600",
        threadCount: 78,
        postCount: 423,
    },
]
