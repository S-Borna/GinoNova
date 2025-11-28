/**
 * ============================================================================
 * USE TIMER — Timer Hook for Studyflow
 * ============================================================================
 *
 * Hook for managing countdown timer with pause/resume functionality.
 *
 * Features:
 * - Countdown from specified duration
 * - Pause/resume
 * - Progress percentage
 * - Callbacks for completion
 * - Tick callback for updates
 *
 * @phase A.6 - Studyflow Integration
 */

"use client"

import { useState, useEffect, useCallback, useRef } from "react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface UseTimerOptions {
    /** Initial duration in seconds */
    initialDuration: number
    /** Callback when timer completes */
    onComplete?: () => void
    /** Callback on each tick (every second) */
    onTick?: (remaining: number) => void
    /** Auto-start the timer */
    autoStart?: boolean
}

export interface UseTimerReturn {
    /** Time remaining in seconds */
    remaining: number
    /** Total duration in seconds */
    duration: number
    /** Elapsed time in seconds */
    elapsed: number
    /** Progress percentage (0-100) */
    progress: number
    /** Whether timer is running */
    isRunning: boolean
    /** Whether timer is paused */
    isPaused: boolean
    /** Whether timer has completed */
    isComplete: boolean
    /** Start the timer */
    start: () => void
    /** Pause the timer */
    pause: () => void
    /** Resume the timer */
    resume: () => void
    /** Reset the timer to initial duration */
    reset: (newDuration?: number) => void
    /** Add time to the timer */
    addTime: (seconds: number) => void
    /** Skip to completion */
    skip: () => void
}

/* ============================================================================
   HOOK
   ============================================================================ */

export function useTimer({
    initialDuration,
    onComplete,
    onTick,
    autoStart = false,
}: UseTimerOptions): UseTimerReturn {
    const [duration, setDuration] = useState(initialDuration)
    const [remaining, setRemaining] = useState(initialDuration)
    const [isRunning, setIsRunning] = useState(autoStart)
    const [isPaused, setIsPaused] = useState(false)
    const [isComplete, setIsComplete] = useState(false)

    // Refs for callbacks to avoid stale closures
    const onCompleteRef = useRef(onComplete)
    const onTickRef = useRef(onTick)

    // Update refs when callbacks change
    useEffect(() => {
        onCompleteRef.current = onComplete
    }, [onComplete])

    useEffect(() => {
        onTickRef.current = onTick
    }, [onTick])

    // Timer interval effect
    useEffect(() => {
        if (!isRunning || isPaused || isComplete) return

        const intervalId = setInterval(() => {
            setRemaining((prev) => {
                const newRemaining = prev - 1

                // Call tick callback
                onTickRef.current?.(newRemaining)

                // Check for completion
                if (newRemaining <= 0) {
                    setIsRunning(false)
                    setIsComplete(true)
                    onCompleteRef.current?.()
                    return 0
                }

                return newRemaining
            })
        }, 1000)

        return () => clearInterval(intervalId)
    }, [isRunning, isPaused, isComplete])

    // Reset when initial duration changes
    useEffect(() => {
        setDuration(initialDuration)
        setRemaining(initialDuration)
        setIsComplete(false)
        if (autoStart) {
            setIsRunning(true)
            setIsPaused(false)
        }
    }, [initialDuration, autoStart])

    const start = useCallback(() => {
        setIsRunning(true)
        setIsPaused(false)
        setIsComplete(false)
    }, [])

    const pause = useCallback(() => {
        setIsPaused(true)
    }, [])

    const resume = useCallback(() => {
        setIsPaused(false)
    }, [])

    const reset = useCallback((newDuration?: number) => {
        const dur = newDuration ?? initialDuration
        setDuration(dur)
        setRemaining(dur)
        setIsRunning(false)
        setIsPaused(false)
        setIsComplete(false)
    }, [initialDuration])

    const addTime = useCallback((seconds: number) => {
        setRemaining((prev) => Math.max(0, prev + seconds))
        setDuration((prev) => prev + seconds)
    }, [])

    const skip = useCallback(() => {
        setRemaining(0)
        setIsRunning(false)
        setIsComplete(true)
        onCompleteRef.current?.()
    }, [])

    // Calculate derived values
    const elapsed = duration - remaining
    const progress = duration > 0 ? ((duration - remaining) / duration) * 100 : 0

    return {
        remaining,
        duration,
        elapsed,
        progress,
        isRunning,
        isPaused,
        isComplete,
        start,
        pause,
        resume,
        reset,
        addTime,
        skip,
    }
}

/* ============================================================================
   HELPER HOOKS
   ============================================================================ */

/**
 * Hook for managing a Pomodoro-style timer with focus and break phases
 */
export interface UsePomodoroOptions {
    focusDuration: number // minutes
    breakDuration: number // minutes
    longBreakDuration: number // minutes
    sessionsUntilLongBreak: number
    onFocusComplete?: () => void
    onBreakComplete?: () => void
    onSessionComplete?: (sessions: number) => void
}

export interface UsePomodoroReturn extends UseTimerReturn {
    phase: "focus" | "break"
    currentSession: number
    isLongBreak: boolean
    startFocus: () => void
    startBreak: () => void
    skipPhase: () => void
}

export function usePomodoro({
    focusDuration,
    breakDuration,
    longBreakDuration,
    sessionsUntilLongBreak,
    onFocusComplete,
    onBreakComplete,
    onSessionComplete,
}: UsePomodoroOptions): UsePomodoroReturn {
    const [phase, setPhase] = useState<"focus" | "break">("focus")
    const [currentSession, setCurrentSession] = useState(1)

    const isLongBreak = currentSession % sessionsUntilLongBreak === 0
    const currentBreakDuration = isLongBreak ? longBreakDuration : breakDuration

    const currentDuration =
        phase === "focus"
            ? focusDuration * 60
            : currentBreakDuration * 60

    const handleComplete = useCallback(() => {
        if (phase === "focus") {
            onFocusComplete?.()
            setPhase("break")
        } else {
            onBreakComplete?.()
            setPhase("focus")
            setCurrentSession((prev) => {
                const newSession = prev + 1
                onSessionComplete?.(newSession)
                return newSession
            })
        }
    }, [phase, onFocusComplete, onBreakComplete, onSessionComplete])

    const timer = useTimer({
        initialDuration: currentDuration,
        onComplete: handleComplete,
    })

    const startFocus = useCallback(() => {
        setPhase("focus")
        timer.reset(focusDuration * 60)
        timer.start()
    }, [focusDuration, timer])

    const startBreak = useCallback(() => {
        setPhase("break")
        timer.reset(currentBreakDuration * 60)
        timer.start()
    }, [currentBreakDuration, timer])

    const skipPhase = useCallback(() => {
        timer.skip()
    }, [timer])

    return {
        ...timer,
        phase,
        currentSession,
        isLongBreak,
        startFocus,
        startBreak,
        skipPhase,
    }
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default useTimer
