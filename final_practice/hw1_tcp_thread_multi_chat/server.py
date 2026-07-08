import socket
import threading
import time

port = 2500
BUFSIZE = 1024

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

def handleClient(conn: socket.socket, address):
    print('new client', address)
    clients.append(conn)

    while (True):
        data = conn.recv(BUFSIZE)

        if (not data or 'quit' in data.decode()):
            print(address, 'exited')
            if (conn in clients):
                clients.remove(conn)
            conn.close()
            break
    
        print(time.asctime() + str(address) + ':' + data.decode())

        for c in clients:
            if (c != conn):
                c.send(data)

while (True):
    conn, address = sock.accept()
    th = threading.Thread(target=handleClient, args=(conn, address))
    th.start()