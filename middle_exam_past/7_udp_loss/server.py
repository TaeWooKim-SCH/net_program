import socket, random

HOST, PORT = 'localhost', 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print('Mbox server running on', PORT)
mailbox = {} # {'mboxID': [msg1, msg2, ...]}

while True:
  data, addr = sock.recvfrom(1024)

  # 25% 확률로 응답하지 않음 (고의 손실)
  if random.random() < 0.25:
    print('(Drop)', data.decode())
    continue

  msg = data.decode().strip()
  if msg == 'quit':
    sock.sendto(b'Bye', addr)
    break
  
  tokens = msg.split(' ', 2) # 최대 3개 (send, mboxID, message)
  if len(tokens) >= 3 and tokens[0] == 'send':
    mid = tokens[1]; text = tokens[2]
    mailbox.setdefault(mid, []).append(text)
    sock.sendto(b'OK', addr)
  elif len(tokens) >= 2 and tokens[0] == 'receive':
    mid = tokens[1]
    box = mailbox.get(mid, [])
    if not box:
      sock.sendto(b'No messages', addr)
    else:
      first = box.pop(0)
      sock.sendto(first.encode(), addr)
  else:
    sock.sendto(b'Unknown command', addr)