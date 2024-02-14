"""init  tables

Revision ID: 614e36d40a02
Revises: a9c6f3765ddc
Create Date: 2024-02-14 01:02:55.905858

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Table, MetaData


# revision identifiers, used by Alembic.
revision: str = '614e36d40a02'
down_revision: Union[str, None] = 'a9c6f3765ddc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    meta_data = MetaData()
    meta_data.reflect(bind=op.get_bind())

    players = Table('players', meta_data)
    op.bulk_insert(players,
        [
            {'id': 1, 'firstname': 'John', 'lastname': 'Wick'},
            {'id': 2, 'firstname': 'John', 'lastname': 'Price'},
            {'id': 3, 'firstname': 'James', 'lastname': 'Bond'},
            {'id': 4, 'firstname': 'John', 'lastname': 'Marston'},
            {'id': 5, 'firstname': 'John', 'lastname': 'Rambo'},
            {'id': 6, 'firstname': 'Tony', 'lastname': 'Montana'},
            {'id': 7, 'firstname': 'John', 'lastname': 'Smith'},
            {'id': 8, 'firstname': 'John', 'lastname': 'Doe'},
        ]
    )
    op.execute('SELECT setval(\'players_id_seq\', (SELECT max("id") from players))')

    scores = Table('scores', meta_data)
    op.bulk_insert(scores,
    [
        {'id': 1, 'game_title': 'Tetris', 'score': 1602, 'player_id': 1},
        {'id': 2, 'game_title': 'Tetris', 'score': 1590, 'player_id': 2},
        {'id': 3, 'game_title': 'Tetris', 'score': 1200, 'player_id': 3},
        {'id': 4, 'game_title': 'Tetris', 'score': 728, 'player_id': 8},
        {'id': 5, 'game_title': 'Pinball', 'score': 82820, 'player_id': 1},
        {'id': 6, 'game_title': 'Tetris', 'score': 2830, 'player_id': 6},
        {'id': 7, 'game_title': 'Pinball', 'score': 75932, 'player_id': 6},
        {'id': 8, 'game_title': 'Pinball', 'score': 30212, 'player_id': 8},
        {'id': 9, 'game_title': 'Pong', 'score': 8393, 'player_id': 2},
        {'id': 10, 'game_title': 'Pong', 'score': 3021, 'player_id': 8},
        {'id': 11, 'game_title': 'Pong', 'score': 6537, 'player_id': 1},
        {'id': 12, 'game_title': 'Pong', 'score': 4458, 'player_id': 4},
        {'id': 13, 'game_title': 'Pinball', 'score': 46009, 'player_id': 2},
        {'id': 14, 'game_title': 'Tetris', 'score': 453, 'player_id': 5},
        {'id': 15, 'game_title': 'Pinball', 'score': 52882, 'player_id': 5},
        {'id': 16, 'game_title': 'Pinball', 'score': 56831, 'player_id': 3},
        {'id': 17, 'game_title': 'Pong', 'score': 552, 'player_id': 3},
        {'id': 18, 'game_title': 'Pong', 'score': 1084, 'player_id': 5},
    ]
    )
    op.execute('SELECT setval(\'scores_id_seq\', (SELECT max("id") from scores))')


def downgrade() -> None:
    op.execute('DELETE FROM scores WHERE id < 19')
    op.execute('DELETE FROM players WHERE id < 9')
