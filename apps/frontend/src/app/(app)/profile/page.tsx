"use client"

/**
 * ============================================================================
 * PROFILE PAGE — Premium User Profile & Settings
 * ============================================================================
 *
 * Premium Upgrade Phase 2 - Enhanced with:
 * - Hero header with gradient and glow
 * - Achievement showcase (favorite achievements)
 * - Learning goals section
 * - Premium stat cards with animations
 * - Clean dark theme throughout
 *
 * @phase Premium Upgrade Phase 2
 */

import { useState } from "react"
import { useTheme } from "next-themes"
import { useAuth } from "@/components/auth"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    User,
    Mail,
    Calendar,
    Shield,
    Bell,
    Moon,
    Sun,
    LogOut,
    Save,
    Camera,
    Trophy,
    Flame,
    Clock,
    AlertTriangle,
    RotateCcw,
    X,
    Sparkles,
    Target,
    Zap,
    Star,
    Award,
    TrendingUp,
} from "lucide-react"
import { resetProgress } from "@/lib/auth"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Achievement {
    id: string;
    name: string;
    icon: string;
    description: string;
    unlocked: boolean;
    isFavorite?: boolean;
}

interface LearningGoal {
    id: string;
    title: string;
    target: number;
    current: number;
    unit: string;
    color: string;
}

/* ============================================================================
   MOCK DATA
   ============================================================================ */

const MOCK_ACHIEVEMENTS: Achievement[] = [
    { id: "1", name: "First Steps", icon: "🚀", description: "Complete your first task", unlocked: true, isFavorite: true },
    { id: "2", name: "Week Warrior", icon: "🔥", description: "7-day study streak", unlocked: true, isFavorite: true },
    { id: "3", name: "Docker Pro", icon: "🐳", description: "Master containerization", unlocked: true, isFavorite: true },
    { id: "4", name: "Linux Guru", icon: "🐧", description: "Complete Linux track", unlocked: false },
];

const MOCK_GOALS: LearningGoal[] = [
    { id: "1", title: "Weekly XP", target: 500, current: 325, unit: "XP", color: "amber" },
    { id: "2", title: "Tasks This Week", target: 10, current: 7, unit: "tasks", color: "emerald" },
    { id: "3", title: "Streak Goal", target: 30, current: 14, unit: "days", color: "orange" },
];

/* ============================================================================
   PREMIUM STAT CARD
   ============================================================================ */

interface StatCardProps {
    icon: React.ReactNode;
    label: string;
    value: string | number;
    color: "gold" | "fire" | "blue" | "purple";
}

const statColors = {
    gold: {
        bg: "bg-amber-500/10",
        border: "border-amber-500/20",
        text: "text-amber-400",
        glow: "shadow-[0_0_20px_rgba(245,158,11,0.2)]",
    },
    fire: {
        bg: "bg-orange-500/10",
        border: "border-orange-500/20",
        text: "text-orange-400",
        glow: "shadow-[0_0_20px_rgba(249,115,22,0.2)]",
    },
    blue: {
        bg: "bg-blue-500/10",
        border: "border-blue-500/20",
        text: "text-blue-400",
        glow: "shadow-[0_0_20px_rgba(59,130,246,0.2)]",
    },
    purple: {
        bg: "bg-purple-500/10",
        border: "border-purple-500/20",
        text: "text-purple-400",
        glow: "shadow-[0_0_20px_rgba(139,92,246,0.2)]",
    },
};

function StatCard({ icon, label, value, color }: StatCardProps) {
    const colors = statColors[color];

    return (
        <div className={cn(
            "flex items-center gap-3 px-4 py-3 rounded-xl",
            "border transition-all duration-300",
            "hover:scale-[1.02]",
            colors.bg,
            colors.border,
            colors.glow
        )}>
            <div className={colors.text}>{icon}</div>
            <div>
                <p className="text-xs text-zinc-500">{label}</p>
                <p className={cn("font-bold", colors.text)}>{value}</p>
            </div>
        </div>
    );
}

