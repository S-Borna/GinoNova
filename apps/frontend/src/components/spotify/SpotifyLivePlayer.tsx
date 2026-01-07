"use client"

/**
 * Spotify Live Player Widget
 * 
 * SIMPLE: Click widget → Music starts playing
 * NO flyout, NO extra buttons, just ONE CLICK
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
    Music, 
    Volume2,
    Radio,
    Headphones,
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

interface SpotifyLivePlayerProps {
    className?: string
}

export function SpotifyLivePlayer({ className }: SpotifyLivePlayerProps) {
    const [track, setTrack] = useState<Track | null>(null)
    const [loading, setLoading] = useState(true)
    const [isPlayingOnWebsite, setIsPlayingOnWebsite] = useState(false)
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
        // STOP polling completely when playing to prevent music interruption
        if (!isPlayingOnWebsite) {
            const interval = setInterval(fetchNowPlaying, 30000)
            return () => clearInterval(interval)
        }
    }, [isPlayingOnWebsite]) // eslint-disable-line react-hooks/exhaustive-deps

    // Fetch embed when user starts playing
    useEffect(() => {
        if (isPlayingOnWebsite && track && !embedUrl && !embedLoading) {
            fetchSpotifyEmbed()
        }
    }, [isPlayingOnWebsite, track, embedUrl, embedLoading, fetchSpotifyEmbed])

    // Handle widget click - START MUSIC IMMEDIATELY
    const handleWidgetClick = () => {
        if (!isPlayingOnWebsite && track) {
            setIsPlayingOnWebsite(true)
            // Fetch embed if not already loaded
            if (!embedUrl && !embedLoading) {
                fetchSpotifyEmbed()
            }
        } else if (isPlayingOnWebsite) {
            setIsPlayingOnWebsite(false)
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
            {/* Hidden Spotify Embed - Plays music in background */}
            {isPlayingOnWebsite && embedUrl && (
                <iframe
                    key={embedUrl}
                    src={`${embedUrl}&autoplay=1`}
                    width="0"
                    height="0"
                    frameBorder="0"
                    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                    loading="eager"
                    style={{ position: 'absolute', opacity: 0, pointerEvents: 'none' }}
                />
            )}

            {/* Main Widget - ONE CLICK TO PLAY */}
            <motion.div
                className={cn(
                    "flex items-center gap-2 px-2 py-1.5 rounded-xl cursor-pointer",
                    "bg-gradient-to-r from-green-500/10 to-emerald-500/10",
                    "border border-green-500/20 hover:border-green-500/40",
                    "transition-all duration-200",
                    "h-[56px] w-[280px]",
                    isPlayingOnWebsite && "border-green-500/60 shadow-lg shadow-green-500/20"
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
                    {/* Only show Spotify indicator if ACTUALLY playing on Spotify */}
                    {track.isPlaying && !isPlayingOnWebsite && (
                        <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-500 rounded-full animate-pulse" />
                    )}
                    {/* Playing from website indicator */}
                    {isPlayingOnWebsite && (
                        <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full flex items-center justify-center animate-pulse">
                            <Volume2 className="w-2.5 h-2.5 text-black" />
                        </div>
                    )}
                </div>

                {/* Track Info */}
                <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1">
                        {isPlayingOnWebsite ? (
                            // Playing on website
                            <>
                                <Volume2 className="w-2.5 h-2.5 text-green-400 animate-pulse" />
                                <span className="text-[10px] text-green-500 font-bold animate-pulse">🔊 SPELAR HÄR</span>
                            </>
                        ) : track.isPlaying ? (
                            // Playing on YOUR Spotify right now
                            <>
                                <Radio className="w-2.5 h-2.5 text-green-400 animate-pulse" />
                                <span className="text-[10px] text-green-400 font-medium">LIVE NU</span>
                            </>
                        ) : (
                            // Not playing - just last played
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

                {/* Play/Stop indicator */}
                <div className={cn(
                    "p-1.5 rounded-full flex-shrink-0 transition-colors",
                    isPlayingOnWebsite 
                        ? "bg-green-500 text-black animate-pulse"
                        : "bg-zinc-800 text-zinc-400"
                )}>
                    {embedLoading ? (
                        <Loader2 className="w-3.5 h-3.5 animate-spin" />
                    ) : isPlayingOnWebsite ? (
                        <Volume2 className="w-3.5 h-3.5" />
                    ) : (
                        <Play className="w-3.5 h-3.5" fill="currentColor" />
                    )}
                </div>
            </motion.div>
        </div>
    )
}

export default SpotifyLivePlayer
