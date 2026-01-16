"use client"

/**
 * ============================================================================
 * APP SHELL - Main Application Layout Wrapper
 * ============================================================================
 *
 * Design Philosophy:
 * - Responsive layout with sidebar, topbar, and mobile nav
 * - Smooth transitions between breakpoints
 * - Persistent sidebar state
 * - Clean content area with proper spacing
 *
 * Breakpoints:
 * - Mobile: < 768px (bottom nav, no sidebar)
 * - Tablet: 768px - 1024px (collapsed sidebar)
 * - Desktop: > 1024px (full sidebar)
 *
 * @phase D.3 - Navigation + Layout
 */

import * as React from "react"
import { cn } from "@/lib/utils"
import { Sidebar } from "./Sidebar"
import { TopBar } from "./TopBar"
import { MobileNav } from "./MobileNav"
import { MobileSideMenu } from "./MobileSideMenu"
import { Breadcrumbs } from "./Breadcrumbs"

/* ============================================================================
   TYPES
   ============================================================================ */

interface AppShellProps {
    children: React.ReactNode
    showBreadcrumbs?: boolean
    className?: string
}

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

    // Load from localStorage on mount
    React.useEffect(() => {
        const stored = localStorage.getItem("sidebar-collapsed")
        if (stored !== null) {
            setCollapsed(stored === "true")
        }
    }, [])

    const toggle = React.useCallback(() => {
        setCollapsed(prev => {
            const newValue = !prev
            localStorage.setItem("sidebar-collapsed", String(newValue))
            return newValue
        })
    }, [])

    return { collapsed, toggle }
}

/* ============================================================================
   MAIN APP SHELL COMPONENT
   ============================================================================ */

export function AppShell({ children, showBreadcrumbs = true, className }: AppShellProps) {
    const { collapsed, toggle } = useSidebarState()
    const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false)
    const isDesktop = useMediaQuery("(min-width: 1024px)")
    const isTablet = useMediaQuery("(min-width: 768px)")
    const isMobile = !isTablet

    // Auto-collapse on tablet
    const effectiveCollapsed = isTablet && !isDesktop ? true : collapsed

    // Handle mobile menu
    const handleOpenMobileMenu = React.useCallback(() => {
        setMobileMenuOpen(true)
    }, [])

    const handleCloseMobileMenu = React.useCallback(() => {
        setMobileMenuOpen(false)
    }, [])

    return (
        <div className="min-h-screen bg-neutral-50 dark:bg-neutral-950">
            {/* Mobile Side Menu */}
            {isMobile && (
                <MobileSideMenu
                    isOpen={mobileMenuOpen}
                    onClose={handleCloseMobileMenu}
                />
            )}

            {/* Sidebar - hidden on mobile */}
            {isTablet && (
                <Sidebar
                    collapsed={effectiveCollapsed}
                    onToggleCollapse={toggle}
                />
            )}

            {/* Main content area */}
            <div className={cn(
                "min-h-screen transition-all duration-300",
                isTablet && (effectiveCollapsed ? "pl-[72px]" : "pl-[240px]"),
                isMobile && "pb-20" // Space for mobile nav
            )}>
                {/* Top bar */}
                <TopBar
                    showMenuButton={isMobile}
                    onMenuClick={handleOpenMobileMenu}
                />

                {/* Page content */}
                <main className={cn("px-3 py-4 sm:px-4 sm:py-6 md:px-6 lg:px-8", className)}>
                    {/* Breadcrumbs */}
                    {showBreadcrumbs && (
                        <div className="mb-4 sm:mb-6">
                            <Breadcrumbs />
                        </div>
                    )}

                    {/* Page content with fade-in animation */}
                    <div className="animate-fade-in">
                        {children}
                    </div>
                </main>
            </div>

            {/* Mobile navigation - shown only on mobile */}
            {isMobile && <MobileNav />}
        </div>
    )
}

export default AppShell
