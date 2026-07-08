import requests
import re

URL = "https://www.python.org/"

rsp = requests.get(URL)

result = re.findall(r'Py\w*[r]+', rsp.text)
print(result)