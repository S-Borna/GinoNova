"use client"

/**
 * ============================================================================
 * ✨ EXAM PARTICLE EFFECTS — WOW FACTOR VISUALS ✨
 * ============================================================================
 *
 * Premium particle system for exam simulator:
 * - Success confetti on correct answers
 * - Error particles on wrong answers
 * - Ambient floating particles
 * - Celebration fireworks on completion
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"

interface ParticleEffectProps {
    type: 'success' | 'error' | 'celebration' | 'ambient'
    trigger?: boolean
    onComplete?: () => void
}

export function ExamParticles({ type, trigger = false, onComplete }: ParticleEffectProps) {
    const [show, setShow] = React.useState(false)

    React.useEffect(() => {
        if (trigger && type !== 'ambient') {
            setShow(true)
            const timeout = setTimeout(() => {
                setShow(false)
                onComplete?.()
            }, 2000)
            return () => clearTimeout(timeout)
        }
        if (type === 'ambient') {
            setShow(true)
        }
    }, [trigger, type, onComplete])

    if (!show) return null

    // Success confetti
    if (type === 'success') {
        return (
            <div className="fixed inset-0 pointer-events-none z-50">
                {[...Array(30)].map((_, i) => {
                    const angle = (i / 30) * Math.PI * 2
                    const distance = 200 + Math.random() * 300
                    const size = 6 + Math.random() * 8
                    const colors = ['#22c55e', '#10b981', '#4ade80', '#86efac', '#bbf7d0']

                    return (
                        <motion.div
                            key={i}
                            className="absolute rounded-full"
                            style={{
                                left: '50%',
                                top: '50%',
                                width: size,
                                height: size,
                                background: colors[i % colors.length],
                                boxShadow: `0 0 ${size * 2}px ${colors[i % colors.length]}`,
                            }}
                            initial={{ x: 0, y: 0, opacity: 0, scale: 0 }}
                            animate={{
                                x: Math.cos(angle) * distance,
                                y: Math.sin(angle) * distance - 100,
                                opacity: [0, 1, 0],
                                scale: [0, 2, 0],
                                rotate: [0, 360 * (Math.random() > 0.5 ? 1 : -1)]
                            }}
                            transition={{
                                duration: 1.5,
                                ease: [0.16, 1, 0.3, 1],
                                delay: Math.random() * 0.2
                            }}
                        />
                    )
                })}
            </div>
        )
    }

    // Error particles
    if (type === 'error') {
        return (
            <div className="fixed inset-0 pointer-events-none z-50">
                {[...Array(20)].map((_, i) => {
                    const angle = (i / 20) * Math.PI * 2
                    const distance = 150 + Math.random() * 200
                    const size = 4 + Math.random() * 6
                    const colors = ['#ef4444', '#f87171', '#fca5a5', '#ff6b6b']

                    return (
                        <motion.div
                            key={i}
                            className="absolute"
                            style={{
                                left: '50%',
                                top: '50%',
                                width: size,
                                height: size * 3,
                                background: `linear-gradient(to bottom, ${colors[i % colors.length]}, transparent)`,
                            }}
                            initial={{ x: 0, y: 0, opacity: 0, scaleY: 0 }}
                            animate={{
                                x: Math.cos(angle) * distance,
                                y: Math.sin(angle) * distance,
                                opacity: [0, 0.8, 0],
                                scaleY: [0, 1, 0.5]
                            }}
                            transition={{
                                duration: 1,
                                ease: "easeOut",
                                delay: Math.random() * 0.1
                            }}
                        />
                    )
                })}
            </div>
        )
    }

    // Celebration fireworks
    if (type === 'celebration') {
        return (
            <div className="fixed inset-0 pointer-events-none z-50">
                {[...Array(50)].map((_, i) => {
                    const angle = (i / 50) * Math.PI * 2
                    const distance = 300 + Math.random() * 500
                    const size = 8 + Math.random() * 12
                    const colors = ['#8b5cf6', '#06b6d4', '#ec4899', '#22d3ee', '#a78bfa', '#10b981']

                    return (
                        <motion.div
                            key={i}
                            className="absolute rounded-full"
                            style={{
                                left: '50%',
                                top: '40%',
                                width: size,
                                height: size,
                                background: colors[i % colors.length],
                                boxShadow: `0 0 ${size * 3}px ${colors[i % colors.length]}`,
                            }}
                            initial={{ x: 0, y: 0, opacity: 0, scale: 0 }}
                            animate={{
                                x: Math.cos(angle) * distance,
                                y: Math.sin(angle) * distance - 200,
                                opacity: [0, 1, 1, 0],
                                scale: [0, 1.5, 1, 0],
                                rotate: [0, 720]
                            }}
                            transition={{
                                duration: 2,
                                ease: [0.16, 1, 0.3, 1],
                                delay: Math.random() * 0.3
                            }}
                        />
                    )
                })}

                {/* Additional sparkles */}
                {[...Array(30)].map((_, i) => {
                    const x = -50 + Math.random() * 100
                    const y = -30 + Math.random() * 60
                    const size = 3 + Math.random() * 5

                    return (
                        <motion.div
                            key={`sparkle-${i}`}
                            className="absolute rounded-full bg-white"
                            style={{
                                left: `${50 + x}%`,
                                top: `${40 + y}%`,
                                width: size,
                                height: size,
                                boxShadow: '0 0 10px rgba(255,255,255,0.8)',
                            }}
                            initial={{ opacity: 0, scale: 0 }}
                            animate={{
                                opacity: [0, 1, 0],
                                scale: [0, 2, 0],
                            }}
                            transition={{
                                duration: 1.5,
                                repeat: 3,
                                delay: Math.random() * 2
                            }}
                        />
                    )
                })}
            </div>
        )
    }

    // Ambient particles
    if (type === 'ambient') {
        return (
            <div className="fixed inset-0 pointer-events-none z-10">
                {[...Array(15)].map((_, i) => {
                    const size = 2 + Math.random() * 3
                    const x = Math.random() * 100
                    const y = Math.random() * 100
                    const duration = 15 + Math.random() * 10
                    const delay = Math.random() * 5
                    const colors = ['#8b5cf6', '#06b6d4', '#ec4899', '#ffffff']

                    return (
                        <motion.div
                            key={i}
                            className="absolute rounded-full"
                            style={{
                                width: size,
                                height: size,
                                left: `${x}%`,
                                top: `${y}%`,
                                background: colors[i % colors.length],
                                boxShadow: `0 0 ${size * 4}px ${colors[i % colors.length]}`,
                                opacity: 0.3
                            }}
                            animate={{
                                y: [0, -100, 0],
                                opacity: [0.1, 0.5, 0.1],
                                scale: [1, 1.5, 1]
                            }}
                            transition={{
                                duration,
                                repeat: Infinity,
                                delay,
                                ease: "easeInOut"
                            }}
                        />
                    )
                })}
            </div>
        )
    }

    return null
}

