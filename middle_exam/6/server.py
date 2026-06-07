import socket;
import random;

port = 3333;
BUFF_SIZE = 1024;

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udp_socket.bind(('', port));

while (True):
  # 클라이언트로부터 메세지 수신 부분
  # 메세지 수신 후 30% 확률로 응답하지 않고 70% 확률로 'ack' 응답 메세지를 클라이언트로 전송
  udp_socket.settimeout(None) # 소켓의 블로킹 모드 설정. None인 경우, 무한정 블로킹됨
  while (True):
    data, address = udp_socket.recvfrom(BUFF_SIZE);
    if (random.random() <= 0.3):
      continue;
    else:
      udp_socket.sendto(b'ack', address);
      print('<-', data.decode());
      break;

  # 클라이언트로 메세지 전송 부분
  # 'ack' 응답 메세지를 수신하지 못하는 경우, 1초 간격으로 최대 3회 재전송 (총 4회)
  msg = input('-> ');
  reTx = 0;
  while (reTx <= 5):
    response = str(reTx) + ' ' + msg;
    udp_socket.sendto(response.encode('utf-8'), address);
    udp_socket.settimeout(1) # 1초 간격 재전송을 위한 소켓의 timeout 설정

    try:
      data, address = udp_socket.recvfrom(BUFF_SIZE);
    except socket.timeout:
      reTx += 1;
      continue;
    else:
      break;