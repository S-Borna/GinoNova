"use client"

/**
 * ============================================================================
 * PWA INSTALL PROMPT — "Add to Home Screen" Component
 * ============================================================================
 *
 * Shows a banner prompting users to install the app on their device.
 * Appears after 30 seconds of browsing if:
 * - The app is not already installed
 * - The browser supports PWA installation
 * - User hasn't dismissed it recently
 *
 * @phase PWA-IMPLEMENTATION
 */

import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { X, Download, Smartphone, Share } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

interface BeforeInstallPromptEvent extends Event {
    prompt: () => Promise<void>
    userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>
}

declare global {
    interface WindowEventMap {
        beforeinstallprompt: BeforeInstallPromptEvent
    }
}

export function PWAInstallPrompt() {
    const [deferredPrompt, setDeferredPrompt] = useState<BeforeInstallPromptEvent | null>(null)
    const [showPrompt, setShowPrompt] = useState(false)
    const [isIOS, setIsIOS] = useState(false)
    const [isStandalone, setIsStandalone] = useState(false)
    const [isMobile, setIsMobile] = useState(false)

    useEffect(() => {
        // Check if mobile device (width < 768px)
        const mobile = window.innerWidth < 768
        setIsMobile(mobile)
        
        // Don't show on desktop at all
        if (!mobile) return

        // Check if already installed (standalone mode)
        const standalone = window.matchMedia('(display-mode: standalone)').matches ||
                          (window.navigator as any).standalone === true
        setIsStandalone(standalone)

        // Check for iOS
        const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !(window as any).MSStream
        setIsIOS(iOS)

        // Listen for install prompt (Chrome, Edge, etc.)
        const handleBeforeInstall = (e: BeforeInstallPromptEvent) => {
            e.preventDefault()
            setDeferredPrompt(e)
            
            // Check if user dismissed recently
            const dismissed = localStorage.getItem('pwa-install-dismissed')
            if (dismissed) {
                const dismissedTime = parseInt(dismissed, 10)
                const hoursSinceDismissed = (Date.now() - dismissedTime) / (1000 * 60 * 60)
                // Don't show if dismissed in last 24 hours
                if (hoursSinceDismissed < 24) return
            }

            // Show prompt after delay
            setTimeout(() => setShowPrompt(true), 30000) // 30 seconds
        }

        window.addEventListener('beforeinstallprompt', handleBeforeInstall)
        
        // Also show iOS prompt after delay
        if (iOS && !standalone) {
            const dismissed = localStorage.getItem('pwa-install-dismissed')
            if (!dismissed || Date.now() - parseInt(dismissed, 10) > 24 * 60 * 60 * 1000) {
                setTimeout(() => setShowPrompt(true), 30000)
            }
        }

        return () => {
            window.removeEventListener('beforeinstallprompt', handleBeforeInstall)
        }
    }, [])

    const handleInstall = useCallback(async () => {
        if (!deferredPrompt) {
            // No prompt available (localhost, unsupported browser, etc.)
            // Show instructions based on browser
            const isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor)
            const isEdge = /Edg/.test(navigator.userAgent)
            
            if (isChrome || isEdge) {
                alert('Klicka på meny-ikonen (⋮) i webbläsaren och välj "Installera app" eller "Lägg till på hemskärmen"')
            } else {
                alert('PWA-installation kräver HTTPS. Testa på produktion!')
            }
            
            // Still dismiss the prompt
            setShowPrompt(false)
            localStorage.setItem('pwa-install-dismissed', Date.now().toString())
            return
        }

        deferredPrompt.prompt()
        const { outcome } = await deferredPrompt.userChoice

        if (outcome === 'accepted') {
            console.log('[PWA] User accepted install')
        }

        setDeferredPrompt(null)
        setShowPrompt(false)
        localStorage.setItem('pwa-install-dismissed', Date.now().toString())
    }, [deferredPrompt])

    const handleDismiss = useCallback(() => {
        setShowPrompt(false)
        localStorage.setItem('pwa-install-dismissed', Date.now().toString())
    }, [])

    // Don't show if already installed or on desktop
    if (isStandalone || !isMobile) return null

    return (
        <AnimatePresence>
            {showPrompt && (
                <motion.div
                    initial={{ y: 100, opacity: 0 }}
                    animate={{ y: 0, opacity: 1 }}
                    exit={{ y: 100, opacity: 0 }}
                    transition={{ type: "spring", damping: 25, stiffness: 300 }}
                    className={cn(
                        "fixed bottom-20 left-4 right-4 z-50 md:left-auto md:right-6 md:bottom-6 md:w-96",
                        "bg-gradient-to-br from-purple-900/95 to-indigo-900/95",
                        "backdrop-blur-xl rounded-2xl",
                        "border border-purple-500/30",
                        "shadow-2xl shadow-purple-500/20",
                        "p-4"
                    )}
                >
                    {/* Close button */}
                    <button
                        onClick={handleDismiss}
                        className="absolute top-3 right-3 p-1.5 rounded-full hover:bg-white/10 transition-colors"
                        aria-label="Stäng"
                    >
                        <X className="w-4 h-4 text-zinc-400" />
                    </button>

                    <div className="flex items-start gap-4">
                        {/* Icon */}
                        <div className={cn(
                            "w-14 h-14 rounded-xl flex-shrink-0",
                            "bg-gradient-to-br from-purple-500 to-pink-500",
                            "flex items-center justify-center",
                            "shadow-lg shadow-purple-500/30"
                        )}>
                            <Smartphone className="w-7 h-7 text-white" />
                        </div>

                        {/* Content */}
                        <div className="flex-1 min-w-0">
                            <h3 className="text-lg font-bold text-white mb-1">
                                Installera GinoNova
                            </h3>
                            <p className="text-sm text-zinc-300 mb-3">
                                {isIOS 
                                    ? "Tryck på dela-knappen och välj 'Lägg till på hemskärmen'"
                                    : "Få snabbare åtkomst och offlinestöd genom att installera appen"
                                }
                            </p>

                            {/* Actions */}
                            {isIOS ? (
                                <div className="flex items-center gap-2 text-xs text-zinc-400">
                                    <Share className="w-4 h-4" />
                                    <span>Safari → Dela → Lägg till på hemskärmen</span>
                                </div>
                            ) : (
                                <div className="flex gap-2">
                                    <Button
                                        onClick={handleInstall}
                                        size="sm"
                                        className={cn(
                                            "bg-gradient-to-r from-purple-500 to-pink-500",
                                            "hover:from-purple-600 hover:to-pink-600",
                                            "text-white font-semibold",
                                            "shadow-lg shadow-purple-500/30"
                                        )}
                                    >
                                        <Download className="w-4 h-4 mr-2" />
                                        Installera
                                    </Button>
                                    <Button
                                        onClick={handleDismiss}
                                        variant="ghost"
                                        size="sm"
                                        className="text-zinc-400 hover:text-white"
                                    >
                                        Inte nu
                                    </Button>
                                </div>
                            )}
                        </div>
                    </div>
                </motion.div>
            )}
        </AnimatePresence>
    )
}

export default PWAInstallPrompt
