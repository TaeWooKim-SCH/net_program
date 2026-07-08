import asyncio
import random

PORT = 9999

class IoTProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport          # 응답 보낼 때 사용

    def datagram_received(self, data, addr):  # 데이터그램 수신 시 자동 호출
        text = data.decode().strip()
        if text == '1':
            msg = f"Temp={random.randint(0, 40)}"
            self.transport.sendto(msg.encode(), addr)   # 보낸 주소로 응답
        elif text == '2':
            msg = f"Humid={random.randint(0, 100)}"
            self.transport.sendto(msg.encode(), addr)

async def main():
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: IoTProtocol(),
        local_addr=('localhost', PORT)
    )
    print('server started')
    try:
        await asyncio.sleep(float('inf'))   # 서버 계속 유지
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())