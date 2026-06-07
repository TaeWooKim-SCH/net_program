import socket

port = 2500
BUFSIZE = 1024

sock = socket.create_server(('', port), family=socket.AF_INET, backlog=1)
connection, address = sock.accept()
print('connected by', address[0], address[1])

while True:
  data = connection.recv(BUFSIZE)
  if (not data):
    break;

  print("Received message: ", data.decode())
  connection.send(data)

connection.close();