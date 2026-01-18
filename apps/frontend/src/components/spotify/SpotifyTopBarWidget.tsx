"use client"

/**
 * Spotify TopBar Widget - Compact player for TopBar
 *
 * Features:
 * - Compact widget showing currently playing track
 * - Click → Flyout expands LEFT (not down)
 * - Spotify embed player in flyout
 * - All controls visible without scroll
 */

import * as React from "react"
import { useState, useEffect, useCallback, useRef } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Music,
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

interface SpotifyTopBarWidgetProps {
    className?: string
}

export function SpotifyTopBarWidget({ className }: SpotifyTopBarWidgetProps) {
    const [track, setTrack] = useState<Track | null>(null)
    const [loading, setLoading] = useState(true)
    const [isOpen, setIsOpen] = useState(false)
    const [embedUrl, setEmbedUrl] = useState<string | null>(null)
    const [embedLoading, setEmbedLoading] = useState(false)
    const [lastTrackKey, setLastTrackKey] = useState<string>("")
    const containerRef = useRef<HTMLDivElement>(null)

    // Close on outside click
    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
                setIsOpen(false)
            }
        }
        document.addEventListener("mousedown", handleClickOutside)
        return () => document.removeEventListener("mousedown", handleClickOutside)
    }, [])

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
                    if (newKey !== lastTrackKey) {
                        setTrack({
                            isPlaying: data.isPlaying,
                            name: data.track.name,
                            artist: data.track.artist,
                            album: data.track.album,
                            albumArt: data.track.albumArt,
                        })
                        setLastTrackKey(newKey)
                        setEmbedUrl(null)
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
        const interval = setInterval(fetchNowPlaying, 30000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Auto-fetch embed when track changes
    useEffect(() => {
        if (track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [track, embedUrl, embedLoading, fetchSpotifyEmbed])

    // Handle widget click
    const handleClick = async () => {
        if (!track) return

        if (!isOpen) {
            if (!embedUrl && !embedLoading) {
                await fetchSpotifyEmbed()
            }
            setIsOpen(true)
        } else {
            setIsOpen(false)
        }
    }

    // Loading state
    if (loading) {
        return (
            <div className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-xl",
                "bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <div className="w-6 h-6 rounded bg-zinc-800 animate-pulse" />
                <div className="h-3 w-16 bg-zinc-800 rounded animate-pulse hidden sm:block" />
            </div>
        )
    }

    // Nothing playing
    if (!track?.name) {
        return (
            <div className={cn(
                "flex items-center gap-2 px-3 py-1.5 rounded-xl",
                "bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <Music className="w-4 h-4 text-zinc-500" />
                <span className="text-xs text-zinc-500 hidden sm:block">No music</span>
            </div>
        )
    }

    return (
        <motion.div
            ref={containerRef}
            className={cn("relative", className)}
            animate={{ x: isOpen ? 150 : 0 }}
            transition={{ duration: 0.2, ease: "easeOut" }}
        >
            {/* WIDGET - Compact clickable bar */}
            <motion.button
                className={cn(
                    "flex items-center gap-3 px-4 py-2 rounded-xl cursor-pointer",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    isOpen && "border-green-500/60"
                )}
                onClick={handleClick}
                whileTap={{ scale: 0.98 }}
            >
                {/* Equalizer Bars - Only animate when music is playing */}
                <div className="flex items-end gap-[2px] h-4">
                    {[0, 1, 2, 3].map((i) => (
                        <motion.div
                            key={i}
                            className={cn(
                                "w-[3px] rounded-full",
                                track.isPlaying ? "bg-green-500" : "bg-green-500/50"
                            )}
                            animate={track.isPlaying ? {
                                height: ["40%", "100%", "60%", "80%", "40%"],
                            } : {
                                height: ["30%", "50%", "40%", "60%"][i] + "%"
                            }}
                            transition={track.isPlaying ? {
                                duration: 0.8,
                                repeat: Infinity,
                                delay: i * 0.15,
                                ease: "easeInOut",
                            } : {
                                duration: 0.3
                            }}
                        />
                    ))}
                </div>

                {/* Track Info */}
                <div className="min-w-0">
                    <p className="text-sm font-medium text-white truncate">{track.name}</p>
                    <p className="text-xs text-zinc-400 truncate">{track.artist}</p>
                </div>

                {/* Play/Close Icon */}
                <div className={cn(
                    "p-1.5 rounded-full flex-shrink-0",
                    isOpen ? "bg-red-500/20 text-red-400" : "bg-green-500/20 text-green-400"
                )}>
                    {embedLoading ? (
                        <Loader2 className="w-3 h-3 animate-spin" />
                    ) : isOpen ? (
                        <X className="w-3 h-3" />
                    ) : (
                        <Play className="w-3 h-3" fill="currentColor" />
                    )}
                </div>
            </motion.button>

            {/* FLYOUT - Opens to the LEFT of widget */}
            {/* 
             * IMPORTANT: We use CSS visibility instead of conditional rendering
             * to prevent the Spotify iframe from unmounting and stopping playback
             * when the flyout is closed or user navigates/clicks elsewhere
             */}
            {embedUrl && (
                <motion.div
                    initial={{ opacity: 0, x: 10, scale: 0.95 }}
                    animate={{ 
                        opacity: isOpen ? 1 : 0, 
                        x: isOpen ? 0 : 10, 
                        scale: isOpen ? 1 : 0.95,
                        pointerEvents: isOpen ? "auto" : "none"
                    }}
                    transition={{ duration: 0.15, ease: "easeOut" }}
                    className={cn(
                        "absolute right-full top-1/2 -translate-y-1/2 mr-2",
                        "w-[300px]",
                        "rounded-xl overflow-hidden",
                        "bg-zinc-900/95 backdrop-blur-xl",
                        "border border-green-500/30",
                        "shadow-2xl shadow-green-500/10",
                        "z-50",
                        !isOpen && "invisible"
                    )}
                    style={{ visibility: isOpen ? "visible" : "hidden" }}
                >
                    {/* Spotify Embed - stays mounted to keep playing */}
                    <iframe
                        key={embedUrl}
                        src={`${embedUrl}&autoplay=1`}
                        width="100%"
                        height="80"
                        frameBorder="0"
                        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                        allowFullScreen
                        loading="eager"
                        className="rounded-xl"
                    />
                </motion.div>
            )}
        </motion.div>
    )
}

export default SpotifyTopBarWidget
