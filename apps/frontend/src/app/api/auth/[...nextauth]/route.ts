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
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || "https://saas-project-production-31f8.up.railway.app"

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
                        // Store the backend JWT token
                        token.accessToken = data.access_token
                        token.backendUser = data.user
                    } else {
                        console.error("Failed to authenticate with backend:", await response.text())
                    }
                } catch (error) {
                    console.error("OAuth backend error:", error)
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
