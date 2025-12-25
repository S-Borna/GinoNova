"use client"

/**
 * ============================================================================
 * COSMIC LOCKED OVERLAY — Premium Access Gate ✨
 * ============================================================================
 *
 * A beautiful cosmic overlay that indicates locked content for non-authenticated users.
 * Features:
 * - Deep space cosmic blur effect
 * - Animated stars and nebula
 * - Glass morphism card with CTA
 * - Smooth fade animations
 *
 * @phase MILESTONE-2.0-ACCESS-CONTROL
 */

import { motion } from "framer-motion"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { Lock, Sparkles, Rocket, LogIn, UserPlus } from "lucide-react"

interface CosmicLockedOverlayProps {
    /** Title for the locked page */
    title?: string
    /** Description of what the page contains */
    description?: string
    /** Additional className */
    className?: string
}

export function CosmicLockedOverlay({
    title = "Premium Content",
    description = "Logga in för att få tillgång till denna funktion",
    className,
}: CosmicLockedOverlayProps) {
    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className={cn(
                "absolute inset-0 z-50",
                "flex items-center justify-center",
                "overflow-hidden",
                className
            )}
        >
            {/* Deep Space Background */}
            <div className="absolute inset-0 bg-[#030308]">
                {/* Nebula gradients */}
                <motion.div
                    className="absolute w-[800px] h-[800px] rounded-full"
                    style={{
                        background: "radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 60%)",
                        filter: "blur(100px)",
                        top: "-20%",
                        right: "-20%",
                    }}
                    animate={{
                        scale: [1, 1.3, 1],
                        opacity: [0.3, 0.5, 0.3],
                    }}
                    transition={{ duration: 10, repeat: Infinity, ease: "easeInOut" }}
                />
                <motion.div
                    className="absolute w-[600px] h-[600px] rounded-full"
                    style={{
                        background: "radial-gradient(circle, rgba(6,182,212,0.1) 0%, transparent 60%)",
                        filter: "blur(80px)",
                        bottom: "-10%",
                        left: "-15%",
                    }}
                    animate={{
                        scale: [1.2, 1, 1.2],
                        opacity: [0.2, 0.4, 0.2],
                    }}
                    transition={{ duration: 12, repeat: Infinity, ease: "easeInOut" }}
                />
                <motion.div
                    className="absolute w-[400px] h-[400px] rounded-full"
                    style={{
                        background: "radial-gradient(circle, rgba(236,72,153,0.08) 0%, transparent 60%)",
                        filter: "blur(60px)",
                        top: "30%",
                        left: "20%",
                    }}
                    animate={{
                        x: [0, 50, 0],
                        y: [0, -30, 0],
                        opacity: [0.15, 0.25, 0.15],
                    }}
                    transition={{ duration: 15, repeat: Infinity, ease: "easeInOut" }}
                />

                {/* Star field */}
                <div className="absolute inset-0">
                    {Array.from({ length: 50 }).map((_, i) => (
                        <motion.div
                            key={i}
                            className="absolute w-1 h-1 bg-white rounded-full"
                            style={{
                                top: `${Math.random() * 100}%`,
                                left: `${Math.random() * 100}%`,
                                opacity: Math.random() * 0.5 + 0.2,
                            }}
                            animate={{
                                opacity: [0.2, 0.8, 0.2],
                                scale: [1, 1.5, 1],
                            }}
                            transition={{
                                duration: 2 + Math.random() * 3,
                                repeat: Infinity,
                                delay: Math.random() * 2,
                            }}
                        />
                    ))}
                </div>

                {/* Grid overlay */}
                <div
                    className="absolute inset-0 opacity-[0.02]"
                    style={{
                        backgroundImage: `
                            linear-gradient(rgba(139,92,246,0.5) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(139,92,246,0.5) 1px, transparent 1px)
                        `,
                        backgroundSize: '80px 80px'
                    }}
                />
            </div>

            {/* Frosted glass card */}
            <motion.div
                initial={{ scale: 0.9, opacity: 0, y: 20 }}
                animate={{ scale: 1, opacity: 1, y: 0 }}
                transition={{ delay: 0.2, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                className={cn(
                    "relative z-10 max-w-md mx-4",
                    "p-8 rounded-3xl",
                    "bg-gradient-to-br from-white/10 via-white/5 to-transparent",
                    "backdrop-blur-2xl",
                    "border border-white/20",
                    "shadow-[0_0_80px_rgba(139,92,246,0.2),0_20px_60px_rgba(0,0,0,0.5)]"
                )}
            >
                {/* Glow effect behind card */}
                <div className="absolute inset-0 rounded-3xl bg-gradient-to-br from-purple-500/10 to-cyan-500/5 blur-xl -z-10" />

                {/* Lock icon with animation */}
                <motion.div
                    className={cn(
                        "mx-auto w-20 h-20 rounded-2xl mb-6",
                        "bg-gradient-to-br from-purple-600/30 to-pink-600/20",
                        "border border-purple-500/30",
                        "flex items-center justify-center",
                        "shadow-[0_0_40px_rgba(139,92,246,0.3)]"
                    )}
                    animate={{
                        boxShadow: [
                            "0 0 30px rgba(139,92,246,0.2)",
                            "0 0 60px rgba(139,92,246,0.4)",
                            "0 0 30px rgba(139,92,246,0.2)",
                        ],
                    }}
                    transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                >
                    <Lock className="w-10 h-10 text-purple-300" />
                </motion.div>

                {/* Title */}
                <h2 className={cn(
                    "text-2xl font-bold text-center mb-2",
                    "bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent"
                )}>
                    {title}
                </h2>

                {/* Description */}
                <p className="text-zinc-400 text-center mb-6 leading-relaxed">
                    {description}
                </p>

                {/* Free badge */}
                <motion.div
                    className={cn(
                        "flex items-center justify-center gap-2 mb-6",
                        "px-4 py-2 mx-auto w-fit rounded-full",
                        "bg-gradient-to-r from-emerald-500/20 to-cyan-500/20",
                        "border border-emerald-500/30",
                        "shadow-[0_0_20px_rgba(16,185,129,0.2)]"
                    )}
                    animate={{
                        boxShadow: [
                            "0 0 15px rgba(16,185,129,0.2)",
                            "0 0 30px rgba(16,185,129,0.3)",
                            "0 0 15px rgba(16,185,129,0.2)",
                        ],
                    }}
                    transition={{ duration: 2, repeat: Infinity }}
                >
                    <Sparkles className="w-4 h-4 text-emerald-400" />
                    <span className="text-sm font-bold text-emerald-300">
                        100% GRATIS — Ingen betalning krävs
                    </span>
                </motion.div>

                {/* CTA Buttons */}
                <div className="space-y-3">
                    <Link href="/login" className="block">
                        <motion.button
                            className={cn(
                                "w-full flex items-center justify-center gap-2",
                                "px-6 py-3.5 rounded-xl",
                                "bg-gradient-to-r from-purple-600 via-purple-500 to-pink-500",
                                "text-white font-bold text-base",
                                "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
                                "border border-purple-400/30",
                                "transition-all duration-300"
                            )}
                            whileHover={{
                                scale: 1.02,
                                boxShadow: "0 0 50px rgba(139,92,246,0.5)",
                            }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <LogIn className="w-5 h-5" />
                            Logga in
                        </motion.button>
                    </Link>

                    <Link href="/register" className="block">
                        <motion.button
                            className={cn(
                                "w-full flex items-center justify-center gap-2",
                                "px-6 py-3.5 rounded-xl",
                                "bg-white/5 hover:bg-white/10",
                                "text-zinc-300 hover:text-white font-medium text-base",
                                "border border-white/10 hover:border-white/20",
                                "transition-all duration-300"
                            )}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <UserPlus className="w-5 h-5" />
                            Skapa gratis konto
                        </motion.button>
                    </Link>
                </div>

                {/* Bottom text */}
                <p className="text-zinc-500 text-xs text-center mt-6">
                    Gå med 10,000+ användare som lär sig DevOps
                </p>

                {/* Decorative rocket */}
                <motion.div
                    className="absolute -top-4 -right-4"
                    animate={{
                        y: [0, -10, 0],
                        rotate: [0, 5, 0],
                    }}
                    transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                >
                    <div className={cn(
                        "w-12 h-12 rounded-xl",
                        "bg-gradient-to-br from-orange-500/30 to-pink-500/20",
                        "border border-orange-500/30",
                        "flex items-center justify-center",
                        "shadow-[0_0_20px_rgba(249,115,22,0.3)]"
                    )}>
                        <Rocket className="w-6 h-6 text-orange-300" />
                    </div>
                </motion.div>
            </motion.div>
        </motion.div>
    )
}

export default CosmicLockedOverlay
