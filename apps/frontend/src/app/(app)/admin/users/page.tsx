"use client"

/**
 * ============================================================================
 * ADMIN USERS PAGE — User Management for Admins
 * ============================================================================
 *
 * Features:
 * - List all users with stats
 * - Only visible to admin (said.ebadi@hotmail.com)
 *
 * @phase Admin
 */

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import { useAuth } from "@/components/auth"
import { getToken } from "@/lib/auth"
import {
    Users,
    Trophy,
    Flame,
    CheckCircle,
    Calendar,
    Shield,
    Loader2,
} from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
const ADMIN_EMAIL = "said.ebadi@hotmail.com"

interface AdminUser {
    id: string
    full_name: string | null
    email: string
    created_at: string
    total_xp: number
    level: number
    tasks_completed: number
}

interface AdminUsersResponse {
    users: AdminUser[]
    total: number
}

export default function AdminUsersPage() {
    const { user, loading: authLoading } = useAuth()
    const router = useRouter()
    const [users, setUsers] = useState<AdminUser[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    // Check if current user is admin
    const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL

    useEffect(() => {
        // Wait for auth to load
        if (authLoading) return

        // Redirect non-admins
        if (!user || !isAdmin) {
            router.push("/dashboard")
            return
        }

        // Fetch users
        const fetchUsers = async () => {
            try {
                const token = getToken()
                const res = await fetch(`${API_BASE_URL}/api/admin/users`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                })

                if (!res.ok) {
                    if (res.status === 403) {
                        router.push("/dashboard")
                        return
                    }
                    throw new Error("Failed to fetch users")
                }

                const data: AdminUsersResponse = await res.json()
                setUsers(data.users)
            } catch (err) {
                setError(err instanceof Error ? err.message : "An error occurred")
            } finally {
                setLoading(false)
            }
        }

        fetchUsers()
    }, [user, authLoading, isAdmin, router])

    // Format date
    const formatDate = (dateString: string) => {
        return new Date(dateString).toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric",
        })
    }

    // Loading state
    if (authLoading || loading) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="flex flex-col items-center gap-4">
                    <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
                    <p className="text-gray-500">Loading users...</p>
                </div>
            </div>
        )
    }

    // Not admin - should redirect, but show message just in case
    if (!isAdmin) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="text-center">
                    <Shield className="w-16 h-16 text-red-400 mx-auto mb-4" />
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                        Access Denied
                    </h1>
                    <p className="text-gray-500">
                        You don&apos;t have permission to view this page.
                    </p>
                </div>
            </div>
        )
    }

    // Error state
    if (error) {
        return (
            <div className="flex items-center justify-center min-h-[60vh]">
                <div className="text-center">
                    <p className="text-red-500">{error}</p>
                </div>
            </div>
        )
    }

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            {/* Header */}
            <div className="mb-8">
                <div className="flex items-center gap-3 mb-2">
                    <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center">
                        <Shield className="w-5 h-5 text-white" />
                    </div>
                    <div>
                        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Admin: Users
                        </h1>
                        <p className="text-sm text-gray-500">
                            {users.length} registered users
                        </p>
                    </div>
                </div>
            </div>

            {/* Users Table */}
            <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead>
                            <tr className="bg-gray-50 dark:bg-gray-900/50 border-b border-gray-200 dark:border-gray-700">
                                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center gap-2">
                                        <Users className="w-4 h-4" />
                                        User
                                    </div>
                                </th>
                                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center gap-2">
                                        <Calendar className="w-4 h-4" />
                                        Joined
                                    </div>
                                </th>
                                <th className="px-6 py-4 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-2">
                                        <Trophy className="w-4 h-4" />
                                        Level
                                    </div>
                                </th>
                                <th className="px-6 py-4 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-2">
                                        <Flame className="w-4 h-4" />
                                        XP
                                    </div>
                                </th>
                                <th className="px-6 py-4 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                    <div className="flex items-center justify-center gap-2">
                                        <CheckCircle className="w-4 h-4" />
                                        Tasks Done
                                    </div>
                                </th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
                            {users.map((u) => (
                                <tr
                                    key={u.id}
                                    className="hover:bg-gray-50 dark:hover:bg-gray-900/30 transition-colors"
                                >
                                    <td className="px-6 py-4">
                                        <div className="flex items-center gap-3">
                                            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white font-bold">
                                                {u.full_name?.[0]?.toUpperCase() ||
                                                    u.email[0].toUpperCase()}
                                            </div>
                                            <div>
                                                <p className="font-medium text-gray-900 dark:text-white">
                                                    {u.full_name || "No name"}
                                                </p>
                                                <p className="text-sm text-gray-500">
                                                    {u.email}
                                                </p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="px-6 py-4 text-gray-600 dark:text-gray-400">
                                        {formatDate(u.created_at)}
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-semibold bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400">
                                            Lvl {u.level}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-semibold bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400">
                                            {u.total_xp.toLocaleString()} XP
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 text-center">
                                        <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-semibold bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400">
                                            {u.tasks_completed}
                                        </span>
                                    </td>
                                </tr>
                            ))}

                            {users.length === 0 && (
                                <tr>
                                    <td
                                        colSpan={5}
                                        className="px-6 py-12 text-center text-gray-500"
                                    >
                                        No users found
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}
