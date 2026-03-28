import socket;

addr = ('localhost', 9000);

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.connect(addr);
  msg = sock.recv(1024);
  print(msg.decode());