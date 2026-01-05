"use client"

/**
 * ============================================================================
 * SIGNUP PAGE — Premium Account Creation
 * ============================================================================
 *
 * Beautiful signup page with name, email, password fields,
 * password confirmation, terms acceptance, and social login.
 *
 * @phase A.2 - Authentication UI
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
import {
    validateEmail,
    validatePassword,
    normalizeEmail,
    PASSWORD_MIN_LENGTH,
} from "@/lib/auth"

export default function SignupPage() {
    const [firstName, setFirstName] = React.useState("")
    const [lastName, setLastName] = React.useState("")
    const [email, setEmail] = React.useState("")
    const [password, setPassword] = React.useState("")
    const [confirmPassword, setConfirmPassword] = React.useState("")
    const [acceptTerms, setAcceptTerms] = React.useState(false)
    const [error, setError] = React.useState("")
    const [nameError, setNameError] = React.useState("")
    const [emailError, setEmailError] = React.useState("")
    const [passwordError, setPasswordError] = React.useState("")
    const [confirmError, setConfirmError] = React.useState("")
    const [isLoading, setIsLoading] = React.useState(false)

    const { register } = useAuth()
    const router = useRouter()

    const handleEmailBlur = () => {
        if (email) {
            const validation = validateEmail(email)
            setEmailError(validation.valid ? "" : validation.error || "")
        }
    }

    const handlePasswordBlur = () => {
        if (password) {
            const validation = validatePassword(password)
            setPasswordError(validation.valid ? "" : validation.error || "")
        }
    }

    const handleConfirmBlur = () => {
        if (confirmPassword && password !== confirmPassword) {
            setConfirmError("Passwords do not match")
        } else {
            setConfirmError("")
        }
    }

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        setError("")
        setNameError("")
        setEmailError("")
        setPasswordError("")
        setConfirmError("")

        // Validation - require first and last name
        if (!firstName.trim() || !lastName.trim()) {
            setNameError("Both first and last name are required")
            return
        }

        const fullName = `${firstName.trim()} ${lastName.trim()}`

        // Validation
        const emailValidation = validateEmail(email)
        if (!emailValidation.valid) {
            setEmailError(emailValidation.error || "Invalid email")
            return
        }

        const passwordValidation = validatePassword(password)
        if (!passwordValidation.valid) {
            setPasswordError(passwordValidation.error || "Invalid password")
            return
        }

        if (password !== confirmPassword) {
            setConfirmError("Passwords do not match")
            return
        }

        if (!acceptTerms) {
            setError("Please accept the terms and conditions")
            return
        }

        setIsLoading(true)

        try {
            await register(normalizeEmail(email), password, fullName)
            router.push("/dashboard")
        } catch (err) {
            setError(err instanceof Error ? err.message : "Registration failed. Please try again.")
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
                <motion.div
                    className="flex items-center justify-center lg:hidden gap-2 mb-6"
                    animate={{ opacity: 1 }}
                >
                    <motion.div
                        animate={{ rotate: 360 }}
                        transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
                    >
                        <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 via-pink-500 to-cyan-400 flex items-center justify-center shadow-[0_0_20px_rgba(168,85,247,0.6)]">
                            <Sparkles className="w-5 h-5 text-white" />
                        </div>
                    </motion.div>
                    <div className="flex items-baseline">
                        <span className="text-2xl font-black tracking-tight bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text text-transparent">
                            Gino
                        </span>
                        <span
                            className="text-2xl font-black tracking-tight"
                            style={{
                                background: "linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #06b6d4 100%)",
                                WebkitBackgroundClip: "text",
                                WebkitTextFillColor: "transparent",
                                filter: "drop-shadow(0 0 8px rgba(168,85,247,0.5))",
                            }}
                        >
                            Nova
                        </span>
                    </div>
                </motion.div>

                <h1 className="text-2xl sm:text-3xl font-bold text-neutral-900 dark:text-white">
                    Create your account
                </h1>
                <p className="mt-2 text-neutral-600 dark:text-neutral-400">
                    Start your DevOps journey today
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

                {/* Name fields - side by side */}
                <div className="grid grid-cols-2 gap-3">
                    <AuthInput
                        label="First name"
                        type="text"
                        placeholder="John"
                        value={firstName}
                        onChange={(e) => {
                            setFirstName(e.target.value)
                            if (nameError) setNameError("")
                        }}
                        error={nameError && !firstName.trim() ? nameError : ""}
                        disabled={isLoading}
                        autoComplete="given-name"
                        required
                    />
                    <AuthInput
                        label="Last name"
                        type="text"
                        placeholder="Doe"
                        value={lastName}
                        onChange={(e) => {
                            setLastName(e.target.value)
                            if (nameError) setNameError("")
                        }}
                        error={nameError && !lastName.trim() ? nameError : ""}
                        disabled={isLoading}
                        autoComplete="family-name"
                        required
                    />
                </div>

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
                    label={`Password (min ${PASSWORD_MIN_LENGTH} characters)`}
                    type="password"
                    placeholder="Create a strong password"
                    value={password}
                    onChange={(e) => {
                        setPassword(e.target.value)
                        if (passwordError) setPasswordError("")
                    }}
                    onBlur={handlePasswordBlur}
                    error={passwordError}
                    disabled={isLoading}
                    autoComplete="new-password"
                    required
                />

                {/* Confirm password */}
                <AuthInput
                    label="Confirm password"
                    type="password"
                    placeholder="Confirm your password"
                    value={confirmPassword}
                    onChange={(e) => {
                        setConfirmPassword(e.target.value)
                        if (confirmError) setConfirmError("")
                    }}
                    onBlur={handleConfirmBlur}
                    error={confirmError}
                    success={confirmPassword.length > 0 && password === confirmPassword}
                    disabled={isLoading}
                    autoComplete="new-password"
                    required
                />

                {/* Terms checkbox */}
                <AuthCheckbox
                    id="accept-terms"
                    label={
                        <>
                            I agree to the{" "}
                            <Link
                                href="/terms"
                                className="text-primary-600 hover:text-primary-500"
                            >
                                Terms of Service
                            </Link>{" "}
                            and{" "}
                            <Link
                                href="/privacy"
                                className="text-primary-600 hover:text-primary-500"
                            >
                                Privacy Policy
                            </Link>
                        </>
                    }
                    checked={acceptTerms}
                    onChange={setAcceptTerms}
                    className="pt-2"
                />

                {/* Submit */}
                <AuthSubmitButton isLoading={isLoading} className="mt-6">
                    <Sparkles className="w-4 h-4" />
                    Create account
                    <ArrowRight className="w-4 h-4" />
                </AuthSubmitButton>
            </form>

            {/* Sign in link */}
            <p className="text-center text-sm text-neutral-600 dark:text-neutral-400">
                Already have an account?{" "}
                <Link
                    href="/login"
                    className="font-semibold text-primary-600 hover:text-primary-500 transition-colors"
                >
                    Sign in
                </Link>
            </p>
        </motion.div>
    )
}
