import os
from dotenv import load_dotenv
import requests
from requests import Response
from models import Player

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")


response: Response = requests.get(f'{API_BASE_URL}/players?limit=9999')
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    players: list[Player] = [Player(player) for player in response.json()]
    players_names: list = [player.get_full_name() for player in players]
    print(f'The players names are : {players_names}')
else:
    print('Something went wrong')
