"use client"

/**
 * ============================================================================
 * THE MATRIX - CHOOSE YOUR PATH 🔴🔵
 * ============================================================================
 *
 * "This is your last chance. After this, there is no turning back.
 *  You take the blue pill — the story ends, you wake up and believe
 *  whatever you want to believe. You take the red pill — you stay in
 *  Wonderland, and I show you how deep the rabbit hole goes."
 *                                                    - Morpheus
 *
 * Red Pill = Camp DevOps (structured awakening to DevOps reality)
 * Blue Pill = SkillsMaps (choose your own reality, à la carte)
 *
 * @phase MATRIX-AWAKENING
 */

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { PageLayout } from "@saas/ui"
import { usePlatform } from "@/hooks/useOperatingSystem"
import { PlatformSelector, PlatformBadge } from "@/components/onboarding"
import { cn } from "@/lib/utils"
import {
    ArrowRight,
    Sparkles,
    CheckCircle2,
    Rabbit,
    Eye,
} from "lucide-react"

/* ============================================================================
   MATRIX RAIN EFFECT
   ============================================================================ */

function MatrixRain() {
    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none opacity-20">
            {[...Array(20)].map((_, i) => (
                <motion.div
                    key={i}
                    className="absolute text-green-500 font-mono text-xs"
                    initial={{
                        x: `${Math.random() * 100}%`,
                        y: "-10%",
                        opacity: Math.random() * 0.5 + 0.2,
                    }}
                    animate={{
                        y: "110%",
                        transition: {
                            duration: Math.random() * 10 + 10,
                            repeat: Infinity,
                            ease: "linear",
                            delay: Math.random() * 5,
                        },
                    }}
                >
                    {[...Array(20)].map((_, j) => (
                        <div key={j} className="mb-1">
                            {String.fromCharCode(0x30A0 + Math.random() * 96)}
                        </div>
                    ))}
                </motion.div>
            ))}
        </div>
    )
}

/* ============================================================================
   PILL CARD COMPONENT - MATRIX EDITION
   ============================================================================ */

interface PillCardProps {
    title: string
    subtitle: string
    description: string
    pillColor: "red" | "blue"
    href: string
    features: string[]
    stats: { label: string; value: string }[]
    morpheusQuote: string
    index: number
}

