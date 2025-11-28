"use client"

/**
 * ============================================================================
 * TASK NAVIGATION - Previous/Next Task Navigation
 * ============================================================================
 *
 * Features:
 * - Previous/Next task buttons
 * - Progress indicator (current/total)
 * - "Complete & Continue" button
 * - Keyboard navigation support
 * - Track-colored progress bar
 *
 * @phase C.2 - Task Content Display
 */

import * as React from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    ChevronLeft,
    ChevronRight,
    Check,
    ArrowRight,
    Loader2,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface TaskInfo {
    id: string
    title: string
}

interface TaskNavProps {
    moduleId: string
    moduleSlug?: string
    currentIndex: number
    totalTasks: number
    previousTask?: TaskInfo | null
    nextTask?: TaskInfo | null
    isCompleted?: boolean
    isCompleting?: boolean
    onComplete?: () => void | Promise<void>
    trackColor?: string
    className?: string
}

/* ============================================================================
   PROGRESS BAR
   ============================================================================ */

interface ProgressBarProps {
    current: number
    total: number
    trackColor?: string
}

function ProgressBar({ current, total, trackColor = "#6366f1" }: ProgressBarProps) {
    const percentage = total > 0 ? (current / total) * 100 : 0

    return (
        <div className="flex items-center gap-3">
            <div className="flex-1 h-2 bg-neutral-200 dark:bg-neutral-700 rounded-full overflow-hidden">
                <div
                    className="h-full rounded-full transition-all duration-500 ease-out"
                    style={{
                        width: `${percentage}%`,
                        backgroundColor: trackColor,
                    }}
                />
            </div>
            <span className="text-sm font-medium text-neutral-600 dark:text-neutral-400 whitespace-nowrap">
                {current} / {total}
            </span>
        </div>
    )
}

/* ============================================================================
   NAV BUTTON
   ============================================================================ */

interface NavButtonProps {
    task: TaskInfo | null | undefined
    moduleId: string
    direction: "prev" | "next"
}

function NavButton({ task, moduleId, direction }: NavButtonProps) {
    const isPrev = direction === "prev"

    if (!task) {
        return (
            <div className="flex-1">
                <Button
                    variant="ghost"
                    disabled
                    className={cn(
                        "w-full h-auto py-3 px-4 opacity-50",
                        isPrev ? "justify-start" : "justify-end"
                    )}
                >
                    {isPrev ? (
                        <ChevronLeft className="h-5 w-5 mr-2" />
                    ) : (
                        <ChevronRight className="h-5 w-5 ml-2" />
                    )}
                    <span className="text-sm text-neutral-400">
                        {isPrev ? "No previous task" : "No next task"}
                    </span>
                </Button>
            </div>
        )
    }

    return (
        <div className="flex-1">
            <Link href={`/modules/${moduleId}/tasks/${task.id}`}>
                <Button
                    variant="ghost"
                    className={cn(
                        "w-full h-auto py-3 px-4 group",
                        "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                        isPrev ? "justify-start text-left" : "justify-end text-right"
                    )}
                >
                    {isPrev && (
                        <ChevronLeft className="h-5 w-5 mr-2 text-neutral-400 group-hover:text-neutral-600 dark:group-hover:text-neutral-300 transition-colors" />
                    )}
                    <div className={cn("flex flex-col", isPrev ? "items-start" : "items-end")}>
                        <span className="text-xs text-neutral-400 uppercase tracking-wide">
                            {isPrev ? "Previous" : "Next"}
                        </span>
                        <span className="text-sm font-medium text-neutral-700 dark:text-neutral-200 line-clamp-1">
                            {task.title}
                        </span>
                    </div>
                    {!isPrev && (
                        <ChevronRight className="h-5 w-5 ml-2 text-neutral-400 group-hover:text-neutral-600 dark:group-hover:text-neutral-300 transition-colors" />
                    )}
                </Button>
            </Link>
        </div>
    )
}

/* ============================================================================
   MAIN TASK NAV COMPONENT
   ============================================================================ */

export function TaskNav({
    moduleId,
    currentIndex,
    totalTasks,
    previousTask,
    nextTask,
    isCompleted = false,
    isCompleting = false,
    onComplete,
    trackColor = "#6366f1",
    className,
}: TaskNavProps) {
    // Keyboard navigation
    React.useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            // Don't trigger if user is typing in an input
            if (
                e.target instanceof HTMLInputElement ||
                e.target instanceof HTMLTextAreaElement
            ) {
                return
            }

            if (e.key === "ArrowLeft" && previousTask) {
                window.location.href = `/modules/${moduleId}/tasks/${previousTask.id}`
            } else if (e.key === "ArrowRight" && nextTask) {
                window.location.href = `/modules/${moduleId}/tasks/${nextTask.id}`
            }
        }

        window.addEventListener("keydown", handleKeyDown)
        return () => window.removeEventListener("keydown", handleKeyDown)
    }, [moduleId, previousTask, nextTask])

    return (
        <div
            className={cn(
                "border-t border-neutral-200 dark:border-neutral-700",
                "bg-white dark:bg-neutral-900",
                className
            )}
        >
            {/* Progress bar */}
            <div className="px-6 py-3 border-b border-neutral-100 dark:border-neutral-800">
                <ProgressBar
                    current={currentIndex + 1}
                    total={totalTasks}
                    trackColor={trackColor}
                />
            </div>

            {/* Navigation buttons */}
            <div className="px-4 py-3">
                <div className="flex items-center gap-2">
                    {/* Previous button */}
                    <NavButton
                        task={previousTask}
                        moduleId={moduleId}
                        direction="prev"
                    />

                    {/* Complete & Continue button */}
                    <div className="flex-shrink-0">
                        {isCompleted ? (
                            <Button
                                variant="outline"
                                className="gap-2 text-green-600 border-green-200 bg-green-50 hover:bg-green-100 dark:bg-green-950/20 dark:border-green-800"
                                disabled
                            >
                                <Check className="h-4 w-4" />
                                Completed
                            </Button>
                        ) : (
                            <Button
                                onClick={onComplete}
                                disabled={isCompleting}
                                className="gap-2"
                                style={{ backgroundColor: trackColor }}
                            >
                                {isCompleting ? (
                                    <>
                                        <Loader2 className="h-4 w-4 animate-spin" />
                                        Saving...
                                    </>
                                ) : nextTask ? (
                                    <>
                                        Complete & Continue
                                        <ArrowRight className="h-4 w-4" />
                                    </>
                                ) : (
                                    <>
                                        <Check className="h-4 w-4" />
                                        Complete Task
                                    </>
                                )}
                            </Button>
                        )}
                    </div>

                    {/* Next button */}
                    <NavButton
                        task={nextTask}
                        moduleId={moduleId}
                        direction="next"
                    />
                </div>
            </div>

            {/* Keyboard hint */}
            <div className="hidden md:flex items-center justify-center py-2 border-t border-neutral-100 dark:border-neutral-800">
                <span className="text-xs text-neutral-400">
                    Use <kbd className="px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-neutral-600 dark:text-neutral-400 font-mono">←</kbd> and{" "}
                    <kbd className="px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-neutral-600 dark:text-neutral-400 font-mono">→</kbd> to navigate
                </span>
            </div>
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default TaskNav
