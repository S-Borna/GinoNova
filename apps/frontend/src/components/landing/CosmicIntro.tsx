"use client"

/**
 * ============================================================================
 * 🌌 COSMIC INTRO — THE BIG BANG GENESIS 🌌
 * ============================================================================
 *
 * A mesmerizing intro animation that plays once when the landing page loads.
 * Premium GinoNova brand reveal with dramatic explosion effect.
 *
 * Sequence:
 * 1. Pure darkness with subtle pulse (0-0.5s)
 * 2. Central core ignites with cyan/purple energy (0.5-1.2s)
 * 3. Shockwave rings expand outward (1-2s)
 * 4. Energy beams radiate from center (1.5-2.5s)
 * 5. GinoNova logo reveal with epic tagline (2-3s)
 * 6. Graceful fade to landing page (3-4s)
 *
 * Tagline: "Engineer the Future" — AI • DevOps • MLOps • Cloud
 * Inspired by: Cutting-edge tech, Apple, luxury brand intros
 *
 * @phase MILESTONE-3.0-EPIC-RELAUNCH
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"

interface CosmicIntroProps {
    onComplete: () => void
    duration?: number // Total duration in seconds
}

export function CosmicIntro({ onComplete, duration = 4 }: CosmicIntroProps) {
    const [phase, setPhase] = React.useState<"ignite" | "expand" | "fade">("ignite")

    React.useEffect(() => {
        // Phase transitions - slightly longer for more dramatic effect
        const igniteTimer = setTimeout(() => setPhase("expand"), 1000)
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
                    {[...Array(10)].map((_, i) => (
                        <motion.div
                            key={`ring-${i}`}
                            className="absolute rounded-full"
                            style={{
                                border: `${1.5 + i * 0.4}px solid`,
                                borderColor: i % 3 === 0
                                    ? "rgba(139, 92, 246, 0.6)"  // Purple
                                    : i % 3 === 1
                                        ? "rgba(99, 102, 241, 0.5)"  // Indigo
                                        : "rgba(167, 139, 250, 0.4)", // Light purple
                            }}
                            initial={{
                                width: 0,
                                height: 0,
                                opacity: 0
                            }}
                            animate={{
                                width: [0, 200 + i * 200, 500 + i * 350],
                                height: [0, 200 + i * 200, 500 + i * 350],
                                opacity: [0, 0.9, 0],
                            }}
                            transition={{
                                duration: 2.8,
                                delay: 0.6 + i * 0.12,
                                ease: [0.16, 1, 0.3, 1],
                            }}
                        />
                    ))}

                    {/* Energy beams radiating outward */}
                    {[...Array(16)].map((_, i) => (
                        <motion.div
                            key={`beam-${i}`}
                            className="absolute origin-center"
                            style={{
                                width: "3px",
                                height: "0px",
                                background: `linear-gradient(to top, transparent, ${i % 4 === 0 ? "rgba(139, 92, 246, 0.8)" :
                                    i % 4 === 1 ? "rgba(99, 102, 241, 0.7)" :
                                        i % 4 === 2 ? "rgba(167, 139, 250, 0.6)" :
                                            "rgba(196, 181, 253, 0.5)"
                                    }, transparent)`,
                                transform: `rotate(${i * 22.5}deg)`,
                                transformOrigin: "center bottom",
                            }}
                            initial={{ height: 0, opacity: 0 }}
                            animate={{
                                height: ["0px", "800px", "1500px"],
                                opacity: [0, 1, 0],
                            }}
                            transition={{
                                duration: 2.2,
                                delay: 0.9 + i * 0.04,
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

                    {/* Central core - outer glow - PURPLE/VIOLET */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(139, 92, 246, 0.4) 0%, rgba(99, 102, 241, 0.25) 40%, transparent 70%)",
                            filter: "blur(50px)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 500, 700, 400],
                            height: [0, 500, 700, 400],
                            opacity: [0, 0.9, 1, 0.7],
                        }}
                        transition={{
                            duration: 2.8,
                            delay: 0.2,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Central core - mid glow - SOFT VIOLET */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(167, 139, 250, 0.5) 0%, rgba(139, 92, 246, 0.35) 50%, transparent 70%)",
                            filter: "blur(30px)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 250, 350, 180],
                            height: [0, 250, 350, 180],
                            opacity: [0, 1, 1, 0.8],
                        }}
                        transition={{
                            duration: 2.5,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Central core - inner bright - SOFT WHITE/PURPLE CENTER */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "radial-gradient(circle, rgba(255, 255, 255, 0.9) 0%, rgba(224, 231, 255, 0.85) 30%, rgba(167, 139, 250, 0.6) 60%, transparent 80%)",
                            boxShadow: "0 0 60px rgba(255, 255, 255, 0.6), 0 0 120px rgba(139, 92, 246, 0.5), 0 0 200px rgba(99, 102, 241, 0.4)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0, scale: 0 }}
                        animate={{
                            width: [0, 100, 150, 80],
                            height: [0, 100, 150, 80],
                            opacity: [0, 1, 1, 0.95],
                            scale: [0, 1.3, 1.1, 0.9],
                        }}
                        transition={{
                            duration: 2,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    />

                    {/* Pulsating core center - the ignition point */}
                    <motion.div
                        className="absolute rounded-full"
                        style={{
                            background: "linear-gradient(135deg, #fff 0%, #c4b5fd 50%, #8b5cf6 100%)",
                            boxShadow: "0 0 40px rgba(255, 255, 255, 0.7), 0 0 80px rgba(139, 92, 246, 0.8), 0 0 120px rgba(99, 102, 241, 0.6)",
                        }}
                        initial={{ width: 0, height: 0, opacity: 0 }}
                        animate={{
                            width: [0, 40, 60, 25],
                            height: [0, 40, 60, 25],
                            opacity: [0, 1, 1, 1],
                        }}
                        transition={{
                            duration: 1.8,
                            delay: 0.3,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    >
                        {/* Inner pulse - breathing effect */}
                        <motion.div
                            className="absolute inset-0 rounded-full bg-white"
                            animate={{
                                scale: [1, 1.8, 1],
                                opacity: [1, 0.3, 1],
                            }}
                            transition={{
                                duration: 0.6,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        />
                    </motion.div>

                    {/* Particle dust explosion - purple/violet mix */}
                    {[...Array(60)].map((_, i) => {
                        const angle = (i / 60) * Math.PI * 2
                        const distance = 350 + Math.random() * 600
                        const size = 2 + Math.random() * 5
                        const colors = [
                            "rgba(139, 92, 246, 0.9)",   // Purple
                            "rgba(167, 139, 250, 0.85)", // Light purple
                            "rgba(99, 102, 241, 0.8)",   // Indigo
                            "rgba(224, 231, 255, 0.9)",  // Soft white
                            "rgba(196, 181, 253, 0.85)", // Lavender
                        ]

                        return (
                            <motion.div
                                key={`particle-${i}`}
                                className="absolute rounded-full"
                                style={{
                                    width: size,
                                    height: size,
                                    background: colors[i % colors.length],
                                    boxShadow: `0 0 ${size * 3}px ${colors[i % colors.length]}`,
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
                                    scale: [0, 2, 0],
                                }}
                                transition={{
                                    duration: 2.5,
                                    delay: 0.9 + Math.random() * 0.6,
                                    ease: [0.16, 1, 0.3, 1],
                                }}
                            />
                        )
                    })}

                    {/* Stardust particles - slower, ambient - purple dust */}
                    {[...Array(30)].map((_, i) => {
                        const angle = Math.random() * Math.PI * 2
                        const distance = 100 + Math.random() * 700

                        return (
                            <motion.div
                                key={`stardust-${i}`}
                                className="absolute w-1 h-1 rounded-full"
                                style={{
                                    background: i % 2 === 0 ? "#a78bfa" : "#e0e7ff",
                                    boxShadow: i % 2 === 0
                                        ? "0 0 8px rgba(167, 139, 250, 0.8)"
                                        : "0 0 6px rgba(224, 231, 255, 0.7)",
                                }}
                                initial={{
                                    x: Math.cos(angle) * (distance * 0.3),
                                    y: Math.sin(angle) * (distance * 0.3),
                                    opacity: 0,
                                }}
                                animate={{
                                    x: Math.cos(angle) * distance,
                                    y: Math.sin(angle) * distance,
                                    opacity: [0, 0.9, 0],
                                }}
                                transition={{
                                    duration: 3.5,
                                    delay: 0.6 + i * 0.08,
                                    ease: "easeOut",
                                }}
                            />
                        )
                    })}

                    {/* ===== GINONIVO LOGO REVEAL ===== */}
                    <motion.div
                        className="absolute flex flex-col items-center gap-2"
                        initial={{ opacity: 0, scale: 0.5, y: 80 }}
                        animate={{
                            opacity: [0, 0, 1, 1, 0],
                            scale: [0.5, 0.5, 1.1, 1, 0.95],
                            y: [80, 80, 0, 0, -10],
                        }}
                        transition={{
                            duration: 3.5,
                            delay: 0.6,
                            times: [0, 0.25, 0.45, 0.85, 1],
                            ease: [0.16, 1, 0.3, 1],
                        }}
                    >
                        {/* Main Logo Text */}
                        <motion.div
                            className="relative"
                            animate={{
                                textShadow: [
                                    "0 0 15px rgba(139, 92, 246, 0.4)",
                                    "0 0 30px rgba(139, 92, 246, 0.6)",
                                    "0 0 15px rgba(139, 92, 246, 0.4)",
                                ]
                            }}
                            transition={{
                                duration: 2,
                                repeat: Infinity,
                                ease: "easeInOut",
                            }}
                        >
                            <span
                                className="text-6xl md:text-7xl font-black tracking-tight"
                                style={{
                                    background: "linear-gradient(135deg, #e0e7ff 0%, #a78bfa 30%, #8b5cf6 50%, #a78bfa 70%, #e0e7ff 100%)",
                                    backgroundClip: "text",
                                    WebkitBackgroundClip: "text",
                                    color: "transparent",
                                    filter: "drop-shadow(0 0 25px rgba(139, 92, 246, 0.7)) drop-shadow(0 0 50px rgba(124, 58, 237, 0.4))",
                                }}
                            >
                                GinoNova
                            </span>
                        </motion.div>

                        {/* Epic tagline */}
                        <motion.div
                            className="flex flex-col items-center gap-1"
                            initial={{ opacity: 0, y: 10 }}
                            animate={{
                                opacity: [0, 0, 1, 1, 0],
                                y: [10, 10, 0, 0, -5],
                            }}
                            transition={{
                                duration: 3.5,
                                delay: 0.8,
                                times: [0, 0.3, 0.5, 0.85, 1],
                                ease: "easeOut",
                            }}
                        >
                            <span
                                className="text-base md:text-lg font-bold tracking-[0.25em] uppercase"
                                style={{
                                    background: "linear-gradient(90deg, #06b6d4 0%, #8b5cf6 50%, #ec4899 100%)",
                                    backgroundClip: "text",
                                    WebkitBackgroundClip: "text",
                                    color: "transparent",
                                    textShadow: "0 0 20px rgba(139, 92, 246, 0.5)",
                                    filter: "drop-shadow(0 0 15px rgba(139, 92, 246, 0.4))",
                                }}
                            >
                                Engineer the Future
                            </span>
                            <span
                                className="text-xs md:text-sm font-medium tracking-[0.35em] uppercase"
                                style={{
                                    color: "rgba(167, 139, 250, 0.7)",
                                    textShadow: "0 0 10px rgba(139, 92, 246, 0.3)",
                                }}
                            >
                                AI • DevOps • MLOps • Cloud
                            </span>
                        </motion.div>
                    </motion.div>
                </motion.div>
            ) : null}
        </AnimatePresence>
    )
}

export default CosmicIntro
