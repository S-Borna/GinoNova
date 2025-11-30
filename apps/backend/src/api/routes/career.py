"""
Career Engine API Routes
Phase 19 - Jobs & Career Engine

Endpoints for:
- Skills management and skill graph
- Portfolio projects
- Resume generation
- Job matching
- Career recommendations
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, Query

from ...core.deps import get_current_user
from ...schemas.career import (
    UserSkillCreate,
    UserSkillPublic,
    UserSkillInDB,
    SkillGraph,
    SkillGraphNode,
    SkillGraphEdge,
    PortfolioProjectCreate,
    PortfolioProjectUpdate,
    PortfolioProjectPublic,
    PortfolioProjectInDB,
    ResumeGenerateRequest,
    ResumeVersionPublic,
    ResumeVersionInDB,
    JobMatchResult,
    RoleRequirement,
    CareerRecommendation,
    CareerRecommendationInDB,
    CareerDashboard,
    CareerStatusResponse,
)

router = APIRouter(prefix="/career", tags=["career"])

# ==============================================================================
# IN-MEMORY STORAGE (Replace with database in production)
# ==============================================================================
user_skills_db: dict[UUID, list[UserSkillInDB]] = {}
portfolio_projects_db: dict[UUID, list[PortfolioProjectInDB]] = {}
resume_versions_db: dict[UUID, list[ResumeVersionInDB]] = {}
recommendations_db: dict[UUID, list[CareerRecommendationInDB]] = {}

# Skill definitions
SKILL_DEFINITIONS = {
    "docker": {"name": "Docker", "category": "containers"},
    "kubernetes": {"name": "Kubernetes", "category": "orchestration"},
    "terraform": {"name": "Terraform", "category": "iac"},
    "ansible": {"name": "Ansible", "category": "configuration"},
    "aws": {"name": "AWS", "category": "cloud"},
    "azure": {"name": "Azure", "category": "cloud"},
    "gcp": {"name": "GCP", "category": "cloud"},
    "jenkins": {"name": "Jenkins", "category": "cicd"},
    "github-actions": {"name": "GitHub Actions", "category": "cicd"},
    "gitlab-ci": {"name": "GitLab CI", "category": "cicd"},
    "prometheus": {"name": "Prometheus", "category": "monitoring"},
    "grafana": {"name": "Grafana", "category": "monitoring"},
    "linux": {"name": "Linux", "category": "os"},
    "bash": {"name": "Bash Scripting", "category": "scripting"},
    "python": {"name": "Python", "category": "programming"},
    "git": {"name": "Git", "category": "vcs"},
}

# Role requirements
ROLE_REQUIREMENTS = {
    "devops_engineer": {
        "name": "DevOps Engineer",
        "skills": [
            ("docker", 3), ("kubernetes", 3), ("linux", 3), ("git", 4),
            ("bash", 3), ("python", 2), ("jenkins", 2), ("terraform", 2),
        ]
    },
    "cloud_engineer": {
        "name": "Cloud Engineer",
        "skills": [
            ("aws", 4), ("terraform", 4), ("linux", 3), ("docker", 3),
            ("python", 3), ("kubernetes", 2), ("networking", 3),
        ]
    },
    "platform_engineer": {
        "name": "Platform Engineer",
        "skills": [
            ("kubernetes", 4), ("docker", 4), ("terraform", 4), ("python", 3),
            ("linux", 4), ("prometheus", 3), ("github-actions", 3),
        ]
    },
    "sre": {
        "name": "Site Reliability Engineer",
        "skills": [
            ("kubernetes", 4), ("prometheus", 4), ("grafana", 3), ("linux", 4),
            ("python", 3), ("docker", 3), ("terraform", 3),
        ]
    },
    "release_engineer": {
        "name": "Release Engineer",
        "skills": [
            ("jenkins", 4), ("github-actions", 4), ("git", 4), ("docker", 3),
            ("bash", 3), ("python", 2), ("kubernetes", 2),
        ]
    },
    "cicd_engineer": {
        "name": "CI/CD Engineer",
        "skills": [
            ("jenkins", 4), ("github-actions", 4), ("gitlab-ci", 3), ("docker", 4),
            ("bash", 4), ("python", 3), ("git", 4),
        ]
    },
}


# ==============================================================================
# STATUS
# ==============================================================================

@router.get("/status", response_model=CareerStatusResponse)
async def get_career_status():
    """Get career engine status"""
    return CareerStatusResponse(
        status="operational",
        phase="19.0",
        features=[
            "skills_management",
            "skill_graph",
            "portfolio_projects",
            "resume_generation",
            "job_matching",
            "career_recommendations",
        ],
        supported_roles=list(ROLE_REQUIREMENTS.keys()),
    )


# ==============================================================================
# SKILLS
# ==============================================================================

@router.get("/skills", response_model=List[UserSkillPublic])
async def list_user_skills(
    category: Optional[str] = None,
    min_level: int = Query(default=0, ge=0, le=5),
    current_user: dict = Depends(get_current_user),
):
    """List current user's skills"""
    user_id = UUID(current_user["id"])

    skills = user_skills_db.get(user_id, [])

    # Filter by category
    if category:
        skills = [s for s in skills if s.skill_category == category]

    # Filter by min level
    skills = [s for s in skills if s.level >= min_level]

    # Convert to public
    return [
        UserSkillPublic(
            id=s.id,
            user_id=s.user_id,
            skill_slug=s.skill_slug,
            skill_name=s.skill_name,
            skill_category=s.skill_category,
            level=s.level,
            evidence=s.evidence,
            tasks_completed=s.tasks_completed,
            updated_at=s.updated_at,
        )
        for s in skills
    ]


