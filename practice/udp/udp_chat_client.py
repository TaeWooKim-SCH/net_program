import socket;

port = 3333;
BUFSIZE = 1024;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

while True:
  msg = input('-> ');
  sock.sendto(msg.encode(), ('localhost', port));
  if (msg == 'q'):
    break;

  data, addr = sock.recvfrom(BUFSIZE);
  print('<- ', data.decode());
  if (data.decode() == 'q'):
    break;

sock.close();