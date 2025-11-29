"""
AI Content Generation Schemas
Phase 17 - AI Content Generation Engine

Pydantic models for:
- Content generation requests
- Generated content (tasks, modules, quizzes, packs)
- Generation status and results
"""
from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==============================================================================
# ENUMS
# ==============================================================================

GenerationType = Literal["task", "module", "quiz", "pack", "hints", "examples"]
GenerationStatus = Literal["pending", "generating", "completed", "failed", "approved", "rejected"]


# ==============================================================================
# GENERATION REQUEST
# ==============================================================================

class GenerationInputs(BaseModel):
    """Inputs for content generation"""
    topic: str = Field(..., min_length=3, max_length=200)
    difficulty: str = "intermediate"  # beginner, intermediate, advanced
    learning_goals: List[str] = []
    target_audience: str = "devops engineers"
    
    # For modules
    num_tasks: Optional[int] = Field(None, ge=3, le=20)
    
    # For quizzes
    num_questions: Optional[int] = Field(None, ge=3, le=15)
    
    # Context
    related_module_slug: Optional[str] = None
    related_task_id: Optional[UUID] = None
    
    # Additional instructions
    additional_context: Optional[str] = None
    include_examples: bool = True
    include_hints: bool = True


class GenerationRequestCreate(BaseModel):
    """Schema for creating a generation request"""
    type: GenerationType
    inputs: GenerationInputs


class GenerationRequestPublic(BaseModel):
    """Public generation request view"""
    id: UUID
    admin_id: Optional[UUID] = None
    type: GenerationType
    inputs: GenerationInputs
    status: GenerationStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None

    class Config:
        from_attributes = True


class GenerationRequestInDB(BaseModel):
    """Internal generation request model"""
    id: UUID = Field(default_factory=uuid4)
    admin_id: Optional[UUID] = None
    type: GenerationType
    inputs: GenerationInputs
    status: GenerationStatus = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None

    class Config:
        from_attributes = True


# ==============================================================================
# GENERATED CONTENT
# ==============================================================================

class GeneratedTask(BaseModel):
    """Generated task content"""
    title: str
    description: str
    content_markdown: str
    difficulty: str = "medium"
    estimated_minutes: int = 15
    xp_reward: int = 25
    tags: List[str] = []
    
    # Interactive content
    code_examples: List[dict] = []
    hints: List[str] = []
    quiz_questions: List[dict] = []
    
    # Solution
    solution_markdown: Optional[str] = None


class GeneratedModule(BaseModel):
    """Generated module content"""
    name: str
    slug: str
    description: str
    difficulty: str = "intermediate"
    estimated_hours: float = 10.0
    learning_objectives: List[str] = []
    prerequisites: List[str] = []
    tags: List[str] = []
    
    # Tasks
    tasks: List[GeneratedTask] = []
    
    # Summary
    summary_markdown: Optional[str] = None


class GeneratedQuiz(BaseModel):
    """Generated quiz content"""
    title: str
    description: str
    difficulty: str = "medium"
    
    questions: List[dict] = []  # QuizBlock format
    
    # Metadata
    passing_score: int = 70
    time_limit_minutes: Optional[int] = None


class GeneratedPack(BaseModel):
    """Generated marketplace pack"""
    title: str
    description: str
    short_description: str
    difficulty: str = "intermediate"
    estimated_hours: float = 20.0
    tags: List[str] = []
    
    # Content
    modules: List[GeneratedModule] = []
    
    # Pricing suggestion
    suggested_price_cents: int = 0


class GeneratedContentPublic(BaseModel):
    """Public generated content view"""
    id: UUID
    request_id: UUID
    type: GenerationType
    status: GenerationStatus
    
    # Content (one of these will be populated)
    task: Optional[GeneratedTask] = None
    module: Optional[GeneratedModule] = None
    quiz: Optional[GeneratedQuiz] = None
    pack: Optional[GeneratedPack] = None
    
    # Metadata
    created_at: datetime
    approved_at: Optional[datetime] = None
    approved_by: Optional[UUID] = None

    class Config:
        from_attributes = True


class GeneratedContentInDB(BaseModel):
    """Internal generated content model"""
    id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    type: GenerationType
    status: GenerationStatus = "pending"
    
    # Raw output
    output_json: dict = {}
    
    # Parsed content
    task: Optional[GeneratedTask] = None
    module: Optional[GeneratedModule] = None
    quiz: Optional[GeneratedQuiz] = None
    pack: Optional[GeneratedPack] = None
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.utcnow)
    approved_at: Optional[datetime] = None
    approved_by: Optional[UUID] = None

    class Config:
        from_attributes = True


# ==============================================================================
# API RESPONSES
# ==============================================================================

class GeneratorStatusResponse(BaseModel):
    """Generator status response"""
    status: str = "operational"
    phase: str
    capabilities: List[str]
    pending_requests: int
    total_generated: int


class GenerationResultResponse(BaseModel):
    """Generation result response"""
    request: GenerationRequestPublic
    content: Optional[GeneratedContentPublic] = None
    preview_url: Optional[str] = None
