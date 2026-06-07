import socket;
import random;
import time;

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udp_socket.bind(('', 7777));

BUFF_SIZE = 1024;
print("Ping 서버가 시작되었습니다.")

while (True):
  recv_data, address = udp_socket.recvfrom(BUFF_SIZE);

  # 클라이언트가 연결을 끊고 나갔을 때의 방어 코드
  if not recv_data:
      print("클라이언트 연결 종료");
      break;
  
  decoded_data = recv_data.decode('utf-8');
  if (decoded_data == 'ping'):
    # 0.02초 ~ 0.03초 정도의 인위적인 네트워크 지연 발생 (테스트용)
    time.sleep(0.02)
    if (random.random() < 0.3):
      udp_socket.sendto('pong'.encode('utf-8'), address);
  else:
    print("ping 메세지가 아닙니다.");

