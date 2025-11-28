"use client"

/**
 * ============================================================================
 * OUTCOME CHECKLIST - Interactive Checklist for Labs & Projects
 * ============================================================================
 *
 * Features:
 * - Checkable outcome items
 * - Progress tracking with percentage
 * - Local storage state persistence
 * - Visual feedback on completion
 * - Animated check transitions
 *
 * @phase C.3 - Labs & Projects Display
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    CheckCircle2,
    Circle,
    Trophy,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface OutcomeItem {
    id: string
    label: string
    description?: string
}

interface OutcomeChecklistProps {
    /** Unique identifier for persistence */
    storageKey: string
    /** List of outcomes to display */
    outcomes: OutcomeItem[]
    /** Track color for styling */
    trackColor?: string
    /** Title override */
    title?: string
    /** Callback when all items are completed */
    onAllComplete?: () => void
    /** Callback when completion state changes */
    onChange?: (completed: string[]) => void
    /** Additional class names */
    className?: string
}

/* ============================================================================
   LOCAL STORAGE HELPERS
   ============================================================================ */

function getStoredState(key: string): string[] {
    if (typeof window === "undefined") return []
    try {
        const stored = localStorage.getItem(`outcome-checklist-${key}`)
        return stored ? JSON.parse(stored) : []
    } catch {
        return []
    }
}

function setStoredState(key: string, completed: string[]): void {
    if (typeof window === "undefined") return
    try {
        localStorage.setItem(`outcome-checklist-${key}`, JSON.stringify(completed))
    } catch {
        // Storage quota exceeded or other error
    }
}

/* ============================================================================
   PROGRESS RING COMPONENT
   ============================================================================ */

interface ProgressRingProps {
    progress: number
    size?: number
    strokeWidth?: number
    trackColor?: string
}

function ProgressRing({
    progress,
    size = 48,
    strokeWidth = 4,
    trackColor = "#6366f1",
}: ProgressRingProps) {
    const radius = (size - strokeWidth) / 2
    const circumference = radius * 2 * Math.PI
    const offset = circumference - (progress / 100) * circumference

    return (
        <div className="relative" style={{ width: size, height: size }}>
            <svg
                className="transform -rotate-90"
                width={size}
                height={size}
            >
                {/* Background circle */}
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke="currentColor"
                    strokeWidth={strokeWidth}
                    className="text-neutral-200 dark:text-neutral-700"
                />
                {/* Progress circle */}
                <circle
                    cx={size / 2}
                    cy={size / 2}
                    r={radius}
                    fill="none"
                    stroke={trackColor}
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    strokeDasharray={circumference}
                    strokeDashoffset={offset}
                    className="transition-all duration-500 ease-out"
                />
            </svg>
            {/* Percentage text */}
            <div className="absolute inset-0 flex items-center justify-center">
                <span
                    className="text-xs font-bold"
                    style={{ color: progress === 100 ? trackColor : undefined }}
                >
                    {Math.round(progress)}%
                </span>
            </div>
        </div>
    )
}

/* ============================================================================
   CHECKLIST ITEM COMPONENT
   ============================================================================ */

interface ChecklistItemProps {
    item: OutcomeItem
    isChecked: boolean
    onToggle: () => void
    trackColor: string
}

function ChecklistItem({
    item,
    isChecked,
    onToggle,
    trackColor,
}: ChecklistItemProps) {
    return (
        <motion.div
            initial={false}
            animate={{
                backgroundColor: isChecked ? `${trackColor}08` : "transparent",
            }}
            className={cn(
                "flex items-start gap-3 p-3 rounded-lg",
                "border border-transparent transition-all duration-200",
                "cursor-pointer select-none",
                "hover:bg-neutral-50 dark:hover:bg-neutral-800/50",
                isChecked && "border-opacity-20"
            )}
            style={{
                borderColor: isChecked ? trackColor : "transparent",
            }}
            onClick={onToggle}
            role="checkbox"
            aria-checked={isChecked}
            tabIndex={0}
            onKeyDown={(e) => {
                if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault()
                    onToggle()
                }
            }}
        >
            {/* Checkbox */}
            <div className="flex-shrink-0 mt-0.5">
                <AnimatePresence mode="wait">
                    {isChecked ? (
                        <motion.div
                            key="checked"
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.8, opacity: 0 }}
                            transition={{ duration: 0.15 }}
                        >
                            <CheckCircle2
                                className="h-5 w-5"
                                style={{ color: trackColor }}
                            />
                        </motion.div>
                    ) : (
                        <motion.div
                            key="unchecked"
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0.8, opacity: 0 }}
                            transition={{ duration: 0.15 }}
                        >
                            <Circle className="h-5 w-5 text-neutral-400 dark:text-neutral-600" />
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>

            {/* Label & Description */}
            <div className="flex-1 min-w-0">
                <p
                    className={cn(
                        "text-sm font-medium transition-colors duration-200",
                        isChecked
                            ? "text-neutral-600 dark:text-neutral-400 line-through"
                            : "text-neutral-900 dark:text-white"
                    )}
                >
                    {item.label}
                </p>
                {item.description && (
                    <p
                        className={cn(
                            "text-xs mt-0.5 transition-colors duration-200",
                            isChecked
                                ? "text-neutral-400 dark:text-neutral-600"
                                : "text-neutral-500 dark:text-neutral-400"
                        )}
                    >
                        {item.description}
                    </p>
                )}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   COMPLETION CELEBRATION
   ============================================================================ */

