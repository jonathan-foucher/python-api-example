from sqlalchemy.orm import Session

import models, schemas


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_players_by_firstname(db: Session, firstname: str):
    return db.query(models.Player).filter(models.Player.firstname == firstname)


def get_players(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Player).offset(skip).limit(limit).all()


def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(firstname=player.firstname, lastname=player.lastname)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_scores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Score).offset(skip).limit(limit).all()


def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()


def get_score_by_player_id_and_game_title(db: Session, player_id: int, game_title: str):
    return db.query(models.Score).filter(models.Score.player_id == player_id and models.Score.game_title == game_title).first()


def create_player_score(db: Session, score: schemas.ScoreCreate, player_id: int):
    db_score = models.Score(**score.model_dump(), player_id=player_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def update_score(db: Session, db_score: schemas.ScoreCreate, score_value: int):
    db_score.score = score_value
    db.commit()
    db.refresh(db_score)
    return db_score


def delete_score(db: Session, db_score: schemas.ScoreCreate):
    db.delete(db_score)


def get_game_titles(db: Session):
    return [r.game_title for r in db.query(models.Score.game_title).distinct().all()]
