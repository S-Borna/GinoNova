"use client"

/**
 * Admin Content - Hantera moduler och kurser
 *
 * Visar:
 * - Lista alla moduler
 * - Seed/reseed content
 * - Aktivera/inaktivera moduler
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    BookOpen,
    RefreshCw,
    Loader2,
    CheckCircle,
    XCircle,
    Database,
    Layers,
    FileText,
    Beaker,
    Play,
    AlertTriangle,
} from "lucide-react"
import Link from "next/link"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Module {
    id: string
    name: string
    slug: string
    description: string
    order_index: number
    difficulty: string
    estimated_hours: number
    is_active: boolean
    track_id: string
}

interface ContentSummary {
    tracks: number
    modules: number
    tasks: number
    labs: number
    projects: number
    total_hours: number
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export default function AdminContentPage() {
    const router = useRouter()
    const { user } = useAuth()

    const [loading, setLoading] = useState(true)
    const [seeding, setSeeding] = useState(false)
    const [modules, setModules] = useState<Module[]>([])
    const [summary, setSummary] = useState<ContentSummary | null>(null)

    // Check admin access
    useEffect(() => {
        if (user && user.email !== ADMIN_EMAIL) {
            router.push("/dashboard")
        }
    }, [user, router])

    // Fetch data
    useEffect(() => {
        fetchContent()
    }, [])

    async function fetchContent() {
        try {
            setLoading(true)
            const token = await getToken()

            // Fetch modules
            const modulesRes = await fetch(`${API_BASE_URL}/api/modules`, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (modulesRes.ok) {
                const modulesData = await modulesRes.json()
                setModules(modulesData)
            }

            // Fetch summary
            const summaryRes = await fetch(`${API_BASE_URL}/api/admin/bootcamp-summary`, {
                headers: { Authorization: `Bearer ${token}` },
            })
            if (summaryRes.ok) {
                const summaryData = await summaryRes.json()
                setSummary(summaryData)
            }
        } catch (err) {
            console.error("Error fetching content:", err)
        } finally {
            setLoading(false)
        }
    }

    async function seedContent() {
        try {
            setSeeding(true)
            const token = await getToken()

            const res = await fetch(`${API_BASE_URL}/api/admin/seed/v3`, {
                method: "POST",
                headers: { Authorization: `Bearer ${token}` },
            })

            if (res.ok) {
                // Refresh content
                await fetchContent()
            }
        } catch (err) {
            console.error("Error seeding content:", err)
        } finally {
            setSeeding(false)
        }
    }

    if (user?.email !== ADMIN_EMAIL) {
        return null
    }

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
                            <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center">
                                <BookOpen className="w-6 h-6" />
                            </div>
                            <div>
                                <h1 className="text-2xl font-bold">Innehåll</h1>
                                <p className="text-zinc-400">
                                    Hantera moduler och kurser
                                </p>
                            </div>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={() => fetchContent()}
                                className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700 transition-colors"
                                title="Uppdatera"
                            >
                                <RefreshCw className={cn("w-5 h-5", loading && "animate-spin")} />
                            </button>
                            <button
                                onClick={seedContent}
                                disabled={seeding}
                                className={cn(
                                    "px-4 py-2 rounded-lg flex items-center gap-2",
                                    "bg-emerald-600 hover:bg-emerald-500 text-white",
                                    "disabled:opacity-50 disabled:cursor-not-allowed"
                                )}
                            >
                                {seeding ? (
                                    <Loader2 className="w-4 h-4 animate-spin" />
                                ) : (
                                    <Database className="w-4 h-4" />
                                )}
                                {seeding ? "Seedar..." : "Seed V3 Content"}
                            </button>
                        </div>
                    </div>
                </div>

                {loading ? (
                    <div className="flex items-center justify-center py-20">
                        <Loader2 className="w-8 h-8 animate-spin text-emerald-500" />
                    </div>
                ) : (
                    <>
                        {/* Summary Stats */}
                        {summary && (
                            <div className="grid grid-cols-2 md:grid-cols-6 gap-4 mb-8">
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <Layers className="w-5 h-5 mx-auto mb-2 text-purple-400" />
                                    <p className="text-2xl font-bold">{summary.tracks}</p>
                                    <p className="text-xs text-zinc-500">Tracks</p>
                                </div>
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <BookOpen className="w-5 h-5 mx-auto mb-2 text-emerald-400" />
                                    <p className="text-2xl font-bold">{summary.modules}</p>
                                    <p className="text-xs text-zinc-500">Moduler</p>
                                </div>
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <FileText className="w-5 h-5 mx-auto mb-2 text-blue-400" />
                                    <p className="text-2xl font-bold">{summary.tasks}</p>
                                    <p className="text-xs text-zinc-500">Tasks</p>
                                </div>
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <Beaker className="w-5 h-5 mx-auto mb-2 text-cyan-400" />
                                    <p className="text-2xl font-bold">{summary.labs}</p>
                                    <p className="text-xs text-zinc-500">Labs</p>
                                </div>
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <Play className="w-5 h-5 mx-auto mb-2 text-orange-400" />
                                    <p className="text-2xl font-bold">{summary.projects}</p>
                                    <p className="text-xs text-zinc-500">Projekt</p>
                                </div>
                                <div className="p-4 rounded-xl bg-zinc-900 border border-zinc-800 text-center">
                                    <AlertTriangle className="w-5 h-5 mx-auto mb-2 text-amber-400" />
                                    <p className="text-2xl font-bold">{summary.total_hours}h</p>
                                    <p className="text-xs text-zinc-500">Timmar</p>
                                </div>
                            </div>
                        )}

                        {/* Modules List */}
                        <div>
                            <h2 className="text-lg font-semibold mb-4">
                                Moduler ({modules.length})
                            </h2>
                            {modules.length === 0 ? (
                                <div className="text-center py-12 bg-zinc-900/50 rounded-xl border border-zinc-800">
                                    <BookOpen className="w-12 h-12 mx-auto mb-3 text-zinc-600" />
                                    <p className="text-zinc-400">Inga moduler hittades</p>
                                    <p className="text-sm text-zinc-500 mt-1">
                                        Klicka på &quot;Seed V3 Content&quot; för att ladda in kursmaterial
                                    </p>
                                </div>
                            ) : (
                                <div className="space-y-2">
                                    {modules
                                        .sort((a, b) => a.order_index - b.order_index)
                                        .map((module) => (
                                            <div
                                                key={module.id}
                                                className={cn(
                                                    "p-4 rounded-xl border flex items-center justify-between",
                                                    module.is_active
                                                        ? "bg-zinc-900 border-zinc-800"
                                                        : "bg-zinc-900/50 border-zinc-800/50 opacity-60"
                                                )}
                                            >
                                                <div className="flex items-center gap-4">
                                                    <div className="w-10 h-10 rounded-lg bg-emerald-500/20 flex items-center justify-center text-emerald-400 font-bold">
                                                        {module.order_index}
                                                    </div>
                                                    <div>
                                                        <p className="font-medium text-white">
                                                            {module.name}
                                                        </p>
                                                        <p className="text-sm text-zinc-500">
                                                            {module.slug} • {module.estimated_hours}h • {module.difficulty}
                                                        </p>
                                                    </div>
                                                </div>
                                                <div className="flex items-center gap-4">
                                                    {module.is_active ? (
                                                        <span className="flex items-center gap-1 text-emerald-400 text-sm">
                                                            <CheckCircle className="w-4 h-4" />
                                                            Aktiv
                                                        </span>
                                                    ) : (
                                                        <span className="flex items-center gap-1 text-zinc-500 text-sm">
                                                            <XCircle className="w-4 h-4" />
                                                            Inaktiv
                                                        </span>
                                                    )}
                                                </div>
                                            </div>
                                        ))}
                                </div>
                            )}
                        </div>
                    </>
                )}
            </div>
        </div>
    )
}
