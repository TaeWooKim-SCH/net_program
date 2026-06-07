import socket;

BUFF_SIZE = 1024;
port = 5555;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind(('', port));

data = dict();

while True:
  recv_msg, addr = sock.recvfrom(BUFF_SIZE);
  split_recv_msg = recv_msg.decode().split(' ');
  req_method = split_recv_msg[0];

  if (req_method == 'send'):
    message = ' '.join(split_recv_msg[2:]);

    mboxID = str(split_recv_msg[1]);
    data[mboxID] = message;

    sock.sendto('OK'.encode(), addr);
  
  elif (req_method == 'receive'):
    mboxID = str(split_recv_msg[1]);
    if (mboxID in data):
      sock.sendto(str(data[mboxID]).encode(), addr);
      del data[mboxID];
    else:
      sock.sendto('No messages'.encode(), addr);
  
  elif (req_method == 'quit'):
    print('서버를 종료합니다.');
    break;
  else:
    sock.sendto('알 수 없는 명령입니다.'.encode(), addr);


