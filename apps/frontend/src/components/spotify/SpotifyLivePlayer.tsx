"use client"

/**
 * Spotify Live Player - ONE CLICK TO PLAY
 *
 * Klicka widgeten → Musik spelas DIREKT i dina högtalare
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
    Square,
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
    const [musicPlaying, setMusicPlaying] = useState(false) // Is music playing on website?
    const [embedUrl, setEmbedUrl] = useState<string | null>(null)
    const [embedLoading, setEmbedLoading] = useState(false)
    const [lastTrackKey, setLastTrackKey] = useState<string>("")
    const iframeRef = React.useRef<HTMLIFrameElement>(null)
    
    // SEPARATE state for flyout - won't change when widget updates!
    const [flyoutEmbedUrl, setFlyoutEmbedUrl] = useState<string | null>(null)

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

    useEffect(() => {
        fetchNowPlaying()
        // Poll every 15 seconds - balance between speed and stability
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Auto-fetch embed when track changes
    useEffect(() => {
        if (track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [track, embedUrl, embedLoading, fetchSpotifyEmbed])

    // Handle widget click - PLAY MUSIC NOW
    const handleWidgetClick = async () => {
        if (!track) return

        if (!musicPlaying) {
            // START PLAYING
            if (!embedUrl && !embedLoading) {
                await fetchSpotifyEmbed()
            }
            // Save current embed URL to flyout (won't change when widget updates)
            if (embedUrl) {
                setFlyoutEmbedUrl(embedUrl)
            }
            setMusicPlaying(true)
        } else {
            // STOP PLAYING
            setMusicPlaying(false)
            setFlyoutEmbedUrl(null)
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
            {/* WIDGET - Always visible, continues updating */}
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-xl cursor-pointer",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    "h-[56px] w-[280px]",
                    musicPlaying && "border-green-500/60 shadow-lg shadow-green-500/20"
                )}
                onClick={handleWidgetClick}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
            >
                {/* Album Art */}
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
                    {/* Spotify playing indicator */}
                    {track.isPlaying && (
                        <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-500 rounded-full animate-pulse" />
                    )}
                </div>

                {/* Track Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1">
                        {track.isPlaying ? (
                            <>
                                <Radio className="w-2.5 h-2.5 text-green-400 animate-pulse" />
                                <span className="text-[10px] text-green-400 font-medium">LIVE</span>
                            </>
                        ) : (
                            <>
                                <Headphones className="w-2.5 h-2.5 text-zinc-500" />
                                <span className="text-[10px] text-zinc-500 font-medium">Senaste</span>
                            </>
                        )}
                        {embedLoading && (
                            <span className="text-[10px] text-zinc-400 ml-1">⏳</span>
                        )}
                    </div>
                    <p className="text-xs font-medium text-white truncate leading-tight">{track.name}</p>
                    <p className="text-[10px] text-zinc-400 truncate leading-tight">{track.artist}</p>
                </div>

                {/* Play Button */}
                <div className={cn(
                    "p-1.5 rounded-full flex-shrink-0 transition-all",
                    "bg-zinc-800 text-zinc-400 hover:bg-zinc-700"
                )}>
                    {embedLoading ? (
                        <Loader2 className="w-3.5 h-3.5 animate-spin" />
                    ) : (
                        <Play className="w-3.5 h-3.5" fill="currentColor" />
                    )}
                </div>
            </motion.div>

            {/* SPOTIFY PLAYER - Flyout to the LEFT */}
            <AnimatePresence>
                {musicPlaying && flyoutEmbedUrl && (
                    <motion.div
                        initial={{ opacity: 0, x: 20, scale: 0.95 }}
                        animate={{ opacity: 1, x: 0, scale: 1 }}
                        exit={{ opacity: 0, x: 20, scale: 0.95 }}
                        transition={{ duration: 0.2, ease: "easeOut" }}
                        className={cn(
                            "fixed top-4 right-[320px] z-40",
                            "rounded-xl overflow-hidden",
                            "bg-zinc-900/95 backdrop-blur-xl",
                            "border border-zinc-800/50",
                            "shadow-2xl shadow-black/50",
                            "h-[80px] w-[280px]"
                        )}
                    >
                        {/* Close button - compact */}
                        <button
                            onClick={(e) => {
                                e.stopPropagation()
                                setMusicPlaying(false)
                                setFlyoutEmbedUrl(null)
                            }}
                            className="absolute top-1 right-1 z-10 p-0.5 rounded-md bg-zinc-800/80 hover:bg-zinc-700 transition-colors"
                        >
                            <X className="w-3 h-3 text-zinc-400" />
                        </button>

                        {/* Spotify Embed - 80px = allt innehåll syns, ingen scroll */}
                        <iframe
                            ref={iframeRef}
                            key={flyoutEmbedUrl}
                            src={`${flyoutEmbedUrl}&autoplay=1`}
                            width="100%"
                            height="80"
                            frameBorder="0"
                            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                            loading="eager"
                            style={{ borderRadius: '12px' }}
                        />
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
