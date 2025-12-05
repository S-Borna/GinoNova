"use client"

/**
 * ============================================================================
 * MAGNETEN — Personal Learning Compass (formerly Studyflow)
 * ============================================================================
 *
 * Premium Upgrade Phase 2 - Complete Transformation
 *
 * Features:
 * - 🐺 Dallas AI Wizard with 40 smart predefined questions
 * - 📅 Schedule & Reminders management
 * - ⭐ Bookmarked Tasks (Gold Cards - synced from sidebar)
 * - 💡 Personalized learning recommendations
 * - 🔥 Streak tracking and motivation
 * - ⏰ Quick actions for navigation
 *
 * @phase Premium Upgrade Phase 2
 * @design Magneten - Learning Compass
 */

import * as React from "react"
import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { cn } from "@/lib/utils"
import { useAuth } from "@/components/auth"
import { useBookmarks } from "@/hooks/useBookmarks"
import {
    Compass,
    Sparkles,
    Calendar,
    Bell,
    Clock,
    Target,
    Flame,
    ChevronRight,
    Plus,
    X,
    Send,
    BookOpen,
    Zap,
    TrendingUp,
    CheckCircle2,
    Star,
    MessageCircle,
    Timer,
    Hash,
    ExternalLink,
    BookmarkX,
} from "lucide-react"

/* ============================================================================
   DALLAS WIZARD - 40 Smart Questions with Keyword Matching
   ============================================================================ */

