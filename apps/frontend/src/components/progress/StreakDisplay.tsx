/**
 * ============================================================================
 * STREAK DISPLAY — Shows Current Learning Streak
 * ============================================================================
 *
 * Displays the user's current daily learning streak with visual flair.
 * Shows flame icon with animated effects when streak is active.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { motion } from "framer-motion"
import { Flame, Calendar } from "lucide-react"
import { cn } from "@/lib/utils"
import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger,
} from "@/components/ui/tooltip"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StreakDisplayProps {
    currentStreak: number
    longestStreak?: number
    lastActivityDate?: string
    isActiveToday?: boolean
    variant?: "default" | "compact" | "badge"
    className?: string
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function StreakDisplay({
    currentStreak,
    longestStreak,
    lastActivityDate,
    isActiveToday = false,
    variant = "default",
    className,
}: StreakDisplayProps) {
    // Determine streak status
    const isStreakAtRisk = !isActiveToday && currentStreak > 0
    const hasStreak = currentStreak > 0
    const isMilestone = currentStreak > 0 && currentStreak % 7 === 0 // Weekly milestone

    // Get flame color based on streak length
    const getFlameColor = () => {
        if (!hasStreak) return "text-muted-foreground"
        if (currentStreak >= 30) return "text-orange-500"
        if (currentStreak >= 14) return "text-amber-500"
        if (currentStreak >= 7) return "text-yellow-500"
        return "text-orange-400"
    }

    // Compact badge variant
    if (variant === "badge") {
        return (
            <TooltipProvider>
                <Tooltip>
                    <TooltipTrigger asChild>
                        <motion.div
                            initial={{ scale: 0.9 }}
                            animate={{ scale: 1 }}
                            className={cn(
                                "flex items-center gap-1.5 px-2 py-1 rounded-full",
                                hasStreak
                                    ? "bg-orange-500/10 border border-orange-500/20"
                                    : "bg-muted/50 border border-border",
                                isStreakAtRisk && "animate-pulse",
                                className
                            )}
                        >
                            <Flame
                                className={cn(
                                    "w-4 h-4",
                                    getFlameColor(),
                                    hasStreak && isActiveToday && "animate-bounce"
                                )}
                            />
                            <span
                                className={cn(
                                    "text-sm font-bold",
                                    hasStreak ? "text-orange-500" : "text-muted-foreground"
                                )}
                            >
                                {currentStreak}
                            </span>
                        </motion.div>
                    </TooltipTrigger>
                    <TooltipContent>
                        <p>
                            {hasStreak
                                ? `${currentStreak} day streak! ${isStreakAtRisk ? "Complete a task today to keep it!" : ""}`
                                : "Start learning to build your streak!"}
                        </p>
                    </TooltipContent>
                </Tooltip>
            </TooltipProvider>
        )
    }

    // Compact variant
    if (variant === "compact") {
        return (
            <div className={cn("flex items-center gap-2", className)}>
                <div
                    className={cn(
                        "flex items-center gap-1.5 px-3 py-1.5 rounded-lg",
                        hasStreak
                            ? "bg-gradient-to-r from-orange-500/10 to-amber-500/10"
                            : "bg-muted"
                    )}
                >
                    <motion.div
                        animate={
                            hasStreak && isActiveToday
                                ? {
                                    scale: [1, 1.2, 1],
                                    rotate: [0, -5, 5, 0],
                                }
                                : {}
                        }
                        transition={{
                            duration: 1,
                            repeat: Infinity,
                            repeatDelay: 2,
                        }}
                    >
                        <Flame className={cn("w-5 h-5", getFlameColor())} />
                    </motion.div>
                    <span
                        className={cn(
                            "text-lg font-bold",
                            hasStreak ? "text-orange-500" : "text-muted-foreground"
                        )}
                    >
                        {currentStreak}
                    </span>
                    <span className="text-sm text-muted-foreground">day streak</span>
                </div>
                {isStreakAtRisk && (
                    <span className="text-xs text-amber-500 animate-pulse">
                        Learn today to keep your streak!
                    </span>
                )}
            </div>
        )
    }

    // Default full variant
    return (
        <div
            className={cn(
                "p-6 rounded-xl",
                "bg-gradient-to-br from-orange-500/10 via-amber-500/5 to-transparent",
                "border border-orange-500/20",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-white">Learning Streak</h3>
                {longestStreak !== undefined && (
                    <span className="text-sm text-muted-foreground">
                        Best: {longestStreak} days
                    </span>
                )}
            </div>

            {/* Main streak display */}
            <div className="flex items-center gap-4 mb-4">
                <motion.div
                    animate={
                        hasStreak && isActiveToday
                            ? {
                                scale: [1, 1.1, 1],
                            }
                            : {}
                    }
                    transition={{
                        duration: 1.5,
                        repeat: Infinity,
                        repeatType: "reverse",
                    }}
                    className={cn(
                        "w-16 h-16 rounded-full flex items-center justify-center",
                        hasStreak
                            ? "bg-gradient-to-br from-orange-500 to-amber-500 shadow-lg shadow-orange-500/30"
                            : "bg-muted"
                    )}
                >
                    <Flame
                        className={cn(
                            "w-8 h-8",
                            hasStreak ? "text-white" : "text-muted-foreground"
                        )}
                    />
                </motion.div>

                <div>
                    <motion.div
                        key={currentStreak}
                        initial={{ scale: 1.5, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        className="flex items-baseline gap-2"
                    >
                        <span
                            className={cn(
                                "text-4xl font-bold",
                                hasStreak
                                    ? "text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-amber-400"
                                    : "text-muted-foreground"
                            )}
                        >
                            {currentStreak}
                        </span>
                        <span className="text-lg text-muted-foreground">
                            {currentStreak === 1 ? "day" : "days"}
                        </span>
                    </motion.div>

                    <p className="text-sm text-muted-foreground mt-1">
                        {!hasStreak
                            ? "Start learning to build your streak!"
                            : isActiveToday
                                ? "Great job! You've learned today."
                                : "Complete a task today to extend your streak!"}
                    </p>
                </div>
            </div>

            {/* Week progress */}
            <div className="space-y-2">
                <div className="flex items-center justify-between text-sm">
                    <span className="text-muted-foreground flex items-center gap-1.5">
                        <Calendar className="w-4 h-4" />
                        This week
                    </span>
                    {isMilestone && (
                        <span className="text-amber-400 text-xs font-medium">
                            🎉 Weekly milestone!
                        </span>
                    )}
                </div>
                <WeekProgress isActiveToday={isActiveToday} currentStreak={currentStreak} />
            </div>

            {/* Streak at risk warning */}
            {isStreakAtRisk && (
                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "mt-4 p-3 rounded-lg",
                        "bg-amber-500/10 border border-amber-500/20"
                    )}
                >
                    <p className="text-sm text-amber-400">
                        ⚠️ Your streak is at risk! Complete at least one task today.
                    </p>
                </motion.div>
            )}
        </div>
    )
}

