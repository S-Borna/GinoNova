"use client"

/**
 * StatsRow Component
 * Phase D.2: Apple-Inspired Stats Cards
 *
 * Four stat cards in a row:
 * - Current Level (with XP progress ring)
 * - Study Streak (flame icon, days count)
 * - Modules Completed (x/10 with mini progress)
 * - Total XP (animated number)
 */

import * as React from "react"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StatsRowProps {
    level?: number
    currentXP?: number
    xpToNextLevel?: number
    streak?: number
    modulesCompleted?: number
    totalModules?: number
    totalXP?: number
    className?: string
}

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    subtext?: string
    gradientFrom: string
    gradientTo: string
    glowColor?: string
    delay?: number
}

/* ============================================================================
   ANIMATED NUMBER HOOK
   ============================================================================ */

function useAnimatedNumber(
    target: number,
    duration: number = 1000,
    delay: number = 0
): number {
    const [current, setCurrent] = React.useState(0)

    React.useEffect(() => {
        const timeout = setTimeout(() => {
            const startTime = Date.now()
            const animate = () => {
                const elapsed = Date.now() - startTime
                const progress = Math.min(elapsed / duration, 1)
                // Easing function: ease-out-expo
                const eased = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress)
                setCurrent(Math.round(target * eased))

                if (progress < 1) {
                    requestAnimationFrame(animate)
                }
            }
            requestAnimationFrame(animate)
        }, delay)

        return () => clearTimeout(timeout)
    }, [target, duration, delay])

    return current
}

/* ============================================================================
   STAT CARD COMPONENT
   ============================================================================ */

function StatCard({
    icon,
    label,
    value,
    subtext,
    gradientFrom,
    gradientTo,
    glowColor = "primary",
    delay = 0,
}: StatCardProps) {
    return (
        <div
            className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6 transition-all duration-200 hover:shadow-md hover:-translate-y-0.5 animate-fade-in-up"
            style={{ animationDelay: `${delay}ms` }}
        >
            <div className="flex items-center gap-4">
                {/* Icon with gradient background */}
                <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center shrink-0"
                    style={{
                        background: `linear-gradient(135deg, ${gradientFrom}, ${gradientTo})`,
                    }}
                >
                    <span className="text-2xl text-white">{icon}</span>
                </div>

                <div className="min-w-0">
                    {/* Label */}
                    <p className="text-sm text-gray-500 dark:text-neutral-400 truncate">
                        {label}
                    </p>
                    {/* Value */}
                    <p className="text-2xl font-bold text-gray-900 dark:text-white">
                        {value}
                    </p>
                    {/* Subtext */}
                    {subtext && (
                        <p className="text-xs text-gray-400 dark:text-neutral-500 mt-0.5">
                            {subtext}
                        </p>
                    )}
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MINI PROGRESS RING
   ============================================================================ */

function MiniProgressRing({
    progress,
    size = 48,
    strokeWidth = 4,
    className
}: {
    progress: number
    size?: number
    strokeWidth?: number
    className?: string
}) {
    const radius = (size - strokeWidth) / 2
    const circumference = radius * 2 * Math.PI
    const offset = circumference - (progress / 100) * circumference

    return (
        <svg
            width={size}
            height={size}
            className={cn("transform -rotate-90", className)}
        >
            {/* Background circle */}
            <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="none"
                stroke="currentColor"
                strokeWidth={strokeWidth}
                className="text-neutral-200 dark:text-neutral-700"
            />
            {/* Progress circle */}
            <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="none"
                stroke="url(#progressGradient)"
                strokeWidth={strokeWidth}
                strokeDasharray={circumference}
                strokeDashoffset={offset}
                strokeLinecap="round"
                className="transition-all duration-1000 ease-out"
            />
            <defs>
                <linearGradient id="progressGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="var(--primary-500, #6366f1)" />
                    <stop offset="100%" stopColor="var(--primary-400, #818cf8)" />
                </linearGradient>
            </defs>
        </svg>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function StatsRow({
    level = 1,
    currentXP = 0,
    xpToNextLevel = 1000,
    streak = 0,
    modulesCompleted = 0,
    totalModules = 10,
    totalXP = 0,
    className,
}: StatsRowProps) {
    // Animated values
    const animatedLevel = useAnimatedNumber(level, 800, 100)
    const animatedStreak = useAnimatedNumber(streak, 800, 200)
    const animatedModules = useAnimatedNumber(modulesCompleted, 800, 300)
    const animatedXP = useAnimatedNumber(totalXP, 1200, 400)

    // Calculate XP progress percentage
    const xpProgress = xpToNextLevel > 0
        ? Math.min(100, Math.round((currentXP / xpToNextLevel) * 100))
        : 0

    return (
        <div className={cn(
            "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6",
            className
        )}>
            {/* Level Card */}
            <div
                className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6 transition-all duration-200 hover:shadow-md hover:-translate-y-0.5 animate-fade-in-up"
                style={{ animationDelay: "100ms" }}
            >
                <div className="flex items-center gap-4">
                    <div className="relative">
                        <MiniProgressRing progress={xpProgress} />
                        <div className="absolute inset-0 flex items-center justify-center">
                            <span className="text-sm font-bold text-indigo-600 dark:text-indigo-400">{animatedLevel}</span>
                        </div>
                    </div>
                    <div>
                        <p className="text-sm text-gray-500 dark:text-neutral-400">
                            Current Level
                        </p>
                        <p className="text-2xl font-bold text-gray-900 dark:text-white">
                            Level {animatedLevel}
                        </p>
                        <p className="text-xs text-gray-400 dark:text-neutral-500">
                            {xpProgress}% to next
                        </p>
                    </div>
                </div>
            </div>

            {/* Streak Card */}
            <StatCard
                icon="🔥"
                label="Study Streak"
                value={`${animatedStreak} days`}
                subtext={streak >= 7 ? "On fire!" : streak > 0 ? "Keep it going!" : "Start today!"}
                gradientFrom="#f97316"
                gradientTo="#ea580c"
                glowColor="warning"
                delay={200}
            />

            {/* Modules Card */}
            <div
                className="bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6 transition-all duration-200 hover:shadow-md hover:-translate-y-0.5 animate-fade-in-up"
                style={{ animationDelay: "300ms" }}
            >
                <div className="flex items-center gap-4">
                    <div
                        className="w-12 h-12 rounded-xl flex items-center justify-center shrink-0"
                        style={{ background: "linear-gradient(135deg, #22c55e, #14b8a6)" }}
                    >
                        <span className="text-2xl text-white">📚</span>
                    </div>
                    <div className="flex-1 min-w-0">
                        <p className="text-sm text-gray-500 dark:text-neutral-400">
                            Modules Complete
                        </p>
                        <p className="text-2xl font-bold text-gray-900 dark:text-white">
                            {animatedModules}/{totalModules}
                        </p>
                    </div>
                </div>
                {/* Progress bar */}
                <div className="mt-4">
                    <div className="w-full bg-gray-200 dark:bg-neutral-700 rounded-full h-2">
                        <div
                            className="bg-gradient-to-r from-emerald-500 to-teal-500 h-2 rounded-full transition-all duration-1000 ease-out"
                            style={{ width: `${(modulesCompleted / totalModules) * 100}%` }}
                        />
                    </div>
                </div>
            </div>

            {/* Total XP Card */}
            <StatCard
                icon="⚡"
                label="Total XP"
                value={animatedXP.toLocaleString()}
                subtext="Experience points"
                gradientFrom="#8b5cf6"
                gradientTo="#6366f1"
                glowColor="primary"
                delay={400}
            />
        </div>
    )
}
