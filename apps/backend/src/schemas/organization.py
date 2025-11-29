"""
Team & Organization Schemas
Phase 18 - Team & Organization Workspaces

Pydantic models for:
- Organizations
- Teams
- Team members
- Team module access
- Organization analytics
"""
from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


# ==============================================================================
# ENUMS
# ==============================================================================

OrgPlan = Literal["free", "pro", "enterprise"]
TeamRole = Literal["admin", "lead", "member"]
ModuleSource = Literal["core", "marketplace", "internal"]


# ==============================================================================
# ORGANIZATION
# ==============================================================================

class OrganizationBase(BaseModel):
    """Base organization model"""
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    
    # Branding
    logo_url: Optional[str] = None
    website: Optional[str] = None
    
    # Contact
    contact_email: Optional[str] = None


class OrganizationCreate(OrganizationBase):
    """Schema for creating an organization"""
    plan: OrgPlan = "free"


class OrganizationUpdate(BaseModel):
    """Schema for updating an organization"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    logo_url: Optional[str] = None
    website: Optional[str] = None
    contact_email: Optional[str] = None


class OrganizationPublic(OrganizationBase):
    """Public organization view"""
    id: UUID
    plan: OrgPlan
    
    # Seats
    seats_total: int = 5
    seats_used: int = 0
    
    # Stats
    teams_count: int = 0
    members_count: int = 0
    modules_installed: int = 0
    
    # Status
    is_active: bool = True
    
    # Dates
    created_at: datetime

    class Config:
        from_attributes = True


class OrganizationInDB(OrganizationBase):
    """Internal organization model"""
    id: UUID = Field(default_factory=uuid4)
    owner_id: UUID  # User who created the org
    plan: OrgPlan = "free"
    
    # Seats
    seats_total: int = 5
    seats_used: int = 0
    
    # Stats
    teams_count: int = 0
    members_count: int = 0
    modules_installed: int = 0
    
    # Status
    is_active: bool = True
    
    # Dates
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# TEAM
# ==============================================================================

class TeamBase(BaseModel):
    """Base team model"""
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=300)


class TeamCreate(TeamBase):
    """Schema for creating a team"""
    organization_id: UUID


class TeamUpdate(BaseModel):
    """Schema for updating a team"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=300)


class TeamPublic(TeamBase):
    """Public team view"""
    id: UUID
    organization_id: UUID
    
    # Stats
    members_count: int = 0
    modules_count: int = 0
    
    # Status
    is_active: bool = True
    
    created_at: datetime

    class Config:
        from_attributes = True


class TeamInDB(TeamBase):
    """Internal team model"""
    id: UUID = Field(default_factory=uuid4)
    organization_id: UUID
    
    # Stats
    members_count: int = 0
    modules_count: int = 0
    
    # Status
    is_active: bool = True
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# TEAM MEMBER
# ==============================================================================

class TeamMemberCreate(BaseModel):
    """Schema for adding a team member"""
    user_id: UUID
    role: TeamRole = "member"


class TeamMemberUpdate(BaseModel):
    """Schema for updating a team member"""
    role: TeamRole


class TeamMemberPublic(BaseModel):
    """Public team member view"""
    id: UUID
    team_id: UUID
    user_id: UUID
    role: TeamRole
    
    # User info (populated from user)
    user_name: str = ""
    user_email: str = ""
    user_avatar: Optional[str] = None
    
    # Stats
    modules_completed: int = 0
    tasks_completed: int = 0
    total_xp: int = 0
    
    joined_at: datetime

    class Config:
        from_attributes = True


class TeamMemberInDB(BaseModel):
    """Internal team member model"""
    id: UUID = Field(default_factory=uuid4)
    team_id: UUID
    user_id: UUID
    role: TeamRole = "member"
    
    # User info
    user_name: str = ""
    user_email: str = ""
    user_avatar: Optional[str] = None
    
    # Stats
    modules_completed: int = 0
    tasks_completed: int = 0
    total_xp: int = 0
    
    is_active: bool = True
    joined_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# TEAM MODULE ACCESS
# ==============================================================================

class TeamModuleAccessCreate(BaseModel):
    """Schema for granting team module access"""
    module_slug: str
    source: ModuleSource = "core"


class TeamModuleAccessPublic(BaseModel):
    """Public team module access view"""
    id: UUID
    team_id: UUID
    module_slug: str
    source: ModuleSource
    
    # Module info
    module_name: str = ""
    
    granted_at: datetime

    class Config:
        from_attributes = True


class TeamModuleAccessInDB(BaseModel):
    """Internal team module access model"""
    id: UUID = Field(default_factory=uuid4)
    team_id: UUID
    module_slug: str
    source: ModuleSource = "core"
    
    # Module info
    module_name: str = ""
    
    is_active: bool = True
    granted_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# ==============================================================================
# ANALYTICS
# ==============================================================================

class TeamAnalytics(BaseModel):
    """Team analytics summary"""
    team_id: UUID
    team_name: str
    
    # Members
    total_members: int = 0
    active_members: int = 0
    
    # Progress
    avg_completion_rate: float = 0.0
    total_tasks_completed: int = 0
    total_xp_earned: int = 0
    avg_time_per_task: float = 0.0
    
    # Top performers
    top_performers: List[dict] = []
    
    # Skill gaps
    skill_gaps: List[str] = []
    recommended_modules: List[str] = []
    
    # Activity
    weekly_active_users: int = 0
    monthly_active_users: int = 0


class OrgAnalytics(BaseModel):
    """Organization analytics summary"""
    organization_id: UUID
    organization_name: str
    
    # Overview
    total_teams: int = 0
    total_members: int = 0
    total_modules_installed: int = 0
    
    # Usage
    seats_used: int = 0
    seats_total: int = 0
    utilization_rate: float = 0.0
    
    # Progress
    avg_completion_rate: float = 0.0
    total_tasks_completed: int = 0
    total_xp_earned: int = 0
    
    # Team breakdown
    team_rankings: List[dict] = []
    
    # Activity
    weekly_active_users: int = 0
    monthly_active_users: int = 0


# ==============================================================================
# API RESPONSES
# ==============================================================================

class OrgStatusResponse(BaseModel):
    """Organization system status"""
    status: str = "operational"
    phase: str
    total_organizations: int = 0
    total_teams: int = 0
    features: List[str]
