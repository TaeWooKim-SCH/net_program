import socket, select
import random

PORT = 9999
BUFSIZE = 1024

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
s_sock.bind(('', PORT))

socks = [s_sock]   # 감시할 소켓 (UDP는 서버 소켓 하나뿐)
print(str(PORT) + '에서 대기 중')

while True:
    r_sock, _, _ = select.select(socks, [], [])

    for s in r_sock:
        data, addr = s.recvfrom(BUFSIZE)      # 누가 보냈는지(addr)도 함께 수신
        text = data.decode().strip()

        if text == '1':
            temperature = random.randint(0, 40)
            s.sendto(f"Temp={temperature}".encode(), addr)    # 보낸 주소로 응답
        elif text == '2':
            humidity = random.randint(0, 100)
            s.sendto(f"Humid={humidity}".encode(), addr)