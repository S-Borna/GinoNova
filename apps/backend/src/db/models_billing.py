"""
Billing & Tenant Models - Phase 11
Stripe subscription management and multi-tenant support.
"""
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

from .database import Base


class PlanType(str, enum.Enum):
    """Subscription plan types."""
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class SubscriptionStatus(str, enum.Enum):
    """Subscription status values."""
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    TRIALING = "trialing"
    PAUSED = "paused"


class SubscriptionPlan(Base):
    """Available subscription plans."""
    __tablename__ = "subscription_plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    plan_type = Column(Enum(PlanType), nullable=False, unique=True)
    price_monthly = Column(Integer, default=0)  # In cents
    price_yearly = Column(Integer, default=0)   # In cents
    stripe_price_monthly_id = Column(String(100), nullable=True)
    stripe_price_yearly_id = Column(String(100), nullable=True)
    ai_quota = Column(Integer, default=10)  # AI calls per day
    max_studyflow_sessions = Column(Integer, default=3)
    features = Column(JSON, default=dict)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Tenant(Base):
    """
    Tenant for multi-tenant support.
    A tenant can be an individual user or an organization.
    """
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=True)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("subscription_plans.id"), nullable=True)
    subscription_status = Column(Enum(SubscriptionStatus), default=SubscriptionStatus.ACTIVE)
    stripe_customer_id = Column(String(255), nullable=True)
    stripe_subscription_id = Column(String(255), nullable=True)
    seats_total = Column(Integer, default=1)
    seats_used = Column(Integer, default=1)
    trial_ends_at = Column(DateTime, nullable=True)
    current_period_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", foreign_keys=[owner_user_id])
    plan = relationship("SubscriptionPlan")
    members = relationship("TenantUser", back_populates="tenant")


class TenantUser(Base):
    """Association between users and tenants (for team management)."""
    __tablename__ = "tenant_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    role = Column(String(20), default="member")  # owner, admin, member
    invited_at = Column(DateTime, default=datetime.utcnow)
    joined_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    tenant = relationship("Tenant", back_populates="members")
    user = relationship("User")


class Invoice(Base):
    """Invoice records for billing history."""
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    stripe_invoice_id = Column(String(255), nullable=True)
    amount = Column(Integer, default=0)  # In cents
    currency = Column(String(3), default="usd")
    status = Column(String(20), default="pending")  # pending, paid, failed
    invoice_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    paid_at = Column(DateTime, nullable=True)

    # Relationships
    tenant = relationship("Tenant")
