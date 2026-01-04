"use client"

/**
 * ============================================================================
 * 🌌 HERO SECTION — COSMIC RELAUNCH EDITION 2025 🌌
 * ============================================================================
 *
 * THE MOST SPECTACULAR LANDING PAGE EVER CREATED
 *
 * Design Philosophy:
 * - Netflix: Cinematic dark elegance, immersive depth
 * - Apple: Breathing space, aspirational typography
 * - Stripe: Energetic gradients, technical sophistication
 * - OpenAI: Neural intelligence, pulsating consciousness
 * - Vercel: Holographic shimmer, premium edge
 * - Disney+: Magic particle systems, wonder
 *
 * Key Selling Points:
 * - 100% FREE - No registration required
 * - Instant access to all learning content
 * - AI-powered personalization
 * - Swedish DevOps community
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 * @target 100,000 daily active users
 */

import * as React from "react"
import Link from "next/link"
import { motion, useMotionValue, useTransform, useSpring, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    ArrowRight,
    Sparkles,
    Zap,
    Brain,
    Rocket,
    Gift,
    CheckCircle2,
} from "lucide-react"

/* ============================================================================
   🌌 COSMIC AURORA BACKGROUND — DEEP SPACE EDITION
   ============================================================================ */

function CosmicBackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* Deep space base */}
            <div
                className="absolute inset-0"
                style={{
                    background: 'radial-gradient(ellipse 150% 100% at 50% 0%, #0a0a12 0%, #05050a 50%, #020203 100%)'
                }}
            />

            {/* Central ambient glow - subtle, no animation */}
            <div
                className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{
                    width: "1000px",
                    height: "800px",
                    background: "radial-gradient(circle, rgba(139,92,246,0.25) 0%, rgba(168,85,247,0.1) 40%, transparent 70%)",
                    filter: "blur(80px)",
                }}
            />

            {/* Secondary glow - cyan accent */}
            <div
                className="absolute bottom-0 right-0 w-[600px] h-[400px]"
                style={{
                    background: "radial-gradient(circle, rgba(34,211,238,0.15) 0%, transparent 60%)",
                    filter: "blur(60px)",
                }}
            />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.02]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139,92,246,0.5) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139,92,246,0.5) 1px, transparent 1px)
                    `,
                    backgroundSize: "80px 80px",
                }}
            />

            {/* Bottom fade to content */}
            <div className="absolute bottom-0 left-0 right-0 h-64 bg-gradient-to-t from-[#05050a] via-[#05050a]/80 to-transparent" />
        </div>
    )
}

/* ============================================================================
   ✨ COSMIC PARTICLE SYSTEM — STARDUST
   ============================================================================ */

function StardustParticles() {
    // Reduced from 50 to 12 particles for better performance
    const particles = React.useMemo(() =>
        Array.from({ length: 12 }, (_, i) => ({
            id: i,
            size: Math.random() * 3 + 1,
            x: Math.random() * 100,
            y: Math.random() * 100,
            duration: Math.random() * 25 + 20,
            delay: Math.random() * 10,
            color: i % 3 === 0 ? "purple" : i % 3 === 1 ? "cyan" : "white",
        })), [])

    const colorMap = {
        purple: "bg-purple-400/80",
        cyan: "bg-cyan-400/80",
        white: "bg-white/60",
    }

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {particles.map((p) => (
                <motion.div
                    key={p.id}
                    className={cn("absolute rounded-full", colorMap[p.color as keyof typeof colorMap])}
                    style={{
                        width: p.size,
                        height: p.size,
                        left: `${p.x}%`,
                        top: `${p.y}%`,
                    }}
                    animate={{
                        y: [0, -150, 0],
                        opacity: [0, 0.8, 0],
                    }}
                    transition={{
                        duration: p.duration,
                        repeat: Infinity,
                        delay: p.delay,
                        ease: "easeInOut",
                    }}
                />
            ))}
        </div>
    )
}

/* ============================================================================
   🎁 FREE ACCESS BADGE — THE GAME CHANGER
   ============================================================================ */

function FreeAccessBadge() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="inline-flex mb-8"
        >
            <div
                className={cn(
                    "flex items-center gap-3 px-6 py-3 rounded-full",
                    "bg-emerald-500/15",
                    "border border-emerald-400/40",
                )}
            >
                <Gift className="w-5 h-5 text-emerald-400" />
                <span className="text-lg font-bold text-emerald-300">
                    100% GRATIS
                </span>
                <span className="text-emerald-300/60">•</span>
                <span className="text-emerald-200/80 font-medium">
                    Ingen registrering krävs
                </span>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   🧠 AI INTELLIGENCE INDICATOR
   ============================================================================ */

function AIIndicator() {
    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.5 }}
            className="flex items-center justify-center gap-2 mb-6"
        >
            <div
                className={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-full",
                    "bg-purple-500/15",
                    "border border-purple-500/30"
                )}
            >
                <Brain className="w-4 h-4 text-purple-400" />
                <span className="text-sm font-semibold text-purple-300">
                    AI-Driven Personalisering
                </span>
                <Zap className="w-4 h-4 text-amber-400" />
            </div>
        </motion.div>
    )
}



/* ============================================================================
   🚀 MAIN HERO COMPONENT — COSMIC RELAUNCH
   ============================================================================ */

export function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Background layers */}
            <CosmicBackground />
            <StardustParticles />

            {/* Content */}
            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center">

                {/* FREE ACCESS BADGE - The game changer */}
                <FreeAccessBadge />

                {/* AI Indicator */}
                <AIIndicator />

                {/* Main headline with cosmic glow */}
                <motion.div
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 1, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                    className="relative mb-8"
                >
                    {/* Glow behind text */}
                    <div className="absolute inset-0 -z-10 blur-[100px] opacity-50">
                        <div className="absolute inset-0 bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600" />
                    </div>

                    <h1 className="text-5xl sm:text-6xl md:text-7xl lg:text-8xl xl:text-9xl font-black tracking-tight leading-[0.9]">
                        <motion.span
                            className="block text-white"
                            style={{
                                textShadow: "0 0 80px rgba(255,255,255,0.3), 0 0 120px rgba(139,92,246,0.2)"
                            }}
                        >
                            Master DevOps
                        </motion.span>
                        <motion.span
                            className="relative block mt-2"
                            animate={{
                                backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                            }}
                            transition={{
                                duration: 6,
                                repeat: Infinity,
                                ease: "linear",
                            }}
                            style={{
                                background: "linear-gradient(90deg, #8B5CF6, #A855F7, #22D3EE, #EC4899, #8B5CF6)",
                                backgroundSize: "200% auto",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                filter: "drop-shadow(0 0 40px rgba(139,92,246,0.6))",
                            }}
                        >
                            Bygg Din Karriär
                        </motion.span>
                    </h1>
                </motion.div>

                {/* Subheadline with feature highlights */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.5 }}
                    className="max-w-4xl mx-auto mb-12"
                >
                    <p className="text-xl sm:text-2xl md:text-3xl text-zinc-300 leading-relaxed font-light">
                        <span className="text-white font-medium">Personliga lärstigar</span>,{" "}
                        <span className="font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
                            interaktiva labs
                        </span>{" "}
                        och{" "}
                        <span className="font-bold bg-gradient-to-r from-pink-400 to-rose-400 bg-clip-text text-transparent">
                            AI-driven feedback
                        </span>.
                    </p>

                    {/* Quick feature list */}
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.8 }}
                        className="flex flex-wrap items-center justify-center gap-x-6 gap-y-2 mt-6 text-sm text-zinc-400"
                    >
                        {[
                            "36 moduler",
                            "80+ hands-on labs",
                            "Riktiga projekt",
                            "Dallas AI-assistent",
                        ].map((item, i) => (
                            <motion.span
                                key={i}
                                initial={{ opacity: 0, x: -10 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ delay: 0.9 + i * 0.1 }}
                                className="flex items-center gap-2"
                            >
                                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                {item}
                            </motion.span>
                        ))}
                    </motion.div>
                </motion.div>

                {/* CTA Button */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.5 }}
                    className="flex items-center justify-center mb-8"
                >
                    <Link href="/skillsmaps">
                        <Button
                            size="xl"
                            className={cn(
                                "gap-3 min-w-[280px] h-16 text-lg font-bold",
                                "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                "hover:from-purple-500 hover:via-violet-500 hover:to-indigo-500",
                                "border-0 rounded-2xl",
                                "shadow-lg shadow-purple-500/25",
                                "transition-all duration-300 hover:scale-[1.02]"
                            )}
                        >
                            <Rocket className="w-5 h-5" />
                            Börja Lära — Gratis
                            <ArrowRight className="w-5 h-5" />
                        </Button>
                    </Link>
                </motion.div>
            </div>

            {/* Scroll indicator - simple version */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.5, duration: 0.6 }}
                className="absolute bottom-8 left-1/2 -translate-x-1/2"
            >
                <motion.div
                    animate={{ y: [0, 8, 0] }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    className="w-6 h-10 rounded-full border border-purple-500/30 flex items-start justify-center p-2"
                >
                    <motion.div
                        animate={{ y: [0, 12, 0], opacity: [0.5, 1, 0.5] }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        className="w-1.5 h-1.5 rounded-full bg-purple-400"
                    />
                </motion.div>
            </motion.div>
        </section>
    )
}

export default Hero
