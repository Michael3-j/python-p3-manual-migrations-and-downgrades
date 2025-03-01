"""Renaming students to scholars

Revision ID: 5214c5c7c515
Revises: 
Create Date: 2025-03-01 17:03:05.766555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5214c5c7c515'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
