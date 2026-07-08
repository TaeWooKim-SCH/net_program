import socket

PORT = 9999
BUFSIZE = 1024
addr = ('localhost', PORT)          # 보낼 대상 주소

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
print('메시지를 입력하세요.')

while True:
    message = input('Message to send: ')
    if message == '':
        continue

    sock.sendto(message.encode(), addr)     # 주소 명시해서 전송
    data, _ = sock.recvfrom(BUFSIZE)        # 응답 수신 (보낸 주소는 안 쓰므로 _)
    print(data.decode())