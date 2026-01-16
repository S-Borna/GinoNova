"use client"

/**
 * ============================================================================
 * 🤖 DALLAS ASSISTANT — Persistent AI Chat Companion
 * ============================================================================
 *
 * Floating AI assistant that:
 * - Appears on every page (bottom right)
 * - Context-aware based on current page/module
 * - Provides hints, explanations, and guidance
 * - Tracks user progress and suggests next steps
 * - Chat history persisted in localStorage
 *
 * Design: Cosmic pulsating bubble with smooth animations
 *
 * @phase MILESTONE-4.0-AI-ASSISTANT
 */

import { useState, useEffect, useRef } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
    X,
    Send,
    Sparkles,
    Lightbulb,
    TrendingUp,
    HelpCircle,
    Minimize2,
    Maximize2,
    Trash2,
} from "lucide-react"
import { usePathname } from "next/navigation"

/* ============================================================================
   TYPES
   ============================================================================ */

interface Message {
    id: string
    role: "user" | "assistant"
    content: string
    timestamp: Date
}

interface QuickAction {
    icon: React.ElementType
    label: string
    prompt: string
}

/* ============================================================================
   CONTEXT-AWARE QUICK ACTIONS
   ============================================================================ */

function getQuickActionsForPage(pathname: string): QuickAction[] {
    // Dashboard
    if (pathname.includes("/dashboard")) {
        return [
            { icon: TrendingUp, label: "Vad ska jag lära mig härnäst?", prompt: "Baserat på min progress, vilken modul borde jag fokusera på?" },
            { icon: Sparkles, label: "Hur går det för mig?", prompt: "Ge mig en sammanfattning av min lärandeframgång och prestationer." },
            { icon: Lightbulb, label: "Studietips", prompt: "Ge mig tips på hur jag lär mig DevOps effektivt." },
        ]
    }

    // Modules page
    if (pathname.includes("/modules") && !pathname.match(/\/modules\/[^/]+/)) {
        return [
            { icon: HelpCircle, label: "Vilken modul först?", prompt: "Jag tittar på modullistan. Vilken bör jag börja med?" },
            { icon: Lightbulb, label: "Förklara förkunskaper", prompt: "Kan du förklara vad förkunskaper är och varför de är viktiga?" },
            { icon: TrendingUp, label: "Karriärråd", prompt: "Vilka moduler är viktigast för att få ett DevOps-jobb?" },
        ]
    }

    // Inside a module
    if (pathname.match(/\/modules\/[^/]+/)) {
        return [
            { icon: HelpCircle, label: "Förklara detta koncept", prompt: "Kan du förklara huvudkonceptet i denna modul på ett enkelt sätt?" },
            { icon: Lightbulb, label: "Ge mig en ledtråd", prompt: "Jag har kört fast på uppgiften. Kan du ge mig en ledtråd utan hela svaret?" },
            { icon: Sparkles, label: "Verkligt exempel", prompt: "Kan du ge mig ett verkligt exempel på hur detta används i produktion?" },
        ]
    }

    // Default quick actions
    return [
        { icon: HelpCircle, label: "Hur fungerar detta?", prompt: "Kan du förklara hur den här sidan fungerar?" },
        { icon: Lightbulb, label: "Ge mig tips", prompt: "Vilka tips har du för att använda denna funktion effektivt?" },
        { icon: TrendingUp, label: "Vad händer sen?", prompt: "Vad borde jag göra härnäst på min läranderesa?" },
    ]
}

/* ============================================================================
   DALLAS AVATAR BUBBLE
   ============================================================================ */

