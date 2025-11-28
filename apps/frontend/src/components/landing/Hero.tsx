"use client"

/**
 * ============================================================================
 * HERO SECTION — Premium Landing Experience
 * ============================================================================
 *
 * Design Philosophy:
 * - Apple: Clean, aspirational, breathing space
 * - Netflix: Dark elegance, immersive gradients
 * - Stripe: Energetic, technically sophisticated
 *
 * Features:
 * - Animated gradient background with subtle movement
 * - Staggered text animations for cinematic reveal
 * - Floating grid particles for depth
 * - Premium glassmorphism stats cards
 * - Responsive design with mobile-first approach
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    ArrowRight,
    Play,
    Sparkles,
    Clock,
    BookOpen,
    Target,
} from "lucide-react"

/* ============================================================================
   ANIMATED BACKGROUND
   ============================================================================ */

function AnimatedBackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* Base gradient */}
            <div className="absolute inset-0 bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950" />

            {/* Animated gradient orbs */}
            <motion.div
                className="absolute top-1/4 -left-1/4 w-[600px] h-[600px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%)",
                }}
                animate={{
                    x: [0, 50, 0],
                    y: [0, 30, 0],
                    scale: [1, 1.1, 1],
                }}
                transition={{
                    duration: 20,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />
            <motion.div
                className="absolute bottom-1/4 -right-1/4 w-[500px] h-[500px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 70%)",
                }}
                animate={{
                    x: [0, -40, 0],
                    y: [0, -50, 0],
                    scale: [1, 1.15, 1],
                }}
                transition={{
                    duration: 25,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />
            <motion.div
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full"
                style={{
                    background: "radial-gradient(circle, rgba(6,182,212,0.08) 0%, transparent 70%)",
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.5, 0.8, 0.5],
                }}
                transition={{
                    duration: 15,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Grid overlay */}
            <div
                className="absolute inset-0 opacity-[0.02]"
                style={{
                    backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                                      linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
                    backgroundSize: "100px 100px",
                }}
            />

            {/* Noise texture */}
            <div
                className="absolute inset-0 opacity-[0.015]"
                style={{
                    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
                }}
            />

            {/* Bottom fade */}
            <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-neutral-950 to-transparent" />
        </div>
    )
}

/* ============================================================================
   FLOATING PARTICLES
   ============================================================================ */

function FloatingParticles() {
    const particles = React.useMemo(() =>
        Array.from({ length: 20 }, (_, i) => ({
            id: i,
            size: Math.random() * 4 + 2,
            x: Math.random() * 100,
            y: Math.random() * 100,
            duration: Math.random() * 20 + 20,
            delay: Math.random() * 5,
        })), [])

    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {particles.map((particle) => (
                <motion.div
                    key={particle.id}
                    className="absolute rounded-full bg-white/20"
                    style={{
                        width: particle.size,
                        height: particle.size,
                        left: `${particle.x}%`,
                        top: `${particle.y}%`,
                    }}
                    animate={{
                        y: [0, -100, 0],
                        opacity: [0, 0.6, 0],
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
   STATS CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    value: string
    label: string
    delay?: number
}

function StatCard({ icon, value, label, delay = 0 }: StatCardProps) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.8 + delay }}
            className={cn(
                "flex items-center gap-3 px-5 py-3",
                "bg-white/5 backdrop-blur-md",
                "border border-white/10 rounded-xl",
                "hover:bg-white/10 hover:border-white/20",
                "transition-all duration-300 group"
            )}
        >
            <div className="p-2 rounded-lg bg-gradient-to-br from-primary-500/20 to-purple-500/20 text-primary-400 group-hover:scale-110 transition-transform duration-300">
                {icon}
            </div>
            <div>
                <div className="text-xl font-bold text-white">{value}</div>
                <div className="text-xs text-neutral-400">{label}</div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   HERO COMPONENT
   ============================================================================ */

export function Hero() {
    return (
        <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Background layers */}
            <AnimatedBackground />
            <FloatingParticles />

            {/* Content */}
            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
                {/* Badge */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6 }}
                    className="inline-flex items-center gap-2 px-4 py-2 mb-8 rounded-full bg-white/5 border border-white/10 backdrop-blur-sm"
                >
                    <Sparkles className="w-4 h-4 text-amber-400" />
                    <span className="text-sm text-neutral-300">
                        Bootcamp v3.0 — Now Live
                    </span>
                </motion.div>

                {/* Main headline */}
                <motion.h1
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight mb-6"
                >
                    <span className="text-white">Master DevOps.</span>
                    <br />
                    <span className="bg-gradient-to-r from-primary-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                        Build Your Career.
                    </span>
                </motion.h1>

                {/* Subheadline */}
                <motion.p
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="text-lg sm:text-xl text-neutral-400 max-w-2xl mx-auto mb-10 leading-relaxed"
                >
                    A comprehensive learning platform with{" "}
                    <span className="text-white font-medium">15 modules</span>,{" "}
                    <span className="text-white font-medium">60+ hands-on labs</span>, and{" "}
                    <span className="text-white font-medium">real-world projects</span>.
                    From Linux basics to Kubernetes mastery.
                </motion.p>

                {/* CTA Buttons */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16"
                >
                    <Link href="/register">
                        <Button
                            size="xl"
                            variant="gradient"
                            className="gap-2 min-w-[200px] shadow-2xl shadow-primary-500/25"
                            rightIcon={<ArrowRight className="w-5 h-5" />}
                        >
                            Start Learning Free
                        </Button>
                    </Link>
                    <Link href="#curriculum">
                        <Button
                            size="xl"
                            variant="glass"
                            className="gap-2 min-w-[200px] text-white"
                            leftIcon={<Play className="w-4 h-4" />}
                        >
                            View Curriculum
                        </Button>
                    </Link>
                </motion.div>

                {/* Stats row */}
                <div className="flex flex-wrap items-center justify-center gap-4 sm:gap-6">
                    <StatCard
                        icon={<Clock className="w-5 h-5" />}
                        value="200+"
                        label="Hours of Content"
                        delay={0}
                    />
                    <StatCard
                        icon={<BookOpen className="w-5 h-5" />}
                        value="15"
                        label="Modules"
                        delay={0.1}
                    />
                    <StatCard
                        icon={<Target className="w-5 h-5" />}
                        value="4"
                        label="Career Tracks"
                        delay={0.2}
                    />
                </div>
            </div>

            {/* Scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.5, duration: 0.6 }}
                className="absolute bottom-8 left-1/2 -translate-x-1/2"
            >
                <motion.div
                    animate={{ y: [0, 8, 0] }}
                    transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                    className="w-6 h-10 rounded-full border-2 border-white/20 flex items-start justify-center p-2"
                >
                    <motion.div
                        animate={{ opacity: [0.5, 1, 0.5] }}
                        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                        className="w-1.5 h-1.5 rounded-full bg-white/60"
                    />
                </motion.div>
            </motion.div>
        </section>
    )
}

export default Hero
