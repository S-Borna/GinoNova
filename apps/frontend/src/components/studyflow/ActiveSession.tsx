"use client"

/**
 * ============================================================================
 * ACTIVE SESSION COMPONENT - Focus Mode Interface
 * ============================================================================
 * 
 * Features:
 * - Large circular timer (Apple Watch style)
 * - Session phase indicator (Focus / Break)
 * - Current task card with "Mark Complete" button
 * - Control buttons (Pause/Resume, Skip break, End session)
 * - Stats sidebar (desktop) / collapsible (mobile)
 * 
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { Timer, MiniTimer } from "./Timer"
import { StreakDisplay } from "./StreakDisplay"
import {
    Pause,
    Play,
    SkipForward,
    Square,
    CheckCircle2,
    BookOpen,
    Clock,
    Zap,
    Target,
    ChevronUp,
    ChevronDown,
    AlertTriangle,
} from "lucide-react"
import type { SessionConfig } from "./SessionSetup"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface ActiveSessionProps {
    config: SessionConfig
    onEndSession: (completed: boolean) => void
    onCompleteTask: () => void
    className?: string
}

interface SessionStats {
    todayTotalFocus: number // minutes
    currentStreak: number // days
    tasksCompletedSession: number
    xpEarnedSession: number
}

/* ============================================================================
   END SESSION DIALOG
   ============================================================================ */

interface EndSessionDialogProps {
    isOpen: boolean
    onConfirm: () => void
    onCancel: () => void
    timeRemaining: number
}

function EndSessionDialog({ isOpen, onConfirm, onCancel, timeRemaining }: EndSessionDialogProps) {
    if (!isOpen) return null

    const minutesLeft = Math.ceil(timeRemaining / 60)

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
            <GlassCard variant="solid" padding="lg" radius="xl" className="max-w-md w-full animate-scale-in">
                <div className="text-center space-y-4">
                    <div className="mx-auto w-14 h-14 rounded-full bg-amber-100 dark:bg-amber-900/30 flex items-center justify-center">
                        <AlertTriangle className="h-7 w-7 text-amber-600 dark:text-amber-400" />
                    </div>
                    <h3 className="text-xl font-bold text-neutral-900 dark:text-white">
                        End Session Early?
                    </h3>
                    <p className="text-neutral-600 dark:text-neutral-400">
                        You still have {minutesLeft} minute{minutesLeft !== 1 ? "s" : ""} left.
                        Are you sure you want to end this session?
                    </p>
                    <div className="flex gap-3 pt-2">
                        <Button
                            variant="outline"
                            className="flex-1"
                            onClick={onCancel}
                        >
                            Keep Focusing
                        </Button>
                        <Button
                            variant="destructive"
                            className="flex-1"
                            onClick={onConfirm}
                        >
                            End Session
                        </Button>
                    </div>
                </div>
            </GlassCard>
        </div>
    )
}

/* ============================================================================
   STATS PANEL
   ============================================================================ */

interface StatsPanelProps {
    stats: SessionStats
    isExpanded: boolean
    onToggle: () => void
    className?: string
}

