import socket
import time

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 2500))

print('Server Started')

while (True):
    data, address = sock.recvfrom(1024)

    # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
    if ('quit' in data.decode()):
        if (address in clients):
            print(address, 'exited')
            clients.remove(address)
            continue;

    # 새로운 클라이언트이면 목록에 추가
    if (address not in clients):
        print('new client', address)
        clients.append(address)
    
    print(time.asctime() + str(address) + ':' + data.decode())

    # 모든 클라이언트에게 전송
    for client in clients:
        if (client != address):
            sock.sendto(data, client)