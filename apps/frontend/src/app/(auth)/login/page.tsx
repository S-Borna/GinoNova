"use client"

/**
 * ============================================================================
 * LOGIN PAGE — Premium Cosmic Sign In Experience ✨
 * ============================================================================
 *
 * Beautiful centered login page with glass morphism and cosmic effects.
 *
 * @phase MILESTONE-2.0 - Premium Auth UI
 */

import * as React from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion } from "framer-motion"
import { Terminal, ArrowRight, Sparkles } from "lucide-react"
import { useAuth } from "@/components/auth"
import {
    AuthInput,
    AuthCheckbox,
    AuthSubmitButton,
    AuthErrorAlert,
} from "@/components/auth/AuthForm"
import { SocialButtons, OrDivider } from "@/components/auth/SocialButtons"
import { validateEmail, normalizeEmail } from "@/lib/auth"
import { cn } from "@/lib/utils"

export default function LoginPage() {
    const [email, setEmail] = React.useState("")
    const [password, setPassword] = React.useState("")
    const [rememberMe, setRememberMe] = React.useState(false)
    const [error, setError] = React.useState("")
    const [emailError, setEmailError] = React.useState("")
    const [isLoading, setIsLoading] = React.useState(false)

    const { login } = useAuth()
    const router = useRouter()

    const handleEmailBlur = () => {
        if (email) {
            const validation = validateEmail(email)
            setEmailError(validation.valid ? "" : validation.error || "")
        }
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setError("")
        setEmailError("")

        // Validation
        const emailValidation = validateEmail(email)
        if (!emailValidation.valid) {
            setEmailError(emailValidation.error || "Invalid email")
            return
        }

        if (!password) {
            setError("Password is required")
            return
        }

        setIsLoading(true)

        try {
            await login(normalizeEmail(email), password)
            router.push("/dashboard")
        } catch (err) {
            setError(err instanceof Error ? err.message : "Login failed. Please try again.")
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className={cn(
                "relative p-8 rounded-3xl",
                "bg-gradient-to-br from-white/10 via-white/5 to-transparent",
                "backdrop-blur-2xl",
                "border border-white/20",
                "shadow-[0_0_80px_rgba(139,92,246,0.15),0_20px_60px_rgba(0,0,0,0.4)]"
            )}
        >
            {/* Shiny border effect */}
            <motion.div
                className="absolute inset-0 rounded-3xl opacity-50"
                style={{
                    background: "linear-gradient(135deg, rgba(139,92,246,0.3) 0%, transparent 50%, rgba(236,72,153,0.2) 100%)",
                }}
                animate={{
                    opacity: [0.3, 0.5, 0.3],
                }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
            />

            {/* Content */}
            <div className="relative z-10 space-y-6">
                {/* Header */}
                <div className="text-center">
                    {/* Logo */}
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        className="flex items-center justify-center gap-2 mb-6"
                    >
                        <div className={cn(
                            "p-2.5 rounded-xl",
                            "bg-gradient-to-br from-purple-600/30 to-pink-600/20",
                            "border border-purple-500/30",
                            "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                        )}>
                            <Terminal className="w-5 h-5 text-purple-300" />
                        </div>
                        <span className="text-xl font-bold bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent">
                            DevOpsHub
                        </span>
                    </motion.div>

                    <h1 className="text-2xl font-bold bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent">
                        Välkommen tillbaka
                    </h1>
                    <p className="mt-2 text-sm text-zinc-400">
                        Logga in för att fortsätta din resa
                    </p>
                </div>

                {/* Social login */}
                <SocialButtons isLoading={isLoading} />

                {/* Divider */}
                <OrDivider />

                {/* Form */}
                <form onSubmit={handleSubmit} className="space-y-4">
                    {/* Error alert */}
                    <AuthErrorAlert message={error} />

                    {/* Email */}
                    <AuthInput
                        label="E-postadress"
                        type="email"
                        placeholder="du@exempel.com"
                        value={email}
                        onChange={(e) => {
                            setEmail(e.target.value)
                            if (emailError) setEmailError("")
                        }}
                        onBlur={handleEmailBlur}
                        error={emailError}
                        disabled={isLoading}
                        autoComplete="email"
                        required
                    />

                    {/* Password */}
                    <AuthInput
                        label="Lösenord"
                        type="password"
                        placeholder="Ange ditt lösenord"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        disabled={isLoading}
                        autoComplete="current-password"
                        required
                    />

                    {/* Remember me & Forgot password */}
                    <div className="flex items-center justify-between">
                        <AuthCheckbox
                            id="remember-me"
                            label="Kom ihåg mig"
                            checked={rememberMe}
                            onChange={setRememberMe}
                        />
                        <Link
                            href="/forgot-password"
                            className="text-sm font-medium text-purple-400 hover:text-purple-300 transition-colors"
                        >
                            Glömt lösenord?
                        </Link>
                    </div>

                    {/* Submit */}
                    <motion.button
                        type="submit"
                        disabled={isLoading}
                        className={cn(
                            "w-full flex items-center justify-center gap-2",
                            "px-6 py-3.5 rounded-xl",
                            "bg-gradient-to-r from-purple-600 via-purple-500 to-pink-500",
                            "text-white font-bold text-base",
                            "shadow-[0_0_30px_rgba(139,92,246,0.4)]",
                            "border border-purple-400/30",
                            "transition-all duration-300",
                            "disabled:opacity-50 disabled:cursor-not-allowed"
                        )}
                        whileHover={{ scale: 1.02, boxShadow: "0 0 50px rgba(139,92,246,0.5)" }}
                        whileTap={{ scale: 0.98 }}
                    >
                        {isLoading ? (
                            <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        ) : (
                            <>
                                Logga in
                                <ArrowRight className="w-4 h-4" />
                            </>
                        )}
                    </motion.button>
                </form>

                {/* Sign up link */}
                <p className="text-center text-sm text-zinc-400">
                    Har du inget konto?{" "}
                    <Link
                        href="/signup"
                        className="font-semibold text-purple-400 hover:text-purple-300 transition-colors"
                    >
                        Skapa konto
                    </Link>
                </p>

                {/* Free badge */}
                <div className="flex items-center justify-center gap-2 text-xs text-zinc-500">
                    <Sparkles className="w-3 h-3 text-emerald-400" />
                    <span>100% gratis • Ingen kreditkort</span>
                </div>
            </div>
        </motion.div>
    )
}
