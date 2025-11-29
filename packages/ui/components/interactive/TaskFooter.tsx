"use client"

/**
 * ============================================================================
 * TASK FOOTER COMPONENT — Design System v1.0
 * ============================================================================
 *
 * Footer for all task pages with navigation and completion.
 * Sticky on desktop, inline on mobile.
 *
 * @example
 * <TaskFooter
 *   prevTaskUrl="/modules/docker/tasks/1"
 *   nextTaskUrl="/modules/docker/tasks/3"
 *   onComplete={() => markComplete()}
 *   xp={50}
 *   difficulty="medium"
 * />
 *
 * @design PHASE 3 — Hands-On, Labs, Exercises & Interactive Components
 */

import * as React from 'react'
import { cn } from '../utils'

export interface TaskFooterProps {
    /** Previous task URL */
    prevTaskUrl?: string
    /** Next task URL */
    nextTaskUrl?: string
    /** Callback when task is marked complete */
    onComplete: () => void
    /** XP reward for completing this task */
    xp: number
    /** Difficulty level (1-5 or string) */
    difficulty: 'easy' | 'medium' | 'hard' | number
    /** Whether task is already completed */
    isCompleted?: boolean
    /** Whether completion is in progress */
    isLoading?: boolean
    /** Additional CSS classes */
    className?: string
}

const difficultyConfig = {
    easy: { label: 'Easy', color: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-400', dots: 1 },
    medium: { label: 'Medium', color: 'bg-amber-100 text-amber-700 dark:bg-amber-900/40 dark:text-amber-400', dots: 2 },
    hard: { label: 'Hard', color: 'bg-red-100 text-red-700 dark:bg-red-900/40 dark:text-red-400', dots: 3 },
}

export function TaskFooter({
    prevTaskUrl,
    nextTaskUrl,
    onComplete,
    xp,
    difficulty,
    isCompleted = false,
    isLoading = false,
    className,
}: TaskFooterProps) {
    const difficultyKey = typeof difficulty === 'number'
        ? difficulty <= 1 ? 'easy' : difficulty <= 2 ? 'medium' : 'hard'
        : difficulty
    const config = difficultyConfig[difficultyKey]

    return (
        <div
            className={cn(
                // Base
                "w-full",
                // Sticky positioning on larger screens
                "lg:sticky lg:bottom-0",
                // Background with blur
                "bg-white/80 dark:bg-neutral-900/80",
                "backdrop-blur-xl",
                "border-t border-neutral-200 dark:border-neutral-800",
                // Padding
                "px-4 py-4 sm:px-6",
                // Shadow for sticky effect
                "shadow-[0_-4px_20px_-4px_rgba(0,0,0,0.1)]",
                className
            )}
        >
            <div className="max-w-4xl mx-auto">
                <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
                    {/* Left: Navigation */}
                    <div className="flex items-center gap-2">
                        {prevTaskUrl ? (
                            <a
                                href={prevTaskUrl}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-xl",
                                    "text-sm font-medium",
                                    "text-neutral-600 dark:text-neutral-400",
                                    "hover:text-neutral-900 dark:hover:text-white",
                                    "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                    "transition-colors"
                                )}
                            >
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                                </svg>
                                Previous
                            </a>
                        ) : (
                            <div className="w-24" /> // Spacer
                        )}
                    </div>

                    {/* Center: Stats & Complete Button */}
                    <div className="flex items-center gap-4">
                        {/* XP Badge */}
                        <div className="flex items-center gap-1.5 text-sm">
                            <svg className="w-4 h-4 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                <path strokeLinecap="round" strokeLinejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                            <span className="font-semibold text-indigo-600 dark:text-indigo-400">+{xp} XP</span>
                        </div>

                        {/* Difficulty Badge */}
                        <div className={cn("px-2.5 py-1 rounded-full text-xs font-medium", config.color)}>
                            {config.label}
                        </div>

                        {/* Complete Button */}
                        <button
                            onClick={onComplete}
                            disabled={isLoading || isCompleted}
                            className={cn(
                                "flex items-center gap-2 px-6 py-2.5 rounded-xl",
                                "text-sm font-semibold",
                                "transition-all duration-200",
                                isCompleted
                                    ? "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-400 cursor-default"
                                    : isLoading
                                        ? "bg-indigo-400 text-white cursor-wait"
                                        : "bg-indigo-500 text-white hover:bg-indigo-600 active:scale-95"
                            )}
                        >
                            {isLoading ? (
                                <>
                                    <svg className="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                                    </svg>
                                    Saving...
                                </>
                            ) : isCompleted ? (
                                <>
                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                                    </svg>
                                    Completed
                                </>
                            ) : (
                                <>
                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                                    </svg>
                                    Mark Complete
                                </>
                            )}
                        </button>
                    </div>

                    {/* Right: Navigation */}
                    <div className="flex items-center gap-2">
                        {nextTaskUrl ? (
                            <a
                                href={nextTaskUrl}
                                className={cn(
                                    "flex items-center gap-2 px-4 py-2 rounded-xl",
                                    "text-sm font-medium",
                                    "text-neutral-600 dark:text-neutral-400",
                                    "hover:text-neutral-900 dark:hover:text-white",
                                    "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                    "transition-colors"
                                )}
                            >
                                Next
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                                </svg>
                            </a>
                        ) : (
                            <div className="w-24" /> // Spacer
                        )}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default TaskFooter
