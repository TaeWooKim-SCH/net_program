import socket;

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
addr = ('localhost', 9000);
sock.connect(addr);

# 연결 직후 메세지 수신
msg = sock.recv(1024);
print(msg.decode());

# 이름 메세지 송신
encoded_name = 'Taewoo Kim'.encode();
sock.send(encoded_name);

# 학번 메세지 수신
msg = sock.recv(1024);
decoded_msg = int.from_bytes(msg, 'big');
print(decoded_msg);

sock.close();
