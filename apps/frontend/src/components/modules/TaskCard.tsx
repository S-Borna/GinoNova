"use client"

/**
 * ============================================================================
 * TASK CARD — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Clean task list item with:
 * - Animated checkbox
 * - Type badge (color coded)
 * - XP reward badge
 * - Expandable description
 * - Multiple states
 *
 * @phase D.4 - Modules UI
 */

import { useState } from "react"
import { cn } from "@/lib/utils"
import {
    Circle,
    CheckCircle2,
    Loader2,
    ChevronDown,
    ChevronUp,
    Star,
    Zap
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type TaskType =
    | "foundation"
    | "practice"
    | "deepening"
    | "project"
    | "challenge"
    | "quiz"

export type TaskCardStatus = "not_started" | "in_progress" | "complete"

export interface TaskCardProps {
    id: string
    orderIndex: number
    title: string
    description?: string
    type: TaskType
    difficulty: number // 1-5
    xpReward: number
    status: TaskCardStatus
    onToggleComplete?: (id: string) => void
    onClick?: (id: string) => void
    isLoading?: boolean
    className?: string
}

/* ============================================================================
   TYPE CONFIG
   ============================================================================ */

const typeConfig: Record<TaskType, {
    label: string
    color: string
    bgColor: string
}> = {
    foundation: {
        label: "Foundation",
        color: "text-blue-600 dark:text-blue-400",
        bgColor: "bg-blue-100 dark:bg-blue-900/30"
    },
    practice: {
        label: "Practice",
        color: "text-green-600 dark:text-green-400",
        bgColor: "bg-green-100 dark:bg-green-900/30"
    },
    deepening: {
        label: "Deepening",
        color: "text-purple-600 dark:text-purple-400",
        bgColor: "bg-purple-100 dark:bg-purple-900/30"
    },
    project: {
        label: "Project",
        color: "text-orange-600 dark:text-orange-400",
        bgColor: "bg-orange-100 dark:bg-orange-900/30"
    },
    challenge: {
        label: "Challenge",
        color: "text-red-600 dark:text-red-400",
        bgColor: "bg-red-100 dark:bg-red-900/30"
    },
    quiz: {
        label: "Quiz",
        color: "text-cyan-600 dark:text-cyan-400",
        bgColor: "bg-cyan-100 dark:bg-cyan-900/30"
    }
}

/* ============================================================================
   DIFFICULTY INDICATOR
   ============================================================================ */

function DifficultyIndicator({ difficulty }: { difficulty: number }) {
    return (
        <div className="flex items-center gap-0.5">
            {Array.from({ length: 5 }).map((_, i) => (
                <Star
                    key={i}
                    className={cn(
                        "w-3 h-3 transition-colors",
                        i < difficulty
                            ? "text-warning-500 fill-warning-500"
                            : "text-neutral-300 dark:text-neutral-600"
                    )}
                />
            ))}
        </div>
    )
}

/* ============================================================================
   TASK CARD COMPONENT
   ============================================================================ */

export function TaskCard({
    id,
    orderIndex,
    title,
    description,
    type,
    difficulty,
    xpReward,
    status,
    onToggleComplete,
    onClick,
    isLoading = false,
    className
}: TaskCardProps) {
    const [isExpanded, setIsExpanded] = useState(false)
    const config = typeConfig[type]
    const isComplete = status === "complete"
    const isInProgress = status === "in_progress"

    const handleCheckboxClick = (e: React.MouseEvent) => {
        e.preventDefault()
        e.stopPropagation()
        if (!isLoading && onToggleComplete) {
            onToggleComplete(id)
        }
    }

    const handleCardClick = () => {
        if (onClick) {
            onClick(id)
        }
    }

    const handleExpandClick = (e: React.MouseEvent) => {
        e.preventDefault()
        e.stopPropagation()
        setIsExpanded(!isExpanded)
    }

    return (
        <div
            className={cn(
                "group relative rounded-xl transition-all duration-200",
                "bg-white dark:bg-neutral-800/50",
                "border border-neutral-200/50 dark:border-neutral-700/50",
                "hover:border-primary-200 dark:hover:border-primary-800/50",
                "hover:shadow-md hover:shadow-primary-500/5",
                onClick && "cursor-pointer",
                isComplete && "opacity-80",
                className
            )}
            onClick={handleCardClick}
        >
            <div className="flex items-start gap-3 p-4">
                {/* Checkbox */}
                <button
                    onClick={handleCheckboxClick}
                    disabled={isLoading}
                    className={cn(
                        "flex-shrink-0 mt-0.5 w-6 h-6 rounded-full transition-all duration-300",
                        "flex items-center justify-center",
                        isLoading && "cursor-wait",
                        !isComplete && !isInProgress && [
                            "border-2 border-neutral-300 dark:border-neutral-600",
                            "hover:border-primary-400 hover:bg-primary-50 dark:hover:bg-primary-900/20"
                        ],
                        isInProgress && [
                            "border-2 border-primary-400",
                            "bg-primary-100 dark:bg-primary-900/30"
                        ],
                        isComplete && [
                            "bg-success-500 border-success-500",
                            "animate-scale-in"
                        ]
                    )}
                >
                    {isLoading ? (
                        <Loader2 className="w-4 h-4 text-primary-500 animate-spin" />
                    ) : isComplete ? (
                        <CheckCircle2 className="w-5 h-5 text-white" />
                    ) : isInProgress ? (
                        <Loader2 className="w-4 h-4 text-primary-500" />
                    ) : (
                        <Circle className="w-4 h-4 text-neutral-400 opacity-0 group-hover:opacity-100 transition-opacity" />
                    )}
                </button>

                {/* Content */}
                <div className="flex-1 min-w-0">
                    {/* Top row: Task number + Type badge + Difficulty */}
                    <div className="flex items-center gap-2 mb-1">
                        <span className="text-xs font-medium text-neutral-400 dark:text-neutral-500">
                            Task {orderIndex}
                        </span>
                        <span className={cn(
                            "px-2 py-0.5 rounded-full text-xs font-medium",
                            config.bgColor,
                            config.color
                        )}>
                            {config.label}
                        </span>
                        <DifficultyIndicator difficulty={difficulty} />
                    </div>

                    {/* Title */}
                    <h4 className={cn(
                        "text-base font-medium transition-colors",
                        isComplete
                            ? "text-neutral-500 dark:text-neutral-400 line-through decoration-neutral-400/50"
                            : "text-neutral-900 dark:text-white"
                    )}>
                        {title}
                    </h4>

                    {/* Description preview (if exists and expanded) */}
                    {description && isExpanded && (
                        <p className="mt-2 text-sm text-neutral-600 dark:text-neutral-400 animate-fade-in">
                            {description}
                        </p>
                    )}
                </div>

                {/* Right side: XP + Expand button */}
                <div className="flex items-center gap-2 flex-shrink-0">
                    {/* XP Badge */}
                    <div className={cn(
                        "flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold",
                        isComplete
                            ? "bg-success-100 dark:bg-success-900/30 text-success-600 dark:text-success-400"
                            : "bg-xp-100 dark:bg-xp-900/30 text-xp-600 dark:text-xp-400"
                    )}>
                        <Zap className="w-3 h-3" />
                        <span>{xpReward} XP</span>
                    </div>

                    {/* Expand button (if has description) */}
                    {description && (
                        <button
                            onClick={handleExpandClick}
                            className={cn(
                                "p-1 rounded-lg transition-colors",
                                "text-neutral-400 hover:text-neutral-600",
                                "hover:bg-neutral-100 dark:hover:bg-neutral-700"
                            )}
                        >
                            {isExpanded ? (
                                <ChevronUp className="w-4 h-4" />
                            ) : (
                                <ChevronDown className="w-4 h-4" />
                            )}
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}

export default TaskCard
