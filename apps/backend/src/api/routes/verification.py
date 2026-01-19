"""
Email Verification Routes
Handles email verification flow for new users
"""
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.db.models import User
from src.services.email_service import (
    generate_verification_code,
    get_code_expiry,
    send_verification_email,
    send_welcome_email,
)
from src.core.deps import get_current_user
from src.schemas.user import UserPublic

router = APIRouter()


class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: str


class ResendCodeRequest(BaseModel):
    email: EmailStr


class VerificationResponse(BaseModel):
    ok: bool
    message: str
    is_verified: bool = False


@router.post("/verify", response_model=VerificationResponse)
def verify_email(
    data: VerifyCodeRequest,
    db: Session = Depends(get_db)
):
    """
    Verify email with 6-digit code.
    Called after user enters the code from their email.
    """
    # Find user by email
    user = db.query(User).filter(
        User.email == data.email.lower().strip()
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Användare hittades inte"
        )
    
    # Already verified?
    if user.is_verified:
        return VerificationResponse(
            ok=True,
            message="E-post redan verifierad",
            is_verified=True
        )
    
    # Check if code exists
    if not user.verification_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ingen verifieringskod skickad. Begär en ny kod."
        )
    
    # Check if code expired
    if user.verification_code_expires_at:
        expires_at = user.verification_code_expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        
        if datetime.now(timezone.utc) > expires_at:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Verifieringskoden har gått ut. Begär en ny kod."
            )
    
    # Check code
    if user.verification_code != data.code.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Felaktig verifieringskod"
        )
    
    # Success! Mark as verified
    user.is_verified = True
    user.verification_code = None
    user.verification_code_expires_at = None
    user.updated_at = datetime.now(timezone.utc)
    db.commit()
    
    # Send welcome email (async/background would be better)
    try:
        send_welcome_email(user.email, user.full_name)
    except Exception as e:
        print(f"[Verify] Failed to send welcome email: {e}")
    
    # Log verification
    try:
        from src.api.routes.admin_v2 import add_activity_log
        add_activity_log(
            activity_type="email_verified",
            user_id=str(user.id),
            user_email=user.email,
            user_name=user.full_name,
            details="Email verification completed"
        )
    except Exception:
        pass
    
    return VerificationResponse(
        ok=True,
        message="E-post verifierad! Välkommen till GinoNova!",
        is_verified=True
    )


@router.post("/resend", response_model=VerificationResponse)
def resend_verification_code(
    data: ResendCodeRequest,
    db: Session = Depends(get_db)
):
    """
    Resend verification code to email.
    Rate limited to prevent abuse.
    """
    # Find user
    user = db.query(User).filter(
        User.email == data.email.lower().strip()
    ).first()
    
    if not user:
        # Don't reveal if email exists or not
        return VerificationResponse(
            ok=True,
            message="Om kontot finns skickas en ny kod till din e-post"
        )
    
    # Already verified?
    if user.is_verified:
        return VerificationResponse(
            ok=True,
            message="E-post redan verifierad",
            is_verified=True
        )
    
    # Rate limit: Check if code was sent recently (within 1 minute)
    if user.verification_code_expires_at:
        expires_at = user.verification_code_expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        
        # Code expires in 15 min, so if more than 14 min left, it was just sent
        from datetime import timedelta
        time_until_expiry = expires_at - datetime.now(timezone.utc)
        if time_until_expiry > timedelta(minutes=14):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Vänta en minut innan du begär en ny kod"
            )
    
    # Generate new code
    code = generate_verification_code()
    user.verification_code = code
    user.verification_code_expires_at = get_code_expiry()
    user.updated_at = datetime.now(timezone.utc)
    db.commit()
    
    # Send email
    success = send_verification_email(user.email, code, user.full_name)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Kunde inte skicka verifieringsmail. Försök igen senare."
        )
    
    return VerificationResponse(
        ok=True,
        message="En ny verifieringskod har skickats till din e-post"
    )


@router.get("/status")
def get_verification_status(
    current_user: UserPublic = Depends(get_current_user)
):
    """
    Check if current user's email is verified.
    """
    return {
        "email": current_user.email,
        "is_verified": getattr(current_user, 'is_verified', False)
    }
