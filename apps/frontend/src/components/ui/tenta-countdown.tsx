"use client"

/**
 * ============================================================================
 * ⏱️ TENTA COUNTDOWN — DOE25 Linux Tenta 7 Jan 2026 09:30
 * ============================================================================
 *
 * Cosmic countdown timer with:
 * - Live updating seconds
 * - Pulsing animation when < 24h
 * - Gradient glow effects
 * - Responsive design (compact for TopBar, full for landing)
 *
 * @phase DOE25-TENTA-MODULE
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Clock, Zap } from "lucide-react"

/* ============================================================================
   CONSTANTS
   ============================================================================ */

// Target: 7 January 2026 at 09:30 Swedish time
const TENTA_DATE = new Date("2026-01-07T09:30:00+01:00")

/* ============================================================================
   TYPES
   ============================================================================ */

interface TimeLeft {
    days: number
    hours: number
    minutes: number
    seconds: number
    total: number
}

interface TentaCountdownProps {
    variant?: "compact" | "full"
    examDate?: string
    className?: string
}

/* ============================================================================
   HELPER FUNCTIONS
   ============================================================================ */

function calculateTimeLeft(): TimeLeft {
    const now = new Date()
    const difference = TENTA_DATE.getTime() - now.getTime()

    if (difference <= 0) {
        return { days: 0, hours: 0, minutes: 0, seconds: 0, total: 0 }
    }

    return {
        days: Math.floor(difference / (1000 * 60 * 60 * 24)),
        hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
        minutes: Math.floor((difference / 1000 / 60) % 60),
        seconds: Math.floor((difference / 1000) % 60),
        total: difference
    }
}

function padZero(num: number): string {
    return num.toString().padStart(2, "0")
}

/* ============================================================================
   COMPACT VARIANT — For TopBar
   ============================================================================ */

function CompactCountdown({ className }: { className?: string }) {
    const [timeLeft, setTimeLeft] = React.useState<TimeLeft>(calculateTimeLeft)
    const [mounted, setMounted] = React.useState(false)

    React.useEffect(() => {
        setMounted(true)
        const timer = setInterval(() => {
            setTimeLeft(calculateTimeLeft())
        }, 1000)
        return () => clearInterval(timer)
    }, [])

    if (!mounted) return null

    const isUrgent = timeLeft.days < 1
    const isFinished = timeLeft.total <= 0

    if (isFinished) {
        return (
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-3 py-1.5 rounded-lg",
                    "bg-emerald-500/20 border border-emerald-400/40",
                    className
                )}
                animate={{ scale: [1, 1.02, 1] }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                <Zap className="w-4 h-4 text-emerald-400" />
                <span className="text-sm font-bold text-emerald-300">TENTA IDAG!</span>
            </motion.div>
        )
    }

    return (
        <motion.div
            className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-lg",
                "border transition-all duration-300",
                isUrgent
                    ? "bg-red-500/20 border-red-400/40 shadow-[0_0_15px_rgba(239,68,68,0.3)]"
                    : "bg-purple-500/15 border-purple-400/30 shadow-[0_0_15px_rgba(139,92,246,0.2)]",
                className
            )}
            animate={isUrgent ? { scale: [1, 1.02, 1] } : {}}
            transition={{ duration: 1.5, repeat: Infinity }}
        >
            <Clock className={cn(
                "w-4 h-4",
                isUrgent ? "text-red-400" : "text-purple-400"
            )} />

            <div className="flex items-center gap-1 font-mono text-sm font-bold">
                {timeLeft.days > 0 && (
                    <>
                        <span className={isUrgent ? "text-red-300" : "text-purple-300"}>
                            {timeLeft.days}d
                        </span>
                        <span className="text-zinc-500">:</span>
                    </>
                )}
                <span className={isUrgent ? "text-red-300" : "text-purple-300"}>
                    {padZero(timeLeft.hours)}
                </span>
                <span className="text-zinc-500">:</span>
                <span className={isUrgent ? "text-red-300" : "text-purple-300"}>
                    {padZero(timeLeft.minutes)}
                </span>
                <span className="text-zinc-500">:</span>
                <span className={cn(
                    "tabular-nums",
                    isUrgent ? "text-red-300" : "text-purple-300"
                )}>
                    {padZero(timeLeft.seconds)}
                </span>
            </div>

            <span className={cn(
                "hidden sm:block text-xs font-medium",
                isUrgent ? "text-red-400/70" : "text-purple-400/70"
            )}>
                DOE25
            </span>
        </motion.div>
    )
}

/* ============================================================================
   FULL VARIANT — For Landing Page
   ============================================================================ */

