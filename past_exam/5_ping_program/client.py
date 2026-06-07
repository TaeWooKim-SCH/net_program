import socket;
import time;

PORT = 7000;
BUFF_SIZE = 1024;

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp_socket.connect(('localhost', PORT));

for _ in range(3):
  tcp_socket.send('ping'.encode('utf-8'));

  # 문제 요구사항: ping 메시지 보낸 후 시간 기록
  start_time = time.time();

  tcp_socket.recv(BUFF_SIZE);

  # 문제 요구사항: pong 메시지 받은 후 시간 기록
  end_time = time.time();
  print(f"Success (RTT: {end_time - start_time:.5f})");