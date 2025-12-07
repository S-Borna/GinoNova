"use client"

/**
 * Admin Permissions - Hantera användarbehörigheter
 *
 * Admin kan ge/ta bort åtkomst till specifika features:
 * - AI Quiz
 * - Premium moduler
 * - etc.
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    Search,
    Shield,
    Brain,
    BookOpen,
    Sparkles,
    Check,
    X,
    Loader2,
    Save,
    Users,
    Lock,
    Unlock,
} from "lucide-react"
import Link from "next/link"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

/* ============================================================================
   TYPES
   ============================================================================ */

interface UserPermission {
    id: string
    email: string
    full_name: string | null
    permissions: {
        ai_quiz: boolean
        premium_modules: boolean
        study_room: boolean
        skillpath: boolean
    }
}

interface Feature {
    key: keyof UserPermission["permissions"]
    label: string
    icon: React.ElementType
    description: string
    color: string
}

const FEATURES: Feature[] = [
    {
        key: "ai_quiz",
        label: "AI Quiz",
        icon: Brain,
        description: "Tillgång till AI-genererade quiz",
        color: "purple"
    },
    {
        key: "premium_modules",
        label: "Premium Moduler",
        icon: Sparkles,
        description: "Avancerade läromoduler",
        color: "amber"
    },
    {
        key: "study_room",
        label: "Studyroom",
        icon: BookOpen,
        description: "Flashcards och Quiz",
        color: "blue"
    },
    {
        key: "skillpath",
        label: "Skillpath Board",
        icon: Shield,
        description: "Analytics dashboard",
        color: "emerald"
    },
]

/* ============================================================================
   ADMIN PERMISSIONS PAGE
   ============================================================================ */

