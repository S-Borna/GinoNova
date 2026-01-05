"use client"

/**
 * Admin v2 User Detail - Full user profile with tabs
 */

import { useEffect, useState, useCallback } from "react"
import { useParams, useRouter } from "next/navigation"
import Link from "next/link"
import Image from "next/image"
import {
    ArrowLeft,
    RefreshCw,
    User as UserIcon,
    Mail,
    Calendar,
    Clock,
    Shield,
    Ban,
    LogOut,
    Trash2,
    Activity,
    BookOpen,
    Brain,
    BarChart3,
    Settings,
    Save,
    X,
    Check,
    Flame
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || ""

// Types
interface UserDetail {
    id: string
    email: string
    full_name: string | null
    avatar_url: string | null
    is_admin: boolean
    is_banned: boolean
    is_active: boolean
    is_verified: boolean
    oauth_provider: string | null
    created_at: string
    last_activity_at: string | null
    total_xp: number
    level: number
    current_streak: number
    permissions: {
        ai_quiz_access: boolean
        premium_modules_access: boolean
        study_room_access: boolean
        skillpath_access: boolean
    }
    stats: {
        modules_completed: number
        tasks_completed: number
        study_sessions: number
        ai_requests: number
    }
    status: "online" | "away" | "offline"
}

interface ActivityItem {
    id: string
    type: string
    description: string
    timestamp: string
    metadata?: Record<string, unknown>
}

interface LearningData {
    modules: Array<{
        id: string
        name: string
        progress: number
        completed_at?: string
    }>
    skill_paths: Array<{
        id: string
        name: string
        progress: number
    }>
    recent_tasks: Array<{
        id: string
        title: string
        completed_at: string
    }>
}

interface AIUsageData {
    total_requests: number
    tokens_used: number
    requests_by_day: Array<{ date: string; count: number }>
    top_features: Array<{ name: string; count: number }>
}

type TabId = "overview" | "activity" | "learning" | "ai"

// Tab Components
function OverviewTab({ user, onUpdate }: { user: UserDetail, onUpdate: () => void }) {
    const [editing, setEditing] = useState(false)
    const [loading, setLoading] = useState(false)
    const [permissions, setPermissions] = useState(user.permissions)
    
    const savePermissions = async () => {
        const token = getToken()
        if (!token) return
        
        setLoading(true)
        try {
            const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${user.id}`, {
                method: "PUT",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ permissions })
            })
            
            if (res.ok) {
                setEditing(false)
                onUpdate()
            }
        } finally {
            setLoading(false)
        }
    }
    
    const statCards = [
        { label: "Total XP", value: user.total_xp.toLocaleString(), icon: BarChart3, color: "text-purple-400" },
        { label: "Level", value: user.level, icon: Shield, color: "text-blue-400" },
        { label: "Streak", value: `${user.current_streak} days`, icon: Flame, color: "text-orange-400" },
        { label: "Modules", value: user.stats.modules_completed, icon: BookOpen, color: "text-green-400" },
        { label: "Tasks", value: user.stats.tasks_completed, icon: Check, color: "text-emerald-400" },
        { label: "Study Sessions", value: user.stats.study_sessions, icon: Clock, color: "text-cyan-400" },
        { label: "AI Requests", value: user.stats.ai_requests, icon: Brain, color: "text-pink-400" }
    ]
    
    return (
        <div className="space-y-6">
            {/* Stats Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {statCards.map(card => (
                    <div key={card.label} className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4">
                        <card.icon className={cn("w-5 h-5 mb-2", card.color)} />
                        <div className="text-2xl font-bold">{card.value}</div>
                        <div className="text-xs text-zinc-500">{card.label}</div>
                    </div>
                ))}
            </div>
            
            {/* Account Info */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                <h3 className="font-semibold mb-4">Account Information</h3>
                <div className="grid md:grid-cols-2 gap-4 text-sm">
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">User ID</span>
                        <span className="font-mono text-xs">{user.id}</span>
                    </div>
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">OAuth Provider</span>
                        <span>{user.oauth_provider || "None"}</span>
                    </div>
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">Email Verified</span>
                        <span className={user.is_verified ? "text-green-400" : "text-red-400"}>
                            {user.is_verified ? "Yes" : "No"}
                        </span>
                    </div>
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">Account Status</span>
                        <span className={user.is_active ? "text-green-400" : "text-red-400"}>
                            {user.is_banned ? "Banned" : user.is_active ? "Active" : "Inactive"}
                        </span>
                    </div>
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">Created</span>
                        <span>{new Date(user.created_at).toLocaleDateString("sv-SE")}</span>
                    </div>
                    <div className="flex justify-between py-2 border-b border-zinc-800">
                        <span className="text-zinc-400">Last Active</span>
                        <span>
                            {user.last_activity_at 
                                ? new Date(user.last_activity_at).toLocaleString("sv-SE")
                                : "Never"}
                        </span>
                    </div>
                </div>
            </div>
            
            {/* Permissions */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold">Permissions</h3>
                    {editing ? (
                        <div className="flex gap-2">
                            <button
                                onClick={() => { setPermissions(user.permissions); setEditing(false) }}
                                className="p-2 rounded-lg bg-zinc-800 hover:bg-zinc-700"
                            >
                                <X className="w-4 h-4" />
                            </button>
                            <button
                                onClick={savePermissions}
                                disabled={loading}
                                className="flex items-center gap-2 px-3 py-2 bg-green-600 hover:bg-green-700 rounded-lg text-sm"
                            >
                                {loading ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Save className="w-4 h-4" />}
                                Save
                            </button>
                        </div>
                    ) : (
                        <button
                            onClick={() => setEditing(true)}
                            className="px-3 py-2 bg-zinc-800 hover:bg-zinc-700 rounded-lg text-sm"
                        >
                            Edit
                        </button>
                    )}
                </div>
                
                <div className="space-y-3">
                    {Object.entries(permissions).map(([key, value]) => (
                        <div key={key} className="flex items-center justify-between py-2 border-b border-zinc-800">
                            <span className="text-sm">
                                {key.split("_").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ")}
                            </span>
                            {editing ? (
                                <button
                                    onClick={() => setPermissions(p => ({ ...p, [key]: !p[key as keyof typeof p] }))}
                                    className={cn(
                                        "w-12 h-6 rounded-full transition",
                                        value ? "bg-green-600" : "bg-zinc-700"
                                    )}
                                >
                                    <div className={cn(
                                        "w-5 h-5 rounded-full bg-white transition-transform",
                                        value ? "translate-x-6" : "translate-x-0.5"
                                    )} />
                                </button>
                            ) : (
                                <span className={cn(
                                    "px-2 py-1 rounded text-xs font-medium",
                                    value ? "bg-green-500/20 text-green-400" : "bg-red-500/20 text-red-400"
                                )}>
                                    {value ? "Enabled" : "Disabled"}
                                </span>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

function ActivityTab({ userId }: { userId: string }) {
    const [activities, setActivities] = useState<ActivityItem[]>([])
    const [loading, setLoading] = useState(true)
    
    useEffect(() => {
        async function fetchActivity() {
            const token = getToken()
            if (!token) return
            
            try {
                const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${userId}/activity`, {
                    headers: { Authorization: `Bearer ${token}` }
                })
                
                if (res.ok) {
                    const data = await res.json()
                    setActivities(data.activities || [])
                }
            } finally {
                setLoading(false)
            }
        }
        
        fetchActivity()
    }, [userId])
    
    const getActivityIcon = (type: string) => {
        switch (type) {
            case "login": return <UserIcon className="w-4 h-4 text-blue-400" />
            case "module": return <BookOpen className="w-4 h-4 text-green-400" />
            case "task": return <Check className="w-4 h-4 text-emerald-400" />
            case "ai": return <Brain className="w-4 h-4 text-pink-400" />
            default: return <Activity className="w-4 h-4 text-zinc-400" />
        }
    }
    
    if (loading) {
        return (
            <div className="space-y-4">
                {[...Array(10)].map((_, i) => (
                    <div key={i} className="animate-pulse flex gap-4">
                        <div className="w-8 h-8 bg-zinc-800 rounded-full" />
                        <div className="flex-1 space-y-2">
                            <div className="h-4 w-3/4 bg-zinc-800 rounded" />
                            <div className="h-3 w-1/4 bg-zinc-800 rounded" />
                        </div>
                    </div>
                ))}
            </div>
        )
    }
    
    if (activities.length === 0) {
        return (
            <div className="text-center py-12 text-zinc-500">
                No activity recorded yet
            </div>
        )
    }
    
    return (
        <div className="space-y-4">
            {activities.map((activity) => (
                <div 
                    key={activity.id}
                    className="flex gap-4 p-4 bg-zinc-900/50 border border-zinc-800 rounded-xl"
                >
                    <div className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center">
                        {getActivityIcon(activity.type)}
                    </div>
                    <div className="flex-1">
                        <p className="text-sm">{activity.description}</p>
                        <p className="text-xs text-zinc-500 mt-1">
                            {new Date(activity.timestamp).toLocaleString("sv-SE")}
                        </p>
                    </div>
                </div>
            ))}
        </div>
    )
}

