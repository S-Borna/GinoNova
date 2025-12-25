"use client"

/**
 * ============================================================================
 * 🛤️ TRACKS PREVIEW — COSMIC LEARNING PATHS 🛤️
 * ============================================================================
 *
 * Four stunning career tracks displayed as holographic cards
 * with cosmic particle effects and premium hover states.
 *
 * Design Philosophy:
 * - Each track is a portal to mastery
 * - Cards feel like floating holographic displays
 * - Swedish text for local audience
 * - Clear progression path visible
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Terminal,
    Cloud,
    Container,
    Rocket,
    ChevronRight,
    Clock,
    BookOpen,
    Sparkles,
    ArrowRight,
} from "lucide-react"

/* ============================================================================
   🎯 TRACK DATA — SWEDISH VERSION
   ============================================================================ */

const TRACKS = [
    {
        id: "foundation",
        name: "Foundation",
        tagline: "Bygg din grund",
        description: "Bemästra grunderna: Linux, Shell scripting, Git workflows, och Python automation. Perfekt start för alla.",
        icon: Terminal,
        modules: 5,
        hours: 80,
        color: "#6366f1",
        accentColor: "indigo",
        gradient: "from-indigo-500 to-violet-600",
        glowColor: "rgba(99,102,241,0.4)",
        topics: ["Linux Mastery", "Shell Scripting", "Git & GitHub", "Python Basics"],
    },
    {
        id: "cloud",
        name: "Cloud & Infrastructure",
        tagline: "Skala till molnet",
        description: "Deploya och hantera infrastruktur på AWS med Terraform och serverless arkitekturer.",
        icon: Cloud,
        modules: 4,
        hours: 70,
        color: "#8b5cf6",
        accentColor: "purple",
        gradient: "from-violet-500 to-purple-600",
        glowColor: "rgba(139,92,246,0.4)",
        topics: ["AWS Services", "Terraform IaC", "Serverless", "Networking"],
    },
    {
        id: "containers",
        name: "Containers & K8s",
        tagline: "Containerize allt",
        description: "Master Docker och Kubernetes för modern applikationsdeploy och skalning.",
        icon: Container,
        modules: 3,
        hours: 60,
        color: "#06b6d4",
        accentColor: "cyan",
        gradient: "from-cyan-500 to-teal-600",
        glowColor: "rgba(6,182,212,0.4)",
        topics: ["Docker", "Docker Compose", "Kubernetes", "Helm Charts"],
    },
    {
        id: "platform",
        name: "Platform Engineering",
        tagline: "Bygg produktionssystem",
        description: "Implementera GitOps, observability, och SRE-principer för production-grade plattformar.",
        icon: Rocket,
        modules: 3,
        hours: 60,
        color: "#f97316",
        accentColor: "orange",
        gradient: "from-orange-500 to-red-600",
        glowColor: "rgba(249,115,22,0.4)",
        topics: ["GitOps & ArgoCD", "Monitoring", "SRE Practices", "DevSecOps"],
    },
]

/* ============================================================================
   🌟 HOLOGRAPHIC TRACK CARD
   ============================================================================ */

interface TrackCardProps {
    track: typeof TRACKS[0]
    index: number
}

