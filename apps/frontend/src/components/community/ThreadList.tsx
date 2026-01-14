"use client"

/**
 * ============================================================================
 * THREAD LIST — Discussion Thread Listing
 * ============================================================================
 *
 * Card-based layout with filtering, sorting, and search
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { type Thread, type Category, CATEGORIES } from "@/lib/community-types"
import { getReputationLevel } from "@/lib/reputation"
import Link from "next/link"
import {
    Search,
    Filter,
    Clock,
    TrendingUp,
    MessageCircle,
    Eye,
    ThumbsUp,
    Pin,
    CheckCircle,
    Sparkles,
    X,
} from "lucide-react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

interface ThreadListProps {
    threads: Thread[]
    defaultSort?: "latest" | "popular" | "trending"
    defaultCategory?: string | null
    showFilters?: boolean
    className?: string
}

export function ThreadList({
    threads,
    defaultSort = "latest",
    defaultCategory = null,
    showFilters = true,
    className,
}: ThreadListProps) {
    const [searchQuery, setSearchQuery] = useState("")
    const [sortBy, setSortBy] = useState<"latest" | "popular" | "trending">(
        defaultSort
    )
    const [selectedCategory, setSelectedCategory] = useState<string | null>(
        defaultCategory
    )
    const [showCategoryFilter, setShowCategoryFilter] = useState(false)

    // Filter threads
    const filteredThreads = threads.filter((thread) => {
        if (selectedCategory && thread.categoryId !== selectedCategory) {
            return false
        }
        if (searchQuery) {
            const query = searchQuery.toLowerCase()
            return (
                thread.title.toLowerCase().includes(query) ||
                thread.content.toLowerCase().includes(query) ||
                thread.tags.some((tag) => tag.toLowerCase().includes(query)) ||
                thread.author.name.toLowerCase().includes(query)
            )
        }
        return true
    })

    // Sort threads
    const sortedThreads = [...filteredThreads].sort((a, b) => {
        // Always pin threads first
        if (a.isPinned !== b.isPinned) return a.isPinned ? -1 : 1

        switch (sortBy) {
            case "popular":
                return b.upvotes - a.upvotes
            case "trending":
                // Trending considers upvotes and recent activity
                const aScore = b.upvotes * 0.7 + b.views * 0.3
                const bScore = a.upvotes * 0.7 + a.views * 0.3
                return bScore - aScore
            case "latest":
            default:
                return (
                    b.lastActivityAt.getTime() - a.lastActivityAt.getTime()
                )
        }
    })

    const selectedCategoryData = selectedCategory
        ? CATEGORIES.find((c) => c.id === selectedCategory)
        : null

    return (
        <div className={cn("space-y-6", className)}>
            {/* Search and Filters */}
            {showFilters && (
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="space-y-4"
                >
                    {/* Search Bar */}
                    <div className="relative">
                        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                        <Input
                            placeholder="Search discussions, tags, or users..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className={cn(
                                "pl-12 pr-4 h-12 rounded-xl",
                                "bg-[#0a0a0f] border-zinc-800",
                                "focus:border-purple-500 transition-colors"
                            )}
                        />
                        {searchQuery && (
                            <button
                                onClick={() => setSearchQuery("")}
                                className="absolute right-4 top-1/2 -translate-y-1/2 text-zinc-500 hover:text-white"
                            >
                                <X className="w-4 h-4" />
                            </button>
                        )}
                    </div>

                    {/* Sort and Filter Buttons */}
                    <div className="flex flex-wrap gap-2">
                        <Button
                            variant={sortBy === "latest" ? "default" : "outline"}
                            onClick={() => setSortBy("latest")}
                            className={cn(
                                "rounded-xl",
                                sortBy === "latest" &&
                                    "bg-purple-600 hover:bg-purple-500"
                            )}
                        >
                            <Clock className="w-4 h-4 mr-2" />
                            Latest
                        </Button>
                        <Button
                            variant={sortBy === "popular" ? "default" : "outline"}
                            onClick={() => setSortBy("popular")}
                            className={cn(
                                "rounded-xl",
                                sortBy === "popular" &&
                                    "bg-purple-600 hover:bg-purple-500"
                            )}
                        >
                            <ThumbsUp className="w-4 h-4 mr-2" />
                            Popular
                        </Button>
                        <Button
                            variant={sortBy === "trending" ? "default" : "outline"}
                            onClick={() => setSortBy("trending")}
                            className={cn(
                                "rounded-xl",
                                sortBy === "trending" &&
                                    "bg-purple-600 hover:bg-purple-500"
                            )}
                        >
                            <TrendingUp className="w-4 h-4 mr-2" />
                            Trending
                        </Button>

                        <div className="relative">
                            <Button
                                variant={selectedCategory ? "default" : "outline"}
                                onClick={() =>
                                    setShowCategoryFilter(!showCategoryFilter)
                                }
                                className={cn(
                                    "rounded-xl",
                                    selectedCategory &&
                                        "bg-purple-600 hover:bg-purple-500"
                                )}
                            >
                                <Filter className="w-4 h-4 mr-2" />
                                {selectedCategoryData
                                    ? `${selectedCategoryData.icon} ${selectedCategoryData.name}`
                                    : "All Categories"}
                            </Button>

                            {/* Category Dropdown */}
                            <AnimatePresence>
                                {showCategoryFilter && (
                                    <motion.div
                                        initial={{ opacity: 0, y: -10, scale: 0.95 }}
                                        animate={{ opacity: 1, y: 0, scale: 1 }}
                                        exit={{ opacity: 0, y: -10, scale: 0.95 }}
                                        className={cn(
                                            "absolute top-full mt-2 left-0 z-50",
                                            "w-72 p-2 rounded-xl",
                                            "bg-zinc-900 border border-zinc-800",
                                            "shadow-2xl max-h-96 overflow-y-auto"
                                        )}
                                    >
                                        <button
                                            onClick={() => {
                                                setSelectedCategory(null)
                                                setShowCategoryFilter(false)
                                            }}
                                            className={cn(
                                                "w-full p-3 rounded-lg text-left",
                                                "hover:bg-zinc-800 transition-colors",
                                                !selectedCategory && "bg-zinc-800"
                                            )}
                                        >
                                            <div className="font-medium text-white">
                                                All Categories
                                            </div>
                                            <div className="text-xs text-zinc-500">
                                                View all discussions
                                            </div>
                                        </button>
                                        {CATEGORIES.map((category) => (
                                            <button
                                                key={category.id}
                                                onClick={() => {
                                                    setSelectedCategory(category.id)
                                                    setShowCategoryFilter(false)
                                                }}
                                                className={cn(
                                                    "w-full p-3 rounded-lg text-left",
                                                    "hover:bg-zinc-800 transition-colors",
                                                    selectedCategory === category.id &&
                                                        "bg-zinc-800"
                                                )}
                                            >
                                                <div className="flex items-center gap-2 mb-1">
                                                    <span className="text-lg">
                                                        {category.icon}
                                                    </span>
                                                    <span className="font-medium text-white">
                                                        {category.name}
                                                    </span>
                                                </div>
                                                <div className="text-xs text-zinc-500 flex items-center gap-3">
                                                    <span>
                                                        {category.threadCount} threads
                                                    </span>
                                                    <span>•</span>
                                                    <span>
                                                        {category.postCount} posts
                                                    </span>
                                                </div>
                                            </button>
                                        ))}
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </div>

                        {selectedCategory && (
                            <Button
                                variant="ghost"
                                onClick={() => setSelectedCategory(null)}
                                className="rounded-xl text-zinc-400 hover:text-white"
                            >
                                <X className="w-4 h-4 mr-2" />
                                Clear Filter
                            </Button>
                        )}
                    </div>
                </motion.div>
            )}

            {/* Thread List */}
            <div className="space-y-4">
                <AnimatePresence mode="popLayout">
                    {sortedThreads.map((thread, index) => (
                        <motion.div
                            key={thread.id}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.95 }}
                            transition={{ delay: index * 0.05 }}
                        >
                            <ThreadCard thread={thread} />
                        </motion.div>
                    ))}
                </AnimatePresence>

                {/* Empty State */}
                {sortedThreads.length === 0 && (
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className={cn(
                            "p-12 rounded-2xl text-center",
                            "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                            "border border-zinc-800/80"
                        )}
                    >
                        <Sparkles className="w-12 h-12 text-zinc-600 mx-auto mb-4" />
                        <h3 className="text-xl font-bold text-white mb-2">
                            No threads found
                        </h3>
                        <p className="text-zinc-500 mb-6">
                            {searchQuery
                                ? "Try adjusting your search or filters"
                                : "Be the first to start a discussion!"}
                        </p>
                        {searchQuery && (
                            <Button
                                onClick={() => {
                                    setSearchQuery("")
                                    setSelectedCategory(null)
                                }}
                                className="rounded-xl bg-purple-600 hover:bg-purple-500"
                            >
                                Clear Search
                            </Button>
                        )}
                    </motion.div>
                )}
            </div>

            {/* Results Count */}
            {sortedThreads.length > 0 && (
                <p className="text-sm text-zinc-500 text-center">
                    Showing {sortedThreads.length} of {threads.length} discussions
                </p>
            )}
        </div>
    )
}

