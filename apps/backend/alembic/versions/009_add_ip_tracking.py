"""Add IP tracking fields to users

Revision ID: 009_add_ip_tracking
Revises: 008_add_exam_results
Create Date: 2026-01-06

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '009_add_ip_tracking'
down_revision = '008_add_exam_results'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add IP tracking columns
    op.add_column('users', sa.Column('registration_ip', sa.String(45), nullable=True))
    op.add_column('users', sa.Column('last_login_ip', sa.String(45), nullable=True))
    
    # Index on registration_ip for duplicate detection
    op.create_index('ix_users_registration_ip', 'users', ['registration_ip'])


def downgrade() -> None:
    op.drop_index('ix_users_registration_ip', table_name='users')
    op.drop_column('users', 'last_login_ip')
    op.drop_column('users', 'registration_ip')
