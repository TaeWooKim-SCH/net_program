import socket

tcp_socket = socket.create_connection(('localhost', 9999))

data_size = 20 # 수신할 데이터의 크기
rx_size = 0
total_data = []

while (rx_size < data_size):
  # 최대 4바이트 수신하도록 설정
  data = tcp_socket.recv(4)
  if (not data):
    break

  rx_size += len(data)
  total_data.append(data.decode())
  print(total_data)


message = ''.join(total_data)
print(message)

tcp_socket.close()