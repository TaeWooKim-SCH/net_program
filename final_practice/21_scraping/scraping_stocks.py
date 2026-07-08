import requests
import re

url = 'https://finance.naver.com/item/main.nhn?code=005930'
rsp = requests.get(url)
html = rsp.text
stock_results = re.findall(r'<dl class="blind">([\s\S]+?)<\/dl>', html) # <dl class>~</dl> 정보를 추출
samsung_stock = stock_results[0] # HTML 내에 2개의 <dl class>~</dl> 부분이 존재. 첫 번째 것을 선택

# 주식 정보(<dd>~</dd>)를 추출
info_list = re.findall(r'<dd>([\s\S]+?)<\/dd>', samsung_stock)

for info in info_list:
    print(info)