/* ============================================================================
   WEEK PROGRESS COMPONENT
   ============================================================================ */

interface WeekProgressProps {
    isActiveToday: boolean
    currentStreak: number
}

function WeekProgress({ isActiveToday, currentStreak }: WeekProgressProps) {
    const days = ["M", "T", "W", "T", "F", "S", "S"]
    const today = new Date().getDay()
    // Convert to Monday-start (0 = Monday, 6 = Sunday)
    const todayIndex = today === 0 ? 6 : today - 1

    // Simple visualization - shows active days based on streak
    const activeDays = Math.min(currentStreak, 7)
    const startIndex = Math.max(0, todayIndex - activeDays + (isActiveToday ? 1 : 0))

    return (
        <div className="flex items-center gap-1.5">
            {days.map((day, index) => {
                const isToday = index === todayIndex
                const isActive =
                    index >= startIndex &&
                    index <= todayIndex &&
                    (index < todayIndex || isActiveToday)

                return (
                    <div key={index} className="flex-1 flex flex-col items-center gap-1">
                        <motion.div
                            initial={false}
                            animate={{
                                backgroundColor: isActive
                                    ? "rgb(249, 115, 22)"
                                    : isToday
                                        ? "rgb(249, 115, 22, 0.3)"
                                        : "rgb(255, 255, 255, 0.1)",
                                scale: isToday ? 1.1 : 1,
                            }}
                            className={cn(
                                "w-full h-8 rounded-lg flex items-center justify-center",
                                isToday && !isActive && "border-2 border-orange-500/50"
                            )}
                        >
                            {isActive && (
                                <Flame className="w-4 h-4 text-white" />
                            )}
                        </motion.div>
                        <span
                            className={cn(
                                "text-xs",
                                isToday ? "text-white font-medium" : "text-muted-foreground"
                            )}
                        >
                            {day}
                        </span>
                    </div>
                )
            })}
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default StreakDisplay
