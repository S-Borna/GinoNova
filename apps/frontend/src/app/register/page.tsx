"use client"

/**
 * Register Page
 * Phase 1.4: Registration form with inline validation
 */

import { useState, FormEvent, useEffect } from "react"
import { useRouter, usePathname } from "next/navigation"
import Link from "next/link"
import { useAuth } from "@/components/auth"
import {
    validateEmail,
    validatePassword,
    normalizeEmail,
    PASSWORD_MIN_LENGTH,
} from "@/lib/auth"

export default function RegisterPage() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [fullName, setFullName] = useState("")
    const [error, setError] = useState("")
    const [emailError, setEmailError] = useState("")
    const [passwordError, setPasswordError] = useState("")
    const [isLoading, setIsLoading] = useState(false)
    const { register } = useAuth()
    const router = useRouter()
    const pathname = usePathname()

    // Clear errors on route change
    useEffect(() => {
        setError("")
        setEmailError("")
        setPasswordError("")
    }, [pathname])

    const handleEmailBlur = () => {
        const validation = validateEmail(email)
        setEmailError(validation.valid ? "" : validation.error || "")
    }

    const handlePasswordBlur = () => {
        const validation = validatePassword(password)
        setPasswordError(validation.valid ? "" : validation.error || "")
    }

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault()
        setError("")
        setEmailError("")
        setPasswordError("")

        // Client-side validation
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

        setIsLoading(true)

        try {
            await register(normalizeEmail(email), password, fullName || undefined)
            router.push("/dashboard")
        } catch (err) {
            setError(err instanceof Error ? err.message : "Registration failed")
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50">
            <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
                <div>
                    <h2 className="text-center text-3xl font-bold text-gray-900">
                        Create your account
                    </h2>
                </div>

                <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                    {error && (
                        <div className="bg-red-50 text-red-500 p-3 rounded text-sm">
                            {error}
                        </div>
                    )}

                    <div className="space-y-4">
                        <div>
                            <label htmlFor="fullName" className="block text-sm font-medium text-gray-700">
                                Full Name (optional)
                            </label>
                            <input
                                id="fullName"
                                name="fullName"
                                type="text"
                                autoComplete="name"
                                value={fullName}
                                onChange={(e) => setFullName(e.target.value)}
                                disabled={isLoading}
                                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
                            />
                        </div>

                        <div>
                            <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                                Email address
                            </label>
                            <input
                                id="email"
                                name="email"
                                type="email"
                                autoComplete="email"
                                required
                                value={email}
                                onChange={(e) => {
                                    setEmail(e.target.value)
                                    if (emailError) setEmailError("")
                                }}
                                onBlur={handleEmailBlur}
                                disabled={isLoading}
                                className={`mt-1 block w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed ${
                                    emailError ? "border-red-500" : "border-gray-300"
                                }`}
                            />
                            {emailError && (
                                <p className="mt-1 text-sm text-red-500">{emailError}</p>
                            )}
                        </div>

                        <div>
                            <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                                Password (min {PASSWORD_MIN_LENGTH} characters)
                            </label>
                            <input
                                id="password"
                                name="password"
                                type="password"
                                autoComplete="new-password"
                                required
                                minLength={PASSWORD_MIN_LENGTH}
                                value={password}
                                onChange={(e) => {
                                    setPassword(e.target.value)
                                    if (passwordError) setPasswordError("")
                                }}
                                onBlur={handlePasswordBlur}
                                disabled={isLoading}
                                className={`mt-1 block w-full px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed ${
                                    passwordError ? "border-red-500" : "border-gray-300"
                                }`}
                            />
                            {passwordError && (
                                <p className="mt-1 text-sm text-red-500">{passwordError}</p>
                            )}
                        </div>
                    </div>

                    <div>
                        <button
                            type="submit"
                            disabled={isLoading}
                            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            {isLoading ? "Creating account..." : "Create account"}
                        </button>
                    </div>

                    <div className="text-center text-sm">
                        <span className="text-gray-600">Already have an account? </span>
                        <Link href="/login" className="text-blue-600 hover:text-blue-500">
                            Sign in
                        </Link>
                    </div>
                </form>
            </div>
        </div>
    )
}
