"use client"

/**
 * ============================================================================
 * TOP BAR - Premium Header Navigation
 * ============================================================================
 * 
 * Design Philosophy:
 * - Clean, minimal header with essential controls
 * - Breadcrumbs for navigation context
 * - User menu with dropdown
 * - Notifications bell with badge
 * 
 * @phase D.3 - Navigation + Layout
 */

import * as React from "react"
import Link from "next/link"
import { usePathname, useRouter } from "next/navigation"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import { Button } from "@/components/ui/button"
import {
    Bell,
    Search,
    Settings,
    LogOut,
    User,
    Moon,
    Sun,
    ChevronDown,
    Menu
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface TopBarProps {
    onMenuClick?: () => void
    showMenuButton?: boolean
    className?: string
}

/* ============================================================================
   USER DROPDOWN
   ============================================================================ */

function UserDropdown() {
    const { user, logout } = useAuth()
    const router = useRouter()
    const [isOpen, setIsOpen] = React.useState(false)
    const dropdownRef = React.useRef<HTMLDivElement>(null)

    // Close on outside click
    React.useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsOpen(false)
            }
        }
        document.addEventListener("mousedown", handleClickOutside)
        return () => document.removeEventListener("mousedown", handleClickOutside)
    }, [])

    const handleLogout = async () => {
        await logout()
        router.push("/login")
    }

    const userInitial = user?.full_name?.[0] || user?.email?.[0] || "?"

    return (
        <div ref={dropdownRef} className="relative">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-xl",
                    "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                    "transition-colors duration-150"
                )}
            >
                {/* Avatar */}
                <div className={cn(
                    "w-8 h-8 rounded-full flex items-center justify-center",
                    "bg-gradient-to-br from-primary-400 to-primary-600",
                    "text-white text-sm font-medium"
                )}>
                    {userInitial}
                </div>
                
                {/* Name (hidden on mobile) */}
                <span className="hidden md:block text-sm font-medium text-neutral-700 dark:text-neutral-300 max-w-[120px] truncate">
                    {user?.full_name || user?.email?.split("@")[0] || "User"}
                </span>
                
                <ChevronDown className={cn(
                    "h-4 w-4 text-neutral-400 transition-transform duration-200",
                    isOpen && "rotate-180"
                )} />
            </button>

            {/* Dropdown menu */}
            {isOpen && (
                <div className={cn(
                    "absolute right-0 top-full mt-2 w-56",
                    "bg-white dark:bg-neutral-900",
                    "border border-neutral-200 dark:border-neutral-800",
                    "rounded-xl shadow-lg",
                    "py-2 z-50",
                    "animate-fade-in-up"
                )}>
                    {/* User info */}
                    <div className="px-4 py-2 border-b border-neutral-100 dark:border-neutral-800">
                        <p className="text-sm font-medium text-neutral-900 dark:text-white truncate">
                            {user?.full_name || "User"}
                        </p>
                        <p className="text-xs text-neutral-500 dark:text-neutral-400 truncate">
                            {user?.email}
                        </p>
                    </div>

                    {/* Menu items */}
                    <div className="py-1">
                        <Link
                            href="/profile"
                            onClick={() => setIsOpen(false)}
                            className={cn(
                                "flex items-center gap-3 px-4 py-2 text-sm",
                                "text-neutral-700 dark:text-neutral-300",
                                "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                "transition-colors"
                            )}
                        >
                            <User className="h-4 w-4" />
                            Profile
                        </Link>
                        
                        <Link
                            href="/settings"
                            onClick={() => setIsOpen(false)}
                            className={cn(
                                "flex items-center gap-3 px-4 py-2 text-sm",
                                "text-neutral-700 dark:text-neutral-300",
                                "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                "transition-colors"
                            )}
                        >
                            <Settings className="h-4 w-4" />
                            Settings
                        </Link>

                        <button
                            onClick={() => {
                                // Toggle theme (placeholder)
                                document.documentElement.classList.toggle("dark")
                                setIsOpen(false)
                            }}
                            className={cn(
                                "w-full flex items-center gap-3 px-4 py-2 text-sm",
                                "text-neutral-700 dark:text-neutral-300",
                                "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                "transition-colors"
                            )}
                        >
                            <Sun className="h-4 w-4 dark:hidden" />
                            <Moon className="h-4 w-4 hidden dark:block" />
                            Toggle Theme
                        </button>
                    </div>

                    {/* Logout */}
                    <div className="border-t border-neutral-100 dark:border-neutral-800 pt-1">
                        <button
                            onClick={handleLogout}
                            className={cn(
                                "w-full flex items-center gap-3 px-4 py-2 text-sm",
                                "text-red-600 dark:text-red-400",
                                "hover:bg-red-50 dark:hover:bg-red-900/20",
                                "transition-colors"
                            )}
                        >
                            <LogOut className="h-4 w-4" />
                            Sign out
                        </button>
                    </div>
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   NOTIFICATION BELL
   ============================================================================ */

function NotificationBell() {
    const [hasUnread] = React.useState(true) // Placeholder

    return (
        <button
            className={cn(
                "relative p-2 rounded-xl",
                "text-neutral-600 dark:text-neutral-400",
                "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                "transition-colors duration-150"
            )}
            aria-label="Notifications"
        >
            <Bell className="h-5 w-5" />
            {hasUnread && (
                <span className={cn(
                    "absolute top-1.5 right-1.5 w-2 h-2",
                    "bg-red-500 rounded-full",
                    "ring-2 ring-white dark:ring-neutral-900"
                )} />
            )}
        </button>
    )
}

/* ============================================================================
   SEARCH BAR (Placeholder)
   ============================================================================ */

function SearchBar() {
    return (
        <div className={cn(
            "hidden lg:flex items-center gap-2 px-3 py-2",
            "bg-neutral-100 dark:bg-neutral-800/50",
            "rounded-xl border border-transparent",
            "focus-within:border-primary-300 dark:focus-within:border-primary-700",
            "focus-within:bg-white dark:focus-within:bg-neutral-800",
            "transition-all duration-200"
        )}>
            <Search className="h-4 w-4 text-neutral-400" />
            <input
                type="text"
                placeholder="Search..."
                className={cn(
                    "w-48 bg-transparent text-sm",
                    "text-neutral-900 dark:text-white",
                    "placeholder:text-neutral-400",
                    "focus:outline-none"
                )}
            />
            <kbd className="hidden xl:inline-flex h-5 items-center gap-1 rounded border border-neutral-200 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-800 px-1.5 font-mono text-[10px] text-neutral-500">
                ⌘K
            </kbd>
        </div>
    )
}

/* ============================================================================
   MAIN TOP BAR COMPONENT
   ============================================================================ */

export function TopBar({ onMenuClick, showMenuButton = false, className }: TopBarProps) {
    return (
        <header className={cn(
            "sticky top-0 z-30 h-16",
            "bg-white/80 dark:bg-neutral-900/80 backdrop-blur-xl",
            "border-b border-neutral-200/50 dark:border-neutral-800/50",
            className
        )}>
            <div className="h-full px-4 flex items-center justify-between gap-4">
                {/* Left side */}
                <div className="flex items-center gap-4">
                    {/* Mobile menu button */}
                    {showMenuButton && (
                        <button
                            onClick={onMenuClick}
                            className={cn(
                                "lg:hidden p-2 rounded-xl",
                                "text-neutral-600 dark:text-neutral-400",
                                "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                "transition-colors"
                            )}
                            aria-label="Open menu"
                        >
                            <Menu className="h-5 w-5" />
                        </button>
                    )}

                    {/* Search */}
                    <SearchBar />
                </div>

                {/* Right side */}
                <div className="flex items-center gap-2">
                    <NotificationBell />
                    <UserDropdown />
                </div>
            </div>
        </header>
    )
}

export default TopBar