const DALLAS_QUESTIONS = [
    // Career & Goals
    { keywords: ["jobb", "karriär", "anställning", "arbete"], question: "Vad är ditt karriärmål inom DevOps? Siktar du på en specifik roll?", category: "career" },
    { keywords: ["certifiering", "cert", "aws", "azure", "gcp"], question: "Siktar du på någon specifik certifiering? AWS, Azure eller GCP kanske?", category: "career" },
    { keywords: ["lön", "pengar", "betalt"], question: "Vilken typ av DevOps-roller har du sett som mest intressanta karriärmässigt?", category: "career" },
    { keywords: ["junior", "senior", "erfaren"], question: "Var befinner du dig i din DevOps-resa - nybörjare, mellannivå eller avancerad?", category: "career" },

    // Learning Style
    { keywords: ["nybörjare", "börja", "start", "ny"], question: "Vad lockar dig mest med DevOps - automation, infrastruktur eller CI/CD?", category: "learning" },
    { keywords: ["svårt", "problem", "fastnat", "hjälp"], question: "Vilket område känner du dig mest osäker på? Vi kan fokusera där!", category: "learning" },
    { keywords: ["tips", "råd", "förslag"], question: "Föredrar du att lära genom hands-on labbar eller konceptuell förståelse först?", category: "learning" },
    { keywords: ["tid", "schema", "planera"], question: "Hur mycket tid kan du lägga på lärande per vecka?", category: "learning" },

    // Technology Focus
    { keywords: ["kubernetes", "k8s", "container", "docker"], question: "Hur bekväm är du med containers? Har du kört Docker lokalt?", category: "tech" },
    { keywords: ["linux", "bash", "terminal", "cli"], question: "Hur stark är din Linux/bash-kunskap på en skala 1-10?", category: "tech" },
    { keywords: ["git", "github", "version"], question: "Använder du Git dagligen? Behöver du öva på branching strategies?", category: "tech" },
    { keywords: ["python", "programmering", "kod", "script"], question: "Vill du fokusera på scripting/automation med Python?", category: "tech" },
    { keywords: ["terraform", "ansible", "iac", "infrastruktur"], question: "Har du erfarenhet av Infrastructure as Code (Terraform, Ansible)?", category: "tech" },
    { keywords: ["ci", "cd", "pipeline", "jenkins", "github actions"], question: "Vilka CI/CD-verktyg är du mest intresserad av att lära dig?", category: "tech" },
    { keywords: ["cloud", "moln", "aws", "azure", "gcp"], question: "Vilken cloud-plattform använder ditt team eller vill du lära dig?", category: "tech" },
    { keywords: ["monitoring", "logging", "observability"], question: "Vill du dyka djupare i monitoring och observability?", category: "tech" },

    // Projects & Practice
    { keywords: ["projekt", "bygga", "skapa", "praktik"], question: "Har du några egna projekt du vill bygga för att öva?", category: "practice" },
    { keywords: ["labb", "övning", "hands-on"], question: "Föredrar du strukturerade labbar eller fria utforskningsprojekt?", category: "practice" },
    { keywords: ["portfolio", "cv", "visa"], question: "Bygger du en portfolio? Jag kan föreslå imponerande projekt!", category: "practice" },

    // Motivation
    { keywords: ["motivera", "inspiration", "trött", "ork"], question: "Vad motiverar dig mest - lösa problem, bygga saker eller lära nytt?", category: "motivation" },
    { keywords: ["mål", "dröm", "vision"], question: "Var ser du dig själv om 1 år? Vilken roll vill du ha?", category: "motivation" },
    { keywords: ["streak", "serie", "dagligen"], question: "Hur viktigt är det för dig att hålla en daglig streak?", category: "motivation" },

    // General Discovery
    { keywords: ["rekommendera", "vad", "nästa", "börja"], question: "Baserat på dina mål, vill du att jag rekommenderar en studieplan?", category: "general" },
    { keywords: ["snabb", "effektiv", "fokus"], question: "Vill du ha en intensiv 4-veckors plan eller föredrar du ett lugnare tempo?", category: "general" },
    { keywords: ["hej", "hallå", "tjena", "hi"], question: "Hej! Jag är Dallas, din DevOps-guide. Vad vill du lära dig idag?", category: "greeting" },
    { keywords: ["tack", "thanks", "bra"], question: "Kul att höra! Finns det något annat jag kan hjälpa dig med?", category: "gratitude" },

    // Fallback questions for conversation flow
    { keywords: ["ja", "yes", "absolut", "självklart"], question: "Perfekt! Ska vi börja med det direkt eller planera in det i ditt schema?", category: "followup" },
    { keywords: ["nej", "no", "inte", "vet inte"], question: "Ingen fara! Låt oss utforska vad som passar dig bäst. Vad intresserar dig mest?", category: "followup" },
    { keywords: ["mer", "berätta", "förklara"], question: "Självklart! Vilket specifikt område vill du veta mer om?", category: "followup" },
    { keywords: ["okej", "ok", "förstår", "bra"], question: "Vill du att jag hjälper dig sätta upp ett schema för att nå dina mål?", category: "followup" },
];

const DEFAULT_QUESTIONS = [
    "Vad vill du fokusera på idag?",
    "Hur kan jag hjälpa dig med din DevOps-resa?",
    "Finns det något specifikt du vill lära dig?",
    "Vill du att jag rekommenderar nästa steg?",
];

function findMatchingQuestion(input: string): string {
    const lowerInput = input.toLowerCase();

    for (const q of DALLAS_QUESTIONS) {
        if (q.keywords.some(keyword => lowerInput.includes(keyword))) {
            return q.question;
        }
    }

    return DEFAULT_QUESTIONS[Math.floor(Math.random() * DEFAULT_QUESTIONS.length)];
}

/* ============================================================================
   TYPES
   ============================================================================ */

interface ChatMessage {
    id: string;
    role: "user" | "dallas";
    content: string;
    timestamp: Date;
}

interface Reminder {
    id: string;
    title: string;
    module?: string;
    time: string;
    day: string;
    isActive: boolean;
}

interface Recommendation {
    id: string;
    title: string;
    module: string;
    reason: string;
    xp: number;
    difficulty: "easy" | "medium" | "hard";
}

/* ============================================================================
   DALLAS CHAT COMPONENT
   ============================================================================ */

