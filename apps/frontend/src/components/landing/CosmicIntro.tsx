"use client"

import * as React from "react"
import { motion } from "framer-motion"

const TECH_LOGOS = [
    { name: "docker", color: "2496ED" },
    { name: "kubernetes", color: "326CE5" },
    { name: "linux", color: "FCC624" },
    { name: "python", color: "3776AB" },
    { name: "amazonaws", color: "FF9900" },
    { name: "terraform", color: "7B42BC" },
    { name: "ansible", color: "EE0000" },
    { name: "git", color: "F05032" },
    { name: "github", color: "ffffff" },
    { name: "gitlab", color: "FC6D26" },
    { name: "nginx", color: "009639" },
    { name: "postgresql", color: "4169E1" },
    { name: "redis", color: "DC382D" },
    { name: "prometheus", color: "E6522C" },
    { name: "grafana", color: "F46800" },
    { name: "jenkins", color: "D24939" },
]

interface CosmicIntroProps {
    onComplete: () => void
    duration?: number
}

export default function CosmicIntro({ onComplete, duration = 5 }: CosmicIntroProps) {
    const [phase, setPhase] = React.useState<"float" | "approach" | "devour" | "fadeout">("float")

    React.useEffect(() => {
        const t1 = setTimeout(() => setPhase("approach"), 800)
        const t2 = setTimeout(() => setPhase("devour"), 2200)
        // Start fadeout early and call onComplete to load landing underneath
        const t3 = setTimeout(() => {
            setPhase("fadeout")
            onComplete() // Landing page starts loading NOW (underneath)
        }, duration * 1000 - 1200)

        return () => {
            clearTimeout(t1)
            clearTimeout(t2)
            clearTimeout(t3)
        }
    }, [duration, onComplete])

    return (
        <motion.div
            className="fixed inset-0 z-[9999] flex items-center justify-center overflow-hidden"
            initial={{ opacity: 1 }}
            animate={{ 
                opacity: phase === "fadeout" ? 0 : 1,
                scale: phase === "fadeout" ? 1.5 : 1,
            }}
            transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
            style={{ pointerEvents: phase === "fadeout" ? "none" : "auto" }}
        >
            <div
                className="absolute inset-0"
                style={{
                    background: "radial-gradient(ellipse at center, #0a0a20 0%, #050510 50%, #000 100%)"
                }}
            />

            {TECH_LOGOS.map((logo, i) => {
                const angle = (i / TECH_LOGOS.length) * Math.PI * 2
                const radius = 250 + (i % 3) * 80
                const x = Math.cos(angle) * radius
                const y = Math.sin(angle) * radius

                return (
                    <motion.img
                        key={logo.name}
                        src={`https://cdn.simpleicons.org/${logo.name}/${logo.color}`}
                        alt={logo.name}
                        className="absolute w-8 h-8 md:w-10 md:h-10"
                        style={{
                            left: "50%",
                            top: "50%",
                            filter: `drop-shadow(0 0 8px #${logo.color})`
                        }}
                        initial={{ x, y, scale: 0, opacity: 0 }}
                        animate={{
                            x: phase === "devour" ? 0 : x,
                            y: phase === "devour" ? 0 : y,
                            scale: phase === "devour" ? 0 : 1,
                            opacity: phase === "devour" ? 0 : 1,
                            rotate: phase === "devour" ? 360 : 0,
                        }}
                        transition={{
                            duration: phase === "devour" ? 0.8 : 0.6,
                            delay: phase === "float" ? i * 0.05 : i * 0.03,
                            ease: "easeOut",
                        }}
                    />
                )
            })}

            {phase !== "float" && [...Array(24)].map((_, i) => {
                const angle = (i / 24) * Math.PI * 2
                return (
                    <motion.div
                        key={`streak-${i}`}
                        className="absolute"
                        style={{
                            width: 2,
                            height: 120,
                            background: `linear-gradient(transparent, ${i % 2 === 0 ? "#8b5cf6" : "#6366f1"}, transparent)`,
                            left: "50%",
                            top: "50%",
                            transformOrigin: "center bottom",
                            transform: `rotate(${angle}rad)`,
                        }}
                        initial={{ scaleY: 0, opacity: 0 }}
                        animate={{ scaleY: [0, 3, 0], opacity: [0, 0.8, 0], y: [-600, 0] }}
                        transition={{
                            duration: 1.2,
                            delay: (i % 4) * 0.1,
                            repeat: Infinity,
                        }}
                    />
                )
            })}

            <motion.div
                className="absolute flex flex-col items-center gap-4 z-20"
                initial={{ scale: 0.05, opacity: 0 }}
                animate={{
                    scale: phase === "float" ? 0.05 : phase === "approach" ? 0.6 : 1,
                    opacity: phase === "float" ? 0 : 1,
                }}
                transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
            >
                <motion.div
                    className="absolute w-64 h-64 rounded-full"
                    style={{
                        background: "conic-gradient(from 0deg, #8b5cf680, #6366f180, #a78bfa80, #8b5cf680)",
                        filter: "blur(40px)",
                    }}
                    animate={{ rotate: 360 }}
                    transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                />

                <motion.div
                    className="absolute w-20 h-20 rounded-full bg-black"
                    style={{ boxShadow: "0 0 60px 20px rgba(0,0,0,0.9)" }}
                    animate={{ scale: phase === "devour" ? [1, 1.5, 1] : 1 }}
                    transition={{ duration: 0.8 }}
                />

                <span
                    className="relative z-10 text-5xl md:text-7xl font-black"
                    style={{
                        background: "linear-gradient(135deg, #e0e7ff, #a78bfa, #8b5cf6)",
                        backgroundClip: "text",
                        WebkitBackgroundClip: "text",
                        color: "transparent",
                        filter: "drop-shadow(0 0 30px #8b5cf6)",
                    }}
                >
                    GinoNova
                </span>

                <motion.div
                    className="flex flex-col items-center gap-1"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{
                        opacity: phase === "approach" || phase === "devour" ? 1 : 0,
                        y: 0
                    }}
                    transition={{ delay: 0.3 }}
                >
                    <span
                        className="text-lg font-bold tracking-[0.2em] uppercase"
                        style={{
                            background: "linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899)",
                            backgroundClip: "text",
                            WebkitBackgroundClip: "text",
                            color: "transparent",
                        }}
                    >
                        Engineer the Future
                    </span>
                    <span className="text-sm text-purple-300/80 tracking-[0.3em] uppercase">
                        AI • DevOps • MLOps • Cloud
                    </span>
                </motion.div>
            </motion.div>
        </motion.div>
    )
}

