"use client"

/**
 * ============================================================================
 * BREADCRUMBS - Navigation Context Display
 * ============================================================================
 * 
 * Design Philosophy:
 * - Auto-generated from current route
 * - Clickable ancestor links
 * - Current page non-clickable
 * - Truncates on mobile
 * 
 * @phase D.3 - Navigation + Layout
 */

import * as React from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { cn } from "@/lib/utils"
import { ChevronRight, Home } from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface BreadcrumbsProps {
    className?: string
    homeLabel?: string
    maxItems?: number
}

interface BreadcrumbItem {
    label: string
    href: string
    isCurrent: boolean
}

/* ============================================================================
   ROUTE LABEL MAPPING
   ============================================================================ */

const routeLabels: Record<string, string> = {
    dashboard: "Dashboard",
    modules: "Modules",
    studyflow: "Studyflow",
    progress: "Progress",
    profile: "Profile",
    settings: "Settings",
    help: "Help",
    tasks: "Tasks",
    login: "Login",
    register: "Register",
    new: "New",
    edit: "Edit",
}

function formatSegment(segment: string, prevSegment?: string): string {
    // Check if it's a known route
    if (routeLabels[segment.toLowerCase()]) {
        return routeLabels[segment.toLowerCase()]
    }
    
    // Check if it's a UUID or ID - show contextual name based on previous segment
    if (segment.match(/^[0-9a-f-]{36}$/i) || segment.match(/^\d+$/)) {
        // Context-aware naming
        if (prevSegment === "modules") return "Module"
        if (prevSegment === "tasks") return "Task"
        if (prevSegment === "tracks") return "Track"
        return "Details"
    }
    
    // Convert slug to title case
    return segment
        .split(/[-_]/)
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(" ")
}

/* ============================================================================
   MAIN BREADCRUMBS COMPONENT
   ============================================================================ */

export function Breadcrumbs({ 
    className, 
    homeLabel = "Home",
    maxItems = 4 
}: BreadcrumbsProps) {
    const pathname = usePathname()
    
    const breadcrumbs = React.useMemo((): BreadcrumbItem[] => {
        if (!pathname) return []
        
        const segments = pathname.split("/").filter(Boolean)
        
        // Build breadcrumb items
        const items: BreadcrumbItem[] = segments.map((segment, index) => {
            const href = "/" + segments.slice(0, index + 1).join("/")
            const isCurrent = index === segments.length - 1
            const prevSegment = index > 0 ? segments[index - 1] : undefined
            
            return {
                label: formatSegment(segment, prevSegment),
                href,
                isCurrent
            }
        })

        // Truncate if too many items
        if (items.length > maxItems) {
            const first = items[0]
            const last = items.slice(-2)
            return [
                first,
                { label: "...", href: "#", isCurrent: false },
                ...last
            ]
        }

        return items
    }, [pathname, maxItems])

    // Don't render if on home/dashboard with no segments
    if (breadcrumbs.length === 0) return null

    return (
        <nav 
            aria-label="Breadcrumb"
            className={cn("flex items-center", className)}
        >
            <ol className="flex items-center gap-1 text-sm">
                {/* Home link */}
                <li>
                    <Link
                        href="/dashboard"
                        className={cn(
                            "flex items-center gap-1 px-2 py-1 rounded-md",
                            "text-neutral-500 dark:text-neutral-400",
                            "hover:text-neutral-700 dark:hover:text-neutral-200",
                            "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                            "transition-colors duration-150"
                        )}
                    >
                        <Home className="h-4 w-4" />
                        <span className="sr-only md:not-sr-only">{homeLabel}</span>
                    </Link>
                </li>

                {/* Breadcrumb items */}
                {breadcrumbs.map((item, index) => (
                    <li key={item.href + index} className="flex items-center">
                        <ChevronRight className="h-4 w-4 text-neutral-300 dark:text-neutral-600 mx-1" />
                        
                        {item.isCurrent ? (
                            <span 
                                className={cn(
                                    "px-2 py-1 font-medium",
                                    "text-neutral-900 dark:text-white",
                                    "max-w-[150px] truncate"
                                )}
                                aria-current="page"
                            >
                                {item.label}
                            </span>
                        ) : item.label === "..." ? (
                            <span className="px-2 py-1 text-neutral-400">
                                {item.label}
                            </span>
                        ) : (
                            <Link
                                href={item.href}
                                className={cn(
                                    "px-2 py-1 rounded-md",
                                    "text-neutral-500 dark:text-neutral-400",
                                    "hover:text-neutral-700 dark:hover:text-neutral-200",
                                    "hover:bg-neutral-100 dark:hover:bg-neutral-800",
                                    "transition-colors duration-150",
                                    "max-w-[120px] truncate"
                                )}
                            >
                                {item.label}
                            </Link>
                        )}
                    </li>
                ))}
            </ol>
        </nav>
    )
}

export default Breadcrumbs
