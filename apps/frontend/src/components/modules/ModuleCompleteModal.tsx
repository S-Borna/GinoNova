/**
 * ============================================================================
 * MODULE COMPLETE MODAL — Celebration for Completing a Module
 * ============================================================================
 *
 * Modal displayed when user completes all tasks in a module.
 * Shows stats, XP earned, and unlocks next module.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { useEffect, useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import {
    CheckCircle2,
    ChevronRight,
    Trophy,
    Clock,
    Star,
    Zap,
    Lock,
    Unlock,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { XP_REWARDS } from "@/lib/progress"
import { cn } from "@/lib/utils"
import Link from "next/link"

/* ============================================================================
   TYPES
   ============================================================================ */

interface ModuleCompleteModalProps {
    isOpen: boolean
    onClose: () => void
    moduleId: string
    moduleName: string
    moduleSlug?: string
    trackName: string
    trackColor?: string
    tasksCompleted: number
    labsCompleted: number
    projectCompleted: boolean
    xpEarned: number
    timeSpent?: number // minutes
    nextModule?: {
        id: string
        name: string
        slug: string
        isUnlocked: boolean
    } | null
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function ModuleCompleteModal({
    isOpen,
    onClose,
    moduleId,
    moduleName,
    moduleSlug,
    trackName,
    trackColor = "#6366f1",
    tasksCompleted,
    labsCompleted,
    projectCompleted,
    xpEarned,
    timeSpent,
    nextModule,
}: ModuleCompleteModalProps) {
    const [showStats, setShowStats] = useState(false)
    const [showNext, setShowNext] = useState(false)

    // Stagger animations
    useEffect(() => {
        if (isOpen) {
            const statsTimer = setTimeout(() => setShowStats(true), 600)
            const nextTimer = setTimeout(() => setShowNext(true), 1200)

            return () => {
                clearTimeout(statsTimer)
                clearTimeout(nextTimer)
            }
        } else {
            setShowStats(false)
            setShowNext(false)
        }
    }, [isOpen])

    const bonusXP = XP_REWARDS.MODULE_COMPLETE_BONUS

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

                    {/* Celebration particles */}
                    <div className="absolute inset-0 overflow-hidden pointer-events-none">
                        {[...Array(20)].map((_, i) => (
                            <motion.div
                                key={i}
                                initial={{
                                    x: "50vw",
                                    y: "50vh",
                                    scale: 0,
                                }}
                                animate={{
                                    x: `${20 + Math.random() * 60}vw`,
                                    y: `${20 + Math.random() * 60}vh`,
                                    scale: [0, 1, 0],
                                }}
                                transition={{
                                    duration: 2,
                                    delay: i * 0.05,
                                    ease: "easeOut",
                                }}
                                className="absolute w-3 h-3 rounded-full"
                                style={{
                                    backgroundColor: trackColor,
                                    opacity: 0.6,
                                }}
                            />
                        ))}
                    </div>

                    {/* Modal Content */}
                    <motion.div
                        initial={{ scale: 0.8, opacity: 0, y: 50 }}
                        animate={{ scale: 1, opacity: 1, y: 0 }}
                        exit={{ scale: 0.9, opacity: 0, y: 20 }}
                        transition={{
                            type: "spring",
                            stiffness: 300,
                            damping: 25,
                        }}
                        className={cn(
                            "relative w-full max-w-lg",
                            "bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900",
                            "rounded-3xl shadow-2xl",
                            "border border-white/10",
                            "overflow-hidden"
                        )}
                    >
                        {/* Top color bar */}
                        <div
                            className="h-2"
                            style={{
                                background: `linear-gradient(to right, ${trackColor}, ${trackColor}88)`,
                            }}
                        />

                        {/* Content */}
                        <div className="p-8">
                            {/* Success icon */}
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                transition={{
                                    type: "spring",
                                    stiffness: 300,
                                    delay: 0.1,
                                }}
                                className="flex justify-center mb-6"
                            >
                                <div
                                    className={cn(
                                        "w-24 h-24 rounded-full",
                                        "flex items-center justify-center",
                                        "shadow-lg"
                                    )}
                                    style={{
                                        background: `linear-gradient(135deg, ${trackColor}33, ${trackColor}11)`,
                                        borderColor: trackColor,
                                        borderWidth: 2,
                                    }}
                                >
                                    <motion.div
                                        initial={{ scale: 0, rotate: -180 }}
                                        animate={{ scale: 1, rotate: 0 }}
                                        transition={{ delay: 0.3, type: "spring" }}
                                    >
                                        <CheckCircle2
                                            className="w-12 h-12"
                                            style={{ color: trackColor }}
                                        />
                                    </motion.div>
                                </div>
                            </motion.div>

                            {/* Title */}
                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.2 }}
                                className="text-center mb-6"
                            >
                                <p
                                    className="text-sm font-medium mb-2"
                                    style={{ color: trackColor }}
                                >
                                    {trackName}
                                </p>
                                <h2 className="text-2xl font-bold text-white mb-2">
                                    Module Complete!
                                </h2>
                                <p className="text-lg text-white/80">{moduleName}</p>
                            </motion.div>

                            {/* Stats grid */}
                            <AnimatePresence>
                                {showStats && (
                                    <motion.div
                                        initial={{ opacity: 0, y: 20 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0 }}
                                        className="grid grid-cols-2 gap-3 mb-6"
                                    >
                                        <StatCard
                                            icon={<CheckCircle2 className="w-5 h-5" />}
                                            label="Tasks"
                                            value={tasksCompleted}
                                            color="#22c55e"
                                            delay={0}
                                        />
                                        <StatCard
                                            icon={<Zap className="w-5 h-5" />}
                                            label="Labs"
                                            value={labsCompleted}
                                            color="#3b82f6"
                                            delay={0.1}
                                        />
                                        {timeSpent && (
                                            <StatCard
                                                icon={<Clock className="w-5 h-5" />}
                                                label="Time"
                                                value={`${Math.round(timeSpent / 60)}h`}
                                                color="#a855f7"
                                                delay={0.2}
                                            />
                                        )}
                                        <StatCard
                                            icon={<Star className="w-5 h-5" />}
                                            label="XP Earned"
                                            value={`+${xpEarned}`}
                                            color="#f97316"
                                            delay={0.3}
                                            highlight
                                        />
                                    </motion.div>
                                )}
                            </AnimatePresence>

                            {/* Bonus XP banner */}
                            <motion.div
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: 0.8 }}
                                className={cn(
                                    "mb-6 p-4 rounded-xl",
                                    "bg-gradient-to-r from-orange-500/20 to-amber-500/20",
                                    "border border-orange-500/30"
                                )}
                            >
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-3">
                                        <Trophy className="w-6 h-6 text-orange-400" />
                                        <span className="font-medium text-white">
                                            Completion Bonus
                                        </span>
                                    </div>
                                    <span className="text-lg font-bold text-orange-400">
                                        +{bonusXP} XP
                                    </span>
                                </div>
                            </motion.div>

                            {/* Next module preview */}
                            <AnimatePresence>
                                {showNext && nextModule && (
                                    <motion.div
                                        initial={{ opacity: 0, y: 20 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0 }}
                                        className={cn(
                                            "mb-6 p-4 rounded-xl",
                                            "bg-white/5 border border-white/10"
                                        )}
                                    >
                                        <div className="flex items-center gap-2 text-sm text-muted-foreground mb-2">
                                            {nextModule.isUnlocked ? (
                                                <Unlock className="w-4 h-4 text-green-400" />
                                            ) : (
                                                <Lock className="w-4 h-4" />
                                            )}
                                            <span>
                                                {nextModule.isUnlocked
                                                    ? "Next module unlocked!"
                                                    : "Up next"}
                                            </span>
                                        </div>
                                        <p className="font-medium text-white">
                                            {nextModule.name}
                                        </p>
                                    </motion.div>
                                )}
                            </AnimatePresence>

                            {/* Action buttons */}
                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 1 }}
                                className="flex gap-3"
                            >
                                <Button
                                    variant="outline"
                                    onClick={onClose}
                                    className="flex-1"
                                >
                                    Close
                                </Button>
                                {nextModule ? (
                                    <Button
                                        asChild
                                        className={cn(
                                            "flex-1 font-semibold",
                                            "bg-gradient-to-r",
                                            "shadow-lg"
                                        )}
                                        style={{
                                            backgroundImage: `linear-gradient(to right, ${trackColor}, ${trackColor}cc)`,
                                            boxShadow: `0 4px 14px ${trackColor}40`,
                                        }}
                                    >
                                        <Link prefetch={false} href={`/modules/${nextModule.slug}`}>
                                            Start Next Module
                                            <ChevronRight className="ml-1 w-4 h-4" />
                                        </Link>
                                    </Button>
                                ) : (
                                    <Button
                                        asChild
                                        className="flex-1 bg-gradient-to-r from-green-500 to-emerald-500"
                                    >
                                        <Link prefetch={false} href="/modules">
                                            View All Modules
                                            <ChevronRight className="ml-1 w-4 h-4" />
                                        </Link>
                                    </Button>
                                )}
                            </motion.div>
                        </div>
                    </motion.div>
                </motion.div>
            )}
        </AnimatePresence>
    )
}

/* ============================================================================
   STAT CARD COMPONENT
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
    delay: number
    highlight?: boolean
}

function StatCard({ icon, label, value, color, delay, highlight }: StatCardProps) {
    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay }}
            className={cn(
                "p-3 rounded-xl",
                "bg-white/5 border border-white/10",
                highlight && "bg-orange-500/10 border-orange-500/20"
            )}
        >
            <div className="flex items-center gap-2 mb-1">
                <span style={{ color }}>{icon}</span>
                <span className="text-xs text-muted-foreground">{label}</span>
            </div>
            <p
                className={cn(
                    "text-xl font-bold",
                    highlight ? "text-orange-400" : "text-white"
                )}
            >
                {value}
            </p>
        </motion.div>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default ModuleCompleteModal
