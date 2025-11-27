"use client"

/**
 * ============================================================================
 * TIMER COMPONENT - Circular Progress Timer
 * ============================================================================
 * 
 * Apple Watch-style circular timer with:
 * - SVG progress ring that depletes
 * - Gradient ring colors
 * - Pulse animation when < 1 min left
 * - High contrast time display
 * 
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TimerProps {
    /** Total time in seconds */
    totalSeconds: number
    /** Remaining time in seconds */
    remainingSeconds: number
    /** Whether the timer is in break mode */
    isBreak?: boolean
    /** Size of the timer (diameter in pixels) */
    size?: number
    /** Optional className */
    className?: string
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function formatTime(seconds: number): { minutes: string; seconds: string } {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return {
        minutes: mins.toString().padStart(2, "0"),
        seconds: secs.toString().padStart(2, "0"),
    }
}

/* ============================================================================
   TIMER COMPONENT
   ============================================================================ */

export function Timer({
    totalSeconds,
    remainingSeconds,
    isBreak = false,
    size = 280,
    className,
}: TimerProps) {
    // Calculate progress (0-1)
    const progress = totalSeconds > 0 ? remainingSeconds / totalSeconds : 0
    
    // SVG circle calculations
    const strokeWidth = 12
    const radius = (size - strokeWidth) / 2
    const circumference = 2 * Math.PI * radius
    const strokeDashoffset = circumference * (1 - progress)
    
    // Time formatting
    const time = formatTime(remainingSeconds)
    
    // Low time warning (< 60 seconds)
    const isLowTime = remainingSeconds > 0 && remainingSeconds < 60
    
    // Colors based on mode
    const gradientId = isBreak ? "breakGradient" : "focusGradient"
    const focusColors = { start: "#6366f1", end: "#8b5cf6" } // Primary purple
    const breakColors = { start: "#22c55e", end: "#10b981" } // Green
    const colors = isBreak ? breakColors : focusColors

    return (
        <div className={cn("relative inline-flex items-center justify-center", className)}>
            {/* SVG Timer Ring */}
            <svg
                width={size}
                height={size}
                className="transform -rotate-90"
            >
                {/* Gradient Definition */}
                <defs>
                    <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stopColor={colors.start} />
                        <stop offset="100%" stopColor={colors.end} />
                    </linearGradient>
                    
                    {/* Glow filter */}
                    <filter id="timerGlow" x="-50%" y="-50%" width="200%" height="200%">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
                        <feMerge>
                            <feMergeNode in="blur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                </defs>

                {/* Background track */}
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={strokeWidth}
                    className="text-neutral-200 dark:text-neutral-700"
                />

                {/* Progress ring */}
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke={`url(#${gradientId})`}
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={strokeDashoffset}
                    filter="url(#timerGlow)"
                    className={cn(
                        "transition-all duration-1000 ease-linear",
                        isLowTime && "animate-pulse"
                    )}
                />
            </svg>

            {/* Time Display - Centered */}
            <div className="absolute inset-0 flex flex-col items-center justify-center">
                {/* Time */}
                <div className={cn(
                    "flex items-baseline gap-1 font-mono tabular-nums",
                    isLowTime && "animate-pulse"
                )}>
                    <span className={cn(
                        "text-6xl font-bold tracking-tight",
                        isBreak 
                            ? "text-emerald-600 dark:text-emerald-400"
                            : "text-neutral-900 dark:text-white"
                    )}>
                        {time.minutes}
                    </span>
                    <span className={cn(
                        "text-4xl font-bold",
                        isBreak 
                            ? "text-emerald-600/80 dark:text-emerald-400/80"
                            : "text-neutral-500"
                    )}>
                        :
                    </span>
                    <span className={cn(
                        "text-6xl font-bold tracking-tight",
                        isBreak 
                            ? "text-emerald-600 dark:text-emerald-400"
                            : "text-neutral-900 dark:text-white"
                    )}>
                        {time.seconds}
                    </span>
                </div>

                {/* Phase Label */}
                <span className={cn(
                    "mt-2 text-sm font-medium uppercase tracking-wider",
                    isBreak 
                        ? "text-emerald-500 dark:text-emerald-400"
                        : "text-primary-500 dark:text-primary-400"
                )}>
                    {isBreak ? "Break Time" : "Focus Time"}
                </span>
            </div>

            {/* Ambient Glow Effect */}
            <div
                className={cn(
                    "absolute inset-0 rounded-full opacity-20 blur-3xl pointer-events-none",
                    isBreak
                        ? "bg-gradient-to-br from-emerald-400 to-green-500"
                        : "bg-gradient-to-br from-primary-400 to-primary-600"
                )}
                style={{
                    transform: "scale(1.1)",
                }}
            />
        </div>
    )
}

/* ============================================================================
   MINI TIMER - Compact version for sidebar/stats
   ============================================================================ */

export interface MiniTimerProps {
    remainingSeconds: number
    totalSeconds: number
    isBreak?: boolean
    className?: string
}

export function MiniTimer({
    remainingSeconds,
    totalSeconds,
    isBreak = false,
    className,
}: MiniTimerProps) {
    const time = formatTime(remainingSeconds)
    const progress = totalSeconds > 0 ? remainingSeconds / totalSeconds : 0
    const circumference = 2 * Math.PI * 18 // radius 18
    const strokeDashoffset = circumference * (1 - progress)

    return (
        <div className={cn("inline-flex items-center gap-2", className)}>
            {/* Mini Ring */}
            <svg width="44" height="44" className="transform -rotate-90">
                <circle
                    cx="22"
                    cy="22"
                    r="18"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="4"
                    className="text-neutral-200 dark:text-neutral-700"
                />
                <circle
                    cx="22"
                    cy="22"
                    r="18"
                    fill="none"
                    stroke={isBreak ? "#22c55e" : "#6366f1"}
                    strokeWidth="4"
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={strokeDashoffset}
                    className="transition-all duration-1000 ease-linear"
                />
            </svg>

            {/* Time */}
            <span className={cn(
                "font-mono font-semibold tabular-nums",
                isBreak 
                    ? "text-emerald-600 dark:text-emerald-400"
                    : "text-neutral-900 dark:text-white"
            )}>
                {time.minutes}:{time.seconds}
            </span>
        </div>
    )
}

export default Timer
