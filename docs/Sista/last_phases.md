================================================================================
PHASE 22 — PostgreSQL + Redis (KRITISK - GÖR FÖRST)
================================================================================

STATUS: ✅ KLAR (2025-11-29)

UTFÖRT:

- [x] psycopg2-binary redan fanns i pyproject.toml
- [x] asyncpg redan fanns i pyproject.toml
- [x] redis = "^5.0.0" tillagt i pyproject.toml
- [x] Skapade apps/backend/src/db/redis_client.py med:
      - get_redis_client() singleton
      - is_redis_configured() check
      - cache_get/set/delete funktioner
      - check_rate_limit() för Phase 29
- [x] Uppdaterade lifespan i main.py med Redis-logik
- [x] CORS redan korrekt konfigurerad för saids-devopshub.netlify.app

BAKGRUND:
Backend körs på Railway. PostgreSQL och Redis är konfigurerade med DATABASE_URL och REDIS_URL.
Backend-koden stödjer redan PostgreSQL men dependencies saknas.

STEG 1 — Uppdatera apps/backend/pyproject.toml

Lägg till under [tool.poetry.dependencies]:

psycopg2-binary = "^2.9.9"
asyncpg = "^0.29.0"
redis = "^5.0.0"

STEG 2 — Skapa apps/backend/src/db/redis_client.py

"""
Redis Client - Phase 22
"""
import os
import json
import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)
REDIS_URL = os.getenv("REDIS_URL", "")
_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is not None:
        return _redis_client
    if not REDIS_URL:
        logger.warning("REDIS_URL not set")
        return None
    try:
        import redis
        _redis_client = redis.from_url(REDIS_URL, decode_responses=True, socket_timeout=5)
        _redis_client.ping()
        logger.info("✅ Redis connected")
        return _redis_client
    except Exception as e:
        logger.error(f"Redis failed: {e}")
        return None

def is_redis_configured() -> bool:
    return get_redis_client() is not None

def cache_get(key: str) -> Optional[Any]:
    client = get_redis_client()
    if not client:
        return None
    try:
        value = client.get(key)
        return json.loads(value) if value else None
    except:
        return None

def cache_set(key: str, value: Any, ttl: int = 300) -> bool:
    client = get_redis_client()
    if not client:
        return False
    try:
        client.setex(key, ttl, json.dumps(value, default=str))
        return True
    except:
        return False

def cache_delete(key: str) -> bool:
    client = get_redis_client()
    if not client:
        return False
    try:
        client.delete(key)
        return True
    except:
        return False

STEG 3 — Uppdatera apps/backend/src/main.py lifespan

Ersätt lifespan-funktionen:

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting DevOps Hub Backend...")

    from .db.database import is_db_configured, init_db
    if is_db_configured():
        logger.info("🗄️ PostgreSQL detected - initializing tables...")
        try:
            init_db()
            logger.info("✅ Database tables ready!")
        except Exception as e:
            logger.error(f"❌ Database init failed: {e}")
    else:
        logger.info("📝 Using in-memory storage (no DATABASE_URL)")

    from .db.redis_client import is_redis_configured
    if is_redis_configured():
        logger.info("🔴 Redis connected!")
    else:
        logger.info("📝 Redis not configured")

    auto_seed_if_empty()
    logger.info("✅ Backend ready!")
    yield
    logger.info("👋 Shutting down...")

STEG 4 — Säkerställ CORS i main.py

default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://saasprojekt.netlify.app",
]

STEG 5 — Commit och push

cd apps/backend && poetry lock && poetry install
git add . && git commit -m "fix(phase22): add PostgreSQL and Redis dependencies" && git push origin main

VERIFIERING:
Railway logs ska visa:

- "🗄️ PostgreSQL detected - initializing tables..."
- "✅ Database tables ready!"
- "🔴 Redis connected!"

================================================================================
PHASE 11 — Billing + Tenants (Stripe)
================================================================================

STATUS: ✅ KLAR (2025-11-29)

UTFÖRT:
- [x] Skapade apps/backend/src/db/models_billing.py med:
      - PlanType enum (FREE, PRO, ENTERPRISE)
      - SubscriptionStatus enum (ACTIVE, CANCELED, PAST_DUE, TRIALING, PAUSED)
      - SubscriptionPlan model med Stripe price IDs
      - Tenant model för multi-tenant support
      - TenantUser model för team management
      - Invoice model för billing history
