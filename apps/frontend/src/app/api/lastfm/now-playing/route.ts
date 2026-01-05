/**
 * Last.fm Now Playing API Route
 * 
 * Fetches currently playing/recent track from Last.fm
 * Works automatically if you have Last.fm connected to Spotify!
 * 
 * Requires environment variables:
 * - LASTFM_API_KEY (get free at https://www.last.fm/api/account/create)
 * - LASTFM_USERNAME (your Last.fm username)
 */

import { NextResponse } from 'next/server'

const LASTFM_API_URL = 'https://ws.audioscrobbler.com/2.0/'

const api_key = process.env.LASTFM_API_KEY
const username = process.env.LASTFM_USERNAME

export async function GET() {
    // Check if Last.fm is configured
    if (!api_key || !username) {
        return NextResponse.json(
            { isPlaying: false, error: 'Last.fm not configured' },
            { status: 200 }
        )
    }

    try {
        const params = new URLSearchParams({
            method: 'user.getrecenttracks',
            user: username,
            api_key: api_key,
            format: 'json',
            limit: '1',
        })

        const response = await fetch(`${LASTFM_API_URL}?${params}`, {
            cache: 'no-store', // Never cache - always fetch fresh data
        })

        if (!response.ok) {
            return NextResponse.json({ isPlaying: false })
        }

        const data = await response.json()

        // Check if there are any tracks
        const tracks = data.recenttracks?.track
        if (!tracks || tracks.length === 0) {
            return NextResponse.json({ isPlaying: false })
        }

        const track = tracks[0]
        
        // Check if currently playing (has @attr.nowplaying)
        const isPlaying = track['@attr']?.nowplaying === 'true'

        // Get album art - Last.fm provides multiple sizes
        const images = track.image || []
        const albumImageUrl = images.find((img: any) => img.size === 'extralarge')?.['#text'] 
            || images.find((img: any) => img.size === 'large')?.['#text']
            || images[images.length - 1]?.['#text']
            || ''

        return NextResponse.json({
            isPlaying,
            title: track.name || 'Unknown',
            artist: track.artist?.['#text'] || track.artist?.name || 'Unknown',
            album: track.album?.['#text'] || '',
            albumImageUrl,
            songUrl: track.url || `https://www.last.fm/music/${encodeURIComponent(track.artist?.['#text'] || '')}/_/${encodeURIComponent(track.name || '')}`,
            // Last.fm doesn't provide progress, but we can show it's live
            progressMs: 0,
            durationMs: 0,
            source: 'lastfm',
            scrobbledAt: isPlaying ? null : track.date?.uts ? parseInt(track.date.uts) * 1000 : null,
        })
    } catch (error) {
        console.error('Last.fm API error:', error)
        return NextResponse.json(
            { isPlaying: false, error: 'Failed to fetch' },
            { status: 200 }
        )
    }
}
