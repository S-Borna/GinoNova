"use client"

/**
 * ============================================================================
 * SETTINGS PAGE — Premium Polish Edition
 * ============================================================================
 *
 * User settings and preferences management
 *
 * Sections:
 * - Account Settings
 * - Appearance (Theme)
 * - Notifications
 * - Privacy & Security
 * - Danger Zone
 *
 * @phase Premium Upgrade Phase 2
 */

import * as React from "react"
import { useState } from "react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import {
    Settings,
    User,
    Bell,
    Shield,
    Trash2,
    Mail,
    Smartphone,
    Lock,
    Key,
    Eye,
    EyeOff,
    Save,
    ChevronRight,
    AlertTriangle,
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

interface SettingsSection {
    id: string
    label: string
    icon: React.ElementType
    description: string
}

/* ============================================================================
   SETTINGS SECTIONS CONFIG
   ============================================================================ */

const SETTINGS_SECTIONS: SettingsSection[] = [
    { id: "account", label: "Account", icon: User, description: "Manage your account details" },
    { id: "notifications", label: "Notifications", icon: Bell, description: "Configure alerts and updates" },
    { id: "security", label: "Security", icon: Shield, description: "Password and privacy settings" },
    { id: "danger", label: "Danger Zone", icon: AlertTriangle, description: "Irreversible actions" },
]

/* ============================================================================
   SECTION COMPONENTS
   ============================================================================ */

function AccountSection() {
    const { user } = useAuth()
    const [fullName, setFullName] = useState(user?.full_name || "")
    const [email, setEmail] = useState(user?.email || "")
    const [isSaving, setIsSaving] = useState(false)

    const handleSave = async () => {
        setIsSaving(true)
        // Simulate save
        await new Promise(resolve => setTimeout(resolve, 1000))
        setIsSaving(false)
    }

    return (
        <div className="space-y-6">
            <div>
                <h3 className="text-lg font-semibold text-zinc-100 mb-1">Account Information</h3>
                <p className="text-sm text-zinc-400">Update your personal details</p>
            </div>

            <div className="space-y-4">
                {/* Full Name */}
                <div>
                    <label className="block text-sm font-medium text-zinc-300 mb-2">
                        Full Name
                    </label>
                    <input
                        type="text"
                        value={fullName}
                        onChange={(e) => setFullName(e.target.value)}
                        className={cn(
                            "w-full px-4 py-3 rounded-xl",
                            "bg-zinc-800/50 border border-zinc-700/50",
                            "text-zinc-100 placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50",
                            "transition-colors"
                        )}
                        placeholder="Enter your full name"
                    />
                </div>

                {/* Email */}
                <div>
                    <label className="block text-sm font-medium text-zinc-300 mb-2">
                        Email Address
                    </label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className={cn(
                            "w-full px-4 py-3 rounded-xl",
                            "bg-zinc-800/50 border border-zinc-700/50",
                            "text-zinc-100 placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50",
                            "transition-colors"
                        )}
                        placeholder="Enter your email"
                    />
                </div>

                {/* Save Button */}
                <button
                    onClick={handleSave}
                    disabled={isSaving}
                    className={cn(
                        "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                        "bg-purple-600 hover:bg-purple-500",
                        "text-white font-medium",
                        "transition-colors",
                        "disabled:opacity-50 disabled:cursor-not-allowed"
                    )}
                >
                    <Save className="w-4 h-4" />
                    {isSaving ? "Saving..." : "Save Changes"}
                </button>
            </div>
        </div>
    )
}

