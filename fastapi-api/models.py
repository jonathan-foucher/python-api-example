from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from database import Base


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)

    scores = relationship("Score", back_populates="player")


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    game_title = Column(String, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))

    UniqueConstraint('game_title', 'player_id', name='uniq_score')
    player = relationship("Player", back_populates="scores")
