"use client"

/**
 * ============================================================================
 * HERO SECTION — AI-POWERED PREMIUM LANDING EXPERIENCE
 * ============================================================================
 *
 * Design Philosophy:
 * - Apple: Clean, aspirational, breathing space
 * - Netflix: Dark elegance, immersive gradients
 * - Stripe: Energetic, technically sophisticated
 * - OpenAI: Neural glow, pulsating intelligence
 * - Vercel: Holographic shimmer, premium feel
 *
 * Features:
 * - Neural network animated background
 * - AI chip pulsating glow effects
 * - Holographic gradient text animations
 * - Dynamic particle system with connections
 * - Premium glassmorphism with AI accent
 * - Cinematic entrance animations
 *
 * @phase A.1 - Landing Page
 * @upgrade HERO GLOW-UP v2.0 - AI-Powered Intelligence
 */

import * as React from "react"
import Link from "next/link"
import { motion, useMotionValue, useTransform, useSpring } from "framer-motion"
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
    Cpu,
} from "lucide-react"

/* ============================================================================
   AI NEURAL NETWORK BACKGROUND
   ============================================================================ */

function NeuralBackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* MILESTONE 2.0: Cosmic deep space gradient */}
            <div className="absolute inset-0" style={{ background: 'linear-gradient(180deg, #05050a 0%, #0a0a12 50%, #0e0e18 100%)' }} />

            {/* AI Core Glow - Central pulsating orb - MORE PURPLE */}
            <motion.div
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[1000px]"
                style={{
                    background: "radial-gradient(circle, rgba(168,85,247,0.3) 0%, rgba(139,92,246,0.15) 30%, transparent 70%)",
                    filter: "blur(60px)",
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.5, 0.8, 0.5],
                }}
                transition={{
                    duration: 4,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Neural pulse rings - PURPLE themed */}
            {[...Array(3)].map((_, i) => (
                <motion.div
                    key={i}
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full"
                    style={{
                        width: `${400 + i * 200}px`,
                        height: `${400 + i * 200}px`,
                        border: '1px solid rgba(168, 85, 247, 0.2)',
                    }}
                    animate={{
                        scale: [1, 1.5, 1],
                        opacity: [0.4, 0, 0.4],
                    }}
                    transition={{
                        duration: 4,
                        repeat: Infinity,
                        delay: i * 1.3,
                        ease: "easeOut",
                    }}
                />
            ))}

            {/* Animated gradient orbs - STRONGER COLORS */}
            <motion.div
                className="absolute top-0 -left-1/4 w-[800px] h-[800px] rounded-full"
                style={{
                    background: "conic-gradient(from 0deg, rgba(168,85,247,0.4), rgba(139,92,246,0.3), rgba(6,182,212,0.2), rgba(168,85,247,0.4))",
                    filter: "blur(100px)",
                }}
                animate={{
                    rotate: [0, 360],
                    scale: [1, 1.1, 1],
                }}
                transition={{
                    rotate: { duration: 30, repeat: Infinity, ease: "linear" },
                    scale: { duration: 8, repeat: Infinity, ease: "easeInOut" },
                }}
            />
            <motion.div
                className="absolute -bottom-1/4 -right-1/4 w-[700px] h-[700px] rounded-full"
                style={{
                    background: "conic-gradient(from 180deg, rgba(236,72,153,0.3), rgba(168,85,247,0.4), rgba(99,102,241,0.3), rgba(236,72,153,0.3))",
                    filter: "blur(80px)",
                }}
                animate={{
                    rotate: [360, 0],
                    scale: [1, 1.15, 1],
                }}
                transition={{
                    rotate: { duration: 25, repeat: Infinity, ease: "linear" },
                    scale: { duration: 6, repeat: Infinity, ease: "easeInOut" },
                }}
            />

            {/* AI circuit grid */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(99,102,241,0.5) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(99,102,241,0.5) 1px, transparent 1px),
                        linear-gradient(rgba(139,92,246,0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139,92,246,0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: "100px 100px, 100px 100px, 20px 20px, 20px 20px",
                }}
            />

            {/* Scanning line effect */}
            <motion.div
                className="absolute inset-x-0 h-[2px] bg-gradient-to-r from-transparent via-primary-500/50 to-transparent"
                animate={{
                    top: ["-10%", "110%"],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "linear",
                }}
            />

            {/* Noise texture */}
            <div
                className="absolute inset-0 opacity-[0.02]"
                style={{
                    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
                }}
            />

            {/* Bottom fade with glow */}
            <div className="absolute bottom-0 left-0 right-0 h-48 bg-gradient-to-t from-black via-black/80 to-transparent" />
        </div>
    )
}

