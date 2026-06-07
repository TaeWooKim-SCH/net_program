############## TCP 서버 기본 골격 ##############
# import socket;

# PORT = 8000;

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # 1. TCP 소켓 생성
# s.bind(('', PORT)); # 2. 주소 바인딩 (모든 인터페이스)
# s.listen(5); # 3. 연결 대기

# while True:
#   client, addr = s.accept(); # 4. 연결 수락 → (소켓, 주소)
#   data = client.recv(1024); # 5. 데이터 수신 (bytes)
#   client.send(b'response'); # 6. 데이터 송신 (bytes)
#   client.close(); # 7. 클라이언트 소켓 종료

############## TCP 클라이언트 기본 골격 ##############
# import socket;

# PORT = 8000;

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# s.connect(('localhost', PORT)); # 서버 접속

# s.send(b'request');

# data = s.recv(1024);

# print(data.decode());

# s.close();


############## UDP 서버 기본 골격 ##############
# import socket;

# PORT = 8000;

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); # UDP 소켓
# s.bind(('', PORT));

# while True:
#   data, addr = s.recvfrom(1024); # (데이터, 보낸이 주소)
#   s.sendto(b'reply', addr); # 보낸이에게 응답


############## UDP 클라이언트 기본 골격 ##############
# import socket;

# PORT = 8000;
# SERVER = ('localhost', PORT);

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

# s.sendto(b'hello', SERVER);

# data, addr = s.recvfrom(1024);

# s.close();


############## 정수를 네트워크 바이트 순서(빅엔디언)로 변환 ##############
# 정수 → 2바이트 bytes (빅엔디언, 네트워크 바이트 순서)
n = 1234;
b = n.to_bytes(2, 'big'); # b'\x04\xd2'

# bytes → 정수 (빅엔디언)
n2 = int.from_bytes(b, 'big'); # 1234

# 또는 struct 모듈 사용
import struct;
b = struct.pack('!H', 1234); # H = unsigned short(2바이트), ! = 네트워크
n2, = struct.unpack('!H', b);