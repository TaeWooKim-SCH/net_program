import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

while (True):
    text = input('단어를 입력하세요: ')

    url = 'https://openapi.naver.com/v1/search/errata.json'
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    payload = {
        'query': text
    }

    rsp = requests.get(url, headers=headers, params=payload)
    print(f"API 결과: {rsp.json().get('errata')}")
