"use client"

/**
 * ============================================================================
 * TASK CARD — Design System v1.0
 * ============================================================================
 *
 * Tesla/Google-inspired card for module pages and dashboard.
 * Features:
 * - 16px border radius
 * - Thin border rgba(0,0,0,0.05)
 * - Soft hover shadow
 * - Large title with emoji
 * - Metadata row (time, XP, difficulty)
 * - Start/Continue button
 *
 * @example
 * <TaskCard
 *   title="Install Docker"
 *   type="foundation"
 *   xpReward={50}
 *   estimatedMinutes={15}
 *   difficulty={2}
 *   status="not_started"
 *   onClick={() => router.push('/task/1')}
 * />
 */

import * as React from 'react'
import { useState } from 'react'
import { cn } from './utils'

export type TaskType =
    | 'foundation'
    | 'practice'
    | 'deepening'
    | 'project'
    | 'challenge'
    | 'quiz'

export type TaskStatus = 'not_started' | 'in_progress' | 'complete'

export interface TaskCardProps {
    /** Task ID */
    id?: string
    /** Task order number */
    orderIndex?: number
    /** Task title */
    title: string
    /** Task description (optional) */
    description?: string
    /** Task type */
    type: TaskType
    /** Difficulty level (1-5) */
    difficulty: number
    /** XP reward for completing */
    xpReward: number
    /** Estimated completion time in minutes */
    estimatedMinutes?: number
    /** Current completion status */
    status: TaskStatus
    /** Click handler */
    onClick?: () => void
    /** Loading state */
    isLoading?: boolean
    /** Additional CSS classes */
    className?: string
}

// Type configuration with emojis and colors
const typeConfig: Record<TaskType, {
    label: string
    emoji: string
    colorClass: string
    bgClass: string
}> = {
    foundation: {
        label: 'Foundation',
        emoji: '📚',
        colorClass: 'text-blue-600 dark:text-blue-400',
        bgClass: 'bg-blue-50 dark:bg-blue-950/40',
    },
    practice: {
        label: 'Practice',
        emoji: '💻',
        colorClass: 'text-emerald-600 dark:text-emerald-400',
        bgClass: 'bg-emerald-50 dark:bg-emerald-950/40',
    },
    deepening: {
        label: 'Deep Dive',
        emoji: '🔍',
        colorClass: 'text-violet-600 dark:text-violet-400',
        bgClass: 'bg-violet-50 dark:bg-violet-950/40',
    },
    project: {
        label: 'Project',
        emoji: '🚀',
        colorClass: 'text-orange-600 dark:text-orange-400',
        bgClass: 'bg-orange-50 dark:bg-orange-950/40',
    },
    challenge: {
        label: 'Challenge',
        emoji: '🏆',
        colorClass: 'text-rose-600 dark:text-rose-400',
        bgClass: 'bg-rose-50 dark:bg-rose-950/40',
    },
    quiz: {
        label: 'Quiz',
        emoji: '❓',
        colorClass: 'text-cyan-600 dark:text-cyan-400',
        bgClass: 'bg-cyan-50 dark:bg-cyan-950/40',
    },
}

// Difficulty dots component
function DifficultyDots({ difficulty }: { difficulty: number }) {
    const labels = ['Beginner', 'Easy', 'Medium', 'Hard', 'Expert']
    return (
        <div className="flex items-center gap-1.5">
            <div className="flex items-center gap-0.5">
                {Array.from({ length: 5 }).map((_, i) => (
                    <div
                        key={i}
                        className={cn(
                            'w-1.5 h-1.5 rounded-full transition-all',
                            i < difficulty
                                ? 'bg-neutral-800 dark:bg-neutral-200'
                                : 'bg-neutral-200 dark:bg-neutral-700'
                        )}
                    />
                ))}
            </div>
            <span className="text-xs text-[#6B7280] dark:text-neutral-400">
                {labels[Math.min(difficulty - 1, 4)] || 'Beginner'}
            </span>
        </div>
    )
}

// Loading spinner
function Spinner() {
    return (
        <svg
            className="animate-spin w-4 h-4"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
        >
            <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
            />
            <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
        </svg>
    )
}

// Icons
function ClockIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10" />
            <path d="M12 6v6l4 2" />
        </svg>
    )
}

function ZapIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
        </svg>
    )
}

function PlayIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="currentColor">
            <polygon points="5 3 19 12 5 21 5 3" />
        </svg>
    )
}

function ChevronRightIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polyline points="9 18 15 12 9 6" />
        </svg>
    )
}

function CheckCircleIcon({ className }: { className?: string }) {
    return (
        <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
            <polyline points="22 4 12 14.01 9 11.01" />
        </svg>
    )
}

