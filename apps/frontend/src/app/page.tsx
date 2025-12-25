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
} from "@/components/landing"
import { CosmicIntro } from "@/components/landing/CosmicIntro"

export default function LandingPage() {
    const [showIntro, setShowIntro] = React.useState(true)
    const [contentReady, setContentReady] = React.useState(false)

    // Check if user has seen intro in this session
    React.useEffect(() => {
        const hasSeenIntro = sessionStorage.getItem("cosmic-intro-seen")
        if (hasSeenIntro) {
            setShowIntro(false)
            setContentReady(true)
        }
    }, [])

    const handleIntroComplete = React.useCallback(() => {
        sessionStorage.setItem("cosmic-intro-seen", "true")
        setShowIntro(false)
        setContentReady(true)
    }, [])

    return (
        <>
            {/* Cosmic Big Bang Intro */}
            {showIntro && (
                <CosmicIntro onComplete={handleIntroComplete} duration={3.5} />
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
