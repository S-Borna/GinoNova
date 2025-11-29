/**
 * ============================================================================
 * COLOR TOKENS — Design System v1.0
 * ============================================================================
 *
 * Matching landing page aesthetic with professional SaaS palette.
 * Used across all task pages, modules, dashboards, and interactive components.
 */

export const colors = {
    // Primary brand colors
    primary: {
        DEFAULT: '#4F46E5',
        light: '#6366F1',
        dark: '#4338CA',
        50: '#EEF2FF',
        100: '#E0E7FF',
        200: '#C7D2FE',
        500: '#6366F1',
        600: '#4F46E5',
        700: '#4338CA',
    },

    // Backgrounds
    background: {
        DEFAULT: '#FFFFFF',
        secondary: '#F9FAFB',
        tertiary: '#F3F4F6',
    },

    // Surfaces (cards, code blocks, etc.)
    surface: {
        DEFAULT: '#F6F8FA',
        elevated: '#FFFFFF',
        muted: '#F1F5F9',
    },

    // Borders
    border: {
        DEFAULT: 'rgba(0, 0, 0, 0.08)',
        light: 'rgba(0, 0, 0, 0.05)',
        medium: 'rgba(0, 0, 0, 0.12)',
        dark: 'rgba(0, 0, 0, 0.16)',
    },

    // Text colors
    text: {
        primary: '#111827',
        secondary: '#6B7280',
        tertiary: '#9CA3AF',
        inverse: '#FFFFFF',
        muted: '#9CA3AF',
    },

    // Semantic colors
    success: {
        DEFAULT: '#10B981',
        light: '#D1FAE5',
        dark: '#059669',
    },
    warning: {
        DEFAULT: '#F59E0B',
        light: '#FEF3C7',
        dark: '#D97706',
    },
    error: {
        DEFAULT: '#EF4444',
        light: '#FEE2E2',
        dark: '#DC2626',
    },
    info: {
        DEFAULT: '#3B82F6',
        light: '#DBEAFE',
        dark: '#2563EB',
    },

    // XP/Gamification
    xp: {
        DEFAULT: '#F59E0B',
        light: '#FEF3C7',
        glow: 'rgba(245, 158, 11, 0.2)',
    },

    // Dark mode variants
    dark: {
        background: '#0F172A',
        surface: '#1E293B',
        surfaceElevated: '#334155',
        border: 'rgba(255, 255, 255, 0.08)',
        text: {
            primary: '#F8FAFC',
            secondary: '#94A3B8',
            tertiary: '#64748B',
        },
    },
} as const

// CSS custom properties for runtime theming
export const colorCssVars = {
    '--color-primary': colors.primary.DEFAULT,
    '--color-primary-light': colors.primary.light,
    '--color-background': colors.background.DEFAULT,
    '--color-surface': colors.surface.DEFAULT,
    '--color-border': colors.border.DEFAULT,
    '--color-text-primary': colors.text.primary,
    '--color-text-secondary': colors.text.secondary,
} as const

export type ColorToken = keyof typeof colors
