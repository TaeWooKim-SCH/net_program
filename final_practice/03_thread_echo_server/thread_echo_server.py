import socket
import threading

port = 2500
BUFSIZE = 1024

def echoTask(sock: socket.socket):
    while True:
        data = sock.recv(BUFSIZE)
        if (not data):
            break
        print('Received message:', data.decode())
        sock.send(data)
    
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    connection, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = threading.Tread(target=echoTask, args=(connection,))
    th.start()