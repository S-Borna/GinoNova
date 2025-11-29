import type { ReactNode } from 'react';
import type { Metadata, Viewport } from 'next';
// import { Providers } from '@/components/Providers';
// import './globals.css';

/* ============================================================================
   SEO & METADATA
   ============================================================================ */

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://devopshub.io';

export const metadata: Metadata = {
    metadataBase: new URL(siteUrl),
    title: {
        default: 'My DOE Hub — Master DevOps. Build Your Career.',
        template: '%s | My DOE Hub',
    },
    description: 'Master DevOps with 15 structured modules, 60+ hands-on labs, and real-world projects.',
};

export const viewport: Viewport = {
    width: 'device-width',
    initialScale: 1,
};

export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="en" suppressHydrationWarning>
            <body>
                {children}
            </body>
        </html>
    );
}
