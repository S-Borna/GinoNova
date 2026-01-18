"use client"

/**
 * Admin v2 Settings - Platform configuration
 */

import { useEffect, useState, useCallback } from "react"
import {
    RefreshCw,
    Save,
    Shield,
    Bell,
    Globe,
    Database,
    Palette,
    Zap,
    AlertCircle,
    CheckCircle,
    X,
    Info
} from "lucide-react"
import { getToken } from "@/lib/auth"
import { cn } from "@/lib/utils"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Types
interface Settings {
    general: {
        site_name: string
        site_description: string
        maintenance_mode: boolean
        registration_enabled: boolean
        email_verification_required: boolean
    }
    security: {
        max_login_attempts: number
        lockout_duration_minutes: number
        session_timeout_hours: number
        require_2fa_for_admins: boolean
        password_min_length: number
    }
    notifications: {
        email_notifications_enabled: boolean
        slack_webhook_url: string
        notify_on_new_user: boolean
        notify_on_error: boolean
        daily_report_enabled: boolean
    }
    ai: {
        ai_features_enabled: boolean
        max_requests_per_user_day: number
        max_tokens_per_request: number
        rate_limit_enabled: boolean
        allowed_models: string[]
    }
    features: {
        study_room_enabled: boolean
        skillpath_enabled: boolean
        premium_modules_enabled: boolean
        ai_quiz_enabled: boolean
        leaderboard_enabled: boolean
        achievements_enabled: boolean
    }
}

type TabId = "general" | "security" | "notifications" | "ai" | "features"

// Components
function Toast({ message, type, onClose }: { message: string, type: "success" | "error", onClose: () => void }) {
    useEffect(() => {
        const timer = setTimeout(onClose, 4000)
        return () => clearTimeout(timer)
    }, [onClose])

    return (
        <div className={cn(
            "fixed bottom-4 right-4 z-50 flex items-center gap-3 px-4 py-3 rounded-lg shadow-lg",
            type === "success" ? "bg-green-600" : "bg-red-600"
        )}>
            {type === "success" ? <CheckCircle className="w-5 h-5" /> : <AlertCircle className="w-5 h-5" />}
            <span className="text-sm">{message}</span>
            <button onClick={onClose} className="ml-2 hover:opacity-70">
                <X className="w-4 h-4" />
            </button>
        </div>
    )
}

function Toggle({ enabled, onChange, disabled = false }: {
    enabled: boolean
    onChange: (value: boolean) => void
    disabled?: boolean
}) {
    return (
        <button
            type="button"
            onClick={() => !disabled && onChange(!enabled)}
            disabled={disabled}
            className={cn(
                "relative w-12 h-6 rounded-full transition",
                enabled ? "bg-green-600" : "bg-zinc-700",
                disabled && "opacity-50 cursor-not-allowed"
            )}
        >
            <div className={cn(
                "absolute top-0.5 w-5 h-5 rounded-full bg-white shadow transition-transform",
                enabled ? "translate-x-6" : "translate-x-0.5"
            )} />
        </button>
    )
}

function SettingRow({
    title,
    description,
    children
}: {
    title: string
    description?: string
    children: React.ReactNode
}) {
    return (
        <div className="flex items-center justify-between py-4 border-b border-zinc-800 last:border-0">
            <div className="pr-4">
                <div className="font-medium">{title}</div>
                {description && <div className="text-sm text-zinc-400 mt-0.5">{description}</div>}
            </div>
            <div className="shrink-0">{children}</div>
        </div>
    )
}

function NumberInput({
    value,
    onChange,
    min = 0,
    max = 9999,
    disabled = false
}: {
    value: number
    onChange: (value: number) => void
    min?: number
    max?: number
    disabled?: boolean
}) {
    return (
        <input
            type="number"
            value={value}
            onChange={(e) => {
                const num = parseInt(e.target.value) || min
                onChange(Math.min(max, Math.max(min, num)))
            }}
            min={min}
            max={max}
            disabled={disabled}
            className="w-24 px-3 py-2 bg-zinc-900 border border-zinc-700 rounded-lg text-white text-right focus:outline-none focus:border-purple-500 disabled:opacity-50"
        />
    )
}

function TextInput({
    value,
    onChange,
    placeholder = "",
    type = "text",
    disabled = false
}: {
    value: string
    onChange: (value: string) => void
    placeholder?: string
    type?: "text" | "url" | "password"
    disabled?: boolean
}) {
    return (
        <input
            type={type}
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            disabled={disabled}
            className="w-64 px-3 py-2 bg-zinc-900 border border-zinc-700 rounded-lg text-white focus:outline-none focus:border-purple-500 disabled:opacity-50"
        />
    )
}

