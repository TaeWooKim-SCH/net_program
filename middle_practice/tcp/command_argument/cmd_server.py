import socket
import sys

port = 2500
BUFSIZE = 1024

if (len(sys.argv) > 1):
  port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

connection, address = sock.accept()
print('connected by', address)

while True:
  data = connection.recv(BUFSIZE)
  if (not data):
    break

  print("received message: ", data.decode())
  connection.send(data)

connection.close()