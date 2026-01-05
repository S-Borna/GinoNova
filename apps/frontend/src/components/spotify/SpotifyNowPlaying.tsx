"use client"

/**
 * Spotify Now Playing Widget
 * Shows what Said is currently listening to on Spotify
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { motion } from "framer-motion"
import { cn } from "@/lib/utils"
import { Music, Volume2, Pause } from "lucide-react"

interface SpotifyTrack {
    isPlaying: boolean
    title: string | null
    artist: string | null
    album: string | null
    albumImageUrl: string | null
    songUrl: string | null
    durationMs: number
    progressMs: number
}

interface SpotifyNowPlayingProps {
    className?: string
    variant?: 'compact' | 'full' | 'mini'
}

export function SpotifyNowPlaying({
    className,
    variant = 'compact'
}: SpotifyNowPlayingProps) {
    const [track, setTrack] = useState<SpotifyTrack | null>(null)
    const [loading, setLoading] = useState(true)
    const [progress, setProgress] = useState(0)

    useEffect(() => {
        const fetchNowPlaying = async () => {
            try {
                const res = await fetch(`/api/music/now-playing?t=${Date.now()}`, {
                    cache: 'no-store'
                })
                if (res.ok) {
                    const data = await res.json()
                    // Map the Last.fm response to our track format
                    if (data.track) {
                        setTrack({
                            isPlaying: data.isPlaying,
                            title: data.track.name,
                            artist: data.track.artist,
                            album: data.track.album,
                            albumImageUrl: data.track.albumArt,
                            songUrl: data.track.lastFmUrl,
                            durationMs: 0,
                            progressMs: 0
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
        }

        fetchNowPlaying()
        const interval = setInterval(fetchNowPlaying, 15000)
        return () => clearInterval(interval)
    }, [])

    // Update progress smoothly when playing
    useEffect(() => {
        if (!track?.isPlaying || !track.durationMs) return

        const interval = setInterval(() => {
            setProgress(prev => {
                const increment = (1000 / track.durationMs) * 100
                return Math.min(prev + increment, 100)
            })
        }, 1000)

        return () => clearInterval(interval)
    }, [track?.isPlaying, track?.durationMs])

    // Loading state
    if (loading) {
        if (variant === 'mini') {
            return (
                <div className={cn(
                    "flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/50 border border-zinc-800",
                    className
                )}>
                    <div className="w-4 h-4 rounded-sm bg-zinc-800 animate-pulse" />
                    <div className="w-16 h-3 bg-zinc-800 rounded animate-pulse" />
                </div>
            )
        }

        return (
            <div className={cn(
                "flex items-center gap-3 p-3 rounded-xl bg-zinc-900/50 border border-zinc-800",
                className
            )}>
                <div className="w-12 h-12 rounded-lg bg-zinc-800 animate-pulse" />
                <div className="flex-1 space-y-2">
                    <div className="h-4 w-24 bg-zinc-800 rounded animate-pulse" />
                    <div className="h-3 w-16 bg-zinc-800 rounded animate-pulse" />
                </div>
            </div>
        )
    }

    if (!track?.title) {
        if (variant === 'mini') {
            return (
                <div className={cn(
                    "flex items-center gap-2 px-3 py-1.5 rounded-full bg-zinc-900/50 border border-zinc-800",
                    className
                )}>
                    <Music className="w-4 h-4 text-zinc-500" />
                    <span className="text-xs text-zinc-500">Offline</span>
                </div>
            )
        }

        return null // Don't show widget if nothing playing (for compact/full)
    }

    // Mini variant
    if (variant === 'mini') {
        return (
            <motion.a
                href={track.songUrl || '#'}
                target="_blank"
                rel="noopener noreferrer"
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className={cn(
                    "group flex items-center gap-2 px-3 py-1.5 rounded-full",
                    track.isPlaying
                        ? "bg-gradient-to-r from-green-500/10 to-emerald-500/10 border border-green-500/20 hover:border-green-500/40"
                        : "bg-zinc-900/50 border border-zinc-800 hover:border-zinc-700",
                    "transition-all cursor-pointer",
                    className
                )}
            >
                <div className="relative">
                    {track.albumImageUrl ? (
                        <img
                            src={track.albumImageUrl}
                            alt={track.album || ''}
                            className="w-5 h-5 rounded-sm"
                        />
                    ) : (
                        <Music className="w-5 h-5 text-zinc-400" />
                    )}
                    {track.isPlaying && (
                        <div className="absolute -bottom-0.5 -right-0.5 w-2 h-2 bg-green-500 rounded-full animate-pulse" />
                    )}
                </div>
                <span className={cn(
                    "text-xs max-w-[120px] truncate",
                    track.isPlaying ? "text-green-400" : "text-zinc-400"
                )}>
                    {track.title}
                </span>
                {track.isPlaying && <Volume2 className="w-3 h-3 text-green-500/50" />}
            </motion.a>
        )
    }

    // Compact variant
    if (variant === 'compact') {
        return (
            <div className="relative">
                <motion.a
                    href={track.songUrl || '#'}
                    target="_blank"
                    rel="noopener noreferrer"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className={cn(
                        "flex items-center gap-3 p-3 rounded-xl",
                        "bg-gradient-to-r from-zinc-900/80 to-zinc-900/50",
                        track.isPlaying
                            ? "border border-green-500/30 hover:border-green-500/50"
                            : "border border-zinc-800 hover:border-zinc-700",
                        "transition-all cursor-pointer",
                        className
                    )}
                >
                    {/* Album art */}
                    <div className="relative shrink-0">
                        {track.albumImageUrl ? (
                            <img
                                src={track.albumImageUrl}
                                alt={track.album || ''}
                                className="w-12 h-12 rounded-lg shadow-lg"
                            />
                        ) : (
                            <div className="w-12 h-12 rounded-lg bg-zinc-800 flex items-center justify-center">
                                <Music className="w-5 h-5 text-zinc-500" />
                            </div>
                        )}
                        {track.isPlaying && (
                            <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-green-500 rounded-full flex items-center justify-center">
                                <Volume2 className="w-2.5 h-2.5 text-white" />
                            </div>
                        )}
                        {!track.isPlaying && (
                            <div className="absolute -bottom-1 -right-1 w-4 h-4 bg-zinc-700 rounded-full flex items-center justify-center">
                                <Pause className="w-2.5 h-2.5 text-zinc-400" />
                            </div>
                        )}
                    </div>

                    {/* Track info */}
                    <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-2">
                            <span className={cn(
                                "text-xs font-medium",
                                track.isPlaying ? "text-green-400" : "text-zinc-500"
                            )}>
                                {track.isPlaying ? 'SPELAR NU' : 'PAUSAD'}
                            </span>
                            {track.isPlaying && (
                                <div className="flex gap-0.5">
                                    {[...Array(3)].map((_, i) => (
                                        <motion.div
                                            key={i}
                                            className="w-0.5 bg-green-500 rounded-full"
                                            animate={{ height: [4, 12, 4] }}
                                            transition={{
                                                duration: 0.5,
                                                repeat: Infinity,
                                                delay: i * 0.1
                                            }}
                                        />
                                    ))}
                                </div>
                            )}
                        </div>
                        <p className="text-sm font-medium text-white truncate">{track.title}</p>
                        <p className="text-xs text-zinc-400 truncate">{track.artist}</p>
                        
                        {/* Progress bar */}
                        {track.isPlaying && (
                            <div className="mt-2 h-1 bg-zinc-800 rounded-full overflow-hidden">
                                <motion.div
                                    className="h-full bg-green-500"
                                    initial={{ width: `${progress}%` }}
                                    animate={{ width: `${progress}%` }}
                                    transition={{ duration: 0.5 }}
                                />
                            </div>
                        )}
                    </div>

                    {/* Spotify logo */}
                    <div className="shrink-0 opacity-50 group-hover:opacity-100 transition-opacity">
                        <svg className="w-5 h-5 text-green-500" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                        </svg>
                    </div>
                </motion.a>
            </div>
        )
    }

    // Full variant
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "rounded-2xl overflow-hidden",
                "bg-gradient-to-br from-zinc-900 via-zinc-900 to-green-950/20",
                "border border-zinc-800",
                className
            )}
        >
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-zinc-800/50">
                <div className="flex items-center gap-2">
                    <svg className="w-5 h-5 text-green-500" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                    </svg>
                    <span className="text-sm font-medium text-white">Spotify</span>
                </div>
                <div className={cn(
                    "flex items-center gap-1.5 px-2 py-1 rounded-full text-xs",
                    track.isPlaying
                        ? "bg-green-500/20 text-green-400"
                        : "bg-zinc-800 text-zinc-400"
                )}>
                    {track.isPlaying ? (
                        <>
                            <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
                            Live
                        </>
                    ) : (
                        <>
                            <Pause className="w-3 h-3" />
                            Pausad
                        </>
                    )}
                </div>
            </div>

            {/* Content */}
            <a
                href={track.songUrl || '#'}
                target="_blank"
                rel="noopener noreferrer"
                className="block p-4 hover:bg-white/5 transition-colors"
            >
                <div className="flex gap-4">
                    {/* Album Art */}
                    <div className="relative shrink-0">
                        {track.albumImageUrl ? (
                            <img
                                src={track.albumImageUrl}
                                alt={track.album || ''}
                                className="w-20 h-20 rounded-xl shadow-lg"
                            />
                        ) : (
                            <div className="w-20 h-20 rounded-xl bg-zinc-800 flex items-center justify-center">
                                <Music className="w-8 h-8 text-zinc-600" />
                            </div>
                        )}
                    </div>

                    {/* Track Info */}
                    <div className="flex-1 min-w-0">
                        <h3 className="text-lg font-bold text-white truncate">{track.title}</h3>
                        <p className="text-sm text-zinc-400 truncate">{track.artist}</p>
                        <p className="text-xs text-zinc-500 truncate mt-1">{track.album}</p>

                        {/* Progress Bar */}
                        <div className="mt-3">
                            <div className="h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                                <motion.div
                                    className="h-full bg-green-500"
                                    initial={{ width: `${progress}%` }}
                                    animate={{ width: `${progress}%` }}
                                    transition={{ duration: 0.5 }}
                                />
                            </div>
                            <div className="flex justify-between mt-1 text-[10px] text-zinc-500">
                                <span>{formatTime(track.progressMs)}</span>
                                <span>{formatTime(track.durationMs)}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </motion.div>
    )
}

function formatTime(ms: number): string {
    const seconds = Math.floor(ms / 1000)
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, '0')}`
}
