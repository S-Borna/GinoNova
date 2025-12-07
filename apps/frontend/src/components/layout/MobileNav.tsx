"use client"

/**
 * ============================================================================
 * MOBILE NAVIGATION - Bottom Tab Bar
 * ============================================================================
 * 
 * Design Philosophy:
 * - iOS tab bar inspired design
 * - Safe area padding for notched phones
 * - Active state with filled icons
 * - Subtle tap feedback animation
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

interface MobileNavProps {
    className?: string
}

/* ============================================================================
   NAVIGATION CONFIG
   ============================================================================ */

const navItems: NavItem[] = [
    { label: "Home", href: "/dashboard", icon: Home },
    { label: "Modules", href: "/modules", icon: BookOpen },
    { label: "Studyroom", href: "/study", icon: Clock },
    { label: "Progress", href: "/progress", icon: BarChart3 },
    { label: "Profile", href: "/profile", icon: User },
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
                "flex flex-col items-center justify-center gap-1 flex-1 py-2",
                "transition-all duration-150 ease-out",
                "active:scale-95", // Haptic-feel tap feedback
                isActive
                    ? "text-primary-600 dark:text-primary-400"
                    : "text-neutral-400 dark:text-neutral-500"
            )}
        >
            <div className="relative">
                <Icon 
                    className={cn(
                        "h-6 w-6 transition-transform duration-200",
                        isActive && "scale-110"
                    )} 
                    strokeWidth={isActive ? 2.5 : 2}
                />
                {/* Active indicator dot */}
                {isActive && (
                    <span className={cn(
                        "absolute -bottom-1 left-1/2 -translate-x-1/2",
                        "w-1 h-1 rounded-full",
                        "bg-primary-500"
                    )} />
                )}
            </div>
            <span className={cn(
                "text-[10px] font-medium transition-colors",
                isActive && "font-semibold"
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
            "bg-white/90 dark:bg-neutral-900/90 backdrop-blur-xl",
            "border-t border-neutral-200/50 dark:border-neutral-800/50",
            // Safe area padding for notched phones
            "pb-safe-area-inset-bottom",
            className
        )}>
            <div className="flex items-center justify-around px-2 pt-1">
                {navItems.map((item) => (
                    <NavItemComponent
                        key={item.href}
                        item={item}
                        isActive={isActive(item.href)}
                    />
                ))}
            </div>
            
            {/* Home indicator spacing (iOS) */}
            <div className="h-1 md:hidden" />
        </nav>
    )
}

export default MobileNav
