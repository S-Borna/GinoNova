"use client"

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { ArrowUp } from "lucide-react"
import { cn } from "@/lib/utils"

/**
 * Mobile-only Scroll to Top Button
 * Appears at top center on mobile when user scrolls down
 */
export function ScrollToTop() {
    const [isVisible, setIsVisible] = React.useState(false)
    const [isMounted, setIsMounted] = React.useState(false)

    React.useEffect(() => {
        setIsMounted(true)

        // Check scroll position
        const handleScroll = () => {
            setIsVisible(window.scrollY > 400)
        }
        handleScroll() // Check initial position
        window.addEventListener("scroll", handleScroll)

        return () => {
            window.removeEventListener("scroll", handleScroll)
        }
    }, [])

    const scrollToTop = () => {
        window.scrollTo({ top: 0, behavior: "smooth" })
    }

    // Don't render on server
    if (!isMounted) return null

    return (
        <AnimatePresence>
            {isVisible && (
                <motion.button
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -20 }}
                    onClick={scrollToTop}
                    className={cn(
                        "fixed top-20 left-1/2 -translate-x-1/2 z-[100]",
                        "px-4 py-2 rounded-full",
                        "bg-gradient-to-br from-purple-600 to-pink-600",
                        "shadow-lg shadow-purple-500/30",
                        "flex items-center gap-2",
                        "active:scale-95",
                        "transition-transform duration-150",
                        "md:hidden" // Only show on mobile
                    )}
                    aria-label="Scroll to top"
                >
                    <motion.div
                        animate={{ y: [0, -3, 0] }}
                        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <ArrowUp className="w-4 h-4 text-white" />
                    </motion.div>
                    <span className="text-white text-sm font-medium">Till toppen</span>
                </motion.button>
            )}
        </AnimatePresence>
    )
}

export default ScrollToTop
