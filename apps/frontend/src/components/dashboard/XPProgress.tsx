"use client"

/**
 * XPProgress Component
 * Phase D.2: Apple Watch-Style XP Ring
 *
 * Features:
 * - Large circular progress indicator
 * - Current XP / XP to next level
 * - Level badge in center
 * - Animated on load
 */

import * as React from "react"
import { GlassCard } from "@/components/ui/glass-card"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface XPProgressProps {
    currentXP?: number
    xpToNextLevel?: number
    level?: number
    totalXP?: number
    className?: string
}

/* ============================================================================
   CIRCULAR PROGRESS COMPONENT
   ============================================================================ */

function CircularProgress({
    progress,
    size = 200,
    strokeWidth = 12,
    className,
}: {
    progress: number
    size?: number
    strokeWidth?: number
    className?: string
}) {
    const [animatedProgress, setAnimatedProgress] = React.useState(0)
    const radius = (size - strokeWidth) / 2
    const circumference = radius * 2 * Math.PI
    const offset = circumference - (animatedProgress / 100) * circumference

    React.useEffect(() => {
        // Animate from 0 to target
        const timeout = setTimeout(() => {
            setAnimatedProgress(progress)
        }, 100)
        return () => clearTimeout(timeout)
    }, [progress])

    return (
        <svg
            width={size}
            height={size}
            className={cn("transform -rotate-90", className)}
        >
            <defs>
                {/* Main gradient */}
                <linearGradient id="xpGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#6366f1" />
                    <stop offset="50%" stopColor="#8b5cf6" />
                    <stop offset="100%" stopColor="#a855f7" />
                </linearGradient>
                {/* Glow filter */}
                <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur stdDeviation="4" result="coloredBlur" />
                    <feMerge>
                        <feMergeNode in="coloredBlur" />
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

            {/* Progress arc */}
            <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="none"
                stroke="url(#xpGradient)"
                strokeWidth={strokeWidth}
                strokeDasharray={circumference}
                strokeDashoffset={offset}
                strokeLinecap="round"
                filter="url(#glow)"
                className="transition-all duration-1500 ease-out"
            />

            {/* Progress end cap glow */}
            {animatedProgress > 0 && (
                <circle
                    cx={
                        size / 2 +
                        radius * Math.cos((2 * Math.PI * animatedProgress) / 100 - Math.PI / 2)
                    }
                    cy={
                        size / 2 +
                        radius * Math.sin((2 * Math.PI * animatedProgress) / 100 - Math.PI / 2)
                    }
                    r={strokeWidth / 2}
                    fill="#a855f7"
                    className="transition-all duration-1500 ease-out"
                />
            )}
        </svg>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function XPProgress({
    currentXP = 0,
    xpToNextLevel = 1000,
    level = 1,
    totalXP = 0,
    className,
}: XPProgressProps) {
    // Calculate percentage
    const progress = xpToNextLevel > 0
        ? Math.min(100, Math.round((currentXP / xpToNextLevel) * 100))
        : 0

    const xpNeeded = Math.max(0, xpToNextLevel - currentXP)

    // Animated XP counter
    const [displayXP, setDisplayXP] = React.useState(0)
    React.useEffect(() => {
        const timeout = setTimeout(() => {
            const duration = 1200
            const startTime = Date.now()
            const animate = () => {
                const elapsed = Date.now() - startTime
                const p = Math.min(elapsed / duration, 1)
                const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p)
                setDisplayXP(Math.round(currentXP * eased))
                if (p < 1) requestAnimationFrame(animate)
            }
            requestAnimationFrame(animate)
        }, 200)
        return () => clearTimeout(timeout)
    }, [currentXP])

    return (
        <GlassCard
            variant="default"
            padding="lg"
            radius="lg"
            className={cn("animate-fade-in-up", className)}
            style={{ animationDelay: "200ms" }}
        >
            <div className="flex flex-col lg:flex-row items-center gap-8">
                {/* Circular Progress */}
                <div className="relative">
                    <CircularProgress progress={progress} size={200} strokeWidth={14} />

                    {/* Center content */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center">
                        {/* Level badge */}
                        <div className="px-3 py-1 rounded-full bg-gradient-to-r from-primary-500 to-primary-600 text-white text-xs font-bold mb-2 shadow-lg">
                            LEVEL {level}
                        </div>

                        {/* XP value */}
                        <div className="text-3xl font-bold text-neutral-900 dark:text-white">
                            {displayXP.toLocaleString()}
                        </div>
                        <div className="text-sm text-neutral-500 dark:text-neutral-400">
                            / {xpToNextLevel.toLocaleString()} XP
                        </div>
                    </div>
                </div>

                {/* XP Details */}
                <div className="flex-1 text-center lg:text-left space-y-4">
                    <div>
                        <h3 className="text-xl font-bold text-neutral-900 dark:text-white mb-1">
                            XP Progress
                        </h3>
                        <p className="text-neutral-500 dark:text-neutral-400">
                            {xpNeeded.toLocaleString()} XP to Level {level + 1}
                        </p>
                    </div>

                    {/* Progress bar */}
                    <div className="space-y-2">
                        <div className="flex justify-between text-sm">
                            <span className="text-neutral-600 dark:text-neutral-400">Progress</span>
                            <span className="font-medium text-primary-600 dark:text-primary-400">{progress}%</span>
                        </div>
                        <div className="h-3 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                            <div
                                className="h-full bg-gradient-to-r from-primary-500 via-primary-400 to-accent-info rounded-full transition-all duration-1000 ease-out animate-shimmer"
                                style={{ width: `${progress}%` }}
                            />
                        </div>
                    </div>

                    {/* Total XP stat */}
                    <div className="pt-4 border-t border-neutral-200 dark:border-neutral-700">
                        <div className="flex items-center justify-center lg:justify-start gap-2">
                            <span className="text-2xl">⚡</span>
                            <div>
                                <div className="text-2xl font-bold text-neutral-900 dark:text-white">
                                    {totalXP.toLocaleString()}
                                </div>
                                <div className="text-xs text-neutral-500 dark:text-neutral-400">
                                    Total XP Earned
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </GlassCard>
    )
}
