"use client"

/**
 * Pulsmätning - Hur mår du idag?
 * 
 * Dallas frågar hur användaren mår och ger personlig vägledning.
 * Spara flashcards och quiz för snabb åtkomst.
 */

import * as React from "react"
import { useState, useEffect, useRef } from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"
import {
    Send,
    BookOpen,
    Target,
    Focus,
    Bookmark,
    BookmarkX,
    Sparkles,
    Heart,
    TrendingUp,
    Clock,
    Brain,
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

/* ============================================================================
   DALLAS CHAT COMPONENT
   ============================================================================ */

interface Message {
    role: "assistant" | "user"
    content: string
}

function DallasChat({ userName }: { userName: string }) {
    const [messages, setMessages] = useState<Message[]>([
        {
            role: "assistant",
            content: `Hur mår du idag, ${userName || "du"}? 🫶`
        }
    ])
    const [input, setInput] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const messagesEndRef = useRef<HTMLDivElement>(null)

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }

    useEffect(() => {
        scrollToBottom()
    }, [messages])

    async function sendMessage() {
        if (!input.trim() || isLoading) return

        const userMessage = input.trim()
        setInput("")
        setMessages(prev => [...prev, { role: "user", content: userMessage }])
        setIsLoading(true)

        try {
            // Skicka till backend Dallas endpoint (använder billig GPT)
            const res = await fetch(`${API_BASE_URL}/api/dallas/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: userMessage,
                    context: "pulse_check",
                    user_name: userName
                })
            })

            if (res.ok) {
                const data = await res.json()
                setMessages(prev => [...prev, { 
                    role: "assistant", 
                    content: data.response || "Jag förstår. Berätta mer! 💜"
                }])
            } else {
                // Fallback om API inte finns
                const fallbackResponses = [
                    `Det låter som att du har mycket på gång! Ta det lugnt och kom ihåg att vila är också viktigt för inlärning. 🌟`,
                    `Tack för att du delar! DevOps är en resa, inte en sprint. Du gör framsteg varje dag! 💪`,
                    `Jag hör dig! Ska vi fokusera på något specifikt idag? Kanske några flashcards för att komma igång? 📚`,
                    `Det är helt okej att känna så. Vill du att jag rekommenderar något att börja med? 🎯`
                ]
                const randomResponse = fallbackResponses[Math.floor(Math.random() * fallbackResponses.length)]
                setMessages(prev => [...prev, { role: "assistant", content: randomResponse }])
            }
        } catch {
            setMessages(prev => [...prev, { 
                role: "assistant", 
                content: "Jag är här för dig! Berätta mer om hur du känner dig. 💜"
            }])
        } finally {
            setIsLoading(false)
        }
    }

    function handleKeyPress(e: React.KeyboardEvent) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault()
            sendMessage()
        }
    }

    return (
        <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl overflow-hidden">
            {/* Dallas Header */}
            <div className="bg-gradient-to-r from-zinc-800/80 to-zinc-900/80 p-4 border-b border-zinc-700/50">
                <div className="flex items-center gap-3">
                    <div className="relative">
                        <div className="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-blue-600 flex items-center justify-center">
                            <span className="text-2xl">🐴</span>
                        </div>
                        <div className="absolute -bottom-0.5 -right-0.5 w-4 h-4 bg-emerald-500 rounded-full border-2 border-zinc-900" />
                    </div>
                    <div>
                        <h3 className="font-semibold text-white">Dallas</h3>
                        <p className="text-xs text-zinc-400">Din DevOps-guide</p>
                    </div>
                    <div className="ml-auto">
                        <span className="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-1 rounded-full flex items-center gap-1">
                            <span className="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-pulse" />
                            Online
                        </span>
                    </div>
                </div>
            </div>

            {/* Messages */}
            <div className="h-64 overflow-y-auto p-4 space-y-4">
                {messages.map((msg, i) => (
                    <div
                        key={i}
                        className={cn(
                            "flex gap-3",
                            msg.role === "user" ? "justify-end" : "justify-start"
                        )}
                    >
                        {msg.role === "assistant" && (
                            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500/30 to-blue-600/30 flex items-center justify-center shrink-0">
                                <span className="text-sm">🐴</span>
                            </div>
                        )}
                        <div className={cn(
                            "max-w-[80%] p-3 rounded-2xl text-sm",
                            msg.role === "user"
                                ? "bg-purple-600/30 text-white rounded-br-md"
                                : "bg-zinc-800/80 text-zinc-200 rounded-bl-md"
                        )}>
                            {msg.content}
                        </div>
                    </div>
                ))}
                {isLoading && (
                    <div className="flex gap-3">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500/30 to-blue-600/30 flex items-center justify-center">
                            <span className="text-sm">🐴</span>
                        </div>
                        <div className="bg-zinc-800/80 p-3 rounded-2xl rounded-bl-md">
                            <div className="flex gap-1">
                                <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input */}
            <div className="p-4 border-t border-zinc-800">
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="Skriv till Dallas..."
                        className={cn(
                            "flex-1 bg-zinc-800/50 border border-zinc-700 rounded-xl px-4 py-3",
                            "text-sm text-white placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50"
                        )}
                    />
                    <button
                        onClick={sendMessage}
                        disabled={!input.trim() || isLoading}
                        className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-r from-purple-600 to-blue-600",
                            "hover:from-purple-500 hover:to-blue-500",
                            "disabled:opacity-50 disabled:cursor-not-allowed",
                            "transition-all"
                        )}
                    >
                        <Send className="w-5 h-5 text-white" />
                    </button>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PULSE PAGE
   ============================================================================ */

export default function PulsePage() {
    const { user } = useAuth()
    const userName = user?.email?.split("@")[0] || "du"
    const displayName = userName.charAt(0).toUpperCase() + userName.slice(1)

    // Placeholder för sparade flashcards/quiz
    const [savedItems, setSavedItems] = useState<any[]>([])

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-6">
            <div className="max-w-4xl mx-auto space-y-6">
                
                {/* ============================================================
                    HEADER - Pulsmätning
                    ============================================================ */}
                <div className={cn(
                    "relative overflow-hidden rounded-2xl p-6",
                    "bg-gradient-to-r from-purple-600/30 via-pink-500/20 to-orange-500/20",
                    "border border-purple-500/30"
                )}>
                    <div className="flex items-center gap-4">
                        <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
                            <Heart className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold">
                                Ta en egen pulsmätning, {displayName}!
                            </h1>
                            <p className="text-zinc-400 text-sm">
                                Planera din DevOps-resa, sätt upp mål och följ din progress
                            </p>
                        </div>
                    </div>
                </div>

                {/* ============================================================
                    DALLAS CHAT
                    ============================================================ */}
                <DallasChat userName={displayName} />

                {/* ============================================================
                    MINA SPARADE FLASHCARDS OCH QUIZ
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-amber-500/30 rounded-2xl p-6">
                    <div className="flex items-center gap-3 mb-4">
                        <Bookmark className="w-5 h-5 text-amber-400" />
                        <h2 className="text-lg font-semibold">Mina Flashcards och Quiz</h2>
                    </div>

                    {savedItems.length === 0 ? (
                        <div className="text-center py-8">
                            <BookmarkX className="w-12 h-12 text-zinc-600 mx-auto mb-3" />
                            <p className="text-zinc-500">Inga sparade flashcards eller quiz</p>
                            <p className="text-sm text-zinc-600 flex items-center justify-center gap-1 mt-1">
                                <Bookmark className="w-4 h-4 text-amber-500" />
                                Stjärnmarkera flashcards och quiz i Studyroom
                            </p>
                        </div>
                    ) : (
                        <div className="space-y-2">
                            {savedItems.map((item, i) => (
                                <div 
                                    key={i}
                                    className="flex items-center gap-3 p-3 bg-zinc-800/50 rounded-xl hover:bg-zinc-800 transition-colors cursor-pointer"
                                >
                                    <BookOpen className="w-5 h-5 text-purple-400" />
                                    <span className="flex-1">{item.title}</span>
                                </div>
                            ))}
                        </div>
                    )}
                </div>

                {/* ============================================================
                    SNABBKNAPPAR (3 rutor)
                    ============================================================ */}
                <div className="grid grid-cols-3 gap-4">
                    {/* Fortsätt lära */}
                    <Link
                        href="/study"
                        className={cn(
                            "flex flex-col items-center gap-3 p-6 rounded-2xl",
                            "bg-zinc-900/60 border border-zinc-800",
                            "hover:border-purple-500/50 hover:bg-zinc-900",
                            "transition-all duration-200"
                        )}
                    >
                        <div className="w-14 h-14 rounded-2xl bg-purple-500/20 flex items-center justify-center">
                            <BookOpen className="w-7 h-7 text-purple-400" />
                        </div>
                        <span className="text-sm font-medium text-zinc-300">Fortsätt lära</span>
                    </Link>

                    {/* Se progress */}
                    <Link
                        href="/progress"
                        className={cn(
                            "flex flex-col items-center gap-3 p-6 rounded-2xl",
                            "bg-zinc-900/60 border border-zinc-800",
                            "hover:border-amber-500/50 hover:bg-zinc-900",
                            "transition-all duration-200"
                        )}
                    >
                        <div className="w-14 h-14 rounded-2xl bg-amber-500/20 flex items-center justify-center">
                            <TrendingUp className="w-7 h-7 text-amber-400" />
                        </div>
                        <span className="text-sm font-medium text-zinc-300">Se progress</span>
                    </Link>

                    {/* Fokusläge */}
                    <Link
                        href="/focus"
                        className={cn(
                            "flex flex-col items-center gap-3 p-6 rounded-2xl",
                            "bg-zinc-900/60 border border-zinc-800",
                            "hover:border-emerald-500/50 hover:bg-zinc-900",
                            "transition-all duration-200"
                        )}
                    >
                        <div className="w-14 h-14 rounded-2xl bg-emerald-500/20 flex items-center justify-center">
                            <Focus className="w-7 h-7 text-emerald-400" />
                        </div>
                        <span className="text-sm font-medium text-zinc-300">Fokusläge</span>
                    </Link>
                </div>

                {/* ============================================================
                    REKOMMENDERAT FÖR DIG
                    ============================================================ */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6">
                    <div className="flex items-center gap-3 mb-4">
                        <Sparkles className="w-5 h-5 text-purple-400" />
                        <h2 className="text-lg font-semibold">Rekommenderat för dig</h2>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                        <Link
                            href="/study/linux-mastery/flashcards"
                            className="flex items-center gap-3 p-4 bg-zinc-800/50 rounded-xl hover:bg-zinc-800 transition-colors"
                        >
                            <div className="w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center">
                                <BookOpen className="w-5 h-5 text-purple-400" />
                            </div>
                            <div className="flex-1">
                                <p className="font-medium text-sm">Linux Flashcards</p>
                                <p className="text-xs text-zinc-500">90 kort • Grundläggande</p>
                            </div>
                        </Link>

                        <Link
                            href="/study/docker-mastery/quiz"
                            className="flex items-center gap-3 p-4 bg-zinc-800/50 rounded-xl hover:bg-zinc-800 transition-colors"
                        >
                            <div className="w-10 h-10 rounded-lg bg-blue-500/20 flex items-center justify-center">
                                <Brain className="w-5 h-5 text-blue-400" />
                            </div>
                            <div className="flex-1">
                                <p className="font-medium text-sm">Docker Quiz</p>
                                <p className="text-xs text-zinc-500">60 frågor • Blandad</p>
                            </div>
                        </Link>
                    </div>
                </div>

            </div>
        </div>
    )
}
