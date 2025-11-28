"use client"

/**
 * ============================================================================
 * LOGIN PAGE — Premium Sign In Experience
 * ============================================================================
 *
 * Beautiful login page with email/password form, social login,
 * remember me option, and forgot password link.
 *
 * @phase A.2 - Authentication UI
 */

import * as React from "react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { motion } from "framer-motion"
import { Terminal, ArrowRight } from "lucide-react"
import { useAuth } from "@/components/auth"
import {
    AuthInput,
    AuthCheckbox,
    AuthSubmitButton,
    AuthErrorAlert,
} from "@/components/auth/AuthForm"
import { SocialButtons, OrDivider } from "@/components/auth/SocialButtons"
import { validateEmail, normalizeEmail } from "@/lib/auth"

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
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="space-y-8"
        >
            {/* Header */}
            <div className="text-center lg:text-left">
                {/* Mobile logo */}
                <div className="flex items-center justify-center lg:hidden gap-2 mb-6">
                    <div className="p-2 rounded-lg bg-gradient-to-br from-primary-500 to-purple-600">
                        <Terminal className="w-5 h-5 text-white" />
                    </div>
                    <span className="text-xl font-bold text-neutral-900 dark:text-white">
                        DevOpsHub
                    </span>
                </div>

                <h1 className="text-2xl sm:text-3xl font-bold text-neutral-900 dark:text-white">
                    Welcome back
                </h1>
                <p className="mt-2 text-neutral-600 dark:text-neutral-400">
                    Sign in to continue your learning journey
                </p>
            </div>

            {/* Social login */}
            <SocialButtons isLoading={isLoading} />

            {/* Divider */}
            <OrDivider />

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-5">
                {/* Error alert */}
                <AuthErrorAlert message={error} />

                {/* Email */}
                <AuthInput
                    label="Email address"
                    type="email"
                    placeholder="you@example.com"
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
                    label="Password"
                    type="password"
                    placeholder="Enter your password"
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
                        label="Remember me"
                        checked={rememberMe}
                        onChange={setRememberMe}
                    />
                    <Link
                        href="/forgot-password"
                        className="text-sm font-medium text-primary-600 hover:text-primary-500 transition-colors"
                    >
                        Forgot password?
                    </Link>
                </div>

                {/* Submit */}
                <AuthSubmitButton isLoading={isLoading}>
                    Sign in
                    <ArrowRight className="w-4 h-4" />
                </AuthSubmitButton>
            </form>

            {/* Sign up link */}
            <p className="text-center text-sm text-neutral-600 dark:text-neutral-400">
                Don&apos;t have an account?{" "}
                <Link
                    href="/signup"
                    className="font-semibold text-primary-600 hover:text-primary-500 transition-colors"
                >
                    Create account
                </Link>
            </p>
        </motion.div>
    )
}
