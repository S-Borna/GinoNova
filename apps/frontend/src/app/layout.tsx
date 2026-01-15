import type { ReactNode } from 'react';
import type { Metadata, Viewport } from 'next';
import { Inter, JetBrains_Mono } from 'next/font/google';
import './globals.css';
import { Providers } from '@/components/Providers';

// Primary font: Inter — Clean, modern, highly legible
const inter = Inter({
    subsets: ['latin'],
    variable: '--font-inter',
    display: 'swap',
});

// Monospace font: JetBrains Mono — Code blocks, technical content
const jetbrainsMono = JetBrains_Mono({
    subsets: ['latin'],
    variable: '--font-mono',
    display: 'swap',
});

/* ============================================================================
   SEO & METADATA
   ============================================================================ */

const siteConfig = {
    name: "GinoNova - AI Powered Learning",
    company: 'The Ebadi Group',
    description:
        'Master DevOps with 15 structured modules, 60+ hands-on labs, and real-world projects. From Linux fundamentals to Kubernetes, become a DevOps engineer.',
    url: process.env.NEXT_PUBLIC_SITE_URL || 'https://devopshub.io',
    ogImage: '/og-image.png',
    twitterHandle: '@devopshub',
    author: 'The Ebadi Group',
    keywords: [
        'DevOps',
        'DevOps bootcamp',
        'DevOps course',
        'DevOps learning',
        'Kubernetes',
        'Docker',
        'AWS',
        'Terraform',
        'CI/CD',
        'GitOps',
        'Cloud engineering',
        'Infrastructure as Code',
        'SRE',
        'Site Reliability Engineering',
        'Platform engineering',
        'Linux',
        'Python for DevOps',
    ],
};

export const metadata: Metadata = {
    metadataBase: new URL(siteConfig.url),
    title: {
        default: `${siteConfig.name} — Master DevOps. Build Your Career.`,
        template: `%s | ${siteConfig.name}`,
    },
    description: siteConfig.description,
    keywords: siteConfig.keywords,
    authors: [{ name: siteConfig.author }],
    creator: siteConfig.author,
    publisher: siteConfig.name,
    robots: {
        index: true,
        follow: true,
        googleBot: {
            index: true,
            follow: true,
            'max-video-preview': -1,
            'max-image-preview': 'large',
            'max-snippet': -1,
        },
    },
    openGraph: {
        type: 'website',
        locale: 'en_US',
        url: siteConfig.url,
        siteName: siteConfig.name,
        title: `${siteConfig.name} — Master DevOps. Build Your Career.`,
        description: siteConfig.description,
        images: [
            {
                url: siteConfig.ogImage,
                width: 1200,
                height: 630,
                alt: 'DevOpsHub — Master DevOps. Build Your Career.',
            },
        ],
    },
    twitter: {
        card: 'summary_large_image',
        title: `${siteConfig.name} — Master DevOps. Build Your Career.`,
        description: siteConfig.description,
        images: [siteConfig.ogImage],
        creator: siteConfig.twitterHandle,
    },
    icons: {
        icon: '/icon',
        shortcut: '/icon',
        apple: '/apple-icon',
    },
    manifest: '/site.webmanifest',
    alternates: {
        canonical: siteConfig.url,
    },
    category: 'education',
};

export const viewport: Viewport = {
    themeColor: [
        { media: '(prefers-color-scheme: light)', color: '#ffffff' },
        { media: '(prefers-color-scheme: dark)', color: '#0a0a0a' },
    ],
    width: 'device-width',
    initialScale: 1,
    maximumScale: 5,
};

export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`} suppressHydrationWarning>
            <body className="font-sans antialiased">
                <Providers>{children}</Providers>
            </body>
        </html>
    );
}