function PillCard({
    title,
    subtitle,
    description,
    pillColor,
    href,
    features,
    stats,
    morpheusQuote,
    index,
}: PillCardProps) {
    const [isHovered, setIsHovered] = useState(false)

    const colors = {
        red: {
            primary: "#EF4444",
            secondary: "#DC2626",
            glow: "rgba(239, 68, 68, 0.4)",
            gradient: "from-red-600 via-red-500 to-orange-500",
            bgGradient: "from-red-950/40 via-zinc-900 to-zinc-950",
            borderGlow: "shadow-[0_0_30px_rgba(239,68,68,0.3)]",
            text: "text-red-400",
        },
        blue: {
            primary: "#3B82F6",
            secondary: "#2563EB",
            glow: "rgba(59, 130, 246, 0.4)",
            gradient: "from-blue-600 via-blue-500 to-cyan-500",
            bgGradient: "from-blue-950/40 via-zinc-900 to-zinc-950",
            borderGlow: "shadow-[0_0_30px_rgba(59,130,246,0.3)]",
            text: "text-blue-400",
        },
    }

    const c = colors[pillColor]

    return (
        <motion.div
            initial={{ opacity: 0, y: 50, rotateY: index === 0 ? 10 : -10 }}
            animate={{ opacity: 1, y: 0, rotateY: 0 }}
            transition={{ delay: 0.3 + index * 0.2, duration: 0.7, type: "spring" }}
            onHoverStart={() => setIsHovered(true)}
            onHoverEnd={() => setIsHovered(false)}
        >
            <Link href={href} className="block group">
                <div
                    className={cn(
                        "relative overflow-hidden rounded-3xl",
                        "bg-gradient-to-br",
                        c.bgGradient,
                        "border-2 transition-all duration-500",
                        isHovered ? "border-white/30" : "border-white/10",
                        "p-8 h-full min-h-[580px]",
                        isHovered && c.borderGlow
                    )}
                >
                    {/* Animated glow orb */}
                    <motion.div
                        className="absolute w-64 h-64 rounded-full blur-[100px] pointer-events-none"
                        animate={{
                            x: isHovered ? "10%" : "-20%",
                            y: isHovered ? "-10%" : "-30%",
                            opacity: isHovered ? 0.6 : 0.3,
                        }}
                        style={{ background: c.glow }}
                        transition={{ duration: 0.8 }}
                    />

                    {/* Pill icon with pulse effect */}
                    <div className="relative flex justify-center mb-8">
                        <motion.div
                            className={cn(
                                "relative w-24 h-24 rounded-full",
                                "bg-gradient-to-br",
                                c.gradient,
                                "flex items-center justify-center",
                                "shadow-2xl"
                            )}
                            animate={{
                                boxShadow: isHovered
                                    ? `0 0 60px ${c.glow}, 0 0 100px ${c.glow}`
                                    : `0 0 30px ${c.glow}`,
                                scale: isHovered ? 1.1 : 1,
                            }}
                            transition={{ duration: 0.4 }}
                        >
                            {/* Rotating ring */}
                            <motion.div
                                className={cn(
                                    "absolute inset-[-4px] rounded-full border-2 border-dashed",
                                    pillColor === "red" ? "border-red-400/40" : "border-blue-400/40"
                                )}
                                animate={{ rotate: 360 }}
                                transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
                            />

                            {/* Pill shape */}
                            <div
                                className={cn(
                                    "w-12 h-6 rounded-full",
                                    "shadow-inner"
                                )}
                                style={{
                                    background: `linear-gradient(135deg, white 0%, ${c.primary} 100%)`,
                                }}
                            />
                        </motion.div>

                        {/* Floating particles around pill */}
                        {isHovered && (
                            <>
                                {[...Array(6)].map((_, i) => (
                                    <motion.div
                                        key={i}
                                        className={cn(
                                            "absolute w-2 h-2 rounded-full",
                                            pillColor === "red" ? "bg-red-400" : "bg-blue-400"
                                        )}
                                        initial={{
                                            x: 0,
                                            y: 0,
                                            opacity: 0,
                                        }}
                                        animate={{
                                            x: Math.cos((i * 60 * Math.PI) / 180) * 60,
                                            y: Math.sin((i * 60 * Math.PI) / 180) * 60,
                                            opacity: [0, 1, 0],
                                        }}
                                        transition={{
                                            duration: 1.5,
                                            repeat: Infinity,
                                            delay: i * 0.1,
                                        }}
                                    />
                                ))}
                            </>
                        )}
                    </div>

                    {/* Title & Subtitle */}
                    <div className="relative text-center mb-6">
                        <motion.p
                            className={cn("text-sm font-bold uppercase tracking-widest mb-2", c.text)}
                            animate={{ opacity: isHovered ? 1 : 0.8 }}
                        >
                            {subtitle}
                        </motion.p>
                        <h2 className="text-3xl font-black text-white tracking-tight">
                            {title}
                        </h2>
                    </div>

                    {/* Morpheus Quote */}
                    <motion.div
                        className={cn(
                            "relative mb-6 p-4 rounded-xl",
                            "bg-black/30 border border-white/10",
                            "italic text-sm text-zinc-400 text-center"
                        )}
                        animate={{ opacity: isHovered ? 1 : 0.7 }}
                    >
                        <span className="text-2xl mr-2">&ldquo;</span>
                        {morpheusQuote}
                        <span className="text-2xl ml-1">&rdquo;</span>
                        <p className={cn("mt-2 text-xs font-semibold not-italic", c.text)}>
                            — Morpheus
                        </p>
                    </motion.div>

                    {/* Description */}
                    <p className="text-zinc-400 mb-6 leading-relaxed text-center">
                        {description}
                    </p>

                    {/* Features */}
                    <div className="space-y-3 mb-6">
                        {features.map((feature, i) => (
                            <motion.div
                                key={i}
                                className="flex items-center gap-3"
                                initial={{ opacity: 0, x: -20 }}
                                animate={{ opacity: 1, x: 0 }}
                                transition={{ delay: 0.5 + i * 0.1 }}
                            >
                                <CheckCircle2
                                    className={cn("w-5 h-5 shrink-0", c.text)}
                                />
                                <span className="text-sm text-zinc-300">{feature}</span>
                            </motion.div>
                        ))}
                    </div>

                    {/* Stats */}
                    <div className={cn(
                        "grid grid-cols-3 gap-3 mb-6 p-4 rounded-xl",
                        "bg-black/30 border border-white/5"
                    )}>
                        {stats.map((stat, i) => (
                            <div key={i} className="text-center">
                                <p className={cn("text-2xl font-black", c.text)}>{stat.value}</p>
                                <p className="text-xs text-zinc-500">{stat.label}</p>
                            </div>
                        ))}
                    </div>

                    {/* CTA Button */}
                    <motion.div
                        className={cn(
                            "flex items-center justify-center gap-3",
                            "py-4 px-6 rounded-xl",
                            "font-bold text-white text-lg",
                            "bg-gradient-to-r",
                            c.gradient,
                            "transition-all duration-300"
                        )}
                        animate={{
                            boxShadow: isHovered
                                ? `0 0 40px ${c.glow}`
                                : `0 0 20px ${c.glow}`,
                        }}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                    >
                        <span>Ta {pillColor === "red" ? "röda" : "blåa"} pillret</span>
                        <ArrowRight className="w-5 h-5 transition-transform group-hover:translate-x-1" />
                    </motion.div>
                </div>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   LEARN PAGE - THE MATRIX
   ============================================================================ */

export default function LearnPage() {
    const router = useRouter()
    const { hasSelected, isLoading: platformLoading } = usePlatform()
    const [showContent, setShowContent] = useState(false)

    useEffect(() => {
        if (hasSelected) {
            // Dramatic reveal
            const timer = setTimeout(() => setShowContent(true), 100)
            return () => clearTimeout(timer)
        }
    }, [hasSelected])

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
            <div className="relative min-h-[90vh]">
                {/* Matrix rain background */}
                <MatrixRain />

                {/* Content */}
                <AnimatePresence>
                    {showContent && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ duration: 0.5 }}
                            className="relative z-10"
                        >
                            {/* Header - Morpheus intro */}
                            <motion.div
                                initial={{ opacity: 0, y: -30 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.2 }}
                                className="text-center mb-12"
                            >
                                {/* Eye icon */}
                                <motion.div
                                    initial={{ scale: 0, rotate: -180 }}
                                    animate={{ scale: 1, rotate: 0 }}
                                    transition={{ type: "spring", delay: 0.3 }}
                                    className={cn(
                                        "w-20 h-20 mx-auto mb-6 rounded-2xl",
                                        "bg-gradient-to-br from-green-600 to-emerald-700",
                                        "flex items-center justify-center",
                                        "shadow-[0_0_40px_rgba(16,185,129,0.4)]"
                                    )}
                                >
                                    <Eye className="w-10 h-10 text-white" />
                                </motion.div>

                                {/* Main title */}
                                <motion.h1
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.4 }}
                                    className={cn(
                                        "text-4xl md:text-5xl font-black mb-4",
                                        "bg-gradient-to-r from-green-400 via-emerald-300 to-green-400",
                                        "bg-clip-text text-transparent"
                                    )}
                                >
                                    Välj ditt öde
                                </motion.h1>

                                {/* Subtitle */}
                                <motion.p
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    transition={{ delay: 0.5 }}
                                    className="text-lg text-zinc-400 max-w-2xl mx-auto mb-3"
                                >
                                    &ldquo;This is your last chance. After this, there is no turning back...&rdquo;
                                </motion.p>

                                {/* Rabbit hole tagline */}
                                <motion.div
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    transition={{ delay: 0.6 }}
                                    className={cn(
                                        "inline-flex items-center gap-2 px-4 py-2 rounded-full",
                                        "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                                        "border border-green-500/30",
                                        "text-green-400 text-sm font-medium"
                                    )}
                                >
                                    <Rabbit className="w-4 h-4" />
                                    How deep does the rabbit hole go?
                                    <Sparkles className="w-4 h-4" />
                                </motion.div>

                                {/* Platform badge */}
                                <motion.div
                                    initial={{ opacity: 0 }}
                                    animate={{ opacity: 1 }}
                                    transition={{ delay: 0.7 }}
                                    className="mt-4"
                                >
                                    <PlatformBadge className="mx-auto" />
                                </motion.div>
                            </motion.div>

                            {/* Pill Cards */}
                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
                                <PillCard
                                    title="Camp DevOps"
                                    subtitle="🔴 Red Pill"
                                    pillColor="red"
                                    href="/modules"
                                    morpheusQuote="You stay in Wonderland, and I show you how deep the rabbit hole goes."
                                    description="Vakna upp till DevOps-verkligheten. En komplett, guidad resa från nybörjare till expert. 4 tracks, 15 moduler, 384 praktiska tasks."
                                    features={[
                                        "Strukturerad väg från start till mål",
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

                                <PillCard
                                    title="SkillsMaps"
                                    subtitle="🔵 Blue Pill"
                                    pillColor="blue"
                                    href="/skillsmaps"
                                    morpheusQuote="The story ends, you wake up and believe whatever you want to believe."
                                    description="Välj din egen verklighet. Plocka exakt de färdigheter du behöver. 18 kompletta kunskapsstigar, välj fritt i din egen ordning."
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

                            {/* Footer */}
                            <motion.div
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: 1 }}
                                className="text-center mt-12 space-y-2"
                            >
                                <p className="text-zinc-500 text-sm">
                                    🐇 &ldquo;Remember, all I&apos;m offering is the truth. Nothing more.&rdquo;
                                </p>
                                <p className="text-zinc-600 text-xs">
                                    Du kan alltid byta väg via sidomenyn
                                </p>
                            </motion.div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        </PageLayout>
    )
}
