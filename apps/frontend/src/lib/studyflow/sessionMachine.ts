/**
 * ============================================================================
 * SESSION STATE MACHINE — Studyflow State Management
 * ============================================================================
 *
 * Finite state machine for managing Studyflow session states.
 *
 * States:
 * - idle: No active session
 * - setup: User configuring session settings
 * - focus: Active focus/work period
 * - break: Break period between focus sessions
 * - paused: Session temporarily paused
 * - complete: Session finished
 *
 * @phase A.6 - Studyflow Integration
 */

/* ============================================================================
   TYPES
   ============================================================================ */

export type SessionState =
    | "idle"
    | "setup"
    | "focus"
    | "break"
    | "paused"
    | "complete"

export type SessionEvent =
    | { type: "START_SETUP" }
    | { type: "START_SESSION"; payload: SessionSettings }
    | { type: "PAUSE" }
    | { type: "RESUME" }
    | { type: "FOCUS_END" }
    | { type: "BREAK_END" }
    | { type: "SKIP_BREAK" }
    | { type: "END_SESSION" }
    | { type: "RESET" }
    | { type: "COMPLETE_TASK"; payload: { taskId: string; xpEarned: number } }

export type SessionMode = "pomodoro" | "deep-focus" | "custom"

export interface SessionSettings {
    mode: SessionMode
    focusDuration: number // minutes
    breakDuration: number // minutes
    longBreakDuration: number // minutes
    sessionsUntilLongBreak: number
    autoStartBreaks: boolean
    autoStartFocus: boolean
    soundEnabled: boolean
    notificationsEnabled: boolean
    selectedTaskId?: string
}

export interface SessionContext {
    state: SessionState
    settings: SessionSettings
    currentSession: number // which focus session (1, 2, 3...)
    totalFocusTime: number // seconds accumulated
    totalBreakTime: number // seconds accumulated
    tasksCompleted: string[] // task IDs
    xpEarned: number
    startedAt: string | null // ISO timestamp
    pausedAt: string | null // ISO timestamp
    focusStartedAt: string | null // when current focus period started
    breakStartedAt: string | null // when current break period started
}

export interface SessionTransition {
    from: SessionState
    to: SessionState
    event: SessionEvent["type"]
}

/* ============================================================================
   DEFAULT VALUES
   ============================================================================ */

export const DEFAULT_SETTINGS: SessionSettings = {
    mode: "pomodoro",
    focusDuration: 25,
    breakDuration: 5,
    longBreakDuration: 15,
    sessionsUntilLongBreak: 4,
    autoStartBreaks: true,
    autoStartFocus: false,
    soundEnabled: true,
    notificationsEnabled: true,
}

export const PRESET_MODES: Record<SessionMode, Partial<SessionSettings>> = {
    pomodoro: {
        focusDuration: 25,
        breakDuration: 5,
        longBreakDuration: 15,
        sessionsUntilLongBreak: 4,
    },
    "deep-focus": {
        focusDuration: 50,
        breakDuration: 10,
        longBreakDuration: 20,
        sessionsUntilLongBreak: 2,
    },
    custom: {
        // User-defined, no preset values
    },
}

export function createInitialContext(): SessionContext {
    return {
        state: "idle",
        settings: { ...DEFAULT_SETTINGS },
        currentSession: 0,
        totalFocusTime: 0,
        totalBreakTime: 0,
        tasksCompleted: [],
        xpEarned: 0,
        startedAt: null,
        pausedAt: null,
        focusStartedAt: null,
        breakStartedAt: null,
    }
}

/* ============================================================================
   STATE MACHINE TRANSITIONS
   ============================================================================ */

/**
 * Valid state transitions
 */
const TRANSITIONS: Record<SessionState, Partial<Record<SessionEvent["type"], SessionState>>> = {
    idle: {
        START_SETUP: "setup",
    },
    setup: {
        START_SESSION: "focus",
        RESET: "idle",
    },
    focus: {
        PAUSE: "paused",
        FOCUS_END: "break",
        END_SESSION: "complete",
        COMPLETE_TASK: "focus", // Stay in focus, just update context
    },
    break: {
        PAUSE: "paused",
        BREAK_END: "focus",
        SKIP_BREAK: "focus",
        END_SESSION: "complete",
    },
    paused: {
        RESUME: "focus", // or break, depends on where we paused from
        END_SESSION: "complete",
        RESET: "idle",
    },
    complete: {
        RESET: "idle",
        START_SETUP: "setup",
    },
}

/* ============================================================================
   STATE MACHINE LOGIC
   ============================================================================ */

/**
 * Check if a transition is valid
 */
export function canTransition(
    currentState: SessionState,
    event: SessionEvent["type"]
): boolean {
    const validTransitions = TRANSITIONS[currentState]
    return validTransitions?.[event] !== undefined
}

/**
 * Get the next state for a given event
 */
export function getNextState(
    currentState: SessionState,
    event: SessionEvent["type"]
): SessionState | null {
    const validTransitions = TRANSITIONS[currentState]
    return validTransitions?.[event] ?? null
}

/**
 * Main state machine transition function
 * Returns new context or null if transition is invalid
 */
