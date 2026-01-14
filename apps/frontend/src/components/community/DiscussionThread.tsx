"use client"

/**
 * ============================================================================
 * DISCUSSION THREAD — Thread View with Nested Replies
 * ============================================================================
 *
 * Complete thread display with replies, voting, and markdown support
 */

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { type Thread, type Reply } from "@/lib/community-types"
import { getReputationLevel } from "@/lib/reputation"
import Link from "next/link"
import {
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
    Pin,
    Lock,
    MoreVertical,
    ArrowLeft,
    Code,
    Image as ImageIcon,
    Bold,
    Italic,
    List,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

interface DiscussionThreadProps {
    thread: Thread
    replies: Reply[]
    currentUserId?: string
    onReply?: (replyId: string, content: string) => void
    onVote?: (
        targetType: "thread" | "reply",
        targetId: string,
        voteType: "up" | "down"
    ) => void
    onAcceptAnswer?: (replyId: string) => void
    onDelete?: (targetType: "thread" | "reply", targetId: string) => void
    onEdit?: (
        targetType: "thread" | "reply",
        targetId: string,
        content: string
    ) => void
    className?: string
}

export function DiscussionThread({
    thread,
    replies,
    currentUserId = "user1",
    onReply,
    onVote,
    onAcceptAnswer,
    onDelete,
    onEdit,
    className,
}: DiscussionThreadProps) {
    const [replyContent, setReplyContent] = useState("")
    const [threadUpvoted, setThreadUpvoted] = useState(false)
    const [threadDownvoted, setThreadDownvoted] = useState(false)
    const repLevel = getReputationLevel(thread.author.reputation)
    const timeAgo = formatTimeAgo(thread.createdAt)
    const isThreadAuthor = thread.authorId === currentUserId

    const handleSubmitReply = () => {
        if (replyContent.trim() && onReply) {
            onReply(thread.id, replyContent)
            setReplyContent("")
        }
    }

    return (
        <div className={cn("space-y-8", className)}>
            {/* Back Button */}
            <Link href="/community" prefetch={false}>
                <Button variant="ghost" className="rounded-xl">
                    <ArrowLeft className="w-4 h-4 mr-2" />
                    Back to Community
                </Button>
            </Link>

            {/* Thread */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "p-8 rounded-3xl",
                    "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                    "border",
                    thread.isPinned
                        ? "border-amber-500/40 bg-amber-500/5"
                        : "border-zinc-800/80"
                )}
                style={{
                    boxShadow: "0 0 40px rgba(0, 0, 0, 0.5)",
                }}
            >
                {/* Thread Header */}
                <div className="flex items-start gap-4 mb-6">
                    <Link
                        href={`/community/user/${thread.authorId}`}
                        prefetch={false}
                    >
                        <div
                            className={cn(
                                "w-16 h-16 rounded-xl shrink-0 cursor-pointer",
                                "bg-gradient-to-br",
                                repLevel.gradient,
                                "flex items-center justify-center",
                                "text-xl font-bold text-white",
                                "hover:scale-105 transition-transform"
                            )}
                            style={{
                                boxShadow: `0 0 30px ${repLevel.glowColor}`,
                            }}
                        >
                            {thread.author.avatar}
                        </div>
                    </Link>

                    <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                            <Link
                                href={`/community/user/${thread.authorId}`}
                                prefetch={false}
                            >
                                <span
                                    className={cn(
                                        "text-lg font-semibold hover:underline cursor-pointer",
                                        repLevel.color
                                    )}
                                >
                                    {thread.author.name}
                                </span>
                            </Link>
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

                    {isThreadAuthor && (
                        <div className="flex items-center gap-2">
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <Edit className="w-4 h-4" />
                            </Button>
                            <Button
                                variant="ghost"
                                size="sm"
                                className="rounded-lg text-red-400 hover:text-red-300"
                                onClick={() => onDelete?.("thread", thread.id)}
                            >
                                <Trash2 className="w-4 h-4" />
                            </Button>
                        </div>
                    )}
                </div>

                {/* Thread Title */}
                <h1 className="text-3xl font-black text-white mb-4">
                    {thread.title}
                </h1>

                {/* Category and Tags */}
                <div className="flex items-center gap-3 mb-6">
                    <Link
                        href={`/community?category=${thread.category.slug}`}
                        prefetch={false}
                    >
                        <span
                            className={cn(
                                "px-3 py-1.5 rounded-lg text-sm font-medium cursor-pointer",
                                "bg-gradient-to-r",
                                thread.category.gradient,
                                "bg-opacity-20",
                                "hover:bg-opacity-30 transition-all"
                            )}
                        >
                            {thread.category.icon} {thread.category.name}
                        </span>
                    </Link>
                    {thread.tags.map((tag) => (
                        <span
                            key={tag}
                            className="px-3 py-1.5 rounded-lg bg-zinc-800/50 text-zinc-400 text-sm hover:bg-zinc-800 transition-colors cursor-pointer"
                        >
                            #{tag}
                        </span>
                    ))}
                </div>

                {/* Thread Content */}
                <div className="prose prose-invert max-w-none mb-6">
                    <MarkdownContent content={thread.content} />
                </div>

                {/* Thread Actions */}
                <div className="flex items-center gap-2 flex-wrap pt-6 border-t border-zinc-800">
                    <div className="flex items-center gap-1">
                        <Button
                            variant="ghost"
                            className={cn(
                                "rounded-lg",
                                threadUpvoted && "text-emerald-400"
                            )}
                            onClick={() => {
                                setThreadUpvoted(!threadUpvoted)
                                setThreadDownvoted(false)
                                onVote?.(
                                    "thread",
                                    thread.id,
                                    threadUpvoted ? "down" : "up"
                                )
                            }}
                        >
                            <ThumbsUp className="w-5 h-5 mr-2" />
                            {thread.upvotes + (threadUpvoted ? 1 : 0)}
                        </Button>
                        <Button
                            variant="ghost"
                            className={cn(
                                "rounded-lg",
                                threadDownvoted && "text-red-400"
                            )}
                            onClick={() => {
                                setThreadDownvoted(!threadDownvoted)
                                setThreadUpvoted(false)
                                onVote?.(
                                    "thread",
                                    thread.id,
                                    threadDownvoted ? "up" : "down"
                                )
                            }}
                        >
                            <ThumbsDown className="w-5 h-5" />
                        </Button>
                    </div>

                    <Button variant="ghost" className="rounded-lg">
                        <Share2 className="w-5 h-5 mr-2" />
                        Share Thread
                    </Button>

                    <Button
                        variant="ghost"
                        className="rounded-lg text-red-400 hover:text-red-300 ml-auto"
                    >
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

                <div className="space-y-4">
                    {replies.map((reply) => (
                        <ReplyCard
                            key={reply.id}
                            reply={reply}
                            currentUserId={currentUserId}
                            isThreadAuthor={isThreadAuthor}
                            onReply={onReply}
                            onVote={onVote}
                            onAcceptAnswer={onAcceptAnswer}
                            onDelete={onDelete}
                        />
                    ))}
                </div>

                {replies.length === 0 && (
                    <div className="text-center py-12 text-zinc-500">
                        <MessageCircle className="w-12 h-12 mx-auto mb-4 text-zinc-700" />
                        <p className="text-lg">No replies yet</p>
                        <p className="text-sm">Be the first to share your thoughts!</p>
                    </div>
                )}
            </motion.div>

            {/* Reply Form */}
            {!thread.isLocked && (
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3 }}
                    className={cn(
                        "p-6 rounded-2xl",
                        "bg-gradient-to-br from-[#0a0a0f] to-[#0d0d14]",
                        "border border-zinc-800/80"
                    )}
                >
                    <h3 className="text-lg font-semibold text-white mb-4">
                        Your Reply
                    </h3>
                    <Textarea
                        placeholder="Share your thoughts... (Markdown supported)"
                        value={replyContent}
                        onChange={(e) => setReplyContent(e.target.value)}
                        className="mb-4 rounded-xl bg-zinc-900/50 border-zinc-800 min-h-[150px] font-mono text-sm"
                    />
                    <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-2">
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <Bold className="w-4 h-4" />
                            </Button>
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <Italic className="w-4 h-4" />
                            </Button>
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <Code className="w-4 h-4" />
                            </Button>
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <List className="w-4 h-4" />
                            </Button>
                            <Button variant="ghost" size="sm" className="rounded-lg">
                                <ImageIcon className="w-4 h-4" />
                            </Button>
                        </div>
                        <Button
                            onClick={handleSubmitReply}
                            disabled={!replyContent.trim()}
                            className="rounded-xl bg-gradient-to-r from-purple-600 to-purple-500 hover:from-purple-500 hover:to-purple-400"
                        >
                            <MessageCircle className="w-4 h-4 mr-2" />
                            Post Reply
                        </Button>
                    </div>
                </motion.div>
            )}

            {thread.isLocked && (
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.3 }}
                    className={cn(
                        "p-6 rounded-2xl text-center",
                        "bg-zinc-900/50 border border-zinc-800/80"
                    )}
                >
                    <Lock className="w-8 h-8 text-zinc-600 mx-auto mb-2" />
                    <p className="text-zinc-500">
                        This thread has been locked and cannot accept new replies.
                    </p>
                </motion.div>
            )}
        </div>
    )
}

