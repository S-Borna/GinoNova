"use client"

/**
 * ============================================================================
 * APP LAYOUT — Protected Application Shell
 * ============================================================================
 *
 * Authenticated layout wrapping all app pages.
 * Includes Sidebar, TopBar, MobileNav from D.3 design sprint.
 * Protected by auth - redirects to login if not authenticated.
 *
 * @phase A.3 - App Shell & Routing
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { AuthProvider, useAuth } from "@/components/auth"
import { useRouter } from "next/navigation"
import { Sidebar } from "@/components/layout/Sidebar"
import { TopBar } from "@/components/layout/TopBar"
import { MobileNav } from "@/components/layout/MobileNav"
import { Breadcrumbs } from "@/components/layout/Breadcrumbs"

/* ============================================================================
   HOOKS
   ============================================================================ */

function useMediaQuery(query: string): boolean {
    const [matches, setMatches] = React.useState(false)

    React.useEffect(() => {
        const media = window.matchMedia(query)
        if (media.matches !== matches) {
            setMatches(media.matches)
        }

        const listener = () => setMatches(media.matches)
        media.addEventListener("change", listener)
        return () => media.removeEventListener("change", listener)
    }, [matches, query])

    return matches
}

function useSidebarState() {
    const [collapsed, setCollapsed] = React.useState(false)

    React.useEffect(() => {
        const stored = localStorage.getItem("sidebar-collapsed")
        if (stored !== null) {
            setCollapsed(stored === "true")
        }
    }, [])

    const toggle = React.useCallback(() => {
        setCollapsed((prev) => {
            const newValue = !prev
            localStorage.setItem("sidebar-collapsed", String(newValue))
            return newValue
        })
    }, [])

    return { collapsed, toggle }
}

/* ============================================================================
   LOADING SCREEN
   ============================================================================ */

function LoadingScreen() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-neutral-50 dark:bg-neutral-950">
            <div className="flex flex-col items-center gap-4">
                <div className="relative">
                    <div className="w-16 h-16 rounded-full border-4 border-neutral-200 dark:border-neutral-800" />
                    <div className="absolute inset-0 w-16 h-16 rounded-full border-4 border-transparent border-t-primary-500 animate-spin" />
                </div>
                <p className="text-neutral-600 dark:text-neutral-400 text-sm font-medium">
                    Loading My DOE Hub...
                </p>
            </div>
        </div>
    )
}

/* ============================================================================
   APP LAYOUT INNER — Uses auth hooks
   ============================================================================ */

function AppLayoutInner({ children }: { children: React.ReactNode }) {
    const { user, loading } = useAuth()
    const router = useRouter()
    const { collapsed, toggle } = useSidebarState()
    const isDesktop = useMediaQuery("(min-width: 1024px)")
    const isTablet = useMediaQuery("(min-width: 768px)")
    const isMobile = !isTablet

    // Redirect to login if not authenticated
    React.useEffect(() => {
        if (!loading && !user) {
            router.push("/login")
        }
    }, [user, loading, router])

    // Show loading while checking auth
    if (loading) {
        return <LoadingScreen />
    }

    // Don't render if no user (will redirect)
    if (!user) {
        return <LoadingScreen />
    }

    // Auto-collapse on tablet
    const effectiveCollapsed = isTablet && !isDesktop ? true : collapsed

    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            {/* Sidebar - hidden on mobile */}
            {isTablet && (
                <Sidebar
                    collapsed={effectiveCollapsed}
                    onToggleCollapse={toggle}
                />
            )}

            {/* Main content area */}
            <div
                className={cn(
                    "min-h-screen transition-all duration-300",
                    isTablet && (effectiveCollapsed ? "pl-[72px]" : "pl-[240px]"),
                    isMobile && "pb-20" // Space for mobile nav
                )}
            >
                {/* Top bar */}
                <TopBar showMenuButton={isMobile} />

                {/* Page content */}
                <main className="px-4 py-6 md:px-6 lg:px-8">
                    {/* Breadcrumbs */}
                    <div className="mb-6">
                        <Breadcrumbs />
                    </div>

                    {/* Page content with fade-in animation */}
                    <div className="animate-fade-in">{children}</div>
                </main>
            </div>

            {/* Mobile navigation - shown only on mobile */}
            {isMobile && <MobileNav />}
        </div>
    )
}

/* ============================================================================
   APP LAYOUT — Wrapper with AuthProvider
   ============================================================================ */

export function AppLayoutClient({ children }: { children: React.ReactNode }) {
    return (
        <AuthProvider>
            <AppLayoutInner>{children}</AppLayoutInner>
        </AuthProvider>
    )
}
