"use client"

/**
 * ============================================================================
 * 🌌 COSMIC INTRO — THE BIG BANG GENESIS 🌌
 * ============================================================================
 *
 * A mesmerizing intro animation that plays once when the landing page loads.
 *
 * Sequence:
 * 1. Pure darkness (0-0.3s)
 * 2. Central core ignites with pulsating energy (0.3-1s)
 * 3. Light rings expand outward like planetary rings (1-2s)
 * 4. Energy beams radiate from center (1.5-2.5s)
 * 5. Graceful fade to landing page (2.5-3.5s)
 *
 * Inspired by: Bose, Apple, luxury brand intros
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"

interface CosmicIntroProps {
    onComplete: () => void
    duration?: number // Total duration in seconds
}

export function CosmicIntro({ onComplete, duration = 3.5 }: CosmicIntroProps) {
    const [phase, setPhase] = React.useState<"ignite" | "expand" | "fade">("ignite")

    React.useEffect(() => {
        // Phase transitions
        const igniteTimer = setTimeout(() => setPhase("expand"), 800)
        const fadeTimer = setTimeout(() => setPhase("fade"), duration * 1000 - 1000)
        const completeTimer = setTimeout(onComplete, duration * 1000)

        return () => {
            clearTimeout(igniteTimer)
            clearTimeout(fadeTimer)
            clearTimeout(completeTimer)
        }
    }, [duration, onComplete])

    return (
        <AnimatePresence>
            {phase !== "fade" ? (
                <motion.div
                    className="fixed inset-0 z-[9999] flex items-center justify-center overflow-hidden"
                    style={{ backgroundColor: "#020203" }}
                    initial={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 1, ease: [0.16, 1, 0.3, 1] }}
                >
                    {/* Deep space background gradient */}
                    <div
                        className="absolute inset-0"
                        style={{
                            background: "radial-gradient(ellipse at center, #0a0a12 0%, #050508 40%, #020203 100%)"
                        }}
                    />

                    {/* Expanding ring waves - outer to inner stagger */}
                    {[...Array(8)].map((_, i) => (
                        <motion.div
                            key={`ring-${i}`}
                            className="absolute rounded-full"
                            style={{
                                border: `${1 + i * 0.3}px solid`,
                                borderColor: i % 2 === 0
                                    ? "rgba(139, 92, 246, 0.6)"
                                    : "rgba(34, 211, 238, 0.4)",
                            }}
                            initial={{
                                width: 0,
                                height: 0,
                                opacity: 0
                            }}
                            animate={{
                                width: [0, 200 + i * 180, 400 + i * 300],
                                height: [0, 200 + i * 180, 400 + i * 300],
                                opacity: [0, 0.8, 0],
                            }}
                            transition={{
                                duration: 2.5,
                                delay: 0.5 + i * 0.15,
                                ease: [0.16, 1, 0.3, 1],
                            }}
                        />
                    ))}

                    {/* Energy beams radiating outward */}
                    {[...Array(12)].map((_, i) => (
                        <motion.div
                            key={`beam-${i}`}
                            className="absolute origin-center"
                            style={{
                                width: "2px",
                                height: "0px",
                                background: `linear-gradient(to top, transparent, ${i % 3 === 0 ? "rgba(168, 85, 247, 0.8)" :
                                        i % 3 === 1 ? "rgba(34, 211, 238, 0.7)" :
                                            "rgba(236, 72, 153, 0.6)"
                                    }, transparent)`,
                                transform: `rotate(${i * 30}deg)`,
                                transformOrigin: "center bottom",
                            }}
                            initial={{ height: 0, opacity: 0 }}
                            animate={{
                                height: ["0px", "600px", "1200px"],
                                opacity: [0, 1, 0],
                            }}
                            transition={{
                                duration: 2,
                                delay: 0.8 + i * 0.05,
                                ease: [0.16, 1, 0.3, 1],
                            }}
                        />
                    ))}

                    {/* Secondary thin beams */}
                    {[...Array(24)].map((_, i) => (
                        <motion.div
                            key={`thin-beam-${i}`}
                            className="absolute"
                            style={{
                                width: "1px",
                                height: "0px",
                                background: `linear-gradient(to top, transparent, rgba(255, 255, 255, 0.3), transparent)`,
                                transform: `rotate(${i * 15}deg)`,
                                transformOrigin: "center bottom",
                            }}
                            initial={{ height: 0, opacity: 0 }}
                            animate={{
                                height: ["0px", "400px", "800px"],
                                opacity: [0, 0.6, 0],
                            }}
                            transition={{
                                duration: 1.8,
                                delay: 1 + i * 0.03,
                                ease: "easeOut",
                            }}
                        />
                    ))}

                    {/* Central core - outer glow */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(139, 92, 246, 0.4) 0%, rgba(168, 85, 247, 0.2) 40%, transparent 70%)",
                            filter: "blur(40px)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 400, 600, 300],
                            height: [0, 400, 600, 300],
                            opacity: [0, 0.8, 1, 0.6],
                        }}
                        transition={{
                            duration: 2.5,
                            delay: 0.2,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Central core - mid glow */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(34, 211, 238, 0.5) 0%, rgba(99, 102, 241, 0.3) 50%, transparent 70%)",
                            filter: "blur(25px)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 200, 300, 150],
                            height: [0, 200, 300, 150],
                            opacity: [0, 1, 1, 0.7],
                        }}
                        transition={{
                            duration: 2.2,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Central core - inner bright */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(200, 180, 255, 0.9) 30%, rgba(139, 92, 246, 0.6) 60%, transparent 80%)",
                            boxShadow: "0 0 60px rgba(255, 255, 255, 0.8), 0 0 120px rgba(139, 92, 246, 0.6), 0 0 200px rgba(168, 85, 247, 0.4)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0, scale: 0 }}
                        animate={{
                            width: [0, 80, 120, 60],
                            height: [0, 80, 120, 60],
                            opacity: [0, 1, 1, 0.9],
                            scale: [0, 1.2, 1, 0.8],
                        }}
                        transition={{
                            duration: 2,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Pulsating core center - the ignition point */}
                    <motion.div
                        className="absolute rounded-full bg-white"
                        style={{
                            boxShadow: "0 0 40px #fff, 0 0 80px rgba(168, 85, 247, 1), 0 0 120px rgba(139, 92, 246, 0.8)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 30, 50, 20],
                            height: [0, 30, 50, 20],
                            opacity: [0, 1, 1, 1],
                        }}
                        transition={{
                            duration: 1.5,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    >
                        {/* Inner pulse */}
                        <motion.div
                            className="absolute inset-0 rounded-full bg-white"
                            animate={{
                                scale: [1, 1.5, 1],
                                opacity: [1, 0.5, 1],
                            }}
                            transition={{
                                duration: 0.8,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        />
                    </motion.div>

                    {/* Particle dust explosion */}
                    {[...Array(40)].map((_, i) => {
                        const angle = (i / 40) * Math.PI * 2
                        const distance = 300 + Math.random() * 500
                        const size = 2 + Math.random() * 4
                        const colors = [
                            "rgba(168, 85, 247, 0.9)",
                            "rgba(34, 211, 238, 0.8)",
                            "rgba(236, 72, 153, 0.7)",
                            "rgba(255, 255, 255, 0.9)",
                        ]

                        return (
                            <motion.div
                                key={`particle-${i}`}
                                className="absolute rounded-full"
                                style={{
                                    width: size,
                                    height: size,
                                    background: colors[i % colors.length],
                                    boxShadow: `0 0 ${size * 2}px ${colors[i % colors.length]}`,
                                }}
                                initial={{
                                    x: 0,
                                    y: 0,
                                    opacity: 0,
                                    scale: 0,
                                }}
                                animate={{
                                    x: Math.cos(angle) * distance,
                                    y: Math.sin(angle) * distance,
                                    opacity: [0, 1, 0],
                                    scale: [0, 1.5, 0],
                                }}
                                transition={{
                                    duration: 2,
                                    delay: 0.8 + Math.random() * 0.5,
                                    ease: [0.16, 1, 0.3, 1],
                                }}
                            />
                        )
                    })}

                    {/* Stardust particles - slower, ambient */}
                    {[...Array(20)].map((_, i) => {
                        const angle = Math.random() * Math.PI * 2
                        const distance = 100 + Math.random() * 600

                        return (
                            <motion.div
                                key={`stardust-${i}`}
                                className="absolute w-1 h-1 rounded-full bg-white"
                                style={{
                                    boxShadow: "0 0 6px rgba(255, 255, 255, 0.8)",
                                }}
                                initial={{
                                    x: Math.cos(angle) * (distance * 0.3),
                                    y: Math.sin(angle) * (distance * 0.3),
                                    opacity: 0,
                                }}
                                animate={{
                                    x: Math.cos(angle) * distance,
                                    y: Math.sin(angle) * distance,
                                    opacity: [0, 0.8, 0],
                                }}
                                transition={{
                                    duration: 3,
                                    delay: 0.5 + i * 0.1,
                                    ease: "easeOut",
                                }}
                            />
                        )
                    })}

                    {/* Logo/brand reveal - optional DevOpsHub text */}
                    <motion.div
                        className="absolute flex items-center gap-3"
                        initial={{ opacity: 0, scale: 0.8, y: 100 }}
                        animate={{
                            opacity: [0, 0, 1, 1, 0],
                            scale: [0.8, 0.8, 1, 1, 0.9],
                            y: [100, 100, 0, 0, -20],
                        }}
                        transition={{
                            duration: 3,
                            delay: 0.5,
                            times: [0, 0.3, 0.5, 0.8, 1],
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    >
                        <span className="text-4xl font-black tracking-tight">
                            <span className="text-white">DevOps</span>
                            <span
                                className="bg-gradient-to-r from-purple-400 via-violet-400 to-cyan-400 bg-clip-text text-transparent"
                                style={{ filter: "drop-shadow(0 0 20px rgba(139, 92, 246, 0.8))" }}
                            >
                                Hub
                            </span>
                        </span>
                    </motion.div>
                </motion.div>
            ) : null}
        </AnimatePresence>
    )
}

export default CosmicIntro
