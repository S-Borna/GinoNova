"use client"

/**
 * ============================================================================
 * ⚔️ COMPARISON SECTION — WHY WE'RE BETTER
 * ============================================================================
 *
 * Show how DevOpsHub CRUSHES the competition.
 * Direct comparison with Udemy, Coursera, Pluralsight.
 *
 * Design Philosophy:
 * - Clear competitive advantages
 * - Visual comparison table
 * - Emphasize FREE, AI-powered, Swedish
 * - Make visitors realize: "This is actually better AND free?!"
 *
 * @phase MILESTONE-3.0-WOW-LANDING
 */

import * as React from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Check,
    X,
    Crown,
    Sparkles,
    Zap,
    Brain,
    Heart,
    DollarSign,
} from "lucide-react"

/* ============================================================================
   🎯 COMPARISON DATA
   ============================================================================ */

interface ComparisonFeature {
    feature: string
    devopshub: boolean | string
    udemy: boolean | string
    coursera: boolean | string
    pluralsight: boolean | string
    highlight?: boolean
}

const FEATURES: ComparisonFeature[] = [
    {
        feature: "Pris",
        devopshub: "100% GRATIS",
        udemy: "199-599 kr/kurs",
        coursera: "399 kr/månad",
        pluralsight: "449 kr/månad",
        highlight: true,
    },
    {
        feature: "AI-Driven Personalisering",
        devopshub: true,
        udemy: false,
        coursera: false,
        pluralsight: false,
        highlight: true,
    },
    {
        feature: "Dallas AI-Assistent",
        devopshub: true,
        udemy: false,
        coursera: false,
        pluralsight: false,
        highlight: true,
    },
    {
        feature: "Hands-On Labs (Cloud)",
        devopshub: true,
        udemy: false,
        coursera: "Begränsat",
        pluralsight: "Begränsat",
    },
    {
        feature: "Realtidsfeedback",
        devopshub: true,
        udemy: false,
        coursera: false,
        pluralsight: "Begränsat",
    },
    {
        feature: "Svenskt Innehåll",
        devopshub: true,
        udemy: "Varierande",
        coursera: "Begränsat",
        pluralsight: "Begränsat",
        highlight: true,
    },
    {
        feature: "Community & Mentorer",
        devopshub: true,
        udemy: "Begränsat",
        coursera: true,
        pluralsight: "Begränsat",
    },
    {
        feature: "Portfolio-Projekt",
        devopshub: true,
        udemy: "Varierande",
        coursera: "Varierande",
        pluralsight: true,
    },
    {
        feature: "Certifikat",
        devopshub: true,
        udemy: true,
        coursera: true,
        pluralsight: true,
    },
    {
        feature: "Ingen Registrering",
        devopshub: true,
        udemy: false,
        coursera: false,
        pluralsight: false,
        highlight: true,
    },
]

/* ============================================================================
   ✅ VALUE INDICATOR COMPONENT
   ============================================================================ */

interface ValueIndicatorProps {
    value: boolean | string
    isDevOpsHub?: boolean
}

function ValueIndicator({ value, isDevOpsHub = false }: ValueIndicatorProps) {
    if (typeof value === "string") {
        return (
            <span
                className={cn(
                    "text-sm font-semibold",
                    isDevOpsHub
                        ? "text-emerald-400"
                        : "text-zinc-400"
                )}
            >
                {value}
            </span>
        )
    }

    if (value) {
        return (
            <Check
                className={cn(
                    "w-5 h-5",
                    isDevOpsHub ? "text-emerald-400" : "text-zinc-500"
                )}
            />
        )
    }

    return <X className="w-5 h-5 text-zinc-700" />
}

/* ============================================================================
   🚀 MAIN COMPONENT — COMPARISON SECTION
   ============================================================================ */

