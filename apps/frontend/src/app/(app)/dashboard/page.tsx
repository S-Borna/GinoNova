"use client"

/**
 * ============================================================================
 * DASHBOARD PAGE — COSMIC EDITION 🌌
 * ============================================================================
 *
 * The MOTHERSHIP - Command Center for DevOps Learning
 *
 * Design Philosophy (COSMIC GLOW UP):
 * - Deep space background (#05050a)
 * - Multi-layered aurora orbs (purple/cyan/pink)
 * - Pulsating icon glows
 * - Netflix-smooth animations [0.16, 1, 0.3, 1]
 * - Premium glassmorphism with cosmic glow
 *
 * @phase MILESTONE-2.0-COSMIC
 */

import { useEffect, useState, useCallback } from "react"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { getDashboardSummary, DashboardSummary } from "@/lib/dashboard"
import { motion } from "framer-motion"
import Link from "next/link"
import { AIRecommendations } from "@/components/dashboard/AIRecommendations"
import { FeatureShowcase } from "@/components/dashboard/FeatureShowcase"
import { ContinueLearning } from "@/components/dashboard/ContinueLearning"
import { DallasAssistant } from "@/components/ai/DallasAssistant"

// 🛡️ SECURITY: Disable prefetching on all links
const SecureLink = ({ href, children, className }: { href: string; children: React.ReactNode; className?: string }) => (
    <Link href={href} prefetch={false} className={className}>{children}</Link>
)

// @saas/ui Design System
import { PageLayout, Section } from "@saas/ui"

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            {/* Deep cosmic base */}
            <div className="absolute inset-0 bg-[#05050a]" />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />

            {/* Aurora orb 1 - Purple (top right) */}
            <motion.div
                className="absolute -top-40 -right-40 w-[800px] h-[800px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, rgba(139, 92, 246, 0.05) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.1, 1],
                    opacity: [0.6, 0.8, 0.6],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "easeInOut"
                }}
            />

            {/* Aurora orb 2 - Cyan (bottom left) */}
            <motion.div
                className="absolute -bottom-60 -left-60 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(34, 211, 238, 0.12) 0%, rgba(34, 211, 238, 0.04) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.15, 1],
                    opacity: [0.5, 0.7, 0.5],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                    delay: 2
                }}
            />

            {/* Aurora orb 3 - Pink (center) */}
            <motion.div
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(236, 72, 153, 0.08) 0%, rgba(236, 72, 153, 0.02) 40%, transparent 70%)',
                }}
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.4, 0.6, 0.4],
                }}
                transition={{
                    duration: 12,
                    repeat: Infinity,
                    ease: "easeInOut",
                    delay: 4
                }}
            />
        </div>
    )
}

// UI Components
import { Button } from "@/components/ui/button"
import {
    RefreshCw,
    Zap,
    Flame,
    BookOpen,
    Target,
    Trophy,
    Sparkles,
    Star,
    Rocket,
    ArrowRight,
    Play,
    Clock,
    TrendingUp,
    ChevronRight,
} from "lucide-react"

/* ============================================================================
   HELPERS
   ============================================================================ */

function calculateLevel(xp: number): { level: number; currentXP: number; xpToNextLevel: number } {
    let level = 1
    let totalXPForLevel = 100
    let remainingXP = xp

    while (remainingXP >= totalXPForLevel) {
        remainingXP -= totalXPForLevel
        level++
        totalXPForLevel = Math.floor(100 * Math.pow(1.5, level - 1))
    }

    return {
        level,
        currentXP: remainingXP,
        xpToNextLevel: totalXPForLevel,
    }
}

/* ============================================================================
   COSMIC HERO - Command Center Header
   ============================================================================ */

