import socket;
import random;
import sys;

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
tcp_socket.bind(('', 5050));
tcp_socket.listen(5);

BUFF_SIZE = 1024;
print("측정 서버가 시작되었습니다.")

# 2바이트 송신자 ID(정수), 2바이트 수신자 ID(정수), 1바이트 조도값(정수), 1바이트 습도값(정수), 1바이트 온도값(정수), 1바이트 기압값(정수), 4바이트 순서번호(정수)

while (True):
  client, address = tcp_socket.accept();

  while (True):
    recv_data = client.recv(BUFF_SIZE).decode('utf-8');

    if (recv_data == 'Hello'):

      sender_id = random.randint(1, 50_000);
      receiver_id = random.randint(1, 50_000);
      lumi = random.randint(1, 100);
      humi = random.randint(1, 100);
      temp = random.randint(1, 100);
      air = random.randint(1, 100);
      seq = random.randint(1, 100_000);

      bytes_sender_id = sender_id.to_bytes(2, byteorder='big', signed=False);
      bytes_receiver_id = receiver_id.to_bytes(2, byteorder='big', signed=False);
      bytes_lumi = lumi.to_bytes(1, byteorder='big', signed=False);
      bytes_humi = humi.to_bytes(1, byteorder='big', signed=False);
      bytes_temp = temp.to_bytes(1, byteorder='big', signed=False);
      bytes_air = air.to_bytes(1, byteorder='big', signed=False);
      bytes_seq = seq.to_bytes(4, byteorder='big', signed=False);

      # 바이트 크기 확인
      # print(len(bytes_receiver_id));

      payload = bytes_sender_id + bytes_receiver_id + bytes_lumi + bytes_humi + bytes_temp + bytes_air + bytes_seq;

      client.send(payload);


