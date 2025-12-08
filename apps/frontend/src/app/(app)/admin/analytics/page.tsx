"use client"

/**
 * Admin Analytics - AI Usage & Platform Statistics
 *
 * Visar:
 * - AI-användning per användare (Dallas, AI Quiz)
 * - Veckovis kostnad och tokens
 * - Platform-statistik
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    Brain,
    TrendingUp,
    Users,
    DollarSign,
    Zap,
    Calendar,
    BarChart3,
    Loader2,
    RefreshCw,
} from "lucide-react"
import Link from "next/link"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface AIUsageUser {
    user_id: string
    email: string
    full_name: string
    total_calls: number
    total_tokens: number
    total_cost_usd: number
}

interface WeeklySummary {
    year: number
    week: number
    total_calls: number
    unique_users: number
    total_tokens: number
    total_cost_usd: number
}

interface AIUsageResponse {
    totals: {
        total_calls: number
        total_tokens: number
        total_cost_usd: number
        unique_users: number
    }
    users: AIUsageUser[]
    weekly_summary: WeeklySummary[]
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export default function AdminAnalyticsPage() {
    const router = useRouter()
    const { user } = useAuth()

    const [loading, setLoading] = useState(true)
    const [data, setData] = useState<AIUsageResponse | null>(null)
    const [selectedWeek, setSelectedWeek] = useState<number | null>(null)

    // Check admin access
    useEffect(() => {
        if (user && user.email !== ADMIN_EMAIL) {
            router.push("/dashboard")
        }
    }, [user, router])

    // Fetch AI usage data
    useEffect(() => {
        fetchAIUsage()
    }, [selectedWeek])

    async function fetchAIUsage() {
        try {
            setLoading(true)
            const token = await getToken()

            const params = new URLSearchParams()
            if (selectedWeek) {
                params.set("week", selectedWeek.toString())
                params.set("year", new Date().getFullYear().toString())
            }

            const res = await fetch(`${API_BASE_URL}/api/admin/ai-usage?${params}`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })

            if (res.ok) {
                const result = await res.json()
                setData(result)
            }
        } catch (err) {
            console.error("Error fetching AI usage:", err)
        } finally {
            setLoading(false)
        }
    }

    if (user?.email !== ADMIN_EMAIL) {
        return null
    }

    const currentWeek = Math.ceil((new Date().getTime() - new Date(new Date().getFullYear(), 0, 1).getTime()) / (7 * 24 * 60 * 60 * 1000))

    return (
        <div className="min-h-screen bg-zinc-950 text-white p-8">
            <div className="max-w-6xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <Link
                        href="/admin"
                        className="text-zinc-400 hover:text-white flex items-center gap-2 mb-4"
                    >
                        <ArrowLeft className="w-4 h-4" />
                        Tillbaka till Admin
                    </Link>
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center">
                                <BarChart3 className="w-6 h-6" />
                            </div>
                            <div>
                                <h1 className="text-2xl font-bold">Analytics</h1>
                                <p className="text-zinc-400">
                                    AI-användning och kostnader
                                </p>
                            </div>
                        </div>
                        <button
                            onClick={() => fetchAIUsage()}
                            className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 transition-colors"
                        >
                            <RefreshCw className={cn("w-5 h-5", loading && "animate-spin")} />
                        </button>
                    </div>
                </div>

                {/* Week Filter */}
                <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
                    <button
                        onClick={() => setSelectedWeek(null)}
                        className={cn(
                            "px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap",
                            selectedWeek === null
                                ? "bg-amber-500 text-black"
                                : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                        )}
                    >
                        Alla
                    </button>
                    {[...Array(4)].map((_, i) => {
                        const week = currentWeek - i
                        return (
                            <button
                                key={week}
                                onClick={() => setSelectedWeek(week)}
                                className={cn(
                                    "px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap",
                                    selectedWeek === week
                                        ? "bg-amber-500 text-black"
                                        : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                                )}
                            >
                                Vecka {week}
                            </button>
                        )
                    })}
                </div>

                {loading ? (
                    <div className="flex items-center justify-center py-20">
                        <Loader2 className="w-8 h-8 animate-spin text-amber-500" />
                    </div>
                ) : data ? (
                    <>
                        {/* Summary Cards */}
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                            <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800">
                                <div className="flex items-center gap-2 text-zinc-400 mb-2">
                                    <Zap className="w-4 h-4" />
                                    <span className="text-sm">API-anrop</span>
                                </div>
                                <p className="text-2xl font-bold text-white">
                                    {data.totals.total_calls.toLocaleString()}
                                </p>
                            </div>
                            <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800">
                                <div className="flex items-center gap-2 text-zinc-400 mb-2">
                                    <Brain className="w-4 h-4" />
                                    <span className="text-sm">Tokens</span>
                                </div>
                                <p className="text-2xl font-bold text-white">
                                    {data.totals.total_tokens.toLocaleString()}
                                </p>
                            </div>
                            <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800">
                                <div className="flex items-center gap-2 text-zinc-400 mb-2">
                                    <DollarSign className="w-4 h-4" />
                                    <span className="text-sm">Kostnad</span>
                                </div>
                                <p className="text-2xl font-bold text-emerald-400">
                                    ${data.totals.total_cost_usd.toFixed(4)}
                                </p>
                            </div>
                            <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800">
                                <div className="flex items-center gap-2 text-zinc-400 mb-2">
                                    <Users className="w-4 h-4" />
                                    <span className="text-sm">Användare</span>
                                </div>
                                <p className="text-2xl font-bold text-white">
                                    {data.totals.unique_users}
                                </p>
                            </div>
                        </div>

                        {/* Weekly Summary */}
                        {data.weekly_summary.length > 0 && (
                            <div className="mb-8">
                                <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
                                    <Calendar className="w-5 h-5 text-amber-400" />
                                    Veckovis sammanfattning
                                </h2>
                                <div className="overflow-x-auto">
                                    <table className="w-full">
                                        <thead>
                                            <tr className="text-left text-zinc-400 text-sm border-b border-zinc-800">
                                                <th className="pb-3 pr-4">Vecka</th>
                                                <th className="pb-3 pr-4">Anrop</th>
                                                <th className="pb-3 pr-4">Användare</th>
                                                <th className="pb-3 pr-4">Tokens</th>
                                                <th className="pb-3">Kostnad</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {data.weekly_summary.map((week) => (
                                                <tr key={`${week.year}-${week.week}`} className="border-b border-zinc-800/50">
                                                    <td className="py-3 pr-4">
                                                        <span className="font-medium">V{week.week}</span>
                                                        <span className="text-zinc-500 text-sm ml-1">{week.year}</span>
                                                    </td>
                                                    <td className="py-3 pr-4">{week.total_calls}</td>
                                                    <td className="py-3 pr-4">{week.unique_users}</td>
                                                    <td className="py-3 pr-4">{week.total_tokens.toLocaleString()}</td>
                                                    <td className="py-3 text-emerald-400">${week.total_cost_usd.toFixed(4)}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        )}

                        {/* Users List */}
                        <div>
                            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
                                <TrendingUp className="w-5 h-5 text-amber-400" />
                                Användning per användare
                            </h2>
                            {data.users.length === 0 ? (
                                <div className="text-center py-12 text-zinc-500">
                                    <Brain className="w-12 h-12 mx-auto mb-3 opacity-30" />
                                    <p>Ingen AI-användning registrerad ännu</p>
                                    <p className="text-sm mt-1">Data visas när användare interagerar med Dallas eller AI Quiz</p>
                                </div>
                            ) : (
                                <div className="space-y-2">
                                    {data.users.map((u) => (
                                        <div
                                            key={u.user_id}
                                            className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 flex items-center justify-between"
                                        >
                                            <div>
                                                <p className="font-medium text-white">
                                                    {u.full_name || u.email}
                                                </p>
                                                <p className="text-sm text-zinc-500">{u.email}</p>
                                            </div>
                                            <div className="flex items-center gap-6 text-right">
                                                <div>
                                                    <p className="text-sm text-zinc-400">Anrop</p>
                                                    <p className="font-semibold">{u.total_calls}</p>
                                                </div>
                                                <div>
                                                    <p className="text-sm text-zinc-400">Tokens</p>
                                                    <p className="font-semibold">{u.total_tokens.toLocaleString()}</p>
                                                </div>
                                                <div>
                                                    <p className="text-sm text-zinc-400">Kostnad</p>
                                                    <p className="font-semibold text-emerald-400">
                                                        ${u.total_cost_usd.toFixed(4)}
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </>
                ) : (
                    <div className="text-center py-12 text-zinc-500">
                        <p>Kunde inte hämta data</p>
                    </div>
                )}
            </div>
        </div>
    )
}
