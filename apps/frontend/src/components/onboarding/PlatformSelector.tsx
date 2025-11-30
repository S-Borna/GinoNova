"use client"

/**
 * ============================================================================
 * PLATFORM SELECTOR - OS & Distro Selection with Wave Animation
 * ============================================================================
 *
 * A beautiful onboarding component that lets users select their operating
 * system and Linux distribution. Features a smooth wave animation when
 * selection is complete.
 *
 * Flow:
 * 1. User selects OS (macOS / Windows / Linux)
 * 2. If Linux → Select distro (Ubuntu recommended)
 * 3. Wave animation reveals modules
 *
 * @phase FAS-3.1 - OS-Adaptive Content System
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
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface PlatformSelectorProps {
    onComplete?: () => void
    className?: string
}

/* ============================================================================
   OS ICONS
   ============================================================================ */

const OSIcons = {
    macos: Apple,
    windows: Monitor,
    linux: Terminal,
}

/* ============================================================================
   WAVE ANIMATION COMPONENT
   ============================================================================ */

function WaveReveal({ 
    children, 
    isVisible, 
    delay = 0 
}: { 
    children: React.ReactNode
    isVisible: boolean
    delay?: number 
}) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 50, scale: 0.95 }}
            animate={isVisible ? { 
                opacity: 1, 
                y: 0, 
                scale: 1,
                transition: {
                    type: "spring",
                    stiffness: 100,
                    damping: 15,
                    delay: delay * 0.1,
                }
            } : {
                opacity: 0,
                y: 50,
                scale: 0.95,
            }}
        >
            {children}
        </motion.div>
    )
}

/* ============================================================================
   OS SELECTION CARD
   ============================================================================ */

interface OSCardProps {
    osKey: OperatingSystem
    isSelected: boolean
    onClick: () => void
    disabled?: boolean
}

