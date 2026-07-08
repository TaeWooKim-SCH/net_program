import socket
import threading

port = 3333
BUFSIZE = 1024

def sendTask(sock: socket.socket):
    while (True):
        resp = input()
        print('->', resp)
        sock.send(resp.encode())
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

connection, address = sock.accept()

th = threading.Thread(target=sendTask, args=(connection,))
th.start()

while (True):
    data = connection.recv(BUFSIZE)
    print('<-', data.decode())

