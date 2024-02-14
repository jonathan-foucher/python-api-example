from pydantic import BaseModel


class ScoreBase(BaseModel):
    score: int
    game_title: str


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    player_id: int

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    firstname: str
    lastname: str


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int
    scores: list[Score] = []

    class Config:
        orm_mode = True
