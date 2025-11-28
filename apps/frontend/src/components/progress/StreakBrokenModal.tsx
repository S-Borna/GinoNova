/**
 * ============================================================================
 * STREAK BROKEN MODAL — Notification When Streak is Lost
 * ============================================================================
 *
 * Modal displayed when user's learning streak is broken due to inactivity.
 * Provides motivation to start a new streak.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { motion, AnimatePresence } from "framer-motion"
import { Flame, RefreshCw, ArrowRight } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import Link from "next/link"

/* ============================================================================
   TYPES
   ============================================================================ */

interface StreakBrokenModalProps {
    isOpen: boolean
    onClose: () => void
    previousStreak: number
    longestStreak?: number
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function StreakBrokenModal({
    isOpen,
    onClose,
    previousStreak,
    longestStreak,
}: StreakBrokenModalProps) {
    const wasLongStreak = previousStreak >= 7

    return (
        <AnimatePresence>
            {isOpen && (
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="fixed inset-0 z-50 flex items-center justify-center p-4"
                >
                    {/* Backdrop */}
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
                        onClick={onClose}
                    />

                    {/* Modal Content */}
                    <motion.div
                        initial={{ scale: 0.9, opacity: 0, y: 20 }}
                        animate={{ scale: 1, opacity: 1, y: 0 }}
                        exit={{ scale: 0.95, opacity: 0, y: 10 }}
                        transition={{
                            type: "spring",
                            stiffness: 300,
                            damping: 30,
                        }}
                        className={cn(
                            "relative w-full max-w-md",
                            "bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900",
                            "rounded-2xl shadow-2xl",
                            "border border-white/10",
                            "overflow-hidden"
                        )}
                    >
                        {/* Top accent */}
                        <div className="h-1 bg-gradient-to-r from-slate-500 via-slate-400 to-slate-500" />

                        {/* Content */}
                        <div className="p-8 text-center">
                            {/* Icon */}
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                transition={{ delay: 0.1 }}
                                className="flex justify-center mb-6"
                            >
                                <div
                                    className={cn(
                                        "w-20 h-20 rounded-full",
                                        "bg-slate-800 border-2 border-slate-600",
                                        "flex items-center justify-center",
                                        "relative"
                                    )}
                                >
                                    <Flame className="w-10 h-10 text-slate-500" />
                                    {/* Broken effect */}
                                    <motion.div
                                        initial={{ opacity: 0, scale: 0.5 }}
                                        animate={{ opacity: 1, scale: 1 }}
                                        transition={{ delay: 0.3 }}
                                        className="absolute -top-1 -right-1 w-6 h-6 bg-red-500 rounded-full flex items-center justify-center"
                                    >
                                        <span className="text-white text-xs font-bold">!</span>
                                    </motion.div>
                                </div>
                            </motion.div>

                            {/* Title */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.2 }}
                            >
                                <h2 className="text-2xl font-bold text-white mb-2">
                                    Streak Lost
                                </h2>
                                <p className="text-muted-foreground">
                                    Your{" "}
                                    <span className="text-orange-400 font-semibold">
                                        {previousStreak} day
                                    </span>{" "}
                                    streak has ended
                                </p>
                            </motion.div>

                            {/* Message */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.3 }}
                                className="mt-6 mb-6"
                            >
                                {wasLongStreak ? (
                                    <div className="space-y-3">
                                        <p className="text-white/80">
                                            You were on an amazing run! 🙌
                                        </p>
                                        <p className="text-sm text-muted-foreground">
                                            Every expert was once a beginner who didn&apos;t give up.
                                            Start fresh today!
                                        </p>
                                    </div>
                                ) : (
                                    <p className="text-white/80">
                                        No worries! Building habits takes time.
                                        <br />
                                        Let&apos;s start a new streak today! 💪
                                    </p>
                                )}
                            </motion.div>

                            {/* Stats */}
                            {longestStreak !== undefined && longestStreak > previousStreak && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.4 }}
                                    className={cn(
                                        "mb-6 p-4 rounded-xl",
                                        "bg-white/5 border border-white/10"
                                    )}
                                >
                                    <p className="text-sm text-muted-foreground">
                                        Your longest streak:
                                    </p>
                                    <p className="text-2xl font-bold text-orange-400 flex items-center justify-center gap-2">
                                        <Flame className="w-5 h-5" />
                                        {longestStreak} days
                                    </p>
                                    <p className="text-xs text-muted-foreground mt-1">
                                        Can you beat your record?
                                    </p>
                                </motion.div>
                            )}

                            {/* Actions */}
                            <motion.div
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.5 }}
                                className="flex flex-col gap-3"
                            >
                                <Button
                                    asChild
                                    size="lg"
                                    className="w-full bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-semibold"
                                >
                                    <Link href="/dashboard">
                                        <RefreshCw className="mr-2 w-4 h-4" />
                                        Start New Streak
                                    </Link>
                                </Button>

                                <Button
                                    variant="ghost"
                                    size="lg"
                                    onClick={onClose}
                                    className="w-full text-muted-foreground hover:text-white"
                                >
                                    Dismiss
                                    <ArrowRight className="ml-2 w-4 h-4" />
                                </Button>
                            </motion.div>
                        </div>
                    </motion.div>
                </motion.div>
            )}
        </AnimatePresence>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default StreakBrokenModal
