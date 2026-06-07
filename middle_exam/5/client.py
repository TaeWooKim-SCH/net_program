import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5555))

BUFF_SIZE = 1024
while True:
  msg = input('> ').strip()
  if msg == '':
    continue

  sock.send(msg.encode())
  sock.settimeout(1);

  data = sock.recv(BUFF_SIZE)

  print('Server:', data.decode())

  if msg == 'quit':
    break
sock.close()
