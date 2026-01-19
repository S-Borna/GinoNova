"""
Email Service - Using Resend for transactional emails
Handles email verification, password reset, etc.
"""
import os
import random
import string
from datetime import datetime, timedelta, timezone
from typing import Optional

import resend

# Initialize Resend with API key
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
if RESEND_API_KEY:
    resend.api_key = RESEND_API_KEY

# Email settings
# Domain verified at resend.com/domains
FROM_EMAIL = "GinoNova <noreply@ginonova.com>"
VERIFICATION_CODE_LENGTH = 6
VERIFICATION_CODE_EXPIRY_MINUTES = 15


def generate_verification_code() -> str:
    """Generate a 6-digit verification code"""
    return ''.join(random.choices(string.digits, k=VERIFICATION_CODE_LENGTH))


def get_code_expiry() -> datetime:
    """Get expiry time for verification code (15 minutes from now)"""
    return datetime.now(timezone.utc) + timedelta(minutes=VERIFICATION_CODE_EXPIRY_MINUTES)


def send_verification_email(to_email: str, code: str, user_name: Optional[str] = None) -> bool:
    """
    Send email verification code to user.

    Args:
        to_email: Recipient email address
        code: 6-digit verification code
        user_name: Optional user name for personalization

    Returns:
        True if email sent successfully, False otherwise
    """
    if not RESEND_API_KEY:
        print(f"[Email] RESEND_API_KEY not set - would send code {code} to {to_email}")
        return True  # Return True in dev mode

    greeting = f"Hej {user_name}!" if user_name else "Hej!"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px;">
        <div style="max-width: 500px; margin: 0 auto; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 16px; padding: 40px; border: 1px solid #2d2d44;">

            <!-- Logo -->
            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="font-size: 28px; margin: 0; background: linear-gradient(135deg, #a855f7, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                    🚀 GinoNova
                </h1>
                <p style="color: #888; margin-top: 5px; font-size: 14px;">DevOps Learning Platform</p>
            </div>

            <!-- Greeting -->
            <p style="font-size: 18px; margin-bottom: 20px;">{greeting}</p>

            <p style="color: #ccc; line-height: 1.6;">
                Välkommen till GinoNova! För att slutföra din registrering, använd denna verifieringskod:
            </p>

            <!-- Code Box -->
            <div style="background: linear-gradient(135deg, #2d1f4e 0%, #1e3a5f 100%); border-radius: 12px; padding: 25px; text-align: center; margin: 30px 0; border: 2px solid #a855f7;">
                <p style="color: #888; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin: 0 0 10px 0;">Din verifieringskod</p>
                <p style="font-size: 36px; font-weight: bold; letter-spacing: 8px; margin: 0; color: #a855f7; font-family: 'Courier New', monospace;">
                    {code}
                </p>
            </div>

            <p style="color: #888; font-size: 14px; line-height: 1.6;">
                ⏱️ Koden är giltig i <strong style="color: #fff;">15 minuter</strong>.
            </p>

            <p style="color: #888; font-size: 14px; line-height: 1.6;">
                Om du inte skapade ett konto på GinoNova, ignorera detta mail.
            </p>

            <!-- Footer -->
            <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #333; text-align: center;">
                <p style="color: #666; font-size: 12px; margin: 0;">
                    © 2026 GinoNova • DevOps Education
                </p>
                <p style="color: #555; font-size: 11px; margin-top: 10px;">
                    Detta mail skickades till {to_email}
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    text_content = f"""
{greeting}

Välkommen till GinoNova!

Din verifieringskod är: {code}

Koden är giltig i 15 minuter.

Om du inte skapade ett konto på GinoNova, ignorera detta mail.

---
GinoNova - DevOps Learning Platform
https://ginonova.com
    """

    try:
        params = {
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": f"🔐 Din verifieringskod: {code}",
            "html": html_content,
            "text": text_content,
        }

        response = resend.Emails.send(params)
        print(f"[Email] ✅ Verification email sent to {to_email}, id: {response.get('id')}")
        return True

    except Exception as e:
        print(f"[Email] ❌ Failed to send verification email to {to_email}: {e}")
        return False


def send_welcome_email(to_email: str, user_name: Optional[str] = None) -> bool:
    """
    Send welcome email after successful verification.
    """
    if not RESEND_API_KEY:
        print(f"[Email] RESEND_API_KEY not set - would send welcome to {to_email}")
        return True

    greeting = f"Hej {user_name}!" if user_name else "Hej!"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #0a0a0a; color: #ffffff; margin: 0; padding: 40px 20px;">
        <div style="max-width: 500px; margin: 0 auto; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 16px; padding: 40px; border: 1px solid #2d2d44;">

            <div style="text-align: center; margin-bottom: 30px;">
                <h1 style="font-size: 28px; margin: 0;">🎉 Välkommen till GinoNova!</h1>
            </div>

            <p style="font-size: 18px; margin-bottom: 20px;">{greeting}</p>

            <p style="color: #ccc; line-height: 1.6;">
                Ditt konto är nu verifierat! Du har nu tillgång till:
            </p>

            <ul style="color: #ccc; line-height: 2;">
                <li>🎓 <strong>Camp DevOps</strong> - Strukturerade utbildningsmoduler</li>
                <li>📝 <strong>Tenta Simulator</strong> - 770+ övningsfrågor</li>
                <li>🤖 <strong>AI Quiz</strong> - Dynamiskt genererade frågor</li>
                <li>💡 <strong>Dallas AI</strong> - Din DevOps-assistent</li>
            </ul>

            <div style="text-align: center; margin: 30px 0;">
                <a href="https://ginonova.com/dashboard" style="display: inline-block; background: linear-gradient(135deg, #a855f7, #6366f1); color: white; text-decoration: none; padding: 14px 30px; border-radius: 8px; font-weight: 600;">
                    Börja lära dig →
                </a>
            </div>

            <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #333; text-align: center;">
                <p style="color: #666; font-size: 12px;">© 2026 GinoNova</p>
            </div>
        </div>
    </body>
    </html>
    """

    try:
        params = {
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": "🎉 Välkommen till GinoNova!",
            "html": html_content,
        }

        response = resend.Emails.send(params)
        print(f"[Email] ✅ Welcome email sent to {to_email}")
        return True

    except Exception as e:
        print(f"[Email] ❌ Failed to send welcome email: {e}")
        return False
