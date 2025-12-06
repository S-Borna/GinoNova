"""
Interactive Learning Engine - Content Block Schemas
Phase ILE.1: Data Structure for Interactive Learning

Content blocks are the building blocks of interactive tasks:
- TextBlock: Markdown content
- CodeBlock: Syntax-highlighted code with explanation
- TerminalBlock: Interactive terminal practice
- QuizBlock: Multiple choice questions
- CheckpointBlock: Progress markers
"""
from datetime import datetime
from typing import Optional, List, Literal, Union, Any
from uuid import UUID
from pydantic import BaseModel, Field


# ==============================================================================
# CONTENT BLOCK TYPES
# ==============================================================================

BlockType = Literal[
    "text", "code", "terminal", "quiz", "checkpoint",
    "flashcard", "intro", "concept", "practice", "challenge"
]


class TextBlock(BaseModel):
    """Markdown text content block"""
    type: Literal["text"] = "text"
    content: str = Field(..., description="Markdown content")

    class Config:
        from_attributes = True


class CodeBlock(BaseModel):
    """Code snippet with syntax highlighting"""
    type: Literal["code"] = "code"
    language: str = Field(..., description="Programming language for syntax highlighting")
    code: str = Field(..., description="The code content")
    filename: Optional[str] = Field(None, description="Optional filename to display")
    highlight_lines: Optional[List[int]] = Field(None, description="Lines to highlight")
    explanation: Optional[str] = Field(None, description="Explanation shown below or on hover")

    class Config:
        from_attributes = True


class ExpectedCommand(BaseModel):
    """Expected command for terminal validation"""
    command: str = Field(..., description="The command user should type")
    regex: Optional[str] = Field(None, description="Regex pattern to match variations")
    output: Optional[str] = Field(None, description="Simulated output to display")
    explanation: str = Field(..., description="Why this command is used")
    allow_variations: bool = Field(default=False, description="Accept slight variations")

    class Config:
        from_attributes = True


class TerminalBlock(BaseModel):
    """Interactive terminal practice block"""
    type: Literal["terminal"] = "terminal"
    instructions: str = Field(..., description="Instructions for the user")
    expected_commands: List[ExpectedCommand] = Field(..., description="Commands to complete")
    hints: Optional[List[str]] = Field(None, description="Progressive hints")
    validation_script: Optional[str] = Field(None, description="Optional validation script")

    class Config:
        from_attributes = True


class QuizOption(BaseModel):
    """Quiz answer option"""
    text: str = Field(..., description="Option text")
    is_correct: bool = Field(..., description="Whether this is the correct answer")
    feedback: Optional[str] = Field(None, description="Feedback shown when selected")

    class Config:
        from_attributes = True


class QuizBlock(BaseModel):
    """Multiple choice quiz block"""
    type: Literal["quiz"] = "quiz"
    question: str = Field(..., description="The question")
    options: List[QuizOption] = Field(..., min_length=2, description="Answer options")
    explanation: str = Field(..., description="Explanation shown after answering")
    xp_bonus: int = Field(default=5, ge=0, description="Bonus XP for correct answer")

    class Config:
        from_attributes = True


class CheckpointValidation(BaseModel):
    """Checkpoint validation configuration"""
    command: Optional[str] = Field(None, description="Command to run for validation")
    expected_output: Optional[str] = Field(None, description="Expected output")
    file_to_check: Optional[str] = Field(None, description="File that should exist")

    class Config:
        from_attributes = True


class CheckpointBlock(BaseModel):
    """Progress checkpoint block"""
    type: Literal["checkpoint"] = "checkpoint"
    title: str = Field(..., description="Checkpoint title")
    description: str = Field(..., description="What the user has learned")
    validation_type: Literal["manual", "command", "file"] = Field(
        default="manual",
        description="How to validate checkpoint"
    )
    validation: Optional[CheckpointValidation] = Field(None, description="Validation config")

    class Config:
        from_attributes = True


# ==============================================================================
# NEW V2 BLOCKS - Interactive Learning
# ==============================================================================

class Flashcard(BaseModel):
    """Single flashcard for memorization"""
    term: str = Field(..., description="Front of card - the term/concept")
    definition: str = Field(..., description="Back of card - the definition/explanation")

    class Config:
        from_attributes = True


class FlashcardBlock(BaseModel):
    """Flashcard deck for memorization practice"""
    type: Literal["flashcard"] = "flashcard"
    title: str = Field(default="Flashcards", description="Title for the flashcard section")
    cards: List[Flashcard] = Field(..., min_length=1, description="List of flashcards")
    shuffle: bool = Field(default=True, description="Whether to shuffle cards")

    class Config:
        from_attributes = True


class IntroBlock(BaseModel):
    """Introduction block with learning objectives"""
    type: Literal["intro"] = "intro"
    headline: str = Field(..., description="Attention-grabbing headline")
    hook: str = Field(..., description="Why this matters - motivational text")
    learning_objectives: List[str] = Field(..., min_length=1, description="What user will learn")
    prerequisites: Optional[List[str]] = Field(None, description="What user should know first")
    estimated_minutes: int = Field(default=30, description="Estimated time for entire node")

    class Config:
        from_attributes = True


class ConceptBlock(BaseModel):
    """Single concept explanation with diagram and tips"""
    type: Literal["concept"] = "concept"
    title: str = Field(..., description="Concept title")
    explanation: str = Field(..., description="Markdown explanation")
    diagram: Optional[str] = Field(None, description="ASCII/text diagram")
    pro_tip: Optional[str] = Field(None, description="Pro tip for this concept")
    common_mistake: Optional[str] = Field(None, description="Common mistake to avoid")

    class Config:
        from_attributes = True