function ThreadCard({ thread }: { thread: Thread }) {
    const repLevel = getReputationLevel(thread.author.reputation)
    const timeAgo = formatTimeAgo(thread.lastActivityAt)

    return (
        <Link href={`/community/${thread.id}`} prefetch={false}>
            <motion.div
                whileHover={{ scale: 1.01, y: -2 }}
                className={cn(
                    "group p-5 rounded-2xl cursor-pointer",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border border-zinc-800/80",
                    "hover:border-purple-500/30",
                    "transition-all duration-300",
                    thread.isPinned && "border-amber-500/40 bg-amber-500/5"
                )}
                style={{
                    boxShadow: "0 0 30px rgba(0, 0, 0, 0.5)",
                }}
            >
                <div className="flex gap-4">
                    {/* Author Avatar */}
                    <div className="shrink-0">
                        <div
                            className={cn(
                                "w-12 h-12 rounded-xl",
                                "bg-gradient-to-br",
                                repLevel.gradient,
                                "flex items-center justify-center",
                                "text-sm font-bold text-white"
                            )}
                        >
                            {thread.author.avatar}
                        </div>
                    </div>

                    {/* Thread Content */}
                    <div className="flex-1 min-w-0">
                        <div className="flex items-start gap-2 mb-2">
                            {thread.isPinned && (
                                <Pin className="w-4 h-4 text-amber-400 shrink-0 mt-1" />
                            )}
                            <h3
                                className={cn(
                                    "text-lg font-semibold",
                                    "group-hover:text-purple-400 transition-colors"
                                )}
                            >
                                {thread.title}
                            </h3>
                            {thread.hasAcceptedAnswer && (
                                <CheckCircle className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                            )}
                        </div>

                        <div className="flex items-center gap-2 mb-3 text-sm text-zinc-500">
                            <span className={repLevel.color}>
                                {thread.author.name}
                            </span>
                            <span>•</span>
                            <span
                                className={cn(
                                    "px-2 py-0.5 rounded-md text-xs",
                                    "bg-gradient-to-r",
                                    thread.category.gradient,
                                    "bg-opacity-20"
                                )}
                            >
                                {thread.category.icon} {thread.category.name}
                            </span>
                            <span>•</span>
                            <span>{timeAgo}</span>
                        </div>

                        {/* Tags */}
                        <div className="flex flex-wrap gap-2 mb-3">
                            {thread.tags.map((tag) => (
                                <span
                                    key={tag}
                                    className="px-2 py-1 rounded-lg bg-zinc-800/50 text-zinc-400 text-xs"
                                >
                                    #{tag}
                                </span>
                            ))}
                        </div>

                        {/* Stats */}
                        <div className="flex items-center gap-4 text-xs text-zinc-600">
                            <span className="flex items-center gap-1">
                                <Eye className="w-3 h-3" />
                                {thread.views}
                            </span>
                            <span className="flex items-center gap-1">
                                <MessageCircle className="w-3 h-3" />
                                {thread.replyCount} replies
                            </span>
                            <span className="flex items-center gap-1 text-emerald-400">
                                <ThumbsUp className="w-3 h-3" />
                                {thread.upvotes}
                            </span>
                        </div>
                    </div>
                </div>
            </motion.div>
        </Link>
    )
}

function formatTimeAgo(date: Date): string {
    const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000)
    if (seconds < 60) return "just now"
    const minutes = Math.floor(seconds / 60)
    if (minutes < 60) return `${minutes}m ago`
    const hours = Math.floor(minutes / 60)
    if (hours < 24) return `${hours}h ago`
    const days = Math.floor(hours / 24)
    if (days < 7) return `${days}d ago`
    const weeks = Math.floor(days / 7)
    if (weeks < 4) return `${weeks}w ago`
    const months = Math.floor(days / 30)
    return `${months}mo ago`
}
