"""Initial tables - users tracks modules tasks labs projects progress studyflow

Revision ID: 001_initial_tables
Revises:
Create Date: 2025-11-28

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001_initial_tables'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Users table
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('email', sa.String(255), unique=True, nullable=False, index=True),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('full_name', sa.String(255), nullable=True),
        sa.Column('avatar_url', sa.String(500), nullable=True),
        sa.Column('bio', sa.Text(), nullable=True),
        sa.Column('github_username', sa.String(100), nullable=True),
        sa.Column('linkedin_url', sa.String(255), nullable=True),
        sa.Column('website_url', sa.String(255), nullable=True),
        sa.Column('timezone', sa.String(50), server_default='UTC'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('is_admin', sa.Boolean(), server_default='false'),
        sa.Column('is_verified', sa.Boolean(), server_default='false'),
        sa.Column('total_xp', sa.Integer(), server_default='0'),
        sa.Column('current_streak', sa.Integer(), server_default='0'),
        sa.Column('longest_streak', sa.Integer(), server_default='0'),
        sa.Column('last_activity_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Tracks table
    op.create_table(
        'tracks',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('slug', sa.String(100), unique=True, nullable=False, index=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('order_index', sa.Integer(), server_default='1'),
        sa.Column('color', sa.String(7), server_default='#6366f1'),
        sa.Column('icon', sa.String(10), server_default='📚'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Modules table
    op.create_table(
        'modules',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('track_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('tracks.id'), nullable=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('slug', sa.String(200), unique=True, nullable=False, index=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('order_index', sa.Integer(), server_default='1'),
        sa.Column('difficulty', sa.String(20), server_default='intermediate'),
        sa.Column('estimated_hours', sa.Float(), server_default='10.0'),
        sa.Column('prerequisites', postgresql.JSON(), server_default='[]'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_modules_track_order', 'modules', ['track_id', 'order_index'])

    # Tasks table
    op.create_table(
        'tasks',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('module_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('modules.id'), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('order_index', sa.Integer(), server_default='1'),
        sa.Column('difficulty', sa.String(20), server_default='medium'),
        sa.Column('estimated_minutes', sa.Integer(), server_default='15'),
        sa.Column('xp_reward', sa.Integer(), server_default='25'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_tasks_module_order', 'tasks', ['module_id', 'order_index'])

    # Labs table
    op.create_table(
        'labs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('module_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('modules.id'), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('slug', sa.String(200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('instructions', sa.Text(), nullable=True),
        sa.Column('order_index', sa.Integer(), server_default='1'),
        sa.Column('difficulty', sa.String(20), server_default='medium'),
        sa.Column('estimated_hours', sa.Float(), server_default='2.0'),
        sa.Column('xp_reward', sa.Integer(), server_default='100'),
        sa.Column('expected_outcomes', postgresql.JSON(), server_default='[]'),
        sa.Column('hints', postgresql.JSON(), server_default='[]'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_labs_module_order', 'labs', ['module_id', 'order_index'])

    # Projects table
    op.create_table(
        'projects',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('module_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('modules.id'), nullable=False, unique=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('slug', sa.String(200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('requirements', sa.Text(), nullable=True),
        sa.Column('deliverables', postgresql.JSON(), server_default='[]'),
        sa.Column('estimated_hours', sa.Float(), server_default='5.0'),
        sa.Column('xp_reward', sa.Integer(), server_default='500'),
        sa.Column('is_active', sa.Boolean(), server_default='true'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Progress table
    op.create_table(
        'progress',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('module_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('modules.id'), nullable=True),
        sa.Column('task_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('tasks.id'), nullable=True),
        sa.Column('lab_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('labs.id'), nullable=True),
        sa.Column('project_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('projects.id'), nullable=True),
        sa.Column('status', sa.String(20), server_default='not_started'),
        sa.Column('progress_percent', sa.Integer(), server_default='0'),
        sa.Column('xp_earned', sa.Integer(), server_default='0'),
        sa.Column('completed_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_progress_user_module', 'progress', ['user_id', 'module_id'])
    op.create_index('ix_progress_user_task', 'progress', ['user_id', 'task_id'])

    # Studyflow sessions table
    op.create_table(
        'studyflow_sessions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('session_type', sa.String(20), server_default='pomodoro'),
        sa.Column('duration_minutes', sa.Integer(), server_default='25'),
        sa.Column('actual_duration', sa.Integer(), nullable=True),
        sa.Column('tasks_completed', sa.Integer(), server_default='0'),
        sa.Column('xp_earned', sa.Integer(), server_default='0'),
        sa.Column('started_at', sa.DateTime(), server_default=sa.func.now()),
        sa.Column('ended_at', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(20), server_default='active'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_studyflow_user_date', 'studyflow_sessions', ['user_id', 'started_at'])


def downgrade() -> None:
    op.drop_table('studyflow_sessions')
    op.drop_table('progress')
    op.drop_table('projects')
    op.drop_table('labs')
    op.drop_table('tasks')
    op.drop_table('modules')
    op.drop_table('tracks')
    op.drop_table('users')
