"use client"

/**
 * Last.fm Now Playing Widget
 * Shows what you're currently listening to via Last.fm scrobbles
 * Works with Spotify, Apple Music, or any scrobbler!
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Music, ExternalLink, Volume2, Clock, X } from "lucide-react"

interface LastFmTrack {
    isPlaying: boolean
    title: string
    artist: string
    album: string
    albumImageUrl: string
    songUrl: string
    source: 'lastfm'
    scrobbledAt?: number | null
}

interface LastFmNowPlayingProps {
    className?: string
    variant?: 'compact' | 'full' | 'mini'
}

const STORAGE_KEY = 'lastfm-widget-hidden'

export function LastFmNowPlaying({
    className,
    variant = 'compact'
}: LastFmNowPlayingProps) {
    const [track, setTrack] = useState<LastFmTrack | null>(null)
    const [loading, setLoading] = useState(true)
    const [isHidden, setIsHidden] = useState(false)

    // Check localStorage on mount
    useEffect(() => {
        const hidden = localStorage.getItem(STORAGE_KEY)
        if (hidden === 'true') {
            setIsHidden(true)
        }
    }, [])

    const handleDismiss = (e: React.MouseEvent) => {
        e.preventDefault()
        e.stopPropagation()
        setIsHidden(true)
        localStorage.setItem(STORAGE_KEY, 'true')
    }

    useEffect(() => {
        if (isHidden) return // Don't fetch if hidden
        
        const fetchNowPlaying = async () => {
            try {
                // Add cache buster to prevent browser caching
                const response = await fetch(`/api/lastfm/now-playing?t=${Date.now()}`)
                if (response.ok) {
                    const data = await response.json()
                    if (data.title) {
                        setTrack(data)
                    } else {
                        setTrack(null)
                    }
                } else {
                    setTrack(null)
                }
            } catch (err) {
                setTrack(null)
            } finally {
                setLoading(false)
            }
        }

        fetchNowPlaying()

        // Poll every 15 seconds for more responsive updates
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, [isHidden])

    // Format relative time
    const formatTimeAgo = (timestamp: number) => {
        const seconds = Math.floor((Date.now() - timestamp) / 1000)
        if (seconds < 60) return 'just nu'
        if (seconds < 3600) return `${Math.floor(seconds / 60)} min sedan`
        if (seconds < 86400) return `${Math.floor(seconds / 3600)} tim sedan`
        return `${Math.floor(seconds / 86400)} dagar sedan`
    }

    // Don't render if user dismissed
    if (isHidden) {
        return null
    }

    if (loading) {
        return (
            <div className={cn(
                "flex items-center gap-3 p-3 rounded-xl bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <div className="w-12 h-12 rounded-lg bg-zinc-800 animate-pulse" />
                <div className="flex-1 space-y-2">
                    <div className="h-4 w-24 bg-zinc-800 rounded animate-pulse" />
                    <div className="h-3 w-16 bg-zinc-800 rounded animate-pulse" />
                </div>
            </div>
        )
    }

    if (!track) {
        if (variant === 'mini') {
            return (
                <div className={cn(
                    "flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/50 border border-zinc-800",
                    className
                )}>
                    <Music className="w-4 h-4 text-zinc-500" />
                    <span className="text-xs text-zinc-500">Offline</span>
                </div>
            )
        }

        return (
            <div className={cn(
                "flex items-center gap-3 p-4 rounded-xl bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <div className="w-12 h-12 rounded-lg bg-zinc-800/50 flex items-center justify-center">
                    <Music className="w-5 h-5 text-zinc-600" />
                </div>
                <div>
                    <p className="text-sm text-zinc-500">Inget nyligen spelat</p>
                    <p className="text-xs text-zinc-600">Kom tillbaka senare</p>
                </div>
            </div>
        )
    }

    // Mini variant
    if (variant === 'mini') {
        return (
            <motion.a
                href={track.songUrl}
                target="_blank"
                rel="noopener noreferrer"
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "group flex items-center gap-2 px-3 py-1.5 rounded-full",
                    track.isPlaying
                        ? "bg-gradient-to-r from-red-500/10 to-pink-500/10 border border-red-500/20 hover:border-red-500/40"
                        : "bg-zinc-900/50 border border-zinc-800 hover:border-zinc-700",
                    "transition-all cursor-pointer",
                    className
                )}
            >
                <div className="relative">
                    {track.albumImageUrl ? (
                        <img
                            src={track.albumImageUrl}
                            alt={track.album}
                            className="w-5 h-5 rounded-sm"
                        />
                    ) : (
                        <Music className="w-5 h-5 text-zinc-400" />
                    )}
                    {track.isPlaying && (
                        <div className="absolute -bottom-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full animate-pulse" />
                    )}
                </div>
                <span className={cn(
                    "text-xs max-w-[120px] truncate",
                    track.isPlaying ? "text-red-400" : "text-zinc-400"
                )}>
                    {track.title}
                </span>
                {track.isPlaying && <Volume2 className="w-3 h-3 text-red-500/50" />}
            </motion.a>
        )
    }

    // Compact variant
    if (variant === 'compact') {
        return (
            <div className="relative group/dismiss">
                <motion.a
                    href={track.songUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "flex items-center gap-3 p-3 rounded-xl",
                        "bg-gradient-to-r from-zinc-900/80 to-zinc-900/50",
                        track.isPlaying
                            ? "border border-red-500/30 hover:border-red-500/50"
                            : "border border-zinc-800 hover:border-zinc-700",
                        "transition-all cursor-pointer",
                        className
                    )}
                >
                {/* Album art */}
                <div className="relative shrink-0">
                    {track.albumImageUrl ? (
                        <img
                            src={track.albumImageUrl}
                            alt={track.album}
                            className="w-12 h-12 rounded-lg shadow-lg"
                        />
                    ) : (
                        <div className="w-12 h-12 rounded-lg bg-zinc-800 flex items-center justify-center">
                            <Music className="w-5 h-5 text-zinc-500" />
                        </div>
                    )}
                    {track.isPlaying && (
                        <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center">
                            <Volume2 className="w-2.5 h-2.5 text-white" />
                        </div>
                    )}
                </div>

                {/* Track info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                        <span className={cn(
                            "text-xs font-medium",
                            track.isPlaying ? "text-red-400" : "text-zinc-500"
                        )}>
                            {track.isPlaying ? 'LYSSNAR PÅ' : 'SENAST SPELAD'}
                        </span>
                        {track.isPlaying && (
                            <div className="flex gap-0.5">
                                {[...Array(3)].map((_, i) => (
                                    <motion.div
                                        key={i}
                                        className="w-0.5 bg-red-500 rounded-full"
                                        animate={{ height: [4, 12, 4] }}
                                        transition={{
                                            duration: 0.5,
                                            repeat: Infinity,
                                            delay: i * 0.1
                                        }}
                                    />
                                ))}
                            </div>
                        )}
                    </div>
                    <p className="text-sm font-medium text-white truncate">{track.title}</p>
                    <p className="text-xs text-zinc-400 truncate">{track.artist}</p>
                    {!track.isPlaying && track.scrobbledAt && (
                        <p className="text-[10px] text-zinc-500 flex items-center gap-1 mt-0.5">
                            <Clock className="w-3 h-3" />
                            {formatTimeAgo(track.scrobbledAt)}
                        </p>
                    )}
                </div>

                {/* Last.fm logo */}
                <div className="shrink-0 opacity-50 group-hover:opacity-100 transition-opacity">
                    <svg className="w-5 h-5 text-red-500" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M10.584 17.21l-.88-2.392s-1.43 1.594-3.573 1.594c-1.897 0-3.244-1.649-3.244-4.288 0-3.382 1.704-4.591 3.381-4.591 2.42 0 3.189 1.567 3.849 3.574l.88 2.749c.88 2.666 2.529 4.81 7.285 4.81 3.409 0 5.718-1.044 5.718-3.793 0-2.227-1.265-3.381-3.63-3.931l-1.758-.385c-1.21-.275-1.567-.77-1.567-1.594 0-.935.742-1.484 1.952-1.484 1.32 0 2.034.495 2.144 1.677l2.749-.33c-.22-2.474-1.924-3.492-4.729-3.492-2.474 0-4.893.935-4.893 3.932 0 1.87.907 3.051 3.189 3.601l1.87.44c1.402.33 1.869.825 1.869 1.704 0 1.017-.99 1.43-2.86 1.43-2.776 0-3.931-1.457-4.591-3.464l-.907-2.749c-1.155-3.573-2.997-4.893-6.653-4.893C2.144 5.333 0 7.89 0 12.233c0 4.18 2.144 6.434 5.993 6.434 3.106 0 4.591-1.457 4.591-1.457z" />
                    </svg>
                </div>
            </motion.a>
            
            {/* Dismiss button */}
            <button
                onClick={handleDismiss}
                className="absolute -top-1.5 -right-1.5 w-5 h-5 rounded-full bg-zinc-800 border border-zinc-700 flex items-center justify-center opacity-0 group-hover/dismiss:opacity-100 transition-opacity hover:bg-zinc-700 hover:border-zinc-600"
                title="Dölj widgeten"
            >
                <X className="w-3 h-3 text-zinc-400" />
            </button>
        </div>
        )
    }

    // Full variant
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-zinc-900 via-zinc-900 to-red-950/20",
                "border border-zinc-800",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-zinc-800/50">
                <div className="flex items-center gap-2">
                    <svg className="w-5 h-5 text-red-500" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M10.584 17.21l-.88-2.392s-1.43 1.594-3.573 1.594c-1.897 0-3.244-1.649-3.244-4.288 0-3.382 1.704-4.591 3.381-4.591 2.42 0 3.189 1.567 3.849 3.574l.88 2.749c.88 2.666 2.529 4.81 7.285 4.81 3.409 0 5.718-1.044 5.718-3.793 0-2.227-1.265-3.381-3.63-3.931l-1.758-.385c-1.21-.275-1.567-.77-1.567-1.594 0-.935.742-1.484 1.952-1.484 1.32 0 2.034.495 2.144 1.677l2.749-.33c-.22-2.474-1.924-3.492-4.729-3.492-2.474 0-4.893.935-4.893 3.932 0 1.87.907 3.051 3.189 3.601l1.87.44c1.402.33 1.869.825 1.869 1.704 0 1.017-.99 1.43-2.86 1.43-2.776 0-3.931-1.457-4.591-3.464l-.907-2.749c-1.155-3.573-2.997-4.893-6.653-4.893C2.144 5.333 0 7.89 0 12.233c0 4.18 2.144 6.434 5.993 6.434 3.106 0 4.591-1.457 4.591-1.457z" />
                    </svg>
                    <span className="text-sm font-medium text-white">
                        {track.isPlaying ? 'Lyssnar just nu' : 'Senast spelad'}
                    </span>
                </div>
                <a
                    href={track.songUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-zinc-400 hover:text-red-400 transition-colors"
                >
                    <ExternalLink className="w-4 h-4" />
                </a>
            </div>

            {/* Content */}
            <div className="p-4">
                <div className="flex gap-4">
                    {/* Album art */}
                    <div className="relative shrink-0">
                        {track.albumImageUrl ? (
                            <img
                                src={track.albumImageUrl}
                                alt={track.album}
                                className="w-20 h-20 rounded-xl shadow-xl"
                            />
                        ) : (
                            <div className="w-20 h-20 rounded-xl bg-zinc-800 flex items-center justify-center">
                                <Music className="w-8 h-8 text-zinc-600" />
                            </div>
                        )}
                        {track.isPlaying && (
                            <motion.div
                                className="absolute inset-0 rounded-xl border-2 border-red-500/30"
                                animate={{ scale: [1, 1.05, 1] }}
                                transition={{ duration: 2, repeat: Infinity }}
                            />
                        )}
                    </div>

                    {/* Track info */}
                    <div className="flex-1 min-w-0 flex flex-col justify-center">
                        <p className="text-lg font-bold text-white truncate">{track.title}</p>
                        <p className="text-sm text-zinc-400 truncate">{track.artist}</p>
                        {track.album && <p className="text-xs text-zinc-500 truncate">{track.album}</p>}
                        {!track.isPlaying && track.scrobbledAt && (
                            <p className="text-xs text-zinc-500 flex items-center gap-1 mt-1">
                                <Clock className="w-3 h-3" />
                                {formatTimeAgo(track.scrobbledAt)}
                            </p>
                        )}
                    </div>
                </div>
            </div>

            {/* Visualizer bars (only when playing) */}
            {track.isPlaying && (
                <div className="flex items-end justify-center gap-1 h-8 px-4 pb-3">
                    {[...Array(12)].map((_, i) => (
                        <motion.div
                            key={i}
                            className="w-1 bg-red-500/40 rounded-full"
                            animate={{
                                height: [4, Math.random() * 20 + 8, 4]
                            }}
                            transition={{
                                duration: 0.5 + Math.random() * 0.3,
                                repeat: Infinity,
                                delay: i * 0.05
                            }}
                        />
                    ))}
                </div>
            )}
        </motion.div>
    )
}

export default LastFmNowPlaying