// Tab Components
function GeneralSettings({ settings, onChange }: {
    settings: Settings["general"]
    onChange: (key: string, value: unknown) => void
}) {
    return (
        <div className="space-y-1">
            <SettingRow title="Site Name" description="Displayed in browser title and emails">
                <TextInput
                    value={settings.site_name}
                    onChange={(v) => onChange("site_name", v)}
                />
            </SettingRow>
            <SettingRow title="Site Description" description="Meta description for SEO">
                <TextInput
                    value={settings.site_description}
                    onChange={(v) => onChange("site_description", v)}
                />
            </SettingRow>
            <SettingRow title="Maintenance Mode" description="Disable site for non-admins">
                <Toggle
                    enabled={settings.maintenance_mode}
                    onChange={(v) => onChange("maintenance_mode", v)}
                />
            </SettingRow>
            <SettingRow title="Registration" description="Allow new user signups">
                <Toggle
                    enabled={settings.registration_enabled}
                    onChange={(v) => onChange("registration_enabled", v)}
                />
            </SettingRow>
            <SettingRow title="Email Verification" description="Require email verification for new users">
                <Toggle
                    enabled={settings.email_verification_required}
                    onChange={(v) => onChange("email_verification_required", v)}
                />
            </SettingRow>
        </div>
    )
}

function SecuritySettings({ settings, onChange }: {
    settings: Settings["security"]
    onChange: (key: string, value: unknown) => void
}) {
    return (
        <div className="space-y-1">
            <SettingRow title="Max Login Attempts" description="Before account lockout">
                <NumberInput
                    value={settings.max_login_attempts}
                    onChange={(v) => onChange("max_login_attempts", v)}
                    min={3}
                    max={20}
                />
            </SettingRow>
            <SettingRow title="Lockout Duration" description="Minutes until login re-enabled">
                <NumberInput
                    value={settings.lockout_duration_minutes}
                    onChange={(v) => onChange("lockout_duration_minutes", v)}
                    min={5}
                    max={1440}
                />
            </SettingRow>
            <SettingRow title="Session Timeout" description="Hours until auto-logout">
                <NumberInput
                    value={settings.session_timeout_hours}
                    onChange={(v) => onChange("session_timeout_hours", v)}
                    min={1}
                    max={168}
                />
            </SettingRow>
            <SettingRow title="Require 2FA for Admins" description="Force two-factor for admin accounts">
                <Toggle
                    enabled={settings.require_2fa_for_admins}
                    onChange={(v) => onChange("require_2fa_for_admins", v)}
                />
            </SettingRow>
            <SettingRow title="Password Min Length" description="Minimum characters required">
                <NumberInput
                    value={settings.password_min_length}
                    onChange={(v) => onChange("password_min_length", v)}
                    min={6}
                    max={32}
                />
            </SettingRow>
        </div>
    )
}

function NotificationSettings({ settings, onChange }: {
    settings: Settings["notifications"]
    onChange: (key: string, value: unknown) => void
}) {
    return (
        <div className="space-y-1">
            <SettingRow title="Email Notifications" description="Send system emails">
                <Toggle
                    enabled={settings.email_notifications_enabled}
                    onChange={(v) => onChange("email_notifications_enabled", v)}
                />
            </SettingRow>
            <SettingRow title="Slack Webhook" description="For real-time alerts">
                <TextInput
                    value={settings.slack_webhook_url}
                    onChange={(v) => onChange("slack_webhook_url", v)}
                    placeholder="https://hooks.slack.com/..."
                    type="url"
                />
            </SettingRow>
            <SettingRow title="New User Alerts" description="Notify on user registration">
                <Toggle
                    enabled={settings.notify_on_new_user}
                    onChange={(v) => onChange("notify_on_new_user", v)}
                />
            </SettingRow>
            <SettingRow title="Error Alerts" description="Notify on system errors">
                <Toggle
                    enabled={settings.notify_on_error}
                    onChange={(v) => onChange("notify_on_error", v)}
                />
            </SettingRow>
            <SettingRow title="Daily Report" description="Send daily activity summary">
                <Toggle
                    enabled={settings.daily_report_enabled}
                    onChange={(v) => onChange("daily_report_enabled", v)}
                />
            </SettingRow>
        </div>
    )
}

