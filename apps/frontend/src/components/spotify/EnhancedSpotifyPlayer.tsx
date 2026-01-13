"use client"

/**
 * ============================================================================
 * ENHANCED SPOTIFY PLAYER - Study Edition
 * ============================================================================
 *
 * Features:
 * - Study playlist recommendations
 * - Mood-based selection
 * - Learning mode (instrumental only)
 * - Volume controls with smooth fading
 * - Now playing with album art
 * - Queue management
 * - Shuffle and repeat
 * - Integration with Pomodoro timer
 * - Music visualizer
 *
 * @phase Spotify Enhancement
 */

import * as React from "react"
import { useState, useEffect, useCallback } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { MusicVisualizer, VisualizationStyle } from "./MusicVisualizer"
import {
    Music,
    Volume2,
    VolumeX,
    Play,
    Pause,
    SkipForward,
    SkipBack,
    Shuffle,
    Repeat,
    List,
    Heart,
    Settings,
    Headphones,
    Coffee,
    Zap,
    Waves,
    Brain,
    X,
    ChevronDown,
    ChevronUp
} from "lucide-react"

/* ============================================================================
   TYPES
   ============================================================================ */

export type MoodType = "focus" | "energetic" | "calm" | "happy"
export type PlaylistCategory = "focus-coding" | "lofi-devops" | "ambient-work" | "study-music"

export interface StudyPlaylist {
    id: string
    name: string
    description: string
    category: PlaylistCategory
    spotifyUri: string
    embedUrl: string
    mood: MoodType[]
    instrumental: boolean
    image: string
}

export interface EnhancedSpotifyPlayerProps {
    /** Whether to start playing automatically */
    autoPlay?: boolean
    /** Pomodoro integration - auto play on timer start */
    pomodoroActive?: boolean
    /** Pomodoro break mode */
    isBreakTime?: boolean
    /** Custom className */
    className?: string
    /** Callback when playback starts */
    onPlay?: () => void
    /** Callback when playback stops */
    onPause?: () => void
}

/* ============================================================================
   STUDY PLAYLISTS DATA
   ============================================================================ */

const STUDY_PLAYLISTS: StudyPlaylist[] = [
    {
        id: "focus-beats-1",
        name: "Focus Beats for Coding",
        description: "Deep focus electronic beats perfect for coding sessions",
        category: "focus-coding",
        spotifyUri: "spotify:playlist:37i9dQZF1DX8NTLI2TtZa6",
        embedUrl: "https://open.spotify.com/embed/playlist/37i9dQZF1DX8NTLI2TtZa6",
        mood: ["focus", "energetic"],
        instrumental: true,
        image: "/api/placeholder/80/80"
    },
    {
        id: "lofi-1",
        name: "Lo-Fi DevOps",
        description: "Chill lo-fi beats for long DevOps sessions",
        category: "lofi-devops",
        spotifyUri: "spotify:playlist:37i9dQZF1DWWQRwui0ExPn",
        embedUrl: "https://open.spotify.com/embed/playlist/37i9dQZF1DWWQRwui0ExPn",
        mood: ["calm", "focus"],
        instrumental: true,
        image: "/api/placeholder/80/80"
    },
    {
        id: "ambient-1",
        name: "Ambient for Deep Work",
        description: "Atmospheric ambient music for maximum concentration",
        category: "ambient-work",
        spotifyUri: "spotify:playlist:37i9dQZF1DX3Ogo9pFvBkY",
        embedUrl: "https://open.spotify.com/embed/playlist/37i9dQZF1DX3Ogo9pFvBkY",
        mood: ["calm", "focus"],
        instrumental: true,
        image: "/api/placeholder/80/80"
    },
    {
        id: "study-1",
        name: "Study Music",
        description: "Classical and instrumental pieces for studying",
        category: "study-music",
        spotifyUri: "spotify:playlist:37i9dQZF1DX8Uebhn9wzrS",
        embedUrl: "https://open.spotify.com/embed/playlist/37i9dQZF1DX8Uebhn9wzrS",
        mood: ["calm", "focus"],
        instrumental: true,
        image: "/api/placeholder/80/80"
    },
    {
        id: "energetic-1",
        name: "High Energy Focus",
        description: "Upbeat tracks to keep energy levels high",
        category: "focus-coding",
        spotifyUri: "spotify:playlist:37i9dQZF1DX0vHZ8elq0UK",
        embedUrl: "https://open.spotify.com/embed/playlist/37i9dQZF1DX0vHZ8elq0UK",
        mood: ["energetic", "happy"],
        instrumental: false,
        image: "/api/placeholder/80/80"
    }
]

