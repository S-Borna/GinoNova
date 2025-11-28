"use client"

/**
 * ============================================================================
 * HINTS COMPONENT - Progressive Hint Reveal System
 * ============================================================================
 *
 * Features:
 * - Expandable hint sections
 * - Progressive reveal (unlock hints one by one)
 * - Confirmation dialog before revealing
 * - Visual indication of hint levels
 * - Markdown support for hint content
 *
 * @phase C.3 - Labs & Projects Display
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { motion, AnimatePresence } from "framer-motion"
import {
    Lightbulb,
    ChevronDown,
    Lock,
    Unlock,
    AlertTriangle,
    Eye,
    EyeOff,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
} from "@/components/ui/alert-dialog"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface HintItem {
    id: string
    title: string
    content: string
    level?: "easy" | "medium" | "detailed"
}

interface HintsProps {
    /** Unique identifier for persistence */
    storageKey: string
    /** List of hints to display */
    hints: HintItem[]
    /** Track color for styling */
    trackColor?: string
    /** Whether to require confirmation before revealing */
    requireConfirmation?: boolean
    /** Title override */
    title?: string
    /** Additional class names */
    className?: string
}

/* ============================================================================
   LOCAL STORAGE HELPERS
   ============================================================================ */

function getRevealedHints(key: string): string[] {
    if (typeof window === "undefined") return []
    try {
        const stored = localStorage.getItem(`hints-revealed-${key}`)
        return stored ? JSON.parse(stored) : []
    } catch {
        return []
    }
}

function setRevealedHints(key: string, revealed: string[]): void {
    if (typeof window === "undefined") return
    try {
        localStorage.setItem(`hints-revealed-${key}`, JSON.stringify(revealed))
    } catch {
        // Storage quota exceeded or other error
    }
}

/* ============================================================================
   HINT LEVEL INDICATOR
   ============================================================================ */

interface HintLevelProps {
    level?: "easy" | "medium" | "detailed"
}

const LEVEL_CONFIG = {
    easy: {
        label: "Gentle Nudge",
        color: "#22c55e",
        bgColor: "bg-green-50 dark:bg-green-950/30",
        textColor: "text-green-700 dark:text-green-400",
    },
    medium: {
        label: "Helpful Hint",
        color: "#f59e0b",
        bgColor: "bg-amber-50 dark:bg-amber-950/30",
        textColor: "text-amber-700 dark:text-amber-400",
    },
    detailed: {
        label: "Detailed Guide",
        color: "#ef4444",
        bgColor: "bg-red-50 dark:bg-red-950/30",
        textColor: "text-red-700 dark:text-red-400",
    },
}

function HintLevel({ level = "medium" }: HintLevelProps) {
    const config = LEVEL_CONFIG[level]

    return (
        <span
            className={cn(
                "inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium",
                config.bgColor,
                config.textColor
            )}
        >
            {config.label}
        </span>
    )
}

/* ============================================================================
   SINGLE HINT ITEM
   ============================================================================ */

interface HintItemComponentProps {
    hint: HintItem
    index: number
    isRevealed: boolean
    isLocked: boolean
    onReveal: () => void
    trackColor: string
}

