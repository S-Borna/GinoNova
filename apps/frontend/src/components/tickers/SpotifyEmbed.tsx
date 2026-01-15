'use client'

/**
 * Now Playing Widget - Pure Last.fm
 *
 * Shows currently playing music using Last.fm scrobbles.
 * No Spotify API needed! Beautiful custom design.
 *
 * Features:
 * - Auto-refresh every 15 seconds
 * - Smooth animations
 * - NOW PLAYING / Last played status
 * - Album art with vinyl effect
 * - Click to open in Last.fm
 */

import * as React from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Music2, ExternalLink, WifiOff, Radio, Disc3 } from 'lucide-react'
import { cn } from '@/lib/utils'
import type { NowPlayingResponse } from '@/app/api/music/now-playing/route'

/* ============================================================================
   TYPES
   ============================================================================ */

interface NowPlayingWidgetProps {
  /** Widget variant */
  variant?: 'compact' | 'full' | 'mini'
  /** Additional CSS classes */
  className?: string
  /** Polling interval in ms (default: 15000) */
  pollInterval?: number
}

/* ============================================================================
   HELPER: Time ago
   ============================================================================ */

function timeAgo(timestamp: number): string {
  const seconds = Math.floor((Date.now() - timestamp) / 1000)

  if (seconds < 60) return 'just nu'
  if (seconds < 120) return '1 min sedan'
  if (seconds < 3600) return `${Math.floor(seconds / 60)} min sedan`
  if (seconds < 7200) return '1 timme sedan'
  if (seconds < 86400) return `${Math.floor(seconds / 3600)} timmar sedan`
  return 'ett tag sedan'
}

/* ============================================================================
   SKELETON LOADER
   ============================================================================ */

function SkeletonLoader({ variant }: { variant: NowPlayingWidgetProps['variant'] }) {
  if (variant === 'mini') {
    return (
      <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-900/80 animate-pulse">
        <div className="w-8 h-8 rounded bg-zinc-800" />
        <div className="flex flex-col gap-1">
          <div className="w-20 h-3 rounded bg-zinc-800" />
          <div className="w-14 h-2 rounded bg-zinc-800" />
        </div>
      </div>
    )
  }

  return (
    <div className="rounded-xl bg-zinc-900/90 border border-zinc-800 overflow-hidden animate-pulse p-4">
      <div className="flex items-center gap-4">
        <div className="w-16 h-16 rounded-lg bg-zinc-800" />
        <div className="flex-1 space-y-2">
          <div className="w-32 h-4 rounded bg-zinc-800" />
          <div className="w-24 h-3 rounded bg-zinc-800" />
          <div className="w-20 h-3 rounded bg-zinc-800" />
        </div>
      </div>
    </div>
  )
}

/* ============================================================================
   ERROR STATE
   ============================================================================ */

function ErrorState({ variant }: { variant: NowPlayingWidgetProps['variant'] }) {
  if (variant === 'mini') {
    return (
      <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-900/60 text-zinc-500">
        <WifiOff className="w-4 h-4" />
        <span className="text-xs">Offline</span>
      </div>
    )
  }

  return (
    <div className="rounded-xl bg-zinc-900/90 border border-zinc-800 p-6 text-center">
      <WifiOff className="w-8 h-8 text-zinc-600 mx-auto mb-2" />
      <p className="text-sm text-zinc-500">Musik ej tillgänglig</p>
    </div>
  )
}

/* ============================================================================
   EMPTY STATE
   ============================================================================ */

function EmptyState({ variant }: { variant: NowPlayingWidgetProps['variant'] }) {
  if (variant === 'mini') {
    return (
      <div className="flex items-center gap-2 px-3 py-2 rounded-xl bg-zinc-900/60 text-zinc-500">
        <Music2 className="w-4 h-4" />
        <span className="text-xs">Inget spelas</span>
      </div>
    )
  }

  return (
    <div className="rounded-xl bg-zinc-900/90 border border-zinc-800 p-6 text-center">
      <Music2 className="w-8 h-8 text-zinc-600 mx-auto mb-2" />
      <p className="text-sm text-zinc-500">Inget spelas just nu</p>
      <p className="text-xs text-zinc-600 mt-1">Starta Spotify så syns det här!</p>
    </div>
  )
}

/* ============================================================================
   SPINNING VINYL (for album art)
   ============================================================================ */

