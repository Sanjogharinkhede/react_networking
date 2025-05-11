"""create dob for user

Revision ID: c86b9ebd9ce8
Revises: 
Create Date: 2025-05-12 00:28:37.726756

"""
import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c86b9ebd9ce8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users',
                  sa.Column('dob',
                            sa.Date,
                            nullable=True,
                            server_default=sa.text("'1970-01-01'")
))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users','dob')
