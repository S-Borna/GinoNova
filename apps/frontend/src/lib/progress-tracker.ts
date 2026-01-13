/**
 * ============================================================================
 * 📊 PROGRESS TRACKER — Advanced Learning Analytics
 * ============================================================================
 *
 * Comprehensive progress tracking system that monitors:
 * - Module completion status
 * - Task completion rates
 * - Time spent learning (session tracking)
 * - XP earning and leveling
 * - Streaks and consistency
 * - Skills acquired
 *
 * Data stored in localStorage with backup to backend (future)
 *
 * @phase MILESTONE-4.0-PROGRESS-TRACKING
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TaskProgress {
    taskId: string
    moduleId: string
    completed: boolean
    completedAt?: Date
    timeSpent: number // minutes
    attempts: number
    xpEarned: number
}

export interface ModuleProgress {
    moduleId: string
    status: "not_started" | "in_progress" | "completed"
    startedAt?: Date
    completedAt?: Date
    tasksCompleted: number
    totalTasks: number
    timeSpent: number // minutes
    xpEarned: number
    progressPercent: number
}

export interface LearningSession {
    id: string
    moduleId: string
    startTime: Date
    endTime?: Date
    duration: number // minutes
    tasksCompleted: string[]
    xpEarned: number
    notes?: string
}

export interface UserStats {
    totalXP: number
    level: number
    currentLevelXP: number
    xpToNextLevel: number
    modulesCompleted: number
    totalModules: number
    tasksCompleted: number
    totalTasks: number
    currentStreak: number
    longestStreak: number
    totalTimeSpent: number // minutes
    lastActiveDate: Date
    skillsAcquired: string[]
    achievements: Achievement[]
}

export interface Achievement {
    id: string
    title: string
    description: string
    icon: string
    unlockedAt: Date
    rarity: "common" | "rare" | "epic" | "legendary"
}

export interface ProgressData {
    userId: string
    stats: UserStats
    modules: Record<string, ModuleProgress>
    tasks: Record<string, TaskProgress>
    sessions: LearningSession[]
    lastSynced: Date
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const STORAGE_KEY = "devops-hub-progress"
const BASE_XP_PER_LEVEL = 100
const LEVEL_MULTIPLIER = 1.5

// XP rewards
const XP_REWARDS = {
    TASK_COMPLETION: 25,
    MODULE_COMPLETION: 100,
    FIRST_MODULE: 50,
    STREAK_BONUS: 10,
    PERFECT_SCORE: 25,
}

/* ============================================================================
   LEVEL CALCULATION
   ============================================================================ */

export function calculateLevel(totalXP: number): {
    level: number
    currentLevelXP: number
    xpToNextLevel: number
    progressToNextLevel: number
} {
    let level = 1
    let xpRequired = BASE_XP_PER_LEVEL
    let remainingXP = totalXP

    while (remainingXP >= xpRequired) {
        remainingXP -= xpRequired
        level++
        xpRequired = Math.floor(BASE_XP_PER_LEVEL * Math.pow(LEVEL_MULTIPLIER, level - 1))
    }

    const progressToNextLevel = (remainingXP / xpRequired) * 100

    return {
        level,
        currentLevelXP: remainingXP,
        xpToNextLevel: xpRequired,
        progressToNextLevel: Math.round(progressToNextLevel),
    }
}

/* ============================================================================
   STREAK CALCULATION
   ============================================================================ */

function calculateStreak(sessions: LearningSession[]): {
    current: number
    longest: number
} {
    if (sessions.length === 0) return { current: 0, longest: 0 }

    // Sort sessions by date
    const sortedSessions = [...sessions].sort((a, b) =>
        new Date(b.startTime).getTime() - new Date(a.startTime).getTime()
    )

    // Get unique days
    const uniqueDays = new Set(
        sortedSessions.map(s =>
            new Date(s.startTime).toDateString()
        )
    )

    const days = Array.from(uniqueDays).sort((a, b) =>
        new Date(b).getTime() - new Date(a).getTime()
    )

    // Calculate current streak
    let currentStreak = 0
    const today = new Date().toDateString()
    const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000).toDateString()

    if (days[0] === today || days[0] === yesterday) {
        currentStreak = 1
        let lastDate = new Date(days[0])

        for (let i = 1; i < days.length; i++) {
            const currentDate = new Date(days[i])
            const diffDays = Math.floor(
                (lastDate.getTime() - currentDate.getTime()) / (24 * 60 * 60 * 1000)
            )

            if (diffDays === 1) {
                currentStreak++
                lastDate = currentDate
            } else {
                break
            }
        }
    }

    // Calculate longest streak
    let longestStreak = 0
    let tempStreak = 1

    for (let i = 1; i < days.length; i++) {
        const prevDate = new Date(days[i - 1])
        const currentDate = new Date(days[i])
        const diffDays = Math.floor(
            (prevDate.getTime() - currentDate.getTime()) / (24 * 60 * 60 * 1000)
        )

        if (diffDays === 1) {
            tempStreak++
        } else {
            longestStreak = Math.max(longestStreak, tempStreak)
            tempStreak = 1
        }
    }
    longestStreak = Math.max(longestStreak, tempStreak)

    return {
        current: currentStreak,
        longest: longestStreak,
    }
}

