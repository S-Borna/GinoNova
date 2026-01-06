/**
 * Progress API Client + Calculations
 * Phase 5.0: Progress Engine Foundation with standardized error handling
 * Phase A.5: XP, Level, and Progress Calculations
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types
export type ProgressStatus = "not_started" | "in_progress" | "completed"
export type TargetType = "module" | "task" | "studyflow"

// Types matching backend schemas
export interface ProgressPublic {
    id: string
    user_id: string
    module_id: string | null
    task_id: string | null
    studyflow_id: string | null
    status: ProgressStatus
    progress: number
    created_at: string
    updated_at: string
}

export interface ProgressCreate {
    user_id: string
    module_id?: string | null
    task_id?: string | null
    studyflow_id?: string | null
    progress?: number
}

export interface ProgressUpdate {
    progress?: number
}

// Standardized API response types
export interface ApiSuccess<T> {
    ok: true
    data: T
}

export interface ApiFailure {
    ok: false
    status: number
    message: string
}

export type ApiResult<T> = ApiSuccess<T> | ApiFailure

// Helper functions
export function getTargetType(progress: ProgressPublic): TargetType {
    if (progress.module_id) return "module"
    if (progress.task_id) return "task"
    if (progress.studyflow_id) return "studyflow"
    return "module" // fallback
}

export function getTargetId(progress: ProgressPublic): string | null {
    return progress.module_id || progress.task_id || progress.studyflow_id
}

export function mapStatusToColor(status: ProgressStatus): string {
    switch (status) {
        case "completed":
            return "bg-green-100 text-green-800"
        case "in_progress":
            return "bg-yellow-100 text-yellow-800"
        case "not_started":
        default:
            return "bg-gray-100 text-gray-800"
    }
}

export function mapStatusToLabel(status: ProgressStatus): string {
    switch (status) {
        case "completed":
            return "Completed"
        case "in_progress":
            return "In Progress"
        case "not_started":
        default:
            return "Not Started"
    }
}

export function mapTargetTypeToColor(targetType: TargetType): string {
    switch (targetType) {
        case "module":
            return "bg-blue-100 text-blue-800"
        case "task":
            return "bg-purple-100 text-purple-800"
        case "studyflow":
            return "bg-indigo-100 text-indigo-800"
        default:
            return "bg-gray-100 text-gray-800"
    }
}

export function mapTargetTypeToLabel(targetType: TargetType): string {
    switch (targetType) {
        case "module":
            return "Module"
        case "task":
            return "Task"
        case "studyflow":
            return "Studyflow"
        default:
            return "Unknown"
    }
}

export function getTargetLink(progress: ProgressPublic): string {
    const targetType = getTargetType(progress)
    const targetId = getTargetId(progress)

    if (!targetId) return "#"

    switch (targetType) {
        case "module":
            return `/modules/${targetId}`
        case "task":
            return `/tasks/${targetId}`
        case "studyflow":
            return `/studyflow/${targetId}`
        default:
            return "#"
    }
}

/**
 * Get all progress records for a specific user
 */
export async function getUserProgress(userId: string): Promise<ApiResult<ProgressPublic[]>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/user/${userId}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch progress" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Get a single progress record by ID
 */
export async function getProgress(id: string): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to fetch progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to fetch progress" }
        }

        const data = await res.json()
        return { ok: true, data }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Create a new progress record
 */
export async function createProgress(data: ProgressCreate): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to create progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to create progress" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/**
 * Update an existing progress record
 */
