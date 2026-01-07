"use client"

/**
 * ============================================================================
 * 🌐 NAVBAR — COSMIC STICKY NAVIGATION 🌐
 * ============================================================================
 *
 * Premium glassmorphism navbar with cosmic glow effects,
 * responsive design, and butter-smooth animations.
 *
 * Features:
 * - Scroll-triggered blur & background
 * - Responsive hamburger menu
 * - Cosmic CTA button
 * - Swedish text
 *
 * @phase MILESTONE-2.0-COSMIC-RELAUNCH
 */

import * as React from "react"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Menu,
    X,
    ChevronRight,
    Sparkles,
} from "lucide-react"
// TentaCountdown removed
import { SpotifyNowPlaying } from "@/components/spotify/SpotifyNowPlaying"

/* ============================================================================
   🚀 MAIN COMPONENT
   ============================================================================ */

export function Navbar() {
    const [isScrolled, setIsScrolled] = React.useState(false)
    const [isMobileMenuOpen, setIsMobileMenuOpen] = React.useState(false)

    // Handle scroll effect
    React.useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 20)
        }
        window.addEventListener("scroll", handleScroll)
        return () => window.removeEventListener("scroll", handleScroll)
    }, [])

    // Prevent body scroll when mobile menu is open
    React.useEffect(() => {
        if (isMobileMenuOpen) {
            document.body.style.overflow = "hidden"
        } else {
            document.body.style.overflow = ""
        }
        return () => {
            document.body.style.overflow = ""
        }
    }, [isMobileMenuOpen])

    return (
        <>
            <header
                className={cn(
                    "fixed top-0 left-0 right-0 z-50",
                    "transition-all duration-500 ease-out"
                )}
            >
                {/* Background with cosmic blur */}
                <div
                    className={cn(
                        "absolute inset-0 -z-10 transition-all duration-500",
                        isScrolled
                            ? "bg-[#05050a]/80 backdrop-blur-xl border-b border-purple-500/10"
                            : "bg-transparent"
                    )}
                />

                {/* Subtle glow line at top when scrolled */}
                <motion.div
                    className={cn(
                        "absolute bottom-0 left-0 right-0 h-px",
                        "bg-gradient-to-r from-transparent via-purple-500/30 to-transparent",
                        "transition-opacity duration-500"
                    )}
                    initial={{ opacity: 0 }}
                    animate={{ opacity: isScrolled ? 1 : 0 }}
                />

                <nav className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                    <div
                        className={cn(
                            "flex items-center justify-between",
                            "transition-all duration-300",
                            isScrolled ? "h-16" : "h-20"
                        )}
                    >

                        {/* Spotify Now Playing - Desktop */}
                        <div className="hidden lg:block">
                            <SpotifyNowPlaying variant="compact" />
                        </div>

                        {/* Mobile menu button */}
                        <motion.button
                            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                            className={cn(
                                "md:hidden p-2.5 rounded-xl",
                                "text-zinc-400 hover:text-white",
                                "hover:bg-white/5 transition-colors duration-200"
                            )}
                            whileTap={{ scale: 0.9 }}
                            aria-label="Toggle menu"
                        >
                            {isMobileMenuOpen ? (
                                <X className="w-6 h-6" />
                            ) : (
                                <Menu className="w-6 h-6" />
                            )}
                        </motion.button>
                    </div>
                </nav>
            </header>

            {/* Mobile Menu Overlay */}
            <AnimatePresence>
                {isMobileMenuOpen && (
                    <>
                        {/* Backdrop */}
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            transition={{ duration: 0.2 }}
                            className="fixed inset-0 z-40 bg-[#05050a]/95 backdrop-blur-xl md:hidden"
                            onClick={() => setIsMobileMenuOpen(false)}
                        />

                        {/* Menu Panel */}
                        <motion.div
                            initial={{ opacity: 0, y: -20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -20 }}
                            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                            className="fixed top-20 left-4 right-4 z-50 md:hidden"
                        >
                            <div
                                className={cn(
                                    "p-6 rounded-2xl",
                                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                    "border border-purple-500/20",
                                    "shadow-[0_20px_60px_rgba(139,92,246,0.2)]"
                                )}
                            >
                                {/* Mobile menu content placeholder */}
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </>
    )
}

export default Navbar
