"use client"

/**
 * ============================================================================
 * AUTH BRANDING — Split Screen Branding Panel
 * ============================================================================
 *
 * Premium branding panel for auth pages with animated gradient background,
 * logo, tagline, and feature highlights.
 *
 * @phase A.2 - Authentication UI
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Terminal,
    Sparkles,
    BookOpen,
    Beaker,
    Trophy,
} from "lucide-react"

/* ============================================================================
   FEATURE HIGHLIGHTS
   ============================================================================ */

const FEATURES = [
    {
        icon: BookOpen,
        title: "15 Comprehensive Modules",
        description: "From Linux basics to Kubernetes mastery",
    },
    {
        icon: Beaker,
        title: "60+ Hands-on Labs",
        description: "Real cloud environments, not simulations",
    },
    {
        icon: Trophy,
        title: "Track Your Progress",
        description: "XP system, streaks, and achievements",
    },
]

/* ============================================================================
   ANIMATED BACKGROUND
   ============================================================================ */

function AnimatedBackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* Base gradient */}
            <div className="absolute inset-0 bg-gradient-to-br from-primary-600 via-purple-600 to-primary-800" />

            {/* Animated orbs */}
            <motion.div
                animate={{
                    scale: [1, 1.2, 1],
                    opacity: [0.3, 0.5, 0.3],
                    x: [0, 30, 0],
                    y: [0, -20, 0],
                }}
                transition={{
                    duration: 8,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-cyan-500/30 rounded-full blur-[100px]"
            />
            <motion.div
                animate={{
                    scale: [1.2, 1, 1.2],
                    opacity: [0.2, 0.4, 0.2],
                    x: [0, -20, 0],
                    y: [0, 30, 0],
                }}
                transition={{
                    duration: 10,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-purple-500/30 rounded-full blur-[100px]"
            />

            {/* Grid pattern overlay */}
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                                     linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
                    backgroundSize: "50px 50px",
                }}
            />
        </div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

interface AuthBrandingProps {
    className?: string
}

export function AuthBranding({ className }: AuthBrandingProps) {
    return (
        <div
            className={cn(
                "relative hidden lg:flex flex-col justify-between p-12 text-white",
                className
            )}
        >
            <AnimatedBackground />

            {/* Content */}
            <div className="relative z-10">
                {/* Logo */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6 }}
                    className="flex items-center gap-3"
                >
                    <div className="p-2.5 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20">
                        <Terminal className="w-6 h-6" />
                    </div>
                    <span className="text-2xl font-bold">DevOpsHub</span>
                </motion.div>
            </div>

            {/* Main content */}
            <div className="relative z-10 space-y-8">
                {/* Headline */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.2 }}
                >
                    <h1 className="text-4xl font-bold leading-tight mb-4">
                        Master DevOps.
                        <br />
                        Build Your Career.
                    </h1>
                    <p className="text-lg text-white/70 max-w-md">
                        Join thousands of engineers learning modern DevOps skills
                        through hands-on projects and real-world labs.
                    </p>
                </motion.div>

                {/* Features */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.4 }}
                    className="space-y-4"
                >
                    {FEATURES.map((feature, index) => {
                        const Icon = feature.icon
                        return (
                            <motion.div
                                key={feature.title}
                                initial={{ opacity: 0, x: -20 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ duration: 0.4, delay: 0.5 + index * 0.1 }}
                                className="flex items-start gap-4"
                            >
                                <div className="p-2 rounded-lg bg-white/10 backdrop-blur-sm">
                                    <Icon className="w-5 h-5" />
                                </div>
                                <div>
                                    <div className="font-medium">{feature.title}</div>
                                    <div className="text-sm text-white/60">
                                        {feature.description}
                                    </div>
                                </div>
                            </motion.div>
                        )
                    })}
                </motion.div>
            </div>

            {/* Footer */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 0.6, delay: 0.8 }}
                className="relative z-10"
            >
                <div className="flex items-center gap-2 text-sm text-white/50">
                    <Sparkles className="w-4 h-4" />
                    <span>Free to start • No credit card required</span>
                </div>
            </motion.div>
        </div>
    )
}

export default AuthBranding
