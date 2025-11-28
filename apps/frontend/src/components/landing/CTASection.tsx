"use client"

/**
 * ============================================================================
 * CTA SECTION — Final Call to Action
 * ============================================================================
 *
 * Design: Dramatic gradient background with compelling copy
 * and prominent action buttons.
 *
 * @phase A.1 - Landing Page
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import Link from "next/link"
import { ArrowRight, Sparkles, Zap } from "lucide-react"

export function CTASection() {
    return (
        <section className="relative py-24 overflow-hidden">
            {/* Background */}
            <div className="absolute inset-0">
                {/* Base gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-neutral-950 via-primary-950/50 to-neutral-950" />

                {/* Animated gradient orbs */}
                <motion.div
                    animate={{
                        scale: [1, 1.2, 1],
                        opacity: [0.3, 0.5, 0.3],
                    }}
                    transition={{
                        duration: 8,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[500px] bg-primary-500/20 rounded-full blur-[150px]"
                />
                <motion.div
                    animate={{
                        scale: [1.2, 1, 1.2],
                        opacity: [0.2, 0.4, 0.2],
                    }}
                    transition={{
                        duration: 10,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[400px] bg-purple-500/20 rounded-full blur-[150px]"
                />

                {/* Grid pattern overlay */}
                <div
                    className="absolute inset-0 opacity-[0.03]"
                    style={{
                        backgroundImage: `radial-gradient(circle at center, rgba(255,255,255,0.1) 1px, transparent 1px)`,
                        backgroundSize: "40px 40px",
                    }}
                />
            </div>

            <div className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                {/* Badge */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                >
                    <span className="inline-flex items-center gap-2 px-4 py-1.5 mb-6 text-xs font-semibold tracking-wider uppercase text-primary-300 bg-primary-500/20 rounded-full border border-primary-500/30">
                        <Zap className="w-3.5 h-3.5" />
                        Start Your Journey
                    </span>
                </motion.div>

                {/* Headline */}
                <motion.h2
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.1 }}
                    className="text-3xl sm:text-4xl lg:text-6xl font-bold text-white mb-6"
                >
                    Ready to Become a{" "}
                    <span className="relative inline-block">
                        <span className="bg-gradient-to-r from-primary-400 via-purple-400 to-cyan-400 bg-clip-text text-transparent">
                            DevOps Expert
                        </span>
                        {/* Underline decoration */}
                        <motion.span
                            initial={{ scaleX: 0 }}
                            whileInView={{ scaleX: 1 }}
                            viewport={{ once: true }}
                            transition={{ duration: 0.8, delay: 0.5 }}
                            className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-primary-500 to-purple-500 rounded-full origin-left"
                        />
                    </span>
                    ?
                </motion.h2>

                {/* Subtext */}
                <motion.p
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.2 }}
                    className="text-xl text-neutral-300 mb-8 max-w-2xl mx-auto"
                >
                    Join DevOpsHub today and gain access to a complete learning platform
                    designed to take you from beginner to production-ready in months, not years.
                </motion.p>

                {/* CTA Buttons */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-4"
                >
                    {/* Primary CTA */}
                    <Link href="/register" className="w-full sm:w-auto">
                        <button
                            className={cn(
                                "w-full sm:w-auto inline-flex items-center justify-center gap-2",
                                "px-8 py-4 rounded-xl text-lg font-semibold",
                                "bg-gradient-to-r from-primary-500 to-purple-600",
                                "text-white shadow-lg shadow-primary-500/30",
                                "hover:shadow-xl hover:shadow-primary-500/40 hover:scale-[1.02]",
                                "transition-all duration-300"
                            )}
                        >
                            <Sparkles className="w-5 h-5" />
                            Get Started Free
                            <ArrowRight className="w-5 h-5" />
                        </button>
                    </Link>

                    {/* Secondary CTA */}
                    <Link href="/modules" className="w-full sm:w-auto">
                        <button
                            className={cn(
                                "w-full sm:w-auto inline-flex items-center justify-center gap-2",
                                "px-8 py-4 rounded-xl text-lg font-semibold",
                                "bg-white/10 backdrop-blur-sm",
                                "text-white border border-white/20",
                                "hover:bg-white/20 hover:border-white/30",
                                "transition-all duration-300"
                            )}
                        >
                            Browse Modules
                        </button>
                    </Link>
                </motion.div>

                {/* Trust text */}
                <motion.p
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.5 }}
                    className="mt-8 text-sm text-neutral-500"
                >
                    No credit card required · Start learning in minutes · Cancel anytime
                </motion.p>
            </div>
        </section>
    )
}

export default CTASection
