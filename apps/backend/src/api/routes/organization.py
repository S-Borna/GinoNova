"""
Organization & Team API Routes
Phase 18 - Team & Organization Workspaces

Endpoints for:
- Organization management
- Team management
- Team members
- Team module access
- Organization/Team analytics
"""
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from fastapi import APIRouter, Response, HTTPException, status

from ...schemas.organization import (
    OrganizationCreate, OrganizationUpdate, OrganizationPublic, OrganizationInDB,
    TeamCreate, TeamUpdate, TeamPublic, TeamInDB,
    TeamMemberCreate, TeamMemberUpdate, TeamMemberPublic, TeamMemberInDB,
    TeamModuleAccessCreate, TeamModuleAccessPublic, TeamModuleAccessInDB,
    TeamAnalytics, OrgAnalytics, OrgStatusResponse,
)


router = APIRouter(prefix="/org", tags=["organization"])

PHASE_VERSION = "18.0"


def add_phase_header(response: Response) -> None:
    """Add X-Phase header to response"""
    response.headers["X-Phase"] = PHASE_VERSION


# ==============================================================================
# IN-MEMORY STORAGE
# ==============================================================================

_organizations: dict[UUID, OrganizationInDB] = {}
_teams: dict[UUID, TeamInDB] = {}
_team_members: dict[UUID, TeamMemberInDB] = {}
_team_module_access: dict[UUID, TeamModuleAccessInDB] = {}


# ==============================================================================
# HELPERS
# ==============================================================================

def _seed_sample_org():
    """Seed sample organization for demo"""
    if _organizations:
        return
    
    # Create sample org
    org_id = uuid4()
    owner_id = uuid4()
    
    org = OrganizationInDB(
        id=org_id,
        owner_id=owner_id,
        name="DevOps Academy",
        description="A sample organization for DevOps training",
        plan="enterprise",
        seats_total=50,
        seats_used=12,
        teams_count=3,
        members_count=12,
        modules_installed=8,
    )
    _organizations[org_id] = org
    
    # Create sample teams
    team_data = [
        {"name": "Cloud Infrastructure", "description": "AWS, GCP, Azure specialists"},
        {"name": "Platform Engineering", "description": "Kubernetes and container orchestration"},
        {"name": "SRE Team", "description": "Site Reliability Engineering"},
    ]
    
    for i, td in enumerate(team_data):
        team_id = uuid4()
        team = TeamInDB(
            id=team_id,
            organization_id=org_id,
            name=td["name"],
            description=td["description"],
            members_count=4,
            modules_count=3,
        )
        _teams[team_id] = team
        
        # Add sample members
        for j in range(4):
            member_id = uuid4()
            role = "lead" if j == 0 else "member"
            member = TeamMemberInDB(
                id=member_id,
                team_id=team_id,
                user_id=uuid4(),
                role=role,
                user_name=f"Team Member {j+1}",
                user_email=f"member{j+1}@example.com",
                modules_completed=5 + j,
                tasks_completed=20 + j * 5,
                total_xp=500 + j * 100,
            )
            _team_members[member_id] = member


# ==============================================================================
# ORGANIZATION ENDPOINTS
# ==============================================================================

@router.get("/status", response_model=OrgStatusResponse)
def org_status(response: Response):
    """Get organization system status"""
    add_phase_header(response)
    _seed_sample_org()
    
    return OrgStatusResponse(
        status="operational",
        phase=PHASE_VERSION,
        total_organizations=len(_organizations),
        total_teams=len(_teams),
        features=[
            "organizations",
            "teams",
            "team_members",
            "role_management",
            "module_access",
            "org_analytics",
            "team_analytics",
            "seat_management",
        ],
    )


@router.get("", response_model=OrganizationPublic)
@router.get("/", response_model=OrganizationPublic)
def get_current_organization(response: Response):
    """Get current user's organization"""
    add_phase_header(response)
    _seed_sample_org()
    
    # Return first org for demo
    if _organizations:
        org = list(_organizations.values())[0]
        return OrganizationPublic(**org.model_dump())
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No organization found"
    )


@router.post("", response_model=OrganizationPublic, status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=OrganizationPublic, status_code=status.HTTP_201_CREATED)
def create_organization(data: OrganizationCreate, response: Response):
    """Create a new organization"""
    add_phase_header(response)
    
    # TODO: Get user from auth
    owner_id = uuid4()
    
    # Plan limits
    seat_limits = {"free": 5, "pro": 25, "enterprise": 100}
    
    org = OrganizationInDB(
        id=uuid4(),
        owner_id=owner_id,
        name=data.name,
        description=data.description,
        logo_url=data.logo_url,
        website=data.website,
        contact_email=data.contact_email,
        plan=data.plan,
        seats_total=seat_limits.get(data.plan, 5),
    )
    _organizations[org.id] = org
    
    return OrganizationPublic(**org.model_dump())