@router.post("/skills", response_model=UserSkillPublic)
async def add_or_update_skill(
    skill: UserSkillCreate,
    current_user: dict = Depends(get_current_user),
):
    """Add or update a user skill"""
    user_id = UUID(current_user["id"])

    # Get skill definition
    skill_def = SKILL_DEFINITIONS.get(skill.skill_slug, {
        "name": skill.skill_slug.replace("-", " ").title(),
        "category": "general",
    })

    # Get user's skills
    if user_id not in user_skills_db:
        user_skills_db[user_id] = []

    # Check if skill exists
    existing = next(
        (s for s in user_skills_db[user_id] if s.skill_slug == skill.skill_slug),
        None
    )

    if existing:
        # Update
        existing.level = skill.level
        existing.evidence = skill.evidence
        existing.tasks_completed = len(skill.evidence)
        existing.updated_at = datetime.utcnow()

        return UserSkillPublic(
            id=existing.id,
            user_id=existing.user_id,
            skill_slug=existing.skill_slug,
            skill_name=existing.skill_name,
            skill_category=existing.skill_category,
            level=existing.level,
            evidence=existing.evidence,
            tasks_completed=existing.tasks_completed,
            updated_at=existing.updated_at,
        )
    else:
        # Create
        new_skill = UserSkillInDB(
            id=uuid4(),
            user_id=user_id,
            skill_slug=skill.skill_slug,
            skill_name=skill_def["name"],
            skill_category=skill_def["category"],
            level=skill.level,
            evidence=skill.evidence,
            tasks_completed=len(skill.evidence),
        )
        user_skills_db[user_id].append(new_skill)

        return UserSkillPublic(
            id=new_skill.id,
            user_id=new_skill.user_id,
            skill_slug=new_skill.skill_slug,
            skill_name=new_skill.skill_name,
            skill_category=new_skill.skill_category,
            level=new_skill.level,
            evidence=new_skill.evidence,
            tasks_completed=new_skill.tasks_completed,
            updated_at=new_skill.updated_at,
        )


@router.delete("/skills/{skill_slug}")
async def remove_skill(
    skill_slug: str,
    current_user: dict = Depends(get_current_user),
):
    """Remove a skill from user's profile"""
    user_id = UUID(current_user["id"])

    if user_id not in user_skills_db:
        raise HTTPException(status_code=404, detail="Skill not found")

    user_skills_db[user_id] = [
        s for s in user_skills_db[user_id] if s.skill_slug != skill_slug
    ]

    return {"status": "deleted", "skill_slug": skill_slug}