export function transition(
    context: SessionContext,
    event: SessionEvent
): SessionContext | null {
    const nextState = getNextState(context.state, event.type)

    if (!nextState) {
        console.warn(
            `[SessionMachine] Invalid transition: ${context.state} -> ${event.type}`
        )
        return null
    }

    // Create new context based on event
    const newContext: SessionContext = { ...context }
    const now = new Date().toISOString()

    switch (event.type) {
        case "START_SETUP":
            newContext.state = "setup"
            break

        case "START_SESSION":
            newContext.state = "focus"
            newContext.settings = event.payload
            newContext.currentSession = 1
            newContext.startedAt = now
            newContext.focusStartedAt = now
            newContext.totalFocusTime = 0
            newContext.totalBreakTime = 0
            newContext.tasksCompleted = []
            newContext.xpEarned = 0
            break

        case "PAUSE":
            newContext.state = "paused"
            newContext.pausedAt = now
            // Accumulate time spent so far
            if (context.state === "focus" && context.focusStartedAt) {
                const focusElapsed = Math.floor(
                    (Date.now() - new Date(context.focusStartedAt).getTime()) / 1000
                )
                newContext.totalFocusTime += focusElapsed
                newContext.focusStartedAt = null
            } else if (context.state === "break" && context.breakStartedAt) {
                const breakElapsed = Math.floor(
                    (Date.now() - new Date(context.breakStartedAt).getTime()) / 1000
                )
                newContext.totalBreakTime += breakElapsed
                newContext.breakStartedAt = null
            }
            break

        case "RESUME":
            // Resume to the state we were in before pausing
            // We need to track what state we paused from
            // For simplicity, assume we resume to focus (can be enhanced)
            newContext.state = "focus"
            newContext.pausedAt = null
            newContext.focusStartedAt = now
            break

        case "FOCUS_END":
            // Accumulate focus time
            if (context.focusStartedAt) {
                const focusElapsed = Math.floor(
                    (Date.now() - new Date(context.focusStartedAt).getTime()) / 1000
                )
                newContext.totalFocusTime += focusElapsed
            }

            // Check if it's time for a long break
            const isLongBreak =
                context.currentSession % context.settings.sessionsUntilLongBreak === 0

            newContext.state = "break"
            newContext.focusStartedAt = null
            newContext.breakStartedAt = now
            break

        case "BREAK_END":
        case "SKIP_BREAK":
            // Accumulate break time (only if not skipped or if partial)
            if (context.breakStartedAt && event.type === "BREAK_END") {
                const breakElapsed = Math.floor(
                    (Date.now() - new Date(context.breakStartedAt).getTime()) / 1000
                )
                newContext.totalBreakTime += breakElapsed
            }

            newContext.state = "focus"
            newContext.currentSession = context.currentSession + 1
            newContext.breakStartedAt = null
            newContext.focusStartedAt = now
            break

        case "END_SESSION":
            // Accumulate any remaining time
            if (context.state === "focus" && context.focusStartedAt) {
                const focusElapsed = Math.floor(
                    (Date.now() - new Date(context.focusStartedAt).getTime()) / 1000
                )
                newContext.totalFocusTime += focusElapsed
            } else if (context.state === "break" && context.breakStartedAt) {
                const breakElapsed = Math.floor(
                    (Date.now() - new Date(context.breakStartedAt).getTime()) / 1000
                )
                newContext.totalBreakTime += breakElapsed
            }

            newContext.state = "complete"
            newContext.focusStartedAt = null
            newContext.breakStartedAt = null
            break

        case "COMPLETE_TASK":
            newContext.tasksCompleted = [
                ...context.tasksCompleted,
                event.payload.taskId,
            ]
            newContext.xpEarned = context.xpEarned + event.payload.xpEarned
            // State stays the same (focus)
            break

        case "RESET":
            return createInitialContext()

        default:
            return null
    }

    newContext.state = nextState
    return newContext
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

/**
 * Check if current break should be a long break
 */
export function isLongBreak(context: SessionContext): boolean {
    return (
        context.currentSession > 0 &&
        context.currentSession % context.settings.sessionsUntilLongBreak === 0
    )
}

/**
 * Get the current break duration based on session number
 */
export function getCurrentBreakDuration(context: SessionContext): number {
    return isLongBreak(context)
        ? context.settings.longBreakDuration
        : context.settings.breakDuration
}

/**
 * Format seconds to MM:SS string
 */
export function formatTime(seconds: number): string {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`
}

/**
 * Format seconds to human-readable duration
 */
export function formatDuration(seconds: number): string {
    const hours = Math.floor(seconds / 3600)
    const mins = Math.floor((seconds % 3600) / 60)

    if (hours > 0) {
        return `${hours}h ${mins}m`
    }
    return `${mins}m`
}

/**
 * Calculate progress percentage (0-100)
 */
export function calculateProgress(
    elapsed: number,
    total: number
): number {
    if (total <= 0) return 0
    return Math.min(100, Math.max(0, (elapsed / total) * 100))
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

const sessionMachine = {
    createInitialContext,
    transition,
    canTransition,
    getNextState,
    isLongBreak,
    getCurrentBreakDuration,
    formatTime,
    formatDuration,
    calculateProgress,
}

export default sessionMachine
