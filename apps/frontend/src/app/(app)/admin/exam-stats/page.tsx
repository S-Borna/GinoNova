"use client"

/**
 * Admin Exam Stats - Overview of all exam simulations
 * Shows totals, per-user results, and trends
 */

import { useEffect, useState, useCallback } from "react"
import {
    RefreshCw,
    Trophy,
    Users,
    BookOpen,
    Clock,
    TrendingUp,
    TrendingDown,
    Target,
    Award,
    BarChart3,
    Calendar,
    Trash2
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

type TimeRange = "7d" | "30d" | "90d"

interface ExamStats {
    total_exams: number
    total_exams_today: number
    total_exams_week: number
    total_questions_answered: number
    avg_score: number
    avg_time_minutes: number
    unique_users: number
    top_performers: Array<{
        user_id: string
        email: string
        full_name: string | null
        total_exams: number
        avg_score: number
        best_score: number
        total_questions: number
        total_correct: number
        avg_time_minutes: number
        last_exam_at: string | null
    }>
    recent_exams: Array<{
        id: string
        user_email: string
        user_name: string | null
        score_percent: number
        correct_answers: number
        question_count: number
        time_spent_minutes: number
        sources: string[]
        completed_at: string | null
    }>
    score_distribution: Record<string, number>
    exams_by_day: Array<{
        date: string
        count: number
        avg_score: number
    }>
}

function StatCard({
    icon: Icon,
    value,
    label,
    subtext,
    color = "purple"
}: {
    icon: React.ElementType
    value: string | number
    label: string
    subtext?: string
    color?: "purple" | "blue" | "green" | "orange" | "pink"
}) {
    const colors = {
        purple: "from-purple-500/20 to-purple-600/20 text-purple-400",
        blue: "from-blue-500/20 to-blue-600/20 text-blue-400",
        green: "from-green-500/20 to-green-600/20 text-green-400",
        orange: "from-orange-500/20 to-orange-600/20 text-orange-400",
        pink: "from-pink-500/20 to-pink-600/20 text-pink-400"
    }

    return (
        <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
            <div className={cn(
                "w-10 h-10 rounded-lg flex items-center justify-center mb-3 bg-gradient-to-br",
                colors[color] || colors.purple
            )}>
                <Icon className="w-5 h-5" />
            </div>
            <div className="text-2xl font-bold mb-1">{value}</div>
            <div className="text-sm text-zinc-400">{label}</div>
            {subtext && <div className="text-xs text-zinc-500 mt-1">{subtext}</div>}
        </div>
    )
}

function ScoreBar({ score }: { score: number }) {
    const getColor = (s: number) => {
        if (s >= 80) return "bg-green-500"
        if (s >= 60) return "bg-yellow-500"
        if (s >= 40) return "bg-orange-500"
        return "bg-red-500"
    }

    return (
        <div className="flex items-center gap-2">
            <div className="flex-1 h-2 bg-zinc-800 rounded-full overflow-hidden">
                <div
                    className={cn("h-full rounded-full transition-all", getColor(score))}
                    style={{ width: `${score}%` }}
                />
            </div>
            <span className={cn(
                "text-sm font-medium w-12 text-right",
                score >= 60 ? "text-green-400" : "text-red-400"
            )}>
                {score.toFixed(0)}%
            </span>
        </div>
    )
}

function ExamsByDayChart({ data }: { data: Array<{ date: string; count: number; avg_score: number }> }) {
    const maxCount = Math.max(...data.map(d => d.count), 1)
    const showEveryN = data.length > 7 ? Math.ceil(data.length / 5) : 1

    return (
        <div>
            <div className="flex items-end gap-1 h-40">
                {data.map((item, i) => {
                    const height = (item.count / maxCount) * 100
                    const formattedDate = (() => {
                        try {
                            const d = new Date(item.date)
                            return d.toLocaleDateString('sv-SE', { day: 'numeric', month: 'short' })
                        } catch {
                            return item.date.slice(-5)
                        }
                    })()
                    const showLabel = i % showEveryN === 0 || i === data.length - 1

                    return (
                        <div key={item.date} className="flex-1 flex flex-col items-center gap-1 group">
                            <div
                                className="w-full bg-emerald-500 rounded-t opacity-80 hover:opacity-100 transition cursor-pointer relative"
                                style={{ height: `${height}%`, minHeight: item.count > 0 ? 4 : 0 }}
                            >
                                <div className="absolute -top-16 left-1/2 -translate-x-1/2 bg-zinc-800 px-2 py-1 rounded text-xs opacity-0 group-hover:opacity-100 transition whitespace-nowrap z-10">
                                    <div>{formattedDate}</div>
                                    <div>{item.count} tentor</div>
                                    <div>Snitt: {item.avg_score}%</div>
                                </div>
                            </div>
                            {showLabel ? (
                                <span className="text-[10px] text-zinc-500 whitespace-nowrap">
                                    {formattedDate}
                                </span>
                            ) : (
                                <span className="text-[10px] text-transparent">.</span>
                            )}
                        </div>
                    )
                })}
            </div>
            <div className="text-center text-xs text-zinc-500 mt-2">Tentor per dag</div>
        </div>
    )
}

function ScoreDistributionChart({ data }: { data: Record<string, number> }) {
    const total = Object.values(data).reduce((a, b) => a + b, 0) || 1
    const ranges = ["0-20", "20-40", "40-60", "60-80", "80-100"]
    const colors = ["bg-red-500", "bg-orange-500", "bg-yellow-500", "bg-lime-500", "bg-green-500"]

    return (
        <div className="space-y-2">
            {ranges.map((range, i) => {
                const count = data[range] || 0
                const percent = (count / total) * 100

                return (
                    <div key={range} className="flex items-center gap-3">
                        <span className="text-xs text-zinc-400 w-14">{range}%</span>
                        <div className="flex-1 h-4 bg-zinc-800 rounded-full overflow-hidden">
                            <div
                                className={cn("h-full rounded-full transition-all", colors[i])}
                                style={{ width: `${percent}%` }}
                            />
                        </div>
                        <span className="text-xs text-zinc-500 w-8 text-right">{count}</span>
                    </div>
                )
            })}
        </div>
    )
}

export default function AdminExamStatsPage() {
    const [data, setData] = useState<ExamStats | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [timeRange, setTimeRange] = useState<TimeRange>("30d")
    const [deleting, setDeleting] = useState<string | null>(null)

    const fetchData = useCallback(async () => {
        const token = getToken()
        if (!token) {
            setError("Not authenticated")
            setLoading(false)
            return
        }

        setLoading(true)
        setError(null)

        try {
            const res = await fetch(
                `${API_BASE_URL}/api/admin/exam-stats?range=${timeRange}`,
                { headers: { Authorization: `Bearer ${token}` } }
            )

            if (!res.ok) {
                throw new Error(`API error: ${res.status}`)
            }

            const result = await res.json()
            setData(result)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Failed to load data")
        } finally {
            setLoading(false)
        }
    }, [timeRange])

    const deleteUserResults = async (userId: string, userName: string) => {
        if (!confirm(`Är du säker på att du vill ta bort alla tentaresultat för ${userName}?`)) {
            return
        }

        const token = getToken()
        if (!token) return

        setDeleting(userId)
        try {
            const res = await fetch(
                `${API_BASE_URL}/api/admin/exam-stats/user/${userId}`,
                {
                    method: 'DELETE',
                    headers: { Authorization: `Bearer ${token}` }
                }
            )

            if (!res.ok) {
                throw new Error(`Failed to delete: ${res.status}`)
            }

            const result = await res.json()
            alert(result.message)
            fetchData() // Refresh data
        } catch (err) {
            alert(err instanceof Error ? err.message : "Kunde inte ta bort")
        } finally {
            setDeleting(null)
        }
    }

    useEffect(() => {
        fetchData()
    }, [fetchData])

    return (
        <div className="p-6 max-w-7xl mx-auto">
            {/* Header */}
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-2xl font-bold flex items-center gap-2">
                        <Trophy className="w-7 h-7 text-yellow-500" />
                        Exam Stats
                    </h1>
                    <p className="text-zinc-400 text-sm">
                        Tenta-simuleringar och resultat
                    </p>
                </div>
                <div className="flex items-center gap-3">
                    {/* Time range selector */}
                    <div className="flex bg-zinc-800 rounded-lg p-1">
                        {(["7d", "30d", "90d"] as TimeRange[]).map((range) => (
                            <button
                                key={range}
                                onClick={() => setTimeRange(range)}
                                className={cn(
                                    "px-3 py-1 rounded text-sm transition",
                                    timeRange === range
                                        ? "bg-purple-600 text-white"
                                        : "text-zinc-400 hover:text-white"
                                )}
                            >
                                {range}
                            </button>
                        ))}
                    </div>
                    <button
                        onClick={fetchData}
                        disabled={loading}
                        className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Refresh
                    </button>
                </div>
            </div>

            {error && (
                <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-6 text-red-400">
                    {error}
                </div>
            )}

            {/* Stats Grid */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
                <StatCard
                    icon={BookOpen}
                    value={data?.total_exams || 0}
                    label="Totalt tentor"
                    subtext={`${data?.total_exams_today || 0} idag`}
                    color="purple"
                />
                <StatCard
                    icon={Target}
                    value={`${data?.avg_score || 0}%`}
                    label="Genomsnittlig poäng"
                    color="green"
                />
                <StatCard
                    icon={Users}
                    value={data?.unique_users || 0}
                    label="Unika användare"
                    color="blue"
                />
                <StatCard
                    icon={Clock}
                    value={`${data?.avg_time_minutes || 0} min`}
                    label="Snitt tid per tenta"
                    color="orange"
                />
            </div>

            <div className="grid lg:grid-cols-2 gap-6 mb-8">
                {/* Exams by Day Chart */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
                    <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                        <Calendar className="w-5 h-5 text-emerald-400" />
                        Tentor per dag
                    </h3>
                    {data?.exams_by_day && data.exams_by_day.length > 0 ? (
                        <ExamsByDayChart data={data.exams_by_day} />
                    ) : (
                        <div className="h-40 flex items-center justify-center text-zinc-500">
                            Ingen data ännu
                        </div>
                    )}
                </div>

                {/* Score Distribution */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
                    <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                        <BarChart3 className="w-5 h-5 text-purple-400" />
                        Poängfördelning
                    </h3>
                    {data?.score_distribution ? (
                        <ScoreDistributionChart data={data.score_distribution} />
                    ) : (
                        <div className="h-40 flex items-center justify-center text-zinc-500">
                            Ingen data ännu
                        </div>
                    )}
                </div>
            </div>

            <div className="grid lg:grid-cols-2 gap-6">
                {/* Top Performers */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
                    <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                        <Trophy className="w-5 h-5 text-yellow-400" />
                        Top Performers
                    </h3>
                    {data?.top_performers && data.top_performers.length > 0 ? (
                        <div className="space-y-3">
                            {data.top_performers.slice(0, 5).map((user, i) => (
                                <div
                                    key={user.user_id}
                                    className="flex items-center gap-3 p-3 bg-zinc-800/50 rounded-lg"
                                >
                                    <div className={cn(
                                        "w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold",
                                        i === 0 ? "bg-yellow-500/20 text-yellow-400" :
                                            i === 1 ? "bg-zinc-400/20 text-zinc-300" :
                                                i === 2 ? "bg-orange-500/20 text-orange-400" :
                                                    "bg-zinc-700 text-zinc-400"
                                    )}>
                                        {i + 1}
                                    </div>
                                    <div className="flex-1 min-w-0">
                                        <div className="font-medium truncate">
                                            {user.full_name || user.email.split('@')[0]}
                                        </div>
                                        <div className="text-xs text-zinc-500">
                                            {user.total_exams} tentor • Bäst: {user.best_score}%
                                        </div>
                                    </div>
                                    <div className="text-right">
                                        <div className={cn(
                                            "text-lg font-bold",
                                            user.avg_score >= 60 ? "text-green-400" : "text-orange-400"
                                        )}>
                                            {user.avg_score}%
                                        </div>
                                        <div className="text-xs text-zinc-500">snitt</div>
                                    </div>
                                    <button
                                        onClick={() => deleteUserResults(user.user_id, user.full_name || user.email)}
                                        disabled={deleting === user.user_id}
                                        className="p-2 rounded-lg bg-red-500/10 text-red-400 hover:bg-red-500/20 transition-colors disabled:opacity-50"
                                        title="Ta bort alla resultat"
                                    >
                                        {deleting === user.user_id ? (
                                            <RefreshCw className="w-4 h-4 animate-spin" />
                                        ) : (
                                            <Trash2 className="w-4 h-4" />
                                        )}
                                    </button>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <div className="py-8 text-center text-zinc-500">
                            Inga tentor genomförda ännu
                        </div>
                    )}
                </div>

                {/* Recent Exams */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-5">
                    <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                        <Clock className="w-5 h-5 text-blue-400" />
                        Senaste tentor
                    </h3>
                    {data?.recent_exams && data.recent_exams.length > 0 ? (
                        <div className="space-y-2">
                            {data.recent_exams.slice(0, 6).map((exam) => (
                                <div
                                    key={exam.id}
                                    className="flex items-center gap-3 p-3 bg-zinc-800/50 rounded-lg"
                                >
                                    <div className="flex-1 min-w-0">
                                        <div className="font-medium truncate text-sm">
                                            {exam.user_name || exam.user_email.split('@')[0]}
                                        </div>
                                        <div className="text-xs text-zinc-500">
                                            {exam.correct_answers}/{exam.question_count} rätt • {exam.time_spent_minutes} min
                                        </div>
                                    </div>
                                    <ScoreBar score={exam.score_percent} />
                                </div>
                            ))}
                        </div>
                    ) : (
                        <div className="py-8 text-center text-zinc-500">
                            Inga tentor genomförda ännu
                        </div>
                    )}
                </div>
            </div>

            {/* Total Questions Answered */}
            <div className="mt-8 bg-gradient-to-r from-purple-500/10 to-blue-500/10 border border-purple-500/20 rounded-xl p-6 text-center">
                <div className="text-4xl font-bold text-purple-400 mb-2">
                    {(data?.total_questions_answered || 0).toLocaleString()}
                </div>
                <div className="text-zinc-400">Totalt besvarade frågor</div>
            </div>
        </div>
    )
}
