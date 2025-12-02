// My DOE Hub - Premium Student Design System
// "Learn like a pro, feel like home"

export const colors = {
    // Backgrounds - Rich, deep darks (samma approach som MakeThePlay)
    bg: {
        primary: '#0a0a0f',      // Djupare än tidigare
        secondary: '#0f0f17',    // Sidebar, cards
        tertiary: '#141420',     // Elevated elements
        card: '#12121c',         // Module cards
        elevated: '#1a1a28',     // Hover states
    },

    // Purple/Violet - Signature color (raffinerad)
    purple: {
        50: '#faf5ff',
        100: '#f3e8ff',
        200: '#e9d5ff',
        300: '#d8b4fe',
        400: '#c084fc',
        500: '#a855f7',          // Primary accent
        600: '#9333ea',          // Hover
        700: '#7e22ce',          // Active
        800: '#6b21a8',
        900: '#581c87',
        glow: 'rgba(168, 85, 247, 0.25)',
        glowStrong: 'rgba(168, 85, 247, 0.4)',
    },

    // Gradient för hero/banners
    gradient: {
        hero: 'linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #c084fc 100%)',
        heroSubtle: 'linear-gradient(135deg, rgba(124, 58, 237, 0.8) 0%, rgba(168, 85, 247, 0.6) 100%)',
        card: 'linear-gradient(135deg, rgba(168, 85, 247, 0.1) 0%, rgba(124, 58, 237, 0.05) 100%)',
        primary: 'linear-gradient(135deg, #a855f7 0%, #7c3aed 100%)',
        gold: 'linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%)',
    },

    // Semantic - XP & Progress
    xp: {
        gold: '#fbbf24',         // XP color
        goldGlow: 'rgba(251, 191, 36, 0.2)',
    },
    streak: {
        fire: '#f97316',         // Streak fire
        fireGlow: 'rgba(249, 115, 22, 0.2)',
    },
    success: {
        green: '#22c55e',        // Completed
        greenGlow: 'rgba(34, 197, 94, 0.15)',
    },

    // Text hierarchy
    text: {
        primary: '#f8fafc',      // Bright white
        secondary: '#a1a1aa',    // Zinc-400
        muted: '#71717a',        // Zinc-500
        disabled: '#52525b',     // Zinc-600
    },

    // Borders
    border: {
        subtle: 'rgba(255, 255, 255, 0.06)',
        default: 'rgba(255, 255, 255, 0.1)',
        hover: 'rgba(255, 255, 255, 0.15)',
        purple: 'rgba(168, 85, 247, 0.3)',
    }
} as const;

export const typography = {
    fontFamily: {
        sans: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
        mono: "'JetBrains Mono', 'SF Mono', monospace",
        display: "'Inter', -apple-system, sans-serif",
    },

    fontSize: {
        xs: '11px',
        sm: '13px',
        base: '14px',
        lg: '16px',
        xl: '20px',
        '2xl': '24px',
        '3xl': '32px',
        '4xl': '40px',
        '5xl': '48px',
    },

    fontWeight: {
        light: 300,
        normal: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
        extrabold: 800,
    },
} as const;

export const shadows = {
    sm: '0 1px 2px rgba(0, 0, 0, 0.4)',
    md: '0 4px 6px rgba(0, 0, 0, 0.4)',
    lg: '0 10px 25px rgba(0, 0, 0, 0.5)',
    glow: {
        purple: '0 0 20px rgba(168, 85, 247, 0.2)',
        purpleStrong: '0 0 30px rgba(168, 85, 247, 0.35)',
        gold: '0 0 15px rgba(251, 191, 36, 0.25)',
        fire: '0 0 15px rgba(249, 115, 22, 0.25)',
    },
    card: '0 4px 20px rgba(0, 0, 0, 0.3)',
    cardHover: '0 8px 30px rgba(0, 0, 0, 0.4)',
} as const;

export const borderRadius = {
    sm: '6px',
    md: '8px',
    lg: '12px',
    xl: '16px',
    '2xl': '20px',
    '3xl': '24px',
    full: '9999px',
} as const;

export const spacing = {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px',
    '2xl': '48px',
    '3xl': '64px',
} as const;

export const animation = {
    duration: {
        fast: '150ms',
        normal: '200ms',
        slow: '300ms',
        slower: '500ms',
    },
    easing: {
        default: 'cubic-bezier(0.4, 0, 0.2, 1)',
        in: 'cubic-bezier(0.4, 0, 1, 1)',
        out: 'cubic-bezier(0, 0, 0.2, 1)',
        bounce: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
    },
} as const;

// Export default theme object
const theme = {
    colors,
    typography,
    shadows,
    borderRadius,
    spacing,
    animation,
} as const;

export default theme;
