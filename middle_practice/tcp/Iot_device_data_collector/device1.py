# 온도, 습도, 조도 측정 제공

import socket;
import random;

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp_socket.bind(('', 8001));
tcp_socket.listen(5);

BUFF_SIZE = 1024;
print("서버 구동 시작... (종료하려면 터미널에서 Ctrl + C 를 누르세요)");

while (True):
  client, address = tcp_socket.accept();

  while True:
    recv_data = client.recv(BUFF_SIZE).decode('utf-8');

    if (recv_data == 'Request'):
      temperature = random.randint(0, 40); # 온도
      humidity = random.randint(0, 100); # 습도
      illuminance = random.randint(70, 150); # 조도
      client.send(f"{temperature} {humidity} {illuminance}".encode('utf-8'));
    elif (recv_data == 'quit'):
      client.close();
      break;
  tcp_socket.close();
  break;
