"use client"

/**
 * ============================================================================
 * MODULE CARD — Apple-Inspired Design (D.4)
 * ============================================================================
 *
 * Beautiful module card with:
 * - Glass card styling with gradient border on hover
 * - Module number badge
 * - Progress bar with percentage
 * - Status indicators
 * - Smooth hover animations
 *
 * @phase D.4 - Modules UI
 */

import { cn } from "@/lib/utils"
import Link from "next/link"
import {
    Lock,
    Circle,
    PlayCircle,
    CheckCircle2,
    ChevronRight,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type ModuleStatus = "locked" | "not_started" | "in_progress" | "complete"

export interface ModuleCardProps {
    id: string
    orderIndex: number
    title: string
    description: string
    icon?: string // emoji
    progress: number // 0-100
    tasksCompleted: number
    totalTasks: number
    status: ModuleStatus
    estimatedHours?: number
    prerequisiteModule?: string // Name of prerequisite if locked
    className?: string
}

/* ============================================================================
   STATUS CONFIG
   ============================================================================ */

const statusConfig: Record<ModuleStatus, {
    icon: React.ComponentType<{ className?: string }>
    label: string
    color: string
    bgColor: string
    buttonText: string
}> = {
    locked: {
        icon: Lock,
        label: "Locked",
        color: "text-neutral-400",
        bgColor: "bg-neutral-100 dark:bg-neutral-800",
        buttonText: "Locked"
    },
    not_started: {
        icon: Circle,
        label: "Not Started",
        color: "text-neutral-500",
        bgColor: "bg-neutral-100 dark:bg-neutral-800",
        buttonText: "Start"
    },
    in_progress: {
        icon: PlayCircle,
        label: "In Progress",
        color: "text-primary-500",
        bgColor: "bg-primary-100 dark:bg-primary-900/30",
        buttonText: "Continue"
    },
    complete: {
        icon: CheckCircle2,
        label: "Complete",
        color: "text-success-500",
        bgColor: "bg-success-100 dark:bg-success-900/30",
        buttonText: "Review"
    }
}

/* ============================================================================
   MODULE CARD COMPONENT
   ============================================================================ */

export function ModuleCard({
    id,
    orderIndex,
    title,
    description,
    icon = "📚",
    progress,
    tasksCompleted,
    totalTasks,
    status,
    estimatedHours,
    prerequisiteModule,
    className
}: ModuleCardProps) {
    const config = statusConfig[status]
    const StatusIcon = config.icon
    const isLocked = status === "locked"

    const cardContent = (
        <div
            className={cn(
                "bg-white dark:bg-neutral-800 rounded-xl shadow-sm border border-gray-100 dark:border-neutral-700 p-6 transition-all duration-200",
                !isLocked && "hover:shadow-md hover:-translate-y-0.5 cursor-pointer",
                isLocked && "opacity-70 cursor-not-allowed",
                className
            )}
        >
            {/* Top row: Icon + Title + Status */}
            <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                    {/* Module icon */}
                    <span className="text-2xl">{isLocked ? "🔒" : icon}</span>
                    <div>
                        <h3 className={cn(
                            "font-semibold",
                            isLocked
                                ? "text-gray-400 dark:text-neutral-500"
                                : "text-gray-900 dark:text-white"
                        )}>
                            {title}
                        </h3>
                        <p className="text-sm text-gray-500 dark:text-neutral-400">
                            {tasksCompleted} / {totalTasks} tasks
                        </p>
                    </div>
                </div>

                {/* Status badge */}
                <span className={cn(
                    "px-2.5 py-1 text-xs font-medium rounded-full",
                    status === "complete" && "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400",
                    status === "in_progress" && "bg-indigo-100 text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-400",
                    status === "not_started" && "bg-gray-100 text-gray-600 dark:bg-neutral-700 dark:text-neutral-400",
                    status === "locked" && "bg-gray-100 text-gray-400 dark:bg-neutral-700 dark:text-neutral-500"
                )}>
                    {config.label}
                </span>
            </div>

            {/* Description */}
            {description && (
                <p className={cn(
                    "text-sm line-clamp-2 mb-4",
                    isLocked
                        ? "text-gray-400 dark:text-neutral-500"
                        : "text-gray-600 dark:text-neutral-400"
                )}>
                    {description}
                </p>
            )}

            {/* Progress bar */}
            <div className="mb-4">
                <div className="w-full bg-gray-200 dark:bg-neutral-700 rounded-full h-2">
                    <div
                        className={cn(
                            "h-2 rounded-full transition-all duration-500",
                            status === "complete"
                                ? "bg-gradient-to-r from-emerald-500 to-teal-500"
                                : "bg-gradient-to-r from-indigo-500 to-purple-500"
                        )}
                        style={{ width: `${progress}%` }}
                    />
                </div>
                <div className="flex justify-between text-xs mt-1.5">
                    <span className="text-gray-500 dark:text-neutral-400">
                        {estimatedHours && `~${estimatedHours}h`}
                    </span>
                    <span className={cn(
                        "font-medium",
                        status === "complete" ? "text-emerald-600" : "text-indigo-600"
                    )}>
                        {progress}%
                    </span>
                </div>
            </div>

            {/* Action button / Locked message */}
            {isLocked ? (
                <div className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl bg-gray-100 dark:bg-neutral-700 text-gray-400 text-sm">
                    <Lock className="w-4 h-4" />
                    <span>Complete {prerequisiteModule || "previous"} first</span>
                </div>
            ) : (
                <button
                    className={cn(
                        "w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-medium transition-all duration-200",
                        status === "complete"
                            ? "bg-gray-100 dark:bg-neutral-700 text-gray-700 dark:text-neutral-300 hover:bg-gray-200 dark:hover:bg-neutral-600"
                            : status === "in_progress"
                                ? "bg-gradient-to-r from-indigo-500 to-purple-600 text-white hover:shadow-lg"
                                : "bg-indigo-500 text-white hover:bg-indigo-600"
                    )}
                >
                    <span>{config.buttonText}</span>
                    <ChevronRight className="w-4 h-4" />
                </button>
            )}
        </div>
    )

    // Wrap in link if not locked
    if (isLocked) {
        return cardContent
    }

    return (
        <Link href={`/modules/${id}`} className="block">
            {cardContent}
        </Link>
    )
}

export default ModuleCard
