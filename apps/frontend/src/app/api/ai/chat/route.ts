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
            // If backend fails, return fallback response (works in dev AND production)
            console.error("Backend AI error:", response.status)
            return NextResponse.json({
                response: getFallbackResponse(message),
                session_id: session_id || "fallback-session",
                tokens_used: 0,
            })
        }

        const data = await response.json()
        return NextResponse.json(data)
    } catch (error) {
        console.error("AI chat error:", error)

        // Always use fallback on error
        try {
            const body = await request.clone().json().catch(() => ({ message: "" }))
            return NextResponse.json({
                response: getFallbackResponse(body.message || ""),
                session_id: "fallback-session",
                tokens_used: 0,
            })
        } catch {
            return NextResponse.json({
                response: getFallbackResponse(""),
                session_id: "fallback-session",
                tokens_used: 0,
            })
        }
    }
}

/**
 * Development fallback responses - includes Help Center FAQ knowledge
 */
function getFallbackResponse(message: string): string {
    const lowerMessage = message.toLowerCase()

    // === HELP CENTER FAQ KNOWLEDGE ===

    // Getting Started
    if (lowerMessage.includes("start") || lowerMessage.includes("börja") || lowerMessage.includes("begin")) {
        return `Great question about getting started! 🚀

Here's how to begin your DevOps journey:

1. **Head to Modules** - Pick a track that matches your goals
2. **Start from the beginning** - Each module builds on previous knowledge
3. **Complete tasks** - Earn XP and track your progress
4. **Keep your streak** - Learn daily for bonus rewards!

Check out the Linux or Docker modules if you're just starting out. What area interests you most?`
    }

    if (lowerMessage.includes("xp") || lowerMessage.includes("points") || lowerMessage.includes("poäng")) {
        return `XP (Experience Points) are your progress currency! 🏆

**How to earn XP:**
- Complete tasks (varies by difficulty)
- Maintain daily streaks
- Achieve milestones
- Finish modules

Different tasks award different XP - harder tasks = more XP! Your total XP shows on your profile. Keep learning to level up! 💪`
    }

    if (lowerMessage.includes("streak") || lowerMessage.includes("serie") || lowerMessage.includes("daily")) {
        return `Streaks track your consistency! 🔥

**How it works:**
- Complete at least 1 task per day
- Your streak counts consecutive days
- Longer streaks = special badges + bonus XP

Miss a day? Your streak resets to 0. But don't worry - just start again! Consistency beats perfection.`
    }

    // Features
    if (lowerMessage.includes("bookmark") || lowerMessage.includes("bokmärk") || lowerMessage.includes("star") || lowerMessage.includes("spara")) {
        return `Bookmarks help you save tasks for later! ⭐

**How to use:**
- Click the star icon on any task
- Bookmarked tasks appear in the right sidebar
- Perfect for tasks you want to revisit

Pro tip: Use bookmarks to build a study playlist of topics you find challenging!`
    }

    if (lowerMessage.includes("skillpath") || lowerMessage.includes("skill path") || lowerMessage.includes("board") || lowerMessage.includes("map")) {
        return `The SkillPath Board is your visual learning map! 🗺️

**What it shows:**
- How different DevOps technologies connect
- Your progress through skill trees
- Recommended next steps
- Dependencies between skills

Think of it as your GPS for the DevOps landscape. Each node is a skill you can master!`
    }

    if (lowerMessage.includes("dallas") || lowerMessage.includes("ai") || lowerMessage.includes("help") || lowerMessage.includes("hjälp")) {
        return `I'm Dallas, your AI DevOps guide! 🐺

**I can help with:**
- Explaining concepts
- Giving hints when you're stuck
- Recommending what to learn next
- Answering questions about the platform

Just ask me anything about DevOps - Linux, Docker, Kubernetes, CI/CD, cloud, and more!`
    }

    // Account
    if (lowerMessage.includes("password") || lowerMessage.includes("lösenord") || lowerMessage.includes("security")) {
        return `For security settings: 🔒

Go to **Settings → Security** to:
- Change your password
- Update security preferences

You'll need your current password to make changes. Keep your credentials safe!`
    }

    if (lowerMessage.includes("delete") || lowerMessage.includes("account") || lowerMessage.includes("radera") || lowerMessage.includes("konto")) {
        return `About your account: 👤

You can delete your account from **Settings → Danger Zone**.

⚠️ **Warning:** This is irreversible and will permanently delete:
- All your progress
- XP and achievements
- Bookmarks and history

Make sure you really want to do this before proceeding!`
    }

    // Technical topics
    if (lowerMessage.includes("linux") || lowerMessage.includes("terminal") || lowerMessage.includes("bash")) {
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

Check out the Linux module for a deep dive! Want me to explain any specific command?`
    }

    if (lowerMessage.includes("docker") || lowerMessage.includes("container")) {
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

The Docker module covers everything from basics to production patterns. What specific aspect would you like to explore?`
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

    if (lowerMessage.includes("next") || lowerMessage.includes("nästa") || lowerMessage.includes("what should") || lowerMessage.includes("recommend")) {
        return `Based on a typical learning path, here's what I'd recommend:

1. **Linux Fundamentals** - Master the terminal first
2. **Git & Version Control** - Essential for collaboration
3. **Docker** - Containerization basics
4. **CI/CD** - Automate your workflows
5. **Kubernetes** - Orchestration at scale
6. **Cloud (AWS/GCP/Azure)** - Infrastructure

Where are you in your journey? I can give more specific recommendations!`
    }

    // Greetings - warm and welcoming
    if (lowerMessage.match(/^(hej|hello|hi|hey|tjena|hallå|hejsan|tjo|yo|sup|what'?s up|god dag|goddag|morsning|tjenare)[\s!?.]*$/i) ||
        lowerMessage.includes("hej dallas") || lowerMessage.includes("hi dallas") || lowerMessage.includes("hello dallas")) {
        const greetings = [
            `Hej hej! 👋✨ Vad kul att du är här! Jag är Dallas, din DevOps-kompis. Hur kan jag hjälpa dig idag? Vill du lära dig något nytt eller har du en fråga?`,
            `Tjena! 🐺 Välkommen! Jag är Dallas och jag älskar att hjälpa dig med DevOps. Vad har du på hjärtat idag?`,
            `Hey there! 👋🚀 Så roligt att träffas! Jag är Dallas, redo att guida dig genom DevOps-världen. Vad vill du utforska?`,
            `Hallå! ✨ Kul att se dig! Jag är Dallas, din personliga DevOps-guide. Ställ en fråga eller säg bara vad du vill lära dig!`,
            `Hejsan! 🎉 Välkommen till DevOps Hub! Jag är Dallas och jag finns här för att hjälpa dig. Vad kan jag göra för dig?`,
            `Yo! 🐺💜 Skönt att du droppar in! Jag är Dallas - fråga mig vad som helst om Linux, Docker, Kubernetes eller DevOps generellt!`
        ]
        return greetings[Math.floor(Math.random() * greetings.length)]
    }

    // Thanks
    if (lowerMessage.match(/^(tack|thanks|thx|thank you|tackar|tack så mycket)[\s!?.]*$/i)) {
        const thanksResponses = [
            `Ingen orsak! 😊 Det är alltid kul att hjälpa. Har du fler frågor är det bara att fråga!`,
            `Varsågod! 🐺✨ Jag finns här om du behöver mer hjälp!`,
            `Alltid redo att hjälpa! 💪 Lycka till med dina DevOps-äventyr!`,
            `Det var så lite! 🚀 Hojta till om du undrar något mer!`
        ]
        return thanksResponses[Math.floor(Math.random() * thanksResponses.length)]
    }

    // How are you / small talk
    if (lowerMessage.includes("hur mår du") || lowerMessage.includes("how are you") || lowerMessage.includes("läget") || lowerMessage.includes("how's it going")) {
        return `Jag mår toppen! 🐺✨ Tack för att du frågar! Alltid peppad på att hjälpa dig lära dig nya saker. Vad kan jag hjälpa dig med idag?`
    }

    // Who are you
    if (lowerMessage.includes("vem är du") || lowerMessage.includes("who are you") || lowerMessage.includes("vad är du")) {
        return `Jag är Dallas! 🐺 Din AI-kompis och DevOps-guide här på plattformen.

Jag kan hjälpa dig med:
• 🐧 Linux & Bash-kommandon
• 🐳 Docker & containers
• ☸️ Kubernetes
• ☁️ AWS, Azure & molntjänster
• 🔄 CI/CD pipelines
• 💡 Tips för din lärresa

Jag älskar att förklara saker och finns här 24/7. Fråga på! 💜`
    }

    // Goodbye
    if (lowerMessage.match(/^(hejdå|bye|goodbye|ses|vi ses|ciao|adjö)[\s!?.]*$/i)) {
        const goodbyes = [
            `Hejdå! 👋 Lycka till med pluggandet! Kom tillbaka när som helst! 🐺`,
            `Vi ses! 🚀 Fortsätt vara awesome! Jag finns här när du behöver mig!`,
            `Bye bye! ✨ Ha det så bra och fortsätt lära dig coola saker!`,
            `Adjö för nu! 💜 Glöm inte: Consistency beats perfection!`
        ]
        return goodbyes[Math.floor(Math.random() * goodbyes.length)]
    }

    // Default response
    return `Hej! 👋 Jag är Dallas, din DevOps-guide! 🐺

Jag kan hjälpa dig med:
• 🐧 Linux-kommandon & Bash
• 🐳 Docker & containers
• ☸️ Kubernetes-orkestrering
• ☁️ AWS, Azure, GCP
• 🔄 CI/CD pipelines
• 📚 Plattformsfrågor (XP, streaks, bookmarks)

Vad vill du lära dig idag? Bara att fråga! 💜`
}
