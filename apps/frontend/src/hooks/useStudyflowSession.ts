/**
 * ============================================================================
 * USE STUDYFLOW SESSION — Session Management Hook
 * ============================================================================
 *
 * Comprehensive hook for managing Studyflow sessions with:
 * - State machine integration
 * - Timer management
 * - localStorage persistence
 * - Backend sync
 *
 * @phase A.6 - Studyflow Integration
 */

"use client"

import { useState, useEffect, useCallback, useRef } from "react"
import { useTimer } from "./useTimer"
import {
    type SessionContext,
    type SessionEvent,
    type SessionSettings,
    type SessionState,
    createInitialContext,
    transition,
    getCurrentBreakDuration,
    DEFAULT_SETTINGS,
    formatTime,
    formatDuration,
} from "@/lib/studyflow/sessionMachine"

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const STORAGE_KEY = "devopshub_studyflow_session"
const SETTINGS_KEY = "devopshub_studyflow_settings"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface UseStudyflowSessionReturn {
    // State
    context: SessionContext
    state: SessionState
    settings: SessionSettings
    
    // Timer
    timeRemaining: number
    timeElapsed: number
    progress: number
    formattedTime: string
    
    // Session info
    currentSession: number
    totalFocusTime: number
    totalBreakTime: number
    tasksCompleted: string[]
    xpEarned: number
    isLongBreak: boolean
    
    // Status flags
    isIdle: boolean
    isSetup: boolean
    isFocus: boolean
    isBreak: boolean
    isPaused: boolean
    isComplete: boolean
    isRunning: boolean
    
    // Actions
    startSetup: () => void
    startSession: (settings?: Partial<SessionSettings>) => void
    pause: () => void
    resume: () => void
    skipBreak: () => void
    endSession: () => void
    reset: () => void
    completeTask: (taskId: string, xpEarned: number) => void
    updateSettings: (settings: Partial<SessionSettings>) => void
    
    // Persistence
    saveSession: () => void
    restoreSession: () => boolean
    clearSession: () => void
}

/* ============================================================================
   HOOK
   ============================================================================ */

