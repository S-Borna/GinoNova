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
    const [isMuted, setIsMuted] = useState(false) // Start unmuted for autoplay
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
        // STOP polling completely when embed is active to prevent music interruption
        if (!embedUrl || isMuted) {
            const interval = setInterval(fetchNowPlaying, 30000)
            return () => clearInterval(interval)
        }
    }, [embedUrl, isMuted]) // eslint-disable-line react-hooks/exhaustive-deps

    // Fetch embed when unmuted OR when track changes
    useEffect(() => {
        if (!isMuted && track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [isMuted, track, embedUrl, embedLoading, fetchSpotifyEmbed])

    // Auto-expand and unmute when track is loaded
    useEffect(() => {
        if (track && embedUrl && !isExpanded) {
            setIsExpanded(true)
        }
    }, [track, embedUrl, isExpanded])

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
{/* Main Widget - Kompakt, samma storlek som flyout */}
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-xl cursor-pointer",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    "h-[56px] w-[280px]"
                )}
                onClick={() => setIsExpanded(!isExpanded)}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                {/* Album Art - smaller */}
                <div className="relative flex-shrink-0">
                    {track.albumArt ? (
                        <img
                            src={track.albumArt}
                            alt={track.album || 'Album'}
                            className="w-12 h-12 rounded-md object-cover"
                        />
                    ) : (
                        <div className="w-12 h-12 rounded-md bg-zinc-800 flex items-center justify-center">
                            <Music className="w-5 h-5 text-zinc-500" />
                        </div>
                    )}
                    {track.isPlaying && (
                        <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-500 rounded-full animate-pulse" />
                    )}
                    {/* Playing from website indicator */}
                    {!isMuted && embedUrl && (
                        <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full flex items-center justify-center">
                            <Volume2 className="w-2.5 h-2.5 text-black" />
                        </div>
                    )}
                </div>

                {/* Track Info - compact */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1">
                        {track.isPlaying ? (
                            <Radio className="w-2.5 h-2.5 text-green-400 animate-pulse" />
                        ) : (
                            <Headphones className="w-2.5 h-2.5 text-zinc-400" />
                        )}
                        <span className="text-[10px] text-green-400 font-medium">
                            {track.isPlaying ? 'LIVE' : 'Recent'}
                        </span>
                        {!isMuted && embedUrl && (
                            <span className="text-[10px] text-green-500 font-bold ml-1">🔊 WEB</span>
                        )}
                    </div>
                    <p className="text-xs font-medium text-white truncate leading-tight">{track.name}</p>
                    <p className="text-[10px] text-zinc-400 truncate leading-tight">{track.artist}</p>
                </div>

                {/* Mute/Unmute - smaller */}
                <button
                    onClick={(e) => { e.stopPropagation(); toggleMute(); }}
                    className={cn(
                        "p-1.5 rounded-full transition-colors flex-shrink-0",
                        isMuted 
                            ? "bg-zinc-800 hover:bg-zinc-700 text-zinc-400"
                            : "bg-green-500 hover:bg-green-400 text-black"
                    )}
                    title={isMuted ? "Lyssna med Said" : "Tysta"}
                >
                    {isMuted ? <VolumeX className="w-3.5 h-3.5" /> : <Volume2 className="w-3.5 h-3.5" />}
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
                            "w-[280px] h-[56px]"
                        )}
                    >
                        {/* Compact Spotify Embed - No header, just player */}
                        <div className="relative h-[56px]">
                            {!isMuted && embedUrl ? (
                                <iframe
                                    key={embedUrl}
                                    src={`${embedUrl}&autoplay=1`}
                                    width="100%"
                                    height="80"
                                    frameBorder="0"
                                    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                                    loading="eager"
                                    style={{ borderRadius: '12px' }}
                                />
                            ) : !isMuted && embedLoading ? (
                                <div className="flex items-center justify-center h-full">
                                    <Loader2 className="w-5 h-5 text-green-400 animate-spin" />
                                </div>
                            ) : (
                                <div className="flex items-center justify-center h-full px-3">
                                    <button
                                        onClick={toggleMute}
                                        className="px-4 py-2 text-xs font-medium text-black bg-green-500 rounded-full hover:bg-green-400 flex items-center gap-2"
                                    >
                                        <Volume2 className="w-4 h-4" />
                                        Spela
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