@router.get("/skills/graph", response_model=SkillGraph)
async def get_skill_graph(
    current_user: dict = Depends(get_current_user),
):
    """Get user's skill graph with relationships"""
    user_id = UUID(current_user["id"])

    skills = user_skills_db.get(user_id, [])

    # Build nodes
    nodes = [
        SkillGraphNode(
            slug=s.skill_slug,
            name=s.skill_name,
            level=s.level,
            category=s.skill_category,
        )
        for s in skills
    ]

    # Build edges (related skills)
    skill_relations = {
        "docker": ["kubernetes", "linux", "docker-compose"],
        "kubernetes": ["docker", "helm", "prometheus", "linux"],
        "terraform": ["aws", "azure", "gcp", "ansible"],
        "aws": ["terraform", "cloudformation", "lambda"],
        "jenkins": ["docker", "git", "bash"],
        "github-actions": ["git", "docker", "yaml"],
        "prometheus": ["grafana", "kubernetes", "alertmanager"],
    }

    edges = []
    skill_slugs = {s.skill_slug for s in skills}

    for skill_slug in skill_slugs:
        related = skill_relations.get(skill_slug, [])
        for rel in related:
            if rel in skill_slugs:
                edges.append(SkillGraphEdge(
                    from_skill=skill_slug,
                    to_skill=rel,
                    strength=0.8,
                ))

    # Calculate summary
    avg_level = sum(s.level for s in skills) / len(skills) if skills else 0

    categories = {}
    for s in skills:
        categories[s.skill_category] = categories.get(s.skill_category, 0) + s.level
    strongest_category = max(categories.keys(), key=lambda k: categories[k]) if categories else ""

    return SkillGraph(
        user_id=user_id,
        nodes=nodes,
        edges=edges,
        total_skills=len(skills),
        avg_level=round(avg_level, 2),
        strongest_category=strongest_category,
    )


# ==============================================================================
# PORTFOLIO
# ==============================================================================

