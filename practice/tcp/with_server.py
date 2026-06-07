import socket;

addr = ('localhost', 9000);

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('', 9000));
  s.listen(2);

  while True:
    client, addr = s.accept();
    with client:
      print(('Connection from', addr));
      client.send(b'Hello ' + addr[0].encode());