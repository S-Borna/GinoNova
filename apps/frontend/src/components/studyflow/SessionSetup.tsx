"use client"

/**
 * ============================================================================
 * SESSION SETUP COMPONENT - Pre-Session Configuration
 * ============================================================================
 * 
 * Features:
 * - Mode selection: Pomodoro (25/5), Deep Focus (50/10), Custom
 * - Task selection: Current module's next task or browse
 * - Goal setting: Tasks or minutes
 * - Big "Start Session" button
 * 
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { GlassCard, GlassCardHeader, GlassCardTitle, GlassCardContent } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import { 
    Clock, 
    Focus, 
    Settings2, 
    Target, 
    BookOpen,
    CheckCircle2,
    Play,
    Zap,
    Timer as TimerIcon
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type SessionMode = "pomodoro" | "deep-focus" | "custom"

export interface SessionConfig {
    mode: SessionMode
    workMinutes: number
    breakMinutes: number
    taskId?: string
    taskTitle?: string
    moduleTitle?: string
    goalType: "tasks" | "minutes" | "none"
    goalValue?: number
}

export interface TaskOption {
    id: string
    title: string
    moduleId: string
    moduleTitle: string
    isRecommended?: boolean
}

export interface SessionSetupProps {
    onStartSession: (config: SessionConfig) => void
    availableTasks?: TaskOption[]
    className?: string
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const SESSION_MODES = {
    pomodoro: {
        label: "Pomodoro",
        description: "25 min work / 5 min break",
        workMinutes: 25,
        breakMinutes: 5,
        icon: Clock,
        color: "primary" as const,
    },
    "deep-focus": {
        label: "Deep Focus",
        description: "50 min work / 10 min break",
        workMinutes: 50,
        breakMinutes: 10,
        icon: Focus,
        color: "info" as const,
    },
    custom: {
        label: "Custom",
        description: "Set your own times",
        workMinutes: 30,
        breakMinutes: 5,
        icon: Settings2,
        color: "warning" as const,
    },
}

const GOAL_OPTIONS = [
    { type: "none" as const, label: "No goal", description: "Just focus", icon: Zap },
    { type: "tasks" as const, label: "Complete tasks", description: "e.g. 3 tasks", icon: Target },
    { type: "minutes" as const, label: "Study time", description: "e.g. 60 minutes", icon: TimerIcon },
]

/* ============================================================================
   MODE CARD
   ============================================================================ */

interface ModeCardProps {
    mode: SessionMode
    selected: boolean
    onSelect: () => void
}

function ModeCard({ mode, selected, onSelect }: ModeCardProps) {
    const config = SESSION_MODES[mode]
    const Icon = config.icon

    return (
        <GlassCard
            variant={selected ? "primary" : "default"}
            interactive
            padding="md"
            className={cn(
                "cursor-pointer transition-all duration-200",
                selected && "ring-2 ring-primary-500 ring-offset-2"
            )}
            onClick={onSelect}
        >
            <div className="flex items-start gap-4">
                <div className={cn(
                    "p-3 rounded-xl",
                    selected 
                        ? "bg-primary-500 text-white" 
                        : "bg-neutral-100 text-neutral-600 dark:bg-neutral-800 dark:text-neutral-300"
                )}>
                    <Icon className="h-6 w-6" />
                </div>
                <div className="flex-1">
                    <h3 className="font-semibold text-neutral-900 dark:text-white">
                        {config.label}
                    </h3>
                    <p className="text-sm text-neutral-500 dark:text-neutral-400">
                        {config.description}
                    </p>
                </div>
                {selected && (
                    <CheckCircle2 className="h-5 w-5 text-primary-500 flex-shrink-0" />
                )}
            </div>
        </GlassCard>
    )
}

/* ============================================================================
   TASK SELECTOR
   ============================================================================ */

interface TaskSelectorProps {
    tasks: TaskOption[]
    selectedTaskId?: string
    onSelectTask: (task: TaskOption | undefined) => void
}

