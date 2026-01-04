"use client"

/**
 * ============================================================================
 * 🎯 CTA SECTION — COSMIC FINALE 🎯
 * ============================================================================
 *
 * The grand finale of the landing page.
 * Massive cosmic energy converging to a single point: START LEARNING.
 *
 * Design Philosophy:
 * - Maximum visual impact
 * - Clear value proposition (FREE, no registration)
 * - Urgency without desperation
 * - Swedish text for local audience
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    ArrowRight,
    Rocket,
    Gift,
    CheckCircle2,
} from "lucide-react"

/* ============================================================================
   🌌 COSMIC CTA BACKGROUND
   ============================================================================ */

function CTABackground() {
    return (
        <div className="absolute inset-0 overflow-hidden">
            {/* Deep space base */}
            <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#0a0a12] to-[#05050a]" />

            {/* Central ambient glow - static */}
            <div
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{
                    width: "800px",
                    height: "600px",
                    background: "radial-gradient(ellipse, rgba(139,92,246,0.2) 0%, rgba(168,85,247,0.1) 40%, transparent 70%)",
                    filter: "blur(60px)",
                }}
            />

            {/* Secondary glow - cyan accent */}
            <div
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
                style={{
                    width: "500px",
                    height: "300px",
                    background: "radial-gradient(ellipse, rgba(34,211,238,0.12) 0%, transparent 60%)",
                    filter: "blur(50px)",
                }}
            />

            {/* Subtle grid pattern */}
            <div
                className="absolute inset-0 opacity-[0.015]"
                style={{
                    backgroundImage: `radial-gradient(circle at center, rgba(139,92,246,0.4) 1px, transparent 1px)`,
                    backgroundSize: "50px 50px",
                }}
            />

            {/* Top separator */}
            <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-500/30 to-transparent" />
        </div>
    )
}

/* ============================================================================
   🚀 MAIN CTA COMPONENT
   ============================================================================ */

export function CTASection() {
    return (
        <section className="relative py-32 md:py-40 overflow-hidden">
            {/* Background */}
            <CTABackground />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                {/* FREE badge - emphasize the offer */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                    className="mb-8"
                >
                    <div
                        className={cn(
                            "inline-flex items-center gap-3 px-6 py-3 rounded-full",
                            "bg-emerald-500/15",
                            "border border-emerald-400/40"
                        )}
                    >
                        <Gift className="w-5 h-5 text-emerald-400" />
                        <span className="text-lg font-bold text-emerald-300">
                            HELT GRATIS
                        </span>
                        <span className="text-emerald-300/60">•</span>
                        <span className="text-emerald-200/80 font-medium">
                            Ingen registrering
                        </span>
                    </div>
                </motion.div>

                {/* Main headline */}
                <motion.h2
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.1 }}
                    className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black text-white mb-8"
                >
                    Redo att bli{" "}
                    <span className="relative inline-block">
                        <motion.span
                            className="bg-gradient-to-r from-purple-400 via-violet-400 to-cyan-400 bg-clip-text text-transparent"
                            animate={{
                                backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                            }}
                            transition={{ duration: 5, repeat: Infinity, ease: "linear" }}
                            style={{
                                backgroundSize: "200% auto",
                                filter: "drop-shadow(0 0 40px rgba(139,92,246,0.5))",
                            }}
                        >
                            DevOps Expert
                        </motion.span>
                        {/* Animated underline */}
                        <motion.span
                            initial={{ scaleX: 0 }}
                            whileInView={{ scaleX: 1 }}
                            viewport={{ once: true }}
                            transition={{ duration: 1, delay: 0.6 }}
                            className="absolute -bottom-2 left-0 right-0 h-1.5 bg-gradient-to-r from-purple-500 via-violet-500 to-cyan-500 rounded-full origin-left"
                        />
                    </span>
                    ?
                </motion.h2>

                {/* Subtext */}
                <motion.p
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="text-xl sm:text-2xl text-zinc-300 mb-8 max-w-3xl mx-auto leading-relaxed"
                >
                    Börja din resa mot en karriär inom DevOps.{" "}
                    <span className="text-purple-400 font-medium">
                        Från nybörjare till production-ready på månader, inte år.
                    </span>
                </motion.p>

                {/* Feature checklist */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.3 }}
                    className="flex flex-wrap justify-center gap-x-8 gap-y-3 mb-12"
                >
                    {[
                        "Inga kreditkort",
                        "Börja direkt",
                        "Alltid gratis",
                        "AI-assisterad",
                    ].map((item, i) => (
                        <motion.div
                            key={i}
                            initial={{ opacity: 0, x: -10 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            viewport={{ once: true }}
                            transition={{ delay: 0.4 + i * 0.1 }}
                            className="flex items-center gap-2 text-zinc-300"
                        >
                            <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                            <span className="font-medium">{item}</span>
                        </motion.div>
                    ))}
                </motion.div>

                {/* CTA Buttons */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-5"
                >
                    {/* Primary CTA */}
                    <Link href="/skillsmaps">
                        <Button
                            size="xl"
                            className={cn(
                                "gap-3 min-w-[300px] h-16 text-lg font-bold",
                                "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                "hover:from-purple-500 hover:via-violet-500 hover:to-indigo-500",
                                "border-0 rounded-2xl",
                                "shadow-lg shadow-purple-500/25",
                                "transition-all duration-300 hover:scale-[1.02]"
                            )}
                        >
                            <Rocket className="w-5 h-5" />
                            Börja Lära Nu — Gratis
                            <ArrowRight className="w-5 h-5" />
                        </Button>
                    </Link>

                    {/* Secondary CTA */}
                    <Link href="/modules">
                        <Button
                            size="xl"
                            variant="outline"
                            className={cn(
                                "gap-2 min-w-[200px] h-16 text-lg font-semibold",
                                "bg-white/5",
                                "border border-white/20 hover:border-white/40",
                                "text-white hover:bg-white/10",
                                "rounded-2xl",
                                "transition-all duration-300"
                            )}
                        >
                            Utforska Moduler
                        </Button>
                    </Link>
                </motion.div>


            </div>
        </section>
    )
}

export default CTASection
