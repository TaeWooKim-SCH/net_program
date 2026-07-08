# 웹 스크래핑 예제: 특정 정보 추출하기

import re
import requests

url = 'https://home.sch.ac.kr/iot'
rsp = requests.get(url)
html = rsp.text
results = re.findall(r'<p><span>관심분야</span><br>([\d\D]+?)</p>', html)

for id, info in enumerate(results):
    print(id+1, info)