@router.get("/portfolio", response_model=List[PortfolioProjectPublic])
async def list_portfolio_projects(
    public_only: bool = False,
    featured_only: bool = False,
    current_user: dict = Depends(get_current_user),
):
    """List user's portfolio projects"""
    user_id = UUID(current_user["id"])

    projects = portfolio_projects_db.get(user_id, [])

    # Filter
    if public_only:
        projects = [p for p in projects if p.is_public]
    if featured_only:
        projects = [p for p in projects if p.is_featured]

    return [
        PortfolioProjectPublic(
            id=p.id,
            user_id=p.user_id,
            title=p.title,
            description=p.description,
            github_url=p.github_url,
            demo_url=p.demo_url,
            screenshot_url=p.screenshot_url,
            skills=p.skills,
            technologies=p.technologies,
            is_public=p.is_public,
            is_featured=p.is_featured,
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in projects
        if p.is_active
    ]


@router.post("/portfolio", response_model=PortfolioProjectPublic)
async def create_portfolio_project(
    project: PortfolioProjectCreate,
    current_user: dict = Depends(get_current_user),
):
    """Create a portfolio project"""
    user_id = UUID(current_user["id"])

    if user_id not in portfolio_projects_db:
        portfolio_projects_db[user_id] = []

    new_project = PortfolioProjectInDB(
        id=uuid4(),
        user_id=user_id,
        title=project.title,
        description=project.description,
        github_url=project.github_url,
        demo_url=project.demo_url,
        screenshot_url=project.screenshot_url,
        skills=project.skills,
        technologies=project.technologies,
        is_public=project.is_public,
        is_featured=project.is_featured,
    )

    portfolio_projects_db[user_id].append(new_project)

    return PortfolioProjectPublic(
        id=new_project.id,
        user_id=new_project.user_id,
        title=new_project.title,
        description=new_project.description,
        github_url=new_project.github_url,
        demo_url=new_project.demo_url,
        screenshot_url=new_project.screenshot_url,
        skills=new_project.skills,
        technologies=new_project.technologies,
        is_public=new_project.is_public,
        is_featured=new_project.is_featured,
        created_at=new_project.created_at,
        updated_at=new_project.updated_at,
    )


@router.get("/portfolio/{project_id}", response_model=PortfolioProjectPublic)
async def get_portfolio_project(
    project_id: UUID,
    current_user: dict = Depends(get_current_user),
):
    """Get a specific portfolio project"""
    user_id = UUID(current_user["id"])

    projects = portfolio_projects_db.get(user_id, [])
    project = next((p for p in projects if p.id == project_id and p.is_active), None)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return PortfolioProjectPublic(
        id=project.id,
        user_id=project.user_id,
        title=project.title,
        description=project.description,
        github_url=project.github_url,
        demo_url=project.demo_url,
        screenshot_url=project.screenshot_url,
        skills=project.skills,
        technologies=project.technologies,
        is_public=project.is_public,
        is_featured=project.is_featured,
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.put("/portfolio/{project_id}", response_model=PortfolioProjectPublic)
async def update_portfolio_project(
    project_id: UUID,
    update: PortfolioProjectUpdate,
    current_user: dict = Depends(get_current_user),
):
    """Update a portfolio project"""
    user_id = UUID(current_user["id"])

    projects = portfolio_projects_db.get(user_id, [])
    project = next((p for p in projects if p.id == project_id and p.is_active), None)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Update fields
    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(project, key, value)
    project.updated_at = datetime.utcnow()

    return PortfolioProjectPublic(
        id=project.id,
        user_id=project.user_id,
        title=project.title,
        description=project.description,
        github_url=project.github_url,
        demo_url=project.demo_url,
        screenshot_url=project.screenshot_url,
        skills=project.skills,
        technologies=project.technologies,
        is_public=project.is_public,
        is_featured=project.is_featured,
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.delete("/portfolio/{project_id}")
async def delete_portfolio_project(
    project_id: UUID,
    current_user: dict = Depends(get_current_user),
):
    """Delete a portfolio project (soft delete)"""
    user_id = UUID(current_user["id"])

    projects = portfolio_projects_db.get(user_id, [])
    project = next((p for p in projects if p.id == project_id and p.is_active), None)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.is_active = False
    project.updated_at = datetime.utcnow()

    return {"status": "deleted", "project_id": str(project_id)}


# ==============================================================================
# RESUME
# ==============================================================================

@router.get("/resume/versions", response_model=List[ResumeVersionPublic])
async def list_resume_versions(
    current_user: dict = Depends(get_current_user),
):
    """List user's resume versions"""
    user_id = UUID(current_user["id"])

    versions = resume_versions_db.get(user_id, [])

    return [
        ResumeVersionPublic(
            id=v.id,
            user_id=v.user_id,
            version_name=v.version_name,
            format=v.format,
            rendered_url=v.rendered_url,
            download_url=v.download_url,
            target_role=v.target_role,
            ats_score=v.ats_score,
            created_at=v.created_at,
        )
        for v in versions
        if v.is_active
    ]


@router.post("/resume/generate", response_model=ResumeVersionPublic)
async def generate_resume(
    request: ResumeGenerateRequest,
    current_user: dict = Depends(get_current_user),
):
    """Generate a new resume version"""
    user_id = UUID(current_user["id"])

    if user_id not in resume_versions_db:
        resume_versions_db[user_id] = []

    # Count versions
    version_num = len(resume_versions_db[user_id]) + 1

    # Build resume content
    skills = user_skills_db.get(user_id, [])
    projects = portfolio_projects_db.get(user_id, [])

    content = {
        "summary": request.custom_summary or "DevOps professional",
        "target_role": request.target_role,
        "skills": [
            {"name": s.skill_name, "level": s.level, "category": s.skill_category}
            for s in skills
        ] if request.include_skills else [],
        "projects": [
            {"title": p.title, "description": p.description, "technologies": p.technologies}
            for p in projects if p.is_active and p.is_public
        ] if request.include_projects else [],
    }

    # Calculate ATS score (simplified)
    ats_score = 60
    if len(skills) >= 5:
        ats_score += 10
    if len(skills) >= 10:
        ats_score += 10
    if len(projects) >= 2:
        ats_score += 10
    if request.target_role:
        ats_score += 10

    # Create version
    new_version = ResumeVersionInDB(
        id=uuid4(),
        user_id=user_id,
        version_name=f"v{version_num}",
        format=request.format,
        content_json=content,
        rendered_url=f"/api/career/resume/{user_id}/v{version_num}.{request.format}",
        download_url=f"/api/career/resume/{user_id}/v{version_num}.{request.format}?download=true",
        target_role=request.target_role,
        ats_score=min(ats_score, 100),
    )

    resume_versions_db[user_id].append(new_version)

    return ResumeVersionPublic(
        id=new_version.id,
        user_id=new_version.user_id,
        version_name=new_version.version_name,
        format=new_version.format,
        rendered_url=new_version.rendered_url,
        download_url=new_version.download_url,
        target_role=new_version.target_role,
        ats_score=new_version.ats_score,
        created_at=new_version.created_at,
    )


@router.delete("/resume/{version_id}")
async def delete_resume_version(
    version_id: UUID,
    current_user: dict = Depends(get_current_user),
):
    """Delete a resume version"""
    user_id = UUID(current_user["id"])

    versions = resume_versions_db.get(user_id, [])
    version = next((v for v in versions if v.id == version_id and v.is_active), None)

    if not version:
        raise HTTPException(status_code=404, detail="Resume version not found")

    version.is_active = False

    return {"status": "deleted", "version_id": str(version_id)}


# ==============================================================================
# JOB MATCHING
# ==============================================================================

@router.get("/match/{role}", response_model=JobMatchResult)
async def match_role(
    role: str,
    current_user: dict = Depends(get_current_user),
):
    """Get job match analysis for a specific role"""
    if role not in ROLE_REQUIREMENTS:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown role: {role}. Supported: {list(ROLE_REQUIREMENTS.keys())}"
        )

    user_id = UUID(current_user["id"])
    skills = user_skills_db.get(user_id, [])
    skill_levels = {s.skill_slug: s.level for s in skills}

    role_def = ROLE_REQUIREMENTS[role]
    requirements = role_def["skills"]

    # Analyze requirements
    gaps = []
    strengths = []
    met_count = 0

    for skill_slug, required_level in requirements:
        user_level = skill_levels.get(skill_slug, 0)
        skill_def = SKILL_DEFINITIONS.get(skill_slug, {"name": skill_slug.title()})

        is_met = user_level >= required_level
        if is_met:
            met_count += 1
            if user_level > required_level:
                strengths.append(f"{skill_def['name']} (Level {user_level})")
        else:
            gaps.append(RoleRequirement(
                skill_slug=skill_slug,
                skill_name=skill_def["name"],
                required_level=required_level,
                user_level=user_level,
                is_met=False,
            ))

    # Calculate readiness score
    readiness = int((met_count / len(requirements)) * 100) if requirements else 0

    # Recommendations
    recommended_modules = []
    for gap in gaps[:3]:
        recommended_modules.append(f"module-{gap.skill_slug}")

    # Time estimate
    gap_levels = sum(g.required_level - g.user_level for g in gaps)
    weeks = gap_levels * 2  # ~2 weeks per level gap

    return JobMatchResult(
        role=role,
        role_name=role_def["name"],
        readiness_score=readiness,
        requirements_met=met_count,
        requirements_total=len(requirements),
        strengths=strengths[:5],
        gaps=gaps,
        recommended_modules=recommended_modules,
        recommended_tasks=[],
        estimated_time_to_ready=f"{weeks} weeks" if weeks > 0 else "Ready now!",
    )


@router.get("/match", response_model=List[JobMatchResult])
async def match_all_roles(
    current_user: dict = Depends(get_current_user),
):
    """Get job match analysis for all supported roles"""
    results = []

    for role in ROLE_REQUIREMENTS:
        result = await match_role(role, current_user)
        results.append(result)

    # Sort by readiness score descending
    results.sort(key=lambda r: r.readiness_score, reverse=True)

    return results


# ==============================================================================
# RECOMMENDATIONS
# ==============================================================================

@router.get("/recommendations", response_model=List[CareerRecommendation])
async def list_recommendations(
    current_user: dict = Depends(get_current_user),
):
    """Get career recommendations"""
    user_id = UUID(current_user["id"])

    # Generate recommendations based on matching
    match_results = await match_all_roles(current_user)

    recommendations = []
    for match in match_results[:3]:  # Top 3 roles
        if match.readiness_score < 100:
            rec = CareerRecommendation(
                id=uuid4(),
                user_id=user_id,
                target_role=match.role,
                role_name=match.role_name,
                current_readiness=match.readiness_score,
                missing_skills=[g.skill_slug for g in match.gaps],
                recommended_modules=match.recommended_modules,
                recommended_tasks=[],
                estimated_weeks=int(match.estimated_time_to_ready.split()[0]) if match.estimated_time_to_ready != "Ready now!" else 0,
                created_at=datetime.utcnow(),
            )
            recommendations.append(rec)

    return recommendations


# ==============================================================================
# DASHBOARD
# ==============================================================================

@router.get("/dashboard", response_model=CareerDashboard)
async def get_career_dashboard(
    current_user: dict = Depends(get_current_user),
):
    """Get career dashboard summary"""
    user_id = UUID(current_user["id"])

    # Skills
    skills = user_skills_db.get(user_id, [])

    categories = {}
    for s in skills:
        if s.skill_category not in categories:
            categories[s.skill_category] = 0
        categories[s.skill_category] += 1

    top_skills = sorted(skills, key=lambda s: s.level, reverse=True)[:5]

    # Portfolio
    projects = portfolio_projects_db.get(user_id, [])
    active_projects = [p for p in projects if p.is_active]
    featured_projects = [p for p in active_projects if p.is_featured]

    # Resumes
    versions = resume_versions_db.get(user_id, [])
    active_versions = [v for v in versions if v.is_active]
    latest_ats = active_versions[-1].ats_score if active_versions else 0

    # Matching
    match_results = await match_all_roles(current_user)
    best_match = match_results[0] if match_results else None

    # Overall readiness (average of all roles)
    overall_readiness = (
        int(sum(m.readiness_score for m in match_results) / len(match_results))
        if match_results else 0
    )

    # Next steps
    next_steps = []
    if not skills:
        next_steps.append("Add your first skill to get started")
    elif len(skills) < 5:
        next_steps.append("Add more skills to improve your profile")

    if not active_projects:
        next_steps.append("Create a portfolio project")

    if not active_versions:
        next_steps.append("Generate your first resume")

    if best_match and best_match.gaps:
        gap = best_match.gaps[0]
        next_steps.append(f"Learn {gap.skill_name} to improve {best_match.role_name} readiness")

    return CareerDashboard(
        user_id=user_id,
        overall_readiness=overall_readiness,
        primary_role=best_match.role_name if best_match else None,
        total_skills=len(skills),
        skills_by_category=categories,
        top_skills=[
            {"slug": s.skill_slug, "name": s.skill_name, "level": s.level}
            for s in top_skills
        ],
        portfolio_projects=len(active_projects),
        featured_projects=len(featured_projects),
        resume_versions=len(active_versions),
        latest_ats_score=latest_ats,
        best_role_match=best_match.role if best_match else None,
        best_match_score=best_match.readiness_score if best_match else 0,
        next_steps=next_steps[:5],
    )


# ==============================================================================
# PUBLIC PORTFOLIO
# ==============================================================================

@router.get("/public/{user_id}/portfolio", response_model=List[PortfolioProjectPublic])
async def get_public_portfolio(user_id: UUID):
    """Get a user's public portfolio (no auth required)"""
    projects = portfolio_projects_db.get(user_id, [])

    return [
        PortfolioProjectPublic(
            id=p.id,
            user_id=p.user_id,
            title=p.title,
            description=p.description,
            github_url=p.github_url,
            demo_url=p.demo_url,
            screenshot_url=p.screenshot_url,
            skills=p.skills,
            technologies=p.technologies,
            is_public=p.is_public,
            is_featured=p.is_featured,
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in projects
        if p.is_active and p.is_public
    ]
