"""
Career Engine Schemas
Phase 19 - Jobs & Career Engine

Pydantic models for:
- User skills and skill graph
- Portfolio projects
- Resume versions
- Career recommendations
- Job matching
"""
from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==============================================================================
# ENUMS
# ==============================================================================

SkillLevel = Literal[0, 1, 2, 3, 4, 5]  # 0=none, 1=beginner, 5=expert
ResumeFormat = Literal["pdf", "markdown", "json"]
CareerRole = Literal[
    "devops_engineer",
    "cloud_engineer",
    "platform_engineer",
    "sre",
    "release_engineer",
    "cicd_engineer",
]


# ==============================================================================
# SKILLS
# ==============================================================================

class UserSkillBase(BaseModel):
    """Base user skill model"""
    skill_slug: str = Field(..., min_length=2, max_length=100)
    level: int = Field(default=0, ge=0, le=5)


class UserSkillCreate(UserSkillBase):
    """Schema for creating/updating a user skill"""
    evidence: List[str] = []  # Task IDs that prove this skill


class UserSkillPublic(UserSkillBase):
    """Public user skill view"""
    id: UUID
    user_id: UUID

    # Metadata
    skill_name: str = ""
    skill_category: str = "general"

    # Evidence
    evidence: List[str] = []
    tasks_completed: int = 0

    updated_at: datetime

    class Config:
        from_attributes = True


class UserSkillInDB(UserSkillBase):
    """Internal user skill model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID

    skill_name: str = ""
    skill_category: str = "general"

    evidence: List[str] = []
    tasks_completed: int = 0

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


class SkillGraphNode(BaseModel):
    """Node in skill graph"""
    slug: str
    name: str
    level: int = 0
    category: str = "general"


class SkillGraphEdge(BaseModel):
    """Edge in skill graph"""
    from_skill: str
    to_skill: str
    strength: float = 1.0


class SkillGraph(BaseModel):
    """User's skill graph"""
    user_id: UUID
    nodes: List[SkillGraphNode] = []
    edges: List[SkillGraphEdge] = []

    # Summary
    total_skills: int = 0
    avg_level: float = 0.0
    strongest_category: str = ""


# ==============================================================================
# PORTFOLIO
# ==============================================================================

class PortfolioProjectBase(BaseModel):
    """Base portfolio project model"""
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=2000)

    # Links
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    screenshot_url: Optional[str] = None

    # Skills
    skills: List[str] = []
    technologies: List[str] = []

    # Visibility
    is_public: bool = True
    is_featured: bool = False


class PortfolioProjectCreate(PortfolioProjectBase):
    """Schema for creating a portfolio project"""
    pass


class PortfolioProjectUpdate(BaseModel):
    """Schema for updating a portfolio project"""
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10, max_length=2000)
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    screenshot_url: Optional[str] = None
    skills: Optional[List[str]] = None
    technologies: Optional[List[str]] = None
    is_public: Optional[bool] = None
    is_featured: Optional[bool] = None


class PortfolioProjectPublic(PortfolioProjectBase):
    """Public portfolio project view"""
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PortfolioProjectInDB(PortfolioProjectBase):
    """Internal portfolio project model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# RESUME
# ==============================================================================

class ResumeGenerateRequest(BaseModel):
    """Request to generate a resume"""
    format: ResumeFormat = "pdf"

    # Options
    include_skills: bool = True
    include_projects: bool = True
    include_certificates: bool = True

    # Customization
    target_role: Optional[CareerRole] = None
    custom_summary: Optional[str] = None


class ResumeVersionPublic(BaseModel):
    """Public resume version view"""
    id: UUID
    user_id: UUID
    version_name: str
    format: ResumeFormat

    # URLs
    rendered_url: Optional[str] = None
    download_url: Optional[str] = None

    # Metadata
    target_role: Optional[str] = None
    ats_score: int = 0  # ATS compatibility score 0-100

    created_at: datetime

    class Config:
        from_attributes = True


class ResumeVersionInDB(BaseModel):
    """Internal resume version model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    version_name: str
    format: ResumeFormat = "pdf"

    # Content
    content_json: dict = {}
    rendered_url: Optional[str] = None
    download_url: Optional[str] = None

    # Metadata
    target_role: Optional[str] = None
    ats_score: int = 0

    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# JOB MATCHING
# ==============================================================================

class RoleRequirement(BaseModel):
    """Skill requirement for a role"""
    skill_slug: str
    skill_name: str
    required_level: int
    user_level: int
    is_met: bool


class JobMatchResult(BaseModel):
    """Job matching result for a role"""
    role: str  # CareerRole as string
    role_name: str

    # Score
    readiness_score: int = Field(ge=0, le=100)

    # Requirements analysis
    requirements_met: int = 0
    requirements_total: int = 0

    # Details
    strengths: List[str] = []
    gaps: List[RoleRequirement] = []

    # Recommendations
    recommended_modules: List[str] = []
    recommended_tasks: List[str] = []
    estimated_time_to_ready: str = ""


class CareerRecommendation(BaseModel):
    """Career path recommendation"""
    id: UUID
    user_id: UUID

    # Target
    target_role: CareerRole
    role_name: str

    # Current state
    current_readiness: int = 0

    # Path
    missing_skills: List[str] = []
    recommended_modules: List[str] = []
    recommended_tasks: List[str] = []

    # Timeline
    estimated_weeks: int = 0

    created_at: datetime

    class Config:
        from_attributes = True


class CareerRecommendationInDB(BaseModel):
    """Internal career recommendation model"""
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID

    target_role: CareerRole
    role_name: str

    current_readiness: int = 0

    missing_skills: List[str] = []
    recommended_modules: List[str] = []
    recommended_tasks: List[str] = []

    estimated_weeks: int = 0

    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# CAREER DASHBOARD
# ==============================================================================

class CareerDashboard(BaseModel):
    """Career dashboard summary"""
    user_id: UUID

    # Overall
    overall_readiness: int = 0
    primary_role: Optional[str] = None

    # Skills
    total_skills: int = 0
    skills_by_category: dict = {}
    top_skills: List[dict] = []

    # Portfolio
    portfolio_projects: int = 0
    featured_projects: int = 0

    # Resumes
    resume_versions: int = 0
    latest_ats_score: int = 0

    # Matching
    best_role_match: Optional[str] = None
    best_match_score: int = 0

    # Recommendations
    next_steps: List[str] = []


# ==============================================================================
# API RESPONSES
# ==============================================================================

class CareerStatusResponse(BaseModel):
    """Career engine status"""
    status: str = "operational"
    phase: str
    features: List[str]
    supported_roles: List[str]