class PracticeStep(BaseModel):
    """Single practice step in a terminal exercise"""
    step: int = Field(..., description="Step number")
    title: str = Field(..., description="Step title")
    instruction: str = Field(..., description="What user should do")
    command: str = Field(..., description="Command to type")
    expected_output: str = Field(default="", description="Expected output")
    explanation: str = Field(..., description="Why this command works")

    class Config:
        from_attributes = True


class PracticeBlock(BaseModel):
    """Interactive practice section with simulated terminal"""
    type: Literal["practice"] = "practice"
    description: str = Field(..., description="Overview of the practice session")
    exercises: List[PracticeStep] = Field(..., min_length=1, description="Steps to complete")

    class Config:
        from_attributes = True


class ChallengeBlock(BaseModel):
    """End-of-node challenge that combines all concepts"""
    type: Literal["challenge"] = "challenge"
    title: str = Field(..., description="Challenge title")
    scenario: str = Field(..., description="Real-world scenario description")
    requirements: List[str] = Field(..., min_length=1, description="What user must do")
    hints: Optional[List[str]] = Field(None, description="Progressive hints")
    solution: Optional[str] = Field(None, description="Solution code/commands (hidden until revealed)")
    validation_commands: Optional[List[str]] = Field(None, description="Commands to verify completion")
    xp_bonus: int = Field(default=20, description="Bonus XP for completing challenge")

    class Config:
        from_attributes = True


# Union of all block types (updated with new V2 blocks)
ContentBlock = Union[
    TextBlock, 
    CodeBlock, 
    TerminalBlock, 
    QuizBlock, 
    CheckpointBlock,
    FlashcardBlock,
    IntroBlock,
    ConceptBlock,
    PracticeBlock,
    ChallengeBlock
]


# ==============================================================================
# COMPLETION REQUIREMENTS
# ==============================================================================

RequirementType = Literal[
    "all_terminals_complete",
    "all_quizzes_answered",
    "all_quizzes_correct",
    "checkpoint_reached",
    "min_time_spent"
]


class CompletionRequirement(BaseModel):
    """Requirement for task completion"""
    type: RequirementType = Field(..., description="Type of requirement")
    value: Optional[Any] = Field(None, description="Optional value (e.g., min seconds)")

    class Config:
        from_attributes = True


# ==============================================================================
# TASK PROGRESS TRACKING
# ==============================================================================

class BlockProgress(BaseModel):
    """Progress for a single block"""
    block_index: int = Field(..., description="Index of the block in content array")
    completed: bool = Field(default=False, description="Whether block is completed")
    attempts: int = Field(default=0, description="Number of attempts")
    completed_at: Optional[datetime] = Field(None, description="When completed")

    class Config:
        from_attributes = True


class QuizAnswer(BaseModel):
    """Record of a quiz answer"""
    block_index: int = Field(..., description="Index of quiz block")
    selected_option: int = Field(..., description="Index of selected option")
    is_correct: bool = Field(..., description="Whether answer was correct")
    answered_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


class TerminalCommand(BaseModel):
    """Record of a terminal command"""
    block_index: int = Field(..., description="Index of terminal block")
    command_index: int = Field(..., description="Which command in the expected list")
    command: str = Field(..., description="Command entered by user")
    was_correct: bool = Field(..., description="Whether command was correct")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


class TaskBlockProgress(BaseModel):
    """Complete progress tracking for a task"""
    user_id: UUID
    task_id: UUID
    status: Literal["not_started", "in_progress", "completed"] = "not_started"

    # Block-level tracking
    block_progress: List[BlockProgress] = Field(default_factory=list)
    quiz_answers: List[QuizAnswer] = Field(default_factory=list)
    terminal_history: List[TerminalCommand] = Field(default_factory=list)

    # Timing
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    total_time_spent: int = Field(default=0, description="Seconds spent on task")

    # XP
    xp_earned: int = Field(default=0, description="Total XP earned including bonuses")

    class Config:
        from_attributes = True


class TaskBlockProgressCreate(BaseModel):
    """Schema for creating task progress"""
    task_id: UUID

    class Config:
        from_attributes = True


class TaskBlockProgressUpdate(BaseModel):
    """Schema for updating task progress"""
    block_index: Optional[int] = None
    block_completed: Optional[bool] = None
    quiz_answer: Optional[QuizAnswer] = None
    terminal_command: Optional[TerminalCommand] = None
    time_spent_delta: Optional[int] = Field(None, description="Seconds to add")

    class Config:
        from_attributes = True


# ==============================================================================
# ENHANCED TASK SCHEMAS
# ==============================================================================

class TaskWithBlocks(BaseModel):
    """Task with interactive content blocks"""
    id: UUID
    module_id: UUID
    title: str
    description: Optional[str] = None

    # Interactive content
    content_blocks: List[ContentBlock] = Field(default_factory=list)
    requirements: List[CompletionRequirement] = Field(default_factory=list)

    # Metadata
    order_index: int = 1
    difficulty: str = "medium"
    estimated_minutes: int = 15
    xp_reward: int = 25
    is_active: bool = True

    # Legacy support
    content: Optional[str] = Field(None, description="Legacy markdown content")

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TaskProgressResponse(BaseModel):
    """Response for task progress endpoint"""
    task_id: UUID
    user_id: UUID
    status: str
    progress_percent: int = Field(default=0, description="0-100 completion percentage")
    blocks_completed: int = 0
    blocks_total: int = 0
    quizzes_correct: int = 0
    quizzes_total: int = 0
    terminals_completed: int = 0
    terminals_total: int = 0
    xp_earned: int = 0
    xp_potential: int = Field(default=0, description="Max XP including bonuses")
    time_spent: int = 0
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True
