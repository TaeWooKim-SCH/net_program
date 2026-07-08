import socket;
import random;

BUFF_SIZE = 1024;
PORT = 8000;

def run_server():
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
  udp_socket.bind(('', PORT));

  print(f"UDP IoT 서버가 시작되었습니다. (포트: {PORT})")

  while (True):
    # UDP 소켓 생성
    data, address = udp_socket.recvfrom(BUFF_SIZE);
    request = data.decode('utf-8').strip();

    # 초기값 0 설정
    temp, humid, lumi = 0, 0, 0;

    # 요청에 따른 랜덤 값 생성
    if (request == '1'):
      temp = random.randint(1, 50);
    elif (request == '2'):
      humid = random.randint(1, 100);
    elif (request == '3'):
      lumi = random.randint(1, 150);
    else:
      print(f"[{address}] 잘못된 요청 수신: {request}");
      continue;

    # 2바이트 정수 형태 & 빅 엔디언(네트워크 바이트 오더)으로 변환
    # signed=True는 정수형 변환의 표준을 맞추기 위함
    bytes_temp = temp.to_bytes(2, byteorder='big', signed=True); # 양수의 범위만 다루면 False로 설정해야 좋음
    bytes_humid = humid.to_bytes(2, byteorder='big', signed=True);
    bytes_lumi = lumi.to_bytes(2, byteorder='big', signed=True);

    # 총 6바이트의 페이로드 생성 (온도2 + 습도2 + 조도2)
    payload = bytes_temp + bytes_humid + bytes_lumi;

    # 클라이언트에게 응답 전송
    udp_socket.sendto(payload, address);

if (__name__ == "__main__"):
  run_server();
