import socket;

BUFF_SIZE = 1024;
port = 5555;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.connect(('localhost', port));

while True:
  send_msg = input('명령을 입력해주세요: ');
  split_send_msg = send_msg.split(' ');
  req_method = split_send_msg[0];

  sock.send(send_msg.encode());
  if (req_method == 'quit'):
    break;
  
  recv_msg = sock.recv(BUFF_SIZE);
  print(recv_msg.decode());