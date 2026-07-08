from urllib import parse
import requests

URL = "https://search.naver.com/search.naver?query=soonchunhyang"

parsed_url = parse.urlparse(URL)
print(parsed_url)

new_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
print(f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}")

payload = {'query': 'IoT'}
rsp = requests.get(new_url, params=payload)
print(rsp.url)
