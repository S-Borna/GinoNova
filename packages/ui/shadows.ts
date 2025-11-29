/**
 * ============================================================================
 * SHADOW TOKENS — Design System v1.0
 * ============================================================================
 *
 * Subtle, professional shadows matching landing page aesthetic.
 * Google/Tesla-inspired minimal elevation system.
 */

export const shadows = {
    // No shadow
    none: 'none',

    // Subtle shadows
    xs: '0 1px 2px rgba(0, 0, 0, 0.04)',
    sm: '0 1px 3px rgba(0, 0, 0, 0.06)',

    // Standard shadows
    md: '0 4px 6px -1px rgba(0, 0, 0, 0.06), 0 2px 4px -2px rgba(0, 0, 0, 0.04)',
    lg: '0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
    xl: '0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04)',

    // Semantic shadows
    card: '0 4px 12px rgba(0, 0, 0, 0.06)',
    cardHover: '0 8px 24px rgba(0, 0, 0, 0.08)',
    code: '0 2px 8px rgba(0, 0, 0, 0.05)',
    codeHover: '0 4px 12px rgba(0, 0, 0, 0.06)',
    dropdown: '0 4px 16px rgba(0, 0, 0, 0.12)',
    modal: '0 24px 48px rgba(0, 0, 0, 0.16)',
    tooltip: '0 2px 8px rgba(0, 0, 0, 0.12)',

    // Interactive states
    focus: '0 0 0 3px rgba(79, 70, 229, 0.2)',
    focusError: '0 0 0 3px rgba(239, 68, 68, 0.2)',
    focusSuccess: '0 0 0 3px rgba(16, 185, 129, 0.2)',

    // Inset shadows
    inset: 'inset 0 2px 4px rgba(0, 0, 0, 0.04)',
    insetCode: 'inset 0 1px 2px rgba(0, 0, 0, 0.02)',

    // Dark mode shadows
    dark: {
        card: '0 4px 12px rgba(0, 0, 0, 0.3)',
        cardHover: '0 8px 24px rgba(0, 0, 0, 0.4)',
        code: '0 2px 8px rgba(0, 0, 0, 0.2)',
        dropdown: '0 4px 16px rgba(0, 0, 0, 0.4)',
    },
} as const

// Tailwind class mappings
export const shadowClasses = {
    card: 'shadow-[0_4px_12px_rgba(0,0,0,0.06)]',
    cardHover: 'hover:shadow-[0_8px_24px_rgba(0,0,0,0.08)]',
    code: 'shadow-[0_2px_8px_rgba(0,0,0,0.05)]',
    dropdown: 'shadow-[0_4px_16px_rgba(0,0,0,0.12)]',
    modal: 'shadow-[0_24px_48px_rgba(0,0,0,0.16)]',
    focus: 'focus:ring-2 focus:ring-primary-500/20',
} as const

export type ShadowToken = keyof typeof shadows
