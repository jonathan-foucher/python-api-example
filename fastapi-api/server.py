from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/my-app/hello-world-path")
def hello_world():
    return 'Hello World!'


@app.get("/players", response_model=list[schemas.Player])
def get_players(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_players(db=db, skip=skip, limit=limit)


@app.get("/players/{player_id}", response_model=schemas.Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db=db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player


@app.get("/players", response_model=list[schemas.Player])
def get_players_by_firstname(firstname: str, db: Session = Depends(get_db)):
    return crud.get_players_by_firstname(db=db, firstname=firstname)


@app.post("/players", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)


@app.get("/scores", response_model=list[schemas.Score])
def get_scores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_scores(db=db, skip=skip, limit=limit)


@app.post("/players/{player_id}/scores", response_model=schemas.Score)
def create_score_for_player(player_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    db_score = crud.get_score_by_player_id_and_game_title(db=db, player_id=player_id, game_title=score.game_title)
    if db_score:
        raise HTTPException(status_code=400, detail="Score already registered")
    return crud.create_player_score(db=db, score=score, player_id=player_id)


@app.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score_value: int, db: Session = Depends(get_db)):
    db_score = crud.get_score(db=db, score_id=score_id)
    if not db_score:
        raise HTTPException(status_code=404, detail="Score not found")
    return crud.update_score(db=db, db_score=db_score, score_value=score_value)


@app.delete("/scores/{score_id}", response_model=None)
def update_score(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.get_score(db=db, score_id=score_id)
    if not db_score:
        raise HTTPException(status_code=404, detail="Score not found")
    crud.delete_score(db=db, db_score=db_score)
    return Response(status_code=status.HTTP_200_OK)


@app.get("/scores/game_titles", response_model=list[str])
def update_score(db: Session = Depends(get_db)):
    return crud.get_game_titles(db=db)