function TaskSelector({ tasks, selectedTaskId, onSelectTask }: TaskSelectorProps) {
    const recommendedTask = tasks.find(t => t.isRecommended)
    const selectedTask = tasks.find(t => t.id === selectedTaskId)

    return (
        <div className="space-y-3">
            {/* Recommended Task Card */}
            {recommendedTask && (
                <GlassCard
                    variant={selectedTaskId === recommendedTask.id ? "success" : "light"}
                    interactive
                    padding="sm"
                    className={cn(
                        "cursor-pointer",
                        selectedTaskId === recommendedTask.id && "ring-2 ring-emerald-500 ring-offset-2"
                    )}
                    onClick={() => onSelectTask(recommendedTask)}
                >
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-emerald-100 text-emerald-600 rounded-lg dark:bg-emerald-900/30 dark:text-emerald-400">
                            <Zap className="h-4 w-4" />
                        </div>
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2">
                                <span className="text-xs font-medium text-emerald-600 dark:text-emerald-400">
                                    RECOMMENDED
                                </span>
                            </div>
                            <p className="font-medium text-neutral-900 dark:text-white truncate">
                                {recommendedTask.title}
                            </p>
                            <p className="text-xs text-neutral-500 dark:text-neutral-400">
                                {recommendedTask.moduleTitle}
                            </p>
                        </div>
                        {selectedTaskId === recommendedTask.id && (
                            <CheckCircle2 className="h-5 w-5 text-emerald-500 flex-shrink-0" />
                        )}
                    </div>
                </GlassCard>
            )}

            {/* Other Tasks */}
            <div className="max-h-48 overflow-y-auto space-y-2">
                {tasks.filter(t => !t.isRecommended).slice(0, 5).map(task => (
                    <GlassCard
                        key={task.id}
                        variant={selectedTaskId === task.id ? "primary" : "light"}
                        interactive
                        padding="sm"
                        className={cn(
                            "cursor-pointer",
                            selectedTaskId === task.id && "ring-2 ring-primary-500 ring-offset-2"
                        )}
                        onClick={() => onSelectTask(task)}
                    >
                        <div className="flex items-center gap-3">
                            <div className="p-2 bg-neutral-100 text-neutral-600 rounded-lg dark:bg-neutral-800 dark:text-neutral-300">
                                <BookOpen className="h-4 w-4" />
                            </div>
                            <div className="flex-1 min-w-0">
                                <p className="font-medium text-neutral-900 dark:text-white truncate">
                                    {task.title}
                                </p>
                                <p className="text-xs text-neutral-500 dark:text-neutral-400">
                                    {task.moduleTitle}
                                </p>
                            </div>
                            {selectedTaskId === task.id && (
                                <CheckCircle2 className="h-5 w-5 text-primary-500 flex-shrink-0" />
                            )}
                        </div>
                    </GlassCard>
                ))}
            </div>

            {/* No task option */}
            <button
                type="button"
                onClick={() => onSelectTask(undefined)}
                className={cn(
                    "w-full py-2 px-4 text-sm text-neutral-500 hover:text-neutral-700",
                    "dark:text-neutral-400 dark:hover:text-neutral-200",
                    "transition-colors rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800",
                    !selectedTaskId && "text-primary-600 dark:text-primary-400"
                )}
            >
                {selectedTaskId ? "Clear selection" : "✓ No specific task selected"}
            </button>
        </div>
    )
}

/* ============================================================================
   GOAL SELECTOR
   ============================================================================ */

interface GoalSelectorProps {
    goalType: "tasks" | "minutes" | "none"
    goalValue?: number
    onChangeGoalType: (type: "tasks" | "minutes" | "none") => void
    onChangeGoalValue: (value: number) => void
}

