import { NextResponse } from 'next/server'

/**
 * Deezer Track Search API
 * 
 * Searches for tracks and returns preview URL for playback.
 * Deezer API is FREE - NO API KEY NEEDED!
 */

// Cache for track lookups (1 hour)
const trackCache = new Map<string, { data: DeezerTrack; timestamp: number }>()
const CACHE_DURATION = 60 * 60 * 1000

interface DeezerTrack {
    id: number
    title: string
    artist: string
    album: string
    albumArt: string
    previewUrl: string // 30-second preview MP3
    deezerUrl: string
}

export async function GET(request: Request) {
    const { searchParams } = new URL(request.url)
    const track = searchParams.get('track')
    const artist = searchParams.get('artist')

    if (!track || !artist) {
        return NextResponse.json({ error: 'Missing track or artist' }, { status: 400 })
    }

    const cacheKey = `${track}-${artist}`.toLowerCase()
    
    // Check cache
    const cached = trackCache.get(cacheKey)
    if (cached && Date.now() - cached.timestamp < CACHE_DURATION) {
        return NextResponse.json({ track: cached.data, cached: true })
    }

    try {
        const query = encodeURIComponent(`${track} ${artist}`)
        const response = await fetch(`https://api.deezer.com/search?q=${query}&limit=1`, {
            headers: { 'Accept': 'application/json' }
        })

        if (!response.ok) {
            throw new Error(`Deezer API error: ${response.status}`)
        }

        const data = await response.json()
        
        if (data.data && data.data.length > 0) {
            const result = data.data[0]
            const trackData: DeezerTrack = {
                id: result.id,
                title: result.title,
                artist: result.artist?.name || artist,
                album: result.album?.title || '',
                albumArt: result.album?.cover_big || result.album?.cover_medium || '',
                previewUrl: result.preview, // 30-second MP3 preview
                deezerUrl: result.link
            }

            // Cache result
            trackCache.set(cacheKey, { data: trackData, timestamp: Date.now() })

            return NextResponse.json({ track: trackData, cached: false })
        }

        return NextResponse.json({ track: null, error: 'No results found' })

    } catch (error) {
        console.error('[Deezer API] Error:', error)
        return NextResponse.json({ 
            error: 'Failed to search',
            details: error instanceof Error ? error.message : 'Unknown'
        }, { status: 500 })
    }
}
