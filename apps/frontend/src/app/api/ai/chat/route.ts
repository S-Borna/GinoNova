/**
 * AI Chat API Route - Proxies requests to backend AI service
 * @phase AI-WIZARD-FAS-1
 */

import { NextRequest, NextResponse } from "next/server"

const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function POST(request: NextRequest) {
    try {
        const body = await request.json()
        const { message, context, session_id } = body

        // Forward to backend AI service
        const response = await fetch(`${BACKEND_URL}/api/ai/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                // Forward auth token if present
                ...(request.headers.get("Authorization")
                    ? { Authorization: request.headers.get("Authorization")! }
                    : {}),
            },
            body: JSON.stringify({
                message,
                context,
                session_id,
            }),
        })

        if (!response.ok) {
            // If backend fails, return a graceful error
            console.error("Backend AI error:", response.status)
            
            // Fallback response for development
            if (process.env.NODE_ENV === "development") {
                return NextResponse.json({
                    response: getFallbackResponse(message),
                    session_id: session_id || "dev-session",
                    tokens_used: 0,
                })
            }
            
            return NextResponse.json(
                { error: "AI service unavailable" },
                { status: 503 }
            )
        }

        const data = await response.json()
        return NextResponse.json(data)
    } catch (error) {
        console.error("AI chat error:", error)
        
        // Fallback for development
        if (process.env.NODE_ENV === "development") {
            const body = await request.clone().json().catch(() => ({ message: "" }))
            return NextResponse.json({
                response: getFallbackResponse(body.message || ""),
                session_id: "dev-session",
                tokens_used: 0,
            })
        }
        
        return NextResponse.json(
            { error: "Internal server error" },
            { status: 500 }
        )
    }
}

/**
 * Development fallback responses
 */
function getFallbackResponse(message: string): string {
    const lowerMessage = message.toLowerCase()

    if (lowerMessage.includes("linux") || lowerMessage.includes("terminal")) {
        return `Great question about Linux! 🐧

Here's a quick tip: The terminal is your best friend in DevOps. Start with these essentials:

\`\`\`bash
# List files with details
ls -la

# Navigate directories
cd /path/to/directory

# View file contents
cat filename.txt
\`\`\`

Check out the Linux SkillsMap for a deep dive! Want me to explain any specific command?`
    }

    if (lowerMessage.includes("docker")) {
        return `Docker is essential for modern DevOps! 🐳

Here's a quick overview:

\`\`\`bash
# Run a container
docker run -d --name myapp nginx

# List running containers
docker ps

# View logs
docker logs myapp
\`\`\`

The Docker SkillsMap covers everything from basics to advanced production patterns. What specific aspect would you like to explore?`
    }

    if (lowerMessage.includes("kubernetes") || lowerMessage.includes("k8s")) {
        return `Kubernetes is the orchestration king! ☸️

Key concepts:
- **Pods**: Smallest deployable units
- **Deployments**: Manage replicas
- **Services**: Expose your apps

\`\`\`yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: app
    image: nginx
\`\`\`

What would you like to learn about Kubernetes?`
    }

    if (lowerMessage.includes("help") || lowerMessage.includes("hint")) {
        return `I'm here to help! 🧙‍♂️

Here's what I can do:
- **Explain concepts**: Ask me about any DevOps topic
- **Give hints**: If you're stuck on a task, I'll guide you
- **Suggest next steps**: Based on your progress

What are you working on right now?`
    }

    if (lowerMessage.includes("next") || lowerMessage.includes("what should")) {
        return `Based on a typical learning path, here's what I'd recommend:

1. **Linux Fundamentals** - Master the terminal first
2. **Git & Version Control** - Essential for collaboration
3. **Docker** - Containerization basics
4. **CI/CD** - Automate your workflows
5. **Kubernetes** - Orchestration at scale
6. **Cloud (AWS/GCP/Azure)** - Infrastructure

Where are you in your journey? I can give more specific recommendations!`
    }

    // Default response
    return `Hey! 👋 I'm your DevOps Wizard.

I can help you with:
- Linux commands and concepts
- Docker containerization
- Kubernetes orchestration
- AWS cloud services
- CI/CD pipelines
- And much more!

What would you like to learn about today?`
}
