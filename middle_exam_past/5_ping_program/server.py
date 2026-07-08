import socket;
import time;

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp_socket.bind(('', 7000));
tcp_socket.listen(5);

BUFF_SIZE = 1024;
print("Ping 서버가 시작되었습니다.")

while (True):
  client, address = tcp_socket.accept();

  while (True):
    recv_data = client.recv(BUFF_SIZE);

    # 클라이언트가 연결을 끊고 나갔을 때의 방어 코드
    if not recv_data:
        print("클라이언트 연결 종료");
        break;
    
    decoded_data = recv_data.decode('utf-8');
    if (decoded_data == 'ping'):
      # 0.02초 ~ 0.03초 정도의 인위적인 네트워크 지연 발생 (테스트용)
      time.sleep(0.02)
      client.send('pong'.encode('utf-8'));
    else:
      print("ping 메세지가 아닙니다.");

