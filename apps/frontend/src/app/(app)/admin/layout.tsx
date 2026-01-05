"use client"

/**
 * Admin v2 Layout - Sidebar navigation
 */

import { ReactNode } from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import {
    LayoutDashboard,
    Users,
    BarChart3,
    Bot,
    Settings,
    ChevronLeft,
    Shield
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
        <div className="min-h-screen bg-zinc-950 text-white flex">
            {/* Sidebar */}
            <aside className="w-64 bg-zinc-900/50 border-r border-zinc-800 flex flex-col">
                {/* Header */}
                <div className="p-4 border-b border-zinc-800">
                    <Link href="/dashboard" className="flex items-center gap-2 text-zinc-400 hover:text-white text-sm mb-3">
                        <ChevronLeft className="w-4 h-4" />
                        Back to App
                    </Link>
                    <h1 className="text-xl font-bold flex items-center gap-2">
                        <Shield className="w-6 h-6 text-purple-500" />
                        Admin v2
                    </h1>
                </div>

                {/* Navigation */}
                <nav className="flex-1 p-3">
                    <ul className="space-y-1">
                        {navItems.map((item) => {
                            const isActive = pathname === item.href ||
                                (item.href !== "/admin" && pathname.startsWith(item.href))

                            return (
                                <li key={item.href}>
                                    <Link
                                        href={item.href}
                                        className={cn(
                                            "flex items-center gap-3 px-3 py-2 rounded-lg transition-colors",
                                            isActive
                                                ? "bg-purple-600 text-white"
                                                : "text-zinc-400 hover:text-white hover:bg-zinc-800"
                                        )}
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