function StatsPanel({ stats, isExpanded, onToggle, className }: StatsPanelProps) {
    return (
        <div className={cn("lg:w-80", className)}>
            {/* Mobile Toggle */}
            <button
                type="button"
                onClick={onToggle}
                className="lg:hidden w-full flex items-center justify-between py-2 px-4 text-neutral-600 dark:text-neutral-400"
            >
                <span className="text-sm font-medium">Session Stats</span>
                {isExpanded ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
            </button>

            {/* Stats Content */}
            <div className={cn(
                "space-y-4 overflow-hidden transition-all duration-300",
                isExpanded ? "max-h-96 opacity-100" : "max-h-0 opacity-0 lg:max-h-96 lg:opacity-100"
            )}>
                {/* Streak */}
                <GlassCard padding="md">
                    <StreakDisplay streak={stats.currentStreak} compact />
                </GlassCard>

                {/* Today's Stats */}
                <GlassCard padding="md">
                    <h4 className="text-sm font-medium text-neutral-500 dark:text-neutral-400 mb-3">
                        Today&apos;s Progress
                    </h4>
                    <div className="space-y-3">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2 text-neutral-600 dark:text-neutral-300">
                                <Clock className="h-4 w-4 text-primary-500" />
                                <span className="text-sm">Total Focus</span>
                            </div>
                            <span className="font-semibold text-neutral-900 dark:text-white">
                                {stats.todayTotalFocus} min
                            </span>
                        </div>
                    </div>
                </GlassCard>

                {/* Session Stats */}
                <GlassCard padding="md">
                    <h4 className="text-sm font-medium text-neutral-500 dark:text-neutral-400 mb-3">
                        This Session
                    </h4>
                    <div className="space-y-3">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2 text-neutral-600 dark:text-neutral-300">
                                <Target className="h-4 w-4 text-emerald-500" />
                                <span className="text-sm">Tasks Done</span>
                            </div>
                            <span className="font-semibold text-neutral-900 dark:text-white">
                                {stats.tasksCompletedSession}
                            </span>
                        </div>
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2 text-neutral-600 dark:text-neutral-300">
                                <Zap className="h-4 w-4 text-amber-500" />
                                <span className="text-sm">XP Earned</span>
                            </div>
                            <span className="font-semibold text-amber-600 dark:text-amber-400">
                                +{stats.xpEarnedSession} XP
                            </span>
                        </div>
                    </div>
                </GlassCard>
            </div>
        </div>
    )
}

/* ============================================================================
   TASK CARD
   ============================================================================ */

interface TaskCardProps {
    taskTitle?: string
    moduleTitle?: string
    isCompleted: boolean
    onComplete: () => void
}

function TaskCard({ taskTitle, moduleTitle, isCompleted, onComplete }: TaskCardProps) {
    if (!taskTitle) return null

    return (
        <GlassCard
            variant={isCompleted ? "success" : "default"}
            padding="md"
            className="mt-8 max-w-md mx-auto"
        >
            <div className="flex items-center gap-4">
                <div className={cn(
                    "p-3 rounded-xl",
                    isCompleted
                        ? "bg-emerald-100 text-emerald-600 dark:bg-emerald-900/30 dark:text-emerald-400"
                        : "bg-neutral-100 text-neutral-600 dark:bg-neutral-800 dark:text-neutral-300"
                )}>
                    {isCompleted ? (
                        <CheckCircle2 className="h-6 w-6" />
                    ) : (
                        <BookOpen className="h-6 w-6" />
                    )}
                </div>
                <div className="flex-1 min-w-0">
                    <p className="text-xs text-neutral-500 dark:text-neutral-400 uppercase tracking-wider">
                        Current Task
                    </p>
                    <p className={cn(
                        "font-semibold text-neutral-900 dark:text-white truncate",
                        isCompleted && "line-through opacity-60"
                    )}>
                        {taskTitle}
                    </p>
                    {moduleTitle && (
                        <p className="text-sm text-neutral-500 dark:text-neutral-400">
                            {moduleTitle}
                        </p>
                    )}
                </div>
                {!isCompleted && (
                    <Button
                        variant="gradient"
                        size="sm"
                        onClick={onComplete}
                    >
                        Complete
                    </Button>
                )}
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   MAIN ACTIVE SESSION COMPONENT
   ============================================================================ */

export function ActiveSession({
    config,
    onEndSession,
    onCompleteTask,
    className,
}: ActiveSessionProps) {
    // Timer state
    const [isPaused, setIsPaused] = React.useState(false)
    const [isBreak, setIsBreak] = React.useState(false)
    const [remainingSeconds, setRemainingSeconds] = React.useState(config.workMinutes * 60)
    const [taskCompleted, setTaskCompleted] = React.useState(false)
    
    // UI state
    const [showEndDialog, setShowEndDialog] = React.useState(false)
    const [statsExpanded, setStatsExpanded] = React.useState(false)
    
    // Stats (mock data for now)
    const [stats, setStats] = React.useState<SessionStats>({
        todayTotalFocus: 45,
        currentStreak: 7,
        tasksCompletedSession: 0,
        xpEarnedSession: 0,
    })

    // Current total seconds for progress calculation
    const totalSeconds = isBreak ? config.breakMinutes * 60 : config.workMinutes * 60

    // Timer tick effect
    React.useEffect(() => {
        if (isPaused) return

        const interval = setInterval(() => {
            setRemainingSeconds(prev => {
                if (prev <= 1) {
                    // Timer complete
                    if (isBreak) {
                        // Break over, start work
                        setIsBreak(false)
                        return config.workMinutes * 60
                    } else {
                        // Work over, start break
                        setIsBreak(true)
                        return config.breakMinutes * 60
                    }
                }
                return prev - 1
            })
        }, 1000)

        return () => clearInterval(interval)
    }, [isPaused, isBreak, config.workMinutes, config.breakMinutes])

    // Handle task completion
    const handleCompleteTask = () => {
        setTaskCompleted(true)
        setStats(prev => ({
            ...prev,
            tasksCompletedSession: prev.tasksCompletedSession + 1,
            xpEarnedSession: prev.xpEarnedSession + 50,
        }))
        onCompleteTask()
    }

    // Handle skip break
    const handleSkipBreak = () => {
        setIsBreak(false)
        setRemainingSeconds(config.workMinutes * 60)
    }

    // Handle end session
    const handleEndSession = () => {
        setShowEndDialog(false)
        onEndSession(false)
    }

    return (
        <div className={cn("min-h-[80vh] flex flex-col lg:flex-row gap-8", className)}>
            {/* Main Timer Area */}
            <div className="flex-1 flex flex-col items-center justify-center">
                {/* Phase Label */}
                <div className={cn(
                    "mb-6 px-4 py-2 rounded-full text-sm font-semibold uppercase tracking-wider",
                    isBreak
                        ? "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400"
                        : "bg-primary-100 text-primary-700 dark:bg-primary-900/30 dark:text-primary-400"
                )}>
                    {isBreak ? "☕ Break Time" : "🎯 Focus Time"}
                </div>

                {/* Timer */}
                <Timer
                    totalSeconds={totalSeconds}
                    remainingSeconds={remainingSeconds}
                    isBreak={isBreak}
                    size={320}
                />

                {/* Controls */}
                <div className="mt-8 flex items-center gap-4">
                    {/* Pause/Resume */}
                    <Button
                        variant={isPaused ? "gradient" : "outline"}
                        size="icon-lg"
                        onClick={() => setIsPaused(!isPaused)}
                        className="h-14 w-14 rounded-full"
                    >
                        {isPaused ? (
                            <Play className="h-6 w-6" />
                        ) : (
                            <Pause className="h-6 w-6" />
                        )}
                    </Button>

                    {/* Skip Break (only during break) */}
                    {isBreak && (
                        <Button
                            variant="outline"
                            size="lg"
                            onClick={handleSkipBreak}
                            leftIcon={<SkipForward className="h-4 w-4" />}
                        >
                            Skip Break
                        </Button>
                    )}

                    {/* End Session */}
                    <Button
                        variant="ghost"
                        size="icon-lg"
                        onClick={() => setShowEndDialog(true)}
                        className="h-14 w-14 rounded-full text-neutral-500 hover:text-red-500"
                    >
                        <Square className="h-5 w-5" />
                    </Button>
                </div>

                {/* Current Task */}
                <TaskCard
                    taskTitle={config.taskTitle}
                    moduleTitle={config.moduleTitle}
                    isCompleted={taskCompleted}
                    onComplete={handleCompleteTask}
                />
            </div>

            {/* Stats Sidebar */}
            <StatsPanel
                stats={stats}
                isExpanded={statsExpanded}
                onToggle={() => setStatsExpanded(!statsExpanded)}
            />

            {/* End Session Dialog */}
            <EndSessionDialog
                isOpen={showEndDialog}
                onConfirm={handleEndSession}
                onCancel={() => setShowEndDialog(false)}
                timeRemaining={remainingSeconds}
            />
        </div>
    )
}

export default ActiveSession
