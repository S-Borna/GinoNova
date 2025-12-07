"use client"

/**
 * Pulsmätning - Hur mår du idag?
 *
 * Dallas frågar hur användaren mår och ger personlig vägledning.
 * Spara flashcards och quiz för snabb åtkomst.
 * Session timer med veckohistorik.
 */

import * as React from "react"
import { useState, useEffect, useRef } from "react"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"
import { useSessionTimer } from "@/hooks/useSessionTimer"
import { useFavorites, FavoriteItem } from "@/hooks/useFavorites"
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
    Star,
    X,
    Trash2,
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
   WEEKLY SESSION CARD
   ============================================================================ */

function WeeklySessionCard() {
    const { weeklyTotalSeconds, todaySeconds, currentSessionSeconds, formatTimeShort, weekHistory } = useSessionTimer()

    // Beräkna dagarna i veckan
    const weekDays = ["Mån", "Tis", "Ons", "Tor", "Fre", "Lör", "Sön"]
    const today = new Date()
    const currentDay = today.getDay() === 0 ? 6 : today.getDay() - 1 // Måndag = 0

    return (
        <div className="bg-zinc-900/60 border border-emerald-500/30 rounded-2xl p-6">
            <div className="flex items-center gap-3 mb-4">
                <Clock className="w-5 h-5 text-emerald-400" />
                <h2 className="text-lg font-semibold">Veckans studietid</h2>
            </div>

            {/* Total tid denna vecka */}
            <div className="text-center mb-6">
                <p className="text-4xl font-bold text-emerald-400 font-mono">
                    {formatTimeShort(weeklyTotalSeconds)}
                </p>
                <p className="text-sm text-zinc-500 mt-1">denna vecka</p>
            </div>

            {/* Dagars aktivitet */}
            <div className="flex justify-between gap-1 mb-4">
                {weekDays.map((day, i) => (
                    <div key={day} className="flex flex-col items-center gap-1">
                        <div className={cn(
                            "w-8 h-8 rounded-lg flex items-center justify-center text-xs",
                            i === currentDay
                                ? "bg-emerald-500 text-white font-bold"
                                : i < currentDay
                                    ? "bg-emerald-500/30 text-emerald-400"
                                    : "bg-zinc-800 text-zinc-600"
                        )}>
                            {day[0]}
                        </div>
                    </div>
                ))}
            </div>

            {/* Idag och session */}
            <div className="grid grid-cols-2 gap-3 pt-4 border-t border-zinc-800">
                <div className="text-center">
                    <p className="text-lg font-semibold text-white">{formatTimeShort(todaySeconds)}</p>
                    <p className="text-xs text-zinc-500">idag</p>
                </div>
                <div className="text-center">
                    <p className="text-lg font-semibold text-purple-400">{formatTimeShort(currentSessionSeconds)}</p>
                    <p className="text-xs text-zinc-500">denna session</p>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   FAVORITES CARD
   ============================================================================ */

function FavoritesCard() {
    const { favorites, removeFavorite } = useFavorites()

    return (
        <div className="bg-zinc-900/60 border border-amber-500/30 rounded-2xl p-6">
            <div className="flex items-center gap-3 mb-4">
                <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
                <h2 className="text-lg font-semibold">Mina Flashcards och Quiz</h2>
                {favorites.length > 0 && (
                    <span className="ml-auto text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full">
                        {favorites.length}
                    </span>
                )}
            </div>

            {favorites.length === 0 ? (
                <div className="text-center py-6">
                    <BookmarkX className="w-10 h-10 text-zinc-600 mx-auto mb-2" />
                    <p className="text-zinc-500 text-sm">Inga sparade favoriter</p>
                    <p className="text-xs text-zinc-600 flex items-center justify-center gap-1 mt-1">
                        <Star className="w-3 h-3 text-amber-500" />
                        Stjärnmarkera i Studyroom
                    </p>
                </div>
            ) : (
                <div className="space-y-2 max-h-64 overflow-y-auto">
                    {favorites.map((item) => (
                        <div
                            key={item.id}
                            className="group flex items-center gap-2 p-2 bg-zinc-800/50 rounded-xl hover:bg-zinc-800 transition-colors"
                        >
                            {item.type === "flashcard" ? (
                                <BookOpen className="w-4 h-4 text-purple-400 shrink-0" />
                            ) : (
                                <Brain className="w-4 h-4 text-blue-400 shrink-0" />
                            )}
                            <span className="font-medium text-sm text-amber-300">{item.customName}</span>
                            <span className="text-xs text-zinc-500 truncate flex-1">{item.moduleTitle}</span>
                            <button
                                onClick={() => removeFavorite(item.id)}
                                className="opacity-0 group-hover:opacity-100 p-1 hover:bg-red-500/20 rounded transition-all"
                            >
                                <Trash2 className="w-3 h-3 text-red-400" />
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    )
}

/* ============================================================================
   MAIN PULSE PAGE
   ============================================================================ */

export default function PulsePage() {
    const { user } = useAuth()
    // Extrahera förnamn från full_name eller email
    const fullName = user?.full_name || user?.email?.split("@")[0] || "du"
    const firstName = fullName.split(" ")[0] // Ta bara förnamnet
    const displayName = firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase()

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
                                Pulsmätning, {displayName}!
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
                    VECKANS STUDIETID + MINA FAVORITER (side by side)
                    ============================================================ */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <WeeklySessionCard />
                    <FavoritesCard />
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
