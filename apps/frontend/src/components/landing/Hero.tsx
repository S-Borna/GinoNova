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
    Play,
    Sparkles,
    Clock,
    BookOpen,
    Target,
    Zap,
    Brain,
    Rocket,
    Gift,
    Users,
    Star,
    CheckCircle2,
    Globe,
    Shield,
    Infinity as InfinityIcon,
} from "lucide-react"

/* ============================================================================
   🌌 COSMIC AURORA BACKGROUND — DEEP SPACE EDITION
   ============================================================================ */

function CosmicBackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* Deep space base - even darker than before */}
            <div
                className="absolute inset-0"
                style={{
                    background: 'radial-gradient(ellipse 150% 100% at 50% 0%, #0a0a12 0%, #05050a 50%, #020203 100%)'
                }}
            />

            {/* Central cosmic core - massive pulsating energy */}
            <motion.div
                className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{
                    width: "1200px",
                    height: "1200px",
                    background: "radial-gradient(circle, rgba(139,92,246,0.4) 0%, rgba(168,85,247,0.2) 25%, rgba(99,102,241,0.1) 50%, transparent 70%)",
                    filter: "blur(80px)",
                }}
                animate={{
                    scale: [1, 1.3, 1],
                    opacity: [0.4, 0.7, 0.4],
                }}
                transition={{
                    duration: 6,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Aurora wave 1 - Purple majesty */}
            <motion.div
                className="absolute top-0 -left-1/4 w-[1000px] h-[800px] rounded-full"
                style={{
                    background: "conic-gradient(from 0deg, rgba(168,85,247,0.5), rgba(139,92,246,0.3), rgba(99,102,241,0.2), transparent, rgba(168,85,247,0.5))",
                    filter: "blur(100px)",
                }}
                animate={{
                    rotate: [0, 360],
                    x: [0, 100, 0],
                }}
                transition={{
                    rotate: { duration: 40, repeat: Infinity, ease: "linear" },
                    x: { duration: 15, repeat: Infinity, ease: "easeInOut" },
                }}
            />

            {/* Aurora wave 2 - Cyan whispers */}
            <motion.div
                className="absolute -bottom-1/4 -right-1/4 w-[900px] h-[900px] rounded-full"
                style={{
                    background: "conic-gradient(from 180deg, rgba(34,211,238,0.3), rgba(6,182,212,0.2), rgba(99,102,241,0.15), transparent, rgba(34,211,238,0.3))",
                    filter: "blur(90px)",
                }}
                animate={{
                    rotate: [360, 0],
                    y: [0, -80, 0],
                }}
                transition={{
                    rotate: { duration: 35, repeat: Infinity, ease: "linear" },
                    y: { duration: 12, repeat: Infinity, ease: "easeInOut" },
                }}
            />

            {/* Aurora wave 3 - Pink magic */}
            <motion.div
                className="absolute top-1/4 right-0 w-[600px] h-[600px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(236,72,153,0.25) 0%, rgba(168,85,247,0.15) 50%, transparent 70%)",
                    filter: "blur(70px)",
                }}
                animate={{
                    x: [0, -50, 0],
                    y: [0, 50, 0],
                    scale: [1, 1.2, 1],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Neural network pulse rings - consciousness expanding */}
            {[...Array(5)].map((_, i) => (
                <motion.div
                    key={i}
                    className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full"
                    style={{
                        width: `${300 + i * 150}px`,
                        height: `${300 + i * 150}px`,
                        border: '1px solid',
                        borderColor: `rgba(139, 92, 246, ${0.3 - i * 0.05})`,
                    }}
                    animate={{
                        scale: [1, 2, 1],
                        opacity: [0.5, 0, 0.5],
                    }}
                    transition={{
                        duration: 5,
                        repeat: Infinity,
                        delay: i * 1,
                        ease: "easeOut",
                    }}
                />
            ))}

            {/* Holographic circuit grid */}
            <div
                className="absolute inset-0 opacity-[0.025]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139,92,246,0.8) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139,92,246,0.8) 1px, transparent 1px),
                        linear-gradient(rgba(34,211,238,0.4) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(34,211,238,0.4) 1px, transparent 1px)
                    `,
                    backgroundSize: "120px 120px, 120px 120px, 24px 24px, 24px 24px",
                }}
            />

            {/* Vertical scanning beam - AI awareness */}
            <motion.div
                className="absolute inset-y-0 w-[400px] bg-gradient-to-r from-transparent via-purple-500/10 to-transparent"
                animate={{
                    x: ["-100%", "calc(100vw + 100%)"],
                }}
                transition={{
                    duration: 12,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            {/* Horizontal scan line */}
            <motion.div
                className="absolute inset-x-0 h-[2px] bg-gradient-to-r from-transparent via-cyan-400/40 to-transparent"
                animate={{
                    top: ["-5%", "105%"],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "linear",
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
    const particles = React.useMemo(() =>
        Array.from({ length: 50 }, (_, i) => ({
            id: i,
            size: Math.random() * 4 + 1,
            x: Math.random() * 100,
            y: Math.random() * 100,
            duration: Math.random() * 20 + 15,
            delay: Math.random() * 8,
            color: i % 4 === 0 ? "purple" : i % 4 === 1 ? "cyan" : i % 4 === 2 ? "pink" : "white",
        })), [])

    const colorMap = {
        purple: "bg-purple-400 shadow-[0_0_15px_rgba(168,85,247,1)]",
        cyan: "bg-cyan-400 shadow-[0_0_15px_rgba(34,211,238,1)]",
        pink: "bg-pink-400 shadow-[0_0_15px_rgba(236,72,153,1)]",
        white: "bg-white shadow-[0_0_10px_rgba(255,255,255,0.8)]",
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
                        y: [0, -200, 0],
                        x: [0, Math.random() * 60 - 30, 0],
                        opacity: [0, 1, 0],
                        scale: [0.3, 1.5, 0.3],
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
            initial={{ opacity: 0, y: 30, scale: 0.8 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
            className="inline-flex mb-8"
        >
            <motion.div
                className={cn(
                    "relative flex items-center gap-3 px-6 py-3 rounded-full",
                    "bg-gradient-to-r from-emerald-500/20 via-green-500/15 to-emerald-500/20",
                    "border-2 border-emerald-400/50",
                    "backdrop-blur-xl",
                )}
                animate={{
                    boxShadow: [
                        "0 0 20px rgba(52,211,153,0.3), 0 0 40px rgba(52,211,153,0.1)",
                        "0 0 30px rgba(52,211,153,0.5), 0 0 60px rgba(52,211,153,0.2)",
                        "0 0 20px rgba(52,211,153,0.3), 0 0 40px rgba(52,211,153,0.1)",
                    ],
                }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                {/* Animated glow ring */}
                <motion.div
                    className="absolute inset-0 rounded-full"
                    style={{
                        background: "linear-gradient(90deg, rgba(52,211,153,0.4), rgba(16,185,129,0.2), rgba(52,211,153,0.4))",
                        backgroundSize: "200% 100%",
                    }}
                    animate={{
                        backgroundPosition: ["0% 0%", "200% 0%"],
                    }}
                    transition={{
                        duration: 2,
                        repeat: Infinity,
                        ease: "linear",
                    }}
                />

                <motion.div
                    animate={{ rotate: [0, 15, -15, 0] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    className="relative"
                >
                    <Gift className="w-5 h-5 text-emerald-400" />
                </motion.div>

                <div className="relative flex items-center gap-2">
                    <span className="text-lg font-black bg-gradient-to-r from-emerald-300 via-green-300 to-emerald-300 bg-clip-text text-transparent">
                        100% GRATIS
                    </span>
                    <span className="text-emerald-300/80 font-medium">•</span>
                    <span className="text-emerald-200/90 font-medium">
                        Ingen registrering krävs
                    </span>
                </div>

                <motion.div
                    animate={{ scale: [1, 1.2, 1] }}
                    transition={{ duration: 1.5, repeat: Infinity }}
                >
                    <Sparkles className="w-5 h-5 text-yellow-400" />
                </motion.div>
            </motion.div>
        </motion.div>
    )
}

/* ============================================================================
   🧠 AI INTELLIGENCE INDICATOR
   ============================================================================ */

function AIIndicator() {
    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3, duration: 0.6 }}
            className="flex items-center justify-center gap-2 mb-6"
        >
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-4 py-2 rounded-full",
                    "bg-gradient-to-r from-purple-500/20 via-violet-500/15 to-indigo-500/20",
                    "border border-purple-500/40",
                    "backdrop-blur-sm"
                )}
                animate={{
                    boxShadow: [
                        "0 0 15px rgba(139,92,246,0.3)",
                        "0 0 30px rgba(139,92,246,0.5)",
                        "0 0 15px rgba(139,92,246,0.3)",
                    ]
                }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                <motion.div
                    animate={{ rotate: 360 }}
                    transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
                >
                    <Brain className="w-4 h-4 text-purple-400" />
                </motion.div>
                <span className="text-sm font-semibold bg-gradient-to-r from-purple-300 to-violet-300 bg-clip-text text-transparent">
                    AI-Driven Personalisering
                </span>
                <motion.div
                    animate={{ scale: [1, 1.3, 1], opacity: [0.5, 1, 0.5] }}
                    transition={{ duration: 1.5, repeat: Infinity }}
                >
                    <Zap className="w-4 h-4 text-amber-400" />
                </motion.div>
            </motion.div>
        </motion.div>
    )
}

/* ============================================================================
   🎯 HOLOGRAPHIC STAT CARD — PREMIUM VERSION
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    value: string
    label: string
    delay?: number
    gradient: string
    glowColor: string
}

function StatCard({ icon, value, label, delay = 0, gradient, glowColor }: StatCardProps) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 30, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.8 + delay, ease: [0.16, 1, 0.3, 1] }}
            whileHover={{ scale: 1.08, y: -8 }}
            className="relative group"
        >
            {/* Outer glow on hover */}
            <motion.div
                className="absolute -inset-2 rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-xl"
                style={{ background: glowColor }}
            />

            <div
                className={cn(
                    "relative flex items-center gap-4 px-6 py-5",
                    "bg-gradient-to-br from-white/[0.08] to-white/[0.02]",
                    "backdrop-blur-xl",
                    "border border-white/[0.15] group-hover:border-white/30",
                    "rounded-2xl",
                    "transition-all duration-500",
                    "overflow-hidden"
                )}
            >
                {/* Holographic shine */}
                <motion.div
                    className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700"
                    style={{
                        background: "linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.15) 45%, rgba(255,255,255,0.08) 50%, transparent 55%)",
                    }}
                    animate={{
                        x: ["-100%", "200%"],
                    }}
                    transition={{
                        duration: 1.5,
                        repeat: Infinity,
                        repeatDelay: 2,
                    }}
                />

                {/* Icon container */}
                <motion.div
                    className={cn(
                        "relative p-3 rounded-xl",
                        "bg-gradient-to-br",
                        gradient,
                        "group-hover:scale-110 transition-transform duration-300"
                    )}
                    whileHover={{ rotate: 5 }}
                >
                    {icon}
                </motion.div>

                <div className="relative">
                    <motion.div
                        className="text-3xl font-black text-white"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 1 + delay }}
                    >
                        {value}
                    </motion.div>
                    <div className="text-xs text-zinc-400 font-semibold uppercase tracking-wider">
                        {label}
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   ⭐ SOCIAL PROOF TICKER
   ============================================================================ */

function SocialProofTicker() {
    const proofs = [
        { icon: Users, text: "10,000+ aktiva användare" },
        { icon: Star, text: "4.9/5 betyg" },
        { icon: Globe, text: "Svenskt community" },
        { icon: Shield, text: "Ingen kreditkort krävs" },
        { icon: InfinityIcon, text: "Livstids tillgång" },
    ]

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2, duration: 0.8 }}
            className="flex flex-wrap items-center justify-center gap-6 mt-12 mb-8"
        >
            {proofs.map((proof, i) => (
                <motion.div
                    key={i}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 1.3 + i * 0.1 }}
                    className="flex items-center gap-2 text-sm text-zinc-400"
                >
                    <proof.icon className="w-4 h-4 text-purple-400" />
                    <span>{proof.text}</span>
                </motion.div>
            ))}
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
                        Sveriges{" "}
                        <span className="font-bold bg-gradient-to-r from-purple-400 to-violet-400 bg-clip-text text-transparent">
                            smartaste
                        </span>{" "}
                        läroplattform för DevOps.{" "}
                        <br className="hidden sm:block" />
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

                {/* CTA Buttons - PREMIUM STYLING */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.7 }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-5 mb-8"
                >
                    {/* Primary CTA - Start Learning */}
                    <Link href="/skillsmaps">
                        <motion.div
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.98 }}
                            className="relative group"
                        >
                            {/* Animated glow */}
                            <motion.div
                                className="absolute -inset-1 bg-gradient-to-r from-purple-600 via-violet-600 to-cyan-600 rounded-2xl blur-lg"
                                animate={{
                                    opacity: [0.6, 1, 0.6],
                                }}
                                transition={{ duration: 2, repeat: Infinity }}
                            />
                            <Button
                                size="xl"
                                className={cn(
                                    "relative gap-3 min-w-[280px] h-16 text-lg font-bold",
                                    "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                    "hover:from-purple-500 hover:via-violet-500 hover:to-indigo-500",
                                    "border-0 rounded-2xl",
                                    "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
                                    "transition-all duration-300"
                                )}
                            >
                                <Rocket className="w-5 h-5" />
                                Börja Lära — Gratis
                                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                            </Button>
                        </motion.div>
                    </Link>

                    {/* Secondary CTA - View Curriculum */}
                    <Link href="#curriculum">
                        <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.98 }}>
                            <Button
                                size="xl"
                                variant="outline"
                                className={cn(
                                    "gap-2 min-w-[200px] h-16 text-lg font-semibold",
                                    "bg-white/5 backdrop-blur-xl",
                                    "border-2 border-white/20 hover:border-white/40",
                                    "text-white hover:bg-white/10",
                                    "rounded-2xl",
                                    "transition-all duration-300"
                                )}
                            >
                                <Play className="w-5 h-5" />
                                Se Curriculum
                            </Button>
                        </motion.div>
                    </Link>
                </motion.div>

                {/* Social Proof */}
                <SocialProofTicker />

                {/* Stats row */}
                <motion.div
                    className="flex flex-wrap items-center justify-center gap-5"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 1 }}
                >
                    <StatCard
                        icon={<Clock className="w-6 h-6 text-white" />}
                        value="310+"
                        label="Timmar Content"
                        delay={0}
                        gradient="from-purple-500 to-violet-600"
                        glowColor="rgba(139,92,246,0.3)"
                    />
                    <StatCard
                        icon={<BookOpen className="w-6 h-6 text-white" />}
                        value="36"
                        label="Moduler"
                        delay={0.1}
                        gradient="from-cyan-500 to-blue-600"
                        glowColor="rgba(34,211,238,0.3)"
                    />
                    <StatCard
                        icon={<Target className="w-6 h-6 text-white" />}
                        value="4"
                        label="Karriärspår"
                        delay={0.2}
                        gradient="from-pink-500 to-rose-600"
                        glowColor="rgba(236,72,153,0.3)"
                    />
                    <StatCard
                        icon={<Brain className="w-6 h-6 text-white" />}
                        value="AI"
                        label="Assisterad"
                        delay={0.3}
                        gradient="from-amber-500 to-orange-600"
                        glowColor="rgba(251,191,36,0.3)"
                    />
                </motion.div>
            </div>

            {/* Scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 2, duration: 0.8 }}
                className="absolute bottom-8 left-1/2 -translate-x-1/2"
            >
                <motion.div
                    animate={{ y: [0, 12, 0] }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    className="relative w-8 h-14 rounded-full border-2 border-purple-500/40 flex items-start justify-center p-2"
                >
                    {/* Glow */}
                    <div className="absolute inset-0 rounded-full bg-purple-500/10 blur-lg" />
                    <motion.div
                        animate={{
                            opacity: [0.4, 1, 0.4],
                            y: [0, 16, 0]
                        }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        className="w-2 h-2 rounded-full bg-purple-400 shadow-[0_0_15px_rgba(168,85,247,1)]"
                    />
                </motion.div>
            </motion.div>
        </section>
    )
}

export default Hero
