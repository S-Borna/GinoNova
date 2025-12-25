"use client";

/**
 * ============================================================================
 * AI QUIZ GENERATOR — COSMIC EDITION 🌌
 * ============================================================================
 *
 * COSMIC DESIGN:
 * - Deep space background (#05050a)
 * - Multi-layered aurora orbs
 * - Pulsating icon glows
 * - Netflix-smooth animations
 *
 * @phase MILESTONE-2.0-COSMIC
 */

import { useState, useEffect } from "react";
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

/* ============================================================================
   COSMIC AURORA BACKGROUND
   ============================================================================ */

function CosmicAurora() {
  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden">
      <div className="absolute inset-0 bg-[#05050a]" />
      <div
        className="absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage: `
                        linear-gradient(rgba(168, 85, 247, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(168, 85, 247, 0.3) 1px, transparent 1px)
                    `,
          backgroundSize: '60px 60px'
        }}
      />
      <motion.div
        className="absolute -top-40 -right-40 w-[700px] h-[700px] rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(168, 85, 247, 0.15) 0%, rgba(168, 85, 247, 0.05) 40%, transparent 70%)',
        }}
        animate={{ scale: [1, 1.1, 1], opacity: [0.5, 0.7, 0.5] }}
        transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
      />
      <motion.div
        className="absolute -bottom-60 -left-60 w-[600px] h-[600px] rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(236, 72, 153, 0.1) 0%, transparent 60%)',
        }}
        animate={{ scale: [1, 1.15, 1], opacity: [0.4, 0.6, 0.4] }}
        transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
      />
      <motion.div
        className="absolute top-1/3 left-1/4 w-[500px] h-[500px] rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 60%)',
        }}
        animate={{ scale: [1, 1.2, 1], opacity: [0.3, 0.5, 0.3] }}
        transition={{ duration: 12, repeat: Infinity, ease: "easeInOut", delay: 4 }}
      />
    </div>
  )
}

// Hardcode API URL to ensure it works
const API_BASE_URL = "https://saas-project-production-31f8.up.railway.app";

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

  // No access view - Cosmic styled
  if (hasAccess === false) {
    return (
      <div className="min-h-screen bg-[#05050a] relative">
        <CosmicAurora />
        <div className="relative z-10 p-8">
          <div className="max-w-2xl mx-auto">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            >
              <Card className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border-purple-500/30 shadow-[0_0_40px_rgba(168,85,247,0.1)]">
                <CardHeader className="text-center">
                  <motion.div
                    className="mx-auto w-16 h-16 bg-gradient-to-br from-purple-500/30 to-pink-500/30 rounded-full flex items-center justify-center mb-4 border border-purple-500/40"
                    animate={{
                      boxShadow: [
                        '0 0 20px rgba(168,85,247,0.3)',
                        '0 0 35px rgba(168,85,247,0.5)',
                        '0 0 20px rgba(168,85,247,0.3)'
                      ]
                    }}
                    transition={{ duration: 2.5, repeat: Infinity }}
                  >
                    <Lock className="w-8 h-8 text-purple-400" />
                  </motion.div>
                  <CardTitle className="text-2xl text-white">Premium Feature</CardTitle>
                  <CardDescription className="text-purple-200/60">
                    {accessMessage}
                  </CardDescription>
                </CardHeader>
                <CardContent className="text-center">
                  <div className="space-y-4">
                    <motion.div
                      className="flex items-center justify-center gap-2 text-zinc-300"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.2 }}
                    >
                      <Sparkles className="w-5 h-5 text-yellow-500" />
                      <span>AI-powered quiz generation</span>
                    </motion.div>
                    <motion.div
                      className="flex items-center justify-center gap-2 text-zinc-300"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.3 }}
                    >
                      <Brain className="w-5 h-5 text-purple-500" />
                      <span>Adaptive difficulty levels</span>
                    </motion.div>
                    <motion.div
                      className="flex items-center justify-center gap-2 text-zinc-300"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.4 }}
                    >
                      <Target className="w-5 h-5 text-green-500" />
                      <span>Module-specific questions</span>
                    </motion.div>
                  </div>
                  <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 0.5 }}
                  >
                    <Badge className="mt-6 bg-gradient-to-r from-purple-600 to-pink-600 shadow-[0_0_15px_rgba(168,85,247,0.4)]">
                      Coming Soon
                    </Badge>
                  </motion.div>
                </CardContent>
              </Card>
            </motion.div>
          </div>
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

  // Quiz results view - Cosmic celebration
  if (quiz?.showResult) {
    const percentage = Math.round((quiz.score / quiz.questions.length) * 100);

    return (
      <div className="min-h-screen bg-[#05050a] relative">
        <CosmicAurora />
        <div className="relative z-10 p-8">
          <div className="max-w-2xl mx-auto">
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            >
              <Card className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border-emerald-500/30 shadow-[0_0_50px_rgba(52,211,153,0.15)]">
                <CardHeader className="text-center">
                  <motion.div
                    className="mx-auto w-20 h-20 bg-gradient-to-br from-green-500/30 to-emerald-500/30 rounded-full flex items-center justify-center mb-4 border border-emerald-500/40"
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
                    <GraduationCap className="w-10 h-10 text-green-400" />
                  </motion.div>
                  <CardTitle className="text-3xl text-white">Quiz Complete!</CardTitle>
                  <CardDescription className="text-emerald-200/60">
                    You scored {quiz.score} out of {quiz.questions.length}
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="text-center">
                    <motion.div
                      className="text-6xl font-bold bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent"
                      animate={{ scale: [1, 1.05, 1] }}
                      transition={{ duration: 2, repeat: Infinity }}
                    >
                      {percentage}%
                    </motion.div>
                    <Progress value={percentage} className="mt-4 h-3 bg-zinc-800" />
                  </div>

                  <div className="flex justify-center gap-4">
                    <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                      <Button onClick={resetQuiz} variant="outline" className="border-emerald-500/40 hover:bg-emerald-500/10">
                        <RotateCcw className="w-4 h-4 mr-2" />
                        New Quiz
                      </Button>
                    </motion.div>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          </div>
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

  // Quiz setup view - Cosmic styled
  return (
    <div className="min-h-screen bg-[#05050a] relative">
      <CosmicAurora />
      <div className="relative z-10 p-8">
        <div className="max-w-2xl mx-auto">
          {/* Cosmic Header */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className="text-center mb-8"
          >
            <motion.div
              className="inline-flex items-center gap-2 bg-gradient-to-r from-purple-500/20 to-pink-500/20 px-4 py-2 rounded-full mb-4 border border-purple-500/30"
              animate={{ boxShadow: ['0 0 15px rgba(168,85,247,0.2)', '0 0 25px rgba(168,85,247,0.4)', '0 0 15px rgba(168,85,247,0.2)'] }}
              transition={{ duration: 2.5, repeat: Infinity }}
            >
              <motion.div
                animate={{ rotate: [0, 10, -10, 0], scale: [1, 1.1, 1] }}
                transition={{ duration: 3, repeat: Infinity }}
              >
                <Sparkles className="w-4 h-4 text-purple-400" />
              </motion.div>
              <span className="text-purple-300 text-sm">AI-Powered</span>
            </motion.div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent mb-2">Quiz Generator</h1>
            <p className="text-purple-200/60">
              Test your knowledge with AI-generated questions
            </p>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          >
            <Card className="bg-gradient-to-br from-[#0d0d14] to-[#0a0a0f] border-purple-500/30 shadow-[0_0_40px_rgba(168,85,247,0.1)]">
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
                  Configure Your Quiz
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
                  <label className="text-sm text-purple-200/60">Select Module ({modules.length} available)</label>
                  <Select value={selectedModule} onValueChange={setSelectedModule}>
                    <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60 focus:ring-purple-500/20">
                      <SelectValue placeholder="Choose a module..." />
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
                  <label className="text-sm text-purple-200/60">Quiz Type</label>
                  <Select value={quizType} onValueChange={(v: string) => setQuizType(v as "mcq" | "flashcard")}>
                    <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                      <SelectItem value="mcq" className="text-white hover:bg-purple-500/20">Multiple Choice</SelectItem>
                      <SelectItem value="flashcard" className="text-white hover:bg-purple-500/20">Flashcards</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <label className="text-sm text-purple-200/60">Difficulty</label>
                  <Select value={difficulty} onValueChange={(v: string) => setDifficulty(v as typeof difficulty)}>
                    <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                      <SelectItem value="beginner" className="text-white hover:bg-purple-500/20">Beginner</SelectItem>
                      <SelectItem value="intermediate" className="text-white hover:bg-purple-500/20">Intermediate</SelectItem>
                      <SelectItem value="advanced" className="text-white hover:bg-purple-500/20">Advanced</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <label className="text-sm text-purple-200/60">Number of Questions</label>
                  <Select value={String(questionCount)} onValueChange={(v: string) => setQuestionCount(Number(v))}>
                    <SelectTrigger className="bg-[#0a0a0f] border-purple-500/30 text-white focus:border-purple-500/60">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent className="bg-[#0d0d14] border-purple-500/30">
                      <SelectItem value="5" className="text-white hover:bg-purple-500/20">5 Questions</SelectItem>
                      <SelectItem value="10" className="text-white hover:bg-purple-500/20">10 Questions</SelectItem>
                      <SelectItem value="15" className="text-white hover:bg-purple-500/20">15 Questions</SelectItem>
                      <SelectItem value="20" className="text-white hover:bg-purple-500/20">20 Questions</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
                  <Button
                    onClick={generateQuiz}
                    disabled={!selectedModule || loading}
                    className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 shadow-[0_0_25px_rgba(168,85,247,0.4)] disabled:opacity-50 disabled:shadow-none"
                  >
                    {loading ? (
                      <>
                        <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                        Generating Quiz...
                      </>
                    ) : (
                      <>
                        <Zap className="w-4 h-4 mr-2" />
                        Generate Quiz
                      </>
                    )}
                  </Button>
                </motion.div>
              </CardContent>
            </Card>
          </motion.div>
        </div>
      </div>
    </div>
  );
}