export default function AdminPermissionsPage() {
    const router = useRouter()
    const { user } = useAuth()

    const [users, setUsers] = useState<UserPermission[]>([])
    const [loading, setLoading] = useState(true)
    const [saving, setSaving] = useState<string | null>(null)
    const [searchQuery, setSearchQuery] = useState("")
    const [changes, setChanges] = useState<Map<string, Partial<UserPermission["permissions"]>>>(new Map())

    // Check admin access
    useEffect(() => {
        if (user && user.email !== ADMIN_EMAIL) {
            router.push("/dashboard")
        }
    }, [user, router])

    // Fetch users
    useEffect(() => {
        fetchUsers()
    }, [])

    async function fetchUsers() {
        try {
            setLoading(true)
            const token = await getToken()

            // Fetch users from admin API
            const res = await fetch(`${API_BASE_URL}/api/admin/users?per_page=100`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            })

            if (res.ok) {
                const data = await res.json()
                // Map to permission format
                const mappedUsers: UserPermission[] = data.users.map((u: any) => ({
                    id: u.id,
                    email: u.email,
                    full_name: u.full_name,
                    permissions: u.permissions || {
                        ai_quiz: true,        // Default: alla har tillgång
                        premium_modules: true,
                        study_room: true,
                        skillpath: true,
                    }
                }))
                setUsers(mappedUsers)
            }
        } catch (err) {
            console.error("Error fetching users:", err)
        } finally {
            setLoading(false)
        }
    }

    function togglePermission(userId: string, feature: keyof UserPermission["permissions"]) {
        const user = users.find(u => u.id === userId)
        if (!user) return

        const currentValue = user.permissions[feature]
        const existingChanges = changes.get(userId) || {}

        setChanges(new Map(changes).set(userId, {
            ...existingChanges,
            [feature]: !currentValue
        }))

        // Update local state for immediate feedback
        setUsers(users.map(u =>
            u.id === userId
                ? { ...u, permissions: { ...u.permissions, [feature]: !currentValue } }
                : u
        ))
    }

    async function savePermissions(userId: string) {
        const userChanges = changes.get(userId)
        if (!userChanges) return

        try {
            setSaving(userId)
            const token = await getToken()

            // Note: Backend needs to implement this endpoint
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${userId}/permissions`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ permissions: userChanges })
            })

            if (res.ok) {
                // Clear changes for this user
                const newChanges = new Map(changes)
                newChanges.delete(userId)
                setChanges(newChanges)
            }
        } catch (err) {
            console.error("Error saving permissions:", err)
        } finally {
            setSaving(null)
        }
    }

    // Filter users by search
    const filteredUsers = users.filter(u =>
        u.email.toLowerCase().includes(searchQuery.toLowerCase()) ||
        (u.full_name?.toLowerCase() || "").includes(searchQuery.toLowerCase())
    )

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
                    <div className="flex items-center gap-4">
                        <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-purple-500 to-blue-600 flex items-center justify-center">
                            <Shield className="w-6 h-6" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold">Behörigheter</h1>
                            <p className="text-zinc-400">
                                Hantera användares åtkomst till features
                            </p>
                        </div>
                    </div>
                </div>

                {/* Search */}
                <div className="relative mb-6">
                    <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
                    <input
                        type="text"
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        placeholder="Sök användare..."
                        className={cn(
                            "w-full pl-12 pr-4 py-3 rounded-xl",
                            "bg-zinc-900 border border-zinc-800",
                            "text-white placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50"
                        )}
                    />
                </div>

                {/* Feature Legend */}
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-2xl p-4 mb-6">
                    <h2 className="text-sm font-semibold text-zinc-400 mb-3">FEATURES</h2>
                    <div className="flex flex-wrap gap-4">
                        {FEATURES.map((f) => (
                            <div key={f.key} className="flex items-center gap-2">
                                <f.icon className={cn(
                                    "w-4 h-4",
                                    f.color === "purple" && "text-purple-400",
                                    f.color === "amber" && "text-amber-400",
                                    f.color === "blue" && "text-blue-400",
                                    f.color === "emerald" && "text-emerald-400",
                                )} />
                                <span className="text-sm text-zinc-300">{f.label}</span>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Users List */}
                {loading ? (
                    <div className="flex items-center justify-center py-20">
                        <Loader2 className="w-8 h-8 text-purple-500 animate-spin" />
                    </div>
                ) : (
                    <div className="space-y-3">
                        {filteredUsers.map((u) => (
                            <div
                                key={u.id}
                                className="bg-zinc-900/60 border border-zinc-800 rounded-xl p-4"
                            >
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center gap-3">
                                        <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-500/30 to-blue-500/30 flex items-center justify-center">
                                            <Users className="w-5 h-5 text-purple-400" />
                                        </div>
                                        <div>
                                            <p className="font-medium">{u.full_name || "Ingen namn"}</p>
                                            <p className="text-sm text-zinc-500">{u.email}</p>
                                        </div>
                                    </div>

                                    <div className="flex items-center gap-2">
                                        {/* Feature Toggles */}
                                        {FEATURES.map((f) => (
                                            <button
                                                key={f.key}
                                                onClick={() => togglePermission(u.id, f.key)}
                                                className={cn(
                                                    "w-10 h-10 rounded-lg flex items-center justify-center transition-all",
                                                    u.permissions[f.key]
                                                        ? "bg-emerald-500/20 text-emerald-400"
                                                        : "bg-red-500/20 text-red-400"
                                                )}
                                                title={`${f.label}: ${u.permissions[f.key] ? "Aktiverad" : "Avaktiverad"}`}
                                            >
                                                {u.permissions[f.key] ? (
                                                    <Unlock className="w-4 h-4" />
                                                ) : (
                                                    <Lock className="w-4 h-4" />
                                                )}
                                            </button>
                                        ))}

                                        {/* Save button */}
                                        {changes.has(u.id) && (
                                            <button
                                                onClick={() => savePermissions(u.id)}
                                                disabled={saving === u.id}
                                                className={cn(
                                                    "ml-2 px-4 py-2 rounded-lg",
                                                    "bg-purple-600 hover:bg-purple-500",
                                                    "text-sm font-medium transition-colors",
                                                    "disabled:opacity-50"
                                                )}
                                            >
                                                {saving === u.id ? (
                                                    <Loader2 className="w-4 h-4 animate-spin" />
                                                ) : (
                                                    <Save className="w-4 h-4" />
                                                )}
                                            </button>
                                        )}
                                    </div>
                                </div>
                            </div>
                        ))}

                        {filteredUsers.length === 0 && (
                            <div className="text-center py-12 text-zinc-500">
                                Inga användare hittades
                            </div>
                        )}
                    </div>
                )}
            </div>
        </div>
    )
}