function HintItemComponent({
    hint,
    index,
    isRevealed,
    isLocked,
    onReveal,
    trackColor,
}: HintItemComponentProps) {
    const [isExpanded, setIsExpanded] = React.useState(false)

    return (
        <div
            className={cn(
                "border rounded-lg overflow-hidden transition-all duration-200",
                isRevealed
                    ? "border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-900"
                    : "border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900/50"
            )}
        >
            {/* Header */}
            <button
                onClick={() => {
                    if (isRevealed) {
                        setIsExpanded(!isExpanded)
                    } else if (!isLocked) {
                        onReveal()
                    }
                }}
                disabled={isLocked}
                className={cn(
                    "w-full flex items-center gap-3 p-4 text-left",
                    "transition-colors duration-200",
                    isRevealed && "hover:bg-neutral-50 dark:hover:bg-neutral-800/50",
                    isLocked && "opacity-60 cursor-not-allowed"
                )}
            >
                {/* Icon */}
                <div
                    className={cn(
                        "flex-shrink-0 p-2 rounded-lg",
                        isRevealed
                            ? "bg-amber-100 dark:bg-amber-900/30"
                            : "bg-neutral-200 dark:bg-neutral-800"
                    )}
                >
                    {isLocked ? (
                        <Lock className="h-4 w-4 text-neutral-400" />
                    ) : isRevealed ? (
                        <Lightbulb className="h-4 w-4 text-amber-500" />
                    ) : (
                        <Unlock className="h-4 w-4 text-neutral-500" />
                    )}
                </div>

                {/* Title */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                        <span className="text-xs font-medium text-neutral-400 dark:text-neutral-500">
                            Hint {index + 1}
                        </span>
                        {hint.level && <HintLevel level={hint.level} />}
                    </div>
                    <p
                        className={cn(
                            "text-sm font-medium mt-0.5 truncate",
                            isRevealed
                                ? "text-neutral-900 dark:text-white"
                                : "text-neutral-500 dark:text-neutral-400"
                        )}
                    >
                        {isRevealed ? hint.title : "Click to reveal hint"}
                    </p>
                </div>

                {/* Action indicator */}
                {!isLocked && (
                    <div className="flex-shrink-0">
                        {isRevealed ? (
                            <ChevronDown
                                className={cn(
                                    "h-5 w-5 text-neutral-400 transition-transform duration-200",
                                    isExpanded && "rotate-180"
                                )}
                            />
                        ) : (
                            <Eye className="h-5 w-5 text-neutral-400" />
                        )}
                    </div>
                )}
            </button>

            {/* Content */}
            <AnimatePresence>
                {isRevealed && isExpanded && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.2 }}
                    >
                        <div
                            className="px-4 pb-4 border-t border-neutral-100 dark:border-neutral-800"
                            style={{ borderLeftColor: trackColor, borderLeftWidth: 3 }}
                        >
                            <div className="pt-4 prose prose-sm dark:prose-invert max-w-none">
                                <div
                                    className="text-sm text-neutral-700 dark:text-neutral-300"
                                    dangerouslySetInnerHTML={{ __html: hint.content }}
                                />
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function Hints({
    storageKey,
    hints,
    trackColor = "#6366f1",
    requireConfirmation = true,
    title = "Need Help?",
    className,
}: HintsProps) {
    // State
    const [revealed, setRevealed] = React.useState<string[]>([])
    const [isInitialized, setIsInitialized] = React.useState(false)
    const [confirmDialog, setConfirmDialog] = React.useState<{
        open: boolean
        hintId: string | null
        hintIndex: number
    }>({
        open: false,
        hintId: null,
        hintIndex: 0,
    })
    const [showAllHints, setShowAllHints] = React.useState(false)

    // Load saved state on mount
    React.useEffect(() => {
        const stored = getRevealedHints(storageKey)
        setRevealed(stored)
        setIsInitialized(true)
    }, [storageKey])

    // Handle reveal
    const handleReveal = (hintId: string, index: number) => {
        if (requireConfirmation) {
            setConfirmDialog({ open: true, hintId, hintIndex: index })
        } else {
            revealHint(hintId)
        }
    }

    const revealHint = (hintId: string) => {
        setRevealed((prev) => {
            const newRevealed = [...prev, hintId]
            setRevealedHints(storageKey, newRevealed)
            return newRevealed
        })
        setConfirmDialog({ open: false, hintId: null, hintIndex: 0 })
    }

    // Calculate next available hint index
    const getNextAvailableIndex = () => {
        for (let i = 0; i < hints.length; i++) {
            if (!revealed.includes(hints[i].id)) {
                return i
            }
        }
        return -1
    }

    const nextAvailableIndex = getNextAvailableIndex()

    // Don't render until initialized (prevents hydration mismatch)
    if (!isInitialized) {
        return (
            <div className={cn("rounded-xl border border-neutral-200 dark:border-neutral-800", className)}>
                <div className="p-4">
                    <div className="h-6 w-32 bg-neutral-200 dark:bg-neutral-800 rounded animate-pulse" />
                </div>
                <div className="px-4 pb-4 space-y-3">
                    {hints.slice(0, 2).map((_, i) => (
                        <div key={i} className="h-16 bg-neutral-100 dark:bg-neutral-900 rounded-lg animate-pulse" />
                    ))}
                </div>
            </div>
        )
    }

    const revealedCount = revealed.length
    const totalCount = hints.length
    const allRevealed = revealedCount === totalCount

    return (
        <>
            <div
                className={cn(
                    "rounded-xl border border-neutral-200 dark:border-neutral-800",
                    "bg-white dark:bg-neutral-900",
                    className
                )}
            >
                {/* Header */}
                <div className="flex items-center justify-between p-4 border-b border-neutral-200 dark:border-neutral-800">
                    <div className="flex items-center gap-3">
                        <div
                            className="p-2 rounded-lg"
                            style={{ backgroundColor: `${trackColor}15` }}
                        >
                            <Lightbulb
                                className="h-5 w-5"
                                style={{ color: trackColor }}
                            />
                        </div>
                        <div>
                            <h3 className="font-semibold text-neutral-900 dark:text-white">
                                {title}
                            </h3>
                            <p className="text-xs text-neutral-500 dark:text-neutral-400 mt-0.5">
                                {revealedCount} of {totalCount} hints revealed
                            </p>
                        </div>
                    </div>

                    {/* Toggle all hints visibility */}
                    {hints.length > 3 && (
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={() => setShowAllHints(!showAllHints)}
                            className="text-neutral-500"
                        >
                            {showAllHints ? (
                                <>
                                    <EyeOff className="h-4 w-4 mr-1.5" />
                                    Show Less
                                </>
                            ) : (
                                <>
                                    <Eye className="h-4 w-4 mr-1.5" />
                                    Show All
                                </>
                            )}
                        </Button>
                    )}
                </div>

                {/* Hints list */}
                <div className="p-4 space-y-3">
                    {(showAllHints ? hints : hints.slice(0, 3)).map((hint, index) => {
                        const isRevealed = revealed.includes(hint.id)
                        // Lock hints that come after the next available one (progressive reveal)
                        const isLocked = !isRevealed && index > nextAvailableIndex

                        return (
                            <HintItemComponent
                                key={hint.id}
                                hint={hint}
                                index={index}
                                isRevealed={isRevealed}
                                isLocked={isLocked}
                                onReveal={() => handleReveal(hint.id, index)}
                                trackColor={trackColor}
                            />
                        )
                    })}

                    {/* Show count of remaining hidden hints */}
                    {!showAllHints && hints.length > 3 && (
                        <div className="text-center py-2">
                            <button
                                onClick={() => setShowAllHints(true)}
                                className="text-sm text-neutral-500 hover:text-neutral-700 dark:hover:text-neutral-300 transition-colors"
                            >
                                + {hints.length - 3} more hints available
                            </button>
                        </div>
                    )}
                </div>

                {/* All revealed message */}
                {allRevealed && (
                    <div className="px-4 pb-4">
                        <div className="flex items-center gap-2 p-3 rounded-lg bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/50">
                            <Lightbulb className="h-4 w-4 text-amber-500" />
                            <p className="text-sm text-amber-700 dark:text-amber-400">
                                All hints have been revealed. Good luck!
                            </p>
                        </div>
                    </div>
                )}
            </div>

            {/* Confirmation Dialog */}
            <AlertDialog
                open={confirmDialog.open}
                onOpenChange={(open: boolean) =>
                    setConfirmDialog((prev) => ({ ...prev, open }))
                }
            >
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogTitle className="flex items-center gap-2">
                            <AlertTriangle className="h-5 w-5 text-amber-500" />
                            Reveal Hint {confirmDialog.hintIndex + 1}?
                        </AlertDialogTitle>
                        <AlertDialogDescription>
                            Try to solve the problem on your own first. Hints are
                            here to help when you&apos;re truly stuck.
                            <br />
                            <br />
                            <span className="text-neutral-600 dark:text-neutral-400">
                                Once revealed, this hint will remain visible.
                            </span>
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel>Keep Trying</AlertDialogCancel>
                        <AlertDialogAction
                            onClick={() =>
                                confirmDialog.hintId && revealHint(confirmDialog.hintId)
                            }
                            style={{ backgroundColor: trackColor }}
                        >
                            Show Hint
                        </AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        </>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default Hints
