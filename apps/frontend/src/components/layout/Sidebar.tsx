"use client"

/**
 * ============================================================================
 * SIDEBAR - Premium Polish Navigation ✨
 * ============================================================================
 *
 * Design Philosophy:
 * - Premium dark theme with Focus Purple accents
 * - Chill Mint (#22D3AC) glow on active items
 * - Subtle hover animations
 * - Glassmorphism with deep backgrounds
 * - Admin link only visible to admin users
 *
 * @phase D.3 - Navigation + Layout
 * @polish Premium Polish v1.0
 */

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"
import {
    Home,
    BookOpen,
    Clock,
    BarChart3,
    User,
    Settings,
    HelpCircle,
    ChevronLeft,
    ChevronRight,
    LayoutDashboard,
    Map,
    GraduationCap,
    Shield,
    Brain,
    Heart,
    Zap,
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
    adminOnly?: boolean
}

interface SidebarProps {
    collapsed?: boolean
    onToggleCollapse?: () => void
    className?: string
}

/* ============================================================================
   NAVIGATION CONFIG
   ============================================================================ */

const mainNavItems: NavItem[] = [
    { label: "Dashboard", href: "/dashboard", icon: Home },
    { label: "Skillpath", href: "/skillpath-board", icon: LayoutDashboard },
    { label: "Camp DevOps", href: "/modules", icon: BookOpen },
    { label: "SkillsMaps", href: "/skillsmaps", icon: Map },
    { label: "FastTrack", href: "/fasttrack", icon: Zap },
    { label: "Studyroom", href: "/study", icon: Clock },
    { label: "AI Quiz", href: "/quiz", icon: Brain },
    { label: "Pulsmätning", href: "/pulse", icon: Heart },
    { label: "Profile", href: "/profile", icon: User },
    { label: "Admin", href: "/admin", icon: Shield, adminOnly: true },
]

const bottomNavItems: NavItem[] = [
    { label: "Settings", href: "/settings", icon: Settings },
    { label: "Help", href: "/help", icon: HelpCircle },
]

/* ============================================================================
   NAV ITEM COMPONENT - Premium Polish Edition
   ============================================================================ */

interface NavItemProps {
    item: NavItem
    isActive: boolean
    collapsed: boolean
}

function NavItemComponent({ item, isActive, collapsed }: NavItemProps) {
    const Icon = item.icon

    return (
        <Link
            href={item.href}
            prefetch={false}
            className={cn(
                "group relative flex items-center gap-3 px-3 py-2.5 rounded-xl",
                "transition-all duration-300 ease-out",
                isActive
                    ? [
                        // Active state: Focus Purple with Chill Mint glow
                        "bg-gradient-to-r from-purple-600 to-purple-500",
                        "text-white font-medium",
                        "shadow-[0_0_20px_rgba(34,211,172,0.3),0_4px_12px_rgba(139,92,246,0.4)]",
                        "border border-purple-400/30"
                    ]
                    : [
                        // Inactive state
                        "text-zinc-400",
                        "hover:text-zinc-200",
                        "hover:bg-zinc-800/60",
                        "hover:shadow-[0_0_12px_rgba(34,211,172,0.15)]",
                        "border border-transparent hover:border-zinc-700/50"
                    ],
                collapsed && "justify-center px-2"
            )}
        >
            {/* Subtle glow effect behind icon when active */}
            {isActive && (
                <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-purple-600/20 to-emerald-500/10 blur-xl -z-10" />
            )}

            <Icon className={cn(
                "h-5 w-5 shrink-0 transition-all duration-300",
                isActive
                    ? "drop-shadow-[0_0_6px_rgba(34,211,172,0.6)]"
                    : "group-hover:scale-110 group-hover:text-emerald-400"
            )} />

            {/* Label - hidden when collapsed */}
            {!collapsed && (
                <span className={cn(
                    "text-sm truncate transition-colors duration-200",
                    isActive ? "font-semibold" : "font-medium"
                )}>
                    {item.label}
                </span>
            )}

            {/* Active indicator dot */}
            {isActive && !collapsed && (
                <div className={cn(
                    "absolute right-3 w-1.5 h-1.5 rounded-full",
                    "bg-emerald-400 shadow-[0_0_8px_rgba(34,211,172,0.8)]",
                    "animate-pulse"
                )} />
            )}

            {/* Tooltip when collapsed */}
            {collapsed && (
                <div className={cn(
                    "absolute left-full ml-3 px-3 py-1.5 rounded-lg",
                    "bg-zinc-900 border border-zinc-700/50",
                    "text-zinc-200 text-xs font-medium whitespace-nowrap",
                    "opacity-0 invisible group-hover:opacity-100 group-hover:visible",
                    "transition-all duration-200 z-50",
                    "shadow-lg shadow-black/40",
                    "pointer-events-none"
                )}>
                    {item.label}
                    {/* Arrow */}
                    <div className={cn(
                        "absolute top-1/2 -left-1.5 -translate-y-1/2",
                        "border-[6px] border-transparent border-r-zinc-900"
                    )} />
                </div>
            )}
        </Link>
    )
}

