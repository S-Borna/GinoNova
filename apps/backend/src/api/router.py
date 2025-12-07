from fastapi import APIRouter
from .system import system_router
from .auth import auth_router
from .version import router as version_router
from .modules import modules_router
from .tasks import tasks_router
from .studyflow import studyflow_router
from .progress import progress_router
from .dashboard import dashboard_router
from .ai import ai_router
from .data import data_router
from .admin import admin_router
from .profile import profile_router
from .task_progress import task_progress_router
from .routes.billing import router as billing_router
from .routes.certificates import router as certificates_router
from .routes.badges import router as badges_router
from .routes.ai_chat import router as ai_chat_router
from .routes.analytics import router as analytics_router
from .routes.notifications import router as notifications_router
from .routes.search import router as search_router
from .routes.notion import router as notion_router
from .routes.content import router as content_router
from .routes.marketplace import router as marketplace_router
from .routes.community import router as community_router
from .routes.ai_generator import router as ai_generator_router
from .routes.organization import router as organization_router
from .routes.career import router as career_router
from .routes.bookmarks import router as bookmarks_router
from .routes.quiz import router as quiz_router
from .routes.study import router as study_router
from .routes.dallas import router as dallas_router

# Phase 22-28: Final production-ready routes
from .routes.observability import observability_router
from .routes.iac import iac_router
from .routes.finops import finops_router
from .routes.monitoring import monitoring_router
from .routes.ml import ml_router
from .routes.public_api import public_api_router

api_router = APIRouter()

api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(version_router, prefix="/version", tags=["version"])
api_router.include_router(modules_router, prefix="/modules", tags=["modules"])
api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
api_router.include_router(task_progress_router, prefix="/tasks", tags=["task-progress"])
api_router.include_router(studyflow_router, prefix="/studyflow", tags=["studyflow"])
api_router.include_router(progress_router, prefix="/progress", tags=["progress"])
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(ai_router, prefix="/ai", tags=["ai"])
api_router.include_router(data_router, tags=["data"])
api_router.include_router(admin_router, prefix="/admin", tags=["admin"])
api_router.include_router(profile_router, prefix="/profile", tags=["profile"])
api_router.include_router(billing_router, tags=["billing"])
api_router.include_router(certificates_router, tags=["certificates"])
api_router.include_router(badges_router, tags=["badges"])
api_router.include_router(ai_chat_router, tags=["ai-assistant"])
api_router.include_router(analytics_router, tags=["analytics"])
api_router.include_router(notifications_router, tags=["notifications"])
api_router.include_router(search_router, tags=["search"])
api_router.include_router(notion_router, tags=["notion"])
api_router.include_router(content_router, tags=["content"])
api_router.include_router(marketplace_router, tags=["marketplace"])
api_router.include_router(community_router, tags=["community"])
api_router.include_router(ai_generator_router, tags=["ai-generator"])
api_router.include_router(organization_router, tags=["organization"])
api_router.include_router(career_router, tags=["career"])
api_router.include_router(bookmarks_router, tags=["bookmarks"])
api_router.include_router(quiz_router, tags=["quiz"])
api_router.include_router(study_router, tags=["study"])
api_router.include_router(dallas_router, tags=["dallas"])

# Phase 22-28: Final production-ready routes
api_router.include_router(observability_router, tags=["observability"])
api_router.include_router(iac_router, tags=["iac"])
api_router.include_router(finops_router, tags=["finops"])
api_router.include_router(monitoring_router, tags=["monitoring"])
api_router.include_router(ml_router, tags=["ml"])
api_router.include_router(public_api_router, tags=["public-api"])
