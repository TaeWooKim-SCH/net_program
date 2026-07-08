import selectors
import socket
import random
import time

sel = selectors.DefaultSelector()

senders = {}
INTERVAL = 5

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
sock.bind(('', 2502))
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
            heart_rate = random.randint(40, 140) # 심박수
            steps = random.randint(2000, 6000) # 걸음수
            calories_burned = random.randint(1000, 4000) # 소모칼로리

            try:
                client.send(f"{heart_rate} {steps} {calories_burned}".encode('utf-8'))
            except OSError:
                senders.pop(client, None)
                continue
            senders[client] = now + INTERVAL