import MyTcpServer as my

port = 2500
BUFSIZE = 1024

sock = my.TcpServer(port)
connect, address = sock.accept()
print('connected by', address)

while True:
  data = connect.recv(BUFSIZE)
  if (not data):
    break;

  print("Received message: ", data.decode())
  connect.send(data)

connect.close();