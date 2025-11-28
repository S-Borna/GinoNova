"use client"

/**
 * ============================================================================
 * FEATURES SECTION — Six Key Platform Features
 * ============================================================================
 *
 * Design: Bento-grid inspired layout with glassmorphism cards,
 * animated icons, and premium micro-interactions.
 *
 * @phase A.1 - Landing Page
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
} from "lucide-react"

/* ============================================================================
   FEATURE DATA
   ============================================================================ */

const FEATURES = [
    {
        id: "learning-path",
        title: "Structured Learning Path",
        description: "Progress through 15 carefully crafted modules. Each builds on the last, ensuring you never miss foundational concepts.",
        icon: Route,
        color: "primary",
        gradient: "from-indigo-500 to-violet-600",
        span: "md:col-span-2",
    },
    {
        id: "hands-on-labs",
        title: "Hands-On Labs",
        description: "Practice in real cloud environments. No simulations—actual infrastructure you build and tear down.",
        icon: Beaker,
        color: "cyan",
        gradient: "from-cyan-500 to-teal-600",
        span: "",
    },
    {
        id: "real-projects",
        title: "Real-World Projects",
        description: "Build portfolio-worthy projects: CI/CD pipelines, Kubernetes clusters, monitoring stacks.",
        icon: FolderGit2,
        color: "purple",
        gradient: "from-violet-500 to-purple-600",
        span: "",
    },
    {
        id: "progress-tracking",
        title: "Progress Tracking",
        description: "Visual dashboards show your advancement. Earn XP, level up, and track your hours invested.",
        icon: TrendingUp,
        color: "emerald",
        gradient: "from-emerald-500 to-green-600",
        span: "",
    },
    {
        id: "studyflow",
        title: "Studyflow System",
        description: "Smart study sessions with Pomodoro timers, focus modes, and productivity analytics.",
        icon: Timer,
        color: "orange",
        gradient: "from-orange-500 to-amber-600",
        span: "",
    },
    {
        id: "certificates",
        title: "Certificates & Badges",
        description: "Earn verified certificates for each track. Showcase your skills to potential employers.",
        icon: Award,
        color: "yellow",
        gradient: "from-yellow-500 to-orange-600",
        span: "md:col-span-2",
    },
]

/* ============================================================================
   FEATURE CARD COMPONENT
   ============================================================================ */

interface FeatureCardProps {
    feature: typeof FEATURES[0]
    index: number
}

function FeatureCard({ feature, index }: FeatureCardProps) {
    const Icon = feature.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{ duration: 0.5, delay: index * 0.08 }}
            className={cn("group relative", feature.span)}
        >
            <div
                className={cn(
                    "relative h-full p-6 rounded-2xl overflow-hidden",
                    "bg-white/[0.03] backdrop-blur-sm",
                    "border border-white/[0.08]",
                    "hover:bg-white/[0.05] hover:border-white/[0.15]",
                    "transition-all duration-500"
                )}
            >
                {/* Subtle gradient overlay on hover */}
                <div
                    className={cn(
                        "absolute inset-0 opacity-0 group-hover:opacity-100",
                        "transition-opacity duration-500 pointer-events-none",
                        "bg-gradient-to-br",
                        feature.gradient
                    )}
                    style={{ opacity: 0 }}
                />
                <div
                    className="absolute inset-0 opacity-0 group-hover:opacity-[0.03] transition-opacity duration-500 pointer-events-none bg-gradient-to-br"
                    style={{
                        backgroundImage: `linear-gradient(135deg, var(--${feature.color}-500, #6366f1) 0%, transparent 50%)`,
                    }}
                />

                {/* Content */}
                <div className="relative z-10 flex flex-col h-full">
                    {/* Icon */}
                    <div
                        className={cn(
                            "inline-flex p-3 rounded-xl mb-4 w-fit",
                            "bg-gradient-to-br",
                            feature.gradient,
                            "shadow-lg group-hover:scale-105 group-hover:rotate-3",
                            "transition-all duration-300"
                        )}
                    >
                        <Icon className="w-5 h-5 text-white" />
                    </div>

                    {/* Title */}
                    <h3 className="text-lg font-semibold text-white mb-2 group-hover:text-white/95">
                        {feature.title}
                    </h3>

                    {/* Description */}
                    <p className="text-sm text-neutral-400 leading-relaxed">
                        {feature.description}
                    </p>
                </div>

                {/* Corner accent */}
                <div className="absolute top-0 right-0 w-20 h-20 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                    <div
                        className={cn(
                            "absolute top-0 right-0 w-full h-full",
                            "bg-gradient-to-bl",
                            feature.gradient,
                            "opacity-5 blur-2xl"
                        )}
                    />
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function Features() {
    return (
        <section className="relative py-24 bg-neutral-950 overflow-hidden">
            {/* Background elements */}
            <div className="absolute inset-0">
                {/* Grid pattern */}
                <div
                    className="absolute inset-0 opacity-[0.02]"
                    style={{
                        backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                                         linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
                        backgroundSize: "60px 60px",
                    }}
                />

                {/* Ambient glow */}
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[600px] bg-primary-500/5 rounded-full blur-[150px]" />
            </div>

            <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-16"
                >
                    <div className="inline-flex items-center gap-2 px-4 py-1.5 mb-4 text-xs font-semibold tracking-wider uppercase text-primary-400 bg-primary-500/10 rounded-full">
                        <Sparkles className="w-3.5 h-3.5" />
                        Platform Features
                    </div>
                    <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
                        Everything You Need to{" "}
                        <span className="bg-gradient-to-r from-cyan-400 to-primary-400 bg-clip-text text-transparent">
                            Succeed
                        </span>
                    </h2>
                    <p className="text-lg text-neutral-400 max-w-2xl mx-auto">
                        A complete learning platform designed for maximum effectiveness.
                        Every feature serves your growth.
                    </p>
                </motion.div>

                {/* Features bento grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    {FEATURES.map((feature, index) => (
                        <FeatureCard key={feature.id} feature={feature} index={index} />
                    ))}
                </div>
            </div>
        </section>
    )
}

export default Features