function SpinningVinyl({
  albumArt,
  isPlaying,
  size = 64
}: {
  albumArt: string | null
  isPlaying: boolean
  size?: number
}) {
  return (
    <div className="relative" style={{ width: size, height: size }}>
      {/* Vinyl disc background */}
      <motion.div
        className="absolute inset-0 rounded-full bg-gradient-to-br from-zinc-800 to-zinc-900 border border-zinc-700"
        animate={isPlaying ? { rotate: 360 } : { rotate: 0 }}
        transition={isPlaying ? {
          duration: 3,
          repeat: Infinity,
          ease: "linear"
        } : { duration: 0.3 }}
      >
        {/* Vinyl grooves */}
        <div className="absolute inset-2 rounded-full border border-zinc-600/30" />
        <div className="absolute inset-4 rounded-full border border-zinc-600/20" />
        <div className="absolute inset-6 rounded-full border border-zinc-600/10" />
      </motion.div>

      {/* Album art center */}
      <div
        className="absolute rounded-full overflow-hidden shadow-lg"
        style={{
          inset: size * 0.15,
        }}
      >
        {albumArt ? (
          <img
            src={albumArt}
            alt="Album art"
            className="w-full h-full object-cover"
          />
        ) : (
          <div className="w-full h-full bg-gradient-to-br from-emerald-600 to-emerald-800 flex items-center justify-center">
            <Music2 className="w-1/2 h-1/2 text-white/60" />
          </div>
        )}
      </div>

      {/* Center hole */}
      <div
        className="absolute rounded-full bg-zinc-900 border border-zinc-700"
        style={{
          width: size * 0.12,
          height: size * 0.12,
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)'
        }}
      />
    </div>
  )
}

/* ============================================================================
   EQUALIZER BARS (animated)
   ============================================================================ */

function EqualizerBars({ isPlaying }: { isPlaying: boolean }) {
  return (
    <div className="npw-eq flex items-end gap-0.5 h-4">
      {[0, 0.2, 0.1, 0.3, 0.15].map((delay, i) => (
        <motion.div
          key={i}
          className="w-1 bg-emerald-500 rounded-full"
          animate={isPlaying ? {
            height: ['4px', '16px', '8px', '14px', '4px'],
          } : { height: '4px' }}
          transition={isPlaying ? {
            duration: 0.8,
            repeat: Infinity,
            delay,
            ease: "easeInOut"
          } : { duration: 0.2 }}
        />
      ))}
    </div>
  )
}

/* ============================================================================
   MINI VARIANT (for TopBar)
   ============================================================================ */

function MiniWidget({
  data,
  className
}: {
  data: NowPlayingResponse
  className?: string
}) {
  const track = data.track

  if (!track) {
    return <EmptyState variant="mini" />
  }

  return (
    <motion.a
      href={track.spotifyUrl}
      target="_blank"
      rel="noopener noreferrer"
      className={cn(
        "flex items-center gap-2 px-3 py-1.5 rounded-xl",
        "bg-zinc-900/80 hover:bg-zinc-800/90",
        "border border-zinc-800/50 hover:border-emerald-500/30",
        "transition-all duration-300 group cursor-pointer",
        className
      )}
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
    >
      {/* Album art */}
      {track.albumArt ? (
        <img
          src={track.albumArt}
          alt={track.album}
          className="w-8 h-8 rounded object-cover"
        />
      ) : (
        <div className="w-8 h-8 rounded bg-zinc-800 flex items-center justify-center">
          <Music2 className="w-4 h-4 text-zinc-500" />
        </div>
      )}

      {/* Track info */}
      <div className="npw-track flex flex-col min-w-0 max-w-[120px]">
        <span className="text-xs font-medium text-white truncate">
          {track.name}
        </span>
        <span className="text-[10px] text-zinc-400 truncate">
          {track.artist}
        </span>
      </div>

      {/* Now playing indicator */}
      {data.isPlaying && <EqualizerBars isPlaying={true} />}
    </motion.a>
  )
}

/* ============================================================================
   COMPACT VARIANT (for widgets/sidebar)
   ============================================================================ */

function CompactWidget({
  data,
  className
}: {
  data: NowPlayingResponse
  className?: string
}) {
  const track = data.track

  if (!track) {
    return <EmptyState variant="compact" />
  }

  return (
    <motion.a
      href={track.spotifyUrl}
      target="_blank"
      rel="noopener noreferrer"
      className={cn(
        "block rounded-xl bg-gradient-to-br from-zinc-900 to-zinc-950",
        "border border-zinc-800 overflow-hidden",
        "hover:border-emerald-500/40 transition-all duration-500",
        "group cursor-pointer",
        className
      )}
      whileHover={{ scale: 1.01 }}
    >
      {/* Status header */}
      <div className="px-4 py-2.5 flex items-center justify-between border-b border-zinc-800/50 bg-black/30">
        <div className="flex items-center gap-2">
          {data.isPlaying ? (
            <>
              <Radio className="w-4 h-4 text-emerald-400" />
              <span className="text-xs font-medium text-emerald-400">SPELAR NU</span>
              <EqualizerBars isPlaying={true} />
            </>
          ) : (
            <>
              <Disc3 className="w-4 h-4 text-zinc-500" />
              <span className="text-xs text-zinc-500">
                Senast spelat {track.playedAt ? timeAgo(track.playedAt) : ''}
              </span>
            </>
          )}
        </div>

        <ExternalLink className="w-3.5 h-3.5 text-zinc-600 group-hover:text-zinc-400 transition-colors" />
      </div>

      {/* Track content */}
      <div className="p-4 flex items-center gap-4">
        <SpinningVinyl
          albumArt={track.albumArt}
          isPlaying={data.isPlaying}
          size={72}
        />

        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-white truncate group-hover:text-emerald-400 transition-colors">
            {track.name}
          </h3>
          <p className="text-sm text-zinc-400 truncate">
            {track.artist}
          </p>
          <p className="text-xs text-zinc-500 truncate mt-0.5">
            {track.album}
          </p>
        </div>
      </div>
    </motion.a>
  )
}

