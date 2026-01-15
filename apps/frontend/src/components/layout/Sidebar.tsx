"use client"

/**
 * ============================================================================
 * SIDEBAR - Premium Cosmic Navigation ✨
 * ============================================================================
 *
 * Design Philosophy:
 * - Premium cosmic dark theme with vibrant gradients
 * - Glassmorphism with aurora effects
 * - Magical micro-interactions
 * - Netflix-smooth animations
 * - Apple-level polish
 *
 * @phase D.3 - Navigation + Layout
 * @polish Premium Polish v2.0 - Cosmic Edition
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
    ChevronLeft,
    LayoutDashboard,
    Map,
    Shield,
    Brain,
    Heart,
    Zap,
    Sparkles,
    Code2,
    Trophy,
    Users,
    BarChart3,
    type LucideIcon
} from "lucide-react"

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface NavItem {
    label: string
    href: string
    icon: LucideIcon
    gradient: string
    glowColor: string
    adminOnly?: boolean
    authRequired?: boolean
}

interface SidebarProps {
    collapsed?: boolean
    onToggleCollapse?: () => void
    className?: string
}

/* ============================================================================
   NAVIGATION CONFIG - With Unique Gradients & Glows
   ============================================================================ */

const mainNavItems: NavItem[] = [
    {
        label: "Dashboard",
        href: "/dashboard",
        icon: Home,
        gradient: "from-violet-500 to-purple-600",
        glowColor: "rgba(139, 92, 246, 0.5)"
    },
    {
        label: "Skillpath",
        href: "/skillpath-board",
        icon: LayoutDashboard,
        gradient: "from-blue-500 to-indigo-600",
        glowColor: "rgba(99, 102, 241, 0.5)"
    },
    {
        label: "Camp DevOps",
        href: "/modules",
        icon: BookOpen,
        gradient: "from-emerald-500 to-teal-600",
        glowColor: "rgba(16, 185, 129, 0.5)"
    },
    {
        label: "SkillsMaps",
        href: "/skillsmaps",
        icon: Map,
        gradient: "from-orange-500 to-amber-600",
        glowColor: "rgba(249, 115, 22, 0.5)"
    },
    {
        label: "Studyroom",
        href: "/study",
        icon: Clock,
        gradient: "from-blue-500 to-cyan-600",
        glowColor: "rgba(59, 130, 246, 0.5)"
    },
    {
        label: "AI Quiz",
        href: "/quiz",
        icon: Brain,
        gradient: "from-violet-500 to-purple-600",
        glowColor: "rgba(139, 92, 246, 0.5)"
    },
    {
        label: "FastTrack",
        href: "/fasttrack",
        icon: Zap,
        gradient: "from-yellow-400 to-amber-500",
        glowColor: "rgba(250, 204, 21, 0.5)"
    },
    {
        label: "Code Playground",
        href: "/playground",
        icon: Code2,
        gradient: "from-indigo-500 to-purple-600",
        glowColor: "rgba(99, 102, 241, 0.5)"
    },
    {
        label: "Community",
        href: "/community",
        icon: Users,
        gradient: "from-pink-500 to-rose-600",
        glowColor: "rgba(236, 72, 153, 0.5)"
    },
    {
        label: "Analytics",
        href: "/analytics",
        icon: BarChart3,
        gradient: "from-cyan-500 to-teal-600",
        glowColor: "rgba(6, 182, 212, 0.5)"
    },
    {
        label: "Certificates",
        href: "/certificates",
        icon: Trophy,
        gradient: "from-amber-500 to-yellow-600",
        glowColor: "rgba(245, 158, 11, 0.5)"
    },
    {
        label: "Pulsmätning",
        href: "/pulse",
        icon: Heart,
        gradient: "from-red-500 to-pink-600",
        glowColor: "rgba(239, 68, 68, 0.5)"
    },
    {
        label: "Profile",
        href: "/profile",
        icon: User,
        gradient: "from-slate-400 to-zinc-500",
        glowColor: "rgba(148, 163, 184, 0.5)",
        authRequired: true
    },
    {
        label: "Admin",
        href: "/admin",
        icon: Shield,
        gradient: "from-purple-600 to-violet-700",
        glowColor: "rgba(147, 51, 234, 0.5)",
        adminOnly: true
    },
]

const bottomNavItems: NavItem[] = [
    {
        label: "Settings",
        href: "/settings",
        icon: Settings,
        gradient: "from-zinc-500 to-slate-600",
        glowColor: "rgba(113, 113, 122, 0.5)"
    },
    {
        label: "Help",
        href: "/help",
        icon: HelpCircle,
        gradient: "from-emerald-400 to-green-500",
        glowColor: "rgba(52, 211, 153, 0.5)"
    },
]

