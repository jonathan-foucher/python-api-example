import os
from dotenv import load_dotenv
import requests
from requests import Response

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")


response: Response = requests.get(f'{API_BASE_URL}/scores/game_titles')
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    game_titles: list[str] = response.json()
    print(f'The games titles are : {game_titles}')
else:
    print('Something went wrong')
