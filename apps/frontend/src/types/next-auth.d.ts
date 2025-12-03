/**
 * NextAuth Type Declarations
 * Extends default NextAuth types with custom properties
 */

import { DefaultSession, DefaultUser } from "next-auth"
import { JWT, DefaultJWT } from "next-auth/jwt"

declare module "next-auth" {
    interface Session extends DefaultSession {
        accessToken?: string
        backendUser?: {
            id: string
            email: string
            full_name: string
            is_admin: boolean
        }
    }

    interface User extends DefaultUser {
        accessToken?: string
    }
}

declare module "next-auth/jwt" {
    interface JWT extends DefaultJWT {
        accessToken?: string
        backendUser?: {
            id: string
            email: string
            full_name: string
            is_admin: boolean
        }
    }
}
