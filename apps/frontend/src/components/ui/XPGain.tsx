/**
 * ============================================================================
 * XP GAIN — Animated XP Reward Display
 * ============================================================================
 *
 * Floating XP animation with particles for rewarding user actions.
 *
 * @phase A.5 - Progress & Completion Logic
 */

"use client"

import { useEffect, useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"

/* ============================================================================
   TYPES
   ============================================================================ */

interface XPGainProps {
    xp: number
    show: boolean
    onComplete?: () => void
    position?: "center" | "top-right" | "bottom-center"
    size?: "sm" | "md" | "lg"
    showBreakdown?: boolean
    breakdown?: { label: string; xp: number }[]
    className?: string
}

interface Particle {
    id: number
    x: number
    y: number
    size: number
    delay: number
    duration: number
}

/* ============================================================================
   COMPONENT
   ============================================================================ */

export function XPGain({
    xp,
    show,
    onComplete,
    position = "center",
    size = "md",
    showBreakdown = false,
    breakdown = [],
    className,
}: XPGainProps) {
    const [particles, setParticles] = useState<Particle[]>([])

    // Generate particles on show
    useEffect(() => {
        if (show) {
            const newParticles: Particle[] = Array.from({ length: 12 }, (_, i) => ({
                id: i,
                x: (Math.random() - 0.5) * 200,
                y: (Math.random() - 0.5) * 200,
                size: Math.random() * 8 + 4,
                delay: Math.random() * 0.3,
                duration: Math.random() * 0.5 + 0.5,
            }))
            setParticles(newParticles)

            // Trigger onComplete after animation
            const timer = setTimeout(() => {
                onComplete?.()
            }, 2000)

            return () => clearTimeout(timer)
        }
    }, [show, onComplete])

    const positionStyles = {
        center: "fixed inset-0 flex items-center justify-center z-50",
        "top-right": "fixed top-20 right-8 z-50",
        "bottom-center": "fixed bottom-32 left-1/2 -translate-x-1/2 z-50",
    }

    const sizeStyles = {
        sm: { text: "text-2xl", container: "p-4" },
        md: { text: "text-4xl", container: "p-6" },
        lg: { text: "text-6xl", container: "p-8" },
    }

    return (
        <AnimatePresence>
            {show && (
                <div className={cn(positionStyles[position], className)}>
                    {/* Background overlay for center position */}
                    {position === "center" && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            className="absolute inset-0 bg-black/20 backdrop-blur-sm"
                        />
                    )}

                    {/* Main XP display */}
                    <motion.div
                        initial={{ scale: 0, opacity: 0, rotate: -10 }}
                        animate={{ scale: 1, opacity: 1, rotate: 0 }}
                        exit={{ scale: 0.5, opacity: 0, y: -50 }}
                        transition={{
                            type: "spring",
                            stiffness: 300,
                            damping: 15,
                        }}
                        className={cn(
                            "relative",
                            sizeStyles[size].container
                        )}
                    >
                        {/* Glow effect */}
                        <div className="absolute inset-0 bg-orange-500/30 blur-3xl rounded-full" />

                        {/* XP Text */}
                        <motion.div
                            initial={{ y: 20 }}
                            animate={{ y: 0 }}
                            className="relative text-center"
                        >
                            <motion.span
                                className={cn(
                                    sizeStyles[size].text,
                                    "font-black text-transparent bg-clip-text",
                                    "bg-gradient-to-r from-orange-400 via-amber-400 to-yellow-400",
                                    "drop-shadow-[0_0_30px_rgba(251,146,60,0.5)]"
                                )}
                                animate={{
                                    scale: [1, 1.1, 1],
                                }}
                                transition={{
                                    duration: 0.5,
                                    repeat: 2,
                                    repeatType: "reverse",
                                }}
                            >
                                +{xp} XP
                            </motion.span>

                            {/* Breakdown list */}
                            {showBreakdown && breakdown.length > 0 && (
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.3 }}
                                    className="mt-4 space-y-1"
                                >
                                    {breakdown.map((item, i) => (
                                        <motion.div
                                            key={i}
                                            initial={{ opacity: 0, x: -20 }}
                                            animate={{ opacity: 1, x: 0 }}
                                            transition={{ delay: 0.4 + i * 0.1 }}
                                            className="flex items-center justify-center gap-2 text-sm text-orange-200"
                                        >
                                            <span>{item.label}</span>
                                            <span className="font-bold text-orange-400">+{item.xp}</span>
                                        </motion.div>
                                    ))}
                                </motion.div>
                            )}
                        </motion.div>

                        {/* Particles */}
                        {particles.map((particle) => (
                            <motion.div
                                key={particle.id}
                                initial={{
                                    scale: 0,
                                    x: 0,
                                    y: 0,
                                    opacity: 1,
                                }}
                                animate={{
                                    scale: [0, 1, 0],
                                    x: particle.x,
                                    y: particle.y,
                                    opacity: [0, 1, 0],
                                }}
                                transition={{
                                    duration: particle.duration,
                                    delay: particle.delay,
                                    ease: "easeOut",
                                }}
                                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none"
                                style={{
                                    width: particle.size,
                                    height: particle.size,
                                }}
                            >
                                <div
                                    className="w-full h-full rounded-full"
                                    style={{
                                        background: `radial-gradient(circle, rgb(251, 146, 60) 0%, rgba(251, 146, 60, 0) 70%)`,
                                    }}
                                />
                            </motion.div>
                        ))}

                        {/* Sparkle ring */}
                        <motion.div
                            initial={{ scale: 0.5, opacity: 0 }}
                            animate={{ scale: 2, opacity: [0, 0.5, 0] }}
                            transition={{ duration: 1, ease: "easeOut" }}
                            className="absolute inset-0 rounded-full border-2 border-orange-400/50"
                        />
                    </motion.div>
                </div>
            )}
        </AnimatePresence>
    )
}

