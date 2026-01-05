/**
 * Music Now Playing API - Pure Last.fm
 *
 * Uses Last.fm scrobbles to show currently playing music.
 * No Spotify API needed! Just Last.fm API key (free, always available).
 */

import { NextResponse } from 'next/server'

/* ============================================================================
   TYPES
   ============================================================================ */

interface LastFmTrack {
    name: string
    artist: {
        '#text': string
        mbid?: string
    }
    album: {
        '#text': string
        mbid?: string
    }
    image: Array<{
        '#text': string
        size: string
    }>
    url: string
    date?: {
        uts: string
        '#text': string
    }
    '@attr'?: {
        nowplaying: string
    }
}

interface LastFmResponse {
    recenttracks: {
        track: LastFmTrack[]
        '@attr': {
            user: string
            totalPages: string
            page: string
            perPage: string
            total: string
        }
    }
}

export interface NowPlayingResponse {
    isPlaying: boolean
    track: {
        name: string
        artist: string
        album: string
        albumArt: string | null
        spotifyUrl: string
        lastFmUrl: string
        playedAt?: number
    } | null
    timestamp: number
    source: 'lastfm' | 'cache' | 'none'
}

/* ============================================================================
   CACHE
   ============================================================================ */

interface CachedData {
    data: NowPlayingResponse
    cachedAt: number
}

let cache: CachedData | null = null
const CACHE_TTL = 15 * 1000 // 15 seconds - faster updates!

/* ============================================================================
   LAST.FM API
   ============================================================================ */

async function getLastFmCurrentTrack(): Promise<{
    track: LastFmTrack | null
    isPlaying: boolean
}> {
    const apiKey = process.env.LASTFM_API_KEY
    const username = process.env.LASTFM_USERNAME

    if (!apiKey || !username) {
        console.warn('[Last.fm] Missing LASTFM_API_KEY or LASTFM_USERNAME')
        return { track: null, isPlaying: false }
    }

    try {
        const url = new URL('http://ws.audioscrobbler.com/2.0/')
        url.searchParams.set('method', 'user.getrecenttracks')
        url.searchParams.set('user', username)
        url.searchParams.set('api_key', apiKey)
        url.searchParams.set('format', 'json')
        url.searchParams.set('limit', '1')

        const response = await fetch(url.toString(), {
            next: { revalidate: 0 },
        })

        if (!response.ok) {
            console.error('[Last.fm] API error:', response.status)
            return { track: null, isPlaying: false }
        }

        const data: LastFmResponse = await response.json()

        if (!data.recenttracks?.track?.length) {
            return { track: null, isPlaying: false }
        }

        const track = data.recenttracks.track[0]
        const isPlaying = track['@attr']?.nowplaying === 'true'

        return { track, isPlaying }

    } catch (error) {
        console.error('[Last.fm] Error fetching track:', error)
        return { track: null, isPlaying: false }
    }
}

/* ============================================================================
   GET BEST ALBUM ART
   ============================================================================ */

function getBestAlbumArt(images: LastFmTrack['image']): string | null {
    if (!images?.length) return null

    // Get largest available (extralarge > large > medium > small)
    const extralarge = images.find(img => img.size === 'extralarge')
    const large = images.find(img => img.size === 'large')
    const medium = images.find(img => img.size === 'medium')

    const url = extralarge?.['#text'] || large?.['#text'] || medium?.['#text']

    // Last.fm returns empty string for missing images
    return url && url.length > 0 ? url : null
}

/* ============================================================================
   MAIN API HANDLER
   ============================================================================ */

export async function GET() {
    const now = Date.now()

    // Check cache first
    if (cache && (now - cache.cachedAt) < CACHE_TTL) {
        return NextResponse.json(cache.data, {
            headers: {
                'Cache-Control': 'public, s-maxage=15, stale-while-revalidate=30',
                'X-Cache': 'HIT',
            },
        })
    }

    // Fetch from Last.fm
    const { track: lastFmTrack, isPlaying } = await getLastFmCurrentTrack()

    if (!lastFmTrack) {
        const response: NowPlayingResponse = {
            isPlaying: false,
            track: null,
            timestamp: now,
            source: 'none',
        }

        cache = { data: response, cachedAt: now }

        return NextResponse.json(response, {
            headers: {
                'Cache-Control': 'public, s-maxage=15, stale-while-revalidate=30',
                'X-Cache': 'MISS',
            },
        })
    }

    // Build Spotify search URL (opens in Spotify app/web)
    const trackName = lastFmTrack.name
    const artistName = lastFmTrack.artist['#text']
    const spotifySearchQuery = encodeURIComponent(`${trackName} ${artistName}`)
    const spotifyUrl = `https://open.spotify.com/search/${spotifySearchQuery}`

    // Build response
    const response: NowPlayingResponse = {
        isPlaying,
        track: {
            name: trackName,
            artist: artistName,
            album: lastFmTrack.album['#text'],
            albumArt: getBestAlbumArt(lastFmTrack.image),
            spotifyUrl,
            lastFmUrl: lastFmTrack.url,
            playedAt: lastFmTrack.date ? parseInt(lastFmTrack.date.uts) * 1000 : undefined,
        },
        timestamp: now,
        source: 'lastfm',
    }

    cache = { data: response, cachedAt: now }

    return NextResponse.json(response, {
        headers: {
            'Cache-Control': 'public, s-maxage=15, stale-while-revalidate=30',
            'X-Cache': 'MISS',
        },
    })
}
