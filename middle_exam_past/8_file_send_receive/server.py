import socket, os

HOST, PORT = 'localhost', 6789
BUF = 65535

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print('UDP file server running on', PORT)

while True:
  data, addr = sock.recvfrom(BUF)
  if data != b'Hello':
    continue
  print('Hello from', addr)

  # 'Filename' 전송
  sock.sendto(b'Filename', addr)

  # 파일 이름 수신
  data, _ = sock.recvfrom(BUF)
  filename = data.decode().strip()
  print('Requested:', filename)

  if not os.path.exists(filename):
    sock.sendto(b'No File', addr)
  else:
    with open(filename, 'rb') as f:
      content = f.read()
    # 2초 간격으로 최대 3회 재전송
    for attempt in range(3):
      sock.sendto(content, addr)
      print(f'File sent ({attempt+1}/3)')
      sock.settimeout(2.0)

      try:
        ack, _ = sock.recvfrom(BUF)
        if ack == b'Bye':
          print('Got Bye. Done.')
          break
      except socket.timeout:
        print('Bye not received, retransmit...')
    sock.settimeout(None)

  # 'No File'을 받은 클라이언트도 Bye를 보냄
  try:
    sock.settimeout(2.0)
    ack, _ = sock.recvfrom(BUF)
    print('Got:', ack.decode())
  except socket.timeout:
    pass
  sock.settimeout(None)