function CompletionCelebration({ trackColor }: { trackColor: string }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "flex items-center gap-3 p-4 rounded-lg",
                "bg-gradient-to-r from-amber-50 to-green-50",
                "dark:from-amber-950/20 dark:to-green-950/20",
                "border border-green-200 dark:border-green-800/50"
            )}
        >
            <div
                className="p-2 rounded-full"
                style={{ backgroundColor: `${trackColor}20` }}
            >
                <Trophy className="h-5 w-5 text-amber-500" />
            </div>
            <div>
                <p className="text-sm font-medium text-green-700 dark:text-green-400">
                    All outcomes completed!
                </p>
                <p className="text-xs text-green-600 dark:text-green-500">
                    Great job finishing all the expected outcomes
                </p>
            </div>
            <Sparkles className="h-5 w-5 text-amber-400 ml-auto" />
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function OutcomeChecklist({
    storageKey,
    outcomes,
    trackColor = "#6366f1",
    title = "Expected Outcomes",
    onAllComplete,
    onChange,
    className,
}: OutcomeChecklistProps) {
    // State
    const [completed, setCompleted] = React.useState<string[]>([])
    const [isInitialized, setIsInitialized] = React.useState(false)

    // Load saved state on mount
    React.useEffect(() => {
        const stored = getStoredState(storageKey)
        setCompleted(stored)
        setIsInitialized(true)
    }, [storageKey])

    // Calculate progress
    const progress = outcomes.length > 0
        ? (completed.length / outcomes.length) * 100
        : 0
    const isAllComplete = completed.length === outcomes.length && outcomes.length > 0

    // Handle toggle
    const handleToggle = (id: string) => {
        setCompleted((prev) => {
            const newCompleted = prev.includes(id)
                ? prev.filter((i) => i !== id)
                : [...prev, id]

            // Persist to storage
            setStoredState(storageKey, newCompleted)

            // Callbacks
            onChange?.(newCompleted)
            if (newCompleted.length === outcomes.length && outcomes.length > 0) {
                onAllComplete?.()
            }

            return newCompleted
        })
    }

    // Don't render until initialized (prevents hydration mismatch)
    if (!isInitialized) {
        return (
            <div className={cn("rounded-xl border border-neutral-200 dark:border-neutral-800", className)}>
                <div className="p-4">
                    <div className="h-6 w-40 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                </div>
                <div className="px-4 pb-4 space-y-2">
                    {outcomes.map((_, i) => (
                        <div key={i} className="h-12 bg-neutral-100 dark:bg-neutral-900 rounded-lg animate-pulse" />
                    ))}
                </div>
            </div>
        )
    }

    return (
        <div
            className={cn(
                "rounded-xl border border-neutral-200 dark:border-neutral-800",
                "bg-white dark:bg-neutral-900",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-neutral-200 dark:border-neutral-800">
                <div>
                    <h3 className="font-semibold text-neutral-900 dark:text-white">
                        {title}
                    </h3>
                    <p className="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
                        {completed.length} of {outcomes.length} completed
                    </p>
                </div>
                <ProgressRing
                    progress={progress}
                    trackColor={trackColor}
                />
            </div>

            {/* Checklist items */}
            <div className="p-2 space-y-1">
                {outcomes.map((outcome) => (
                    <ChecklistItem
                        key={outcome.id}
                        item={outcome}
                        isChecked={completed.includes(outcome.id)}
                        onToggle={() => handleToggle(outcome.id)}
                        trackColor={trackColor}
                    />
                ))}
            </div>

            {/* Completion celebration */}
            <AnimatePresence>
                {isAllComplete && (
                    <div className="p-4 pt-2">
                        <CompletionCelebration trackColor={trackColor} />
                    </div>
                )}
            </AnimatePresence>
        </div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default OutcomeChecklist
