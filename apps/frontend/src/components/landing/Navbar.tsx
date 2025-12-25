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
import { usePathname } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Terminal,
    Menu,
    X,
    ChevronRight,
    Sparkles,
    Rocket,
    BookOpen,
    LayoutDashboard,
    Timer,
    Map,
} from "lucide-react"

/* ============================================================================
   🗺️ NAVIGATION DATA
   ============================================================================ */

const NAV_LINKS = [
    { label: "Lärstigar", href: "/skillsmaps", icon: Map },
    { label: "Moduler", href: "/modules", icon: BookOpen },
    { label: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
    { label: "Studyflow", href: "/studyflow", icon: Timer },
]

/* ============================================================================
   🚀 MAIN COMPONENT
   ============================================================================ */

export function Navbar() {
    const pathname = usePathname()
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

    // Close mobile menu on route change
    React.useEffect(() => {
        setIsMobileMenuOpen(false)
    }, [pathname])

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
                        {/* Logo */}
                        <Link href="/" className="flex items-center gap-3 group">
                            <motion.div
                                className={cn(
                                    "p-2.5 rounded-xl",
                                    "bg-gradient-to-br from-purple-600 to-violet-700",
                                    "shadow-[0_0_20px_rgba(139,92,246,0.4)]",
                                    "group-hover:shadow-[0_0_30px_rgba(139,92,246,0.6)]",
                                    "transition-all duration-300"
                                )}
                                whileHover={{ scale: 1.05, rotate: 5 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                <Terminal className="w-5 h-5 text-white" />
                            </motion.div>
                            <span className="text-xl font-bold">
                                <span className="text-white">DevOps</span>
                                <span className="bg-gradient-to-r from-purple-400 to-violet-400 bg-clip-text text-transparent">Hub</span>
                            </span>
                        </Link>

                        {/* Desktop Navigation */}
                        <div className="hidden md:flex items-center gap-1">
                            {NAV_LINKS.map((link) => {
                                const isActive = pathname === link.href
                                const Icon = link.icon

                                return (
                                    <Link
                                        key={link.href}
                                        href={link.href}
                                        className={cn(
                                            "relative px-4 py-2.5 rounded-xl text-sm font-medium",
                                            "transition-all duration-300",
                                            "flex items-center gap-2",
                                            isActive
                                                ? "text-white bg-white/10"
                                                : "text-zinc-400 hover:text-white hover:bg-white/5"
                                        )}
                                    >
                                        <Icon className="w-4 h-4" />
                                        {link.label}
                                        {isActive && (
                                            <motion.div
                                                className="absolute bottom-1 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-purple-400"
                                                layoutId="nav-indicator"
                                            />
                                        )}
                                    </Link>
                                )
                            })}
                        </div>

                        {/* Desktop CTA */}
                        <div className="hidden md:flex items-center gap-3">
                            <Link
                                href="/skillsmaps"
                                className="group relative"
                            >
                                <motion.div
                                    className="absolute -inset-1 bg-gradient-to-r from-purple-600 to-cyan-600 rounded-xl blur-md opacity-60 group-hover:opacity-100 transition-opacity duration-300"
                                    animate={{
                                        opacity: [0.4, 0.7, 0.4],
                                    }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                />
                                <motion.button
                                    className={cn(
                                        "relative flex items-center gap-2",
                                        "px-5 py-2.5 rounded-xl text-sm font-bold",
                                        "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                        "text-white",
                                        "transition-all duration-300"
                                    )}
                                    whileHover={{ scale: 1.05 }}
                                    whileTap={{ scale: 0.98 }}
                                >
                                    <Rocket className="w-4 h-4" />
                                    Börja Gratis
                                    <ChevronRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
                                </motion.button>
                            </Link>
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
                                {/* Nav Links */}
                                <div className="space-y-2 mb-6">
                                    {NAV_LINKS.map((link, i) => {
                                        const isActive = pathname === link.href
                                        const Icon = link.icon

                                        return (
                                            <motion.div
                                                key={link.href}
                                                initial={{ opacity: 0, x: -20 }}
                                                animate={{ opacity: 1, x: 0 }}
                                                transition={{ delay: i * 0.05 }}
                                            >
                                                <Link
                                                    href={link.href}
                                                    className={cn(
                                                        "flex items-center justify-between p-4 rounded-xl",
                                                        "transition-all duration-200",
                                                        isActive
                                                            ? "bg-purple-500/20 text-white"
                                                            : "text-zinc-400 hover:text-white hover:bg-white/5"
                                                    )}
                                                >
                                                    <span className="flex items-center gap-3">
                                                        <Icon className="w-5 h-5" />
                                                        <span className="font-medium">{link.label}</span>
                                                    </span>
                                                    <ChevronRight className="w-4 h-4" />
                                                </Link>
                                            </motion.div>
                                        )
                                    })}
                                </div>

                                {/* Mobile CTA */}
                                <motion.div
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: 0.2 }}
                                >
                                    <Link href="/skillsmaps" className="block">
                                        <button
                                            className={cn(
                                                "w-full flex items-center justify-center gap-2",
                                                "p-4 rounded-xl text-base font-bold",
                                                "bg-gradient-to-r from-purple-600 via-violet-600 to-indigo-600",
                                                "text-white",
                                                "shadow-[0_0_30px_rgba(139,92,246,0.4)]"
                                            )}
                                        >
                                            <Rocket className="w-5 h-5" />
                                            Börja Lära — Gratis
                                        </button>
                                    </Link>
                                </motion.div>
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </>
    )
}

export default Navbar
