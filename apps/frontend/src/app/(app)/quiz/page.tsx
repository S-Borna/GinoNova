"use client";

/**
 * ============================================================================
 * AI QUIZ GENERATOR — DOE25 PREMIUM DESIGN
 * ============================================================================
 *
 * Premium Quiz page with DOE25 Tenta-style design:
 * - COSMIC background with aurora effects
 * - Hero header with stats grid
 * - Premium progress tracking
 *
 * @phase DOE25-REDESIGN
 */

import { useState, useEffect } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import {
  Brain,
  Sparkles,
  BookOpen,
  CheckCircle2,
  XCircle,
  ChevronRight,
  RotateCcw,
  Loader2,
  Lock,
  Zap,
  Target,
  GraduationCap,
  ArrowLeft,
  Trophy,
  Clock,
  Play,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { getToken } from "@/lib/auth";
import { CosmicAurora } from "@/components/ui/cosmic-aurora";
import { cn } from "@/lib/utils";

const API_BASE_URL = "https://saas-project-production-31f8.up.railway.app";

/* ============================================================================
   STATS CARD — Same as DOE25 Tenta
   ============================================================================ */

function StatCard({
  icon,
  label,
  value,
  color
}: {
  icon: React.ReactNode
  label: string
  value: string | number
  color: string
}) {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className={cn(
        "flex items-center gap-4 p-4 rounded-xl",
        "bg-white/5 border border-white/10",
        "hover:border-white/20 transition-colors"
      )}
    >
      <div className={cn(
        "w-12 h-12 rounded-xl flex items-center justify-center",
        `bg-gradient-to-br ${color}`
      )}>
        {icon}
      </div>
      <div>
        <p className="text-2xl font-bold text-white">{value}</p>
        <p className="text-sm text-zinc-400">{label}</p>
      </div>
    </motion.div>
  )
}

interface Module {
  slug: string;
  title: string;
  description: string;
}

interface MCQQuestion {
  question: string;
  options: string[];
  correct: string;
  explanation: string;
}

interface FlashcardQuestion {
  front: string;
  back: string;
  hint?: string;
}

type Question = MCQQuestion | FlashcardQuestion;

interface QuizState {
  questions: Question[];
  currentIndex: number;
  score: number;
  answers: (string | null)[];
  showResult: boolean;
  flipped: boolean[];
}

