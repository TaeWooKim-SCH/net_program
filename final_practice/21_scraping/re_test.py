import re

text = '''
긴급한 사항이 있으면 010-1234-5678 또는
010-987-6543으로 연락주세요.
연락이 안되는 경우,
daeheekim@sch.ac.kr로 연락주세요.
zop1234@hanmail.net
'''

result = re.findall(r'\d{3}-\d{3,4}-\d{4}', text) # 전화번호
print(result)

# 이메일 모두 배열 형태로
# ex) ['daeheekim@sch.ac.kr', 'zop1234@hanmail.net']
result = re.findall(r'[\w.]+@.+\.[a-z]{2,3}', text)
print(result)
print(result[0])

# 이메일을 잘라서 튜플 형태가 한 요소로 배열에 담김
# ex) [('daeheekim', '@', 'sch.ac', '.kr'), ('zop1234', '@', 'hanmail', '.net')]
result = re.findall(r'([\w.]+)(@)(.+)(\.[a-z]{2,3})', text) #
print(result)
print(''.join(result[0]))