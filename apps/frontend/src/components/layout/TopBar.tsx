"use client"

/**
 * ============================================================================
 * TOP BAR - Enterprise Level 5 Header with GinoNova Branding
 * ============================================================================
 *
 * Design Philosophy:
 * - Premium glassmorphism with GinoNova glow radiation
 * - Centered logo with effects spilling across entire bar
 * - Command palette ready (⌘K)
 * - Enterprise-grade polish
 *
 * @phase ENTERPRISE-LEVEL-5
 */

import * as React from "react"
import Link from "next/link"
import Image from "next/image"
import { usePathname, useRouter } from "next/navigation"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import { Button } from "@/components/ui/button"
import { ThemeToggle } from "@/components/ui/ThemeToggle"
import {
    Search,
    Settings,
    LogOut,
    User,
    ChevronDown,
    Menu,
    Command,
    Clock,
    X
} from "lucide-react"
import { useSessionTimer } from "@/hooks/useSessionTimer"
import { NowPlayingWidget } from "@/components/tickers/SpotifyEmbed"
import { SpotifyTopBarWidget } from "@/components/spotify/SpotifyTopBarWidget"
import { AdminActivityFlash } from "@/components/admin/AdminActivityFlash"
import { AdminStatusWidget } from "@/components/admin/AdminStatusWidget"
import { AdminInboxWidget } from "@/components/admin/AdminInboxWidget"
import { UserBroadcast } from "@/components/broadcast/UserBroadcast"

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
                {/* Name (hidden on mobile) */}
                <span className="hidden md:block text-sm font-medium text-neutral-700 dark:text-neutral-300 max-w-[150px] truncate">
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
   SEARCH BAR - Global Search with Command Palette
   ============================================================================ */

interface SearchResult {
    id: string
    type: "module" | "skillmap" | "path" | "lesson"
    title: string
    description?: string
    url: string
    icon: string
}

