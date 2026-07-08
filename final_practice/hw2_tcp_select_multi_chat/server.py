import socket, select

BUFSIZE = 1024
PORT = 2500

socks = []
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(str(PORT) + '에서 접속 대기 중')

while (True):
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock: # 읽기 가능한 소켓 리스트 검사
        if (s == s_sock): # 새 클라이언트
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('new client', addr)
        else: # 기존 클라이언트
            data = s.recv(BUFSIZE)
            if (not data or 'quit' in data.decode()):
                print(addr, 'exited')
                s.close()
                socks.remove(s)
                continue
            print('Received:', data.decode())
        
            for c in socks:
                if (c != s and c != s_sock):
                    c.send(data)