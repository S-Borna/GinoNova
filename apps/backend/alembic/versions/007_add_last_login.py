"""Add last_login_at field to users

Revision ID: 007_add_last_login
Revises: 006_add_ai_usage_logs
Create Date: 2026-01-05
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '007_add_last_login'
down_revision = '006_add_ai_usage_logs'
branch_labels = None
depends_on = None


def upgrade():
    # Add last_login_at column to users table
    op.add_column('users', sa.Column('last_login_at', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('users', 'last_login_at')
