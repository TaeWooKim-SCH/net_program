import selectors, socket, random

sel = selectors.DefaultSelector()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9999))
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ)   # 소켓 하나만 등록 (콜백 없이도 가능)

while True:
    events = sel.select()
    for key, mask in events:
        data, addr = sock.recvfrom(1024)    # accept 없음! 바로 recvfrom
        text = data.decode().strip()
        if text == '1':
            sock.sendto(f"Temp={random.randint(0,40)}".encode(), addr)
        elif text == '2':
            sock.sendto(f"Humid={random.randint(0,100)}".encode(), addr)