function LearningTab({ userId }: { userId: string }) {
    const [data, setData] = useState<LearningData | null>(null)
    const [loading, setLoading] = useState(true)
    
    useEffect(() => {
        async function fetchLearning() {
            const token = getToken()
            if (!token) return
            
            try {
                const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${userId}/learning`, {
                    headers: { Authorization: `Bearer ${token}` }
                })
                
                if (res.ok) {
                    setData(await res.json())
                }
            } finally {
                setLoading(false)
            }
        }
        
        fetchLearning()
    }, [userId])
    
    if (loading) {
        return <div className="animate-pulse space-y-4">
            {[...Array(3)].map((_, i) => (
                <div key={i} className="h-20 bg-zinc-800 rounded-xl" />
            ))}
        </div>
    }
    
    if (!data) {
        return <div className="text-center py-12 text-zinc-500">No learning data available</div>
    }
    
    return (
        <div className="space-y-6">
            {/* Modules */}
            <div>
                <h3 className="font-semibold mb-4">Modules Progress</h3>
                {data.modules.length === 0 ? (
                    <p className="text-zinc-500 text-sm">No modules started</p>
                ) : (
                    <div className="space-y-3">
                        {data.modules.map(module => (
                            <div key={module.id} className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4">
                                <div className="flex justify-between mb-2">
                                    <span className="font-medium">{module.name}</span>
                                    <span className="text-sm text-zinc-400">{module.progress}%</span>
                                </div>
                                <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                    <div 
                                        className={cn(
                                            "h-full rounded-full transition-all",
                                            module.progress === 100 ? "bg-green-500" : "bg-purple-500"
                                        )}
                                        style={{ width: `${module.progress}%` }}
                                    />
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
            
            {/* Skill Paths */}
            <div>
                <h3 className="font-semibold mb-4">Skill Paths</h3>
                {data.skill_paths.length === 0 ? (
                    <p className="text-zinc-500 text-sm">No skill paths started</p>
                ) : (
                    <div className="space-y-3">
                        {data.skill_paths.map(path => (
                            <div key={path.id} className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-4">
                                <div className="flex justify-between mb-2">
                                    <span className="font-medium">{path.name}</span>
                                    <span className="text-sm text-zinc-400">{path.progress}%</span>
                                </div>
                                <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                    <div 
                                        className="h-full bg-blue-500 rounded-full"
                                        style={{ width: `${path.progress}%` }}
                                    />
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
            
            {/* Recent Tasks */}
            <div>
                <h3 className="font-semibold mb-4">Recent Completed Tasks</h3>
                {data.recent_tasks.length === 0 ? (
                    <p className="text-zinc-500 text-sm">No tasks completed</p>
                ) : (
                    <div className="space-y-2">
                        {data.recent_tasks.map(task => (
                            <div key={task.id} className="flex justify-between items-center py-2 border-b border-zinc-800">
                                <span className="text-sm">{task.title}</span>
                                <span className="text-xs text-zinc-500">
                                    {new Date(task.completed_at).toLocaleDateString("sv-SE")}
                                </span>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    )
}

function AIUsageTab({ userId }: { userId: string }) {
    const [data, setData] = useState<AIUsageData | null>(null)
    const [loading, setLoading] = useState(true)
    
    useEffect(() => {
        async function fetchAI() {
            const token = getToken()
            if (!token) return
            
            try {
                const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${userId}/ai-usage`, {
                    headers: { Authorization: `Bearer ${token}` }
                })
                
                if (res.ok) {
                    setData(await res.json())
                }
            } finally {
                setLoading(false)
            }
        }
        
        fetchAI()
    }, [userId])
    
    if (loading) {
        return <div className="animate-pulse space-y-4">
            <div className="h-32 bg-zinc-800 rounded-xl" />
            <div className="h-48 bg-zinc-800 rounded-xl" />
        </div>
    }
    
    if (!data) {
        return <div className="text-center py-12 text-zinc-500">No AI usage data available</div>
    }
    
    return (
        <div className="space-y-6">
            {/* Summary */}
            <div className="grid md:grid-cols-2 gap-4">
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                    <Brain className="w-6 h-6 text-pink-400 mb-2" />
                    <div className="text-3xl font-bold">{data.total_requests.toLocaleString()}</div>
                    <div className="text-sm text-zinc-500">Total AI Requests</div>
                </div>
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                    <BarChart3 className="w-6 h-6 text-purple-400 mb-2" />
                    <div className="text-3xl font-bold">{data.tokens_used.toLocaleString()}</div>
                    <div className="text-sm text-zinc-500">Tokens Used</div>
                </div>
            </div>
            
            {/* Daily Chart */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                <h3 className="font-semibold mb-4">Requests Last 7 Days</h3>
                <div className="flex items-end gap-2 h-32">
                    {data.requests_by_day.map((day, i) => {
                        const max = Math.max(...data.requests_by_day.map(d => d.count), 1)
                        const height = (day.count / max) * 100
                        return (
                            <div key={i} className="flex-1 flex flex-col items-center gap-2">
                                <div 
                                    className="w-full bg-purple-500 rounded-t"
                                    style={{ height: `${height}%`, minHeight: day.count > 0 ? 4 : 0 }}
                                />
                                <span className="text-xs text-zinc-500">
                                    {new Date(day.date).toLocaleDateString("sv-SE", { weekday: "short" })}
                                </span>
                            </div>
                        )
                    })}
                </div>
            </div>
            
            {/* Top Features */}
            <div className="bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                <h3 className="font-semibold mb-4">Top Features Used</h3>
                {data.top_features.length === 0 ? (
                    <p className="text-zinc-500 text-sm">No features used yet</p>
                ) : (
                    <div className="space-y-3">
                        {data.top_features.map((feature, i) => {
                            const max = Math.max(...data.top_features.map(f => f.count), 1)
                            const width = (feature.count / max) * 100
                            return (
                                <div key={i}>
                                    <div className="flex justify-between text-sm mb-1">
                                        <span>{feature.name}</span>
                                        <span className="text-zinc-400">{feature.count}</span>
                                    </div>
                                    <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                        <div 
                                            className="h-full bg-pink-500 rounded-full"
                                            style={{ width: `${width}%` }}
                                        />
                                    </div>
                                </div>
                            )
                        })}
                    </div>
                )}
            </div>
        </div>
    )
}

