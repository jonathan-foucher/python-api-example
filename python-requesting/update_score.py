import os
from dotenv import load_dotenv
import requests
from requests import Response
from models import Score

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

score_id = 19
score: Score = Score()
score_value = 4832

response: Response = requests.patch(
    url=f'{API_BASE_URL}/scores/{score_id}?score_value=4832',
    params={'score_value': score_value})
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    score: Score = Score(response.json())
    print(f'Score id {score.id} has been updated with score value {score.score}')
else:
    print('Something went wrong')
