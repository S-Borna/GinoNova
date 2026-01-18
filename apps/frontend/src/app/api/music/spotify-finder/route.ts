import { NextResponse } from 'next/server'

/**
 * Spotify Track Finder API
 *
 * Uses Deezer + Songlink to find Spotify track ID.
 * NO SPOTIFY API KEYS NEEDED!
 *
 * Flow: Track name → Deezer → Songlink → Spotify embed URL
 */

// Cache for track lookups (1 hour)
const trackCache = new Map<string, { spotifyId: string; timestamp: number }>()
const CACHE_DURATION = 60 * 60 * 1000

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
        return NextResponse.json({
            spotifyId: cached.spotifyId,
            embedUrl: `https://open.spotify.com/embed/track/${cached.spotifyId}?utm_source=generator&theme=0`,
            spotifyUrl: `https://open.spotify.com/track/${cached.spotifyId}`,
            spotifyUri: `spotify:track:${cached.spotifyId}`,
            cached: true
        })
    }

    try {
        // Step 1: Search Deezer for track ID
        const query = encodeURIComponent(`${track} ${artist}`)
        const deezerRes = await fetch(`https://api.deezer.com/search?q=${query}&limit=1`)

        if (!deezerRes.ok) {
            throw new Error('Deezer search failed')
        }

        const deezerData = await deezerRes.json()

        if (!deezerData.data || deezerData.data.length === 0) {
            return NextResponse.json({ error: 'Track not found on Deezer' }, { status: 404 })
        }

        const deezerId = deezerData.data[0].id

        // Step 2: Use Songlink to get Spotify ID
        const songlinkUrl = `https://api.song.link/v1-alpha.1/links?url=https%3A%2F%2Fdeezer.com%2Ftrack%2F${deezerId}`
        const songlinkRes = await fetch(songlinkUrl)

        if (!songlinkRes.ok) {
            throw new Error('Songlink lookup failed')
        }

        const songlinkData = await songlinkRes.json()

        // Extract Spotify ID
        const spotifyEntity = songlinkData.linksByPlatform?.spotify
        if (!spotifyEntity) {
            return NextResponse.json({ error: 'Track not found on Spotify' }, { status: 404 })
        }

        // Extract ID from entityUniqueId like "SPOTIFY_SONG::47EiUVwUp4C9fGccaPuUCS"
        const spotifyUniqueId = spotifyEntity.entityUniqueId
        const spotifyId = spotifyUniqueId?.split('::')[1] || spotifyEntity.url?.split('/track/')[1]

        if (!spotifyId) {
            return NextResponse.json({ error: 'Could not extract Spotify ID' }, { status: 404 })
        }

        // Cache result
        trackCache.set(cacheKey, { spotifyId, timestamp: Date.now() })

        return NextResponse.json({
            spotifyId,
            embedUrl: `https://open.spotify.com/embed/track/${spotifyId}?utm_source=generator&theme=0`,
            spotifyUrl: `https://open.spotify.com/track/${spotifyId}`,
            spotifyUri: `spotify:track:${spotifyId}`,
            cached: false
        })

    } catch (error) {
        console.error('[Spotify Finder] Error:', error)
        return NextResponse.json({
            error: 'Failed to find track',
            details: error instanceof Error ? error.message : 'Unknown'
        }, { status: 500 })
    }
}
