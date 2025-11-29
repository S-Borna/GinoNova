/**
 * ============================================================================
 * TYPOGRAPHY TOKENS — Design System v1.0
 * ============================================================================
 *
 * Professional typography scale matching landing page quality.
 * Font families: Inter for UI, SF Pro for headings, Roboto Mono for code.
 */

export const typography = {
    // Font families
    fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        display: ['SF Pro Display', 'Inter', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'SF Mono', 'Consolas', 'monospace'],
    },

    // Font sizes (px and rem)
    fontSize: {
        xs: ['12px', { lineHeight: '16px', letterSpacing: '0.01em' }],
        sm: ['14px', { lineHeight: '20px', letterSpacing: '0' }],
        base: ['16px', { lineHeight: '24px', letterSpacing: '-0.01em' }],
        lg: ['18px', { lineHeight: '28px', letterSpacing: '-0.01em' }],
        xl: ['20px', { lineHeight: '28px', letterSpacing: '-0.02em' }],
        '2xl': ['24px', { lineHeight: '32px', letterSpacing: '-0.02em' }],
        '3xl': ['30px', { lineHeight: '36px', letterSpacing: '-0.02em' }],
        '4xl': ['34px', { lineHeight: '40px', letterSpacing: '-0.02em' }],
        '5xl': ['48px', { lineHeight: '56px', letterSpacing: '-0.03em' }],
    },

    // Font weights
    fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
    },

    // Heading styles (ready-to-use)
    headings: {
        h1: {
            fontSize: '34px',
            fontWeight: '600',
            lineHeight: '40px',
            letterSpacing: '-0.02em',
        },
        h2: {
            fontSize: '24px',
            fontWeight: '500',
            lineHeight: '32px',
            letterSpacing: '-0.02em',
        },
        h3: {
            fontSize: '18px',
            fontWeight: '500',
            lineHeight: '28px',
            letterSpacing: '-0.01em',
        },
        h4: {
            fontSize: '16px',
            fontWeight: '500',
            lineHeight: '24px',
            letterSpacing: '0',
        },
    },

    // Body styles
    body: {
        large: {
            fontSize: '18px',
            fontWeight: '400',
            lineHeight: '28px',
        },
        base: {
            fontSize: '16px',
            fontWeight: '400',
            lineHeight: '24px',
        },
        small: {
            fontSize: '14px',
            fontWeight: '400',
            lineHeight: '20px',
        },
    },

    // Code styles
    code: {
        inline: {
            fontSize: '14px',
            fontWeight: '500',
            fontFamily: 'JetBrains Mono, monospace',
        },
        block: {
            fontSize: '14px',
            fontWeight: '400',
            lineHeight: '22px',
            fontFamily: 'JetBrains Mono, monospace',
        },
    },

    // Label/Caption styles
    caption: {
        fontSize: '12px',
        fontWeight: '500',
        lineHeight: '16px',
        letterSpacing: '0.02em',
        textTransform: 'uppercase' as const,
    },
} as const

// Tailwind class mappings
export const typographyClasses = {
    h1: 'text-[34px] font-semibold leading-[40px] tracking-tight',
    h2: 'text-2xl font-medium leading-8 tracking-tight',
    h3: 'text-lg font-medium leading-7',
    h4: 'text-base font-medium leading-6',
    body: 'text-base font-normal leading-6',
    bodySmall: 'text-sm font-normal leading-5',
    code: 'text-sm font-medium font-mono',
    caption: 'text-xs font-medium uppercase tracking-wide',
} as const

export type TypographyToken = keyof typeof typography