@router.put("/{org_id}", response_model=OrganizationPublic)
def update_organization(org_id: UUID, data: OrganizationUpdate, response: Response):
    """Update an organization"""
    add_phase_header(response)
    
    org = _organizations.get(org_id)
    if not org:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(org, field, value)
    
    org.updated_at = datetime.utcnow()
    
    return OrganizationPublic(**org.model_dump())


# ==============================================================================
# TEAM ENDPOINTS
# ==============================================================================

@router.get("/teams", response_model=List[TeamPublic])
def list_teams(org_id: Optional[UUID] = None, response: Optional[Response] = None):
    """List teams for organization"""
    if response:
        add_phase_header(response)
    
    _seed_sample_org()
    
    teams = list(_teams.values())
    
    if org_id:
        teams = [t for t in teams if t.organization_id == org_id]
    
    teams = [t for t in teams if t.is_active]
    
    return [TeamPublic(**t.model_dump()) for t in teams]


@router.post("/teams", response_model=TeamPublic, status_code=status.HTTP_201_CREATED)
def create_team(data: TeamCreate, response: Response):
    """Create a new team"""
    add_phase_header(response)
    
    # Check org exists
    org = _organizations.get(data.organization_id)
    if not org:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found"
        )
    
    team = TeamInDB(
        id=uuid4(),
        organization_id=data.organization_id,
        name=data.name,
        description=data.description,
    )
    _teams[team.id] = team
    
    # Update org stats
    org.teams_count += 1
    
    return TeamPublic(**team.model_dump())


@router.get("/teams/{team_id}", response_model=TeamPublic)
def get_team(team_id: UUID, response: Response):
    """Get team details"""
    add_phase_header(response)
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    return TeamPublic(**team.model_dump())


@router.put("/teams/{team_id}", response_model=TeamPublic)
def update_team(team_id: UUID, data: TeamUpdate, response: Response):
    """Update a team"""
    add_phase_header(response)
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if value is not None:
            setattr(team, field, value)
    
    team.updated_at = datetime.utcnow()
    
    return TeamPublic(**team.model_dump())


@router.delete("/teams/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_team(team_id: UUID, response: Response):
    """Delete a team (soft delete)"""
    add_phase_header(response)
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    team.is_active = False
    
    # Update org stats
    org = _organizations.get(team.organization_id)
    if org:
        org.teams_count = max(0, org.teams_count - 1)


# ==============================================================================
# TEAM MEMBER ENDPOINTS
# ==============================================================================

@router.get("/teams/{team_id}/members", response_model=List[TeamMemberPublic])
def list_team_members(team_id: UUID, response: Response):
    """List team members"""
    add_phase_header(response)
    _seed_sample_org()
    
    members = [
        TeamMemberPublic(**m.model_dump())
        for m in _team_members.values()
        if m.team_id == team_id and m.is_active
    ]
    
    return members


@router.post("/teams/{team_id}/members", response_model=TeamMemberPublic, status_code=status.HTTP_201_CREATED)
def add_team_member(team_id: UUID, data: TeamMemberCreate, response: Response):
    """Add a member to team"""
    add_phase_header(response)
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    # Check seat availability
    org = _organizations.get(team.organization_id)
    if org and org.seats_used >= org.seats_total:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No available seats in organization"
        )
    
    member = TeamMemberInDB(
        id=uuid4(),
        team_id=team_id,
        user_id=data.user_id,
        role=data.role,
        user_name=f"User {data.user_id}",  # TODO: Get from user service
    )
    _team_members[member.id] = member
    
    # Update stats
    team.members_count += 1
    if org:
        org.seats_used += 1
        org.members_count += 1
    
    return TeamMemberPublic(**member.model_dump())


@router.put("/teams/{team_id}/members/{member_id}/role", response_model=TeamMemberPublic)
def update_member_role(team_id: UUID, member_id: UUID, data: TeamMemberUpdate, response: Response):
    """Update team member role"""
    add_phase_header(response)
    
    member = _team_members.get(member_id)
    if not member or member.team_id != team_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team member not found"
        )
    
    member.role = data.role
    
    return TeamMemberPublic(**member.model_dump())


@router.delete("/teams/{team_id}/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_team_member(team_id: UUID, member_id: UUID, response: Response):
    """Remove a member from team"""
    add_phase_header(response)
    
    member = _team_members.get(member_id)
    if not member or member.team_id != team_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team member not found"
        )
    
    member.is_active = False
    
    # Update stats
    team = _teams.get(team_id)
    if team:
        team.members_count = max(0, team.members_count - 1)
    
    org = _organizations.get(team.organization_id) if team else None
    if org:
        org.seats_used = max(0, org.seats_used - 1)
        org.members_count = max(0, org.members_count - 1)