- [x] Skapade apps/backend/src/api/routes/billing.py med:
      - GET /billing/plans - hämta alla planer
      - GET /billing/status - hämta billing status för användare
      - POST /billing/checkout - skapa Stripe checkout session
      - POST /billing/portal - skapa Stripe billing portal session
      - POST /billing/webhook - hantera Stripe webhooks
- [x] La till stripe = "^7.0.0" och openai = "^1.0.0" i pyproject.toml
- [x] Registrerade billing_router i api/router.py

BAKGRUND:
Monetisering med Free/Pro/Enterprise plans via Stripe.

STEG 1 — Skapa apps/backend/src/db/models_billing.py

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum
from .database import Base

class PlanType(str, enum.Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"

class SubscriptionStatus(str, enum.Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    TRIALING = "trialing"

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    plan_type = Column(Enum(PlanType), nullable=False, unique=True)
    price_monthly = Column(Integer, default=0)
    price_yearly = Column(Integer, default=0)
    ai_quota = Column(Integer, default=10)
    max_studyflow_sessions = Column(Integer, default=3)
    features = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("subscription_plans.id"))
    subscription_status = Column(Enum(SubscriptionStatus), default=SubscriptionStatus.ACTIVE)
    stripe_customer_id = Column(String(255), nullable=True)
    stripe_subscription_id = Column(String(255), nullable=True)
    seats_total = Column(Integer, default=1)
    seats_used = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", foreign_keys=[owner_user_id])
    plan = relationship("SubscriptionPlan")

class TenantUser(Base):
    __tablename__ = "tenant_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    role = Column(String(20), default="member")
    created_at = Column(DateTime, default=datetime.utcnow)

STEG 2 — Skapa apps/backend/src/api/routes/billing.py

from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
import os

router = APIRouter(prefix="/billing", tags=["billing"])

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

@router.get("/plans")
async def get_plans():
    return {
        "plans": [
            {"name": "Free", "price": 0, "features": ["5 modules", "3 AI calls/day", "Basic progress"]},
            {"name": "Pro", "price": 29, "features": ["All modules", "Unlimited AI", "Certificates", "Priority support"]},
            {"name": "Enterprise", "price": 99, "features": ["Everything in Pro", "Team management", "SSO", "Custom content"]},
        ]
    }

@router.post("/checkout")
async def create_checkout_session(plan: str):
    if not STRIPE_SECRET_KEY:
        raise HTTPException(status_code=503, detail="Billing not configured")

    import stripe
    stripe.api_key = STRIPE_SECRET_KEY

    price_ids = {
        "pro_monthly": "price_xxx",
        "pro_yearly": "price_xxx",
        "enterprise_monthly": "price_xxx",
    }

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": price_ids.get(plan), "quantity": 1}],
        mode="subscription",
        success_url="https://saasprojekt.netlify.app/dashboard?success=true",
        cancel_url="https://saasprojekt.netlify.app/pricing?canceled=true",
    )

    return {"checkout_url": session.url}

@router.post("/webhook")
async def stripe_webhook(request):
    import stripe
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)
    except:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        # Update user subscription in database

    return {"status": "ok"}

STEG 3 — Lägg till stripe dependency

I apps/backend/pyproject.toml:
stripe = "^7.0.0"

STEG 4 — Registrera router i main.py

from .api.routes.billing import router as billing_router
app.include_router(billing_router, prefix="/api")

STEG 5 — Commit

git add . && git commit -m "feat(phase11): add billing models and Stripe endpoints" && git push origin main

================================================================================
PHASE 29 — Production Hardening
================================================================================

STATUS: ✅ KLAR (2025-11-29)

UTFÖRT:
- [x] Skapade apps/backend/src/api/middleware/rate_limit.py med:
      - RateLimitMiddleware med Redis-baserad rate limiting
      - Exempt paths för health checks
      - X-RateLimit headers i responses
- [x] Skapade apps/backend/src/api/middleware/error_handler.py med:
      - ErrorHandlerMiddleware för global exception handling
      - Unique request_id för error tracking
      - Safe error messages till klienten
- [x] Skapade apps/backend/src/core/security_audit.py med:
      - sanitize_input() för XSS/SQL protection
      - validate_email() för email validation
      - check_password_strength() för lösenordsvalidering
      - sanitize_filename() för filuppladdningar
      - is_safe_url() för redirect-validering
      - log_security_event() för audit trail
- [x] Registrerade middleware i main.py (100 req/min limit)