function ReplyCard({
    reply,
    depth = 0,
    currentUserId,
    isThreadAuthor,
    onReply,
    onVote,
    onAcceptAnswer,
    onDelete,
}: {
    reply: Reply
    depth?: number
    currentUserId: string
    isThreadAuthor: boolean
    onReply?: (replyId: string, content: string) => void
    onVote?: (
        targetType: "thread" | "reply",
        targetId: string,
        voteType: "up" | "down"
    ) => void
    onAcceptAnswer?: (replyId: string) => void
    onDelete?: (targetType: "thread" | "reply", targetId: string) => void
}) {
    const [showReplyBox, setShowReplyBox] = useState(false)
    const [replyContent, setReplyContent] = useState("")
    const [upvoted, setUpvoted] = useState(false)
    const [downvoted, setDownvoted] = useState(false)

    const repLevel = getReputationLevel(reply.author.reputation)
    const timeAgo = formatTimeAgo(reply.createdAt)
    const canNest = depth < 3
    const isAuthor = reply.authorId === currentUserId

    const handleSubmitReply = () => {
        if (replyContent.trim() && onReply) {
            onReply(reply.id, replyContent)
            setReplyContent("")
            setShowReplyBox(false)
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(depth > 0 && "ml-8 mt-4", depth === 0 && "mb-6")}
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
                    <Link
                        href={`/community/user/${reply.authorId}`}
                        prefetch={false}
                    >
                        <div
                            className={cn(
                                "w-10 h-10 rounded-xl shrink-0 cursor-pointer",
                                "bg-gradient-to-br",
                                repLevel.gradient,
                                "flex items-center justify-center",
                                "text-sm font-bold text-white",
                                "hover:scale-105 transition-transform"
                            )}
                        >
                            {reply.author.avatar}
                        </div>
                    </Link>

                    <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                            <Link
                                href={`/community/user/${reply.authorId}`}
                                prefetch={false}
                            >
                                <span
                                    className={cn(
                                        "font-semibold hover:underline cursor-pointer",
                                        repLevel.color
                                    )}
                                >
                                    {reply.author.name}
                                </span>
                            </Link>
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
                        <div className="text-xs text-zinc-600">
                            {reply.author.reputation} reputation
                        </div>
                    </div>

                    {(isAuthor || isThreadAuthor) && (
                        <button className="p-1.5 rounded-lg hover:bg-zinc-800/50 text-zinc-500 hover:text-zinc-300">
                            <MoreVertical className="w-4 h-4" />
                        </button>
                    )}
                </div>

                {/* Content */}
                <div className="prose prose-invert prose-sm max-w-none mb-4">
                    <MarkdownContent content={reply.content} />
                </div>

                {/* Actions */}
                <div className="flex items-center gap-2 flex-wrap">
                    <div className="flex items-center gap-1">
                        <Button
                            variant="ghost"
                            size="sm"
                            className={cn("rounded-lg", upvoted && "text-emerald-400")}
                            onClick={() => {
                                setUpvoted(!upvoted)
                                setDownvoted(false)
                                onVote?.("reply", reply.id, upvoted ? "down" : "up")
                            }}
                        >
                            <ThumbsUp className="w-4 h-4 mr-1" />
                            {reply.upvotes + (upvoted ? 1 : 0)}
                        </Button>
                        <Button
                            variant="ghost"
                            size="sm"
                            className={cn("rounded-lg", downvoted && "text-red-400")}
                            onClick={() => {
                                setDownvoted(!downvoted)
                                setUpvoted(false)
                                onVote?.("reply", reply.id, downvoted ? "up" : "down")
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

                    <Button
                        variant="ghost"
                        size="sm"
                        className="rounded-lg ml-auto"
                    >
                        <Share2 className="w-4 h-4 mr-1" />
                        Share
                    </Button>

                    {!isAuthor && (
                        <Button
                            variant="ghost"
                            size="sm"
                            className="rounded-lg text-red-400 hover:text-red-300"
                        >
                            <Flag className="w-4 h-4 mr-1" />
                            Report
                        </Button>
                    )}

                    {isAuthor && (
                        <Button
                            variant="ghost"
                            size="sm"
                            className="rounded-lg text-red-400 hover:text-red-300"
                            onClick={() => onDelete?.("reply", reply.id)}
                        >
                            <Trash2 className="w-4 h-4 mr-1" />
                            Delete
                        </Button>
                    )}
                </div>

                {/* Reply Box */}
                <AnimatePresence>
                    {showReplyBox && (
                        <motion.div
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: "auto" }}
                            exit={{ opacity: 0, height: 0 }}
                            className="mt-4"
                        >
                            <Textarea
                                placeholder="Write your reply... (Markdown supported)"
                                value={replyContent}
                                onChange={(e) => setReplyContent(e.target.value)}
                                className="mb-2 rounded-xl bg-zinc-900/50 border-zinc-800 font-mono text-sm"
                                rows={4}
                            />
                            <div className="flex gap-2">
                                <Button
                                    onClick={handleSubmitReply}
                                    disabled={!replyContent.trim()}
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
                </AnimatePresence>
            </div>

            {/* Nested Replies */}
            {reply.replies && reply.replies.length > 0 && (
                <div className="mt-2">
                    {reply.replies.map((nestedReply) => (
                        <ReplyCard
                            key={nestedReply.id}
                            reply={nestedReply}
                            depth={depth + 1}
                            currentUserId={currentUserId}
                            isThreadAuthor={isThreadAuthor}
                            onReply={onReply}
                            onVote={onVote}
                            onAcceptAnswer={onAcceptAnswer}
                            onDelete={onDelete}
                        />
                    ))}
                </div>
            )}
        </motion.div>
    )
}

function MarkdownContent({ content }: { content: string }) {
    // Simple markdown parser for code blocks
    const parts = content.split("```")

    return (
        <div className="text-zinc-300 whitespace-pre-wrap leading-relaxed">
            {parts.map((part, i) =>
                i % 2 === 0 ? (
                    <span key={i}>{part}</span>
                ) : (
                    <pre
                        key={i}
                        className="my-3 p-4 rounded-xl bg-zinc-900/80 border border-zinc-800 overflow-x-auto text-sm"
                    >
                        <code className="text-emerald-400 font-mono">{part}</code>
                    </pre>
                )
            )}
        </div>
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
