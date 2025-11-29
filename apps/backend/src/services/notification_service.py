"""
Notification Service - Phase 12
Functions for creating and sending notifications.
"""
from typing import Optional, List
import logging
import os

logger = logging.getLogger(__name__)

# Email provider config
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", "noreply@devopshub.se")


# Notification types
NOTIFICATION_TYPES = {
    "streak_reminder": {
        "title_template": "Håll din streak igång! 🔥",
        "message_template": "Du har inte studerat idag. Gör en snabb session för att behålla din {streak}-dagars streak.",
    },
    "streak_broken": {
        "title_template": "Din streak avbröts 😢",
        "message_template": "Din {streak}-dagars streak tog slut. Börja om och bygg en ny!",
    },
    "achievement": {
        "title_template": "Ny prestation! 🏆",
        "message_template": "Grattis! Du har låst upp: {achievement}",
    },
    "badge_earned": {
        "title_template": "Nytt badge! 🎖️",
        "message_template": "Du har tjänat: {badge_name} (Nivå {level})",
    },
    "module_complete": {
        "title_template": "Modul klar! 🎉",
        "message_template": "Du har slutfört {module_name}! Fortsätt till nästa utmaning.",
    },
    "certificate_ready": {
        "title_template": "Ditt certifikat är klart! 📜",
        "message_template": "Grattis till din prestation! Ditt certifikat för {reference_name} är nu tillgängligt.",
    },
    "weekly_summary": {
        "title_template": "Din veckosummering 📊",
        "message_template": "Denna vecka: {study_hours}h studietid, {tasks_completed} uppgifter, {xp_earned} XP",
    },
    "new_content": {
        "title_template": "Nytt innehåll tillgängligt! 🆕",
        "message_template": "{content_title} har lagts till i {module_name}.",
    },
    "inactivity": {
        "title_template": "Vi saknar dig! 👋",
        "message_template": "Det har gått {days} dagar sedan du loggade in. Kom tillbaka och fortsätt lära dig!",
    },
}


async def create_notification(
    user_id: str,
    notification_type: str,
    data: dict = {},
    action_url: Optional[str] = None
) -> dict:
    """
    Create an in-app notification.

    Args:
        user_id: User to notify
        notification_type: Type from NOTIFICATION_TYPES
        data: Template variables
        action_url: Deep link URL

    Returns:
        Created notification dict
    """
    template = NOTIFICATION_TYPES.get(notification_type, {})

    title = template.get("title_template", notification_type)
    message = template.get("message_template", "")

    # Fill in template variables
    try:
        title = title.format(**data)
        message = message.format(**data)
    except KeyError as e:
        logger.warning(f"Missing template variable: {e}")

    # TODO: Save to database
    # notification = Notification(
    #     user_id=user_id,
    #     type=notification_type,
    #     title=title,
    #     message=message,
    #     data=data,
    #     action_url=action_url,
    # )
    # db.add(notification)
    # db.commit()

    logger.info(f"Notification created for {user_id}: {notification_type}")

    return {
        "user_id": user_id,
        "type": notification_type,
        "title": title,
        "message": message,
        "action_url": action_url,
    }


async def send_streak_reminder(user_id: str, current_streak: int) -> bool:
    """Send streak reminder notification."""
    await create_notification(
        user_id=user_id,
        notification_type="streak_reminder",
        data={"streak": current_streak},
        action_url="/dashboard"
    )
    return True


async def send_achievement_notification(user_id: str, achievement: str) -> bool:
    """Send achievement notification."""
    await create_notification(
        user_id=user_id,
        notification_type="achievement",
        data={"achievement": achievement},
        action_url="/profile/achievements"
    )
    return True


async def send_badge_notification(
    user_id: str,
    badge_name: str,
    level: int
) -> bool:
    """Send badge earned notification."""
    await create_notification(
        user_id=user_id,
        notification_type="badge_earned",
        data={"badge_name": badge_name, "level": level},
        action_url="/profile/badges"
    )
    return True


async def send_module_complete_notification(
    user_id: str,
    module_name: str,
    module_slug: str
) -> bool:
    """Send module completion notification."""
    await create_notification(
        user_id=user_id,
        notification_type="module_complete",
        data={"module_name": module_name},
        action_url=f"/modules/{module_slug}"
    )
    return True


async def send_email(
    to_email: str,
    subject: str,
    html_content: str,
    user_id: Optional[str] = None
) -> bool:
    """
    Send email via SendGrid.

    Args:
        to_email: Recipient email
        subject: Email subject
        html_content: HTML body
        user_id: User ID for logging

    Returns:
        True if sent successfully
    """
    if not SENDGRID_API_KEY:
        logger.warning("SendGrid not configured, email not sent")
        return False

    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        logger.info(f"Email sent to {to_email}: {response.status_code}")

        # TODO: Log to email_logs table

        return response.status_code in [200, 201, 202]

    except ImportError:
        logger.error("SendGrid module not installed")
        return False
    except Exception as e:
        logger.error(f"Email send failed: {e}")
        return False


async def send_weekly_summary_email(
    user_id: str,
    email: str,
    stats: dict
) -> bool:
    """Send weekly summary email."""
    subject = "Din veckosummering från DevOpsHub 📊"

    html_content = f"""
    <h1>Hej!</h1>
    <p>Här är din veckosummering:</p>
    <ul>
        <li><strong>Studietid:</strong> {stats.get('study_hours', 0)} timmar</li>
        <li><strong>Uppgifter:</strong> {stats.get('tasks_completed', 0)} slutförda</li>
        <li><strong>XP:</strong> {stats.get('xp_earned', 0)} intjänade</li>
        <li><strong>Streak:</strong> {stats.get('current_streak', 0)} dagar</li>
    </ul>
    <p>Fortsätt så! 💪</p>
    <p><a href="https://saids-devopshub.netlify.app/dashboard">Gå till Dashboard</a></p>
    """

    return await send_email(email, subject, html_content, user_id)
