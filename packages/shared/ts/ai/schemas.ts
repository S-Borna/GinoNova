/**
 * AI Engine Response Schemas
 * Phase 7.3: Shared cross-language schema module
 *
 * These schemas define the response models for the DevOpsHub AI Engine.
 * TypeScript equivalents of Python models in packages/shared/python/shared/ai/schemas.py
 *
 * Uses Zod for runtime validation.
 */
import { z } from "zod";

// ============================================================================
// RECOMMENDATION SCHEMAS
// ============================================================================

/**
 * Recommended task with confidence score.
 */
export const TaskRecommendationSchema = z.object({
    task_id: z.string().describe("UUID of the recommended task"),
    title: z.string().describe("Task title"),
    confidence: z.number().min(0.0).max(1.0).describe("Confidence score (0.0-1.0)"),
    reason: z.string().nullable().optional().describe("Explanation for the recommendation"),
});
export type TaskRecommendation = z.infer<typeof TaskRecommendationSchema>;

/**
 * Recommended module with confidence score.
 */
export const ModuleRecommendationSchema = z.object({
    module_id: z.string().describe("UUID of the recommended module"),
    name: z.string().describe("Module name"),
    confidence: z.number().min(0.0).max(1.0).describe("Confidence score (0.0-1.0)"),
    reason: z.string().nullable().optional().describe("Explanation for the recommendation"),
});
export type ModuleRecommendation = z.infer<typeof ModuleRecommendationSchema>;

/**
 * Recommended studyflow session configuration.
 */
export const StudyflowRecommendationSchema = z.object({
    mode: z.enum(["pomodoro", "taskrunner", "sprint"]).describe("Recommended session mode"),
    duration: z.number().int().min(5).max(120).describe("Recommended duration in minutes"),
    intensity: z.enum(["low", "medium", "high"]).describe("Recommended intensity level"),
});
export type StudyflowRecommendation = z.infer<typeof StudyflowRecommendationSchema>;

/**
 * Container for all recommendation types.
 */
export const RecommendationsSchema = z.object({
    next_task: TaskRecommendationSchema.nullable().optional().describe("Recommended next task"),
    next_module: ModuleRecommendationSchema.nullable().optional().describe("Recommended next module"),
    studyflow: StudyflowRecommendationSchema.nullable().optional().describe("Recommended studyflow config"),
});
export type Recommendations = z.infer<typeof RecommendationsSchema>;

/**
 * Full recommendations response.
 */
export const RecommendationsResponseSchema = z.object({
    recommendations: RecommendationsSchema,
    generated_at: z.string().datetime().describe("When recommendations were generated"),
    expires_at: z.string().datetime().describe("When recommendations expire (cache TTL)"),
});
export type RecommendationsResponse = z.infer<typeof RecommendationsResponseSchema>;

// ============================================================================
// NEXT STEP SCHEMAS
// ============================================================================

/**
 * Single next action recommendation.
 */
export const NextStepResponseSchema = z.object({
    action_type: z.enum(["task", "module", "studyflow", "break"]).describe("Type of recommended action"),
    action_id: z.string().nullable().optional().describe("ID of the recommended item (if applicable)"),
    title: z.string().describe("Human-readable action title"),
    description: z.string().describe("Explanation of why this action is recommended"),
    confidence: z.number().min(0.0).max(1.0).describe("Confidence score"),
    estimated_duration: z.number().int().nullable().optional().describe("Estimated time in minutes"),
    generated_at: z.string().datetime(),
});
export type NextStepResponse = z.infer<typeof NextStepResponseSchema>;

// ============================================================================
// DIFFICULTY SCHEMAS
// ============================================================================

/**
 * Task difficulty estimate for a specific user.
 */
export const DifficultyEstimateSchema = z.object({
    task_id: z.string().describe("UUID of the task"),
    base_difficulty: z.enum(["easy", "medium", "hard"]).describe("Original task difficulty"),
    user_adjusted_difficulty: z.number().min(1.0).max(5.0).describe("User-adjusted difficulty (1.0-5.0)"),
    estimated_duration: z.number().int().min(1).describe("Estimated completion time in minutes"),
    success_probability: z.number().min(0.0).max(1.0).describe("Estimated success probability"),
    prerequisites_met: z.boolean().describe("Whether user has completed prerequisites"),
    generated_at: z.string().datetime(),
});
export type DifficultyEstimate = z.infer<typeof DifficultyEstimateSchema>;

// ============================================================================
// SUMMARY SCHEMAS
// ============================================================================

/**
 * A single highlight from the daily summary.
 */
export const SummaryHighlightSchema = z.object({
    type: z.enum(["achievement", "progress", "streak", "recommendation"]).describe("Type of highlight"),
    title: z.string().describe("Highlight title"),
    description: z.string().describe("Highlight description"),
    metric: z.string().nullable().optional().describe("Associated metric value"),
});
export type SummaryHighlight = z.infer<typeof SummaryHighlightSchema>;

/**
 * Daily AI-generated summary for user.
 */
export const DailySummaryResponseSchema = z.object({
    date: z.string().describe("Date of the summary (YYYY-MM-DD)"),
    greeting: z.string().describe("Personalized greeting message"),
    highlights: z.array(SummaryHighlightSchema).default([]).describe("Key highlights"),
    tasks_completed: z.number().int().min(0).describe("Number of tasks completed today"),
    xp_earned: z.number().int().min(0).describe("XP earned today"),
    study_minutes: z.number().int().min(0).describe("Total study time in minutes"),
    streak_days: z.number().int().min(0).describe("Current streak in days"),
    motivation_message: z.string().describe("AI-generated motivation message"),
    generated_at: z.string().datetime(),
});
export type DailySummaryResponse = z.infer<typeof DailySummaryResponseSchema>;

// ============================================================================
// STATUS SCHEMA
// ============================================================================

/**
 * AI Engine status check response.
 */
export const AIStatusResponseSchema = z.object({
    phase: z.string(),
    feature: z.string(),
    status: z.string(),
    engines: z.record(z.string()),
    cache_enabled: z.boolean(),
    fallback_mode: z.string(),
});
export type AIStatusResponse = z.infer<typeof AIStatusResponseSchema>;

// ============================================================================
// EXPORTS
// ============================================================================

export const AISchemas = {
    TaskRecommendation: TaskRecommendationSchema,
    ModuleRecommendation: ModuleRecommendationSchema,
    StudyflowRecommendation: StudyflowRecommendationSchema,
    Recommendations: RecommendationsSchema,
    RecommendationsResponse: RecommendationsResponseSchema,
    NextStepResponse: NextStepResponseSchema,
    DifficultyEstimate: DifficultyEstimateSchema,
    SummaryHighlight: SummaryHighlightSchema,
    DailySummaryResponse: DailySummaryResponseSchema,
    AIStatusResponse: AIStatusResponseSchema,
};