export function ComparisonSection() {
    return (
        <section className="relative py-32 overflow-hidden bg-[#05050a]">
            {/* Cosmic background elements */}
            <div className="absolute inset-0">
                {/* Base gradient */}
                <div className="absolute inset-0 bg-gradient-to-b from-[#05050a] via-[#0a0a12] to-[#05050a]" />

                {/* Large ambient glow */}
                <div
                    className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1000px] h-[600px]"
                    style={{
                        background: "radial-gradient(ellipse, rgba(16,185,129,0.08) 0%, transparent 60%)",
                        filter: "blur(80px)",
                    }}
                />

                {/* Grid pattern overlay */}
                <div
                    className="absolute inset-0 opacity-[0.015]"
                    style={{
                        backgroundImage: `
                            linear-gradient(rgba(255,255,255,0.3) 1px, transparent 1px),
                            linear-gradient(90deg, rgba(255,255,255,0.3) 1px, transparent 1px)
                        `,
                        backgroundSize: "60px 60px",
                    }}
                />

                {/* Top separator */}
                <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-emerald-500/30 to-transparent" />
            </div>

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Section header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                    className="text-center mb-20"
                >
                    {/* Badge */}
                    <div
                        className={cn(
                            "inline-flex items-center gap-2 px-5 py-2 mb-6",
                            "text-sm font-semibold tracking-wide uppercase",
                            "text-emerald-300 bg-emerald-500/15 rounded-full",
                            "border border-emerald-500/30"
                        )}
                    >
                        <Crown className="w-4 h-4" />
                        Varför DevOpsHub?
                    </div>

                    <h2 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6">
                        Bättre än konkurrenterna.{" "}
                        <span
                            className="bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400 bg-clip-text text-transparent"
                            style={{ filter: "drop-shadow(0 0 25px rgba(16,185,129,0.4))" }}
                        >
                            100% Gratis.
                        </span>
                    </h2>

                    <p className="text-lg sm:text-xl text-zinc-400 max-w-3xl mx-auto leading-relaxed">
                        Vi erbjuder alla premium-funktioner från Udemy, Coursera och Pluralsight —{" "}
                        <span className="text-white font-medium">
                            plus AI-driven personalisering och Dallas-assistenten
                        </span>{" "}
                        — helt utan kostnad.
                    </p>
                </motion.div>

                {/* Comparison table */}
                <motion.div
                    initial={{ opacity: 0, y: 40 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.2 }}
                    className="relative"
                >
                    {/* Outer glow */}
                    <div
                        className="absolute -inset-4 rounded-3xl opacity-20 blur-2xl"
                        style={{ background: "rgba(16,185,129,0.3)" }}
                    />

                    <div
                        className={cn(
                            "relative overflow-hidden rounded-2xl",
                            "bg-gradient-to-br from-[#0d0d14]/90 to-[#0a0a0f]/90",
                            "backdrop-blur-xl",
                            "border border-white/10"
                        )}
                    >
                        {/* Table container with horizontal scroll on mobile */}
                        <div className="overflow-x-auto">
                            <table className="w-full">
                                {/* Header */}
                                <thead>
                                    <tr className="border-b border-white/10">
                                        <th className="p-4 text-left text-sm font-semibold text-zinc-400 min-w-[200px]">
                                            Funktion
                                        </th>
                                        <th className="p-4 text-center min-w-[150px]">
                                            <div className="flex flex-col items-center gap-2">
                                                <div className="inline-flex items-center gap-2 px-3 py-1.5 bg-gradient-to-r from-emerald-500/20 to-teal-500/20 rounded-full border border-emerald-500/30">
                                                    <Crown className="w-4 h-4 text-emerald-400" />
                                                    <span className="text-sm font-bold text-emerald-300">
                                                        DevOpsHub
                                                    </span>
                                                </div>
                                            </div>
                                        </th>
                                        <th className="p-4 text-center text-sm font-semibold text-zinc-400 min-w-[120px]">
                                            Udemy
                                        </th>
                                        <th className="p-4 text-center text-sm font-semibold text-zinc-400 min-w-[120px]">
                                            Coursera
                                        </th>
                                        <th className="p-4 text-center text-sm font-semibold text-zinc-400 min-w-[120px]">
                                            Pluralsight
                                        </th>
                                    </tr>
                                </thead>

                                {/* Body */}
                                <tbody>
                                    {FEATURES.map((item, index) => (
                                        <motion.tr
                                            key={item.feature}
                                            initial={{ opacity: 0, x: -20 }}
                                            whileInView={{ opacity: 1, x: 0 }}
                                            viewport={{ once: true, margin: "-50px" }}
                                            transition={{ delay: index * 0.05 }}
                                            className={cn(
                                                "border-b border-white/5",
                                                item.highlight && "bg-emerald-500/5"
                                            )}
                                        >
                                            <td className="p-4 text-sm font-medium text-white">
                                                <div className="flex items-center gap-2">
                                                    {item.highlight && (
                                                        <Sparkles className="w-4 h-4 text-emerald-400" />
                                                    )}
                                                    {item.feature}
                                                </div>
                                            </td>
                                            <td className="p-4 text-center">
                                                <div className="flex items-center justify-center">
                                                    <ValueIndicator
                                                        value={item.devopshub}
                                                        isDevOpsHub
                                                    />
                                                </div>
                                            </td>
                                            <td className="p-4 text-center">
                                                <div className="flex items-center justify-center">
                                                    <ValueIndicator value={item.udemy} />
                                                </div>
                                            </td>
                                            <td className="p-4 text-center">
                                                <div className="flex items-center justify-center">
                                                    <ValueIndicator value={item.coursera} />
                                                </div>
                                            </td>
                                            <td className="p-4 text-center">
                                                <div className="flex items-center justify-center">
                                                    <ValueIndicator value={item.pluralsight} />
                                                </div>
                                            </td>
                                        </motion.tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </motion.div>

                {/* Bottom highlight - Unique advantages */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, delay: 0.6 }}
                    className="mt-16"
                >
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {[
                            {
                                icon: Brain,
                                title: "AI-Powered",
                                description: "Dallas AI-assistent hjälper dig 24/7",
                                color: "purple",
                            },
                            {
                                icon: DollarSign,
                                title: "100% Gratis",
                                description: "Spara 5,000+ kr/år jämfört med konkurrenter",
                                color: "emerald",
                            },
                            {
                                icon: Heart,
                                title: "Svenskt",
                                description: "Skapat för den svenska DevOps-communityn",
                                color: "pink",
                            },
                        ].map((item, index) => {
                            const Icon = item.icon
                            return (
                                <motion.div
                                    key={item.title}
                                    initial={{ opacity: 0, y: 20 }}
                                    whileInView={{ opacity: 1, y: 0 }}
                                    viewport={{ once: true }}
                                    transition={{ delay: 0.7 + index * 0.1 }}
                                    className={cn(
                                        "p-6 rounded-xl text-center",
                                        "bg-white/5 border border-white/10",
                                        "hover:bg-white/10 hover:border-white/20",
                                        "transition-all duration-300"
                                    )}
                                >
                                    <Icon
                                        className={cn(
                                            "w-8 h-8 mx-auto mb-3",
                                            item.color === "purple" && "text-purple-400",
                                            item.color === "emerald" && "text-emerald-400",
                                            item.color === "pink" && "text-pink-400"
                                        )}
                                    />
                                    <h3 className="text-lg font-bold text-white mb-2">
                                        {item.title}
                                    </h3>
                                    <p className="text-sm text-zinc-400">
                                        {item.description}
                                    </p>
                                </motion.div>
                            )
                        })}
                    </div>
                </motion.div>
            </div>
        </section>
    )
}

export default ComparisonSection
