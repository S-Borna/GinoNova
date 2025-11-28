import type { ReactNode } from 'react';
import { Inter, JetBrains_Mono } from 'next/font/google';
import './globals.css';
import { AuthProvider } from '@/components/auth';
import { QueryProvider } from '@/providers/QueryProvider';
import { Toaster } from '@/components/ui/sonner';

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

export const metadata = {
    title: 'DevOpsHub',
    description: 'DevOps Learning Platform',
};

export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
            <body className="font-sans antialiased">
                <QueryProvider>
                    <AuthProvider>{children}</AuthProvider>
                </QueryProvider>
                <Toaster position="top-right" richColors closeButton />
            </body>
        </html>
    );
}
