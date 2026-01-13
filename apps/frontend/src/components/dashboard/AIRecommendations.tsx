"use client"

/**
 * ============================================================================
 * 🤖 AI RECOMMENDATIONS — SMART NEXT STEPS
 * ============================================================================
 *
 * AI-powered recommendations showing what to learn next based on:
 * - Current progress
 * - Skill gaps
 * - Industry trends
 * - Career goals
 *
 * Design: Cosmic gradient cards with pulsating AI icon
 *
 * @phase MILESTONE-3.0-DASHBOARD-ENHANCEMENT
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import Link from "next/link"
import {
    Brain,
    Sparkles,
    TrendingUp,
    Clock,
    ChevronRight,
    Zap,
} from "lucide-react"

/* ============================================================================
   RECOMMENDATION DATA (Will be AI-powered in future)
   ============================================================================ */

interface Recommendation {
    id: string
    title: string
    reason: string
    moduleSlug: string
    priority: "high" | "medium" | "low"
    estimatedTime: string
    skillGap: string
    icon: React.ElementType
    color: {
        from: string
        to: string
        glow: string
    }
}

const RECOMMENDATIONS: Recommendation[] = [
    {
        id: "k8s",
        title: "Kubernetes Fundamentals",
        reason: "95% of DevOps jobs require Kubernetes",
        moduleSlug: "/modules/kubernetes-fundamentals",
        priority: "high",
        estimatedTime: "2h",
        skillGap: "Container orchestration",
        icon: TrendingUp,
        color: {
            from: "#8b5cf6",
            to: "#a855f7",
            glow: "rgba(139,92,246,0.4)",
        },
    },
    {
        id: "cicd",
        title: "CI/CD Pipelines Advanced",
        reason: "Complement your Docker knowledge",
        moduleSlug: "/modules/cicd-advanced",
        priority: "high",
        estimatedTime: "1.5h",
        skillGap: "Automation & deployment",
        icon: Zap,
        color: {
            from: "#06b6d4",
            to: "#0891b2",
            glow: "rgba(6,182,212,0.4)",
        },
    },
    {
        id: "aws",
        title: "AWS Cloud Fundamentals",
        reason: "Most companies use AWS infrastructure",
        moduleSlug: "/modules/aws-fundamentals",
        priority: "medium",
        estimatedTime: "2.5h",
        skillGap: "Cloud computing",
        icon: Sparkles,
        color: {
            from: "#ec4899",
            to: "#db2777",
            glow: "rgba(236,72,153,0.4)",
        },
    },
]

/* ============================================================================
   RECOMMENDATION CARD COMPONENT
   ============================================================================ */

interface RecommendationCardProps {
    recommendation: Recommendation
    index: number
}

function RecommendationCard({ recommendation, index }: RecommendationCardProps) {
    const Icon = recommendation.icon

    const priorityColors = {
        high: "text-emerald-400 bg-emerald-500/15 border-emerald-500/30",
        medium: "text-amber-400 bg-amber-500/15 border-amber-500/30",
        low: "text-blue-400 bg-blue-500/15 border-blue-500/30",
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1, duration: 0.5 }}
            className="group relative"
        >
            {/* Outer glow on hover */}
            <motion.div
                className="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-700"
                style={{ background: recommendation.color.glow }}
            />

            <Link href={recommendation.moduleSlug} prefetch={false}>
                <div
                    className={cn(
                        "relative p-5 rounded-2xl overflow-hidden cursor-pointer h-full",
                        "bg-gradient-to-br from-[#0d0d14]/90 to-[#0a0a0f]/90",
                        "border border-white/10",
                        "group-hover:border-white/25",
                        "transition-all duration-500"
                    )}
                >
                    {/* Animated gradient background */}
                    <motion.div
                        className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-700"
                        style={{
                            background: `radial-gradient(circle at 50% 0%, ${recommendation.color.glow} 0%, transparent 60%)`,
                        }}
                    />

                    {/* Content */}
                    <div className="relative z-10">
                        {/* Header: Icon + Priority */}
                        <div className="flex items-start justify-between mb-3">
                            <motion.div
                                className="p-2.5 rounded-xl"
                                style={{
                                    background: `linear-gradient(135deg, ${recommendation.color.from}, ${recommendation.color.to})`,
                                    boxShadow: `0 8px 25px -8px ${recommendation.color.glow}`,
                                }}
                                whileHover={{ scale: 1.1, rotate: 5 }}
                                transition={{ type: "spring", stiffness: 400 }}
                            >
                                <Icon className="w-5 h-5 text-white" />
                            </motion.div>

                            <span
                                className={cn(
                                    "text-xs font-semibold px-2.5 py-1 rounded-full border uppercase",
                                    priorityColors[recommendation.priority]
                                )}
                            >
                                {recommendation.priority}
                            </span>
                        </div>

                        {/* Title */}
                        <h3 className="text-base font-bold text-white mb-2 group-hover:text-white/95">
                            {recommendation.title}
                        </h3>

                        {/* Reason */}
                        <p className="text-sm text-zinc-400 mb-3 leading-relaxed">
                            {recommendation.reason}
                        </p>

                        {/* Metadata row */}
                        <div className="flex items-center justify-between pt-3 border-t border-white/10">
                            <div className="flex items-center gap-3 text-xs text-zinc-500">
                                <span className="flex items-center gap-1">
                                    <Clock className="w-3.5 h-3.5" />
                                    {recommendation.estimatedTime}
                                </span>
                                <span className="text-zinc-700">•</span>
                                <span>{recommendation.skillGap}</span>
                            </div>

                            <ChevronRight className="w-4 h-4 text-zinc-600 group-hover:text-white group-hover:translate-x-1 transition-all duration-300" />
                        </div>
                    </div>
                </div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function AIRecommendations() {
    return (
        <div className="space-y-4">
            {/* Section Header */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                    <motion.div
                        animate={{
                            scale: [1, 1.2, 1],
                            rotate: [0, 180, 360],
                        }}
                        transition={{
                            duration: 4,
                            repeat: Infinity,
                            ease: "easeInOut",
                        }}
                    >
                        <Brain className="w-6 h-6 text-purple-400" />
                    </motion.div>
                    <div>
                        <h2 className="text-xl font-bold text-white">
                            Dallas rekommenderar
                        </h2>
                        <p className="text-sm text-zinc-500">
                            AI-drivna förslag baserade på din progress
                        </p>
                    </div>
                </div>

                <motion.div
                    className="px-3 py-1.5 rounded-full bg-purple-500/15 border border-purple-500/30"
                    animate={{
                        boxShadow: [
                            "0 0 20px rgba(139,92,246,0.2)",
                            "0 0 30px rgba(139,92,246,0.4)",
                            "0 0 20px rgba(139,92,246,0.2)",
                        ],
                    }}
                    transition={{ duration: 2, repeat: Infinity }}
                >
                    <span className="text-xs font-semibold text-purple-300 uppercase tracking-wide">
                        AI-Powered
                    </span>
                </motion.div>
            </div>

            {/* Recommendations Grid */}
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                {RECOMMENDATIONS.map((rec, index) => (
                    <RecommendationCard
                        key={rec.id}
                        recommendation={rec}
                        index={index}
                    />
                ))}
            </div>
        </div>
    )
}

export default AIRecommendations
