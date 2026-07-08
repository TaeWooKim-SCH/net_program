import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

display_count = 5

url = "https://openapi.naver.com/v1/search/news.json"
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

params = {
    "query": "헤드라인",
    "display": display_count,
    "sort": "date" # 최신순으로 정렬
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

print(f"\n최신 헤드라인 뉴스 {display_count}개:\n")
for i, item in enumerate(data['items']):
    print(f"{i+1}. {item['title'].replace('<b>', '').replace('</b>', '')} - {item['link']}")