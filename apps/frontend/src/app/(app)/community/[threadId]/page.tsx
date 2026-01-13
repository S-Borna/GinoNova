"use client"

/**
 * ============================================================================
 * THREAD VIEW PAGE — Single Thread Discussion
 * ============================================================================
 *
 * View thread with nested replies, voting, and best answer
 */

import { useState } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import Link from "next/link"
import {
    ArrowLeft,
    ThumbsUp,
    ThumbsDown,
    MessageCircle,
    Share2,
    Flag,
    Edit,
    Trash2,
    CheckCircle,
    Quote,
    Eye,
    Clock,
    Pin,
    Lock,
    MoreVertical,
    Code,
    Image as ImageIcon,
    ExternalLink,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { CATEGORIES, type Reply } from "@/lib/community-types"
import { getReputationLevel } from "@/lib/reputation"

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_THREAD = {
    id: "1",
    title: "How to optimize Docker image size for production?",
    content: `I'm working on a Node.js application and my Docker image is currently 1.2GB, which seems way too large for production.

I'm using the official \`node:18\` base image and installing dependencies with npm. Here's my current Dockerfile:

\`\`\`dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
\`\`\`

What are the best practices for reducing Docker image size? Should I use Alpine? What about multi-stage builds?

Any help would be appreciated!`,
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
}

const MOCK_REPLIES: Reply[] = [
    {
        id: "r1",
        threadId: "1",
        content: `Great question! Here are my top recommendations:

1. **Use Alpine-based images**: Switch from \`node:18\` to \`node:18-alpine\` to reduce base image size from ~900MB to ~170MB

2. **Multi-stage builds**: Separate build and runtime stages

3. **Layer optimization**: Order your Dockerfile commands from least to most frequently changing

Here's an optimized Dockerfile:

\`\`\`dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
EXPOSE 3000
CMD ["node", "dist/index.js"]
\`\`\`

This should get you down to ~200MB or less!`,
        authorId: "user2",
        author: {
            id: "user2",
            name: "Alex Rodriguez",
            avatar: "AR",
            reputation: 2156,
        },
        upvotes: 42,
        downvotes: 1,
        isAccepted: true,
        createdAt: new Date("2025-01-12T11:15:00"),
        updatedAt: new Date("2025-01-12T11:15:00"),
        replies: [
            {
                id: "r1-1",
                threadId: "1",
                content:
                    "This is exactly what I needed! Thank you so much. Just implemented it and my image is now 185MB. Huge improvement! 🎉",
                authorId: "user1",
                author: {
                    id: "user1",
                    name: "Sarah Chen",
                    avatar: "SC",
                    reputation: 1250,
                },
                parentReplyId: "r1",
                upvotes: 8,
                downvotes: 0,
                isAccepted: false,
                createdAt: new Date("2025-01-12T14:30:00"),
                updatedAt: new Date("2025-01-12T14:30:00"),
            },
        ],
    },
    {
        id: "r2",
        threadId: "1",
        content: `Also consider using \`.dockerignore\` file to exclude unnecessary files from your build context:

\`\`\`
node_modules
npm-debug.log
.git
.env
*.md
.vscode
\`\`\`

This can significantly speed up your build process and reduce context size!`,
        authorId: "user3",
        author: {
            id: "user3",
            name: "Mike Johnson",
            avatar: "MJ",
            reputation: 856,
        },
        upvotes: 18,
        downvotes: 0,
        isAccepted: false,
        createdAt: new Date("2025-01-12T12:00:00"),
        updatedAt: new Date("2025-01-12T12:00:00"),
    },
    {
        id: "r3",
        threadId: "1",
        content: `One more tip: Use \`npm ci\` instead of \`npm install\` for cleaner and faster installs in CI/CD pipelines. It uses package-lock.json and ensures reproducible builds.`,
        authorId: "user4",
        author: {
            id: "user4",
            name: "Emma Wilson",
            avatar: "EW",
            reputation: 423,
        },
        upvotes: 12,
        downvotes: 0,
        isAccepted: false,
        createdAt: new Date("2025-01-13T09:15:00"),
        updatedAt: new Date("2025-01-13T09:15:00"),
    },
]

/* ============================================================================
   COMPONENTS
   ============================================================================ */

function ReplyCard({
    reply,
    depth = 0,
    onReply,
    onAcceptAnswer,
    isThreadAuthor = false,
}: {
    reply: Reply
    depth?: number
    onReply: (replyId: string) => void
    onAcceptAnswer?: (replyId: string) => void
    isThreadAuthor?: boolean
}) {
    const [showReplyBox, setShowReplyBox] = useState(false)
    const [replyContent, setReplyContent] = useState("")
    const [upvoted, setUpvoted] = useState(false)
    const [downvoted, setDownvoted] = useState(false)

    const repLevel = getReputationLevel(reply.author.reputation)
    const timeAgo = formatTimeAgo(reply.createdAt)
    const canNest = depth < 3

    const handleSubmitReply = () => {
        if (replyContent.trim()) {
            onReply(reply.id)
            setReplyContent("")
            setShowReplyBox(false)
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                depth > 0 && "ml-8 mt-4",
                depth === 0 && "mb-6"
            )}
        >
            <div
                className={cn(
                    "p-5 rounded-2xl",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border",
                    reply.isAccepted
                        ? "border-emerald-500/50 bg-emerald-500/5"
                        : "border-zinc-800/80"
                )}
            >
                {/* Header */}
                <div className="flex items-start gap-4 mb-4">
                    <div
                        className={cn(
                            "w-10 h-10 rounded-xl shrink-0",
                            "bg-gradient-to-br",
                            repLevel.gradient,
                            "flex items-center justify-center",
                            "text-sm font-bold text-white"
                        )}
                    >
                        {reply.author.avatar}
                    </div>

                    <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                            <span className={cn("font-semibold", repLevel.color)}>
                                {reply.author.name}
                            </span>
                            <span className="text-xs text-zinc-600">
                                {repLevel.level} {repLevel.icon}
                            </span>
                            <span className="text-xs text-zinc-600">•</span>
                            <span className="text-xs text-zinc-600">{timeAgo}</span>
                            {reply.isAccepted && (
                                <>
                                    <span className="text-xs text-zinc-600">•</span>
                                    <span className="text-xs text-emerald-400 flex items-center gap-1">
                                        <CheckCircle className="w-3 h-3" />
                                        Best Answer
                                    </span>
                                </>
                            )}
                        </div>
                        <div className="flex items-center gap-2 text-xs text-zinc-600">
                            <span>{reply.author.reputation} reputation</span>
                        </div>
                    </div>

                    <button className="p-1.5 rounded-lg hover:bg-zinc-800/50 text-zinc-500 hover:text-zinc-300">
                        <MoreVertical className="w-4 h-4" />
                    </button>
                </div>

                {/* Content */}
                <div className="text-zinc-300 mb-4 whitespace-pre-wrap leading-relaxed">
                    {reply.content.split("```").map((part, i) =>
                        i % 2 === 0 ? (
                            <span key={i}>{part}</span>
                        ) : (
                            <pre
                                key={i}
                                className="my-3 p-4 rounded-xl bg-zinc-900/80 border border-zinc-800 overflow-x-auto text-sm"
                            >
                                <code className="text-emerald-400">{part}</code>
                            </pre>
                        )
                    )}
                </div>

                {/* Actions */}
                <div className="flex items-center gap-2 flex-wrap">
                    <div className="flex items-center gap-1">
                        <Button
                            variant="ghost"
                            size="sm"
                            className={cn(
                                "rounded-lg",
                                upvoted && "text-emerald-400"
                            )}
                            onClick={() => {
                                setUpvoted(!upvoted)
                                setDownvoted(false)
                            }}
                        >
                            <ThumbsUp className="w-4 h-4 mr-1" />
                            {reply.upvotes + (upvoted ? 1 : 0)}
                        </Button>
                        <Button
                            variant="ghost"
                            size="sm"
                            className={cn(
                                "rounded-lg",
                                downvoted && "text-red-400"
                            )}
                            onClick={() => {
                                setDownvoted(!downvoted)
                                setUpvoted(false)
                            }}
                        >
                            <ThumbsDown className="w-4 h-4" />
                        </Button>
                    </div>

                    {canNest && (
                        <Button
                            variant="ghost"
                            size="sm"
                            className="rounded-lg"
                            onClick={() => setShowReplyBox(!showReplyBox)}
                        >
                            <MessageCircle className="w-4 h-4 mr-1" />
                            Reply
                        </Button>
                    )}

                    <Button variant="ghost" size="sm" className="rounded-lg">
                        <Quote className="w-4 h-4 mr-1" />
                        Quote
                    </Button>

                    {isThreadAuthor && !reply.isAccepted && onAcceptAnswer && (
                        <Button
                            variant="ghost"
                            size="sm"
                            className="rounded-lg text-emerald-400 hover:text-emerald-300"
                            onClick={() => onAcceptAnswer(reply.id)}
                        >
                            <CheckCircle className="w-4 h-4 mr-1" />
                            Mark as Answer
                        </Button>
                    )}

                    <Button variant="ghost" size="sm" className="rounded-lg ml-auto">
                        <Share2 className="w-4 h-4 mr-1" />
                        Share
                    </Button>

                    <Button
                        variant="ghost"
                        size="sm"
                        className="rounded-lg text-red-400"
                    >
                        <Flag className="w-4 h-4 mr-1" />
                        Report
                    </Button>
                </div>

                {/* Reply Box */}
                {showReplyBox && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        className="mt-4"
                    >
                        <Textarea
                            placeholder="Write your reply..."
                            value={replyContent}
                            onChange={(e) => setReplyContent(e.target.value)}
                            className="mb-2 rounded-xl bg-zinc-900/50 border-zinc-800"
                            rows={4}
                        />
                        <div className="flex gap-2">
                            <Button
                                onClick={handleSubmitReply}
                                className="rounded-lg bg-purple-600 hover:bg-purple-500"
                            >
                                Post Reply
                            </Button>
                            <Button
                                variant="ghost"
                                onClick={() => setShowReplyBox(false)}
                                className="rounded-lg"
                            >
                                Cancel
                            </Button>
                        </div>
                    </motion.div>
                )}
            </div>

            {/* Nested Replies */}
            {reply.replies && reply.replies.length > 0 && (
                <div className="mt-2">
                    {reply.replies.map((nestedReply) => (
                        <ReplyCard
                            key={nestedReply.id}
                            reply={nestedReply}
                            depth={depth + 1}
                            onReply={onReply}
                            onAcceptAnswer={onAcceptAnswer}
                            isThreadAuthor={isThreadAuthor}
                        />
                    ))}
                </div>
            )}
        </motion.div>
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

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function ThreadPage({ params }: { params: { threadId: string } }) {
    const [replyContent, setReplyContent] = useState("")
    const [upvoted, setUpvoted] = useState(false)
    const [downvoted, setDownvoted] = useState(false)

    const thread = MOCK_THREAD
    const replies = MOCK_REPLIES
    const repLevel = getReputationLevel(thread.author.reputation)
    const timeAgo = formatTimeAgo(thread.createdAt)

    const handleReply = (replyId: string) => {
        console.log("Reply to:", replyId)
    }

    const handleAcceptAnswer = (replyId: string) => {
        console.log("Accept answer:", replyId)
    }

    const handleSubmitReply = () => {
        if (replyContent.trim()) {
            console.log("Submit reply:", replyContent)
            setReplyContent("")
        }
    }

    return (
        <div className="min-h-screen">
            {/* Back Button */}
            <Link href="/community" prefetch={false}>
                <Button variant="ghost" className="mb-6 rounded-xl">
                    <ArrowLeft className="w-4 h-4 mr-2" />
                    Back to Community
                </Button>
            </Link>

            {/* Thread */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "p-8 rounded-3xl mb-8",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border",
                    thread.isPinned
                        ? "border-amber-500/40 bg-amber-500/5"
                        : "border-zinc-800/80"
                )}
            >
                {/* Thread Header */}
                <div className="flex items-start gap-4 mb-6">
                    <div
                        className={cn(
                            "w-16 h-16 rounded-xl shrink-0",
                            "bg-gradient-to-br",
                            repLevel.gradient,
                            "flex items-center justify-center",
                            "text-xl font-bold text-white"
                        )}
                    >
                        {thread.author.avatar}
                    </div>

                    <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                            <span className={cn("text-lg font-semibold", repLevel.color)}>
                                {thread.author.name}
                            </span>
                            <span className="text-sm text-zinc-600">
                                {repLevel.level} {repLevel.icon}
                            </span>
                            {thread.isPinned && (
                                <>
                                    <span className="text-zinc-600">•</span>
                                    <Pin className="w-4 h-4 text-amber-400" />
                                    <span className="text-sm text-amber-400">Pinned</span>
                                </>
                            )}
                            {thread.isLocked && (
                                <>
                                    <span className="text-zinc-600">•</span>
                                    <Lock className="w-4 h-4 text-zinc-500" />
                                    <span className="text-sm text-zinc-500">Locked</span>
                                </>
                            )}
                        </div>
                        <div className="flex items-center gap-3 text-sm text-zinc-600">
                            <span>{thread.author.reputation} reputation</span>
                            <span>•</span>
                            <span>{timeAgo}</span>
                            <span>•</span>
                            <span className="flex items-center gap-1">
                                <Eye className="w-3 h-3" />
                                {thread.views} views
                            </span>
                        </div>
                    </div>

                    <div className="flex items-center gap-2">
                        <Button variant="ghost" size="sm" className="rounded-lg">
                            <Edit className="w-4 h-4" />
                        </Button>
                        <Button
                            variant="ghost"
                            size="sm"
                            className="rounded-lg text-red-400"
                        >
                            <Trash2 className="w-4 h-4" />
                        </Button>
                    </div>
                </div>

                {/* Thread Title */}
                <h1 className="text-3xl font-black text-white mb-4">{thread.title}</h1>

                {/* Category and Tags */}
                <div className="flex items-center gap-3 mb-6">
                    <span
                        className={cn(
                            "px-3 py-1.5 rounded-lg text-sm font-medium",
                            "bg-gradient-to-r",
                            thread.category.gradient,
                            "bg-opacity-20"
                        )}
                    >
                        {thread.category.icon} {thread.category.name}
                    </span>
                    {thread.tags.map((tag) => (
                        <span
                            key={tag}
                            className="px-3 py-1.5 rounded-lg bg-zinc-800/50 text-zinc-400 text-sm"
                        >
                            #{tag}
                        </span>
                    ))}
                </div>

                {/* Thread Content */}
                <div className="text-zinc-300 mb-6 whitespace-pre-wrap leading-relaxed text-lg">
                    {thread.content.split("```").map((part, i) =>
                        i % 2 === 0 ? (
                            <span key={i}>{part}</span>
                        ) : (
                            <pre
                                key={i}
                                className="my-4 p-4 rounded-xl bg-zinc-900/80 border border-zinc-800 overflow-x-auto text-sm"
                            >
                                <code className="text-emerald-400">{part}</code>
                            </pre>
                        )
                    )}
                </div>

                {/* Thread Actions */}
                <div className="flex items-center gap-2 flex-wrap pt-6 border-t border-zinc-800">
                    <div className="flex items-center gap-1">
                        <Button
                            variant="ghost"
                            className={cn("rounded-lg", upvoted && "text-emerald-400")}
                            onClick={() => {
                                setUpvoted(!upvoted)
                                setDownvoted(false)
                            }}
                        >
                            <ThumbsUp className="w-5 h-5 mr-2" />
                            {thread.upvotes + (upvoted ? 1 : 0)}
                        </Button>
                        <Button
                            variant="ghost"
                            className={cn("rounded-lg", downvoted && "text-red-400")}
                            onClick={() => {
                                setDownvoted(!downvoted)
                                setUpvoted(false)
                            }}
                        >
                            <ThumbsDown className="w-5 h-5" />
                        </Button>
                    </div>

                    <Button variant="ghost" className="rounded-lg">
                        <Share2 className="w-5 h-5 mr-2" />
                        Share Thread
                    </Button>

                    <Button variant="ghost" className="rounded-lg text-red-400 ml-auto">
                        <Flag className="w-5 h-5 mr-2" />
                        Report
                    </Button>
                </div>
            </motion.div>

            {/* Replies Section */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
            >
                <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-2">
                    <MessageCircle className="w-6 h-6 text-purple-400" />
                    {thread.replyCount} Replies
                </h2>

                {replies.map((reply) => (
                    <ReplyCard
                        key={reply.id}
                        reply={reply}
                        onReply={handleReply}
                        onAcceptAnswer={handleAcceptAnswer}
                        isThreadAuthor={true}
                    />
                ))}
            </motion.div>

            {/* Reply Form */}
            {!thread.isLocked && (
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3 }}
                    className={cn(
                        "p-6 rounded-2xl mt-8",
                        "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                        "border border-zinc-800/80"
                    )}
                >
                    <h3 className="text-lg font-semibold text-white mb-4">
                        Your Reply
                    </h3>
                    <Textarea
                        placeholder="Share your thoughts..."
                        value={replyContent}
                        onChange={(e) => setReplyContent(e.target.value)}
                        className="mb-4 rounded-xl bg-zinc-900/50 border-zinc-800 min-h-[150px]"
                    />
                    <div className="flex items-center gap-2">
                        <Button
                            onClick={handleSubmitReply}
                            className="rounded-xl bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
                        >
                            <MessageCircle className="w-4 h-4 mr-2" />
                            Post Reply
                        </Button>
                        <Button variant="ghost" className="rounded-xl">
                            <Code className="w-4 h-4 mr-2" />
                            Code Block
                        </Button>
                        <Button variant="ghost" className="rounded-xl">
                            <ImageIcon className="w-4 h-4 mr-2" />
                            Upload Image
                        </Button>
                    </div>
                </motion.div>
            )}
        </div>
    )
}
