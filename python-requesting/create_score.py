import os
from dotenv import load_dotenv
import requests
from requests import Response
from models import Score

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

player_id = 9
score: Score = Score()
score.game_title = 'Tetris'
score.score = 4637

response: Response = requests.post(
    url=f'{API_BASE_URL}/players/{player_id}/scores',
    headers={'Content-Type': 'application/json'},
    data=score.to_json())
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    score: Score = Score(response.json())
    print(f'Score {{ {score} }} has been created with id {score.id} for player id {player_id}')
else:
    print('Something went wrong')
