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
    "focus-visible:ring-primary-500",
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
          "bg-primary-600",
          "text-white",
          "shadow-sm",
          "hover:bg-primary-700",
          "active:bg-primary-800",
        ],

        // Gradient: Premium gradient effect (Apple-style)
        gradient: [
          "bg-gradient-to-r",
          "from-primary-500",
          "to-primary-600",
          "text-white",
          "shadow-md",
          "hover:from-primary-600",
          "hover:to-primary-700",
          "hover:shadow-lg",
          "hover:-translate-y-0.5",
          "active:translate-y-0",
          "active:shadow-md",
        ],

        // Ghost Gradient: Subtle gradient on hover
        "ghost-gradient": [
          "text-primary-600",
          "dark:text-primary-400",
          "hover:bg-gradient-to-r",
          "hover:from-primary-50",
          "hover:to-primary-100/50",
          "dark:hover:from-primary-900/30",
          "dark:hover:to-primary-800/20",
        ],

        // Glow: Gradient with animated glow effect
        glow: [
          "bg-gradient-to-r",
          "from-primary-500",
          "to-primary-600",
          "text-white",
          "shadow-glow-primary",
          "hover:shadow-glow-lg",
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
          "text-neutral-900",
          "shadow-soft",
          "hover:bg-white/20",
          "hover:border-white/30",
          "dark:text-white",
          "dark:hover:bg-white/15",
        ],

        // Destructive: Danger/delete actions
        destructive: [
          "bg-accent-danger",
          "text-white",
          "shadow-sm",
          "hover:bg-red-600",
          "active:bg-red-700",
        ],

        // Outline: Bordered button
        outline: [
          "border",
          "border-neutral-200",
          "bg-transparent",
          "text-neutral-900",
          "shadow-sm",
          "hover:bg-neutral-50",
          "hover:border-neutral-300",
          "dark:border-neutral-700",
          "dark:text-neutral-100",
          "dark:hover:bg-neutral-800",
          "dark:hover:border-neutral-600",
        ],

        // Secondary: Muted secondary button
        secondary: [
          "bg-neutral-100",
          "text-neutral-900",
          "shadow-sm",
          "hover:bg-neutral-200",
          "active:bg-neutral-300",
          "dark:bg-neutral-800",
          "dark:text-neutral-100",
          "dark:hover:bg-neutral-700",
        ],

        // Ghost: Minimal hover effect
        ghost: [
          "text-neutral-600",
          "hover:bg-neutral-100",
          "hover:text-neutral-900",
          "dark:text-neutral-400",
          "dark:hover:bg-neutral-800",
          "dark:hover:text-neutral-100",
        ],

        // Link: Text-only with underline
        link: [
          "text-primary-600",
          "underline-offset-4",
          "hover:underline",
          "dark:text-primary-400",
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
