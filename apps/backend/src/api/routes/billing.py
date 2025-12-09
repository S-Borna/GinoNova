"""
Billing API Routes - Phase 11
Stripe subscription management endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from uuid import UUID
from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/billing", tags=["billing"])

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://ginonova.com")


# Response models
class PlanResponse(BaseModel):
    name: str
    price: int
    billing: str
    features: list[str]


class CheckoutRequest(BaseModel):
    plan: str  # pro_monthly, pro_yearly, enterprise_monthly, enterprise_yearly


class CheckoutResponse(BaseModel):
    checkout_url: str


# Plan definitions
PLANS = [
    {
        "name": "Free",
        "price": 0,
        "billing": "forever",
        "features": [
            "5 modules access",
            "3 AI hints per day",
            "Basic progress tracking",
            "Community support",
        ]
    },
    {
        "name": "Pro",
        "price": 29,
        "billing": "monthly",
        "features": [
            "All 15 modules",
            "Unlimited AI hints",
            "Certificates on completion",
            "Priority support",
            "StudyFlow advanced features",
            "Progress analytics",
        ]
    },
    {
        "name": "Enterprise",
        "price": 99,
        "billing": "monthly",
        "features": [
            "Everything in Pro",
            "Team management (up to 50 seats)",
            "SSO integration",
            "Custom content",
            "Dedicated support",
            "Admin dashboard",
            "API access",
        ]
    },
]


@router.get("/plans")
async def get_plans():
    """Get all available subscription plans."""
    return {"plans": PLANS}


@router.get("/status")
async def get_billing_status(user_id: Optional[UUID] = None):
    """Get current billing status for user."""
    # TODO: Implement actual database lookup
    return {
        "plan": "free",
        "status": "active",
        "ai_quota_remaining": 3,
        "next_billing_date": None,
    }


@router.post("/checkout", response_model=CheckoutResponse)
async def create_checkout_session(request: CheckoutRequest):
    """Create Stripe checkout session for subscription."""
    if not STRIPE_SECRET_KEY:
        raise HTTPException(
            status_code=503,
            detail="Billing is not configured. Please contact support."
        )

    try:
        import stripe
        stripe.api_key = STRIPE_SECRET_KEY

        # Price IDs from Stripe Dashboard
        # TODO: Replace with actual Stripe price IDs
        price_ids = {
            "pro_monthly": os.getenv("STRIPE_PRICE_PRO_MONTHLY", "price_placeholder"),
            "pro_yearly": os.getenv("STRIPE_PRICE_PRO_YEARLY", "price_placeholder"),
            "enterprise_monthly": os.getenv("STRIPE_PRICE_ENTERPRISE_MONTHLY", "price_placeholder"),
            "enterprise_yearly": os.getenv("STRIPE_PRICE_ENTERPRISE_YEARLY", "price_placeholder"),
        }

        price_id = price_ids.get(request.plan)
        if not price_id or price_id == "price_placeholder":
            raise HTTPException(
                status_code=400,
                detail=f"Invalid plan: {request.plan}"
            )

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            mode="subscription",
            success_url=f"{FRONTEND_URL}/dashboard?checkout=success",
            cancel_url=f"{FRONTEND_URL}/pricing?checkout=canceled",
            metadata={
                "plan": request.plan,
            }
        )

        return CheckoutResponse(checkout_url=session.url)

    except ImportError:
        raise HTTPException(
            status_code=503,
            detail="Stripe module not installed"
        )
    except Exception as e:
        logger.error(f"Stripe checkout error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to create checkout session"
        )


@router.post("/portal")
async def create_portal_session(user_id: Optional[UUID] = None):
    """Create Stripe billing portal session for managing subscription."""
    if not STRIPE_SECRET_KEY:
        raise HTTPException(status_code=503, detail="Billing not configured")

    # TODO: Get stripe_customer_id from database based on user_id
    stripe_customer_id = None

    if not stripe_customer_id:
        raise HTTPException(
            status_code=400,
            detail="No active subscription found"
        )

    try:
        import stripe
        stripe.api_key = STRIPE_SECRET_KEY

        session = stripe.billing_portal.Session.create(
            customer=stripe_customer_id,
            return_url=f"{FRONTEND_URL}/settings/billing",
        )

        return {"portal_url": session.url}

    except Exception as e:
        logger.error(f"Stripe portal error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create portal session")


@router.post("/webhook")
async def stripe_webhook(request: Request):
    """Handle Stripe webhook events."""
    if not STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=503, detail="Webhook not configured")

    try:
        import stripe
        payload = await request.body()
        sig_header = request.headers.get("stripe-signature")

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
        except stripe.error.SignatureVerificationError:
            raise HTTPException(status_code=400, detail="Invalid signature")

        event_type = event["type"]
        event_data = event["data"]["object"]

        logger.info(f"Stripe webhook: {event_type}")

        # Handle different event types
        if event_type == "checkout.session.completed":
            # New subscription created
            customer_id = event_data.get("customer")
            subscription_id = event_data.get("subscription")
            # TODO: Update user's subscription in database

        elif event_type == "customer.subscription.updated":
            # Subscription changed (upgrade/downgrade)
            subscription_id = event_data.get("id")
            status = event_data.get("status")
            # TODO: Update subscription status

        elif event_type == "customer.subscription.deleted":
            # Subscription canceled
            subscription_id = event_data.get("id")
            # TODO: Downgrade user to free plan

        elif event_type == "invoice.paid":
            # Payment successful
            customer_id = event_data.get("customer")
            # TODO: Update billing history

        elif event_type == "invoice.payment_failed":
            # Payment failed
            customer_id = event_data.get("customer")
            # TODO: Notify user, update status to past_due

        return {"status": "ok", "event": event_type}

    except ImportError:
        raise HTTPException(status_code=503, detail="Stripe module not installed")
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        raise HTTPException(status_code=500, detail="Webhook processing failed")
