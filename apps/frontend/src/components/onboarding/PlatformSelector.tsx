"use client"

/**
 * ============================================================================
 * PLATFORM SELECTOR - PREMIUM DELUXE x1000 EDITION ✨
 * ============================================================================
 *
 * Ultra-premium OS selection experience with:
 * - Glassmorphism cards with holographic borders
 * - Animated gradient backgrounds
 * - Floating particles effect
 * - 3D hover transforms
 * - Pulsing glow effects
 * - Premium micro-interactions
 *
 * @phase PREMIUM-DELUXE-POLISH
 */

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    usePlatform,
    OS_OPTIONS,
    LINUX_DISTROS,
    type OperatingSystem,
    type LinuxDistro,
} from "@/hooks/useOperatingSystem"
import {
    Apple,
    Monitor,
    Terminal,
    Check,
    ChevronRight,
    Sparkles,
    HelpCircle,
    RotateCcw,
    Cpu,
    Zap,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface PlatformSelectorProps {
    onComplete?: () => void
    className?: string
}

/* ============================================================================
   FLOATING PARTICLES BACKGROUND
   ============================================================================ */

function FloatingParticles() {
    return (
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
            {[...Array(20)].map((_, i) => (
                <motion.div
                    key={i}
                    className="absolute w-1 h-1 bg-purple-500/30 rounded-full"
                    initial={{
                        x: Math.random() * 100 + "%",
                        y: "110%",
                        scale: Math.random() * 0.5 + 0.5,
                    }}
                    animate={{
                        y: "-10%",
                        transition: {
                            duration: Math.random() * 10 + 15,
                            repeat: Infinity,
                            ease: "linear",
                            delay: Math.random() * 5,
                        },
                    }}
                />
            ))}
        </div>
    )
}

/* ============================================================================
   PREMIUM OS CARD - DELUXE EDITION
   ============================================================================ */

interface OSCardProps {
    osKey: OperatingSystem
    isSelected: boolean
    onClick: () => void
    disabled?: boolean
    index: number
}

function PremiumOSCard({ osKey, isSelected, onClick, disabled, index }: OSCardProps) {
    const [isHovered, setIsHovered] = useState(false)

    if (!osKey) return null

    const config = OS_OPTIONS[osKey]

    const cardConfig = {
        macos: {
            emoji: "🍎",
            gradient: "from-zinc-800 via-zinc-900 to-black",
            accentGradient: "from-blue-500 via-purple-500 to-pink-500",
            glowColor: "rgba(147, 51, 234, 0.4)",
            subtitle: "Apple Silicon (M1/M2/M3) / Intel",
        },
        windows: {
            emoji: "🪟",
            gradient: "from-blue-900 via-blue-950 to-slate-900",
            accentGradient: "from-cyan-400 via-blue-500 to-indigo-600",
            glowColor: "rgba(59, 130, 246, 0.4)",
            subtitle: "Windows 10/11 med WSL2",
        },
        linux: {
            emoji: "🐧",
            gradient: "from-orange-900/80 via-amber-950 to-zinc-900",
            accentGradient: "from-orange-400 via-amber-500 to-yellow-500",
            glowColor: "rgba(245, 158, 11, 0.4)",
            subtitle: "Välj din distribution i nästa steg",
        },
    }

    const cardStyle = cardConfig[osKey]

    return (
        <motion.button
            onClick={onClick}
            disabled={disabled}
            onHoverStart={() => setIsHovered(true)}
            onHoverEnd={() => setIsHovered(false)}
            initial={{ opacity: 0, y: 60, rotateX: -15 }}
            animate={{ opacity: 1, y: 0, rotateX: 0 }}
            transition={{
                type: "spring",
                stiffness: 100,
                damping: 15,
                delay: index * 0.15,
            }}
            whileHover={{
                scale: 1.05,
                y: -12,
                rotateY: 5,
                transition: { type: "spring", stiffness: 400, damping: 25 }
            }}
            whileTap={{ scale: 0.98 }}
            className={cn(
                "relative group flex flex-col items-center justify-center",
                "w-full h-[260px] rounded-3xl",
                "transition-all duration-500",
                "perspective-1000",
                disabled && "opacity-50 cursor-not-allowed"
            )}
            style={{
                transformStyle: "preserve-3d",
            }}
        >
            {/* Holographic border effect */}
            <div className={cn(
                "absolute -inset-[2px] rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500",
                "bg-gradient-to-r",
                cardStyle.accentGradient,
                "blur-sm"
            )} />

            {/* Animated border gradient */}
            <motion.div
                className={cn(
                    "absolute -inset-[1px] rounded-3xl",
                    isSelected ? "opacity-100" : "opacity-0 group-hover:opacity-70",
                )}
                animate={{
                    background: [
                        `linear-gradient(0deg, ${cardStyle.glowColor}, transparent, ${cardStyle.glowColor})`,
                        `linear-gradient(180deg, ${cardStyle.glowColor}, transparent, ${cardStyle.glowColor})`,
                        `linear-gradient(360deg, ${cardStyle.glowColor}, transparent, ${cardStyle.glowColor})`,
                    ],
                }}
                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
            />

            {/* Main card background */}
            <div className={cn(
                "absolute inset-0 rounded-3xl",
                "bg-gradient-to-br",
                cardStyle.gradient,
                "border border-white/10",
                isSelected && "border-white/30"
            )} />

            {/* Glassmorphism overlay */}
            <div className="absolute inset-0 rounded-3xl bg-white/5 backdrop-blur-sm" />

            {/* Glow effect when selected/hovered */}
            <motion.div
                className="absolute inset-0 rounded-3xl"
                animate={{
                    boxShadow: isSelected || isHovered
                        ? `0 0 60px 10px ${cardStyle.glowColor}, inset 0 0 30px ${cardStyle.glowColor}`
                        : "0 0 0px 0px transparent",
                }}
                transition={{ duration: 0.4 }}
            />

            {/* Content */}
            <div className="relative z-10 flex flex-col items-center gap-4 p-6">
                {/* Emoji icon with floating animation */}
                <motion.div
                    className={cn(
                        "relative w-20 h-20 rounded-2xl flex items-center justify-center",
                        "bg-gradient-to-br from-white/10 to-white/5",
                        "border border-white/20",
                        "shadow-2xl"
                    )}
                    animate={isHovered ? {
                        y: [0, -8, 0],
                        transition: { duration: 2, repeat: Infinity, ease: "easeInOut" }
                    } : {}}
                >
                    <span className="text-5xl drop-shadow-2xl">{cardStyle.emoji}</span>

                    {/* Sparkle effects */}
                    {isSelected && (
                        <>
                            <motion.div
                                className="absolute -top-1 -right-1 text-yellow-400"
                                animate={{ rotate: 360, scale: [1, 1.2, 1] }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                <Sparkles className="w-4 h-4" />
                            </motion.div>
                            <motion.div
                                className="absolute -bottom-1 -left-1 text-purple-400"
                                animate={{ rotate: -360, scale: [1, 1.3, 1] }}
                                transition={{ duration: 2.5, repeat: Infinity }}
                            >
                                <Zap className="w-3 h-3" />
                            </motion.div>
                        </>
                    )}
                </motion.div>

                {/* Title */}
                <div className="text-center">
                    <motion.h3
                        className="text-2xl font-bold text-white tracking-tight"
                        animate={isSelected ? { scale: [1, 1.05, 1] } : {}}
                        transition={{ duration: 0.5 }}
                    >
                        {config.name}
                    </motion.h3>
                    <p className="text-sm text-white/60 mt-2 max-w-[180px]">
                        {cardStyle.subtitle}
                    </p>
                </div>

                {/* Selection indicator */}
                <AnimatePresence>
                    {isSelected && (
                        <motion.div
                            initial={{ scale: 0, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            exit={{ scale: 0, opacity: 0 }}
                            className={cn(
                                "absolute -top-3 -right-3 w-10 h-10 rounded-full",
                                "bg-gradient-to-br from-emerald-400 to-emerald-600",
                                "flex items-center justify-center",
                                "shadow-[0_0_20px_rgba(52,211,153,0.6)]",
                                "border-2 border-white/30"
                            )}
                        >
                            <Check className="w-5 h-5 text-white" strokeWidth={3} />
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>

            {/* Bottom highlight line */}
            <motion.div
                className={cn(
                    "absolute bottom-0 left-1/2 -translate-x-1/2 h-1 rounded-full",
                    "bg-gradient-to-r",
                    cardStyle.accentGradient
                )}
                animate={{
                    width: isSelected || isHovered ? "60%" : "0%",
                    opacity: isSelected || isHovered ? 1 : 0,
                }}
                transition={{ duration: 0.3 }}
            />
        </motion.button>
    )
}

/* ============================================================================
   PREMIUM DISTRO CARD
   ============================================================================ */

interface DistroCardProps {
    distroKey: LinuxDistro
    isSelected: boolean
    onClick: () => void
    index: number
}

function PremiumDistroCard({ distroKey, isSelected, onClick, index }: DistroCardProps) {
    if (!distroKey) return null

    const config = LINUX_DISTROS[distroKey]

    return (
        <motion.button
            onClick={onClick}
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02, x: 8 }}
            whileTap={{ scale: 0.98 }}
            className={cn(
                "relative group flex items-center gap-4 p-5 rounded-2xl",
                "bg-gradient-to-r from-zinc-900/90 via-zinc-800/90 to-zinc-900/90",
                "border transition-all duration-300",
                isSelected
                    ? "border-orange-500/50 shadow-[0_0_30px_rgba(249,115,22,0.2)]"
                    : "border-white/10 hover:border-white/20",
                "backdrop-blur-sm"
            )}
        >
            {/* Recommended badge */}
            {config.recommended && (
                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    className={cn(
                        "absolute -top-3 left-4 px-3 py-1 rounded-full",
                        "bg-gradient-to-r from-amber-500 to-orange-500",
                        "text-white text-xs font-bold tracking-wide",
                        "shadow-[0_0_15px_rgba(245,158,11,0.5)]",
                        "flex items-center gap-1"
                    )}
                >
                    <Sparkles className="w-3 h-3" />
                    RECOMMENDED
                </motion.div>
            )}

            {/* Selection check */}
            {isSelected && (
                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    className={cn(
                        "absolute -top-2 -right-2 w-7 h-7 rounded-full",
                        "bg-gradient-to-br from-emerald-400 to-emerald-600",
                        "flex items-center justify-center",
                        "shadow-[0_0_15px_rgba(52,211,153,0.5)]"
                    )}
                >
                    <Check className="w-4 h-4 text-white" strokeWidth={3} />
                </motion.div>
            )}

            {/* Icon */}
            <div className={cn(
                "w-14 h-14 rounded-xl flex items-center justify-center text-3xl",
                "bg-gradient-to-br from-white/10 to-white/5",
                "border border-white/10",
                "group-hover:scale-110 transition-transform duration-300"
            )}>
                {config.icon}
            </div>

            {/* Content */}
            <div className="flex-1 text-left">
                <div className="flex items-center gap-2">
                    <h4 className="font-bold text-white text-lg">{config.name}</h4>
                    <span className="text-xs text-white/40 px-2 py-0.5 bg-white/10 rounded-full">
                        {config.version}
                    </span>
                </div>
                <p className="text-sm text-white/50 mt-1 line-clamp-1">
                    {config.description}
                </p>
                <div className="flex items-center gap-2 mt-2">
                    <code className="text-xs text-orange-400/80 bg-orange-500/10 px-2 py-0.5 rounded font-mono">
                        {config.packageManager}
                    </code>
                </div>
            </div>

            {/* Arrow */}
            <ChevronRight className={cn(
                "w-5 h-5 text-white/30 transition-all duration-300",
                "group-hover:text-white/60 group-hover:translate-x-1"
            )} />
        </motion.button>
    )
}

/* ============================================================================
   PREMIUM HELP SECTION
   ============================================================================ */

function PremiumHelpSection() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className={cn(
                "mt-8 p-5 rounded-2xl",
                "bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10",
                "border border-amber-500/20",
                "backdrop-blur-sm"
            )}
        >
            <div className="flex items-start gap-4">
                <div className={cn(
                    "w-10 h-10 rounded-xl flex items-center justify-center",
                    "bg-gradient-to-br from-amber-500 to-orange-500",
                    "shadow-[0_0_20px_rgba(245,158,11,0.4)]"
                )}>
                    <HelpCircle className="w-5 h-5 text-white" />
                </div>
                <div>
                    <h4 className="font-bold text-amber-300">
                        Osäker på vad du ska välja?
                    </h4>
                    <p className="text-sm text-amber-200/70 mt-1 leading-relaxed">
                        Nybörjare? Välj <strong className="text-amber-300">Ubuntu 24.04 LTS</strong> — bäst dokumentation och community-support.
                        På <strong className="text-amber-300">Windows</strong> installeras WSL2 med Ubuntu automatiskt.
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT - PREMIUM DELUXE
   ============================================================================ */

export function PlatformSelector({ onComplete, className }: PlatformSelectorProps) {
    const { os, distro, setOS, setDistro, hasSelected, clearSelection } = usePlatform()
    const [step, setStep] = useState<"os" | "distro" | "complete">("os")
    const [showComplete, setShowComplete] = useState(false)

    // If already selected, immediately call onComplete
    useEffect(() => {
        if (hasSelected) {
            onComplete?.()
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [hasSelected])

    const handleOSSelect = (selectedOS: OperatingSystem) => {
        setOS(selectedOS)
        if (selectedOS === "linux") {
            setStep("distro")
        } else {
            // Go directly to content - no confirmation step
            onComplete?.()
        }
    }

    const handleDistroSelect = (selectedDistro: LinuxDistro) => {
        setDistro(selectedDistro)
        // Go directly to content - no confirmation step
        onComplete?.()
    }

    const handleReset = () => {
        clearSelection()
        setStep("os")
        setShowComplete(false)
    }

    return (
        <div className={cn(
            "relative w-full max-w-5xl mx-auto py-8",
            className
        )}>
            {/* Floating particles background */}
            <FloatingParticles />

            {/* Ambient glow effects */}
            <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[120px] pointer-events-none" />
            <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-[120px] pointer-events-none" />

            <AnimatePresence mode="wait">
                {/* Step 1: OS Selection - PREMIUM */}
                {step === "os" && (
                    <motion.div
                        key="os-selection"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0, y: -30 }}
                        className="relative space-y-10"
                    >
                        {/* Premium Header */}
                        <div className="text-center">
                            <motion.div
                                initial={{ scale: 0, rotate: -180 }}
                                animate={{ scale: 1, rotate: 0 }}
                                transition={{ type: "spring", stiffness: 200, delay: 0.2 }}
                                className={cn(
                                    "relative w-24 h-24 mx-auto mb-6",
                                    "rounded-3xl",
                                    "bg-gradient-to-br from-purple-600 via-violet-600 to-indigo-600",
                                    "flex items-center justify-center",
                                    "shadow-[0_0_60px_rgba(139,92,246,0.5)]"
                                )}
                            >
                                {/* Rotating ring */}
                                <motion.div
                                    className="absolute inset-[-4px] rounded-3xl border-2 border-dashed border-purple-400/30"
                                    animate={{ rotate: 360 }}
                                    transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
                                />
                                <Cpu className="w-12 h-12 text-white" />
                            </motion.div>

                            <motion.h2
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.4 }}
                                className={cn(
                                    "text-4xl font-black tracking-tight",
                                    "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                                )}
                            >
                                Välj ditt operativsystem
                            </motion.h2>

                            <motion.p
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.5 }}
                                className="text-lg text-white/50 mt-3 max-w-lg mx-auto"
                            >
                                Innehållet anpassas efter ditt val för bästa inlärningsupplevelse
                            </motion.p>
                        </div>

                        {/* Premium OS Cards Grid */}
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 px-4">
                            {(["macos", "windows", "linux"] as const).map((osKey, index) => (
                                <PremiumOSCard
                                    key={osKey}
                                    osKey={osKey}
                                    isSelected={os === osKey}
                                    onClick={() => handleOSSelect(osKey)}
                                    index={index}
                                />
                            ))}
                        </div>

                        {/* Bottom decoration line */}
                        <motion.div
                            initial={{ scaleX: 0 }}
                            animate={{ scaleX: 1 }}
                            transition={{ delay: 0.8, duration: 0.8 }}
                            className="w-32 h-1 mx-auto rounded-full bg-gradient-to-r from-transparent via-purple-500/50 to-transparent"
                        />
                    </motion.div>
                )}

                {/* Step 2: Distro Selection - PREMIUM */}
                {step === "distro" && (
                    <motion.div
                        key="distro-selection"
                        initial={{ opacity: 0, x: 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: -50 }}
                        className="relative space-y-8"
                    >
                        {/* Header */}
                        <div className="text-center">
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                className={cn(
                                    "w-20 h-20 mx-auto mb-4",
                                    "rounded-2xl",
                                    "bg-gradient-to-br from-orange-500 to-amber-600",
                                    "flex items-center justify-center",
                                    "shadow-[0_0_40px_rgba(249,115,22,0.4)]"
                                )}
                            >
                                <span className="text-4xl">🐧</span>
                            </motion.div>

                            <h2 className={cn(
                                "text-3xl font-bold",
                                "bg-gradient-to-r from-orange-300 via-amber-200 to-orange-300 bg-clip-text text-transparent"
                            )}>
                                Vilken Linux-distribution använder du?
                            </h2>
                            <p className="text-white/50 mt-2">
                                Välj din distro för korrekta pakethanteringskommandon
                            </p>
                        </div>

                        {/* Back button */}
                        <Button
                            variant="ghost"
                            onClick={() => {
                                setOS(null)
                                setStep("os")
                            }}
                            className="text-white/60 hover:text-white hover:bg-white/10"
                        >
                            ← Tillbaka till OS-val
                        </Button>

                        {/* Distro Cards */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl mx-auto">
                            {(["ubuntu", "debian", "fedora", "arch", "centos"] as const).map((distroKey, index) => (
                                <PremiumDistroCard
                                    key={distroKey}
                                    distroKey={distroKey}
                                    isSelected={distro === distroKey}
                                    onClick={() => handleDistroSelect(distroKey)}
                                    index={index}
                                />
                            ))}
                        </div>

                        <PremiumHelpSection />
                    </motion.div>
                )}

                {/* Step 3: Complete - PREMIUM SUCCESS */}
                {step === "complete" && showComplete && (
                    <motion.div
                        key="complete"
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="relative text-center py-12"
                    >
                        {/* Success checkmark with rings */}
                        <motion.div
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ type: "spring", stiffness: 200, delay: 0.2 }}
                            className="relative w-28 h-28 mx-auto mb-8"
                        >
                            {/* Pulsing rings */}
                            <motion.div
                                className="absolute inset-0 rounded-full border-2 border-emerald-500/30"
                                animate={{ scale: [1, 1.5], opacity: [0.5, 0] }}
                                transition={{ duration: 2, repeat: Infinity }}
                            />
                            <motion.div
                                className="absolute inset-0 rounded-full border-2 border-emerald-500/30"
                                animate={{ scale: [1, 1.8], opacity: [0.3, 0] }}
                                transition={{ duration: 2, repeat: Infinity, delay: 0.5 }}
                            />

                            {/* Main icon */}
                            <div className={cn(
                                "absolute inset-0 rounded-full",
                                "bg-gradient-to-br from-emerald-400 to-teal-600",
                                "flex items-center justify-center",
                                "shadow-[0_0_50px_rgba(52,211,153,0.5)]"
                            )}>
                                <Check className="w-14 h-14 text-white" strokeWidth={3} />
                            </div>
                        </motion.div>

                        <motion.h2
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.4 }}
                            className="text-3xl font-bold text-white mb-3"
                        >
                            Perfekt! Du är redo att börja
                        </motion.h2>

                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ delay: 0.5 }}
                            className={cn(
                                "inline-flex items-center gap-3 px-6 py-3 rounded-2xl mb-8",
                                "bg-gradient-to-r from-white/5 to-white/10",
                                "border border-white/10"
                            )}
                        >
                            <span className="text-white/60">Plattform:</span>
                            <span className="font-bold text-white">
                                {os === "macos" && "🍎 macOS"}
                                {os === "windows" && "🪟 Windows (WSL2)"}
                                {os === "linux" && distro && `🐧 Linux (${LINUX_DISTROS[distro].name})`}
                            </span>
                        </motion.div>

                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.6 }}
                            className="flex items-center justify-center gap-4"
                        >
                            <Button
                                variant="outline"
                                onClick={handleReset}
                                className={cn(
                                    "rounded-xl px-6",
                                    "border-white/20 text-white/70 hover:text-white",
                                    "hover:bg-white/10"
                                )}
                            >
                                <RotateCcw className="w-4 h-4 mr-2" />
                                Ändra val
                            </Button>
                            <Button
                                onClick={() => onComplete?.()}
                                className={cn(
                                    "rounded-xl px-8 py-6 text-lg font-semibold",
                                    "bg-gradient-to-r from-purple-600 to-indigo-600",
                                    "hover:from-purple-500 hover:to-indigo-500",
                                    "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
                                    "hover:shadow-[0_0_40px_rgba(139,92,246,0.6)]",
                                    "transition-all duration-300"
                                )}
                            >
                                Fortsätt till modulerna
                                <ChevronRight className="w-5 h-5 ml-2" />
                            </Button>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

/* ============================================================================
   PLATFORM BADGE - Premium Version
   ============================================================================ */

export function PlatformBadge({ className }: { className?: string }) {
    const { os, distro, hasSelected, clearSelection } = usePlatform()

    if (!hasSelected) return null

    const getLabel = () => {
        if (os === "macos") return "macOS"
        if (os === "windows") return "Windows"
        if (os === "linux" && distro) return LINUX_DISTROS[distro].name
        return "Linux"
    }

    const getIcon = () => {
        if (os === "macos") return "🍎"
        if (os === "windows") return "🪟"
        return "🐧"
    }

    return (
        <button
            onClick={clearSelection}
            className={cn(
                "inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-medium",
                "bg-gradient-to-r from-purple-500/20 to-indigo-500/20",
                "text-purple-300 border border-purple-500/30",
                "hover:from-purple-500/30 hover:to-indigo-500/30",
                "transition-all duration-300",
                className
            )}
            title="Klicka för att ändra"
        >
            <span>{getIcon()}</span>
            <span>{getLabel()}</span>
        </button>
    )
}

export default PlatformSelector