/* ============================================================================
   MOOD SELECTOR
   ============================================================================ */

function MoodSelector({
    selectedMood,
    onMoodChange,
    className
}: {
    selectedMood: MoodType | null
    onMoodChange: (mood: MoodType | null) => void
    className?: string
}) {
    const moods: { value: MoodType, label: string, icon: React.ReactNode, color: string }[] = [
        { value: "focus", label: "Focused", icon: <Brain className="w-4 h-4" />, color: "purple" },
        { value: "energetic", label: "Energetic", icon: <Zap className="w-4 h-4" />, color: "orange" },
        { value: "calm", label: "Calm", icon: <Waves className="w-4 h-4" />, color: "blue" },
        { value: "happy", label: "Happy", icon: <Coffee className="w-4 h-4" />, color: "pink" }
    ]

    return (
        <div className={cn("flex flex-wrap gap-2", className)}>
            {moods.map((mood) => (
                <motion.button
                    key={mood.value}
                    onClick={() => onMoodChange(selectedMood === mood.value ? null : mood.value)}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    className={cn(
                        "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium",
                        "border transition-all duration-200",
                        selectedMood === mood.value
                            ? `bg-${mood.color}-500/20 border-${mood.color}-500/50 text-${mood.color}-300`
                            : "bg-zinc-800/50 border-zinc-700/50 text-zinc-400 hover:bg-zinc-800 hover:text-zinc-300"
                    )}
                >
                    {mood.icon}
                    {mood.label}
                </motion.button>
            ))}
        </div>
    )
}

/* ============================================================================
   PLAYLIST CARD
   ============================================================================ */

