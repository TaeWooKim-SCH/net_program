import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

print(int(sock.recv(BUFSIZE).decode()))

sock.close()