"use client"

/**
 * ============================================================================
 * ⭐ FEATURES SECTION — COSMIC BENTO GRID ⭐
 * ============================================================================
 *
 * Premium bento-grid layout showcasing platform features
 * with holographic cards, cosmic particles, and stunning animations.
 *
 * Design Philosophy:
 * - Apple-inspired breathing animations
 * - Stripe-level gradient sophistication
 * - Netflix cinematic depth
 * - Each feature card is a mini experience
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Route,
    Beaker,
    FolderGit2,
    TrendingUp,
    Timer,
    Award,
    Sparkles,
    Brain,
    Rocket,
    Code2,
    Users,
    BarChart3,
    Trophy,
} from "lucide-react"

/* ============================================================================
   🎯 FEATURE DATA — SWEDISH VERSION
   ============================================================================ */

const FEATURES = [
    {
        id: "learning-path",
        title: "20+ Premium Learning Paths",
        description: "Hela DevOps-ekosystemet: Linux, Kubernetes, Docker, AWS, Azure, GCP, Terraform, Ansible, CI/CD, Python, Go, Monitoring, Security och mer.",
        icon: Route,
        gradient: "from-indigo-500 to-violet-600",
        glowColor: "rgba(99,102,241,0.4)",
        span: "md:col-span-2 md:row-span-1",
        accent: "indigo",
    },
    {
        id: "code-playground",
        title: "Interactive Code Playground",
        description: "Testa kod direkt i browsern: Python, Bash, Docker, Kubernetes, Terraform. Monaco Editor med syntax highlighting och real-time feedback.",
        icon: Code2,
        gradient: "from-purple-500 to-indigo-600",
        glowColor: "rgba(139,92,246,0.4)",
        span: "",
        accent: "purple",
    },
    {
        id: "community",
        title: "Community & Forums",
        description: "Diskussionsforum med reputation system, badges, upvotes. Ställ frågor, hjälp andra, tjäna Legend status.",
        icon: Users,
        gradient: "from-pink-500 to-rose-600",
        glowColor: "rgba(236,72,153,0.4)",
        span: "",
        accent: "pink",
    },
    {
        id: "ai-assistant",
        title: "Dallas AI-Assistent 🐺",
        description: "Persistent AI-assistent på varje sida. Kontextmedveten hjälp, personliga rekommendationer, quiz-generering och 24/7 support.",
        icon: Brain,
        gradient: "from-violet-500 to-purple-600",
        glowColor: "rgba(139,92,246,0.4)",
        span: "",
        accent: "violet",
    },
    {
        id: "analytics",
        title: "Advanced Analytics",
        description: "Spåra studietid, learning velocity, skill distribution. AI-powered insights och benchmarking mot peers.",
        icon: BarChart3,
        gradient: "from-cyan-500 to-teal-600",
        glowColor: "rgba(6,182,212,0.4)",
        span: "",
        accent: "cyan",
    },
    {
        id: "certificates",
        title: "Certificates & Achievements",
        description: "Tjäna verifierade certifikat, badges, och achievements. Visa upp dina kunskaper på LinkedIn och GitHub.",
        icon: Trophy,
        gradient: "from-amber-500 to-yellow-600",
        glowColor: "rgba(245,158,11,0.4)",
        span: "",
        accent: "amber",
    },
    {
        id: "progress-tracking",
        title: "Gamification & XP System",
        description: "XP points, leveling, streaks, leaderboards. Varje modul ger XP baserat på svårighetsgrad och time investment.",
        icon: TrendingUp,
        gradient: "from-emerald-500 to-green-600",
        glowColor: "rgba(16,185,129,0.4)",
        span: "",
        accent: "emerald",
    },
    {
        id: "studyflow",
        title: "Enhanced Study Experience",
        description: "Spotify integration med music visualizer, Pomodoro timers, study room modes. Last.fm scrobbling stöd.",
        icon: Timer,
        gradient: "from-orange-500 to-red-600",
        glowColor: "rgba(249,115,22,0.4)",
        span: "md:col-span-2 md:row-span-1",
        accent: "orange",
    },
]

/* ============================================================================
   🌟 FEATURE CARD COMPONENT — HOLOGRAPHIC
   ============================================================================ */

interface FeatureCardProps {
    feature: typeof FEATURES[0]
    index: number
}

