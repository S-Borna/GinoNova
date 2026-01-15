import { ImageResponse } from 'next/og'

export const runtime = 'edge'

export const size = {
    width: 180,
    height: 180,
}
export const contentType = 'image/png'

export default function AppleIcon() {
    return new ImageResponse(
        (
            <div
                style={{
                    width: 180,
                    height: 180,
                    borderRadius: 40,
                    background: 'linear-gradient(135deg, #1a1a2e 0%, #0a0a12 100%)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                }}
            >
                <div
                    style={{
                        width: 140,
                        height: 140,
                        borderRadius: '50%',
                        background: 'linear-gradient(135deg, #a78bfa 0%, #8b5cf6 50%, #6366f1 100%)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: '0 0 40px rgba(139, 92, 246, 0.6)',
                    }}
                >
                    <span
                        style={{
                            color: 'white',
                            fontSize: 80,
                            fontWeight: 800,
                            fontFamily: 'sans-serif',
                        }}
                    >
                        G
                    </span>
                </div>
            </div>
        ),
        { ...size }
    )
}
