# 문제 1 - 문자열 인덱싱/슬라이싱 문제
string = 'Hello, IoT';

def test1(text):
  print(text * 3); # 문자열 3번 반복
  print(text[:4]); # 문자열 처음 4문자
  print(text[len(text) - 5:]); # 문자열 마지막 5문자
  print(text.lower()); # 문자열 모두 소문자
  print(text[::-1]); # 문자열 거꾸로 출력