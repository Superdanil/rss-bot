"""Added users table

Revision ID: 2d9f27149827
Revises: 
Create Date: 2024-09-30 22:33:55.953407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '2d9f27149827'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('telegram_id', sa.Integer(), nullable=False),
                    sa.Column('user_firstname', sa.String(), nullable=False),
                    sa.Column('user_lastname', sa.String(), nullable=False),
                    sa.Column('user_username', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('telegram_id')
                    )


def downgrade() -> None:
    op.drop_table('users')