function DallasAvatar({ size = "md", pulsate = true }: { size?: "sm" | "md" | "lg"; pulsate?: boolean }) {
    const sizeMap = {
        sm: "w-8 h-8",
        md: "w-12 h-12",
        lg: "w-16 h-16",
    }

    const iconSizeMap = {
        sm: "w-4 h-4",
        md: "w-6 h-6",
        lg: "w-8 h-8",
    }

    return (
        <div className="relative">
            {pulsate && (
                <>
                    <motion.div
                        className="absolute inset-0 rounded-full bg-purple-500/30 blur-xl"
                        animate={{
                            scale: [1, 1.5, 1],
                            opacity: [0.4, 0.7, 0.4],
                        }}
                        transition={{ duration: 2, repeat: Infinity }}
                    />
                    <motion.div
                        className="absolute inset-0 rounded-full bg-cyan-500/20 blur-lg"
                        animate={{
                            scale: [1.3, 1, 1.3],
                            opacity: [0.3, 0.6, 0.3],
                        }}
                        transition={{ duration: 2.5, repeat: Infinity }}
                    />
                </>
            )}
            <div className={cn(
                sizeMap[size],
                "relative rounded-full",
                "bg-gradient-to-br from-gray-700 via-gray-600 to-gray-800",
                "flex items-center justify-center",
                "shadow-[0_0_20px_rgba(59,130,246,0.4)]",
                "border border-gray-500/30"
            )}>
                <span className={cn(
                    size === "sm" ? "text-base" : size === "md" ? "text-xl" : "text-2xl"
                )}>🐺</span>
            </div>
        </div>
    )
}

/* ============================================================================
   MESSAGE BUBBLE
   ============================================================================ */

interface MessageBubbleProps {
    message: Message
}

function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.role === "user"

    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "flex gap-3 mb-4",
                isUser ? "flex-row-reverse" : "flex-row"
            )}
        >
            {!isUser && <DallasAvatar size="sm" pulsate={false} />}

            <div className={cn(
                "max-w-[80%] p-4 rounded-2xl",
                isUser
                    ? "bg-gradient-to-br from-purple-600 to-purple-500 text-white rounded-tr-none"
                    : "bg-gradient-to-br from-zinc-800 to-zinc-900 text-zinc-100 border border-zinc-700 rounded-tl-none"
            )}>
                <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
                <p className={cn(
                    "text-xs mt-2",
                    isUser ? "text-purple-200" : "text-zinc-500"
                )}>
                    {new Date(message.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </p>
            </div>
        </motion.div>
    )
}

/* ============================================================================
   MAIN DALLAS ASSISTANT COMPONENT
   ============================================================================ */

