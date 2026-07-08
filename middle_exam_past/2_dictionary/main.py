# 문제 2 - 딕셔너리 조작 문제
days = {
  'January': 31,
  'February': 28,
  'March': 31,
  'April': 30,
  'May': 31,
  'June': 30,
  'July': 31,
  'August': 31,
  'September': 30,
  'October': 31,
  'November': 30,
  'December': 31
};

def test2(days: dict):
  print(sorted(days.keys())); # 키 값 기준으로 정렬 후 키 배열 반환
  print(sorted(days.items(), key = lambda x: x[1])); # value 기준으로 오름차순으로 (key-value) 쌍 * 첫 번째 매개변수 기준으로 람다 변수로 들어감
  
  month = input();
  print(''.join([str(v) for k, v in days.items() if k.startswith(month)])); # 첫 3자리(Jan, Feb 등)로 월의 일수 찾기