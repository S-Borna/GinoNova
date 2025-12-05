import { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'DevOpsHub',
    short_name: 'DevOpsHub',
    description: 'Master DevOps skills with interactive learning paths',
    start_url: '/',
    display: 'standalone',
    background_color: '#0a0a0a',
    theme_color: '#8b5cf6',
    icons: [
      {
        src: '/icon.svg',
        sizes: 'any',
        type: 'image/svg+xml',
      },
    ],
  }
}
