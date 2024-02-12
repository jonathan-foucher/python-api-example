### Build docker image for the postgres database
```
docker build -t django-db docker/.
```

### Run docker image
```
docker run --name django-db -p 5432:5432 -d django-db
```

### Run the migration scripts
```
python3 manage.py migrate
```

### Load data
```
python3 manage.py loaddata players_init
```

### Start the application on port 8082
```
python3 manage.py runserver localhost:8082
```

### Try the GET endpoint to get all players
```
curl http://localhost:8082/players/
```