function FeatureCard({ feature, index }: FeatureCardProps) {
    const Icon = feature.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 30, scale: 0.95 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ once: true, margin: "-30px" }}
            transition={{
                duration: 0.7,
                delay: index * 0.08,
                ease: [0.16, 1, 0.3, 1]
            }}
            className={cn("group relative", feature.span)}
        >
            {/* Outer glow */}
            <motion.div
                className="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-700"
                style={{ background: feature.glowColor }}
            />

            <div
                className={cn(
                    "relative h-full p-6 lg:p-8 rounded-2xl overflow-hidden",
                    "bg-gradient-to-br from-[#0d0d14]/90 to-[#0a0a0f]/90",
                    "backdrop-blur-xl",
                    "border border-white/[0.08]",
                    "group-hover:border-white/[0.2]",
                    "transition-all duration-500"
                )}
            >
                {/* Animated gradient background on hover */}
                <motion.div
                    className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700"
                    style={{
                        background: `radial-gradient(circle at 30% 20%, ${feature.glowColor} 0%, transparent 50%)`,
                    }}
                />

                {/* Holographic shimmer effect */}
                <motion.div
                    className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                    style={{
                        background: "linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.1) 45%, rgba(255,255,255,0.05) 50%, transparent 55%)",
                    }}
                    animate={{
                        x: ["-100%", "200%"],
                    }}
                    transition={{
                        duration: 1.8,
                        repeat: Infinity,
                        repeatDelay: 2.5,
                    }}
                />

                {/* Content */}
                <div className="relative z-10 flex flex-col h-full">
                    {/* Icon with animated glow */}
                    <motion.div
                        className={cn(
                            "inline-flex p-3 rounded-xl mb-5 w-fit",
                            "bg-gradient-to-br",
                            feature.gradient,
                        )}
                        style={{
                            boxShadow: `0 8px 30px -8px ${feature.glowColor}`,
                        }}
                        whileHover={{ scale: 1.1, rotate: 5 }}
                        transition={{ type: "spring", stiffness: 400 }}
                    >
                        <Icon className="w-5 h-5 text-white" />
                    </motion.div>

                    {/* Title */}
                    <h3 className="text-lg lg:text-xl font-bold text-white mb-3 group-hover:text-white/95">
                        {feature.title}
                    </h3>

                    {/* Description */}
                    <p className="text-sm lg:text-base text-zinc-400 leading-relaxed">
                        {feature.description}
                    </p>
                </div>

            </div>
        </motion.div>
    )
}

/* ============================================================================
   🚀 MAIN COMPONENT — COSMIC FEATURES SECTION
   ============================================================================ */

export function Features() {
    return (
        <section className="relative py-32 overflow-hidden bg-[#05050a]">
            {/* Cosmic background elements */}
            <div className="absolute inset-0">
                {/* Base gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#0a0a12] to-[#05050a]" />

                {/* Large ambient glow - centered, static */}
                <div
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[600px]"
                    style={{
                        background: "radial-gradient(ellipse, rgba(99,102,241,0.06) 0%, transparent 60%)",
                        filter: "blur(80px)",
                    }}
                />

                {/* Secondary glow - cyan accent */}
                <div
                    className="absolute bottom-1/4 right-1/4 w-[500px] h-[300px]"
                    style={{
                        background: "radial-gradient(ellipse, rgba(6,182,212,0.06) 0%, transparent 60%)",
                        filter: "blur(60px)",
                    }}
                />

                {/* Grid pattern overlay */}
                <div
                    className="absolute inset-0 opacity-[0.015]"
                    style={{
                        backgroundImage: `
                            linear-gradient(rgba(255,255,255,0.3) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(255,255,255,0.3) 1px, transparent 1px)
                        `,
                        backgroundSize: "60px 60px",
                    }}
                />

                {/* Separator line */}
                <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-500/30 to-transparent" />
            </div>

            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                    className="text-center mb-20"
                >
                    {/* Badge */}
                    <div
                        className={cn(
                            "inline-flex items-center gap-2 px-5 py-2 mb-6",
                            "text-sm font-semibold tracking-wide uppercase",
                            "text-cyan-300 bg-cyan-500/15 rounded-full",
                            "border border-cyan-500/30"
                        )}
                    >
                        <Sparkles className="w-4 h-4" />
                        Plattformsfunktioner
                    </div>

                    <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6">
                        Allt du behöver för att{" "}
                        <span
                            className="bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400 bg-clip-text text-transparent"
                            style={{ filter: "drop-shadow(0 0 25px rgba(34,211,238,0.4))" }}
                        >
                            Lyckas
                        </span>
                    </h2>

                    <p className="text-lg sm:text-xl text-zinc-400 max-w-3xl mx-auto leading-relaxed">
                        En komplett läroplattform designad för maximal effektivitet.{" "}
                        <span className="text-white font-medium">Varje funktion tjänar din utveckling.</span>
                    </p>
                </motion.div>

                {/* Features bento grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
                    {FEATURES.map((feature, index) => (
                        <FeatureCard key={feature.id} feature={feature} index={index} />
                    ))}
                </div>

                {/* Bottom highlight */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="flex items-center justify-center mt-16"
                >
                    <div
                        className={cn(
                            "flex items-center gap-3 px-6 py-3 rounded-full",
                            "bg-purple-500/10",
                            "border border-white/10"
                        )}
                    >
                        <Rocket className="w-5 h-5 text-purple-400" />
                        <span className="text-sm font-medium text-zinc-300">
                            Och mycket mer — upptäck allting när du börjar lära
                        </span>
                    </div>
                </motion.div>
            </div>
        </section>
    )
}

export default Features
