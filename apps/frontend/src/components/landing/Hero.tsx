"use client"

/**
 * ============================================================================
 * 🌌 HERO SECTION — EPIC TECH MASTERY EDITION 2026 🌌
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
 * - Complete tech stack: AI, DevOps, MLOps, Cloud (GCP, AWS, Azure)
 * - Swedish tech community
 *
 * @phase MILESTONE-3.0-EPIC-RELAUNCH
 * @target 100,000 daily active users
 */

import * as React from "react"
import Link from "next/link"
import Image from "next/image"
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
    Cloud,
    Code,
    Cpu,
    Server,
    Database,
    Network,
    Boxes,
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

            {/* Central ambient glow - enhanced */}
            <div
                className="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{
                    width: "1200px",
                    height: "900px",
                    background: "radial-gradient(circle, rgba(139,92,246,0.3) 0%, rgba(168,85,247,0.15) 40%, transparent 70%)",
                    filter: "blur(100px)",
                }}
            />

            {/* Multi-color accent glows */}
            <div
                className="absolute bottom-0 right-0 w-[700px] h-[500px]"
                style={{
                    background: "radial-gradient(circle, rgba(34,211,238,0.2) 0%, transparent 60%)",
                    filter: "blur(80px)",
                }}
            />

            <div
                className="absolute top-1/4 left-0 w-[500px] h-[400px]"
                style={{
                    background: "radial-gradient(circle, rgba(236,72,153,0.15) 0%, transparent 60%)",
                    filter: "blur(70px)",
                }}
            />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139,92,246,0.6) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139,92,246,0.6) 1px, transparent 1px)
                    `,
                    backgroundSize: "60px 60px",
                }}
            />

            {/* Bottom fade to content */}
            <div className="absolute bottom-0 left-0 right-0 h-64 bg-gradient-to-t from-[#05050a] via-[#05050a]/80 to-transparent" />
        </div>
    )
}

/* ============================================================================
   ✨ COSMIC PARTICLE SYSTEM — ENHANCED STARDUST
   ============================================================================ */

function StardustParticles() {
    const particles = React.useMemo(() =>
        Array.from({ length: 20 }, (_, i) => ({
            id: i,
            size: Math.random() * 3 + 1,
            x: Math.random() * 100,
            y: Math.random() * 100,
            duration: Math.random() * 30 + 25,
            delay: Math.random() * 15,
            color: i % 4 === 0 ? "purple" : i % 4 === 1 ? "cyan" : i % 4 === 2 ? "pink" : "white",
        })), [])

    const colorMap = {
        purple: "bg-purple-400/80",
        cyan: "bg-cyan-400/80",
        pink: "bg-pink-400/80",
        white: "bg-white/60",
    }

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {particles.map((p) => (
                <motion.div
                    key={p.id}
                    className={cn("absolute rounded-full", colorMap[p.color as keyof typeof colorMap] || colorMap.purple)}
                    style={{
                        width: p.size,
                        height: p.size,
                        left: `${p.x}%`,
                        top: `${p.y}%`,
                        boxShadow: `0 0 ${p.size * 4}px currentColor`,
                    }}
                    animate={{
                        y: [0, -180, 0],
                        opacity: [0, 0.9, 0],
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
   ☁️ GINONOVA CLOUD OVERLAY — FLOATING LOGO
   ============================================================================ */

function GinoNovaCloudOverlay() {
    return (
        <motion.div
            initial={{ opacity: 0, y: -50 }}
            animate={{
                opacity: [0, 0.12, 0.12],
                y: [-50, 0, 0],
            }}
            transition={{
                duration: 3,
                times: [0, 0.5, 1],
                ease: [0.16, 1, 0.3, 1]
            }}
            className="absolute top-12 left-1/2 -translate-x-1/2 z-0 pointer-events-none"
        >
            <motion.div
                animate={{
                    y: [0, -15, 0],
                    scale: [1, 1.05, 1],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "easeInOut"
                }}
                className="relative"
            >
                {/* Massive glow behind logo */}
                <div
                    className="absolute inset-0 blur-[120px]"
                    style={{
                        background: "radial-gradient(circle, rgba(139,92,246,0.4) 0%, rgba(99,102,241,0.2) 50%, transparent 70%)",
                        width: "800px",
                        height: "800px",
                        transform: "translate(-50%, -50%)",
                        top: "50%",
                        left: "50%",
                    }}
                />

                {/* Logo SVG */}
                <div className="relative" style={{ filter: "drop-shadow(0 0 50px rgba(139,92,246,0.7))" }}>
                    <Image
                        src="/ginonova-logo.svg"
                        alt="GinoNova"
                        width={700}
                        height={700}
                        className="opacity-90"
                        priority
                    />
                </div>
            </motion.div>
        </motion.div>
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
            transition={{ duration: 0.6, delay: 0.3 }}
            className="inline-flex mb-8"
        >
            <div
                className={cn(
                    "flex items-center gap-3 px-6 py-3 rounded-full",
                    "bg-emerald-500/15 backdrop-blur-sm",
                    "border border-emerald-400/40",
                    "shadow-lg shadow-emerald-500/10"
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
   🧠 AI & TECH STACK INDICATOR
   ============================================================================ */

function TechStackIndicator() {
    const stacks = [
        { icon: Brain, label: "AI & Machine Learning", color: "purple" },
        { icon: Cloud, label: "Multi-Cloud Mastery", color: "cyan" },
        { icon: Server, label: "DevOps Excellence", color: "emerald" },
        { icon: Cpu, label: "MLOps Engineering", color: "pink" },
    ]

    const colorClasses = {
        purple: { bg: "bg-purple-500/15", border: "border-purple-500/30", text: "text-purple-300", icon: "text-purple-400" },
        cyan: { bg: "bg-cyan-500/15", border: "border-cyan-500/30", text: "text-cyan-300", icon: "text-cyan-400" },
        emerald: { bg: "bg-emerald-500/15", border: "border-emerald-500/30", text: "text-emerald-300", icon: "text-emerald-400" },
        pink: { bg: "bg-pink-500/15", border: "border-pink-500/30", text: "text-pink-300", icon: "text-pink-400" },
    }

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 0.6 }}
            className="flex flex-wrap items-center justify-center gap-3 mb-8"
        >
            {stacks.map((stack, i) => {
                const colors = colorClasses[stack.color as keyof typeof colorClasses]
                const Icon = stack.icon

                return (
                    <motion.div
                        key={i}
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: 0.6 + i * 0.1, duration: 0.5 }}
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-full backdrop-blur-sm",
                            colors.bg,
                            colors.border,
                            "border"
                        )}
                    >
                        <Icon className={cn("w-4 h-4", colors.icon)} />
                        <span className={cn("text-xs sm:text-sm font-semibold", colors.text)}>
                            {stack.label}
                        </span>
                    </motion.div>
                )
            })}
        </motion.div>
    )
}

/* ============================================================================
   💎 TECH STACK SHOWCASE — ANIMATED LOGOS
   ============================================================================ */

function TechStackShowcase() {
    const techStacks = [
        // Row 1: Cloud Platforms
        ["Google Cloud", "AWS", "Azure", "Kubernetes"],
        // Row 2: DevOps & CI/CD
        ["Docker", "Terraform", "GitHub Actions", "Jenkins"],
        // Row 3: AI & ML
        ["Python", "TensorFlow", "PyTorch", "Scikit-learn"],
        // Row 4: Monitoring & More
        ["Prometheus", "Grafana", "Linux", "Go"],
    ]

    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1 }}
            className="max-w-5xl mx-auto mb-12"
        >
            <div className="space-y-4">
                {techStacks.map((row, rowIndex) => (
                    <motion.div
                        key={rowIndex}
                        initial={{ opacity: 0, x: rowIndex % 2 === 0 ? -50 : 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 1.2 + rowIndex * 0.1, duration: 0.6 }}
                        className="flex flex-wrap items-center justify-center gap-3"
                    >
                        {row.map((tech, techIndex) => (
                            <motion.div
                                key={techIndex}
                                initial={{ opacity: 0, scale: 0.8 }}
                                animate={{ opacity: 1, scale: 1 }}
                                whileHover={{ scale: 1.1, y: -5 }}
                                transition={{
                                    delay: 1.3 + rowIndex * 0.1 + techIndex * 0.05,
                                    duration: 0.3
                                }}
                                className={cn(
                                    "px-4 py-2 rounded-lg",
                                    "bg-gradient-to-br from-white/[0.08] to-white/[0.02]",
                                    "border border-white/10",
                                    "backdrop-blur-sm",
                                    "hover:border-purple-400/40",
                                    "transition-all duration-300",
                                    "shadow-lg shadow-black/20"
                                )}
                            >
                                <span className="text-sm font-semibold text-zinc-300 whitespace-nowrap">
                                    {tech}
                                </span>
                            </motion.div>
                        ))}
                    </motion.div>
                ))}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   🚀 MAIN HERO COMPONENT — EPIC TECH MASTERY
   ============================================================================ */

export function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Background layers */}
            <CosmicBackground />
            <StardustParticles />

            {/* Floating GinoNova Logo Overlay */}
            <GinoNovaCloudOverlay />

            {/* Content */}
            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32 text-center">

                {/* FREE ACCESS BADGE */}
                <FreeAccessBadge />

                {/* Tech Stack Indicators */}
                <TechStackIndicator />

                {/* Main headline with cosmic glow */}
                <motion.div
                    initial={{ opacity: 0, y: 40 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 1, delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
                    className="relative mb-10"
                >
                    {/* Glow behind text */}
                    <div className="absolute inset-0 -z-10 blur-[120px] opacity-60">
                        <div className="absolute inset-0 bg-gradient-to-r from-purple-600 via-cyan-500 to-pink-600" />
                    </div>

                    <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-black tracking-tight leading-[1.05]">
                        <motion.span
                            className="block text-white mb-3"
                            style={{
                                textShadow: "0 0 80px rgba(255,255,255,0.4), 0 0 120px rgba(139,92,246,0.3)"
                            }}
                        >
                            Master the Complete
                        </motion.span>
                        <motion.span
                            className="relative block"
                            animate={{
                                backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                            }}
                            transition={{
                                duration: 8,
                                repeat: Infinity,
                                ease: "linear",
                            }}
                            style={{
                                background: "linear-gradient(90deg, #8B5CF6, #06b6d4, #ec4899, #22d3ee, #a78bfa, #8B5CF6)",
                                backgroundSize: "300% auto",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                filter: "drop-shadow(0 0 50px rgba(139,92,246,0.7))",
                            }}
                        >
                            Tech Stack
                        </motion.span>
                    </h1>
                </motion.div>

                {/* Subheadline with epic description */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.7 }}
                    className="max-w-4xl mx-auto mb-10"
                >
                    <p className="text-lg sm:text-xl md:text-2xl text-zinc-300 leading-relaxed font-light">
                        From{" "}
                        <span className="font-bold bg-gradient-to-r from-purple-400 to-violet-400 bg-clip-text text-transparent">
                            AI & Machine Learning
                        </span>{" "}
                        to{" "}
                        <span className="font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
                            DevOps & MLOps
                        </span>,{" "}
                        master{" "}
                        <span className="font-bold bg-gradient-to-r from-pink-400 to-rose-400 bg-clip-text text-transparent">
                            Google Cloud, AWS, Azure
                        </span>,{" "}
                        and every critical technology in between.
                    </p>

                    {/* Quick feature list */}
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.9 }}
                        className="flex flex-wrap items-center justify-center gap-x-6 gap-y-2 mt-6 text-sm text-zinc-400"
                    >
                        {[
                            "31+ moduler",
                            "700+ quiz-frågor",
                            "500+ flashcards",
                            "200+ scenarios",
                            "AI Quiz Generator",
                            "Dallas AI-assistent",
                        ].map((item, i) => (
                            <motion.span
                                key={i}
                                initial={{ opacity: 0, x: -10 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ delay: 1 + i * 0.08 }}
                                className="flex items-center gap-2"
                            >
                                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                                <span className="font-medium">{item}</span>
                            </motion.span>
                        ))}
                    </motion.div>
                </motion.div>

                {/* CTA Button - Above Tech Stack */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 1.2 }}
                    className="flex items-center justify-center mb-10"
                >
                    <Link href="/skillsmaps">
                        <Button
                            size="xl"
                            className={cn(
                                "gap-3 min-w-[300px] h-16 text-lg font-bold",
                                "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                "hover:from-purple-500 hover:via-violet-500 hover:to-indigo-500",
                                "border-0 rounded-2xl",
                                "shadow-2xl shadow-purple-500/30",
                                "hover:shadow-purple-500/50",
                                "transition-all duration-300 hover:scale-[1.05]",
                                "backdrop-blur-sm"
                            )}
                        >
                            <Rocket className="w-6 h-6" />
                            Starta Din Resa — Gratis
                            <ArrowRight className="w-6 h-6" />
                        </Button>
                    </Link>
                </motion.div>

                {/* Tech Stack Visual Showcase */}
                <TechStackShowcase />
            </div>

            {/* Scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 2, duration: 0.6 }}
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