/* ============================================================================
   NAV ITEM COMPONENT - Premium Cosmic Edition
   ============================================================================ */

interface NavItemProps {
    item: NavItem
    isActive: boolean
    collapsed: boolean
    index: number
}

function NavItemComponent({ item, isActive, collapsed, index }: NavItemProps) {
    const Icon = item.icon
    const [isHovered, setIsHovered] = React.useState(false)

    return (
        <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.03, duration: 0.3 }}
        >
            <Link
                href={item.href}
                prefetch={false}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                className={cn(
                    "group relative flex items-center gap-3 px-3 py-2.5 rounded-xl",
                    "transition-all duration-300 ease-out",
                    "overflow-hidden",
                    collapsed && "justify-center px-2"
                )}
            >
                {/* Background layers */}
                <AnimatePresence>
                    {isActive && (
                        <>
                            {/* Active gradient background */}
                            <motion.div
                                className={cn(
                                    "absolute inset-0 rounded-xl",
                                    `bg-gradient-to-r ${item.gradient}`
                                )}
                                initial={{ opacity: 0, scale: 0.8 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0.8 }}
                                transition={{ duration: 0.2 }}
                            />
                            {/* Outer glow effect */}
                            <motion.div
                                className="absolute -inset-1 rounded-xl blur-lg opacity-40 -z-10"
                                style={{ background: `linear-gradient(135deg, ${item.glowColor}, transparent)` }}
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 0.4 }}
                            />
                            {/* Shimmer overlay */}
                            <motion.div
                                className="absolute inset-0 rounded-xl"
                                style={{
                                    background: "linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.15) 50%, transparent 100%)",
                                    backgroundSize: "200% 100%",
                                }}
                                animate={{
                                    backgroundPosition: ["-200% 0%", "200% 0%"],
                                }}
                                transition={{
                                    duration: 2,
                                    repeat: Infinity,
                                    repeatDelay: 3,
                                }}
                            />
                        </>
                    )}
                </AnimatePresence>

                {/* Hover background */}
                <motion.div
                    className={cn(
                        "absolute inset-0 rounded-xl",
                        "bg-gradient-to-r from-white/[0.03] to-white/[0.08]",
                        "border border-white/[0.08]"
                    )}
                    initial={{ opacity: 0 }}
                    animate={{ opacity: isHovered && !isActive ? 1 : 0 }}
                    transition={{ duration: 0.2 }}
                />

                {/* Icon container */}
                <motion.div
                    className={cn(
                        "relative z-10 flex items-center justify-center",
                        "w-9 h-9 rounded-lg",
                        isActive
                            ? "bg-white/20 shadow-lg backdrop-blur-sm"
                            : "bg-zinc-800/60 group-hover:bg-zinc-700/60",
                        "transition-all duration-300",
                        "border",
                        isActive ? "border-white/20" : "border-zinc-700/50 group-hover:border-zinc-600/50"
                    )}
                    animate={isHovered && !isActive ? { scale: 1.05, y: -1 } : { scale: 1, y: 0 }}
                    transition={{ type: "spring", stiffness: 400, damping: 25 }}
                >
                    <Icon className={cn(
                        "h-4 w-4 transition-all duration-300",
                        isActive
                            ? "text-white drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]"
                            : "text-zinc-400 group-hover:text-white"
                    )} />
                </motion.div>

                {/* Label */}
                {!collapsed && (
                    <motion.span
                        className={cn(
                            "relative z-10 text-sm truncate transition-all duration-200",
                            isActive
                                ? "text-white font-semibold"
                                : "text-zinc-400 group-hover:text-white font-medium"
                        )}
                    >
                        {item.label}
                    </motion.span>
                )}

                {/* Active indicator */}
                {isActive && !collapsed && (
                    <motion.div
                        className="absolute right-3 z-10"
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        transition={{ type: "spring", stiffness: 500, damping: 30 }}
                    >
                        <div className="relative">
                            <motion.div
                                className="w-2 h-2 rounded-full bg-white"
                                animate={{
                                    boxShadow: [
                                        "0 0 0 0 rgba(255,255,255,0.4)",
                                        "0 0 0 8px rgba(255,255,255,0)",
                                    ],
                                }}
                                transition={{ duration: 1.5, repeat: Infinity }}
                            />
                        </div>
                    </motion.div>
                )}

                {/* Tooltip when collapsed */}
                <AnimatePresence>
                    {collapsed && isHovered && (
                        <motion.div
                            initial={{ opacity: 0, x: -10, scale: 0.95 }}
                            animate={{ opacity: 1, x: 0, scale: 1 }}
                            exit={{ opacity: 0, x: -10, scale: 0.95 }}
                            transition={{ duration: 0.15 }}
                            className={cn(
                                "absolute left-full ml-3 px-3 py-2 rounded-xl z-50",
                                "bg-zinc-900/95 backdrop-blur-xl",
                                "border border-zinc-700/50",
                                "shadow-xl shadow-black/50",
                                "whitespace-nowrap"
                            )}
                        >
                            <span className="text-sm font-medium text-white">{item.label}</span>
                            {/* Arrow */}
                            <div className={cn(
                                "absolute top-1/2 -left-2 -translate-y-1/2",
                                "w-0 h-0",
                                "border-y-[6px] border-y-transparent",
                                "border-r-[8px] border-r-zinc-900"
                            )} />
                        </motion.div>
                    )}
                </AnimatePresence>
            </Link>
        </motion.div>
    )
}