export function TaskCard({
    id,
    orderIndex,
    title,
    description,
    type,
    difficulty,
    xpReward,
    estimatedMinutes = 15,
    status,
    onClick,
    isLoading = false,
    className,
}: TaskCardProps) {
    const [isHovered, setIsHovered] = useState(false)
    const config = typeConfig[type] || typeConfig.foundation
    const isComplete = status === 'complete'
    const isInProgress = status === 'in_progress'

    return (
        <div
            className={cn(
                // Base card styling
                'relative transition-all duration-300 ease-out',
                'rounded-2xl',                                    // 16px radius
                'bg-white dark:bg-neutral-900',
                'border border-[rgba(0,0,0,0.05)] dark:border-[rgba(255,255,255,0.08)]',
                // Hover shadow (Tesla-style)
                isHovered && 'shadow-[0_4px_12px_rgba(0,0,0,0.06)] dark:shadow-[0_4px_12px_rgba(0,0,0,0.3)]',
                // Complete state
                isComplete && 'bg-neutral-50 dark:bg-neutral-900/50',
                // Clickable
                onClick && 'cursor-pointer',
                className
            )}
            onClick={onClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            <div className="p-5">
                {/* Header: Icon + Status Badge */}
                <div className="flex items-start justify-between mb-4">
                    {/* Emoji Icon */}
                    <div
                        className={cn(
                            'w-12 h-12 rounded-xl flex items-center justify-center',
                            'transition-transform duration-200',
                            config.bgClass,
                            isHovered && 'scale-105'
                        )}
                    >
                        <span className="text-2xl" role="img" aria-label={config.label}>
                            {config.emoji}
                        </span>
                    </div>

                    {/* Status Badge */}
                    <div className="flex items-center gap-2">
                        {isComplete && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/40">
                                <CheckCircleIcon className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                                <span className="text-xs font-medium text-emerald-700 dark:text-emerald-300">Done</span>
                            </div>
                        )}
                        {isInProgress && (
                            <div className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-blue-100 dark:bg-blue-900/40">
                                <Spinner />
                                <span className="text-xs font-medium text-blue-700 dark:text-blue-300">In Progress</span>
                            </div>
                        )}
                        {!isComplete && !isInProgress && (
                            <span className={cn(
                                'px-2.5 py-1 rounded-full text-xs font-medium',
                                config.bgClass,
                                config.colorClass
                            )}>
                                {config.label}
                            </span>
                        )}
                    </div>
                </div>

                {/* Task Number */}
                {orderIndex !== undefined && (
                    <span className="text-xs font-medium text-[#9CA3AF] dark:text-neutral-500 tracking-wide uppercase">
                        Task {orderIndex}
                    </span>
                )}

                {/* Title */}
                <h3
                    className={cn(
                        'mt-1 text-xl font-medium leading-tight tracking-tight',
                        'text-[#111827] dark:text-white',
                        isComplete && 'text-[#6B7280] dark:text-neutral-400'
                    )}
                >
                    {title}
                </h3>

                {/* Description */}
                {description && (
                    <p className="mt-2 text-sm leading-relaxed text-[#6B7280] dark:text-neutral-400 line-clamp-2">
                        {description}
                    </p>
                )}

                {/* Meta Row */}
                <div className="flex items-center gap-4 mt-4 pt-4 border-t border-neutral-100 dark:border-neutral-800">
                    {/* Time */}
                    <div className="flex items-center gap-1.5 text-[#6B7280] dark:text-neutral-400">
                        <ClockIcon className="w-3.5 h-3.5" />
                        <span className="text-xs font-medium">{estimatedMinutes} min</span>
                    </div>

                    {/* XP */}
                    <div className="flex items-center gap-1.5 text-amber-600 dark:text-amber-400">
                        <ZapIcon className="w-3.5 h-3.5" />
                        <span className="text-xs font-bold">{xpReward} XP</span>
                    </div>

                    {/* Difficulty */}
                    <DifficultyDots difficulty={difficulty} />

                    {/* Action Button */}
                    {!isComplete && (
                        <button
                            disabled={isLoading}
                            className={cn(
                                'ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl',
                                'text-sm font-medium transition-all duration-200',
                                'bg-[#4F46E5] hover:bg-[#4338CA]',
                                'text-white',
                                'active:scale-[0.98]',
                                isLoading && 'opacity-50 cursor-wait'
                            )}
                            onClick={(e) => {
                                e.stopPropagation()
                                onClick?.()
                            }}
                        >
                            {isLoading ? (
                                <Spinner />
                            ) : isInProgress ? (
                                <>
                                    <span>Continue</span>
                                    <ChevronRightIcon className="w-4 h-4" />
                                </>
                            ) : (
                                <>
                                    <PlayIcon className="w-3.5 h-3.5" />
                                    <span>Start</span>
                                </>
                            )}
                        </button>
                    )}

                    {/* Completed: Review button */}
                    {isComplete && (
                        <button
                            className={cn(
                                'ml-auto flex items-center gap-1.5 px-4 py-2 rounded-xl',
                                'text-sm font-medium transition-all duration-200',
                                'bg-neutral-100 dark:bg-neutral-800',
                                'text-[#6B7280] dark:text-neutral-300',
                                'hover:bg-neutral-200 dark:hover:bg-neutral-700'
                            )}
                            onClick={(e) => {
                                e.stopPropagation()
                                onClick?.()
                            }}
                        >
                            <span>Review</span>
                            <ChevronRightIcon className="w-4 h-4" />
                        </button>
                    )}
                </div>
            </div>

            {/* Progress bar for in-progress */}
            {isInProgress && (
                <div className="absolute bottom-0 left-0 right-0 h-1 bg-neutral-100 dark:bg-neutral-800 rounded-b-2xl overflow-hidden">
                    <div className="h-full w-1/3 bg-[#4F46E5] animate-pulse" />
                </div>
            )}
        </div>
    )
}

export default TaskCard