function NotificationsSection() {
    const [emailNotifs, setEmailNotifs] = useState(true)
    const [pushNotifs, setPushNotifs] = useState(false)
    const [weeklyDigest, setWeeklyDigest] = useState(true)
    const [streakReminders, setStreakReminders] = useState(true)

    const toggles = [
        { id: "email", label: "Email Notifications", description: "Receive updates via email", icon: Mail, value: emailNotifs, onChange: setEmailNotifs },
        { id: "push", label: "Push Notifications", description: "Browser push notifications", icon: Smartphone, value: pushNotifs, onChange: setPushNotifs },
        { id: "weekly", label: "Weekly Digest", description: "Summary of your progress each week", icon: Bell, value: weeklyDigest, onChange: setWeeklyDigest },
        { id: "streak", label: "Streak Reminders", description: "Get reminded to keep your streak", icon: Bell, value: streakReminders, onChange: setStreakReminders },
    ]

    return (
        <div className="space-y-6">
            <div>
                <h3 className="text-lg font-semibold text-zinc-100 mb-1">Notifications</h3>
                <p className="text-sm text-zinc-400">Choose what you want to be notified about</p>
            </div>

            <div className="space-y-4">
                {toggles.map((toggle) => (
                    <div
                        key={toggle.id}
                        className={cn(
                            "flex items-center justify-between p-4 rounded-xl",
                            "bg-zinc-800/30 border border-zinc-700/30"
                        )}
                    >
                        <div className="flex items-center gap-3">
                            <div className="w-10 h-10 rounded-lg bg-zinc-700/50 flex items-center justify-center">
                                <toggle.icon className="w-5 h-5 text-zinc-400" />
                            </div>
                            <div>
                                <p className="text-sm font-medium text-zinc-200">{toggle.label}</p>
                                <p className="text-xs text-zinc-500">{toggle.description}</p>
                            </div>
                        </div>
                        <button
                            onClick={() => toggle.onChange(!toggle.value)}
                            className={cn(
                                "relative w-12 h-6 rounded-full transition-colors",
                                toggle.value ? "bg-purple-600" : "bg-zinc-700"
                            )}
                        >
                            <div className={cn(
                                "absolute top-1 w-4 h-4 rounded-full bg-white transition-transform",
                                toggle.value ? "left-7" : "left-1"
                            )} />
                        </button>
                    </div>
                ))}
            </div>
        </div>
    )
}

