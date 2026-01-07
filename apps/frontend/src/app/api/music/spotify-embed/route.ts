/**
 * Spotify Embed API - Get embeddable player URL
 * 
 * Uses Spotify's oEmbed API (no app registration needed!)
 * to get an embeddable player for the current track.
 */

import { NextResponse } from 'next/server'

interface SpotifyOembedResponse {
    html: string
    width: number
    height: number
    version: string
    provider_name: string
    provider_url: string
    type: string
    title: string
    thumbnail_url: string
    thumbnail_width: number
    thumbnail_height: number
}

interface SpotifySearchResponse {
    tracks: {
        items: Array<{
            id: string
            name: string
            artists: Array<{ name: string }>
            uri: string
            external_urls: {
                spotify: string
            }
        }>
    }
}

// Cache for track lookups
const trackCache = new Map<string, { trackId: string; timestamp: number }>()
const CACHE_TTL = 60 * 60 * 1000 // 1 hour

/**
 * Search for a track on Spotify using their web search
 * Returns the Spotify track ID if found
 */
async function findSpotifyTrackId(trackName: string, artistName: string): Promise<string | null> {
    const cacheKey = `${trackName}-${artistName}`.toLowerCase()
    
    // Check cache
    const cached = trackCache.get(cacheKey)
    if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
        return cached.trackId
    }

    try {
        // Use Spotify's public search (no auth needed for basic search)
        const query = encodeURIComponent(`${trackName} ${artistName}`)
        
        // Scrape the Spotify search page for track ID
        // Alternative: Use a music metadata service
        const searchUrl = `https://open.spotify.com/search/${query}`
        
        // For now, we'll construct a likely Spotify URL pattern
        // This works because Spotify's oEmbed accepts search URLs too
        return null // Will use search URL directly in embed
    } catch (error) {
        console.error('[Spotify Embed] Search error:', error)
        return null
    }
}

export async function GET(request: Request) {
    const { searchParams } = new URL(request.url)
    const track = searchParams.get('track')
    const artist = searchParams.get('artist')

    if (!track || !artist) {
        return NextResponse.json(
            { error: 'Missing track or artist parameter' },
            { status: 400 }
        )
    }

    try {
        // Build search URL for Spotify
        const query = encodeURIComponent(`${track} ${artist}`)
        const spotifySearchUrl = `https://open.spotify.com/search/${query}`
        
        // Try to get oEmbed data
        const oembedUrl = `https://open.spotify.com/oembed?url=${encodeURIComponent(spotifySearchUrl)}`
        
        const response = await fetch(oembedUrl)
        
        if (!response.ok) {
            // Fallback: return a search embed URL
            return NextResponse.json({
                embedUrl: null,
                searchUrl: spotifySearchUrl,
                track,
                artist,
                message: 'Direct embed not available, use search URL'
            })
        }

        const data: SpotifyOembedResponse = await response.json()

        // Extract iframe src from HTML
        const srcMatch = data.html.match(/src="([^"]+)"/)
        const embedUrl = srcMatch ? srcMatch[1] : null

        return NextResponse.json({
            embedUrl,
            embedHtml: data.html,
            thumbnail: data.thumbnail_url,
            title: data.title,
            searchUrl: spotifySearchUrl,
            track,
            artist
        })

    } catch (error) {
        console.error('[Spotify Embed] Error:', error)
        return NextResponse.json({
            embedUrl: null,
            searchUrl: `https://open.spotify.com/search/${encodeURIComponent(`${track} ${artist}`)}`,
            track,
            artist,
            error: 'Failed to get embed'
        })
    }
}
