# 심박수, 걸음수, 소모 칼로리 측정 제공

import socket;
import random;

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp_socket.bind(('', 8002));
tcp_socket.listen(5);

BUFF_SIZE = 1024;
print("서버 구동 시작... (종료하려면 터미널에서 Ctrl + C 를 누르세요)");

while (True):
  client, address = tcp_socket.accept();

  while (True):
    recv_data = client.recv(BUFF_SIZE).decode('utf-8');

    if (recv_data == 'Request'):
      heart_rate = random.randint(40, 140); # 온도
      steps = random.randint(2000, 6000); # 습도
      calories_burned = random.randint(1000, 4000); # 조도
      client.send(f"{heart_rate} {steps} {calories_burned}".encode('utf-8'));
    elif (recv_data == 'quit'):
      client.close();
      break;
  tcp_socket.close();
  break;