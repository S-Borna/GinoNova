# OAuth Setup Guide — DevOpsHub

This guide explains how to configure Google, GitHub, and Discord OAuth for DevOpsHub.

## Prerequisites

1. Access to Netlify dashboard for frontend environment variables
2. Access to Railway dashboard for backend environment variables
3. Admin access to create OAuth apps on each provider

---

## 🔐 Step 1: Generate NextAuth Secret

Generate a secure secret for NextAuth:

```bash
openssl rand -base64 32
```

Add this to Netlify as `NEXTAUTH_SECRET`.

---

## 🌐 Step 2: Configure NEXTAUTH_URL

Set `NEXTAUTH_URL` to your frontend URL:
- Production: `https://saids-devopshub.netlify.app`
- Local dev: `http://localhost:3000`

---

## 🔵 Google OAuth Setup

### 1. Go to Google Cloud Console
Visit: https://console.cloud.google.com/apis/credentials

### 2. Create OAuth Client
1. Click **"Create Credentials"** → **"OAuth client ID"**
2. Application type: **Web application**
3. Name: `DevOpsHub`
4. Authorized JavaScript origins:
   - `https://saids-devopshub.netlify.app`
   - `http://localhost:3000` (for local dev)
5. Authorized redirect URIs:
   - `https://saids-devopshub.netlify.app/api/auth/callback/google`
   - `http://localhost:3000/api/auth/callback/google` (for local dev)

### 3. Copy Credentials
Add to Netlify environment variables:
- `GOOGLE_CLIENT_ID` = Your Client ID
- `GOOGLE_CLIENT_SECRET` = Your Client Secret

### 4. Configure OAuth Consent Screen
1. Go to **OAuth consent screen**
2. User Type: **External**
3. App name: `DevOpsHub`
4. User support email: Your email
5. Scopes: Add `email` and `profile`
6. Test users: Add your email for testing

---

## ⚫ GitHub OAuth Setup

### 1. Go to GitHub Developer Settings
Visit: https://github.com/settings/developers

### 2. Create OAuth App
1. Click **"New OAuth App"**
2. Application name: `DevOpsHub`
3. Homepage URL: `https://saids-devopshub.netlify.app`
4. Authorization callback URL: `https://saids-devopshub.netlify.app/api/auth/callback/github`

### 3. Copy Credentials
After creating, click **"Generate a new client secret"**

Add to Netlify environment variables:
- `GITHUB_CLIENT_ID` = Your Client ID
- `GITHUB_CLIENT_SECRET` = Your Client Secret

---

## 🟣 Discord OAuth Setup

### 1. Go to Discord Developer Portal
Visit: https://discord.com/developers/applications

### 2. Create Application
1. Click **"New Application"**
2. Name: `DevOpsHub`
3. Go to **OAuth2** → **General**

### 3. Configure Redirects
Add redirect URIs:
- `https://saids-devopshub.netlify.app/api/auth/callback/discord`
- `http://localhost:3000/api/auth/callback/discord` (for local dev)

### 4. Copy Credentials
Add to Netlify environment variables:
- `DISCORD_CLIENT_ID` = Application ID (from General tab)
- `DISCORD_CLIENT_SECRET` = Client Secret (from OAuth2 tab)

### 5. Configure Bot (Optional - for Discord integration)
If you want to integrate with Discord servers later:
1. Go to **Bot** tab
2. Create a bot
3. Save the bot token for future use

---

## 🚀 Deployment Checklist

### Netlify Environment Variables
Add these to Netlify dashboard (Site settings → Environment variables):

```
NEXTAUTH_SECRET=<generated-secret>
NEXTAUTH_URL=https://saids-devopshub.netlify.app

GOOGLE_CLIENT_ID=<your-google-client-id>
GOOGLE_CLIENT_SECRET=<your-google-client-secret>

GITHUB_CLIENT_ID=<your-github-client-id>
GITHUB_CLIENT_SECRET=<your-github-client-secret>

DISCORD_CLIENT_ID=<your-discord-client-id>
DISCORD_CLIENT_SECRET=<your-discord-client-secret>
```

### Railway Backend
The backend OAuth endpoint is already configured. No additional variables needed.

### CORS Configuration
Make sure your backend CORS settings include:
- `https://saids-devopshub.netlify.app`

---

## 🧪 Testing

### Local Development
1. Copy `env/frontend.env.example` to `apps/frontend/.env.local`
2. Fill in your OAuth credentials
3. Set `NEXTAUTH_URL=http://localhost:3000`
4. Run `npm run dev` in frontend

### Production Testing
1. Deploy to Netlify
2. Click each OAuth button on login page
3. Verify user is created in database
4. Check that session persists after redirect

---

## 🔧 Troubleshooting

### "Redirect URI mismatch" error
- Verify the callback URL in provider matches exactly
- Check for trailing slashes
- Ensure HTTPS is used in production

### "Invalid client" error
- Verify CLIENT_ID and CLIENT_SECRET are correct
- Check that the OAuth app is not suspended/deleted

### Session not persisting
- Verify NEXTAUTH_SECRET is set
- Check browser cookies are enabled
- Verify NEXTAUTH_URL matches your domain

### Backend authentication fails
- Check backend CORS settings
- Verify API_URL is correct
- Check backend logs for errors

---

## 📁 Files Modified

### Frontend
- `src/app/api/auth/[...nextauth]/route.ts` — NextAuth API route
- `src/components/auth/SocialButtons.tsx` — OAuth buttons
- `src/components/auth/AuthProvider.tsx` — Session integration
- `src/components/auth/NextAuthProvider.tsx` — SessionProvider wrapper
- `src/components/Providers.tsx` — Added NextAuthProvider
- `src/types/next-auth.d.ts` — TypeScript types

### Backend
- `src/api/auth.py` — OAuth endpoint
- `src/schemas/user.py` — OAuthRequest schema
- `src/db/models.py` — OAuth fields in User model

---

## 🎯 Next Steps

1. Set up OAuth credentials for each provider
2. Add environment variables to Netlify
3. Trigger a redeploy
4. Test each login method
5. Optionally: Add Discord bot for server integration
