"use client"

/**
 * Spotify Live Player - Widget + Flyout
 *
 * Features:
 * - Shows currently playing track from Last.fm
 * - Click widget → Flyout with Spotify embed player
 * - Music plays directly in browser (no external links)
 * - Auto-fetches Spotify embed URL
 * - Continues polling even when music is playing
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Music,
    Volume2,
    Radio,
    Headphones,
    Loader2,
    Play,
    X
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
    const [musicPlaying, setMusicPlaying] = useState(false) // Flyout open state
    const [embedUrl, setEmbedUrl] = useState<string | null>(null)
    const [embedLoading, setEmbedLoading] = useState(false)
    const [lastTrackKey, setLastTrackKey] = useState<string>("")
    const iframeRef = React.useRef<HTMLIFrameElement>(null)

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

    // Initial fetch and polling
    useEffect(() => {
        fetchNowPlaying()
        // Poll every 30 seconds (even when flyout is open)
        const interval = setInterval(fetchNowPlaying, 30000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Auto-fetch embed when track changes
    useEffect(() => {
        if (track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [track, embedUrl, embedLoading, fetchSpotifyEmbed])

    // Handle widget click - toggle flyout
    const handleWidgetClick = async () => {
        if (!track) return

        if (!musicPlaying) {
            // Open flyout
            if (!embedUrl && !embedLoading) {
                await fetchSpotifyEmbed()
            }
            setMusicPlaying(true)
        } else {
            // Close flyout
            setMusicPlaying(false)
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
        <div className={cn("relative w-full", className)}>
            {/* WIDGET - Compact for sidebar */}
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-lg cursor-pointer w-full",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    musicPlaying && "border-green-500/60"
                )}
                onClick={handleWidgetClick}
                whileTap={{ scale: 0.98 }}
            >
                {/* Album Art */}
                <div className="relative flex-shrink-0">
                    {track.albumArt ? (
                        <img
                            src={track.albumArt}
                            alt={track.album || 'Album'}
                            className="w-10 h-10 rounded object-cover"
                        />
                    ) : (
                        <div className="w-10 h-10 rounded bg-zinc-800 flex items-center justify-center">
                            <Music className="w-4 h-4 text-zinc-500" />
                        </div>
                    )}
                    {/* Live indicator */}
                    {track.isPlaying && (
                        <div className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                    )}
                </div>

                {/* Track Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1">
                        {track.isPlaying ? (
                            <span className="text-[9px] text-green-400 font-medium">● LIVE</span>
                        ) : (
                            <span className="text-[9px] text-zinc-500">Senaste</span>
                        )}
                    </div>
                    <p className="text-[11px] font-medium text-white truncate leading-tight">{track.name}</p>
                    <p className="text-[9px] text-zinc-400 truncate leading-tight">{track.artist}</p>
                </div>

                {/* Play Button */}
                <div className={cn(
                    "p-1 rounded-full flex-shrink-0",
                    "bg-green-500/20 text-green-400"
                )}>
                    {embedLoading ? (
                        <Loader2 className="w-3 h-3 animate-spin" />
                    ) : (
                        <Play className="w-3 h-3" fill="currentColor" />
                    )}
                </div>
            </motion.div>

            {/* SPOTIFY PLAYER FLYOUT - Opens downward */}
            <AnimatePresence>
                {musicPlaying && embedUrl && (
                    <motion.div
                        initial={{ opacity: 0, y: -10, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -10, scale: 0.95 }}
                        transition={{ duration: 0.15 }}
                        className={cn(
                            "absolute top-full left-0 right-0 mt-2 z-50",
                            "rounded-lg overflow-hidden",
                            "bg-zinc-900/95 backdrop-blur-xl",
                            "border border-zinc-700/50",
                            "shadow-xl"
                        )}
                    >
                        {/* Close button - minimal */}
                        <div className="flex justify-end px-2 pt-1.5">
                            <button
                                onClick={(e) => {
                                    e.stopPropagation()
                                    setMusicPlaying(false)
                                }}
                                className="p-0.5 rounded hover:bg-zinc-800 transition-colors"
                            >
                                <X className="w-3.5 h-3.5 text-zinc-500" />
                            </button>
                        </div>

                        {/* Spotify Embed - Compact */}
                        <div className="px-2 pb-2">
                            <iframe
                                ref={iframeRef}
                                key={embedUrl}
                                src={`${embedUrl}?autoplay=1`}
                                width="100%"
                                height="80"
                                frameBorder="0"
                                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                                loading="eager"
                                style={{ borderRadius: '6px' }}
                            />
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
