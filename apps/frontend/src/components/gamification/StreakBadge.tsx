"use client"

/**
 * ============================================================================
 * STREAK BADGE - Premium Gamification Component ✨
 * ============================================================================
 *
 * Visual streak indicator with:
 * - Fire animation for active streaks
 * - Milestone celebrations
 * - Premium glow effects
 *
 * @phase Premium Polish v1.0
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { Flame, Zap, Trophy } from "lucide-react"

// ============================================================================
// TYPES
// ============================================================================

interface StreakBadgeProps {
    currentStreak: number
    bestStreak?: number
    className?: string
    size?: "sm" | "md" | "lg"
    showLabel?: boolean
}

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

function getStreakLevel(streak: number): {
    level: string
    color: string
    bgColor: string
    glowColor: string
    icon: typeof Flame
} {
    if (streak >= 30) return {
        level: "Legendary",
        color: "text-purple-400",
        bgColor: "bg-purple-500/20",
        glowColor: "shadow-[0_0_20px_rgba(139,92,246,0.5)]",
        icon: Trophy,
    }
    if (streak >= 14) return {
        level: "Epic",
        color: "text-amber-400",
        bgColor: "bg-amber-500/20",
        glowColor: "shadow-[0_0_20px_rgba(245,158,11,0.5)]",
        icon: Zap,
    }
    if (streak >= 7) return {
        level: "Hot",
        color: "text-orange-400",
        bgColor: "bg-orange-500/20",
        glowColor: "shadow-[0_0_20px_rgba(249,115,22,0.4)]",
        icon: Flame,
    }
    if (streak >= 3) return {
        level: "Warming Up",
        color: "text-yellow-400",
        bgColor: "bg-yellow-500/20",
        glowColor: "shadow-[0_0_15px_rgba(250,204,21,0.3)]",
        icon: Flame,
    }
    return {
        level: "Starting",
        color: "text-zinc-400",
        bgColor: "bg-zinc-500/20",
        glowColor: "",
        icon: Flame,
    }
}

// ============================================================================
// COMPONENT
// ============================================================================

export function StreakBadge({
    currentStreak,
    bestStreak,
    className,
    size = "md",
    showLabel = true,
}: StreakBadgeProps) {
    const streakInfo = getStreakLevel(currentStreak)
    const Icon = streakInfo.icon

    const sizeClasses = {
        sm: {
            container: "px-2 py-1 gap-1.5",
            icon: "w-4 h-4",
            text: "text-sm",
            label: "text-[10px]",
        },
        md: {
            container: "px-3 py-1.5 gap-2",
            icon: "w-5 h-5",
            text: "text-base",
            label: "text-xs",
        },
        lg: {
            container: "px-4 py-2 gap-3",
            icon: "w-6 h-6",
            text: "text-lg",
            label: "text-sm",
        },
    }

    const sizes = sizeClasses[size]

    return (
        <div
            className={cn(
                "inline-flex items-center rounded-full",
                "border border-zinc-700/50",
                "bg-zinc-900/80 backdrop-blur-sm",
                streakInfo.glowColor,
                "transition-all duration-300",
                "hover:scale-105",
                sizes.container,
                className
            )}
        >
            {/* Animated Icon */}
            <div className={cn(
                "relative flex items-center justify-center",
                streakInfo.bgColor,
                "rounded-full p-1"
            )}>
                <Icon className={cn(
                    sizes.icon,
                    streakInfo.color,
                    currentStreak >= 3 && "animate-pulse"
                )} />

                {/* Fire particles for hot streaks */}
                {currentStreak >= 7 && (
                    <>
                        <span className="absolute -top-1 -right-1 w-1.5 h-1.5 rounded-full bg-orange-400 animate-ping" />
                        <span className="absolute -bottom-1 -left-1 w-1 h-1 rounded-full bg-yellow-400 animate-ping" style={{ animationDelay: "200ms" }} />
                    </>
                )}
            </div>

            {/* Streak Count */}
            <div className="flex flex-col">
                <span className={cn(
                    "font-bold leading-none",
                    sizes.text,
                    streakInfo.color
                )}>
                    {currentStreak} day{currentStreak !== 1 ? "s" : ""}
                </span>
                {showLabel && (
                    <span className={cn(
                        "text-zinc-500 uppercase tracking-wider",
                        sizes.label
                    )}>
                        {streakInfo.level}
                    </span>
                )}
            </div>

            {/* Best streak indicator */}
            {bestStreak && currentStreak === bestStreak && currentStreak > 0 && (
                <span className={cn(
                    "ml-1 px-1.5 py-0.5 rounded-full",
                    "bg-emerald-500/20 text-emerald-400",
                    "text-[10px] font-bold uppercase"
                )}>
                    Best!
                </span>
            )}
        </div>
    )
}