BAKGRUND:
Säkerhet, rate limiting, error handling för production.

STEG 1 — Skapa apps/backend/src/api/middleware/rate_limit.py

from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from ..db.redis_client import check_rate_limit, is_redis_configured
import logging

logger = logging.getLogger(__name__)

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.rpm = requests_per_minute

    async def dispatch(self, request: Request, call_next) -> Response:
        if request.url.path in ["/health", "/.well-known/health"]:
            return await call_next(request)

        if not is_redis_configured():
            return await call_next(request)

        client_ip = request.headers.get("X-Forwarded-For", request.client.host)
        identifier = f"ip:{client_ip}"

        allowed, remaining = check_rate_limit(identifier, self.rpm, 60)

        if not allowed:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded"
            )

        response = await call_next(request)
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        return response

STEG 2 — Skapa apps/backend/src/api/middleware/error_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging
import traceback

logger = logging.getLogger(__name__)

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            logger.error(f"Unhandled error: {e}\n{traceback.format_exc()}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error", "request_id": str(id(request))}
            )

STEG 3 — Lägg till middleware i main.py

from .api.middleware.rate_limit import RateLimitMiddleware
from .api.middleware.error_handler import ErrorHandlerMiddleware

app.add_middleware(RateLimitMiddleware, requests_per_minute=100)
app.add_middleware(ErrorHandlerMiddleware)

STEG 4 — Skapa apps/backend/src/core/security_audit.py

"""
Security utilities
"""
import re
from typing import Optional

def sanitize_input(value: str, max_length: int = 1000) -> str:
    if not value:
        return ""
    value = value[:max_length]
    value = re.sub(r'<[^>]*>', '', value)
    return value.strip()

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def check_password_strength(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain lowercase letter"
    if not re.search(r'\d', password):
        return False, "Password must contain a number"
    return True, "Password is strong"

STEG 5 — Commit

git add . && git commit -m "feat(phase29): add rate limiting and security hardening" && git push origin main

================================================================================
PHASE 21 — Certification & Badge System
================================================================================

BAKGRUND:
Certifikat och badges för att validera kompetens.

STEG 1 — Skapa apps/backend/src/db/models_certification.py

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum
from .database import Base

class CertificateType(str, enum.Enum):
    MODULE = "module"
    TRACK = "track"
    MASTER = "master"

class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    certificate_type = Column(Enum(CertificateType), nullable=False)
    reference_id = Column(String(100), nullable=False)
    reference_name = Column(String(255), nullable=False)
    pdf_url = Column(String(500), nullable=True)
    verification_code = Column(String(50), unique=True, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

    user = relationship("User")

class Badge(Base):
    __tablename__ = "badges"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    badge_slug = Column(String(100), nullable=False)
    badge_name = Column(String(255), nullable=False)
    level = Column(Integer, default=1)
    awarded_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

STEG 2 — Skapa apps/backend/src/api/routes/certificates.py

from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List
import secrets

router = APIRouter(prefix="/certificates", tags=["certificates"])

@router.get("/")
async def get_my_certificates(user_id: UUID):
    # Fetch from database
    return {"certificates": []}

@router.get("/verify/{code}")
async def verify_certificate(code: str):
    # Public endpoint - no auth required
    # Lookup certificate by verification_code
    return {"valid": True, "certificate": {}}

@router.post("/generate/{module_id}")
async def generate_certificate(module_id: str, user_id: UUID):
    verification_code = secrets.token_urlsafe(16)
    # Check if user completed module 100%
    # Generate PDF
    # Store in database
    return {"certificate_id": "xxx", "verification_code": verification_code}

STEG 3 — Skapa apps/backend/src/api/routes/badges.py

from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/badges", tags=["badges"])

BADGE_DEFINITIONS = {
    "linux_beginner": {"name": "Linux Beginner", "levels": 5},
    "git_master": {"name": "Git Master", "levels": 5},
    "docker_pro": {"name": "Docker Pro", "levels": 5},
    "k8s_ninja": {"name": "Kubernetes Ninja", "levels": 5},
    "streak_warrior": {"name": "Streak Warrior", "levels": 5},
}

@router.get("/")
async def get_my_badges(user_id: UUID):
    return {"badges": []}

@router.get("/available")
async def get_available_badges():
    return {"badges": BADGE_DEFINITIONS}

@router.post("/check")
async def check_and_award_badges(user_id: UUID):
    # Check progress and award badges
    return {"new_badges": []}

STEG 4 — Registrera routers

from .api.routes.certificates import router as certificates_router
from .api.routes.badges import router as badges_router
app.include_router(certificates_router, prefix="/api")
app.include_router(badges_router, prefix="/api")

STEG 5 — Commit

git add . && git commit -m "feat(phase21): add certification and badge system" && git push origin main

================================================================================
PHASE 16 — AI Assistant (User-Facing)
================================================================================

BAKGRUND:
AI chatbot för hints, förklaringar och studyflow-rekommendationer.

STEG 1 — Skapa apps/backend/src/db/models_ai_chat.py

from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from .database import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    session_id = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    context = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

STEG 2 — Skapa apps/backend/src/services/ai_assistant.py

import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

SYSTEM_PROMPT = """Du är DevOpsHub Assistant, en hjälpsam AI-tutor för DevOps-utbildning.

Du hjälper studenter med:

- Förklara DevOps-koncept (Linux, Git, Docker, Kubernetes, AWS, Terraform)
- Ge hints på uppgifter utan att ge hela svaret
- Föreslå studiestrategier
- Svara på tekniska frågor

Håll svar koncisa och pedagogiska. Använd kodexempel när relevant.
Om studenten kämpar, ge ledtrådar istället för direkta svar."""

async def get_ai_response(
    message: str,
    context: Optional[dict] = None,
    history: list = []
) -> str:
    if not OPENAI_API_KEY:
        return "AI Assistant är inte konfigurerad. Kontakta support."

    try:
        from openai import AsyncOpenAI
        client = AsyncOpenAI(api_key=OPENAI_API_KEY)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if context:
            context_str = f"\nKontext: Studenten arbetar med {context.get('module', 'okänd modul')}, uppgift: {context.get('task', 'okänd')}"
            messages[0]["content"] += context_str

        for h in history[-10:]:
            messages.append({"role": h["role"], "content": h["content"]})

        messages.append({"role": "user", "content": message})

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1000,
            temperature=0.7
        )

        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"AI error: {e}")
        return "Ett fel uppstod. Försök igen."