/* ============================================================================
   INLINE XP GAIN (for task cards)
   ============================================================================ */

interface InlineXPGainProps {
    xp: number
    show: boolean
    className?: string
}

export function InlineXPGain({ xp, show, className }: InlineXPGainProps) {
    return (
        <AnimatePresence>
            {show && (
                <motion.span
                    initial={{ opacity: 0, y: 10, scale: 0.5 }}
                    animate={{ opacity: 1, y: -20, scale: 1 }}
                    exit={{ opacity: 0, y: -30 }}
                    transition={{ duration: 0.5 }}
                    className={cn(
                        "absolute -top-2 right-0 px-2 py-0.5 rounded-full",
                        "bg-orange-500 text-white text-xs font-bold",
                        "shadow-lg shadow-orange-500/50",
                        className
                    )}
                >
                    +{xp} XP
                </motion.span>
            )}
        </AnimatePresence>
    )
}

/* ============================================================================
   XP COUNTER (for header/stats)
   ============================================================================ */

interface XPCounterProps {
    value: number
    previousValue?: number
    className?: string
}

export function XPCounter({ value, previousValue, className }: XPCounterProps) {
    const [displayValue, setDisplayValue] = useState(previousValue ?? value)
    const [isAnimating, setIsAnimating] = useState(false)

    useEffect(() => {
        if (previousValue !== undefined && value !== previousValue) {
            setIsAnimating(true)

            // Animate counter
            const duration = 1000
            const startTime = Date.now()
            const startValue = previousValue

            const animate = () => {
                const elapsed = Date.now() - startTime
                const progress = Math.min(elapsed / duration, 1)

                // Ease out cubic
                const easeProgress = 1 - Math.pow(1 - progress, 3)
                const currentValue = Math.round(
                    startValue + (value - startValue) * easeProgress
                )

                setDisplayValue(currentValue)

                if (progress < 1) {
                    requestAnimationFrame(animate)
                } else {
                    setIsAnimating(false)
                }
            }

            requestAnimationFrame(animate)
        } else {
            setDisplayValue(value)
        }
    }, [value, previousValue])

    return (
        <motion.span
            className={cn(
                "font-bold tabular-nums",
                isAnimating && "text-orange-500",
                className
            )}
            animate={isAnimating ? { scale: [1, 1.1, 1] } : {}}
            transition={{ duration: 0.3 }}
        >
            {displayValue.toLocaleString()}
        </motion.span>
    )
}

/* ============================================================================
   EXPORTS
   ============================================================================ */

export default XPGain
