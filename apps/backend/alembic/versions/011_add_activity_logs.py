"""add activity_logs table

Revision ID: 011
Revises: 010
Create Date: 2026-01-18

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = '011'
down_revision = '010'
branch_labels = None
depends_on = None


def table_exists(table_name):
    """Check if a table exists in the database."""
    bind = op.get_bind()
    inspector = inspect(bind)
    return table_name in inspector.get_table_names()


def upgrade():
    # Create activity_logs table for admin notifications (multi-worker safe)
    if not table_exists('activity_logs'):
        op.create_table(
            'activity_logs',
            sa.Column('id', UUID(as_uuid=True), primary_key=True),
            sa.Column('type', sa.String(50), nullable=False),
            sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
            sa.Column('user_email', sa.String(255), nullable=False),
            sa.Column('user_name', sa.String(255), nullable=True),
            sa.Column('details', sa.Text, nullable=True),
            sa.Column('oauth_provider', sa.String(50), nullable=True),
            sa.Column('created_at', sa.DateTime, default=datetime.utcnow)
        )

        # Create indexes for efficient queries
        op.create_index('ix_activity_logs_type', 'activity_logs', ['type'])
        op.create_index('ix_activity_logs_created_at', 'activity_logs', ['created_at'])
        op.create_index('ix_activity_logs_type_created', 'activity_logs', ['type', 'created_at'])


def downgrade():
    if table_exists('activity_logs'):
        op.drop_index('ix_activity_logs_type_created', table_name='activity_logs')
        op.drop_index('ix_activity_logs_created_at', table_name='activity_logs')
        op.drop_index('ix_activity_logs_type', table_name='activity_logs')
        op.drop_table('activity_logs')
