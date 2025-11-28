/**
 * Button Component
 * Phase D.1: Apple-Inspired Premium Button System
 *
 * Features:
 * - 10 variants including gradient, glass, and glow effects
 * - 5 sizes from xs to xl
 * - Smooth transitions and micro-interactions
 * - Full accessibility support
 */

import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

/* ============================================================================
   BUTTON VARIANTS
   ============================================================================ */

const buttonVariants = cva(
  // Base styles: Foundation for all buttons
  [
    "inline-flex",
    "items-center",
    "justify-center",
    "gap-2",
    "whitespace-nowrap",
    "rounded-lg",
    "text-sm",
    "font-medium",
    "transition-all",
    "duration-200",
    // Focus states
    "focus-visible:outline-none",
    "focus-visible:ring-2",
    "focus-visible:ring-indigo-500",
    "focus-visible:ring-offset-2",
    // Disabled states
    "disabled:pointer-events-none",
    "disabled:opacity-50",
    // Icon handling
    "[&_svg]:pointer-events-none",
    "[&_svg]:size-4",
    "[&_svg]:shrink-0",
  ],
  {
    variants: {
      /**
       * Visual style variants
       */
      variant: {
        // Default: Solid primary button
        default: [
          "bg-indigo-600",
          "text-white",
          "shadow-sm",
          "hover:bg-indigo-700",
          "active:bg-indigo-800",
        ],

        // Gradient: Premium gradient effect (Apple-style)
        gradient: [
          "bg-gradient-to-r",
          "from-indigo-500",
          "to-purple-600",
          "text-white",
          "shadow-md",
          "hover:from-indigo-600",
          "hover:to-purple-700",
          "hover:shadow-lg",
          "hover:-translate-y-0.5",
          "active:translate-y-0",
          "active:shadow-md",
        ],

        // Ghost Gradient: Subtle gradient on hover
        "ghost-gradient": [
          "text-indigo-600",
          "dark:text-indigo-400",
          "hover:bg-gradient-to-r",
          "hover:from-indigo-50",
          "hover:to-indigo-100/50",
          "dark:hover:from-indigo-900/30",
          "dark:hover:to-indigo-800/20",
        ],

        // Glow: Gradient with animated glow effect
        glow: [
          "bg-gradient-to-r",
          "from-indigo-500",
          "to-purple-600",
          "text-white",
          "shadow-lg",
          "shadow-indigo-500/30",
          "hover:shadow-xl",
          "hover:shadow-indigo-500/40",
          "hover:-translate-y-0.5",
          "active:translate-y-0",
          "transition-all",
          "duration-300",
        ],

        // Glass: Glassmorphism effect
        glass: [
          "bg-white/10",
          "backdrop-blur-md",
          "border",
          "border-white/20",
          "text-gray-900",
          "shadow-sm",
          "hover:bg-white/20",
          "hover:border-white/30",
          "dark:text-white",
          "dark:hover:bg-white/15",
        ],

        // Destructive: Danger/delete actions
        destructive: [
          "bg-red-500",
          "text-white",
          "shadow-sm",
          "hover:bg-red-600",
          "active:bg-red-700",
        ],

        // Outline: Bordered button
        outline: [
          "border",
          "border-gray-200",
          "bg-transparent",
          "text-gray-900",
          "shadow-sm",
          "hover:bg-gray-50",
          "hover:border-gray-300",
          "dark:border-gray-700",
          "dark:text-gray-100",
          "dark:hover:bg-gray-800",
          "dark:hover:border-gray-600",
        ],

        // Secondary: Muted secondary button
        secondary: [
          "bg-gray-100",
          "text-gray-900",
          "shadow-sm",
          "hover:bg-gray-200",
          "active:bg-gray-300",
          "dark:bg-gray-800",
          "dark:text-gray-100",
          "dark:hover:bg-gray-700",
        ],

        // Ghost: Minimal hover effect
        ghost: [
          "text-gray-600",
          "hover:bg-gray-100",
          "hover:text-gray-900",
          "dark:text-gray-400",
          "dark:hover:bg-gray-800",
          "dark:hover:text-gray-100",
        ],

        // Link: Text-only with underline
        link: [
          "text-indigo-600",
          "underline-offset-4",
          "hover:underline",
          "dark:text-indigo-400",
        ],
      },

      /**
       * Size variants
       */
      size: {
        xs: "h-7 px-2.5 text-xs rounded-md",
        sm: "h-8 px-3 text-xs rounded-md",
        default: "h-9 px-4 py-2",
        lg: "h-10 px-6 text-base",
        xl: "h-12 px-8 text-base font-semibold rounded-xl",
        icon: "h-9 w-9",
        "icon-sm": "h-8 w-8",
        "icon-lg": "h-10 w-10",
      },

      /**
       * Full width option
       */
      fullWidth: {
        true: "w-full",
        false: "",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
      fullWidth: false,
    },
  }
)

/* ============================================================================
   BUTTON COMPONENT
   ============================================================================ */

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
  VariantProps<typeof buttonVariants> {
  /**
   * Render as child element (for composition with Next.js Link, etc.)
   */
  asChild?: boolean
  /**
   * Loading state with spinner
   */
  loading?: boolean
  /**
   * Icon to display before text
   */
  leftIcon?: React.ReactNode
  /**
   * Icon to display after text
   */
  rightIcon?: React.ReactNode
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      className,
      variant,
      size,
      fullWidth,
      asChild = false,
      loading = false,
      leftIcon,
      rightIcon,
      disabled,
      children,
      ...props
    },
    ref
  ) => {
    const Comp = asChild ? Slot : "button"
    const isDisabled = disabled || loading

    return (
      <Comp
        className={cn(buttonVariants({ variant, size, fullWidth, className }))}
        ref={ref}
        disabled={isDisabled}
        {...props}
      >
        {/* Loading spinner */}
        {loading && (
          <svg
            className="animate-spin -ml-1 mr-2 h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            />
          </svg>
        )}

        {/* Left icon */}
        {!loading && leftIcon && (
          <span className="inline-flex shrink-0">{leftIcon}</span>
        )}

        {/* Button content */}
        {children}

        {/* Right icon */}
        {rightIcon && (
          <span className="inline-flex shrink-0">{rightIcon}</span>
        )}
      </Comp>
    )
  }
)
Button.displayName = "Button"

/* ============================================================================
   EXPORTS
   ============================================================================ */

export { Button, buttonVariants }
