"use client"

/**
 * ============================================================================
 * NAVBAR — Sticky Navigation with Scroll Effects
 * ============================================================================
 *
 * Design: Glassmorphism navbar with blur effect on scroll,
 * responsive hamburger menu, and premium micro-interactions.
 *
 * @phase A.1 - Landing Page
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
    LogIn,
} from "lucide-react"

/* ============================================================================
   NAVIGATION DATA
   ============================================================================ */

const NAV_LINKS = [
    { label: "Modules", href: "/modules" },
    { label: "Dashboard", href: "/dashboard" },
    { label: "Progress", href: "/progress" },
    { label: "Studyflow", href: "/studyflow" },
]

/* ============================================================================
   MAIN COMPONENT
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
                    "transition-all duration-300 ease-out"
                )}
            >
                <nav
                    className={cn(
                        "mx-auto max-w-7xl px-4 sm:px-6 lg:px-8",
                        "transition-all duration-300"
                    )}
                >
                    <div
                        className={cn(
                            "flex items-center justify-between h-16 md:h-20",
                            "transition-all duration-300",
                            isScrolled && "h-14 md:h-16"
                        )}
                    >
                        {/* Logo */}
                        <Link
                            href="/"
                            className="flex items-center gap-2 group"
                        >
                            <div
                                className={cn(
                                    "p-2 rounded-lg bg-gradient-to-br from-primary-500 to-purple-600",
                                    "group-hover:scale-105 transition-transform duration-200"
                                )}
                            >
                                <Terminal className="w-5 h-5 text-white" />
                            </div>
                            <span className="text-lg font-bold text-white">
                                My DOE Hub
                            </span>
                        </Link>

                        {/* Desktop Navigation */}
                        <div className="hidden md:flex items-center gap-1">
                            {NAV_LINKS.map((link) => {
                                const isActive = pathname === link.href

                                return (
                                    <Link
                                        key={link.href}
                                        href={link.href}
                                        className={cn(
                                            "px-4 py-2 rounded-lg text-sm font-medium",
                                            "transition-all duration-200",
                                            isActive
                                                ? "text-white bg-white/10"
                                                : "text-neutral-400 hover:text-white hover:bg-white/5"
                                        )}
                                    >
                                        {link.label}
                                    </Link>
                                )
                            })}
                        </div>

                        {/* Desktop CTAs */}
                        <div className="hidden md:flex items-center gap-3">
                            <Link
                                href="/login"
                                className={cn(
                                    "px-4 py-2 rounded-lg text-sm font-medium",
                                    "text-neutral-300 hover:text-white",
                                    "transition-colors duration-200"
                                )}
                            >
                                <span className="flex items-center gap-2">
                                    <LogIn className="w-4 h-4" />
                                    Sign In
                                </span>
                            </Link>
                            <Link
                                href="/register"
                                className={cn(
                                    "inline-flex items-center gap-2",
                                    "px-4 py-2 rounded-lg text-sm font-semibold",
                                    "bg-gradient-to-r from-primary-500 to-purple-600",
                                    "text-white shadow-lg shadow-primary-500/20",
                                    "hover:shadow-xl hover:shadow-primary-500/30 hover:scale-[1.02]",
                                    "transition-all duration-200"
                                )}
                            >
                                <Sparkles className="w-4 h-4" />
                                Get Started
                            </Link>
                        </div>

                        {/* Mobile menu button */}
                        <button
                            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                            className={cn(
                                "md:hidden p-2 rounded-lg",
                                "text-neutral-400 hover:text-white",
                                "hover:bg-white/5 transition-colors duration-200"
                            )}
                            aria-label="Toggle menu"
                        >
                            {isMobileMenuOpen ? (
                                <X className="w-6 h-6" />
                            ) : (
                                <Menu className="w-6 h-6" />
                            )}
                        </button>
                    </div>
                </nav>

                {/* Backdrop blur bar (appears on scroll) */}
                <div
                    className={cn(
                        "absolute inset-0 -z-10",
                        "bg-neutral-950/80 backdrop-blur-xl",
                        "border-b border-white/[0.06]",
                        "transition-opacity duration-300",
                        isScrolled ? "opacity-100" : "opacity-0"
                    )}
                />
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
                            onClick={() => setIsMobileMenuOpen(false)}
                            className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm md:hidden"
                        />

                        {/* Menu panel */}
                        <motion.div
                            initial={{ x: "100%" }}
                            animate={{ x: 0 }}
                            exit={{ x: "100%" }}
                            transition={{ type: "spring", damping: 30, stiffness: 300 }}
                            className="fixed top-0 right-0 bottom-0 z-50 w-full max-w-sm bg-neutral-950 border-l border-white/10 md:hidden"
                        >
                            <div className="flex flex-col h-full p-6">
                                {/* Close button */}
                                <div className="flex items-center justify-between mb-8">
                                    <Link
                                        href="/"
                                        className="flex items-center gap-2"
                                        onClick={() => setIsMobileMenuOpen(false)}
                                    >
                                        <div className="p-2 rounded-lg bg-gradient-to-br from-primary-500 to-purple-600">
                                            <Terminal className="w-5 h-5 text-white" />
                                        </div>
                                        <span className="text-lg font-bold text-white">
                                            My DOE Hub
                                        </span>
                                    </Link>
                                    <button
                                        onClick={() => setIsMobileMenuOpen(false)}
                                        className="p-2 rounded-lg text-neutral-400 hover:text-white hover:bg-white/5 transition-colors"
                                    >
                                        <X className="w-6 h-6" />
                                    </button>
                                </div>

                                {/* Navigation links */}
                                <div className="flex-1 space-y-1">
                                    {NAV_LINKS.map((link, index) => {
                                        const isActive = pathname === link.href

                                        return (
                                            <motion.div
                                                key={link.href}
                                                initial={{ opacity: 0, x: 20 }}
                                                animate={{ opacity: 1, x: 0 }}
                                                transition={{ delay: index * 0.05 }}
                                            >
                                                <Link
                                                    href={link.href}
                                                    onClick={() => setIsMobileMenuOpen(false)}
                                                    className={cn(
                                                        "flex items-center justify-between",
                                                        "px-4 py-3 rounded-xl",
                                                        "transition-all duration-200",
                                                        isActive
                                                            ? "text-white bg-white/10"
                                                            : "text-neutral-400 hover:text-white hover:bg-white/5"
                                                    )}
                                                >
                                                    <span className="text-base font-medium">
                                                        {link.label}
                                                    </span>
                                                    <ChevronRight className="w-5 h-5" />
                                                </Link>
                                            </motion.div>
                                        )
                                    })}
                                </div>

                                {/* CTAs */}
                                <div className="pt-6 space-y-3 border-t border-white/10">
                                    <Link
                                        href="/login"
                                        onClick={() => setIsMobileMenuOpen(false)}
                                        className={cn(
                                            "flex items-center justify-center gap-2 w-full",
                                            "px-4 py-3 rounded-xl text-base font-medium",
                                            "text-neutral-300 bg-white/5 hover:bg-white/10",
                                            "transition-colors duration-200"
                                        )}
                                    >
                                        <LogIn className="w-5 h-5" />
                                        Sign In
                                    </Link>
                                    <Link
                                        href="/register"
                                        onClick={() => setIsMobileMenuOpen(false)}
                                        className={cn(
                                            "flex items-center justify-center gap-2 w-full",
                                            "px-4 py-3 rounded-xl text-base font-semibold",
                                            "bg-gradient-to-r from-primary-500 to-purple-600",
                                            "text-white shadow-lg shadow-primary-500/20",
                                            "transition-all duration-200"
                                        )}
                                    >
                                        <Sparkles className="w-5 h-5" />
                                        Get Started Free
                                    </Link>
                                </div>
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </>
    )
}

export default Navbar
