"use client"

/**
 * ============================================================================
 * TASK EXERCISE — Interactive exercise component
 * ============================================================================
 *
 * Exercise section for tasks with:
 * - Highlighted background
 * - Clear structure
 * - Checkpoints
 *
 * @version 2.0
 * @date 2025-11-29
 */

import { cn } from "@/lib/utils"
import { Lightbulb, CheckCircle2, Circle } from "lucide-react"

interface TaskExerciseProps {
    title: string
    description?: string
    steps?: string[]
    completedSteps?: number[]
    hint?: string
    className?: string
}

export function TaskExercise({
    title,
    description,
    steps = [],
    completedSteps = [],
    hint,
    className
}: TaskExerciseProps) {
    return (
        <div
            className={cn(
                // Background
                "bg-gradient-to-br from-amber-50/80 to-orange-50/60",
                "dark:from-amber-950/20 dark:to-orange-950/20",
                // Border
                "border border-amber-200/50 dark:border-amber-800/30",
                // Border radius
                "rounded-xl",
                // Padding
                "p-6",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-start gap-3 mb-4">
                <div className="p-2 rounded-lg bg-amber-100 dark:bg-amber-900/40">
                    <Lightbulb className="w-5 h-5 text-amber-600 dark:text-amber-400" />
                </div>
                <div>
                    <h3 className="text-lg font-medium text-neutral-900 dark:text-white">
                        {title}
                    </h3>
                    {description && (
                        <p className="mt-1 text-sm text-neutral-600 dark:text-neutral-400">
                            {description}
                        </p>
                    )}
                </div>
            </div>

            {/* Steps */}
            {steps.length > 0 && (
                <div className="space-y-3 mt-4">
                    {steps.map((step, index) => {
                        const isCompleted = completedSteps.includes(index)
                        return (
                            <div
                                key={index}
                                className={cn(
                                    "flex items-start gap-3 p-3 rounded-lg",
                                    "transition-colors duration-200",
                                    isCompleted
                                        ? "bg-emerald-100/50 dark:bg-emerald-900/20"
                                        : "bg-white/60 dark:bg-neutral-800/40"
                                )}
                            >
                                {isCompleted ? (
                                    <CheckCircle2 className="w-5 h-5 text-emerald-500 flex-shrink-0 mt-0.5" />
                                ) : (
                                    <Circle className="w-5 h-5 text-neutral-300 dark:text-neutral-600 flex-shrink-0 mt-0.5" />
                                )}
                                <span
                                    className={cn(
                                        "text-sm",
                                        isCompleted
                                            ? "text-emerald-700 dark:text-emerald-300"
                                            : "text-neutral-700 dark:text-neutral-300"
                                    )}
                                >
                                    {step}
                                </span>
                            </div>
                        )
                    })}
                </div>
            )}

            {/* Hint */}
            {hint && (
                <div className="mt-4 pt-4 border-t border-amber-200/50 dark:border-amber-800/30">
                    <p className="text-xs text-amber-600 dark:text-amber-400">
                        💡 <span className="font-medium">Hint:</span> {hint}
                    </p>
                </div>
            )}
        </div>
    )
}

export default TaskExercise
