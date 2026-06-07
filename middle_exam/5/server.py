import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5555))
sock.listen(5);

BUFF_SIZE = 1024;

print('Mbox server running on', 5555)
mailbox = {} # {'mboxID': [msg1, msg2, ...]}

while True:
  client, address = sock.accept();

  while (True):
    data = client.recv(BUFF_SIZE)

    msg = data.decode().strip()
    if msg == 'quit':
      client.send(b'Bye')
      break
    
    tokens = msg.split(' ', 2) # 최대 3개 (send, mboxID, message)
    if len(tokens) >= 3 and tokens[0] == 'send':
      mid = tokens[1]; text = tokens[2]
      mailbox.setdefault(mid, []).append(text)
      client.send(b'OK')
    elif len(tokens) >= 2 and tokens[0] == 'receive':
      mid = tokens[1]
      box = mailbox.get(mid, [])
      if not box:
        client.send(b'No messages')
      else:
        first = box.pop(0)
        client.send(first.encode())
    else:
      client.send(b'Unknown command')