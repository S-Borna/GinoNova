"""
Phase 28 - Public API, Webhooks & Integration Layer API routes.
"""
from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4
import secrets

from fastapi import APIRouter, Query, Response, Header

from ...schemas.public_api import (
    PublicAPIStatus,
    APIKey,
    APIKeyCreate,
    APIKeyCreated,
    APIKeyPermission,
    APIKeyUsage,
    APIKeyValidation,
    WebhookEndpoint,
    WebhookEndpointCreate,
    WebhookEndpointCreated,
    WebhookEvent,
    WebhookDelivery,
    DeliveryStatus,
    RateLimitInfo,
)

public_api_router = APIRouter(prefix="/public", tags=["Public API"])


def add_phase_header(response: Response):
    response.headers["X-Phase"] = "28-public-api"


def generate_api_key() -> str:
    """Generate a secure API key."""
    return f"dvh_{secrets.token_urlsafe(32)}"


def generate_webhook_secret() -> str:
    """Generate a webhook secret."""
    return f"whsec_{secrets.token_urlsafe(24)}"


# ============ Status Endpoints ============

@public_api_router.get("/status", response_model=PublicAPIStatus)
def get_public_api_status(response: Response) -> PublicAPIStatus:
    """
    Get Public API status.
    """
    add_phase_header(response)

    return PublicAPIStatus(
        status="operational",
        version="28.0",
        api_version="v1",
        base_url="/api/v1/public",
        documentation_url="/docs",
        total_api_keys=45,
        total_webhooks=12,
        requests_today=15420
    )


# ============ API Key Endpoints ============

