"use client"

/**
 * ============================================================================
 * MOBILE SIDE MENU - Slide-in Navigation Panel
 * ============================================================================
 *
 * Design Philosophy:
 * - Full-screen slide-in from left
 * - Same cosmic theme as desktop sidebar
 * - Large touch targets (min 48px)
 * - Smooth animations with backdrop blur
 * - Quick access to all navigation items
 *
 * @phase MOBILE-OPTIMIZATION-v2
 */

import * as React from "react"
import Link from "next/link"
import Image from "next/image"
import { usePathname } from "next/navigation"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"
import {
    Home,
    BookOpen,
    Clock,
    User,
    Settings,
    HelpCircle,
    LayoutDashboard,
    Map,
    Shield,
    Brain,
    Zap,
    Code2,
    Trophy,
    Users,
    BarChart3,
    X,
    ChevronRight,
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
    adminOnly?: boolean
    authRequired?: boolean
}

interface MobileSideMenuProps {
    isOpen: boolean
    onClose: () => void
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   NAVIGATION CONFIG
   ============================================================================ */

const mainNavItems: NavItem[] = [
    {
        label: "Dashboard",
        href: "/dashboard",
        icon: Home,
        gradient: "from-violet-500 to-purple-600",
    },
    {
        label: "Skillpath",
        href: "/skillpath-board",
        icon: LayoutDashboard,
        gradient: "from-blue-500 to-indigo-600",
    },
    {
        label: "Camp DevOps",
        href: "/modules",
        icon: BookOpen,
        gradient: "from-emerald-500 to-teal-600",
    },
    {
        label: "SkillsMaps",
        href: "/skillsmaps",
        icon: Map,
        gradient: "from-orange-500 to-amber-600",
    },
    {
        label: "Studyroom",
        href: "/study",
        icon: Clock,
        gradient: "from-blue-500 to-cyan-600",
    },
    {
        label: "AI Quiz",
        href: "/ai-quiz",
        icon: Brain,
        gradient: "from-violet-500 to-purple-600",
    },
    {
        label: "FastTrack",
        href: "/fasttrack",
        icon: Zap,
        gradient: "from-yellow-400 to-amber-500",
    },
    {
        label: "Code Playground",
        href: "/playground",
        icon: Code2,
        gradient: "from-indigo-500 to-purple-600",
    },
    {
        label: "Community",
        href: "/community",
        icon: Users,
        gradient: "from-pink-500 to-rose-600",
    },
    {
        label: "Analytics",
        href: "/analytics",
        icon: BarChart3,
        gradient: "from-cyan-500 to-teal-600",
    },
    {
        label: "Certificates",
        href: "/certificates",
        icon: Trophy,
        gradient: "from-amber-500 to-yellow-600",
    },
]

const bottomNavItems: NavItem[] = [
    {
        label: "Profile",
        href: "/profile",
        icon: User,
        gradient: "from-slate-400 to-zinc-500",
        authRequired: true
    },
    {
        label: "Settings",
        href: "/settings",
        icon: Settings,
        gradient: "from-zinc-500 to-slate-600",
    },
    {
        label: "Admin",
        href: "/admin",
        icon: Shield,
        gradient: "from-purple-600 to-violet-700",
        adminOnly: true
    },
]

/* ============================================================================
   NAV ITEM COMPONENT
   ============================================================================ */

interface NavItemComponentProps {
    item: NavItem
    isActive: boolean
    onClose: () => void
    index: number
}

function NavItemComponent({ item, isActive, onClose, index }: NavItemComponentProps) {
    const Icon = item.icon

    return (
        <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.03, duration: 0.2 }}
        >
            <Link
                href={item.href}
                onClick={onClose}
                className={cn(
                    "flex items-center gap-4 px-4 py-4",
                    "rounded-xl transition-all duration-200",
                    "min-h-[56px]", // Touch target
                    "touch-manipulation active:scale-[0.98]",
                    isActive
                        ? `bg-gradient-to-r ${item.gradient} text-white shadow-lg`
                        : "text-zinc-400 hover:text-white hover:bg-white/5"
                )}
            >
                <div className={cn(
                    "w-10 h-10 rounded-lg flex items-center justify-center",
                    isActive
                        ? "bg-white/20"
                        : `bg-gradient-to-br ${item.gradient} bg-opacity-20`
                )}>
                    <Icon className="w-5 h-5" />
                </div>
                <span className="font-medium text-base flex-1">{item.label}</span>
                <ChevronRight className={cn(
                    "w-5 h-5 transition-transform",
                    isActive && "translate-x-1"
                )} />
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   MAIN MOBILE SIDE MENU COMPONENT
   ============================================================================ */

export function MobileSideMenu({ isOpen, onClose }: MobileSideMenuProps) {
    const pathname = usePathname()
    const { user } = useAuth()
    const isAdmin = user?.email === ADMIN_EMAIL

    const isActive = (href: string) => {
        if (!pathname) return false
        if (href === "/dashboard") {
            return pathname === "/dashboard" || pathname === "/"
        }
        return pathname.startsWith(href)
    }

    // Filter items based on auth and admin status
    const filteredMainItems = mainNavItems.filter(item => {
        if (item.authRequired && !user) return false
        if (item.adminOnly && !isAdmin) return false
        return true
    })

    const filteredBottomItems = bottomNavItems.filter(item => {
        if (item.authRequired && !user) return false
        if (item.adminOnly && !isAdmin) return false
        return true
    })

    return (
        <AnimatePresence>
            {isOpen && (
                <>
                    {/* Backdrop */}
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 0.2 }}
                        className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
                        onClick={onClose}
                    />

                    {/* Menu Panel */}
                    <motion.div
                        initial={{ x: "-100%" }}
                        animate={{ x: 0 }}
                        exit={{ x: "-100%" }}
                        transition={{ type: "spring", damping: 25, stiffness: 300 }}
                        className={cn(
                            "fixed left-0 top-0 bottom-0 z-50",
                            "w-[85vw] max-w-[320px]",
                            "bg-[#0a0a12]/98 backdrop-blur-xl",
                            "border-r border-purple-500/20",
                            "flex flex-col",
                            "safe-area-inset-left"
                        )}
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between p-4 border-b border-white/10">
                            <Link href="/dashboard" onClick={onClose} className="flex items-center gap-3">
                                <Image
                                    src="/ginonova-logo.svg"
                                    alt="GinoNova"
                                    width={40}
                                    height={40}
                                    className="w-10 h-10"
                                />
                                <span className="text-xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
                                    GinoNova
                                </span>
                            </Link>
                            <button
                                onClick={onClose}
                                className={cn(
                                    "p-2 rounded-lg",
                                    "text-zinc-400 hover:text-white",
                                    "hover:bg-white/10",
                                    "transition-colors",
                                    "min-h-[44px] min-w-[44px] flex items-center justify-center"
                                )}
                            >
                                <X className="w-6 h-6" />
                            </button>
                        </div>

                        {/* Navigation */}
                        <div className="flex-1 overflow-y-auto py-4 px-3">
                            <nav className="space-y-1">
                                {filteredMainItems.map((item, index) => (
                                    <NavItemComponent
                                        key={item.href}
                                        item={item}
                                        isActive={isActive(item.href)}
                                        onClose={onClose}
                                        index={index}
                                    />
                                ))}
                            </nav>
                        </div>

                        {/* Bottom Section */}
                        <div className="border-t border-white/10 p-3 space-y-1">
                            {filteredBottomItems.map((item, index) => (
                                <NavItemComponent
                                    key={item.href}
                                    item={item}
                                    isActive={isActive(item.href)}
                                    onClose={onClose}
                                    index={filteredMainItems.length + index}
                                />
                            ))}
                        </div>

                        {/* Safe area bottom padding */}
                        <div className="h-safe-area-inset-bottom" />
                    </motion.div>
                </>
            )}
        </AnimatePresence>
    )
}

export default MobileSideMenu
