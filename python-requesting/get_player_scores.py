import os
from dotenv import load_dotenv
import requests
from requests import Response
from models import Player

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

player_id: int = 3
response: Response = requests.get(f'{API_BASE_URL}/players/{player_id}')
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    player: Player = Player(response.json())
    print(f'{player.get_full_name()} scores are {player.scores}')
else:
    print('Something went wrong')