function SecuritySection() {
    const [showPassword, setShowPassword] = useState(false)
    const [currentPassword, setCurrentPassword] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")

    return (
        <div className="space-y-6">
            <div>
                <h3 className="text-lg font-semibold text-zinc-100 mb-1">Security</h3>
                <p className="text-sm text-zinc-400">Manage your password and security settings</p>
            </div>

            {/* Change Password */}
            <div className="space-y-4">
                <h4 className="text-sm font-medium text-zinc-300">Change Password</h4>

                <div className="relative">
                    <input
                        type={showPassword ? "text" : "password"}
                        value={currentPassword}
                        onChange={(e) => setCurrentPassword(e.target.value)}
                        className={cn(
                            "w-full px-4 py-3 pr-12 rounded-xl",
                            "bg-zinc-800/50 border border-zinc-700/50",
                            "text-zinc-100 placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50",
                            "transition-colors"
                        )}
                        placeholder="Current password"
                    />
                    <button
                        onClick={() => setShowPassword(!showPassword)}
                        className="absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500 hover:text-zinc-300"
                    >
                        {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                    </button>
                </div>

                <input
                    type="password"
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    className={cn(
                        "w-full px-4 py-3 rounded-xl",
                        "bg-zinc-800/50 border border-zinc-700/50",
                        "text-zinc-100 placeholder:text-zinc-500",
                        "focus:outline-none focus:border-purple-500/50",
                        "transition-colors"
                    )}
                    placeholder="New password"
                />

                <input
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className={cn(
                        "w-full px-4 py-3 rounded-xl",
                        "bg-zinc-800/50 border border-zinc-700/50",
                        "text-zinc-100 placeholder:text-zinc-500",
                        "focus:outline-none focus:border-purple-500/50",
                        "transition-colors"
                    )}
                    placeholder="Confirm new password"
                />

                <button
                    className={cn(
                        "flex items-center gap-2 px-5 py-2.5 rounded-xl",
                        "bg-purple-600 hover:bg-purple-500",
                        "text-white font-medium",
                        "transition-colors"
                    )}
                >
                    <Key className="w-4 h-4" />
                    Update Password
                </button>
            </div>

            {/* Two-Factor Authentication */}
            <div className={cn(
                "flex items-center justify-between p-4 rounded-xl",
                "bg-zinc-800/30 border border-zinc-700/30"
            )}>
                <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-lg bg-emerald-500/20 flex items-center justify-center">
                        <Lock className="w-5 h-5 text-emerald-400" />
                    </div>
                    <div>
                        <p className="text-sm font-medium text-zinc-200">Two-Factor Authentication</p>
                        <p className="text-xs text-zinc-500">Add an extra layer of security</p>
                    </div>
                </div>
                <button className={cn(
                    "px-4 py-2 rounded-lg text-sm font-medium",
                    "bg-zinc-700 hover:bg-zinc-600 text-zinc-200",
                    "transition-colors"
                )}>
                    Enable
                </button>
            </div>
        </div>
    )
}

function DangerZoneSection() {
    const [confirmDelete, setConfirmDelete] = useState("")

    return (
        <div className="space-y-6">
            <div>
                <h3 className="text-lg font-semibold text-red-400 mb-1">Danger Zone</h3>
                <p className="text-sm text-zinc-400">These actions are irreversible. Please proceed with caution.</p>
            </div>

            {/* Delete Account */}
            <div className={cn(
                "p-5 rounded-xl",
                "bg-red-950/20 border border-red-500/30"
            )}>
                <div className="flex items-start gap-4">
                    <div className="w-10 h-10 rounded-lg bg-red-500/20 flex items-center justify-center shrink-0">
                        <Trash2 className="w-5 h-5 text-red-400" />
                    </div>
                    <div className="flex-1">
                        <h4 className="text-sm font-medium text-red-300 mb-1">Delete Account</h4>
                        <p className="text-xs text-zinc-400 mb-4">
                            Once you delete your account, all of your data will be permanently removed.
                            This action cannot be undone.
                        </p>
                        <input
                            type="text"
                            value={confirmDelete}
                            onChange={(e) => setConfirmDelete(e.target.value)}
                            className={cn(
                                "w-full px-4 py-2.5 rounded-lg mb-3",
                                "bg-zinc-900/50 border border-red-500/30",
                                "text-zinc-100 placeholder:text-zinc-600",
                                "focus:outline-none focus:border-red-500/50",
                                "text-sm"
                            )}
                            placeholder="Type 'DELETE' to confirm"
                        />
                        <button
                            disabled={confirmDelete !== "DELETE"}
                            className={cn(
                                "px-4 py-2 rounded-lg text-sm font-medium",
                                "bg-red-600 hover:bg-red-500 text-white",
                                "transition-colors",
                                "disabled:opacity-50 disabled:cursor-not-allowed"
                            )}
                        >
                            Delete Account
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function SettingsPage() {
    const [activeSection, setActiveSection] = useState("account")

    const renderSection = () => {
        switch (activeSection) {
            case "account":
                return <AccountSection />
            case "notifications":
                return <NotificationsSection />
            case "security":
                return <SecuritySection />
            case "danger":
                return <DangerZoneSection />
            default:
                return <AccountSection />
        }
    }

    return (
        <div className="min-h-screen bg-zinc-950">
            <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                {/* Header */}
                <div className="mb-8">
                    <div className="flex items-center gap-3 mb-2">
                        <div className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center",
                            "bg-gradient-to-br from-purple-500 to-blue-600",
                            "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                        )}>
                            <Settings className="w-6 h-6 text-white" />
                        </div>
                        <div>
                            <h1 className="text-2xl font-bold text-zinc-100">Settings</h1>
                            <p className="text-sm text-zinc-400">Manage your account and preferences</p>
                        </div>
                    </div>
                </div>

                {/* Content */}
                <div className="grid lg:grid-cols-4 gap-6">
                    {/* Sidebar Navigation */}
                    <div className="lg:col-span-1">
                        <nav className="space-y-1">
                            {SETTINGS_SECTIONS.map((section) => (
                                <button
                                    key={section.id}
                                    onClick={() => setActiveSection(section.id)}
                                    className={cn(
                                        "w-full flex items-center gap-3 px-4 py-3 rounded-xl",
                                        "transition-all text-left",
                                        activeSection === section.id
                                            ? "bg-purple-500/20 text-purple-300 border border-purple-500/30"
                                            : "text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200 border border-transparent"
                                    )}
                                >
                                    <section.icon className="w-5 h-5" />
                                    <span className="text-sm font-medium">{section.label}</span>
                                    {activeSection === section.id && (
                                        <ChevronRight className="w-4 h-4 ml-auto" />
                                    )}
                                </button>
                            ))}
                        </nav>
                    </div>

                    {/* Main Content */}
                    <div className={cn(
                        "lg:col-span-3 p-6 rounded-2xl",
                        "bg-zinc-900/80 border border-zinc-800/60"
                    )}>
                        {renderSection()}
                    </div>
                </div>
            </div>
        </div>
    )
}
