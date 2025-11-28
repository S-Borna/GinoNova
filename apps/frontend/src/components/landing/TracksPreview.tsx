"use client"

/**
 * ============================================================================
 * TRACKS PREVIEW — Four Learning Tracks Showcase
 * ============================================================================
 *
 * Design: Premium cards with track-specific gradients, subtle animations,
 * and a professional grid layout that scales beautifully.
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Terminal,
    Cloud,
    Container,
    Rocket,
    ChevronRight,
} from "lucide-react"

/* ============================================================================
   TRACK DATA
   ============================================================================ */

const TRACKS = [
    {
        id: "foundation",
        name: "Foundation",
        tagline: "Build Your Core Skills",
        description: "Master the fundamentals: Linux, Shell scripting, Git workflows, and Python automation.",
        icon: Terminal,
        modules: 5,
        hours: 80,
        color: "#6366f1",
        gradient: "from-indigo-500 to-violet-600",
        bgGradient: "from-indigo-500/10 to-violet-600/5",
        topics: ["Linux Mastery", "Shell Scripting", "Git & GitHub", "Python Basics"],
    },
    {
        id: "cloud",
        name: "Cloud & Infrastructure",
        tagline: "Scale to the Cloud",
        description: "Deploy and manage infrastructure on AWS with Terraform and serverless architectures.",
        icon: Cloud,
        modules: 4,
        hours: 70,
        color: "#8b5cf6",
        gradient: "from-violet-500 to-purple-600",
        bgGradient: "from-violet-500/10 to-purple-600/5",
        topics: ["AWS Services", "Terraform IaC", "Serverless", "Networking"],
    },
    {
        id: "containers",
        name: "Containers & Orchestration",
        tagline: "Containerize Everything",
        description: "Master Docker and Kubernetes for modern application deployment and scaling.",
        icon: Container,
        modules: 3,
        hours: 60,
        color: "#06b6d4",
        gradient: "from-cyan-500 to-teal-600",
        bgGradient: "from-cyan-500/10 to-teal-600/5",
        topics: ["Docker", "Docker Compose", "Kubernetes", "Helm Charts"],
    },
    {
        id: "platform",
        name: "Platform Engineering",
        tagline: "Build Production Systems",
        description: "Implement GitOps, observability, and SRE practices for production-grade platforms.",
        icon: Rocket,
        modules: 3,
        hours: 60,
        color: "#f97316",
        gradient: "from-orange-500 to-red-600",
        bgGradient: "from-orange-500/10 to-red-600/5",
        topics: ["GitOps & ArgoCD", "Monitoring", "SRE Practices", "DevSecOps"],
    },
]

/* ============================================================================
   TRACK CARD COMPONENT
   ============================================================================ */

interface TrackCardProps {
    track: typeof TRACKS[0]
    index: number
}

function TrackCard({ track, index }: TrackCardProps) {
    const Icon = track.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-50px" }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
            className="group relative"
        >
            {/* Card */}
            <div
                className={cn(
                    "relative h-full p-6 rounded-2xl overflow-hidden",
                    "bg-gradient-to-br",
                    track.bgGradient,
                    "border border-white/10",
                    "hover:border-white/20 hover:shadow-2xl",
                    "transition-all duration-500"
                )}
            >
                {/* Glow effect on hover */}
                <div
                    className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                    style={{
                        background: `radial-gradient(circle at 50% 0%, ${track.color}20 0%, transparent 50%)`,
                    }}
                />

                {/* Content */}
                <div className="relative z-10">
                    {/* Icon */}
                    <div
                        className={cn(
                            "inline-flex p-3 rounded-xl mb-4",
                            "bg-gradient-to-br",
                            track.gradient,
                            "shadow-lg group-hover:scale-110 transition-transform duration-300"
                        )}
                        style={{ boxShadow: `0 10px 40px -10px ${track.color}60` }}
                    >
                        <Icon className="w-6 h-6 text-white" />
                    </div>

                    {/* Title & tagline */}
                    <h3 className="text-xl font-bold text-white mb-1">
                        {track.name}
                    </h3>
                    <p
                        className="text-sm font-medium mb-3"
                        style={{ color: track.color }}
                    >
                        {track.tagline}
                    </p>

                    {/* Description */}
                    <p className="text-neutral-400 text-sm leading-relaxed mb-4">
                        {track.description}
                    </p>

                    {/* Topics */}
                    <div className="flex flex-wrap gap-2 mb-6">
                        {track.topics.map((topic) => (
                            <span
                                key={topic}
                                className="px-2.5 py-1 text-xs font-medium rounded-full bg-white/5 text-neutral-300 border border-white/10"
                            >
                                {topic}
                            </span>
                        ))}
                    </div>

                    {/* Stats */}
                    <div className="flex items-center justify-between pt-4 border-t border-white/10">
                        <div className="flex items-center gap-4">
                            <div>
                                <div className="text-lg font-bold text-white">{track.modules}</div>
                                <div className="text-xs text-neutral-500">Modules</div>
                            </div>
                            <div className="w-px h-8 bg-white/10" />
                            <div>
                                <div className="text-lg font-bold text-white">{track.hours}h</div>
                                <div className="text-xs text-neutral-500">Content</div>
                            </div>
                        </div>

                        {/* Arrow */}
                        <div
                            className="p-2 rounded-full bg-white/5 text-neutral-400 group-hover:text-white group-hover:bg-white/10 transition-all duration-300"
                        >
                            <ChevronRight className="w-5 h-5 group-hover:translate-x-0.5 transition-transform duration-300" />
                        </div>
                    </div>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function TracksPreview() {
    return (
        <section className="relative py-24 bg-neutral-950 overflow-hidden">
            {/* Background gradient */}
            <div className="absolute inset-0">
                <div className="absolute inset-0 bg-gradient-to-b from-neutral-950 via-neutral-900 to-neutral-950" />
                <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent" />
            </div>

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="text-center mb-16"
                >
                    <span className="inline-block px-4 py-1.5 mb-4 text-xs font-semibold tracking-wider uppercase text-primary-400 bg-primary-500/10 rounded-full">
                        Learning Paths
                    </span>
                    <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-4">
                        Four Tracks to{" "}
                        <span className="bg-gradient-to-r from-primary-400 to-purple-400 bg-clip-text text-transparent">
                            DevOps Mastery
                        </span>
                    </h2>
                    <p className="text-lg text-neutral-400 max-w-2xl mx-auto">
                        Progress through structured learning paths designed to take you from
                        beginner to production-ready DevOps engineer.
                    </p>
                </motion.div>

                {/* Track cards grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    {TRACKS.map((track, index) => (
                        <TrackCard key={track.id} track={track} index={index} />
                    ))}
                </div>

                {/* Bottom decoration */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.8 }}
                    whileInView={{ opacity: 1, scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.4 }}
                    className="flex items-center justify-center mt-16 gap-8"
                >
                    <div className="h-px w-16 bg-gradient-to-r from-transparent to-white/20" />
                    <div className="text-sm text-neutral-500">
                        Total: <span className="text-white font-medium">15 modules</span> ·{" "}
                        <span className="text-white font-medium">270+ hours</span> ·{" "}
                        <span className="text-white font-medium">60+ labs</span>
                    </div>
                    <div className="h-px w-16 bg-gradient-to-l from-transparent to-white/20" />
                </motion.div>
            </div>
        </section>
    )
}

export default TracksPreview
