import socket;

BUFF_SIZE = 1024;
port = 5555;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.connect(('localhost', port));

for i in range(10):
  time = 0.1;
  data = 'Hello, IoT';

  while True:
    sock.send(data.encode());
    print('Packet sent({}): Waiting up to {} secs for ack'.format(i, time));
    sock.settimeout(time); # 타임아웃 걺

    try:
      data = sock.recv(BUFF_SIZE);
    except socket.timeout:
      time *= 2; # 대기시간 2배 증가
      if (time > 2.0): # 최대 대기시간 초과
        break;

    else:
      print('Response', data.decode());
      break;