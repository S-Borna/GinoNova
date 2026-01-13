"use client"

/**
 * ============================================================================
 * 📊 STATS SECTION — IMPRESSIVE NUMBERS THAT SELL
 * ============================================================================
 *
 * Massive, animated statistics that show the platform's value.
 * Numbers that make visitors think: "Wow, this is serious."
 *
 * Design Philosophy:
 * - Large, bold numbers with animated counters
 * - Cosmic glow effects on hover
 * - Social proof through metrics
 * - Swedish text for local audience
 *
 * @phase MILESTONE-3.0-WOW-LANDING
 */

import * as React from "react"
import { motion, useInView, useMotionValue, useSpring } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Users,
    BookOpen,
    Award,
    TrendingUp,
    Code,
    Clock,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   🎯 STATS DATA — IMPRESSIVE METRICS
   ============================================================================ */

const STATS = [
    {
        id: "students",
        value: 10000,
        suffix: "+",
        label: "Aktiva Studenter",
        description: "Bygger sina karriärer",
        icon: Users,
        color: "#8b5cf6",
        gradient: "from-purple-500 to-violet-600",
        glowColor: "rgba(139,92,246,0.4)",
    },
    {
        id: "modules",
        value: 36,
        suffix: "",
        label: "Moduler",
        description: "Varje ämne täckt",
        icon: BookOpen,
        color: "#06b6d4",
        gradient: "from-cyan-500 to-teal-600",
        glowColor: "rgba(6,182,212,0.4)",
    },
    {
        id: "labs",
        value: 80,
        suffix: "+",
        label: "Hands-On Labs",
        description: "Praktisk erfarenhet",
        icon: Code,
        color: "#ec4899",
        gradient: "from-pink-500 to-rose-600",
        glowColor: "rgba(236,72,153,0.4)",
    },
    {
        id: "hours",
        value: 600,
        suffix: "+",
        label: "Timmar Innehåll",
        description: "Komplett utbildning",
        icon: Clock,
        color: "#f59e0b",
        gradient: "from-amber-500 to-orange-600",
        glowColor: "rgba(245,158,11,0.4)",
    },
    {
        id: "certificates",
        value: 5000,
        suffix: "+",
        label: "Certifikat Utfärdade",
        description: "Bevisad kompetens",
        icon: Award,
        color: "#10b981",
        gradient: "from-emerald-500 to-green-600",
        glowColor: "rgba(16,185,129,0.4)",
    },
    {
        id: "placement",
        value: 92,
        suffix: "%",
        label: "Jobbplacering",
        description: "Inom 6 månader",
        icon: TrendingUp,
        color: "#6366f1",
        gradient: "from-indigo-500 to-violet-600",
        glowColor: "rgba(99,102,241,0.4)",
    },
]

/* ============================================================================
   🔢 ANIMATED COUNTER COMPONENT
   ============================================================================ */

interface AnimatedCounterProps {
    value: number
    suffix?: string
}

function AnimatedCounter({ value, suffix = "" }: AnimatedCounterProps) {
    const ref = React.useRef<HTMLSpanElement>(null)
    const isInView = useInView(ref, { once: true, margin: "-100px" })
    const motionValue = useMotionValue(0)
    const springValue = useSpring(motionValue, {
        damping: 60,
        stiffness: 100,
    })
    const [displayValue, setDisplayValue] = React.useState(0)

    React.useEffect(() => {
        if (isInView) {
            motionValue.set(value)
        }
    }, [isInView, value, motionValue])

    React.useEffect(() => {
        const unsubscribe = springValue.on("change", (latest) => {
            setDisplayValue(Math.floor(latest))
        })
        return () => unsubscribe()
    }, [springValue])

    return (
        <span ref={ref}>
            {displayValue.toLocaleString()}
            {suffix}
        </span>
    )
}

/* ============================================================================
   📈 STAT CARD COMPONENT
   ============================================================================ */

interface StatCardProps {
    stat: typeof STATS[0]
    index: number
}

