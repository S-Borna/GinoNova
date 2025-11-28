/**
 * ============================================================================
 * COMPLETE BUTTON — Task Completion with XP Animation
 * ============================================================================
 *
 * Button component for marking tasks as complete with optimistic updates,
 * XP animation, and level-up detection.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { useState, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Check, Loader2, CheckCircle2 } from "lucide-react"
import { Button } from "@/components/ui/button"
import { useCompleteTask } from "@/hooks/useProgress"
import { wouldLevelUp, getLevelUpInfo } from "@/lib/progress"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface CompleteButtonProps {
    taskId: string
    moduleId: string
    xpReward?: number
    currentXP?: number
    isCompleted?: boolean
    onComplete?: (result: {
        xpEarned: number
        levelUp?: { oldLevel: number; newLevel: number }
        moduleComplete?: boolean
    }) => void
    onLevelUp?: (oldLevel: number, newLevel: number) => void
    onModuleComplete?: () => void
    variant?: "default" | "inline" | "card"
    size?: "sm" | "default" | "lg"
    className?: string
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function CompleteButton({
    taskId,
    moduleId,
    xpReward = 25,
    currentXP = 0,
    isCompleted = false,
    onComplete,
    onLevelUp,
    onModuleComplete,
    variant = "default",
    size = "default",
    className,
}: CompleteButtonProps) {
    const [showXP, setShowXP] = useState(false)
    const [earnedXP, setEarnedXP] = useState(0)
    const [completed, setCompleted] = useState(isCompleted)

    const { mutate: completeTask, isPending } = useCompleteTask()

    const handleComplete = useCallback(() => {
        if (completed || isPending) return

        // Optimistic update
        setCompleted(true)
        setEarnedXP(xpReward)
        setShowXP(true)

        // Check for level up
        const levelUpInfo = getLevelUpInfo(currentXP, xpReward)

        // Send to backend
        completeTask(taskId, {
            onSuccess: (data) => {
                const result = {
                    xpEarned: data?.xp_earned || xpReward,
                    levelUp: levelUpInfo
                        ? { oldLevel: levelUpInfo.oldLevel, newLevel: levelUpInfo.newLevel }
                        : undefined,
                    moduleComplete: data?.next_task === undefined,
                }

                onComplete?.(result)

                if (levelUpInfo) {
                    onLevelUp?.(levelUpInfo.oldLevel, levelUpInfo.newLevel)
                }

                if (result.moduleComplete) {
                    onModuleComplete?.()
                }
            },
            onError: () => {
                // Rollback on error
                setCompleted(false)
                setShowXP(false)
            },
        })

        // Hide XP animation after delay
        setTimeout(() => setShowXP(false), 2000)
    }, [
        taskId,
        xpReward,
        currentXP,
        completed,
        isPending,
        completeTask,
        onComplete,
        onLevelUp,
        onModuleComplete,
    ])

    // Completed state
    if (completed && !showXP) {
        return (
            <motion.div
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                className={cn(
                    "flex items-center gap-2 text-green-500",
                    variant === "inline" && "text-sm",
                    className
                )}
            >
                <CheckCircle2 className="h-5 w-5" />
                <span className="font-medium">Completed</span>
            </motion.div>
        )
    }

    // Default variant
    if (variant === "default") {
        return (
            <div className="relative">
                <Button
                    onClick={handleComplete}
                    disabled={completed || isPending}
                    size={size}
                    className={cn(
                        "relative overflow-hidden",
                        "bg-gradient-to-r from-green-500 to-emerald-500",
                        "hover:from-green-600 hover:to-emerald-600",
                        "text-white font-semibold",
                        "shadow-lg shadow-green-500/25",
                        "transition-all duration-300",
                        completed && "bg-green-600",
                        className
                    )}
                >
                    {isPending ? (
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    ) : completed ? (
                        <Check className="mr-2 h-4 w-4" />
                    ) : null}
                    {completed ? "Completed!" : "Complete Task"}
                </Button>

                {/* XP Animation */}
                <AnimatePresence>
                    {showXP && (
                        <XPFloatingAnimation xp={earnedXP} />
                    )}
                </AnimatePresence>
            </div>
        )
    }

    // Inline variant (for task lists)
    if (variant === "inline") {
        return (
            <div className="relative">
                <button
                    onClick={handleComplete}
                    disabled={completed || isPending}
                    className={cn(
                        "flex items-center gap-2 px-3 py-1.5 rounded-full",
                        "text-sm font-medium transition-all duration-200",
                        completed
                            ? "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400"
                            : "bg-primary/10 text-primary hover:bg-primary/20",
                        isPending && "opacity-50 cursor-not-allowed",
                        className
                    )}
                >
                    {isPending ? (
                        <Loader2 className="h-4 w-4 animate-spin" />
                    ) : completed ? (
                        <Check className="h-4 w-4" />
                    ) : (
                        <div className="h-4 w-4 rounded-full border-2 border-current" />
                    )}
                    <span>{completed ? "Done" : "Mark Complete"}</span>
                </button>

                <AnimatePresence>
                    {showXP && (
                        <XPFloatingAnimation xp={earnedXP} position="right" />
                    )}
                </AnimatePresence>
            </div>
        )
    }

    // Card variant (for end of task content)
    if (variant === "card") {
        return (
            <motion.div
                className={cn(
                    "relative p-6 rounded-xl",
                    "bg-gradient-to-br from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20",
                    className
                )}
                whileHover={{ scale: 1.02 }}
                transition={{ duration: 0.2 }}
            >
                <div className="flex items-center justify-between">
                    <div>
                        <h3 className="font-semibold text-lg">Ready to continue?</h3>
                        <p className="text-sm text-muted-foreground mt-1">
                            Mark this task as complete to earn{" "}
                            <span className="text-orange-500 font-bold">+{xpReward} XP</span>
                        </p>
                    </div>

                    <Button
                        onClick={handleComplete}
                        disabled={completed || isPending}
                        size="lg"
                        className={cn(
                            "bg-gradient-to-r from-green-500 to-emerald-500",
                            "hover:from-green-600 hover:to-emerald-600",
                            "text-white font-semibold px-8",
                            "shadow-lg shadow-green-500/25"
                        )}
                    >
                        {isPending ? (
                            <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                        ) : completed ? (
                            <Check className="mr-2 h-5 w-5" />
                        ) : null}
                        {completed ? "Completed!" : "Complete & Continue"}
                    </Button>
                </div>

                <AnimatePresence>
                    {showXP && (
                        <XPFloatingAnimation xp={earnedXP} position="center" size="lg" />
                    )}
                </AnimatePresence>
            </motion.div>
        )
    }

    return null
}

/* ============================================================================
   XP FLOATING ANIMATION (INLINE)
   ============================================================================ */

interface XPFloatingAnimationProps {
    xp: number
    position?: "top" | "right" | "center"
    size?: "sm" | "default" | "lg"
}

function XPFloatingAnimation({
    xp,
    position = "top",
    size = "default",
}: XPFloatingAnimationProps) {
    const positionStyles = {
        top: "absolute -top-8 left-1/2 -translate-x-1/2",
        right: "absolute -right-2 top-0",
        center: "absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2",
    }

    const sizeStyles = {
        sm: "text-lg",
        default: "text-xl",
        lg: "text-3xl",
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.5 }}
            animate={{ opacity: 1, y: -20, scale: 1 }}
            exit={{ opacity: 0, y: -40, scale: 0.8 }}
            transition={{ duration: 0.6, ease: "easeOut" }}
            className={cn(
                positionStyles[position],
                sizeStyles[size],
                "font-bold text-orange-500 pointer-events-none z-50",
                "drop-shadow-lg"
            )}
        >
            +{xp} XP
        </motion.div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default CompleteButton