function TrackCard({ track, index }: TrackCardProps) {
    const Icon = track.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 40, rotateX: -10 }}
            whileInView={{ opacity: 1, y: 0, rotateX: 0 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{
                duration: 0.8,
                delay: index * 0.15,
                ease: [0.16, 1, 0.3, 1]
            }}
            className="group relative"
        >
            {/* Outer glow effect */}
            <motion.div
                className="absolute -inset-2 rounded-3xl opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-700"
                style={{ background: track.glowColor }}
            />

            {/* Card */}
            <Link href={`/skillsmaps?track=${track.id}`}>
                <div
                    className={cn(
                        "relative h-full p-6 rounded-2xl overflow-hidden cursor-pointer",
                        "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                        "border border-white/10",
                        "group-hover:border-white/25",
                        "transition-all duration-500"
                    )}
                    style={{
                        boxShadow: "0 20px 50px -15px rgba(0,0,0,0.5)",
                    }}
                >
                    {/* Animated background gradient */}
                    <motion.div
                        className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700"
                        style={{
                            background: `radial-gradient(circle at 50% 0%, ${track.glowColor} 0%, transparent 60%)`,
                        }}
                    />

                    {/* Holographic shimmer */}
                    <motion.div
                        className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                        style={{
                            background: "linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.08) 45%, rgba(255,255,255,0.04) 50%, transparent 55%)",
                        }}
                        animate={{
                            x: ["-100%", "200%"],
                        }}
                        transition={{
                            duration: 2,
                            repeat: Infinity,
                            repeatDelay: 3,
                        }}
                    />

                    {/* Content */}
                    <div className="relative z-10">
                        {/* Icon with glow */}
                        <motion.div
                            className={cn(
                                "inline-flex p-3.5 rounded-xl mb-5",
                                "bg-gradient-to-br",
                                track.gradient,
                            )}
                            style={{
                                boxShadow: `0 10px 40px -10px ${track.color}90`,
                            }}
                            whileHover={{ scale: 1.1, rotate: 5 }}
                            transition={{ type: "spring", stiffness: 400 }}
                        >
                            <Icon className="w-6 h-6 text-white" />
                        </motion.div>

                        {/* Title & tagline */}
                        <h3 className="text-xl font-bold text-white mb-1 group-hover:text-white/95">
                            {track.name}
                        </h3>
                        <p
                            className="text-sm font-semibold mb-3"
                            style={{ color: track.color }}
                        >
                            {track.tagline}
                        </p>

                        {/* Description */}
                        <p className="text-zinc-400 text-sm leading-relaxed mb-5">
                            {track.description}
                        </p>

                        {/* Topics as pills */}
                        <div className="flex flex-wrap gap-2 mb-6">
                            {track.topics.map((topic) => (
                                <motion.span
                                    key={topic}
                                    whileHover={{ scale: 1.05 }}
                                    className={cn(
                                        "px-3 py-1.5 text-xs font-semibold rounded-full",
                                        "bg-white/5 text-zinc-300",
                                        "border border-white/10",
                                        "group-hover:bg-white/10 group-hover:border-white/20",
                                        "transition-all duration-300"
                                    )}
                                >
                                    {topic}
                                </motion.span>
                            ))}
                        </div>

                        {/* Stats row */}
                        <div className="flex items-center justify-between pt-4 border-t border-white/10">
                            <div className="flex items-center gap-4">
                                <div className="flex items-center gap-2">
                                    <BookOpen className="w-4 h-4 text-zinc-500" />
                                    <div>
                                        <div className="text-base font-bold text-white">{track.modules}</div>
                                        <div className="text-[10px] text-zinc-500 uppercase tracking-wide">Moduler</div>
                                    </div>
                                </div>
                                <div className="w-px h-8 bg-white/10" />
                                <div className="flex items-center gap-2">
                                    <Clock className="w-4 h-4 text-zinc-500" />
                                    <div>
                                        <div className="text-base font-bold text-white">{track.hours}h</div>
                                        <div className="text-[10px] text-zinc-500 uppercase tracking-wide">Content</div>
                                    </div>
                                </div>
                            </div>

                            {/* Arrow CTA */}
                            <motion.div
                                className={cn(
                                    "p-2.5 rounded-full",
                                    "bg-white/5 text-zinc-400",
                                    "group-hover:text-white",
                                    "transition-all duration-300"
                                )}
                                style={{
                                    background: `linear-gradient(135deg, ${track.color}20, ${track.color}05)`,
                                }}
                                whileHover={{ scale: 1.1 }}
                            >
                                <ArrowRight className="w-5 h-5 group-hover:translate-x-0.5 transition-transform duration-300" />
                            </motion.div>
                        </div>
                    </div>

                    {/* Decorative corner accent */}
                    <div
                        className="absolute top-0 right-0 w-32 h-32 opacity-10"
                        style={{
                            background: `radial-gradient(circle at 100% 0%, ${track.color} 0%, transparent 70%)`,
                        }}
                    />
                </div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   🚀 MAIN COMPONENT — COSMIC TRACKS SECTION
   ============================================================================ */

export function TracksPreview() {
    return (
        <section className="relative py-32 overflow-hidden bg-[#05050a]">
            {/* Cosmic background elements */}
            <div className="absolute inset-0">
                {/* Deep space gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#080811] to-[#05050a]" />

                {/* Ambient aurora glow */}
                <motion.div
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[600px]"
                    style={{
                        background: "radial-gradient(ellipse, rgba(139,92,246,0.08) 0%, transparent 60%)",
                        filter: "blur(60px)",
                    }}
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.5, 0.8, 0.5],
                    }}
                    transition={{
                        duration: 8,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                />

                {/* Grid pattern */}
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
                    <motion.span
                        className={cn(
                            "inline-flex items-center gap-2 px-5 py-2 mb-6",
                            "text-sm font-semibold tracking-wide uppercase",
                            "text-purple-300 bg-purple-500/15 rounded-full",
                            "border border-purple-500/30"
                        )}
                        initial={{ opacity: 0, scale: 0.9 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                    >
                        <Sparkles className="w-4 h-4" />
                        Lärstigar
                    </motion.span>

                    <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6">
                        Fyra vägar till{" "}
                        <span
                            className="bg-gradient-to-r from-purple-400 via-violet-400 to-cyan-400 bg-clip-text text-transparent"
                            style={{ filter: "drop-shadow(0 0 30px rgba(139,92,246,0.4))" }}
                        >
                            DevOps Mastery
                        </span>
                    </h2>

                    <p className="text-lg sm:text-xl text-zinc-400 max-w-3xl mx-auto leading-relaxed">
                        Strukturerade lärstigar som tar dig från nybörjare till
                        production-ready DevOps-ingenjör. Välj din väg och börja idag.
                    </p>
                </motion.div>

                {/* Track cards grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 lg:gap-8">
                    {TRACKS.map((track, index) => (
                        <TrackCard key={track.id} track={track} index={index} />
                    ))}
                </div>

                {/* Bottom stats summary */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.6 }}
                    className="flex items-center justify-center mt-20 gap-8"
                >
                    <div className="h-px w-20 bg-gradient-to-r from-transparent to-purple-500/40" />

                    <div className="flex items-center gap-8 text-sm text-zinc-400">
                        <motion.div
                            whileHover={{ scale: 1.05 }}
                            className="flex items-center gap-2"
                        >
                            <span className="text-2xl font-black text-white">15</span>
                            <span>moduler</span>
                        </motion.div>
                        <div className="w-1 h-1 rounded-full bg-purple-500/50" />
                        <motion.div
                            whileHover={{ scale: 1.05 }}
                            className="flex items-center gap-2"
                        >
                            <span className="text-2xl font-black text-white">270+</span>
                            <span>timmar</span>
                        </motion.div>
                        <div className="w-1 h-1 rounded-full bg-purple-500/50" />
                        <motion.div
                            whileHover={{ scale: 1.05 }}
                            className="flex items-center gap-2"
                        >
                            <span className="text-2xl font-black text-white">60+</span>
                            <span>labs</span>
                        </motion.div>
                    </div>

                    <div className="h-px w-20 bg-gradient-to-l from-transparent to-purple-500/40" />
                </motion.div>
            </div>
        </section>
    )
}

export default TracksPreview
