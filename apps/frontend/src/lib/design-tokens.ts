/**
 * ============================================================================
 * DESIGN TOKENS — Material 3 + Tesla + Apple Hybrid System
 * ============================================================================
 *
 * Unified design tokens for:
 * - Typography (Inter, SF Pro, Roboto)
 * - Spacing (Tesla-inspired generous whitespace)
 * - Shadows (subtle, layered)
 * - Border radius (Apple-style rounded)
 * - Colors (minimal, functional)
 *
 * @version 2.0
 * @date 2025-11-29
 */

/* ============================================================================
   TYPOGRAPHY
   ============================================================================ */

export const typography = {
    // Font families
    fontFamily: {
        sans: 'Inter, "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        mono: '"SF Mono", "Fira Code", "JetBrains Mono", Consolas, monospace',
    },

    // Font sizes
    fontSize: {
        h1: "34px",
        h2: "24px",
        h3: "18px",
        body: "16px",
        small: "14px",
        code: "14px",
        meta: "12px",
    },

    // Font weights
    fontWeight: {
        regular: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
    },

    // Line heights
    lineHeight: {
        tight: 1.3,
        normal: 1.6,
        relaxed: 1.75,
    },
} as const

/* ============================================================================
   SPACING — Tesla-inspired generous whitespace
   ============================================================================ */

export const spacing = {
    // Base unit: 4px
    xs: "4px",
    sm: "8px",
    md: "12px",
    lg: "16px",
    xl: "20px",
    "2xl": "24px",
    "3xl": "28px",
    "4xl": "32px",
    "5xl": "40px",
    "6xl": "48px",

    // Semantic spacing
    section: "32px",           // Section padding
    blockGap: "24px",          // Gap between content blocks
    textAboveCode: "28px",     // Space above code blocks
    textBelowCode: "16px",     // Space below code blocks
    cardPadding: "20px",       // Card internal padding
    cardGap: "16px",           // Gap between cards
    contentMaxWidth: "840px",  // Max width for content
} as const

/* ============================================================================
   SHADOWS — Subtle, layered for depth
   ============================================================================ */

export const shadows = {
    none: "none",
    sm: "0 1px 2px rgba(0, 0, 0, 0.04)",
    md: "0 2px 8px rgba(0, 0, 0, 0.05)",
    lg: "0 4px 12px rgba(0, 0, 0, 0.06)",
    xl: "0 8px 24px rgba(0, 0, 0, 0.08)",

    // Interactive states
    cardHover: "0 4px 12px rgba(0, 0, 0, 0.06)",
    codeBlock: "0 2px 8px rgba(0, 0, 0, 0.05)",
    button: "0 2px 6px rgba(0, 0, 0, 0.08)",
    buttonHover: "0 4px 12px rgba(0, 0, 0, 0.12)",
} as const

/* ============================================================================
   BORDER RADIUS — Apple-style rounded corners
   ============================================================================ */

export const borderRadius = {
    none: "0",
    sm: "6px",
    md: "8px",
    lg: "12px",
    xl: "16px",
    "2xl": "20px",
    full: "9999px",

    // Semantic
    card: "16px",
    codeBlock: "12px",
    button: "12px",
    input: "10px",
    badge: "8px",
    tag: "6px",
} as const

/* ============================================================================
   COLORS — Functional, minimal palette
   ============================================================================ */

export const colors = {
    // Backgrounds
    background: {
        primary: "#ffffff",
        secondary: "#fafafa",
        tertiary: "#f5f5f5",
        code: "#f6f8fa",
        dark: {
            primary: "#0a0a0a",
            secondary: "#121212",
            tertiary: "#1a1a1a",
            code: "#1e1e1e",
        },
    },

    // Text
    text: {
        primary: "#171717",
        secondary: "#525252",
        tertiary: "#737373",
        muted: "#a3a3a3",
        dark: {
            primary: "#fafafa",
            secondary: "#d4d4d4",
            tertiary: "#a3a3a3",
            muted: "#737373",
        },
    },

    // Borders
    border: {
        default: "rgba(0, 0, 0, 0.08)",
        subtle: "rgba(0, 0, 0, 0.05)",
        strong: "rgba(0, 0, 0, 0.15)",
        dark: {
            default: "rgba(255, 255, 255, 0.08)",
            subtle: "rgba(255, 255, 255, 0.05)",
            strong: "rgba(255, 255, 255, 0.15)",
        },
    },

    // Accent colors
    accent: {
        primary: "#6366f1",    // Indigo
        secondary: "#8b5cf6",  // Purple
        success: "#22c55e",    // Green
        warning: "#f59e0b",    // Amber
        error: "#ef4444",      // Red
        info: "#3b82f6",       // Blue
    },

    // Table rows
    table: {
        rowAlt: "rgba(0, 0, 0, 0.02)",
        rowHover: "rgba(0, 0, 0, 0.04)",
        dark: {
            rowAlt: "rgba(255, 255, 255, 0.02)",
            rowHover: "rgba(255, 255, 255, 0.04)",
        },
    },
} as const

/* ============================================================================
   TRANSITIONS
   ============================================================================ */

export const transitions = {
    fast: "150ms ease",
    normal: "200ms ease",
    slow: "300ms ease",
    spring: "300ms cubic-bezier(0.34, 1.56, 0.64, 1)",
} as const

/* ============================================================================
   TAILWIND CLASS HELPERS
   ============================================================================ */

export const tw = {
    // Typography classes
    h1: "text-[34px] font-semibold leading-tight tracking-tight",
    h2: "text-2xl font-medium leading-tight",
    h3: "text-lg font-medium leading-snug",
    body: "text-base font-normal leading-relaxed",
    small: "text-sm font-normal leading-relaxed",
    code: "text-sm font-medium font-mono",
    meta: "text-xs font-medium tracking-wide",

    // Spacing helpers
    sectionPadding: "p-8",
    blockGap: "gap-6",
    textAboveCode: "mb-7",
    textBelowCode: "mt-4",
    cardPadding: "p-5",
    contentWidth: "max-w-[840px]",

    // Shadows
    shadowCard: "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",
    shadowCardHover: "hover:shadow-[0_4px_12px_rgba(0,0,0,0.06)]",
    shadowCode: "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",

    // Border radius
    radiusCard: "rounded-2xl",
    radiusCode: "rounded-xl",
    radiusButton: "rounded-xl",
    radiusBadge: "rounded-lg",

    // Borders
    borderSubtle: "border border-black/5 dark:border-white/5",
    borderDefault: "border border-black/[0.08] dark:border-white/[0.08]",

    // Code block
    codeBlock: [
        "bg-[#f6f8fa] dark:bg-[#1e1e1e]",
        "rounded-xl",
        "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",
        "p-5",
        "overflow-x-auto",
        "transition-all duration-200",
        "hover:brightness-[1.02]",
    ].join(" "),

    // Card
    card: [
        "bg-white dark:bg-neutral-900",
        "rounded-2xl",
        "border border-black/5 dark:border-white/5",
        "shadow-[0_2px_8px_rgba(0,0,0,0.05)]",
        "p-5",
        "transition-all duration-200",
        "hover:shadow-[0_4px_12px_rgba(0,0,0,0.06)]",
    ].join(" "),

    // Table
    tableRow: "h-[46px] px-3",
    tableRowAlt: "bg-black/[0.02] dark:bg-white/[0.02]",
    tableBorder: "border border-black/[0.08] dark:border-white/[0.08]",
} as const

const designTokens = {
    typography,
    spacing,
    shadows,
    borderRadius,
    colors,
    transitions,
    tw,
}

export default designTokens