export function DallasAssistant() {
    const [isOpen, setIsOpen] = useState(false)
    const [isMinimized, setIsMinimized] = useState(false)
    const [messages, setMessages] = useState<Message[]>([])
    const [input, setInput] = useState("")
    const [isTyping, setIsTyping] = useState(false)
    const messagesEndRef = useRef<HTMLDivElement>(null)
    const pathname = usePathname()

    // Load chat history from localStorage on mount
    useEffect(() => {
        try {
            const saved = localStorage.getItem("dallas-chat-history")
            if (saved) {
                const parsed = JSON.parse(saved)
                setMessages(parsed.map((m: any) => ({ ...m, timestamp: new Date(m.timestamp) })))
            } else {
                // Welcome message
                const welcomeMessage: Message = {
                    id: "welcome",
                    role: "assistant",
                    content: "Hej! Jag är Dallas, din AI-studiekompis 🐺\n\nJag finns här för att hjälpa dig bemästra DevOps! Fråga mig om moduler, koncept eller din lärandeväg. Jag kan också ge dig ledtrådar när du kör fast!",
                    timestamp: new Date(),
                }
                setMessages([welcomeMessage])
            }
        } catch (error) {
            console.error("Failed to load chat history:", error)
        }
    }, [])

    // Save chat history to localStorage whenever messages change
    useEffect(() => {
        if (messages.length > 1) { // Don't save just the welcome message
            try {
                localStorage.setItem("dallas-chat-history", JSON.stringify(messages))
            } catch (error) {
                console.error("Failed to save chat history:", error)
            }
        }
    }, [messages])

    // Auto-scroll to bottom when new messages arrive
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }, [messages])

    // Simulate AI response (in production, this would call your backend AI service)
    const generateAIResponse = async (userMessage: string): Promise<string> => {
        const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://api.ginonova.com"

        try {
            // Call backend Dallas AI service (connected to OpenAI)
            const response = await fetch(`${API_BASE_URL}/api/dallas/chat`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    message: userMessage,
                    context: pathname.includes("/modules/") ? "module" :
                        pathname.includes("/dashboard") ? "dashboard" : "general",
                    user_name: "User"
                }),
            })

            if (response.ok) {
                const data = await response.json()
                return data.response || "Hmm, jag fick inget svar. Försök igen!"
            }

            // Fallback if backend fails
            throw new Error("Backend unavailable")
        } catch (error) {
            console.error("Dallas API error:", error)

            // Smart fallback responses (Swedish) - with ACTUAL technical answers
            const lowerMessage = userMessage.toLowerCase()

            // TECHNICAL QUESTIONS - Give actual answers!
            
            // Symbolic vs Hard links
            if (lowerMessage.includes("symbolic") || lowerMessage.includes("symlink") || lowerMessage.includes("hard link") || lowerMessage.includes("länk")) {
                return "**Symbolic link vs Hard link:**\n\n🔗 **Symbolic link (soft link):**\n- Pekar på filens SÖKVÄG (som en genväg)\n- Kan peka på mappar\n- Kan peka över filsystem\n- Går sönder om originalet tas bort\n- `ln -s target link`\n\n🔗 **Hard link:**\n- Pekar på filens INODE (samma data)\n- Kan INTE peka på mappar\n- Måste vara på samma filsystem\n- Originalet kan tas bort, datan finns kvar\n- `ln target link`\n\n📖 Man page: https://man7.org/linux/man-pages/man1/ln.1.html"
            }

            // Permissions
            if (lowerMessage.includes("chmod") || lowerMessage.includes("permission") || lowerMessage.includes("rättighet") || lowerMessage.includes("755") || lowerMessage.includes("644")) {
                return "**Linux-rättigheter:**\n\n`rwx` = read(4) + write(2) + execute(1)\n\n**Vanliga värden:**\n- `755` = rwxr-xr-x (körbara filer)\n- `644` = rw-r--r-- (vanliga filer)\n- `700` = rwx------ (privat)\n\n**Kommandon:**\n- `chmod 755 fil` - numeriskt\n- `chmod u+x fil` - symboliskt\n- `chown user:group fil` - ändra ägare\n\n📖 Man page: https://man7.org/linux/man-pages/man1/chmod.1.html"
            }

            // Process management
            if (lowerMessage.includes("process") || lowerMessage.includes("kill") || lowerMessage.includes("ps aux") || lowerMessage.includes("signal")) {
                return "**Processhantering:**\n\n**Visa processer:**\n- `ps aux` - alla processer\n- `top` / `htop` - realtid\n- `pgrep namn` - hitta PID\n\n**Avsluta processer:**\n- `kill PID` - SIGTERM (snällt)\n- `kill -9 PID` - SIGKILL (tvinga)\n- `killall namn` - efter namn\n\n**Bakgrund:**\n- `command &` - kör i bakgrund\n- `nohup command &` - överlev logout\n- `jobs` - lista bakgrundsjobb\n\n📖 Man page: https://man7.org/linux/man-pages/man1/kill.1.html"
            }

            // Docker basics
            if (lowerMessage.includes("docker") || lowerMessage.includes("container") || lowerMessage.includes("image")) {
                return "**Docker grunderna:**\n\n**Image vs Container:**\n- Image = mall/blueprint (som en klass)\n- Container = körande instans (som ett objekt)\n\n**Vanliga kommandon:**\n- `docker build -t namn .` - bygg image\n- `docker run -d -p 8080:80 image` - kör container\n- `docker ps` - visa körande containers\n- `docker logs container` - visa loggar\n- `docker exec -it container bash` - gå in\n\n📖 Docs: https://docs.docker.com/get-started/"
            }

            // Grep/find/search
            if (lowerMessage.includes("grep") || lowerMessage.includes("find") || lowerMessage.includes("sök") || lowerMessage.includes("hitta")) {
                return "**Söka i Linux:**\n\n**grep - sök i filinnehåll:**\n- `grep 'text' fil` - sök i fil\n- `grep -r 'text' mapp/` - rekursivt\n- `grep -i 'text'` - case-insensitive\n- `grep -n 'text'` - visa radnummer\n\n**find - sök filer:**\n- `find /sökväg -name '*.log'` - efter namn\n- `find . -type f -size +100M` - stora filer\n- `find . -mtime -7` - ändrade senaste 7 dagar\n\n📖 Man pages: https://man7.org/linux/man-pages/man1/grep.1.html"
            }

            // Help with concepts (generic)
            if (lowerMessage.includes("förklara") || lowerMessage.includes("vad är") || lowerMessage.includes("explain") || lowerMessage.includes("what is") || lowerMessage.includes("skillnad")) {
                return "Bra fråga! Kan du specificera lite mer vad du undrar över? 🤔\n\nJag kan hjälpa med:\n- Linux-kommandon och filsystem\n- Docker och containers\n- Nätverk och SSH\n- Bash-skript\n- Rättigheter och säkerhet\n\nVilket område gäller din fråga?"
            }

            // Hints
            if (lowerMessage.includes("ledtråd") || lowerMessage.includes("fast") || lowerMessage.includes("hint") || lowerMessage.includes("stuck")) {
                return "Jag ser att du jobbar dig igenom denna utmaning! Här är en knuff i rätt riktning:\n\n💡 Tänk på kommandostrukturen du lärde dig tidigare. Vilken flagga skulle hjälpa dig se dolda filer?\n\nTesta och berätta hur det går!"
            }

            // Next steps
            if (lowerMessage.includes("nästa") || lowerMessage.includes("härnäst") || lowerMessage.includes("next") || lowerMessage.includes("should i learn")) {
                return "Baserat på din progress rekommenderar jag:\n\n🚀 Fokusera på Docker härnäst - det är grundläggande för modern DevOps\n⏱️ Bör ta ca 8-10 timmar att slutföra\n💼 95% av DevOps-jobb kräver containerkunskap\n\nRedo att köra? Kolla /skillsmaps/kubernetes-fundamentals!"
            }

            // Progress check
            if (lowerMessage.includes("progress") || lowerMessage.includes("hur går det")) {
                return "Du krossar det! 🎉\n\n✅ 3 moduler slutförda\n⚡ 450 XP intjänat\n🔥 5 dagars lärandestreak\n\nDu är bland topp 20% av alla studenter denna månad. Fortsätt så!"
            }

            // Study tips
            if (lowerMessage.includes("tips") || lowerMessage.includes("hur lär")) {
                return "Här är mina beprövade DevOps-lärandestrategier:\n\n1. **Hands-on övning** - Läs inte bara, gör!\n2. **Bygg riktiga projekt** - Portfolio > certifikat\n3. **Lär dig offentligt** - Dela vad du lär dig\n4. **Gå med i communities** - DevOps Reddit, Discord\n5. **Konsistens > intensitet** - 1 timme dagligen slår 7 timmar på söndag\n\nVilket område vill du fokusera på?"
            }

            // Career advice
            if (lowerMessage.includes("jobb") || lowerMessage.includes("karriär") || lowerMessage.includes("job") || lowerMessage.includes("career")) {
                return "Låt oss prata karriärstrategi! 💼\n\n**Mest efterfrågade skills just nu:**\n- Kubernetes (högsta prioritet)\n- CI/CD pipelines\n- Molnplattformar (AWS/Azure)\n- Infrastructure as Code\n\n**Mitt råd:** Bemästra Docker först, sedan Kubernetes. Den kombon öppnar dörrar hos 90% av företagen.\n\nVill du ha specifika jobbsökningstips?"
            }

            // Default contextual response
            if (pathname.includes("/modules/")) {
                return "Jag är här för att hjälpa dig med denna modul! Fråga mig gärna om:\n\n- Förklaringar av koncept\n- Ledtrådar till övningar\n- Exempel från verkligheten\n- Ytterligare resurser\n\nVad skulle hjälpa dig mest just nu?"
            }

            // Generic helpful response
            return "Jag är här för att guida dig på din DevOps-resa! 🐺\n\n- Frågor om moduler och koncept\n- Personliga lärrekommendationer\n- Hjälp när du kör fast\n- Karriärråd och studietips\n\nVad vill du veta?"
        }
    }

    const handleSend = async () => {
        if (!input.trim()) return

        const userMessage: Message = {
            id: `user-${Date.now()}`,
            role: "user",
            content: input.trim(),
            timestamp: new Date(),
        }

        setMessages(prev => [...prev, userMessage])
        setInput("")
        setIsTyping(true)

        // Generate AI response
        try {
            const aiResponse = await generateAIResponse(input.trim())
            const assistantMessage: Message = {
                id: `assistant-${Date.now()}`,
                role: "assistant",
                content: aiResponse,
                timestamp: new Date(),
            }
            setMessages(prev => [...prev, assistantMessage])
        } catch (error) {
            console.error("Failed to generate response:", error)
            const errorMessage: Message = {
                id: `error-${Date.now()}`,
                role: "assistant",
                content: "Hoppsan! Något gick fel. Kan du försöka fråga igen?",
                timestamp: new Date(),
            }
            setMessages(prev => [...prev, errorMessage])
        } finally {
            setIsTyping(false)
        }
    }

    const handleQuickAction = (prompt: string) => {
        setInput(prompt)
        setTimeout(() => handleSend(), 100)
    }

    // Clear chat and start fresh
    const handleClearChat = () => {
        const welcomeMessage: Message = {
            id: "welcome-" + Date.now(),
            role: "assistant",
            content: "Chatten har rensats! 🐺\n\nJag är redo för nya frågor. Hur kan jag hjälpa dig idag?",
            timestamp: new Date(),
        }
        setMessages([welcomeMessage])
        localStorage.removeItem("dallas-chat-history")
    }

    const quickActions = getQuickActionsForPage(pathname)

    return (
        <>
            {/* Floating Bubble */}
            <AnimatePresence>
                {!isOpen && (
                    <motion.button
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        exit={{ scale: 0, opacity: 0 }}
                        whileHover={{ scale: 1.1 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={() => setIsOpen(true)}
                        className={cn(
                            "fixed bottom-6 right-6 z-50",
                            "w-16 h-16 rounded-full",
                            "bg-gradient-to-br from-purple-600 via-purple-500 to-cyan-500",
                            "shadow-[0_0_40px_rgba(139,92,246,0.6)]",
                            "flex items-center justify-center",
                            "cursor-pointer group",
                            "border-2 border-white/20"
                        )}
                    >
                        <span className="text-3xl group-hover:scale-110 transition-transform">🐺</span>

                        {/* Notification dot (example for new recommendations) */}
                        <motion.div
                            className="absolute -top-1 -right-1 w-4 h-4 bg-emerald-500 rounded-full border-2 border-[#05050a]"
                            animate={{
                                scale: [1, 1.2, 1],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />

                        {/* Pulsating rings */}
                        <motion.div
                            className="absolute inset-0 rounded-full border-2 border-purple-400"
                            animate={{
                                scale: [1, 1.4, 1],
                                opacity: [0.5, 0, 0.5],
                            }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />
                    </motion.button>
                )}
            </AnimatePresence>

            {/* Chat Window */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: 20, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 20, scale: 0.95 }}
                        className={cn(
                            "fixed z-50",
                            isMinimized
                                ? "bottom-6 right-6 w-80 h-16"
                                : "bottom-6 right-6 w-[400px] h-[600px]",
                            "bg-gradient-to-br from-zinc-900/98 via-zinc-900/98 to-zinc-950/98",
                            "backdrop-blur-xl",
                            "rounded-3xl",
                            "border border-white/10",
                            "shadow-[0_0_80px_rgba(139,92,246,0.3)]",
                            "flex flex-col",
                            "overflow-hidden",
                            "transition-all duration-300"
                        )}
                    >
                        {/* Header */}
                        <div className={cn(
                            "p-4 border-b border-white/10",
                            "bg-gradient-to-r from-purple-600/20 to-cyan-600/20",
                            "flex items-center justify-between"
                        )}>
                            <div className="flex items-center gap-3">
                                <DallasAvatar size="sm" />
                                <div>
                                    <h3 className="font-bold text-white">Dallas</h3>
                                    <p className="text-xs text-zinc-400">Din AI-studiekompis</p>
                                </div>
                            </div>
                            <div className="flex items-center gap-1">
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={handleClearChat}
                                    className="text-zinc-400 hover:text-amber-400 p-2 h-auto"
                                    title="Rensa chatt"
                                >
                                    <Trash2 className="w-4 h-4" />
                                </Button>
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={() => setIsMinimized(!isMinimized)}
                                    className="text-zinc-400 hover:text-white p-2 h-auto"
                                    title={isMinimized ? "Maximera" : "Minimera"}
                                >
                                    {isMinimized ? <Maximize2 className="w-4 h-4" /> : <Minimize2 className="w-4 h-4" />}
                                </Button>
                                <Button
                                    variant="ghost"
                                    size="sm"
                                    onClick={() => setIsOpen(false)}
                                    className="text-zinc-400 hover:text-red-400 p-2 h-auto"
                                    title="Stäng"
                                >
                                    <X className="w-4 h-4" />
                                </Button>
                            </div>
                        </div>

                        {!isMinimized && (
                            <>
                                {/* Quick Actions */}
                                <div className="p-4 border-b border-white/10 bg-zinc-900/50">
                                    <p className="text-xs text-zinc-500 mb-2 uppercase tracking-wider">Snabbval</p>
                                    <div className="flex flex-wrap gap-2">
                                        {quickActions.map((action, index) => (
                                            <motion.button
                                                key={index}
                                                initial={{ opacity: 0, scale: 0.9 }}
                                                animate={{ opacity: 1, scale: 1 }}
                                                transition={{ delay: index * 0.1 }}
                                                whileHover={{ scale: 1.05 }}
                                                whileTap={{ scale: 0.95 }}
                                                onClick={() => handleQuickAction(action.prompt)}
                                                className={cn(
                                                    "px-3 py-2 rounded-xl text-xs font-medium",
                                                    "bg-gradient-to-br from-purple-600/20 to-purple-500/10",
                                                    "border border-purple-500/30",
                                                    "text-purple-300 hover:text-purple-200",
                                                    "flex items-center gap-1.5",
                                                    "transition-all duration-200"
                                                )}
                                            >
                                                <action.icon className="w-3 h-3" />
                                                {action.label}
                                            </motion.button>
                                        ))}
                                    </div>
                                </div>

                                {/* Messages */}
                                <div className="flex-1 overflow-y-auto p-4 space-y-4">
                                    {messages.map((message) => (
                                        <MessageBubble key={message.id} message={message} />
                                    ))}

                                    {isTyping && (
                                        <motion.div
                                            initial={{ opacity: 0 }}
                                            animate={{ opacity: 1 }}
                                            className="flex gap-3"
                                        >
                                            <DallasAvatar size="sm" pulsate={false} />
                                            <div className="p-4 rounded-2xl rounded-tl-none bg-gradient-to-br from-zinc-800 to-zinc-900 border border-zinc-700">
                                                <div className="flex gap-1">
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0 }}
                                                    />
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0.2 }}
                                                    />
                                                    <motion.div
                                                        className="w-2 h-2 bg-purple-400 rounded-full"
                                                        animate={{ opacity: [0.3, 1, 0.3] }}
                                                        transition={{ duration: 1, repeat: Infinity, delay: 0.4 }}
                                                    />
                                                </div>
                                            </div>
                                        </motion.div>
                                    )}

                                    <div ref={messagesEndRef} />
                                </div>

                                {/* Input */}
                                <div className="p-4 border-t border-white/10 bg-zinc-900/50">
                                    <div className="flex gap-2">
                                        <input
                                            type="text"
                                            value={input}
                                            onChange={(e) => setInput(e.target.value)}
                                            onKeyDown={(e) => {
                                                if (e.key === "Enter" && !e.shiftKey) {
                                                    e.preventDefault()
                                                    handleSend()
                                                }
                                            }}
                                            placeholder="Fråga Dallas vad som helst..."
                                            className={cn(
                                                "flex-1 px-4 py-3 rounded-xl",
                                                "bg-zinc-800 border border-zinc-700",
                                                "text-white placeholder:text-zinc-500",
                                                "focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20",
                                                "transition-all duration-200"
                                            )}
                                        />
                                        <Button
                                            onClick={handleSend}
                                            disabled={!input.trim() || isTyping}
                                            className={cn(
                                                "px-4 py-3 rounded-xl",
                                                "bg-gradient-to-r from-purple-600 to-purple-500",
                                                "hover:from-purple-500 hover:to-purple-400",
                                                "disabled:opacity-50 disabled:cursor-not-allowed",
                                                "shadow-[0_0_20px_rgba(139,92,246,0.4)]"
                                            )}
                                        >
                                            <Send className="w-5 h-5" />
                                        </Button>
                                    </div>
                                    <p className="text-xs text-zinc-600 mt-2 text-center">
                                        Tryck Enter för att skicka, Shift+Enter för ny rad
                                    </p>
                                </div>
                            </>
                        )}
                    </motion.div>
                )}
            </AnimatePresence>
        </>
    )
}

export default DallasAssistant
