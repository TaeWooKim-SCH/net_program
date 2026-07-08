# 사용자
# - 2개의 IoT 디바이스와 TCP 연결
# - 수집한 데이터는 시간정보를 추가해 파일에 저장 (data.txt)


import socket;
import datetime;

socket_device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
socket_device1.connect(('localhost', 8001));
print('connected to device1');

socket_device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
socket_device2.connect(('localhost', 8002));
print('connected to device2');

BUFF_SIZE = 1024;


while (True):
  command = input('명령어 입력 > ');

  if (command == '1'):
    socket_device1.send('Request'.encode('utf-8'));
    recv_data = socket_device1.recv(BUFF_SIZE).decode('utf-8').split(' ');

    date_now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y');
    data_file = open('data.txt', 'a');
    data_file.write(f"{date_now}: Device1: Temp={recv_data[0]}, Humid={recv_data[1]}, Iilum={recv_data[2]}\n");
    data_file.close();

  elif (command == '2'):
    socket_device2.send('Request'.encode('utf-8'));
    recv_data = socket_device2.recv(BUFF_SIZE).decode('utf-8').split(' ');

    date_now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y');
    data_file = open('data.txt', 'a');
    data_file.write(f"{date_now}: Device2: Heartbeat={recv_data[0]}, Steps={recv_data[1]}, Cal={recv_data[2]}\n");
    data_file.close();

  elif (command == 'quit'):
    socket_device1.send('quit'.encode('utf-8'));
    socket_device2.send('quit'.encode('utf-8'));
    break;