# ==============================================================================
# MODULE ACCESS ENDPOINTS
# ==============================================================================

@router.get("/teams/{team_id}/modules", response_model=List[TeamModuleAccessPublic])
def list_team_modules(team_id: UUID, response: Response):
    """List modules assigned to team"""
    add_phase_header(response)
    
    access = [
        TeamModuleAccessPublic(**a.model_dump())
        for a in _team_module_access.values()
        if a.team_id == team_id and a.is_active
    ]
    
    return access


@router.post("/teams/{team_id}/modules", response_model=TeamModuleAccessPublic, status_code=status.HTTP_201_CREATED)
def add_team_module(team_id: UUID, data: TeamModuleAccessCreate, response: Response):
    """Grant team access to a module"""
    add_phase_header(response)
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    access = TeamModuleAccessInDB(
        id=uuid4(),
        team_id=team_id,
        module_slug=data.module_slug,
        source=data.source,
        module_name=data.module_slug.replace("-", " ").title(),
    )
    _team_module_access[access.id] = access
    
    # Update stats
    team.modules_count += 1
    
    org = _organizations.get(team.organization_id)
    if org:
        org.modules_installed += 1
    
    return TeamModuleAccessPublic(**access.model_dump())


@router.delete("/teams/{team_id}/modules/{access_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_team_module(team_id: UUID, access_id: UUID, response: Response):
    """Remove team's access to a module"""
    add_phase_header(response)
    
    access = _team_module_access.get(access_id)
    if not access or access.team_id != team_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module access not found"
        )
    
    access.is_active = False
    
    # Update stats
    team = _teams.get(team_id)
    if team:
        team.modules_count = max(0, team.modules_count - 1)


# ==============================================================================
# ANALYTICS ENDPOINTS
# ==============================================================================

@router.get("/analytics", response_model=OrgAnalytics)
def get_org_analytics(response: Response):
    """Get organization analytics"""
    add_phase_header(response)
    _seed_sample_org()
    
    if not _organizations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No organization found"
        )
    
    org = list(_organizations.values())[0]
    
    # Build team rankings
    team_rankings = []
    for team in _teams.values():
        if team.organization_id == org.id and team.is_active:
            members = [m for m in _team_members.values() if m.team_id == team.id and m.is_active]
            total_xp = sum(m.total_xp for m in members)
            team_rankings.append({
                "team_id": str(team.id),
                "team_name": team.name,
                "members": len(members),
                "total_xp": total_xp,
                "avg_xp": total_xp / len(members) if members else 0,
            })
    
    team_rankings.sort(key=lambda x: x["total_xp"], reverse=True)
    
    return OrgAnalytics(
        organization_id=org.id,
        organization_name=org.name,
        total_teams=org.teams_count,
        total_members=org.members_count,
        total_modules_installed=org.modules_installed,
        seats_used=org.seats_used,
        seats_total=org.seats_total,
        utilization_rate=org.seats_used / org.seats_total * 100 if org.seats_total > 0 else 0,
        avg_completion_rate=65.5,  # Mock
        total_tasks_completed=sum(m.tasks_completed for m in _team_members.values()),
        total_xp_earned=sum(m.total_xp for m in _team_members.values()),
        team_rankings=team_rankings,
        weekly_active_users=10,
        monthly_active_users=12,
    )


@router.get("/teams/{team_id}/analytics", response_model=TeamAnalytics)
def get_team_analytics(team_id: UUID, response: Response):
    """Get team analytics"""
    add_phase_header(response)
    _seed_sample_org()
    
    team = _teams.get(team_id)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found"
        )
    
    members = [m for m in _team_members.values() if m.team_id == team_id and m.is_active]
    
    # Build top performers
    top_performers = sorted(members, key=lambda m: m.total_xp, reverse=True)[:5]
    top_performers_data = [
        {
            "user_id": str(m.user_id),
            "name": m.user_name,
            "xp": m.total_xp,
            "tasks_completed": m.tasks_completed,
        }
        for m in top_performers
    ]
    
    return TeamAnalytics(
        team_id=team.id,
        team_name=team.name,
        total_members=len(members),
        active_members=len(members),  # All are active in demo
        avg_completion_rate=72.3,  # Mock
        total_tasks_completed=sum(m.tasks_completed for m in members),
        total_xp_earned=sum(m.total_xp for m in members),
        avg_time_per_task=18.5,  # Mock
        top_performers=top_performers_data,
        skill_gaps=["kubernetes", "terraform"],  # Mock
        recommended_modules=["k8s-mastery", "iac-fundamentals"],  # Mock
        weekly_active_users=len(members),
        monthly_active_users=len(members),
    )
