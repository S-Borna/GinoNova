"use client"

/**
 * Music Live Player Widget
 * 
 * Shows what Said is listening to AND plays it via Deezer preview.
 * NO API KEYS NEEDED - Deezer API is completely free!
 * 
 * Features:
 * - Shows current track from Last.fm
 * - Click to expand player
 * - Plays 30-second preview via Deezer
 * - Volume control
 */

import * as React from "react"
import { useState, useEffect, useCallback, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { 
    Music, 
    Volume2, 
    VolumeX,
    Radio,
    Headphones,
    X,
    Play,
    Pause,
    Loader2
} from "lucide-react"

interface Track {
    isPlaying: boolean
    name: string | null
    artist: string | null
    album: string | null
    albumArt: string | null
}

interface DeezerTrack {
    previewUrl: string
    albumArt: string
}

interface SpotifyLivePlayerProps {
    className?: string
}

export function SpotifyLivePlayer({ className }: SpotifyLivePlayerProps) {
    const [track, setTrack] = useState<Track | null>(null)
    const [loading, setLoading] = useState(true)
    const [isExpanded, setIsExpanded] = useState(false)
    const [isPlaying, setIsPlaying] = useState(false)
    const [deezerTrack, setDeezerTrack] = useState<DeezerTrack | null>(null)
    const [audioLoading, setAudioLoading] = useState(false)
    const audioRef = useRef<HTMLAudioElement | null>(null)

    // Fetch current track from Last.fm
    const fetchNowPlaying = useCallback(async () => {
        try {
            const res = await fetch(`/api/music/now-playing?t=${Date.now()}`, {
                cache: 'no-store'
            })
            if (res.ok) {
                const data = await res.json()
                if (data.track) {
                    const newTrack = {
                        isPlaying: data.isPlaying,
                        name: data.track.name,
                        artist: data.track.artist,
                        album: data.track.album,
                        albumArt: data.track.albumArt,
                    }
                    
                    // Only update if track changed
                    if (!track || track.name !== newTrack.name || track.artist !== newTrack.artist) {
                        setTrack(newTrack)
                        setDeezerTrack(null) // Reset for new track
                        setIsPlaying(false)
                    }
                } else {
                    setTrack(null)
                    setDeezerTrack(null)
                }
            }
        } catch (error) {
            console.error('Failed to fetch music:', error)
        } finally {
            setLoading(false)
        }
    }, [track])

    // Fetch Deezer preview when play is clicked
    const fetchDeezerPreview = useCallback(async () => {
        if (!track?.name || !track?.artist) return null
        
        setAudioLoading(true)
        try {
            const res = await fetch(
                `/api/music/deezer-track?track=${encodeURIComponent(track.name)}&artist=${encodeURIComponent(track.artist)}`
            )
            if (res.ok) {
                const data = await res.json()
                if (data.track?.previewUrl) {
                    return data.track
                }
            }
        } catch (e) {
            console.error('Failed to get Deezer track:', e)
        } finally {
            setAudioLoading(false)
        }
        return null
    }, [track])

    useEffect(() => {
        fetchNowPlaying()
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, []) // eslint-disable-line react-hooks/exhaustive-deps

    // Setup audio element
    useEffect(() => {
        audioRef.current = new Audio()
        audioRef.current.volume = 0.7
        
        audioRef.current.onended = () => setIsPlaying(false)
        audioRef.current.onpause = () => setIsPlaying(false)
        audioRef.current.onplay = () => setIsPlaying(true)
        
        return () => {
            if (audioRef.current) {
                audioRef.current.pause()
                audioRef.current = null
            }
        }
    }, [])

    const togglePlay = async () => {
        if (!audioRef.current) return

        if (isPlaying) {
            audioRef.current.pause()
            setIsPlaying(false)
            return
        }

        // Fetch Deezer preview if not already loaded
        let preview = deezerTrack
        if (!preview) {
            preview = await fetchDeezerPreview()
            if (preview) {
                setDeezerTrack(preview)
            }
        }

        if (preview?.previewUrl) {
            audioRef.current.src = preview.previewUrl
            try {
                await audioRef.current.play()
                setIsPlaying(true)
                if (!isExpanded) setIsExpanded(true)
            } catch (e) {
                console.error('Playback failed:', e)
            }
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
                            src={deezerTrack?.albumArt || track.albumArt}
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

                {/* Play/Pause Button */}
                <button
                    onClick={(e) => { e.stopPropagation(); togglePlay(); }}
                    disabled={audioLoading}
                    className={cn(
                        "p-2 rounded-full transition-colors",
                        isPlaying 
                            ? "bg-green-500 hover:bg-green-400 text-black"
                            : "bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white"
                    )}
                    title={isPlaying ? "Pausa" : "Lyssna med Said"}
                >
                    {audioLoading ? (
                        <Loader2 className="w-4 h-4 animate-spin" />
                    ) : isPlaying ? (
                        <Pause className="w-4 h-4" fill="currentColor" />
                    ) : (
                        <Play className="w-4 h-4" fill="currentColor" />
                    )}
                </button>
            </motion.div>

            {/* Expanded Player */}
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
                            "shadow-2xl shadow-black/50",
                            "min-w-[280px]"
                        )}
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between px-3 py-2 bg-zinc-800/50 border-b border-zinc-700/50">
                            <div className="flex items-center gap-2">
                                {isPlaying && <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />}
                                <span className="text-xs text-zinc-400">
                                    {isPlaying ? '♪ Spelar nu' : 'Lyssna med Said'}
                                </span>
                            </div>
                            <button
                                onClick={(e) => { e.stopPropagation(); setIsExpanded(false); }}
                                className="p-1 rounded-full hover:bg-zinc-700/50 text-zinc-400 hover:text-white"
                            >
                                <X className="w-4 h-4" />
                            </button>
                        </div>

                        {/* Player Content */}
                        <div className="p-4">
                            <div className="flex gap-4 items-center">
                                {/* Album Art */}
                                <div className="relative">
                                    {(deezerTrack?.albumArt || track.albumArt) ? (
                                        <img
                                            src={deezerTrack?.albumArt || track.albumArt!}
                                            alt={track.album || 'Album'}
                                            className={cn(
                                                "w-16 h-16 rounded-lg object-cover shadow-lg",
                                                isPlaying && "animate-pulse"
                                            )}
                                        />
                                    ) : (
                                        <div className="w-16 h-16 rounded-lg bg-zinc-800 flex items-center justify-center">
                                            <Music className="w-6 h-6 text-zinc-500" />
                                        </div>
                                    )}
                                </div>
                                
                                {/* Track Info */}
                                <div className="flex-1 min-w-0">
                                    <p className="text-base font-semibold text-white truncate">{track.name}</p>
                                    <p className="text-sm text-zinc-400 truncate">{track.artist}</p>
                                    {track.album && (
                                        <p className="text-xs text-zinc-500 truncate mt-0.5">{track.album}</p>
                                    )}
                                </div>
                            </div>

                            {/* Play Button */}
                            <button
                                onClick={togglePlay}
                                disabled={audioLoading}
                                className={cn(
                                    "w-full mt-4 py-3 px-4 rounded-xl font-semibold",
                                    "flex items-center justify-center gap-2 transition-all",
                                    isPlaying 
                                        ? "bg-zinc-800 hover:bg-zinc-700 text-white"
                                        : "bg-green-500 hover:bg-green-400 text-black"
                                )}
                            >
                                {audioLoading ? (
                                    <>
                                        <Loader2 className="w-5 h-5 animate-spin" />
                                        Laddar...
                                    </>
                                ) : isPlaying ? (
                                    <>
                                        <Pause className="w-5 h-5" fill="currentColor" />
                                        Pausa
                                    </>
                                ) : (
                                    <>
                                        <Play className="w-5 h-5" fill="currentColor" />
                                        Spela preview
                                    </>
                                )}
                            </button>
                        </div>

                        {/* Footer */}
                        <div className="px-4 py-2 bg-zinc-800/30 border-t border-zinc-700/50">
                            <p className="text-xs text-zinc-500 text-center">
                                30 sek förhandslyssning via Deezer
                            </p>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    )
}

export default SpotifyLivePlayer
