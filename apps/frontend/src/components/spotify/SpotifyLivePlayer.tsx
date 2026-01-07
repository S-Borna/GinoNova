"use client"

/**
 * Spotify Live Player Widget
 *
 * Shows what Said is listening to with REAL Spotify embed.
 * NO API KEYS NEEDED - uses Deezer + Songlink to find Spotify track.
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Music,
    Volume2,
    VolumeX,
    Radio,
    Headphones,
    X,
    Loader2
} from "lucide-react"

interface Track {
    isPlaying: boolean
    name: string | null
    artist: string | null
    album: string | null
    albumArt: string | null
}

interface SpotifyLivePlayerProps {
    className?: string
}

export function SpotifyLivePlayer({ className }: SpotifyLivePlayerProps) {
    const [track, setTrack] = useState<Track | null>(null)
    const [loading, setLoading] = useState(true)
    const [isExpanded, setIsExpanded] = useState(false)
    const [isMuted, setIsMuted] = useState(true)
    const [embedUrl, setEmbedUrl] = useState<string | null>(null)
    const [embedLoading, setEmbedLoading] = useState(false)
    const [lastTrackKey, setLastTrackKey] = useState<string>("")

    // Fetch current track from Last.fm
    const fetchNowPlaying = useCallback(async () => {
        try {
            const res = await fetch(`/api/music/now-playing?t=${Date.now()}`, {
                cache: 'no-store'
            })
            if (res.ok) {
                const data = await res.json()
                if (data.track) {
                    const newKey = `${data.track.name}-${data.track.artist}`

                    // Only update if track actually changed (prevent re-renders)
                    if (newKey !== lastTrackKey) {
                        setTrack({
                            isPlaying: data.isPlaying,
                            name: data.track.name,
                            artist: data.track.artist,
                            album: data.track.album,
                            albumArt: data.track.albumArt,
                        })
                        setLastTrackKey(newKey)
                        setEmbedUrl(null) // Reset embed for new track
                    }
                    // Don't update state if track is the same - prevents iframe reload
                } else {
                    if (track !== null) {
                        setTrack(null)
                        setEmbedUrl(null)
                    }
                }
            }
        } catch (error) {
            console.error('Failed to fetch music:', error)
        } finally {
            setLoading(false)
        }
    }, [lastTrackKey, track])

    // Fetch Spotify embed URL
    const fetchSpotifyEmbed = useCallback(async () => {
        if (!track?.name || !track?.artist || embedUrl) return

        setEmbedLoading(true)
        try {
            const res = await fetch(
                `/api/music/spotify-finder?track=${encodeURIComponent(track.name)}&artist=${encodeURIComponent(track.artist)}`
            )
            if (res.ok) {
                const data = await res.json()
                if (data.embedUrl) {
                    setEmbedUrl(data.embedUrl)
                }
            }
        } catch (e) {
            console.error('Failed to get Spotify embed:', e)
        } finally {
            setEmbedLoading(false)
        }
    }, [track, embedUrl])

    useEffect(() => {
        fetchNowPlaying()
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Fetch embed when unmuted
    useEffect(() => {
        if (!isMuted && track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [isMuted, track, embedUrl, embedLoading, fetchSpotifyEmbed])

    const toggleMute = () => {
        const newMuted = !isMuted
        setIsMuted(newMuted)
        if (!newMuted && !isExpanded) {
            setIsExpanded(true)
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
            {/* Main Widget */}
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
                    <p className="text-sm font-medium text-white truncate">{track.name}</p>
                    <p className="text-xs text-zinc-400 truncate">{track.artist}</p>
                </div>

                {/* Mute/Unmute */}
                <button
                    onClick={(e) => { e.stopPropagation(); toggleMute(); }}
                    className={cn(
                        "p-2 rounded-full transition-colors",
                        isMuted
                            ? "bg-zinc-800 hover:bg-zinc-700 text-zinc-400"
                            : "bg-green-500 hover:bg-green-400 text-black"
                    )}
                    title={isMuted ? "Lyssna med Said" : "Tysta"}
                >
                    {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
                </button>
            </motion.div>

            {/* Expanded Spotify Player - Flyout to the left */}
            <AnimatePresence>
                {isExpanded && (
                    <motion.div
                        initial={{ opacity: 0, x: 10, scale: 0.95 }}
                        animate={{ opacity: 1, x: 0, scale: 1 }}
                        exit={{ opacity: 0, x: 10, scale: 0.95 }}
                        transition={{ duration: 0.2 }}
                        className={cn(
                            "absolute top-0 right-full mr-2 z-50",
                            "rounded-xl overflow-hidden",
                            "bg-zinc-900 border border-zinc-800",
                            "shadow-2xl shadow-black/50",
                            "w-[320px]"
                        )}
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between px-3 py-2 bg-zinc-800/50 border-b border-zinc-700/50">
                            <div className="flex items-center gap-2">
                                {!isMuted && <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />}
                                <span className="text-xs text-zinc-400">
                                    {isMuted ? 'Tryck för att lyssna' : 'Lyssna med Said'}
                                </span>
                            </div>
                            <button
                                onClick={(e) => { e.stopPropagation(); setIsExpanded(false); }}
                                className="p-1 rounded-full hover:bg-zinc-700/50 text-zinc-400 hover:text-white"
                            >
                                <X className="w-4 h-4" />
                            </button>
                        </div>

                        {/* Spotify Embed */}
                        <div className="relative" style={{ height: isMuted ? 100 : 152 }}>
                            {!isMuted && embedUrl ? (
                                <iframe
                                    key={embedUrl}
                                    src={embedUrl}
                                    width="100%"
                                    height="152"
                                    frameBorder="0"
                                    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                                    loading="lazy"
                                    style={{ borderRadius: '0 0 12px 12px' }}
                                />
                            ) : !isMuted && embedLoading ? (
                                <div className="flex flex-col items-center justify-center h-full p-4">
                                    <Loader2 className="w-6 h-6 text-green-400 animate-spin mb-2" />
                                    <p className="text-sm text-zinc-400">Laddar Spotify...</p>
                                </div>
                            ) : (
                                <div className="flex flex-col items-center justify-center h-full p-4 text-center">
                                    <VolumeX className="w-6 h-6 text-zinc-500 mb-2" />
                                    <p className="text-sm text-zinc-400">Spelaren är tystad</p>
                                    <button
                                        onClick={toggleMute}
                                        className="mt-2 px-4 py-1.5 text-xs font-medium text-black bg-green-500 rounded-full hover:bg-green-400"
                                    >
                                        ▶ Spela på Spotify
                                    </button>
                                </div>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
