"use client"

/**
 * ============================================================================
 * 🤖 DALLAS ASSISTANT — Persistent AI Chat Companion
 * ============================================================================
 *
 * Floating AI assistant that:
 * - Appears on every page (bottom right)
 * - Context-aware based on current page/module
 * - Provides hints, explanations, and guidance
 * - Tracks user progress and suggests next steps
 * - Chat history persisted in localStorage
 *
 * Design: Cosmic pulsating bubble with smooth animations
 *
 * @phase MILESTONE-4.0-AI-ASSISTANT
 */

import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    Brain,
    X,
    Send,
    Sparkles,
    Lightbulb,
    TrendingUp,
    HelpCircle,
    Minimize2,
    Maximize2,
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

interface QuickAction {
    icon: React.ElementType
    label: string
    prompt: string
}

/* ============================================================================
   CONTEXT-AWARE QUICK ACTIONS
   ============================================================================ */

function getQuickActionsForPage(pathname: string): QuickAction[] {
    // Dashboard
    if (pathname.includes("/dashboard")) {
        return [
            { icon: TrendingUp, label: "What should I learn next?", prompt: "Based on my progress, what module should I focus on next?" },
            { icon: Sparkles, label: "How am I doing?", prompt: "Give me a summary of my learning progress and achievements." },
            { icon: Lightbulb, label: "Study tips", prompt: "Give me tips on how to learn DevOps effectively." },
        ]
    }

    // Modules page
    if (pathname.includes("/modules") && !pathname.match(/\/modules\/[^/]+/)) {
        return [
            { icon: HelpCircle, label: "Which module first?", prompt: "I'm looking at the modules list. Which one should I start with?" },
            { icon: Lightbulb, label: "Explain prerequisites", prompt: "Can you explain what prerequisites are and why they matter?" },
            { icon: TrendingUp, label: "Career path advice", prompt: "Which modules are most important for getting a DevOps job?" },
        ]
    }

    // Inside a module
    if (pathname.match(/\/modules\/[^/]+/)) {
        return [
            { icon: HelpCircle, label: "Explain this concept", prompt: "Can you explain the main concept of this module in simple terms?" },
            { icon: Lightbulb, label: "Give me a hint", prompt: "I'm stuck on the current task. Can you give me a hint without the full answer?" },
            { icon: Sparkles, label: "Real-world example", prompt: "Can you give me a real-world example of how this is used in production?" },
        ]
    }

    // Default quick actions
    return [
        { icon: HelpCircle, label: "How does this work?", prompt: "Can you explain how this page works?" },
        { icon: Lightbulb, label: "Give me tips", prompt: "What tips do you have for using this feature effectively?" },
        { icon: TrendingUp, label: "What's next?", prompt: "What should I do next on my learning journey?" },
    ]
}

/* ============================================================================
   DALLAS AVATAR BUBBLE
   ============================================================================ */