function OSCard({ osKey, isSelected, onClick, disabled }: OSCardProps) {
    if (!osKey) return null
    
    const config = OS_OPTIONS[osKey]
    const Icon = OSIcons[osKey]

    return (
        <motion.button
            onClick={onClick}
            disabled={disabled}
            whileHover={{ scale: 1.02, y: -4 }}
            whileTap={{ scale: 0.98 }}
            className={cn(
                "relative flex flex-col items-center gap-4 p-6 rounded-2xl border-2 transition-all duration-300",
                "bg-white dark:bg-neutral-800 shadow-sm hover:shadow-lg",
                isSelected
                    ? "border-indigo-500 bg-indigo-50 dark:bg-indigo-950/30 ring-4 ring-indigo-500/20"
                    : "border-gray-200 dark:border-neutral-700 hover:border-indigo-300",
                disabled && "opacity-50 cursor-not-allowed"
            )}
        >
            {/* Selection indicator */}
            <AnimatePresence>
                {isSelected && (
                    <motion.div
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        exit={{ scale: 0, opacity: 0 }}
                        className="absolute -top-2 -right-2 w-8 h-8 bg-indigo-500 rounded-full flex items-center justify-center shadow-lg"
                    >
                        <Check className="w-5 h-5 text-white" />
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Icon */}
            <div className={cn(
                "w-16 h-16 rounded-2xl flex items-center justify-center text-3xl transition-colors",
                isSelected
                    ? "bg-indigo-100 dark:bg-indigo-900/50"
                    : "bg-gray-100 dark:bg-neutral-700"
            )}>
                {osKey === "macos" && "🍎"}
                {osKey === "windows" && "🪟"}
                {osKey === "linux" && "🐧"}
            </div>

            {/* Text */}
            <div className="text-center">
                <h3 className={cn(
                    "text-lg font-semibold",
                    isSelected ? "text-indigo-600 dark:text-indigo-400" : "text-gray-900 dark:text-white"
                )}>
                    {config.name}
                </h3>
                <p className="text-sm text-gray-500 dark:text-neutral-400 mt-1">
                    {config.description}
                </p>
            </div>
        </motion.button>
    )
}

/* ============================================================================
   DISTRO SELECTION CARD
   ============================================================================ */

interface DistroCardProps {
    distroKey: LinuxDistro
    isSelected: boolean
    onClick: () => void
}

function DistroCard({ distroKey, isSelected, onClick }: DistroCardProps) {
    if (!distroKey) return null
    
    const config = LINUX_DISTROS[distroKey]

    return (
        <motion.button
            onClick={onClick}
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            className={cn(
                "relative flex items-center gap-4 p-4 rounded-xl border-2 transition-all duration-300 text-left",
                "bg-white dark:bg-neutral-800",
                isSelected
                    ? "border-indigo-500 bg-indigo-50 dark:bg-indigo-950/30"
                    : "border-gray-200 dark:border-neutral-700 hover:border-indigo-300",
                config.recommended && !isSelected && "ring-2 ring-amber-400/50"
            )}
        >
            {/* Recommended badge */}
            {config.recommended && (
                <div className="absolute -top-2 left-4 px-2 py-0.5 bg-amber-400 text-amber-900 text-xs font-bold rounded-full flex items-center gap-1">
                    <Sparkles className="w-3 h-3" />
                    REKOMMENDERAD
                </div>
            )}

            {/* Selection indicator */}
            {isSelected && (
                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    className="absolute -top-2 -right-2 w-6 h-6 bg-indigo-500 rounded-full flex items-center justify-center"
                >
                    <Check className="w-4 h-4 text-white" />
                </motion.div>
            )}

            {/* Icon */}
            <div className={cn(
                "w-12 h-12 rounded-xl flex items-center justify-center text-2xl shrink-0",
                isSelected ? "bg-indigo-100 dark:bg-indigo-900/50" : "bg-gray-100 dark:bg-neutral-700"
            )}>
                {config.icon}
            </div>

            {/* Content */}
            <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2">
                    <h4 className={cn(
                        "font-semibold",
                        isSelected ? "text-indigo-600 dark:text-indigo-400" : "text-gray-900 dark:text-white"
                    )}>
                        {config.name}
                    </h4>
                    <span className="text-xs text-gray-400 dark:text-neutral-500">
                        {config.version}
                    </span>
                </div>
                <p className="text-sm text-gray-500 dark:text-neutral-400 mt-0.5 line-clamp-2">
                    {config.description}
                </p>
                <div className="flex items-center gap-2 mt-1">
                    <code className="text-xs bg-gray-100 dark:bg-neutral-700 px-1.5 py-0.5 rounded">
                        {config.packageManager}
                    </code>
                </div>
            </div>
        </motion.button>
    )
}

/* ============================================================================
   HELP SECTION
   ============================================================================ */

function HelpSection() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mt-8 p-4 bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800 rounded-xl"
        >
            <div className="flex items-start gap-3">
                <HelpCircle className="w-5 h-5 text-amber-600 dark:text-amber-400 shrink-0 mt-0.5" />
                <div>
                    <h4 className="font-semibold text-amber-800 dark:text-amber-300">
                        Osäker på vad du ska välja?
                    </h4>
                    <p className="text-sm text-amber-700 dark:text-amber-400 mt-1">
                        Om du är nybörjare rekommenderar vi <strong>Ubuntu 24.04 LTS</strong>. 
                        Det är det mest använda operativsystemet för DevOps och har bäst dokumentation 
                        och community-support. Alla våra tasks är testade och fungerar garanterat på Ubuntu.
                    </p>
                    <p className="text-sm text-amber-700 dark:text-amber-400 mt-2">
                        Om du använder <strong>Windows</strong>, installeras WSL2 (Windows Subsystem for Linux) 
                        med Ubuntu automatiskt — så du får det bästa av båda världar!
                    </p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function PlatformSelector({ onComplete, className }: PlatformSelectorProps) {
    const { os, distro, setOS, setDistro, hasSelected, clearSelection } = usePlatform()
    const [step, setStep] = useState<"os" | "distro" | "complete">("os")
    const [showComplete, setShowComplete] = useState(false)

    // Determine current step based on state
    useEffect(() => {
        if (hasSelected) {
            setStep("complete")
            setShowComplete(true)
        } else if (os === "linux") {
            setStep("distro")
        } else if (os) {
            // macOS or Windows selected - complete
            setStep("complete")
            setShowComplete(true)
        } else {
            setStep("os")
        }
    }, [os, distro, hasSelected])

    const handleOSSelect = (selectedOS: OperatingSystem) => {
        setOS(selectedOS)
        if (selectedOS === "linux") {
            setStep("distro")
        } else {
            // Auto-complete for macOS/Windows
            setTimeout(() => {
                setShowComplete(true)
                onComplete?.()
            }, 500)
        }
    }

    const handleDistroSelect = (selectedDistro: LinuxDistro) => {
        setDistro(selectedDistro)
        setTimeout(() => {
            setShowComplete(true)
            onComplete?.()
        }, 500)
    }

    const handleReset = () => {
        clearSelection()
        setStep("os")
        setShowComplete(false)
    }

    return (
        <div className={cn("w-full max-w-4xl mx-auto", className)}>
            <AnimatePresence mode="wait">
                {/* Step 1: OS Selection */}
                {step === "os" && (
                    <motion.div
                        key="os-selection"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -20 }}
                        className="space-y-6"
                    >
                        {/* Header */}
                        <div className="text-center">
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                transition={{ type: "spring", stiffness: 200 }}
                                className="w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-3xl flex items-center justify-center mx-auto mb-4 shadow-xl"
                            >
                                <Terminal className="w-10 h-10 text-white" />
                            </motion.div>
                            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                                Välj ditt operativsystem
                            </h2>
                            <p className="text-gray-500 dark:text-neutral-400 mt-2">
                                Innehållet anpassas efter ditt val för bästa inlärningsupplevelse
                            </p>
                        </div>

                        {/* OS Cards */}
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                            {(["macos", "windows", "linux"] as const).map((osKey, index) => (
                                <motion.div
                                    key={osKey}
                                    initial={{ opacity: 0, y: 30 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: index * 0.1 }}
                                >
                                    <OSCard
                                        osKey={osKey}
                                        isSelected={os === osKey}
                                        onClick={() => handleOSSelect(osKey)}
                                    />
                                </motion.div>
                            ))}
                        </div>

                        <HelpSection />
                    </motion.div>
                )}

                {/* Step 2: Distro Selection (Linux only) */}
                {step === "distro" && (
                    <motion.div
                        key="distro-selection"
                        initial={{ opacity: 0, x: 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: -50 }}
                        className="space-y-6"
                    >
                        {/* Header */}
                        <div className="text-center">
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                className="w-20 h-20 bg-gradient-to-br from-orange-500 to-red-600 rounded-3xl flex items-center justify-center mx-auto mb-4 shadow-xl"
                            >
                                <span className="text-4xl">🐧</span>
                            </motion.div>
                            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                                Vilken Linux-distribution använder du?
                            </h2>
                            <p className="text-gray-500 dark:text-neutral-400 mt-2">
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
                            className="mb-4"
                        >
                            ← Tillbaka till OS-val
                        </Button>

                        {/* Distro Cards */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            {(["ubuntu", "debian", "fedora", "arch", "centos"] as const).map((distroKey, index) => (
                                <motion.div
                                    key={distroKey}
                                    initial={{ opacity: 0, y: 30 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: index * 0.08 }}
                                >
                                    <DistroCard
                                        distroKey={distroKey}
                                        isSelected={distro === distroKey}
                                        onClick={() => handleDistroSelect(distroKey)}
                                    />
                                </motion.div>
                            ))}
                        </div>

                        <HelpSection />
                    </motion.div>
                )}

                {/* Step 3: Complete - Show success */}
                {step === "complete" && showComplete && (
                    <motion.div
                        key="complete"
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="text-center py-8"
                    >
                        <motion.div
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ type: "spring", stiffness: 200, delay: 0.2 }}
                            className="w-24 h-24 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-xl"
                        >
                            <Check className="w-12 h-12 text-white" />
                        </motion.div>

                        <motion.h2
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.3 }}
                            className="text-2xl font-bold text-gray-900 dark:text-white mb-2"
                        >
                            Perfekt! Du är redo att börja
                        </motion.h2>

                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ delay: 0.4 }}
                            className="flex items-center justify-center gap-2 text-lg text-gray-600 dark:text-neutral-300 mb-6"
                        >
                            <span>Plattform:</span>
                            <span className="font-semibold text-indigo-600 dark:text-indigo-400">
                                {os === "macos" && "macOS"}
                                {os === "windows" && "Windows (WSL2)"}
                                {os === "linux" && distro && `Linux (${LINUX_DISTROS[distro].name})`}
                            </span>
                        </motion.div>

                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.5 }}
                            className="flex items-center justify-center gap-3"
                        >
                            <Button
                                variant="outline"
                                size="sm"
                                onClick={handleReset}
                                className="rounded-xl"
                            >
                                <RotateCcw className="w-4 h-4 mr-2" />
                                Ändra val
                            </Button>
                            <Button
                                onClick={onComplete}
                                className="rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700"
                            >
                                Fortsätt till modulerna
                                <ChevronRight className="w-4 h-4 ml-2" />
                            </Button>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

/* ============================================================================
   PLATFORM BADGE - Show current selection in header/sidebar
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
                "bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300",
                "hover:bg-indigo-200 dark:hover:bg-indigo-900/50 transition-colors",
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
