import socket
import os

BUF_SIZE = 1024
LENGTH = 4

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('', 7777))
tcp_socket.listen(10)
print('File server is running...')

while (True):
  client, address = tcp_socket.accept()

  msg = client.recv(BUF_SIZE) # 'Hello' 메세지 수신
  if (not msg):
    client.close()
    continue
  elif (msg != b'Hello'):
    print('client:', address, msg.decode())
    client.close()
    continue
  else:
    print('client:', address, msg.decode())
  
  # 'Filename' 메세지 전송
  client.send(b'Filename')
  # 파일 이름 수신
  msg = client.recv(BUF_SIZE)
  if (not msg):
    client.close()
    continue

  filename = msg.decode()
  print('client:', address, filename)

  try:
    filesize = os.path.getsize(filename)
    print(filesize)
  except:
    client.send(b'Nofile')
    client.close()
    continue
  
  else: # 파일 크기 전송
    fs_binary = filesize.to_bytes(LENGTH, 'big')
    client.send(fs_binary)

  f = open(filename, 'rb') # 파일 열기
  data = f.read() # 파일 읽기
  client.sendall(data) # 파일 전송

  msg = client.recv(BUF_SIZE)
  if (not msg):
    pass
  else:
    print('client:', address, msg.decode())

  f.close()
  client.close()