"use client"

/**
 * ============================================================================
 * MODULE PROGRESS SIDEBAR — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Sticky sidebar for module detail page with:
 * - Circular progress ring
 * - XP earned / total
 * - Time spent
 * - Continue Learning button
 * - Mini task checklist
 *
 * @phase D.4 - Modules UI
 */

import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import {
    CheckCircle2,
    Circle,
    Clock,
    Zap,
    PlayCircle,
    BookOpen
} from "lucide-react"
import Link from "next/link"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface MiniTask {
    id: string
    title: string
    isComplete: boolean
}

export interface ModuleProgressProps {
    moduleId: string
    progress: number // 0-100
    xpEarned: number
    totalXP: number
    timeSpentMinutes: number
    tasksCompleted: number
    totalTasks: number
    tasks: MiniTask[]
    nextTaskId?: string
    className?: string
}

/* ============================================================================
   CIRCULAR PROGRESS
   ============================================================================ */

function CircularProgress({
    progress,
    size = 160,
    strokeWidth = 12
}: {
    progress: number
    size?: number
    strokeWidth?: number
}) {
    const radius = (size - strokeWidth) / 2
    const circumference = radius * 2 * Math.PI
    const offset = circumference - (progress / 100) * circumference

    return (
        <div className="relative" style={{ width: size, height: size }}>
            {/* Background ring */}
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
            </svg>

            {/* Progress ring */}
            <svg
                className="absolute inset-0 -rotate-90"
                width={size}
                height={size}
            >
                <defs>
                    <linearGradient id="progressGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stopColor="var(--color-primary-500, #6366f1)" />
                        <stop offset="100%" stopColor="var(--color-primary-600, #4f46e5)" />
                    </linearGradient>
                </defs>
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="url(#progressGradient)"
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={offset}
                    className="transition-all duration-700 ease-out"
                />
            </svg>

            {/* Center content */}
            <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className="text-4xl font-bold text-neutral-900 dark:text-white">
                    {Math.round(progress)}%
                </span>
                <span className="text-sm text-neutral-500 dark:text-neutral-400">
                    Complete
                </span>
            </div>
        </div>
    )
}

/* ============================================================================
   FORMAT TIME
   ============================================================================ */

function formatTime(minutes: number): string {
    if (minutes < 60) {
        return `${minutes}m`
    }
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    return mins > 0 ? `${hours}h ${mins}m` : `${hours}h`
}

/* ============================================================================
   MODULE PROGRESS COMPONENT
   ============================================================================ */

export function ModuleProgress({
    moduleId,
    progress,
    xpEarned,
    totalXP,
    timeSpentMinutes,
    tasksCompleted,
    totalTasks,
    tasks,
    nextTaskId,
    className
}: ModuleProgressProps) {
    return (
        <GlassCard
            variant="default"
            padding="lg"
            radius="xl"
            className={cn(
                "sticky top-24",
                className
            )}
        >
            {/* Progress Ring */}
            <div className="flex justify-center mb-6">
                <CircularProgress progress={progress} />
            </div>

            {/* Stats grid */}
            <div className="grid grid-cols-2 gap-4 mb-6">
                {/* XP */}
                <div className={cn(
                    "p-3 rounded-xl text-center",
                    "bg-xp-50 dark:bg-xp-900/20"
                )}>
                    <Zap className="w-5 h-5 mx-auto mb-1 text-xp-500" />
                    <div className="text-lg font-bold text-xp-600 dark:text-xp-400">
                        {xpEarned}
                    </div>
                    <div className="text-xs text-neutral-500">
                        of {totalXP} XP
                    </div>
                </div>

                {/* Time */}
                <div className={cn(
                    "p-3 rounded-xl text-center",
                    "bg-info-50 dark:bg-info-900/20"
                )}>
                    <Clock className="w-5 h-5 mx-auto mb-1 text-info-500" />
                    <div className="text-lg font-bold text-info-600 dark:text-info-400">
                        {formatTime(timeSpentMinutes)}
                    </div>
                    <div className="text-xs text-neutral-500">
                        Time Spent
                    </div>
                </div>
            </div>

            {/* Tasks summary */}
            <div className={cn(
                "flex items-center justify-between p-3 rounded-xl mb-6",
                "bg-neutral-100 dark:bg-neutral-800/50"
            )}>
                <div className="flex items-center gap-2">
                    <BookOpen className="w-5 h-5 text-primary-500" />
                    <span className="text-sm font-medium text-neutral-700 dark:text-neutral-300">
                        Tasks
                    </span>
                </div>
                <span className="text-sm font-bold text-neutral-900 dark:text-white">
                    {tasksCompleted} / {totalTasks}
                </span>
            </div>

            {/* Continue Learning button */}
            {nextTaskId ? (
                <Link href={`/modules/${moduleId}/tasks/${nextTaskId}`} className="block mb-6">
                    <Button
                        className={cn(
                            "w-full rounded-xl",
                            "bg-gradient-to-r from-primary-500 to-primary-600",
                            "hover:from-primary-600 hover:to-primary-700",
                            "shadow-lg shadow-primary-500/25"
                        )}
                    >
                        <PlayCircle className="w-4 h-4 mr-2" />
                        Continue Learning
                    </Button>
                </Link>
            ) : progress < 100 ? (
                <Link href={`/modules/${moduleId}`} className="block mb-6">
                    <Button
                        className={cn(
                            "w-full rounded-xl",
                            "bg-gradient-to-r from-primary-500 to-primary-600",
                            "hover:from-primary-600 hover:to-primary-700"
                        )}
                    >
                        <PlayCircle className="w-4 h-4 mr-2" />
                        Start Learning
                    </Button>
                </Link>
            ) : (
                <Button
                    variant="outline"
                    className="w-full rounded-xl mb-6"
                    disabled
                >
                    <CheckCircle2 className="w-4 h-4 mr-2 text-success-500" />
                    Module Complete
                </Button>
            )}

            {/* Mini task checklist */}
            <div className="border-t border-neutral-200 dark:border-neutral-700 pt-4">
                <h4 className="text-xs font-semibold text-neutral-500 uppercase tracking-wider mb-3">
                    Task Checklist
                </h4>
                <div className="space-y-2 max-h-48 overflow-y-auto">
                    {tasks.map((task, index) => (
                        <div
                            key={task.id}
                            className={cn(
                                "flex items-center gap-2 text-sm",
                                task.isComplete
                                    ? "text-neutral-400 dark:text-neutral-500"
                                    : "text-neutral-700 dark:text-neutral-300"
                            )}
                        >
                            {task.isComplete ? (
                                <CheckCircle2 className="w-4 h-4 text-success-500 flex-shrink-0" />
                            ) : (
                                <Circle className="w-4 h-4 text-neutral-300 dark:text-neutral-600 flex-shrink-0" />
                            )}
                            <span className={cn(
                                "truncate",
                                task.isComplete && "line-through"
                            )}>
                                {index + 1}. {task.title}
                            </span>
                        </div>
                    ))}
                </div>
            </div>
        </GlassCard>
    )
}

export default ModuleProgress
