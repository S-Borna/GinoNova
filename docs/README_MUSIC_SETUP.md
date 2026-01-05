# 🎵 Music Widget Setup Guide

## Pure Last.fm - No Spotify API Needed!

This widget shows what you're currently listening to using Last.fm scrobbles.
**Zero Spotify API hassle** - just a free Last.fm API key!

### Why Last.fm?
- ✅ Free API key (instant, no approval)
- ✅ Real-time via Spotify scrobbling  
- ✅ Works today (Spotify API is blocked for new apps)
- ✅ Beautiful custom vinyl-style widget

---

## Setup (2 minutes!)

### Step 1: Get Last.fm API Key

1. Go to [Last.fm API](https://www.last.fm/api/account/create)
2. Sign in or create account
3. Create an app (any name)
4. Copy your **API Key**

### Step 2: Connect Spotify to Last.fm

1. Go to [Last.fm Settings → Applications](https://www.last.fm/settings/applications)
2. Click **"Connect"** next to Spotify
3. Authorize - Done! Every track you play now scrobbles.

### Step 3: Add Environment Variables

```env
LASTFM_API_KEY=your_api_key_here
LASTFM_USERNAME=your_lastfm_username
```

### Step 4: Restart & Enjoy!

```bash
npm run dev
```

Go to `/pulse` - your music widget is live! 🎶

---

## Widget Variants

```tsx
// Mini - for TopBar
<NowPlayingWidget variant="mini" />

// Compact - for sidebar/cards  
<NowPlayingWidget variant="compact" />

// Full - for dedicated sections
<NowPlayingWidget variant="full" />
```

---

## Features

- 🎵 **Spinning vinyl** animation when playing
- 📊 **Equalizer bars** animation
- 🔄 **Auto-refresh** every 15 seconds
- ⏱️ **"Last played X ago"** when not playing
- 🖼️ **Album art** from Last.fm
- 🔗 **Click to open** in Last.fm

---

## API

### `GET /api/music/now-playing`

```json
{
  "isPlaying": true,
  "track": {
    "name": "Track Name",
    "artist": "Artist",
    "album": "Album",
    "albumArt": "https://...",
    "lastFmUrl": "https://last.fm/..."
  },
  "timestamp": 1704456789000,
  "source": "lastfm"
}
```

---

## Troubleshooting

**Widget shows "Inget spelas"**
- Make sure Spotify is connected to Last.fm
- Check your scrobbles at last.fm/user/[username]
- Verify LASTFM_USERNAME is correct

**Album art missing**
- Some tracks don't have art in Last.fm
- Fallback gradient is shown instead
