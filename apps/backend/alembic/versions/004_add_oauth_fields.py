"""Add OAuth fields to users table

Revision ID: 004_add_oauth_fields
Revises: 003_add_bookmarks
Create Date: 2025-12-03

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004_add_oauth_fields'
down_revision = '003_add_bookmarks'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add OAuth provider fields to users table
    op.add_column('users', sa.Column('oauth_provider', sa.String(50), nullable=True))
    op.add_column('users', sa.Column('oauth_provider_id', sa.String(255), nullable=True))

    # Make hashed_password nullable for OAuth users
    op.alter_column('users', 'hashed_password',
                    existing_type=sa.String(255),
                    nullable=True)


def downgrade() -> None:
    # Remove OAuth fields
    op.drop_column('users', 'oauth_provider_id')
    op.drop_column('users', 'oauth_provider')

    # Make hashed_password required again
    op.alter_column('users', 'hashed_password',
                    existing_type=sa.String(255),
                    nullable=False)
