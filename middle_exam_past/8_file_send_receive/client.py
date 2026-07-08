import socket, sys

SERVER = ('localhost', 6789)
BUF = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 1. Hello
sock.sendto(b'Hello', SERVER)

# 2. 'Filename' 수신
data, _ = sock.recvfrom(BUF)
if data != b'Filename':
  print('Unexpected:', data); sock.close(); sys.exit()

# 3. 파일 이름 입력 후 전송
filename = input('Enter filename: ').strip()
sock.sendto(filename.encode(), SERVER)

# 4. 파일 또는 'No File' 수신
data, _ = sock.recvfrom(BUF)
if data == b'No File':
  print('Server: No File')

else:
  with open('recv_' + filename, 'wb') as f:
    f.write(data)
  print('File received:', len(data), 'bytes')

# 5. 종료 통보
sock.sendto(b'Bye', SERVER)
sock.close()
