"use client"

/**
 * SafeLink - Security-hardened Link component
 * 
 * Disables prefetching to prevent route exposure in DevTools Network tab.
 * Use this instead of next/link throughout the app.
 */

import Link, { LinkProps } from "next/link"
import { forwardRef, ReactNode } from "react"

interface SafeLinkProps extends Omit<LinkProps, 'prefetch'> {
    children: ReactNode
    className?: string
}

const SafeLink = forwardRef<HTMLAnchorElement, SafeLinkProps>(
    ({ children, ...props }, ref) => {
        return (
            <Link ref={ref} prefetch={false} {...props}>
                {children}
            </Link>
        )
    }
)

SafeLink.displayName = "SafeLink"

export { SafeLink }
