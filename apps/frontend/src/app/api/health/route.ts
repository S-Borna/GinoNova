import { NextResponse } from 'next/server';

const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function GET() {
    // Basic health check
    const healthData: Record<string, unknown> = {
        status: "ok",
        timestamp: new Date().toISOString(),
        env: {
            NEXT_PUBLIC_API_URL: BACKEND_URL,
            NODE_ENV: process.env.NODE_ENV,
        }
    };

    // Try to reach backend
    try {
        const backendResponse = await fetch(`${BACKEND_URL}/api/health`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });
        healthData.backend = {
            reachable: backendResponse.ok,
            status: backendResponse.status,
        };
    } catch (error) {
        healthData.backend = {
            reachable: false,
            error: error instanceof Error ? error.message : "Unknown error",
        };
    }

    // Try Dallas status
    try {
        const dallasResponse = await fetch(`${BACKEND_URL}/api/dallas/status`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        });
        if (dallasResponse.ok) {
            healthData.dallas = await dallasResponse.json();
        } else {
            healthData.dallas = { error: `Status ${dallasResponse.status}` };
        }
    } catch (error) {
        healthData.dallas = {
            reachable: false,
            error: error instanceof Error ? error.message : "Unknown error",
        };
    }

    return NextResponse.json(healthData);
}
