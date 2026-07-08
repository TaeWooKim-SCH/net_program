import socket

SERVER = ('localhost', 5555)
BUFF_SIZE = 1024
MAX_RETRY = 2 # 최초 포함 3번

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  msg = input('> ').strip()
  if msg == '':
    continue

  retry = 0
  data = None
  while retry <= MAX_RETRY:
    sock.sendto(msg.encode(), SERVER)
    sock.settimeout(1.0) # 1초 대기

    try:
      data, _ = sock.recvfrom(BUFF_SIZE)
    except socket.timeout:
      retry += 1
      print(f'Timeout, retransmit ({retry}/{MAX_RETRY})')
      continue
    else:
      break
  if data is None:
    print('Failed: No response after 3 attempts')
  else:
    print('Server:', data.decode())

  if msg == 'quit':
    break
sock.close()
