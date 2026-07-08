import socket
import threading

port = 2500
BUFSIZE = 1024

def recvTask(sock: socket.socket):
    while (True):
        data = sock.recv(BUFSIZE)
        print(data.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

my_id = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

th = threading.Thread(target=recvTask, args=(sock,))
th.daemon = True
th.start()

while (True):
    text = input()
    message = '[' + my_id + '] ' + text
    sock.send(message.encode())
    if (text == 'quit'):
        break
sock.close()