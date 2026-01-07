import { NextResponse } from 'next/server'

/**
 * Spotify Track Search API
 * 
 * Searches Spotify and returns the track ID for embedding.
 * Uses web scraping - NO API KEYS NEEDED!
 */

// Cache for track lookups (1 hour)
const trackCache = new Map<string, { trackId: string; timestamp: number }>()
const CACHE_DURATION = 60 * 60 * 1000 // 1 hour

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
        const embedUrl = `https://open.spotify.com/embed/track/${cached.trackId}?utm_source=oembed&theme=0`
        return NextResponse.json({ 
            trackId: cached.trackId,
            embedUrl,
            cached: true 
        })
    }

    try {
        // Search Spotify web (no API needed)
        const query = encodeURIComponent(`${track} ${artist}`)
        const searchUrl = `https://open.spotify.com/search/${query}`
        
        const response = await fetch(searchUrl, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml',
            }
        })

        if (!response.ok) {
            throw new Error(`Spotify search failed: ${response.status}`)
        }

        const html = await response.text()
        
        // Extract track ID from the HTML - look for track links
        // Pattern: /track/[alphanumeric ID]
        const trackMatch = html.match(/\/track\/([a-zA-Z0-9]{22})/)
        
        if (trackMatch && trackMatch[1]) {
            const trackId = trackMatch[1]
            
            // Cache the result
            trackCache.set(cacheKey, { trackId, timestamp: Date.now() })
            
            const embedUrl = `https://open.spotify.com/embed/track/${trackId}?utm_source=oembed&theme=0`
            
            return NextResponse.json({ 
                trackId,
                embedUrl,
                cached: false
            })
        }

        // Fallback: return search URL (user opens manually)
        return NextResponse.json({ 
            trackId: null,
            embedUrl: null,
            searchUrl: `https://open.spotify.com/search/${query}`,
            error: 'Track ID not found in search results'
        })

    } catch (error) {
        console.error('[Spotify Search] Error:', error)
        return NextResponse.json({ 
            error: 'Failed to search Spotify',
            details: error instanceof Error ? error.message : 'Unknown error'
        }, { status: 500 })
    }
}
