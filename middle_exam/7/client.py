import socket;
import time;

PORT = 7777;
BUFF_SIZE = 1024;
SERVER = ('localhost', PORT);

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);


# 문제 요구사항: ping 메시지 보낸 후 시간 기록
start_time = None;
end_time = None;

# 'ack' 응답 메시지를 수신하지 못하는 경우, 1초 간격으로 최대 3회 재전송 (총 4회)
reTx = 0 # 재전송 횟수 초기화
while reTx <= 2:
  udp_socket.sendto('ping'.encode('utf-8'), SERVER);
  udp_socket.settimeout(2);

  if (reTx == 0):
    start_time = time.time();

  try:
    # 서버로부터 메세지 대기
    data, addr = udp_socket.recvfrom(BUFF_SIZE)
    if (data):
      end_time = time.time();
      print(f"Success (RTT: {end_time - start_time:.5f})");
      break;
  except socket.timeout:
    if (reTx == 2):
      print('Fail');
      break;
    # 타임아웃(2초) 발생 시 재전송 횟수 1 증가시키고 다시 시도
    reTx += 1
    continue
  else:
    # 정상적으로 'ack'를 받으면 송신 루프 종료
    break