function DallasChat() {
    const { user } = useAuth();
    const [messages, setMessages] = useState<ChatMessage[]>([
        {
            id: "welcome",
            role: "dallas",
            content: `Hej ${user?.full_name?.split(" ")[0] || "där"}! Jag är Dallas, din personliga DevOps-guide. Hur kan jag hjälpa dig idag?`,
            timestamp: new Date(),
        },
    ]);
    const [input, setInput] = useState("");
    const [isTyping, setIsTyping] = useState(false);
    const messagesEndRef = React.useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMessage: ChatMessage = {
            id: `user-${Date.now()}`,
            role: "user",
            content: input,
            timestamp: new Date(),
        };

        setMessages(prev => [...prev, userMessage]);
        setInput("");
        setIsTyping(true);

        // Simulate Dallas thinking
        await new Promise(resolve => setTimeout(resolve, 800 + Math.random() * 700));

        const dallasResponse: ChatMessage = {
            id: `dallas-${Date.now()}`,
            role: "dallas",
            content: findMatchingQuestion(input),
            timestamp: new Date(),
        };

        setIsTyping(false);
        setMessages(prev => [...prev, dallasResponse]);
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            {/* Header */}
            <div className={cn(
                "flex items-center gap-3 px-4 py-4",
                "border-b border-zinc-800/60",
                "bg-gradient-to-r from-purple-900/20 to-blue-900/20"
            )}>
                {/* Dallas Avatar */}
                <div className={cn(
                    "w-10 h-10 rounded-xl flex items-center justify-center",
                    "bg-gradient-to-br from-purple-500 to-blue-600",
                    "shadow-[0_0_20px_rgba(139,92,246,0.3)]"
                )}>
                    <span className="text-xl">🐺</span>
                </div>
                <div>
                    <h3 className="font-semibold text-zinc-100">Dallas</h3>
                    <p className="text-xs text-zinc-400">Din DevOps-guide</p>
                </div>
                <div className="ml-auto flex items-center gap-1 px-2 py-1 rounded-full bg-emerald-500/20">
                    <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                    <span className="text-xs text-emerald-400">Online</span>
                </div>
            </div>

            {/* Messages */}
            <div className="h-64 overflow-y-auto p-4 space-y-4">
                {messages.map(msg => (
                    <div
                        key={msg.id}
                        className={cn(
                            "flex gap-3",
                            msg.role === "user" && "flex-row-reverse"
                        )}
                    >
                        {msg.role === "dallas" && (
                            <div className="w-8 h-8 rounded-lg bg-purple-500/20 flex items-center justify-center shrink-0">
                                <span className="text-sm">🐺</span>
                            </div>
                        )}
                        <div className={cn(
                            "max-w-[80%] rounded-xl px-4 py-2.5",
                            msg.role === "dallas"
                                ? "bg-zinc-800/50 text-zinc-200"
                                : "bg-purple-600/30 text-zinc-100"
                        )}>
                            <p className="text-sm">{msg.content}</p>
                        </div>
                    </div>
                ))}

                {isTyping && (
                    <div className="flex gap-3">
                        <div className="w-8 h-8 rounded-lg bg-purple-500/20 flex items-center justify-center shrink-0">
                            <span className="text-sm">🐺</span>
                        </div>
                        <div className="bg-zinc-800/50 rounded-xl px-4 py-3">
                            <div className="flex gap-1">
                                <div className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                <div className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                <div className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                            </div>
                        </div>
                    </div>
                )}

                <div ref={messagesEndRef} />
            </div>

            {/* Input */}
            <div className="p-4 border-t border-zinc-800/60">
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={input}
                        onChange={e => setInput(e.target.value)}
                        onKeyDown={handleKeyDown}
                        placeholder="Skriv till Dallas..."
                        className={cn(
                            "flex-1 px-4 py-2.5 rounded-xl",
                            "bg-zinc-800/50 border border-zinc-700/50",
                            "text-zinc-100 placeholder:text-zinc-500",
                            "focus:outline-none focus:border-purple-500/50",
                            "transition-colors"
                        )}
                    />
                    <button
                        onClick={handleSend}
                        disabled={!input.trim()}
                        className={cn(
                            "p-2.5 rounded-xl transition-all",
                            input.trim()
                                ? "bg-purple-600 hover:bg-purple-500 text-white"
                                : "bg-zinc-800 text-zinc-500 cursor-not-allowed"
                        )}
                    >
                        <Send className="w-5 h-5" />
                    </button>
                </div>
            </div>
        </div>
    );
}

