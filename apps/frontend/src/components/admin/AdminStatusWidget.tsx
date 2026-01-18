"use client"

/**
 * Admin Status Widget - Shows admin online/offline status
 * Users can send messages to admin when online
 * 
 * Placed in TopBar between "Locked in!" and profile dropdown
 */

import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { 
    MessageCircle, 
    Send, 
    X, 
    Check,
    User,
    Sparkles
} from "lucide-react"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth/AuthProvider"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

interface AdminStatusWidgetProps {
    className?: string
}

export function AdminStatusWidget({ className }: AdminStatusWidgetProps) {
    const { user } = useAuth()
    const [isAdminOnline, setIsAdminOnline] = useState(false)
    const [showMessageModal, setShowMessageModal] = useState(false)
    const [message, setMessage] = useState("")
    const [subject, setSubject] = useState("General")
    const [sending, setSending] = useState(false)
    const [sent, setSent] = useState(false)
    const [error, setError] = useState<string | null>(null)

    // Don't show for admin users
    const isAdmin = user?.is_admin || user?.email?.toLowerCase() === "said.ebadi@hotmail.com"
    if (isAdmin) return null

    // Check admin online status
    const checkAdminStatus = useCallback(async () => {
        try {
            const token = localStorage.getItem("auth_token")
            if (!token) return

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/status/online`, {
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            })

            if (response.ok) {
                const data = await response.json()
                setIsAdminOnline(data.online)
            }
        } catch {
            // Silent fail
        }
    }, [])

    // Poll admin status every 30 seconds
    useEffect(() => {
        checkAdminStatus()
        const interval = setInterval(checkAdminStatus, 30000)
        return () => clearInterval(interval)
    }, [checkAdminStatus])

    // Send message to admin
    const handleSendMessage = async () => {
        if (!message.trim()) return

        setSending(true)
        setError(null)

        try {
            const token = localStorage.getItem("auth_token")
            if (!token) throw new Error("Not authenticated")

            const response = await fetch(`${API_BASE_URL}/api/admin/v2/contact/message`, {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message, subject })
            })

            if (!response.ok) throw new Error("Failed to send message")

            setSent(true)
            setMessage("")
            
            // Close modal after showing success
            setTimeout(() => {
                setShowMessageModal(false)
                setSent(false)
            }, 2000)
        } catch (err) {
            setError("Failed to send message. Please try again.")
        } finally {
            setSending(false)
        }
    }

    return (
        <>
            {/* Status Badge */}
            <motion.button
                onClick={() => isAdminOnline && setShowMessageModal(true)}
                disabled={!isAdminOnline}
                className={cn(
                    "hidden md:flex items-center gap-2 px-3 py-1.5 rounded-xl",
                    "border backdrop-blur-sm transition-all duration-300",
                    isAdminOnline 
                        ? "bg-gradient-to-r from-violet-500/15 to-purple-500/10 border-violet-500/30 hover:border-violet-400/50 cursor-pointer"
                        : "bg-neutral-500/10 border-neutral-500/20 cursor-default",
                    className
                )}
                whileHover={isAdminOnline ? { scale: 1.02 } : {}}
                whileTap={isAdminOnline ? { scale: 0.98 } : {}}
            >
                {/* Pulsating dot */}
                <span className="relative flex h-2.5 w-2.5">
                    {isAdminOnline && (
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-violet-400 opacity-75" />
                    )}
                    <span className={cn(
                        "relative inline-flex rounded-full h-2.5 w-2.5",
                        isAdminOnline ? "bg-violet-400" : "bg-neutral-500"
                    )} />
                </span>

                {/* Text */}
                <span className={cn(
                    "text-xs font-medium whitespace-nowrap",
                    isAdminOnline ? "text-violet-300" : "text-neutral-500"
                )}>
                    Admin {isAdminOnline ? "Online" : "Offline"}
                </span>

                {/* Message icon (only when online) */}
                {isAdminOnline && (
                    <MessageCircle className="w-3.5 h-3.5 text-violet-400" />
                )}
            </motion.button>

            {/* Message Modal */}
            <AnimatePresence>
                {showMessageModal && (
                    <>
                        {/* Backdrop */}
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => !sending && setShowMessageModal(false)}
                            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
                        />

                        {/* Modal */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.95, y: 20 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.95, y: 20 }}
                            className={cn(
                                "fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50",
                                "w-full max-w-md mx-4",
                                "bg-gradient-to-br from-[#1a1a2e] to-[#16162a]",
                                "border border-violet-500/20 rounded-2xl",
                                "shadow-2xl shadow-violet-500/10"
                            )}
                        >
                            {/* Header */}
                            <div className="flex items-center justify-between p-4 border-b border-white/5">
                                <div className="flex items-center gap-3">
                                    <div className="p-2 rounded-xl bg-violet-500/20">
                                        <Sparkles className="w-5 h-5 text-violet-400" />
                                    </div>
                                    <div>
                                        <h3 className="text-white font-semibold">Contact Admin</h3>
                                        <p className="text-xs text-neutral-400">Send a message directly</p>
                                    </div>
                                </div>
                                <button
                                    onClick={() => !sending && setShowMessageModal(false)}
                                    className="p-2 rounded-lg hover:bg-white/5 transition-colors"
                                >
                                    <X className="w-4 h-4 text-neutral-400" />
                                </button>
                            </div>

                            {/* Content */}
                            <div className="p-4 space-y-4">
                                {sent ? (
                                    <motion.div
                                        initial={{ scale: 0.8, opacity: 0 }}
                                        animate={{ scale: 1, opacity: 1 }}
                                        className="flex flex-col items-center justify-center py-8 gap-3"
                                    >
                                        <div className="p-3 rounded-full bg-emerald-500/20">
                                            <Check className="w-8 h-8 text-emerald-400" />
                                        </div>
                                        <p className="text-white font-medium">Message Sent!</p>
                                        <p className="text-sm text-neutral-400">Admin will respond soon</p>
                                    </motion.div>
                                ) : (
                                    <>
                                        {/* Subject selector */}
                                        <div>
                                            <label className="text-xs text-neutral-400 mb-1.5 block">Subject</label>
                                            <select
                                                value={subject}
                                                onChange={(e) => setSubject(e.target.value)}
                                                className={cn(
                                                    "w-full px-3 py-2.5 rounded-xl",
                                                    "bg-white/5 border border-white/10",
                                                    "text-white text-sm",
                                                    "focus:border-violet-500/50 focus:outline-none focus:ring-2 focus:ring-violet-500/20",
                                                    "transition-all"
                                                )}
                                            >
                                                <option value="General">General Question</option>
                                                <option value="Bug Report">Bug Report</option>
                                                <option value="Feature Request">Feature Request</option>
                                                <option value="Account Issue">Account Issue</option>
                                                <option value="Feedback">Feedback</option>
                                            </select>
                                        </div>

                                        {/* Message input */}
                                        <div>
                                            <label className="text-xs text-neutral-400 mb-1.5 block">Message</label>
                                            <textarea
                                                value={message}
                                                onChange={(e) => setMessage(e.target.value)}
                                                placeholder="Type your message here..."
                                                rows={4}
                                                maxLength={500}
                                                className={cn(
                                                    "w-full px-3 py-2.5 rounded-xl resize-none",
                                                    "bg-white/5 border border-white/10",
                                                    "text-white text-sm placeholder:text-neutral-600",
                                                    "focus:border-violet-500/50 focus:outline-none focus:ring-2 focus:ring-violet-500/20",
                                                    "transition-all"
                                                )}
                                            />
                                            <div className="flex justify-between mt-1.5">
                                                <span className="text-xs text-neutral-500">
                                                    {message.length}/500 characters
                                                </span>
                                            </div>
                                        </div>

                                        {/* Error */}
                                        {error && (
                                            <p className="text-sm text-red-400 text-center">{error}</p>
                                        )}

                                        {/* Send button */}
                                        <button
                                            onClick={handleSendMessage}
                                            disabled={!message.trim() || sending}
                                            className={cn(
                                                "w-full flex items-center justify-center gap-2 px-4 py-3 rounded-xl",
                                                "bg-gradient-to-r from-violet-600 to-purple-600",
                                                "hover:from-violet-500 hover:to-purple-500",
                                                "text-white font-medium text-sm",
                                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                                "transition-all duration-200"
                                            )}
                                        >
                                            {sending ? (
                                                <>
                                                    <span className="animate-spin rounded-full h-4 w-4 border-2 border-white/30 border-t-white" />
                                                    Sending...
                                                </>
                                            ) : (
                                                <>
                                                    <Send className="w-4 h-4" />
                                                    Send Message
                                                </>
                                            )}
                                        </button>
                                    </>
                                )}
                            </div>
                        </motion.div>
                    </>
                )}
            </AnimatePresence>
        </>
    )
}

export default AdminStatusWidget
