"""
AI Chat History Models - Phase 16
Store chat conversations with AI assistant.
"""
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from .database import Base


class ChatSession(Base):
    """
    A chat session groups related messages together.
    """
    __tablename__ = "chat_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=True)  # Auto-generated from first message
    context_type = Column(String(50), nullable=True)  # "module", "task", "general"
    context_id = Column(String(100), nullable=True)  # module_id, task_id if relevant
    messages_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ChatMessage(Base):
    """
    Individual message in a chat session.
    """
    __tablename__ = "chat_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    role = Column(String(20), nullable=False)  # "user", "assistant", "system"
    content = Column(Text, nullable=False)
    context = Column(JSON, nullable=True)  # Additional context (task info, etc.)
    tokens_used = Column(Integer, nullable=True)  # For quota tracking
    created_at = Column(DateTime, default=datetime.utcnow)


class AIUsageLog(Base):
    """
    Track AI usage for quota management.
    """
    __tablename__ = "ai_usage_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    usage_type = Column(String(50), nullable=False)  # "chat", "hint", "explain"
    tokens_input = Column(Integer, default=0)
    tokens_output = Column(Integer, default=0)
    model = Column(String(50), default="gpt-4o-mini")
    created_at = Column(DateTime, default=datetime.utcnow)
