import asyncio
import time
import random

PORT = 9000
INTERVAL = 2

device_name = input('디바이스 이름을 입력해주세요')
next_send = time.time()

port = 2500
BUFSIZE = 1024

async def main():
    reader, writer = await asyncio.open_connection('localhost', port)
    next_send = time.time()
    
    while True:
        data = input('Enter the message to send: ')
        writer.write(data.encode())
        await writer.drain()

        temperature = random.randint(0, 40)
        battery = random.randint(0, 100)
        
        next_send = time.time() + INTERVAL
        
        
        data = await reader.read(BUFSIZE)
        print('Received:', data.decode())

asyncio.run(main())