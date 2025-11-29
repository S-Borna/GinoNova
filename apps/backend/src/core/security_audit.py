"""
Security Audit Utilities - Phase 29
Input validation, sanitization, and security helpers.
"""
import re
from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)


def sanitize_input(value: str, max_length: int = 1000) -> str:
    """
    Sanitize user input by removing HTML tags and limiting length.
    
    Args:
        value: Input string to sanitize
        max_length: Maximum allowed length
        
    Returns:
        Sanitized string
    """
    if not value:
        return ""
    
    # Truncate to max length
    value = value[:max_length]
    
    # Remove HTML/script tags
    value = re.sub(r'<[^>]*>', '', value)
    
    # Remove potential SQL injection patterns
    value = re.sub(r'[;\'"\\]', '', value)
    
    return value.strip()


def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid email format
    """
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def check_password_strength(password: str) -> Tuple[bool, str]:
    """
    Check password strength and return validation result.
    
    Args:
        password: Password to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    if len(password) > 128:
        return False, "Password must be less than 128 characters"
    
    # Optional: Stricter requirements for production
    # if not re.search(r'[A-Z]', password):
    #     return False, "Password must contain an uppercase letter"
    # if not re.search(r'[a-z]', password):
    #     return False, "Password must contain a lowercase letter"
    # if not re.search(r'\d', password):
    #     return False, "Password must contain a number"
    # if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #     return False, "Password must contain a special character"
    
    return True, "Password is valid"


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe storage.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    if not filename:
        return "unnamed"
    
    # Remove path separators and dangerous characters
    filename = re.sub(r'[/\\:*?"<>|]', '', filename)
    
    # Remove leading/trailing dots and spaces
    filename = filename.strip('. ')
    
    # Limit length
    if len(filename) > 255:
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        filename = name[:250] + ('.' + ext if ext else '')
    
    return filename or "unnamed"


def is_safe_url(url: str, allowed_hosts: list[str] = None) -> bool:
    """
    Check if URL is safe for redirects.
    
    Args:
        url: URL to validate
        allowed_hosts: List of allowed hostnames
        
    Returns:
        True if URL is safe
    """
    if not url:
        return False
    
    # Allow relative URLs
    if url.startswith('/') and not url.startswith('//'):
        return True
    
    # Check against allowed hosts
    if allowed_hosts:
        from urllib.parse import urlparse
        try:
            parsed = urlparse(url)
            return parsed.netloc in allowed_hosts
        except Exception:
            return False
    
    return False


def log_security_event(
    event_type: str,
    user_id: Optional[str] = None,
    ip_address: Optional[str] = None,
    details: Optional[dict] = None
):
    """
    Log security-relevant events for audit trail.
    
    Args:
        event_type: Type of security event
        user_id: User ID if applicable
        ip_address: Client IP address
        details: Additional details
    """
    log_data = {
        "event": event_type,
        "user_id": user_id,
        "ip": ip_address,
        **(details or {})
    }
    
    logger.warning(f"SECURITY_EVENT: {log_data}")
