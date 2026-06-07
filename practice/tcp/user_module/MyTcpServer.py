class TcpServer:
  def __init__(self, port):
    import socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind(('', port))
    self.sock.listen(5)
  
  def accept(self):
    self.c_sock, self.c_addr = self.sock.accept()
    return self.c_sock, self.c_addr


if (__name__ == '__main__'):
  sock = TcpServer(8888);

  client, addr = sock.accept();
  print('connected by ', addr);

  client.send(b'Hello Client');
  client.close();
