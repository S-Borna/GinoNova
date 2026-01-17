"use client"

/**
 * ============================================================================
 * 🌌 LANDING PAGE — COSMIC RELAUNCH EDITION 🌌
 * ============================================================================
 *
 * The main entry point for DevOpsHub. A premium, high-conversion landing page
 * with a stunning Big Bang intro animation.
 *
 * Sequence:
 * 1. Cosmic Intro Animation (3.5s) — Big Bang genesis moment
 * 2. Landing Page Reveal — Hero, Tracks, Features, etc.
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import { motion } from "framer-motion"
import {
    Hero,
    Features,
    CTASection,
    Footer,
    Navbar,
    TracksPreview,
} from "@/components/landing"
import CosmicIntro from "@/components/landing/CosmicIntro"
import { ComparisonSection } from "@/components/landing/ComparisonSection"

export default function LandingPage() {
    const [isMobile, setIsMobile] = React.useState(false)
    const [introFading, setIntroFading] = React.useState(false)
    const [introGone, setIntroGone] = React.useState(false)

    // Check if mobile on mount
    React.useEffect(() => {
        const mobile = window.innerWidth < 768
        setIsMobile(mobile)
        // On mobile: skip intro animation entirely, show landing immediately
        if (mobile) {
            setIntroFading(true)
            setIntroGone(true)
        }
    }, [])

    const handleIntroComplete = React.useCallback(() => {
        // Intro starts fading - begin showing landing underneath
        setIntroFading(true)
        // Remove intro overlay completely after fade animation
        setTimeout(() => setIntroGone(true), 1300)
    }, [])

    return (
        <>
            {/* Landing page - on mobile: visible immediately, on desktop: fades in after intro */}
            <motion.div
                className="relative min-h-screen bg-[#05050a] text-white overflow-x-hidden"
                initial={{ opacity: isMobile ? 1 : 0 }}
                animate={{ opacity: introFading ? 1 : 0 }}
                transition={{ duration: isMobile ? 0 : 1.0, ease: [0.16, 1, 0.3, 1] }}
            >
                <Navbar />
                <main>
                    <Hero />
                    <ComparisonSection />
                    <TracksPreview />
                    <Features />
                    <CTASection />
                </main>
                <Footer />
            </motion.div>

            {/* Cosmic Intro - overlays landing, fades away */}
            {!introGone && (
                <CosmicIntro onComplete={handleIntroComplete} duration={4} />
            )}
        </>
    )
}