// Main Component
export default function AdminV2UserDetail() {
    const params = useParams()
    const router = useRouter()
    const userId = params.userId as string
    
    const [user, setUser] = useState<UserDetail | null>(null)
    const [loading, setLoading] = useState(true)
    const [activeTab, setActiveTab] = useState<TabId>("overview")
    const [actionLoading, setActionLoading] = useState(false)
    
    const fetchUser = useCallback(async () => {
        const token = getToken()
        if (!token) return
        
        try {
            const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${userId}`, {
                headers: { Authorization: `Bearer ${token}` }
            })
            
            if (res.ok) {
                setUser(await res.json())
            } else if (res.status === 404) {
                router.push("/admin-v2/users")
            }
        } finally {
            setLoading(false)
        }
    }, [userId, router])
    
    useEffect(() => {
        fetchUser()
    }, [fetchUser])
    
    const executeAction = async (action: string, method = "POST") => {
        const token = getToken()
        if (!token || !user) return
        
        setActionLoading(true)
        
        try {
            const res = await fetch(`${API_BASE_URL}/api/admin-v2/users/${userId}/${action}`, {
                method,
                headers: { Authorization: `Bearer ${token}` }
            })
            
            if (res.ok) {
                fetchUser()
            }
        } finally {
            setActionLoading(false)
        }
    }
    
    const tabs = [
        { id: "overview" as TabId, label: "Overview", icon: UserIcon },
        { id: "activity" as TabId, label: "Activity", icon: Activity },
        { id: "learning" as TabId, label: "Learning", icon: BookOpen },
        { id: "ai" as TabId, label: "AI Usage", icon: Brain }
    ]
    
    if (loading) {
        return (
            <div className="p-6">
                <div className="animate-pulse space-y-6">
                    <div className="h-8 w-32 bg-zinc-800 rounded" />
                    <div className="flex gap-6">
                        <div className="w-24 h-24 bg-zinc-800 rounded-xl" />
                        <div className="space-y-3 flex-1">
                            <div className="h-6 w-48 bg-zinc-800 rounded" />
                            <div className="h-4 w-64 bg-zinc-800 rounded" />
                        </div>
                    </div>
                </div>
            </div>
        )
    }
    
    if (!user) {
        return (
            <div className="p-6 text-center">
                <p className="text-zinc-500">User not found</p>
                <Link href="/admin-v2/users" className="text-purple-400 hover:underline mt-2 inline-block">
                    Back to Users
                </Link>
            </div>
        )
    }
    
    return (
        <div className="p-6">
            {/* Back Button */}
            <Link 
                href="/admin-v2/users"
                className="inline-flex items-center gap-2 text-sm text-zinc-400 hover:text-white mb-6 transition"
            >
                <ArrowLeft className="w-4 h-4" />
                Back to Users
            </Link>
            
            {/* Header */}
            <div className="flex flex-col md:flex-row gap-6 mb-8">
                {/* Avatar */}
                <div className="relative">
                    {user.avatar_url ? (
                        <Image
                            src={user.avatar_url}
                            alt={user.full_name || user.email}
                            width={96}
                            height={96}
                            className="w-24 h-24 rounded-xl object-cover"
                        />
                    ) : (
                        <div className={cn(
                            "w-24 h-24 rounded-xl flex items-center justify-center text-2xl font-bold",
                            user.is_admin 
                                ? "bg-gradient-to-br from-purple-500 to-pink-500"
                                : "bg-zinc-800 text-zinc-400"
                        )}>
                            {user.full_name 
                                ? user.full_name.split(" ").map(n => n[0]).join("").toUpperCase().slice(0, 2)
                                : user.email.slice(0, 2).toUpperCase()}
                        </div>
                    )}
                    {/* Status */}
                    <div className={cn(
                        "absolute -bottom-1 -right-1 w-5 h-5 rounded-full border-4 border-zinc-950",
                        user.status === "online" && "bg-green-500",
                        user.status === "away" && "bg-yellow-500",
                        user.status === "offline" && "bg-zinc-600",
                        user.is_banned && "bg-red-500"
                    )} />
                </div>
                
                {/* Info */}
                <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                        <h1 className="text-2xl font-bold">{user.full_name || user.email}</h1>
                        {user.is_admin && (
                            <span className="px-2 py-1 text-xs font-bold rounded bg-purple-500/20 text-purple-400">
                                ADMIN
                            </span>
                        )}
                        {user.is_banned && (
                            <span className="px-2 py-1 text-xs font-bold rounded bg-red-500/20 text-red-400">
                                BANNED
                            </span>
                        )}
                    </div>
                    <div className="flex items-center gap-4 text-sm text-zinc-400">
                        <span className="flex items-center gap-1">
                            <Mail className="w-4 h-4" />
                            {user.email}
                        </span>
                        <span className="flex items-center gap-1">
                            <Calendar className="w-4 h-4" />
                            Joined {new Date(user.created_at).toLocaleDateString("sv-SE")}
                        </span>
                    </div>
                </div>
                
                {/* Actions */}
                <div className="flex gap-2">
                    <button
                        onClick={() => executeAction("toggle-admin")}
                        disabled={actionLoading}
                        className={cn(
                            "p-2 rounded-lg transition",
                            user.is_admin 
                                ? "bg-zinc-800 hover:bg-zinc-700" 
                                : "bg-purple-600/20 hover:bg-purple-600/30 text-purple-400"
                        )}
                        title={user.is_admin ? "Remove Admin" : "Make Admin"}
                    >
                        <Shield className="w-5 h-5" />
                    </button>
                    <button
                        onClick={() => executeAction("force-logout")}
                        disabled={actionLoading}
                        className="p-2 rounded-lg bg-orange-600/20 hover:bg-orange-600/30 text-orange-400 transition"
                        title="Force Logout"
                    >
                        <LogOut className="w-5 h-5" />
                    </button>
                    <button
                        onClick={() => executeAction(user.is_banned ? "unban" : "ban")}
                        disabled={actionLoading}
                        className={cn(
                            "p-2 rounded-lg transition",
                            user.is_banned 
                                ? "bg-green-600/20 hover:bg-green-600/30 text-green-400" 
                                : "bg-red-600/20 hover:bg-red-600/30 text-red-400"
                        )}
                        title={user.is_banned ? "Unban User" : "Ban User"}
                    >
                        <Ban className="w-5 h-5" />
                    </button>
                </div>
            </div>
            
            {/* Tabs */}
            <div className="flex gap-1 p-1 bg-zinc-900/50 rounded-lg mb-6 w-fit">
                {tabs.map(tab => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition",
                            activeTab === tab.id
                                ? "bg-zinc-800 text-white"
                                : "text-zinc-400 hover:text-white"
                        )}
                    >
                        <tab.icon className="w-4 h-4" />
                        {tab.label}
                    </button>
                ))}
            </div>
            
            {/* Tab Content */}
            <div>
                {activeTab === "overview" && <OverviewTab user={user} onUpdate={fetchUser} />}
                {activeTab === "activity" && <ActivityTab userId={userId} />}
                {activeTab === "learning" && <LearningTab userId={userId} />}
                {activeTab === "ai" && <AIUsageTab userId={userId} />}
            </div>
        </div>
    )
}
