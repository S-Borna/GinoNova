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
            } else {
                // Fallback: create search embed directly
                const searchQuery = encodeURIComponent(`${track.name} ${track.artist}`)
                setEmbedUrl(`https://open.spotify.com/embed/search/${searchQuery}?utm_source=generator&theme=0`)
            }
        } catch (e) {
            console.error('Failed to get Spotify embed:', e)
            // Fallback on error too
            const searchQuery = encodeURIComponent(`${track.name} ${track.artist}`)
            setEmbedUrl(`https://open.spotify.com/embed/search/${searchQuery}?utm_source=generator&theme=0`)
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
        <div className={cn("w-full", className)}>
            {/* WIDGET - Compact clickable bar */}
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-lg cursor-pointer w-full",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    musicPlaying && "border-green-500/60 rounded-b-none"
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
                            className="w-8 h-8 rounded object-cover"
                        />
                    ) : (
                        <div className="w-8 h-8 rounded bg-zinc-800 flex items-center justify-center">
                            <Music className="w-3 h-3 text-zinc-500" />
                        </div>
                    )}
                    {/* Live indicator */}
                    {track.isPlaying && (
                        <div className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                    )}
                </div>

                {/* Track Info */}
                <div className="flex-1 min-w-0">
                    <p className="text-[10px] font-medium text-white truncate leading-tight">{track.name}</p>
                    <p className="text-[8px] text-zinc-400 truncate leading-tight">{track.artist}</p>
                </div>

                {/* Play/Close Button */}
                <div className={cn(
                    "p-1 rounded-full flex-shrink-0",
                    musicPlaying ? "bg-red-500/20 text-red-400" : "bg-green-500/20 text-green-400"
                )}>
                    {embedLoading ? (
                        <Loader2 className="w-3 h-3 animate-spin" />
                    ) : musicPlaying ? (
                        <X className="w-3 h-3" />
                    ) : (
                        <Play className="w-3 h-3" fill="currentColor" />
                    )}
                </div>
            </motion.div>

            {/* SPOTIFY PLAYER - Inline expansion (not overlay) */}
            <AnimatePresence>
                {musicPlaying && embedUrl && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        exit={{ opacity: 0, height: 0 }}
                        transition={{ duration: 0.2 }}
                        className={cn(
                            "overflow-hidden",
                            "rounded-b-lg",
                            "bg-zinc-900/95",
                            "border border-t-0 border-green-500/20"
                        )}
                    >
                        {/* Spotify Embed - Compact 80px */}
                        <iframe
                            ref={iframeRef}
                            key={embedUrl}
                            src={`${embedUrl}?autoplay=1`}
                            width="100%"
                            height="80"
                            frameBorder="0"
                            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                            loading="eager"
                            className="rounded-b-lg"
                        />
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
