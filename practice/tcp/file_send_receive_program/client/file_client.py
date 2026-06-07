import socket
import sys

BUF_SIZE = 1024
LENGTH = 4 # 파일 크기: 4바이트

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 7777))

tcp_socket.send(b'Hello') # 'Hello' 메세지 전송

msg = tcp_socket.recv(BUF_SIZE) # 'Filename' 메세지 수신
if (not msg):
  tcp_socket.close()
  sys.exit()
elif (msg != b'Filename'):
  print('server:', msg.decode())
  tcp_socket.close()
  sys.exit()
else:
  print('server:', msg.decode())

filename = input('Enter a filename: ')
tcp_socket.send(filename.encode()) # 파일 이름 전송

msg = tcp_socket.recv(BUF_SIZE)
if (not msg):
  tcp_socket.close()
  sys.exit()
elif (msg == b'Nofile'):
  print('server:', msg.decode())
  tcp_socket.close()
  sys.exit()
else:
  received_size = len(msg)
  data = msg
  while (received_size < LENGTH):
    msg = tcp_socket(BUF_SIZE)
    if (not msg):
      tcp_socket.close()
      sys.exit()
    
    data += msg
    received_size += len(msg)
  if (received_size < LENGTH):
    tcp_socket.close()
    sys.exit()
  
  filesize = int.from_bytes(data, 'big')
  print('server:', filesize) # 4바이트

received_size = 0
f = open(filename, 'wb') # 파일 오픈
while (received_size < filesize): # 실제 파일 수신
  data = tcp_socket.recv(BUF_SIZE)
  if (not data):
    break

  f.write(data)
  received_size += len(data)

if (received_size < filesize):
  tcp_socket.close()
  sys.exit()

print('Download complete')
tcp_socket.send(b'Bye') # Bye 메세지 전송
f.close()
tcp_socket.close()
