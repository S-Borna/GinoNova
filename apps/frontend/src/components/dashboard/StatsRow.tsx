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
import { GlassCard } from "@/components/ui/glass-card"
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
        <GlassCard
            variant="default"
            padding="md"
            radius="lg"
            interactive
            className={cn(
                "group relative overflow-hidden",
                "animate-fade-in-up",
                "hover:shadow-glow-" + glowColor
            )}
            style={{ animationDelay: `${delay}ms` }}
        >
            {/* Icon with gradient background */}
            <div
                className={cn(
                    "w-12 h-12 rounded-xl flex items-center justify-center mb-4",
                    "bg-gradient-to-br shadow-lg",
                    "transition-transform duration-300 group-hover:scale-110"
                )}
                style={{
                    background: `linear-gradient(135deg, ${gradientFrom}, ${gradientTo})`,
                }}
            >
                <span className="text-2xl text-white">{icon}</span>
            </div>

            {/* Value */}
            <div className="text-3xl font-bold text-neutral-900 dark:text-white tracking-tight mb-1">
                {value}
            </div>

            {/* Label */}
            <div className="text-sm font-medium text-neutral-500 dark:text-neutral-400">
                {label}
            </div>

            {/* Subtext */}
            {subtext && (
                <div className="text-xs text-neutral-400 dark:text-neutral-500 mt-1">
                    {subtext}
                </div>
            )}

            {/* Hover glow effect */}
            <div
                className={cn(
                    "absolute -bottom-12 -right-12 w-32 h-32 rounded-full blur-2xl opacity-0",
                    "transition-opacity duration-300 group-hover:opacity-30"
                )}
                style={{
                    background: `linear-gradient(135deg, ${gradientFrom}, ${gradientTo})`,
                }}
                aria-hidden="true"
            />
        </GlassCard>
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
            "grid grid-cols-2 lg:grid-cols-4 gap-4",
            className
        )}>
            {/* Level Card */}
            <GlassCard
                variant="default"
                padding="md"
                radius="lg"
                interactive
                className="group relative overflow-hidden animate-fade-in-up"
                style={{ animationDelay: "100ms" }}
            >
                <div className="flex items-start justify-between">
                    <div>
                        <div className="text-sm font-medium text-neutral-500 dark:text-neutral-400 mb-1">
                            Current Level
                        </div>
                        <div className="text-4xl font-bold text-neutral-900 dark:text-white tracking-tight">
                            {animatedLevel}
                        </div>
                        <div className="text-xs text-neutral-400 dark:text-neutral-500 mt-1">
                            {xpProgress}% to next
                        </div>
                    </div>
                    <MiniProgressRing progress={xpProgress} />
                </div>

                {/* Glow effect */}
                <div
                    className="absolute -bottom-8 -right-8 w-24 h-24 rounded-full bg-primary-500/20 blur-2xl opacity-0 transition-opacity group-hover:opacity-100"
                    aria-hidden="true"
                />
            </GlassCard>

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
            <GlassCard
                variant="default"
                padding="md"
                radius="lg"
                interactive
                className="group relative overflow-hidden animate-fade-in-up"
                style={{ animationDelay: "300ms" }}
            >
                <div className="flex items-start justify-between mb-3">
                    <div
                        className="w-12 h-12 rounded-xl flex items-center justify-center bg-gradient-to-br from-emerald-500 to-teal-500 shadow-lg transition-transform duration-300 group-hover:scale-110"
                    >
                        <span className="text-2xl text-white">📚</span>
                    </div>
                </div>
                <div className="text-3xl font-bold text-neutral-900 dark:text-white tracking-tight mb-1">
                    {animatedModules}/{totalModules}
                </div>
                <div className="text-sm font-medium text-neutral-500 dark:text-neutral-400">
                    Modules Complete
                </div>
                {/* Mini progress bar */}
                <div className="mt-3 h-1.5 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                    <div
                        className="h-full bg-gradient-to-r from-emerald-500 to-teal-500 rounded-full transition-all duration-1000 ease-out"
                        style={{ width: `${(modulesCompleted / totalModules) * 100}%` }}
                    />
                </div>

                <div
                    className="absolute -bottom-8 -right-8 w-24 h-24 rounded-full bg-emerald-500/20 blur-2xl opacity-0 transition-opacity group-hover:opacity-100"
                    aria-hidden="true"
                />
            </GlassCard>

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
