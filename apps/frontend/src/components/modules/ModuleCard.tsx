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
import { GlassCard } from "@/components/ui/glass-card"
import { ProgressBar } from "@/components/ui/progress-bar"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import {
    Lock,
    Circle,
    PlayCircle,
    CheckCircle2,
    Clock,
    ChevronRight,
    BookOpen
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
        <GlassCard
            variant="default"
            padding="none"
            radius="xl"
            interactive={!isLocked}
            className={cn(
                "group relative overflow-hidden transition-all duration-300",
                // Hover effects for non-locked cards
                !isLocked && [
                    "hover:-translate-y-1",
                    "hover:shadow-xl hover:shadow-primary-500/10",
                    "dark:hover:shadow-primary-500/5"
                ],
                // Locked state styling
                isLocked && "opacity-70 cursor-not-allowed",
                className
            )}
        >
            {/* Gradient border on hover (non-locked only) */}
            {!isLocked && (
                <div className={cn(
                    "absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-300",
                    "bg-gradient-to-br from-primary-500/20 via-transparent to-primary-600/20",
                    "group-hover:opacity-100"
                )} />
            )}

            {/* Card content */}
            <div className="relative p-6">
                {/* Top row: Number badge + Status */}
                <div className="flex items-center justify-between mb-4">
                    {/* Module number badge */}
                    <div className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center",
                        "text-sm font-bold",
                        isLocked
                            ? "bg-neutral-200 dark:bg-neutral-700 text-neutral-400"
                            : "bg-gradient-to-br from-primary-500 to-primary-600 text-white shadow-lg shadow-primary-500/25"
                    )}>
                        {String(orderIndex).padStart(2, "0")}
                    </div>

                    {/* Status badge */}
                    <div className={cn(
                        "flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium",
                        config.bgColor,
                        config.color
                    )}>
                        <StatusIcon className="w-3.5 h-3.5" />
                        <span>{config.label}</span>
                    </div>
                </div>

                {/* Icon + Title + Description */}
                <div className="mb-4">
                    {/* Large icon */}
                    <div className={cn(
                        "text-4xl mb-3 transition-transform duration-300",
                        !isLocked && "group-hover:scale-110"
                    )}>
                        {icon}
                    </div>

                    {/* Title */}
                    <h3 className={cn(
                        "text-lg font-semibold mb-1.5",
                        isLocked
                            ? "text-neutral-400 dark:text-neutral-500"
                            : "text-neutral-900 dark:text-white"
                    )}>
                        {title}
                    </h3>

                    {/* Description (2 lines max) */}
                    <p className={cn(
                        "text-sm line-clamp-2",
                        isLocked
                            ? "text-neutral-400 dark:text-neutral-500"
                            : "text-neutral-600 dark:text-neutral-400"
                    )}>
                        {description}
                    </p>
                </div>

                {/* Progress section */}
                <div className="mb-4 space-y-2">
                    {/* Progress bar */}
                    <ProgressBar
                        value={progress}
                        className={cn(
                            "h-2",
                            isLocked && "opacity-50"
                        )}
                    />

                    {/* Progress text */}
                    <div className="flex items-center justify-between text-xs">
                        <span className={cn(
                            isLocked
                                ? "text-neutral-400"
                                : "text-neutral-600 dark:text-neutral-400"
                        )}>
                            <BookOpen className="w-3 h-3 inline-block mr-1" />
                            {tasksCompleted}/{totalTasks} tasks
                        </span>
                        <span className={cn(
                            "font-medium",
                            status === "complete"
                                ? "text-success-500"
                                : isLocked
                                    ? "text-neutral-400"
                                    : "text-primary-500"
                        )}>
                            {progress}%
                        </span>
                    </div>
                </div>

                {/* Estimated time (if provided) */}
                {estimatedHours && (
                    <div className={cn(
                        "flex items-center gap-1.5 text-xs mb-4",
                        isLocked
                            ? "text-neutral-400"
                            : "text-neutral-500 dark:text-neutral-400"
                    )}>
                        <Clock className="w-3.5 h-3.5" />
                        <span>~{estimatedHours} hours</span>
                    </div>
                )}

                {/* Action button / Locked message */}
                {isLocked ? (
                    <div className={cn(
                        "flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl",
                        "bg-neutral-100 dark:bg-neutral-800",
                        "text-neutral-400 text-sm"
                    )}>
                        <Lock className="w-4 h-4" />
                        <span>Complete {prerequisiteModule || "previous module"} to unlock</span>
                    </div>
                ) : (
                    <Button
                        variant={status === "complete" ? "outline" : "default"}
                        className={cn(
                            "w-full rounded-xl group/btn",
                            status === "in_progress" && "bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700"
                        )}
                    >
                        <span>{config.buttonText}</span>
                        <ChevronRight className="w-4 h-4 ml-1 transition-transform group-hover/btn:translate-x-0.5" />
                    </Button>
                )}
            </div>
        </GlassCard>
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
