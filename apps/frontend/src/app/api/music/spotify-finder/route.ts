import { NextResponse } from 'next/server'

/**
 * Spotify Track Finder API
 *
 * Uses iTunes Search + Songlink to find Spotify track ID.
 * iTunes is more reliable from Cloudflare Workers than Deezer.
 * Falls back to Spotify Search URI if lookup fails.
 * NO SPOTIFY API KEYS NEEDED!
 *
 * Flow: Track name → iTunes → Songlink → Spotify URI
 * Fallback: Spotify Search URI (always works)
 */

// Cache for track lookups (1 hour)
const trackCache = new Map<string, { spotifyId: string | null; timestamp: number }>()
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
        if (cached.spotifyId) {
            return NextResponse.json({
                spotifyId: cached.spotifyId,
                embedUrl: `https://open.spotify.com/embed/track/${cached.spotifyId}?utm_source=generator&theme=0`,
                spotifyUrl: `https://open.spotify.com/track/${cached.spotifyId}`,
                spotifyUri: `spotify:track:${cached.spotifyId}`,
                cached: true
            })
        }
    }

    try {
        // Step 1: Search iTunes for track
        const query = encodeURIComponent(`${track} ${artist}`)
        
        const itunesRes = await fetch(
            `https://itunes.apple.com/search?term=${query}&media=music&limit=1`,
            { 
                headers: { 'Accept': 'application/json' }
            }
        )

        if (!itunesRes.ok) {
            console.error('[Spotify Finder] iTunes failed:', itunesRes.status)
            return createSearchFallback(track, artist)
        }

        const itunesData = await itunesRes.json()

        if (!itunesData.results || itunesData.results.length === 0) {
            console.warn('[Spotify Finder] Track not found on iTunes')
            return createSearchFallback(track, artist)
        }

        const itunesTrackId = itunesData.results[0].trackId

        // Step 2: Use Songlink to get Spotify ID
        // Using song.link/i/ format which works better
        const songlinkUrl = `https://api.song.link/v1-alpha.1/links?url=https%3A%2F%2Fsong.link%2Fi%2F${itunesTrackId}`
        const songlinkRes = await fetch(songlinkUrl, {
            headers: { 'Accept': 'application/json' }
        })

        if (!songlinkRes.ok) {
            console.error('[Spotify Finder] Songlink failed:', songlinkRes.status)
            return createSearchFallback(track, artist)
        }

        const songlinkData = await songlinkRes.json()

        // Extract Spotify ID
        const spotifyEntity = songlinkData.linksByPlatform?.spotify
        if (!spotifyEntity) {
            console.warn('[Spotify Finder] No Spotify link in Songlink response')
            return createSearchFallback(track, artist)
        }

        // Get the native URI directly from Songlink response
        const spotifyUri = spotifyEntity.nativeAppUriDesktop
        const spotifyUrl = spotifyEntity.url
        
        // Extract ID from entityUniqueId or URI
        const spotifyId = spotifyEntity.entityUniqueId?.split('::')[1] || 
                          spotifyUri?.replace('spotify:track:', '') ||
                          spotifyUrl?.split('/track/')[1]

        if (!spotifyId) {
            return createSearchFallback(track, artist)
        }

        // Cache result
        trackCache.set(cacheKey, { spotifyId, timestamp: Date.now() })


        return NextResponse.json({
            spotifyId,
            embedUrl: `https://open.spotify.com/embed/track/${spotifyId}?utm_source=generator&theme=0`,
            spotifyUrl: spotifyUrl || `https://open.spotify.com/track/${spotifyId}`,
            spotifyUri: spotifyUri || `spotify:track:${spotifyId}`,
            cached: false,
            method: 'itunes-songlink'
        })

    } catch (error) {
        console.error('[Spotify Finder] Error:', error)
        return createSearchFallback(track, artist)
    }
}

/**
 * Fallback: Create a Spotify search embed URL
 * This always works - opens Spotify search for the track
 */
function createSearchFallback(track: string, artist: string) {
    const searchQuery = encodeURIComponent(`${track} ${artist}`)
    
    return NextResponse.json({
        spotifyId: null,
        // Spotify search embed - always works!
        embedUrl: `https://open.spotify.com/embed/search/${searchQuery}?utm_source=generator&theme=0`,
        spotifyUrl: `https://open.spotify.com/search/${searchQuery}`,
        // Search URI opens Spotify app with search query - will show search results
        spotifyUri: `spotify:search:${track} ${artist}`,
        cached: false,
        method: 'search-fallback'
    })
}
