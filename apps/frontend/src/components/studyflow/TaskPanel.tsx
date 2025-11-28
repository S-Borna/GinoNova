/**
 * ============================================================================
 * TASK PANEL — Current Task Display for Studyflow
 * ============================================================================
 *
 * Shows the currently selected task with ability to:
 * - View task content
 * - Mark as complete
 * - Navigate to next task
 *
 * @phase A.6 - Studyflow Integration
 */

"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import {
    CheckCircle2,
    ChevronDown,
    ChevronUp,
    FileText,
    Clock,
    Zap,
    ArrowRight,
    ExternalLink,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import Link from "next/link"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface TaskPanelTask {
    id: string
    title: string
    description?: string
    type: "lesson" | "quiz" | "exercise" | "lab"
    xpReward: number
    estimatedMinutes?: number
    moduleId: string
    moduleName: string
    isCompleted: boolean
}

interface TaskPanelProps {
    currentTask: TaskPanelTask | null
    nextTask?: TaskPanelTask | null
    onCompleteTask: (taskId: string, xpReward: number) => void
    onSelectTask?: (task: TaskPanelTask) => void
    isLoading?: boolean
    className?: string
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function TaskPanel({
    currentTask,
    nextTask,
    onCompleteTask,
    onSelectTask,
    isLoading = false,
    className,
}: TaskPanelProps) {
    const [isExpanded, setIsExpanded] = useState(true)
    const [isCompleting, setIsCompleting] = useState(false)

    const handleComplete = async () => {
        if (!currentTask || currentTask.isCompleted) return

        setIsCompleting(true)
        try {
            await onCompleteTask(currentTask.id, currentTask.xpReward)
        } finally {
            setIsCompleting(false)
        }
    }

    const handleSelectNext = () => {
        if (nextTask && onSelectTask) {
            onSelectTask(nextTask)
        }
    }

    const getTypeIcon = (type: TaskPanelTask["type"]) => {
        switch (type) {
            case "lesson":
                return "📖"
            case "quiz":
                return "❓"
            case "exercise":
                return "💻"
            case "lab":
                return "🧪"
            default:
                return "📝"
        }
    }

    const getTypeColor = (type: TaskPanelTask["type"]) => {
        switch (type) {
            case "lesson":
                return "text-blue-400"
            case "quiz":
                return "text-purple-400"
            case "exercise":
                return "text-green-400"
            case "lab":
                return "text-orange-400"
            default:
                return "text-gray-400"
        }
    }

    if (!currentTask) {
        return (
            <div
                className={cn(
                    "p-4 rounded-xl bg-white/5 border border-white/10",
                    className
                )}
            >
                <div className="flex items-center gap-3 text-muted-foreground">
                    <FileText className="w-5 h-5" />
                    <span>No task selected</span>
                </div>
                <p className="mt-2 text-sm text-muted-foreground">
                    Select a task to work on during your focus session.
                </p>
            </div>
        )
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-xl bg-white/5 border border-white/10 overflow-hidden",
                className
            )}
        >
            {/* Header */}
            <button
                onClick={() => setIsExpanded(!isExpanded)}
                className={cn(
                    "w-full p-4 flex items-center justify-between",
                    "hover:bg-white/5 transition-colors"
                )}
            >
                <div className="flex items-center gap-3">
                    <span className="text-xl">{getTypeIcon(currentTask.type)}</span>
                    <div className="text-left">
                        <p className="text-xs text-muted-foreground">
                            Current Task
                        </p>
                        <p className="font-medium text-white line-clamp-1">
                            {currentTask.title}
                        </p>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    {currentTask.isCompleted && (
                        <CheckCircle2 className="w-5 h-5 text-green-400" />
                    )}
                    {isExpanded ? (
                        <ChevronUp className="w-5 h-5 text-muted-foreground" />
                    ) : (
                        <ChevronDown className="w-5 h-5 text-muted-foreground" />
                    )}
                </div>
            </button>

