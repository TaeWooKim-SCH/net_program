import socket
import threading

port = 3333
BUFSIZE = 1024

def recvTask(sock: socket.socket):
    while (True):
        data = sock.recv(BUFSIZE)
        print('<-', data.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

th = threading.Thread(target=recvTask, args=(sock,))
th.start()

while (True):
    msg = input()
    print('->', msg)
    sock.send(msg.encode())