/**
 * Countdown timer with epic animation
 */
interface CountdownProps {
    onComplete: () => void
}

export function ExamCountdown({ onComplete }: CountdownProps) {
    const [count, setCount] = React.useState(3)

    React.useEffect(() => {
        if (count === 0) {
            setTimeout(onComplete, 500)
            return
        }

        const timer = setTimeout(() => {
            setCount(count - 1)
        }, 1000)

        return () => clearTimeout(timer)
    }, [count, onComplete])

    if (count === 0) {
        return (
            <motion.div
                className="fixed inset-0 flex items-center justify-center bg-black/90 backdrop-blur-xl z-50"
                initial={{ opacity: 1 }}
                animate={{ opacity: 0 }}
                transition={{ duration: 0.5 }}
            >
                <motion.div
                    initial={{ scale: 0.5, opacity: 0 }}
                    animate={{ scale: [0.5, 1.2, 1], opacity: [0, 1, 0] }}
                    transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                    className="text-9xl font-black text-transparent bg-clip-text bg-gradient-to-r from-green-400 to-emerald-500"
                    style={{
                        filter: "drop-shadow(0 0 50px rgba(34, 211, 152, 0.8))"
                    }}
                >
                    GO!
                </motion.div>
            </motion.div>
        )
    }

    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black/90 backdrop-blur-xl z-50">
            {/* Background particles */}
            <ExamParticles type="ambient" />

            {/* Countdown number */}
            <motion.div
                key={count}
                initial={{ scale: 0.5, opacity: 0, rotate: -20 }}
                animate={{ scale: [0.5, 1.2, 1], opacity: [0, 1, 1], rotate: 0 }}
                exit={{ scale: 0.8, opacity: 0 }}
                transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                className="relative"
            >
                {/* Glow effect */}
                <div
                    className="absolute inset-0 blur-[100px]"
                    style={{
                        background: count === 3 ? "rgba(239, 68, 68, 0.6)" :
                                   count === 2 ? "rgba(245, 158, 11, 0.6)" :
                                   "rgba(34, 197, 94, 0.6)"
                    }}
                />

                {/* Number */}
                <motion.div
                    animate={{
                        textShadow: [
                            "0 0 30px rgba(255,255,255,0.5)",
                            "0 0 60px rgba(255,255,255,0.8)",
                            "0 0 30px rgba(255,255,255,0.5)"
                        ]
                    }}
                    transition={{ duration: 0.6, repeat: Infinity }}
                    className="text-[20rem] font-black text-transparent bg-clip-text"
                    style={{
                        background: count === 3 ? "linear-gradient(135deg, #ef4444, #dc2626)" :
                                   count === 2 ? "linear-gradient(135deg, #f59e0b, #d97706)" :
                                   "linear-gradient(135deg, #22c55e, #16a34a)",
                        WebkitBackgroundClip: "text",
                        backgroundClip: "text"
                    }}
                >
                    {count}
                </motion.div>

                {/* Ring animation */}
                <motion.div
                    className="absolute inset-0 rounded-full border-4"
                    style={{
                        borderColor: count === 3 ? "#ef4444" :
                                    count === 2 ? "#f59e0b" :
                                    "#22c55e"
                    }}
                    initial={{ scale: 0.8, opacity: 1 }}
                    animate={{ scale: 2.5, opacity: 0 }}
                    transition={{ duration: 1, ease: "easeOut" }}
                />
            </motion.div>

            {/* Bottom text */}
            <motion.p
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                className="absolute bottom-32 text-2xl font-semibold text-white/80"
            >
                {count === 3 ? "Förbered dig..." : count === 2 ? "Nästan redo..." : "Lycka till!"}
            </motion.p>
        </div>
    )
}