async def get_hint(task_id: str, task_content: str, user_attempt: str) -> str:
    prompt = f"""Studenten arbetar med denna uppgift:
{task_content}

Deras försök/fråga: {user_attempt}

Ge en hint som leder dem i rätt riktning utan att ge hela svaret."""

    return await get_ai_response(prompt)

STEG 3 — Skapa apps/backend/src/api/routes/ai_chat.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
from ...services.ai_assistant import get_ai_response, get_hint

router = APIRouter(prefix="/ai", tags=["ai"])

class ChatMessage(BaseModel):
    message: str
    context: Optional[dict] = None

class HintRequest(BaseModel):
    task_id: str
    task_content: str
    user_question: str

@router.post("/chat")
async def chat(request: ChatMessage, user_id: UUID):
    response = await get_ai_response(
        message=request.message,
        context=request.context,
        history=[]
    )
    return {"response": response}

@router.post("/hint")
async def get_task_hint(request: HintRequest, user_id: UUID):
    hint = await get_hint(
        task_id=request.task_id,
        task_content=request.task_content,
        user_attempt=request.user_question
    )
    return {"hint": hint}

@router.get("/history/{session_id}")
async def get_chat_history(session_id: str, user_id: UUID):
    return {"history": []}

STEG 4 — Lägg till openai dependency

I apps/backend/pyproject.toml:
openai = "^1.0.0"

STEG 5 — Registrera router

from .api.routes.ai_chat import router as ai_chat_router
app.include_router(ai_chat_router, prefix="/api")

STEG 6 — Commit

git add . && git commit -m "feat(phase16): add AI assistant chat and hints" && git push origin main

================================================================================
PHASE 13 — Analytics Insight Engine
================================================================================

BAKGRUND:
Spåra användarbeteende, studietid, framsteg för insikter.

STEG 1 — Skapa apps/backend/src/db/models_analytics.py

from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, JSON, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
import uuid
from .database import Base

class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    event_type = Column(String(100), nullable=False)
    event_data = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

class DailyStats(Base):
    __tablename__ = "daily_stats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    study_minutes = Column(Integer, default=0)
    tasks_completed = Column(Integer, default=0)
    xp_earned = Column(Integer, default=0)
    sessions_count = Column(Integer, default=0)

