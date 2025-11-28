/**
 * ============================================================================
 * LEVEL UP MODAL — Celebration for Leveling Up
 * ============================================================================
 *
 * Modal displayed when user gains enough XP to level up.
 * Features celebration animation, confetti, and level stats.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { useEffect, useState, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Star, Sparkles, Trophy, ChevronRight } from "lucide-react"
import { Button } from "@/components/ui/button"
import { getLevelInfo, getXPForLevel } from "@/lib/progress"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface LevelUpModalProps {
    isOpen: boolean
    onClose: () => void
    oldLevel: number
    newLevel: number
    totalXP: number
}

interface Confetti {
    id: number
    x: number
    color: string
    delay: number
    duration: number
    size: number
}

/* ============================================================================
   CONFETTI COLORS
   ============================================================================ */

const CONFETTI_COLORS = [
    "#FFD700", // Gold
    "#FF6B6B", // Coral
    "#4ECDC4", // Teal
    "#A855F7", // Purple
    "#3B82F6", // Blue
    "#F97316", // Orange
    "#22C55E", // Green
    "#EC4899", // Pink
]

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function LevelUpModal({
    isOpen,
    onClose,
    oldLevel,
    newLevel,
    totalXP,
}: LevelUpModalProps) {
    const [confetti, setConfetti] = useState<Confetti[]>([])
    const [showStats, setShowStats] = useState(false)

    const levelInfo = getLevelInfo(totalXP)
    const xpForOldLevel = getXPForLevel(oldLevel)
    const xpForNewLevel = getXPForLevel(newLevel)

    // Generate confetti
    useEffect(() => {
        if (isOpen) {
            const newConfetti: Confetti[] = Array.from({ length: 50 }, (_, i) => ({
                id: i,
                x: Math.random() * 100,
                color: CONFETTI_COLORS[Math.floor(Math.random() * CONFETTI_COLORS.length)],
                delay: Math.random() * 0.5,
                duration: Math.random() * 2 + 2,
                size: Math.random() * 8 + 4,
            }))
            setConfetti(newConfetti)

            // Show stats after animation
            const timer = setTimeout(() => setShowStats(true), 800)
            return () => clearTimeout(timer)
        } else {
            setShowStats(false)
        }
    }, [isOpen])

    const handleClose = useCallback(() => {
        setShowStats(false)
        onClose()
    }, [onClose])

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
                        onClick={handleClose}
                    />

                    {/* Confetti */}
                    <div className="absolute inset-0 overflow-hidden pointer-events-none">
                        {confetti.map((piece) => (
                            <motion.div
                                key={piece.id}
                                initial={{
                                    x: `${piece.x}vw`,
                                    y: -20,
                                    rotate: 0,
                                    opacity: 1,
                                }}
                                animate={{
                                    y: "110vh",
                                    rotate: 720,
                                    opacity: [1, 1, 0],
                                }}
                                transition={{
                                    duration: piece.duration,
                                    delay: piece.delay,
                                    ease: "linear",
                                }}
                                className="absolute"
                                style={{
                                    width: piece.size,
                                    height: piece.size * 0.6,
                                    backgroundColor: piece.color,
                                    borderRadius: 2,
                                }}
                            />
                        ))}
                    </div>

                    {/* Modal Content */}
                    <motion.div
                        initial={{ scale: 0.5, opacity: 0, y: 50 }}
                        animate={{ scale: 1, opacity: 1, y: 0 }}
                        exit={{ scale: 0.9, opacity: 0, y: 20 }}
                        transition={{
                            type: "spring",
                            stiffness: 300,
                            damping: 20,
                        }}
                        className={cn(
                            "relative w-full max-w-md",
                            "bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900",
                            "rounded-3xl shadow-2xl",
                            "border border-white/10",
                            "overflow-hidden"
                        )}
                    >
                        {/* Glow effect */}
                        <div className="absolute inset-0 bg-gradient-to-br from-purple-500/20 via-transparent to-orange-500/20 pointer-events-none" />

                        {/* Content */}
                        <div className="relative p-8 text-center">
                            {/* Stars decoration */}
                            <motion.div
                                initial={{ scale: 0, rotate: -180 }}
                                animate={{ scale: 1, rotate: 0 }}
                                transition={{ delay: 0.2, type: "spring" }}
                                className="absolute top-4 left-4"
                            >
                                <Sparkles className="h-8 w-8 text-yellow-400" />
                            </motion.div>
                            <motion.div
                                initial={{ scale: 0, rotate: 180 }}
                                animate={{ scale: 1, rotate: 0 }}
                                transition={{ delay: 0.3, type: "spring" }}
                                className="absolute top-4 right-4"
                            >
                                <Star className="h-8 w-8 text-yellow-400 fill-yellow-400" />
                            </motion.div>

                            {/* Level badge */}
                            <motion.div
                                initial={{ scale: 0, y: 30 }}
                                animate={{ scale: 1, y: 0 }}
                                transition={{
                                    delay: 0.1,
                                    type: "spring",
                                    stiffness: 200,
                                }}
                                className="relative mx-auto mb-6"
                            >
                                {/* Outer glow */}
                                <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-orange-500 rounded-full blur-xl opacity-50 scale-150" />

                                {/* Level circle */}
                                <div
                                    className={cn(
                                        "relative w-32 h-32 rounded-full",
                                        "bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500",
                                        "flex items-center justify-center",
                                        "shadow-lg shadow-purple-500/50"
                                    )}
                                >
                                    <div
                                        className={cn(
                                            "w-28 h-28 rounded-full",
                                            "bg-slate-900",
                                            "flex flex-col items-center justify-center"
                                        )}
                                    >
                                        <span className="text-xs uppercase tracking-wider text-purple-300 font-medium">
                                            Level
                                        </span>
                                        <motion.span
                                            initial={{ scale: 0 }}
                                            animate={{ scale: [0, 1.2, 1] }}
                                            transition={{ delay: 0.4, duration: 0.5 }}
                                            className="text-5xl font-black text-white"
                                        >
                                            {newLevel}
                                        </motion.span>
                                    </div>
                                </div>
                            </motion.div>

                            {/* Title */}
                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.3 }}
                            >
                                <h2 className="text-3xl font-black text-white mb-2">
                                    Level Up!
                                </h2>
                                <p className="text-purple-300">
                                    You&apos;ve reached Level {newLevel}!
                                </p>
                            </motion.div>

                            {/* Stats */}
                            <AnimatePresence>
                                {showStats && (
                                    <motion.div
                                        initial={{ opacity: 0, height: 0 }}
                                        animate={{ opacity: 1, height: "auto" }}
                                        exit={{ opacity: 0, height: 0 }}
                                        className="mt-6 space-y-4"
                                    >
                                        {/* Progress comparison */}
                                        <div className="flex items-center justify-center gap-4 text-sm">
                                            <div className="text-center">
                                                <div className="text-muted-foreground">From</div>
                                                <div className="text-2xl font-bold text-white/60">
                                                    Level {oldLevel}
                                                </div>
                                            </div>
                                            <ChevronRight className="h-6 w-6 text-purple-400" />
                                            <div className="text-center">
                                                <div className="text-muted-foreground">To</div>
                                                <div className="text-2xl font-bold text-white">
                                                    Level {newLevel}
                                                </div>
                                            </div>
                                        </div>

                                        {/* XP info */}
                                        <div className="bg-white/5 rounded-xl p-4">
                                            <div className="flex items-center justify-between text-sm mb-2">
                                                <span className="text-muted-foreground">Total XP</span>
                                                <span className="font-bold text-orange-400">
                                                    {totalXP.toLocaleString()} XP
                                                </span>
                                            </div>
                                            <div className="flex items-center justify-between text-sm">
                                                <span className="text-muted-foreground">
                                                    Next level at
                                                </span>
                                                <span className="font-medium text-white">
                                                    {levelInfo.xpForNextLevel.toLocaleString()} XP
                                                </span>
                                            </div>
                                            {/* Progress bar */}
                                            <div className="mt-3 h-2 bg-white/10 rounded-full overflow-hidden">
                                                <motion.div
                                                    initial={{ width: 0 }}
                                                    animate={{
                                                        width: `${levelInfo.progressToNextLevel}%`,
                                                    }}
                                                    transition={{ delay: 0.5, duration: 0.8 }}
                                                    className="h-full bg-gradient-to-r from-purple-500 to-orange-500 rounded-full"
                                                />
                                            </div>
                                        </div>
                                    </motion.div>
                                )}
                            </AnimatePresence>

                            {/* Continue button */}
                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.6 }}
                                className="mt-8"
                            >
                                <Button
                                    onClick={handleClose}
                                    size="lg"
                                    className={cn(
                                        "w-full font-bold",
                                        "bg-gradient-to-r from-purple-500 to-orange-500",
                                        "hover:from-purple-600 hover:to-orange-600",
                                        "shadow-lg shadow-purple-500/25"
                                    )}
                                >
                                    <Trophy className="mr-2 h-5 w-5" />
                                    Continue Learning
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

export default LevelUpModal
