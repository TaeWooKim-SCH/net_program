import selectors
import socket
import time

sel = selectors.DefaultSelector() # 이번트 처리기(셀렉터) 생성
clients: list[socket.socket] = []

def accept(sock, mask): # 새로운 클라이언트로부터 연결을 처리하는 함수
    client, address = sock.accept()
    print('connected from', address)
    sel.register(client, selectors.EVENT_READ, read) # 클라이언트 소켓을 이벤트 처리기에 등록
    
    if (client not in clients):
        clients.append(client)

def read(client: socket.socket, mask):
    data = client.recv(1024)
    if (not data):
        sel.unregister(client)
        client.close()
        return
    print('received data:', data.decode())

    decoded_data = data.decode()
    if (decoded_data == "quit"):
        clients.remove(client)
        sel.unregister(client)
        client.close()
        return
        
    # 모든 클라이언트에게 전송
    for c in clients:
        if (c != client):
            c.send(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 6000))
sock.listen(5)

# 서버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
sel.register(sock, selectors.EVENT_READ, accept)
while (True):
    events = sel.select() # 등록된 객체에 대한 이벤트 감시 시작
    for key, mask in events: # 발생한 이벤트를 모두 검사
        callback = key.data # key.data: 이벤트 처리기에 등록한 callback 함수
        callback(key.fileobj, mask) # callback 함수 호출