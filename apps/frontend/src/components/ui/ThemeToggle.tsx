"use client"

/**
 * Theme Toggle Component
 * Comprehensive theme switcher with light/dark/system modes
 */

import { useEffect, useState } from "react"
import { useTheme } from "next-themes"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Sun, Moon, Monitor } from "lucide-react"
import { Button } from "@/components/ui/button"

export interface ThemeToggleProps {
    variant?: "button" | "menu"
    className?: string
}

export function ThemeToggle({ variant = "button", className }: ThemeToggleProps) {
    const { theme, setTheme, systemTheme } = useTheme()
    const [mounted, setMounted] = useState(false)

    // Prevent hydration mismatch
    useEffect(() => {
        setMounted(true)
    }, [])

    if (!mounted) {
        return <div className={cn("w-10 h-10 rounded-xl bg-zinc-800/50 animate-pulse", className)} />
    }

    const currentTheme = theme === "system" ? systemTheme : theme

    if (variant === "button") {
        return (
            <Button
                variant="ghost"
                size="sm"
                onClick={() => {
                    // Cycle through: dark → light → system → dark
                    if (theme === "dark") {
                        setTheme("light")
                    } else if (theme === "light") {
                        setTheme("system")
                    } else {
                        setTheme("dark")
                    }
                }}
                className={cn(
                    "relative rounded-xl h-10 w-10 p-0",
                    "bg-zinc-800/50 border border-zinc-700/50",
                    "hover:bg-zinc-700/50 hover:border-zinc-600",
                    "transition-all duration-200",
                    className
                )}
                aria-label="Toggle theme"
            >
                <AnimatePresence mode="wait" initial={false}>
                    {theme === "dark" && (
                        <motion.div
                            key="dark"
                            initial={{ scale: 0, rotate: -180 }}
                            animate={{ scale: 1, rotate: 0 }}
                            exit={{ scale: 0, rotate: 180 }}
                            transition={{ duration: 0.2 }}
                            className="absolute inset-0 flex items-center justify-center"
                        >
                            <Moon className="w-4 h-4 text-indigo-400" />
                        </motion.div>
                    )}
                    {theme === "light" && (
                        <motion.div
                            key="light"
                            initial={{ scale: 0, rotate: -180 }}
                            animate={{ scale: 1, rotate: 0 }}
                            exit={{ scale: 0, rotate: 180 }}
                            transition={{ duration: 0.2 }}
                            className="absolute inset-0 flex items-center justify-center"
                        >
                            <Sun className="w-4 h-4 text-amber-500" />
                        </motion.div>
                    )}
                    {theme === "system" && (
                        <motion.div
                            key="system"
                            initial={{ scale: 0, rotate: -180 }}
                            animate={{ scale: 1, rotate: 0 }}
                            exit={{ scale: 0, rotate: 180 }}
                            transition={{ duration: 0.2 }}
                            className="absolute inset-0 flex items-center justify-center"
                        >
                            <Monitor className="w-4 h-4 text-cyan-400" />
                        </motion.div>
                    )}
                </AnimatePresence>
            </Button>
        )
    }

    // Menu variant for dropdown menus
    return (
        <div className={cn("p-2 space-y-1", className)}>
            <div className="text-xs font-semibold text-zinc-400 px-2 mb-2">
                Theme
            </div>
            {[
                { value: "light", label: "Light", icon: Sun, color: "text-amber-500" },
                { value: "dark", label: "Dark", icon: Moon, color: "text-indigo-400" },
                { value: "system", label: "System", icon: Monitor, color: "text-cyan-400" },
            ].map((option) => {
                const isActive = theme === option.value
                const Icon = option.icon

                return (
                    <button
                        key={option.value}
                        onClick={() => setTheme(option.value)}
                        className={cn(
                            "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg",
                            "text-sm font-medium transition-all duration-200",
                            isActive
                                ? "bg-zinc-800/80 text-white border border-zinc-700"
                                : "text-zinc-400 hover:text-white hover:bg-zinc-800/50"
                        )}
                    >
                        <Icon className={cn("w-4 h-4", isActive ? option.color : "")} />
                        <span className="flex-1 text-left">{option.label}</span>
                        {isActive && (
                            <motion.div
                                layoutId="theme-indicator"
                                className="w-2 h-2 rounded-full bg-purple-500"
                                transition={{ type: "spring", stiffness: 300, damping: 30 }}
                            />
                        )}
                    </button>
                )
            })}
        </div>
    )
}

// Compact inline toggle (for minimal UIs)
export function ThemeToggleCompact() {
    const { theme, setTheme } = useTheme()
    const [mounted, setMounted] = useState(false)

    useEffect(() => {
        setMounted(true)
    }, [])

    if (!mounted) {
        return <div className="w-8 h-8 rounded-full bg-zinc-800/50 animate-pulse" />
    }

    return (
        <div className="flex items-center gap-1 p-1 bg-zinc-900/50 rounded-full border border-zinc-700/50">
            <button
                onClick={() => setTheme("light")}
                className={cn(
                    "p-1.5 rounded-full transition-all duration-200",
                    theme === "light"
                        ? "bg-amber-500 text-white"
                        : "text-zinc-500 hover:text-zinc-300"
                )}
                aria-label="Light mode"
            >
                <Sun className="w-3.5 h-3.5" />
            </button>
            <button
                onClick={() => setTheme("dark")}
                className={cn(
                    "p-1.5 rounded-full transition-all duration-200",
                    theme === "dark"
                        ? "bg-indigo-500 text-white"
                        : "text-zinc-500 hover:text-zinc-300"
                )}
                aria-label="Dark mode"
            >
                <Moon className="w-3.5 h-3.5" />
            </button>
            <button
                onClick={() => setTheme("system")}
                className={cn(
                    "p-1.5 rounded-full transition-all duration-200",
                    theme === "system"
                        ? "bg-cyan-500 text-white"
                        : "text-zinc-500 hover:text-zinc-300"
                )}
                aria-label="System theme"
            >
                <Monitor className="w-3.5 h-3.5" />
            </button>
        </div>
    )
}