export async function updateProgress(id: string, data: ProgressUpdate): Promise<ApiResult<ProgressPublic>> {
    try {
        const res = await fetch(`${API_BASE_URL}/api/progress/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })

        if (!res.ok) {
            const error = await res.json().catch(() => ({ detail: "Failed to update progress" }))
            return { ok: false, status: res.status, message: error.detail || "Failed to update progress" }
        }

        const responseData = await res.json()
        return { ok: true, data: responseData }
    } catch (error) {
        return { ok: false, status: 0, message: error instanceof Error ? error.message : "Network error" }
    }
}

/* ============================================================================
   XP & LEVEL CONSTANTS (A.5)
   ============================================================================ */

// Level thresholds - XP required to reach each level
export const LEVEL_THRESHOLDS = [
    0,      // Level 1
    100,    // Level 2
    250,    // Level 3
    500,    // Level 4
    800,    // Level 5
    1200,   // Level 6
    1700,   // Level 7
    2300,   // Level 8
    3000,   // Level 9
    3800,   // Level 10
    4700,   // Level 11
    5700,   // Level 12
    6800,   // Level 13
    8000,   // Level 14
    9500,   // Level 15
    11000,  // Level 16
    12800,  // Level 17
    14800,  // Level 18
    17000,  // Level 19
    20000,  // Level 20
] as const

// XP rewards
export const XP_REWARDS = {
    TASK_COMPLETE: 25,
    LAB_COMPLETE: 50,
    PROJECT_COMPLETE: 100,
    MODULE_COMPLETE_BONUS: 150,
    TRACK_COMPLETE_BONUS: 500,
    STREAK_BONUS_3_DAYS: 25,
    STREAK_BONUS_7_DAYS: 75,
    STREAK_BONUS_14_DAYS: 150,
    STREAK_BONUS_30_DAYS: 300,
} as const

export const MAX_LEVEL = 50

/* ============================================================================
   LEVEL INFO TYPE
   ============================================================================ */

export interface LevelInfo {
    level: number
    currentXP: number
    xpForCurrentLevel: number
    xpForNextLevel: number
    xpToNextLevel: number
    progressToNextLevel: number
}

/* ============================================================================
   LEVEL CALCULATIONS
   ============================================================================ */

/**
 * Calculate the user's level from total XP
 */
export function calculateLevel(totalXP: number): number {
    if (totalXP < 0) return 1

    for (let i = LEVEL_THRESHOLDS.length - 1; i >= 0; i--) {
        if (totalXP >= LEVEL_THRESHOLDS[i]) {
            if (i === LEVEL_THRESHOLDS.length - 1) {
                const xpAfterMax = totalXP - LEVEL_THRESHOLDS[i]
                const additionalLevels = Math.floor(xpAfterMax / 3500)
                return Math.min(i + 1 + additionalLevels, MAX_LEVEL)
            }
            return i + 1
        }
    }

    return 1
}

/**
 * Get XP required to reach a specific level
 */
export function getXPForLevel(level: number): number {
    if (level <= 1) return 0
    if (level <= LEVEL_THRESHOLDS.length) {
        return LEVEL_THRESHOLDS[level - 1]
    }
    const lastThreshold = LEVEL_THRESHOLDS[LEVEL_THRESHOLDS.length - 1]
    const additionalLevels = level - LEVEL_THRESHOLDS.length
    return lastThreshold + additionalLevels * 3500
}

/**
 * Calculate XP needed to reach the next level
 */
export function calculateXPToNextLevel(totalXP: number): number {
    const currentLevel = calculateLevel(totalXP)
    if (currentLevel >= MAX_LEVEL) return 0
    const xpForNextLevel = getXPForLevel(currentLevel + 1)
    return xpForNextLevel - totalXP
}

/**
 * Get comprehensive level info for display
 */
export function getLevelInfo(totalXP: number): LevelInfo {
    const level = calculateLevel(totalXP)
    const xpForCurrentLevel = getXPForLevel(level)
    const xpForNextLevel = level >= MAX_LEVEL ? xpForCurrentLevel : getXPForLevel(level + 1)
    const xpToNextLevel = level >= MAX_LEVEL ? 0 : xpForNextLevel - totalXP

    const levelRange = xpForNextLevel - xpForCurrentLevel
    const xpIntoLevel = totalXP - xpForCurrentLevel
    const progressToNextLevel = levelRange > 0 ? (xpIntoLevel / levelRange) * 100 : 100

    return {
        level,
        currentXP: totalXP,
        xpForCurrentLevel,
        xpForNextLevel,
        xpToNextLevel,
        progressToNextLevel: Math.min(Math.max(progressToNextLevel, 0), 100),
    }
}

/**
 * Check if gaining XP would cause a level up
 */
export function wouldLevelUp(currentXP: number, xpGain: number): boolean {
    const currentLevel = calculateLevel(currentXP)
    const newLevel = calculateLevel(currentXP + xpGain)
    return newLevel > currentLevel
}

/**
 * Get level up info if leveling up
 */
export function getLevelUpInfo(
    currentXP: number,
    xpGain: number
): { didLevelUp: boolean; oldLevel: number; newLevel: number } | null {
    const oldLevel = calculateLevel(currentXP)
    const newLevel = calculateLevel(currentXP + xpGain)

    if (newLevel > oldLevel) {
        return { didLevelUp: true, oldLevel, newLevel }
    }

    return null
}

/* ============================================================================
   PROGRESS CALCULATIONS
   ============================================================================ */

export interface TaskForProgress {
    id: string
    xp_reward: number
    is_completed: boolean
}

export interface ModuleForProgress {
    id: string
    tasks_completed: number
    total_tasks: number
    progress: number
    is_locked: boolean
}

export interface TrackForProgress {
    id: string
    modules: ModuleForProgress[]
    progress: number
}

/**
 * Calculate module progress percentage
 */
export function calculateModuleProgress(
    tasks: TaskForProgress[],
    completedTaskIds?: string[]
): number {
    if (!tasks || tasks.length === 0) return 0

    const completed = completedTaskIds
        ? tasks.filter((t) => completedTaskIds.includes(t.id)).length
        : tasks.filter((t) => t.is_completed).length

    return Math.round((completed / tasks.length) * 100)
}

/**
 * Calculate track progress from its modules
 */
export function calculateTrackProgress(modules: ModuleForProgress[]): number {
    if (!modules || modules.length === 0) return 0

    const totalProgress = modules.reduce((sum, m) => sum + m.progress, 0)
    return Math.round(totalProgress / modules.length)
}

/**
 * Calculate overall progress from all tracks
 */
export function calculateOverallProgress(tracks: TrackForProgress[]): number {
    if (!tracks || tracks.length === 0) return 0

    const totalProgress = tracks.reduce((sum, t) => sum + t.progress, 0)
    return Math.round(totalProgress / tracks.length)
}

/**
 * Check if a module is complete
 */
export function isModuleComplete(module: ModuleForProgress): boolean {
    return module.progress === 100 || module.tasks_completed >= module.total_tasks
}

/**
 * Check if a track is complete
 */
export function isTrackComplete(track: TrackForProgress): boolean {
    return track.modules.every((m) => isModuleComplete(m))
}

/* ============================================================================
   STREAK CALCULATIONS
   ============================================================================ */

/**
 * Check if a streak is still active (activity within last 24-48 hours)
 */
export function isStreakActive(lastActivityDate: string | null): boolean {
    if (!lastActivityDate) return false

    const last = new Date(lastActivityDate)
    const now = new Date()

    const lastMidnight = new Date(last)
    lastMidnight.setHours(0, 0, 0, 0)

    const todayMidnight = new Date(now)
    todayMidnight.setHours(0, 0, 0, 0)

    const daysDiff = Math.floor(
        (todayMidnight.getTime() - lastMidnight.getTime()) / (1000 * 60 * 60 * 24)
    )

    return daysDiff <= 1
}

/**
 * Check if streak would be broken (no activity yesterday)
 */
export function isStreakBroken(lastActivityDate: string | null): boolean {
    if (!lastActivityDate) return false

    const last = new Date(lastActivityDate)
    const now = new Date()

    const lastMidnight = new Date(last)
    lastMidnight.setHours(0, 0, 0, 0)

    const todayMidnight = new Date(now)
    todayMidnight.setHours(0, 0, 0, 0)

    const daysDiff = Math.floor(
        (todayMidnight.getTime() - lastMidnight.getTime()) / (1000 * 60 * 60 * 24)
    )

    return daysDiff > 1
}

/**
 * Get streak milestone bonus XP if applicable
 */
export function getStreakBonusXP(streak: number): number {
    if (streak >= 30) return XP_REWARDS.STREAK_BONUS_30_DAYS
    if (streak >= 14) return XP_REWARDS.STREAK_BONUS_14_DAYS
    if (streak >= 7) return XP_REWARDS.STREAK_BONUS_7_DAYS
    if (streak >= 3) return XP_REWARDS.STREAK_BONUS_3_DAYS
    return 0
}

/**
 * Check if reaching a streak milestone
 */
export function isStreakMilestone(streak: number): boolean {
    return [3, 7, 14, 30, 50, 100, 365].includes(streak)
}

/* ============================================================================
   TASK COMPLETION HELPERS
   ============================================================================ */

/**
 * Calculate total XP from completing a task
 */
export function calculateTaskCompletionXP(
    taskXP: number,
    options?: {
        isModuleComplete?: boolean
        isTrackComplete?: boolean
        newStreak?: number
    }
): { totalXP: number; breakdown: { label: string; xp: number }[] } {
    const breakdown: { label: string; xp: number }[] = []

    breakdown.push({ label: "Task Complete", xp: taskXP })

    if (options?.isModuleComplete) {
        breakdown.push({ label: "Module Complete Bonus", xp: XP_REWARDS.MODULE_COMPLETE_BONUS })
    }

    if (options?.isTrackComplete) {
        breakdown.push({ label: "Track Complete Bonus", xp: XP_REWARDS.TRACK_COMPLETE_BONUS })
    }

    if (options?.newStreak && isStreakMilestone(options.newStreak)) {
        const streakXP = getStreakBonusXP(options.newStreak)
        if (streakXP > 0) {
            breakdown.push({ label: `${options.newStreak}-Day Streak Bonus`, xp: streakXP })
        }
    }

    const totalXP = breakdown.reduce((sum, item) => sum + item.xp, 0)

    return { totalXP, breakdown }
}

/**
 * Find the next unlocked task in a module
 */
export function findNextTask<T extends { id: string; is_completed: boolean }>(
    tasks: T[],
    currentTaskId: string
): T | null {
    const currentIndex = tasks.findIndex((t) => t.id === currentTaskId)
    if (currentIndex === -1) return null

    for (let i = currentIndex + 1; i < tasks.length; i++) {
        if (!tasks[i].is_completed) {
            return tasks[i]
        }
    }

    for (let i = 0; i < currentIndex; i++) {
        if (!tasks[i].is_completed) {
            return tasks[i]
        }
    }

    return null
}
