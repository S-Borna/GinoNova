"use client"

/**
 * ============================================================================
 * AI WIZARD FAB - Global Floating Action Button for AI Chat
 * ============================================================================
 *
 * A beautiful floating chat button that's always visible in the bottom-right
 * corner. Expands into a full chat interface when clicked.
 *
 * Features:
 * - Floating button with pulse animation
 * - Expandable chat panel
 * - Context-aware (knows which page you're on)
 * - Persistent across page navigation
 * - Real-time AI responses
 *
 * @phase AI-WIZARD-FAS-1
 */

import { useState, useRef, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
    Bot,
    X,
    Send,
    Sparkles,
    Loader2,
    Minimize2,
    Maximize2,
    MessageCircle,
    Trash2,
} from "lucide-react"
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

interface AIWizardFABProps {
    className?: string
}

/* ============================================================================
   CONSTANTS
   ============================================================================ */

const WELCOME_MESSAGE: Message = {
    id: "welcome",
    role: "assistant",
    content: "Hey! 🧙‍♂️ I'm your DevOps Wizard. Ask me anything about Linux, Docker, Kubernetes, AWS, or any topic on the platform!",
    timestamp: new Date(),
}

const QUICK_ACTIONS = [
    { label: "Explain this module", prompt: "Can you explain what this module is about?" },
    { label: "Give me a hint", prompt: "I'm stuck. Can you give me a hint?" },
    { label: "What's next?", prompt: "What should I learn next?" },
]

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
                <div className="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0">
                    <Bot className="w-4 h-4 text-white" />
                </div>
            )}
            <div
                className={cn(
                    "max-w-[80%] rounded-2xl px-4 py-3",
                    isAssistant
                        ? "bg-white/10 text-white rounded-tl-sm"
                        : "bg-indigo-500 text-white rounded-tr-sm"
                )}
            >
                <p className="text-sm whitespace-pre-wrap">{message.content}</p>
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
            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center flex-shrink-0">
                <Bot className="w-4 h-4 text-white" />
            </div>
            <div className="bg-white/10 rounded-2xl rounded-tl-sm px-4 py-3 flex gap-1">
                <motion.div
                    animate={{ y: [0, -4, 0] }}
                    transition={{ duration: 0.5, repeat: Infinity, delay: 0 }}
                    className="w-2 h-2 bg-indigo-400 rounded-full"
                />
                <motion.div
                    animate={{ y: [0, -4, 0] }}
                    transition={{ duration: 0.5, repeat: Infinity, delay: 0.1 }}
                    className="w-2 h-2 bg-indigo-400 rounded-full"
                />
                <motion.div
                    animate={{ y: [0, -4, 0] }}
                    transition={{ duration: 0.5, repeat: Infinity, delay: 0.2 }}
                    className="w-2 h-2 bg-indigo-400 rounded-full"
                />
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function AIWizardFAB({ className }: AIWizardFABProps) {
    const [isOpen, setIsOpen] = useState(false)
    const [isExpanded, setIsExpanded] = useState(false)
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
            inputRef.current?.focus()
        }
    }, [isOpen])

    // Get current page context
    const getContext = () => {
        const path = pathname || "/"
        if (path.includes("/modules/")) {
            return { type: "module", path }
        }
        if (path.includes("/tasks/")) {
            return { type: "task", path }
        }
        if (path.includes("/dashboard")) {
            return { type: "dashboard", path }
        }
        return { type: "general", path }
    }

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
            // Call AI API
            const response = await fetch("/api/ai/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: userMessage.content,
                    context: getContext(),
                }),
            })

            if (!response.ok) {
                throw new Error("Failed to get response")
            }

            const data = await response.json()

            const assistantMessage: Message = {
                id: (Date.now() + 1).toString(),
                role: "assistant",
                content: data.response || "I'm sorry, I couldn't process that. Please try again.",
                timestamp: new Date(),
            }

            setMessages((prev) => [...prev, assistantMessage])
        } catch (error) {
            // Fallback response
            const fallbackMessage: Message = {
                id: (Date.now() + 1).toString(),
                role: "assistant",
                content: "I'm having trouble connecting right now. Please try again in a moment. 🔧",
                timestamp: new Date(),
            }
            setMessages((prev) => [...prev, fallbackMessage])
        } finally {
            setIsLoading(false)
        }
    }

    const handleQuickAction = (prompt: string) => {
        setInput(prompt)
        handleSend()
    }

    const clearChat = () => {
        setMessages([WELCOME_MESSAGE])
    }

    return (
        <>
            {/* FAB Button */}
            <AnimatePresence>
                {!isOpen && (
                    <motion.button
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        exit={{ scale: 0, opacity: 0 }}
                        whileHover={{ scale: 1.1 }}
                        whileTap={{ scale: 0.9 }}
                        onClick={() => setIsOpen(true)}
                        className={cn(
                            "fixed bottom-6 right-6 z-50",
                            "w-14 h-14 rounded-full",
                            "bg-gradient-to-br from-indigo-500 to-purple-600",
                            "shadow-lg shadow-indigo-500/30",
                            "flex items-center justify-center",
                            "transition-all",
                            className
                        )}
                    >
                        {/* Pulse ring */}
                        <motion.div
                            animate={{
                                scale: [1, 1.5, 1],
                                opacity: [0.5, 0, 0.5],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                            className="absolute inset-0 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600"
                        />
                        <Bot className="w-6 h-6 text-white relative z-10" />
                    </motion.button>
                )}
            </AnimatePresence>

            {/* Chat Panel */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: 20, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 20, scale: 0.95 }}
                        className={cn(
                            "fixed z-50 bg-gray-900/95 backdrop-blur-xl border border-white/10 shadow-2xl",
                            "flex flex-col",
                            isExpanded
                                ? "inset-4 rounded-3xl"
                                : "bottom-6 right-6 w-96 h-[600px] rounded-3xl"
                        )}
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between p-4 border-b border-white/10">
                            <div className="flex items-center gap-3">
                                <div className="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                                    <Bot className="w-5 h-5 text-white" />
                                </div>
                                <div>
                                    <h3 className="font-semibold text-white">DevOps Wizard</h3>
                                    <p className="text-xs text-gray-400">Always here to help</p>
                                </div>
                            </div>
                            <div className="flex items-center gap-2">
                                <button
                                    onClick={clearChat}
                                    className="p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5"
                                    title="Clear chat"
                                >
                                    <Trash2 className="w-4 h-4" />
                                </button>
                                <button
                                    onClick={() => setIsExpanded(!isExpanded)}
                                    className="p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5"
                                >
                                    {isExpanded ? (
                                        <Minimize2 className="w-4 h-4" />
                                    ) : (
                                        <Maximize2 className="w-4 h-4" />
                                    )}
                                </button>
                                <button
                                    onClick={() => setIsOpen(false)}
                                    className="p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-white/5"
                                >
                                    <X className="w-4 h-4" />
                                </button>
                            </div>
                        </div>

                        {/* Messages */}
                        <div className="flex-1 overflow-y-auto p-4 space-y-4">
                            {messages.map((message) => (
                                <ChatMessage key={message.id} message={message} />
                            ))}
                            {isLoading && <TypingIndicator />}
                            <div ref={messagesEndRef} />
                        </div>

                        {/* Quick Actions */}
                        {messages.length <= 2 && (
                            <div className="px-4 pb-2">
                                <div className="flex flex-wrap gap-2">
                                    {QUICK_ACTIONS.map((action) => (
                                        <button
                                            key={action.label}
                                            onClick={() => handleQuickAction(action.prompt)}
                                            className="px-3 py-1.5 text-xs bg-white/5 hover:bg-white/10 text-gray-300 rounded-full transition-colors border border-white/10"
                                        >
                                            {action.label}
                                        </button>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Input */}
                        <div className="p-4 border-t border-white/10">
                            <form
                                onSubmit={(e) => {
                                    e.preventDefault()
                                    handleSend()
                                }}
                                className="flex gap-2"
                            >
                                <Input
                                    ref={inputRef}
                                    value={input}
                                    onChange={(e) => setInput(e.target.value)}
                                    placeholder="Ask me anything..."
                                    className="flex-1 bg-white/5 border-white/10 text-white placeholder:text-gray-500 rounded-xl"
                                    disabled={isLoading}
                                />
                                <Button
                                    type="submit"
                                    disabled={!input.trim() || isLoading}
                                    className="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700 text-white rounded-xl px-4"
                                >
                                    {isLoading ? (
                                        <Loader2 className="w-4 h-4 animate-spin" />
                                    ) : (
                                        <Send className="w-4 h-4" />
                                    )}
                                </Button>
                            </form>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    )
}

export default AIWizardFAB
