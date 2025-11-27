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
            // DevOpsHub Brand Colors
            colors: {
                devops: {
                    primary: 'var(--devops-primary)',
                    'primary-dark': 'var(--devops-primary-dark)',
                    secondary: 'var(--devops-secondary)',
                    success: 'var(--devops-success)',
                    warning: 'var(--devops-warning)',
                    info: 'var(--devops-info)',
                    danger: 'var(--devops-danger)',
                },
            },
            // Typography
            fontFamily: {
                sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
            },
            fontSize: {
                '2xs': ['0.625rem', { lineHeight: '0.875rem' }],
            },
            // Spacing
            spacing: {
                '18': '4.5rem',
                '88': '22rem',
                '112': '28rem',
                '128': '32rem',
            },
            // Border radius
            borderRadius: {
                '4xl': '2rem',
            },
            // Box shadows
            boxShadow: {
                'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
                'glow': '0 0 20px rgba(99, 102, 241, 0.3)',
                'glow-success': '0 0 20px rgba(34, 197, 94, 0.3)',
                'glow-warning': '0 0 20px rgba(249, 115, 22, 0.3)',
                'inner-soft': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.05)',
            },
            // Backdrop blur
            backdropBlur: {
                xs: '2px',
            },
            // Animations
            animation: {
                'fade-in': 'fadeIn 0.3s ease-out forwards',
                'slide-up': 'slideUp 0.4s ease-out forwards',
                'scale-in': 'scaleIn 0.2s ease-out forwards',
                'pulse-soft': 'pulseSoft 2s ease-in-out infinite',
                'shimmer': 'shimmer 1.5s infinite',
                'progress-fill': 'progressFill 1s ease-out forwards',
            },
            keyframes: {
                fadeIn: {
                    '0%': { opacity: '0', transform: 'translateY(10px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                slideUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                },
                scaleIn: {
                    '0%': { opacity: '0', transform: 'scale(0.95)' },
                    '100%': { opacity: '1', transform: 'scale(1)' },
                },
                pulseSoft: {
                    '0%, 100%': { opacity: '1' },
                    '50%': { opacity: '0.7' },
                },
                shimmer: {
                    '0%': { backgroundPosition: '-200% 0' },
                    '100%': { backgroundPosition: '200% 0' },
                },
                progressFill: {
                    '0%': { width: '0%' },
                },
            },
            // Transitions
            transitionDuration: {
                '250': '250ms',
                '350': '350ms',
                '400': '400ms',
            },
            // Z-index scale
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
