### Build docker image for the postgres database
```
docker build -t fastapi-db docker/.
```

### Run docker image
```
docker run --name fastapi-db -p 5432:5432 -d fastapi-db
```

### Run the migrations (create tables and init data)
```
alembic upgrade head
```

### Start the application on port 8081
```
python -m uvicorn server:app --reload --port 8081 
```

## Testing with curl
## \> Hello world endpoint
```
curl http://localhost:8081/my-app/hello-world-path
```

## \> Players endpoints
### GET endpoint to get all players
```
curl http://localhost:8081/players?limit=9999
```

### GET endpoint to get the first page of 5 players
```
curl http://localhost:8081/players?limit=5&skip=0
```

### GET endpoint to get the second page of 5 players
```
curl http://localhost:8081/players?limit=5&skip=5
```

### GET endpoint to get a specific player with id=3
```
curl http://localhost:8081/players/3
```

### GET endpoint to get players filtered by firstname with firstname="John"
```
curl http://localhost:8081/players?firstname=John
```

### POST endpoint to create a new player
```
curl --location 'http://localhost:8081/players' \
--header 'Content-Type: application/json' \
--data '{
    "firstname": "John",
    "lastname": "Hammond"
}'
```

## \> Scores endpoints
### GET endpoint to get all scores
```
curl --location 'http://localhost:8081/scores?limit=9999'
```

### GET endpoint to get the first page of 10 scores
```
curl --location 'http://localhost:8081/scores?limit=10'
```

### GET endpoint to get the second page of 10 scores
```
curl --location 'http://localhost:8081/scores?limit=10&skip=10'
```

### POST endpoint to save the score of a game for a player (player_id=9)
```
curl --location 'http://localhost:8081/players/9/scores' \
--header 'Content-Type: application/json' \
--data '{
    "game_title": "Tetris",
    "score": 4637
}'
```

### PATCH endpoint to update a score (id=19)
```
curl --location --request PATCH 'http://localhost:8081/scores/19?score_value=4832'
```

### DELETE endpoint to delete a score (id=19)
```
curl --location --request DELETE 'http://localhost:8081/scores/19'
```

## \> Game titles endpoint
```
curl --location 'http://localhost:8081/scores/game_titles'
```