/* ============================================================================
   AI NEURAL PARTICLES WITH CONNECTIONS
   ============================================================================ */

function NeuralParticles() {
    const particles = React.useMemo(() =>
        Array.from({ length: 30 }, (_, i) => ({
            id: i,
            size: Math.random() * 4 + 2,
            x: Math.random() * 100,
            y: Math.random() * 100,
            duration: Math.random() * 15 + 15,
            delay: Math.random() * 5,
            glowColor: i % 3 === 0 ? "primary" : i % 3 === 1 ? "purple" : "cyan",
        })), [])

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {particles.map((particle) => (
                <motion.div
                    key={particle.id}
                    className={cn(
                        "absolute rounded-full",
                        particle.glowColor === "primary" && "bg-primary-400 shadow-[0_0_10px_rgba(99,102,241,0.8)]",
                        particle.glowColor === "purple" && "bg-purple-400 shadow-[0_0_10px_rgba(139,92,246,0.8)]",
                        particle.glowColor === "cyan" && "bg-cyan-400 shadow-[0_0_10px_rgba(6,182,212,0.8)]",
                    )}
                    style={{
                        width: particle.size,
                        height: particle.size,
                        left: `${particle.x}%`,
                        top: `${particle.y}%`,
                    }}
                    animate={{
                        y: [0, -150, 0],
                        x: [0, Math.random() * 50 - 25, 0],
                        opacity: [0, 0.8, 0],
                        scale: [0.5, 1.2, 0.5],
                    }}
                    transition={{
                        duration: particle.duration,
                        repeat: Infinity,
                        delay: particle.delay,
                        ease: "easeInOut",
                    }}
                />
            ))}
        </div>
    )
}

/* ============================================================================
   AI BADGE
   ============================================================================ */

function AIBadge() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.6 }}
            className="inline-flex items-center gap-2 mb-8"
        >
            <div className={cn(
                "relative flex items-center gap-2 px-4 py-2 rounded-full",
                "bg-gradient-to-r from-primary-500/10 via-purple-500/10 to-cyan-500/10",
                "border border-primary-500/30",
                "backdrop-blur-sm",
            )}>
                {/* Animated glow ring */}
                <motion.div
                    className="absolute inset-0 rounded-full"
                    style={{
                        background: "linear-gradient(90deg, rgba(99,102,241,0.3), rgba(139,92,246,0.3), rgba(6,182,212,0.3), rgba(99,102,241,0.3))",
                        backgroundSize: "300% 100%",
                    }}
                    animate={{
                        backgroundPosition: ["0% 0%", "100% 0%", "0% 0%"],
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "linear",
                    }}
                />
                <div className="relative flex items-center gap-2">
                    <motion.div
                        animate={{ rotate: 360 }}
                        transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
                    >
                        <Cpu className="w-4 h-4 text-primary-400" />
                    </motion.div>
                    <span className="text-sm font-medium bg-gradient-to-r from-primary-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                        AI-Powered Learning Platform
                    </span>
                    <motion.div
                        animate={{ scale: [1, 1.2, 1] }}
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        <Sparkles className="w-4 h-4 text-yellow-400" />
                    </motion.div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   HOLOGRAPHIC STATS CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    value: string
    label: string
    delay?: number
    accentColor?: "primary" | "purple" | "cyan" | "pink"
}