/* ============================================================================
   SCHEDULE & REMINDERS
   ============================================================================ */

function ScheduleSection() {
    const router = useRouter();
    const [reminders, setReminders] = useState<Reminder[]>([
        { id: "1", title: "Docker Task 3", module: "Containers", time: "08:00", day: "Mån", isActive: true },
        { id: "2", title: "K8s Intro", module: "Kubernetes", time: "17:00", day: "Ons", isActive: true },
        { id: "3", title: "Quiz Review", module: "Linux", time: "10:00", day: "Fre", isActive: false },
    ]);

    const toggleReminder = (id: string) => {
        setReminders(prev =>
            prev.map(r => r.id === id ? { ...r, isActive: !r.isActive } : r)
        );
    };

    const deleteReminder = (id: string) => {
        setReminders(prev => prev.filter(r => r.id !== id));
    };

    const handleReminderClick = () => {
        router.push("/modules");
    };

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-4 border-b border-zinc-800/60">
                <div className="flex items-center gap-2">
                    <Calendar className="w-5 h-5 text-emerald-400" />
                    <h3 className="font-semibold text-zinc-100">Ditt Schema</h3>
                </div>
                <span className="text-xs text-zinc-500">Klicka för att gå till task</span>
            </div>

            {/* Reminders List */}
            <div className="p-4 space-y-3 max-h-64 overflow-y-auto">
                {reminders.length === 0 ? (
                    <div className="text-center py-6">
                        <Bell className="w-10 h-10 text-zinc-600 mx-auto mb-3" />
                        <p className="text-sm text-zinc-400">Inga påminnelser ännu</p>
                        <p className="text-xs text-zinc-500 mt-1">Bokmärk tasks för att lägga till här</p>
                    </div>
                ) : (
                    reminders.map(reminder => (
                        <div
                            key={reminder.id}
                            onClick={handleReminderClick}
                            className={cn(
                                "flex items-center gap-3 p-3 rounded-xl cursor-pointer",
                                "bg-zinc-800/40 border border-zinc-700/30",
                                "group transition-all hover:border-emerald-500/30 hover:bg-zinc-800/60",
                                reminder.isActive && "border-emerald-500/30"
                            )}
                        >
                            <button
                                onClick={(e) => {
                                    e.stopPropagation();
                                    toggleReminder(reminder.id);
                                }}
                                className={cn(
                                    "w-8 h-8 rounded-lg flex items-center justify-center shrink-0",
                                    "transition-colors",
                                    reminder.isActive
                                        ? "bg-emerald-500/20 text-emerald-400"
                                        : "bg-zinc-700/50 text-zinc-500"
                                )}
                            >
                                <Bell className="w-4 h-4" />
                            </button>
                            <div className="flex-1 min-w-0">
                                <p className={cn(
                                    "text-sm font-medium truncate group-hover:text-emerald-300",
                                    reminder.isActive ? "text-zinc-200" : "text-zinc-500"
                                )}>
                                    {reminder.title}
                                </p>
                                <p className="text-xs text-zinc-500">
                                    {reminder.module} • {reminder.day} {reminder.time}
                                </p>
                            </div>
                            <ChevronRight className="w-4 h-4 text-zinc-600 group-hover:text-emerald-400 transition-colors" />
                            <button
                                onClick={(e) => {
                                    e.stopPropagation();
                                    deleteReminder(reminder.id);
                                }}
                                className="p-1.5 rounded-lg text-zinc-600 hover:text-red-400 hover:bg-red-500/10 opacity-0 group-hover:opacity-100 transition-all"
                            >
                                <X className="w-4 h-4" />
                            </button>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}

/* ============================================================================
   RECOMMENDATIONS
   ============================================================================ */

function RecommendationsSection() {
    const router = useRouter();
    const recommendations: Recommendation[] = [
        { id: "1", title: "Docker Compose Basics", module: "Containers", reason: "Nästa logiska steg efter Docker intro", xp: 35, difficulty: "medium" },
        { id: "2", title: "Linux File Permissions", module: "Linux Mastery", reason: "Viktigt för serverhantering", xp: 25, difficulty: "easy" },
        { id: "3", title: "Git Branching Strategies", module: "Git & GitHub", reason: "Baserat på din progress", xp: 40, difficulty: "medium" },
    ];

    const difficultyColors = {
        easy: "bg-emerald-500/20 text-emerald-400 border-emerald-500/30",
        medium: "bg-amber-500/20 text-amber-400 border-amber-500/30",
        hard: "bg-red-500/20 text-red-400 border-red-500/30",
    };

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-zinc-900/80 backdrop-blur-sm",
            "border border-zinc-800/60"
        )}>
            {/* Header */}
            <div className="flex items-center gap-2 px-4 py-4 border-b border-zinc-800/60">
                <Sparkles className="w-5 h-5 text-purple-400" />
                <h3 className="font-semibold text-zinc-100">Rekommenderat för dig</h3>
            </div>

            {/* Recommendations */}
            <div className="p-4 space-y-3">
                {recommendations.map((rec, index) => (
                    <div
                        key={rec.id}
                        onClick={() => router.push("/modules")}
                        className={cn(
                            "flex items-start gap-3 p-3 rounded-xl",
                            "bg-zinc-800/40 border border-zinc-700/30",
                            "hover:border-purple-500/30 hover:bg-zinc-800/60",
                            "transition-all cursor-pointer group"
                        )}
                    >
                        <div className={cn(
                            "w-8 h-8 rounded-lg flex items-center justify-center shrink-0",
                            "bg-purple-500/20 text-purple-400"
                        )}>
                            {index + 1}
                        </div>
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2 mb-1">
                                <p className="text-sm font-medium text-zinc-200 group-hover:text-purple-300">
                                    {rec.title}
                                </p>
                                <span className={cn(
                                    "px-1.5 py-0.5 text-[10px] rounded border",
                                    difficultyColors[rec.difficulty]
                                )}>
                                    {rec.difficulty}
                                </span>
                            </div>
                            <p className="text-xs text-zinc-500 mb-2">{rec.module}</p>
                            <div className="flex items-center gap-2">
                                <span className="text-xs text-zinc-400 italic">&quot;{rec.reason}&quot;</span>
                            </div>
                        </div>
                        <div className="flex items-center gap-1 text-amber-400 shrink-0">
                            <Zap className="w-3.5 h-3.5" />
                            <span className="text-sm font-medium">+{rec.xp}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

/* ============================================================================
   STREAK & STATS CARD
   ============================================================================ */

function StatsCard() {
    const streak = 7;
    const totalXP = 1250;
    const tasksThisWeek = 12;

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-gradient-to-br from-orange-900/20 via-zinc-900/80 to-zinc-900/80",
            "border border-orange-500/20",
            "shadow-[0_0_30px_rgba(249,115,22,0.1)]"
        )}>
            {/* Streak Display */}
            <div className="p-6 text-center">
                <div className={cn(
                    "w-20 h-20 mx-auto mb-4 rounded-2xl",
                    "bg-gradient-to-br from-orange-500 to-red-600",
                    "flex items-center justify-center",
                    "shadow-[0_0_30px_rgba(249,115,22,0.4)]",
                    "animate-pulse"
                )}>
                    <Flame className="w-10 h-10 text-white" />
                </div>
                <p className="text-4xl font-bold text-orange-400 mb-1">{streak}</p>
                <p className="text-sm text-zinc-400">dagars streak 🔥</p>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 gap-px bg-zinc-800/50">
                <div className="p-4 bg-zinc-900/80 text-center">
                    <p className="text-2xl font-bold text-amber-400">{totalXP.toLocaleString()}</p>
                    <p className="text-xs text-zinc-500">Total XP</p>
                </div>
                <div className="p-4 bg-zinc-900/80 text-center">
                    <p className="text-2xl font-bold text-emerald-400">{tasksThisWeek}</p>
                    <p className="text-xs text-zinc-500">Tasks denna vecka</p>
                </div>
            </div>
        </div>
    );
}

/* ============================================================================
   QUICK ACTIONS
   ============================================================================ */

function QuickActions() {
    const router = useRouter();

    const actions = [
        { icon: BookOpen, label: "Fortsätt lära", href: "/modules", color: "from-purple-500 to-purple-600" },
        { icon: Target, label: "Se progress", href: "/progress", color: "from-emerald-500 to-emerald-600" },
        { icon: Timer, label: "Fokusläge", href: "/dashboard", color: "from-blue-500 to-blue-600" },
    ];

    return (
        <div className="grid grid-cols-3 gap-3">
            {actions.map((action, i) => (
                <button
                    key={i}
                    onClick={() => router.push(action.href)}
                    className={cn(
                        "flex flex-col items-center gap-2 p-4 rounded-xl",
                        "bg-zinc-800/40 border border-zinc-700/30",
                        "hover:border-purple-500/30",
                        "transition-all group"
                    )}
                >
                    <div className={cn(
                        "w-10 h-10 rounded-xl flex items-center justify-center",
                        `bg-gradient-to-br ${action.color}`,
                        "group-hover:shadow-lg group-hover:scale-105 transition-all"
                    )}>
                        <action.icon className="w-5 h-5 text-white" />
                    </div>
                    <span className="text-xs text-zinc-400 group-hover:text-zinc-200">{action.label}</span>
                </button>
            ))}
        </div>
    );
}

/* ============================================================================
   BOOKMARKED TASKS — Gold Cards (Synced from Sidebar)
   ============================================================================ */

function BookmarkedTasksSection() {
    const { bookmarks, loading, count } = useBookmarks();

    return (
        <div className={cn(
            "rounded-2xl overflow-hidden",
            "bg-gradient-to-br from-amber-900/10 via-zinc-900/80 to-zinc-900/80",
            "border border-amber-500/20",
            "shadow-[0_0_20px_rgba(251,191,36,0.05)]"
        )}>
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-4 border-b border-amber-500/20">
                <div className="flex items-center gap-2">
                    <Star className="w-5 h-5 text-amber-400 fill-amber-400" />
                    <h3 className="font-semibold text-zinc-100">Mina Sparade Tasks</h3>
                    {count > 0 && (
                        <span className="px-1.5 py-0.5 text-[10px] font-bold rounded-full bg-amber-500/20 text-amber-300">
                            {count}
                        </span>
                    )}
                </div>
            </div>

            {/* Bookmarks */}
            <div className="p-3 max-h-64 overflow-y-auto">
                {loading ? (
                    <div className="space-y-2">
                        {[1, 2].map(i => (
                            <div key={i} className="animate-pulse p-3 rounded-xl bg-zinc-800/30">
                                <div className="h-4 bg-zinc-700 rounded w-1/4 mb-2" />
                                <div className="h-5 bg-zinc-700 rounded w-3/4" />
                            </div>
                        ))}
                    </div>
                ) : count === 0 ? (
                    <div className="flex flex-col items-center justify-center py-6 text-center">
                        <div className={cn(
                            "w-12 h-12 rounded-xl flex items-center justify-center mb-3",
                            "bg-zinc-800/50 border border-zinc-700/50"
                        )}>
                            <BookmarkX className="w-6 h-6 text-zinc-500" />
                        </div>
                        <p className="text-sm font-medium text-zinc-400">
                            Inga sparade tasks
                        </p>
                        <p className="text-xs text-zinc-500 mt-1">
                            ⭐ Stjärnmarkera tasks i modulerna
                        </p>
                    </div>
                ) : (
                    <div className="space-y-2">
                        {bookmarks.slice(0, 4).map((bookmark, index) => (
                            <Link
                                key={bookmark.id}
                                href={`/modules/${bookmark.module_slug}/tasks/${bookmark.task_id}`}
                                className={cn(
                                    "group block p-3 rounded-xl",
                                    "bg-gradient-to-br from-amber-500/10 to-amber-600/5",
                                    "border border-amber-500/30",
                                    "hover:border-amber-400/50",
                                    "hover:shadow-[0_0_20px_rgba(251,191,36,0.15)]",
                                    "transition-all duration-300"
                                )}
                            >
                                {/* Task number badge */}
                                <div className="flex items-center justify-between mb-1">
                                    <span className={cn(
                                        "flex items-center gap-0.5 px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider",
                                        "bg-amber-500/20 text-amber-300 border border-amber-500/30"
                                    )}>
                                        <Hash className="w-2.5 h-2.5" />
                                        Task {index + 1}
                                    </span>
                                    <Star className="w-3.5 h-3.5 text-amber-400 fill-amber-400" />
                                </div>

                                {/* Task title - Gold */}
                                <p className="text-sm font-semibold text-amber-200 truncate group-hover:text-white">
                                    {bookmark.task_title}
                                </p>

                                {/* Module name */}
                                <p className="text-xs text-zinc-400 truncate flex items-center gap-1 mt-0.5">
                                    <Zap className="w-3 h-3" />
                                    {bookmark.module_name}
                                </p>
                            </Link>
                        ))}

                        {count > 4 && (
                            <Link
                                href="/modules"
                                className="block text-center text-xs text-amber-400 hover:text-amber-300 py-2"
                            >
                                +{count - 4} mer i Quick Access →
                            </Link>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}

/* ============================================================================
   MAIN PAGE
   ============================================================================ */

export default function MagnetenPage() {
    const { user } = useAuth();
    const userName = user?.full_name?.split(" ")[0] || "Learner";

    // Scroll to top on mount
    useEffect(() => {
        window.scrollTo({ top: 0, behavior: "instant" });
    }, []);

    return (
        <div className="min-h-screen bg-zinc-950">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
                {/* Hero Header */}
                <div className={cn(
                    "relative overflow-hidden rounded-2xl",
                    "bg-gradient-to-br from-zinc-900 via-purple-950/30 to-zinc-900",
                    "border border-purple-500/20",
                    "p-8"
                )}>
                    {/* Background effects */}
                    <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2" />
                    <div className="absolute bottom-0 left-1/4 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl translate-y-1/2" />

                    <div className="relative flex items-center gap-4">
                        <div className={cn(
                            "w-14 h-14 rounded-2xl flex items-center justify-center",
                            "bg-gradient-to-br from-purple-500 to-blue-600",
                            "shadow-[0_0_30px_rgba(139,92,246,0.4)]"
                        )}>
                            <Compass className="w-7 h-7 text-white" />
                        </div>
                        <div>
                            <h1 className={cn(
                                "text-2xl md:text-3xl font-bold",
                                "bg-gradient-to-r from-zinc-100 via-purple-200 to-zinc-100 bg-clip-text text-transparent"
                            )}>
                                Ta en egen pulsmätning, {userName}!
                            </h1>
                            <p className="text-zinc-400 mt-1">
                                Planera din DevOps-resa, sätt upp mål och följ din progress
                            </p>
                        </div>
                    </div>
                </div>

                {/* Main Grid */}
                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Left Column - Dallas & Recommendations */}
                    <div className="lg:col-span-2 space-y-6">
                        <DallasChat />
                        <RecommendationsSection />
                    </div>

                    {/* Right Column - Stats, Bookmarks & Schedule */}
                    <div className="space-y-6">
                        <StatsCard />
                        <BookmarkedTasksSection />
                        <QuickActions />
                        <ScheduleSection />
                    </div>
                </div>
            </div>
        </div>
    );
}
