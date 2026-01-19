"use client"

/**
 * Email Verification Page
 * User enters 6-digit code sent to their email
 */

import { useState, useEffect, useRef, Suspense } from "react"
import { useRouter, useSearchParams } from "next/navigation"
import { motion } from "framer-motion"
import { Mail, RefreshCw, CheckCircle, AlertCircle, ArrowLeft, Loader2 } from "lucide-react"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

// Loading fallback component
function VerifyEmailLoading() {
    return (
        <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 flex items-center justify-center p-4">
            <div className="text-center">
                <Loader2 className="w-8 h-8 animate-spin text-purple-500 mx-auto mb-4" />
                <p className="text-zinc-400">Laddar...</p>
            </div>
        </div>
    )
}

// Main page component with Suspense wrapper
export default function VerifyEmailPage() {
    return (
        <Suspense fallback={<VerifyEmailLoading />}>
            <VerifyEmailContent />
        </Suspense>
    )
}

// Inner component that uses useSearchParams
function VerifyEmailContent() {
    const router = useRouter()
    const searchParams = useSearchParams()
    const email = searchParams.get("email") || ""

    const [code, setCode] = useState(["", "", "", "", "", ""])
    const [loading, setLoading] = useState(false)
    const [resending, setResending] = useState(false)
    const [error, setError] = useState("")
    const [success, setSuccess] = useState(false)
    const [countdown, setCountdown] = useState(0)

    const inputRefs = useRef<(HTMLInputElement | null)[]>([])

    // Countdown timer for resend
    useEffect(() => {
        if (countdown > 0) {
            const timer = setTimeout(() => setCountdown(countdown - 1), 1000)
            return () => clearTimeout(timer)
        }
    }, [countdown])

    // Focus first input on mount
    useEffect(() => {
        inputRefs.current[0]?.focus()
    }, [])

    const handleChange = (index: number, value: string) => {
        // Only allow digits
        if (value && !/^\d$/.test(value)) return

        const newCode = [...code]
        newCode[index] = value
        setCode(newCode)
        setError("")

        // Auto-focus next input
        if (value && index < 5) {
            inputRefs.current[index + 1]?.focus()
        }

        // Auto-submit when all digits entered
        if (value && index === 5 && newCode.every(d => d)) {
            handleVerify(newCode.join(""))
        }
    }

    const handleKeyDown = (index: number, e: React.KeyboardEvent) => {
        if (e.key === "Backspace" && !code[index] && index > 0) {
            inputRefs.current[index - 1]?.focus()
        }
    }

    const handlePaste = (e: React.ClipboardEvent) => {
        e.preventDefault()
        const pastedData = e.clipboardData.getData("text").replace(/\D/g, "").slice(0, 6)
        if (pastedData.length === 6) {
            const newCode = pastedData.split("")
            setCode(newCode)
            handleVerify(pastedData)
        }
    }

    const handleVerify = async (verificationCode: string) => {
        if (!email) {
            setError("E-postadress saknas. Gå tillbaka och registrera dig igen.")
            return
        }

        setLoading(true)
        setError("")

        try {
            const res = await fetch(`${API_BASE_URL}/api/verify/verify`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, code: verificationCode })
            })

            const data = await res.json()

            if (!res.ok) {
                throw new Error(data.detail || "Verifiering misslyckades")
            }

            setSuccess(true)

            // Redirect to dashboard after 2 seconds
            setTimeout(() => {
                router.push("/dashboard")
            }, 2000)

        } catch (err) {
            setError(err instanceof Error ? err.message : "Något gick fel")
            setCode(["", "", "", "", "", ""])
            inputRefs.current[0]?.focus()
        } finally {
            setLoading(false)
        }
    }

    const handleResend = async () => {
        if (!email || countdown > 0) return

        setResending(true)
        setError("")

        try {
            const res = await fetch(`${API_BASE_URL}/api/verify/resend`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email })
            })

            const data = await res.json()

            if (!res.ok) {
                throw new Error(data.detail || "Kunde inte skicka ny kod")
            }

            setCountdown(60) // 60 second cooldown
            setCode(["", "", "", "", "", ""])
            inputRefs.current[0]?.focus()

        } catch (err) {
            setError(err instanceof Error ? err.message : "Något gick fel")
        } finally {
            setResending(false)
        }
    }

    if (success) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 flex items-center justify-center p-4">
                <motion.div
                    initial={{ scale: 0.8, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    className="text-center"
                >
                    <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-green-500/20 flex items-center justify-center">
                        <CheckCircle className="w-10 h-10 text-green-500" />
                    </div>
                    <h1 className="text-2xl font-bold mb-2">E-post verifierad!</h1>
                    <p className="text-zinc-400 mb-4">Välkommen till GinoNova</p>
                    <p className="text-sm text-zinc-500">Omdirigerar till dashboard...</p>
                </motion.div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 flex items-center justify-center p-4">
            <motion.div
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                className="w-full max-w-md"
            >
                {/* Back button */}
                <button
                    onClick={() => router.back()}
                    className="flex items-center gap-2 text-zinc-400 hover:text-white mb-8 transition"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Tillbaka
                </button>

                {/* Card */}
                <div className="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-8">
                    {/* Icon */}
                    <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-gradient-to-br from-purple-500/20 to-blue-500/20 flex items-center justify-center">
                        <Mail className="w-8 h-8 text-purple-400" />
                    </div>

                    {/* Title */}
                    <h1 className="text-2xl font-bold text-center mb-2">Verifiera din e-post</h1>
                    <p className="text-zinc-400 text-center mb-8">
                        Vi har skickat en 6-siffrig kod till<br />
                        <span className="text-white font-medium">{email || "din e-post"}</span>
                    </p>

                    {/* Code inputs */}
                    <div className="flex justify-center gap-3 mb-6">
                        {code.map((digit, index) => (
                            <input
                                key={index}
                                ref={el => { inputRefs.current[index] = el }}
                                type="text"
                                inputMode="numeric"
                                maxLength={1}
                                value={digit}
                                onChange={e => handleChange(index, e.target.value)}
                                onKeyDown={e => handleKeyDown(index, e)}
                                onPaste={index === 0 ? handlePaste : undefined}
                                disabled={loading}
                                className={`
                                    w-12 h-14 text-center text-2xl font-bold rounded-xl
                                    bg-zinc-800 border-2 transition-all
                                    focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20
                                    disabled:opacity-50
                                    ${digit ? "border-purple-500/50" : "border-zinc-700"}
                                `}
                            />
                        ))}
                    </div>

                    {/* Error message */}
                    {error && (
                        <motion.div
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className="flex items-center gap-2 text-red-400 text-sm mb-4 justify-center"
                        >
                            <AlertCircle className="w-4 h-4" />
                            {error}
                        </motion.div>
                    )}

                    {/* Loading state */}
                    {loading && (
                        <div className="flex items-center justify-center gap-2 text-purple-400 mb-4">
                            <RefreshCw className="w-4 h-4 animate-spin" />
                            Verifierar...
                        </div>
                    )}

                    {/* Resend button */}
                    <div className="text-center">
                        <p className="text-zinc-500 text-sm mb-2">Fick du ingen kod?</p>
                        <button
                            onClick={handleResend}
                            disabled={resending || countdown > 0}
                            className={`
                                text-purple-400 hover:text-purple-300 font-medium text-sm
                                disabled:opacity-50 disabled:cursor-not-allowed
                                flex items-center gap-2 mx-auto transition
                            `}
                        >
                            {resending ? (
                                <>
                                    <RefreshCw className="w-4 h-4 animate-spin" />
                                    Skickar...
                                </>
                            ) : countdown > 0 ? (
                                `Skicka igen om ${countdown}s`
                            ) : (
                                "Skicka ny kod"
                            )}
                        </button>
                    </div>
                </div>

                {/* Help text */}
                <div className="mt-6 p-3 bg-amber-500/10 border border-amber-500/20 rounded-lg">
                    <p className="text-xs text-amber-300 text-center">
                        💡 <strong>Hittar du inte mailet?</strong> Kolla skräpposten/spam-mappen!
                        <br />
                        <span className="text-amber-400/70">Mailet kommer från noreply@ginonova.com</span>
                    </p>
                </div>
            </motion.div>
        </div>
    )
}