function StatCard({ icon, value, label, delay = 0, accentColor = "primary" }: StatCardProps) {
    const colorClasses = {
        primary: {
            glow: "shadow-primary-500/20 hover:shadow-primary-500/40",
            border: "border-primary-500/20 hover:border-primary-500/40",
            icon: "from-primary-500/30 to-purple-500/20 text-primary-400",
            accent: "bg-primary-500",
        },
        purple: {
            glow: "shadow-purple-500/20 hover:shadow-purple-500/40",
            border: "border-purple-500/20 hover:border-purple-500/40",
            icon: "from-purple-500/30 to-pink-500/20 text-purple-400",
            accent: "bg-purple-500",
        },
        cyan: {
            glow: "shadow-cyan-500/20 hover:shadow-cyan-500/40",
            border: "border-cyan-500/20 hover:border-cyan-500/40",
            icon: "from-cyan-500/30 to-blue-500/20 text-cyan-400",
            accent: "bg-cyan-500",
        },
        pink: {
            glow: "shadow-pink-500/20 hover:shadow-pink-500/40",
            border: "border-pink-500/20 hover:border-pink-500/40",
            icon: "from-pink-500/30 to-rose-500/20 text-pink-400",
            accent: "bg-pink-500",
        },
    }

    const colors = colorClasses[accentColor]

    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.8 + delay }}
            whileHover={{ scale: 1.05, y: -5 }}
            className={cn(
                "relative flex items-center gap-3 px-5 py-4",
                "bg-white/[0.03] backdrop-blur-xl",
                "border rounded-2xl",
                "transition-all duration-500",
                "group cursor-default overflow-hidden",
                colors.border,
                colors.glow,
                "shadow-lg hover:shadow-xl"
            )}
        >
            {/* Holographic shine effect */}
            <motion.div
                className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                style={{
                    background: "linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.1) 45%, rgba(255,255,255,0.05) 50%, transparent 55%)",
                }}
                animate={{
                    x: ["-100%", "200%"],
                }}
                transition={{
                    duration: 1.5,
                    repeat: Infinity,
                    repeatDelay: 3,
                }}
            />

            {/* Accent line */}
            <div className={cn("absolute left-0 top-1/4 bottom-1/4 w-[2px] rounded-full", colors.accent)} />

            <div className={cn(
                "relative p-2.5 rounded-xl bg-gradient-to-br",
                "group-hover:scale-110 transition-transform duration-300",
                colors.icon
            )}>
                {icon}
            </div>
            <div className="relative">
                <motion.div
                    className="text-2xl font-bold text-white"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 1 + delay }}
                >
                    {value}
                </motion.div>
                <div className="text-xs text-neutral-400 font-medium uppercase tracking-wider">{label}</div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   HERO COMPONENT — AI-POWERED GLOW-UP
   ============================================================================ */

