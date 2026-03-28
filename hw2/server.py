import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.bind(('', 9000));
s.listen(2);

while True:
  client, addr = s.accept();
  print('Connection from ', addr);

  # 연결 직후 메세지 송신
  client.send(b'Hello ' + addr[0].encode());

  # 이름 메세지 수신
  msg = client.recv(1024);
  decoded_msg = msg.decode();
  print(decoded_msg);

  # 학번 메세지 송신
  student_id = (20211483).to_bytes(4, 'big');
  client.send(student_id);

  # 클라이언트 소켓 종료
  client.close();