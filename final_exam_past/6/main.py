import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://dapi.kakao.com/v2/vision/adult/detect'
headers = {'Authorization': f'KakaoAK {os.getenv("KAKAO_API_KEY")}'}

with open('iot.png', 'rb') as f:
    files = {'image': f}
    response = requests.post(url, headers=headers, files=files)

result = response.json()['result']
print(f"normal: {result['normal']}")
print(f"soft: {result['soft']}")
print(f"adult: {result['adult']}")