/**
 * ============================================================================
 * NEXTAUTH API ROUTE — OAuth Authentication
 * ============================================================================
 *
 * Handles OAuth authentication with Google, GitHub, and Discord.
 * Integrates with the existing JWT-based backend auth system.
 *
 * @phase OAuth Integration
 */

import NextAuth from "next-auth"
import type { NextAuthOptions } from "next-auth"
import type { Provider } from "next-auth/providers/index"
import GoogleProvider from "next-auth/providers/google"
import GitHubProvider from "next-auth/providers/github"
import DiscordProvider from "next-auth/providers/discord"

// Use server-side env var (without NEXT_PUBLIC_ prefix works on server)
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || "https://api.ginonova.com"

// Only include providers that have valid credentials
const providers: Provider[] = []

if (process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET) {
    providers.push(
        GoogleProvider({
            clientId: process.env.GOOGLE_CLIENT_ID,
            clientSecret: process.env.GOOGLE_CLIENT_SECRET,
        })
    )
}

if (process.env.GITHUB_CLIENT_ID && process.env.GITHUB_CLIENT_SECRET) {
    providers.push(
        GitHubProvider({
            clientId: process.env.GITHUB_CLIENT_ID,
            clientSecret: process.env.GITHUB_CLIENT_SECRET,
        })
    )
}

if (process.env.DISCORD_CLIENT_ID && process.env.DISCORD_CLIENT_SECRET) {
    providers.push(
        DiscordProvider({
            clientId: process.env.DISCORD_CLIENT_ID,
            clientSecret: process.env.DISCORD_CLIENT_SECRET,
        })
    )
}

const authOptions: NextAuthOptions = {
    providers,
    callbacks: {
        async signIn({ user, account }) {
            // Allow sign in and handle user creation in jwt callback
            return true
        },
        async jwt({ token, user, account }) {
            // On initial sign in, register/login with backend
            if (account && user) {
                try {
                    const response = await fetch(`${API_BASE_URL}/api/auth/oauth`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            email: user.email,
                            name: user.name,
                            provider: account.provider,
                            provider_id: account.providerAccountId,
                            avatar: user.image,
                        }),
                    })

                    if (response.ok) {
                        const data = await response.json()
                        // Store the backend JWT token and expiry time
                        token.accessToken = data.access_token
                        token.backendUser = data.user
                        // Track when token was issued (for refresh logic)
                        token.tokenIssuedAt = Date.now()
                    } else {
                        console.error("Failed to authenticate with backend:", await response.text())
                    }
                } catch (error) {
                    console.error("OAuth backend error:", error)
                }
            }
            
            // REFRESH BACKEND TOKEN if it's older than 12 hours
            // Backend tokens expire in 24h, so refresh at 12h to be safe
            const tokenAge = Date.now() - (token.tokenIssuedAt as number || 0)
            const TWELVE_HOURS = 12 * 60 * 60 * 1000
            
            if (token.backendUser && tokenAge > TWELVE_HOURS) {
                console.log("[NextAuth] Refreshing backend token for:", (token.backendUser as any)?.email)
                try {
                    const response = await fetch(`${API_BASE_URL}/api/auth/oauth`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            email: (token.backendUser as any)?.email,
                            name: (token.backendUser as any)?.full_name,
                            provider: "refresh", // Indicates this is a token refresh
                            provider_id: (token.backendUser as any)?.id,
                            avatar: null,
                        }),
                    })

                    if (response.ok) {
                        const data = await response.json()
                        token.accessToken = data.access_token
                        token.backendUser = data.user
                        token.tokenIssuedAt = Date.now()
                        console.log("[NextAuth] Backend token refreshed successfully")
                    }
                } catch (error) {
                    console.error("[NextAuth] Failed to refresh backend token:", error)
                }
            }
            
            return token
        },
        async session({ session, token }) {
            // Pass backend token and user to client session
            if (token.accessToken) {
                session.accessToken = token.accessToken as string
            }
            if (token.backendUser) {
                session.backendUser = token.backendUser as {
                    id: string
                    email: string
                    full_name: string
                    is_admin: boolean
                }
            }
            return session
        },
        async redirect({ url, baseUrl }) {
            // After sign in, redirect to dashboard
            if (url.startsWith(baseUrl)) {
                return `${baseUrl}/dashboard`
            }
            return baseUrl + "/dashboard"
        },
    },
    pages: {
        signIn: "/login",
        error: "/login",
    },
    session: {
        strategy: "jwt",
    },
    secret: process.env.NEXTAUTH_SECRET,
}

const handler = NextAuth(authOptions)

export { handler as GET, handler as POST }