// Mock search data - will be replaced with real API
const SEARCH_DATA: SearchResult[] = [
    // Main pages - these routes exist
    { id: "p1", type: "path", title: "Dashboard", description: "Your learning overview", url: "/dashboard", icon: "📊" },
    { id: "p2", type: "path", title: "All Modules", description: "Browse all learning modules", url: "/modules", icon: "📚" },
    { id: "p3", type: "path", title: "SkillPath Board", description: "Visual skill progression", url: "/skillpath-board", icon: "🗺️" },
    { id: "p4", type: "path", title: "Study Flow", description: "Focus mode learning", url: "/studyflow", icon: "🎯" },
    { id: "p5", type: "path", title: "Progress Tracker", description: "Track your achievements", url: "/progress", icon: "📈" },
    { id: "p6", type: "path", title: "Profile Settings", description: "Manage your account", url: "/profile", icon: "👤" },
    // Topics to search for in modules
    { id: "t1", type: "module", title: "Linux", description: "Command line & system admin", url: "/modules", icon: "🐧" },
    { id: "t2", type: "module", title: "Docker", description: "Containerization basics", url: "/modules", icon: "🐳" },
    { id: "t3", type: "module", title: "Kubernetes", description: "Container orchestration", url: "/modules", icon: "☸️" },
    { id: "t4", type: "module", title: "AWS", description: "Cloud fundamentals", url: "/modules", icon: "☁️" },
    { id: "t5", type: "module", title: "Python", description: "Scripting & automation", url: "/modules", icon: "🐍" },
    { id: "t6", type: "module", title: "CI/CD", description: "Pipelines & automation", url: "/modules", icon: "🚀" },
    // SkillMaps - point to skillpath board (8 complete, 156 nodes total)
    { id: "s1", type: "skillmap", title: "Python SkillMap", description: "21 nodes • Complete path", url: "/skillpath-board", icon: "🐍" },
    { id: "s2", type: "skillmap", title: "Linux SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "🐧" },
    { id: "s3", type: "skillmap", title: "Docker SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "🐳" },
    { id: "s4", type: "skillmap", title: "Kubernetes SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "☸️" },
    { id: "s5", type: "skillmap", title: "CI/CD SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "🚀" },
    { id: "s6", type: "skillmap", title: "Git & GitHub SkillMap", description: "15 nodes • Complete path", url: "/skillpath-board", icon: "📦" },
    { id: "s7", type: "skillmap", title: "Terraform SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "🏗️" },
    { id: "s8", type: "skillmap", title: "AWS SkillMap", description: "20 nodes • Complete path", url: "/skillpath-board", icon: "☁️" },
]

function SearchBar() {
    const [isOpen, setIsOpen] = React.useState(false)
    const [query, setQuery] = React.useState("")
    const [results, setResults] = React.useState<SearchResult[]>([])
    const inputRef = React.useRef<HTMLInputElement>(null)
    const router = useRouter()

    // Filter results based on query
    React.useEffect(() => {
        if (query.trim()) {
            const filtered = SEARCH_DATA.filter(item =>
                item.title.toLowerCase().includes(query.toLowerCase()) ||
                item.description?.toLowerCase().includes(query.toLowerCase())
            )
            setResults(filtered)
        } else {
            setResults([])
        }
    }, [query])

    // Keyboard shortcut ⌘K
    React.useEffect(() => {
        function handleKeyDown(e: KeyboardEvent) {
            if ((e.metaKey || e.ctrlKey) && e.key === "k") {
                e.preventDefault()
                setIsOpen(true)
                setTimeout(() => inputRef.current?.focus(), 100)
            }
            if (e.key === "Escape") {
                setIsOpen(false)
                setQuery("")
            }
        }
        document.addEventListener("keydown", handleKeyDown)
        return () => document.removeEventListener("keydown", handleKeyDown)
    }, [])

    const handleSelect = (result: SearchResult) => {
        router.push(result.url)
        setIsOpen(false)
        setQuery("")
    }

    const groupedResults = {
        module: results.filter(r => r.type === "module"),
        skillmap: results.filter(r => r.type === "skillmap"),
        path: results.filter(r => r.type === "path"),
    }

    return (
        <>
            {/* Search trigger button - Compact for sidebar */}
            <motion.button
                onClick={() => {
                    setIsOpen(true)
                    setTimeout(() => inputRef.current?.focus(), 100)
                }}
                className={cn(
                    "relative flex items-center gap-2 px-2.5 py-1.5",
                    "bg-zinc-900/60 backdrop-blur-sm",
                    "rounded-lg border border-zinc-700/50",
                    "hover:border-purple-500/40 hover:bg-zinc-800/70",
                    "transition-all duration-300",
                    "cursor-pointer group",
                    "shadow-md shadow-black/20"
                )}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                {/* Subtle glow on hover */}
                <div className="absolute inset-0 rounded-lg bg-gradient-to-r from-purple-500/0 via-purple-500/10 to-pink-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

                <Search className="relative h-3.5 w-3.5 text-zinc-500 group-hover:text-purple-400 transition-colors" />
                <span className="relative text-xs text-zinc-500 group-hover:text-zinc-300 transition-colors">Search...</span>
                <kbd className="relative hidden sm:inline-flex h-4 items-center rounded border border-zinc-700 bg-zinc-800/80 px-1 font-mono text-[9px] text-zinc-500 group-hover:border-purple-500/30 group-hover:text-purple-400 transition-colors">
                    ⌘K
                </kbd>
            </motion.button>

            {/* Search modal */}
            {isOpen && (
                <>
                    {/* Backdrop */}
                    <div
                        className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50"
                        onClick={() => {
                            setIsOpen(false)
                            setQuery("")
                        }}
                    />

                    {/* Modal */}
                    <div className={cn(
                        "fixed left-1/2 top-[20%] -translate-x-1/2 z-50",
                        "w-[90vw] max-w-xl",
                        "bg-white dark:bg-neutral-900",
                        "rounded-2xl shadow-2xl",
                        "border border-neutral-200 dark:border-neutral-700",
                        "overflow-hidden"
                    )}>
                        {/* Search input */}
                        <div className="flex items-center gap-3 px-4 py-3 border-b border-neutral-200 dark:border-neutral-700">
                            <Search className="h-5 w-5 text-neutral-400" />
                            <input
                                ref={inputRef}
                                type="text"
                                value={query}
                                onChange={(e) => setQuery(e.target.value)}
                                placeholder="Search modules, skillmaps, paths..."
                                className={cn(
                                    "flex-1 bg-transparent text-base",
                                    "text-neutral-900 dark:text-white",
                                    "placeholder:text-neutral-400",
                                    "focus:outline-none"
                                )}
                            />
                            <button
                                onClick={() => {
                                    setIsOpen(false)
                                    setQuery("")
                                }}
                                className="p-1.5 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
                                aria-label="Close search"
                            >
                                <X className="h-5 w-5 text-neutral-400" />
                            </button>
                        </div>

                        {/* Results */}
                        <div className="max-h-[50vh] overflow-y-auto">
                            {query && results.length === 0 && (
                                <div className="px-4 py-8 text-center text-neutral-500">
                                    No results found for &quot;{query}&quot;
                                </div>
                            )}

                            {!query && (
                                <div className="px-4 py-4">
                                    <p className="text-xs text-neutral-400 uppercase tracking-wide mb-3">Quick Links</p>
                                    <div className="grid grid-cols-2 gap-2">
                                        {SEARCH_DATA.slice(0, 6).map(item => (
                                            <button
                                                key={item.id}
                                                onClick={() => handleSelect(item)}
                                                className="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors text-left"
                                            >
                                                <span>{item.icon}</span>
                                                <span className="text-sm text-neutral-700 dark:text-neutral-300 truncate">{item.title}</span>
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Modules */}
                            {groupedResults.module.length > 0 && (
                                <div className="px-2 py-2">
                                    <p className="text-xs text-neutral-400 uppercase tracking-wide px-2 mb-1">Modules</p>
                                    {groupedResults.module.map(result => (
                                        <button
                                            key={result.id}
                                            onClick={() => handleSelect(result)}
                                            className="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
                                        >
                                            <span className="text-xl">{result.icon}</span>
                                            <div className="text-left">
                                                <p className="text-sm font-medium text-neutral-900 dark:text-white">{result.title}</p>
                                                <p className="text-xs text-neutral-500">{result.description}</p>
                                            </div>
                                        </button>
                                    ))}
                                </div>
                            )}

                            {/* SkillMaps */}
                            {groupedResults.skillmap.length > 0 && (
                                <div className="px-2 py-2">
                                    <p className="text-xs text-neutral-400 uppercase tracking-wide px-2 mb-1">SkillMaps</p>
                                    {groupedResults.skillmap.map(result => (
                                        <button
                                            key={result.id}
                                            onClick={() => handleSelect(result)}
                                            className="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
                                        >
                                            <span className="text-xl">{result.icon}</span>
                                            <div className="text-left">
                                                <p className="text-sm font-medium text-neutral-900 dark:text-white">{result.title}</p>
                                                <p className="text-xs text-neutral-500">{result.description}</p>
                                            </div>
                                        </button>
                                    ))}
                                </div>
                            )}

                            {/* Paths */}
                            {groupedResults.path.length > 0 && (
                                <div className="px-2 py-2">
                                    <p className="text-xs text-neutral-400 uppercase tracking-wide px-2 mb-1">Learning Paths</p>
                                    {groupedResults.path.map(result => (
                                        <button
                                            key={result.id}
                                            onClick={() => handleSelect(result)}
                                            className="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-colors"
                                        >
                                            <span className="text-xl">{result.icon}</span>
                                            <div className="text-left">
                                                <p className="text-sm font-medium text-neutral-900 dark:text-white">{result.title}</p>
                                                <p className="text-xs text-neutral-500">{result.description}</p>
                                            </div>
                                        </button>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                </>
            )}
        </>
    )
}

/* ============================================================================
   SESSION TIMER DISPLAY
   ============================================================================ */

function SessionTimerDisplay() {
    const [mounted, setMounted] = React.useState(false)
    const { currentSessionSeconds, formatTime } = useSessionTimer()

    // Prevent hydration mismatch
    React.useEffect(() => {
        setMounted(true)
    }, [])

    if (!mounted) {
        return (
            <div className={cn(
                "hidden md:flex items-center gap-2 px-3 py-1.5 rounded-xl",
                "bg-emerald-500/10 border border-emerald-500/20",
                "text-emerald-600 dark:text-emerald-400"
            )}>
                <span className="text-sm font-medium">Locked in!</span>
                <span className="text-sm font-mono font-medium">0:00</span>
            </div>
        )
    }

    return (
        <div className={cn(
            "hidden md:flex items-center gap-2 px-3 py-1.5 rounded-xl",
            "bg-emerald-500/10 border border-emerald-500/20",
            "text-emerald-600 dark:text-emerald-400"
        )}>
            <span className="text-sm font-medium">Locked in!</span>
            <span className="text-sm font-mono font-medium">
                {formatTime(currentSessionSeconds)}
            </span>
        </div>
    )
}

/* ============================================================================
   MAIN TOP BAR COMPONENT
   ============================================================================ */

export function TopBar({ onMenuClick, showMenuButton = false, className }: TopBarProps) {
    const { user } = useAuth()
    const isAuthenticated = !!user

    return (
        <header className={cn(
            "fixed top-0 left-0 right-0 z-50",
            "h-14 sm:h-16 lg:h-[72px]",
            "bg-[#0a0a12]/95 backdrop-blur-xl",
            "border-b border-purple-500/10",
            className
        )}>
            {/* GinoNova Glow Radiation - Full width */}
            <div className="absolute inset-0 pointer-events-none">
                {/* Left glow */}
                <motion.div
                    className="absolute left-0 top-0 bottom-0 w-1/3 mix-blend-screen"
                    style={{
                        background: "linear-gradient(90deg, rgba(139,92,246,0.24) 0%, rgba(139,92,246,0.08) 55%, transparent 100%)",
                    }}
                    animate={{
                        opacity: [0.5, 0.8, 0.5],
                    }}
                    transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                />

                {/* Center intense glow under logo */}
                <motion.div
                    className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[520px] h-36 mix-blend-screen"
                    style={{
                        background: "radial-gradient(ellipse, rgba(139,92,246,0.55) 0%, rgba(236,72,153,0.28) 42%, transparent 72%)",
                        filter: "blur(22px)",
                    }}
                    animate={{
                        opacity: [0.4, 0.7, 0.4],
                        scale: [1, 1.1, 1],
                    }}
                    transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                />

                {/* Right glow */}
                <motion.div
                    className="absolute right-0 top-0 bottom-0 w-1/3 mix-blend-screen"
                    style={{
                        background: "linear-gradient(270deg, rgba(236,72,153,0.2) 0%, rgba(139,92,246,0.07) 55%, transparent 100%)",
                    }}
                    animate={{
                        opacity: [0.4, 0.7, 0.4],
                    }}
                    transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", delay: 1 }}
                />

                {/* Shimmer effect across the bar */}
                <motion.div
                    className="absolute inset-0"
                    style={{
                        background: "linear-gradient(90deg, transparent 0%, rgba(139,92,246,0.12) 50%, transparent 100%)",
                        backgroundSize: "200% 100%",
                    }}
                    animate={{
                        backgroundPosition: ["-200% 0%", "200% 0%"],
                    }}
                    transition={{
                        duration: 8,
                        repeat: Infinity,
                        ease: "linear",
                    }}
                />

                {/* Bottom glow line */}
                <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-500/40 to-transparent" />
            </div>

            <div className="relative h-full px-2 sm:px-4 flex items-center justify-between">
                {/* Left side */}
                <div className="flex items-center gap-2 sm:gap-4 shrink-0 flex-1">
                    {/* Mobile menu button */}
                    {showMenuButton && (
                        <button
                            onClick={onMenuClick}
                            className={cn(
                                "lg:hidden p-2.5 rounded-xl",
                                "text-zinc-400",
                                "hover:bg-white/5",
                                "transition-colors",
                                "min-h-[44px] min-w-[44px] flex items-center justify-center" // Touch target
                            )}
                            aria-label="Open menu"
                        >
                            <Menu className="h-5 w-5" />
                        </button>
                    )}

                    {/* GinoNova Logo - Now part of TopBar, overflow visible for larger logo */}
                    <Link href="/dashboard" className="hidden lg:block shrink-0 overflow-visible">
                        <motion.div
                            className="relative overflow-visible"
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            {/* Logo glow - Subtle */}
                            <motion.div
                                className="absolute -inset-6 rounded-2xl"
                                style={{
                                    background: "radial-gradient(circle, rgba(139,92,246,0.4), rgba(236,72,153,0.2), transparent)",
                                    filter: "blur(20px)",
                                }}
                                animate={{
                                    opacity: [0.3, 0.5, 0.3],
                                    scale: [1, 1.1, 1],
                                }}
                                transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                            />
                            <motion.div
                                animate={{
                                    filter: [
                                        "drop-shadow(0 0 8px rgba(139,92,246,0.4))",
                                        "drop-shadow(0 0 16px rgba(139,92,246,0.6))",
                                        "drop-shadow(0 0 8px rgba(139,92,246,0.4))"
                                    ]
                                }}
                                transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
                            >
                                <Image
                                    src="/ginonova-logo-horizontal.svg"
                                    alt="GinoNova"
                                    width={400}
                                    height={100}
                                    className="h-20 w-auto"
                                    priority
                                />
                            </motion.div>
                        </motion.div>
                    </Link>

                    {/* Tattooed Quote - Left side, after logo (tablet+) */}
                    <motion.div
                        className="hidden sm:block relative select-none -ml-2"
                        animate={{
                            scale: [1, 1.02, 1],
                        }}
                        transition={{
                            duration: 3,
                            repeat: Infinity,
                            ease: "easeInOut"
                        }}
                    >
                        {/* Glow layers */}
                        <div className="absolute inset-0 blur-xl bg-gradient-to-r from-purple-500/40 via-pink-500/30 to-cyan-500/40 rounded-full" />
                        <div className="absolute inset-0 blur-md bg-gradient-to-r from-purple-400/20 via-pink-400/20 to-cyan-400/20 rounded-full" />

                        {/* Main text */}
                        <motion.p
                            className="relative text-base md:text-lg xl:text-xl font-medium italic tracking-wide whitespace-nowrap"
                            style={{
                                fontFamily: "'Georgia', 'Times New Roman', serif",
                                background: "linear-gradient(135deg, #c084fc 0%, #f472b6 35%, #22d3ee 70%, #c084fc 100%)",
                                backgroundSize: "200% 200%",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                backgroundClip: "text",
                                textShadow: "0 0 40px rgba(192,132,252,0.5), 0 0 80px rgba(244,114,182,0.3)",
                                filter: "drop-shadow(0 0 12px rgba(192,132,252,0.4))",
                            }}
                            animate={{
                                backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"],
                            }}
                            transition={{
                                duration: 5,
                                repeat: Infinity,
                                ease: "linear"
                            }}
                        >
                            Skapad med <span className="not-italic">❤️</span> för DevOps ingenjörer
                        </motion.p>
                    </motion.div>
                </div>

                {/* Center - Quote on mobile, Spotify + more on larger screens */}
                <div className="sm:hidden flex-1 flex items-center justify-center">
                    <motion.div
                        className="relative select-none"
                        animate={{ scale: [1, 1.02, 1] }}
                        transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                    >
                        <div className="absolute inset-0 blur-lg bg-gradient-to-r from-purple-500/30 via-pink-500/20 to-cyan-500/30 rounded-full" />
                        <motion.p
                            className="relative text-sm font-medium italic tracking-wide whitespace-nowrap"
                            style={{
                                fontFamily: "'Georgia', 'Times New Roman', serif",
                                background: "linear-gradient(135deg, #c084fc 0%, #f472b6 35%, #22d3ee 70%, #c084fc 100%)",
                                backgroundSize: "200% 200%",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                backgroundClip: "text",
                            }}
                            animate={{ backgroundPosition: ["0% 50%", "100% 50%", "0% 50%"] }}
                            transition={{ duration: 5, repeat: Infinity, ease: "linear" }}
                        >
                            <span className="not-italic">❤️</span> DevOps
                        </motion.p>
                    </motion.div>
                </div>

                {/* Center - Spotify Widget + Broadcasts + Admin Flash (tablet+) */}
                <div className="hidden sm:flex items-center justify-center gap-4 flex-1">
                    {isAuthenticated && <SpotifyTopBarWidget />}
                    {/* Broadcast in center - with margin to separate from Spotify */}
                    {isAuthenticated && <div className="mx-2"><UserBroadcast /></div>}
                    {isAuthenticated && <AdminActivityFlash />}
                </div>

                {/* Right side */}
                <div className="flex items-center gap-2 sm:gap-3 shrink-0 justify-end">
                    {/* Broadcast messages - Mobile */}
                    {isAuthenticated && <div className="sm:hidden"><UserBroadcast /></div>}
                    {/* Admin Activity Flash - Mobile (between items) */}
                    {isAuthenticated && <div className="sm:hidden"><AdminActivityFlash /></div>}
                    {/* Session Timer - Only show on larger screens */}
                    {isAuthenticated && <div className="hidden md:block"><SessionTimerDisplay /></div>}

                    {/* Admin Inbox - Shows unread user messages (admin only) */}
                    {isAuthenticated && <AdminInboxWidget />}

                    {/* Admin Status Widget - For non-admin users to see if admin is online */}
                    {isAuthenticated && <AdminStatusWidget />}

                    {/* User dropdown */}
                    {isAuthenticated && <UserDropdown />}
                </div>
            </div>
        </header>
    )
}

export default TopBar
export { SearchBar }