export default function QuizPage() {
  const [hasAccess, setHasAccess] = useState<boolean | null>(null);
  const [accessMessage, setAccessMessage] = useState("");
  const [modules, setModules] = useState<Module[]>([]);
  const [selectedModule, setSelectedModule] = useState<string>("");
  const [quizType, setQuizType] = useState<"mcq" | "flashcard">("mcq");
  const [difficulty, setDifficulty] = useState<"beginner" | "intermediate" | "advanced">("intermediate");
  const [questionCount, setQuestionCount] = useState(10);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [quiz, setQuiz] = useState<QuizState | null>(null);

  // Check access on mount
  useEffect(() => {
    const init = async () => {
      const token = getToken();
      console.log("Quiz init - token:", token ? "EXISTS" : "NULL");

      if (!token) {
        console.log("No token, skipping API calls");
        setHasAccess(false);
        setAccessMessage("Please log in to access the quiz");
        return;
      }

      // Fetch both in parallel
      try {
        const [accessRes, modulesRes] = await Promise.all([
          fetch(`${API_BASE_URL}/api/quiz/access`, {
            headers: { Authorization: `Bearer ${token}` },
          }),
          fetch(`${API_BASE_URL}/api/quiz/modules`, {
            headers: { Authorization: `Bearer ${token}` },
          }),
        ]);

        console.log("Access status:", accessRes.status);
        console.log("Modules status:", modulesRes.status);

        if (accessRes.ok) {
          const accessData = await accessRes.json();
          console.log("Access data:", accessData);
          setHasAccess(accessData.has_access);
          setAccessMessage(accessData.message);
        } else {
          setHasAccess(false);
          setAccessMessage("Could not verify access");
        }

        if (modulesRes.ok) {
          const modulesData = await modulesRes.json();
          console.log("Modules data:", modulesData);
          setModules(modulesData.modules || []);
        }
      } catch (err) {
        console.error("Init error:", err);
        setHasAccess(false);
        setAccessMessage("Connection error");
      }
    };
    init();
  }, []);

  const checkAccess = async () => {
    // Now handled in init
  };

  const fetchModules = async () => {
    // Now handled in init
  };

  const generateQuiz = async () => {
    if (!selectedModule) return;

    setLoading(true);
    setError(null);

    try {
      const token = getToken();
      const res = await fetch(`${API_BASE_URL}/api/quiz/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          module_slug: selectedModule,
          quiz_type: quizType,
          count: questionCount,
          difficulty,
        }),
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.detail || "Failed to generate quiz");
      }

      const data = await res.json();
      setQuiz({
        questions: data.questions,
        currentIndex: 0,
        score: 0,
        answers: new Array(data.questions.length).fill(null),
        showResult: false,
        flipped: new Array(data.questions.length).fill(false),
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to generate quiz");
    } finally {
      setLoading(false);
    }
  };

  const handleMCQAnswer = (answer: string) => {
    if (!quiz) return;

    const currentQuestion = quiz.questions[quiz.currentIndex] as MCQQuestion;
    const isCorrect = answer === currentQuestion.correct;

    const newAnswers = [...quiz.answers];
    newAnswers[quiz.currentIndex] = answer;

    setQuiz({
      ...quiz,
      answers: newAnswers,
      score: isCorrect ? quiz.score + 1 : quiz.score,
    });
  };

  const handleFlipCard = () => {
    if (!quiz) return;

    const newFlipped = [...quiz.flipped];
    newFlipped[quiz.currentIndex] = !newFlipped[quiz.currentIndex];

    setQuiz({
      ...quiz,
      flipped: newFlipped,
    });
  };

  const nextQuestion = () => {
    if (!quiz) return;

    if (quiz.currentIndex < quiz.questions.length - 1) {
      setQuiz({
        ...quiz,
        currentIndex: quiz.currentIndex + 1,
      });
    } else {
      setQuiz({
        ...quiz,
        showResult: true,
      });
    }
  };

  const resetQuiz = () => {
    setQuiz(null);
    setSelectedModule("");
  };

  // No access view - DOE25 Premium styled
  if (hasAccess === false) {
    return (
      <div className="min-h-screen bg-[#05050a] relative">
        <CosmicAurora />
        <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {/* Back */}
          <Link
            href="/learn"
            className={cn(
              "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
              "text-zinc-400 hover:text-white",
              "bg-white/5 hover:bg-white/10 border border-white/10",
              "transition-all duration-300"
            )}
          >
            <ArrowLeft className="w-4 h-4" />
            Tillbaka till Learning
          </Link>

          {/* Hero Header — Locked */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
              "relative overflow-hidden rounded-3xl mb-8",
              "bg-gradient-to-br from-purple-500/10 via-pink-500/10 to-zinc-500/10",
              "border border-purple-500/20",
              "p-8 md:p-12"
            )}
          >
            {/* Background Glow */}
            <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/20 rounded-full blur-[100px]" />

            <div className="relative text-center">
              <motion.div
                className={cn(
                  "w-24 h-24 mx-auto mb-6 rounded-3xl flex items-center justify-center",
                  "bg-gradient-to-br from-purple-500/30 to-pink-500/30",
                  "border border-purple-500/40 shadow-lg shadow-purple-500/20"
                )}
                animate={{
                  boxShadow: [
                    '0 0 20px rgba(168,85,247,0.3)',
                    '0 0 35px rgba(168,85,247,0.5)',
                    '0 0 20px rgba(168,85,247,0.3)'
                  ]
                }}
                transition={{ duration: 2.5, repeat: Infinity }}
              >
                <Lock className="w-12 h-12 text-purple-400" />
              </motion.div>

              <div className="flex items-center justify-center gap-3 mb-4">
                <span className="px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 text-purple-400 text-xs font-bold uppercase tracking-wider">
                  Premium
                </span>
              </div>

              <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                AI Quiz Generator
              </h1>

              <p className="text-lg text-zinc-300 max-w-2xl mx-auto mb-8">
                {accessMessage}
              </p>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-2xl mx-auto">
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.2 }}
                  className="flex items-center gap-3 p-4 rounded-xl bg-white/5 border border-white/10"
                >
                  <Sparkles className="w-6 h-6 text-yellow-500" />
                  <span className="text-zinc-300">AI-genererade frågor</span>
                </motion.div>
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.3 }}
                  className="flex items-center gap-3 p-4 rounded-xl bg-white/5 border border-white/10"
                >
                  <Brain className="w-6 h-6 text-purple-500" />
                  <span className="text-zinc-300">Adaptiv svårighet</span>
                </motion.div>
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.4 }}
                  className="flex items-center gap-3 p-4 rounded-xl bg-white/5 border border-white/10"
                >
                  <Target className="w-6 h-6 text-green-500" />
                  <span className="text-zinc-300">Modul-specifikt</span>
                </motion.div>
              </div>

              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.5 }}
              >
                <Badge className="mt-8 bg-gradient-to-r from-purple-600 to-pink-600 shadow-[0_0_15px_rgba(168,85,247,0.4)] text-lg px-6 py-2">
                  Kommer snart
                </Badge>
              </motion.div>
            </div>
          </motion.div>
        </div>
      </div>
    );
  }

  // Loading access check - Cosmic styled
  if (hasAccess === null) {
    return (
      <div className="min-h-screen bg-[#05050a] relative flex items-center justify-center">
        <CosmicAurora />
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
        >
          <Loader2 className="w-8 h-8 text-purple-500" />
        </motion.div>
      </div>
    );
  }

  // Quiz results view - DOE25 Premium celebration
  if (quiz?.showResult) {
    const percentage = Math.round((quiz.score / quiz.questions.length) * 100);

    return (
      <div className="min-h-screen bg-[#05050a] relative">
        <CosmicAurora />
        <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {/* Hero Header — Results */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className={cn(
              "relative overflow-hidden rounded-3xl",
              "bg-gradient-to-br from-emerald-500/10 via-purple-500/10 to-cyan-500/10",
              "border border-emerald-500/20",
              "p-8 md:p-12"
            )}
          >
            {/* Background Glow */}
            <div className="absolute top-0 right-0 w-96 h-96 bg-emerald-500/20 rounded-full blur-[100px]" />
            <div className="absolute bottom-0 left-0 w-64 h-64 bg-purple-500/10 rounded-full blur-[80px]" />

            <div className="relative text-center">
              <motion.div
                className={cn(
                  "w-24 h-24 mx-auto mb-6 rounded-3xl flex items-center justify-center",
                  "bg-gradient-to-br from-emerald-500/30 to-green-500/30",
                  "border border-emerald-500/40 shadow-lg shadow-emerald-500/20"
                )}
                animate={{
                  boxShadow: [
                    '0 0 25px rgba(52,211,153,0.3)',
                    '0 0 45px rgba(52,211,153,0.5)',
                    '0 0 25px rgba(52,211,153,0.3)'
                  ],
                  scale: [1, 1.05, 1]
                }}
                transition={{ duration: 2.5, repeat: Infinity }}
              >
                <GraduationCap className="w-12 h-12 text-emerald-400" />
              </motion.div>

              <div className="flex items-center justify-center gap-3 mb-4">
                <span className="px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider">
                  Quiz Klar!
                </span>
              </div>

              <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                Bra jobbat!
              </h1>

              <p className="text-lg text-zinc-300 mb-6">
                Du fick {quiz.score} av {quiz.questions.length} rätt
              </p>

              <motion.div
                className="text-7xl font-black bg-gradient-to-r from-emerald-400 via-green-400 to-cyan-400 bg-clip-text text-transparent mb-8"
                animate={{ scale: [1, 1.05, 1] }}
                transition={{ duration: 2, repeat: Infinity }}
              >
                {percentage}%
              </motion.div>

              {/* Stats Grid */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                <StatCard
                  icon={<CheckCircle2 className="w-6 h-6 text-white" />}
                  label="Rätt svar"
                  value={quiz.score}
                  color="from-emerald-500 to-green-500"
                />
                <StatCard
                  icon={<XCircle className="w-6 h-6 text-white" />}
                  label="Fel svar"
                  value={quiz.questions.length - quiz.score}
                  color="from-red-500 to-orange-500"
                />
                <StatCard
                  icon={<Target className="w-6 h-6 text-white" />}
                  label="Totalt"
                  value={quiz.questions.length}
                  color="from-purple-500 to-pink-500"
                />
                <StatCard
                  icon={<Trophy className="w-6 h-6 text-white" />}
                  label="Procent"
                  value={`${percentage}%`}
                  color="from-amber-500 to-yellow-500"
                />
              </div>

              {/* Progress Bar */}
              <div className="max-w-md mx-auto mb-8">
                <div className="h-4 bg-zinc-800 rounded-full overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${percentage}%` }}
                    transition={{ duration: 1, ease: "easeOut" }}
                    className="h-full bg-gradient-to-r from-emerald-500 via-green-500 to-cyan-500 rounded-full"
                  />
                </div>
              </div>

              <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                <Button
                  onClick={resetQuiz}
                  className={cn(
                    "px-8 py-6 rounded-xl text-lg font-semibold",
                    "bg-gradient-to-r from-purple-600 to-cyan-600",
                    "hover:from-purple-500 hover:to-cyan-500",
                    "shadow-lg shadow-purple-500/30"
                  )}
                >
                  <RotateCcw className="w-5 h-5 mr-2" />
                  Nytt Quiz
                </Button>
              </motion.div>
            </div>
          </motion.div>
        </div>
      </div>
    );
  }

  // Active quiz view - Cosmic
  if (quiz) {
    const currentQuestion = quiz.questions[quiz.currentIndex];
    const progress = ((quiz.currentIndex + 1) / quiz.questions.length) * 100;

    return (
      <div className="min-h-screen bg-[#05050a] relative">
        <CosmicAurora />
        <div className="relative z-10 p-8">
          <div className="max-w-3xl mx-auto">
            <div className="mb-6">
              <div className="flex justify-between text-sm text-zinc-400 mb-2">
                <span>Question {quiz.currentIndex + 1} of {quiz.questions.length}</span>
                <motion.span
                  key={quiz.score}
                  initial={{ scale: 1.2 }}
                  animate={{ scale: 1 }}
                  className="text-purple-400"
                >
                  Score: {quiz.score}
                </motion.span>
              </div>
              <div className="h-2 bg-zinc-800/50 rounded-full overflow-hidden">
                <motion.div
                  className="h-full bg-gradient-to-r from-purple-500 to-pink-500"
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                />
              </div>
            </div>

            <AnimatePresence mode="wait">
              <motion.div
                key={quiz.currentIndex}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -20 }}
                transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
              >
                {quizType === "mcq" ? (
                  <Card className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border-purple-500/30 shadow-[0_0_30px_rgba(168,85,247,0.1)]">
                    <CardHeader>
                      <CardTitle className="text-xl text-white">
                        {(currentQuestion as MCQQuestion).question}
                      </CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      {(currentQuestion as MCQQuestion).options.map((option, idx) => {
                        const letter = option.charAt(0);
                        const isSelected = quiz.answers[quiz.currentIndex] === letter;
                        const isCorrect = letter === (currentQuestion as MCQQuestion).correct;
                        const showResult = quiz.answers[quiz.currentIndex] !== null;

                        return (
                          <motion.button
                            key={idx}
                            whileHover={!showResult ? { scale: 1.01 } : {}}
                            whileTap={!showResult ? { scale: 0.99 } : {}}
                            onClick={() => !showResult && handleMCQAnswer(letter)}
                            disabled={showResult}
                            className={`w-full p-4 rounded-xl text-left transition-all duration-300 ${showResult
                              ? isCorrect
                                ? "bg-emerald-500/20 border-emerald-500/50 shadow-[0_0_20px_rgba(52,211,153,0.2)]"
                                : isSelected
                                  ? "bg-red-500/20 border-red-500/50"
                                  : "bg-zinc-800/30 border-zinc-700/30"
                              : isSelected
                                ? "bg-purple-500/20 border-purple-500/50 shadow-[0_0_15px_rgba(168,85,247,0.2)]"
                                : "bg-[#0a0a0f] border-zinc-700/30 hover:bg-zinc-800/50 hover:border-purple-500/30"
                              } border`}
                          >
                            <div className="flex items-center gap-3">
                              {showResult && isCorrect && (
                                <motion.div initial={{ scale: 0 }} animate={{ scale: 1 }}>
                                  <CheckCircle2 className="w-5 h-5 text-green-500" />
                                </motion.div>
                              )}
                              {showResult && isSelected && !isCorrect && (
                                <motion.div initial={{ scale: 0 }} animate={{ scale: 1 }}>
                                  <XCircle className="w-5 h-5 text-red-500" />
                                </motion.div>
                              )}
                              <span className="text-white">{option}</span>
                            </div>
                          </motion.button>
                        );
                      })}

                      {quiz.answers[quiz.currentIndex] !== null && (
                        <motion.div
                          initial={{ opacity: 0, y: 10 }}
                          animate={{ opacity: 1, y: 0 }}
                          className="mt-4 p-4 bg-zinc-800/30 rounded-xl border border-zinc-700/30"
                        >
                          <p className="text-zinc-300 text-sm">
                            <strong className="text-purple-300">Explanation:</strong> {(currentQuestion as MCQQuestion).explanation}
                          </p>
                        </motion.div>
                      )}

                      {quiz.answers[quiz.currentIndex] !== null && (
                        <motion.div
                          initial={{ opacity: 0 }}
                          animate={{ opacity: 1 }}
                          transition={{ delay: 0.2 }}
                        >
                          <Button
                            onClick={nextQuestion}
                            className="w-full mt-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-[0_0_20px_rgba(168,85,247,0.3)]"
                          >
                            {quiz.currentIndex < quiz.questions.length - 1 ? (
                              <>Next <ChevronRight className="w-4 h-4 ml-2" /></>
                            ) : (
                              <>See Results</>
                            )}
                          </Button>
                        </motion.div>
                      )}
                    </CardContent>
                  </Card>
                ) : (
                  <div className="space-y-4">
                    <Card
                      onClick={handleFlipCard}
                      className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border-purple-500/30 min-h-[300px] flex items-center justify-center cursor-pointer hover:border-purple-400/50 transition-all duration-300 hover:shadow-[0_0_30px_rgba(168,85,247,0.2)]"
                    >
                      <CardContent className="text-center p-8">
                        {!quiz.flipped[quiz.currentIndex] ? (
                          <motion.div
                            key="front"
                            initial={{ rotateY: 180 }}
                            animate={{ rotateY: 0 }}
                            transition={{ duration: 0.4 }}
                          >
                            <Badge className="mb-4 bg-purple-500/30 border border-purple-500/40">Front</Badge>
                            <p className="text-2xl text-white">
                              {(currentQuestion as FlashcardQuestion).front}
                            </p>
                            {(currentQuestion as FlashcardQuestion).hint && (
                              <p className="text-sm text-purple-300/60 mt-4">
                                Hint: {(currentQuestion as FlashcardQuestion).hint}
                              </p>
                            )}
                            <p className="text-zinc-500 mt-6 text-sm">Click to flip</p>
                          </motion.div>
                        ) : (
                          <motion.div
                            key="back"
                            initial={{ rotateY: -180 }}
                            animate={{ rotateY: 0 }}
                            transition={{ duration: 0.4 }}
                          >
                            <Badge className="mb-4 bg-emerald-500/30 border border-emerald-500/40">Back</Badge>
                            <p className="text-xl text-white">
                              {(currentQuestion as FlashcardQuestion).back}
                            </p>
                            <p className="text-zinc-500 mt-6 text-sm">Click to flip back</p>
                          </motion.div>
                        )}
                      </CardContent>
                    </Card>

                    <Button
                      onClick={(e) => { e.stopPropagation(); nextQuestion(); }}
                      className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-[0_0_20px_rgba(168,85,247,0.3)]"
                    >
                      {quiz.currentIndex < quiz.questions.length - 1 ? (
                        <>Next Card <ChevronRight className="w-4 h-4 ml-2" /></>
                      ) : (
                        <>Finish</>
                      )}
                    </Button>
                  </div>
                )}
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    );
  }

  // Quiz setup view - DOE25 Premium styled
  return (
    <div className="min-h-screen bg-[#05050a] relative">
      <CosmicAurora />
      <div className="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Back */}
        <Link
          href="/learn"
          className={cn(
            "inline-flex items-center gap-2 text-sm mb-8 px-4 py-2 rounded-xl",
            "text-zinc-400 hover:text-white",
            "bg-white/5 hover:bg-white/10 border border-white/10",
            "transition-all duration-300"
          )}
        >
          <ArrowLeft className="w-4 h-4" />
          Tillbaka till Learning
        </Link>

        {/* Hero Header — DOE25 Style */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className={cn(
            "relative overflow-hidden rounded-3xl mb-8",
            "bg-gradient-to-br from-purple-500/10 via-pink-500/10 to-cyan-500/10",
            "border border-purple-500/20",
            "p-8 md:p-12"
          )}
        >
          {/* Background Glow */}
          <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/20 rounded-full blur-[100px]" />
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-pink-500/10 rounded-full blur-[80px]" />

          <div className="relative">
            <div className="flex flex-col md:flex-row md:items-start gap-6 mb-8">
              {/* Icon */}
              <motion.div
                whileHover={{ scale: 1.05, rotate: 5 }}
                className={cn(
                  "w-24 h-24 rounded-3xl flex items-center justify-center shrink-0",
                  "bg-gradient-to-br from-purple-500/30 to-pink-500/30",
                  "border border-purple-500/40 shadow-lg shadow-purple-500/20"
                )}
              >
                <span className="text-6xl">🧠</span>
              </motion.div>

              <div className="flex-1">
                <div className="flex items-center gap-3 mb-3">
                  <span className="px-3 py-1 rounded-full bg-purple-500/20 border border-purple-500/30 text-purple-400 text-xs font-bold uppercase tracking-wider">
                    AI-Powered
                  </span>
                  <span className="px-3 py-1 rounded-full bg-pink-500/20 border border-pink-500/30 text-pink-400 text-xs font-bold">
                    {modules.length} Moduler
                  </span>
                </div>

                <h1 className="text-3xl md:text-5xl font-black text-white mb-4">
                  AI Quiz Generator
                </h1>

                <p className="text-lg text-zinc-300 max-w-2xl mb-6">
                  Testa dina kunskaper med AI-genererade frågor. Välj modul,
                  svårighetsgrad och antal frågor för att skapa ett personligt quiz.
                </p>
              </div>
            </div>

            {/* Stats Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <StatCard
                icon={<BookOpen className="w-6 h-6 text-white" />}
                label="Moduler"
                value={modules.length}
                color="from-purple-500 to-pink-500"
              />
              <StatCard
                icon={<Target className="w-6 h-6 text-white" />}
                label="Svårighetsgrader"
                value="3"
                color="from-emerald-500 to-green-500"
              />
              <StatCard
                icon={<Zap className="w-6 h-6 text-white" />}
                label="Quiz-typer"
                value="2"
                color="from-amber-500 to-orange-500"
              />
              <StatCard
                icon={<Brain className="w-6 h-6 text-white" />}
                label="AI-driven"
                value="✓"
                color="from-cyan-500 to-blue-500"
              />
            </div>
          </div>
        </motion.div>

        {/* Quiz Configuration Card */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
        >
          <Card className="bg-[#0a0a0f] border-purple-500/30 shadow-[0_0_40px_rgba(168,85,247,0.1)]">
            <CardHeader>
              <CardTitle className="text-white flex items-center gap-2">
                <motion.div
                  animate={{
                    boxShadow: ['0 0 10px rgba(168,85,247,0.3)', '0 0 20px rgba(168,85,247,0.5)', '0 0 10px rgba(168,85,247,0.3)']
                  }}
                  transition={{ duration: 2, repeat: Infinity }}
                  className="p-1 rounded-lg"
                >
                  <Brain className="w-5 h-5 text-purple-400" />
                </motion.div>
                Konfigurera ditt Quiz
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {error && (
                <motion.div
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  className="p-4 bg-red-500/10 border border-red-500/50 rounded-xl text-red-400"
                >
                  {error}
                </motion.div>
              )}

              <div className="space-y-2">
                <label className="text-sm text-purple-200/60">Välj Modul ({modules.length} tillgängliga)</label>
                <Select value={selectedModule} onValueChange={setSelectedModule}>
                  <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60 focus:ring-purple-500/20">
                    <SelectValue placeholder="Välj en modul..." />
                  </SelectTrigger>
                  <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                    {modules.map((module) => (
                      <SelectItem key={module.slug} value={module.slug} className="text-white hover:bg-purple-500/20">
                        {module.title}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <label className="text-sm text-purple-200/60">Quiz-typ</label>
                <Select value={quizType} onValueChange={(v: string) => setQuizType(v as "mcq" | "flashcard")}>
                  <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                    <SelectItem value="mcq" className="text-white hover:bg-purple-500/20">Flervalsfrågor</SelectItem>
                    <SelectItem value="flashcard" className="text-white hover:bg-purple-500/20">Flashcards</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <label className="text-sm text-purple-200/60">Svårighetsgrad</label>
                <Select value={difficulty} onValueChange={(v: string) => setDifficulty(v as typeof difficulty)}>
                  <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                    <SelectItem value="beginner" className="text-white hover:bg-purple-500/20">Nybörjare</SelectItem>
                    <SelectItem value="intermediate" className="text-white hover:bg-purple-500/20">Mellanliggande</SelectItem>
                    <SelectItem value="advanced" className="text-white hover:bg-purple-500/20">Avancerad</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <label className="text-sm text-purple-200/60">Antal frågor</label>
                <Select value={String(questionCount)} onValueChange={(v: string) => setQuestionCount(Number(v))}>
                  <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                    <SelectItem value="5" className="text-white hover:bg-purple-500/20">5 frågor</SelectItem>
                    <SelectItem value="10" className="text-white hover:bg-purple-500/20">10 frågor</SelectItem>
                    <SelectItem value="15" className="text-white hover:bg-purple-500/20">15 frågor</SelectItem>
                    <SelectItem value="20" className="text-white hover:bg-purple-500/20">20 frågor</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                <Button
                  onClick={generateQuiz}
                  disabled={!selectedModule || loading}
                  className={cn(
                    "w-full py-6 rounded-xl",
                    "bg-gradient-to-r from-purple-600 to-pink-600",
                    "hover:from-purple-500 hover:to-pink-500",
                    "shadow-[0_0_25px_rgba(168,85,247,0.4)]",
                    "disabled:opacity-50 disabled:shadow-none",
                    "text-lg font-semibold"
                  )}
                >
                  {loading ? (
                    <>
                      <Loader2 className="w-5 h-5 mr-2 animate-spin" />
                      Genererar Quiz...
                    </>
                  ) : (
                    <>
                      <Play className="w-5 h-5 mr-2 fill-white" />
                      Starta Quiz
                      <ChevronRight className="w-5 h-5 ml-2" />
                    </>
                  )}
                </Button>
              </motion.div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}
