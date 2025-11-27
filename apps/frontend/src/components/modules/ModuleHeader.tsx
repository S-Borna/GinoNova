"use client"

/**
 * ============================================================================
 * MODULE HEADER — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Header section for module detail page with:
 * - Large module icon
 * - Title + description
 * - Difficulty indicator
 * - Estimated time
 * - Progress ring
 *
 * @phase D.4 - Modules UI
 */

import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Clock, Star, BookOpen, Zap } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ModuleHeaderProps {
    title: string
    description: string
    icon?: string // emoji
    difficulty: number // 1-5
    estimatedHours: number
    tasksCount: number
    totalXP: number
    progress: number // 0-100
    className?: string
}

/* ============================================================================
   DIFFICULTY DISPLAY
   ============================================================================ */

function DifficultyDisplay({ difficulty }: { difficulty: number }) {
    const labels = ["Beginner", "Easy", "Intermediate", "Advanced", "Expert"]
    const label = labels[Math.min(difficulty - 1, 4)] || "Unknown"

    return (
        <div className="flex items-center gap-2">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 5 }).map((_, i) => (
                    <Star
                        key={i}
                        className={cn(
                            "w-4 h-4 transition-colors",
                            i < difficulty
                                ? "text-warning-500 fill-warning-500"
                                : "text-neutral-300 dark:text-neutral-600"
                        )}
                    />
                ))}
            </div>
            <span className="text-sm text-neutral-600 dark:text-neutral-400">
                {label}
            </span>
        </div>
    )
}

/* ============================================================================
   MINI PROGRESS RING
   ============================================================================ */

function MiniProgressRing({ progress, size = 80 }: { progress: number; size?: number }) {
    const strokeWidth = 6
    const radius = (size - strokeWidth) / 2
    const circumference = radius * 2 * Math.PI
    const offset = circumference - (progress / 100) * circumference

    return (
        <div className="relative" style={{ width: size, height: size }}>
            <svg
                className="absolute inset-0 -rotate-90"
                width={size}
                height={size}
            >
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={strokeWidth}
                    className="text-neutral-200 dark:text-neutral-700"
                />
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={offset}
                    className={cn(
                        "transition-all duration-500",
                        progress === 100 ? "text-success-500" : "text-primary-500"
                    )}
                />
            </svg>
            <div className="absolute inset-0 flex items-center justify-center">
                <span className="text-lg font-bold text-neutral-900 dark:text-white">
                    {progress}%
                </span>
            </div>
        </div>
    )
}

/* ============================================================================
   MODULE HEADER COMPONENT
   ============================================================================ */

export function ModuleHeader({
    title,
    description,
    icon = "📚",
    difficulty,
    estimatedHours,
    tasksCount,
    totalXP,
    progress,
    className
}: ModuleHeaderProps) {
    return (
        <GlassCard
            variant="default"
            padding="xl"
            radius="xl"
            className={cn(
                "relative overflow-hidden",
                className
            )}
        >
            {/* Background gradient */}
            <div className={cn(
                "absolute inset-0 opacity-50",
                "bg-gradient-to-br from-primary-100 via-transparent to-primary-50",
                "dark:from-primary-900/20 dark:via-transparent dark:to-primary-800/10"
            )} />

            <div className="relative flex flex-col lg:flex-row lg:items-start gap-6">
                {/* Left side: Icon + Title + Description */}
                <div className="flex-1">
                    {/* Large icon */}
                    <div className="text-6xl mb-4 animate-fade-in">
                        {icon}
                    </div>

                    {/* Title */}
                    <h1 className="text-3xl font-bold text-neutral-900 dark:text-white mb-2 animate-fade-in-up">
                        {title}
                    </h1>

                    {/* Description */}
                    <p className="text-lg text-neutral-600 dark:text-neutral-400 mb-4 max-w-2xl animate-fade-in-up">
                        {description}
                    </p>

                    {/* Difficulty */}
                    <div className="mb-4">
                        <DifficultyDisplay difficulty={difficulty} />
                    </div>

                    {/* Info badges row */}
                    <div className="flex flex-wrap items-center gap-3">
                        {/* Estimated time */}
                        <div className={cn(
                            "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                            "bg-info-100 dark:bg-info-900/30",
                            "text-info-700 dark:text-info-400 text-sm font-medium"
                        )}>
                            <Clock className="w-4 h-4" />
                            <span>~{estimatedHours} hours</span>
                        </div>

                        {/* Tasks count */}
                        <div className={cn(
                            "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                            "bg-neutral-100 dark:bg-neutral-800",
                            "text-neutral-700 dark:text-neutral-300 text-sm font-medium"
                        )}>
                            <BookOpen className="w-4 h-4" />
                            <span>{tasksCount} tasks</span>
                        </div>

                        {/* XP available */}
                        <div className={cn(
                            "flex items-center gap-1.5 px-3 py-1.5 rounded-full",
                            "bg-xp-100 dark:bg-xp-900/30",
                            "text-xp-700 dark:text-xp-400 text-sm font-medium"
                        )}>
                            <Zap className="w-4 h-4" />
                            <span>{totalXP} XP</span>
                        </div>
                    </div>
                </div>

                {/* Right side: Progress ring */}
                <div className="flex-shrink-0 flex items-center justify-center lg:justify-end">
                    <MiniProgressRing progress={progress} size={100} />
                </div>
            </div>
        </GlassCard>
    )
}

export default ModuleHeader
