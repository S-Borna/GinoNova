"use client"

/**
 * Offline Page - Shown when user is offline
 */

import { WifiOff, RefreshCw } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function OfflinePage() {
    const handleRetry = () => {
        window.location.reload()
    }

    return (
        <div className="min-h-screen bg-[#05050a] flex items-center justify-center px-4">
            <div className="text-center max-w-md">
                {/* Icon */}
                <div className="w-24 h-24 mx-auto mb-8 rounded-3xl bg-gradient-to-br from-purple-500/20 to-pink-500/20 border border-purple-500/30 flex items-center justify-center">
                    <WifiOff className="w-12 h-12 text-purple-400" />
                </div>

                {/* Title */}
                <h1 className="text-3xl font-black text-white mb-4">
                    Du är offline
                </h1>

                {/* Description */}
                <p className="text-zinc-400 mb-8">
                    Det verkar som att du inte har någon internetanslutning. 
                    Kontrollera din anslutning och försök igen.
                </p>

                {/* Retry button */}
                <Button
                    onClick={handleRetry}
                    className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white font-semibold px-8"
                >
                    <RefreshCw className="w-4 h-4 mr-2" />
                    Försök igen
                </Button>

                {/* Tip */}
                <p className="text-xs text-zinc-500 mt-8">
                    💡 Tips: Installera GinoNova-appen för bättre offlinestöd
                </p>
            </div>
        </div>
    )
}
