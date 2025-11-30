"use client"

/**
 * ============================================================================
 * RELATED TASKS - Fördjupning / Deep Dive Component
 * ============================================================================
 *
 * Shows optional advanced or deep-dive tasks related to the current task.
 * These are NOT locked - users can try them anytime for extra XP.
 *
 * @phase 4.0 - Task Tier System (v4 content as optional related tasks)
 */

import Link from "next/link"
import { cn } from "@saas/ui"
import { GlassCard } from "@/components/ui/glass-card"
import {
    Sparkles,
    ChevronRight,
    Clock,
    Zap,
    BookOpen,
    Rocket,
    GraduationCap,
} from "lucide-react"

export interface RelatedTask {
    id: string
    title: string
    description?: string | null
    task_tier: "standard" | "advanced" | "deep_dive"
    difficulty: "easy" | "medium" | "hard"
    estimated_minutes: number
    xp_reward: number
}

interface RelatedTasksProps {
    tasks: RelatedTask[]
    moduleId: string
    className?: string
}

const tierConfig = {
    advanced: {
        label: "Fördjupning",
        labelEn: "Advanced",
        icon: Rocket,
        bgColor: "bg-purple-500/10 dark:bg-purple-500/20",
        borderColor: "border-purple-500/30",
        textColor: "text-purple-600 dark:text-purple-400",
        badgeColor: "bg-purple-100 text-purple-700 dark:bg-purple-900/50 dark:text-purple-300",
    },
    deep_dive: {
        label: "Deep Dive",
        labelEn: "Expert",
        icon: GraduationCap,
        bgColor: "bg-amber-500/10 dark:bg-amber-500/20",
        borderColor: "border-amber-500/30",
        textColor: "text-amber-600 dark:text-amber-400",
        badgeColor: "bg-amber-100 text-amber-700 dark:bg-amber-900/50 dark:text-amber-300",
    },
    standard: {
        label: "Standard",
        labelEn: "Standard",
        icon: BookOpen,
        bgColor: "bg-blue-500/10 dark:bg-blue-500/20",
        borderColor: "border-blue-500/30",
        textColor: "text-blue-600 dark:text-blue-400",
        badgeColor: "bg-blue-100 text-blue-700 dark:bg-blue-900/50 dark:text-blue-300",
    },
}

function RelatedTaskCard({ task, moduleId }: { task: RelatedTask; moduleId: string }) {
    const config = tierConfig[task.task_tier] || tierConfig.advanced
    const TierIcon = config.icon

    return (
        <Link
            href={`/modules/${moduleId}/tasks/${task.id}`}
            className="block group"
        >
            <div
                className={cn(
                    "relative p-4 rounded-xl border transition-all duration-200",
                    "bg-white/60 dark:bg-neutral-900/60 backdrop-blur-sm",
                    "border-neutral-200/50 dark:border-neutral-700/50",
                    "hover:border-purple-400 dark:hover:border-purple-500",
                    "hover:shadow-lg hover:shadow-purple-500/10",
                    "hover:-translate-y-0.5"
                )}
            >
                {/* Tier badge */}
                <div className="flex items-center justify-between mb-3">
                    <span
                        className={cn(
                            "inline-flex items-center gap-1.5 px-2 py-1 rounded-lg text-xs font-medium",
                            config.badgeColor
                        )}
                    >
                        <TierIcon className="w-3.5 h-3.5" />
                        {config.label}
                    </span>
                    <span
                        className={cn(
                            "px-2 py-0.5 rounded text-xs font-medium",
                            task.difficulty === "easy" && "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/50 dark:text-emerald-300",
                            task.difficulty === "medium" && "bg-amber-100 text-amber-700 dark:bg-amber-900/50 dark:text-amber-300",
                            task.difficulty === "hard" && "bg-red-100 text-red-700 dark:bg-red-900/50 dark:text-red-300"
                        )}
                    >
                        {task.difficulty}
                    </span>
                </div>

                {/* Title */}
                <h4 className="font-semibold text-neutral-900 dark:text-white mb-1 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors">
                    {task.title}
                </h4>

                {/* Description */}
                {task.description && (
                    <p className="text-sm text-neutral-600 dark:text-neutral-400 line-clamp-2 mb-3">
                        {task.description}
                    </p>
                )}

                {/* Meta */}
                <div className="flex items-center justify-between text-xs">
                    <div className="flex items-center gap-3 text-neutral-500">
                        <span className="flex items-center gap-1">
                            <Clock className="w-3.5 h-3.5" />
                            {task.estimated_minutes} min
                        </span>
                        <span className="flex items-center gap-1 text-purple-500 font-medium">
                            <Zap className="w-3.5 h-3.5" />
                            +{task.xp_reward} XP
                        </span>
                    </div>
                    <ChevronRight className="w-4 h-4 text-neutral-400 group-hover:text-purple-500 group-hover:translate-x-0.5 transition-all" />
                </div>
            </div>
        </Link>
    )
}

export function RelatedTasks({ tasks, moduleId, className }: RelatedTasksProps) {
    if (!tasks || tasks.length === 0) {
        return null
    }

    return (
        <div className={cn("mt-8", className)}>
            <GlassCard
                variant="default"
                padding="md"
                radius="xl"
                className={cn(
                    "border-purple-500/20 dark:border-purple-500/30",
                    "bg-gradient-to-br from-purple-50/50 to-white dark:from-purple-950/20 dark:to-neutral-900"
                )}
            >
                {/* Header */}
                <div className="flex items-center gap-3 mb-4 pb-3 border-b border-purple-200/50 dark:border-purple-800/50">
                    <div
                        className={cn(
                            "w-10 h-10 rounded-xl flex items-center justify-center",
                            "bg-purple-500/10 dark:bg-purple-500/20"
                        )}
                    >
                        <Sparkles className="w-5 h-5 text-purple-500" />
                    </div>
                    <div>
                        <h3 className="font-semibold text-neutral-900 dark:text-white">
                            Vill du fördjupa dig?
                        </h3>
                        <p className="text-sm text-neutral-600 dark:text-neutral-400">
                            Utforska relaterade avancerade lektioner för extra XP
                        </p>
                    </div>
                </div>

                {/* Task cards */}
                <div className="space-y-3">
                    {tasks.map((task) => (
                        <RelatedTaskCard
                            key={task.id}
                            task={task}
                            moduleId={moduleId}
                        />
                    ))}
                </div>

                {/* Footer note */}
                <p className="mt-4 pt-3 border-t border-purple-200/50 dark:border-purple-800/50 text-xs text-neutral-500 dark:text-neutral-400 text-center">
                    💡 Dessa lektioner är valfria och ger extra XP
                </p>
            </GlassCard>
        </div>
    )
}

export default RelatedTasks
