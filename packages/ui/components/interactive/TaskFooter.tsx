"use client"

/**
 * ============================================================================
 * TASK FOOTER COMPONENT — PREMIUM VIBRANT DESIGN
 * ============================================================================
 *
 * Footer for all task pages with navigation and completion.
 * Sticky on desktop, inline on mobile.
 * Features stunning gradients and animations.
 *
 * @design VIBRANT-PREMIUM-2024
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
    easy: { 
        label: 'Enkel', 
        gradient: 'from-emerald-500 to-teal-500',
        bg: 'bg-gradient-to-r from-emerald-500/10 to-teal-500/10',
        border: 'border-emerald-500/30',
        text: 'text-emerald-400',
    },
    medium: { 
        label: 'Medel', 
        gradient: 'from-amber-500 to-orange-500',
        bg: 'bg-gradient-to-r from-amber-500/10 to-orange-500/10',
        border: 'border-amber-500/30',
        text: 'text-amber-400',
    },
    hard: { 
        label: 'Svår', 
        gradient: 'from-rose-500 to-red-500',
        bg: 'bg-gradient-to-r from-rose-500/10 to-red-500/10',
        border: 'border-rose-500/30',
        text: 'text-rose-400',
    },
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
                "w-full relative",
                "lg:sticky lg:bottom-0",
                className
            )}
        >
            {/* Background with gradient border */}
            <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-violet-500/50 to-transparent" />
            
            <div className={cn(
                "bg-zinc-900/95 backdrop-blur-xl",
                "px-4 py-5 sm:px-6"
            )}>
                <div className="max-w-4xl mx-auto">
                    <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
                        {/* Left: Previous Navigation */}
                        <div className="flex items-center gap-2">
                            {prevTaskUrl ? (
                                <a
                                    href={prevTaskUrl}
                                    className={cn(
                                        "group flex items-center gap-3 px-5 py-3 rounded-xl",
                                        "bg-zinc-800/60 hover:bg-zinc-700/60",
                                        "border border-zinc-700/50 hover:border-violet-500/30",
                                        "text-sm font-medium text-zinc-400 hover:text-white",
                                        "transition-all duration-300"
                                    )}
                                >
                                    <div className={cn(
                                        "w-8 h-8 rounded-lg flex items-center justify-center",
                                        "bg-zinc-700/50 group-hover:bg-violet-500/20",
                                        "transition-colors duration-300"
                                    )}>
                                        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                                        </svg>
                                    </div>
                                    <span>Föregående</span>
                                </a>
                            ) : (
                                <div className="w-32" />
                            )}
                        </div>

                        {/* Center: Stats & Complete Button */}
                        <div className="flex items-center gap-4">
                            {/* XP Badge */}
                            <div className={cn(
                                "flex items-center gap-2 px-4 py-2 rounded-xl",
                                "bg-gradient-to-r from-amber-500/10 to-orange-500/10",
                                "border border-amber-500/30"
                            )}>
                                <svg className="w-5 h-5 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
                                </svg>
                                <span className={cn(
                                    "font-bold text-transparent bg-clip-text",
                                    "bg-gradient-to-r from-amber-400 to-orange-400"
                                )}>
                                    +{xp} XP
                                </span>
                            </div>

                            {/* Difficulty Badge */}
                            <div className={cn(
                                "px-4 py-2 rounded-xl font-bold text-sm uppercase tracking-wide",
                                config.bg,
                                config.border,
                                "border",
                                config.text
                            )}>
                                {config.label}
                            </div>

                            {/* Complete Button */}
                            <button
                                onClick={onComplete}
                                disabled={isLoading || isCompleted}
                                className={cn(
                                    "relative group flex items-center gap-2 px-8 py-3 rounded-xl",
                                    "text-sm font-bold",
                                    "transition-all duration-300",
                                    "overflow-hidden",
                                    isCompleted
                                        ? cn(
                                            "bg-gradient-to-r from-emerald-500/20 to-teal-500/20",
                                            "border border-emerald-500/30",
                                            "text-emerald-400",
                                            "cursor-default"
                                        )
                                        : isLoading
                                            ? "bg-violet-500/50 text-white cursor-wait"
                                            : cn(
                                                "bg-gradient-to-r from-violet-500 via-purple-500 to-indigo-500",
                                                "hover:from-violet-600 hover:via-purple-600 hover:to-indigo-600",
                                                "text-white",
                                                "shadow-lg shadow-violet-500/25",
                                                "hover:shadow-xl hover:shadow-violet-500/30",
                                                "active:scale-95"
                                            )
                                )}
                            >
                                {/* Shimmer effect for non-completed state */}
                                {!isCompleted && !isLoading && (
                                    <div className="absolute inset-0 -translate-x-full group-hover:translate-x-full transition-transform duration-700 bg-gradient-to-r from-transparent via-white/20 to-transparent" />
                                )}
                                
                                {isLoading ? (
                                    <>
                                        <svg className="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                                        </svg>
                                        <span>Sparar...</span>
                                    </>
                                ) : isCompleted ? (
                                    <>
                                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                                        </svg>
                                        <span>Slutförd</span>
                                    </>
                                ) : (
                                    <>
                                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                                        </svg>
                                        <span>Markera som klar</span>
                                    </>
                                )}
                            </button>
                        </div>

                        {/* Right: Next Navigation */}
                        <div className="flex items-center gap-2">
                            {nextTaskUrl ? (
                                <a
                                    href={nextTaskUrl}
                                    className={cn(
                                        "group flex items-center gap-3 px-5 py-3 rounded-xl",
                                        "bg-gradient-to-r from-violet-500/10 to-purple-500/10",
                                        "border border-violet-500/30",
                                        "text-sm font-medium text-violet-300 hover:text-white",
                                        "hover:from-violet-500/20 hover:to-purple-500/20",
                                        "transition-all duration-300"
                                    )}
                                >
                                    <span>Nästa</span>
                                    <div className={cn(
                                        "w-8 h-8 rounded-lg flex items-center justify-center",
                                        "bg-violet-500/20 group-hover:bg-violet-500/40",
                                        "transition-colors duration-300"
                                    )}>
                                        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                                            <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </div>
                                </a>
                            ) : (
                                <div className="w-32" />
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default TaskFooter
