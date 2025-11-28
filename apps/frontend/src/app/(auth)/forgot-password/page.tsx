"use client"

/**
 * ============================================================================
 * FORGOT PASSWORD PAGE — Password Recovery
 * ============================================================================
 *
 * Clean forgot password page with email input and success state.
 *
 * @phase A.2 - Authentication UI
 */

import * as React from "react"
import Link from "next/link"
import { motion, AnimatePresence } from "framer-motion"
import { Terminal, ArrowLeft, CheckCircle2, Send } from "lucide-react"
import {
    AuthInput,
    AuthSubmitButton,
    AuthErrorAlert,
} from "@/components/auth/AuthForm"
import { validateEmail, normalizeEmail } from "@/lib/auth"

export default function ForgotPasswordPage() {
    const [email, setEmail] = React.useState("")
    const [error, setError] = React.useState("")
    const [emailError, setEmailError] = React.useState("")
    const [isLoading, setIsLoading] = React.useState(false)
    const [isSubmitted, setIsSubmitted] = React.useState(false)

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

        setIsLoading(true)

        try {
            // TODO: Implement actual password reset API call
            // await requestPasswordReset(normalizeEmail(email))

            // Simulate API call
            await new Promise((resolve) => setTimeout(resolve, 1500))
            setIsSubmitted(true)
        } catch (err) {
            setError(
                err instanceof Error
                    ? err.message
                    : "Failed to send reset email. Please try again."
            )
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="space-y-6"
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

                <AnimatePresence mode="wait">
                    {!isSubmitted ? (
                        <motion.div
                            key="header"
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                        >
                            <h1 className="text-2xl sm:text-3xl font-bold text-neutral-900 dark:text-white">
                                Reset your password
                            </h1>
                            <p className="mt-2 text-neutral-600 dark:text-neutral-400">
                                Enter your email and we&apos;ll send you a reset link
                            </p>
                        </motion.div>
                    ) : (
                        <motion.div
                            key="success-header"
                            initial={{ opacity: 0, scale: 0.95 }}
                            animate={{ opacity: 1, scale: 1 }}
                        >
                            <div className="flex items-center justify-center lg:justify-start gap-3 mb-2">
                                <div className="p-2 rounded-full bg-success-100 dark:bg-success-900/30">
                                    <CheckCircle2 className="w-6 h-6 text-success-600 dark:text-success-400" />
                                </div>
                                <h1 className="text-2xl sm:text-3xl font-bold text-neutral-900 dark:text-white">
                                    Check your inbox
                                </h1>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>

            <AnimatePresence mode="wait">
                {!isSubmitted ? (
                    <motion.form
                        key="form"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0, y: -20 }}
                        onSubmit={handleSubmit}
                        className="space-y-4"
                    >
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

                        {/* Submit */}
                        <AuthSubmitButton isLoading={isLoading} className="mt-6">
                            <Send className="w-4 h-4" />
                            Send reset link
                        </AuthSubmitButton>
                    </motion.form>
                ) : (
                    <motion.div
                        key="success"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="space-y-6"
                    >
                        {/* Success message */}
                        <div className="p-4 rounded-xl bg-success-50 dark:bg-success-900/20 border border-success-200 dark:border-success-800">
                            <p className="text-success-800 dark:text-success-200">
                                We&apos;ve sent a password reset link to{" "}
                                <span className="font-semibold">{email}</span>. Please check your
                                email and follow the instructions to reset your password.
                            </p>
                        </div>

                        {/* Helpful tips */}
                        <div className="space-y-3">
                            <h3 className="font-medium text-neutral-900 dark:text-white">
                                Didn&apos;t receive the email?
                            </h3>
                            <ul className="text-sm text-neutral-600 dark:text-neutral-400 space-y-2">
                                <li className="flex items-start gap-2">
                                    <span className="text-primary-500 mt-0.5">•</span>
                                    Check your spam or junk folder
                                </li>
                                <li className="flex items-start gap-2">
                                    <span className="text-primary-500 mt-0.5">•</span>
                                    Make sure you entered the correct email
                                </li>
                                <li className="flex items-start gap-2">
                                    <span className="text-primary-500 mt-0.5">•</span>
                                    Wait a few minutes for the email to arrive
                                </li>
                            </ul>
                        </div>

                        {/* Resend button */}
                        <button
                            type="button"
                            onClick={() => setIsSubmitted(false)}
                            className="w-full py-3 px-4 rounded-xl border border-neutral-300 dark:border-neutral-700
                                       text-neutral-700 dark:text-neutral-300 font-medium
                                       hover:bg-neutral-50 dark:hover:bg-neutral-800
                                       transition-colors duration-200"
                        >
                            Try a different email
                        </button>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Back to login */}
            <div className="pt-4">
                <Link
                    href="/login"
                    className="inline-flex items-center gap-2 text-sm text-neutral-600 dark:text-neutral-400
                             hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Back to sign in
                </Link>
            </div>
        </motion.div>
    )
}
