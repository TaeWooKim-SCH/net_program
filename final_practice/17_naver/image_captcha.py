import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_captcha_key(): # 캡차 키를 발급받는 함수
    url = "https://openapi.naver.com/v1/captcha/nkey?code=0"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("key")
    else:
        print(f"캡차 키 발급 실패: {response.status_code}")
        return None

def get_captcha_image(captcha_key): # 캡차 이미지를 가져와 화면에 표시하는 함수
    url = f"https://openapi.naver.com/v1/captcha/ncaptcha.bin?key={captcha_key}"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            image = Image.open(BytesIO(response.content))
            image.show()
            return True
        except Exception as e:
            print(f"이미지 표시 오류: {e}")
            return False
    else:
        print(f"캡차. 이미지 요청 실패: {response.status_code}")
        return False

def verify_captcha(captcha_key, user_input): # 사용자 입력값을 검증하는 함수
    url = f"https://openapi.naver.com/v1/captcha/nkey?code=1&key={captcha_key}&value={user_input}"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        verification_result = response.json()
        return verification_result.get("result")
    else:
        print(f"캡차 검증 요청 실패: {response.status_code}")
        return False

if __name__ == "__main__":
    captcha_key = get_captcha_key()
    
    if captcha_key:
        if get_captcha_image(captcha_key):
            user_input = input("캡차 이미지의 텍스트를 입력하세요: ")
            verification_result = verify_captcha(captcha_key, user_input)
            if verification_result:
                print("캡차 검증 성공!")
            else:
                print("캡차 검증 실패!")