/* ============================================================================
   ACHIEVEMENT SHOWCASE
   ============================================================================ */

function AchievementShowcase({ achievements }: { achievements: Achievement[] }) {
    const favorites = achievements.filter(a => a.isFavorite && a.unlocked);

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            <div className="flex items-center justify-between px-6 py-4 border-b border-zinc-800/60">
                <div className="flex items-center gap-2">
                    <Award className="w-5 h-5 text-amber-400" />
                    <h3 className="font-semibold text-zinc-100">Achievement Showcase</h3>
                </div>
                <span className="text-xs text-zinc-500">Your favorites</span>
            </div>

            <div className="p-4 grid grid-cols-3 gap-3">
                {favorites.length > 0 ? favorites.map(achievement => (
                    <div
                        key={achievement.id}
                        className={cn(
                            "flex flex-col items-center p-4 rounded-xl text-center",
                            "bg-gradient-to-br from-amber-500/10 to-amber-600/5",
                            "border border-amber-500/20",
                            "shadow-[0_0_15px_rgba(245,158,11,0.15)]",
                            "hover:shadow-[0_0_25px_rgba(245,158,11,0.25)]",
                            "transition-all duration-300"
                        )}
                    >
                        <span className="text-3xl mb-2">{achievement.icon}</span>
                        <span className="text-sm font-medium text-amber-300">{achievement.name}</span>
                    </div>
                )) : (
                    <div className="col-span-3 text-center py-8">
                        <Star className="w-10 h-10 text-zinc-600 mx-auto mb-3" />
                        <p className="text-sm text-zinc-500">No favorite achievements yet</p>
                        <p className="text-xs text-zinc-600 mt-1">Unlock achievements to showcase them here</p>
                    </div>
                )}
            </div>
        </div>
    );
}

/* ============================================================================
   LEARNING GOALS
   ============================================================================ */

