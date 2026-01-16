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
import { motion, AnimatePresence } from "framer-motion"
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
    const [showIntro, setShowIntro] = React.useState(true)
    const [contentReady, setContentReady] = React.useState(false)

    const handleIntroComplete = React.useCallback(() => {
        setShowIntro(false)
        setContentReady(true)
    }, [])

    return (
        <>
            {/* Cosmic Big Bang Intro - GinoNivo Reveal */}
            {showIntro && (
                <CosmicIntro onComplete={handleIntroComplete} duration={4} />
            )}

            {/* Main Landing Page */}
            <AnimatePresence>
                {contentReady && (
                    <motion.div
                        className="relative min-h-screen bg-[#05050a] text-white overflow-x-hidden"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                    >
                        {/* Navigation */}
                        <Navbar />

                        {/* Main Content */}
                        <main>
                            {/* Hero Section */}
                            <Hero />

                            {/* Why Choose GinoNova - Competitive Advantage */}
                            <ComparisonSection />

                            {/* Learning Tracks Preview */}
                            <TracksPreview />

                            {/* Platform Features */}
                            <Features />

                            {/* Final CTA */}
                            <CTASection />
                        </main>

                        {/* Footer */}
                        <Footer />
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    )
}
