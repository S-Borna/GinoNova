"use client"

/**
 * ============================================================================
 * APP LAYOUT — Public Application Shell (MILESTONE 2.0)
 * ============================================================================
 *
 * PUBLIC layout wrapping all app pages - NO AUTH REQUIRED!
 * Includes Sidebar, TopBar, MobileNav from D.3 design sprint.
 *
 * MILESTONE 2.0: Zero friction access - users can browse everything
 * without logging in. Auth is optional for saving progress.
 *
 * @phase MILESTONE-2.0 - Zero Friction Access
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { AuthProvider, useAuth } from "@/components/auth"
import { useRouter, usePathname } from "next/navigation"
import { Sidebar } from "@/components/layout/Sidebar"
import { TopBar } from "@/components/layout/TopBar"
import { MobileNav } from "@/components/layout/MobileNav"
import { Breadcrumbs } from "@/components/layout/Breadcrumbs"
import { RightSidebar } from "@/components/modules/RightSidebar"
import { CosmicLockedOverlay } from "@/components/ui/cosmic-locked-overlay"

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
    const pathname = usePathname()
    const { collapsed, toggle } = useSidebarState()
    const isDesktop = useMediaQuery("(min-width: 1024px)")
    const isTablet = useMediaQuery("(min-width: 768px)")
    const isMobile = !isTablet

    // RightSidebar disabled for modules - Camp DevOps uses clean full-width layout
    // const showRightSidebar = isDesktop && pathname?.includes("/modules/")
    const showRightSidebar = false

    // MILESTONE 2.0: NO AUTH REDIRECT - App is now PUBLIC!
    // Users can browse all content without logging in.
    // Auth is optional - only needed for saving progress, AI quiz, etc.

    // Show brief loading only while auth state initializes (for optional user display)
    if (loading) {
        return <LoadingScreen />
    }

    // REMOVED: Auth wall - no more redirect to login!
    // Previously: if (!user) { router.push("/login") }
    // Now: Everyone can access content!

    // COSMIC LOCKED OVERLAY - Show for non-authenticated users on protected pages
    // Camp DevOps (/modules) is the ONLY publicly accessible content
    const isPublicPage = pathname?.startsWith("/modules") ||
        pathname === "/" ||
        pathname === "/login" ||
        pathname === "/register"
    const showLockedOverlay = !user && !isPublicPage

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
                    showRightSidebar && "pr-[280px]", // Space for right sidebar only on task pages
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

            {/* Right Sidebar - Bookmarks (on all module pages) */}
            {showRightSidebar && (
                <aside className={cn(
                    "fixed right-0 top-0 z-30 h-screen w-[280px]",
                    "bg-zinc-950/95 backdrop-blur-xl",
                    "border-l border-zinc-800/60"
                )}>
                    <RightSidebar />
                </aside>
            )}

            {/* Mobile navigation - shown only on mobile */}
            {isMobile && <MobileNav />}

            {/* Cosmic Locked Overlay - Shows on protected pages for non-authenticated users */}
            {showLockedOverlay && <CosmicLockedOverlay />}
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
