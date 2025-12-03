"use client"

/**
 * ============================================================================
 * LEARNING PATH SELECTOR — Choose Between Bootcamp & SkillsMaps
 * ============================================================================
 *
 * After OS selection, users choose their learning path:
 * - Bootcamp v3.0: Structured 4-track curriculum
 * - SkillsMaps: À la carte skill-based learning
 *
 * @phase LEARNING-PATH-SELECTOR
 */

import { useEffect } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { motion } from "framer-motion"
import { PageLayout } from "@saas/ui"
import { usePlatform } from "@/hooks/useOperatingSystem"
import { PlatformSelector, PlatformBadge } from "@/components/onboarding"
import { cn } from "@/lib/utils"
import {
    GraduationCap,
    Map,
    ArrowRight,
    Sparkles,
    BookOpen,
    Target,
    Clock,
    Trophy,
    Zap,
    CheckCircle2,
} from "lucide-react"

/* ============================================================================
   PATH CARD COMPONENT
   ============================================================================ */

interface PathCardProps {
    title: string
    subtitle: string
    description: string
    icon: React.ReactNode
    emoji: string
    color: string
    href: string
    features: string[]
    stats: { label: string; value: string }[]
    recommended?: boolean
    index: number
}

function PathCard({
    title,
    subtitle,
    description,
    icon,
    emoji,
    color,
    href,
    features,
    stats,
    recommended,
    index,
}: PathCardProps) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 + index * 0.15, duration: 0.5 }}
        >
            <Link href={href} className="block group">
                <div
                    className={cn(
                        "relative overflow-hidden rounded-3xl",
                        "bg-gradient-to-br from-zinc-900 via-zinc-900/95 to-zinc-950",
                        "border border-white/10",
                        "p-8 h-full",
                        "transition-all duration-500",
                        "hover:border-white/20",
                        "hover:shadow-2xl"
                    )}
                    style={{
                        boxShadow: `0 0 0 0 ${color}00`,
                    }}
                >
                    {/* Glow effect on hover */}
                    <div
                        className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-3xl"
                        style={{
                            background: `radial-gradient(circle at 50% 0%, ${color}20, transparent 70%)`,
                        }}
                    />

                    {/* Recommended badge */}
                    {recommended && (
                        <motion.div
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ delay: 0.5, type: "spring" }}
                            className={cn(
                                "absolute -top-0 right-6 px-4 py-2 rounded-b-xl",
                                "bg-gradient-to-r from-amber-500 to-orange-500",
                                "text-white text-sm font-bold",
                                "shadow-lg shadow-amber-500/30",
                                "flex items-center gap-2"
                            )}
                        >
                            <Sparkles className="w-4 h-4" />
                            REKOMMENDERAT
                        </motion.div>
                    )}

                    {/* Header */}
                    <div className="relative flex items-start gap-5 mb-6">
                        <motion.div
                            className={cn(
                                "w-20 h-20 rounded-2xl flex items-center justify-center",
                                "bg-gradient-to-br from-white/10 to-white/5",
                                "border border-white/10",
                                "text-4xl"
                            )}
                            whileHover={{ scale: 1.1, rotate: 5 }}
                            style={{
                                boxShadow: `0 0 30px ${color}30`,
                            }}
                        >
                            {emoji}
                        </motion.div>
                        <div className="flex-1">
                            <p
                                className="text-sm font-semibold uppercase tracking-wider mb-1"
                                style={{ color }}
                            >
                                {subtitle}
                            </p>
                            <h2 className="text-2xl font-black text-white">
                                {title}
                            </h2>
                        </div>
                    </div>

                    {/* Description */}
                    <p className="text-zinc-400 mb-6 leading-relaxed">
                        {description}
                    </p>

                    {/* Features */}
                    <div className="space-y-3 mb-6">
                        {features.map((feature, i) => (
                            <div key={i} className="flex items-center gap-3">
                                <CheckCircle2
                                    className="w-5 h-5 shrink-0"
                                    style={{ color }}
                                />
                                <span className="text-sm text-zinc-300">{feature}</span>
                            </div>
                        ))}
                    </div>

                    {/* Stats */}
                    <div className="grid grid-cols-3 gap-4 mb-6 p-4 rounded-xl bg-white/5 border border-white/5">
                        {stats.map((stat, i) => (
                            <div key={i} className="text-center">
                                <p className="text-xl font-bold text-white">{stat.value}</p>
                                <p className="text-xs text-zinc-500">{stat.label}</p>
                            </div>
                        ))}
                    </div>

                    {/* CTA Button */}
                    <motion.div
                        className={cn(
                            "flex items-center justify-center gap-2",
                            "py-4 px-6 rounded-xl",
                            "font-semibold text-white",
                            "transition-all duration-300",
                            "group-hover:gap-4"
                        )}
                        style={{
                            background: `linear-gradient(135deg, ${color}, ${color}cc)`,
                            boxShadow: `0 0 20px ${color}40`,
                        }}
                    >
                        <span>Börja här</span>
                        <ArrowRight className="w-5 h-5 transition-transform group-hover:translate-x-1" />
                    </motion.div>
                </div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   LEARN PAGE
   ============================================================================ */