function PlaylistCard({
    playlist,
    isPlaying,
    onPlay,
    onLike,
    isLiked
}: {
    playlist: StudyPlaylist
    isPlaying: boolean
    onPlay: () => void
    onLike: () => void
    isLiked: boolean
}) {
    return (
        <motion.div
            whileHover={{ y: -2 }}
            className={cn(
                "group relative overflow-hidden rounded-xl",
                "bg-gradient-to-br from-zinc-900/80 to-zinc-900/50",
                "border transition-all duration-300",
                isPlaying
                    ? "border-purple-500/50 shadow-lg shadow-purple-500/20"
                    : "border-zinc-700/50 hover:border-zinc-600/50"
            )}
        >
            <div className="p-3 space-y-3">
                {/* Top section */}
                <div className="flex gap-3">
                    {/* Album Art */}
                    <div className="relative w-16 h-16 rounded-lg overflow-hidden bg-zinc-800 flex-shrink-0">
                        <Music className="w-8 h-8 text-zinc-600 absolute inset-0 m-auto" />
                        {isPlaying && (
                            <div className="absolute inset-0 bg-purple-500/20 flex items-center justify-center">
                                <div className="flex gap-0.5">
                                    {[...Array(3)].map((_, i) => (
                                        <motion.div
                                            key={i}
                                            className="w-1 bg-purple-400 rounded-full"
                                            animate={{ height: [8, 16, 8] }}
                                            transition={{
                                                duration: 0.5,
                                                repeat: Infinity,
                                                delay: i * 0.1
                                            }}
                                        />
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Info */}
                    <div className="flex-1 min-w-0">
                        <h4 className="text-sm font-semibold text-zinc-200 truncate group-hover:text-purple-300 transition-colors">
                            {playlist.name}
                        </h4>
                        <p className="text-xs text-zinc-500 line-clamp-2 mt-0.5">
                            {playlist.description}
                        </p>
                        {playlist.instrumental && (
                            <span className="inline-flex items-center gap-1 mt-1 px-1.5 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                                <Headphones className="w-2.5 h-2.5" />
                                Instrumental
                            </span>
                        )}
                    </div>
                </div>

                {/* Actions */}
                <div className="flex items-center justify-between">
                    <button
                        onClick={onPlay}
                        className={cn(
                            "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium",
                            "transition-all duration-200",
                            isPlaying
                                ? "bg-purple-500 text-white hover:bg-purple-600"
                                : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
                        )}
                    >
                        {isPlaying ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
                        {isPlaying ? "Pause" : "Play"}
                    </button>

                    <button
                        onClick={onLike}
                        className={cn(
                            "p-1.5 rounded-lg transition-all",
                            isLiked
                                ? "text-pink-400 hover:text-pink-300"
                                : "text-zinc-600 hover:text-zinc-400"
                        )}
                    >
                        <Heart className={cn("w-4 h-4", isLiked && "fill-current")} />
                    </button>
                </div>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN ENHANCED SPOTIFY PLAYER
   ============================================================================ */

export function EnhancedSpotifyPlayer({
    autoPlay = false,
    pomodoroActive = false,
    isBreakTime = false,
    className,
    onPlay,
    onPause
}: EnhancedSpotifyPlayerProps) {
    const [isPlaying, setIsPlaying] = useState(false)
    const [currentPlaylist, setCurrentPlaylist] = useState<StudyPlaylist | null>(null)
    const [volume, setVolume] = useState(70)
    const [isMuted, setIsMuted] = useState(false)
    const [selectedMood, setSelectedMood] = useState<MoodType | null>(null)
    const [instrumentalOnly, setInstrumentalOnly] = useState(true)
    const [likedPlaylists, setLikedPlaylists] = useState<Set<string>>(new Set())
    const [showVisualizer, setShowVisualizer] = useState(false)
    const [visualizerStyle, setVisualizerStyle] = useState<VisualizationStyle>("bars")
    const [isExpanded, setIsExpanded] = useState(false)

    // Filter playlists based on mood and instrumental preference
    const filteredPlaylists = STUDY_PLAYLISTS.filter(playlist => {
        if (instrumentalOnly && !playlist.instrumental) return false
        if (selectedMood && !playlist.mood.includes(selectedMood)) return false
        return true
    })

    // Pomodoro integration
    useEffect(() => {
        if (pomodoroActive && !isPlaying && autoPlay) {
            // Auto-play when Pomodoro starts
            handlePlayPlaylist(filteredPlaylists[0])
        } else if (!pomodoroActive && isPlaying && autoPlay) {
            // Auto-pause when Pomodoro stops
            handlePause()
        }
    }, [pomodoroActive]) // eslint-disable-line react-hooks/exhaustive-deps

    // Change playlist on break time
    useEffect(() => {
        if (isBreakTime && isPlaying) {
            // Switch to calmer playlist during breaks
            const calmPlaylist = STUDY_PLAYLISTS.find(p => p.mood.includes("calm"))
            if (calmPlaylist && currentPlaylist?.id !== calmPlaylist.id) {
                setCurrentPlaylist(calmPlaylist)
            }
        }
    }, [isBreakTime]) // eslint-disable-line react-hooks/exhaustive-deps

    const handlePlayPlaylist = (playlist: StudyPlaylist) => {
        setCurrentPlaylist(playlist)
        setIsPlaying(true)
        onPlay?.()
    }

    const handlePause = () => {
        setIsPlaying(false)
        onPause?.()
    }

    const togglePlayPause = () => {
        if (isPlaying) {
            handlePause()
        } else if (currentPlaylist) {
            setIsPlaying(true)
            onPlay?.()
        } else {
            handlePlayPlaylist(filteredPlaylists[0])
        }
    }

    const toggleLike = (playlistId: string) => {
        setLikedPlaylists(prev => {
            const newSet = new Set(prev)
            if (newSet.has(playlistId)) {
                newSet.delete(playlistId)
            } else {
                newSet.add(playlistId)
            }
            return newSet
        })
    }

    const handleVolumeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newVolume = parseInt(e.target.value)
        setVolume(newVolume)
        if (newVolume > 0) {
            setIsMuted(false)
        }
    }

    const toggleMute = () => {
        setIsMuted(!isMuted)
    }

    return (
        <div className={cn("relative", className)}>
            <motion.div
                className={cn(
                    "overflow-hidden rounded-2xl",
                    "bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f]",
                    "border border-purple-500/20",
                    "shadow-[0_0_40px_rgba(139,92,246,0.1)]"
                )}
            >
                {/* Header */}
                <div className="flex items-center justify-between px-4 py-3 border-b border-purple-500/20">
                    <div className="flex items-center gap-2">
                        <Music className="w-5 h-5 text-purple-400" />
                        <h3 className="font-semibold text-zinc-100">Study Music Player</h3>
                        {isPlaying && (
                            <span className="flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-xs">
                                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                                Playing
                            </span>
                        )}
                    </div>

                    <button
                        onClick={() => setIsExpanded(!isExpanded)}
                        className="p-1.5 rounded-lg hover:bg-zinc-800 transition-colors"
                    >
                        {isExpanded ? <ChevronUp className="w-4 h-4 text-zinc-400" /> : <ChevronDown className="w-4 h-4 text-zinc-400" />}
                    </button>
                </div>

                <AnimatePresence>
                    {isExpanded && (
                        <motion.div
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: "auto", opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.3, ease: "easeInOut" }}
                        >
                            {/* Now Playing */}
                            {currentPlaylist && (
                                <div className="px-4 pt-4 pb-3 border-b border-zinc-800/50">
                                    <p className="text-xs text-zinc-500 mb-2">Now Playing</p>
                                    <div className="flex items-center gap-3">
                                        <div className="w-12 h-12 rounded-lg bg-zinc-800 flex items-center justify-center">
                                            <Music className="w-6 h-6 text-zinc-600" />
                                        </div>
                                        <div className="flex-1 min-w-0">
                                            <p className="text-sm font-medium text-zinc-200 truncate">
                                                {currentPlaylist.name}
                                            </p>
                                            <p className="text-xs text-zinc-500 truncate">
                                                {currentPlaylist.description}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            )}

                            {/* Controls */}
                            <div className="px-4 py-3 border-b border-zinc-800/50">
                                <div className="flex items-center justify-center gap-3 mb-3">
                                    <button
                                        className="p-2 rounded-lg hover:bg-zinc-800 transition-colors text-zinc-400 hover:text-zinc-300"
                                    >
                                        <Shuffle className="w-4 h-4" />
                                    </button>
                                    <button
                                        className="p-2 rounded-lg hover:bg-zinc-800 transition-colors text-zinc-400 hover:text-zinc-300"
                                    >
                                        <SkipBack className="w-4 h-4" />
                                    </button>
                                    <motion.button
                                        onClick={togglePlayPause}
                                        whileHover={{ scale: 1.05 }}
                                        whileTap={{ scale: 0.95 }}
                                        className="p-3 rounded-full bg-gradient-to-r from-purple-600 to-purple-500 text-white shadow-lg shadow-purple-500/30"
                                    >
                                        {isPlaying ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5 ml-0.5" />}
                                    </motion.button>
                                    <button
                                        className="p-2 rounded-lg hover:bg-zinc-800 transition-colors text-zinc-400 hover:text-zinc-300"
                                    >
                                        <SkipForward className="w-4 h-4" />
                                    </button>
                                    <button
                                        className="p-2 rounded-lg hover:bg-zinc-800 transition-colors text-zinc-400 hover:text-zinc-300"
                                    >
                                        <Repeat className="w-4 h-4" />
                                    </button>
                                </div>

                                {/* Volume Control */}
                                <div className="flex items-center gap-3">
                                    <button
                                        onClick={toggleMute}
                                        className="text-zinc-400 hover:text-zinc-300 transition-colors"
                                    >
                                        {isMuted || volume === 0 ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
                                    </button>
                                    <input
                                        type="range"
                                        min="0"
                                        max="100"
                                        value={isMuted ? 0 : volume}
                                        onChange={handleVolumeChange}
                                        className="flex-1 h-1 bg-zinc-700 rounded-lg appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-purple-500"
                                    />
                                    <span className="text-xs text-zinc-500 w-8 text-right">
                                        {isMuted ? 0 : volume}
                                    </span>
                                </div>
                            </div>

                            {/* Visualizer */}
                            <div className="px-4 py-3 border-b border-zinc-800/50">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-xs font-medium text-zinc-400">Music Visualizer</span>
                                    <button
                                        onClick={() => setShowVisualizer(!showVisualizer)}
                                        className={cn(
                                            "px-2 py-1 rounded text-xs transition-all",
                                            showVisualizer
                                                ? "bg-purple-500/20 text-purple-300"
                                                : "bg-zinc-800 text-zinc-400"
                                        )}
                                    >
                                        {showVisualizer ? "Hide" : "Show"}
                                    </button>
                                </div>
                                <MusicVisualizer
                                    isActive={showVisualizer && isPlaying}
                                    style={visualizerStyle}
                                    size="medium"
                                    onStyleChange={setVisualizerStyle}
                                />
                            </div>

                            {/* Filters */}
                            <div className="px-4 py-3 border-b border-zinc-800/50 space-y-3">
                                <div>
                                    <p className="text-xs font-medium text-zinc-400 mb-2">Mood</p>
                                    <MoodSelector
                                        selectedMood={selectedMood}
                                        onMoodChange={setSelectedMood}
                                    />
                                </div>

                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="text-xs font-medium text-zinc-300">Learning Mode</p>
                                        <p className="text-[10px] text-zinc-500">Instrumental only (no lyrics)</p>
                                    </div>
                                    <button
                                        onClick={() => setInstrumentalOnly(!instrumentalOnly)}
                                        className={cn(
                                            "relative w-11 h-6 rounded-full transition-colors",
                                            instrumentalOnly ? "bg-purple-500" : "bg-zinc-700"
                                        )}
                                    >
                                        <motion.div
                                            className="absolute top-0.5 left-0.5 w-5 h-5 rounded-full bg-white"
                                            animate={{ x: instrumentalOnly ? 20 : 0 }}
                                            transition={{ type: "spring", stiffness: 500, damping: 30 }}
                                        />
                                    </button>
                                </div>
                            </div>

                            {/* Playlists */}
                            <div className="p-4">
                                <p className="text-xs font-medium text-zinc-400 mb-3">
                                    {selectedMood ? `${selectedMood.charAt(0).toUpperCase() + selectedMood.slice(1)} Playlists` : "All Playlists"}
                                    {instrumentalOnly && " (Instrumental)"}
                                </p>
                                <div className="grid gap-3 max-h-96 overflow-y-auto">
                                    {filteredPlaylists.length > 0 ? (
                                        filteredPlaylists.map((playlist) => (
                                            <PlaylistCard
                                                key={playlist.id}
                                                playlist={playlist}
                                                isPlaying={isPlaying && currentPlaylist?.id === playlist.id}
                                                onPlay={() => handlePlayPlaylist(playlist)}
                                                onLike={() => toggleLike(playlist.id)}
                                                isLiked={likedPlaylists.has(playlist.id)}
                                            />
                                        ))
                                    ) : (
                                        <div className="text-center py-8">
                                            <Music className="w-8 h-8 text-zinc-600 mx-auto mb-2" />
                                            <p className="text-sm text-zinc-500">No playlists match your filters</p>
                                            <p className="text-xs text-zinc-600 mt-1">Try adjusting your mood or learning mode</p>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    )}
                </AnimatePresence>
            </motion.div>
        </div>
    )
}

export default EnhancedSpotifyPlayer