            {/* Expanded content */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.2 }}
                        className="overflow-hidden"
                    >
                        <div className="px-4 pb-4 space-y-4">
                            {/* Module info */}
                            <div className="flex items-center gap-2 text-sm text-muted-foreground">
                                <span>{currentTask.moduleName}</span>
                            </div>

                            {/* Task metadata */}
                            <div className="flex items-center gap-4 text-sm">
                                <span
                                    className={cn(
                                        "capitalize px-2 py-0.5 rounded-full text-xs",
                                        "bg-white/10",
                                        getTypeColor(currentTask.type)
                                    )}
                                >
                                    {currentTask.type}
                                </span>
                                {currentTask.estimatedMinutes && (
                                    <span className="flex items-center gap-1 text-muted-foreground">
                                        <Clock className="w-3.5 h-3.5" />
                                        {currentTask.estimatedMinutes}m
                                    </span>
                                )}
                                <span className="flex items-center gap-1 text-orange-400">
                                    <Zap className="w-3.5 h-3.5" />
                                    {currentTask.xpReward} XP
                                </span>
                            </div>

                            {/* Description */}
                            {currentTask.description && (
                                <p className="text-sm text-muted-foreground line-clamp-2">
                                    {currentTask.description}
                                </p>
                            )}

                            {/* Actions */}
                            <div className="flex items-center gap-2 pt-2">
                                {!currentTask.isCompleted ? (
                                    <Button
                                        onClick={handleComplete}
                                        disabled={isCompleting || isLoading}
                                        className="flex-1 bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600"
                                    >
                                        {isCompleting ? (
                                            <span className="flex items-center gap-2">
                                                <motion.div
                                                    animate={{ rotate: 360 }}
                                                    transition={{
                                                        duration: 1,
                                                        repeat: Infinity,
                                                        ease: "linear",
                                                    }}
                                                    className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full"
                                                />
                                                Completing...
                                            </span>
                                        ) : (
                                            <span className="flex items-center gap-2">
                                                <CheckCircle2 className="w-4 h-4" />
                                                Mark Complete
                                            </span>
                                        )}
                                    </Button>
                                ) : (
                                    <Button
                                        onClick={handleSelectNext}
                                        disabled={!nextTask}
                                        className="flex-1 bg-gradient-to-r from-indigo-500 to-purple-500"
                                    >
                                        <span className="flex items-center gap-2">
                                            Next Task
                                            <ArrowRight className="w-4 h-4" />
                                        </span>
                                    </Button>
                                )}

                                <Button
                                    variant="outline"
                                    size="icon"
                                    asChild
                                    className="shrink-0"
                                >
                                    <Link
                                        href={`/modules/${currentTask.moduleId}/tasks/${currentTask.id}`}
                                        target="_blank"
                                    >
                                        <ExternalLink className="w-4 h-4" />
                                    </Link>
                                </Button>
                            </div>

                            {/* Next task preview */}
                            {nextTask && !currentTask.isCompleted && (
                                <div className="pt-2 border-t border-white/10">
                                    <p className="text-xs text-muted-foreground mb-1">
                                        Up next:
                                    </p>
                                    <p className="text-sm text-white/70 flex items-center gap-2">
                                        <span>{getTypeIcon(nextTask.type)}</span>
                                        <span className="line-clamp-1">{nextTask.title}</span>
                                    </p>
                                </div>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    )
}

/* ============================================================================
   TASK SELECTOR COMPONENT
   ============================================================================ */

interface TaskSelectorProps {
    tasks: TaskPanelTask[]
    selectedTaskId?: string
    onSelectTask: (task: TaskPanelTask) => void
    className?: string
}

export function TaskSelector({
    tasks,
    selectedTaskId,
    onSelectTask,
    className,
}: TaskSelectorProps) {
    const incompleteTasks = tasks.filter((t) => !t.isCompleted)
    const completedTasks = tasks.filter((t) => t.isCompleted)

    const getTypeIcon = (type: TaskPanelTask["type"]) => {
        switch (type) {
            case "lesson":
                return "📖"
            case "quiz":
                return "❓"
            case "exercise":
                return "💻"
            case "lab":
                return "🧪"
            default:
                return "📝"
        }
    }

    return (
        <div className={cn("space-y-4", className)}>
            {/* Incomplete tasks */}
            {incompleteTasks.length > 0 && (
                <div>
                    <h4 className="text-sm font-medium text-muted-foreground mb-2">
                        Available Tasks ({incompleteTasks.length})
                    </h4>
                    <div className="space-y-2">
                        {incompleteTasks.map((task) => (
                            <button
                                key={task.id}
                                onClick={() => onSelectTask(task)}
                                className={cn(
                                    "w-full p-3 rounded-lg text-left transition-all",
                                    "hover:bg-white/10",
                                    selectedTaskId === task.id
                                        ? "bg-indigo-500/20 border border-indigo-500/40"
                                        : "bg-white/5 border border-white/10"
                                )}
                            >
                                <div className="flex items-center gap-2">
                                    <span>{getTypeIcon(task.type)}</span>
                                    <span className="font-medium text-white line-clamp-1">
                                        {task.title}
                                    </span>
                                </div>
                                <div className="flex items-center gap-3 mt-1 text-xs text-muted-foreground">
                                    <span>{task.moduleName}</span>
                                    <span className="text-orange-400">
                                        +{task.xpReward} XP
                                    </span>
                                </div>
                            </button>
                        ))}
                    </div>
                </div>
            )}

            {/* Completed tasks */}
            {completedTasks.length > 0 && (
                <div>
                    <h4 className="text-sm font-medium text-muted-foreground mb-2">
                        Completed ({completedTasks.length})
                    </h4>
                    <div className="space-y-2 opacity-60">
                        {completedTasks.slice(0, 3).map((task) => (
                            <div
                                key={task.id}
                                className="p-3 rounded-lg bg-white/5 border border-white/10"
                            >
                                <div className="flex items-center gap-2">
                                    <CheckCircle2 className="w-4 h-4 text-green-400" />
                                    <span className="text-sm text-white/70 line-clamp-1">
                                        {task.title}
                                    </span>
                                </div>
                            </div>
                        ))}
                        {completedTasks.length > 3 && (
                            <p className="text-xs text-muted-foreground text-center">
                                +{completedTasks.length - 3} more completed
                            </p>
                        )}
                    </div>
                </div>
            )}

            {/* Empty state */}
            {tasks.length === 0 && (
                <div className="text-center py-8 text-muted-foreground">
                    <FileText className="w-8 h-8 mx-auto mb-2 opacity-50" />
                    <p>No tasks available</p>
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default TaskPanel
