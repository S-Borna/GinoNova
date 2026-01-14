"use client"

/**
 * ============================================================================
 * COMMUNITY FORUM PAGE — Discussion Hub
 * ============================================================================
 *
 * Main community forum with categories, threads, and search
 */

import { useState } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import Link from "next/link"
import {
    MessageSquare,
    Plus,
    Sparkles,
    Users,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { CATEGORIES, type Thread } from "@/lib/community-types"
import { ThreadList } from "@/components/community"

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_THREADS: Thread[] = [
    {
        id: "1",
        title: "How to optimize Docker image size for production?",
        content: "I'm working on a Node.js application...",
        authorId: "user1",
        author: {
            id: "user1",
            name: "Sarah Chen",
            avatar: "SC",
            reputation: 1250,
        },
        categoryId: "docker",
        category: CATEGORIES.find((c) => c.id === "docker")!,
        tags: ["docker", "optimization", "production"],
        views: 342,
        replyCount: 15,
        upvotes: 24,
        downvotes: 2,
        isPinned: true,
        isLocked: false,
        hasAcceptedAnswer: true,
        createdAt: new Date("2025-01-12T10:30:00"),
        updatedAt: new Date("2025-01-13T15:20:00"),
        lastActivityAt: new Date("2025-01-13T15:20:00"),
    },
    {
        id: "2",
        title: "Best practices for Kubernetes monitoring in 2025",
        content: "What are the current best practices...",
        authorId: "user2",
        author: {
            id: "user2",
            name: "Alex Rodriguez",
            avatar: "AR",
            reputation: 856,
        },
        categoryId: "kubernetes",
        category: CATEGORIES.find((c) => c.id === "kubernetes")!,
        tags: ["kubernetes", "monitoring", "prometheus"],
        views: 198,
        replyCount: 8,
        upvotes: 18,
        downvotes: 0,
        isPinned: false,
        isLocked: false,
        hasAcceptedAnswer: false,
        createdAt: new Date("2025-01-13T08:15:00"),
        updatedAt: new Date("2025-01-13T14:30:00"),
        lastActivityAt: new Date("2025-01-13T14:30:00"),
    },
    {
        id: "3",
        title: "Terraform state management - Remote vs Local",
        content: "I'm trying to understand the pros and cons...",
        authorId: "user3",
        author: {
            id: "user3",
            name: "Mike Johnson",
            avatar: "MJ",
            reputation: 423,
        },
        categoryId: "terraform",
        category: CATEGORIES.find((c) => c.id === "terraform")!,
        tags: ["terraform", "state", "best-practices"],
        views: 267,
        replyCount: 12,
        upvotes: 31,
        downvotes: 1,
        isPinned: false,
        isLocked: false,
        hasAcceptedAnswer: true,
        createdAt: new Date("2025-01-11T16:45:00"),
        updatedAt: new Date("2025-01-13T11:20:00"),
        lastActivityAt: new Date("2025-01-13T11:20:00"),
    },
    {
        id: "4",
        title: "Just passed my first DevOps interview! 🎉",
        content: "After 3 months of studying on DevOpsHub...",
        authorId: "user4",
        author: {
            id: "user4",
            name: "Emma Wilson",
            avatar: "EW",
            reputation: 145,
        },
        categoryId: "career",
        category: CATEGORIES.find((c) => c.id === "career")!,
        tags: ["career", "interview", "success"],
        views: 523,
        replyCount: 34,
        upvotes: 67,
        downvotes: 0,
        isPinned: false,
        isLocked: false,
        hasAcceptedAnswer: false,
        createdAt: new Date("2025-01-13T09:00:00"),
        updatedAt: new Date("2025-01-13T16:10:00"),
        lastActivityAt: new Date("2025-01-13T16:10:00"),
    },
    {
        id: "5",
        title: "CI/CD pipeline failing on AWS CodePipeline - Need help!",
        content: "My pipeline keeps failing at the build stage...",
        authorId: "user5",
        author: {
            id: "user5",
            name: "David Kim",
            avatar: "DK",
            reputation: 287,
        },
        categoryId: "help",
        category: CATEGORIES.find((c) => c.id === "help")!,
        tags: ["aws", "cicd", "troubleshooting"],
        views: 156,
        replyCount: 6,
        upvotes: 12,
        downvotes: 0,
        isPinned: false,
        isLocked: false,
        hasAcceptedAnswer: false,
        createdAt: new Date("2025-01-13T13:30:00"),
        updatedAt: new Date("2025-01-13T15:45:00"),
        lastActivityAt: new Date("2025-01-13T15:45:00"),
    },
]

/* ============================================================================
   COMPONENTS
   ============================================================================ */

function CategoryCard({ category }: { category: typeof CATEGORIES[0] }) {
    return (
        <Link href={`/community?category=${category.slug}`} prefetch={false}>
            <motion.div
                whileHover={{ scale: 1.02, y: -2 }}
                className={cn(
                    "group p-5 rounded-2xl cursor-pointer",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border border-zinc-800/80",
                    "hover:border-purple-500/30",
                    "transition-all duration-300"
                )}
                style={{
                    boxShadow: "0 0 30px rgba(0, 0, 0, 0.5)",
                }}
            >
                <div className="flex items-start gap-4">
                    <motion.div
                        className={cn(
                            "w-12 h-12 rounded-xl shrink-0",
                            "bg-gradient-to-br",
                            category.gradient,
                            "flex items-center justify-center text-2xl",
                            "group-hover:scale-110 transition-transform duration-300"
                        )}
                    >
                        {category.icon}
                    </motion.div>
                    <div className="flex-1 min-w-0">
                        <h3
                            className={cn(
                                "text-lg font-semibold mb-1",
                                "group-hover:text-purple-400 transition-colors"
                            )}
                        >
                            {category.name}
                        </h3>
                        <p className="text-sm text-zinc-500 mb-3">
                            {category.description}
                        </p>
                        <div className="flex items-center gap-4 text-xs text-zinc-600">
                            <span className="flex items-center gap-1">
                                <MessageSquare className="w-3 h-3" />
                                {category.threadCount} threads
                            </span>
                            <span className="flex items-center gap-1">
                                <MessageSquare className="w-3 h-3" />
                                {category.postCount} posts
                            </span>
                        </div>
                    </div>
                </div>
            </motion.div>
        </Link>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function CommunityPage() {

    return (
        <div className="min-h-screen">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "relative overflow-hidden rounded-3xl mb-8",
                    "bg-gradient-to-br from-[#0a0a0f] via-purple-950/20 to-[#0a0a0f]",
                    "border border-purple-500/20",
                    "p-8",
                    "shadow-[0_0_80px_rgba(139,92,246,0.15)]"
                )}
            >
                <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px]" />
                <div className="absolute bottom-0 left-0 w-80 h-80 bg-cyan-500/8 rounded-full blur-[80px]" />

                <div className="relative flex flex-col md:flex-row md:items-center md:justify-between gap-6">
                    <div>
                        <div className="flex items-center gap-3 mb-3">
                            <motion.div
                                className="p-2.5 rounded-xl bg-gradient-to-br from-purple-500/30 to-purple-600/20 border border-purple-500/40"
                                animate={{
                                    boxShadow: [
                                        "0 0 20px rgba(139, 92, 246, 0.3)",
                                        "0 0 40px rgba(139, 92, 246, 0.5)",
                                        "0 0 20px rgba(139, 92, 246, 0.3)",
                                    ],
                                }}
                                transition={{
                                    duration: 2,
                                    repeat: Infinity,
                                    ease: "easeInOut",
                                }}
                            >
                                <Users className="w-5 h-5 text-purple-400" />
                            </motion.div>
                            <span className="text-purple-400 font-semibold text-sm uppercase tracking-wider">
                                Community Forum
                            </span>
                        </div>
                        <h1 className="text-4xl font-black mb-3 bg-gradient-to-r from-white via-purple-200 to-cyan-200 bg-clip-text text-transparent">
                            DevOps Discussion Hub
                        </h1>
                        <p className="text-zinc-400 text-lg max-w-2xl">
                            Connect with fellow DevOps engineers, share knowledge, and
                            grow together
                        </p>
                    </div>

                    <Link href="/community/new" prefetch={false}>
                        <Button
                            className={cn(
                                "rounded-xl px-6 py-6 h-auto",
                                "bg-gradient-to-r from-purple-600 to-purple-500",
                                "hover:from-purple-500 hover:to-purple-400",
                                "shadow-[0_0_30px_rgba(139,92,246,0.3)]",
                                "text-base font-semibold"
                            )}
                        >
                            <Plus className="w-5 h-5 mr-2" />
                            New Thread
                        </Button>
                    </Link>
                </div>
            </motion.div>

            {/* Categories */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="mb-8"
            >
                <h2 className="text-2xl font-bold text-white mb-4 flex items-center gap-2">
                    <Sparkles className="w-5 h-5 text-purple-400" />
                    Categories
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {CATEGORIES.map((category) => (
                        <CategoryCard key={category.id} category={category} />
                    ))}
                </div>
            </motion.div>

            {/* Threads List */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
            >
                <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-2">
                    <MessageSquare className="w-5 h-5 text-purple-400" />
                    Recent Discussions
                </h2>
                <ThreadList threads={MOCK_THREADS} showFilters={true} />
            </motion.div>
        </div>
    )
}
