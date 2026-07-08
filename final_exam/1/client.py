from socket import *
import time
import random

PORT = 5000
INTERVAL = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', PORT))

device_name = input('디바이스 이름을 입력해주세요')
sock.send(device_name.encode())
next_send = time.time()

while (True):
    if (time.time() >= next_send):
        temperature = random.randint(0, 100)
        humidity = random.randint(0, 100)
        print(device_name)
        print(temperature)
        print(humidity)
        sock.send((device_name + ' ' + str(temperature) + ' ' + str(humidity)).encode())
        next_send = time.time() + INTERVAL
