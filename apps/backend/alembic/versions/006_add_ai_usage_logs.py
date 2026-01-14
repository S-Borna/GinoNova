"""Add AI usage logs table for tracking OpenAI costs per user

Revision ID: 006_add_ai_usage_logs
Revises: 005_add_user_permissions
Create Date: 2024-12-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision: str = '006_add_ai_usage_logs'
down_revision: Union[str, None] = '005_add_user_permissions'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def table_exists(table_name):
    """Check if table exists in database."""
    bind = op.get_bind()
    inspector = inspect(bind)
    return table_name in inspector.get_table_names()


def upgrade() -> None:
    if table_exists('ai_usage_logs'):
        return
    op.create_table(
        'ai_usage_logs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('feature', sa.String(50), nullable=False),
        sa.Column('model', sa.String(50), nullable=False),
        sa.Column('prompt_tokens', sa.Integer(), default=0),
        sa.Column('completion_tokens', sa.Integer(), default=0),
        sa.Column('total_tokens', sa.Integer(), default=0),
        sa.Column('cost_usd', sa.Float(), default=0.0),
        sa.Column('request_type', sa.String(100), nullable=True),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now()),
        sa.Column('week_number', sa.Integer(), nullable=True),
        sa.Column('year', sa.Integer(), nullable=True),
    )

    # Create indexes
    op.create_index('ix_ai_usage_user_id', 'ai_usage_logs', ['user_id'])
    op.create_index('ix_ai_usage_feature', 'ai_usage_logs', ['feature'])
    op.create_index('ix_ai_usage_created_at', 'ai_usage_logs', ['created_at'])
    op.create_index('ix_ai_usage_week_year', 'ai_usage_logs', ['year', 'week_number'])


def downgrade() -> None:
    op.drop_index('ix_ai_usage_week_year', 'ai_usage_logs')
    op.drop_index('ix_ai_usage_created_at', 'ai_usage_logs')
    op.drop_index('ix_ai_usage_feature', 'ai_usage_logs')
    op.drop_index('ix_ai_usage_user_id', 'ai_usage_logs')
    op.drop_table('ai_usage_logs')