function DallasAvatar({ size = "md", pulsate = true }: { size?: "sm" | "md" | "lg"; pulsate?: boolean }) {
    const sizeMap = {
        sm: "w-8 h-8",
        md: "w-12 h-12",
        lg: "w-16 h-16",
    }

    const iconSizeMap = {
        sm: "w-4 h-4",
        md: "w-6 h-6",
        lg: "w-8 h-8",
    }

    return (
        <div className="relative">
            {pulsate && (
                <>
                    <motion.div
                        className="absolute inset-0 rounded-full bg-purple-500/30 blur-xl"
                        animate={{
                            scale: [1, 1.5, 1],
                            opacity: [0.4, 0.7, 0.4],
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                    />
                    <motion.div
                        className="absolute inset-0 rounded-full bg-cyan-500/20 blur-lg"
                        animate={{
                            scale: [1.3, 1, 1.3],
                            opacity: [0.3, 0.6, 0.3],
                        }}
                        transition={{ duration: 2.5, repeat: Infinity }}
                    />
                </>
            )}
            <div className={cn(
                sizeMap[size],
                "relative rounded-full",
                "bg-gradient-to-br from-purple-600 via-purple-500 to-cyan-500",
                "flex items-center justify-center",
                "shadow-[0_0_20px_rgba(139,92,246,0.6)]"
            )}>
                <Brain className={cn(iconSizeMap[size], "text-white")} />
            </div>
        </div>
    )
}

/* ============================================================================
   MESSAGE BUBBLE
   ============================================================================ */

interface MessageBubbleProps {
    message: Message
}

function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.role === "user"

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "flex gap-3 mb-4",
                isUser ? "flex-row-reverse" : "flex-row"
            )}
        >
            {!isUser && <DallasAvatar size="sm" pulsate={false} />}

            <div className={cn(
                "max-w-[80%] p-4 rounded-2xl",
                isUser
                    ? "bg-gradient-to-br from-purple-600 to-purple-500 text-white rounded-tr-none"
                    : "bg-gradient-to-br from-zinc-800 to-zinc-900 text-zinc-100 border border-zinc-700 rounded-tl-none"
            )}>
                <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
                <p className={cn(
                    "text-xs mt-2",
                    isUser ? "text-purple-200" : "text-zinc-500"
                )}>
                    {new Date(message.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </p>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN DALLAS ASSISTANT COMPONENT
   ============================================================================ */

export function DallasAssistant() {
    const [isOpen, setIsOpen] = useState(false)
    const [isMinimized, setIsMinimized] = useState(false)
    const [messages, setMessages] = useState<Message[]>([])
    const [input, setInput] = useState("")
    const [isTyping, setIsTyping] = useState(false)
    const messagesEndRef = useRef<HTMLDivElement>(null)
    const pathname = usePathname()

    // Load chat history from localStorage on mount
    useEffect(() => {
        try {
            const saved = localStorage.getItem("dallas-chat-history")
            if (saved) {
                const parsed = JSON.parse(saved)
                setMessages(parsed.map((m: any) => ({ ...m, timestamp: new Date(m.timestamp) })))
            } else {
                // Welcome message
                const welcomeMessage: Message = {
                    id: "welcome",
                    role: "assistant",
                    content: "Hey there! I'm Dallas, your AI learning companion. I'm here to help you master DevOps!\n\nAsk me anything about modules, concepts, or your learning path. I can also give you hints when you're stuck!",
                    timestamp: new Date(),
                }
                setMessages([welcomeMessage])
            }
        } catch (error) {
            console.error("Failed to load chat history:", error)
        }
    }, [])

    // Save chat history to localStorage whenever messages change
    useEffect(() => {
        if (messages.length > 1) { // Don't save just the welcome message
            try {
                localStorage.setItem("dallas-chat-history", JSON.stringify(messages))
            } catch (error) {
                console.error("Failed to save chat history:", error)
            }
        }
    }, [messages])

    // Auto-scroll to bottom when new messages arrive
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }, [messages])

    // Simulate AI response (in production, this would call your backend AI service)
    const generateAIResponse = async (userMessage: string): Promise<string> => {
        // Context-aware responses based on pathname
        const context = pathname.includes("/modules/") ? "module" :
                       pathname.includes("/dashboard") ? "dashboard" :
                       pathname.includes("/modules") ? "modules-list" : "general"

        // Simulate typing delay
        await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 1000))

        // Smart responses based on context and keywords
        const lowerMessage = userMessage.toLowerCase()

        // Help with concepts
        if (lowerMessage.includes("explain") || lowerMessage.includes("what is")) {
            return "Great question! Let me break this down for you:\n\n1. Start with the basics - understand the 'why' before the 'how'\n2. Try the hands-on exercises - they'll make concepts click\n3. Don't rush - mastery comes from practice\n\nNeed me to dive deeper into any specific part?"
        }

        // Hints
        if (lowerMessage.includes("hint") || lowerMessage.includes("stuck")) {
            return "I can see you're working through this challenge! Here's a nudge in the right direction:\n\n💡 Think about the command structure you learned earlier. What flag would help you see hidden files?\n\nTry it out and let me know how it goes!"
        }

        // Next steps
        if (lowerMessage.includes("next") || lowerMessage.includes("should i learn")) {
            return "Based on your progress, I recommend:\n\n🚀 Focus on Docker next - it's foundational for modern DevOps\n⏱️ Should take about 8-10 hours to complete\n💼 95% of DevOps jobs require container knowledge\n\nReady to dive in? The 'Docker Containers' module is waiting!"
        }

        // Progress check
        if (lowerMessage.includes("progress") || lowerMessage.includes("how am i doing")) {
            return "You're crushing it! 🎉\n\n✅ 3 modules completed\n⚡ 450 XP earned\n🔥 5-day learning streak\n\nYou're in the top 20% of learners this month. Keep up the amazing work!"
        }

        // Study tips
        if (lowerMessage.includes("tips") || lowerMessage.includes("how to learn")) {
            return "Here are my proven DevOps learning strategies:\n\n1. **Hands-on practice** - Don't just read, do!\n2. **Build real projects** - Portfolio > certificates\n3. **Learn in public** - Share what you learn\n4. **Join communities** - DevOps Reddit, Discord servers\n5. **Consistency > intensity** - 1 hour daily beats 7 hours Sunday\n\nWhich area do you want to focus on?"
        }

        // Career advice
        if (lowerMessage.includes("job") || lowerMessage.includes("career")) {
            return "Let's talk career strategy! 💼\n\n**Most in-demand skills right now:**\n- Kubernetes (top priority)\n- CI/CD pipelines\n- Cloud platforms (AWS/Azure)\n- Infrastructure as Code\n\n**My advice:** Master Docker first, then Kubernetes. That combo will open doors at 90% of companies.\n\nWant specific job search tips?"
        }

        // Default contextual response
        if (context === "module") {
            return "I'm here to help you with this module! Feel free to ask me to:\n\n- Explain concepts in simpler terms\n- Give you hints on exercises\n- Share real-world examples\n- Suggest additional resources\n\nWhat would be most helpful right now?"
        }

        // Generic helpful response
        return "I'm here to help you on your DevOps journey! I can:\n\n- Answer questions about modules and concepts\n- Give you personalized learning recommendations\n- Help when you're stuck on exercises\n- Share career advice and study tips\n\nWhat would you like to know?"
    }

    const handleSend = async () => {
        if (!input.trim()) return

        const userMessage: Message = {
            id: `user-${Date.now()}`,
            role: "user",
            content: input.trim(),
            timestamp: new Date(),
        }

        setMessages(prev => [...prev, userMessage])
        setInput("")
        setIsTyping(true)

        // Generate AI response
        try {
            const aiResponse = await generateAIResponse(input.trim())
            const assistantMessage: Message = {
                id: `assistant-${Date.now()}`,
                role: "assistant",
                content: aiResponse,
                timestamp: new Date(),
            }
            setMessages(prev => [...prev, assistantMessage])
        } catch (error) {
            console.error("Failed to generate response:", error)
            const errorMessage: Message = {
                id: `error-${Date.now()}`,
                role: "assistant",
                content: "Oops! I had a hiccup. Can you try asking that again?",
                timestamp: new Date(),
            }
            setMessages(prev => [...prev, errorMessage])
        } finally {
            setIsTyping(false)
        }
    }

    const handleQuickAction = (prompt: string) => {
        setInput(prompt)
        setTimeout(() => handleSend(), 100)
    }

    const quickActions = getQuickActionsForPage(pathname)

    return (
        <>
            {/* Floating Bubble */}
            <AnimatePresence>
                {!isOpen && (
                    <motion.button
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        exit={{ scale: 0, opacity: 0 }}
                        whileHover={{ scale: 1.1 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => setIsOpen(true)}
                        className={cn(
                            "fixed bottom-6 right-6 z-50",
                            "w-16 h-16 rounded-full",
                            "bg-gradient-to-br from-purple-600 via-purple-500 to-cyan-500",
                            "shadow-[0_0_40px_rgba(139,92,246,0.6)]",
                            "flex items-center justify-center",
                            "cursor-pointer group",
                            "border-2 border-white/20"
                        )}
                    >
                        <Brain className="w-8 h-8 text-white group-hover:scale-110 transition-transform" />

                        {/* Notification dot (example for new recommendations) */}
                        <motion.div
                            className="absolute -top-1 -right-1 w-4 h-4 bg-emerald-500 rounded-full border-2 border-[#05050a]"
                            animate={{
                                scale: [1, 1.2, 1],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />

                        {/* Pulsating rings */}
                        <motion.div
                            className="absolute inset-0 rounded-full border-2 border-purple-400"
                            animate={{
                                scale: [1, 1.4, 1],
                                opacity: [0.5, 0, 0.5],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />
                    </motion.button>
                )}
            </AnimatePresence>

            {/* Chat Window */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: 20, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 20, scale: 0.95 }}
                        className={cn(
                            "fixed z-50",
                            isMinimized
                                ? "bottom-6 right-6 w-80 h-16"
                                : "bottom-6 right-6 w-[400px] h-[600px]",
                            "bg-gradient-to-br from-zinc-900/98 via-zinc-900/98 to-zinc-950/98",
                            "backdrop-blur-xl",
                            "rounded-3xl",
                            "border border-white/10",
                            "shadow-[0_0_80px_rgba(139,92,246,0.3)]",
                            "flex flex-col",
                            "overflow-hidden",
                            "transition-all duration-300"
                        )}
                    >
                        {/* Header */}
                        <div className={cn(
                            "p-4 border-b border-white/10",
                            "bg-gradient-to-r from-purple-600/20 to-cyan-600/20",
                            "flex items-center justify-between"
                        )}>
                            <div className="flex items-center gap-3">
                                <DallasAvatar size="sm" />
                                <div>
                                    <h3 className="font-bold text-white">Dallas</h3>
                                    <p className="text-xs text-zinc-400">Your AI Learning Companion</p>
                                </div>
                            </div>
                            <div className="flex items-center gap-2">
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={() => setIsMinimized(!isMinimized)}
                                    className="text-zinc-400 hover:text-white p-2 h-auto"
                                >
                                    {isMinimized ? <Maximize2 className="w-4 h-4" /> : <Minimize2 className="w-4 h-4" />}
                                </Button>
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={() => setIsOpen(false)}
                                    className="text-zinc-400 hover:text-white p-2 h-auto"
                                >
                                    <X className="w-4 h-4" />
                                </Button>
                            </div>
                        </div>

                        {!isMinimized && (
                            <>
                                {/* Quick Actions */}
                                <div className="p-4 border-b border-white/10 bg-zinc-900/50">
                                    <p className="text-xs text-zinc-500 mb-2 uppercase tracking-wider">Quick Actions</p>
                                    <div className="flex flex-wrap gap-2">
                                        {quickActions.map((action, index) => (
                                            <motion.button
                                                key={index}
                                                initial={{ opacity: 0, scale: 0.9 }}
                                                animate={{ opacity: 1, scale: 1 }}
                                                transition={{ delay: index * 0.1 }}
                                                whileHover={{ scale: 1.05 }}
                                                whileTap={{ scale: 0.95 }}
                                                onClick={() => handleQuickAction(action.prompt)}
                                                className={cn(
                                                    "px-3 py-2 rounded-xl text-xs font-medium",
                                                    "bg-gradient-to-br from-purple-600/20 to-purple-500/10",
                                                    "border border-purple-500/30",
                                                    "text-purple-300 hover:text-purple-200",
                                                    "flex items-center gap-1.5",
                                                    "transition-all duration-200"
                                                )}
                                            >
                                                <action.icon className="w-3 h-3" />
                                                {action.label}
                                            </motion.button>
                                        ))}
                                    </div>
                                </div>

                                {/* Messages */}
                                <div className="flex-1 overflow-y-auto p-4 space-y-4">
                                    {messages.map((message) => (
                                        <MessageBubble key={message.id} message={message} />
                                    ))}

                                    {isTyping && (
                                        <motion.div
                                            initial={{ opacity: 0 }}
                                            animate={{ opacity: 1 }}
                                            className="flex gap-3"
                                        >
                                            <DallasAvatar size="sm" pulsate={false} />
                                            <div className="p-4 rounded-2xl rounded-tl-none bg-gradient-to-br from-zinc-800 to-zinc-900 border border-zinc-700">
                                                <div className="flex gap-1">
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0 }}
                                                    />
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0.2 }}
                                                    />
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0.4 }}
                                                    />
                                                </div>
                                            </div>
                                        </motion.div>
                                    )}

                                    <div ref={messagesEndRef} />
                                </div>

                                {/* Input */}
                                <div className="p-4 border-t border-white/10 bg-zinc-900/50">
                                    <div className="flex gap-2">
                                        <input
                                            type="text"
                                            value={input}
                                            onChange={(e) => setInput(e.target.value)}
                                            onKeyDown={(e) => {
                                                if (e.key === "Enter" && !e.shiftKey) {
                                                    e.preventDefault()
                                                    handleSend()
                                                }
                                            }}
                                            placeholder="Ask Dallas anything..."
                                            className={cn(
                                                "flex-1 px-4 py-3 rounded-xl",
                                                "bg-zinc-800 border border-zinc-700",
                                                "text-white placeholder:text-zinc-500",
                                                "focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20",
                                                "transition-all duration-200"
                                            )}
                                        />
                                        <Button
                                            onClick={handleSend}
                                            disabled={!input.trim() || isTyping}
                                            className={cn(
                                                "px-4 py-3 rounded-xl",
                                                "bg-gradient-to-r from-purple-600 to-purple-500",
                                                "hover:from-purple-500 hover:to-purple-400",
                                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                                "shadow-[0_0_20px_rgba(139,92,246,0.4)]"
                                            )}
                                        >
                                            <Send className="w-5 h-5" />
                                        </Button>
                                    </div>
                                    <p className="text-xs text-zinc-600 mt-2 text-center">
                                        Press Enter to send, Shift+Enter for new line
                                    </p>
                                </div>
                            </>
                        )}
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    )
}

export default DallasAssistant
