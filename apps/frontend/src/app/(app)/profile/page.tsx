"use client"

/**
 * ============================================================================
 * PROFILE PAGE — Premium User Profile & Settings — COSMIC EDITION 🌌
 * ============================================================================
 *
 * COSMIC DESIGN:
 * - Deep space background (#05050a)
 * - Multi-layered aurora orbs
 * - Pulsating icon glows
 * - Netflix-smooth animations
 *
 * @phase MILESTONE-2.0-COSMIC
 */

import { useState } from "react"
import { useTheme } from "next-themes"
import { motion } from "framer-motion"
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
                        linear-gradient(rgba(139, 92, 246, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(139, 92, 246, 0.3) 1px, transparent 1px)
                    `,
                    backgroundSize: '60px 60px'
                }}
            />
            <motion.div
                className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, rgba(139, 92, 246, 0.04) 40%, transparent 70%)',
                }}
                animate={{ scale: [1, 1.1, 1], opacity: [0.5, 0.7, 0.5] }}
                transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
            />
            <motion.div
                className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.15, 1], opacity: [0.4, 0.6, 0.4] }}
                transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
            />
            <motion.div
                className="absolute top-1/2 left-1/4 w-[500px] h-[500px] rounded-full"
                style={{
                    background: 'radial-gradient(circle, rgba(236, 72, 153, 0.06) 0%, transparent 60%)',
                }}
                animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.5, 0.3] }}
                transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
            />
        </div>
    )
}

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
        border: "border-amber-500/30",
        text: "text-amber-400",
        glow: "rgba(245,158,11,0.3)",
    },
    fire: {
        bg: "bg-orange-500/10",
        border: "border-orange-500/30",
        text: "text-orange-400",
        glow: "rgba(249,115,22,0.3)",
    },
    blue: {
        bg: "bg-blue-500/10",
        border: "border-blue-500/30",
        text: "text-blue-400",
        glow: "rgba(59,130,246,0.3)",
    },
    purple: {
        bg: "bg-purple-500/10",
        border: "border-purple-500/30",
        text: "text-purple-400",
        glow: "rgba(139,92,246,0.3)",
    },
};

function StatCard({ icon, label, value, color }: StatCardProps) {
    const colors = statColors[color];

    return (
        <motion.div
            whileHover={{ scale: 1.05, boxShadow: `0 0 25px ${colors.glow}` }}
            className={cn(
                "flex items-center gap-3 px-4 py-3 rounded-xl",
                "border transition-all duration-300",
                "bg-[#0a0a0f]/50",
                colors.border,
                `shadow-[0_0_15px_${colors.glow}]`
            )}
        >
            <motion.div
                className={colors.text}
                animate={{
                    textShadow: [`0 0 8px ${colors.glow}`, `0 0 15px ${colors.glow}`, `0 0 8px ${colors.glow}`]
                }}
                transition={{ duration: 2, repeat: Infinity }}
            >
                {icon}
            </motion.div>
            <div>
                <p className="text-xs text-zinc-500">{label}</p>
                <p className={cn("font-bold", colors.text)}>{value}</p>
            </div>
        </motion.div>
    );
}

/* ============================================================================
   ACHIEVEMENT SHOWCASE
   ============================================================================ */

function AchievementShowcase({ achievements }: { achievements: Achievement[] }) {
    const favorites = achievements.filter(a => a.isFavorite && a.unlocked);

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border border-amber-500/30",
                "shadow-[0_0_30px_rgba(245,158,11,0.1)]"
            )}
        >
            <div className="flex items-center justify-between px-6 py-4 border-b border-amber-500/20">
                <div className="flex items-center gap-2">
                    <motion.div
                        animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.1, 1] }}
                        transition={{ duration: 3, repeat: Infinity }}
                    >
                        <Award className="w-5 h-5 text-amber-400" />
                    </motion.div>
                    <h3 className="font-semibold text-zinc-100">Achievement Showcase</h3>
                </div>
                <span className="text-xs text-amber-300/60">Your favorites</span>
            </div>

            <div className="p-4 grid grid-cols-3 gap-3">
                {favorites.length > 0 ? favorites.map((achievement, index) => (
                    <motion.div
                        key={achievement.id}
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: index * 0.1 }}
                        whileHover={{ scale: 1.05, boxShadow: '0 0 30px rgba(245,158,11,0.3)' }}
                        className={cn(
                            "flex flex-col items-center p-4 rounded-xl text-center",
                            "bg-gradient-to-br from-amber-500/15 to-amber-600/5",
                            "border border-amber-500/30",
                            "shadow-[0_0_15px_rgba(245,158,11,0.15)]",
                            "transition-all duration-300 cursor-pointer"
                        )}
                    >
                        <motion.span
                            className="text-3xl mb-2"
                            animate={{ scale: [1, 1.1, 1] }}
                            transition={{ duration: 2, repeat: Infinity, delay: index * 0.3 }}
                        >
                            {achievement.icon}
                        </motion.span>
                        <span className="text-sm font-medium text-amber-300">{achievement.name}</span>
                    </motion.div>
                )) : (
                    <div className="col-span-3 text-center py-8">
                        <motion.div
                            animate={{ opacity: [0.5, 0.8, 0.5] }}
                            transition={{ duration: 3, repeat: Infinity }}
                        >
                            <Star className="w-10 h-10 text-amber-500/30 mx-auto mb-3" />
                        </motion.div>
                        <p className="text-sm text-zinc-500">No favorite achievements yet</p>
                        <p className="text-xs text-zinc-600 mt-1">Unlock achievements to showcase them here</p>
                    </div>
                )}
            </div>
        </motion.div>
    );
}

/* ============================================================================
   LEARNING GOALS
   ============================================================================ */

function LearningGoals({ goals }: { goals: LearningGoal[] }) {
    const goalColors: Record<string, { bar: string; text: string; glow: string }> = {
        amber: { bar: "bg-amber-500", text: "text-amber-400", glow: "rgba(245,158,11,0.5)" },
        emerald: { bar: "bg-emerald-500", text: "text-emerald-400", glow: "rgba(52,211,153,0.5)" },
        orange: { bar: "bg-orange-500", text: "text-orange-400", glow: "rgba(249,115,22,0.5)" },
        purple: { bar: "bg-purple-500", text: "text-purple-400", glow: "rgba(139,92,246,0.5)" },
    };

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                "border border-purple-500/30",
                "shadow-[0_0_30px_rgba(139,92,246,0.1)]"
            )}
        >
            <div className="flex items-center justify-between px-6 py-4 border-b border-purple-500/20">
                <div className="flex items-center gap-2">
                    <motion.div
                        animate={{
                            boxShadow: ['0 0 10px rgba(139,92,246,0.3)', '0 0 20px rgba(139,92,246,0.5)', '0 0 10px rgba(139,92,246,0.3)']
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                        className="p-1 rounded-lg"
                    >
                        <Target className="w-5 h-5 text-purple-400" />
                    </motion.div>
                    <h3 className="font-semibold text-zinc-100">Learning Goals</h3>
                </div>
                <button className="text-xs text-purple-400 hover:text-purple-300 transition-colors">Edit goals</button>
            </div>

            <div className="p-4 space-y-4">
                {goals.map((goal, index) => {
                    const progress = Math.round((goal.current / goal.target) * 100);
                    const colors = goalColors[goal.color] || goalColors.purple;

                    return (
                        <motion.div
                            key={goal.id}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ delay: index * 0.1 }}
                        >
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-sm text-zinc-300">{goal.title}</span>
                                <span className={cn("text-sm font-medium", colors.text)}>
                                    {goal.current}/{goal.target} {goal.unit}
                                </span>
                            </div>
                            <div className="h-2 bg-zinc-800/50 rounded-full overflow-hidden">
                                <motion.div
                                    className={cn(
                                        "h-full rounded-full transition-all duration-500",
                                        colors.bar
                                    )}
                                    initial={{ width: 0 }}
                                    animate={{ width: `${Math.min(progress, 100)}%` }}
                                    transition={{ duration: 1, delay: 0.3 + index * 0.1, ease: [0.16, 1, 0.3, 1] }}
                                    style={{
                                        boxShadow: progress >= 100 ? `0 0 15px ${colors.glow}` : 'none'
                                    }}
                                />
                            </div>
                        </motion.div>
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
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="absolute inset-0 bg-black/80 backdrop-blur-md"
                onClick={onClose}
            />
            <motion.div
                initial={{ opacity: 0, scale: 0.9, y: 20 }}
                animate={{ opacity: 1, scale: 1, y: 0 }}
                exit={{ opacity: 0, scale: 0.9, y: 20 }}
                transition={{ type: "spring", damping: 25, stiffness: 300 }}
                className={cn(
                    "relative z-10 w-full max-w-md mx-4 rounded-2xl p-6",
                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                    "border border-red-500/30",
                    "shadow-[0_0_50px_rgba(239,68,68,0.2)]"
                )}
            >
                <button
                    onClick={onClose}
                    className="absolute top-4 right-4 p-1 rounded-lg hover:bg-zinc-800/50 transition-colors"
                >
                    <X className="w-5 h-5 text-zinc-500" />
                </button>

                <div className="flex justify-center mb-4">
                    <motion.div
                        className="w-16 h-16 rounded-full bg-red-500/20 flex items-center justify-center"
                        animate={{
                            boxShadow: [
                                '0 0 20px rgba(239,68,68,0.2)',
                                '0 0 40px rgba(239,68,68,0.4)',
                                '0 0 20px rgba(239,68,68,0.2)'
                            ]
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                    >
                        <AlertTriangle className="w-8 h-8 text-red-500" />
                    </motion.div>
                </div>

                <h3 className="text-xl font-bold text-center text-zinc-100 mb-2">Reset All Progress?</h3>
                <p className="text-center text-zinc-400 mb-6">
                    This will permanently delete <strong className="text-red-400">all</strong> your learning progress,
                    completed tasks, and achievements. This action cannot be undone.
                </p>

                <div className="flex gap-3">
                    <Button
                        variant="outline"
                        onClick={onClose}
                        className="flex-1 rounded-xl border-zinc-700 hover:bg-zinc-800/50 transition-all"
                        disabled={isLoading}
                    >
                        Cancel
                    </Button>
                    <Button
                        variant="destructive"
                        onClick={onConfirm}
                        className="flex-1 rounded-xl shadow-[0_0_20px_rgba(239,68,68,0.3)] hover:shadow-[0_0_30px_rgba(239,68,68,0.5)] transition-all"
                        disabled={isLoading}
                    >
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
            </motion.div>
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
        <div className="min-h-screen bg-[#05050a] relative overflow-hidden">
            {/* Cosmic Aurora Background */}
            <CosmicAurora />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
                {/* Hero Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                    className={cn(
                        "relative overflow-hidden rounded-2xl",
                        "bg-gradient-to-br from-[#0d0d14] via-purple-950/20 to-[#0a0a0f]",
                        "border border-purple-500/30",
                        "shadow-[0_0_40px_rgba(139,92,246,0.15)]",
                        "p-8"
                    )}
                >
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />
                    <div className="absolute bottom-0 left-0 w-64 h-64 bg-cyan-500/5 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2" />

                    <div className="relative flex flex-col md:flex-row gap-6">
                        {/* Avatar */}
                        <div className="flex flex-col items-center md:items-start">
                            <motion.div
                                className={cn(
                                    "relative w-24 h-24 rounded-2xl flex items-center justify-center",
                                    "bg-gradient-to-br from-purple-500 to-blue-600",
                                    "text-white text-3xl font-bold"
                                )}
                                animate={{
                                    boxShadow: [
                                        '0 0 30px rgba(139,92,246,0.4)',
                                        '0 0 50px rgba(139,92,246,0.6)',
                                        '0 0 30px rgba(139,92,246,0.4)'
                                    ]
                                }}
                                transition={{ duration: 3, repeat: Infinity }}
                            >
                                {initials}
                                <button className={cn(
                                    "absolute -bottom-2 -right-2 w-8 h-8 rounded-xl",
                                    "bg-zinc-800/80 border border-purple-500/30",
                                    "flex items-center justify-center",
                                    "hover:bg-zinc-700 hover:border-purple-500/50 transition-all"
                                )}>
                                    <Camera className="w-4 h-4 text-zinc-400" />
                                </button>
                            </motion.div>
                        </div>

                        {/* Info */}
                        <div className="flex-1 text-center md:text-left">
                            <motion.h1
                                className={cn(
                                    "text-2xl md:text-3xl font-bold mb-1",
                                    "bg-gradient-to-r from-zinc-100 via-purple-200 to-zinc-100 bg-clip-text text-transparent"
                                )}
                                animate={{
                                    textShadow: [
                                        '0 0 20px rgba(139,92,246,0)',
                                        '0 0 30px rgba(139,92,246,0.3)',
                                        '0 0 20px rgba(139,92,246,0)'
                                    ]
                                }}
                                transition={{ duration: 3, repeat: Infinity }}
                            >
                                {user?.full_name || "DevOps Learner"}
                            </motion.h1>
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
                </motion.div>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Left Column - Account Settings */}
                    <div className="lg:col-span-2 space-y-6">
                        {/* Account Information */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
                            className={cn(
                                "rounded-2xl overflow-hidden",
                                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                "border border-purple-500/20",
                                "shadow-[0_0_20px_rgba(139,92,246,0.08)]"
                            )}
                        >
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-purple-500/20">
                                <motion.div
                                    animate={{
                                        boxShadow: ['0 0 8px rgba(139,92,246,0.2)', '0 0 15px rgba(139,92,246,0.4)', '0 0 8px rgba(139,92,246,0.2)']
                                    }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                    className="p-1 rounded-lg"
                                >
                                    <User className="w-5 h-5 text-purple-400" />
                                </motion.div>
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
                                            className="pl-10 rounded-xl bg-zinc-800/30 border-purple-500/20 text-zinc-100 focus:border-purple-500/50 transition-colors"
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
                                            className="pl-10 rounded-xl bg-zinc-800/20 border-zinc-700/30 text-zinc-500"
                                        />
                                    </div>
                                </div>

                                <div className="md:col-span-2 pt-4 border-t border-purple-500/20">
                                    <Button
                                        onClick={handleSave}
                                        disabled={isSaving}
                                        className="rounded-xl bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 shadow-[0_0_20px_rgba(139,92,246,0.3)] hover:shadow-[0_0_30px_rgba(139,92,246,0.5)] transition-all"
                                    >
                                        <Save className="w-4 h-4 mr-2" />
                                        {isSaving ? "Saving..." : "Save Changes"}
                                    </Button>
                                </div>
                            </div>
                        </motion.div>

                        {/* Preferences */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
                            className={cn(
                                "rounded-2xl overflow-hidden",
                                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                "border border-purple-500/20",
                                "shadow-[0_0_20px_rgba(139,92,246,0.08)]"
                            )}
                        >
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-purple-500/20">
                                <motion.div
                                    animate={{
                                        boxShadow: ['0 0 8px rgba(139,92,246,0.2)', '0 0 15px rgba(139,92,246,0.4)', '0 0 8px rgba(139,92,246,0.2)']
                                    }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                    className="p-1 rounded-lg"
                                >
                                    <Shield className="w-5 h-5 text-purple-400" />
                                </motion.div>
                                <h3 className="font-semibold text-zinc-100">Preferences</h3>
                            </div>

                            <div className="p-6 space-y-4">
                                {/* Theme Toggle */}
                                <div className="flex items-center justify-between py-3">
                                    <div className="flex items-center gap-3">
                                        {isDark ? <Moon className="w-5 h-5 text-purple-400" /> : <Sun className="w-5 h-5 text-amber-400" />}
                                        <div>
                                            <p className="font-medium text-zinc-200">Dark Mode</p>
                                            <p className="text-sm text-zinc-500">Toggle dark/light theme</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={toggleTheme}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-all",
                                            isDark ? "bg-purple-600 shadow-[0_0_10px_rgba(139,92,246,0.5)]" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            isDark ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>

                                {/* Notifications */}
                                <div className="flex items-center justify-between py-3 border-t border-purple-500/20">
                                    <div className="flex items-center gap-3">
                                        <Bell className="w-5 h-5 text-cyan-400" />
                                        <div>
                                            <p className="font-medium text-zinc-200">Push Notifications</p>
                                            <p className="text-sm text-zinc-500">Get notified about your progress</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => setNotificationsEnabled(!notificationsEnabled)}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-all",
                                            notificationsEnabled ? "bg-cyan-600 shadow-[0_0_10px_rgba(34,211,238,0.5)]" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            notificationsEnabled ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>

                                {/* Email Notifications */}
                                <div className="flex items-center justify-between py-3 border-t border-purple-500/20">
                                    <div className="flex items-center gap-3">
                                        <Mail className="w-5 h-5 text-emerald-400" />
                                        <div>
                                            <p className="font-medium text-zinc-200">Email Notifications</p>
                                            <p className="text-sm text-zinc-500">Receive weekly progress reports</p>
                                        </div>
                                    </div>
                                    <button
                                        onClick={() => setEmailNotifications(!emailNotifications)}
                                        className={cn(
                                            "relative w-12 h-6 rounded-full transition-all",
                                            emailNotifications ? "bg-emerald-600 shadow-[0_0_10px_rgba(52,211,153,0.5)]" : "bg-zinc-700"
                                        )}
                                    >
                                        <span className={cn(
                                            "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                            emailNotifications ? "left-7" : "left-1"
                                        )} />
                                    </button>
                                </div>
                            </div>
                        </motion.div>

                        {/* Danger Zone */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.5, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
                            className={cn(
                                "rounded-2xl overflow-hidden",
                                "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                                "border border-red-500/30",
                                "shadow-[0_0_20px_rgba(239,68,68,0.08)]"
                            )}
                        >
                            <div className="flex items-center gap-2 px-6 py-4 border-b border-red-500/30">
                                <motion.div
                                    animate={{
                                        boxShadow: ['0 0 8px rgba(239,68,68,0.2)', '0 0 15px rgba(239,68,68,0.4)', '0 0 8px rgba(239,68,68,0.2)']
                                    }}
                                    transition={{ duration: 2, repeat: Infinity }}
                                    className="p-1 rounded-lg"
                                >
                                    <AlertTriangle className="w-5 h-5 text-red-500" />
                                </motion.div>
                                <h3 className="font-semibold text-zinc-100">Danger Zone</h3>
                            </div>

                            <div className="p-6 space-y-4">
                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-red-500/20">
                                    <div>
                                        <p className="font-medium text-zinc-200">Reset All Progress</p>
                                        <p className="text-sm text-zinc-500">Delete all your learning progress and start fresh.</p>
                                    </div>
                                    <Button
                                        variant="outline"
                                        onClick={() => setShowResetModal(true)}
                                        className="rounded-xl border-red-500/30 text-red-400 hover:bg-red-500/10 hover:border-red-500/50 transition-all"
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
                                    <Button
                                        variant="destructive"
                                        onClick={handleLogout}
                                        className="rounded-xl shadow-[0_0_15px_rgba(239,68,68,0.2)] hover:shadow-[0_0_25px_rgba(239,68,68,0.4)] transition-all"
                                    >
                                        <LogOut className="w-4 h-4 mr-2" />
                                        Sign Out
                                    </Button>
                                </div>
                            </div>
                        </motion.div>
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