export function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Background layers */}
            <NeuralBackground />
            <NeuralParticles />

            {/* Content */}
            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
                {/* AI Badge */}
                <AIBadge />

                {/* Main headline with holographic effect */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="relative mb-6"
                >
                    <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-bold tracking-tight">
                        <span className="text-white drop-shadow-[0_0_30px_rgba(255,255,255,0.3)]">
                            Master DevOps
                        </span>
                        <br />
                        <motion.span
                            className="relative inline-block"
                            animate={{
                                backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                            }}
                            transition={{
                                duration: 5,
                                repeat: Infinity,
                                ease: "linear",
                            }}
                            style={{
                                background: "linear-gradient(90deg, #6366f1, #8b5cf6, #06b6d4, #ec4899, #6366f1)",
                                backgroundSize: "200% auto",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                filter: "drop-shadow(0 0 30px rgba(99,102,241,0.5))",
                            }}
                        >
                            Build Your Career
                        </motion.span>
                    </h1>

                    {/* Glow effect behind text */}
                    <div className="absolute inset-0 -z-10 blur-3xl opacity-30">
                        <div className="absolute inset-0 bg-gradient-to-r from-primary-500 via-purple-500 to-cyan-500" />
                    </div>
                </motion.div>

                {/* AI-Powered Subheadline */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="relative max-w-3xl mx-auto mb-12"
                >
                    {/* AI Intelligence badge */}
                    <div className="flex items-center justify-center gap-2 mb-4">
                        <motion.div
                            animate={{
                                boxShadow: [
                                    "0 0 20px rgba(99,102,241,0.5)",
                                    "0 0 40px rgba(139,92,246,0.7)",
                                    "0 0 20px rgba(99,102,241,0.5)",
                                ]
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                            className="flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-primary-500/20 to-purple-500/20 border border-primary-500/30"
                        >
                            <Brain className="w-4 h-4 text-primary-400" />
                            <span className="text-sm font-semibold text-primary-300">AI-Powered Intelligence</span>
                            <motion.div
                                animate={{ rotate: 360 }}
                                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                            >
                                <Zap className="w-4 h-4 text-yellow-400" />
                            </motion.div>
                        </motion.div>
                    </div>

                    <p className="text-lg sm:text-xl md:text-2xl text-neutral-300 leading-relaxed">
                        The{" "}
                        <span className="relative">
                            <span className="relative z-10 font-semibold text-white">
                                smartest way
                            </span>
                            <motion.span
                                className="absolute inset-x-0 -bottom-1 h-3 bg-gradient-to-r from-primary-500/40 to-purple-500/40 -z-0 rounded"
                                animate={{ scaleX: [0, 1] }}
                                transition={{ duration: 0.8, delay: 1 }}
                            />
                        </span>{" "}
                        to learn DevOps. Personalized paths,{" "}
                        <span className="font-semibold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
                            adaptive difficulty
                        </span>
                        , and{" "}
                        <span className="font-semibold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
                            real-time feedback
                        </span>{" "}
                        powered by AI.
                    </p>

                    {/* Tech specs line */}
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.8 }}
                        className="flex items-center justify-center gap-4 mt-4 text-sm text-neutral-500"
                    >
                        <span className="flex items-center gap-1">
                            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                            36 modules
                        </span>
                        <span className="text-neutral-700">•</span>
                        <span className="flex items-center gap-1">
                            <div className="w-2 h-2 rounded-full bg-primary-500 animate-pulse" />
                            80+ hands-on labs
                        </span>
                        <span className="text-neutral-700">•</span>
                        <span className="flex items-center gap-1">
                            <div className="w-2 h-2 rounded-full bg-purple-500 animate-pulse" />
                            Real projects
                        </span>
                    </motion.div>
                </motion.div>

                {/* CTA Buttons with enhanced glow - MILESTONE 2.0: Direct to learning */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16"
                >
                    <Link href="/skillsmaps">
                        <motion.div
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.98 }}
                            className="relative group"
                        >
                            {/* Button glow */}
                            <div className="absolute -inset-1 bg-gradient-to-r from-primary-500 via-purple-500 to-cyan-500 rounded-2xl blur-lg opacity-70 group-hover:opacity-100 transition-opacity duration-300" />
                            <Button
                                size="xl"
                                variant="gradient"
                                className="relative gap-2 min-w-[220px] text-lg font-semibold"
                                rightIcon={<ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />}
                            >
                                Start Learning Now
                            </Button>
                        </motion.div>
                    </Link>
                    <Link href="#curriculum">
                        <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.98 }}>
                            <Button
                                size="xl"
                                variant="glass"
                                className="gap-2 min-w-[200px] text-white border-white/20 hover:border-white/40 hover:bg-white/10"
                                leftIcon={<Play className="w-4 h-4" />}
                            >
                                View Curriculum
                            </Button>
                        </motion.div>
                    </Link>
                </motion.div>

                {/* Stats row with enhanced cards */}
                <div className="flex flex-wrap items-center justify-center gap-4 sm:gap-6">
                    <StatCard
                        icon={<Clock className="w-5 h-5" />}
                        value="310+"
                        label="Hours of Content"
                        delay={0}
                        accentColor="primary"
                    />
                    <StatCard
                        icon={<BookOpen className="w-5 h-5" />}
                        value="36"
                        label="Modules"
                        delay={0.1}
                        accentColor="purple"
                    />
                    <StatCard
                        icon={<Target className="w-5 h-5" />}
                        value="4"
                        label="Career Tracks"
                        delay={0.2}
                        accentColor="cyan"
                    />
                    <StatCard
                        icon={<Brain className="w-5 h-5" />}
                        value="AI"
                        label="Powered"
                        delay={0.3}
                        accentColor="pink"
                    />
                </div>
            </div>

            {/* Enhanced scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.5, duration: 0.6 }}
                className="absolute bottom-8 left-1/2 -translate-x-1/2"
            >
                <motion.div
                    animate={{ y: [0, 8, 0] }}
                    transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                    className="relative w-6 h-10 rounded-full border-2 border-primary-500/30 flex items-start justify-center p-2"
                >
                    {/* Glow effect */}
                    <div className="absolute inset-0 rounded-full bg-primary-500/10 blur-md" />
                    <motion.div
                        animate={{ opacity: [0.5, 1, 0.5] }}
                        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                        className="w-1.5 h-1.5 rounded-full bg-primary-400 shadow-[0_0_10px_rgba(99,102,241,0.8)]"
                    />
                </motion.div>
            </motion.div>
        </section>
    )
}

export default Hero