function PremiumHero({ userName, level, streak }: { userName: string; level: number; streak: number }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative overflow-hidden rounded-3xl",
                "bg-gradient-to-br from-[#0a0a0f] via-purple-950/20 to-[#0a0a0f]",
                "border border-purple-500/20",
                "p-8 md:p-10",
                "shadow-[0_0_80px_rgba(139,92,246,0.15)]"
            )}
        >
            {/* Cosmic glow effects */}
            <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-purple-500/10 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/4" />
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-cyan-500/8 rounded-full blur-[100px] translate-y-1/2 -translate-x-1/4" />
            <div className="absolute top-1/2 left-1/2 w-[400px] h-[400px] bg-pink-500/5 rounded-full blur-[80px] -translate-x-1/2 -translate-y-1/2" />

            {/* Subtle grid overlay */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(139, 92, 246, 0.5) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.5) 1px, transparent 1px)
                    `,
                    backgroundSize: '40px 40px'
                }}
            />

            {/* Animated cosmic particles */}
            <motion.div
                className="absolute top-8 right-20 text-purple-400/60"
                animate={{
                    rotate: 360,
                    scale: [1, 1.3, 1],
                    opacity: [0.4, 0.8, 0.4]
                }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
            >
                <Sparkles className="w-6 h-6" />
            </motion.div>
            <motion.div
                className="absolute bottom-12 right-40 text-cyan-400/40"
                animate={{
                    rotate: -360,
                    scale: [1, 1.4, 1],
                    opacity: [0.3, 0.7, 0.3]
                }}
                transition={{ duration: 5, repeat: Infinity, delay: 1, ease: "easeInOut" }}
            >
                <Star className="w-5 h-5" />
            </motion.div>
            <motion.div
                className="absolute top-1/2 right-16 text-pink-400/30"
                animate={{ y: [0, -15, 0], opacity: [0.3, 0.6, 0.3] }}
                transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
            >
                <Zap className="w-4 h-4" />
            </motion.div>

            <div className="relative flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                <div>
                    <motion.div
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                        className="flex items-center gap-3 mb-3"
                    >
                        {/* Pulsating icon container */}
                        <motion.div
                            className={cn(
                                "relative p-2.5 rounded-xl",
                                "bg-gradient-to-br from-purple-500/30 to-purple-600/20",
                                "border border-purple-500/40"
                            )}
                            animate={{
                                boxShadow: [
                                    '0 0 20px rgba(139, 92, 246, 0.3)',
                                    '0 0 40px rgba(139, 92, 246, 0.5)',
                                    '0 0 20px rgba(139, 92, 246, 0.3)',
                                ]
                            }}
                            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        >
                            <Rocket className="w-5 h-5 text-purple-400" />
                        </motion.div>
                        <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                            Command Center
                        </span>
                    </motion.div>

                    <motion.h1
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                        className={cn(
                            "text-3xl md:text-4xl lg:text-5xl font-black mb-3",
                            "bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent"
                        )}
                    >
                        Welcome back, {userName}! 🚀
                    </motion.h1>

                    <motion.p
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.4, ease: [0.16, 1, 0.3, 1] }}
                        className="text-zinc-400 text-lg max-w-xl"
                    >
                        Your DevOps journey awaits. Let&apos;s crush some goals today!
                    </motion.p>
                </div>

                {/* Stats badges with cosmic glow */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
                    className="flex gap-4"
                >
                    {/* Level Badge */}
                    <motion.div
                        className={cn(
                            "flex items-center gap-3 px-5 py-4 rounded-2xl",
                            "bg-gradient-to-br from-purple-600/25 to-purple-500/10",
                            "border border-purple-500/40",
                            "backdrop-blur-sm"
                        )}
                        whileHover={{ scale: 1.02 }}
                        animate={{
                            boxShadow: [
                                '0 0 30px rgba(139, 92, 246, 0.2)',
                                '0 0 50px rgba(139, 92, 246, 0.35)',
                                '0 0 30px rgba(139, 92, 246, 0.2)',
                            ]
                        }}
                        transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <motion.div
                            className={cn(
                                "w-12 h-12 rounded-xl",
                                "bg-gradient-to-br from-purple-500 to-purple-700",
                                "flex items-center justify-center"
                            )}
                            animate={{
                                boxShadow: [
                                    '0 0 15px rgba(139, 92, 246, 0.5)',
                                    '0 0 30px rgba(139, 92, 246, 0.8)',
                                    '0 0 15px rgba(139, 92, 246, 0.5)',
                                ]
                            }}
                            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        >
                            <Zap className="w-6 h-6 text-white" />
                        </motion.div>
                        <div>
                            <p className="text-zinc-500 text-xs uppercase tracking-wider">Level</p>
                            <p className="text-2xl font-bold text-purple-400">{level}</p>
                        </div>
                    </motion.div>

                    {/* Streak Badge */}
                    <motion.div
                        className={cn(
                            "flex items-center gap-3 px-5 py-4 rounded-2xl",
                            "bg-gradient-to-br from-orange-600/25 to-orange-500/10",
                            "border border-orange-500/40",
                            "backdrop-blur-sm"
                        )}
                        whileHover={{ scale: 1.02 }}
                        animate={{
                            boxShadow: [
                                '0 0 30px rgba(249, 115, 22, 0.15)',
                                '0 0 50px rgba(249, 115, 22, 0.3)',
                                '0 0 30px rgba(249, 115, 22, 0.15)',
                            ]
                        }}
                        transition={{ duration: 3, repeat: Infinity, ease: "easeInOut", delay: 1 }}
                    >
                        <motion.div
                            className={cn(
                                "w-12 h-12 rounded-xl",
                                "bg-gradient-to-br from-orange-500 to-red-600",
                                "flex items-center justify-center"
                            )}
                            animate={{
                                boxShadow: [
                                    '0 0 15px rgba(249, 115, 22, 0.4)',
                                    '0 0 30px rgba(249, 115, 22, 0.7)',
                                    '0 0 15px rgba(249, 115, 22, 0.4)',
                                ]
                            }}
                            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        >
                            <Flame className="w-6 h-6 text-white" />
                        </motion.div>
                        <div>
                            <p className="text-zinc-500 text-xs uppercase tracking-wider">Streak</p>
                            <p className="text-2xl font-bold text-orange-400">{streak} days</p>
                        </div>
                    </motion.div>
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   COSMIC STAT CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode
    label: string
    value: string | number
    subtext?: string
    color: "purple" | "emerald" | "amber" | "orange" | "blue" | "cyan"
    delay?: number
}

function PremiumStatCard({ icon, label, value, subtext, color, delay = 0 }: StatCardProps) {
    const colorMap = {
        purple: {
            bg: "from-purple-600/25 to-purple-500/5",
            border: "border-purple-500/40",
            glow: [
                '0 0 25px rgba(139, 92, 246, 0.15)',
                '0 0 40px rgba(139, 92, 246, 0.25)',
                '0 0 25px rgba(139, 92, 246, 0.15)',
            ],
            text: "text-purple-400",
            iconBg: "from-purple-500 to-purple-700",
            iconGlow: 'rgba(139, 92, 246, 0.5)',
        },
        emerald: {
            bg: "from-emerald-600/25 to-emerald-500/5",
            border: "border-emerald-500/40",
            glow: [
                '0 0 25px rgba(16, 185, 129, 0.15)',
                '0 0 40px rgba(16, 185, 129, 0.25)',
                '0 0 25px rgba(16, 185, 129, 0.15)',
            ],
            text: "text-emerald-400",
            iconBg: "from-emerald-500 to-teal-600",
            iconGlow: 'rgba(16, 185, 129, 0.5)',
        },
        cyan: {
            bg: "from-cyan-600/25 to-cyan-500/5",
            border: "border-cyan-500/40",
            glow: [
                '0 0 25px rgba(34, 211, 238, 0.15)',
                '0 0 40px rgba(34, 211, 238, 0.25)',
                '0 0 25px rgba(34, 211, 238, 0.15)',
            ],
            text: "text-cyan-400",
            iconBg: "from-cyan-500 to-cyan-600",
            iconGlow: 'rgba(34, 211, 238, 0.5)',
        },
        amber: {
            bg: "from-amber-600/25 to-amber-500/5",
            border: "border-amber-500/40",
            glow: [
                '0 0 25px rgba(245, 158, 11, 0.15)',
                '0 0 40px rgba(245, 158, 11, 0.25)',
                '0 0 25px rgba(245, 158, 11, 0.15)',
            ],
            text: "text-amber-400",
            iconBg: "from-amber-500 to-orange-600",
            iconGlow: 'rgba(245, 158, 11, 0.5)',
        },
        orange: {
            bg: "from-orange-600/25 to-orange-500/5",
            border: "border-orange-500/40",
            glow: [
                '0 0 25px rgba(249, 115, 22, 0.15)',
                '0 0 40px rgba(249, 115, 22, 0.25)',
                '0 0 25px rgba(249, 115, 22, 0.15)',
            ],
            text: "text-orange-400",
            iconBg: "from-orange-500 to-red-600",
            iconGlow: 'rgba(249, 115, 22, 0.5)',
        },
        blue: {
            bg: "from-blue-600/25 to-blue-500/5",
            border: "border-blue-500/40",
            glow: [
                '0 0 25px rgba(59, 130, 246, 0.15)',
                '0 0 40px rgba(59, 130, 246, 0.25)',
                '0 0 25px rgba(59, 130, 246, 0.15)',
            ],
            text: "text-blue-400",
            iconBg: "from-blue-500 to-indigo-600",
            iconGlow: 'rgba(59, 130, 246, 0.5)',
        },
    }

    const styles = colorMap[color] || colorMap.purple

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
            whileHover={{ scale: 1.03, y: -5 }}
            className={cn(
                "relative p-5 rounded-2xl",
                "bg-gradient-to-br",
                styles.bg,
                "border",
                styles.border,
                "backdrop-blur-sm",
                "transition-all duration-300"
            )}
            style={{
                boxShadow: styles.glow[0]
            }}
        >
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-zinc-500 text-sm font-medium mb-1">{label}</p>
                    <p className={cn("text-3xl font-bold", styles.text)}>{value}</p>
                    {subtext && <p className="text-zinc-600 text-xs mt-1">{subtext}</p>}
                </div>
                <motion.div
                    className={cn(
                        "w-11 h-11 rounded-xl",
                        "bg-gradient-to-br",
                        styles.iconBg,
                        "flex items-center justify-center"
                    )}
                    animate={{
                        boxShadow: [
                            `0 0 10px ${styles.iconGlow}`,
                            `0 0 25px ${styles.iconGlow}`,
                            `0 0 10px ${styles.iconGlow}`,
                        ]
                    }}
                    transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
                >
                    {icon}
                </motion.div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   COSMIC QUICK ACTION CARD
   ============================================================================ */

interface QuickActionProps {
    icon: React.ReactNode
    title: string
    description: string
    href: string
    color: "purple" | "emerald" | "amber" | "cyan"
    delay?: number
}

function QuickActionCard({ icon, title, description, href, color, delay = 0 }: QuickActionProps) {
    const colorMap = {
        purple: {
            bg: "hover:from-purple-600/25 hover:to-purple-500/10",
            border: "hover:border-purple-500/50",
            hoverGlow: "hover:shadow-[0_0_50px_rgba(139,92,246,0.25)]",
            iconBg: "from-purple-500 to-purple-700",
            iconGlow: 'rgba(139, 92, 246, 0.6)',
            textHover: "group-hover:text-purple-300",
        },
        emerald: {
            bg: "hover:from-emerald-600/25 hover:to-emerald-500/10",
            border: "hover:border-emerald-500/50",
            hoverGlow: "hover:shadow-[0_0_50px_rgba(16,185,129,0.25)]",
            iconBg: "from-emerald-500 to-teal-600",
            iconGlow: 'rgba(16, 185, 129, 0.6)',
            textHover: "group-hover:text-emerald-300",
        },
        amber: {
            bg: "hover:from-amber-600/25 hover:to-amber-500/10",
            border: "hover:border-amber-500/50",
            hoverGlow: "hover:shadow-[0_0_50px_rgba(245,158,11,0.25)]",
            iconBg: "from-amber-500 to-orange-600",
            iconGlow: 'rgba(245, 158, 11, 0.6)',
            textHover: "group-hover:text-amber-300",
        },
        cyan: {
            bg: "hover:from-cyan-600/25 hover:to-cyan-500/10",
            border: "hover:border-cyan-500/50",
            hoverGlow: "hover:shadow-[0_0_50px_rgba(34,211,238,0.25)]",
            iconBg: "from-cyan-500 to-cyan-600",
            iconGlow: 'rgba(34, 211, 238, 0.6)',
            textHover: "group-hover:text-cyan-300",
        },
    }

    const styles = colorMap[color] || colorMap.purple

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay, ease: [0.16, 1, 0.3, 1] }}
        >
            <Link href={href} prefetch={false}>
                <motion.div
                    className={cn(
                        "group relative p-6 rounded-2xl",
                        "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                        "border border-zinc-800/80",
                        styles.bg,
                        styles.border,
                        styles.hoverGlow,
                        "transition-all duration-300 cursor-pointer"
                    )}
                    whileHover={{ scale: 1.02, y: -3 }}
                >
                    <div className="flex items-start gap-4">
                        <motion.div
                            className={cn(
                                "w-12 h-12 rounded-xl shrink-0",
                                "bg-gradient-to-br",
                                styles.iconBg,
                                "flex items-center justify-center",
                                "group-hover:scale-110 transition-transform duration-300"
                            )}
                            whileHover={{
                                boxShadow: `0 0 30px ${styles.iconGlow}`
                            }}
                        >
                            {icon}
                        </motion.div>
                        <div className="flex-1">
                            <h3 className={cn(
                                "text-lg font-semibold text-white mb-1 transition-colors",
                                styles.textHover
                            )}>
                                {title}
                            </h3>
                            <p className="text-zinc-500 text-sm">{description}</p>
                        </div>
                        <ChevronRight className="w-5 h-5 text-zinc-600 group-hover:text-purple-400 group-hover:translate-x-1 transition-all" />
                    </div>
                </motion.div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   COSMIC XP PROGRESS RING
   ============================================================================ */

function XPProgressRing({ currentXP, xpToNextLevel, level }: { currentXP: number; xpToNextLevel: number; level: number }) {
    const progress = (currentXP / xpToNextLevel) * 100
    const circumference = 2 * Math.PI * 45

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative p-6 rounded-2xl",
                "bg-gradient-to-br from-amber-600/20 to-amber-500/5",
                "border border-amber-500/40",
                "backdrop-blur-sm"
            )}
            style={{
                boxShadow: '0 0 50px rgba(245, 158, 11, 0.15)'
            }}
        >
            <h3 className="text-zinc-400 font-medium mb-4 flex items-center gap-2">
                <motion.div
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.7, 1, 0.7]
                    }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                >
                    <Trophy className="w-4 h-4 text-amber-400" />
                </motion.div>
                XP Progress
            </h3>

            <div className="flex items-center justify-center">
                <div className="relative">
                    <svg width="120" height="120" className="transform -rotate-90">
                        {/* Background circle */}
                        <circle
                            cx="60"
                            cy="60"
                            r="45"
                            stroke="currentColor"
                            strokeWidth="8"
                            fill="none"
                            className="text-zinc-800/50"
                        />
                        {/* Progress circle with glow */}
                        <motion.circle
                            cx="60"
                            cy="60"
                            r="45"
                            stroke="url(#xpGradient)"
                            strokeWidth="8"
                            fill="none"
                            strokeLinecap="round"
                            strokeDasharray={circumference}
                            strokeDashoffset={circumference - (progress / 100) * circumference}
                            initial={{ strokeDashoffset: circumference }}
                            animate={{
                                strokeDashoffset: circumference - (progress / 100) * circumference,
                                filter: [
                                    'drop-shadow(0 0 4px rgba(245, 158, 11, 0.5))',
                                    'drop-shadow(0 0 12px rgba(245, 158, 11, 0.8))',
                                    'drop-shadow(0 0 4px rgba(245, 158, 11, 0.5))',
                                ]
                            }}
                            transition={{
                                strokeDashoffset: { duration: 1.5, ease: [0.16, 1, 0.3, 1] },
                                filter: { duration: 2, repeat: Infinity, ease: "easeInOut" }
                            }}
                        />
                        <defs>
                            <linearGradient id="xpGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stopColor="#F59E0B" />
                                <stop offset="50%" stopColor="#FB923C" />
                                <stop offset="100%" stopColor="#EF4444" />
                            </linearGradient>
                        </defs>
                    </svg>

                    {/* Center content */}
                    <div className="absolute inset-0 flex flex-col items-center justify-center">
                        <motion.span
                            className="text-2xl font-bold text-amber-400"
                            animate={{
                                textShadow: [
                                    '0 0 10px rgba(245, 158, 11, 0.3)',
                                    '0 0 20px rgba(245, 158, 11, 0.6)',
                                    '0 0 10px rgba(245, 158, 11, 0.3)',
                                ]
                            }}
                            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        >
                            {currentXP}
                        </motion.span>
                        <span className="text-xs text-zinc-500">/ {xpToNextLevel} XP</span>
                    </div>
                </div>
            </div>

            <p className="text-center text-zinc-500 text-sm mt-4">
                <span className="text-amber-400 font-semibold">{xpToNextLevel - currentXP}</span> XP to Level {level + 1}
            </p>
        </motion.div>
    )
}

/* ============================================================================
   SKELETON
   ============================================================================ */

function DashboardSkeleton() {
    return (
        <div className="space-y-8 animate-pulse">
            <div className="h-48 rounded-3xl bg-zinc-800/50" />
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {Array.from({ length: 4 }).map((_, i) => (
                    <div key={i} className="h-28 rounded-2xl bg-zinc-800/50" />
                ))}
            </div>
            <div className="grid lg:grid-cols-3 gap-6">
                <div className="lg:col-span-2 h-64 rounded-2xl bg-zinc-800/50" />
                <div className="h-64 rounded-2xl bg-zinc-800/50" />
            </div>
        </div>
    )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function DashboardError({ onRetry, error }: { onRetry: () => void; error: string }) {
    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className={cn(
                "max-w-md mx-auto text-center p-8 rounded-2xl",
                "bg-gradient-to-br from-red-600/10 to-red-500/5",
                "border border-red-500/30"
            )}
        >
            <div className="w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-red-500 to-red-700 flex items-center justify-center">
                <span className="text-4xl">😔</span>
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Unable to load dashboard</h3>
            <p className="text-zinc-400 mb-6">{error}</p>
            <Button onClick={onRetry} className="rounded-xl bg-red-600 hover:bg-red-700">
                <RefreshCw className="h-4 w-4 mr-2" />
                Try Again
            </Button>
        </motion.div>
    )
}

/* ============================================================================
   MAIN DASHBOARD PAGE
   ============================================================================ */

export default function DashboardPage() {
    const { user } = useAuth()
    const [dashboard, setDashboard] = useState<DashboardSummary | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const fetchDashboard = useCallback(
        async (isRefresh = false) => {
            if (!isRefresh) setLoading(true)
            const result = await getDashboardSummary(user?.id)
            if (result.ok) {
                setDashboard(result.data)
                setError(null)
            } else {
                setError(result.message)
            }
            setLoading(false)
        },
        [user?.id]
    )

    useEffect(() => {
        fetchDashboard()
    }, [fetchDashboard])

    const handleRefresh = () => fetchDashboard(true)

    // Calculate stats
    const totalXP = dashboard?.stats?.total_progress_records ?? 0
    const levelInfo = calculateLevel(totalXP * 25)
    const completedModules = dashboard?.progress?.filter((p) => p.module_id && p.status === "completed").length ?? 0
    const totalModules = dashboard?.stats?.total_modules ?? 0
    const totalTasks = dashboard?.stats?.total_tasks ?? 0
    const completedTasks = dashboard?.progress?.filter((p) => p.status === "completed").length ?? 0
    const streak = 0

    const userName = user?.full_name?.split(" ")[0] || user?.email?.split("@")[0] || "DevOps Pro"

    return (
        <PageLayout maxWidth="wide" background="cosmic">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            {loading ? (
                <DashboardSkeleton />
            ) : error && !dashboard ? (
                <DashboardError error={error} onRetry={handleRefresh} />
            ) : (
                <div className="relative z-10 space-y-8">
                    {/* Premium Hero */}
                    <PremiumHero
                        userName={userName}
                        level={levelInfo.level}
                        streak={streak}
                    />

                    {/* Stats Grid */}
                    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
                        <PremiumStatCard
                            icon={<Zap className="w-5 h-5 text-white" />}
                            label="Total XP"
                            value={levelInfo.level * 100 + levelInfo.currentXP}
                            subtext="Keep earning!"
                            color="amber"
                            delay={0.1}
                        />
                        <PremiumStatCard
                            icon={<Target className="w-5 h-5 text-white" />}
                            label="Tasks Done"
                            value={completedTasks}
                            subtext={`of ${totalTasks} tasks`}
                            color="cyan"
                            delay={0.2}
                        />
                        <PremiumStatCard
                            icon={<BookOpen className="w-5 h-5 text-white" />}
                            label="Modules"
                            value={completedModules}
                            subtext={`of ${totalModules} completed`}
                            color="purple"
                            delay={0.3}
                        />
                        <PremiumStatCard
                            icon={<Flame className="w-5 h-5 text-white" />}
                            label="Streak"
                            value={`${streak} days`}
                            subtext="Don't break it!"
                            color="orange"
                            delay={0.4}
                        />
                    </div>

                    {/* Continue Learning - Most Important CTA */}
                    <ContinueLearning />

                    {/* What's New - Feature Showcase */}
                    <FeatureShowcase />

                    {/* AI-Powered Recommendations */}
                    <AIRecommendations />

                    {/* Quick Actions + XP Progress */}
                    <div className="grid lg:grid-cols-3 gap-6">
                        {/* Quick Actions */}
                        <div className="lg:col-span-2 space-y-4">
                            <h2 className="text-xl font-bold text-white flex items-center gap-2">
                                <motion.div
                                    animate={{
                                        scale: [1, 1.15, 1],
                                        opacity: [0.8, 1, 0.8]
                                    }}
                                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                                >
                                    <Play className="w-5 h-5 text-purple-400" />
                                </motion.div>
                                Quick Actions
                            </h2>
                            <div className="grid md:grid-cols-2 gap-4">
                                <QuickActionCard
                                    icon={<BookOpen className="w-5 h-5 text-white" />}
                                    title="Continue Learning"
                                    description="Jump back into your modules"
                                    href="/modules"
                                    color="purple"
                                    delay={0.5}
                                />
                                <QuickActionCard
                                    icon={<Clock className="w-5 h-5 text-white" />}
                                    title="Study Session"
                                    description="Start a focused learning session"
                                    href="/studyflow"
                                    color="cyan"
                                    delay={0.6}
                                />
                                <QuickActionCard
                                    icon={<TrendingUp className="w-5 h-5 text-white" />}
                                    title="View Progress"
                                    description="Track your learning journey"
                                    href="/progress"
                                    color="amber"
                                    delay={0.7}
                                />
                                <QuickActionCard
                                    icon={<Target className="w-5 h-5 text-white" />}
                                    title="Skillpath Board"
                                    description="Plan your DevOps career path"
                                    href="/skillpath-board"
                                    color="emerald"
                                    delay={0.8}
                                />
                            </div>
                        </div>

                        {/* XP Progress */}
                        <XPProgressRing
                            currentXP={levelInfo.currentXP}
                            xpToNextLevel={levelInfo.xpToNextLevel}
                            level={levelInfo.level}
                        />
                    </div>
                </div>
            )}

            {/* Dallas AI Assistant - Floating Chat */}
            <DallasAssistant />
        </PageLayout>
    )
}
