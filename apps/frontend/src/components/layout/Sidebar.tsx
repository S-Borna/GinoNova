"use client"

/**
 * ============================================================================
 * SIDEBAR - Premium Desktop Navigation
 * ============================================================================
 * 
 * Design Philosophy:
 * - Apple-inspired clean navigation
 * - Collapsible with smooth animations
 * - Glassmorphism effect
 * - Active state with gradient background
 * 
 * @phase D.3 - Navigation + Layout
 */

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
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
    type LucideIcon
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface NavItem {
    label: string
    href: string
    icon: LucideIcon
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
    { label: "Modules", href: "/modules", icon: BookOpen },
    { label: "Studyflow", href: "/studyflow", icon: Clock },
    { label: "Progress", href: "/progress", icon: BarChart3 },
    { label: "Profile", href: "/profile", icon: User },
]

const bottomNavItems: NavItem[] = [
    { label: "Settings", href: "/settings", icon: Settings },
    { label: "Help", href: "/help", icon: HelpCircle },
]

/* ============================================================================
   NAV ITEM COMPONENT
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
            className={cn(
                "group relative flex items-center gap-3 px-3 py-2.5 rounded-xl",
                "transition-all duration-200 ease-out",
                isActive
                    ? "bg-gradient-to-r from-primary-500 to-primary-600 text-white shadow-md shadow-primary-500/25"
                    : "text-neutral-600 dark:text-neutral-400 hover:bg-neutral-100 dark:hover:bg-neutral-800/50",
                collapsed && "justify-center px-2"
            )}
        >
            <Icon className={cn(
                "h-5 w-5 shrink-0 transition-transform duration-200",
                !isActive && "group-hover:scale-110"
            )} />
            
            {/* Label - hidden when collapsed */}
            {!collapsed && (
                <span className="text-sm font-medium truncate">
                    {item.label}
                </span>
            )}

            {/* Tooltip when collapsed */}
            {collapsed && (
                <div className={cn(
                    "absolute left-full ml-2 px-2 py-1 rounded-md",
                    "bg-neutral-900 dark:bg-neutral-100 text-white dark:text-neutral-900",
                    "text-xs font-medium whitespace-nowrap",
                    "opacity-0 invisible group-hover:opacity-100 group-hover:visible",
                    "transition-all duration-150 z-50",
                    "pointer-events-none"
                )}>
                    {item.label}
                    {/* Arrow */}
                    <div className={cn(
                        "absolute top-1/2 -left-1 -translate-y-1/2",
                        "border-4 border-transparent border-r-neutral-900 dark:border-r-neutral-100"
                    )} />
                </div>
            )}
        </Link>
    )
}

/* ============================================================================
   MAIN SIDEBAR COMPONENT
   ============================================================================ */

export function Sidebar({ collapsed = false, onToggleCollapse, className }: SidebarProps) {
    const pathname = usePathname()

    const isActive = (href: string) => {
        if (!pathname) return false
        if (href === "/dashboard") {
            return pathname === "/dashboard" || pathname === "/"
        }
        return pathname.startsWith(href)
    }

    return (
        <aside className={cn(
            "fixed left-0 top-0 z-40 h-screen flex flex-col",
            "bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl",
            "border-r border-neutral-200/50 dark:border-neutral-800/50",
            "transition-all duration-300 ease-out",
            collapsed ? "w-[72px]" : "w-[240px]",
            className
        )}>
            {/* Logo Section */}
            <div className={cn(
                "flex items-center h-16 px-4",
                "border-b border-neutral-200/50 dark:border-neutral-800/50",
                collapsed && "justify-center px-2"
            )}>
                <Link href="/dashboard" className="flex items-center gap-3">
                    {/* Logo icon */}
                    <div className={cn(
                        "w-9 h-9 rounded-xl flex items-center justify-center shrink-0",
                        "bg-gradient-to-br from-primary-500 to-primary-600",
                        "shadow-lg shadow-primary-500/25"
                    )}>
                        <span className="text-white text-lg font-bold">D</span>
                    </div>
                    
                    {/* Logo text */}
                    {!collapsed && (
                        <span className="text-lg font-semibold text-neutral-900 dark:text-white">
                            DevOpsHub
                        </span>
                    )}
                </Link>
            </div>

            {/* Main Navigation */}
            <nav className="flex-1 px-3 py-4 space-y-1 overflow-y-auto">
                {mainNavItems.map((item) => (
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
                "px-3 py-4 space-y-1",
                "border-t border-neutral-200/50 dark:border-neutral-800/50"
            )}>
                {bottomNavItems.map((item) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                        collapsed={collapsed}
                    />
                ))}

                {/* Collapse Toggle */}
                <button
                    onClick={onToggleCollapse}
                    className={cn(
                        "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl",
                        "text-neutral-500 dark:text-neutral-400",
                        "hover:bg-neutral-100 dark:hover:bg-neutral-800/50",
                        "transition-colors duration-200",
                        collapsed && "justify-center px-2"
                    )}
                    aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
                >
                    {collapsed ? (
                        <ChevronRight className="h-5 w-5" />
                    ) : (
                        <>
                            <ChevronLeft className="h-5 w-5" />
                            <span className="text-sm font-medium">Collapse</span>
                        </>
                    )}
                </button>
            </div>
        </aside>
    )
}

export default Sidebar