@public_api_router.get("/keys")
def list_api_keys(response: Response) -> list[APIKey]:
    """
    List API keys for the authenticated user.
    """
    add_phase_header(response)

    return [
        APIKey(
            id="key-1",
            name="Production API",
            key_prefix="dvh_abc1",
            user_id="user-1",
            permissions=[APIKeyPermission.read_modules, APIKeyPermission.read_tasks, APIKeyPermission.read_analytics],
            rate_limit=2000,
            active=True,
            last_used_at=datetime.utcnow() - timedelta(minutes=5),
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
        APIKey(
            id="key-2",
            name="CI/CD Integration",
            key_prefix="dvh_def2",
            user_id="user-1",
            permissions=[APIKeyPermission.read_modules, APIKeyPermission.write_progress],
            rate_limit=1000,
            active=True,
            last_used_at=datetime.utcnow() - timedelta(hours=2),
            created_at=datetime.utcnow() - timedelta(days=14)
        ),
    ]


@public_api_router.post("/keys", response_model=APIKeyCreated)
def create_api_key(
    key_data: APIKeyCreate,
    response: Response,
) -> APIKeyCreated:
    """
    Create a new API key.
    """
    add_phase_header(response)

    new_key = generate_api_key()

    return APIKeyCreated(
        id=str(uuid4()),
        name=key_data.name,
        key=new_key,
        permissions=key_data.permissions,
        created_at=datetime.utcnow()
    )


@public_api_router.delete("/keys/{key_id}")
def revoke_api_key(key_id: str, response: Response) -> dict:
    """
    Revoke an API key.
    """
    add_phase_header(response)

    return {"status": "revoked", "key_id": key_id}


@public_api_router.get("/keys/{key_id}/usage", response_model=APIKeyUsage)
def get_api_key_usage(key_id: str, response: Response) -> APIKeyUsage:
    """
    Get API key usage statistics.
    """
    add_phase_header(response)

    return APIKeyUsage(
        key_id=key_id,
        requests_today=1250,
        requests_this_month=28500,
        rate_limit=2000,
        rate_limit_remaining=750,
        last_request_at=datetime.utcnow() - timedelta(minutes=2)
    )


@public_api_router.post("/keys/validate", response_model=APIKeyValidation)
def validate_api_key(
    response: Response,
    x_api_key: Optional[str] = Header(None),
) -> APIKeyValidation:
    """
    Validate an API key.
    """
    add_phase_header(response)

    if not x_api_key or not x_api_key.startswith("dvh_"):
        return APIKeyValidation(
            valid=False,
            rate_limit_remaining=0
        )

    return APIKeyValidation(
        valid=True,
        key_id="key-1",
        user_id="user-1",
        permissions=[APIKeyPermission.read_modules, APIKeyPermission.read_tasks],
        rate_limit_remaining=1850
    )


# ============ Webhook Endpoints ============

@public_api_router.get("/webhooks")
def list_webhooks(response: Response) -> list[WebhookEndpoint]:
    """
    List webhook endpoints.
    """
    add_phase_header(response)

    return [
        WebhookEndpoint(
            id="wh-1",
            url="https://example.com/webhooks/devopshub",
            description="Production webhook",
            event_types=[WebhookEvent.task_completed, WebhookEvent.module_completed],
            active=True,
            secret_prefix="whsec_ab",
            created_at=datetime.utcnow() - timedelta(days=30)
        ),
        WebhookEndpoint(
            id="wh-2",
            url="https://api.myapp.com/hooks/learning",
            description="Analytics integration",
            event_types=[WebhookEvent.studyflow_minute, WebhookEvent.ai_recommendation],
            active=True,
            secret_prefix="whsec_cd",
            created_at=datetime.utcnow() - timedelta(days=14)
        ),
    ]


@public_api_router.post("/webhooks", response_model=WebhookEndpointCreated)
def create_webhook(
    webhook_data: WebhookEndpointCreate,
    response: Response,
) -> WebhookEndpointCreated:
    """
    Create a new webhook endpoint.
    """
    add_phase_header(response)

    secret = generate_webhook_secret()

    return WebhookEndpointCreated(
        id=str(uuid4()),
        url=webhook_data.url,
        event_types=webhook_data.event_types,
        secret=secret,
        created_at=datetime.utcnow()
    )


@public_api_router.delete("/webhooks/{webhook_id}")
def delete_webhook(webhook_id: str, response: Response) -> dict:
    """
    Delete a webhook endpoint.
    """
    add_phase_header(response)

    return {"status": "deleted", "webhook_id": webhook_id}


@public_api_router.put("/webhooks/{webhook_id}/toggle")
def toggle_webhook(webhook_id: str, response: Response, active: bool = True) -> WebhookEndpoint:
    """
    Enable or disable a webhook.
    """
    add_phase_header(response)

    return WebhookEndpoint(
        id=webhook_id,
        url="https://example.com/webhooks/devopshub",
        event_types=[WebhookEvent.task_completed],
        active=active,
        secret_prefix="whsec_ab",
        created_at=datetime.utcnow() - timedelta(days=30)
    )


@public_api_router.get("/webhooks/{webhook_id}/deliveries")
def list_webhook_deliveries(
    webhook_id: str,
    response: Response,
    limit: int = Query(20, le=100),
) -> list[WebhookDelivery]:
    """
    List webhook delivery history.
    """
    add_phase_header(response)

    return [
        WebhookDelivery(
            id=str(uuid4()),
            endpoint_id=webhook_id,
            event_type=WebhookEvent.task_completed,
            payload={"user_id": "u-1", "task_id": "t-1", "module_id": "m-1"},
            status=DeliveryStatus.delivered,
            http_status=200,
            attempts=1,
            delivered_at=datetime.utcnow() - timedelta(minutes=i * 10),
            created_at=datetime.utcnow() - timedelta(minutes=i * 10)
        )
        for i in range(min(limit, 10))
    ]


@public_api_router.post("/webhooks/{webhook_id}/test")
def test_webhook(webhook_id: str, response: Response) -> WebhookDelivery:
    """
    Send a test webhook.
    """
    add_phase_header(response)

    return WebhookDelivery(
        id=str(uuid4()),
        endpoint_id=webhook_id,
        event_type=WebhookEvent.task_completed,
        payload={"test": True, "message": "This is a test webhook"},
        status=DeliveryStatus.delivered,
        http_status=200,
        attempts=1,
        delivered_at=datetime.utcnow(),
        created_at=datetime.utcnow()
    )


# ============ Rate Limit Endpoints ============

@public_api_router.get("/rate-limit", response_model=RateLimitInfo)
def get_rate_limit_info(
    response: Response,
    x_api_key: Optional[str] = Header(None),
) -> RateLimitInfo:
    """
    Get current rate limit status.
    """
    add_phase_header(response)

    return RateLimitInfo(
        requests_per_minute=2000,
        writes_per_minute=60,
        ai_calls_per_day=200,
        remaining_requests=1850,
        remaining_writes=55,
        remaining_ai_calls=185,
        reset_at=datetime.utcnow() + timedelta(minutes=1)
    )


# ============ Public Data Endpoints ============

@public_api_router.get("/v1/modules")
def public_list_modules(response: Response) -> list[dict]:
    """
    Public API: List modules.
    """
    add_phase_header(response)

    return [
        {"id": "m-1", "name": "Environment Setup", "slug": "01-environment-setup", "tasks_count": 25},
        {"id": "m-2", "name": "Linux Mastery", "slug": "02-linux-mastery", "tasks_count": 35},
        {"id": "m-3", "name": "Shell Scripting", "slug": "03-shell-scripting", "tasks_count": 30},
    ]


@public_api_router.get("/v1/modules/{module_id}")
def public_get_module(module_id: str, response: Response) -> dict:
    """
    Public API: Get module details.
    """
    add_phase_header(response)

    return {
        "id": module_id,
        "name": "Environment Setup",
        "slug": "01-environment-setup",
        "description": "Set up your DevOps development environment",
        "tasks_count": 25,
        "estimated_hours": 8
    }


@public_api_router.get("/v1/modules/{module_id}/tasks")
def public_list_module_tasks(module_id: str, response: Response) -> list[dict]:
    """
    Public API: List tasks in a module.
    """
    add_phase_header(response)

    return [
        {"id": "t-1", "title": "Install VS Code", "type": "lesson", "xp_reward": 25},
        {"id": "t-2", "title": "Configure Git", "type": "exercise", "xp_reward": 50},
        {"id": "t-3", "title": "Set up SSH keys", "type": "quiz", "xp_reward": 30},
    ]


@public_api_router.get("/v1/users/{user_id}/progress")
def public_get_user_progress(user_id: str, response: Response) -> dict:
    """
    Public API: Get user progress.
    """
    add_phase_header(response)

    return {
        "user_id": user_id,
        "total_xp": 2500,
        "level": 8,
        "tasks_completed": 45,
        "modules_completed": 3,
        "current_streak": 7
    }


@public_api_router.post("/v1/users/{user_id}/progress/update")
def public_update_user_progress(
    user_id: str,
    response: Response,
    task_id: str = Query(...),
    status: str = Query("completed"),
) -> dict:
    """
    Public API: Update user progress.
    """
    add_phase_header(response)

    return {
        "user_id": user_id,
        "task_id": task_id,
        "status": status,
        "xp_earned": 25,
        "updated_at": datetime.utcnow().isoformat()
    }


@public_api_router.get("/v1/analytics/heatmap")
def public_get_heatmap(response: Response) -> dict:
    """
    Public API: Get activity heatmap data.
    """
    add_phase_header(response)

    return {
        "period": "30d",
        "data": [
            {"date": (datetime.utcnow() - timedelta(days=i)).strftime("%Y-%m-%d"), "count": 5 + i % 10}
            for i in range(30)
        ]
    }
