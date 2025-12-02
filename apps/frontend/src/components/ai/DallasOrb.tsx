"use client"

/**
 * ============================================================================
 * DALLAS ORB - Enterprise Level 5 AI Assistant
 * ============================================================================
 *
 * "Knowledge is power. I'm here to empower your DevOps journey."
 *
 * Design Philosophy:
 * - Dallas-inspired mystical orb (grey/white/silver with blue magic)
 * - Ambient breathing glow animation
 * - Positioned under user name in top-right
 * - Opens into elegant centered modal
 * - Enterprise-grade micro-interactions
 *
 * Color Palette:
 * - Grey (#6B7280, #9CA3AF)
 * - White light (#F9FAFB, #FFFFFF)
 * - Blue magic (#3B82F6, #60A5FA)
 * - Silver accents (#E5E7EB)
 *
 * @phase ENTERPRISE-LEVEL-5
 */

import { useState, useRef, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { X, Send, Loader2, Sparkles } from "lucide-react"
import { usePathname } from "next/navigation"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Message {
    id: string
    role: "user" | "assistant"
    content: string
    timestamp: Date
}

/* ============================================================================
   DALLAS QUOTES
   ============================================================================ */

const DALLAS_GREETINGS = [
    "Ready to level up? I'm Dallas, your DevOps guide. Let's build something great! 🚀",
    "Knowledge is power. What would you like to learn today? 💡",
    "Every expert was once a beginner. Let's continue your journey! 🎯",
    "The best time to learn was yesterday. The second best time is now. How can I help? ⚡",
]

const WELCOME_MESSAGE: Message = {
    id: "welcome",
    role: "assistant",
    content: DALLAS_GREETINGS[Math.floor(Math.random() * DALLAS_GREETINGS.length)],
    timestamp: new Date(),
}

const QUICK_PROMPTS = [
    { label: "Guide my path", prompt: "What should I learn next on my DevOps journey?" },
    { label: "Explain this", prompt: "Can you explain what I'm currently working on?" },
    { label: "I need wisdom", prompt: "I'm stuck and need some guidance." },
]

/* ============================================================================
   ANIMATED ORB COMPONENT - The Dallas Crystal
   ============================================================================ */

function MagicOrb({ isActive, onClick }: { isActive: boolean; onClick: () => void }) {
    return (
        <motion.button
            onClick={onClick}
            className="relative group"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            aria-label="Open Dallas AI Assistant"
        >
            {/* Outer glow rings - very subtle breathing */}
            <motion.div
                className="absolute inset-0 rounded-full"
                animate={{
                    boxShadow: [
                        "0 0 4px 1px rgba(59, 130, 246, 0.08)",
                        "0 0 8px 2px rgba(59, 130, 246, 0.12)",
                        "0 0 4px 1px rgba(59, 130, 246, 0.08)",
                    ],
                }}
                transition={{
                    duration: 5,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
            />

            {/* Secondary pulse ring - disabled for subtlety */}
            {/* Removed to reduce glow intensity */}

            {/* Main orb */}
            <div className={cn(
                "relative w-10 h-10 rounded-full",
                "bg-gradient-to-br from-gray-100 via-white to-gray-200",
                "dark:from-gray-700 dark:via-gray-600 dark:to-gray-800",
                "shadow-md",
                "border border-gray-200/50 dark:border-gray-600/50",
                "flex items-center justify-center",
                "overflow-hidden"
            )}>
                {/* Inner magical glow - very subtle */}
                <motion.div
                    className="absolute inset-1 rounded-full bg-gradient-to-br from-blue-400/10 to-indigo-500/10"
                    animate={{
                        opacity: [0.2, 0.3, 0.2],
                    }}
                    transition={{
                        duration: 4,
                        repeat: Infinity,
                        ease: "easeInOut",
                    }}
                />

                {/* Wolf emoji */}
                <span className="text-xl relative z-10">🐺</span>

                {/* Sparkle effects - removed for cleaner look */}
            </div>

            {/* Hover tooltip */}
            <div className={cn(
                "absolute -bottom-8 left-1/2 -translate-x-1/2",
                "px-2 py-1 rounded-md",
                "bg-gray-900 dark:bg-gray-100",
                "text-white dark:text-gray-900",
                "text-xs font-medium whitespace-nowrap",
                "opacity-0 group-hover:opacity-100",
                "transition-opacity duration-200",
                "pointer-events-none"
            )}>
                Dallas
            </div>
        </motion.button>
    )
}

/* ============================================================================
   CHAT MESSAGE COMPONENT
   ============================================================================ */

function ChatMessage({ message }: { message: Message }) {
    const isAssistant = message.role === "assistant"

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "flex gap-3",
                isAssistant ? "justify-start" : "justify-end"
            )}
        >
            {isAssistant && (
                <div className={cn(
                    "w-8 h-8 rounded-full flex-shrink-0",
                    "bg-gradient-to-br from-gray-200 to-gray-300",
                    "dark:from-gray-600 dark:to-gray-700",
                    "flex items-center justify-center",
                    "shadow-md shadow-blue-500/10"
                )}>
                    <span className="text-sm">🐺</span>
                </div>
            )}
            <div
                className={cn(
                    "max-w-[80%] rounded-2xl px-4 py-3",
                    isAssistant
                        ? "bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100 rounded-tl-sm"
                        : "bg-gradient-to-r from-blue-500 to-indigo-500 text-white rounded-tr-sm shadow-lg shadow-blue-500/20"
                )}
            >
                <p className="text-sm whitespace-pre-wrap leading-relaxed">{message.content}</p>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   TYPING INDICATOR
   ============================================================================ */

function TypingIndicator() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="flex gap-3"
        >
            <div className={cn(
                "w-8 h-8 rounded-full flex-shrink-0",
                "bg-gradient-to-br from-gray-200 to-gray-300",
                "dark:from-gray-600 dark:to-gray-700",
                "flex items-center justify-center"
            )}>
                <span className="text-sm">🐺</span>
            </div>
            <div className="bg-gray-100 dark:bg-gray-800 rounded-2xl rounded-tl-sm px-4 py-3 flex gap-1.5">
                {[0, 1, 2].map((i) => (
                    <motion.div
                        key={i}
                        className="w-2 h-2 bg-blue-400 rounded-full"
                        animate={{ y: [0, -6, 0] }}
                        transition={{
                            duration: 0.6,
                            repeat: Infinity,
                            delay: i * 0.15,
                        }}
                    />
                ))}
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN DALLAS ORB COMPONENT
   ============================================================================ */

export function DallasOrb() {
    const [isOpen, setIsOpen] = useState(false)
    const [messages, setMessages] = useState<Message[]>([WELCOME_MESSAGE])
    const [input, setInput] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const messagesEndRef = useRef<HTMLDivElement>(null)
    const inputRef = useRef<HTMLInputElement>(null)
    const pathname = usePathname()

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }, [messages])

    // Focus input when opened
    useEffect(() => {
        if (isOpen) {
            setTimeout(() => inputRef.current?.focus(), 100)
        }
    }, [isOpen])

    // ESC to close
    useEffect(() => {
        const handleEsc = (e: KeyboardEvent) => {
            if (e.key === "Escape") setIsOpen(false)
        }
        window.addEventListener("keydown", handleEsc)
        return () => window.removeEventListener("keydown", handleEsc)
    }, [])

    const getContext = useCallback(() => {
        const path = pathname || "/"
        if (path.includes("/modules/")) return { type: "module", path }
        if (path.includes("/tasks/")) return { type: "task", path }
        if (path.includes("/dashboard")) return { type: "dashboard", path }
        return { type: "general", path }
    }, [pathname])

    const handleSend = async () => {
        if (!input.trim() || isLoading) return

        const userMessage: Message = {
            id: Date.now().toString(),
            role: "user",
            content: input.trim(),
            timestamp: new Date(),
        }

        setMessages((prev) => [...prev, userMessage])
        setInput("")
        setIsLoading(true)

        try {
            const response = await fetch("/api/ai/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: userMessage.content,
                    context: getContext(),
                }),
            })

            if (!response.ok) throw new Error("Failed to get response")

            const data = await response.json()

            const assistantMessage: Message = {
                id: (Date.now() + 1).toString(),
                role: "assistant",
                content: data.response || "The path is unclear... Please try again.",
                timestamp: new Date(),
            }

            setMessages((prev) => [...prev, assistantMessage])
        } catch {
            const fallbackMessage: Message = {
                id: (Date.now() + 1).toString(),
                role: "assistant",
                content: "Even the best systems need a moment. Let me try again for you! 🔄",
                timestamp: new Date(),
            }
            setMessages((prev) => [...prev, fallbackMessage])
        } finally {
            setIsLoading(false)
        }
    }

    const handleQuickPrompt = (prompt: string) => {
        setInput(prompt)
        setTimeout(() => handleSend(), 100)
    }

    return (
        <>
            {/* The Orb - positioned in header */}
            <MagicOrb isActive={isOpen} onClick={() => setIsOpen(true)} />

            {/* Modal Overlay */}
            <AnimatePresence>
                {isOpen && (
                    <>
                        {/* Backdrop */}
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setIsOpen(false)}
                            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
                        />

                        {/* Modal */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.95, y: 20 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.95, y: 20 }}
                            transition={{ type: "spring", damping: 25, stiffness: 300 }}
                            className={cn(
                                "fixed z-50",
                                "top-20 left-4 right-4 bottom-4",
                                "sm:top-auto sm:bottom-auto sm:left-1/2 sm:right-auto",
                                "sm:-translate-x-1/2 sm:top-1/2 sm:-translate-y-1/2",
                                "sm:w-[90vw] sm:max-w-lg sm:h-[70vh] sm:max-h-[500px]",
                                "bg-white dark:bg-gray-900",
                                "rounded-2xl shadow-2xl",
                                "border border-gray-200 dark:border-gray-800",
                                "flex flex-col overflow-hidden"
                            )}
                        >
                            {/* Header */}
                            <div className={cn(
                                "flex items-center justify-between px-6 py-4",
                                "border-b border-gray-100 dark:border-gray-800",
                                "bg-gradient-to-r from-gray-50 to-white dark:from-gray-900 dark:to-gray-800"
                            )}>
                                <div className="flex items-center gap-3">
                                    <div className={cn(
                                        "w-10 h-10 rounded-full",
                                        "bg-gradient-to-br from-gray-100 to-gray-200 dark:from-gray-700 dark:to-gray-800",
                                        "flex items-center justify-center",
                                        "shadow-inner"
                                    )}>
                                        <motion.div
                                            animate={{ scale: [1, 1.1, 1] }}
                                            transition={{ duration: 2, repeat: Infinity }}
                                        >
                                            <span className="text-xl">🐺</span>
                                        </motion.div>
                                    </div>
                                    <div>
                                        <h2 className="font-semibold text-gray-900 dark:text-white">
                                            Dallas
                                        </h2>
                                        <p className="text-xs text-gray-500 dark:text-gray-400 flex items-center gap-1">
                                            <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse" />
                                            Your DevOps AI Guide
                                        </p>
                                    </div>
                                </div>
                                <button
                                    onClick={() => setIsOpen(false)}
                                    className={cn(
                                        "p-2 rounded-xl",
                                        "text-gray-400 hover:text-gray-600 dark:hover:text-gray-300",
                                        "hover:bg-gray-100 dark:hover:bg-gray-800",
                                        "transition-colors"
                                    )}
                                >
                                    <X className="w-5 h-5" />
                                </button>
                            </div>

                            {/* Messages */}
                            <div className="flex-1 overflow-y-auto p-6 space-y-4">
                                {messages.map((message) => (
                                    <ChatMessage key={message.id} message={message} />
                                ))}
                                {isLoading && <TypingIndicator />}
                                <div ref={messagesEndRef} />
                            </div>

                            {/* Quick Prompts */}
                            {messages.length <= 2 && (
                                <div className="px-6 pb-2">
                                    <p className="text-xs text-gray-400 mb-2">Quick actions:</p>
                                    <div className="flex flex-wrap gap-2">
                                        {QUICK_PROMPTS.map((item) => (
                                            <button
                                                key={item.label}
                                                onClick={() => handleQuickPrompt(item.prompt)}
                                                className={cn(
                                                    "px-3 py-1.5 text-xs rounded-full",
                                                    "bg-gray-100 dark:bg-gray-800",
                                                    "text-gray-600 dark:text-gray-300",
                                                    "hover:bg-blue-50 dark:hover:bg-blue-900/20",
                                                    "hover:text-blue-600 dark:hover:text-blue-400",
                                                    "border border-gray-200 dark:border-gray-700",
                                                    "transition-all duration-200"
                                                )}
                                            >
                                                <Sparkles className="w-3 h-3 inline mr-1.5" />
                                                {item.label}
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Input */}
                            <div className={cn(
                                "p-4 border-t border-gray-100 dark:border-gray-800",
                                "bg-gray-50 dark:bg-gray-900"
                            )}>
                                <form
                                    onSubmit={(e) => {
                                        e.preventDefault()
                                        handleSend()
                                    }}
                                    className="flex gap-3"
                                >
                                    <input
                                        ref={inputRef}
                                        value={input}
                                        onChange={(e) => setInput(e.target.value)}
                                        placeholder="Ask Dallas anything..."
                                        className={cn(
                                            "flex-1 px-4 py-3 rounded-xl",
                                            "bg-white dark:bg-gray-800",
                                            "border border-gray-200 dark:border-gray-700",
                                            "text-gray-900 dark:text-white",
                                            "placeholder:text-gray-400",
                                            "focus:outline-none focus:ring-2 focus:ring-blue-500/50",
                                            "transition-shadow"
                                        )}
                                        disabled={isLoading}
                                    />
                                    <button
                                        type="submit"
                                        disabled={!input.trim() || isLoading}
                                        className={cn(
                                            "px-4 py-3 rounded-xl",
                                            "bg-gradient-to-r from-blue-500 to-indigo-500",
                                            "text-white font-medium",
                                            "shadow-lg shadow-blue-500/25",
                                            "hover:shadow-xl hover:shadow-blue-500/30",
                                            "disabled:opacity-50 disabled:cursor-not-allowed",
                                            "transition-all duration-200"
                                        )}
                                    >
                                        {isLoading ? (
                                            <Loader2 className="w-5 h-5 animate-spin" />
                                        ) : (
                                            <Send className="w-5 h-5" />
                                        )}
                                    </button>
                                </form>
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </>
    )
}

export default DallasOrb
