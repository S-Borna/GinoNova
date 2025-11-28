"use client"

/**
 * ============================================================================
 * PROFILE PAGE — User Profile & Settings
 * ============================================================================
 *
 * Features:
 * - User info display
 * - Avatar management
 * - Account settings
 * - Notification preferences
 * - Theme toggle
 *
 * @phase A.3 - App Shell & Routing
 */

import { useState } from "react"
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
} from "lucide-react"

/* ============================================================================
   USER STATS
   ============================================================================ */

interface StatBadgeProps {
    icon: React.ReactNode
    label: string
    value: string | number
    color: string
}

function StatBadge({ icon, label, value, color }: StatBadgeProps) {
    return (
        <div className={cn("flex items-center gap-2 px-4 py-2 rounded-xl", color)}>
            {icon}
            <div>
                <p className="text-xs font-medium opacity-80">{label}</p>
                <p className="font-bold">{value}</p>
            </div>
        </div>
    )
}

/* ============================================================================
   PROFILE PAGE
   ============================================================================ */

export default function ProfilePage() {
    const { user, logout } = useAuth()
    const [isDark, setIsDark] = useState(false)
    const [notificationsEnabled, setNotificationsEnabled] = useState(true)
    const [emailNotifications, setEmailNotifications] = useState(true)
    const [isSaving, setIsSaving] = useState(false)

    // Form state
    const [fullName, setFullName] = useState(user?.full_name || "")
    const [email] = useState(user?.email || "")

    const handleSave = async () => {
        setIsSaving(true)
        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 1000))
        setIsSaving(false)
    }

    const handleLogout = () => {
        logout()
    }

    const toggleTheme = () => {
        setIsDark(!isDark)
        // In real app, this would update the theme context
        document.documentElement.classList.toggle("dark")
    }

    // Get initials for avatar
    const initials = user?.full_name
        ?.split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase() || user?.email?.[0].toUpperCase() || "U"

    // Format join date
    const joinDate = new Date(user?.created_at || Date.now()).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
    })

    return (
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="space-y-6">
                {/* Header */}
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
                        Profile Settings
                    </h1>
                    <p className="text-gray-500 dark:text-gray-400">
                        Manage your account and preferences
                    </p>
                </div>

                {/* Profile Card */}
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex flex-col md:flex-row gap-6">
                        {/* Avatar */}
                        <div className="flex flex-col items-center">
                            <div className="relative w-24 h-24 rounded-2xl flex items-center justify-center bg-gradient-to-br from-indigo-500 to-purple-600 text-white text-3xl font-bold">
                                {initials}
                                <button className="absolute -bottom-2 -right-2 w-8 h-8 rounded-xl bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 flex items-center justify-center hover:bg-gray-50 dark:hover:bg-gray-600 transition-colors">
                                    <Camera className="w-4 h-4 text-gray-600 dark:text-gray-400" />
                                </button>
                            </div>
                            <p className="mt-3 text-sm text-gray-500 dark:text-gray-400">
                                Change avatar
                            </p>
                        </div>

                        {/* Info */}
                        <div className="flex-1">
                            <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-1">
                                {user?.full_name || "DevOps Learner"}
                            </h2>
                            <p className="text-gray-500 dark:text-gray-400 mb-4">
                                {user?.email}
                            </p>

                            {/* Stats */}
                            <div className="flex flex-wrap gap-3">
                                <StatBadge
                                    icon={<Trophy className="w-4 h-4 text-amber-500" />}
                                    label="Level"
                                    value={7}
                                    color="bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400"
                                />
                                <StatBadge
                                    icon={<Flame className="w-4 h-4 text-orange-500" />}
                                    label="Streak"
                                    value="14 days"
                                    color="bg-orange-100 dark:bg-orange-900/30 text-orange-700 dark:text-orange-400"
                                />
                                <StatBadge
                                    icon={<Clock className="w-4 h-4 text-blue-500" />}
                                    label="Joined"
                                    value={joinDate}
                                    color="bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                {/* Account Settings */}
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex items-center gap-2 mb-6">
                        <User className="w-5 h-5 text-indigo-500" />
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                            Account Information
                        </h3>
                    </div>

                    <div className="grid md:grid-cols-2 gap-4">
                        <div className="space-y-2">
                            <Label htmlFor="fullName">Full Name</Label>
                            <div className="relative">
                                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                                <Input
                                    id="fullName"
                                    value={fullName}
                                    onChange={(e) => setFullName(e.target.value)}
                                    className="pl-10 rounded-xl"
                                    placeholder="Your full name"
                                />
                            </div>
                        </div>

                        <div className="space-y-2">
                            <Label htmlFor="email">Email Address</Label>
                            <div className="relative">
                                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                                <Input
                                    id="email"
                                    value={email}
                                    disabled
                                    className="pl-10 rounded-xl bg-gray-50 dark:bg-gray-700"
                                />
                            </div>
                        </div>
                    </div>

                    <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                        <Button
                            onClick={handleSave}
                            disabled={isSaving}
                            className="rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-600 hover:to-purple-700"
                        >
                            <Save className="w-4 h-4 mr-2" />
                            {isSaving ? "Saving..." : "Save Changes"}
                        </Button>
                    </div>
                </div>

                {/* Preferences */}
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex items-center gap-2 mb-6">
                        <Shield className="w-5 h-5 text-indigo-500" />
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                            Preferences
                        </h3>
                    </div>

                    <div className="space-y-4">
                        {/* Theme Toggle */}
                        <div className="flex items-center justify-between py-3">
                            <div className="flex items-center gap-3">
                                {isDark ? (
                                    <Moon className="w-5 h-5 text-gray-500" />
                                ) : (
                                    <Sun className="w-5 h-5 text-gray-500" />
                                )}
                                <div>
                                    <p className="font-medium text-gray-900 dark:text-white">
                                        Dark Mode
                                    </p>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">
                                        Toggle dark/light theme
                                    </p>
                                </div>
                            </div>
                            <button
                                onClick={toggleTheme}
                                className={cn(
                                    "relative w-12 h-6 rounded-full transition-colors",
                                    isDark ? "bg-indigo-500" : "bg-gray-200 dark:bg-gray-600"
                                )}
                            >
                                <span
                                    className={cn(
                                        "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                        isDark ? "left-7" : "left-1"
                                    )}
                                />
                            </button>
                        </div>

                        {/* Notifications */}
                        <div className="flex items-center justify-between py-3 border-t border-gray-200 dark:border-gray-700">
                            <div className="flex items-center gap-3">
                                <Bell className="w-5 h-5 text-gray-500" />
                                <div>
                                    <p className="font-medium text-gray-900 dark:text-white">
                                        Push Notifications
                                    </p>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">
                                        Get notified about your progress
                                    </p>
                                </div>
                            </div>
                            <button
                                onClick={() => setNotificationsEnabled(!notificationsEnabled)}
                                className={cn(
                                    "relative w-12 h-6 rounded-full transition-colors",
                                    notificationsEnabled
                                        ? "bg-indigo-500"
                                        : "bg-gray-200 dark:bg-gray-600"
                                )}
                            >
                                <span
                                    className={cn(
                                        "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                        notificationsEnabled ? "left-7" : "left-1"
                                    )}
                                />
                            </button>
                        </div>

                        {/* Email Notifications */}
                        <div className="flex items-center justify-between py-3 border-t border-gray-200 dark:border-gray-700">
                            <div className="flex items-center gap-3">
                                <Mail className="w-5 h-5 text-gray-500" />
                                <div>
                                    <p className="font-medium text-gray-900 dark:text-white">
                                        Email Notifications
                                    </p>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">
                                        Receive weekly progress reports
                                    </p>
                                </div>
                            </div>
                            <button
                                onClick={() => setEmailNotifications(!emailNotifications)}
                                className={cn(
                                    "relative w-12 h-6 rounded-full transition-colors",
                                    emailNotifications
                                        ? "bg-indigo-500"
                                        : "bg-gray-200 dark:bg-gray-600"
                                )}
                            >
                                <span
                                    className={cn(
                                        "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                        emailNotifications ? "left-7" : "left-1"
                                    )}
                                />
                            </button>
                        </div>
                    </div>
                </div>

                {/* Danger Zone */}
                <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-red-200 dark:border-red-900/50 p-6">
                    <div className="flex items-center gap-2 mb-4">
                        <LogOut className="w-5 h-5 text-red-500" />
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                            Session
                        </h3>
                    </div>
                    <p className="text-gray-500 dark:text-gray-400 mb-4">
                        Sign out of your account on this device.
                    </p>
                    <Button
                        variant="destructive"
                        onClick={handleLogout}
                        className="rounded-xl"
                    >
                        <LogOut className="w-4 h-4 mr-2" />
                        Sign Out
                    </Button>
                </div>
            </div>
        </div>
    )
}