/* ============================================================================
   FULL VARIANT (for dedicated sections)
   ============================================================================ */

function FullWidget({
  data,
  className
}: {
  data: NowPlayingResponse
  className?: string
}) {
  const track = data.track

  if (!track) {
    return <EmptyState variant="full" />
  }

  return (
    <motion.a
      href={track.spotifyUrl}
      target="_blank"
      rel="noopener noreferrer"
      className={cn(
        "block rounded-2xl bg-gradient-to-br from-zinc-900 via-zinc-900 to-emerald-950/20",
        "border border-zinc-800 overflow-hidden shadow-xl",
        "hover:border-emerald-500/40 transition-all duration-500",
        "group cursor-pointer",
        className
      )}
    >
      {/* Header */}
      <div className="px-5 py-3 flex items-center justify-between bg-black/40 backdrop-blur border-b border-zinc-800/50">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-emerald-500/20 flex items-center justify-center">
            <Music2 className="w-4 h-4 text-emerald-400" />
          </div>
          {data.isPlaying ? (
            <div className="flex items-center gap-2">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
                <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500" />
              </span>
              <span className="text-sm font-medium text-emerald-400">SPELAR NU</span>
            </div>
          ) : (
            <span className="text-sm text-zinc-500">
              Senast spelat {track.playedAt ? timeAgo(track.playedAt) : ''}
            </span>
          )}
        </div>

        <div className="flex items-center gap-2 text-xs text-zinc-500 group-hover:text-white transition-colors">
          <span>Öppna i Last.fm</span>
          <ExternalLink className="w-3.5 h-3.5" />
        </div>
      </div>

      {/* Content */}
      <div className="p-6 flex flex-col items-center text-center">
        <SpinningVinyl
          albumArt={track.albumArt}
          isPlaying={data.isPlaying}
          size={160}
        />

        <div className="mt-5 w-full max-w-xs">
          <h3 className="text-xl font-bold text-white truncate group-hover:text-emerald-400 transition-colors">
            {track.name}
          </h3>
          <p className="text-zinc-400 truncate mt-1">
            {track.artist}
          </p>
          <p className="text-sm text-zinc-500 truncate mt-0.5">
            {track.album}
          </p>
        </div>

        {data.isPlaying && (
          <div className="mt-4 flex justify-center">
            <EqualizerBars isPlaying={true} />
          </div>
        )}
      </div>
    </motion.a>
  )
}

/* ============================================================================
   MAIN COMPONENT
   ============================================================================ */

export function NowPlayingWidget({
  variant = 'compact',
  className,
  pollInterval = 15000,
}: NowPlayingWidgetProps) {
  const [data, setData] = React.useState<NowPlayingResponse | null>(null)
  const [isLoading, setIsLoading] = React.useState(true)
  const [error, setError] = React.useState(false)

  // Fetch data
  const fetchData = React.useCallback(async () => {
    try {
      const response = await fetch('/api/music/now-playing')

      if (!response.ok) {
        throw new Error('Failed to fetch')
      }

      const result: NowPlayingResponse = await response.json()
      setData(result)
      setError(false)
    } catch (err) {
      console.error('[NowPlaying] Fetch error:', err)
      setError(true)
    } finally {
      setIsLoading(false)
    }
  }, [])

  // Initial fetch + polling
  React.useEffect(() => {
    fetchData()

    const interval = setInterval(fetchData, pollInterval)
    return () => clearInterval(interval)
  }, [fetchData, pollInterval])

  // Loading state
  if (isLoading) {
    return <SkeletonLoader variant={variant} />
  }

  // Error state
  if (error) {
    return <ErrorState variant={variant} />
  }

  // No data
  if (!data) {
    return <EmptyState variant={variant} />
  }

  // Render appropriate variant with animation
  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={data.track?.name || 'no-track'}
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -10 }}
        transition={{ duration: 0.3 }}
      >
        {variant === 'mini' && <MiniWidget data={data} className={className} />}
        {variant === 'compact' && <CompactWidget data={data} className={className} />}
        {variant === 'full' && <FullWidget data={data} className={className} />}
      </motion.div>
    </AnimatePresence>
  )
}

// Export as both names for backwards compat
export { NowPlayingWidget as SpotifyEmbed }
export default NowPlayingWidget
