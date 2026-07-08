import socket

PORT = 9999
BUFSIZE = 1024

# 서버에 연결
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', PORT))
print('서버에 연결되었습니다. 메시지를 입력하세요. (종료: quit)')

while True:
    message = input('Message to send: ')

    # 빈 입력은 건너뜀 (서버가 빈 데이터를 연결 종료로 인식하므로)
    if (message == ''):
        continue
    
    # 메시지 전송
    sock.send(message.encode())
    
    # 서버가 되돌려준 에코 수신
    data = sock.recv(BUFSIZE)
    if not data:                       # 서버가 연결을 닫은 경우
        print('서버와의 연결이 끊겼습니다.')
        break
    print(data.decode())

sock.close()
print('연결을 종료했습니다.')