function AISettings({ settings, onChange }: {
    settings: Settings["ai"]
    onChange: (key: string, value: unknown) => void
}) {
    return (
        <div className="space-y-1">
            <SettingRow title="AI Features" description="Enable/disable all AI features">
                <Toggle
                    enabled={settings.ai_features_enabled}
                    onChange={(v) => onChange("ai_features_enabled", v)}
                />
            </SettingRow>
            <SettingRow title="Max Requests/Day" description="Per user daily limit">
                <NumberInput
                    value={settings.max_requests_per_user_day}
                    onChange={(v) => onChange("max_requests_per_user_day", v)}
                    min={1}
                    max={1000}
                    disabled={!settings.ai_features_enabled}
                />
            </SettingRow>
            <SettingRow title="Max Tokens/Request" description="Token limit per request">
                <NumberInput
                    value={settings.max_tokens_per_request}
                    onChange={(v) => onChange("max_tokens_per_request", v)}
                    min={100}
                    max={32000}
                    disabled={!settings.ai_features_enabled}
                />
            </SettingRow>
            <SettingRow title="Rate Limiting" description="Enforce request limits">
                <Toggle
                    enabled={settings.rate_limit_enabled}
                    onChange={(v) => onChange("rate_limit_enabled", v)}
                    disabled={!settings.ai_features_enabled}
                />
            </SettingRow>
            <div className="py-4 border-b border-zinc-800">
                <div className="font-medium mb-3">Allowed Models</div>
                <div className="flex flex-wrap gap-2">
                    {["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus", "claude-3-sonnet"].map(model => {
                        const enabled = settings.allowed_models.includes(model)
                        return (
                            <button
                                key={model}
                                onClick={() => {
                                    const models = enabled
                                        ? settings.allowed_models.filter(m => m !== model)
                                        : [...settings.allowed_models, model]
                                    onChange("allowed_models", models)
                                }}
                                disabled={!settings.ai_features_enabled}
                                className={cn(
                                    "px-3 py-1.5 rounded-lg text-sm transition",
                                    enabled
                                        ? "bg-purple-600 text-white"
                                        : "bg-zinc-800 text-zinc-400 hover:bg-zinc-700",
                                    !settings.ai_features_enabled && "opacity-50 cursor-not-allowed"
                                )}
                            >
                                {model}
                            </button>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}

function FeatureSettings({ settings, onChange }: {
    settings: Settings["features"]
    onChange: (key: string, value: unknown) => void
}) {
    const features = [
        { key: "study_room_enabled", title: "Study Room", description: "Collaborative study sessions" },
        { key: "skillpath_enabled", title: "Skill Paths", description: "Guided learning paths" },
        { key: "premium_modules_enabled", title: "Premium Modules", description: "Advanced content" },
        { key: "ai_quiz_enabled", title: "AI Quiz", description: "AI-generated quizzes" },
        { key: "leaderboard_enabled", title: "Leaderboard", description: "User rankings" },
        { key: "achievements_enabled", title: "Achievements", description: "Badges and rewards" }
    ]

    return (
        <div className="space-y-1">
            {features.map(feature => (
                <SettingRow
                    key={feature.key}
                    title={feature.title}
                    description={feature.description}
                >
                    <Toggle
                        enabled={settings[feature.key as keyof Settings["features"]]}
                        onChange={(v) => onChange(feature.key, v)}
                    />
                </SettingRow>
            ))}
        </div>
    )
}

// Main Component
export default function AdminV2Settings() {
    const [settings, setSettings] = useState<Settings | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [saving, setSaving] = useState(false)
    const [hasChanges, setHasChanges] = useState(false)
    const [activeTab, setActiveTab] = useState<TabId>("general")
    const [toast, setToast] = useState<{ message: string, type: "success" | "error" } | null>(null)

    const fetchSettings = useCallback(async () => {
        const token = getToken()
        if (!token) {
            setError("Not authenticated - please log in")
            setLoading(false)
            return
        }

        setLoading(true)
        setError(null)

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/settings`, {
                headers: { Authorization: `Bearer ${token}` }
            })

            if (res.ok) {
                const json = await res.json()
                setSettings(json)
                setHasChanges(false)
            } else {
                const errorText = await res.text()
                console.error("Settings API error:", res.status, errorText)
                setError(`API error: ${res.status} - ${errorText}`)
            }
        } catch (err) {
            console.error("Settings fetch error:", err)
            setError(`Network error: ${err instanceof Error ? err.message : String(err)}`)
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchSettings()
    }, [fetchSettings])

    const saveSettings = async () => {
        const token = getToken()
        if (!token || !settings) return

        setSaving(true)

        try {
            const res = await fetch(`${API_BASE_URL}/api/admin/v2/settings`, {
                method: "PUT",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(settings)
            })

            if (res.ok) {
                setToast({ message: "Settings saved successfully", type: "success" })
                setHasChanges(false)
            } else {
                setToast({ message: "Failed to save settings", type: "error" })
            }
        } catch {
            setToast({ message: "Network error", type: "error" })
        } finally {
            setSaving(false)
        }
    }

    const handleChange = (section: keyof Settings, key: string, value: unknown) => {
        if (!settings) return

        setSettings({
            ...settings,
            [section]: {
                ...settings[section],
                [key]: value
            }
        })
        setHasChanges(true)
    }

    const tabs = [
        { id: "general" as TabId, label: "General", icon: Globe },
        { id: "security" as TabId, label: "Security", icon: Shield },
        { id: "notifications" as TabId, label: "Notifications", icon: Bell },
        { id: "ai" as TabId, label: "AI", icon: Zap },
        { id: "features" as TabId, label: "Features", icon: Palette }
    ]

    return (
        <div className="p-6">
            {/* Header */}
            <div className="flex items-center justify-between mb-6">
                <div>
                    <h1 className="text-2xl font-bold">Settings</h1>
                    <p className="text-sm text-zinc-400">Platform configuration</p>
                </div>
                <div className="flex items-center gap-3">
                    <button
                        onClick={fetchSettings}
                        disabled={loading}
                        className="flex items-center gap-2 px-3 py-2 bg-zinc-800 rounded-lg hover:bg-zinc-700 transition text-sm"
                    >
                        <RefreshCw className={cn("w-4 h-4", loading && "animate-spin")} />
                        Reload
                    </button>
                    <button
                        onClick={saveSettings}
                        disabled={saving || !hasChanges}
                        className={cn(
                            "flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition",
                            hasChanges
                                ? "bg-green-600 hover:bg-green-700"
                                : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                        )}
                    >
                        {saving ? (
                            <RefreshCw className="w-4 h-4 animate-spin" />
                        ) : (
                            <Save className="w-4 h-4" />
                        )}
                        Save Changes
                    </button>
                </div>
            </div>

            {/* Unsaved Warning */}
            {hasChanges && (
                <div className="flex items-center gap-3 p-4 mb-6 bg-orange-500/10 border border-orange-500/20 rounded-xl">
                    <Info className="w-5 h-5 text-orange-400" />
                    <span className="text-sm text-orange-400">You have unsaved changes</span>
                </div>
            )}

            {loading && !settings ? (
                <div className="space-y-4">
                    {[...Array(5)].map((_, i) => (
                        <div key={i} className="h-16 bg-zinc-800 rounded-xl animate-pulse" />
                    ))}
                </div>
            ) : settings ? (
                <div className="flex gap-6">
                    {/* Sidebar Tabs */}
                    <div className="w-48 shrink-0">
                        <div className="space-y-1">
                            {tabs.map(tab => (
                                <button
                                    key={tab.id}
                                    onClick={() => setActiveTab(tab.id)}
                                    className={cn(
                                        "w-full flex items-center gap-3 px-4 py-3 rounded-lg text-left transition",
                                        activeTab === tab.id
                                            ? "bg-purple-600/20 text-purple-400"
                                            : "text-zinc-400 hover:bg-zinc-800 hover:text-white"
                                    )}
                                >
                                    <tab.icon className="w-5 h-5" />
                                    <span className="font-medium">{tab.label}</span>
                                </button>
                            ))}
                        </div>
                    </div>

                    {/* Content */}
                    <div className="flex-1 bg-zinc-900/50 border border-zinc-800 rounded-xl p-6">
                        {activeTab === "general" && (
                            <GeneralSettings
                                settings={settings.general}
                                onChange={(k, v) => handleChange("general", k, v)}
                            />
                        )}
                        {activeTab === "security" && (
                            <SecuritySettings
                                settings={settings.security}
                                onChange={(k, v) => handleChange("security", k, v)}
                            />
                        )}
                        {activeTab === "notifications" && (
                            <NotificationSettings
                                settings={settings.notifications}
                                onChange={(k, v) => handleChange("notifications", k, v)}
                            />
                        )}
                        {activeTab === "ai" && (
                            <AISettings
                                settings={settings.ai}
                                onChange={(k, v) => handleChange("ai", k, v)}
                            />
                        )}
                        {activeTab === "features" && (
                            <FeatureSettings
                                settings={settings.features}
                                onChange={(k, v) => handleChange("features", k, v)}
                            />
                        )}
                    </div>
                </div>
            ) : (
                <div className="text-center py-12">
                    <p className="text-zinc-500 mb-2">Failed to load settings</p>
                    {error && <p className="text-red-400 text-sm">{error}</p>}
                </div>
            )}

            {/* Toast */}
            {toast && (
                <Toast
                    message={toast.message}
                    type={toast.type}
                    onClose={() => setToast(null)}
                />
            )}
        </div>
    )
}
