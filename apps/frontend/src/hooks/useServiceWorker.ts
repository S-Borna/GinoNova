"use client"

/**
 * Service Worker Registration Hook
 * Registers the service worker and handles updates
 */

import { useEffect, useState } from "react"

export function useServiceWorker() {
    const [isReady, setIsReady] = useState(false)
    const [needsUpdate, setNeedsUpdate] = useState(false)
    const [registration, setRegistration] = useState<ServiceWorkerRegistration | null>(null)

    useEffect(() => {
        if (typeof window === 'undefined' || !('serviceWorker' in navigator)) {
            return
        }

        // Don't register in development
        if (process.env.NODE_ENV === 'development') {
            console.log('[SW] Skipping registration in development')
            return
        }

        const registerSW = async () => {
            try {
                const reg = await navigator.serviceWorker.register('/sw.js', {
                    scope: '/',
                })
                
                setRegistration(reg)
                console.log('[SW] Registered successfully')

                // Check for updates
                reg.addEventListener('updatefound', () => {
                    const newWorker = reg.installing
                    if (newWorker) {
                        newWorker.addEventListener('statechange', () => {
                            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                                // New version available
                                setNeedsUpdate(true)
                                console.log('[SW] New version available')
                            }
                        })
                    }
                })

                // Check if ready
                if (reg.active) {
                    setIsReady(true)
                }

            } catch (error) {
                console.error('[SW] Registration failed:', error)
            }
        }

        registerSW()

        // Check for updates periodically (every hour)
        const interval = setInterval(() => {
            registration?.update()
        }, 60 * 60 * 1000)

        return () => clearInterval(interval)
    }, [registration])

    const update = () => {
        if (registration?.waiting) {
            registration.waiting.postMessage('skipWaiting')
            window.location.reload()
        }
    }

    return { isReady, needsUpdate, update }
}

export default useServiceWorker
