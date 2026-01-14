"use client"

/**
 * ===========================================================================
 * FEATURE SHOWCASE — New Features Highlight Section
 * ===========================================================================
 *
 * Displays the platform's newest features with stunning visuals
 * to immediately show users what's new and exciting.
 */

import { motion } from "framer-motion"
import Link from "next/link"
import { cn } from "@/lib/utils"
import {
    Code2,
    Users,
    BarChart3,
    Trophy,
    Brain,
    Sparkles,
    ArrowRight,
} from "lucide-react"

/* ============================================================================
   FEATURE DATA
   ============================================================================ */

const NEW_FEATURES = [
    {
        id: "playground",
        title: "Code Playground",
        description: "Test Python, Bash, Docker, K8s direkt i browsern",
        icon: Code2,
        href: "/playground",
        gradient: "from-indigo-500 via-purple-500 to-pink-500",
        iconGradient: "from-indigo-400 to-purple-600",
        badge: "🔥 NEW",
    },
    {
        id: "community",
        title: "Community",
        description: "Forum, reputation system, diskussioner",
        icon: Users,
        href: "/community",
        gradient: "from-pink-500 via-rose-500 to-red-500",
        iconGradient: "from-pink-400 to-rose-600",
        badge: "🔥 NEW",
    },
    {
        id: "analytics",
        title: "Analytics",
        description: "Spåra studietid, insights, benchmarking",
        icon: BarChart3,
        href: "/analytics",
        gradient: "from-cyan-500 via-teal-500 to-emerald-500",
        iconGradient: "from-cyan-400 to-teal-600",
        badge: "🔥 NEW",
    },
    {
        id: "certificates",
        title: "Certificates",
        description: "Tjäna badges, achievements, certifikat",
        icon: Trophy,
        href: "/certificates",
        gradient: "from-amber-500 via-yellow-500 to-orange-500",
        iconGradient: "from-amber-400 to-yellow-600",
        badge: "🔥 NEW",
    },
]

/* ============================================================================
   FEATURE CARD
   ============================================================================ */

interface FeatureCardProps {
    feature: typeof NEW_FEATURES[0]
    index: number
}

function FeatureCard({ feature, index }: FeatureCardProps) {
    const Icon = feature.icon

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                delay: 0.9 + index * 0.1,
                duration: 0.5,
                ease: [0.16, 1, 0.3, 1]
            }}
        >
            <Link href={feature.href} prefetch={false}>
                <motion.div
                    className={cn(
                        "group relative p-5 rounded-2xl overflow-hidden cursor-pointer",
                        "bg-gradient-to-br from-[#0a0a0f]/90 to-[#0d0d14]/90",
                        "border border-white/[0.08]",
                        "hover:border-white/[0.2]",
                        "backdrop-blur-sm",
                        "transition-all duration-500"
                    )}
                    whileHover={{ scale: 1.03, y: -5 }}
                >
                    {/* Gradient glow on hover */}
                    <motion.div
                        className={cn(
                            "absolute inset-0 opacity-0 group-hover:opacity-100",
                            "bg-gradient-to-br",
                            feature.gradient,
                            "blur-xl",
                            "transition-opacity duration-500"
                        )}
                        style={{ transform: "translateZ(-1px)" }}
                    />

                    {/* Content */}
                    <div className="relative z-10">
                        {/* Badge */}
                        <motion.div
                            className={cn(
                                "inline-block px-2 py-0.5 rounded-full text-[10px] font-bold mb-3",
                                "bg-gradient-to-r",
                                feature.gradient,
                                "text-white"
                            )}
                            animate={{
                                scale: [1, 1.05, 1],
                            }}
                            transition={{
                                duration: 2,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        >
                            {feature.badge}
                        </motion.div>

                        {/* Icon */}
                        <motion.div
                            className={cn(
                                "w-12 h-12 rounded-xl mb-3",
                                "bg-gradient-to-br",
                                feature.iconGradient,
                                "flex items-center justify-center",
                                "group-hover:scale-110 transition-transform duration-300"
                            )}
                            animate={{
                                boxShadow: [
                                    '0 0 20px rgba(139, 92, 246, 0.3)',
                                    '0 0 40px rgba(139, 92, 246, 0.5)',
                                    '0 0 20px rgba(139, 92, 246, 0.3)',
                                ]
                            }}
                            transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                        >
                            <Icon className="w-6 h-6 text-white" />
                        </motion.div>

                        {/* Title */}
                        <h3 className="text-lg font-bold text-white mb-1 flex items-center gap-2">
                            {feature.title}
                            <ArrowRight className="w-4 h-4 text-purple-400 group-hover:translate-x-1 group-hover:text-purple-300 transition-all" />
                        </h3>

                        {/* Description */}
                        <p className="text-sm text-zinc-400 group-hover:text-zinc-300 transition-colors">
                            {feature.description}
                        </p>
                    </div>
                </motion.div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function FeatureShowcase() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className="space-y-4"
        >
            {/* Header */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                    <motion.div
                        animate={{
                            rotate: [0, 360],
                            scale: [1, 1.2, 1],
                        }}
                        transition={{
                            rotate: { duration: 20, repeat: Infinity, ease: "linear" },
                            scale: { duration: 2, repeat: Infinity, ease: "easeInOut" }
                        }}
                    >
                        <Sparkles className="w-6 h-6 text-purple-400" />
                    </motion.div>
                    <h2 className="text-2xl font-bold text-white">
                        What's New
                    </h2>
                    <motion.span
                        className={cn(
                            "px-3 py-1 rounded-full text-xs font-bold",
                            "bg-gradient-to-r from-purple-500 to-pink-500",
                            "text-white"
                        )}
                        animate={{
                            scale: [1, 1.05, 1],
                            boxShadow: [
                                '0 0 20px rgba(168, 85, 247, 0.5)',
                                '0 0 30px rgba(168, 85, 247, 0.8)',
                                '0 0 20px rgba(168, 85, 247, 0.5)',
                            ]
                        }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    >
                        4 NEW FEATURES
                    </motion.span>
                </div>
            </div>

            {/* Feature Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
                {NEW_FEATURES.map((feature, index) => (
                    <FeatureCard key={feature.id} feature={feature} index={index} />
                ))}
            </div>
        </motion.div>
    )
}
