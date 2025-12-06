"use client";

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

  // No access view
  if (hasAccess === false) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 p-8">
        <div className="max-w-2xl mx-auto">
          <Card className="bg-neutral-900/50 border-neutral-800">
            <CardHeader className="text-center">
              <div className="mx-auto w-16 h-16 bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-full flex items-center justify-center mb-4">
                <Lock className="w-8 h-8 text-purple-400" />
              </div>
              <CardTitle className="text-2xl text-white">Premium Feature</CardTitle>
              <CardDescription className="text-neutral-400">
                {accessMessage}
              </CardDescription>
            </CardHeader>
            <CardContent className="text-center">
              <div className="space-y-4">
                <div className="flex items-center justify-center gap-2 text-neutral-300">
                  <Sparkles className="w-5 h-5 text-yellow-500" />
                  <span>AI-powered quiz generation</span>
                </div>
                <div className="flex items-center justify-center gap-2 text-neutral-300">
                  <Brain className="w-5 h-5 text-purple-500" />
                  <span>Adaptive difficulty levels</span>
                </div>
                <div className="flex items-center justify-center gap-2 text-neutral-300">
                  <Target className="w-5 h-5 text-green-500" />
                  <span>Module-specific questions</span>
                </div>
              </div>
              <Badge className="mt-6 bg-gradient-to-r from-purple-600 to-pink-600">
                Coming Soon
              </Badge>
            </CardContent>
          </Card>
        </div>
      </div>
    );
  }

  // Loading access check
  if (hasAccess === null) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 flex items-center justify-center">
        <Loader2 className="w-8 h-8 animate-spin text-purple-500" />
      </div>
    );
  }

  // Quiz results view
  if (quiz?.showResult) {
    const percentage = Math.round((quiz.score / quiz.questions.length) * 100);

    return (
      <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 p-8">
        <div className="max-w-2xl mx-auto">
          <Card className="bg-neutral-900/50 border-neutral-800">
            <CardHeader className="text-center">
              <div className="mx-auto w-20 h-20 bg-gradient-to-br from-green-500/20 to-emerald-500/20 rounded-full flex items-center justify-center mb-4">
                <GraduationCap className="w-10 h-10 text-green-400" />
              </div>
              <CardTitle className="text-3xl text-white">Quiz Complete!</CardTitle>
              <CardDescription className="text-neutral-400">
                You scored {quiz.score} out of {quiz.questions.length}
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="text-center">
                <div className="text-6xl font-bold bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">
                  {percentage}%
                </div>
                <Progress value={percentage} className="mt-4 h-3" />
              </div>

              <div className="flex justify-center gap-4">
                <Button onClick={resetQuiz} variant="outline">
                  <RotateCcw className="w-4 h-4 mr-2" />
                  New Quiz
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    );
  }

  // Active quiz view
  if (quiz) {
    const currentQuestion = quiz.questions[quiz.currentIndex];
    const progress = ((quiz.currentIndex + 1) / quiz.questions.length) * 100;

    return (
      <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 p-8">
        <div className="max-w-3xl mx-auto">
          <div className="mb-6">
            <div className="flex justify-between text-sm text-neutral-400 mb-2">
              <span>Question {quiz.currentIndex + 1} of {quiz.questions.length}</span>
              <span>Score: {quiz.score}</span>
            </div>
            <Progress value={progress} className="h-2" />
          </div>

          <AnimatePresence mode="wait">
            <motion.div
              key={quiz.currentIndex}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
            >
              {quizType === "mcq" ? (
                <Card className="bg-neutral-900/50 border-neutral-800">
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
                        <button
                          key={idx}
                          onClick={() => !showResult && handleMCQAnswer(letter)}
                          disabled={showResult}
                          className={`w-full p-4 rounded-lg text-left transition-all ${showResult
                            ? isCorrect
                              ? "bg-green-500/20 border-green-500"
                              : isSelected
                                ? "bg-red-500/20 border-red-500"
                                : "bg-neutral-800/50 border-neutral-700"
                            : isSelected
                              ? "bg-purple-500/20 border-purple-500"
                              : "bg-neutral-800/50 border-neutral-700 hover:bg-neutral-800"
                            } border`}
                        >
                          <div className="flex items-center gap-3">
                            {showResult && isCorrect && (
                              <CheckCircle2 className="w-5 h-5 text-green-500" />
                            )}
                            {showResult && isSelected && !isCorrect && (
                              <XCircle className="w-5 h-5 text-red-500" />
                            )}
                            <span className="text-white">{option}</span>
                          </div>
                        </button>
                      );
                    })}

                    {quiz.answers[quiz.currentIndex] !== null && (
                      <div className="mt-4 p-4 bg-neutral-800/50 rounded-lg">
                        <p className="text-neutral-300 text-sm">
                          <strong>Explanation:</strong> {(currentQuestion as MCQQuestion).explanation}
                        </p>
                      </div>
                    )}

                    {quiz.answers[quiz.currentIndex] !== null && (
                      <Button onClick={nextQuestion} className="w-full mt-4">
                        {quiz.currentIndex < quiz.questions.length - 1 ? (
                          <>Next <ChevronRight className="w-4 h-4 ml-2" /></>
                        ) : (
                          <>See Results</>
                        )}
                      </Button>
                    )}
                  </CardContent>
                </Card>
              ) : (
                <div className="space-y-4">
                  <Card 
                    onClick={handleFlipCard}
                    className="bg-neutral-900/50 border-neutral-800 min-h-[300px] flex items-center justify-center cursor-pointer hover:border-purple-500/50 transition-colors"
                  >
                    <CardContent className="text-center p-8">
                      {!quiz.flipped[quiz.currentIndex] ? (
                        <div>
                          <Badge className="mb-4">Front</Badge>
                          <p className="text-2xl text-white">
                            {(currentQuestion as FlashcardQuestion).front}
                          </p>
                          {(currentQuestion as FlashcardQuestion).hint && (
                            <p className="text-sm text-neutral-400 mt-4">
                              Hint: {(currentQuestion as FlashcardQuestion).hint}
                            </p>
                          )}
                          <p className="text-neutral-500 mt-6 text-sm">Click to flip</p>
                        </div>
                      ) : (
                        <div>
                          <Badge className="mb-4 bg-green-600">Back</Badge>
                          <p className="text-xl text-white">
                            {(currentQuestion as FlashcardQuestion).back}
                          </p>
                          <p className="text-neutral-500 mt-6 text-sm">Click to flip back</p>
                        </div>
                      )}
                    </CardContent>
                  </Card>

                  <Button onClick={(e) => { e.stopPropagation(); nextQuestion(); }} className="w-full bg-gradient-to-r from-purple-600 to-pink-600">
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
    );
  }

  // Quiz setup view
  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-950 via-neutral-900 to-neutral-950 p-8">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 bg-gradient-to-r from-purple-500/10 to-pink-500/10 px-4 py-2 rounded-full mb-4">
            <Sparkles className="w-4 h-4 text-purple-400" />
            <span className="text-purple-300 text-sm">AI-Powered</span>
          </div>
          <h1 className="text-4xl font-bold text-white mb-2">Quiz Generator</h1>
          <p className="text-neutral-400">
            Test your knowledge with AI-generated questions
          </p>
        </div>

        <Card className="bg-neutral-900/50 border-neutral-800">
          <CardHeader>
            <CardTitle className="text-white flex items-center gap-2">
              <Brain className="w-5 h-5 text-purple-400" />
              Configure Your Quiz
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            {error && (
              <div className="p-4 bg-red-500/10 border border-red-500/50 rounded-lg text-red-400">
                {error}
              </div>
            )}

            <div className="space-y-2">
              <label className="text-sm text-neutral-400">Select Module ({modules.length} available)</label>
              <Select value={selectedModule} onValueChange={setSelectedModule}>
                <SelectTrigger className="bg-neutral-800 border-neutral-700">
                  <SelectValue placeholder="Choose a module..." />
                </SelectTrigger>
                <SelectContent>
                  {modules.map((module) => (
                    <SelectItem key={module.slug} value={module.slug}>
                      {module.title}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <label className="text-sm text-neutral-400">Quiz Type</label>
              <Select value={quizType} onValueChange={(v: string) => setQuizType(v as "mcq" | "flashcard")}>
                <SelectTrigger className="bg-neutral-800 border-neutral-700">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="mcq">Multiple Choice</SelectItem>
                  <SelectItem value="flashcard">Flashcards</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <label className="text-sm text-neutral-400">Difficulty</label>
              <Select value={difficulty} onValueChange={(v: string) => setDifficulty(v as typeof difficulty)}>
                <SelectTrigger className="bg-neutral-800 border-neutral-700">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="beginner">Beginner</SelectItem>
                  <SelectItem value="intermediate">Intermediate</SelectItem>
                  <SelectItem value="advanced">Advanced</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <label className="text-sm text-neutral-400">Number of Questions</label>
              <Select value={String(questionCount)} onValueChange={(v: string) => setQuestionCount(Number(v))}>
                <SelectTrigger className="bg-neutral-800 border-neutral-700">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="5">5 Questions</SelectItem>
                  <SelectItem value="10">10 Questions</SelectItem>
                  <SelectItem value="15">15 Questions</SelectItem>
                  <SelectItem value="20">20 Questions</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <Button
              onClick={generateQuiz}
              disabled={!selectedModule || loading}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700"
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
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