/* ============================================================================
   MAIN SIDEBAR COMPONENT - Premium Cosmic Edition
   ============================================================================ */

export function Sidebar({ collapsed = false, onToggleCollapse, className }: SidebarProps) {
    const pathname = usePathname()
    const { user } = useAuth()
    const [systemExpanded, setSystemExpanded] = React.useState(false)

    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL
    const isAuthenticated = !!user

    const isActive = (href: string) => {
        if (!pathname) return false
        if (href === "/dashboard") {
            return pathname === "/dashboard" || pathname === "/"
        }
        return pathname.startsWith(href)
    }

    const visibleNavItems = mainNavItems.filter(item => {
        if (item.adminOnly && !isAdmin) return false
        if (item.authRequired && !isAuthenticated) return false
        return true
    })

    return (
        <motion.aside
            initial={{ x: -20, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className={cn(
                "fixed left-0 top-0 z-40 h-screen flex flex-col",
                "transition-all duration-300 ease-out",
                collapsed ? "w-[72px]" : "w-[260px]",
                className
            )}
        >
            {/* Background with cosmic gradient */}
            <div className="absolute inset-0 bg-[#0a0a12]">
                {/* Aurora gradient overlay */}
                <div className="absolute inset-0 bg-gradient-to-b from-purple-950/20 via-transparent to-cyan-950/10" />
                {/* Subtle grid pattern */}
                <div
                    className="absolute inset-0 opacity-[0.02]"
                    style={{
                        backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
                    }}
                />
            </div>

            {/* Border glow effect */}
            <div className="absolute right-0 top-0 bottom-0 w-px">
                <div className="absolute inset-0 bg-gradient-to-b from-purple-500/50 via-transparent to-cyan-500/30" />
            </div>

            {/* Logo Section */}
            <div className={cn(
                "relative flex items-center h-44 px-4",
                "border-b border-white/5",
                collapsed ? "justify-center px-2" : "justify-center"
            )}>
                <Link
                    href="/dashboard"
                    className="flex items-center transition-all duration-300 hover:opacity-90 group"
                >
                    {!collapsed ? (
                        <motion.div
                            className="relative flex items-center justify-center w-full"
                            whileHover={{ scale: 1.03 }}
                            whileTap={{ scale: 0.97 }}
                        >
                            {/* Outer glow */}
                            <motion.div
                                className="absolute -inset-2 rounded-2xl opacity-50"
                                style={{
                                    background: "radial-gradient(circle, rgba(139,92,246,0.5), rgba(236,72,153,0.3), transparent)",
                                    filter: "blur(20px)",
                                }}
                                animate={{
                                    opacity: [0.3, 0.6, 0.3],
                                    scale: [1, 1.08, 1],
                                }}
                                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                            />

                            {/* Logo Image */}
                            <motion.div
                                className="relative"
                                animate={{
                                    filter: [
                                        "drop-shadow(0 0 15px rgba(139,92,246,0.6))",
                                        "drop-shadow(0 0 25px rgba(139,92,246,0.8))",
                                        "drop-shadow(0 0 15px rgba(139,92,246,0.6))"
                                    ]
                                }}
                                transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                            >
                                <Image
                                    src="/ginonova-logo-horizontal.svg"
                                    alt="GinoNova"
                                    width={600}
                                    height={150}
                                    className="w-auto h-[165px]"
                                    priority
                                />
                            </motion.div>
                        </motion.div>
                    ) : (
                        /* Collapsed: Logo icon only */
                        <motion.div
                            className="relative"
                            whileHover={{ scale: 1.1 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            <motion.div
                                className="absolute -inset-2 rounded-xl opacity-60"
                                style={{
                                    background: "radial-gradient(circle, rgba(139,92,246,0.6), rgba(236,72,153,0.4))",
                                    filter: "blur(12px)",
                                }}
                                animate={{ opacity: [0.4, 0.8, 0.4] }}
                                transition={{ duration: 2.5, repeat: Infinity }}
                            />
                            <motion.div
                                className="relative"
                                animate={{
                                    filter: [
                                        "drop-shadow(0 0 10px rgba(139,92,246,0.7))",
                                        "drop-shadow(0 0 20px rgba(139,92,246,0.9))",
                                        "drop-shadow(0 0 10px rgba(139,92,246,0.7))"
                                    ]
                                }}
                                transition={{ duration: 2.5, repeat: Infinity }}
                            >
                                <Image
                                    src="/ginonova-logo.svg"
                                    alt="GinoNova"
                                    width={135}
                                    height={135}
                                    className="w-[135px] h-[135px]"
                                    priority
                                />
                            </motion.div>
                        </motion.div>
                    )}
                </Link>
            </div>

            {/* Navigation Section Label */}
            {!collapsed && (
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.2 }}
                    className="relative px-5 pt-6 pb-2"
                >
                    <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-zinc-500">
                        Navigation
                    </span>
                </motion.div>
            )}

            {/* Main Navigation */}
            <nav className="relative flex-1 px-3 py-2 space-y-1 overflow-y-auto scrollbar-thin scrollbar-thumb-zinc-700 scrollbar-track-transparent">
                {visibleNavItems.map((item, index) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                        collapsed={collapsed}
                        index={index}
                    />
                ))}
            </nav>

            {/* Bottom Section - System (Collapsible) */}
            <div className={cn(
                "relative px-3 py-4 space-y-1",
                "border-t border-white/5"
            )}>
                {/* Section label - clickable to collapse */}
                {!collapsed && (
                    <motion.button
                        onClick={() => setSystemExpanded(!systemExpanded)}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="w-full flex items-center justify-between px-3 pb-2 cursor-pointer hover:opacity-80 transition-opacity"
                    >
                        <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-zinc-600">
                            System
                        </span>
                        <motion.div
                            animate={{ rotate: systemExpanded ? 180 : 0 }}
                            transition={{ duration: 0.2 }}
                        >
                            <ChevronLeft className="h-3 w-3 text-zinc-600 -rotate-90" />
                        </motion.div>
                    </motion.button>
                )}

                <AnimatePresence>
                    {(systemExpanded || collapsed) && bottomNavItems.map((item, index) => (
                        <motion.div
                            key={item.href}
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: "auto" }}
                            exit={{ opacity: 0, height: 0 }}
                            transition={{ duration: 0.2 }}
                        >
                            <NavItemComponent
                                item={item}
                                isActive={isActive(item.href)}
                                collapsed={collapsed}
                                index={visibleNavItems.length + index}
                            />
                        </motion.div>
                    ))}
                </AnimatePresence>

                {/* Collapse Toggle */}
                <motion.button
                    onClick={onToggleCollapse}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className={cn(
                        "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl mt-2",
                        "text-zinc-500 hover:text-zinc-300",
                        "bg-zinc-800/30 hover:bg-zinc-800/50",
                        "border border-zinc-700/30 hover:border-zinc-600/50",
                        "transition-all duration-200",
                        collapsed && "justify-center px-2"
                    )}
                    aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
                >
                    <motion.div
                        animate={{ rotate: collapsed ? 180 : 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        <ChevronLeft className="h-4 w-4" />
                    </motion.div>
                    {!collapsed && (
                        <span className="text-sm font-medium">Collapse</span>
                    )}
                </motion.button>
            </div>

            {/* Footer branding */}
            {!collapsed && (
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.5 }}
                    className="relative px-4 py-3 border-t border-white/5"
                >
                    <div className="flex items-center justify-center gap-2">
                        <motion.div
                            animate={{
                                opacity: [0.5, 1, 0.5],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        >
                            <Sparkles className="w-3 h-3 text-purple-400" />
                        </motion.div>
                        <span className="text-[10px] text-zinc-600 font-medium">
                            Premium Learning Platform
                        </span>
                    </div>
                </motion.div>
            )}
        </motion.aside>
    )
}

export default Sidebar
