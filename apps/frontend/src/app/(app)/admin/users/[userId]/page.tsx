"use client"

/**
 * ============================================================================
 * ADMIN USER DETAIL PAGE — View & Edit User Profile
 * ============================================================================
 *
 * Full user management:
 * - View complete profile
 * - Edit user details
 * - Reset password
 * - Activate/deactivate
 * - View activity history
 *
 * @phase Admin
 * @access Admin only
 */

import { useEffect, useState, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import { useAuth } from "@/components/auth/AuthProvider"
import { getToken } from "@/lib/auth"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    ArrowLeft,
    User,
    Mail,
    Calendar,
    Shield,
    Loader2,
    Save,
    Key,
    Trash2,
    Power,
    AlertTriangle,
    CheckCircle,
    XCircle,
    Zap,
    Trophy,
    Target,
    Flame,
    Clock,
    BookOpen,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import Link from "next/link"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

interface AdminUser {
    id: string
    full_name: string | null
    email: string
    avatar_url?: string | null
    bio?: string | null
    is_active: boolean
    is_admin: boolean
    is_verified?: boolean
    created_at: string
    updated_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    current_streak?: number
    longest_streak?: number
    tasks_completed: number
    modules_started?: number
    modules_completed: number
    labs_completed?: number
    projects_completed?: number
    total_study_time?: number
}

export default function AdminUserDetailPage() {
    const params = useParams()
    const router = useRouter()
    const { user: currentUser, loading: authLoading } = useAuth()
    const userId = params?.userId as string | undefined

    const [user, setUser] = useState<AdminUser | null>(null)
    const [loading, setLoading] = useState(true)
    const [saving, setSaving] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [successMessage, setSuccessMessage] = useState<string | null>(null)

    // Form state
    const [isActive, setIsActive] = useState(true)
    const [isAdmin, setIsAdmin] = useState(false)
    const [totalXp, setTotalXp] = useState(0)

    // Password reset
    const [newPassword, setNewPassword] = useState("")
    const [showPasswordReset, setShowPasswordReset] = useState(false)

    const isCurrentUserAdmin = currentUser?.email?.toLowerCase() === ADMIN_EMAIL

    const fetchUser = useCallback(async () => {
        if (!userId) return

        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${userId}`, {
                headers: { Authorization: `Bearer ${token}` },
            })

            if (!res.ok) {
                if (res.status === 404) {
                    setError("Användaren hittades inte")
                    return
                }
                throw new Error("Failed to fetch user")
            }

            const userData: AdminUser = await res.json()
            setUser(userData)
            setIsActive(userData.is_active)
            setIsAdmin(userData.is_admin)
            setTotalXp(userData.total_xp)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Ett fel uppstod")
        } finally {
            setLoading(false)
        }
    }, [userId])

    useEffect(() => {
        if (authLoading) return

        if (!currentUser || !isCurrentUserAdmin) {
            router.push("/dashboard")
            return
        }

        fetchUser()
    }, [currentUser, authLoading, isCurrentUserAdmin, router, fetchUser])

    const handleSave = async () => {
        if (!user) return

        setSaving(true)
        setError(null)
        setSuccessMessage(null)

        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${user.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({
                    is_active: isActive,
                    is_admin: isAdmin,
                    total_xp: totalXp,
                }),
            })

            if (!res.ok) {
                throw new Error("Failed to update user")
            }

            const updated: AdminUser = await res.json()
            setUser(updated)
            setSuccessMessage("Användaren uppdaterad!")
            setTimeout(() => setSuccessMessage(null), 3000)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Kunde inte spara ändringar")
        } finally {
            setSaving(false)
        }
    }

    const handleResetPassword = async () => {
        if (!user || !newPassword) return

        setSaving(true)
        setError(null)

        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${user.id}/reset-password`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ new_password: newPassword }),
            })

            if (!res.ok) {
                throw new Error("Failed to reset password")
            }

            setSuccessMessage("Lösenord återställt!")
            setNewPassword("")
            setShowPasswordReset(false)
            setTimeout(() => setSuccessMessage(null), 3000)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Kunde inte återställa lösenord")
        } finally {
            setSaving(false)
        }
    }

    const handleDeactivate = async () => {
        if (!user) return
        if (!confirm(`Är du säker på att du vill ${user.is_active ? "inaktivera" : "aktivera"} ${user.email}?`)) {
            return
        }

        setSaving(true)
        try {
            const token = getToken()
            const res = await fetch(`${API_BASE_URL}/api/admin/users/${user.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ is_active: !user.is_active }),
            })

            if (!res.ok) {
                throw new Error("Failed to update user status")
            }

            const updated: AdminUser = await res.json()
            setUser(updated)
            setIsActive(updated.is_active)
            setSuccessMessage(`Användaren ${updated.is_active ? "aktiverad" : "inaktiverad"}!`)
            setTimeout(() => setSuccessMessage(null), 3000)
        } catch (err) {
            setError(err instanceof Error ? err.message : "Kunde inte uppdatera status")
        } finally {
            setSaving(false)
        }
    }

    if (authLoading || loading) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <Loader2 className="w-8 h-8 text-purple-500 animate-spin" />
            </div>
        )
    }

    if (!isCurrentUserAdmin) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-white mb-2">Åtkomst nekad</h1>
                </div>
            </div>
        )
    }

    if (error && !user) {
        return (
            <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
                <div className="text-center">
                    <AlertTriangle className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-white mb-2">{error}</h1>
                    <Link href="/admin">
                        <Button variant="outline" className="mt-4">
                            <ArrowLeft className="w-4 h-4 mr-2" />
                            Tillbaka
                        </Button>
                    </Link>
                </div>
            </div>
        )
    }

    if (!user) return null

    return (
        <div className="min-h-screen bg-zinc-950 p-6 lg:p-8">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <Link
                    href="/admin"
                    className="inline-flex items-center gap-2 text-zinc-400 hover:text-white mb-4"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka till Admin
                </Link>

                <div className="flex items-center gap-4">
                    <div className={cn(
                        "w-16 h-16 rounded-2xl flex items-center justify-center",
                        "bg-gradient-to-br from-purple-500 to-indigo-600",
                        "text-white font-bold text-2xl"
                    )}>
                        {user.full_name?.[0]?.toUpperCase() || user.email[0].toUpperCase()}
                    </div>
                    <div>
                        <h1 className="text-2xl font-bold text-white">
                            {user.full_name || "Inget namn"}
                        </h1>
                        <p className="text-zinc-400">{user.email}</p>
                    </div>
                </div>
            </motion.div>

            {/* Messages */}
            {successMessage && (
                <motion.div
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-6 p-4 rounded-xl bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 flex items-center gap-2"
                >
                    <CheckCircle className="w-5 h-5" />
                    {successMessage}
                </motion.div>
            )}

            {error && user && (
                <motion.div
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-6 p-4 rounded-xl bg-red-500/20 border border-red-500/30 text-red-400 flex items-center gap-2"
                >
                    <XCircle className="w-5 h-5" />
                    {error}
                </motion.div>
            )}

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Stats Column */}
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="space-y-4"
                >
                    <div className={cn(
                        "p-6 rounded-2xl",
                        "bg-zinc-900/80 border border-zinc-800"
                    )}>
                        <h3 className="font-semibold text-white mb-4 flex items-center gap-2">
                            <Trophy className="w-5 h-5 text-amber-400" />
                            Statistik
                        </h3>
                        <div className="space-y-4">
                            <div className="flex items-center justify-between">
                                <span className="text-zinc-400">Nivå</span>
                                <span className="text-xl font-bold text-amber-400">
                                    {user.level}
                                </span>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-zinc-400">Total XP</span>
                                <span className="text-xl font-bold text-purple-400">
                                    {user.total_xp.toLocaleString()}
                                </span>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-zinc-400">Tasks klara</span>
                                <span className="text-xl font-bold text-emerald-400">
                                    {user.tasks_completed}
                                </span>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-zinc-400">Moduler klara</span>
                                <span className="text-lg font-semibold text-white">
                                    {user.modules_completed}
                                </span>
                            </div>
                            <div className="flex items-center justify-between">
                                <span className="text-zinc-400">Streak</span>
                                <span className="text-lg font-semibold text-orange-400 flex items-center gap-1">
                                    <Flame className="w-4 h-4" />
                                    {user.current_streak || 0}
                                </span>
                            </div>
                        </div>
                    </div>

                    <div className={cn(
                        "p-6 rounded-2xl",
                        "bg-zinc-900/80 border border-zinc-800"
                    )}>
                        <h3 className="font-semibold text-white mb-4 flex items-center gap-2">
                            <Clock className="w-5 h-5 text-blue-400" />
                            Tidslinje
                        </h3>
                        <div className="space-y-3 text-sm">
                            <div>
                                <span className="text-zinc-500">Registrerad:</span>
                                <p className="text-white">
                                    {new Date(user.created_at).toLocaleDateString("sv-SE", {
                                        year: "numeric",
                                        month: "long",
                                        day: "numeric",
                                        hour: "2-digit",
                                        minute: "2-digit"
                                    })}
                                </p>
                            </div>
                            <div>
                                <span className="text-zinc-500">Senast aktiv:</span>
                                <p className="text-white">
                                    {user.last_activity_at
                                        ? new Date(user.last_activity_at).toLocaleDateString("sv-SE", {
                                            year: "numeric",
                                            month: "long",
                                            day: "numeric",
                                            hour: "2-digit",
                                            minute: "2-digit"
                                        })
                                        : "Aldrig"
                                    }
                                </p>
                            </div>
                        </div>
                    </div>
                </motion.div>

                {/* Edit Form */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="lg:col-span-2 space-y-6"
                >
                    {/* User Settings */}
                    <div className={cn(
                        "p-6 rounded-2xl",
                        "bg-zinc-900/80 border border-zinc-800"
                    )}>
                        <h3 className="font-semibold text-white mb-6 flex items-center gap-2">
                            <User className="w-5 h-5 text-purple-400" />
                            Användarinställningar
                        </h3>

                        <div className="space-y-6">
                            {/* Status Toggle */}
                            <div className="flex items-center justify-between p-4 rounded-xl bg-zinc-800/50">
                                <div>
                                    <p className="font-medium text-white">Aktiv</p>
                                    <p className="text-sm text-zinc-500">
                                        Användaren kan logga in och använda plattformen
                                    </p>
                                </div>
                                <button
                                    onClick={() => setIsActive(!isActive)}
                                    className={cn(
                                        "w-12 h-6 rounded-full transition-colors",
                                        isActive ? "bg-emerald-500" : "bg-zinc-600"
                                    )}
                                >
                                    <div className={cn(
                                        "w-5 h-5 rounded-full bg-white shadow transition-transform",
                                        isActive ? "translate-x-6" : "translate-x-0.5"
                                    )} />
                                </button>
                            </div>

                            {/* Admin Toggle */}
                            <div className="flex items-center justify-between p-4 rounded-xl bg-zinc-800/50">
                                <div>
                                    <p className="font-medium text-white flex items-center gap-2">
                                        <Shield className="w-4 h-4 text-amber-400" />
                                        Admin
                                    </p>
                                    <p className="text-sm text-zinc-500">
                                        Ger tillgång till Admin Command Center
                                    </p>
                                </div>
                                <button
                                    onClick={() => setIsAdmin(!isAdmin)}
                                    className={cn(
                                        "w-12 h-6 rounded-full transition-colors",
                                        isAdmin ? "bg-amber-500" : "bg-zinc-600"
                                    )}
                                >
                                    <div className={cn(
                                        "w-5 h-5 rounded-full bg-white shadow transition-transform",
                                        isAdmin ? "translate-x-6" : "translate-x-0.5"
                                    )} />
                                </button>
                            </div>

                            {/* XP Adjustment */}
                            <div className="p-4 rounded-xl bg-zinc-800/50">
                                <p className="font-medium text-white mb-2 flex items-center gap-2">
                                    <Zap className="w-4 h-4 text-purple-400" />
                                    Total XP
                                </p>
                                <input
                                    type="number"
                                    value={totalXp}
                                    onChange={(e) => setTotalXp(parseInt(e.target.value) || 0)}
                                    className={cn(
                                        "w-full px-4 py-2 rounded-lg",
                                        "bg-zinc-900 border border-zinc-700",
                                        "text-white",
                                        "focus:outline-none focus:border-purple-500"
                                    )}
                                />
                                <p className="text-xs text-zinc-500 mt-1">
                                    Justera XP manuellt om användaren stött på problem
                                </p>
                            </div>

                            {/* Save Button */}
                            <Button
                                onClick={handleSave}
                                disabled={saving}
                                className="w-full bg-purple-600 hover:bg-purple-500"
                            >
                                {saving ? (
                                    <Loader2 className="w-4 h-4 animate-spin mr-2" />
                                ) : (
                                    <Save className="w-4 h-4 mr-2" />
                                )}
                                Spara ändringar
                            </Button>
                        </div>
                    </div>

                    {/* Password Reset */}
                    <div className={cn(
                        "p-6 rounded-2xl",
                        "bg-zinc-900/80 border border-zinc-800"
                    )}>
                        <h3 className="font-semibold text-white mb-4 flex items-center gap-2">
                            <Key className="w-5 h-5 text-amber-400" />
                            Lösenordsåterställning
                        </h3>

                        {showPasswordReset ? (
                            <div className="space-y-4">
                                <input
                                    type="password"
                                    placeholder="Nytt lösenord"
                                    value={newPassword}
                                    onChange={(e) => setNewPassword(e.target.value)}
                                    className={cn(
                                        "w-full px-4 py-2 rounded-lg",
                                        "bg-zinc-800 border border-zinc-700",
                                        "text-white placeholder-zinc-500",
                                        "focus:outline-none focus:border-amber-500"
                                    )}
                                />
                                <div className="flex gap-3">
                                    <Button
                                        onClick={handleResetPassword}
                                        disabled={saving || !newPassword}
                                        className="bg-amber-600 hover:bg-amber-500"
                                    >
                                        {saving ? (
                                            <Loader2 className="w-4 h-4 animate-spin mr-2" />
                                        ) : null}
                                        Återställ lösenord
                                    </Button>
                                    <Button
                                        variant="outline"
                                        onClick={() => {
                                            setShowPasswordReset(false)
                                            setNewPassword("")
                                        }}
                                    >
                                        Avbryt
                                    </Button>
                                </div>
                            </div>
                        ) : (
                            <Button
                                variant="outline"
                                onClick={() => setShowPasswordReset(true)}
                                className="border-amber-500/30 text-amber-400 hover:bg-amber-500/10"
                            >
                                <Key className="w-4 h-4 mr-2" />
                                Återställ lösenord
                            </Button>
                        )}
                    </div>

                    {/* Danger Zone */}
                    <div className={cn(
                        "p-6 rounded-2xl",
                        "bg-red-950/30 border border-red-900/50"
                    )}>
                        <h3 className="font-semibold text-red-400 mb-4 flex items-center gap-2">
                            <AlertTriangle className="w-5 h-5" />
                            Farlig zon
                        </h3>

                        <Button
                            variant="outline"
                            onClick={handleDeactivate}
                            disabled={saving || user.email === ADMIN_EMAIL}
                            className={cn(
                                "border-red-500/30",
                                user.is_active
                                    ? "text-red-400 hover:bg-red-500/10"
                                    : "text-emerald-400 hover:bg-emerald-500/10 border-emerald-500/30"
                            )}
                        >
                            <Power className="w-4 h-4 mr-2" />
                            {user.is_active ? "Inaktivera användare" : "Aktivera användare"}
                        </Button>

                        {user.email === ADMIN_EMAIL && (
                            <p className="text-xs text-zinc-500 mt-2">
                                Du kan inte inaktivera ditt eget admin-konto.
                            </p>
                        )}
                    </div>
                </motion.div>
            </div>
        </div>
    )
}
