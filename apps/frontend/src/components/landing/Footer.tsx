"use client"

/**
 * ============================================================================
 * 🌌 FOOTER — COSMIC EDITION 🌌
 * ============================================================================
 *
 * Premium footer with cosmic accents, organized navigation,
 * and Swedish branding.
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Heart,
    Sparkles,
} from "lucide-react"

/* ============================================================================
   🗺️ NAVIGATION DATA
   ============================================================================ */

const NAV_SECTIONS = [
    {
        title: "Lärande",
        links: [
            { label: "SkillsMaps", href: "/skillsmaps" },
            { label: "Moduler", href: "/modules" },
            { label: "Labs & Projekt", href: "/modules#labs" },
            { label: "Studyflow", href: "/studyflow" },
        ],
    },
    {
        title: "Resurser",
        links: [
            { label: "Dokumentation", href: "/docs" },
            { label: "Community", href: "/community" },
            { label: "Blogg", href: "/blog" },
            { label: "FAQ", href: "/faq" },
        ],
    },
    {
        title: "Plattform",
        links: [
            { label: "Dashboard", href: "/dashboard" },
            { label: "Progress", href: "/progress" },
            { label: "Certifikat", href: "/certificates" },
            { label: "Inställningar", href: "/settings" },
        ],
    },
    {
        title: "Företag",
        links: [
            { label: "Om Oss", href: "/about" },
            { label: "Kontakt", href: "/contact" },
            { label: "Integritet", href: "/privacy" },
            { label: "Villkor", href: "/terms" },
        ],
    },
]


/* ============================================================================
   🚀 MAIN COMPONENT
   ============================================================================ */

export function Footer() {
    const currentYear = new Date().getFullYear()

    return (
        <footer className="relative bg-[#05050a] overflow-hidden">
            {/* Cosmic accent at top */}
            <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-500/30 to-transparent" />

            {/* Ambient glow */}
            <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-purple-500/5 rounded-full blur-[150px] pointer-events-none" />

            <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                {/* Main footer content */}
                <div className="py-16 lg:py-20 grid grid-cols-2 md:grid-cols-4 gap-8 lg:gap-12">
                    {/* Navigation columns */}
                    {NAV_SECTIONS.map((section, i) => (
                        <div key={section.title}>
                            <h4 className="text-sm font-bold text-white mb-4 uppercase tracking-wider">
                                {section.title}
                            </h4>
                            <ul className="space-y-3">
                                {section.links.map((link) => (
                                    <li key={link.href}>
                                        <Link
                                            href={link.href}
                                            className={cn(
                                                "text-sm text-zinc-400",
                                                "hover:text-purple-400 hover:translate-x-1",
                                                "transition-all duration-200",
                                                "inline-flex items-center gap-1"
                                            )}
                                        >
                                            {link.label}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>

                {/* Newsletter / CTA section */}
                <div className="py-8 border-t border-white/5">
                    <div className="flex flex-col md:flex-row items-center justify-between gap-6">
                        <div className="flex items-center gap-3">
                            <motion.div
                                animate={{
                                    rotate: [0, 10, -10, 0],
                                }}
                                transition={{ duration: 4, repeat: Infinity }}
                            >
                                <Sparkles className="w-5 h-5 text-purple-400" />
                            </motion.div>
                            <span className="text-zinc-400">
                                Redo att börja din DevOps-resa?{" "}
                                <Link
                                    href="/skillsmaps"
                                    className="text-purple-400 font-semibold hover:text-purple-300 transition-colors"
                                >
                                    Börja gratis idag →
                                </Link>
                            </span>
                        </div>

                        <div className="flex items-center gap-4">
                            <span className="text-xs text-zinc-500">Made in Sweden 🇸🇪</span>
                        </div>
                    </div>
                </div>

                {/* Bottom bar */}
                <div className="py-6 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4">
                    <p className="text-sm text-zinc-500">
                        © {currentYear} The Ebadi Group. Alla rättigheter förbehållna.
                    </p>

                    <motion.p
                        className="text-sm text-zinc-500 flex items-center gap-1.5"
                        whileHover={{ scale: 1.02 }}
                    >
                        Byggt med{" "}
                        <motion.span
                            animate={{
                                scale: [1, 1.2, 1],
                            }}
                            transition={{ duration: 1.5, repeat: Infinity }}
                        >
                            <Heart className="w-4 h-4 text-red-500 fill-red-500" />
                        </motion.span>
                        {" "}för DevOps-ingenjörer
                    </motion.p>
                </div>
            </div>
        </footer>
    )
}

export default Footer
