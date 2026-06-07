import socket;


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 5050))

tcp_socket.send('Hello'.encode('utf-8'));

data_size = int.from_bytes(tcp_socket.recv(2), byteorder='big', signed=False);
total_data = [];
size_seq = [2, 2, 1, 1, 4, 1024];

for size in size_seq:
  data = tcp_socket.recv(size); # 4바이트씩 읽기
  if (not data):
    break;
  
  if (size == 4):
    total_data.append(socket.inet_ntoa(data));
  else:
    total_data.append(int.from_bytes(data, byteorder='big', signed=False));



print(f"Length={data_size} Lumi:{total_data[0]}, Humi:{total_data[1]}, Temp:{total_data[2]}, Air: {total_data[3]}, IP={total_data[4]}, Variable Data:{'x' * total_data[5]}");
