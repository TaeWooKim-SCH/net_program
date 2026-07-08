import requests
import json

student_1 = {
    'id': '20240001',
    'name': 'Kim',
    'grade': '4.2'
}
student_2 = {
    'id': '20250002',
    'name': 'Lee',
    'grade': '3.5'
}
student_3 = {
    'id': '20260003',
    'name': 'Park',
    'grade': '3.9'
}

url = 'http://localhost:8000/students'
rsp = requests.get(url)

rsp1 = requests.post(url, data=json.dumps(student_1).encode())
rsp2 = requests.post(url, data=json.dumps(student_2).encode())
rsp3 = requests.post(url, data=json.dumps(student_3).encode())

print(rsp.json())