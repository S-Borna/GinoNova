"use client"

/**
 * ============================================================================
 * PULSMÄTNING - Hur mår du idag? — COSMIC EDITION 🌌
 * ============================================================================
 *
 * COSMIC DESIGN:
 * - Deep space background (#05050a)
 * - Multi-layered aurora orbs
 * - Pulsating heart animations
 * - Netflix-smooth animations
 *
 * @phase MILESTONE-2.0-COSMIC
 */

import * as React from "react"
import { useState, useEffect, useRef, useMemo } from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion } from "framer-motion"
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
    Music2,
} from "lucide-react"
import { SpotifyEmbed } from "@/components/tickers/SpotifyEmbed"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
    return (
        <div className="fixed inset-0 pointer-events-none overflow-hidden">
            <div className="absolute inset-0 bg-[#05050a]" />
            <div
                className="absolute inset-0 opacity-[0.03]"
                style={{
                    backgroundImage: `
                        linear-gradient(rgba(236, 72, 153, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(236, 72, 153, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />
            <motion.div
                className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(236, 72, 153, 0.12) 0%, rgba(236, 72, 153, 0.04) 40%, transparent 70%)',
                }}
                animate={{ scale: [1, 1.1, 1], opacity: [0.5, 0.7, 0.5] }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />
            <motion.div
                className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.15, 1], opacity: [0.4, 0.6, 0.4] }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
            />
            <motion.div
                className="absolute top-1/2 right-1/4 w-[500px] h-[500px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(52, 211, 153, 0.06) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.5, 0.3] }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
            />
        </div>
    )
}

/* ============================================================================
   DALLAS CHAT COMPONENT
   ============================================================================ */

interface Message {
    role: "assistant" | "user"
    content: string
}

function DallasChat({ userName, userId }: { userName: string; userId?: string }) {
    const [messages, setMessages] = useState<Message[]>([
        {
            role: "assistant",
            content: `Hur mår du idag, ${userName || "du"}? 🫶`
        }
    ])
    const [input, setInput] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const messagesEndRef = useRef<HTMLDivElement>(null)
    const chatContainerRef = useRef<HTMLDivElement>(null)

    const scrollToBottom = () => {
        // Only scroll within the chat container, not the whole page
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight
        }
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
                    user_name: userName,
                    user_id: userId  // For AI usage tracking
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
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
            className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border border-purple-500/30 rounded-2xl overflow-hidden shadow-[0_0_40px_rgba(139,92,246,0.1)]"
        >
            {/* Dallas Header - Cosmic */}
            <div className="bg-gradient-to-r from-purple-900/30 via-zinc-900/80 to-pink-900/20 p-4 border-b border-purple-500/20">
                <div className="flex items-center gap-3">
                    <div className="relative">
                        <motion.div
                            className="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-blue-600 flex items-center justify-center"
                            animate={{
                                boxShadow: [
                                    '0 0 15px rgba(139,92,246,0.4)',
                                    '0 0 25px rgba(139,92,246,0.6)',
                                    '0 0 15px rgba(139,92,246,0.4)'
                                ]
                            }}
                            transition={{ duration: 2.5, repeat: Infinity }}
                        >
                            <span className="text-2xl">🐺</span>
                        </motion.div>
                        <motion.div
                            className="absolute -bottom-0.5 -right-0.5 w-4 h-4 bg-emerald-500 rounded-full border-2 border-[#0a0a0f]"
                            animate={{ scale: [1, 1.2, 1] }}
                            transition={{ duration: 1.5, repeat: Infinity }}
                        />
                    </div>
                    <div>
                        <h3 className="font-semibold text-white">Dallas</h3>
                        <p className="text-xs text-purple-300/60">Din DevOps-guide</p>
                    </div>
                    <div className="ml-auto">
                        <span className="text-xs bg-emerald-500/20 text-emerald-400 px-2 py-1 rounded-full flex items-center gap-1 border border-emerald-500/30">
                            <motion.span
                                className="w-1.5 h-1.5 bg-emerald-400 rounded-full"
                                animate={{ scale: [1, 1.3, 1], opacity: [1, 0.7, 1] }}
                                transition={{ duration: 1.5, repeat: Infinity }}
                            />
                            Online
                        </span>
                    </div>
                </div>
            </div>

            {/* Messages - Cosmic chat bubbles */}
            <div
                ref={chatContainerRef}
                className="h-64 overflow-y-auto p-4 space-y-4"
            >
                {messages.map((msg, i) => (
                    <motion.div
                        key={i}
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: i * 0.05 }}
                        className={cn(
                            "flex gap-3",
                            msg.role === "user" ? "justify-end" : "justify-start"
                        )}
                    >
                        {msg.role === "assistant" && (
                            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500/30 to-blue-600/30 flex items-center justify-center shrink-0 border border-purple-500/30">
                                <span className="text-sm">🐺</span>
                            </div>
                        )}
                        <div className={cn(
                            "max-w-[80%] p-3 rounded-2xl text-sm",
                            msg.role === "user"
                                ? "bg-gradient-to-r from-purple-600/40 to-purple-500/30 text-white rounded-br-md border border-purple-500/30"
                                : "bg-zinc-800/70 text-zinc-200 rounded-bl-md border border-zinc-700/50"
                        )}>
                            {msg.content}
                        </div>
                    </motion.div>
                ))}
                {isLoading && (
                    <div className="flex gap-3">
                        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500/30 to-blue-600/30 flex items-center justify-center border border-purple-500/30">
                            <span className="text-sm">🐺</span>
                        </div>
                        <div className="bg-zinc-800/70 p-3 rounded-2xl rounded-bl-md border border-zinc-700/50">
                            <div className="flex gap-1">
                                <span className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                <span className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                <span className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                            </div>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            {/* Input - Cosmic styled */}
            <div className="p-4 border-t border-purple-500/20">
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="Skriv till Dallas..."
                        className={cn(
                            "flex-1 bg-[#0a0a0f] border border-purple-500/30 rounded-xl px-4 py-3",
                            "text-sm text-white placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/60 focus:ring-2 focus:ring-purple-500/20",
                            "transition-all duration-300"
                        )}
                    />
                    <motion.button
                        onClick={sendMessage}
                        disabled={!input.trim() || isLoading}
                        whileHover={{ scale: input.trim() && !isLoading ? 1.05 : 1 }}
                        whileTap={{ scale: input.trim() && !isLoading ? 0.95 : 1 }}
                        className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-r from-purple-600 to-blue-600",
                            "hover:from-purple-500 hover:to-blue-500",
                            "disabled:opacity-50 disabled:cursor-not-allowed",
                            "transition-all shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                        )}
                    >
                        <Send className="w-5 h-5 text-white" />
                    </motion.button>
                </div>
            </div>
        </motion.div>
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
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border border-emerald-500/30 rounded-2xl p-6 shadow-[0_0_30px_rgba(52,211,153,0.1)]"
        >
            <div className="flex items-center gap-3 mb-4">
                <motion.div
                    animate={{
                        boxShadow: ['0 0 10px rgba(52,211,153,0.3)', '0 0 20px rgba(52,211,153,0.5)', '0 0 10px rgba(52,211,153,0.3)']
                    }}
                    transition={{ duration: 2, repeat: Infinity }}
                    className="p-1 rounded-lg"
                >
                    <Clock className="w-5 h-5 text-emerald-400" />
                </motion.div>
                <h2 className="text-lg font-semibold">Veckans studietid</h2>
            </div>

            {/* Total tid denna vecka */}
            <div className="text-center mb-6">
                <motion.p
                    className="text-4xl font-bold text-emerald-400 font-mono"
                    animate={{ textShadow: ['0 0 10px rgba(52,211,153,0.3)', '0 0 20px rgba(52,211,153,0.5)', '0 0 10px rgba(52,211,153,0.3)'] }}
                    transition={{ duration: 2.5, repeat: Infinity }}
                >
                    {formatTimeShort(weeklyTotalSeconds)}
                </motion.p>
                <p className="text-sm text-zinc-500 mt-1">denna vecka</p>
            </div>

            {/* Dagars aktivitet - Cosmic styled */}
            <div className="flex justify-between gap-1 mb-4">
                {weekDays.map((day, i) => (
                    <motion.div
                        key={day}
                        className="flex flex-col items-center gap-1"
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: i * 0.05 }}
                    >
                        <div className={cn(
                            "w-8 h-8 rounded-lg flex items-center justify-center text-xs transition-all duration-300",
                            i === currentDay
                                ? "bg-emerald-500 text-white font-bold shadow-[0_0_15px_rgba(52,211,153,0.5)]"
                                : i < currentDay
                                    ? "bg-emerald-500/30 text-emerald-400 border border-emerald-500/30"
                                    : "bg-zinc-800/50 text-zinc-600 border border-zinc-700/30"
                        )}>
                            {day[0]}
                        </div>
                    </motion.div>
                ))}
            </div>

            {/* Idag och session - Cosmic */}
            <div className="grid grid-cols-2 gap-3 pt-4 border-t border-emerald-500/20">
                <div className="text-center">
                    <p className="text-lg font-semibold text-white">{formatTimeShort(todaySeconds)}</p>
                    <p className="text-xs text-zinc-500">idag</p>
                </div>
                <div className="text-center">
                    <motion.p
                        className="text-lg font-semibold text-purple-400"
                        animate={{ opacity: [1, 0.7, 1] }}
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        {formatTimeShort(currentSessionSeconds)}
                    </motion.p>
                    <p className="text-xs text-zinc-500">denna session</p>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   FAVORITES CARD
   ============================================================================ */

interface GroupedFavorites {
    moduleSlug: string
    moduleTitle: string
    flashcards: FavoriteItem[]
    quizzes: FavoriteItem[]
}

function FavoritesCard() {
    const router = useRouter()
    const { favorites, removeFavorite } = useFavorites()

    // Gruppera favoriter per modul
    const groupedFavorites = useMemo(() => {
        const groups: Record<string, GroupedFavorites> = {}

        favorites.forEach(item => {
            if (!groups[item.moduleSlug]) {
                groups[item.moduleSlug] = {
                    moduleSlug: item.moduleSlug,
                    moduleTitle: item.moduleTitle,
                    flashcards: [],
                    quizzes: []
                }
            }
            if (item.type === "flashcard") {
                groups[item.moduleSlug].flashcards.push(item)
            } else {
                groups[item.moduleSlug].quizzes.push(item)
            }
        })

        return Object.values(groups)
    }, [favorites])

    function handleGroupClick(group: GroupedFavorites, type: "flashcard" | "quiz") {
        // Navigera till flashcards eller quiz för modulen
        router.push(`/study/${group.moduleSlug}/${type === "flashcard" ? "flashcards" : "quiz"}`)
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.15, ease: [0.16, 1, 0.3, 1] }}
            className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border border-amber-500/30 rounded-2xl p-6 shadow-[0_0_30px_rgba(251,191,36,0.08)]"
        >
            <div className="flex items-center gap-3 mb-4">
                <motion.div
                    animate={{
                        rotate: [0, 5, -5, 0],
                        scale: [1, 1.1, 1]
                    }}
                    transition={{ duration: 3, repeat: Infinity }}
                >
                    <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
                </motion.div>
                <h2 className="text-lg font-semibold">Mina Flashcards och Quiz</h2>
                {favorites.length > 0 && (
                    <span className="ml-auto text-xs bg-amber-500/20 text-amber-400 px-2 py-0.5 rounded-full border border-amber-500/30">
                        {favorites.length}
                    </span>
                )}
            </div>

            {favorites.length === 0 ? (
                <div className="text-center py-6">
                    <motion.div
                        animate={{ opacity: [0.5, 0.8, 0.5] }}
                        transition={{ duration: 3, repeat: Infinity }}
                    >
                        <BookmarkX className="w-10 h-10 text-amber-500/30 mx-auto mb-2" />
                    </motion.div>
                    <p className="text-zinc-500 text-sm">Inga sparade favoriter</p>
                    <p className="text-xs text-zinc-600 flex items-center justify-center gap-1 mt-1">
                        <Star className="w-3 h-3 text-amber-500" />
                        Stjärnmarkera i Studyroom
                    </p>
                </div>
            ) : (
                <div className="space-y-3 max-h-80 overflow-y-auto">
                    {groupedFavorites.map((group, index) => (
                        <motion.div
                            key={group.moduleSlug}
                            initial={{ opacity: 0, x: -10 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ delay: index * 0.05 }}
                            className="bg-[#0a0a0f]/50 rounded-xl p-3 space-y-2 border border-zinc-700/30"
                        >
                            {/* Modulnamn */}
                            <p className="text-xs text-amber-300/60 font-medium">{group.moduleTitle}</p>

                            {/* Flashcards rad */}
                            {group.flashcards.length > 0 && (
                                <button
                                    onClick={() => handleGroupClick(group, "flashcard")}
                                    className="w-full flex items-center gap-2 p-2 bg-purple-500/10 border border-purple-500/30 rounded-lg hover:bg-purple-500/20 hover:border-purple-400/50 transition-all duration-300 text-left"
                                >
                                    <BookOpen className="w-4 h-4 text-purple-400 shrink-0" />
                                    <span className="text-sm text-purple-300">
                                        {group.flashcards.map(f => f.customName).join(", ")}
                                    </span>
                                    <span className="ml-auto text-xs text-purple-400/60">
                                        {group.flashcards.length} kort
                                    </span>
                                </button>
                            )}

                            {/* Quiz rad */}
                            {group.quizzes.length > 0 && (
                                <button
                                    onClick={() => handleGroupClick(group, "quiz")}
                                    className="w-full flex items-center gap-2 p-2 bg-blue-500/10 border border-blue-500/30 rounded-lg hover:bg-blue-500/20 hover:border-blue-400/50 transition-all duration-300 text-left"
                                >
                                    <Brain className="w-4 h-4 text-blue-400 shrink-0" />
                                    <span className="text-sm text-blue-300">
                                        {group.quizzes.map(q => q.customName).join(", ")}
                                    </span>
                                    <span className="ml-auto text-xs text-blue-400/60">
                                        {group.quizzes.length} frågor
                                    </span>
                                </button>
                            )}
                        </motion.div>
                    ))}
                </div>
            )}
        </motion.div>
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
        <div className="min-h-screen bg-[#05050a] text-white relative">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            <div className="relative z-10 p-6">
                <div className="max-w-4xl mx-auto space-y-6">

                    {/* ============================================================
                        HEADER - Pulsmätning — Cosmic Hero
                        ============================================================ */}
                    <motion.div
                        initial={{ opacity: 0, y: -20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                        className={cn(
                            "relative overflow-hidden rounded-2xl p-6",
                            "bg-gradient-to-r from-pink-600/30 via-purple-500/20 to-orange-500/20",
                            "border border-pink-500/30",
                            "shadow-[0_0_50px_rgba(236,72,153,0.15)]"
                        )}
                    >
                        {/* Background glow effects */}
                        <motion.div
                            className="absolute top-0 right-0 w-64 h-64 bg-pink-500/10 rounded-full blur-3xl"
                            animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.5, 0.3] }}
                            transition={{ duration: 6, repeat: Infinity }}
                        />

                        <div className="relative flex items-center gap-4">
                            <motion.div
                                className="w-14 h-14 rounded-2xl bg-gradient-to-br from-pink-500 to-purple-500 flex items-center justify-center"
                                animate={{
                                    boxShadow: [
                                        '0 0 25px rgba(236,72,153,0.4)',
                                        '0 0 40px rgba(236,72,153,0.6)',
                                        '0 0 25px rgba(236,72,153,0.4)'
                                    ],
                                    scale: [1, 1.05, 1]
                                }}
                                transition={{ duration: 2, repeat: Infinity }}
                            >
                                <Heart className="w-7 h-7 text-white" />
                            </motion.div>
                            <div>
                                <motion.h1
                                    className="text-2xl font-bold bg-gradient-to-r from-white via-pink-200 to-purple-200 bg-clip-text text-transparent"
                                    animate={{ backgroundPosition: ['0% 50%', '100% 50%', '0% 50%'] }}
                                    transition={{ duration: 5, repeat: Infinity }}
                                >
                                    Pulsmätning, {displayName}!
                                </motion.h1>
                                <p className="text-pink-200/60 text-sm">
                                    Planera din DevOps-resa, sätt upp mål och följ din progress
                                </p>
                            </div>
                        </div>
                    </motion.div>

                    {/* ============================================================
                        DALLAS CHAT
                        ============================================================ */}
                    <DallasChat userName={displayName} userId={user?.id} />

                    {/* ============================================================
                        VECKANS STUDIETID + MINA FAVORITER (side by side)
                        ============================================================ */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <WeeklySessionCard />
                        <FavoritesCard />
                    </div>

                    {/* ============================================================
                        NOW PLAYING - Spotify Widget
                        ============================================================ */}
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
                        className="relative"
                    >
                        <div className="flex items-center gap-3 mb-3">
                            <Music2 className="w-5 h-5 text-emerald-400" />
                            <h2 className="text-lg font-semibold">Now Playing</h2>
                        </div>
                        <SpotifyEmbed variant="compact" />
                    </motion.div>

                    {/* ============================================================
                        SNABBKNAPPAR (3 rutor) — Cosmic styled
                        ============================================================ */}
                    <div className="grid grid-cols-3 gap-4">
                        {/* Fortsätt lära */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                            whileHover={{ scale: 1.03, boxShadow: '0 0 30px rgba(139,92,246,0.3)' }}
                            whileTap={{ scale: 0.97 }}
                        >
                            <Link
                                href="/study"
                                className={cn(
                                    "flex flex-col items-center gap-3 p-6 rounded-2xl",
                                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                    "border border-purple-500/30",
                                    "hover:border-purple-400/50",
                                    "transition-all duration-300"
                                )}
                            >
                                <div className="w-14 h-14 rounded-2xl bg-purple-500/20 flex items-center justify-center border border-purple-500/30">
                                    <BookOpen className="w-7 h-7 text-purple-400" />
                                </div>
                                <span className="text-sm font-medium text-zinc-300">Fortsätt lära</span>
                            </Link>
                        </motion.div>

                        {/* Se progress */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
                            whileHover={{ scale: 1.03, boxShadow: '0 0 30px rgba(251,191,36,0.3)' }}
                            whileTap={{ scale: 0.97 }}
                        >
                            <Link
                                href="/progress"
                                className={cn(
                                    "flex flex-col items-center gap-3 p-6 rounded-2xl",
                                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                    "border border-amber-500/30",
                                    "hover:border-amber-400/50",
                                    "transition-all duration-300"
                                )}
                            >
                                <div className="w-14 h-14 rounded-2xl bg-amber-500/20 flex items-center justify-center border border-amber-500/30">
                                    <TrendingUp className="w-7 h-7 text-amber-400" />
                                </div>
                                <span className="text-sm font-medium text-zinc-300">Se progress</span>
                            </Link>
                        </motion.div>

                        {/* Fokusläge */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                            whileHover={{ scale: 1.03, boxShadow: '0 0 30px rgba(52,211,153,0.3)' }}
                            whileTap={{ scale: 0.97 }}
                        >
                            <Link
                                href="/focus"
                                className={cn(
                                    "flex flex-col items-center gap-3 p-6 rounded-2xl",
                                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                    "border border-emerald-500/30",
                                    "hover:border-emerald-400/50",
                                    "transition-all duration-300"
                                )}
                            >
                                <div className="w-14 h-14 rounded-2xl bg-emerald-500/20 flex items-center justify-center border border-emerald-500/30">
                                    <Focus className="w-7 h-7 text-emerald-400" />
                                </div>
                                <span className="text-sm font-medium text-zinc-300">Fokusläge</span>
                            </Link>
                        </motion.div>
                    </div>

                    {/* ============================================================
                        REKOMMENDERAT FÖR DIG — Cosmic styled
                        ============================================================ */}
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.35, ease: [0.16, 1, 0.3, 1] }}
                        className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border border-purple-500/30 rounded-2xl p-6 shadow-[0_0_30px_rgba(139,92,246,0.08)]"
                    >
                        <div className="flex items-center gap-3 mb-4">
                            <motion.div
                                animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.1, 1] }}
                                transition={{ duration: 3, repeat: Infinity }}
                            >
                                <Sparkles className="w-5 h-5 text-purple-400" />
                            </motion.div>
                            <h2 className="text-lg font-semibold">Rekommenderat för dig</h2>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                            <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                                <Link
                                    href="/study/linux-mastery/flashcards"
                                    className="flex items-center gap-3 p-4 bg-[#0a0a0f]/50 rounded-xl hover:bg-purple-500/10 border border-zinc-700/30 hover:border-purple-500/40 transition-all duration-300"
                                >
                                    <div className="w-10 h-10 rounded-lg bg-purple-500/20 flex items-center justify-center border border-purple-500/30">
                                        <BookOpen className="w-5 h-5 text-purple-400" />
                                    </div>
                                    <div className="flex-1">
                                        <p className="font-medium text-sm">Linux Flashcards</p>
                                        <p className="text-xs text-zinc-500">90 kort • Grundläggande</p>
                                    </div>
                                </Link>
                            </motion.div>

                            <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                                <Link
                                    href="/study/docker-mastery/quiz"
                                    className="flex items-center gap-3 p-4 bg-[#0a0a0f]/50 rounded-xl hover:bg-blue-500/10 border border-zinc-700/30 hover:border-blue-500/40 transition-all duration-300"
                                >
                                    <div className="w-10 h-10 rounded-lg bg-blue-500/20 flex items-center justify-center border border-blue-500/30">
                                        <Brain className="w-5 h-5 text-blue-400" />
                                    </div>
                                    <div className="flex-1">
                                        <p className="font-medium text-sm">Docker Quiz</p>
                                        <p className="text-xs text-zinc-500">60 frågor • Blandad</p>
                                    </div>
                                </Link>
                            </motion.div>
                        </div>
                    </motion.div>

                </div>
            </div>
        </div>
    )
}
