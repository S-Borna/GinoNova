/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: [
        './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
        './src/components/**/*.{js,ts,jsx,tsx,mdx}',
        './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            /* ================================================================
               COLORS — DevOpsHub Brand & Design Tokens
               ================================================================ */
            colors: {
                // Primary palette (Indigo-based)
                primary: {
                    50: 'var(--primary-50)',
                    100: 'var(--primary-100)',
                    200: 'var(--primary-200)',
                    300: 'var(--primary-300)',
                    400: 'var(--primary-400)',
                    500: 'var(--primary-500)',
                    600: 'var(--primary-600)',
                    700: 'var(--primary-700)',
                    800: 'var(--primary-800)',
                    900: 'var(--primary-900)',
                    950: 'var(--primary-950)',
                    DEFAULT: 'var(--primary-500)',
                },
                // Accent colors
                accent: {
                    success: 'var(--accent-success)',
                    'success-light': 'var(--accent-success-light)',
                    warning: 'var(--accent-warning)',
                    'warning-light': 'var(--accent-warning-light)',
                    danger: 'var(--accent-danger)',
                    'danger-light': 'var(--accent-danger-light)',
                    info: 'var(--accent-info)',
                    'info-light': 'var(--accent-info-light)',
                    xp: 'var(--accent-xp)',
                    'xp-light': 'var(--accent-xp-light)',
                },
                // Neutral scale
                neutral: {
                    50: 'var(--neutral-50)',
                    100: 'var(--neutral-100)',
                    200: 'var(--neutral-200)',
                    300: 'var(--neutral-300)',
                    400: 'var(--neutral-400)',
                    500: 'var(--neutral-500)',
                    600: 'var(--neutral-600)',
                    700: 'var(--neutral-700)',
                    800: 'var(--neutral-800)',
                    900: 'var(--neutral-900)',
                    950: 'var(--neutral-950)',
                },
                // Legacy devops colors (for backward compatibility)
                devops: {
                    primary: 'var(--primary-500)',
                    'primary-dark': 'var(--primary-600)',
                    secondary: 'var(--primary-400)',
                    success: 'var(--accent-success)',
                    warning: 'var(--accent-warning)',
                    info: 'var(--accent-info)',
                    danger: 'var(--accent-danger)',
                },
            },

            /* ================================================================
               TYPOGRAPHY — Inter & JetBrains Mono
               ================================================================ */
            fontFamily: {
                sans: ['var(--font-inter)', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                mono: ['var(--font-mono)', 'JetBrains Mono', 'Fira Code', 'monospace'],
            },
            fontSize: {
                '2xs': ['0.625rem', { lineHeight: '0.875rem' }],
                // Apple-inspired type scale
                'display-2xl': ['4.5rem', { lineHeight: '1', letterSpacing: '-0.02em', fontWeight: '700' }],
                'display-xl': ['3.75rem', { lineHeight: '1', letterSpacing: '-0.02em', fontWeight: '700' }],
                'display-lg': ['3rem', { lineHeight: '1.1', letterSpacing: '-0.02em', fontWeight: '600' }],
                'display-md': ['2.25rem', { lineHeight: '1.2', letterSpacing: '-0.01em', fontWeight: '600' }],
                'display-sm': ['1.875rem', { lineHeight: '1.3', letterSpacing: '-0.01em', fontWeight: '600' }],
            },

            /* ================================================================
               SPACING — Extended scale
               ================================================================ */
            spacing: {
                '18': '4.5rem',
                '88': '22rem',
                '112': '28rem',
                '128': '32rem',
            },

            /* ================================================================
               BORDER RADIUS — Soft, modern curves
               ================================================================ */
            borderRadius: {
                'sm': 'var(--radius-sm)',
                'DEFAULT': 'var(--radius-md)',
                'md': 'var(--radius-md)',
                'lg': 'var(--radius-lg)',
                'xl': 'var(--radius-xl)',
                '2xl': 'var(--radius-2xl)',
                '3xl': 'var(--radius-3xl)',
                '4xl': '2rem',
            },

            /* ================================================================
               BOX SHADOWS — Layered depth system
               ================================================================ */
            boxShadow: {
                'xs': 'var(--shadow-xs)',
                'sm': 'var(--shadow-sm)',
                'DEFAULT': 'var(--shadow-md)',
                'md': 'var(--shadow-md)',
                'lg': 'var(--shadow-lg)',
                'xl': 'var(--shadow-xl)',
                '2xl': 'var(--shadow-2xl)',
                'soft': 'var(--shadow-soft)',
                'inner-soft': 'var(--shadow-inner-soft)',
                // Glow effects
                'glow': 'var(--shadow-glow-primary)',
                'glow-sm': 'var(--shadow-glow-sm)',
                'glow-lg': 'var(--shadow-glow-lg)',
                'glow-primary': 'var(--shadow-glow-primary)',
                'glow-success': 'var(--shadow-glow-success)',
                'glow-warning': 'var(--shadow-glow-warning)',
                'glow-info': 'var(--shadow-glow-info)',
            },

            /* ================================================================
               BACKDROP BLUR
               ================================================================ */
            backdropBlur: {
                xs: '2px',
                glass: 'var(--blur-glass)',
            },

            /* ================================================================
               ANIMATIONS — Apple-inspired motion
               ================================================================ */
            animation: {
                // Entrance animations
                'fade-in': 'fadeIn var(--duration-normal) var(--ease-out) forwards',
                'fade-in-up': 'fadeInUp var(--duration-slow) var(--ease-out) forwards',
                'fade-in-down': 'fadeInDown var(--duration-slow) var(--ease-out) forwards',
                'slide-up': 'slideUp var(--duration-slow) var(--ease-out) forwards',
                'slide-down': 'slideDown var(--duration-slow) var(--ease-out) forwards',
                'scale-in': 'scaleIn var(--duration-normal) var(--ease-out) forwards',
                'pop-in': 'popIn var(--duration-slow) var(--ease-bounce) forwards',
                'bounce-in': 'bounceIn var(--duration-slowest) var(--ease-out) forwards',
                // Continuous animations
                'pulse-soft': 'pulseSoft 2s var(--ease-in-out) infinite',
                'breathe': 'breathe 3s var(--ease-in-out) infinite',
                'float': 'float 3s var(--ease-in-out) infinite',
                'float-slow': 'floatSlow 6s var(--ease-in-out) infinite',
                'spin-slow': 'spinSlow 3s linear infinite',
                // Loading animations
                'shimmer': 'shimmer 2s linear infinite',
                'skeleton': 'skeleton 1.5s ease-in-out infinite',
                'progress-fill': 'progressFill 1s var(--ease-out) forwards',
                // Interactive animations
                'glow': 'glow 2s var(--ease-in-out) infinite',
                'shake': 'shake 0.5s var(--ease-out)',
                'wiggle': 'wiggle 1s var(--ease-in-out) infinite',
                'gradient': 'gradientShift 3s ease infinite',
            },
            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0' },
                    '100%': { opacity: '1' },
                },
                fadeInUp: {
                    '0%': { opacity: '0', transform: 'translateY(10px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                fadeInDown: {
                    '0%': { opacity: '0', transform: 'translateY(-10px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                slideUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                slideDown: {
                    '0%': { opacity: '0', transform: 'translateY(-20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                scaleIn: {
                    '0%': { opacity: '0', transform: 'scale(0.95)' },
                    '100%': { opacity: '1', transform: 'scale(1)' },
                },
                popIn: {
                    '0%': { opacity: '0', transform: 'scale(0.8)' },
                    '50%': { transform: 'scale(1.02)' },
                    '100%': { opacity: '1', transform: 'scale(1)' },
                },
                bounceIn: {
                    '0%': { opacity: '0', transform: 'scale(0.3)' },
                    '50%': { transform: 'scale(1.05)' },
                    '70%': { transform: 'scale(0.9)' },
                    '100%': { opacity: '1', transform: 'scale(1)' },
                },
                pulseSoft: {
                    '0%, 100%': { opacity: '1' },
                    '50%': { opacity: '0.85' },
                },
                breathe: {
                    '0%, 100%': { transform: 'scale(1)' },
                    '50%': { transform: 'scale(1.02)' },
                },
                float: {
                    '0%, 100%': { transform: 'translateY(0)' },
                    '50%': { transform: 'translateY(-5px)' },
                },
                floatSlow: {
                    '0%, 100%': { transform: 'translateY(0)' },
                    '50%': { transform: 'translateY(-10px)' },
                },
                spinSlow: {
                    '0%': { transform: 'rotate(0deg)' },
                    '100%': { transform: 'rotate(360deg)' },
                },
                shimmer: {
                    '0%': { backgroundPosition: '-200% 0' },
                    '100%': { backgroundPosition: '200% 0' },
                },
                skeleton: {
                    '0%': { backgroundPosition: '-200px 0' },
                    '100%': { backgroundPosition: 'calc(200px + 100%) 0' },
                },
                progressFill: {
                    '0%': { width: '0%' },
                },
                glow: {
                    '0%, 100%': { boxShadow: 'var(--shadow-glow-primary)' },
                    '50%': { boxShadow: 'var(--shadow-glow-primary-intense)' },
                },
                shake: {
                    '0%, 100%': { transform: 'translateX(0)' },
                    '10%, 30%, 50%, 70%, 90%': { transform: 'translateX(-2px)' },
                    '20%, 40%, 60%, 80%': { transform: 'translateX(2px)' },
                },
                wiggle: {
                    '0%, 100%': { transform: 'rotate(-3deg)' },
                    '50%': { transform: 'rotate(3deg)' },
                },
                gradientShift: {
                    '0%': { backgroundPosition: '0% 50%' },
                    '50%': { backgroundPosition: '100% 50%' },
                    '100%': { backgroundPosition: '0% 50%' },
                },
            },

            /* ================================================================
               TRANSITIONS
               ================================================================ */
            transitionDuration: {
                'fastest': 'var(--duration-fastest)',
                'faster': 'var(--duration-faster)',
                'fast': 'var(--duration-fast)',
                'normal': 'var(--duration-normal)',
                'slow': 'var(--duration-slow)',
                'slower': 'var(--duration-slower)',
                'slowest': 'var(--duration-slowest)',
                '250': '250ms',
                '350': '350ms',
                '400': '400ms',
            },
            transitionTimingFunction: {
                'ease-default': 'var(--ease-default)',
                'ease-in': 'var(--ease-in)',
                'ease-out': 'var(--ease-out)',
                'ease-in-out': 'var(--ease-in-out)',
                'ease-bounce': 'var(--ease-bounce)',
                'ease-elastic': 'var(--ease-elastic)',
            },

            /* ================================================================
               Z-INDEX SCALE
               ================================================================ */
            zIndex: {
                '60': '60',
                '70': '70',
                '80': '80',
                '90': '90',
                '100': '100',
            },
        },
    },
    plugins: [],
}
