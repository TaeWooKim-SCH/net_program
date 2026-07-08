import socket;

BUF_SIZE = 1024
LENGTH = 4 # 파일 크기: 4바이트

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 5050))

tcp_socket.send('Hello'.encode('utf-8'));

recv_data = tcp_socket.recv(BUF_SIZE);

sender_id = int.from_bytes(recv_data[0:2], byteorder='big', signed=False);
receiver_id = int.from_bytes(recv_data[2:4], byteorder='big', signed=False);
lumi = int.from_bytes(recv_data[4:5], byteorder='big', signed=False);
humi = int.from_bytes(recv_data[5:6], byteorder='big', signed=False);
temp = int.from_bytes(recv_data[6:7], byteorder='big', signed=False);
air = int.from_bytes(recv_data[7:8], byteorder='big', signed=False);
seq = int.from_bytes(recv_data[8:12], byteorder='big', signed=False);

print(f"Sender:{sender_id}, Receiver:{receiver_id}, Lumi:{lumi}, Humi:{humi}, Temp:{temp}, Air: {air}, Seq: {seq}");
