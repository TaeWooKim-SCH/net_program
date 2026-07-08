import selectors
import socket
import random
import time

sel = selectors.DefaultSelector()

senders = {}
INTERVAL = 3

def read(client, mask):
    data = client.recv(1024)
    if (not data or data.decode() == 'quit'):
        print('client exited')
        senders.pop(client, None)
        sel.unregister(client)
        client.close()
        return
    
    print('received data:', data.decode())

    if (data.decode() == 'Register'):
        senders[client] = time.time()

def accept(sock, mask):
    client, address = sock.accept()
    print('connected from', address)
    sel.register(client, selectors.EVENT_READ, read)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 2501))
sock.listen(5)

sel.register(sock, selectors.EVENT_READ, accept)
while (True):
    events = sel.select(timeout=0.2)
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
    
    now = time.time()
    for client in list(senders.keys()):
        if (now >= senders[client]):
            temperature = random.randint(0, 40) # 온도
            humidity = random.randint(0, 100) # 습도
            illuminance = random.randint(70, 150) # 조도

            try:
                client.send(f"{temperature} {humidity} {illuminance}".encode('utf-8'))
            except OSError:
                senders.pop(client, None)
                continue
            senders[client] = now + INTERVAL


######### 일반 tcp 멀티 스레딩 구현 ##########

# import socket
# import threading
# import random
# import time

# INTERVAL = 3

# def processClient(client: socket.socket, address):
#     print('connected from', address)
#     registered = False
#     next_send = 0

#     client.settimeout(0.2)   # recv를 0.2초만 대기 (selectors의 timeout=0.2 역할)

#     while True:
#         # 1) 데이터 수신 시도 (0.2초 안에 안 오면 timeout 예외)
#         try:
#             data = client.recv(1024)
#             if not data or data.decode() == 'quit':
#                 print('client exited')
#                 break

#             text = data.decode()
#             print('received data:', text)
#             if text == 'Register':
#                 registered = True
#                 next_send = time.time()   # 바로 전송 시작
#         except socket.timeout:
#             pass   # 수신 데이터가 없었을 뿐, 정상. 아래 전송 로직으로 진행
#         except OSError:
#             break

#         # 2) 등록된 클라이언트면 3초마다 센서값 전송
#         if registered and time.time() >= next_send:
#             temperature = random.randint(0, 40)
#             humidity = random.randint(0, 100)
#             illuminance = random.randint(70, 150)
#             try:
#                 client.send(f"{temperature} {humidity} {illuminance}".encode('utf-8'))
#             except OSError:
#                 break
#             next_send = time.time() + INTERVAL

#     client.close()


# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.bind(('', 2501))
# sock.listen(5)
# print('서버 시작')

# while True:
#     client, address = sock.accept()
#     th = threading.Thread(target=processClient, args=(client, address))
#     th.start()