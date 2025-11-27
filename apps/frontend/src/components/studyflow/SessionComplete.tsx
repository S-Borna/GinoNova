"use client"

/**
 * ============================================================================
 * SESSION COMPLETE COMPONENT - Celebration Modal
 * ============================================================================
 * 
 * Features:
 * - Confetti animation (subtle)
 * - "Great work!" message
 * - Session summary (focus time, tasks, XP)
 * - Action buttons (Another Session, View Progress, Take a Break)
 * 
 * @phase D.5 - Studyflow UI
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { GlassCard } from "@/components/ui/glass-card"
import { Button } from "@/components/ui/button"
import {
    Trophy,
    Clock,
    Target,
    Zap,
    Play,
    BarChart2,
    Coffee,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export interface SessionSummary {
    totalFocusMinutes: number
    tasksCompleted: number
    xpEarned: number
    streakDays: number
    isNewRecord?: boolean
}

export interface SessionCompleteProps {
    isOpen: boolean
    summary: SessionSummary
    onStartAnother: () => void
    onViewProgress: () => void
    onClose: () => void
    className?: string
}

/* ============================================================================
   CONFETTI ANIMATION
   ============================================================================ */

function Confetti() {
    const confettiCount = 50
    const colors = [
        "bg-primary-400",
        "bg-primary-500",
        "bg-amber-400",
        "bg-emerald-400",
        "bg-pink-400",
        "bg-cyan-400",
    ]

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {Array.from({ length: confettiCount }).map((_, i) => {
                const left = Math.random() * 100
                const animationDelay = Math.random() * 3
                const animationDuration = 3 + Math.random() * 2
                const size = 6 + Math.random() * 8
                const color = colors[Math.floor(Math.random() * colors.length)]

                return (
                    <div
                        key={i}
                        className={cn(
                            "absolute rounded-sm",
                            color
                        )}
                        style={{
                            left: `${left}%`,
                            top: "-20px",
                            width: `${size}px`,
                            height: `${size}px`,
                            animation: `confetti-fall ${animationDuration}s ease-out ${animationDelay}s forwards`,
                            transform: `rotate(${Math.random() * 360}deg)`,
                        }}
                    />
                )
            })}
            <style jsx>{`
                @keyframes confetti-fall {
                    0% {
                        transform: translateY(0) rotate(0deg);
                        opacity: 1;
                    }
                    100% {
                        transform: translateY(600px) rotate(720deg);
                        opacity: 0;
                    }
                }
            `}</style>
        </div>
    )
}

/* ============================================================================
   STAT CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    suffix?: string
    highlight?: boolean
}

function StatCard({ icon, label, value, suffix, highlight }: StatCardProps) {
    return (
        <div className={cn(
            "flex items-center gap-3 p-4 rounded-xl",
            highlight
                ? "bg-gradient-to-br from-amber-100 to-orange-100 dark:from-amber-900/30 dark:to-orange-900/30"
                : "bg-neutral-100 dark:bg-neutral-800"
        )}>
            <div className={cn(
                "p-2 rounded-lg",
                highlight
                    ? "bg-amber-200 text-amber-700 dark:bg-amber-800/50 dark:text-amber-300"
                    : "bg-white text-neutral-600 dark:bg-neutral-700 dark:text-neutral-300"
            )}>
                {icon}
            </div>
            <div>
                <p className="text-xs text-neutral-500 dark:text-neutral-400 uppercase tracking-wider">
                    {label}
                </p>
                <p className="text-xl font-bold text-neutral-900 dark:text-white">
                    {value}{suffix && <span className="text-sm font-normal ml-1">{suffix}</span>}
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   CELEBRATION MESSAGES
   ============================================================================ */

function getCelebrationMessage(summary: SessionSummary): string {
    if (summary.isNewRecord) {
        return "🏆 New personal record!"
    }
    if (summary.tasksCompleted >= 3) {
        return "Incredible productivity!"
    }
    if (summary.totalFocusMinutes >= 50) {
        return "Deep focus achieved!"
    }
    if (summary.streakDays >= 7) {
        return "Week-long streak warrior!"
    }
    return "Great work today!"
}

/* ============================================================================
   MAIN SESSION COMPLETE COMPONENT
   ============================================================================ */

export function SessionComplete({
    isOpen,
    summary,
    onStartAnother,
    onViewProgress,
    onClose,
    className,
}: SessionCompleteProps) {
    if (!isOpen) return null

    const celebrationMessage = getCelebrationMessage(summary)

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
            {/* Confetti */}
            <Confetti />

            {/* Modal */}
            <GlassCard
                variant="solid"
                padding="lg"
                radius="xl"
                className={cn(
                    "max-w-lg w-full animate-scale-in relative z-10",
                    className
                )}
            >
                {/* Header */}
                <div className="text-center mb-6">
                    {/* Trophy Icon */}
                    <div className="mx-auto w-20 h-20 rounded-full bg-gradient-to-br from-amber-100 to-orange-100 dark:from-amber-900/30 dark:to-orange-900/30 flex items-center justify-center mb-4 relative">
                        <Trophy className="h-10 w-10 text-amber-500 dark:text-amber-400" />
                        <Sparkles className="absolute -top-1 -right-1 h-6 w-6 text-amber-400 animate-pulse" />
                    </div>

                    {/* Title */}
                    <h2 className="text-2xl font-bold text-neutral-900 dark:text-white mb-2">
                        {celebrationMessage}
                    </h2>
                    <p className="text-neutral-500 dark:text-neutral-400">
                        You&apos;ve completed your study session
                    </p>
                </div>

                {/* Stats Grid */}
                <div className="grid grid-cols-2 gap-3 mb-6">
                    <StatCard
                        icon={<Clock className="h-5 w-5" />}
                        label="Focus Time"
                        value={summary.totalFocusMinutes}
                        suffix="min"
                    />
                    <StatCard
                        icon={<Target className="h-5 w-5" />}
                        label="Tasks Done"
                        value={summary.tasksCompleted}
                    />
                    <StatCard
                        icon={<Zap className="h-5 w-5" />}
                        label="XP Earned"
                        value={`+${summary.xpEarned}`}
                        highlight
                    />
                    <StatCard
                        icon={<Trophy className="h-5 w-5" />}
                        label="Streak"
                        value={summary.streakDays}
                        suffix="days"
                    />
                </div>

                {/* Action Buttons */}
                <div className="space-y-3">
                    <Button
                        variant="gradient"
                        size="lg"
                        fullWidth
                        onClick={onStartAnother}
                        leftIcon={<Play className="h-5 w-5" />}
                    >
                        Start Another Session
                    </Button>
                    <div className="flex gap-3">
                        <Button
                            variant="outline"
                            size="lg"
                            className="flex-1"
                            onClick={onViewProgress}
                            leftIcon={<BarChart2 className="h-4 w-4" />}
                        >
                            View Progress
                        </Button>
                        <Button
                            variant="ghost"
                            size="lg"
                            className="flex-1"
                            onClick={onClose}
                            leftIcon={<Coffee className="h-4 w-4" />}
                        >
                            Take a Break
                        </Button>
                    </div>
                </div>
            </GlassCard>
        </div>
    )
}

export default SessionComplete