export default function LearnPage() {
    const router = useRouter()
    const { hasSelected, isLoading: platformLoading, os, distro } = usePlatform()

    // Platform loading
    if (platformLoading) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="animate-pulse space-y-8">
                    <div className="h-32 rounded-3xl bg-zinc-800/50" />
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div className="h-96 rounded-3xl bg-zinc-800/50" />
                        <div className="h-96 rounded-3xl bg-zinc-800/50" />
                    </div>
                </div>
            </PageLayout>
        )
    }

    // Show platform selector if not yet selected
    if (!hasSelected) {
        return (
            <PageLayout maxWidth="wide" background="gray">
                <div className="min-h-[70vh] flex items-center justify-center py-12">
                    <PlatformSelector redirectTo="/learn" />
                </div>
            </PageLayout>
        )
    }

    return (
        <PageLayout maxWidth="wide" background="gray">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center mb-12"
            >
                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ type: "spring", delay: 0.1 }}
                    className={cn(
                        "w-20 h-20 mx-auto mb-6 rounded-2xl",
                        "bg-gradient-to-br from-purple-600 to-indigo-600",
                        "flex items-center justify-center",
                        "shadow-lg shadow-purple-500/30"
                    )}
                >
                    <Target className="w-10 h-10 text-white" />
                </motion.div>

                <h1 className={cn(
                    "text-4xl md:text-5xl font-black mb-4",
                    "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                )}>
                    Välj din lärstig
                </h1>
                <p className="text-xl text-zinc-400 max-w-2xl mx-auto mb-4">
                    Två kraftfulla sätt att lära sig DevOps — välj det som passar dig bäst
                </p>
                <PlatformBadge className="mx-auto" />
            </motion.div>

            {/* Path Cards */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
                <PathCard
                    title="Bootcamp v3.0"
                    subtitle="Strukturerad inlärning"
                    description="En komplett, guidad resa genom DevOps. Perfekt för nybörjare som vill ha en tydlig väg från start till mål. 4 specialiserade tracks, 15 moduler, 384 praktiska tasks."
                    emoji="🎓"
                    icon={<GraduationCap className="w-8 h-8" />}
                    color="#8B5CF6"
                    href="/modules"
                    recommended={true}
                    features={[
                        "Steg-för-steg curriculum",
                        "4 specialiserade tracks",
                        "Praktiska labs & projekt",
                        "Certifieringsförberedelse",
                    ]}
                    stats={[
                        { label: "Moduler", value: "15" },
                        { label: "Tasks", value: "384" },
                        { label: "Labs", value: "83" },
                    ]}
                    index={0}
                />

                <PathCard
                    title="SkillsMaps"
                    subtitle="À la carte"
                    description="Välj exakt vilka färdigheter du vill lära dig. Perfekt för den som redan har viss erfarenhet och vill fördjupa sig i specifika områden. 18 kompletta kunskapsstigar."
                    emoji="🗺️"
                    icon={<Map className="w-8 h-8" />}
                    color="#06B6D4"
                    href="/skillsmaps"
                    features={[
                        "Välj fritt bland 18 SkillsMaps",
                        "Djupdyk i specifika teknologier",
                        "Flexibel ordning",
                        "356 kunskapsnoder",
                    ]}
                    stats={[
                        { label: "SkillsMaps", value: "18" },
                        { label: "Noder", value: "356" },
                        { label: "XP", value: "40K+" },
                    ]}
                    index={1}
                />
            </div>

            {/* Footer note */}
            <motion.p
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.8 }}
                className="text-center text-zinc-500 text-sm mt-12"
            >
                💡 Du kan alltid byta mellan Bootcamp och SkillsMaps via sidomenyn
            </motion.p>
        </PageLayout>
    )
}
