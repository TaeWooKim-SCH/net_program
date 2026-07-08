import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

rows = 3
cols = 3
query = "고양이" # 검색어
display_count = rows * cols # 표시할 이미지 개수
url = "https://openapi.naver.com/v1/search/image"

images = []
while (len(images) < 9):
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    
    params = {
        "query": query,
        "display": display_count - len(images),
        "sort": "sim" # 정확도순으로 정렬
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for i, item in enumerate(data['items']):
            image_url = item['link']
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                image_data = BytesIO(image_response.content)
                img = Image.open(image_data)
                images.append(img)
            except requests.exceptions.RequestException as e:
                print(f"이미지 {i+1} 다운로드 실패: {image_url} - {e}")
            except Exception as e:
                print(f"이미지 {i+1} 처리 실패: {image_url} - {e}")
    else:
        print(f"Error Code: {response.status_code}")
        print(response.text)

fig, axes = plt.subplots(rows, cols, figsize=(8, 8))
axes = axes.ravel() # 1차원 배열로 만들기

for i in range(len(images)):
    axes[i].imshow(images[i])
    axes[i].axis('off')
    axes[i].set_title(f"#{i+1}", fontsize=10)

plt.tight_layout()
plt.show()