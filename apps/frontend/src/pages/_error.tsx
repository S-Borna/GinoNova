/**
 * Custom error page for Pages Router compatibility.
 * This overrides Next.js default _error.js to prevent SSR context issues
 * when using App Router with client-side providers like next-themes.
 */

import type { NextPage, NextPageContext } from 'next'

interface ErrorProps {
    statusCode: number | undefined
}

const Error: NextPage<ErrorProps> = ({ statusCode }) => {
    return (
        <div
            style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                minHeight: '100vh',
                fontFamily: 'system-ui, -apple-system, sans-serif',
                backgroundColor: '#0a0a0a',
                color: '#fafafa',
            }}
        >
            <h1 style={{ fontSize: '3rem', marginBottom: '1rem' }}>
                {statusCode || 'Error'}
            </h1>
            <p style={{ fontSize: '1.125rem', color: '#a1a1aa' }}>
                {statusCode
                    ? `A ${statusCode} error occurred on the server`
                    : 'An error occurred on the client'}
            </p>
            {/* eslint-disable-next-line @next/next/no-html-link-for-pages */}
            <a
                href="/"
                style={{
                    marginTop: '2rem',
                    padding: '0.75rem 1.5rem',
                    backgroundColor: '#3b82f6',
                    color: 'white',
                    borderRadius: '0.5rem',
                    textDecoration: 'none',
                }}
            >
                Go Home
            </a>
        </div>
    )
}

Error.getInitialProps = ({ res, err }: NextPageContext) => {
    const statusCode = res ? res.statusCode : err ? err.statusCode : 404
    return { statusCode }
}

export default Error
