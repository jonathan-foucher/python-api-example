import os
from dotenv import load_dotenv
import requests
from requests import Response
from models import Player

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

player: Player = Player()
player.firstname = 'John'
player.lastname = 'Hammond'

response: Response = requests.post(
    url=f'{API_BASE_URL}/players',
    headers={'Content-Type': 'application/json'},
    data=player.to_json())
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    player: Player = Player(response.json())
    print(f'{player.get_full_name()} has been created with id {player.id}')
else:
    print('Something went wrong')
