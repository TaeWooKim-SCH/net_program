import socket
import selectors
import time

sel = selectors.DefaultSelector()

TARGET_PER_DEVICE = 5
counts = {}

f = open('data.txt', 'w', encoding='utf-8')

def make_reader(device_name, fields):
    def read(sock, mask):
        data = sock.recv(1024)
        if (not data):
            print(device_name, 'disconnected')
            sel.unregister(sock)
            sock.close()
            return
        
        values = data.decode().split()

        # 시간 + 디바이스명 + 필드=값 형식으로 한 줄 구성
        timestamp = time.asctime()         # 예: Fri Mar 18 22:55:13 2026
        pairs = ', '.join(
            f'{name}={value}' for name, value in zip(fields, values)
        )
        line = f'{timestamp}: {device_name}: {pairs}'

        print(line)
        f.write(line + '\n')
        f.flush()

        # 수집 개수 카운트
        counts[sock] = counts.get(sock, 0) + 1
        if counts[sock] >= TARGET_PER_DEVICE:
            print(f'{device_name}: {TARGET_PER_DEVICE}개 수집 완료, quit 전송')
            sock.send('quit'.encode())     # 디바이스에게 종료 알림
            sel.unregister(sock)
            sock.close()
    return read

def connect_device(port, device_name, fields):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))
    sock.send('Register'.encode())
    counts[sock] = 0
    sel.register(sock, selectors.EVENT_READ, make_reader(device_name, fields))
    print(f'{device_name} (port {port}) 연결 및 Register 전송')
    return sock

# 두 디바이스에 연결
connect_device(2501, 'Device1', ['Temp', 'Humid', 'Ilum'])
connect_device(2502, 'Device2', ['Heartbeat', 'Steps', 'Cal'])

# 수집 루프: 등록된 소켓이 모두 닫힐 때까지
while sel.get_map():                       # 감시 중인 소켓이 하나라도 있으면 계속
    events = sel.select(timeout=1)
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

f.close()
print('모든 데이터 수집 완료. data.txt 저장됨.')
