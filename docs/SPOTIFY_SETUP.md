# Spotify Now Playing Widget - Setup Guide

## Översikt

Denna guide hjälper dig sätta upp Spotify "Now Playing" widgeten för DevOpsHub.

## Steg 1: Skapa Spotify Developer App

1. Gå till [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Logga in med ditt Spotify-konto
3. Klicka **"Create App"**
4. Fyll i:
   - **App name:** DevOpsHub Now Playing
   - **App description:** Shows what I'm listening to
   - **Redirect URI:** `https://devopshub.se/api/spotify/auth` (eller `http://localhost:3000/api/spotify/auth` för lokal dev)
   - **APIs used:** Web API
5. Klicka **"Save"**
6. Gå till **"Settings"** och kopiera:
   - **Client ID**
   - **Client Secret** (klicka "View client secret")

## Steg 2: Lägg till Environment Variables

Lägg till i din `.env` fil:

```env
SPOTIFY_CLIENT_ID=din_client_id_här
SPOTIFY_CLIENT_SECRET=din_client_secret_här
NEXT_PUBLIC_APP_URL=https://devopshub.se
```

## Steg 3: Generera Refresh Token

1. Starta appen (om inte redan igång)
2. Gå till: `https://devopshub.se/api/spotify/auth`
3. Logga in med ditt Spotify-konto
4. Godkänn behörigheterna
5. Du får en sida med din **refresh token**
6. Kopiera den och lägg till i `.env`:

```env
SPOTIFY_REFRESH_TOKEN=din_refresh_token_här
```

## Steg 4: Starta om servern

```bash
# Om du kör lokalt
npm run dev

# På Railway/Vercel - redeploya med nya env vars
```

## Steg 5: Verifiera att det fungerar

1. Spela något i Spotify
2. Gå till DevOpsHub
3. Kolla widgeten i top bar - den ska visa vad du lyssnar på!

---

## Felsökning

### "Offline" visas trots att jag spelar musik

- Kontrollera att du spelar på samma konto som du autade med
- Spotify Premium krävs för "currently playing" API
- Vänta ~15 sekunder för nästa poll

### Token fungerar inte

- Generera ny refresh token via `/api/spotify/auth`
- Kontrollera att Client ID och Secret stämmer
- Kolla att Redirect URI i Spotify Dashboard matchar

### 403 Forbidden

- Kolla att alla scopes finns:
  - `user-read-currently-playing`
  - `user-read-recently-played`
  - `user-read-playback-state`
- Generera ny token om scopes ändrats

---

## Teknisk info

- **Polling interval:** 15 sekunder
- **Cache:** 10 sekunder server-side
- **Rate limits:** ~1 request/second (vi använder ~0.07/sec)
- **Token refresh:** Automatiskt, refresh token expire aldrig

## API Endpoints

- `GET /api/spotify/now-playing` - Hämtar aktuell/senaste låt
- `GET /api/spotify/auth` - OAuth flow för att generera token

## Behörigheter som begärs

| Scope | Beskrivning |
|-------|-------------|
| `user-read-currently-playing` | Läsa vad som spelas just nu |
| `user-read-recently-played` | Läsa senast spelade (fallback) |
| `user-read-playback-state` | Läsa playback status |
