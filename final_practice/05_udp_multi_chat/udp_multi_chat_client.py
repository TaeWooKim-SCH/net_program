import socket
import threading

def handler(sock):
    while (True):
        message, address = sock.recvfrom(1024)
        print(message.decode())

server_address = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_id = input('ID를 입력하세요: ')
sock.sendto(('[' + my_id + ']').encode(), server_address)

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while (True):
    message = '[' + my_id + '] ' + input()
    sock.sendto(message.encode(), server_address)