/* ============================================================================
   ACHIEVEMENTS CHECK
   ============================================================================ */

const ACHIEVEMENT_DEFINITIONS = [
    {
        id: "first-steps",
        title: "First Steps",
        description: "Complete your first task",
        icon: "🎯",
        rarity: "common" as const,
        check: (data: ProgressData) => data.stats.tasksCompleted >= 1,
    },
    {
        id: "module-master",
        title: "Module Master",
        description: "Complete your first module",
        icon: "📚",
        rarity: "common" as const,
        check: (data: ProgressData) => data.stats.modulesCompleted >= 1,
    },
    {
        id: "on-fire",
        title: "On Fire!",
        description: "Maintain a 7-day streak",
        icon: "🔥",
        rarity: "rare" as const,
        check: (data: ProgressData) => data.stats.currentStreak >= 7,
    },
    {
        id: "unstoppable",
        title: "Unstoppable",
        description: "Maintain a 30-day streak",
        icon: "⚡",
        rarity: "epic" as const,
        check: (data: ProgressData) => data.stats.currentStreak >= 30,
    },
    {
        id: "centurion",
        title: "Centurion",
        description: "Earn 1000 XP",
        icon: "💯",
        rarity: "rare" as const,
        check: (data: ProgressData) => data.stats.totalXP >= 1000,
    },
    {
        id: "grand-master",
        title: "Grand Master",
        description: "Reach level 10",
        icon: "👑",
        rarity: "epic" as const,
        check: (data: ProgressData) => data.stats.level >= 10,
    },
    {
        id: "docker-expert",
        title: "Docker Expert",
        description: "Master containerization",
        icon: "🐳",
        rarity: "rare" as const,
        check: (data: ProgressData) =>
            data.stats.skillsAcquired.some(s => s.toLowerCase().includes("docker")),
    },
    {
        id: "kubernetes-ninja",
        title: "Kubernetes Ninja",
        icon: "☸️",
        description: "Master orchestration",
        rarity: "epic" as const,
        check: (data: ProgressData) =>
            data.stats.skillsAcquired.some(s => s.toLowerCase().includes("kubernetes")),
    },
    {
        id: "night-owl",
        title: "Night Owl",
        description: "Complete a session after midnight",
        icon: "🦉",
        rarity: "common" as const,
        check: (data: ProgressData) =>
            data.sessions.some(s => new Date(s.startTime).getHours() >= 0 && new Date(s.startTime).getHours() < 6),
    },
    {
        id: "marathon-runner",
        title: "Marathon Runner",
        description: "Study for 100+ hours",
        icon: "🏃",
        rarity: "legendary" as const,
        check: (data: ProgressData) => data.stats.totalTimeSpent >= 6000, // 100 hours
    },
]

function checkAchievements(data: ProgressData): Achievement[] {
    const newAchievements: Achievement[] = []
    const existingIds = new Set(data.stats.achievements.map(a => a.id))

    ACHIEVEMENT_DEFINITIONS.forEach(def => {
        if (!existingIds.has(def.id) && def.check(data)) {
            newAchievements.push({
                id: def.id,
                title: def.title,
                description: def.description,
                icon: def.icon,
                rarity: def.rarity,
                unlockedAt: new Date(),
            })
        }
    })

    return newAchievements
}

/* ============================================================================
   STORAGE UTILITIES
   ============================================================================ */

function getDefaultProgressData(userId: string): ProgressData {
    return {
        userId,
        stats: {
            totalXP: 0,
            level: 1,
            currentLevelXP: 0,
            xpToNextLevel: BASE_XP_PER_LEVEL,
            modulesCompleted: 0,
            totalModules: 0,
            tasksCompleted: 0,
            totalTasks: 0,
            currentStreak: 0,
            longestStreak: 0,
            totalTimeSpent: 0,
            lastActiveDate: new Date(),
            skillsAcquired: [],
            achievements: [],
        },
        modules: {},
        tasks: {},
        sessions: [],
        lastSynced: new Date(),
    }
}