export function useStudyflowSession(): UseStudyflowSessionReturn {
    const [context, setContext] = useState<SessionContext>(createInitialContext)
    const [settings, setSettings] = useState<SessionSettings>(DEFAULT_SETTINGS)
    const [pausedFromState, setPausedFromState] = useState<"focus" | "break">("focus")
    
    // Refs for callbacks
    const contextRef = useRef(context)
    contextRef.current = context

    // Calculate timer duration based on current state
    const getTimerDuration = useCallback(() => {
        if (context.state === "focus") {
            return settings.focusDuration * 60
        } else if (context.state === "break") {
            const breakDuration = getCurrentBreakDuration({
                ...context,
                settings,
            })
            return breakDuration * 60
        }
        return settings.focusDuration * 60
    }, [context, settings])

    // Timer for focus/break periods
    const timer = useTimer({
        initialDuration: getTimerDuration(),
        autoStart: false,
        onComplete: () => {
            // Handle timer completion
            if (contextRef.current.state === "focus") {
                dispatch({ type: "FOCUS_END" })
            } else if (contextRef.current.state === "break") {
                dispatch({ type: "BREAK_END" })
            }
        },
    })

    // Dispatch event to state machine
    const dispatch = useCallback((event: SessionEvent) => {
        setContext((prev) => {
            const next = transition(prev, event)
            if (!next) return prev
            
            // Handle state-specific timer actions
            if (event.type === "START_SESSION") {
                timer.reset(event.payload.focusDuration * 60)
                timer.start()
            } else if (event.type === "FOCUS_END") {
                const breakDuration = getCurrentBreakDuration({ ...next, settings })
                timer.reset(breakDuration * 60)
                if (settings.autoStartBreaks) {
                    timer.start()
                }
            } else if (event.type === "BREAK_END" || event.type === "SKIP_BREAK") {
                timer.reset(settings.focusDuration * 60)
                if (settings.autoStartFocus) {
                    timer.start()
                }
            } else if (event.type === "PAUSE") {
                timer.pause()
                setPausedFromState(prev.state === "break" ? "break" : "focus")
            } else if (event.type === "RESUME") {
                timer.resume()
            } else if (event.type === "END_SESSION") {
                timer.pause()
            } else if (event.type === "RESET") {
                timer.reset()
            }
            
            return next
        })
    }, [timer, settings])

    // Load settings from localStorage on mount
    useEffect(() => {
        const savedSettings = localStorage.getItem(SETTINGS_KEY)
        if (savedSettings) {
            try {
                const parsed = JSON.parse(savedSettings)
                setSettings((prev) => ({ ...prev, ...parsed }))
            } catch {
                // Ignore parse errors
            }
        }
    }, [])

    // Save settings when they change
    useEffect(() => {
        localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings))
    }, [settings])

    // Actions
    const startSetup = useCallback(() => {
        dispatch({ type: "START_SETUP" })
    }, [dispatch])

    const startSession = useCallback((partialSettings?: Partial<SessionSettings>) => {
        const sessionSettings = { ...settings, ...partialSettings }
        setSettings(sessionSettings)
        dispatch({ type: "START_SESSION", payload: sessionSettings })
    }, [dispatch, settings])

    const pause = useCallback(() => {
        dispatch({ type: "PAUSE" })
    }, [dispatch])

    const resume = useCallback(() => {
        dispatch({ type: "RESUME" })
    }, [dispatch])

    const skipBreak = useCallback(() => {
        dispatch({ type: "SKIP_BREAK" })
    }, [dispatch])

    const endSession = useCallback(() => {
        dispatch({ type: "END_SESSION" })
    }, [dispatch])

    const reset = useCallback(() => {
        dispatch({ type: "RESET" })
    }, [dispatch])

    const completeTask = useCallback((taskId: string, xpEarned: number) => {
        dispatch({ type: "COMPLETE_TASK", payload: { taskId, xpEarned } })
    }, [dispatch])

    const updateSettings = useCallback((newSettings: Partial<SessionSettings>) => {
        setSettings((prev) => ({ ...prev, ...newSettings }))
    }, [])

    // Persistence
    const saveSession = useCallback(() => {
        const sessionData = {
            context,
            settings,
            timerRemaining: timer.remaining,
            pausedFromState,
            savedAt: new Date().toISOString(),
        }
        localStorage.setItem(STORAGE_KEY, JSON.stringify(sessionData))
    }, [context, settings, timer.remaining, pausedFromState])

    const restoreSession = useCallback((): boolean => {
        const saved = localStorage.getItem(STORAGE_KEY)
        if (!saved) return false

        try {
            const data = JSON.parse(saved)
            
            // Check if session is still valid (not too old)
            const savedAt = new Date(data.savedAt)
            const hoursSinceSave = (Date.now() - savedAt.getTime()) / (1000 * 60 * 60)
            
            // Don't restore sessions older than 2 hours
            if (hoursSinceSave > 2) {
                localStorage.removeItem(STORAGE_KEY)
                return false
            }

            setContext(data.context)
            setSettings(data.settings)
            setPausedFromState(data.pausedFromState || "focus")
            
            // Restore timer state
            if (data.context.state === "focus" || data.context.state === "break") {
                timer.reset(data.timerRemaining)
                // Don't auto-start, let user resume
            }
            
            return true
        } catch {
            localStorage.removeItem(STORAGE_KEY)
            return false
        }
    }, [timer])

    const clearSession = useCallback(() => {
        localStorage.removeItem(STORAGE_KEY)
    }, [])

    // Auto-save on state changes
    useEffect(() => {
        if (context.state !== "idle" && context.state !== "complete") {
            saveSession()
        }
    }, [context, saveSession])

    // Clean up saved session on complete
    useEffect(() => {
        if (context.state === "complete") {
            clearSession()
        }
    }, [context.state, clearSession])

    // Derived state
    const isLongBreak = 
        context.currentSession > 0 &&
        context.currentSession % settings.sessionsUntilLongBreak === 0

    return {
        // State
        context,
        state: context.state,
        settings,
        
        // Timer
        timeRemaining: timer.remaining,
        timeElapsed: timer.elapsed,
        progress: timer.progress,
        formattedTime: formatTime(timer.remaining),
        
        // Session info
        currentSession: context.currentSession,
        totalFocusTime: context.totalFocusTime,
        totalBreakTime: context.totalBreakTime,
        tasksCompleted: context.tasksCompleted,
        xpEarned: context.xpEarned,
        isLongBreak,
        
        // Status flags
        isIdle: context.state === "idle",
        isSetup: context.state === "setup",
        isFocus: context.state === "focus",
        isBreak: context.state === "break",
        isPaused: context.state === "paused",
        isComplete: context.state === "complete",
        isRunning: timer.isRunning && !timer.isPaused,
        
        // Actions
        startSetup,
        startSession,
        pause,
        resume,
        skipBreak,
        endSession,
        reset,
        completeTask,
        updateSettings,
        
        // Persistence
        saveSession,
        restoreSession,
        clearSession,
    }
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default useStudyflowSession
