"""create players table

Revision ID: 5e7ab4f04a7c
Revises: 
Create Date: 2024-02-14 00:42:07.601604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e7ab4f04a7c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'players',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String(30), nullable=False, index=True),
        sa.Column('lastname', sa.String(30), nullable=False, index=True),
    )


def downgrade() -> None:
    op.drop_table('players')
