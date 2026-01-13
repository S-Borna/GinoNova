/**
 * ============================================================================
 * REPUTATION SYSTEM — Community Gamification
 * ============================================================================
 *
 * Point-based reputation system for community engagement
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ReputationLevel {
    level: string
    minPoints: number
    maxPoints: number
    icon: string
    color: string
    gradient: string
    glowColor: string
}

export interface Badge {
    id: string
    name: string
    description: string
    icon: string
    requirement: string
    color: string
}

export interface ReputationPoints {
    postQuestion: number
    replyToQuestion: number
    receiveUpvote: number
    bestAnswer: number
    editWiki: number
    receiveDownvote: number
    helpfulFlag: number
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

export const REPUTATION_POINTS: ReputationPoints = {
    postQuestion: 5,
    replyToQuestion: 10,
    receiveUpvote: 2,
    bestAnswer: 25,
    editWiki: 10,
    receiveDownvote: -1,
    helpfulFlag: 15,
}

export const REPUTATION_LEVELS: ReputationLevel[] = [
    {
        level: "Newbie",
        minPoints: 0,
        maxPoints: 99,
        icon: "🌱",
        color: "text-green-400",
        gradient: "from-green-500 to-emerald-600",
        glowColor: "rgba(34, 197, 94, 0.5)",
    },
    {
        level: "Contributor",
        minPoints: 100,
        maxPoints: 499,
        icon: "⭐",
        color: "text-yellow-400",
        gradient: "from-yellow-500 to-amber-600",
        glowColor: "rgba(234, 179, 8, 0.5)",
    },
    {
        level: "Regular",
        minPoints: 500,
        maxPoints: 999,
        icon: "💎",
        color: "text-cyan-400",
        gradient: "from-cyan-500 to-blue-600",
        glowColor: "rgba(6, 182, 212, 0.5)",
    },
    {
        level: "Veteran",
        minPoints: 1000,
        maxPoints: 2499,
        icon: "🏆",
        color: "text-purple-400",
        gradient: "from-purple-500 to-violet-600",
        glowColor: "rgba(139, 92, 246, 0.5)",
    },
    {
        level: "Legend",
        minPoints: 2500,
        maxPoints: Infinity,
        icon: "👑",
        color: "text-amber-400",
        gradient: "from-amber-500 to-orange-600",
        glowColor: "rgba(245, 158, 11, 0.5)",
    },
]

export const BADGES: Badge[] = [
    {
        id: "helpful",
        name: "Helpful",
        description: "Earned 50 best answers",
        icon: "🎯",
        requirement: "50 best answers",
        color: "text-blue-400",
    },
    {
        id: "mentor",
        name: "Mentor",
        description: "Helped 100 people",
        icon: "🧑‍🏫",
        requirement: "100 helpful replies",
        color: "text-purple-400",
    },
    {
        id: "teacher",
        name: "Teacher",
        description: "Wrote 10 detailed guides",
        icon: "📚",
        requirement: "10 detailed guides",
        color: "text-emerald-400",
    },
    {
        id: "bug-hunter",
        name: "Bug Hunter",
        description: "Reported 5 bugs",
        icon: "🐛",
        requirement: "5 bug reports",
        color: "text-red-400",
    },
    {
        id: "early-adopter",
        name: "Early Adopter",
        description: "Joined in the first month",
        icon: "🚀",
        requirement: "Join early",
        color: "text-cyan-400",
    },
    {
        id: "community-champion",
        name: "Community Champion",
        description: "1000+ reputation points",
        icon: "⚡",
        requirement: "1000+ reputation",
        color: "text-yellow-400",
    },
    {
        id: "welcome-wagon",
        name: "Welcome Wagon",
        description: "Welcomed 25 new members",
        icon: "👋",
        requirement: "25 welcome posts",
        color: "text-pink-400",
    },
    {
        id: "consistent",
        name: "Consistent",
        description: "30 day activity streak",
        icon: "🔥",
        requirement: "30 day streak",
        color: "text-orange-400",
    },
]

/* ============================================================================
   FUNCTIONS
   ============================================================================ */

/**
 * Get reputation level based on points
 */
export function getReputationLevel(points: number): ReputationLevel {
    for (let i = REPUTATION_LEVELS.length - 1; i >= 0; i--) {
        const level = REPUTATION_LEVELS[i]
        if (points >= level.minPoints) {
            return level
        }
    }
    return REPUTATION_LEVELS[0]
}

/**
 * Calculate progress to next level
 */
export function getProgressToNextLevel(points: number): {
    currentLevel: ReputationLevel
    nextLevel: ReputationLevel | null
    progress: number
    pointsToNext: number
} {
    const currentLevel = getReputationLevel(points)
    const currentIndex = REPUTATION_LEVELS.findIndex(
        (l) => l.level === currentLevel.level
    )
    const nextLevel =
        currentIndex < REPUTATION_LEVELS.length - 1
            ? REPUTATION_LEVELS[currentIndex + 1]
            : null

    if (!nextLevel) {
        return {
            currentLevel,
            nextLevel: null,
            progress: 100,
            pointsToNext: 0,
        }
    }

    const pointsInCurrentLevel = points - currentLevel.minPoints
    const pointsNeededForNextLevel = nextLevel.minPoints - currentLevel.minPoints
    const progress = (pointsInCurrentLevel / pointsNeededForNextLevel) * 100

    return {
        currentLevel,
        nextLevel,
        progress,
        pointsToNext: nextLevel.minPoints - points,
    }
}

/**
 * Check if user has earned a badge
 */
export function hasEarnedBadge(
    badgeId: string,
    userStats: {
        bestAnswers?: number
        helpfulReplies?: number
        guides?: number
        bugReports?: number
        reputation?: number
        welcomePosts?: number
        streak?: number
        joinedDaysAgo?: number
    }
): boolean {
    switch (badgeId) {
        case "helpful":
            return (userStats.bestAnswers ?? 0) >= 50
        case "mentor":
            return (userStats.helpfulReplies ?? 0) >= 100
        case "teacher":
            return (userStats.guides ?? 0) >= 10
        case "bug-hunter":
            return (userStats.bugReports ?? 0) >= 5
        case "early-adopter":
            return (userStats.joinedDaysAgo ?? 999) <= 30
        case "community-champion":
            return (userStats.reputation ?? 0) >= 1000
        case "welcome-wagon":
            return (userStats.welcomePosts ?? 0) >= 25
        case "consistent":
            return (userStats.streak ?? 0) >= 30
        default:
            return false
    }
}

/**
 * Get user badges based on their stats
 */
export function getUserBadges(userStats: {
    bestAnswers?: number
    helpfulReplies?: number
    guides?: number
    bugReports?: number
    reputation?: number
    welcomePosts?: number
    streak?: number
    joinedDaysAgo?: number
}): Badge[] {
    return BADGES.filter((badge) => hasEarnedBadge(badge.id, userStats))
}
