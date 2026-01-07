"use client"

/**
 * Spotify Live Player Widget
 * 
 * Shows what Said is currently listening to.
 * Click to open the track in Spotify (no API needed!)
 * 
 * Features:
 * - Shows current track from Last.fm scrobbles
 * - Click to open in Spotify app/web
 * - No Spotify API registration required
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
    Music, 
    Radio,
    Headphones,
    X,
    Play
} from "lucide-react"

interface SpotifyTrack {
    isPlaying: boolean
    name: string | null
    artist: string | null
    album: string | null
    albumArt: string | null
    spotifyUrl: string | null
}

interface SpotifyLivePlayerProps {
    className?: string
    variant?: 'compact' | 'full'
}

export function SpotifyLivePlayer({
    className,
    variant = 'compact'
}: SpotifyLivePlayerProps) {
    const [track, setTrack] = useState<SpotifyTrack | null>(null)
    const [loading, setLoading] = useState(true)
    const [isExpanded, setIsExpanded] = useState(false)

    // Fetch current track from Last.fm
    const fetchNowPlaying = useCallback(async () => {
        try {
            const res = await fetch(`/api/music/now-playing?t=${Date.now()}`, {
                cache: 'no-store'
            })
            if (res.ok) {
                const data = await res.json()
                if (data.track) {
                    setTrack({
                        isPlaying: data.isPlaying,
                        name: data.track.name,
                        artist: data.track.artist,
                        album: data.track.album,
                        albumArt: data.track.albumArt,
                        spotifyUrl: data.track.spotifyUrl
                    })
                } else {
                    setTrack(null)
                }
            }
        } catch (error) {
            console.error('Failed to fetch music data:', error)
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchNowPlaying()
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, [fetchNowPlaying])

    // Build Spotify search URL (works without API!)
    const getSpotifySearchUrl = () => {
        if (!track?.name || !track?.artist) return null
        const query = encodeURIComponent(`${track.name} ${track.artist}`)
        return `https://open.spotify.com/search/${query}`
    }

    // Open in Spotify
    const openInSpotify = () => {
        const url = track?.spotifyUrl || getSpotifySearchUrl()
        if (url) {
            window.open(url, '_blank', 'noopener,noreferrer')
        }
    }

    // Loading state
    if (loading) {
        return (
            <div className={cn(
                "flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <div className="w-8 h-8 rounded-md bg-zinc-800 animate-pulse" />
                <div className="flex-1 space-y-1">
                    <div className="h-3 w-20 bg-zinc-800 rounded animate-pulse" />
                    <div className="h-2 w-14 bg-zinc-800 rounded animate-pulse" />
                </div>
            </div>
        )
    }

    // Nothing playing
    if (!track?.name) {
        return (
            <div className={cn(
                "flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <Music className="w-4 h-4 text-zinc-500" />
                <span className="text-xs text-zinc-500">No music</span>
            </div>
        )
    }

    return (
        <div className={cn("relative", className)}>
            {/* Main Widget - Click to expand */}
            <motion.div
                className={cn(
                    "flex items-center gap-3 px-3 py-2 rounded-xl cursor-pointer",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200"
                )}
                onClick={() => setIsExpanded(!isExpanded)}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                {/* Album Art */}
                <div className="relative">
                    {track.albumArt ? (
                        <img
                            src={track.albumArt}
                            alt={track.album || 'Album'}
                            className="w-10 h-10 rounded-md object-cover"
                        />
                    ) : (
                        <div className="w-10 h-10 rounded-md bg-zinc-800 flex items-center justify-center">
                            <Music className="w-5 h-5 text-zinc-500" />
                        </div>
                    )}
                    
                    {/* Live indicator */}
                    {track.isPlaying && (
                        <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-500 rounded-full animate-pulse" />
                    )}
                </div>

                {/* Track Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1.5">
                        {track.isPlaying ? (
                            <Radio className="w-3 h-3 text-green-400 animate-pulse" />
                        ) : (
                            <Headphones className="w-3 h-3 text-zinc-400" />
                        )}
                        <span className="text-xs text-green-400 font-medium">
                            {track.isPlaying ? 'LIVE' : 'Recently'}
                        </span>
                    </div>
                    <p className="text-sm font-medium text-white truncate">
                        {track.name}
                    </p>
                    <p className="text-xs text-zinc-400 truncate">
                        {track.artist}
                    </p>
                </div>

                {/* Spotify Icon */}
                <div className="p-2 rounded-full bg-green-500/20 text-green-400">
                    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                    </svg>
                </div>
            </motion.div>

            {/* Expanded Panel */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.95 }}
                        transition={{ duration: 0.2 }}
                        className={cn(
                            "absolute top-full left-0 right-0 mt-2 z-50",
                            "rounded-xl overflow-hidden",
                            "bg-zinc-900 border border-zinc-800",
                            "shadow-2xl shadow-black/50"
                        )}
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between px-3 py-2 bg-zinc-800/50 border-b border-zinc-700/50">
                            <div className="flex items-center gap-2">
                                <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                                <span className="text-xs text-zinc-400">
                                    Said lyssnar på
                                </span>
                            </div>
                            <button
                                onClick={(e) => {
                                    e.stopPropagation()
                                    setIsExpanded(false)
                                }}
                                className="p-1 rounded-full hover:bg-zinc-700/50 text-zinc-400 hover:text-white"
                            >
                                <X className="w-4 h-4" />
                            </button>
                        </div>

                        {/* Track Details */}
                        <div className="p-4">
                            <div className="flex gap-4">
                                {/* Large Album Art */}
                                {track.albumArt ? (
                                    <img
                                        src={track.albumArt}
                                        alt={track.album || 'Album'}
                                        className="w-20 h-20 rounded-lg object-cover shadow-lg"
                                    />
                                ) : (
                                    <div className="w-20 h-20 rounded-lg bg-zinc-800 flex items-center justify-center">
                                        <Music className="w-8 h-8 text-zinc-500" />
                                    </div>
                                )}
                                
                                {/* Track Info */}
                                <div className="flex-1 min-w-0">
                                    <p className="text-lg font-semibold text-white truncate">
                                        {track.name}
                                    </p>
                                    <p className="text-sm text-zinc-400 truncate">
                                        {track.artist}
                                    </p>
                                    {track.album && (
                                        <p className="text-xs text-zinc-500 truncate mt-1">
                                            {track.album}
                                        </p>
                                    )}
                                </div>
                            </div>

                            {/* Open in Spotify Button */}
                            <button
                                onClick={openInSpotify}
                                className={cn(
                                    "w-full mt-4 py-3 px-4 rounded-xl",
                                    "bg-green-500 hover:bg-green-400 text-black font-semibold",
                                    "flex items-center justify-center gap-2",
                                    "transition-colors"
                                )}
                            >
                                <Play className="w-5 h-5" fill="currentColor" />
                                Lyssna på Spotify
                            </button>
                        </div>

                        {/* Footer */}
                        <div className="px-4 py-3 bg-zinc-800/30 border-t border-zinc-700/50">
                            <p className="text-xs text-zinc-500 text-center">
                                Öppnas i Spotify-appen eller webbspelaren
                            </p>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
