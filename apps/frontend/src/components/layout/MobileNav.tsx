"use client"

/**
 * ============================================================================
 * MOBILE NAVIGATION - Premium Bottom Tab Bar
 * ============================================================================
 *
 * Design Philosophy:
 * - iOS tab bar inspired design with premium feel
 * - Safe area padding for notched phones
 * - Large touch targets (min 44px)
 * - Smooth animations and haptic-feel feedback
 * - Cosmic theme matching desktop
 *
 * @phase D.3 - Navigation + Layout
 * @polish Mobile Premium v2.0
 */

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Home,
    BookOpen,
    GraduationCap,
    Brain,
    User,
    type LucideIcon
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface NavItem {
    label: string
    href: string
    icon: LucideIcon
    gradient: string
}

interface MobileNavProps {
    className?: string
}

/* ============================================================================
   NAVIGATION CONFIG
   ============================================================================ */

const navItems: NavItem[] = [
    { label: "Home", href: "/dashboard", icon: Home, gradient: "from-violet-500 to-purple-600" },
    { label: "Camp", href: "/modules", icon: BookOpen, gradient: "from-emerald-500 to-teal-600" },
    { label: "Study", href: "/study", icon: GraduationCap, gradient: "from-amber-500 to-orange-600" },
    { label: "AI Quiz", href: "/ai-quiz", icon: Brain, gradient: "from-pink-500 to-rose-600" },
    { label: "Profile", href: "/profile", icon: User, gradient: "from-cyan-500 to-blue-600" },
]

/* ============================================================================
   NAV ITEM COMPONENT
   ============================================================================ */

interface NavItemProps {
    item: NavItem
    isActive: boolean
}

function NavItemComponent({ item, isActive }: NavItemProps) {
    const Icon = item.icon

    return (
        <Link
            href={item.href}
            className={cn(
                "flex flex-col items-center justify-center gap-1 flex-1",
                "min-h-[56px] min-w-[56px]", // Min 44px touch target + padding
                "py-2 px-1",
                "transition-all duration-200 ease-out",
                "active:scale-90", // Haptic-feel tap feedback
                "touch-manipulation", // Optimize for touch
                isActive
                    ? "text-white"
                    : "text-zinc-500"
            )}
        >
            <motion.div
                className="relative"
                animate={isActive ? { scale: 1.1, y: -2 } : { scale: 1, y: 0 }}
                transition={{ type: "spring", stiffness: 400, damping: 20 }}
            >
                {/* Active glow background */}
                {isActive && (
                    <motion.div
                        className={cn(
                            "absolute -inset-2 rounded-xl opacity-60",
                            `bg-gradient-to-br ${item.gradient}`
                        )}
                        initial={{ scale: 0.8, opacity: 0 }}
                        animate={{ scale: 1, opacity: 0.4 }}
                        style={{ filter: "blur(8px)" }}
                    />
                )}

                <div className={cn(
                    "relative p-2 rounded-xl transition-all duration-200",
                    isActive && `bg-gradient-to-br ${item.gradient}`
                )}>
                    <Icon
                        className={cn(
                            "h-6 w-6 transition-all duration-200",
                            isActive ? "text-white" : "text-zinc-400"
                        )}
                        strokeWidth={isActive ? 2.5 : 2}
                    />
                </div>
            </motion.div>

            <span className={cn(
                "text-[10px] font-medium transition-all duration-200",
                isActive ? "text-white font-semibold" : "text-zinc-500"
            )}>
                {item.label}
            </span>
        </Link>
    )
}

/* ============================================================================
   MAIN MOBILE NAV COMPONENT
   ============================================================================ */

export function MobileNav({ className }: MobileNavProps) {
    const pathname = usePathname()

    const isActive = (href: string) => {
        if (!pathname) return false
        if (href === "/dashboard") {
            return pathname === "/dashboard" || pathname === "/"
        }
        return pathname.startsWith(href)
    }

    return (
        <nav className={cn(
            "fixed bottom-0 left-0 right-0 z-50",
            "bg-[#0a0a12]/95 backdrop-blur-xl",
            "border-t border-purple-500/20",
            // Safe area padding for notched phones
            "pb-safe",
            className
        )}>
            {/* Top glow line */}
            <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-500/40 to-transparent" />

            <div className="flex items-center justify-around px-1 py-1">
                {navItems.map((item) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                    />
                ))}
            </div>

            {/* Home indicator spacing (iOS) */}
            <div className="h-safe-area-inset-bottom" />
        </nav>
    )
}

export default MobileNav
