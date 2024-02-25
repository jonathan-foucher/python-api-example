import os
from dotenv import load_dotenv
import requests
from requests import Response

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL")

score_id: int = 19
response: Response = requests.delete(f'{API_BASE_URL}/scores/{score_id}')
print(f'The API answered with {response.status_code} code')

if response.status_code == 200:
    print(f'Score with the id {score_id} has been deleted')
else:
    print('Something went wrong')