export function loadProgress(userId: string): ProgressData {
    try {
        const stored = localStorage.getItem(`${STORAGE_KEY}-${userId}`)
        if (stored) {
            const data = JSON.parse(stored)
            // Convert date strings back to Date objects
            data.stats.lastActiveDate = new Date(data.stats.lastActiveDate)
            data.lastSynced = new Date(data.lastSynced)
            data.sessions = data.sessions.map((s: any) => ({
                ...s,
                startTime: new Date(s.startTime),
                endTime: s.endTime ? new Date(s.endTime) : undefined,
            }))
            data.stats.achievements = data.stats.achievements.map((a: any) => ({
                ...a,
                unlockedAt: new Date(a.unlockedAt),
            }))
            return data
        }
    } catch (error) {
        console.error("Failed to load progress:", error)
    }
    return getDefaultProgressData(userId)
}

export function saveProgress(data: ProgressData): void {
    try {
        data.lastSynced = new Date()
        localStorage.setItem(`${STORAGE_KEY}-${data.userId}`, JSON.stringify(data))
    } catch (error) {
        console.error("Failed to save progress:", error)
    }
}

/* ============================================================================
   PROGRESS TRACKING FUNCTIONS
   ============================================================================ */

export function startSession(userId: string, moduleId: string): LearningSession {
    const session: LearningSession = {
        id: `session-${Date.now()}`,
        moduleId,
        startTime: new Date(),
        duration: 0,
        tasksCompleted: [],
        xpEarned: 0,
    }

    const data = loadProgress(userId)
    data.sessions.push(session)
    data.stats.lastActiveDate = new Date()
    saveProgress(data)

    return session
}

export function endSession(userId: string, sessionId: string): LearningSession | null {
    const data = loadProgress(userId)
    const session = data.sessions.find(s => s.id === sessionId)

    if (session && !session.endTime) {
        session.endTime = new Date()
        session.duration = Math.floor(
            (session.endTime.getTime() - session.startTime.getTime()) / (1000 * 60)
        )
        data.stats.totalTimeSpent += session.duration
        saveProgress(data)
        return session
    }

    return null
}

export function completeTask(
    userId: string,
    moduleId: string,
    taskId: string,
    timeSpent: number = 0
): { xpEarned: number; levelUp: boolean; newAchievements: Achievement[] } {
    const data = loadProgress(userId)

    // Check if already completed
    if (data.tasks[taskId]?.completed) {
        return { xpEarned: 0, levelUp: false, newAchievements: [] }
    }

    // Calculate XP
    let xpEarned = XP_REWARDS.TASK_COMPLETION

    // Streak bonus
    const streaks = calculateStreak(data.sessions)
    if (streaks.current >= 3) {
        xpEarned += XP_REWARDS.STREAK_BONUS
    }

    const oldLevel = data.stats.level

    // Update task progress
    data.tasks[taskId] = {
        taskId,
        moduleId,
        completed: true,
        completedAt: new Date(),
        timeSpent,
        attempts: (data.tasks[taskId]?.attempts || 0) + 1,
        xpEarned,
    }

    // Update module progress
    if (!data.modules[moduleId]) {
        data.modules[moduleId] = {
            moduleId,
            status: "in_progress",
            startedAt: new Date(),
            tasksCompleted: 0,
            totalTasks: 1,
            timeSpent: 0,
            xpEarned: 0,
            progressPercent: 0,
        }
    }

    const moduleProgress = data.modules[moduleId]
    moduleProgress.tasksCompleted++
    moduleProgress.timeSpent += timeSpent
    moduleProgress.xpEarned += xpEarned
    moduleProgress.progressPercent = Math.round(
        (moduleProgress.tasksCompleted / moduleProgress.totalTasks) * 100
    )

    if (moduleProgress.status === "not_started") {
        moduleProgress.status = "in_progress"
        moduleProgress.startedAt = new Date()
    }

    // Update overall stats
    data.stats.tasksCompleted++
    data.stats.totalXP += xpEarned
    data.stats.totalTimeSpent += timeSpent
    data.stats.lastActiveDate = new Date()

    // Recalculate level
    const levelInfo = calculateLevel(data.stats.totalXP)
    data.stats.level = levelInfo.level
    data.stats.currentLevelXP = levelInfo.currentLevelXP
    data.stats.xpToNextLevel = levelInfo.xpToNextLevel

    // Check for achievements
    const newAchievements = checkAchievements(data)
    data.stats.achievements.push(...newAchievements)

    saveProgress(data)

    return {
        xpEarned,
        levelUp: levelInfo.level > oldLevel,
        newAchievements,
    }
}