function FullCountdown({ className }: { className?: string }) {
    const [timeLeft, setTimeLeft] = React.useState<TimeLeft>(calculateTimeLeft)
    const [mounted, setMounted] = React.useState(false)

    React.useEffect(() => {
        setMounted(true)
        const timer = setInterval(() => {
            setTimeLeft(calculateTimeLeft())
        }, 1000)
        return () => clearInterval(timer)
    }, [])

    if (!mounted) return null

    const isUrgent = timeLeft.days < 1
    const isFinished = timeLeft.total <= 0

    if (isFinished) {
        return (
            <motion.div
                className={cn(
                    "flex flex-col items-center gap-4 p-8 rounded-2xl",
                    "bg-gradient-to-br from-emerald-500/20 to-cyan-500/20",
                    "border border-emerald-400/40",
                    "shadow-[0_0_40px_rgba(16,185,129,0.3)]",
                    className
                )}
                animate={{ scale: [1, 1.02, 1] }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                <Zap className="w-12 h-12 text-emerald-400" />
                <span className="text-3xl font-bold text-emerald-300">
                    TENTAN ÄR IDAG! 🚀
                </span>
                <span className="text-emerald-400/70">
                    Lycka till!
                </span>
            </motion.div>
        )
    }

    const timeBlocks = [
        { value: timeLeft.days, label: "DAGAR" },
        { value: timeLeft.hours, label: "TIMMAR" },
        { value: timeLeft.minutes, label: "MIN" },
        { value: timeLeft.seconds, label: "SEK" },
    ]

    return (
        <motion.div
            className={cn(
                "flex flex-col items-center gap-6 p-8 rounded-2xl",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border transition-all duration-500",
                isUrgent
                    ? "border-red-500/40 shadow-[0_0_60px_rgba(239,68,68,0.3)]"
                    : "border-purple-500/30 shadow-[0_0_60px_rgba(139,92,246,0.2)]",
                className
            )}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
        >
            {/* Header */}
            <div className="text-center">
                <motion.div
                    className={cn(
                        "inline-flex items-center gap-2 px-4 py-1.5 rounded-full mb-3",
                        isUrgent
                            ? "bg-red-500/20 text-red-300"
                            : "bg-purple-500/20 text-purple-300"
                    )}
                    animate={isUrgent ? { scale: [1, 1.05, 1] } : {}}
                    transition={{ duration: 1, repeat: Infinity }}
                >
                    <Clock className="w-4 h-4" />
                    <span className="text-sm font-semibold">DOE25 LINUX TENTA</span>
                </motion.div>
                <h3 className="text-xl font-bold text-zinc-300">
                    7 Januari 2026 • 09:30
                </h3>
            </div>

            {/* Countdown blocks */}
            <div className="flex items-center gap-3 sm:gap-4">
                {timeBlocks.map((block, index) => (
                    <React.Fragment key={block.label}>
                        <motion.div
                            className={cn(
                                "flex flex-col items-center gap-2",
                                "p-4 sm:p-5 rounded-xl min-w-[70px] sm:min-w-[85px]",
                                "bg-zinc-900/50 border",
                                isUrgent
                                    ? "border-red-500/30"
                                    : "border-purple-500/20"
                            )}
                            whileHover={{ scale: 1.05 }}
                            transition={{ duration: 0.2 }}
                        >
                            <span className={cn(
                                "text-3xl sm:text-4xl font-bold font-mono tabular-nums",
                                isUrgent ? "text-red-300" : "text-white"
                            )}>
                                {padZero(block.value)}
                            </span>
                            <span className={cn(
                                "text-xs font-medium tracking-wider",
                                isUrgent ? "text-red-400/70" : "text-zinc-500"
                            )}>
                                {block.label}
                            </span>
                        </motion.div>

                        {index < timeBlocks.length - 1 && (
                            <span className={cn(
                                "text-2xl font-bold",
                                isUrgent ? "text-red-400/50" : "text-purple-400/50"
                            )}>
                                :
                            </span>
                        )}
                    </React.Fragment>
                ))}
            </div>

            {/* Motivation text */}
            <p className={cn(
                "text-sm text-center max-w-md",
                isUrgent ? "text-red-300/70" : "text-zinc-400"
            )}>
                {isUrgent
                    ? "🔥 Sista dagen! Du har pluggat hårt - nu är det dags att visa vad du kan!"
                    : "📚 Varje dag räknas. Fokusera, öva, och du kommer klara detta!"}
            </p>
        </motion.div>
    )
}

/* ============================================================================
   MAIN EXPORT
   ============================================================================ */

export function TentaCountdown({ variant = "compact", className }: TentaCountdownProps) {
    if (variant === "full") {
        return <FullCountdown className={className} />
    }
    return <CompactCountdown className={className} />
}

export default TentaCountdown
