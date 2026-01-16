"use client"

/**
 * Module Filters Component
 * Comprehensive filtering and sorting for module discovery
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Filter,
    SortAsc,
    X,
    Check,
    ChevronDown,
    Search,
    Sparkles,
} from "lucide-react"
import { Button } from "@/components/ui/button"

// ============================================================================
// TYPES
// ============================================================================

export type DifficultyFilter = "all" | "beginner" | "intermediate" | "advanced" | "expert"
export type StatusFilter = "all" | "not-started" | "in-progress" | "completed"
export type SortOption = "name" | "difficulty" | "progress" | "estimated_hours"
export type SortDirection = "asc" | "desc"

export interface FilterState {
    difficulty: DifficultyFilter
    status: StatusFilter
    searchQuery: string
    tags: string[]
}

export interface SortState {
    sortBy: SortOption
    sortDirection: SortDirection
}

interface ModuleFiltersProps {
    filters: FilterState
    sort: SortState
    onFilterChange: (filters: FilterState) => void
    onSortChange: (sort: SortState) => void
    availableTags?: string[]
    totalCount: number
    filteredCount: number
}

// ============================================================================
// DIFFICULTY COLORS
// ============================================================================

const difficultyColors = {
    all: "text-zinc-400 bg-zinc-800/50 border-zinc-700",
    beginner: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
    intermediate: "text-amber-400 bg-amber-500/10 border-amber-500/30",
    advanced: "text-red-400 bg-red-500/10 border-red-500/30",
    expert: "text-purple-400 bg-purple-500/10 border-purple-500/30",
}

const statusColors = {
    all: "text-zinc-400 bg-zinc-800/50 border-zinc-700",
    "not-started": "text-zinc-400 bg-zinc-800/50 border-zinc-700",
    "in-progress": "text-cyan-400 bg-cyan-500/10 border-cyan-500/30",
    completed: "text-emerald-400 bg-emerald-500/10 border-emerald-500/30",
}

// ============================================================================
// MAIN COMPONENT
// ============================================================================

export function ModuleFilters({
    filters,
    sort,
    onFilterChange,
    onSortChange,
    availableTags = [],
    totalCount,
    filteredCount,
}: ModuleFiltersProps) {
    const [isExpanded, setIsExpanded] = useState(false)
    const [showSortMenu, setShowSortMenu] = useState(false)

    const activeFiltersCount =
        (filters.difficulty !== "all" ? 1 : 0) +
        (filters.status !== "all" ? 1 : 0) +
        (filters.tags.length > 0 ? filters.tags.length : 0) +
        (filters.searchQuery ? 1 : 0)

    const hasActiveFilters = activeFiltersCount > 0

    // Clear all filters
    const handleClearFilters = () => {
        onFilterChange({
            difficulty: "all",
            status: "all",
            searchQuery: "",
            tags: [],
        })
    }

    // Toggle difficulty filter
    const handleDifficultyClick = (difficulty: DifficultyFilter) => {
        onFilterChange({
            ...filters,
            difficulty: filters.difficulty === difficulty ? "all" : difficulty,
        })
    }

    // Toggle status filter
    const handleStatusClick = (status: StatusFilter) => {
        onFilterChange({
            ...filters,
            status: filters.status === status ? "all" : status,
        })
    }

    // Toggle tag filter
    const handleTagClick = (tag: string) => {
        const newTags = filters.tags.includes(tag)
            ? filters.tags.filter((t) => t !== tag)
            : [...filters.tags, tag]
        onFilterChange({
            ...filters,
            tags: newTags,
        })
    }

    // Handle sort change
    const handleSortChange = (sortBy: SortOption) => {
        const newDirection =
            sort.sortBy === sortBy && sort.sortDirection === "asc" ? "desc" : "asc"
        onSortChange({ sortBy, sortDirection: newDirection })
        setShowSortMenu(false)
    }

    // Search input handler
    const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        onFilterChange({
            ...filters,
            searchQuery: e.target.value,
        })
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "mb-8 rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-zinc-900/90 via-zinc-900/95 to-zinc-950/90",
                "border border-white/[0.08]",
                "backdrop-blur-sm"
            )}
        >
            {/* Compact Header - Always Visible */}
            <div className="p-4">
                <div className="flex items-center gap-3 flex-wrap">
                    {/* Search Bar */}
                    <div className="flex-1 min-w-[240px] relative">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" aria-hidden="true" />
                        <input
                            type="text"
                            placeholder="Search modules..."
                            value={filters.searchQuery}
                            onChange={handleSearchChange}
                            aria-label="Search modules by name"
                            role="searchbox"
                            className={cn(
                                "w-full h-10 pl-10 pr-4 rounded-xl",
                                "bg-zinc-800/50 border border-zinc-700/50",
                                "text-sm text-white placeholder:text-zinc-500",
                                "focus:outline-none focus:ring-2 focus:ring-purple-500/50 focus:border-purple-500/50",
                                "transition-all duration-200"
                            )}
                        />
                    </div>

                    {/* Filter Toggle Button */}
                    <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => setIsExpanded(!isExpanded)}
                        aria-expanded={isExpanded}
                        aria-controls="module-filters-panel"
                        aria-label={`${isExpanded ? "Hide" : "Show"} filters${hasActiveFilters ? ` (${activeFiltersCount} active)` : ""}`}
                        className={cn(
                            "rounded-xl h-10 px-4 gap-2",
                            "border border-zinc-700/50",
                            hasActiveFilters
                                ? "bg-purple-500/10 border-purple-500/30 text-purple-400"
                                : "bg-zinc-800/50 text-zinc-400 hover:text-white"
                        )}
                    >
                        <Filter className="w-4 h-4" aria-hidden="true" />
                        <span className="font-medium">Filters</span>
                        {hasActiveFilters && (
                            <span className="px-1.5 py-0.5 rounded-full bg-purple-500 text-white text-xs font-bold" aria-label={`${activeFiltersCount} filters active`}>
                                {activeFiltersCount}
                            </span>
                        )}
                        <ChevronDown
                            className={cn(
                                "w-4 h-4 transition-transform duration-200",
                                isExpanded && "rotate-180"
                            )}
                            aria-hidden="true"
                        />
                    </Button>

                    {/* Sort Dropdown */}
                    <div className="relative">
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={() => setShowSortMenu(!showSortMenu)}
                            aria-haspopup="menu"
                            aria-expanded={showSortMenu}
                            aria-label={`Sort by ${sort.sortBy} (${sort.sortDirection})`}
                            className={cn(
                                "rounded-xl h-10 px-4 gap-2",
                                "bg-zinc-800/50 border border-zinc-700/50",
                                "text-zinc-400 hover:text-white"
                            )}
                        >
                            <SortAsc className="w-4 h-4" aria-hidden="true" />
                            <span className="font-medium">Sort</span>
                            <ChevronDown className="w-4 h-4" aria-hidden="true" />
                        </Button>

                        {/* Sort Menu */}
                        <AnimatePresence>
                            {showSortMenu && (
                                <motion.div
                                    initial={{ opacity: 0, y: -10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    exit={{ opacity: 0, y: -10 }}
                                    className={cn(
                                        "absolute right-0 top-full mt-2 z-50",
                                        "w-56 rounded-xl overflow-hidden",
                                        "bg-zinc-900 border border-zinc-700/50",
                                        "shadow-xl shadow-black/50"
                                    )}
                                >
                                    {[
                                        { value: "name", label: "Name" },
                                        { value: "difficulty", label: "Difficulty" },
                                        { value: "progress", label: "Progress" },
                                        { value: "estimated_hours", label: "Duration" },
                                    ].map((option) => (
                                        <button
                                            key={option.value}
                                            onClick={() => handleSortChange(option.value as SortOption)}
                                            className={cn(
                                                "w-full px-4 py-3 text-left text-sm",
                                                "flex items-center justify-between",
                                                "hover:bg-zinc-800 transition-colors",
                                                sort.sortBy === option.value
                                                    ? "text-purple-400 bg-purple-500/5"
                                                    : "text-zinc-300"
                                            )}
                                        >
                                            <span>{option.label}</span>
                                            {sort.sortBy === option.value && (
                                                <Check className="w-4 h-4" />
                                            )}
                                        </button>
                                    ))}
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </div>

                    {/* Results Count */}
                    <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-800/30 border border-zinc-700/30">
                        <Sparkles className="w-4 h-4 text-purple-400" />
                        <span className="text-sm font-medium text-zinc-300">
                            <span className="text-purple-400 font-bold">{filteredCount}</span> / {totalCount}
                        </span>
                    </div>

                    {/* Clear Filters */}
                    {hasActiveFilters && (
                        <Button
                            variant="ghost"
                            size="sm"
                            onClick={handleClearFilters}
                            className="rounded-xl h-10 px-3 text-zinc-400 hover:text-white"
                        >
                            <X className="w-4 h-4" />
                        </Button>
                    )}
                </div>
            </div>

            {/* Expanded Filters Panel */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.2 }}
                        className="border-t border-zinc-700/50"
                    >
                        <div className="p-6 space-y-6">
                            {/* Difficulty Filter */}
                            <div>
                                <label className="block text-sm font-semibold text-zinc-300 mb-3">
                                    Difficulty
                                </label>
                                <div className="flex flex-wrap gap-2">
                                    {(["all", "beginner", "intermediate", "advanced", "expert"] as const).map(
                                        (diff) => (
                                            <button
                                                key={diff}
                                                onClick={() => handleDifficultyClick(diff)}
                                                className={cn(
                                                    "px-4 py-2 rounded-xl text-sm font-medium",
                                                    "border transition-all duration-200",
                                                    filters.difficulty === diff
                                                        ? difficultyColors[diff]
                                                        : "text-zinc-500 bg-zinc-800/30 border-zinc-700/30 hover:bg-zinc-800/50"
                                                )}
                                            >
                                                {diff === "all" ? "All Levels" : diff.charAt(0).toUpperCase() + diff.slice(1)}
                                            </button>
                                        )
                                    )}
                                </div>
                            </div>

                            {/* Status Filter */}
                            <div>
                                <label className="block text-sm font-semibold text-zinc-300 mb-3">
                                    Progress Status
                                </label>
                                <div className="flex flex-wrap gap-2">
                                    {(["all", "not-started", "in-progress", "completed"] as const).map(
                                        (status) => (
                                            <button
                                                key={status}
                                                onClick={() => handleStatusClick(status)}
                                                className={cn(
                                                    "px-4 py-2 rounded-xl text-sm font-medium",
                                                    "border transition-all duration-200",
                                                    filters.status === status
                                                        ? statusColors[status]
                                                        : "text-zinc-500 bg-zinc-800/30 border-zinc-700/30 hover:bg-zinc-800/50"
                                                )}
                                            >
                                                {status === "all"
                                                    ? "All Status"
                                                    : status.split("-").map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")}
                                            </button>
                                        )
                                    )}
                                </div>
                            </div>

                            {/* Tags Filter (if available) */}
                            {availableTags.length > 0 && (
                                <div>
                                    <label className="block text-sm font-semibold text-zinc-300 mb-3">
                                        Topics
                                    </label>
                                    <div className="flex flex-wrap gap-2">
                                        {availableTags.map((tag) => {
                                            const isActive = filters.tags.includes(tag)
                                            return (
                                                <button
                                                    key={tag}
                                                    onClick={() => handleTagClick(tag)}
                                                    className={cn(
                                                        "px-3 py-1.5 rounded-lg text-xs font-medium",
                                                        "border transition-all duration-200",
                                                        isActive
                                                            ? "text-purple-400 bg-purple-500/10 border-purple-500/30"
                                                            : "text-zinc-500 bg-zinc-800/30 border-zinc-700/30 hover:bg-zinc-800/50"
                                                    )}
                                                >
                                                    {tag}
                                                </button>
                                            )
                                        })}
                                    </div>
                                </div>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.div>
    )
}

// ============================================================================
// UTILITY FUNCTIONS FOR FILTERING/SORTING
// ============================================================================

export function applyFilters<T extends {
    name: string
    difficulty: string
    status?: string
    tags?: string[]
    progress?: number
}>(
    items: T[],
    filters: FilterState
): T[] {
    return items.filter((item) => {
        // Search query
        if (filters.searchQuery) {
            const query = filters.searchQuery.toLowerCase()
            if (!item.name.toLowerCase().includes(query)) {
                return false
            }
        }

        // Difficulty
        if (filters.difficulty !== "all") {
            if (item.difficulty !== filters.difficulty) {
                return false
            }
        }

        // Status
        if (filters.status !== "all") {
            if (!item.status) return false
            if (item.status !== filters.status) {
                return false
            }
        }

        // Tags
        if (filters.tags.length > 0) {
            if (!item.tags || item.tags.length === 0) return false
            const hasMatchingTag = filters.tags.some((tag) =>
                item.tags!.includes(tag)
            )
            if (!hasMatchingTag) {
                return false
            }
        }

        return true
    })
}

export function applySorting<T extends {
    name: string
    difficulty?: string
    progress?: number
    estimated_hours?: number
    estimatedHours?: number
}>(
    items: T[],
    sort: SortState
): T[] {
    const sorted = [...items].sort((a, b) => {
        let comparison = 0

        switch (sort.sortBy) {
            case "name":
                comparison = a.name.localeCompare(b.name)
                break
            case "difficulty": {
                const difficultyOrder = { beginner: 1, intermediate: 2, advanced: 3, expert: 4 }
                const aDiff = a.difficulty as keyof typeof difficultyOrder
                const bDiff = b.difficulty as keyof typeof difficultyOrder
                comparison = (difficultyOrder[aDiff] || 0) - (difficultyOrder[bDiff] || 0)
                break
            }
            case "progress":
                comparison = (a.progress || 0) - (b.progress || 0)
                break
            case "estimated_hours": {
                const aHours = a.estimated_hours || a.estimatedHours || 0
                const bHours = b.estimated_hours || b.estimatedHours || 0
                comparison = aHours - bHours
                break
            }
        }

        return sort.sortDirection === "asc" ? comparison : -comparison
    })

    return sorted
}