export function completeModule(
    userId: string,
    moduleId: string,
    skills: string[] = []
): { xpEarned: number; levelUp: boolean; newAchievements: Achievement[] } {
    const data = loadProgress(userId)

    // Check if already completed
    if (data.modules[moduleId]?.status === "completed") {
        return { xpEarned: 0, levelUp: false, newAchievements: [] }
    }

    // Calculate XP
    let xpEarned = XP_REWARDS.MODULE_COMPLETION

    // First module bonus
    if (data.stats.modulesCompleted === 0) {
        xpEarned += XP_REWARDS.FIRST_MODULE
    }

    const oldLevel = data.stats.level

    // Update module progress
    if (!data.modules[moduleId]) {
        data.modules[moduleId] = {
            moduleId,
            status: "completed",
            completedAt: new Date(),
            tasksCompleted: 0,
            totalTasks: 0,
            timeSpent: 0,
            xpEarned: 0,
            progressPercent: 100,
        }
    }

    const moduleProgress = data.modules[moduleId]
    moduleProgress.status = "completed"
    moduleProgress.completedAt = new Date()
    moduleProgress.xpEarned += xpEarned
    moduleProgress.progressPercent = 100

    // Update stats
    data.stats.modulesCompleted++
    data.stats.totalXP += xpEarned
    data.stats.lastActiveDate = new Date()

    // Add new skills
    skills.forEach(skill => {
        if (!data.stats.skillsAcquired.includes(skill)) {
            data.stats.skillsAcquired.push(skill)
        }
    })

    // Recalculate level
    const levelInfo = calculateLevel(data.stats.totalXP)
    data.stats.level = levelInfo.level
    data.stats.currentLevelXP = levelInfo.currentLevelXP
    data.stats.xpToNextLevel = levelInfo.xpToNextLevel

    // Update streaks
    const streaks = calculateStreak(data.sessions)
    data.stats.currentStreak = streaks.current
    data.stats.longestStreak = streaks.longest

    // Check for achievements
    const newAchievements = checkAchievements(data)
    data.stats.achievements.push(...newAchievements)

    saveProgress(data)

    return {
        xpEarned,
        levelUp: levelInfo.level > oldLevel,
        newAchievements,
    }
}

export function getProgress(userId: string): ProgressData {
    const data = loadProgress(userId)

    // Recalculate streaks
    const streaks = calculateStreak(data.sessions)
    data.stats.currentStreak = streaks.current
    data.stats.longestStreak = streaks.longest

    return data
}

export function getModuleProgress(userId: string, moduleId: string): ModuleProgress | null {
    const data = loadProgress(userId)
    return data.modules[moduleId] || null
}

export function updateModuleTotalTasks(userId: string, moduleId: string, totalTasks: number): void {
    const data = loadProgress(userId)

    if (!data.modules[moduleId]) {
        data.modules[moduleId] = {
            moduleId,
            status: "not_started",
            tasksCompleted: 0,
            totalTasks,
            timeSpent: 0,
            xpEarned: 0,
            progressPercent: 0,
        }
    } else {
        data.modules[moduleId].totalTasks = totalTasks
        data.modules[moduleId].progressPercent = Math.round(
            (data.modules[moduleId].tasksCompleted / totalTasks) * 100
        )
    }

    saveProgress(data)
}

/* ============================================================================
   ANALYTICS & INSIGHTS
   ============================================================================ */

export function getLearningVelocity(userId: string, days: number = 7): {
    xpPerDay: number
    tasksPerDay: number
    hoursPerDay: number
} {
    const data = loadProgress(userId)
    const cutoffDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000)

    const recentSessions = data.sessions.filter(
        s => new Date(s.startTime) >= cutoffDate
    )

    const totalXP = recentSessions.reduce((sum, s) => sum + s.xpEarned, 0)
    const totalTasks = recentSessions.reduce((sum, s) => sum + s.tasksCompleted.length, 0)
    const totalMinutes = recentSessions.reduce((sum, s) => sum + s.duration, 0)

    return {
        xpPerDay: Math.round(totalXP / days),
        tasksPerDay: Math.round((totalTasks / days) * 10) / 10,
        hoursPerDay: Math.round((totalMinutes / days / 60) * 10) / 10,
    }
}

export function getWeeklyActivity(userId: string): number[] {
    const data = loadProgress(userId)
    const activity = new Array(7).fill(0)

    // Get last 7 days
    for (let i = 0; i < 7; i++) {
        const date = new Date(Date.now() - i * 24 * 60 * 60 * 1000).toDateString()
        const dayMinutes = data.sessions
            .filter(s => new Date(s.startTime).toDateString() === date)
            .reduce((sum, s) => sum + s.duration, 0)
        activity[6 - i] = dayMinutes
    }

    return activity
}