function LearningGoals({ goals }: { goals: LearningGoal[] }) {
    const goalColors: Record<string, { bar: string; text: string }> = {
        amber: { bar: "bg-amber-500", text: "text-amber-400" },
        emerald: { bar: "bg-emerald-500", text: "text-emerald-400" },
        orange: { bar: "bg-orange-500", text: "text-orange-400" },
        purple: { bar: "bg-purple-500", text: "text-purple-400" },
    };

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            <div className="flex items-center justify-between px-6 py-4 border-b border-zinc-800/60">
                <div className="flex items-center gap-2">
                    <Target className="w-5 h-5 text-purple-400" />
                    <h3 className="font-semibold text-zinc-100">Learning Goals</h3>
                </div>
                <button className="text-xs text-purple-400 hover:text-purple-300">Edit goals</button>
            </div>

            <div className="p-4 space-y-4">
                {goals.map(goal => {
                    const progress = Math.round((goal.current / goal.target) * 100);
                    const colors = goalColors[goal.color] || goalColors.purple;

                    return (
                        <div key={goal.id}>
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-sm text-zinc-300">{goal.title}</span>
                                <span className={cn("text-sm font-medium", colors.text)}>
                                    {goal.current}/{goal.target} {goal.unit}
                                </span>
                            </div>
                            <div className="h-2 bg-zinc-800 rounded-full overflow-hidden">
                                <div
                                    className={cn(
                                        "h-full rounded-full transition-all duration-500",
                                        colors.bar,
                                        progress >= 100 && "shadow-[0_0_10px_rgba(34,211,172,0.5)]"
                                    )}
                                    style={{ width: `${Math.min(progress, 100)}%` }}
                                />
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}

/* ============================================================================
   CONFIRMATION MODAL
   ============================================================================ */

interface ConfirmModalProps {
    isOpen: boolean
    onClose: () => void
    onConfirm: () => void
    isLoading: boolean
}

function ConfirmResetModal({ isOpen, onClose, onConfirm, isLoading }: ConfirmModalProps) {
    if (!isOpen) return null

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
            <div className="absolute inset-0 bg-black/70 backdrop-blur-sm" onClick={onClose} />
            <div className="relative z-10 w-full max-w-md mx-4 bg-zinc-900 rounded-2xl shadow-2xl border border-zinc-800 p-6">
                <button
                    onClick={onClose}
                    className="absolute top-4 right-4 p-1 rounded-lg hover:bg-zinc-800 transition-colors"
                >
                    <X className="w-5 h-5 text-zinc-500" />
                </button>

                <div className="flex justify-center mb-4">
                    <div className="w-16 h-16 rounded-full bg-red-500/20 flex items-center justify-center">
                        <AlertTriangle className="w-8 h-8 text-red-500" />
                    </div>
                </div>

                <h3 className="text-xl font-bold text-center text-zinc-100 mb-2">Reset All Progress?</h3>
                <p className="text-center text-zinc-400 mb-6">
                    This will permanently delete <strong className="text-zinc-200">all</strong> your learning progress,
                    completed tasks, and achievements. This action cannot be undone.
                </p>

                <div className="flex gap-3">
                    <Button variant="outline" onClick={onClose} className="flex-1 rounded-xl border-zinc-700" disabled={isLoading}>
                        Cancel
                    </Button>
                    <Button variant="destructive" onClick={onConfirm} className="flex-1 rounded-xl" disabled={isLoading}>
                        {isLoading ? (
                            <>
                                <RotateCcw className="w-4 h-4 mr-2 animate-spin" />
                                Resetting...
                            </>
                        ) : (
                            <>
                                <AlertTriangle className="w-4 h-4 mr-2" />
                                Yes, Reset
                            </>
                        )}
                    </Button>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   PROFILE PAGE
   ============================================================================ */

export default function ProfilePage() {
    const { user, logout, refreshUser } = useAuth()
    const { theme, setTheme } = useTheme()
    const [notificationsEnabled, setNotificationsEnabled] = useState(true)
    const [emailNotifications, setEmailNotifications] = useState(true)
    const [isSaving, setIsSaving] = useState(false)
    const [showResetModal, setShowResetModal] = useState(false)
    const [isResetting, setIsResetting] = useState(false)

    const [fullName, setFullName] = useState(user?.full_name || "")
    const [email] = useState(user?.email || "")

    const handleSave = async () => {
        setIsSaving(true)
        await new Promise((resolve) => setTimeout(resolve, 1000))
        setIsSaving(false)
    }

    const handleLogout = () => { logout() }

    const handleResetProgress = async () => {
        setIsResetting(true)
        try {
            const result = await resetProgress()
            setShowResetModal(false)
            await refreshUser()
            alert(`All progress has been reset successfully! (${result.deleted_records} records deleted)`)
            window.location.reload()
        } catch (error) {
            console.error("Failed to reset progress:", error)
            alert("Failed to reset progress. Please try again.")
        } finally {
            setIsResetting(false)
        }
    }

    const toggleTheme = () => setTheme(theme === "dark" ? "light" : "dark")
    const isDark = theme === "dark"

    const initials = user?.full_name?.split(" ").map((n) => n[0]).join("").toUpperCase() || user?.email?.[0].toUpperCase() || "U"
    const joinDate = new Date(user?.created_at || Date.now()).toLocaleDateString("en-US", { year: "numeric", month: "long" })
    const userName = user?.full_name?.split(" ")[0] || "Learner";

    return (
        <div className="min-h-screen bg-zinc-950">
            <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
                {/* Hero Header */}
                <div className={cn(
                    "relative overflow-hidden rounded-2xl",
                    "bg-gradient-to-br from-zinc-900 via-purple-950/30 to-zinc-900",
                    "border border-purple-500/20",
                    "p-8"
                )}>
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />

                    <div className="relative flex flex-col md:flex-row gap-6">
                        {/* Avatar */}
                        <div className="flex flex-col items-center md:items-start">
                            <div className={cn(
                                "relative w-24 h-24 rounded-2xl flex items-center justify-center",
                                "bg-gradient-to-br from-purple-500 to-blue-600",
                                "text-white text-3xl font-bold",
                                "shadow-[0_0_30px_rgba(139,92,246,0.4)]"
                            )}>
                                {initials}
                                <button className={cn(
                                    "absolute -bottom-2 -right-2 w-8 h-8 rounded-xl",
                                    "bg-zinc-800 border border-zinc-700",
                                    "flex items-center justify-center",
                                    "hover:bg-zinc-700 transition-colors"
                                )}>
                                    <Camera className="w-4 h-4 text-zinc-400" />
                                </button>
                            </div>
                        </div>

                        {/* Info */}
                        <div className="flex-1 text-center md:text-left">
                            <h1 className={cn(
                                "text-2xl md:text-3xl font-bold mb-1",
                                "bg-gradient-to-r from-zinc-100 via-purple-200 to-zinc-100 bg-clip-text text-transparent"
                            )}>
                                {user?.full_name || "DevOps Learner"}
                            </h1>
                            <p className="text-zinc-400 mb-4">{user?.email}</p>

                            {/* Stats */}
                            <div className="flex flex-wrap justify-center md:justify-start gap-3">
                                <StatCard icon={<Trophy className="w-4 h-4" />} label="Level" value={7} color="gold" />
                                <StatCard icon={<Flame className="w-4 h-4" />} label="Streak" value="14 days" color="fire" />
                                <StatCard icon={<Zap className="w-4 h-4" />} label="Total XP" value="2,450" color="purple" />
                                <StatCard icon={<Calendar className="w-4 h-4" />} label="Joined" value={joinDate} color="blue" />
                            </div>
                        </div>
                    </div>
                </div>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Left Column - Account Settings */}
                    <div className="lg:col-span-2 space-y-6">
                        {/* Account Information */}
                        <div className={cn("rounded-2xl overflow-hidden bg-zinc-900/80 backdrop-blur-sm border border-zinc-800/60")}>
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-zinc-800/60">
                                <User className="w-5 h-5 text-purple-400" />
                                <h3 className="font-semibold text-zinc-100">Account Information</h3>
                            </div>

                            <div className="p-6 grid md:grid-cols-2 gap-4">
                                <div className="space-y-2">
                                    <Label htmlFor="fullName" className="text-zinc-400">Full Name</Label>
                                    <div className="relative">
                                        <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                                        <Input
                                            id="fullName"
                                            value={fullName}
                                            onChange={(e) => setFullName(e.target.value)}
                                            className="pl-10 rounded-xl bg-zinc-800/50 border-zinc-700/50 text-zinc-100"
                                            placeholder="Your full name"
                                        />
                                    </div>
                                </div>

                                <div className="space-y-2">
                                    <Label htmlFor="email" className="text-zinc-400">Email Address</Label>
                                    <div className="relative">
                                        <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-500" />
                                        <Input
                                            id="email"
                                            value={email}
                                            disabled
                                            className="pl-10 rounded-xl bg-zinc-800/30 border-zinc-700/30 text-zinc-500"
                                        />
                                    </div>
                                </div>

                                <div className="md:col-span-2 pt-4 border-t border-zinc-800/60">
                                    <Button
                                        onClick={handleSave}
                                        disabled={isSaving}
                                        className="rounded-xl bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500"
                                    >
                                        <Save className="w-4 h-4 mr-2" />
                                        {isSaving ? "Saving..." : "Save Changes"}
                                    </Button>
                                </div>
                            </div>
                        </div>

                        {/* Preferences */}
                        <div className={cn("rounded-2xl overflow-hidden bg-zinc-900/80 backdrop-blur-sm border border-zinc-800/60")}>
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-zinc-800/60">
                                <Shield className="w-5 h-5 text-purple-400" />
                                <h3 className="font-semibold text-zinc-100">Preferences</h3>
                            </div>

                            <div className="p-6 space-y-4">
                                {/* Theme Toggle */}
                                <div className="flex items-center justify-between py-3">
                                    <div className="flex items-center gap-3">
                                        {isDark ? <Moon className="w-5 h-5 text-zinc-500" /> : <Sun className="w-5 h-5 text-zinc-500" />}
                                        <div>
                                            <p className="font-medium text-zinc-200">Dark Mode</p>
                                            <p className="text-sm text-zinc-500">Toggle dark/light theme</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={toggleTheme}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-colors",
                                            isDark ? "bg-purple-600" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            isDark ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>

                                {/* Notifications */}
                                <div className="flex items-center justify-between py-3 border-t border-zinc-800/60">
                                    <div className="flex items-center gap-3">
                                        <Bell className="w-5 h-5 text-zinc-500" />
                                        <div>
                                            <p className="font-medium text-zinc-200">Push Notifications</p>
                                            <p className="text-sm text-zinc-500">Get notified about your progress</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => setNotificationsEnabled(!notificationsEnabled)}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-colors",
                                            notificationsEnabled ? "bg-purple-600" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            notificationsEnabled ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>

                                {/* Email Notifications */}
                                <div className="flex items-center justify-between py-3 border-t border-zinc-800/60">
                                    <div className="flex items-center gap-3">
                                        <Mail className="w-5 h-5 text-zinc-500" />
                                        <div>
                                            <p className="font-medium text-zinc-200">Email Notifications</p>
                                            <p className="text-sm text-zinc-500">Receive weekly progress reports</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => setEmailNotifications(!emailNotifications)}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-colors",
                                            emailNotifications ? "bg-purple-600" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            emailNotifications ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>
                            </div>
                        </div>

                        {/* Danger Zone */}
                        <div className={cn("rounded-2xl overflow-hidden bg-zinc-900/80 backdrop-blur-sm border border-red-500/20")}>
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-red-500/20">
                                <AlertTriangle className="w-5 h-5 text-red-500" />
                                <h3 className="font-semibold text-zinc-100">Danger Zone</h3>
                            </div>

                            <div className="p-6 space-y-4">
                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-zinc-800/60">
                                    <div>
                                        <p className="font-medium text-zinc-200">Reset All Progress</p>
                                        <p className="text-sm text-zinc-500">Delete all your learning progress and start fresh.</p>
                                    </div>
                                    <Button
                                        variant="outline"
                                        onClick={() => setShowResetModal(true)}
                                        className="rounded-xl border-red-500/30 text-red-400 hover:bg-red-500/10"
                                    >
                                        <RotateCcw className="w-4 h-4 mr-2" />
                                        Reset Progress
                                    </Button>
                                </div>

                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                    <div>
                                        <p className="font-medium text-zinc-200">Sign Out</p>
                                        <p className="text-sm text-zinc-500">Sign out of your account on this device.</p>
                                    </div>
                                    <Button variant="destructive" onClick={handleLogout} className="rounded-xl">
                                        <LogOut className="w-4 h-4 mr-2" />
                                        Sign Out
                                    </Button>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Column - Achievement & Goals */}
                    <div className="space-y-6">
                        <AchievementShowcase achievements={MOCK_ACHIEVEMENTS} />
                        <LearningGoals goals={MOCK_GOALS} />
                    </div>
                </div>
            </div>

            <ConfirmResetModal
                isOpen={showResetModal}
                onClose={() => setShowResetModal(false)}
                onConfirm={handleResetProgress}
                isLoading={isResetting}
            />
        </div>
    )
}
