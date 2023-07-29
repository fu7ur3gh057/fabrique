import os
from pathlib import Path

import environ
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

EXTERNAL_API_URL = env("EXTERNAL_API_URL")
EXTERNAL_API_TOKEN = env("EXTERNAL_API_TOKEN")


def send_message_api(data: dict) -> bool:
    headers = {'Authorization': f'Bearer {EXTERNAL_API_TOKEN}'}
    msg_id = data['id']
    response = requests.post(f'{EXTERNAL_API_URL}/{msg_id}', headers=headers, json=data)
    if response.status_code == 200:
        return True
    else:
        return False
