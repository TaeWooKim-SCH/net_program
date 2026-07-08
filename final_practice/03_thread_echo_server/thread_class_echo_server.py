import socket
import threading

port = 2500
BUFSIZE = 1024

class ClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    
    def run (self):
        while (True):
            data = self.sock.recv(BUFSIZE)
            if (not data):
                break
            print('Received message:', data.decode())
            self.sock.send(data)
        self.sock.close()
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while (True):
    connection, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = ClientThread(connection)
    th.start()


            