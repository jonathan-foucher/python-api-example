"""create scores table

Revision ID: a9c6f3765ddc
Revises: 5e7ab4f04a7c
Create Date: 2024-02-14 00:55:49.874358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9c6f3765ddc'
down_revision: Union[str, None] = '5e7ab4f04a7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'scores',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.Column('game_title', sa.String(30), nullable=False, index=True),
        sa.Column('player_id', sa.Integer(), sa.ForeignKey("players.id"), nullable=False),
        sa.UniqueConstraint('game_title', 'player_id', name='uniq_score')
    )


def downgrade() -> None:
    op.drop_table('scores')
