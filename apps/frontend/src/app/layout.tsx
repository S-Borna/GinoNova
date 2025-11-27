import type { ReactNode } from 'react';
import './globals.css';
import { AuthProvider } from '@/components/auth';

export const metadata = {
    title: 'DevOpsHub',
    description: 'DevOps Learning Platform',
};

export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="en">
            <body>
                <AuthProvider>{children}</AuthProvider>
            </body>
        </html>
    );
}
