import selectors
import socket
import random

PORT = 9999
BUFSIZE = 1024

sel = selectors.DefaultSelector() # 이번트 처리기(셀렉터) 생성

def accept(sock, mask): # 새로운 클라이언트로부터 연결을 처리하는 함수
    client, address = sock.accept()
    print('connected from', address)
    sel.register(client, selectors.EVENT_READ, read) # 클라이언트 소켓을 이벤트 처리기에 등록

def read(client, mask):
    data = client.recv(BUFSIZE)
    if (not data):
        sel.unregister(client)
        client.close()
        return
    
    decoded_data = data.decode()
    if (decoded_data == '1'):
        temperature = random.randint(0, 40) # 온도
        client.send(f"Temp={temperature}".encode())
    elif (decoded_data == '2'):
        humidity = random.randint(0, 100) # 습도
        client.send(f"Humid={humidity}".encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', PORT))
sock.listen(5)

# 서버 소켓(신규 클라이언트 연결을 처리하는 소켓)을 이벤트 처리기에 등록
sel.register(sock, selectors.EVENT_READ, accept)
while (True):
    events = sel.select() # 등록된 객체에 대한 이벤트 감시 시작
    for key, mask in events: # 발생한 이벤트를 모두 검사
        callback = key.data # key.data: 이벤트 처리기에 등록한 callback 함수
        callback(key.fileobj, mask) # callback 함수 호출