// ============================================================================
// LARGE STREAK DISPLAY (for profile/dashboard)
// ============================================================================

interface StreakCardProps {
    currentStreak: number
    bestStreak: number
    totalDays?: number
    className?: string
}

export function StreakCard({
    currentStreak,
    bestStreak,
    totalDays = 0,
    className,
}: StreakCardProps) {
    const streakInfo = getStreakLevel(currentStreak)
    const Icon = streakInfo.icon

    return (
        <div className={cn(
            "relative overflow-hidden rounded-2xl",
            "bg-gradient-to-br from-zinc-900 to-zinc-950",
            "border border-zinc-800/60",
            "p-6",
            streakInfo.glowColor,
            className
        )}>
            {/* Background glow */}
            <div className={cn(
                "absolute inset-0 opacity-20",
                "bg-gradient-to-br",
                currentStreak >= 7
                    ? "from-orange-500/30 via-transparent to-amber-500/20"
                    : "from-zinc-700/30 via-transparent to-zinc-800/20"
            )} />

            {/* Content */}
            <div className="relative">
                {/* Header */}
                <div className="flex items-center gap-3 mb-6">
                    <div className={cn(
                        "w-12 h-12 rounded-xl",
                        "flex items-center justify-center",
                        streakInfo.bgColor,
                        currentStreak >= 7 && "animate-pulse"
                    )}>
                        <Icon className={cn("w-6 h-6", streakInfo.color)} />
                    </div>
                    <div>
                        <h3 className="text-lg font-bold text-zinc-100">
                            Learning Streak
                        </h3>
                        <p className={cn("text-sm font-medium", streakInfo.color)}>
                            {streakInfo.level}
                        </p>
                    </div>
                </div>

                {/* Main Streak Display */}
                <div className="text-center mb-6">
                    <div className={cn(
                        "text-6xl font-bold",
                        "bg-gradient-to-r bg-clip-text text-transparent",
                        currentStreak >= 7
                            ? "from-orange-400 via-amber-400 to-yellow-400"
                            : "from-zinc-100 to-zinc-400"
                    )}>
                        {currentStreak}
                    </div>
                    <p className="text-zinc-500 text-sm mt-1">
                        consecutive day{currentStreak !== 1 ? "s" : ""}
                    </p>
                </div>

                {/* Stats Row */}
                <div className="grid grid-cols-2 gap-4">
                    <div className={cn(
                        "text-center p-3 rounded-xl",
                        "bg-zinc-800/40 border border-zinc-700/30"
                    )}>
                        <p className="text-2xl font-bold text-amber-400">{bestStreak}</p>
                        <p className="text-[10px] text-zinc-500 uppercase tracking-wider">
                            Best Streak
                        </p>
                    </div>
                    <div className={cn(
                        "text-center p-3 rounded-xl",
                        "bg-zinc-800/40 border border-zinc-700/30"
                    )}>
                        <p className="text-2xl font-bold text-emerald-400">{totalDays}</p>
                        <p className="text-[10px] text-zinc-500 uppercase tracking-wider">
                            Total Days
                        </p>
                    </div>
                </div>

                {/* Motivation message */}
                {currentStreak > 0 && currentStreak < bestStreak && (
                    <p className="text-center text-xs text-zinc-500 mt-4">
                        {bestStreak - currentStreak} more day{bestStreak - currentStreak !== 1 ? "s" : ""} to beat your record! 💪
                    </p>
                )}
                {currentStreak === bestStreak && currentStreak > 0 && (
                    <p className="text-center text-xs text-emerald-400 mt-4">
                        🎉 You&apos;re at your best streak! Keep it going!
                    </p>
                )}
            </div>
        </div>
    )
}

export default StreakBadge