function GoalSelector({
    goalType,
    goalValue,
    onChangeGoalType,
    onChangeGoalValue,
}: GoalSelectorProps) {
    return (
        <div className="space-y-3">
            {/* Goal Type Tabs */}
            <div className="flex gap-2 p-1 bg-neutral-100 dark:bg-neutral-800 rounded-lg">
                {GOAL_OPTIONS.map(option => {
                    const Icon = option.icon
                    const isSelected = goalType === option.type
                    return (
                        <button
                            key={option.type}
                            type="button"
                            onClick={() => onChangeGoalType(option.type)}
                            className={cn(
                                "flex-1 flex items-center justify-center gap-2 py-2 px-3 rounded-md text-sm font-medium transition-all",
                                isSelected
                                    ? "bg-white dark:bg-neutral-700 text-neutral-900 dark:text-white shadow-sm"
                                    : "text-neutral-500 hover:text-neutral-700 dark:text-neutral-400 dark:hover:text-neutral-200"
                            )}
                        >
                            <Icon className="h-4 w-4" />
                            <span className="hidden sm:inline">{option.label}</span>
                        </button>
                    )
                })}
            </div>

            {/* Goal Value Input */}
            {goalType !== "none" && (
                <div className="flex items-center gap-3">
                    <span className="text-sm text-neutral-600 dark:text-neutral-400">
                        I want to {goalType === "tasks" ? "complete" : "study for"}
                    </span>
                    <input
                        type="number"
                        min={1}
                        max={goalType === "tasks" ? 10 : 240}
                        value={goalValue || (goalType === "tasks" ? 3 : 60)}
                        onChange={(e) => onChangeGoalValue(parseInt(e.target.value) || 1)}
                        className={cn(
                            "w-16 px-2 py-1 text-center font-semibold rounded-lg",
                            "border border-neutral-200 dark:border-neutral-700",
                            "bg-white dark:bg-neutral-800",
                            "text-neutral-900 dark:text-white",
                            "focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                        )}
                    />
                    <span className="text-sm text-neutral-600 dark:text-neutral-400">
                        {goalType === "tasks" ? "tasks" : "minutes"}
                    </span>
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   CUSTOM TIME INPUT
   ============================================================================ */

interface CustomTimeInputProps {
    workMinutes: number
    breakMinutes: number
    onChangeWork: (minutes: number) => void
    onChangeBreak: (minutes: number) => void
}

function CustomTimeInput({
    workMinutes,
    breakMinutes,
    onChangeWork,
    onChangeBreak,
}: CustomTimeInputProps) {
    return (
        <div className="flex items-center gap-6">
            {/* Work Time */}
            <div className="flex items-center gap-2">
                <label className="text-sm text-neutral-600 dark:text-neutral-400">
                    Work:
                </label>
                <input
                    type="number"
                    min={5}
                    max={120}
                    value={workMinutes}
                    onChange={(e) => onChangeWork(parseInt(e.target.value) || 25)}
                    className={cn(
                        "w-16 px-2 py-1 text-center font-semibold rounded-lg",
                        "border border-neutral-200 dark:border-neutral-700",
                        "bg-white dark:bg-neutral-800",
                        "text-neutral-900 dark:text-white",
                        "focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    )}
                />
                <span className="text-sm text-neutral-500">min</span>
            </div>

            {/* Break Time */}
            <div className="flex items-center gap-2">
                <label className="text-sm text-neutral-600 dark:text-neutral-400">
                    Break:
                </label>
                <input
                    type="number"
                    min={1}
                    max={30}
                    value={breakMinutes}
                    onChange={(e) => onChangeBreak(parseInt(e.target.value) || 5)}
                    className={cn(
                        "w-16 px-2 py-1 text-center font-semibold rounded-lg",
                        "border border-neutral-200 dark:border-neutral-700",
                        "bg-white dark:bg-neutral-800",
                        "text-neutral-900 dark:text-white",
                        "focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                    )}
                />
                <span className="text-sm text-neutral-500">min</span>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN SESSION SETUP COMPONENT
   ============================================================================ */

export function SessionSetup({
    onStartSession,
    availableTasks = [],
    className,
}: SessionSetupProps) {
    // State
    const [selectedMode, setSelectedMode] = React.useState<SessionMode>("pomodoro")
    const [customWorkMinutes, setCustomWorkMinutes] = React.useState(30)
    const [customBreakMinutes, setCustomBreakMinutes] = React.useState(5)
    const [selectedTask, setSelectedTask] = React.useState<TaskOption | undefined>(
        availableTasks.find(t => t.isRecommended)
    )
    const [goalType, setGoalType] = React.useState<"tasks" | "minutes" | "none">("none")
    const [goalValue, setGoalValue] = React.useState<number | undefined>(undefined)

    // Calculate effective times
    const modeConfig = SESSION_MODES[selectedMode]
    const workMinutes = selectedMode === "custom" ? customWorkMinutes : modeConfig.workMinutes
    const breakMinutes = selectedMode === "custom" ? customBreakMinutes : modeConfig.breakMinutes

    // Handle start
    const handleStart = () => {
        const config: SessionConfig = {
            mode: selectedMode,
            workMinutes,
            breakMinutes,
            taskId: selectedTask?.id,
            taskTitle: selectedTask?.title,
            moduleTitle: selectedTask?.moduleTitle,
            goalType,
            goalValue: goalType !== "none" ? goalValue : undefined,
        }
        onStartSession(config)
    }

    // Mock tasks for demo
    const tasksToShow = availableTasks.length > 0 ? availableTasks : [
        { id: "1", title: "Install Docker", moduleId: "m9", moduleTitle: "Module 09 · Containers", isRecommended: true },
        { id: "2", title: "Write Dockerfile", moduleId: "m9", moduleTitle: "Module 09 · Containers" },
        { id: "3", title: "Docker Compose Basics", moduleId: "m9", moduleTitle: "Module 09 · Containers" },
    ]

    return (
        <div className={cn("space-y-8", className)}>
            {/* Header */}
            <div className="text-center">
                <h1 className="text-3xl font-bold text-neutral-900 dark:text-white">
                    Ready to Focus?
                </h1>
                <p className="mt-2 text-neutral-500 dark:text-neutral-400">
                    Set up your study session and dive in
                </p>
            </div>

            {/* Mode Selection */}
            <GlassCard padding="lg">
                <GlassCardHeader>
                    <GlassCardTitle className="flex items-center gap-2">
                        <Clock className="h-5 w-5 text-primary-500" />
                        Choose Your Mode
                    </GlassCardTitle>
                </GlassCardHeader>
                <GlassCardContent>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        {(Object.keys(SESSION_MODES) as SessionMode[]).map(mode => (
                            <ModeCard
                                key={mode}
                                mode={mode}
                                selected={selectedMode === mode}
                                onSelect={() => setSelectedMode(mode)}
                            />
                        ))}
                    </div>

                    {/* Custom Time Inputs */}
                    {selectedMode === "custom" && (
                        <div className="mt-6 pt-6 border-t border-neutral-200 dark:border-neutral-700">
                            <CustomTimeInput
                                workMinutes={customWorkMinutes}
                                breakMinutes={customBreakMinutes}
                                onChangeWork={setCustomWorkMinutes}
                                onChangeBreak={setCustomBreakMinutes}
                            />
                        </div>
                    )}
                </GlassCardContent>
            </GlassCard>

            {/* Task Selection */}
            <GlassCard padding="lg">
                <GlassCardHeader>
                    <GlassCardTitle className="flex items-center gap-2">
                        <BookOpen className="h-5 w-5 text-primary-500" />
                        Select a Task (Optional)
                    </GlassCardTitle>
                </GlassCardHeader>
                <GlassCardContent>
                    <TaskSelector
                        tasks={tasksToShow}
                        selectedTaskId={selectedTask?.id}
                        onSelectTask={setSelectedTask}
                    />
                </GlassCardContent>
            </GlassCard>

            {/* Goal Setting */}
            <GlassCard padding="lg">
                <GlassCardHeader>
                    <GlassCardTitle className="flex items-center gap-2">
                        <Target className="h-5 w-5 text-primary-500" />
                        Set a Goal (Optional)
                    </GlassCardTitle>
                </GlassCardHeader>
                <GlassCardContent>
                    <GoalSelector
                        goalType={goalType}
                        goalValue={goalValue}
                        onChangeGoalType={setGoalType}
                        onChangeGoalValue={setGoalValue}
                    />
                </GlassCardContent>
            </GlassCard>

            {/* Session Summary & Start Button */}
            <GlassCard variant="primary" padding="lg" glow="primary">
                <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
                    <div className="text-center sm:text-left">
                        <p className="text-sm text-neutral-600 dark:text-neutral-400">
                            Your Session
                        </p>
                        <p className="text-xl font-bold text-neutral-900 dark:text-white">
                            {workMinutes} min focus + {breakMinutes} min break
                        </p>
                        {selectedTask && (
                            <p className="text-sm text-primary-600 dark:text-primary-400 mt-1">
                                Working on: {selectedTask.title}
                            </p>
                        )}
                    </div>
                    <Button
                        variant="gradient"
                        size="xl"
                        onClick={handleStart}
                        rightIcon={<Play className="h-5 w-5" />}
                        className="min-w-[200px]"
                    >
                        Start Session
                    </Button>
                </div>
            </GlassCard>
        </div>
    )
}

export default SessionSetup
