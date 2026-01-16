import { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
    return {
        name: 'GinoNova - DevOps Learning Platform',
        short_name: 'GinoNova',
        description: 'Master DevOps skills with interactive learning paths, AI quizzes, and hands-on labs',
        start_url: '/',
        display: 'standalone',
        background_color: '#05050a',
        theme_color: '#8b5cf6',
        orientation: 'portrait-primary',
        categories: ['education', 'productivity'],
        lang: 'sv',
        dir: 'ltr',
        icons: [
            {
                src: '/icon.svg',
                sizes: 'any',
                type: 'image/svg+xml',
                purpose: 'any',
            },
            {
                src: '/favicon.svg',
                sizes: 'any',
                type: 'image/svg+xml',
                purpose: 'maskable',
            },
        ],
        shortcuts: [
            {
                name: 'Dashboard',
                short_name: 'Dashboard',
                url: '/dashboard',
            },
            {
                name: 'AI Quiz',
                short_name: 'Quiz',
                url: '/quiz',
            },
            {
                name: 'Camp DevOps',
                short_name: 'Camp',
                url: '/modules',
            },
        ],
    }
}
