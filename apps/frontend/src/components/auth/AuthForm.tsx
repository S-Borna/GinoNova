"use client"

/**
 * ============================================================================
 * AUTH FORM — Reusable Form Components
 * ============================================================================
 *
 * Premium form components for authentication pages with
 * animated focus states, error handling, and accessibility.
 *
 * @phase A.2 - Authentication UI
 */

import * as React from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Eye, EyeOff, AlertCircle, Check, Loader2 } from "lucide-react"

/* ============================================================================
   INPUT COMPONENT
   ============================================================================ */

interface AuthInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label: string
    error?: string
    success?: boolean
}

export const AuthInput = React.forwardRef<HTMLInputElement, AuthInputProps>(
    ({ label, error, success, className, type, id, ...props }, ref) => {
        const [showPassword, setShowPassword] = React.useState(false)
        const [isFocused, setIsFocused] = React.useState(false)
        const inputId = id || label.toLowerCase().replace(/\s+/g, "-")
        const isPassword = type === "password"

        return (
            <div className="space-y-1.5">
                <label
                    htmlFor={inputId}
                    className="block text-sm font-medium text-neutral-700 dark:text-neutral-300"
                >
                    {label}
                </label>
                <div className="relative">
                    <input
                        ref={ref}
                        id={inputId}
                        type={isPassword && showPassword ? "text" : type}
                        onFocus={() => setIsFocused(true)}
                        onBlur={() => setIsFocused(false)}
                        className={cn(
                            "w-full px-4 py-3 rounded-xl text-sm",
                            "bg-neutral-50 dark:bg-neutral-900",
                            "border-2 transition-all duration-200",
                            "placeholder:text-neutral-400 dark:placeholder:text-neutral-500",
                            "disabled:opacity-50 disabled:cursor-not-allowed",
                            // States
                            error
                                ? "border-red-500 focus:border-red-500 focus:ring-2 focus:ring-red-500/20"
                                : success
                                    ? "border-emerald-500 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"
                                    : isFocused
                                        ? "border-primary-500 ring-2 ring-primary-500/20"
                                        : "border-neutral-200 dark:border-neutral-700 hover:border-neutral-300 dark:hover:border-neutral-600",
                            isPassword && "pr-12",
                            className
                        )}
                        {...props}
                    />

                    {/* Password toggle */}
                    {isPassword && (
                        <button
                            type="button"
                            onClick={() => setShowPassword(!showPassword)}
                            className="absolute right-3 top-1/2 -translate-y-1/2 p-1 text-neutral-400 hover:text-neutral-600 transition-colors"
                            tabIndex={-1}
                        >
                            {showPassword ? (
                                <EyeOff className="w-5 h-5" />
                            ) : (
                                <Eye className="w-5 h-5" />
                            )}
                        </button>
                    )}

                    {/* Success indicator */}
                    {success && !isPassword && (
                        <div className="absolute right-3 top-1/2 -translate-y-1/2">
                            <Check className="w-5 h-5 text-emerald-500" />
                        </div>
                    )}
                </div>

                {/* Error message */}
                <AnimatePresence>
                    {error && (
                        <motion.div
                            initial={{ opacity: 0, y: -5 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -5 }}
                            className="flex items-center gap-1.5 text-sm text-red-500"
                        >
                            <AlertCircle className="w-4 h-4" />
                            <span>{error}</span>
                        </motion.div>
                    )}
                </AnimatePresence>
            </div>
        )
    }
)

AuthInput.displayName = "AuthInput"

/* ============================================================================
   CHECKBOX COMPONENT
   ============================================================================ */

interface AuthCheckboxProps {
    id: string
    label: React.ReactNode
    checked: boolean
    onChange: (checked: boolean) => void
    className?: string
}

export function AuthCheckbox({
    id,
    label,
    checked,
    onChange,
    className,
}: AuthCheckboxProps) {
    return (
        <label
            htmlFor={id}
            className={cn(
                "flex items-center gap-3 cursor-pointer group",
                className
            )}
        >
            <div className="relative">
                <input
                    type="checkbox"
                    id={id}
                    checked={checked}
                    onChange={(e) => onChange(e.target.checked)}
                    className="peer sr-only"
                />
                <div
                    className={cn(
                        "w-5 h-5 rounded-md border-2 transition-all duration-200",
                        "flex items-center justify-center",
                        checked
                            ? "bg-primary-500 border-primary-500"
                            : "border-neutral-300 dark:border-neutral-600 group-hover:border-primary-400"
                    )}
                >
                    <AnimatePresence>
                        {checked && (
                            <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                exit={{ scale: 0 }}
                            >
                                <Check className="w-3.5 h-3.5 text-white" />
                            </motion.div>
                        )}
                    </AnimatePresence>
                </div>
            </div>
            <span className="text-sm text-neutral-600 dark:text-neutral-400">
                {label}
            </span>
        </label>
    )
}

/* ============================================================================
   SUBMIT BUTTON
   ============================================================================ */

interface AuthSubmitButtonProps {
    children: React.ReactNode
    isLoading?: boolean
    disabled?: boolean
    className?: string
}

export function AuthSubmitButton({
    children,
    isLoading = false,
    disabled = false,
    className,
}: AuthSubmitButtonProps) {
    return (
        <button
            type="submit"
            disabled={disabled || isLoading}
            className={cn(
                "w-full flex items-center justify-center gap-2",
                "px-4 py-3.5 rounded-xl text-sm font-semibold",
                "bg-gradient-to-r from-primary-500 to-primary-600",
                "text-white shadow-lg shadow-primary-500/25",
                "hover:from-primary-600 hover:to-primary-700 hover:shadow-xl hover:shadow-primary-500/30",
                "hover:-translate-y-0.5 active:translate-y-0",
                "disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0",
                "transition-all duration-200",
                className
            )}
        >
            {isLoading ? (
                <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    <span>Please wait...</span>
                </>
            ) : (
                children
            )}
        </button>
    )
}

/* ============================================================================
   ERROR ALERT
   ============================================================================ */

interface AuthErrorAlertProps {
    message: string
    className?: string
}

export function AuthErrorAlert({ message, className }: AuthErrorAlertProps) {
    if (!message) return null

    return (
        <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "flex items-center gap-3 p-4 rounded-xl",
                "bg-red-50 dark:bg-red-900/20",
                "border border-red-200 dark:border-red-800",
                "text-red-700 dark:text-red-400",
                className
            )}
        >
            <AlertCircle className="w-5 h-5 flex-shrink-0" />
            <p className="text-sm">{message}</p>
        </motion.div>
    )
}

export default AuthInput