function StatCard({ stat, index }: StatCardProps) {
    const Icon = stat.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 40, scale: 0.9 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{
                duration: 0.6,
                delay: index * 0.1,
                ease: [0.16, 1, 0.3, 1],
            }}
            className="group relative"
        >
            {/* Outer glow effect */}
            <motion.div
                className="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-700"
                style={{ background: stat.glowColor }}
            />

            <div
                className={cn(
                    "relative h-full p-6 rounded-2xl overflow-hidden",
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
                        background: `radial-gradient(circle at 50% 0%, ${stat.glowColor} 0%, transparent 60%)`,
                    }}
                />

                {/* Content */}
                <div className="relative z-10 flex flex-col items-center text-center">
                    {/* Icon */}
                    <motion.div
                        className={cn(
                            "inline-flex p-3 rounded-xl mb-4",
                            "bg-gradient-to-br",
                            stat.gradient,
                        )}
                        style={{
                            boxShadow: `0 8px 30px -8px ${stat.glowColor}`,
                        }}
                        whileHover={{ scale: 1.1, rotate: 5 }}
                        transition={{ type: "spring", stiffness: 400 }}
                    >
                        <Icon className="w-5 h-5 text-white" />
                    </motion.div>

                    {/* Number */}
                    <div className="mb-2">
                        <motion.div
                            className="text-4xl md:text-5xl font-black text-white"
                            style={{ textShadow: `0 0 30px ${stat.glowColor}` }}
                        >
                            <AnimatedCounter value={stat.value} suffix={stat.suffix} />
                        </motion.div>
                    </div>

                    {/* Label */}
                    <h3 className="text-lg font-bold text-white mb-1">
                        {stat.label}
                    </h3>

                    {/* Description */}
                    <p className="text-sm text-zinc-400">
                        {stat.description}
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   🚀 MAIN COMPONENT — STATS SECTION
   ============================================================================ */

export function StatsSection() {
    return (
        <section className="relative py-32 overflow-hidden bg-[#05050a]">
            {/* Cosmic background elements */}
            <div className="absolute inset-0">
                {/* Base gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#0a0a12] to-[#05050a]" />

                {/* Large ambient glow - centered */}
                <div
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1200px] h-[800px]"
                    style={{
                        background: "radial-gradient(ellipse, rgba(139,92,246,0.08) 0%, transparent 60%)",
                        filter: "blur(80px)",
                    }}
                />

                {/* Secondary glow - cyan accent */}
                <div
                    className="absolute top-1/4 right-1/4 w-[600px] h-[400px]"
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

                {/* Top separator line */}
                <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-500/30 to-transparent" />
            </div>

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
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
                            "text-purple-300 bg-purple-500/15 rounded-full",
                            "border border-purple-500/30"
                        )}
                    >
                        <Sparkles className="w-4 h-4" />
                        Betrodd av Tusentals
                    </div>

                    <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6">
                        Siffror som{" "}
                        <span
                            className="bg-gradient-to-r from-purple-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent"
                            style={{ filter: "drop-shadow(0 0 25px rgba(139,92,246,0.4))" }}
                        >
                            Talar för Sig
                        </span>
                    </h2>

                    <p className="text-lg sm:text-xl text-zinc-400 max-w-3xl mx-auto leading-relaxed">
                        Sveriges största och mest kompletta DevOps-plattform.{" "}
                        <span className="text-white font-medium">Helt gratis, för alltid.</span>
                    </p>
                </motion.div>

                {/* Stats grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
                    {STATS.map((stat, index) => (
                        <StatCard key={stat.id} stat={stat} index={index} />
                    ))}
                </div>

                {/* Bottom highlight */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                    className="flex items-center justify-center mt-16"
                >
                    <div
                        className={cn(
                            "flex items-center gap-3 px-6 py-3 rounded-full",
                            "bg-emerald-500/10",
                            "border border-emerald-400/30"
                        )}
                    >
                        <Sparkles className="w-5 h-5 text-emerald-400" />
                        <span className="text-sm font-medium text-emerald-300">
                            100% Gratis • Ingen registrering • Börja direkt
                        </span>
                    </div>
                </motion.div>
            </div>
        </section>
    )
}

export default StatsSection