class UserInsights(Base):
    __tablename__ = "user_insights"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    total_study_hours = Column(Float, default=0)
    favorite_time = Column(String(20), nullable=True)
    strongest_skill = Column(String(100), nullable=True)
    weakest_skill = Column(String(100), nullable=True)
    avg_session_length = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)

STEG 2 — Skapa apps/backend/src/api/routes/analytics.py

from fastapi import APIRouter
from uuid import UUID
from datetime import date, timedelta

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.post("/event")
async def track_event(event_type: str, event_data: dict, user_id: UUID):
    # Store event in database
    return {"tracked": True}

@router.get("/user/{user_id}")
async def get_user_analytics(user_id: UUID):
    return {
        "total_study_hours": 0,
        "tasks_completed": 0,
        "current_streak": 0,
        "favorite_time": "morning",
        "weekly_activity": [0, 0, 0, 0, 0, 0, 0],
    }

@router.get("/user/{user_id}/daily")
async def get_daily_stats(user_id: UUID, days: int = 30):
    return {"daily_stats": []}

@router.get("/admin/overview")
async def get_admin_analytics():
    return {
        "total_users": 0,
        "active_today": 0,
        "total_study_hours": 0,
        "popular_modules": [],
    }

STEG 3 — Registrera router

from .api.routes.analytics import router as analytics_router
app.include_router(analytics_router, prefix="/api")

STEG 4 — Commit

git add . && git commit -m "feat(phase13): add analytics insight engine" && git push origin main

================================================================================
PHASE 12 — Notifications
================================================================================

BAKGRUND:
In-app och email-notifikationer.

STEG 1 — Skapa apps/backend/src/db/models_notifications.py

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from .database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(String(1000), nullable=False)
    data = Column(JSON, default=dict)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class NotificationPreference(Base):
    __tablename__ = "notification_preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, unique=True)
    email_enabled = Column(Boolean, default=True)
    push_enabled = Column(Boolean, default=True)
    streak_reminders = Column(Boolean, default=True)
    weekly_summary = Column(Boolean, default=True)
    achievement_alerts = Column(Boolean, default=True)

STEG 2 — Skapa apps/backend/src/api/routes/notifications.py

from fastapi import APIRouter
from uuid import UUID
from typing import List

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.get("/")
async def get_notifications(user_id: UUID, unread_only: bool = False):
    return {"notifications": []}

@router.post("/{notification_id}/read")
async def mark_as_read(notification_id: UUID, user_id: UUID):
    return {"success": True}

@router.post("/read-all")
async def mark_all_as_read(user_id: UUID):
    return {"success": True}

@router.get("/preferences")
async def get_preferences(user_id: UUID):
    return {"preferences": {}}

@router.put("/preferences")
async def update_preferences(user_id: UUID, preferences: dict):
    return {"success": True}

STEG 3 — Skapa apps/backend/src/services/notification_service.py

from typing import Optional
import logging

logger = logging.getLogger(__name__)

async def send_notification(
    user_id: str,
    type: str,
    title: str,
    message: str,
    data: dict = {}
) -> bool:
    # Store in database
    # Optionally send email/push
    logger.info(f"Notification sent to {user_id}: {title}")
    return True

async def send_streak_reminder(user_id: str) -> bool:
    return await send_notification(
        user_id=user_id,
        type="streak_reminder",
        title="Håll din streak igång!",
        message="Du har inte studerat idag. Gör en snabb session för att behålla din streak."
    )

async def send_achievement_notification(user_id: str, achievement: str) -> bool:
    return await send_notification(
        user_id=user_id,
        type="achievement",
        title="Ny prestation!",
        message=f"Grattis! Du har låst upp: {achievement}"
    )

STEG 4 — Registrera router

from .api.routes.notifications import router as notifications_router
app.include_router(notifications_router, prefix="/api")

STEG 5 — Commit

git add . && git commit -m "feat(phase12): add notification system" && git push origin main

================================================================================
EXEKVERINGSORDNING
================================================================================

1. PHASE 22 — PostgreSQL + Redis (KRITISK - fixar "Failed to fetch")
2. PHASE 29 — Production Hardening (säkerhet)
3. PHASE 11 — Billing + Tenants (monetisering)
4. PHASE 21 — Certificates & Badges (user value)
5. PHASE 16 — AI Assistant (user experience)
6. PHASE 13 — Analytics (insikter)
7. PHASE 12 — Notifications (engagement)

Efter varje phase: git push, verifiera Railway deploy, testa funktionalitet.
