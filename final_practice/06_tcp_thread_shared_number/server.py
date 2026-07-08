import socket
import threading

port = 2500
BUFSIZE = 1024

sharedData = 0

def thread_handler(sock):
    global sharedData
    for _ in range(100_000_000):
        sharedData += 1
    print(sharedData)
    sock.send(str(sharedData).encode())
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while (True):
    client, address = sock.accept()
    print('connected by', address)
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()

s.close()