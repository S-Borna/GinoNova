"""add analytics tables

Revision ID: 010
Revises: 009_add_ip_tracking
Create Date: 2026-01-13

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSON
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '010'
down_revision = '009_add_ip_tracking'
branch_labels = None
depends_on = None


def upgrade():
    # Create analytics_events table
    op.create_table(
        'analytics_events',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('event_type', sa.String(100), nullable=False),
        sa.Column('event_data', JSON, default=dict),
        sa.Column('session_id', sa.String(100), nullable=True),
        sa.Column('ip_address', sa.String(45), nullable=True),
        sa.Column('user_agent', sa.String(500), nullable=True),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow)
    )

    # Create indexes for analytics_events
    op.create_index('ix_analytics_user_id', 'analytics_events', ['user_id'])
    op.create_index('ix_analytics_event_type', 'analytics_events', ['event_type'])
    op.create_index('ix_analytics_created_at', 'analytics_events', ['created_at'])
    op.create_index('ix_analytics_user_type_date', 'analytics_events', ['user_id', 'event_type', 'created_at'])

    # Create daily_stats table
    op.create_table(
        'daily_stats',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('study_minutes', sa.Integer, default=0),
        sa.Column('tasks_completed', sa.Integer, default=0),
        sa.Column('tasks_attempted', sa.Integer, default=0),
        sa.Column('xp_earned', sa.Integer, default=0),
        sa.Column('sessions_count', sa.Integer, default=0),
        sa.Column('ai_calls', sa.Integer, default=0),
        sa.Column('hints_used', sa.Integer, default=0),
        sa.Column('modules_touched', JSON, default=list),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    )

    # Create unique index for daily_stats
    op.create_index('ix_daily_stats_user_date', 'daily_stats', ['user_id', 'date'], unique=True)

    # Create user_insights table
    op.create_table(
        'user_insights',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False, unique=True),
        # Study patterns
        sa.Column('total_study_hours', sa.Float, default=0),
        sa.Column('avg_session_length', sa.Integer, default=0),
        sa.Column('favorite_study_time', sa.String(20), nullable=True),
        sa.Column('most_active_day', sa.String(10), nullable=True),
        # Performance
        sa.Column('strongest_skill', sa.String(100), nullable=True),
        sa.Column('weakest_skill', sa.String(100), nullable=True),
        sa.Column('avg_task_completion_time', sa.Integer, nullable=True),
        sa.Column('accuracy_rate', sa.Float, nullable=True),
        # Engagement
        sa.Column('longest_streak', sa.Integer, default=0),
        sa.Column('current_streak', sa.Integer, default=0),
        sa.Column('streak_start_date', sa.Date, nullable=True),
        sa.Column('last_active_date', sa.Date, nullable=True),
        # Predictions
        sa.Column('estimated_completion_date', sa.Date, nullable=True),
        sa.Column('recommended_pace', sa.String(50), nullable=True),
        # Metadata
        sa.Column('calculated_at', sa.DateTime, default=datetime.utcnow),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    )

    # Create module_analytics table
    op.create_table(
        'module_analytics',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('module_id', UUID(as_uuid=True), nullable=False, unique=True),
        sa.Column('module_slug', sa.String(100), nullable=False),
        # Engagement
        sa.Column('total_enrollments', sa.Integer, default=0),
        sa.Column('active_users', sa.Integer, default=0),
        sa.Column('completions', sa.Integer, default=0),
        sa.Column('completion_rate', sa.Float, default=0),
        # Performance
        sa.Column('avg_completion_time', sa.Float, nullable=True),
        sa.Column('avg_score', sa.Float, nullable=True),
        sa.Column('difficulty_rating', sa.Float, nullable=True),
        # Feedback
        sa.Column('avg_rating', sa.Float, nullable=True),
        sa.Column('rating_count', sa.Integer, default=0),
        # Metadata
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    )


def downgrade():
    op.drop_table('module_analytics')
    op.drop_table('user_insights')
    op.drop_index('ix_daily_stats_user_date', 'daily_stats')
    op.drop_table('daily_stats')
    op.drop_index('ix_analytics_user_type_date', 'analytics_events')
    op.drop_index('ix_analytics_created_at', 'analytics_events')
    op.drop_index('ix_analytics_event_type', 'analytics_events')
    op.drop_index('ix_analytics_user_id', 'analytics_events')
    op.drop_table('analytics_events')
