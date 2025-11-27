"use client"

/**
 * ============================================================================
 * STREAK DISPLAY COMPONENT - Gamification Element
 * ============================================================================
 * 
 * Features:
 * - Animated flame icon
 * - Day count with "X day streak!" text
 * - Calendar preview (last 7 days)
 * - Motivational messages
 * 
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { Flame, CheckCircle2 } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface StreakDisplayProps {
    /** Number of consecutive days */
    streak: number
    /** Calendar data for the last 7 days */
    lastWeek?: boolean[]
    /** Compact mode for sidebar */
    compact?: boolean
    /** Optional className */
    className?: string
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const MOTIVATIONAL_MESSAGES = [
    { min: 0, max: 0, message: "Start your streak today!" },
    { min: 1, max: 2, message: "Great start! Keep it going!" },
    { min: 3, max: 6, message: "You're on fire! 🔥" },
    { min: 7, max: 13, message: "A full week! Impressive!" },
    { min: 14, max: 29, message: "Two weeks strong! 💪" },
    { min: 30, max: 59, message: "One month champion! 🏆" },
    { min: 60, max: 89, message: "Unstoppable force! ⚡" },
    { min: 90, max: Infinity, message: "Legend status achieved! 👑" },
]

const DAYS = ["M", "T", "W", "T", "F", "S", "S"]

function getMotivationalMessage(streak: number): string {
    const msg = MOTIVATIONAL_MESSAGES.find(m => streak >= m.min && streak <= m.max)
    return msg?.message || "Keep going!"
}

/* ============================================================================
   FLAME ICON WITH ANIMATION
   ============================================================================ */

interface AnimatedFlameProps {
    streak: number
    size?: "sm" | "md" | "lg"
}

function AnimatedFlame({ streak, size = "md" }: AnimatedFlameProps) {
    const sizeClasses = {
        sm: "h-6 w-6",
        md: "h-10 w-10",
        lg: "h-16 w-16",
    }

    const containerClasses = {
        sm: "h-10 w-10",
        md: "h-16 w-16",
        lg: "h-24 w-24",
    }

    // Flame intensity based on streak
    const intensity = Math.min(streak / 30, 1) // Max at 30 days
    const glowOpacity = 0.3 + intensity * 0.4

    return (
        <div className={cn(
            "relative flex items-center justify-center rounded-full",
            containerClasses[size],
            streak > 0
                ? "bg-gradient-to-br from-amber-100 to-orange-100 dark:from-amber-900/30 dark:to-orange-900/30"
                : "bg-neutral-100 dark:bg-neutral-800"
        )}>
            {/* Glow effect */}
            {streak > 0 && (
                <div
                    className="absolute inset-0 rounded-full bg-gradient-to-br from-amber-400 to-orange-500 blur-xl"
                    style={{ opacity: glowOpacity }}
                />
            )}
            
            {/* Flame icon */}
            <Flame
                className={cn(
                    sizeClasses[size],
                    "relative z-10",
                    streak > 0
                        ? "text-orange-500 dark:text-orange-400 animate-pulse"
                        : "text-neutral-400 dark:text-neutral-500"
                )}
                style={{
                    animationDuration: streak > 7 ? "1s" : "2s",
                }}
            />
        </div>
    )
}

/* ============================================================================
   CALENDAR PREVIEW
   ============================================================================ */

interface CalendarPreviewProps {
    lastWeek: boolean[]
}

function CalendarPreview({ lastWeek }: CalendarPreviewProps) {
    // Ensure we have 7 days
    const days = lastWeek.slice(0, 7)
    while (days.length < 7) {
        days.unshift(false)
    }

    return (
        <div className="flex items-center gap-1">
            {DAYS.map((day, index) => {
                const isComplete = days[index]
                return (
                    <div
                        key={index}
                        className="flex flex-col items-center gap-1"
                    >
                        <span className="text-xs text-neutral-400 dark:text-neutral-500 font-medium">
                            {day}
                        </span>
                        <div
                            className={cn(
                                "h-7 w-7 rounded-full flex items-center justify-center transition-colors",
                                isComplete
                                    ? "bg-emerald-100 dark:bg-emerald-900/30"
                                    : "bg-neutral-100 dark:bg-neutral-800"
                            )}
                        >
                            {isComplete ? (
                                <CheckCircle2 className="h-4 w-4 text-emerald-500" />
                            ) : (
                                <div className="h-2 w-2 rounded-full bg-neutral-300 dark:bg-neutral-600" />
                            )}
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

/* ============================================================================
   COMPACT STREAK DISPLAY
   ============================================================================ */

function CompactStreak({ streak }: { streak: number }) {
    return (
        <div className="flex items-center gap-3">
            <AnimatedFlame streak={streak} size="sm" />
            <div>
                <div className="flex items-baseline gap-1">
                    <span className="text-2xl font-bold text-neutral-900 dark:text-white">
                        {streak}
                    </span>
                    <span className="text-sm text-neutral-500 dark:text-neutral-400">
                        day{streak !== 1 ? "s" : ""}
                    </span>
                </div>
                <p className="text-xs text-amber-600 dark:text-amber-400 font-medium">
                    {streak > 0 ? "🔥 On fire!" : "Start today!"}
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN STREAK DISPLAY COMPONENT
   ============================================================================ */

export function StreakDisplay({
    streak,
    lastWeek = [true, true, true, false, true, true, true], // Mock default
    compact = false,
    className,
}: StreakDisplayProps) {
    if (compact) {
        return (
            <div className={className}>
                <CompactStreak streak={streak} />
            </div>
        )
    }

    return (
        <div className={cn("text-center space-y-4", className)}>
            {/* Flame & Count */}
            <div className="flex flex-col items-center gap-2">
                <AnimatedFlame streak={streak} size="lg" />
                <div className="flex items-baseline gap-2">
                    <span className="text-5xl font-bold text-neutral-900 dark:text-white">
                        {streak}
                    </span>
                    <span className="text-xl text-neutral-500 dark:text-neutral-400">
                        day{streak !== 1 ? "s" : ""}
                    </span>
                </div>
                <p className="text-sm font-medium text-amber-600 dark:text-amber-400">
                    {getMotivationalMessage(streak)}
                </p>
            </div>

            {/* Calendar Preview */}
            <div className="pt-4 border-t border-neutral-200 dark:border-neutral-700">
                <p className="text-xs text-neutral-500 dark:text-neutral-400 mb-3 uppercase tracking-wider">
                    Last 7 Days
                </p>
                <div className="flex justify-center">
                    <CalendarPreview lastWeek={lastWeek} />
                </div>
            </div>
        </div>
    )
}

export default StreakDisplay