/* ============================================================================
   MAIN SIDEBAR COMPONENT - Premium Polish Edition
   ============================================================================ */

export function Sidebar({ collapsed = false, onToggleCollapse, className }: SidebarProps) {
    const pathname = usePathname()
    const { user } = useAuth()

    // Check if user is admin
    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    const isActive = (href: string) => {
        if (!pathname) return false
        if (href === "/dashboard") {
            return pathname === "/dashboard" || pathname === "/"
        }
        return pathname.startsWith(href)
    }

    // Filter nav items based on admin status
    const visibleNavItems = mainNavItems.filter(item => !item.adminOnly || isAdmin)

    return (
        <aside className={cn(
            "fixed left-0 top-0 z-40 h-screen flex flex-col",
            // Premium dark glassmorphism
            "bg-zinc-950/95 backdrop-blur-xl",
            "border-r border-zinc-800/60",
            // Subtle gradient overlay
            "before:absolute before:inset-0 before:bg-gradient-to-b before:from-purple-950/10 before:to-transparent before:pointer-events-none",
            "transition-all duration-300 ease-out",
            collapsed ? "w-[72px]" : "w-[240px]",
            className
        )}>
            {/* Logo Section */}
            <div className={cn(
                "relative flex items-center h-16 px-4",
                "border-b border-zinc-800/60",
                collapsed ? "justify-center px-2" : "justify-center"
            )}>
                <Link
                    href="/dashboard"
                    className={cn(
                        "flex items-center",
                        "transition-all duration-300",
                        "hover:opacity-80"
                    )}
                >
                    {/* DevOpsHub Logo - Full word in badge */}
                    {!collapsed ? (
                        <div className={cn(
                            "flex items-center px-3 py-1.5 rounded-lg",
                            "bg-gradient-to-r from-purple-600 to-purple-500",
                            "shadow-[0_0_20px_rgba(139,92,246,0.4)]"
                        )}>
                            <span className="text-base font-bold text-white tracking-tight">
                                DevOpsHub
                            </span>
                        </div>
                    ) : (
                        /* Collapsed: Only show D icon */
                        <div className={cn(
                            "w-8 h-8 rounded-lg",
                            "bg-gradient-to-br from-purple-500 to-purple-700",
                            "flex items-center justify-center",
                            "shadow-[0_0_20px_rgba(139,92,246,0.4)]",
                            "text-white font-bold text-sm"
                        )}>
                            D
                        </div>
                    )}
                </Link>
            </div>

            {/* Main Navigation */}
            <nav className="relative flex-1 px-3 py-4 space-y-1.5 overflow-y-auto">
                {visibleNavItems.map((item) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                        collapsed={collapsed}
                    />
                ))}
            </nav>

            {/* Bottom Section */}
            <div className={cn(
                "relative px-3 py-4 space-y-1.5",
                "border-t border-zinc-800/60"
            )}>
                {bottomNavItems.map((item) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                        collapsed={collapsed}
                    />
                ))}

                {/* Collapse Toggle - Premium Style */}
                <button
                    onClick={onToggleCollapse}
                    className={cn(
                        "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl",
                        "text-zinc-500 hover:text-zinc-300",
                        "hover:bg-zinc-800/40",
                        "border border-transparent hover:border-zinc-700/30",
                        "transition-all duration-200",
                        collapsed && "justify-center px-2"
                    )}
                    aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
                >
                    {collapsed ? (
                        <ChevronRight className="h-5 w-5 transition-transform hover:translate-x-0.5" />
                    ) : (
                        <>
                            <ChevronLeft className="h-5 w-5 transition-transform hover:-translate-x-0.5" />
                            <span className="text-sm font-medium">Collapse</span>
                        </>
                    )}
                </button>
            </div>
        </aside>
    )
}

export default Sidebar
