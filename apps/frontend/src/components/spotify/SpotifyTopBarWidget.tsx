"use client"

/**
 * Spotify TopBar Widget - Compact player for TopBar
 *
 * Features:
 * - Compact widget showing currently playing track
 * - Click Play → Opens Spotify in new tab for full playback
 * - No 30-second limit since it opens native Spotify
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import {
    Music,
    Loader2,
    Play
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
    const [spotifyUrl, setSpotifyUrl] = useState<string | null>(null)
    const [urlLoading, setUrlLoading] = useState(false)
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
                    if (newKey !== lastTrackKey) {
                        setTrack({
                            isPlaying: data.isPlaying,
                            name: data.track.name,
                            artist: data.track.artist,
                            album: data.track.album,
                            albumArt: data.track.albumArt,
                        })
                        setLastTrackKey(newKey)
                        setSpotifyUrl(null) // Reset URL for new track
                    }
                } else {
                    if (track !== null) {
                        setTrack(null)
                        setSpotifyUrl(null)
                    }
                }
            }
        } catch (error) {
            console.error('Failed to fetch music:', error)
        } finally {
            setLoading(false)
        }
    }, [lastTrackKey, track])

    // Fetch Spotify URL for direct link
    const fetchSpotifyUrl = useCallback(async () => {
        if (!track?.name || !track?.artist || spotifyUrl) return null

        setUrlLoading(true)
        try {
            const res = await fetch(
                `/api/music/spotify-finder?track=${encodeURIComponent(track.name)}&artist=${encodeURIComponent(track.artist)}`
            )
            if (res.ok) {
                const data = await res.json()
                if (data.spotifyUrl) {
                    setSpotifyUrl(data.spotifyUrl)
                    return { url: data.spotifyUrl }
                }
            }
        } catch (e) {
            console.error('Failed to get Spotify URL:', e)
        } finally {
            setUrlLoading(false)
        }
        return null
    }, [track, spotifyUrl])

    // Initial fetch and polling
    useEffect(() => {
        fetchNowPlaying()
        const interval = setInterval(fetchNowPlaying, 30000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Pre-fetch Spotify URL when track changes
    useEffect(() => {
        if (track && !spotifyUrl && !urlLoading) {
            fetchSpotifyUrl()
        }
    }, [track, spotifyUrl, urlLoading, fetchSpotifyUrl])

    // Handle play click - open Spotify web player in new tab
    const handlePlayClick = async (e: React.MouseEvent) => {
        e.stopPropagation()

        if (!track) return

        let url = spotifyUrl

        // If we don't have the URL yet, fetch it
        if (!url && !urlLoading) {
            const result = await fetchSpotifyUrl()
            if (result) {
                url = result.url
            }
        }

        if (url) {
            // Open Spotify web player in new tab
            // This gives full playback (not just 30s preview)
            window.open(url, '_blank', 'noopener,noreferrer')
        } else {
            // Fallback: search on Spotify
            const searchUrl = `https://open.spotify.com/search/${encodeURIComponent(`${track.name} ${track.artist}`)}`
            window.open(searchUrl, '_blank', 'noopener,noreferrer')
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
            className={cn("relative", className)}
        >
            {/* WIDGET - LARGE stretched bar with play button */}
            <div
                className={cn(
                    "flex items-center gap-3 px-4 py-2 rounded-xl",
                    "bg-gradient-to-r from-green-500/15 to-emerald-500/15",
                    "border border-green-500/30",
                    "transition-all duration-200",
                    "min-w-[240px]",
                    "shadow-lg shadow-black/20"
                )}
            >
                {/* Equalizer Bars - LARGE - Only animate when music is playing */}
                <div className="flex items-end gap-0.5 h-5">
                    {[0, 1, 2, 3, 4].map((i) => (
                        <motion.div
                            key={i}
                            className={cn(
                                "w-1 rounded-full",
                                track.isPlaying ? "bg-green-500" : "bg-green-500/50"
                            )}
                            animate={track.isPlaying ? {
                                height: ["4px", "20px", "10px", "16px", "4px"],
                            } : {
                                height: ["4px", "8px", "6px", "10px", "7px"][i]
                            }}
                            transition={track.isPlaying ? {
                                duration: 0.8,
                                repeat: Infinity,
                                delay: i * 0.12,
                                ease: "easeInOut",
                            } : {
                                duration: 0.3
                            }}
                        />
                    ))}
                </div>

                {/* Track Info - LARGER TEXT */}
                <div className="min-w-0 flex-1">
                    <p className="text-sm font-bold text-white truncate">{track.name}</p>
                    <p className="text-xs text-zinc-400 truncate">{track.artist}</p>
                </div>

                {/* Play on Spotify Button - LARGER with Play icon */}
                <motion.button
                    onClick={handlePlayClick}
                    disabled={urlLoading}
                    className={cn(
                        "w-8 h-8 rounded-full flex-shrink-0 flex items-center justify-center",
                        "bg-green-500 hover:bg-green-400",
                        "text-black",
                        "transition-all duration-200",
                        "shadow-md shadow-green-500/40",
                        "disabled:opacity-50 disabled:cursor-wait"
                    )}
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.95 }}
                    title="Spela i Spotify"
                >
                    {urlLoading ? (
                        <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                        <Play className="w-4 h-4 fill-black ml-0.5" />
                    )}
                </motion.button>
            </div>
        </motion.div>
    )
}

export default SpotifyTopBarWidget
