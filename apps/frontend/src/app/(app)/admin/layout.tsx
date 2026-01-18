"use client"

/**
 * Admin v2 Layout - Sidebar navigation with mobile support
 */

import { ReactNode, useState, useEffect } from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import {
    LayoutDashboard,
    Users,
    BarChart3,
    Bot,
    Settings,
    ChevronLeft,
    Shield,
    Menu,
    X
} from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const navItems = [
    { href: "/admin", icon: LayoutDashboard, label: "Dashboard" },
    { href: "/admin/users", icon: Users, label: "Users" },
    { href: "/admin/analytics", icon: BarChart3, label: "Analytics" },
    { href: "/admin/ai-usage", icon: Bot, label: "AI Usage" },
    { href: "/admin/settings", icon: Settings, label: "Settings" },
]

export default function AdminV2Layout({ children }: { children: ReactNode }) {
    const pathname = usePathname()
    const { user, loading } = useAuth()
    const [sidebarOpen, setSidebarOpen] = useState(false)

    // Close sidebar when route changes (mobile)
    useEffect(() => {
        setSidebarOpen(false)
    }, [pathname])

    // Close sidebar on escape key
    useEffect(() => {
        const handleEscape = (e: KeyboardEvent) => {
            if (e.key === "Escape") setSidebarOpen(false)
        }
        document.addEventListener("keydown", handleEscape)
        return () => document.removeEventListener("keydown", handleEscape)
    }, [])

    // Show loading state while checking auth
    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-purple-500 mx-auto mb-4 animate-pulse" />
                    <p className="text-zinc-400">Loading admin panel...</p>
                </div>
            </div>
        )
    }

    // Check admin access
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"

    if (!user || !isAdmin) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-red-500 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold mb-2">Access Denied</h1>
                    <p className="text-zinc-400 mb-4">You need admin privileges to access this area.</p>
                    <Link href="/dashboard" className="text-purple-400 hover:underline">
                        ← Back to Dashboard
                    </Link>
                </div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-zinc-950 text-white flex flex-col md:flex-row">
            {/* Mobile Header */}
            <header className="md:hidden flex items-center justify-between p-4 bg-zinc-900/80 border-b border-zinc-800 sticky top-0 z-40">
                <div className="flex items-center gap-2">
                    <Shield className="w-5 h-5 text-purple-500" />
                    <span className="font-bold">Admin</span>
                </div>
                <button
                    onClick={() => setSidebarOpen(!sidebarOpen)}
                    className="p-2 rounded-lg hover:bg-zinc-800 transition-colors"
                    aria-label={sidebarOpen ? "Close menu" : "Open menu"}
                >
                    {sidebarOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
                </button>
            </header>

            {/* Mobile Overlay */}
            {sidebarOpen && (
                <div
                    className="md:hidden fixed inset-0 bg-black/60 z-40"
                    onClick={() => setSidebarOpen(false)}
                    aria-hidden="true"
                />
            )}

            {/* Sidebar - Hidden on mobile, slide-in when open */}
            <aside className={cn(
                "bg-zinc-900/95 md:bg-zinc-900/50 border-r border-zinc-800 flex flex-col",
                // Desktop: always visible, fixed width
                "md:w-64 md:relative md:translate-x-0",
                // Mobile: fixed overlay, slide in/out
                "fixed inset-y-0 left-0 w-72 z-50 transform transition-transform duration-300 ease-in-out",
                sidebarOpen ? "translate-x-0" : "-translate-x-full md:translate-x-0"
            )}>
                {/* Header */}
                <div className="p-4 border-b border-zinc-800">
                    {/* Mobile close button */}
                    <div className="md:hidden flex justify-end mb-2">
                        <button
                            onClick={() => setSidebarOpen(false)}
                            className="p-1 rounded hover:bg-zinc-800"
                            aria-label="Close sidebar"
                        >
                            <X className="w-5 h-5 text-zinc-400" />
                        </button>
                    </div>
                    <Link href="/dashboard" className="flex items-center gap-2 text-zinc-400 hover:text-white text-sm mb-3">
                        <ChevronLeft className="w-4 h-4" />
                        Back to App
                    </Link>
                    <h1 className="text-xl font-bold flex items-center gap-2">
                        <Shield className="w-6 h-6 text-purple-500" />
                        Admin
                    </h1>
                </div>

                {/* Navigation */}
                <nav className="flex-1 p-3 overflow-y-auto">
                    <ul className="space-y-1">
                        {navItems.map((item) => {
                            const isActive = pathname === item.href ||
                                (item.href !== "/admin" && pathname.startsWith(item.href))

                            return (
                                <li key={item.href}>
                                    <Link
                                        href={item.href}
                                        className={cn(
                                            "flex items-center gap-3 px-3 py-3 md:py-2 rounded-lg transition-colors",
                                            isActive
                                                ? "bg-purple-600 text-white"
                                                : "text-zinc-400 hover:text-white hover:bg-zinc-800"
                                        )}
                                        onClick={() => setSidebarOpen(false)}
                                    >
                                        <item.icon className="w-5 h-5" />
                                        {item.label}
                                    </Link>
                                </li>
                            )
                        })}
                    </ul>
                </nav>

                {/* Footer */}
                <div className="p-4 border-t border-zinc-800 text-xs text-zinc-500">
                    <p>Logged in as:</p>
                    <p className="text-zinc-300 truncate">{user?.email}</p>
                </div>
            </aside>

            {/* Main Content */}
            <main className="flex-1 overflow-auto">
                {children}
            </main>
        </div>
    )
}
